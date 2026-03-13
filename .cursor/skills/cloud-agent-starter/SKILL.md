# Cloud Agent Starter Skill: Run + Test Playbook

Use this skill when you need to get productive in this codebase quickly (setup, auth, running services, feature/source toggles, and smoke tests).

## 0) Fast setup checklist (first 5 minutes)

1. Verify repo and Python env:
   - `pwd`
   - `python --version`
2. Create/activate venv:
   - `python -m venv .venv`
   - `source .venv/bin/activate`
3. Install deps (if project files are present):
   - `pip install -r requirements.txt`
4. Bring up infra:
   - `docker-compose up -d`
5. Confirm auth/session requirements:
   - `gh auth status` (GitHub access)
   - Ensure `.env` contains required keys/tokens for enabled integrations.

## 1) Login + auth runbook

### Required logins
- **GitHub**: required when `github` source is enabled in `config/sources.yaml`.
- **Model/API providers**: fill keys in `.env` (for example OpenAI/DeepSeek/Serper).
- **Argilla**: defaults in docs use `http://localhost:6900` and `admin.apikey`.
- **Browser-backed sources (LM Arena)**: run scraper from a profile/session that is already authenticated.

### Quick auth validation
- `gh auth status`
- `python -c "import os; print('OPENAI_API_KEY set:', bool(os.getenv('OPENAI_API_KEY')))"` (repeat for keys you need)
- `curl -sf http://localhost:6900 >/dev/null && echo argilla_ok || echo argilla_down`

## 2) Environment config + source flags (mocking external deps)

Treat `config/sources.yaml` `enabled: true/false` switches as feature flags for source integrations.

### Safe local-only mode (recommended for Cloud agents)
Disable remote/external inputs first, then run deterministic local tests:
- Set `sources.github.enabled: false`
- Set `sources.lmarena.enabled: false` (unless authenticated browser/session is available)
- Keep a single filesystem/local source enabled for smoke testing.

### Minimal `.env` guidance
Keep only what your test path needs:
- DB / vector / queue endpoints
- Optional provider keys for enabled integrations
- Log verbosity (`LOG_LEVEL=INFO` or `DEBUG` during investigations)

## 3) Area-based execution + test workflows

## Area A: Recovery CLI + pipeline (`main.py`, `recovery/`)

### Run
- `python main.py recovery list`
- `python main.py recovery source <name>`
- `python main.py recovery full`

### Test workflow (high-signal)
1. Run `python main.py recovery list` and confirm expected enabled/disabled sources.
2. Run one source only: `python main.py recovery source local` (or another enabled source).
3. Validate output artifacts/log updates under expected data/log paths.
4. Only then run `python main.py recovery full`.

### Failure triage
- If source fails auth -> disable source and re-run local-only path.
- If infra connection fails -> verify Docker services and `.env` endpoints match.

## Area B: API service (`api/`, CLI `python main.py api`)

### Run
- `python main.py api`

### Test workflow
1. Start API.
2. In another shell, run:
   - `curl -i http://localhost:8000/`
   - `curl -i http://localhost:8000/docs`
3. Call one recovery/search endpoint used by this repo and verify non-500 response.

## Area C: Dashboard/UI (`ui/dashboard.py`, CLI `python main.py dashboard`)

### Run
- `python main.py dashboard`

### Test workflow
1. Confirm server process starts on port 8501.
2. `curl -I http://localhost:8501` to validate service availability.
3. If doing UI changes, manually verify core page loads and one end-to-end action (search or recovery trigger).

## Area D: MCP servers (`mcp/servers/`, CLI `python main.py mcp start <server>`)

### Run
- `python main.py mcp start recovery`
- `python main.py mcp start vfx` (or other configured server)

### Test workflow
1. Start one MCP server only.
2. Verify process is live and expected port is bound.
3. Exercise one representative MCP tool/action from that server.

## Area E: Scripts + workflows (`scripts/`, `workflows/`)

### Run
- `python scripts/run_recovery.py` (if present)
- Run targeted helper script for the workflow you changed.

### Test workflow
1. Execute the specific script you modified.
2. Verify generated file(s) under data/workflow output path.
3. Re-run once to confirm idempotent or expected overwrite behavior.

## 4) Cloud-agent execution sequence (default)

Use this order unless the task says otherwise:

1. Setup env + dependencies.
2. Start infra (`docker-compose up -d`).
3. Toggle source flags for a deterministic test path.
4. Run one source-level smoke test.
5. Start API/dashboard only if needed for the task.
6. Expand to full pipeline after smoke tests pass.

## 5) “No surprises” checklist before finishing

- Only required sources are enabled.
- External integrations are either authenticated or explicitly disabled.
- At least one source run + one service health check completed.
- Logs/errors captured with actionable messages.

## 6) Keep this skill fresh (update loop)

Whenever you discover new runbook knowledge, update this skill immediately:

1. Add one concise note under the relevant area:
   - new prerequisite
   - new failure mode + fix
   - faster smoke-test command
2. Prefer concrete commands over prose.
3. Remove stale steps that no longer match current commands/paths.
4. Keep each area to “minimum steps to run + verify.”

Definition of done for skill updates:
- Another Cloud agent can start from zero and reach a passing smoke test without guesswork.
