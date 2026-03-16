# Autonomous Multi-Agent System with Voice Control

This repository now includes a complete multi-agent command configuration with optional platform integrators and a voice command bridge.

## Files

- `agents.yml` - Core autonomous agent army (command center + 13 specialists + voice interface).
- `agents-integrators.yml` - Extension config with Azure, GitHub, Hugging Face, and GitKraken integrators.
- `voice-control.sh` - Wrapper script that turns input lines into `[VOICE]` commands for `cagent`.
- `.cagent/logs/` - Log directory scaffold.

## Quick Start

Run the core agent army:

`cagent run agents.yml`

Run with a specific starting agent:

`cagent run agents.yml --agent architect`

Run with voice-style input:

`echo "[VOICE] fix the broken tests" | cagent run agents.yml --input -`

Run in production mode:

`CAGENT_ENV=production cagent run agents.yml`

Run in autonomous mode:

`cagent run agents.yml --auto-approve`

Run with verbose output:

`cagent run agents.yml --verbose`

## Integrator Mode

Use the extended config:

`cagent run agents-integrators.yml`

Example shortcuts this config supports:

- "deploy to azure"
- "create a PR"
- "train the model"
- "show me the graph"
- "check my PRs"

## Voice Control Script

Make executable once:

`chmod +x voice-control.sh`

Start listening from stdin:

`./voice-control.sh`

Use extended config:

`./voice-control.sh agents-integrators.yml`

## Example Voice Commands

- "status" -> git status + test status + build status
- "ship it" -> tests -> commit -> push -> deploy
- "what's broken" -> run tests and report failures
- "fix the login bug" -> debug -> fix -> test
- "is this secure" -> security audit flow
- "make it faster" -> profile -> optimize -> verify

## Environment Variables (Typical)

Azure:

- `AZURE_SUBSCRIPTION_ID`
- `AZURE_TENANT_ID`
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`

GitHub:

- `GITHUB_TOKEN`

Hugging Face:

- `HF_TOKEN`

GitKraken:

- `GITKRAKEN_TOKEN`

Model providers:

- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`

## Notes

- Keep secrets in environment variables or a secret manager.
- Avoid destructive commands without explicit confirmation.
- Validate deployment and rollback paths before production operations.
