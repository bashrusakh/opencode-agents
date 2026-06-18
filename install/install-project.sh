#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p .opencode/agents .opencode/commands
cp "$ROOT/agents/"*.md .opencode/agents/
cp "$ROOT/commands/"*.md .opencode/commands/
cp "$ROOT/global/AGENTS.md" ./AGENTS.md
printf 'Installed project-local OpenCode agents/commands and AGENTS.md into %s\n' "$(pwd)"
