#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
BASE="$HOME/.config/opencode"
mkdir -p "$BASE/agents" "$BASE/skills"

OLD_COMMANDS=(
  audit.md bug-issue.md bugfix.md code-explore.md debug.md devops-check.md execute-plan.md plan.md
  pr-followup.md pr-provenance.md release-prep.md review.md ui-a11y-check.md ui-audit.md ui-implement.md
  ui-options.md ui-plan.md ui-redesign.md verify.md ui-mcp-setup.md ui-uupm-setup.md
)
OLD_DOCS=(
  auditor_agent.md git_branch_provenance_policy.md language_spec.md ocr_review_policy.md
  output_formatting_policy.md persistent_planning_policy.md pr_readiness.md ui_component_policy.md
  verification_strategy.md ui_mcp_install_for_agent.md uupm_install_for_agent.md
)

OLD_SNIPPETS=(
  audit-long-running-prompt.md components-json-default-registry-note.md git-branch-provenance-checklist.md
  open-code-review-usage.md opencode-ui-mcp.example.jsonc plan-layout.md ui-uupm-usage.md
)

backup_and_remove() {
  local dir="$1" backup="$2"; shift 2
  local name found=0
  for name in "$@"; do
    if [ -e "$dir/$name" ]; then
      if [ "$found" -eq 0 ]; then mkdir -p "$backup"; found=1; fi
      cp -a "$dir/$name" "$backup/$name"
      rm -f "$dir/$name"
    fi
  done
}

backup_and_remove "$BASE/commands" "$BASE/commands.bak.$STAMP" "${OLD_COMMANDS[@]}"
backup_and_remove "$BASE/docs" "$BASE/docs.bak.$STAMP" "${OLD_DOCS[@]}"
backup_and_remove "$BASE/snippet" "$BASE/snippet.bak.$STAMP" "${OLD_SNIPPETS[@]}"
rmdir "$BASE/snippet" 2>/dev/null || true

cp "$ROOT/agents/"*.md "$BASE/agents/"
if [ -d "$ROOT/skills" ]; then cp -a "$ROOT/skills/." "$BASE/skills/"; fi
if [ -f "$BASE/AGENTS.md" ]; then
  cp "$BASE/AGENTS.md" "$BASE/AGENTS.md.bak.$STAMP"
fi
cp "$ROOT/AGENTS.md" "$BASE/AGENTS.md"

echo "Installed agents to ~/.config/opencode/agents"
echo "Installed skills to ~/.config/opencode/skills"
echo "Installed root AGENTS.md to ~/.config/opencode/AGENTS.md"
echo "Obsolete package-owned command/doc/snippet filenames were backed up and removed when present."
echo "Agents are model-agnostic: use the active OpenCode/OpenChamber model/provider from your current config/UI."
