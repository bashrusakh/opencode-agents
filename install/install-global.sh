#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$HOME/.config/opencode/agents" "$HOME/.config/opencode/commands" "$HOME/.config/opencode/docs" "$HOME/.config/opencode/snippet" "$HOME/.config/opencode/skills"
cp "$ROOT/agents/"*.md "$HOME/.config/opencode/agents/"
cp "$ROOT/commands/"*.md "$HOME/.config/opencode/commands/"
cp "$ROOT/docs/"*.md "$HOME/.config/opencode/docs/"
if [ -d "$ROOT/skills" ]; then cp -a "$ROOT/skills/." "$HOME/.config/opencode/skills/"; fi
if [ -d "$ROOT/snippet" ]; then cp "$ROOT/snippet/"* "$HOME/.config/opencode/snippet/" 2>/dev/null || true; fi
if [ -f "$HOME/.config/opencode/AGENTS.md" ]; then
  cp "$HOME/.config/opencode/AGENTS.md" "$HOME/.config/opencode/AGENTS.md.bak.$(date +%Y%m%d-%H%M%S)"
fi
cp "$ROOT/AGENTS.md" "$HOME/.config/opencode/AGENTS.md"
echo "Installed agents to ~/.config/opencode/agents"
echo "Installed commands to ~/.config/opencode/commands"
echo "Installed docs to ~/.config/opencode/docs"
echo "Installed skills to ~/.config/opencode/skills"
echo "Installed snippet files to ~/.config/opencode/snippet"
echo "Installed root AGENTS.md to ~/.config/opencode/AGENTS.md"
echo "A backup was created if ~/.config/opencode/AGENTS.md already existed."
echo "Agents are model-agnostic: use the active OpenCode/OpenChamber model/provider from your current config/UI."

echo "UUPM setup instructions are in ~/.config/opencode/docs/uupm_install_for_agent.md"
