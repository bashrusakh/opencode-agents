# Git Branch Provenance Policy

The root `AGENTS.md` Git/PR rules are normative. This document provides the detailed provenance, state-identity, and current-state freshness procedure used by the workflow owner. A directly invoked role with no parent/orchestrator owns applicable freshness within its allowed capabilities.

## Core invariant

A PR is the complete base-to-head comparison, not the last commit.

Before mutation or publication, the workflow owner proves:

1. the local task/PR branch is current enough for the intended action;
2. the branch contains only work belonging to the normalized task/PR;
3. for PR work, the canonical PR URL, author/ownership, Draft/Ready state, head SHA/branch, and base are resolved from repository-host metadata when available.

Resolve the actual refs from tracking state, PR metadata, project guidance, or repository metadata. Do not assume a universal remote or base branch. A local checkout is not evidence that a remote/default/base ref is current until that authoritative ref has been refreshed.

Example only:

```text
<base_remote> = origin
<base_branch> = main
<base_ref>    = origin/main
```

Use those values only when repository evidence shows they are correct. Never construct duplicated refs such as `origin/origin/main`.

## Read-only current-state freshness

Use this when the task asks whether code/behavior exists in the **current upstream/default/base state**. It is separate from updating the working tree.

1. Resolve the authoritative target remote/ref from project guidance, repository-host metadata, or tracking state.
2. Refresh that remote ref without changing the checkout.
3. Record the fetched SHA and compare local HEAD with the target so stale/divergent local state is visible.
4. Inspect the fetched ref directly for the current-state claim, including applicable project guidance/config/tests when they materially affect the conclusion; local files may be comparison/history evidence only when they differ.

Typical read-only commands after resolving the actual target:

```bash
git remote -v
git branch -vv
git fetch --prune <target_remote>
git rev-parse <target_ref>
git rev-list --left-right --count HEAD...<target_ref>
```

Use read-only Git access such as `git show <target_ref>:<path>`, `git grep ... <target_ref>`, or an equivalent ref-aware inspection path when the checkout does not match the target. Do not `pull`, rebase, reset, or checkout merely to inspect current upstream code.

If the remote cannot be refreshed, say that current-state freshness is unverified. Do not convert stale local code into a current-upstream conclusion. Delegated leaf specialists should consume the resolved `<target_ref> @ <sha>` supplied by the workflow owner instead of each fetching independently.

## State identity chain

```text
inspect ref/SHA -> executable workspace -> mutation baseline -> reviewed Base SHA + Candidate HEAD -> published state
```

- Static current-state claims may inspect the fetched ref directly with ref-aware tooling; no checkout is required.
- Runtime reproduction/tests prove a named remote target only from a workspace proven to represent it; record `HEAD` and relevant dirty state. A mismatch produces workspace-only evidence.
- New current-target implementation starts from the proven authoritative baseline; existing PR/task work may be ahead only when that exact branch/context is the authorized target and its base relation is proven.
- Authoritative ref/SHA and intended state identity survive delegated handoffs until explicitly changed by the workflow owner.
- PR evidence is pair-bound: record Base SHA + Candidate HEAD. Base drift can stale validation/review even when Candidate HEAD is unchanged.

## Branch safety classes

A branch is suitable for mutation only when repository evidence shows it is one of:

- a clean task branch created from the intended current `<base_ref>`;
- the existing branch for the PR explicitly being followed up;
- another exact branch the user/project has explicitly authorized for this work.

For a new independent task, do not layer work on commits/files from another task. For an existing PR follow-up, commits/files ahead of `<base_ref>` are expected only when they belong to that same PR/task.

## Pre-edit sync and clean-task gate

Before repository mutation, the workflow owner establishes the intended baseline; the mutation-capable role confirms its worktree represents that baseline before editing. A non-mutation orchestrator must not `pull`/checkout merely to prepare another role's worktree. Use the checks below from the role allowed to perform them:

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

Read-only review/audit does not update/rebase branches merely because it inspects a PR. A required freshness `git fetch` refreshes refs/metadata only and is not a branch/worktree update.

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

Record Base SHA when final validation/review starts, refresh it immediately before PR publication, and refresh it again before Ready. If Base SHA changed, recompute the effective diff and affected integration context. Reuse prior evidence only when both are proven unchanged; otherwise refresh affected validation/review. Publishing the exact reviewed Candidate HEAD alone is not an invalidation; an unexpected remote head still blocks publication/Ready until reconciled.

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
- Authoritative target: `<target_ref @ fetched_sha | local workspace | n/a>`
- Target freshness: `<fresh | unverified | local-target | n/a>`
- State identity: `<exact ref/sha | local HEAD + dirty scope | mismatch/unverified>`
- Base: `<base_ref> @ <current_sha>`
- Reviewed Base: `<base_ref @ sha | not reviewed>`
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
