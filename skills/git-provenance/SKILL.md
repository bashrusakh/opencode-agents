---
name: git-provenance
description: Use before repository mutation/publication when branch, worktree, base, upstream, PR-head identity, or current-target provenance matters. Root AGENTS.md remains authoritative.
---

# Git provenance

Use one repository-state/provenance contract for both mutation and publication. Resolve the actual head remote, base remote, base branch, and base ref from project guidance, tracking state, PR metadata, or repository metadata. Do not assume `origin/main` merely because the base is unknown. Keep state identity explicit through the workflow: inspect the intended ref/SHA, mutate only from the proven intended baseline, and bind verification/review/publication claims to the exact state they checked.

The workflow owner owns target freshness/state identity across a delegated workflow. A directly invoked role with no parent owns the applicable freshness step within its capabilities. Delegated leaves consume the caller-supplied authoritative target ref + fetched SHA and do not routinely refetch it; if that identity is absent or unknown, report the gap instead of silently substituting local HEAD/worktree.

For read-only claims about **current upstream/default/base code**, refreshing refs with `git fetch` is a freshness operation, not a working-tree update: fetch the resolved target remote and inspect the fetched ref/SHA directly. Do not `pull`, rebase, reset, checkout, or switch merely to answer a read-only current-state question.

Typical provenance evidence uses explicit resolved refs:

```bash
git status -sb
git branch -vv
git remote -v
git fetch --prune <head_remote>
git fetch --prune <base_remote>
git status -sb
git log --oneline --decorate <base_ref>..HEAD
git log --oneline --decorate --left-right --cherry-pick <base_ref>...HEAD
git diff --name-status <base_ref>...HEAD
git diff --stat <base_ref>...HEAD
```

Use normal `<base_ref>..HEAD` as the primary commit list. The `--cherry-pick` comparison is secondary and must not hide unexpected branch history. Example values such as `origin/main` are valid only when repository evidence proves them; never construct duplicated refs such as `origin/origin/main`.

## Mutation baseline checkpoint

Before the first repository edit, the workflow owner must establish the intended baseline, and the mutation-capable role must verify immediately before editing that its worktree represents that baseline: a fresh base for new work, or the explicitly authorized existing task/PR branch with a proven base relation.

If the branch is merely behind its intended upstream, `git pull --ff-only` may be used only when the worktree is clean, the upstream is the intended task/PR branch, project rules permit it, and section 4 plus the active role allow that branch/worktree update. If the update changes the effective diff/state, affected validation/review becomes stale.

For new independent work, the task branch must be clean relative to the resolved base unless the user explicitly authorized continuing the exact existing branch. If unrelated commits/files are present, branch creation/switch is allowed only when section 4 authorizes that branch mutation; otherwise stop. If the branch diverged, the worktree contains unrelated work, or recovery would rewrite published history, cause conflicts, or violate project rules, stop with the exact state and risk.

## Publication provenance checkpoint

Before commit, push, PR creation/update, or Ready transition, refresh the relevant refs and prove that the branch/effective diff contains only the commits and files intended for the normalized task. A PR is the complete base-to-head comparison, not the last commit. Record the current Base SHA and reconcile base/head drift before reusing evidence or publishing.

For a new independent task, do not publish from a branch that was already ahead of the resolved base before the task started. Recovery to a clean branch may reapply/cherry-pick only intended work when branch mutation is authorized. Force-push, reset, rebase of published history, branch replacement, and other history-rewriting recovery remain separately gated.

Before any commit, check status, review the full diff, include only intended files, run applicable checks, follow project commit/title rules, and exclude secrets, logs, local config, caches, benchmark outputs, and unrelated/generated artifacts. Before pushing, confirm the resolved remote, branch, base, commit range, and changed files; never force-push without the applicable gate.

Before PR creation/update, ensure the base is correct, the diff is reviewable for its current Draft/candidate stage, title/body reflect actual scope and validation, and relevant UI screenshots/manual verification are included when applicable. Owned PRs are created as Draft by default. Keep PR metadata synchronized with the actual commits, changed files, behavior, validation, and current Draft/Ready stage; before Ready it must describe the final candidate.
