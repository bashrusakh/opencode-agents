#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
BASE="$(pwd)"
RUNTIME="$BASE/.opencode"
STATE="$RUNTIME/.agent-pack"
RECEIPT="$STATE/managed-files.sha256"
BACKUP="$STATE/backups/$STAMP"
GLOBAL_ROOT="$HOME/.config/opencode/AGENTS.md"

OLD_AGENTS=(plan.md)
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
OLD_TOOLS=(session_trace.js)

sha256_file() {
  if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | awk '{print $1}'
  else shasum -a 256 "$1" | awk '{print $1}'
  fi
}

is_pack_root() {
  local file="$1"
  [ -f "$file" ] || return 1
  grep -q '^# OpenCode Agent Rules$' "$file" && grep -q '^\*\*Pack version: v30\.' "$file"
}

backup_rel() {
  local rel="$1"
  [ -e "$BASE/$rel" ] || return 0
  mkdir -p "$BACKUP/$(dirname "$rel")"
  cp -a "$BASE/$rel" "$BACKUP/$rel"
}

manifest_has_path() {
  local manifest="$1" rel="$2"
  [ -f "$manifest" ] && awk -v p="$rel" 'substr($0,67)==p {found=1} END{exit !found}' "$manifest"
}

build_manifest() {
  local out="$1" include_root="$2"
  : > "$out"
  if [ "$include_root" = "1" ]; then
    printf '%s  %s\n' "$(sha256_file "$ROOT/AGENTS.md")" "AGENTS.md" >> "$out"
  fi
  while IFS= read -r -d '' src; do
    local sub rel
    sub="${src#"$ROOT/"}"
    rel=".opencode/$sub"
    printf '%s  %s\n' "$(sha256_file "$src")" "$rel" >> "$out"
  done < <(find "$ROOT/agents" "$ROOT/skills" -type f -print0)
}

cleanup_stale_managed() {
  local old="$1" new="$2" line hash rel current
  [ -f "$old" ] || return 0
  while IFS= read -r line; do
    [ ${#line} -ge 67 ] || continue
    hash="${line:0:64}"; rel="${line:66}"
    manifest_has_path "$new" "$rel" && continue
    [ -f "$BASE/$rel" ] || continue
    current="$(sha256_file "$BASE/$rel")"
    if [ "$current" = "$hash" ]; then
      backup_rel "$rel"
      rm -f "$BASE/$rel"
      printf 'Removed stale pack-owned file: %s\n' "$rel"
    else
      printf 'Preserved modified stale managed file: %s\n' "$rel" >&2
    fi
  done < "$old"
}

warn_ambiguous_legacy() {
  local dir="$1"; shift
  local name
  for name in "$@"; do
    if [ -e "$RUNTIME/$dir/$name" ]; then
      printf 'Preserved ambiguous legacy path (filename is not ownership proof): .opencode/%s/%s\n' "$dir" "$name" >&2
    fi
  done
}

# Determine AGENTS.md ownership before mutating anything.
INSTALL_PROJECT_ROOT=0
if [ ! -f "$BASE/AGENTS.md" ]; then
  INSTALL_PROJECT_ROOT=1
elif is_pack_root "$BASE/AGENTS.md"; then
  INSTALL_PROJECT_ROOT=1
elif ! is_pack_root "$GLOBAL_ROOT"; then
  cat >&2 <<'MSG'
Refusing project-local installation because this repository already has a project-owned ./AGENTS.md and no recognizable global OpenCode Agent Pack root is installed.
No files were changed. The project AGENTS.md is authoritative and will not be replaced. Install the pack globally first, then rerun this project installer to add only project-local agents/skills.
MSG
  exit 2
fi

mkdir -p "$RUNTIME/agents" "$RUNTIME/skills" "$STATE"
NEW_MANIFEST="$(mktemp)"
trap 'rm -f "$NEW_MANIFEST"' EXIT
build_manifest "$NEW_MANIFEST" "$INSTALL_PROJECT_ROOT"

cleanup_stale_managed "$RECEIPT" "$NEW_MANIFEST"
warn_ambiguous_legacy agents "${OLD_AGENTS[@]}"
warn_ambiguous_legacy commands "${OLD_COMMANDS[@]}"
warn_ambiguous_legacy docs "${OLD_DOCS[@]}"
warn_ambiguous_legacy snippet "${OLD_SNIPPETS[@]}"
warn_ambiguous_legacy tools "${OLD_TOOLS[@]}"

while IFS= read -r -d '' src; do
  sub="${src#"$ROOT/"}"
  rel=".opencode/$sub"
  backup_rel "$rel"
  mkdir -p "$BASE/$(dirname "$rel")"
  cp -a "$src" "$BASE/$rel"
done < <(find "$ROOT/agents" "$ROOT/skills" -type f -print0)

if [ "$INSTALL_PROJECT_ROOT" = "1" ]; then
  backup_rel "AGENTS.md"
  cp -a "$ROOT/AGENTS.md" "$BASE/AGENTS.md"
  echo "Installed/updated pack-owned project AGENTS.md"
else
  echo "Preserved existing project-owned AGENTS.md; shared pack policy is supplied by the recognizable global pack root."
fi

cp "$NEW_MANIFEST" "$RECEIPT"
printf 'pack_version=v30.86 beta\ninstalled_at=%s\n' "$STAMP" > "$STATE/install-info"

echo "Installed project-local OpenCode agents/skills into $BASE/.opencode"
if [ -d "$BACKUP" ]; then echo "Backed up replaced/stale managed files under $BACKUP"; fi
echo "Ambiguous legacy command/doc/tool filenames are preserved unless a prior package receipt proves ownership."
