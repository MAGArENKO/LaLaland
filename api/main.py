from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Project Recovery System",
    description="Self-sustaining system for recovering and organizing lost project data",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = None


@app.on_event("startup")
async def startup():
    global pipeline
    from orchestrator.pipeline import RecoveryPipeline

    try:
        pipeline = RecoveryPipeline()
        logger.info("Recovery pipeline initialized")
    except Exception as e:
        logger.error(f"Error initializing pipeline: {e}")


class SearchQuery(BaseModel):
    query: str
    limit: int = 10
    filters: Optional[Dict[str, Any]] = None


class SearchResult(BaseModel):
    score: float
    content: str
    source_path: str
    source_type: str
    filename: Optional[str] = None
    language: Optional[str] = None


class PipelineRunResponse(BaseModel):
    run_id: str
    status: str
    items_scraped: int
    items_processed: int
    items_stored: int


class FileProcessRequest(BaseModel):
    file_path: str


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "pipeline_status": pipeline.status.value if pipeline else "not_initialized",
    }


@app.get("/stats")
async def get_statistics():
    if not pipeline:
        raise HTTPException(status_code=503, detail="Pipeline not initialized")
    return pipeline.get_statistics()


@app.post("/search", response_model=List[SearchResult])
async def search(query: SearchQuery):
    if not pipeline:
        raise HTTPException(status_code=503, detail="Pipeline not initialized")

    results = pipeline.search_recovered_data(query.query, query.limit, query.filters)

    return [
        SearchResult(
            score=r.get("score", 0.0),
            content=r.get("content", ""),
            source_path=r.get("source_path", ""),
            source_type=r.get("source_type", "unknown"),
            filename=r.get("filename"),
            language=r.get("language"),
        )
        for r in results
    ]


@app.post("/run")
async def run_pipeline(background_tasks: BackgroundTasks):
    if not pipeline:
        raise HTTPException(status_code=503, detail="Pipeline not initialized")

    if pipeline.status.value == "running":
        raise HTTPException(status_code=409, detail="Pipeline already running")

    import asyncio

    async def _run():
        await pipeline.run_full_pipeline()

    background_tasks.add_task(asyncio.run, _run())

    return {"status": "started", "message": "Pipeline run started in background"}


@app.get("/runs")
async def get_runs():
    if not pipeline:
        raise HTTPException(status_code=503, detail="Pipeline not initialized")

    return [
        {
            "id": run.id,
            "started_at": run.started_at.isoformat(),
            "ended_at": run.ended_at.isoformat() if run.ended_at else None,
            "status": run.status.value,
            "items_scraped": run.items_scraped,
            "items_processed": run.items_processed,
            "items_stored": run.items_stored,
            "errors": run.errors,
        }
        for run in pipeline.runs_history
    ]


@app.get("/sources")
async def get_sources():
    from config.settings import load_sources_config

    return load_sources_config()


@app.post("/sources/{source_type}/rescan")
async def rescan_source(source_type: str, background_tasks: BackgroundTasks):
    return {"status": "queued", "source": source_type}
