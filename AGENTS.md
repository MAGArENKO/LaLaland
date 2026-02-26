# AGENTS.md

## Cursor Cloud specific instructions

### Repository State

This repository is in a **planning/ideation phase**. It contains no runnable application code, no dependency manifests, no build system, and no automated tests. The two files are:

- `README.md` — A ~17,600-line brainstorm/conversation log describing an aspirational AI-powered 3D creative pipeline (Cursor IDE + ComfyUI + Krita + OpenUSD + Blender).
- `python -m venv venv` — A misnamed file (the filename is the command itself) containing 3 lines of shell setup commands. This is not an executable script.

### Key Facts

- **No services to run.** There are no backend servers, frontends, databases, or other services.
- **No dependencies to install.** There are no `requirements.txt`, `package.json`, `pyproject.toml`, or other dependency manifests.
- **No lint/test/build commands.** There are no linters, test suites, or build scripts configured.
- **No Docker configuration.** Despite references in the README, no `Dockerfile` or `docker-compose.yml` exists.
- The README contains many Python code snippets (using `pxr`/OpenUSD, `bpy`/Blender, `requests`, etc.) but none exist as actual source files.

### For Future Agents

If source code is added to this repository in the future, update this section with:
- How to install dependencies
- How to run lint, tests, and the application
- Any non-obvious setup caveats
