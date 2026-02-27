from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any, AsyncIterator
from enum import Enum
import hashlib
from pathlib import Path


class ContentType(Enum):
    SOURCE_CODE = "source_code"
    DOCUMENTATION = "documentation"
    CONFIGURATION = "configuration"
    DATA = "data"
    BINARY = "binary"
    UNKNOWN = "unknown"


class SourceType(Enum):
    GITHUB = "github"
    LOCAL_FILESYSTEM = "local_filesystem"
    GOOGLE_DRIVE = "google_drive"
    DROPBOX = "dropbox"
    EMAIL = "email"
    WEB_CACHE = "web_cache"
    MANUAL = "manual"


@dataclass
class ScrapedItem:
    """Represents a single piece of recovered data."""

    id: str
    source_type: SourceType
    source_path: str
    content: str
    content_type: ContentType
    file_extension: Optional[str] = None
    filename: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None
    scraped_at: datetime = field(default_factory=datetime.utcnow)
    content_hash: str = ""
    size_bytes: int = 0
    language: Optional[str] = None
    confidence_score: float = 1.0

    def __post_init__(self):
        if not self.content_hash and self.content:
            self.content_hash = hashlib.sha256(self.content.encode()).hexdigest()
        if not self.size_bytes and self.content:
            self.size_bytes = len(self.content.encode())
        if not self.id:
            self.id = f"{self.source_type.value}:{self.content_hash[:16]}"


@dataclass
class ScrapeResult:
    """Result of a scraping operation."""

    source_type: SourceType
    items: List[ScrapedItem]
    success: bool
    error_message: Optional[str] = None
    total_found: int = 0
    total_processed: int = 0
    duration_seconds: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


class BaseScraper(ABC):
    """Base class for all scrapers."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.keywords = config.get("project_keywords", [])
        self.file_signatures = config.get("file_signatures", [])

    @property
    @abstractmethod
    def source_type(self) -> SourceType:
        pass

    @abstractmethod
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        pass

    @abstractmethod
    async def validate_connection(self) -> bool:
        pass

    def is_relevant(self, content: str, filename: str = "") -> tuple[bool, float]:
        """Check if content is relevant to the project."""
        score = 0.0
        max_score = len(self.keywords) + len(self.file_signatures)

        if max_score == 0:
            return True, 1.0

        content_lower = content.lower()
        filename_lower = filename.lower()

        for keyword in self.keywords:
            if keyword.lower() in content_lower or keyword.lower() in filename_lower:
                score += 1.0

        for sig in self.file_signatures:
            if sig["pattern"] in content:
                score += 1.5

        confidence = min(score / max_score, 1.0) if max_score > 0 else 1.0
        return score > 0, confidence

    def detect_content_type(self, content: str, filename: str = "") -> ContentType:
        """Detect the type of content."""
        ext = Path(filename).suffix.lower() if filename else ""

        code_extensions = {".py", ".js", ".ts", ".java", ".cpp", ".c", ".go", ".rs", ".rb"}
        doc_extensions = {".md", ".rst", ".txt", ".doc", ".docx", ".pdf"}
        config_extensions = {".json", ".yaml", ".yml", ".toml", ".ini", ".env"}
        data_extensions = {".csv", ".sql", ".xml"}

        if ext in code_extensions:
            return ContentType.SOURCE_CODE
        elif ext in doc_extensions:
            return ContentType.DOCUMENTATION
        elif ext in config_extensions:
            return ContentType.CONFIGURATION
        elif ext in data_extensions:
            return ContentType.DATA

        if any(kw in content[:500] for kw in ["def ", "function ", "class ", "import ", "const ", "let "]):
            return ContentType.SOURCE_CODE
        elif content.startswith("#") or "##" in content[:200]:
            return ContentType.DOCUMENTATION

        return ContentType.UNKNOWN

    def detect_language(self, content: str, filename: str = "") -> Optional[str]:
        """Detect programming language."""
        ext = Path(filename).suffix.lower() if filename else ""

        ext_to_lang = {
            ".py": "python",
            ".js": "javascript",
            ".ts": "typescript",
            ".java": "java",
            ".cpp": "cpp",
            ".c": "c",
            ".go": "go",
            ".rs": "rust",
            ".rb": "ruby",
            ".php": "php",
            ".swift": "swift",
            ".kt": "kotlin",
            ".scala": "scala",
            ".r": "r",
            ".jl": "julia",
            ".sql": "sql",
            ".html": "html",
            ".css": "css",
            ".sh": "bash",
        }

        if ext in ext_to_lang:
            return ext_to_lang[ext]

        if "def " in content and "import " in content:
            return "python"
        elif "function" in content and ("const " in content or "let " in content):
            return "javascript"

        return None
