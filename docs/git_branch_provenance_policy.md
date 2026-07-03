# Git Branch Provenance Policy

This policy prevents agents from editing stale PR branches or publishing unrelated commits/files.

## Core invariant

A PR is the full diff from base branch to head branch, not the agent's last commit. Before mutation/publication, the agent must prove the local branch is current enough to edit and the branch contains only intended work for the normalized task.

Use explicit refs:

```text
<base_remote> = origin
<base_branch> = main
<base_ref>    = origin/main
```

Do not build ambiguous refs such as `origin/origin/main`.

## Pre-edit sync

Before editing code/config/docs in a repository mutation workflow:

```bash
git status -sb
git branch -vv
git remote -v
git fetch --prune <head_remote>
git fetch --prune <base_remote>
git status -sb
git log --oneline --decorate <base_ref>..HEAD
git diff --name-status <base_ref>...HEAD
```

If the current branch tracks an upstream branch and is behind it, fast-forward/update before editing only when the working tree is clean and the operation is safe.

Stop and ask if the branch diverged from upstream, the update/rebase would rewrite published history, conflicts appear, unrelated commits/files are present, or project rules forbid the operation.

Read-only review/audit does not need to update or rebase branches unless it is preparing mutation or publication.

## Pre-publication provenance

Before commit, push, PR creation, or PR update:

```bash
git status -sb
git branch -vv
git fetch --prune <head_remote>
git fetch --prune <base_remote>
git log --oneline --decorate <base_ref>..HEAD
git log --oneline --decorate --left-right --cherry-pick <base_ref>...HEAD
git diff --name-status <base_ref>...HEAD
git diff --stat <base_ref>...HEAD
```

The primary commit list is `<base_ref>..HEAD`. The `--cherry-pick` comparison is secondary and must not hide unexpected branch history.

Stop if the range contains unrelated commits, unrelated files, another issue/PR's work, unexpected generated artifacts, stale local branch state, or branch divergence from upstream.

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
- Base: `<base_ref> @ <sha>`
- Branch: `<branch>`
- Upstream: `<upstream or none>`
- Branch state: `<current | behind | ahead | diverged | unknown>`
- Commits ahead of base: `<N>`
- Unrelated commits/files: `no | yes`
- Safe to edit/commit/push/PR: `yes | no`
```
