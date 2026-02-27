# AGENTS.md

## Cursor Cloud specific instructions

### Repository Purpose

This repository is a **personal recovery archive** — a collection of research materials, AI chat logs, architecture plans, and code snippets the owner gathered after a drive crash. It documents trails followed online and locally while recovering lost work and planning two projects:

1. **MamaAI Agency Recovery System** — A data recovery/organization platform (FastAPI, Argilla, PostgreSQL, Qdrant, Celery)
2. **AI Creative Pipeline** — An AI-driven VFX/3D content creation system (ComfyUI, Krita, OpenUSD, Blender CLI)

### Repository Contents

- `README.md` (~598KB, ~17,600 lines): The primary archive. Contains AI conversation logs, architecture diagrams, inline code snippets, project structures, docker-compose configs, requirements lists, and planning notes. This is **not** structured documentation — it is a raw research dump.
- `python -m venv venv`: A misnamed file (filename accidentally created from a shell command). Contains 3 lines of setup snippets.

**There is no runnable source code.** All code exists only as inline snippets within the README.

### Development Environment

- Python 3.12.3 virtual environment at `.venv/`
- Activate with: `source .venv/bin/activate`
- No dependencies to install (no `requirements.txt` file exists)
- No lint, test, build, or run targets exist

### Notes for Future Agents

- The README contains multiple overlapping versions of planned project structures; the most complete one starts around line 4890.
- Docker Compose configuration for backing services is described starting around line 6461.
- Requirements lists appear at lines ~6567 and ~11481.
- If the owner decides to extract code from the README into actual files, a `requirements.txt`, `docker-compose.yml`, and proper Python package structure will need to be created.
