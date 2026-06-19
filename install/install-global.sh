#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$HOME/.config/opencode/agents" "$HOME/.config/opencode/commands" "$HOME/.config/opencode/docs"
cp "$ROOT/agents/"*.md "$HOME/.config/opencode/agents/"
cp "$ROOT/commands/"*.md "$HOME/.config/opencode/commands/"
cp "$ROOT/docs/"*.md "$HOME/.config/opencode/docs/"
if [ -f "$HOME/.config/opencode/AGENTS.md" ]; then
  cp "$HOME/.config/opencode/AGENTS.md" "$HOME/.config/opencode/AGENTS.md.bak.$(date +%Y%m%d-%H%M%S)"
fi
cp "$ROOT/AGENTS.md" "$HOME/.config/opencode/AGENTS.md"
echo "Installed agents to ~/.config/opencode/agents"
echo "Installed commands to ~/.config/opencode/commands"
echo "Installed docs to ~/.config/opencode/docs"
echo "Installed root AGENTS.md to ~/.config/opencode/AGENTS.md"
echo "A backup was created if ~/.config/opencode/AGENTS.md already existed."
echo "Then run /models in OpenCode and verify model IDs."

echo "UUPM setup instructions are in ~/.config/opencode/docs/UUPM_INSTALL_FOR_AGENT.md"
