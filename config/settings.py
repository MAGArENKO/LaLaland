from pydantic_settings import BaseSettings
from typing import Optional, List
from pathlib import Path
import yaml


class Settings(BaseSettings):
    argilla_api_url: str = "http://localhost:6900"
    argilla_api_key: str = "admin.apikey"
    argilla_workspace: str = "project_recovery"

    database_url: str = "postgresql://recovery:recovery_pass@localhost:5432/project_recovery"

    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "project_fragments"

    redis_url: str = "redis://localhost:6379"

    scan_directories: List[str] = []
    github_token: Optional[str] = None
    github_username: Optional[str] = None

    embedding_model: str = "all-MiniLM-L6-v2"
    chunk_size: int = 1000
    chunk_overlap: int = 200

    scrape_interval_hours: int = 6

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()


def load_sources_config() -> dict:
    """Load sources configuration from YAML."""
    config_path = Path(__file__).parent / "sources.yaml"
    if config_path.exists():
        with open(config_path) as f:
            return yaml.safe_load(f) or {}
    return {}
