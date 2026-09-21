---
name: pr-readiness
description: Use for owned-PR Draft/candidate/publication/readiness workflows. Root AGENTS.md and git-provenance remain authoritative.
---

# PR readiness

Draft publication and Ready-for-review are different boundaries. Here **Ready** means the repository host's Draft -> Ready state for external/public review; it is distinct from the internal `@reviewer` stage. Read-only review never authorizes a PR-state change, and Draft/Ready state must never be changed for a PR that is not confirmed to be owned.

## Draft publication safety

During active work on an owned PR, intermediate Draft publication is allowed only when:

- the `git-provenance` publication checkpoint is satisfied for the current batch;
- the batch remains inside the authorized PR scope;
- applicable section 7.4 evidence is fresh enough for that batch and failures/blockers are stated honestly;
- the PR remains Draft and its current metadata is not misleading.

An intermediate Draft push does not require a separate `@tester` invocation or final `@reviewer` merely because a batch ended. Once the current repository state may be the final content candidate, do not publish it as another intermediate batch: freeze/commit it locally and enter the Candidate HEAD sequence.

## Candidate HEAD

When implementation is complete, establish the final intended local state as **Candidate HEAD**. Refresh and record **Base SHA**, satisfy final applicable local validation, and run whole-PR `@reviewer` against `Base SHA -> Candidate HEAD` **before push**.

Refresh Base SHA again before publishing that candidate and before Ready. If it moved, recompute the effective diff/integration context and refresh only the evidence affected by that change. Push only the exact reviewed Candidate HEAD while the owned PR is Draft, verify that the remote PR head matches it, then consume the required remote CI/status evidence. Pushing an unchanged reviewed SHA does not itself stale review evidence when the reviewed base context and effective diff remain valid.

## Ready-for-review gate

An owned PR may move from Draft to Ready only when all applicable conditions are true for the Candidate HEAD:

- **Scope complete** — in-scope blocking findings/todo items are resolved or rejected with evidence; unrelated latent findings were not silently folded into the PR.
- **Fix/regression contract** — applicable sections 7.2 and 7.3 are satisfied.
- **Local evidence** — applicable section 7.4 evidence is current for the reviewed Base SHA + Candidate HEAD.
- **Reviewer** — `@reviewer` reviewed the complete Base-SHA-to-Candidate-HEAD comparison before push with no unresolved blocking findings and `Coverage: full PR`.
- **Identity/provenance** — the `git-provenance` checkpoint is current, base drift is reconciled, and remote PR head equals the reviewed Candidate HEAD.
- **CI/status** — required/task-relevant remote checks available for the Draft candidate are complete and successful; pending, failed, unknown, or stale required checks block automatic Ready.
- **Metadata** — title/body describe the final candidate, actual validation, and current scope.

If a required check technically cannot run until the PR is marked Ready, do not fabricate a pass or bounce Draft/Ready repeatedly. Report the repository-specific dependency and follow explicit project/user policy for that exception.

A `changes required` reviewer verdict keeps the PR Draft. Resolve findings in bounded batches, refresh affected verification, establish a new Candidate HEAD, and repeat the final whole-PR review before pushing that replacement candidate.

Any repository-content/history change after final candidate verification/review invalidates the evidence it can affect and creates a new candidate. An unchanged reviewed commit may be pushed without re-review solely because publication occurred; verify identity instead. If remote CI requires a content fix, create a new local candidate and repeat the applicable final validation/review sequence. If repository-content work resumes after an owned PR was Ready, return it to Draft before continuing the next update cycle.
