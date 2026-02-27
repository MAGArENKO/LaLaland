import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from argilla_integration.datasets import ArgillaManager
from config.settings import load_sources_config, settings
from processors.processor import DataProcessor
from scrapers.base import ScrapedItem, SourceType
from scrapers.filesystem_scraper import FilesystemScraper
from scrapers.github_scraper import GitHubScraper
from storage.vector_store import VectorStore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PipelineStatus(Enum):
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    ERROR = "error"


@dataclass
class PipelineRun:
    id: str
    started_at: datetime
    ended_at: Optional[datetime] = None
    status: PipelineStatus = PipelineStatus.RUNNING
    items_scraped: int = 0
    items_processed: int = 0
    items_stored: int = 0
    errors: List[str] = field(default_factory=list)


class RecoveryPipeline:
    """Main pipeline for recovering and organizing project data."""

    def __init__(self):
        self.config = load_sources_config()
        self.processor = DataProcessor(
            embedding_model=settings.embedding_model,
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
        )
        self.vector_store = VectorStore(
            url=settings.qdrant_url,
            collection_name=settings.qdrant_collection,
            vector_size=self.processor.vector_size,
        )
        self.argilla = ArgillaManager(
            api_url=settings.argilla_api_url,
            api_key=settings.argilla_api_key,
            workspace=settings.argilla_workspace,
        )

        self.scrapers = self._init_scrapers()

        self.status = PipelineStatus.IDLE
        self.current_run: Optional[PipelineRun] = None
        self.runs_history: List[PipelineRun] = []

        self.item_buffer: List[ScrapedItem] = []
        self.buffer_size = 50

    def _init_scrapers(self) -> Dict[SourceType, Any]:
        scrapers = {}
        scrapers[SourceType.GITHUB] = GitHubScraper(self.config, token=settings.github_token)
        scrapers[SourceType.LOCAL_FILESYSTEM] = FilesystemScraper(self.config)
        return scrapers

    async def run_full_pipeline(self) -> PipelineRun:
        """Run the complete recovery pipeline."""
        run = PipelineRun(
            id=f"run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}",
            started_at=datetime.utcnow(),
        )
        self.current_run = run
        self.status = PipelineStatus.RUNNING

        logger.info(f"Starting pipeline run: {run.id}")

        try:
            dataset = self.argilla.create_recovery_dataset(name=f"recovery_{run.id}")

            for source_type, scraper in self.scrapers.items():
                logger.info(f"Running scraper: {source_type.value}")

                try:
                    if await scraper.validate_connection():
                        async for item in scraper.scrape():
                            run.items_scraped += 1
                            await self._process_item(item, dataset, run)

                            if run.items_scraped % 100 == 0:
                                logger.info(f"Scraped {run.items_scraped} items...")
                    else:
                        logger.warning(f"Could not connect to {source_type.value}")

                except Exception as e:
                    error_msg = f"Error in {source_type.value}: {str(e)}"
                    logger.error(error_msg)
                    run.errors.append(error_msg)

            await self._flush_buffer(dataset, run)
            run.status = PipelineStatus.IDLE

        except Exception as e:
            run.status = PipelineStatus.ERROR
            run.errors.append(f"Pipeline error: {str(e)}")
            logger.error(f"Pipeline failed: {e}")

        finally:
            run.ended_at = datetime.utcnow()
            self.runs_history.append(run)
            self.status = PipelineStatus.IDLE
            self.current_run = None

        logger.info(
            f"Pipeline complete. Scraped: {run.items_scraped}, "
            f"Processed: {run.items_processed}, Stored: {run.items_stored}"
        )

        return run

    async def _process_item(self, item: ScrapedItem, dataset, run: PipelineRun):
        self.item_buffer.append(item)
        if len(self.item_buffer) >= self.buffer_size:
            await self._flush_buffer(dataset, run)

    async def _flush_buffer(self, dataset, run: PipelineRun):
        if not self.item_buffer:
            return

        all_chunks = []
        for item in self.item_buffer:
            chunks = self.processor.process(item)
            all_chunks.extend(chunks)
            run.items_processed += 1

        if all_chunks:
            stored = self.vector_store.upsert_chunks(all_chunks)
            run.items_stored += stored

        self.argilla.add_items_to_dataset(dataset, self.item_buffer)
        self.item_buffer.clear()

    def search_recovered_data(
        self,
        query: str,
        limit: int = 10,
        filters: Optional[Dict] = None,
    ) -> List[Dict[str, Any]]:
        """Search through recovered data."""
        return self.vector_store.search_by_text(query, self.processor, limit, filters)

    def get_statistics(self) -> Dict[str, Any]:
        vector_stats = self.vector_store.get_statistics()
        return {
            "status": self.status.value,
            "vector_store": vector_stats,
            "total_runs": len(self.runs_history),
            "last_run": (
                {
                    "id": self.runs_history[-1].id,
                    "status": self.runs_history[-1].status.value,
                    "items_scraped": self.runs_history[-1].items_scraped,
                    "items_processed": self.runs_history[-1].items_processed,
                    "items_stored": self.runs_history[-1].items_stored,
                }
                if self.runs_history
                else None
            ),
        }
