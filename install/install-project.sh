#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
mkdir -p .opencode/agents .opencode/skills

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

if [ -f ./AGENTS.md ]; then
  cp ./AGENTS.md "./AGENTS.md.bak.$STAMP"
fi
for d in agents skills; do
  if [ -d ".opencode/$d" ]; then
    mkdir -p ".opencode/$d.bak.$STAMP"
    cp -a ".opencode/$d/." ".opencode/$d.bak.$STAMP/" 2>/dev/null || true
  fi
done

# Back up and remove only obsolete package-owned runtime filenames; never disturb unrelated project files.
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

backup_and_remove ".opencode/commands" ".opencode/commands.bak.$STAMP" "${OLD_COMMANDS[@]}"
backup_and_remove ".opencode/docs" ".opencode/docs.bak.$STAMP" "${OLD_DOCS[@]}"
backup_and_remove ".opencode/snippet" ".opencode/snippet.bak.$STAMP" "${OLD_SNIPPETS[@]}"
rmdir ".opencode/snippet" 2>/dev/null || true

cp "$ROOT/AGENTS.md" ./AGENTS.md
cp "$ROOT/agents/"*.md .opencode/agents/
if [ -d "$ROOT/skills" ]; then cp -a "$ROOT/skills/." .opencode/skills/; fi

printf 'Installed project-local OpenCode agents/skills and AGENTS.md into %s\n' "$(pwd)"
echo "Backups were created for existing package-owned/runtime surfaces when present."
echo "Obsolete package-owned command/doc/snippet paths were removed after backup; unrelated project files were left untouched."
