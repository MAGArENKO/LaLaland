import tempfile
from pathlib import Path

import pytest

from scrapers.base import ContentType, ScrapedItem, SourceType
from scrapers.filesystem_scraper import FilesystemScraper


class TestScrapedItem:
    def test_auto_hash(self):
        item = ScrapedItem(
            id="test1",
            source_type=SourceType.LOCAL_FILESYSTEM,
            source_path="/test/file.py",
            content="hello world",
            content_type=ContentType.SOURCE_CODE,
        )
        assert item.content_hash != ""
        assert item.size_bytes > 0

    def test_auto_id(self):
        item = ScrapedItem(
            id="",
            source_type=SourceType.GITHUB,
            source_path="github.com/test",
            content="test content",
            content_type=ContentType.DOCUMENTATION,
        )
        assert item.id.startswith("github:")


class TestContentDetection:
    def setup_method(self):
        self.config = {"project_keywords": [], "file_signatures": []}

    def test_detect_python(self):
        scraper = FilesystemScraper(self.config)
        assert scraper.detect_content_type("", "test.py") == ContentType.SOURCE_CODE
        assert scraper.detect_language("", "test.py") == "python"

    def test_detect_markdown(self):
        scraper = FilesystemScraper(self.config)
        assert scraper.detect_content_type("", "README.md") == ContentType.DOCUMENTATION

    def test_detect_yaml(self):
        scraper = FilesystemScraper(self.config)
        assert scraper.detect_content_type("", "config.yaml") == ContentType.CONFIGURATION

    def test_detect_by_content(self):
        scraper = FilesystemScraper(self.config)
        result = scraper.detect_content_type("def hello():\n    pass\nimport os")
        assert result == ContentType.SOURCE_CODE


class TestRelevance:
    def test_relevant_by_keyword(self):
        config = {"project_keywords": ["recovery"], "file_signatures": []}
        scraper = FilesystemScraper(config)
        is_relevant, confidence = scraper.is_relevant("this is about recovery system", "test.py")
        assert is_relevant
        assert confidence > 0

    def test_not_relevant(self):
        config = {"project_keywords": ["unique_keyword_xyz"], "file_signatures": []}
        scraper = FilesystemScraper(config)
        is_relevant, confidence = scraper.is_relevant("nothing related here", "test.py")
        assert not is_relevant

    def test_no_keywords(self):
        config = {"project_keywords": [], "file_signatures": []}
        scraper = FilesystemScraper(config)
        is_relevant, confidence = scraper.is_relevant("anything", "test.py")
        assert is_relevant
        assert confidence == 1.0


class TestFilesystemScraper:
    @pytest.mark.asyncio
    async def test_validate_existing_path(self):
        config = {
            "sources": {"filesystem": {"paths": ["/tmp"], "enabled": True}},
            "project_keywords": [],
            "file_signatures": [],
        }
        scraper = FilesystemScraper(config)
        assert await scraper.validate_connection()

    @pytest.mark.asyncio
    async def test_validate_nonexistent_path(self):
        config = {
            "sources": {"filesystem": {"paths": ["/nonexistent_path_xyz"]}},
            "project_keywords": [],
            "file_signatures": [],
        }
        scraper = FilesystemScraper(config)
        assert not await scraper.validate_connection()

    @pytest.mark.asyncio
    async def test_scrape_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = Path(tmpdir) / "test.py"
            test_file.write_text("def hello():\n    print('hello recovery')\n")

            config = {
                "sources": {
                    "filesystem": {
                        "enabled": True,
                        "paths": [tmpdir],
                        "patterns": ["*.py"],
                        "exclude_patterns": [],
                    }
                },
                "project_keywords": ["recovery"],
                "file_signatures": [],
            }
            scraper = FilesystemScraper(config)

            items = []
            async for item in scraper.scrape():
                items.append(item)

            assert len(items) == 1
            assert items[0].filename == "test.py"
            assert items[0].language == "python"
            assert "hello recovery" in items[0].content
