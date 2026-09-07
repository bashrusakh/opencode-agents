# Git Branch Provenance Checklist

Use the active root policy and `docs/git_branch_provenance_policy.md`. Resolve actual refs from repository/PR evidence; do not assume `origin/main`.

Example only:

```text
<base_remote>=origin
<base_branch>=main
<base_ref>=origin/main
```

## Pre-edit

```bash
git status -sb
git branch -vv
git remote -v
git fetch --prune <head_remote>
git fetch --prune <base_remote>
git status -sb
git log --oneline --decorate <base_ref>..HEAD
git diff --name-status <base_ref>...HEAD
git diff --stat <base_ref>...HEAD
```

If the intended task/PR branch is merely behind its upstream and the worktree is clean, update only with:

```bash
git pull --ff-only
```

For new independent work, do not inherit unrelated ahead commits/files. For existing PR follow-up, ahead commits/files must belong to that same PR/task. Branch creation/recovery/history operations remain subject to the root authorization gate.

## Pre-publication

```bash
git status -sb
git branch -vv
git fetch --prune <head_remote>
git fetch --prune <base_remote>
git status -sb
git log --oneline --decorate <base_ref>..HEAD
git log --oneline --decorate --left-right --cherry-pick <base_ref>...HEAD
git diff --name-status <base_ref>...HEAD
git diff --stat <base_ref>...HEAD
```

Use `<base_ref>..HEAD` as the primary commit list. If effective branch/diff state changes, re-run affected validation/review/readiness. If the branch diverged or unrelated work appears, stop before publication.

Remember: a PR is the whole base-to-head comparison, not the last commit.
