#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$HOME/.config/opencode/agents" "$HOME/.config/opencode/commands"
cp "$ROOT/agents/"*.md "$HOME/.config/opencode/agents/"
cp "$ROOT/commands/"*.md "$HOME/.config/opencode/commands/"
echo "Installed agents to ~/.config/opencode/agents"
echo "Installed commands to ~/.config/opencode/commands"
echo "Copy global/AGENTS.md manually to the global/location you use for OpenCode rules, or into each project root as AGENTS.md."
echo "Then run /models in OpenCode and verify model IDs."
