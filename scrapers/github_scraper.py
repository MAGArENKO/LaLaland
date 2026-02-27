import asyncio
import base64
from typing import AsyncIterator, Dict, Any, Optional
import logging

from .base import BaseScraper, ScrapedItem, SourceType

logger = logging.getLogger(__name__)


class GitHubScraper(BaseScraper):
    """Scraper for GitHub repositories, gists, and search results."""

    def __init__(self, config: Dict[str, Any], token: Optional[str] = None):
        super().__init__(config)
        self.token = token
        self._github = None
        self.rate_limit_delay = 1.0

    @property
    def github(self):
        if self._github is None:
            try:
                from github import Github

                self._github = Github(self.token) if self.token else Github()
            except ImportError:
                logger.warning("PyGithub not installed, GitHub scraper disabled")
                return None
        return self._github

    @property
    def source_type(self) -> SourceType:
        return SourceType.GITHUB

    async def validate_connection(self) -> bool:
        if not self.github:
            return False
        try:
            from github import GithubException

            rate_limit = self.github.get_rate_limit()
            return rate_limit.core.remaining > 0
        except (GithubException, Exception):
            return False

    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape all configured GitHub sources."""
        if not self.github:
            return

        github_config = self.config.get("sources", {}).get("github", {})

        if not github_config.get("enabled", False):
            return

        from github import GithubException

        for repo_config in github_config.get("repositories", []):
            try:
                async for item in self._scrape_repository(repo_config["owner"], repo_config["repo"]):
                    yield item
            except GithubException as e:
                logger.error(f"GitHub error for {repo_config}: {e}")

        for query in github_config.get("search_queries", []):
            try:
                async for item in self._search_code(query):
                    yield item
            except GithubException as e:
                logger.error(f"GitHub search error: {e}")

        if github_config.get("include_gists", False):
            try:
                async for item in self._scrape_gists():
                    yield item
            except GithubException as e:
                logger.error(f"Error scraping gists: {e}")

    async def _scrape_repository(
        self, owner: str, repo_name: str, branch: str = None
    ) -> AsyncIterator[ScrapedItem]:
        """Scrape all files from a repository."""
        from github import GithubException

        try:
            repo = self.github.get_repo(f"{owner}/{repo_name}")
            default_branch = branch or repo.default_branch
            contents = repo.get_contents("", ref=default_branch)

            while contents:
                file_content = contents.pop(0)

                if file_content.type == "dir":
                    contents.extend(repo.get_contents(file_content.path, ref=default_branch))
                else:
                    try:
                        if file_content.encoding == "base64":
                            content = base64.b64decode(file_content.content).decode("utf-8", errors="ignore")
                        else:
                            content = file_content.content or ""

                        is_relevant, confidence = self.is_relevant(content, file_content.name)

                        if is_relevant or confidence > 0.3:
                            yield ScrapedItem(
                                id=f"github:{owner}/{repo_name}:{file_content.sha[:8]}",
                                source_type=self.source_type,
                                source_path=f"github.com/{owner}/{repo_name}/{file_content.path}",
                                content=content,
                                content_type=self.detect_content_type(content, file_content.name),
                                file_extension=file_content.name.split(".")[-1] if "." in file_content.name else None,
                                filename=file_content.name,
                                metadata={
                                    "repo": f"{owner}/{repo_name}",
                                    "branch": default_branch,
                                    "sha": file_content.sha,
                                    "url": file_content.html_url,
                                    "size": file_content.size,
                                },
                                language=self.detect_language(content, file_content.name),
                                confidence_score=confidence,
                            )
                    except Exception as e:
                        logger.error(f"Error processing {file_content.path}: {e}")

                await asyncio.sleep(self.rate_limit_delay)

        except GithubException as e:
            logger.error(f"GitHub error for {owner}/{repo_name}: {e}")

    async def _search_code(self, query: str) -> AsyncIterator[ScrapedItem]:
        """Search GitHub for code matching query."""
        from github import GithubException

        try:
            username = self.config.get("github_username")
            if username:
                query = f"{query} user:{username}"

            results = self.github.search_code(query)

            for result in results:
                try:
                    content = base64.b64decode(result.content).decode("utf-8", errors="ignore")

                    yield ScrapedItem(
                        id=f"github:search:{result.sha[:8]}",
                        source_type=self.source_type,
                        source_path=result.html_url,
                        content=content,
                        content_type=self.detect_content_type(content, result.name),
                        filename=result.name,
                        metadata={
                            "repo": result.repository.full_name,
                            "search_query": query,
                            "sha": result.sha,
                        },
                        language=self.detect_language(content, result.name),
                        confidence_score=1.0,
                    )

                    await asyncio.sleep(self.rate_limit_delay * 2)

                except Exception as e:
                    logger.error(f"Error processing search result: {e}")

        except GithubException as e:
            logger.error(f"GitHub search error: {e}")

    async def _scrape_gists(self) -> AsyncIterator[ScrapedItem]:
        """Scrape user's gists."""
        from github import GithubException

        try:
            user = self.github.get_user()

            for gist in user.get_gists():
                for filename, file_info in gist.files.items():
                    content = file_info.content or ""

                    is_relevant, confidence = self.is_relevant(content, filename)

                    if is_relevant or confidence > 0.2:
                        yield ScrapedItem(
                            id=f"github:gist:{gist.id}:{filename}",
                            source_type=self.source_type,
                            source_path=gist.html_url,
                            content=content,
                            content_type=self.detect_content_type(content, filename),
                            filename=filename,
                            metadata={
                                "gist_id": gist.id,
                                "description": gist.description,
                                "public": gist.public,
                                "created_at": gist.created_at.isoformat() if gist.created_at else None,
                            },
                            created_at=gist.created_at,
                            modified_at=gist.updated_at,
                            language=file_info.language,
                            confidence_score=confidence,
                        )

                await asyncio.sleep(self.rate_limit_delay)

        except GithubException as e:
            logger.error(f"Error scraping gists: {e}")
