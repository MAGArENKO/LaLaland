#!/usr/bin/env bash
set -euo pipefail

# voice-control.sh
# Text/voice bridge for cagent.
#
# Usage:
#   ./voice-control.sh
#   ./voice-control.sh agents-integrators.yml
#
# You can pipe transcribed speech lines into this script.
# Each non-empty line is wrapped as [VOICE] ... and sent to cagent.

AGENTS_FILE="${1:-agents.yml}"

if ! command -v cagent >/dev/null 2>&1; then
  echo "Error: cagent is not installed or not in PATH." >&2
  exit 1
fi

if [[ ! -f "${AGENTS_FILE}" ]]; then
  echo "Error: agent config file not found: ${AGENTS_FILE}" >&2
  exit 1
fi

echo "Listening for voice text lines. Press Ctrl+C to stop."
echo "Using config: ${AGENTS_FILE}"
echo

while IFS= read -r line; do
  # Trim leading/trailing whitespace.
  trimmed="${line#"${line%%[![:space:]]*}"}"
  trimmed="${trimmed%"${trimmed##*[![:space:]]}"}"

  if [[ -z "${trimmed}" ]]; then
    continue
  fi

  echo "You said: ${trimmed}"
  printf '[VOICE] %s\n' "${trimmed}" | cagent run "${AGENTS_FILE}" --input -
done
