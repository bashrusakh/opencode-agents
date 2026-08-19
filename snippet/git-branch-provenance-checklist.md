# Git Branch Provenance Checklist

Use before editing, committing, pushing, opening a PR, or updating an existing PR.

Use explicit refs such as `<base_remote>=origin`, `<base_branch>=main`, `<base_ref>=origin/main`.

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

If the current branch tracks upstream and is behind it, update before editing only by safe fast-forward:

```bash
git pull --ff-only
```

For a new independent task, `<base_ref>..HEAD` and `<base_ref>...HEAD` must be empty before edits. If not, stop and create a clean branch from `<base_ref>`.

For an existing PR follow-up, ahead commits/files are allowed only when they belong to that same PR/task.

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

If remote head changed or local branch is behind, use `git pull --ff-only` only when safe, then re-run validation and provenance. If the branch diverged or unrelated work appears, stop and ask.

Expected report:

- Base ref
- Current branch
- Upstream tracking branch
- Branch state: current / behind / ahead / diverged / unknown
- Task branch: new clean / existing PR / user-approved / unsafe
- Commits ahead of base
- Changed files
- Unrelated commits/files: yes/no
- Safe to edit/commit/push/PR: yes/no

## PR body sync

After the final intended diff and validation, verify that the PR title/body still match actual commits, changed files, scope, behavior, and validation. If stale, update it when PR update is already allowed; otherwise draft the corrected body and ask.

Final report line:

```text
PR body: updated | unchanged | drafted | skipped — <reason>
```

Remember: a PR is the whole base-to-head diff, not just the last commit.
