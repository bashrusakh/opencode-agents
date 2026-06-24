# Git Branch Provenance Policy

This policy prevents agents from accidentally pulling unrelated commits/files into PRs.

## Core invariant

A PR is the full diff from base branch to head branch, not the agent's last commit. Before commit, push, PR creation, or PR update, the agent must prove the branch contains only intended work for the normalized task.

## Pre-edit sync

Before editing code/config/docs in a repository:

```bash
git status --short
git branch --show-current
git fetch origin <base>
git log --oneline --decorate --left-right --cherry-pick origin/<base>...HEAD
git diff --name-status origin/<base>...HEAD
```

Use the project-local base or active PR base. Default to `origin/main` only when no other base is known.

If the branch is behind the base, rebase/update before editing when the working tree is clean and the operation is safe. If rebase/update would rewrite published history, conflict, include unrelated commits, or violate project rules, stop and ask.

## Pre-PR provenance

Before commit, push, PR creation, or PR update:

```bash
git status --short
git branch --show-current
git fetch origin <base>
git log --oneline --decorate --left-right --cherry-pick origin/<base>...HEAD
git diff --name-status origin/<base>...HEAD
git diff --stat origin/<base>...HEAD
```

Stop if the range contains unrelated commits, unrelated files, another issue/PR's work, unexpected generated artifacts, or stale branch history.

## Clean recovery

Allowed recovery:

1. Create a clean branch from the current base.
2. Cherry-pick or re-apply only intended work.
3. Re-run the provenance gate.
4. Continue only when commit range and changed files match the normalized task.

Force-push, reset, rebase of a published branch, or replacing a PR branch is gated and requires explicit approval after the risk is stated.

## Report format

```md
### Branch provenance

- Base: `origin/<base> @ <sha>`
- Branch: `<branch>`
- Commits ahead of base: `<N>`
- Intended commits: `<list>`
- Unrelated commits: none / `<list>`
- Changed files reviewed: yes/no
- Unrelated files: none / `<list>`
- Safe to commit/push/PR: yes/no
```
