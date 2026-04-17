
from processors.processor import DataProcessor, ProcessedChunk
from scrapers.base import ContentType, ScrapedItem, SourceType


class TestDataProcessor:
    def setup_method(self):
        self.processor = DataProcessor(chunk_size=200, chunk_overlap=50)

    def test_process_item(self):
        item = ScrapedItem(
            id="test1",
            source_type=SourceType.LOCAL_FILESYSTEM,
            source_path="/test/file.py",
            content="def hello():\n    return 'world'\n",
            content_type=ContentType.SOURCE_CODE,
            filename="file.py",
            language="python",
        )

        chunks = self.processor.process(item)
        assert len(chunks) > 0
        assert all(isinstance(c, ProcessedChunk) for c in chunks)
        assert chunks[0].embedding
        assert len(chunks[0].embedding) == self.processor.vector_size

    def test_deduplication(self):
        item = ScrapedItem(
            id="test1",
            source_type=SourceType.LOCAL_FILESYSTEM,
            source_path="/test/file.py",
            content="def hello():\n    return 'world'\n",
            content_type=ContentType.SOURCE_CODE,
        )

        chunks1 = self.processor.process(item)
        chunks2 = self.processor.process(item)
        assert len(chunks1) > 0
        assert len(chunks2) == 0

    def test_chunking_long_content(self):
        long_content = "word " * 500
        item = ScrapedItem(
            id="test_long",
            source_type=SourceType.LOCAL_FILESYSTEM,
            source_path="/test/long.txt",
            content=long_content,
            content_type=ContentType.DOCUMENTATION,
        )

        chunks = self.processor.process(item)
        assert len(chunks) > 1

    def test_compute_similarity(self):
        sim = self.processor.compute_similarity("hello world", "hello world")
        assert sim > 0.9

        sim_diff = self.processor.compute_similarity("hello world", "completely different")
        assert sim_diff < sim
