#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
mkdir -p .opencode/agents .opencode/commands .opencode/docs

if [ -f ./AGENTS.md ]; then
  cp ./AGENTS.md "./AGENTS.md.bak.$STAMP"
fi
if [ -d .opencode/agents ]; then
  mkdir -p ".opencode/agents.bak.$STAMP"
  cp -a .opencode/agents/. ".opencode/agents.bak.$STAMP/" 2>/dev/null || true
fi
if [ -d .opencode/commands ]; then
  mkdir -p ".opencode/commands.bak.$STAMP"
  cp -a .opencode/commands/. ".opencode/commands.bak.$STAMP/" 2>/dev/null || true
fi
if [ -d .opencode/docs ]; then
  mkdir -p ".opencode/docs.bak.$STAMP"
  cp -a .opencode/docs/. ".opencode/docs.bak.$STAMP/" 2>/dev/null || true
fi

cp "$ROOT/AGENTS.md" ./AGENTS.md
cp "$ROOT/agents/"*.md .opencode/agents/
cp "$ROOT/commands/"*.md .opencode/commands/
cp "$ROOT/docs/"*.md .opencode/docs/

printf 'Installed project-local OpenCode agents/commands/docs and AGENTS.md into %s\n' "$(pwd)"
echo "Backups were created when existing files/directories were present."
echo "UUPM setup instructions are in .opencode/docs/UUPM_INSTALL_FOR_AGENT.md"
