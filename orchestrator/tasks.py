import asyncio
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

_celery_app = None


def get_celery_app():
    global _celery_app
    if _celery_app is None:
        try:
            from celery import Celery
            from celery.schedules import crontab

            from config.settings import settings

            _celery_app = Celery("recovery_tasks", broker=settings.redis_url, backend=settings.redis_url)

            _celery_app.conf.update(
                task_serializer="json",
                accept_content=["json"],
                result_serializer="json",
                timezone="UTC",
                enable_utc=True,
            )

            _celery_app.conf.beat_schedule = {
                "run-full-recovery": {
                    "task": "orchestrator.tasks.run_recovery_pipeline",
                    "schedule": crontab(minute=0, hour=f"*/{settings.scrape_interval_hours}"),
                },
                "quick-filesystem-scan": {
                    "task": "orchestrator.tasks.run_filesystem_scan",
                    "schedule": crontab(minute=0),
                },
            }
        except ImportError:
            logger.warning("Celery not available, task scheduling disabled")
    return _celery_app


def run_async(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


app = get_celery_app()

if app:

    @app.task(bind=True, max_retries=3)
    def run_recovery_pipeline(self):
        from orchestrator.pipeline import RecoveryPipeline

        try:
            pipeline = RecoveryPipeline()
            result = run_async(pipeline.run_full_pipeline())
            return {
                "run_id": result.id,
                "status": result.status.value,
                "items_scraped": result.items_scraped,
                "items_processed": result.items_processed,
                "items_stored": result.items_stored,
                "errors": result.errors,
            }
        except Exception as e:
            self.retry(exc=e, countdown=60 * 5)

    @app.task
    def run_filesystem_scan():
        from orchestrator.pipeline import RecoveryPipeline
        from scrapers.base import SourceType

        pipeline = RecoveryPipeline()
        scraper = pipeline.scrapers[SourceType.LOCAL_FILESYSTEM]

        items_found = 0

        async def scan():
            nonlocal items_found
            async for item in scraper.scrape():
                chunks = pipeline.processor.process(item)
                if chunks:
                    pipeline.vector_store.upsert_chunks(chunks)
                    items_found += 1

        run_async(scan())
        return {"items_found": items_found, "timestamp": datetime.utcnow().isoformat()}
