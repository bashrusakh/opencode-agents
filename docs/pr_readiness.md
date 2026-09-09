# PR Draft / readiness lifecycle

The root `AGENTS.md` PR policy is normative. This document separates **work-in-progress Draft publication** from the final **Ready for review** gate.

GitHub Draft is the normal state for an owned PR while implementation, intermediate pushes, CI iteration, or follow-up fixes are still active. Draft is not a synonym for unverified garbage: every published batch still has a provenance/scope safety boundary. Ready means a stable final candidate has passed the stronger gate.

## Ownership and state

Before changing PR state, resolve the canonical PR URL, author/ownership, current Draft/Ready state, head SHA/branch, and base.

- New owned PRs are created Draft by default.
- An owned Ready PR returns to Draft before the first changed diff is pushed/updated remotely, preferably before the first implementation batch when the status tool is available, when updating that PR is already authorized. If the transition is temporarily unavailable, local work may continue but changed PR content is not published while it remains Ready.
- Read-only review/audit/planning does not change PR state.
- Never automatically change Draft/Ready state for a PR that is not confirmed to be owned. Branch naming alone is not ownership proof.

Converting an owned PR back to Draft is part of the already-authorized PR follow-up lifecycle; do not add a duplicate confirmation ritual. If PR mutation itself is not authorized, do not change remote state.

## Draft publication safety

Before an intermediate push/update to an owned Draft PR:

- provenance/base/head/remote are correct for the PR;
- the published diff contains no unrelated commits/files/secrets/artifacts;
- the batch stays inside the authorized PR scope;
- task-relevant batch verification has run where practical, with blockers stated honestly;
- PR metadata describes work-in-progress truthfully;
- the PR remains Draft.

Do **not** require the final reviewer after every intermediate batch. Use focused tester/local/CI evidence while work is still changing. OCR remains reviewer-selected unless user/project policy explicitly requires it.

## Candidate HEAD

When intended implementation and in-scope bugfixes are complete, publish the final intended commits **while the PR is still Draft** under Draft publication safety. The resulting remote PR head/effective diff is the **Candidate HEAD**. All final readiness evidence must refer to that same candidate.

If code/config/tests/dependencies/generated output/history change afterward, the affected candidate evidence is stale. Establish the new Candidate HEAD and rerun only what the change can affect.

## Ready-for-review gate

An owned PR may move from Draft to Ready only when all applicable conditions are current for the Candidate HEAD:

- **Scope/fixes complete** — current todo/findings are reconciled; all in-scope blocking bugs, review findings, and failed checks are resolved or rejected as false/not applicable with evidence. Unrelated latent defects remain follow-up items rather than silently expanding the PR.
- **Behavior/fix contract** — right-level/root cause is established; complex stateful/protocol work has the required invariant/state/transition/interleaving map.
- **Local verification** — task/project checks are green for every affected boundary that can be verified, including changed and preserved behavior.
- **CI/status checks** — all required/task-relevant checks available while Draft are complete and successful for the Candidate HEAD.
- **Reviewer** — final `@reviewer` pass covers the **entire base-to-Candidate-HEAD PR comparison** and has no unresolved blocking findings. Earlier commit/file/incremental-diff reviews do not replace this integrated pass. Large PRs may be reviewed in explicit slices, but every changed file/effective-diff slice must be accounted for and reconciled into one `Coverage: full PR` verdict. OCR, when used, is reconciled into the reviewer verdict under the normal review policy.
- **Provenance** — branch/base/remote state is current and the remote PR head equals the reviewed Candidate HEAD.
- **PR metadata** — title/body describe the final candidate and actual validation.

If a repository has a required check that cannot run until Ready, do not fabricate a pass or bounce Draft/Ready repeatedly. Report the repository-specific dependency and follow explicit project/user policy for that exception.

## Findings and review cycles

Do not translate each review comment into a separate fix/review cycle. Aggregate current review comments, failed checks, tester evidence, reviewer findings, OCR findings when present, and todo; deduplicate and group them by root invariant/ownership before assigning new mutation.

During implementation batches, use targeted verification. Reserve the expensive final whole-PR reviewer pass for a stable Candidate HEAD unless independent review is specifically needed to choose the next safe design direction.

A final reviewer `changes required` verdict keeps the PR Draft. OCR findings, when used, are inputs to that verdict. Fix in bounded batches, rerun affected checks, establish a new candidate, and repeat the final whole-PR reviewer pass.

## Normal ordering

1. resolve PR URL/ownership/state/base/head and collect the current findings set;
2. convert owned Ready PR to Draft when implementation/update begins;
3. implement bounded batches under the orchestrator delegation contract;
4. run focused verification/CI while Draft;
5. when implementation is complete, push the final intended commit(s) while still Draft and establish that remote head as Candidate HEAD;
6. run all applicable final verification/status checks for that remote candidate;
7. run final `@reviewer` over the complete base-to-Candidate-HEAD PR; OCR is reviewer-selected unless explicitly required;
8. resolve blockers and refresh affected evidence until the candidate is clean;
9. refresh provenance and final PR metadata;
10. mark owned PR Ready;
11. if new repository-content work later resumes, convert it back to Draft first.

## Report

Any user-facing report about a specific PR includes:

```text
PR: <canonical URL>
State: Draft | Ready
Candidate HEAD: <sha | not established>
Reviewer: <status>
OCR: <status when used/required | not used>
Checks: <status>
PR body: updated | unchanged | drafted | skipped — <reason>
```
