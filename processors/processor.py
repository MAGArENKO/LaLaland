import hashlib
import logging
import re
from dataclasses import dataclass
from typing import Any, Dict, List

from scrapers.base import ContentType, ScrapedItem

logger = logging.getLogger(__name__)


@dataclass
class ProcessedChunk:
    """A processed chunk of content."""

    id: str
    parent_id: str
    content: str
    embedding: List[float]
    chunk_index: int
    total_chunks: int
    metadata: Dict[str, Any]


class DataProcessor:
    """Process and prepare scraped data for storage.

    Supports both sentence-transformers embeddings (when available)
    and a lightweight hash-based fallback.
    """

    def __init__(
        self,
        embedding_model: str = "all-MiniLM-L6-v2",
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self._model_name = embedding_model
        self._embedding_model = None
        self._vector_size = 384
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.seen_hashes: set = set()

    @property
    def embedding_model(self):
        if self._embedding_model is None:
            try:
                from sentence_transformers import SentenceTransformer

                self._embedding_model = SentenceTransformer(self._model_name)
                self._vector_size = self._embedding_model.get_sentence_embedding_dimension()
                logger.info(f"Loaded embedding model: {self._model_name}")
            except (ImportError, Exception) as e:
                logger.warning(f"sentence-transformers not available ({e}), using hash embeddings")
                self._embedding_model = "fallback"
        return self._embedding_model

    @property
    def vector_size(self) -> int:
        _ = self.embedding_model
        return self._vector_size

    def encode(self, text: str) -> List[float]:
        """Generate embedding for text."""
        if self.embedding_model == "fallback":
            return self._hash_embedding(text)
        return self.embedding_model.encode(text).tolist()

    def _hash_embedding(self, text: str) -> List[float]:
        """Fallback: deterministic hash-based pseudo-embedding."""
        h = hashlib.sha512(text.encode()).digest()
        raw = [b / 255.0 * 2 - 1 for b in h]
        while len(raw) < self._vector_size:
            h = hashlib.sha512(h).digest()
            raw.extend(b / 255.0 * 2 - 1 for b in h)
        return raw[: self._vector_size]

    def process(self, item: ScrapedItem) -> List[ProcessedChunk]:
        """Process a scraped item into chunks with embeddings."""
        if item.content_hash in self.seen_hashes:
            return []
        self.seen_hashes.add(item.content_hash)

        normalized = self._normalize_content(item.content, item.content_type)
        chunks = self._chunk_content(normalized, item.content_type)

        processed = []
        for i, chunk_text in enumerate(chunks):
            embedding = self.encode(chunk_text)
            chunk_id = hashlib.sha256(f"{item.id}:{i}".encode()).hexdigest()[:16]

            processed.append(
                ProcessedChunk(
                    id=chunk_id,
                    parent_id=item.id,
                    content=chunk_text,
                    embedding=embedding,
                    chunk_index=i,
                    total_chunks=len(chunks),
                    metadata={
                        "source_type": item.source_type.value,
                        "source_path": item.source_path,
                        "content_type": item.content_type.value,
                        "filename": item.filename,
                        "language": item.language,
                        "confidence_score": item.confidence_score,
                    },
                )
            )

        return processed

    def _normalize_content(self, content: str, content_type: ContentType) -> str:
        content = re.sub(r"\n{3,}", "\n\n", content)
        content = re.sub(r" {2,}", " ", content)

        if content_type == ContentType.SOURCE_CODE:
            content = self._normalize_code(content)
        elif content_type == ContentType.DOCUMENTATION:
            content = self._normalize_docs(content)

        return content.strip()

    def _normalize_code(self, content: str) -> str:
        lines = content.split("\n")
        return "\n".join(line.rstrip() for line in lines)

    def _normalize_docs(self, content: str) -> str:
        return re.sub(r"<[^>]+>", "", content)

    def _chunk_content(self, content: str, content_type: ContentType) -> List[str]:
        if content_type == ContentType.SOURCE_CODE:
            return self._chunk_code(content)
        return self._chunk_text(content)

    def _chunk_code(self, content: str) -> List[str]:
        chunks = []
        patterns = [
            r"((?:def|async def)\s+\w+[^:]*:.*?)(?=\n(?:def|async def|class)\s|\Z)",
            r"(class\s+\w+[^:]*:.*?)(?=\nclass\s|\Z)",
        ]

        remaining = content
        for pattern in patterns:
            matches = re.findall(pattern, remaining, re.DOTALL)
            for match in matches:
                if len(match) <= self.chunk_size:
                    chunks.append(match)
                else:
                    chunks.extend(self._chunk_text(match))
                remaining = remaining.replace(match, "", 1)

        if remaining.strip():
            chunks.extend(self._chunk_text(remaining))

        return chunks if chunks else self._chunk_text(content)

    def _chunk_text(self, content: str) -> List[str]:
        if len(content) <= self.chunk_size:
            return [content]

        chunks = []
        start = 0

        while start < len(content):
            end = start + self.chunk_size

            if end < len(content):
                for sep in [". ", ".\n", "\n\n", "\n", " "]:
                    last_sep = content[start:end].rfind(sep)
                    if last_sep > self.chunk_size // 2:
                        end = start + last_sep + len(sep)
                        break

            chunks.append(content[start:end].strip())
            start = end - self.chunk_overlap

        return [c for c in chunks if c]

    def compute_similarity(self, text1: str, text2: str) -> float:
        """Compute cosine similarity between two texts."""
        emb1 = self.encode(text1)
        emb2 = self.encode(text2)

        dot = sum(a * b for a, b in zip(emb1, emb2))
        norm1 = sum(a * a for a in emb1) ** 0.5
        norm2 = sum(a * a for a in emb2) ** 0.5

        return dot / (norm1 * norm2) if norm1 and norm2 else 0.0
