# Drive Enhancement Scan (Argilla/Ollama/Docker/Agent Training)

Use `scripts/drive_enhancement_scan.py` to crawl large local folders or full Windows drives and generate:

- A detailed JSON report with keyword hits and project profiling.
- A Markdown summary of enhancement opportunities and development directions.

## What it scans for

Default keywords include:

- `argilla` and `agrilla` (misspelling-safe)
- `ollama`
- `docker`, `docker-compose`
- `server`, `fastapi`, `celery`, `mcp`
- `agent`, `training`, `dataset`

It also detects project roots by common markers (`pyproject.toml`, `requirements.txt`, `package.json`, `Dockerfile`, compose files, `.git`) and creates project-level recommendations.

## Windows examples

Scan specific roots:

- `python scripts/drive_enhancement_scan.py --roots "D:\mamaAIxants" "D:\genesis sytem" "D:\automaticantsXmamaai" "D:\projectXXX"`

Scan all detected drives automatically:

- `python scripts/drive_enhancement_scan.py`

Scan with extra domain terms:

- `python scripts/drive_enhancement_scan.py --roots "D:\" --keyword "distilabel" --keyword "huggingface" --keyword "training grounds"`

## Performance/safety options

- `--max-file-size-mb` (default `2.0`): ignore very large files for content scanning.
- `--max-files-per-root` (default `300000`): traversal cap per root.
- `--max-hits` (default `5000`): cap hit records in output.
- `--output-dir` (default `reports`): where reports are written.

## Output

Reports are written to:

- `reports/drive_enhancement_scan_<timestamp>.json`
- `reports/drive_enhancement_scan_<timestamp>.md`

The Markdown output is the fast executive summary; JSON is for deeper automation and follow-up analysis.
