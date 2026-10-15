---
name: pr-readiness
description: Use for owned-PR Draft/candidate/publication/readiness workflows. Owns the reusable PR lifecycle; root AGENTS.md supplies authorization/gates and git-provenance supplies ref/base/head identity.
---

# PR readiness

**Owned PR** means a pull request whose author is the current authenticated/user account, or a PR this workflow previously created on that user's behalf and whose ownership is confirmed from repository-host metadata. A branch name alone does not establish ownership.

Draft publication and Ready-for-review are different boundaries. Here **Ready** means the repository host's Draft -> Ready state for external/public review; it is distinct from the internal `@reviewer` stage. Read-only review never authorizes a PR-state change, and Draft/Ready state must never be changed for a PR that is not confirmed to be owned.

## Draft publication safety

During active work on an owned PR, intermediate Draft publication is allowed only when:

- the `git-provenance` publication checkpoint is satisfied for the current batch;
- the batch remains inside the authorized PR scope;
- applicable implementation/verification evidence is fresh enough for that batch and failures/blockers are stated honestly;
- the PR remains Draft and its current metadata is not misleading.

An intermediate Draft push does not require a separate `@tester` invocation or final `@reviewer` merely because a batch ended. Once the current repository state may be the final content candidate, do not publish it as another intermediate batch: freeze/commit it locally and enter the Candidate HEAD sequence.

## Candidate HEAD

When implementation is complete, establish the final intended local state as **Candidate HEAD**. Refresh and record **Base SHA**, satisfy final applicable local validation, and run whole-PR `@reviewer` against `Base SHA -> Candidate HEAD` **before push**.

Refresh Base SHA again before publishing that candidate and before Ready. If it moved, recompute the effective diff/integration context and refresh only the evidence affected by that change. Push only the exact reviewed Candidate HEAD while the owned PR is Draft, verify that the remote PR head matches it, then consume the remote CI/status evidence that is legitimately available in the current lifecycle state. Pushing an unchanged reviewed SHA does not itself stale review evidence when the reviewed base context and effective diff remain valid.

## Ready-for-review gate

Under the default pack readiness workflow, the Ready evidence contract is satisfied only when all applicable conditions are true for the Candidate HEAD. A higher-priority instruction may authorize a different state transition under the active workflow-control/user gate, but it does not convert missing evidence into a pass:

- **Scope complete** — in-scope blocking findings/todo items are resolved or rejected with evidence; unrelated latent findings were not silently folded into the PR.
- **Fix/regression contract** — applicable sections 7.2 and 7.3 are satisfied.
- **Local evidence** — applicable implementation/verification evidence is current for the reviewed Base SHA + Candidate HEAD.
- **Reviewer** — `@reviewer` reviewed the complete Base-SHA-to-Candidate-HEAD comparison before push with no unresolved blocking findings and `Coverage: full PR`, **under an authoritative acceptance model that spans the whole PR/task surface rather than only the latest fix/risk slice**. Structural full-diff coverage does not cure an omitted semantic acceptance area. A separately stated executable/live `Acceptance proof: partial` may be compatible with Ready only when the missing proof is an explicitly deferred/out-of-lifecycle evidence surface, not when the reviewer lacked the authoritative acceptance model needed to judge a material PR area. The reviewer verdict establishes Candidate-level independent acceptance evidence; it does **not** itself establish or authorize the Ready transition or any later lifecycle transition. The workflow owner derives Ready only from the complete applicable gate below.
- **Identity/provenance** — the `git-provenance` checkpoint is current, base drift is reconciled, and remote PR head equals the reviewed Candidate HEAD.
- **CI/status** — required/task-relevant remote checks whose evidence is legitimately available before the Ready transition are complete and successful when applicable. A host status token is evidence of state, not a semantic classification by itself: distinguish an executed/pending/failed check from a check awaiting approval, lifecycle transition, or another prerequisite before treating its absence as a Ready blocker.
- **Repository prerequisites** — every repository-defined prerequisite applicable to the change is satisfied. A prerequisite may require a decision or approval recorded outside the PR, including a discussion, issue, RFC, forum, mailing list, or another repository-defined process. Determine both applicability and satisfaction from authoritative repository policy, maintainer decisions, and current authoritative repository/review/status signals. The external artifact being open, closed, or merely linked is not by itself proof that the prerequisite is unresolved or resolved. Block Ready only while the required decision/approval itself remains unresolved, or while repository policy explicitly requires another still-unsatisfied state. Once the prerequisite is satisfied, do not wait for the external artifact to be closed unless closure itself is an explicit repository requirement.
- **Metadata** — title/body describe the final candidate, actual validation, current scope, and any applicable prerequisite outcome without claiming agreement that the authoritative record does not establish.

Repository-prerequisite evidence is workflow state, not Candidate-HEAD content evidence. Refresh any applicable externally held decision/approval state immediately before Ready when it can have changed independently of the code; an unchanged Candidate HEAD does not keep that evidence fresh.

While a required repository prerequisite remains unresolved, keep the owned PR Draft. Continue only already-authorized work that can legitimately resolve or prepare for that prerequisite; do not implement a disputed product/design choice merely to make progress. If resolution depends on a maintainer/user/external decision that the workflow cannot supply, report the exact unresolved decision and wait at that boundary. If an owned PR is already Ready when a mandatory prerequisite is discovered or becomes unresolved, treat readiness as stale and return it to Draft when the active owned-PR publication scope authorizes that state transition; otherwise report the state mismatch as a blocker. Once all applicable prerequisites and the other Ready conditions are satisfied, move the owned PR to Ready without requiring an extra user permission or ceremonial wait beyond the normal publication gate already established for the PR workflow.

Apply Ready conditions by their actual dependency, not by the order in which this skill lists them. A condition is not a pre-Ready blocker merely because its evidence is absent before the transition: if that evidence can exist only after crossing the Ready boundary, establish from authoritative project policy and current host/repository behavior whether another valid pre-Ready path exists, whether the evidence belongs to the post-transition state, or whether project policy is genuinely contradictory. Do not convert lifecycle-dependent unavailability into failure, fabricate a pass, or let a pack default create a circular gate.

Under the default pack readiness workflow, a `changes required` reviewer verdict keeps the PR Draft. Resolve findings in bounded batches, refresh affected verification, establish a new Candidate HEAD, and repeat the final whole-PR review before pushing that replacement candidate. A higher-priority authorized state transition does not erase or satisfy those findings.

Any repository-content/history change after final candidate verification/review invalidates the evidence it can affect and creates a new candidate. An unchanged reviewed commit may be pushed without re-review solely because publication occurred; verify identity instead. If remote CI requires a content fix, create a new local candidate and repeat the applicable final validation/review sequence. If repository-content work resumes after an owned PR was Ready, return it to Draft before continuing the next update cycle.
