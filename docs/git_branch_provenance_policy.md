# Git Branch Provenance Policy

This policy prevents agents from editing stale PR branches, fixing on polluted branches, or publishing unrelated commits/files.

## Core invariant

A PR is the full diff from base branch to head branch, not the agent's last commit.

Before mutation or publication, the active primary/orchestrator must prove two things:

1. the local branch is current enough to edit;
2. the branch belongs to the normalized task and contains only intended work.

Use explicit refs:

```text
<base_remote> = origin
<base_branch> = main
<base_ref>    = origin/main
```

Do not build ambiguous refs such as `origin/origin/main`.

## Branch safety classes

A branch is safe for mutation only when one of these is true:

- it was created fresh from the current `<base_ref>` for this task;
- it is the existing PR branch for the PR explicitly being updated;
- the user explicitly approved continuing this exact branch.

For a new independent task, `<base_ref>..HEAD` and `<base_ref>...HEAD` must be empty before edits. If they are not empty, the branch already contains previous work and is unsafe for a new bugfix.

For an existing PR follow-up, commits/files ahead of `<base_ref>` may exist, but they must belong to that same PR/task.

## Pre-edit branch sync and clean-task gate

Before editing code/config/docs in a mutation workflow:

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

If the current branch tracks an upstream branch and is behind it, update before editing only by safe fast-forward:

```bash
git pull --ff-only
```

Use `git pull --ff-only` only when the working tree is clean and the upstream branch is the intended current PR/task branch.

Stop and ask if:

- the working tree is dirty with changes not proven to belong to the current task;
- the branch diverged from upstream;
- the branch is ahead of `<base_ref>` for a new independent task;
- the ahead commits/files belong to another issue/PR/task;
- the update would merge, rebase, reset, force-push, overwrite, or conflict;
- project rules forbid the operation.

Do not add a fix on top of unrelated commits. Create a clean branch from `<base_ref>` and re-apply only the intended task changes.

Read-only review/audit does not update or rebase branches unless it is preparing mutation or publication.

## Pre-publication sync and provenance

Before commit, push, PR creation, or PR update, fetch again and re-run provenance:

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

If the local branch is now behind its upstream, update only by `git pull --ff-only`, then re-run relevant validation and provenance before publishing.

If the branch diverged, remote head changed unexpectedly, or unrelated work appears, stop and ask. Do not push or open/update a PR.

The primary commit list is `<base_ref>..HEAD`. The `--cherry-pick` comparison is secondary and must not hide unexpected branch history.

A published PR branch must not be rebased, reset, force-pushed, or replaced without explicit approval after the risk is stated.

## PR body sync

For PR mutation, follow-up commits/pushes, PR creation/update, or PR-ready publication, verify after the final intended diff and validation that the PR title/body still match:

- actual commits and changed files;
- normalized scope and behavior;
- validation/tests/manual checks;
- screenshots or manual verification for UI changes when relevant.

If the PR body is stale, incomplete, or contradicts the final diff, update it when PR publication/update is already allowed by the normalized request. Otherwise draft the corrected PR body and ask before publishing.

Final report line:

```text
PR body: updated | unchanged | drafted | skipped — <reason>
```

## Clean recovery

Allowed recovery:

1. Create a clean branch from the current `<base_ref>`.
2. Cherry-pick or re-apply only intended work.
3. Re-run pre-edit sync and provenance.
4. Continue only when commit range and changed files match the normalized task.

If changes were already made on a polluted branch, export only the intended diff, create a clean branch from `<base_ref>`, apply that diff, validate, and re-run provenance.

Force-push, reset, rebase of a published branch, or replacing a PR branch is gated and requires explicit approval after the risk is stated.

## Report format

```md
### Branch provenance
- Base: `<base_ref> @ <sha>`
- Branch: `<branch>`
- Upstream: `<upstream or none>`
- Branch state: `<current | behind | ahead | diverged | unknown>`
- Task branch: `<new clean branch | existing PR branch | user-approved branch | unsafe>`
- Commits ahead of base: `<N>`
- Changed files: `<N>`
- Unrelated commits/files: `no | yes`
- Safe to edit/commit/push/PR: `yes | no`
```
