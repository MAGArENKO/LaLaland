# Recent PR bug scan (repro-first)

This branch documents reproducible, high-confidence issues found in recent PRs and provides minimal patch files to apply on those PR branches.

## Reproduced issues

### PR #2 (`G-cursorcloud-agent-starter-skill-b0fb`)

1. Recovery CLI commands in the new skill do not exist in `main.py`:
   - Repro: `python main.py recovery list`
   - Result: `invalid choice: 'recovery'`
2. MCP command in the new skill does not exist in `main.py`:
   - Repro: `python main.py mcp start recovery`
   - Result: `invalid choice: 'mcp'`

Minimal fix: update skill instructions to match the actual command surface (`api`, `dashboard`, `pipeline`, `worker`, `beat`, `all`).

Patch: `proposed_fixes/pr2_skill_command_fixes.patch`

### PR #1 (`G-cursordevelopment-environment-setup-e796`)

1. Dependency mismatch warning at runtime:
   - Repro: `python -W default -c "import requests"`
   - Result: `RequestsDependencyWarning` due to `chardet (7.x)` installed while requests supports `<6`.
2. Python 3.12 deprecation warning in scraper model:
   - Repro:
     `python -W default -c "from scrapers.base import ScrapedItem,SourceType,ContentType; ScrapedItem(id='1',source_type=SourceType.LOCAL_FILESYSTEM,source_path='x',content='abc',content_type=ContentType.DATA)"`
   - Result: `DeprecationWarning` from `datetime.utcnow()`.

Minimal fixes:
- Pin `chardet` to `<6` in `requirements.txt`.
- Use timezone-aware UTC default (`datetime.now(UTC)`) in `scrapers/base.py`.

Patch: `proposed_fixes/pr1_runtime_warnings_fixes.patch`

## Apply notes

Apply each patch from the corresponding PR branch root:

- `git apply proposed_fixes/pr2_skill_command_fixes.patch`
- `git apply proposed_fixes/pr1_runtime_warnings_fixes.patch`
