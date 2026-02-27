# AGENTS.md

## Cursor Cloud specific instructions

### Repository Overview

**Project Recovery System** — a self-sustaining data recovery and organization platform that scrapes files from multiple sources (filesystem, GitHub), processes them with embeddings (sentence-transformers), stores them in a vector database (Qdrant), and presents them for human review via Argilla or a Streamlit dashboard.

The original `README.md` (~598KB) is the owner's raw research archive gathered after a drive crash. The actual source code was extracted and enhanced from its inline code snippets.

### Services

| Service | Port | How to start | Required? |
|---------|------|-------------|-----------|
| FastAPI API | 8000 | `python main.py api` | Yes |
| Streamlit Dashboard | 8501 | `python main.py dashboard` | Optional |
| PostgreSQL | 5432 | `docker compose up -d postgres` | Optional (not yet wired in) |
| Qdrant | 6333 | `docker compose up -d qdrant` | Optional (in-memory fallback) |
| Redis | 6379 | `docker compose up -d redis` | Optional (needed for Celery) |

### Quick Commands

- **Lint**: `ruff check .` (auto-fix: `ruff check --fix .`)
- **Tests**: `python -m pytest tests/ -v`
- **API**: `source .venv/bin/activate && python main.py api`
- **Dashboard**: `source .venv/bin/activate && python main.py dashboard`
- **Pipeline (one-shot)**: `source .venv/bin/activate && python main.py pipeline`
- **Docker services**: `sudo docker compose up -d`

### Gotchas

- The `qdrant-client>=1.17` uses `query_points()` instead of the deprecated `search()` method.
- All external services (Qdrant, Argilla, Redis) degrade gracefully — the app works without them using in-memory fallbacks.
- The sentence-transformers model (`all-MiniLM-L6-v2`) downloads ~90MB on first use; cached at `~/.cache/huggingface/`.
- Docker requires `fuse-overlayfs` and `iptables-legacy` in the cloud VM (Docker-in-Docker setup).
- The `README.md` is ~600KB — it's the owner's raw research archive, not documentation.
