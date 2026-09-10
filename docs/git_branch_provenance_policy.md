# Git Branch Provenance Policy

The root `AGENTS.md` Git/PR rules are normative. This document provides the detailed provenance procedure used by the active primary/orchestrator.

## Core invariant

A PR is the complete base-to-head comparison, not the last commit.

Before mutation or publication, prove:

1. the local task/PR branch is current enough for the intended action;
2. the branch contains only work belonging to the normalized task/PR;
3. for PR work, the canonical PR URL, author/ownership, Draft/Ready state, head SHA/branch, and base are resolved from repository-host metadata when available.

Resolve the actual refs from tracking state, PR metadata, project guidance, or repository metadata. Do not assume a universal remote or base branch.

Example only:

```text
<base_remote> = origin
<base_branch> = main
<base_ref>    = origin/main
```

Use those values only when repository evidence shows they are correct. Never construct duplicated refs such as `origin/origin/main`.

## Branch safety classes

A branch is suitable for mutation only when repository evidence shows it is one of:

- a clean task branch created from the intended current `<base_ref>`;
- the existing branch for the PR explicitly being followed up;
- another exact branch the user/project has explicitly authorized for this work.

For a new independent task, do not layer work on commits/files from another task. For an existing PR follow-up, commits/files ahead of `<base_ref>` are expected only when they belong to that same PR/task.

## Pre-edit sync and clean-task gate

Before repository mutation by the active primary/orchestrator:

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

If the current branch tracks the intended task/PR upstream and is merely behind, update only with a safe fast-forward when the working tree is clean:

```bash
git pull --ff-only
```

Stop before mutation when:

- unrelated dirty work is present;
- the branch diverged;
- a new independent task would inherit unrelated ahead commits/files;
- the intended base/head/remote cannot be resolved confidently;
- safe update would require merge/rebase/reset/force-push/overwrite or violate project rules.

Do not silently recover by history rewriting. If a clean branch/recovery operation is needed, follow the root authorization gate before creating/replacing branches or performing gated history operations.

Read-only review/audit does not update/rebase branches merely because it inspects a PR.

## Pre-publication provenance

Before commit/push/PR creation/update, fetch again and establish current provenance:

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

Use `<base_ref>..HEAD` as the primary commit list. The `--cherry-pick` comparison is secondary and must not hide unexpected history.

If remote/head/base movement changes the effective diff, reviewed Candidate HEAD, or integration state, re-run affected validation/review/readiness. **Publishing the exact already-reviewed Candidate HEAD is not such an invalidation**: after push, verify that the remote PR head equals the reviewed SHA. If the remote head is unexpected/different, the branch diverged, or unrelated work appears, stop and reconcile provenance before any Ready/publication claim; do not trigger a new full review merely because the expected reviewed SHA was pushed unchanged.

Published PR history must not be reset/rebased/replaced/force-pushed unless the root gate explicitly authorizes that exact action after the risk is stated.

## PR metadata synchronization

For PR mutation/follow-up/publication, keep title/body synchronized with the current Draft/candidate stage. Before Ready, verify after the final intended diff and validation that title/body still match:

- actual commits and changed files;
- normalized scope and behavior;
- actual validation/manual checks;
- UI screenshots/manual verification when relevant and required by project practice.

If metadata is stale and PR update is already authorized, update it. Otherwise draft the corrected metadata and stop before publication.

## Clean recovery

When a polluted branch must be recovered and the necessary branch operations are authorized:

1. create a clean branch from the current intended `<base_ref>`;
2. cherry-pick or re-apply only intended work;
3. re-run sync/provenance;
4. re-run affected validation/review;
5. continue only when the resulting commit range and changed files match the task.

Do not use recovery as a pretext for force-push/reset/rebase of published history without separate authorization.

## Compact report

```md
### Branch provenance
- Base: `<base_ref> @ <sha>`
- Branch: `<branch>`
- Upstream: `<upstream or none>`
- Branch state: `<current | behind | ahead | diverged | unknown>`
- Task context: `<clean task branch | existing PR branch | explicitly authorized branch | unsafe>`
- Commits ahead of base: `<N>`
- Changed files: `<N>`
- Unrelated commits/files: `no | yes | unknown`
- Safe for next requested action: `yes | no`
- PR: `<canonical URL | n/a | unavailable>`
- PR ownership/state: `<owned Draft | owned Ready | not owned | ambiguous | n/a>`
- Candidate HEAD: `<reviewed local sha | not established | n/a>`
- Remote HEAD: `<sha | unavailable | n/a>`
- Candidate identity: `<match | mismatch | not published | n/a>`
```
