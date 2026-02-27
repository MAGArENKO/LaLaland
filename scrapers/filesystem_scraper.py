import asyncio
import aiofiles
import os
from pathlib import Path
from datetime import datetime
from typing import AsyncIterator, Dict, Any, Set, Optional
import fnmatch
import logging

from .base import BaseScraper, ScrapedItem, SourceType

logger = logging.getLogger(__name__)


class FilesystemScraper(BaseScraper):
    """Scraper for local filesystem."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.seen_hashes: Set[str] = set()

    @property
    def source_type(self) -> SourceType:
        return SourceType.LOCAL_FILESYSTEM

    async def validate_connection(self) -> bool:
        fs_config = self.config.get("sources", {}).get("filesystem", {})
        paths = fs_config.get("paths", [])
        return any(Path(p).exists() for p in paths)

    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape configured filesystem paths."""
        fs_config = self.config.get("sources", {}).get("filesystem", {})

        if not fs_config.get("enabled", False):
            return

        paths = fs_config.get("paths", [])
        patterns = fs_config.get("patterns", ["*"])
        exclude_patterns = fs_config.get("exclude_patterns", [])

        for base_path in paths:
            base = Path(base_path)
            if not base.exists():
                logger.warning(f"Path does not exist: {base_path}")
                continue

            async for item in self._scan_directory(base, patterns, exclude_patterns):
                yield item

    async def _scan_directory(
        self, base_path: Path, patterns: list, exclude_patterns: list
    ) -> AsyncIterator[ScrapedItem]:
        """Recursively scan a directory."""
        try:
            for root, dirs, files in os.walk(base_path):
                dirs[:] = [
                    d
                    for d in dirs
                    if not any(fnmatch.fnmatch(d, excl.rstrip("/*")) for excl in exclude_patterns)
                ]

                for filename in files:
                    filepath = Path(root) / filename

                    if not any(fnmatch.fnmatch(filename, pat) for pat in patterns):
                        continue

                    try:
                        rel_path = str(filepath.relative_to(base_path))
                    except ValueError:
                        rel_path = str(filepath)

                    if any(fnmatch.fnmatch(rel_path, excl) for excl in exclude_patterns):
                        continue

                    item = await self._process_file(filepath)
                    if item:
                        yield item

        except PermissionError as e:
            logger.error(f"Permission denied: {e}")

    async def _process_file(self, filepath: Path) -> Optional[ScrapedItem]:
        """Process a single file."""
        try:
            if filepath.stat().st_size > 5 * 1024 * 1024:
                return None

            async with aiofiles.open(filepath, "rb") as f:
                raw_content = await f.read()

            if b"\x00" in raw_content[:1024]:
                return None

            try:
                import chardet

                detected = chardet.detect(raw_content)
                encoding = detected.get("encoding", "utf-8") or "utf-8"
            except ImportError:
                encoding = "utf-8"

            try:
                content = raw_content.decode(encoding)
            except (UnicodeDecodeError, LookupError):
                content = raw_content.decode("utf-8", errors="ignore")

            is_relevant, confidence = self.is_relevant(content, filepath.name)

            if not is_relevant and confidence < 0.1:
                return None

            stat = filepath.stat()

            return ScrapedItem(
                id=f"local:{filepath.as_posix()}",
                source_type=self.source_type,
                source_path=str(filepath.absolute()),
                content=content,
                content_type=self.detect_content_type(content, filepath.name),
                file_extension=filepath.suffix.lstrip("."),
                filename=filepath.name,
                metadata={
                    "absolute_path": str(filepath.absolute()),
                    "relative_path": str(filepath),
                    "encoding": encoding,
                },
                created_at=datetime.fromtimestamp(stat.st_ctime),
                modified_at=datetime.fromtimestamp(stat.st_mtime),
                size_bytes=stat.st_size,
                language=self.detect_language(content, filepath.name),
                confidence_score=confidence,
            )

        except Exception as e:
            logger.error(f"Error processing {filepath}: {e}")
            return None
