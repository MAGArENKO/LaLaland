import pytest

from storage.vector_store import VectorStore
from processors.processor import ProcessedChunk


class TestVectorStoreInMemory:
    def setup_method(self):
        self.store = VectorStore(url="http://nonexistent:6333", collection_name="test")
        self.store._use_qdrant = False

    def test_upsert_and_search(self):
        chunks = [
            ProcessedChunk(
                id="chunk1",
                parent_id="parent1",
                content="hello world python code",
                embedding=[0.1] * 384,
                chunk_index=0,
                total_chunks=1,
                metadata={
                    "source_type": "local_filesystem",
                    "source_path": "/test/file.py",
                    "content_type": "source_code",
                    "filename": "file.py",
                    "language": "python",
                    "confidence_score": 1.0,
                },
            )
        ]

        stored = self.store.upsert_chunks(chunks)
        assert stored == 1

        results = self.store.search([0.1] * 384, limit=5)
        assert len(results) == 1
        assert results[0]["content"] == "hello world python code"

    def test_statistics(self):
        stats = self.store.get_statistics()
        assert stats["backend"] == "in_memory"
        assert stats["total_points"] == 0

    def test_delete_by_source(self):
        chunks = [
            ProcessedChunk(
                id=f"chunk{i}",
                parent_id="parent1",
                content=f"content {i}",
                embedding=[0.1] * 384,
                chunk_index=0,
                total_chunks=1,
                metadata={
                    "source_type": st,
                    "source_path": f"/test/{i}",
                    "content_type": "source_code",
                    "filename": f"file{i}.py",
                    "language": "python",
                    "confidence_score": 1.0,
                },
            )
            for i, st in enumerate(["github", "local_filesystem", "github"])
        ]

        self.store.upsert_chunks(chunks)
        assert self.store.get_statistics()["total_points"] == 3

        self.store.delete_by_source("github")
        assert self.store.get_statistics()["total_points"] == 1
