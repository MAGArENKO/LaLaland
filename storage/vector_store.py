import logging
from typing import Any, Dict, List, Optional

from processors.processor import ProcessedChunk

logger = logging.getLogger(__name__)


class VectorStore:
    """Vector database for semantic search over recovered data.

    Connects to Qdrant when available; falls back to in-memory storage.
    """

    def __init__(
        self,
        url: str = "http://localhost:6333",
        collection_name: str = "project_fragments",
        vector_size: int = 384,
    ):
        self.url = url
        self.collection_name = collection_name
        self.vector_size = vector_size
        self._client = None
        self._in_memory: List[Dict[str, Any]] = []
        self._use_qdrant = True

    @property
    def client(self):
        if self._client is None and self._use_qdrant:
            try:
                from qdrant_client import QdrantClient

                self._client = QdrantClient(url=self.url, timeout=5)
                self._client.get_collections()
                self._ensure_collection()
                logger.info(f"Connected to Qdrant at {self.url}")
            except Exception as e:
                logger.warning(f"Qdrant unavailable ({e}), using in-memory storage")
                self._use_qdrant = False
                self._client = None
        return self._client

    def _ensure_collection(self):
        from qdrant_client.http import models

        collections = self._client.get_collections().collections
        exists = any(c.name == self.collection_name for c in collections)

        if not exists:
            self._client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=self.vector_size, distance=models.Distance.COSINE),
            )
            for field_name in ("source_type", "content_type", "language"):
                self._client.create_payload_index(
                    collection_name=self.collection_name,
                    field_name=field_name,
                    field_schema=models.PayloadSchemaType.KEYWORD,
                )

    def upsert_chunks(self, chunks: List[ProcessedChunk]) -> int:
        """Insert or update chunks."""
        if not chunks:
            return 0

        if self.client:
            return self._upsert_qdrant(chunks)
        return self._upsert_memory(chunks)

    def _upsert_qdrant(self, chunks: List[ProcessedChunk]) -> int:
        from qdrant_client.http import models

        points = [
            models.PointStruct(
                id=hash(chunk.id) % (2**63),
                vector=chunk.embedding,
                payload={
                    "chunk_id": chunk.id,
                    "parent_id": chunk.parent_id,
                    "content": chunk.content,
                    "chunk_index": chunk.chunk_index,
                    "total_chunks": chunk.total_chunks,
                    **chunk.metadata,
                },
            )
            for chunk in chunks
        ]

        self._client.upsert(collection_name=self.collection_name, points=points)
        return len(points)

    def _upsert_memory(self, chunks: List[ProcessedChunk]) -> int:
        for chunk in chunks:
            self._in_memory.append(
                {
                    "chunk_id": chunk.id,
                    "parent_id": chunk.parent_id,
                    "content": chunk.content,
                    "embedding": chunk.embedding,
                    "chunk_index": chunk.chunk_index,
                    "total_chunks": chunk.total_chunks,
                    **chunk.metadata,
                }
            )
        return len(chunks)

    def search(
        self,
        query_vector: List[float],
        limit: int = 10,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """Semantic search over stored chunks."""
        if self.client:
            return self._search_qdrant(query_vector, limit, filters)
        return self._search_memory(query_vector, limit)

    def _search_qdrant(self, query_vector, limit, filters):
        from qdrant_client.http import models

        filter_conditions = []
        if filters:
            for key, value in filters.items():
                if isinstance(value, list):
                    filter_conditions.append(models.FieldCondition(key=key, match=models.MatchAny(any=value)))
                else:
                    filter_conditions.append(models.FieldCondition(key=key, match=models.MatchValue(value=value)))

        query_filter = models.Filter(must=filter_conditions) if filter_conditions else None

        results = self._client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            query_filter=query_filter,
            limit=limit,
            with_payload=True,
        )

        return [{"score": hit.score, **hit.payload} for hit in results.points]

    def _search_memory(self, query_vector, limit):
        scored = []
        for item in self._in_memory:
            emb = item.get("embedding", [])
            if emb:
                dot = sum(a * b for a, b in zip(query_vector, emb))
                n1 = sum(a * a for a in query_vector) ** 0.5
                n2 = sum(a * a for a in emb) ** 0.5
                score = dot / (n1 * n2) if n1 and n2 else 0.0
                scored.append({"score": score, **{k: v for k, v in item.items() if k != "embedding"}})

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:limit]

    def search_by_text(
        self,
        query: str,
        processor,
        limit: int = 10,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """Search using text query."""
        query_vector = processor.encode(query)
        return self.search(query_vector, limit, filters)

    def get_statistics(self) -> Dict[str, Any]:
        """Get collection statistics."""
        if self.client:
            try:
                info = self._client.get_collection(self.collection_name)
                return {
                    "backend": "qdrant",
                    "total_points": info.points_count,
                    "vectors_count": info.vectors_count,
                    "indexed_points": info.indexed_vectors_count,
                }
            except Exception:
                pass

        return {
            "backend": "in_memory",
            "total_points": len(self._in_memory),
            "vectors_count": len(self._in_memory),
            "indexed_points": 0,
        }

    def delete_by_source(self, source_type: str):
        """Delete all chunks from a specific source."""
        if self.client:
            from qdrant_client.http import models

            self._client.delete(
                collection_name=self.collection_name,
                points_selector=models.FilterSelector(
                    filter=models.Filter(
                        must=[models.FieldCondition(key="source_type", match=models.MatchValue(value=source_type))]
                    )
                ),
            )
        else:
            self._in_memory = [item for item in self._in_memory if item.get("source_type") != source_type]
