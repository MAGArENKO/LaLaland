# AGENTS.md

## Cursor Cloud specific instructions

### Repository State

This repository is currently a **planning/design document repository** — not a runnable codebase. It contains:

- `README.md` (~598KB, ~17,600 lines): A large design document composed of AI chat logs, architecture diagrams, and inline code snippets describing a planned **MamaAI Agency Recovery System** and **AI Creative Pipeline**.
- `python -m venv venv`: A misnamed file (filename was accidentally created from a shell command). Contains 3 lines of setup command snippets.

**There are no actual source code files, no `requirements.txt`, no `docker-compose.yml`, no `Dockerfile`, no tests, and no runnable application.**

### Planned Tech Stack (from README)

The README describes a Python-based system using: FastAPI, Streamlit, PostgreSQL, Qdrant (vector DB), Redis, Elasticsearch, Argilla (data labeling), Celery, sentence-transformers, SQLAlchemy, and Docker Compose.

### Development Environment

- Python 3.12.3 virtual environment at `.venv/`
- Activate with: `source .venv/bin/activate`
- No dependencies to install (no `requirements.txt` exists yet)

### What Cannot Be Done Yet

- **Lint**: No source code to lint
- **Test**: No tests exist
- **Build**: No build system exists
- **Run**: No application entry point exists

### Notes for Future Agents

- If source code is extracted from the README into actual files, the development environment will need `requirements.txt` created and dependencies installed.
- The README contains multiple overlapping versions of the same project structure; the most complete version starts around line 4890.
- Docker Compose configuration for backing services (PostgreSQL, Qdrant, Redis, Elasticsearch, Argilla) is described starting around line 6461.
