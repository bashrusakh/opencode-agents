#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
BASE="$HOME/.config/opencode"
STATE="$BASE/.agent-pack"
RECEIPT="$STATE/managed-files.sha256"
BACKUP="$STATE/backups/$STAMP"
FORCE_ROOT="${OPENCODE_AGENT_PACK_REPLACE_GLOBAL_AGENTS:-0}"

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

manifest_hash_for() {
  local manifest="$1" rel="$2"
  awk -v p="$rel" 'substr($0,67)==p {print substr($0,1,64); exit}' "$manifest"
}

build_manifest() {
  local out="$1"
  : > "$out"
  printf '%s  %s\n' "$(sha256_file "$ROOT/AGENTS.md")" "AGENTS.md" >> "$out"
  while IFS= read -r -d '' src; do
    local rel="${src#"$ROOT/"}"
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
    if [ -e "$BASE/$dir/$name" ]; then
      printf 'Preserved ambiguous legacy path (filename is not ownership proof): %s/%s\n' "$dir" "$name" >&2
    fi
  done
}

# Preflight must finish before any mutation.
if [ -f "$BASE/AGENTS.md" ] && ! is_pack_root "$BASE/AGENTS.md" && [ "$FORCE_ROOT" != "1" ]; then
  cat >&2 <<'MSG'
Refusing to replace an existing global ~/.config/opencode/AGENTS.md that is not recognizable as an earlier OpenCode Agent Pack root.
No files were changed. Preserve your global rules, merge/import them deliberately, or rerun with OPENCODE_AGENT_PACK_REPLACE_GLOBAL_AGENTS=1 to explicitly authorize replacement (a backup will be kept).
MSG
  exit 2
fi

mkdir -p "$BASE/agents" "$BASE/skills" "$STATE"
NEW_MANIFEST="$(mktemp)"
trap 'rm -f "$NEW_MANIFEST"' EXIT
build_manifest "$NEW_MANIFEST"

# A receipt proves prior package ownership. Unknown legacy names are preserved and warned.
cleanup_stale_managed "$RECEIPT" "$NEW_MANIFEST"
warn_ambiguous_legacy agents "${OLD_AGENTS[@]}"
warn_ambiguous_legacy commands "${OLD_COMMANDS[@]}"
warn_ambiguous_legacy docs "${OLD_DOCS[@]}"
warn_ambiguous_legacy snippet "${OLD_SNIPPETS[@]}"
warn_ambiguous_legacy tools "${OLD_TOOLS[@]}"

# Back up every colliding destination before replacement.
backup_rel "AGENTS.md"
while IFS= read -r -d '' src; do
  rel="${src#"$ROOT/"}"
  backup_rel "$rel"
  mkdir -p "$BASE/$(dirname "$rel")"
  cp -a "$src" "$BASE/$rel"
done < <(find "$ROOT/agents" "$ROOT/skills" -type f -print0)
cp -a "$ROOT/AGENTS.md" "$BASE/AGENTS.md"

cp "$NEW_MANIFEST" "$RECEIPT"
printf 'pack_version=v30.80 beta\ninstalled_at=%s\n' "$STAMP" > "$STATE/install-info"

echo "Installed agents to ~/.config/opencode/agents"
echo "Installed skills to ~/.config/opencode/skills"
echo "Installed root AGENTS.md to ~/.config/opencode/AGENTS.md"
if [ -d "$BACKUP" ]; then echo "Backed up replaced/stale managed files under $BACKUP"; fi
echo "Ambiguous legacy command/doc/tool filenames are preserved unless a prior package receipt proves ownership."
echo "Agents are model-agnostic: use the active OpenCode/OpenChamber model/provider from your current config/UI."
