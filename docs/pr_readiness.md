# PR Draft / readiness lifecycle

The root `AGENTS.md` PR policy is normative. This document separates **work-in-progress Draft publication** from the final **Ready for external/public review** gate and makes the internal review/push order explicit. Here `Ready` means the repository host's Draft -> Ready state; it is not the internal `@reviewer` stage.

GitHub Draft is the normal state for an owned PR while implementation, intermediate pushes, CI iteration, or follow-up fixes are active. Draft is not a synonym for unverified garbage: every published batch still has a provenance/scope safety boundary. Ready means one exact reviewed candidate was published unchanged and then passed the required remote checks.

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
- proportionate fresh verification evidence exists where practical; implementation-local evidence may satisfy an intermediate batch, and a separate `@tester` invocation is not required merely because the batch ended; blockers are stated honestly;
- PR metadata describes work-in-progress truthfully;
- the PR remains Draft.

Do **not** require the final reviewer or a separate tester pass after every intermediate batch. Use implementation-local evidence by default during mutation batches; group independent `@tester` verification at meaningful integration/candidate boundaries when independence materially adds confidence or policy requires it. Remote CI is a separate evidence layer. Intermediate publication is only for work that is explicitly still in progress or needs remote CI/status evidence. Once the orchestrator believes the current batch may be final repository content, stop using the intermediate path and hold/freeze it locally for Candidate HEAD review before push. OCR remains reviewer-selected unless user/project policy explicitly requires it.

## Candidate HEAD

When intended implementation and in-scope bugfixes are complete:

1. commit the intended final state locally on the PR branch and ensure no uncommitted task changes sit outside it;
2. designate that exact local commit SHA/effective base-to-head diff as the **Candidate HEAD**;
3. satisfy final applicable local validation against that candidate using fresh implementation-local evidence and, when independently useful/required, one batched `@tester` checkpoint for the complete affected boundary;
4. run the final whole-PR `@reviewer` pass against **base -> local Candidate HEAD before push**;
5. if review or local verification requires repository-content changes, create a new Candidate HEAD and repeat the affected local checks plus the whole-PR review;
6. only after reviewer pass, push the exact reviewed Candidate HEAD while the PR remains Draft;
7. resolve/fetch the PR again and require `remote PR HEAD == reviewed Candidate HEAD`; if it mismatches, stop and reconcile branch/provenance rather than silently accepting or reviewing the unexpected remote head;
8. run required remote CI/status checks for that exact matching SHA, then refresh provenance and PR metadata.

A push of the already-reviewed commit does **not** create a new review target: the commit SHA and effective diff are unchanged. Do not repeat full review solely because the candidate was pushed. If the push is followed by a repository-content fix, rebase/amend, dependency/generated-output change, or any other change that produces a different candidate, the affected evidence is stale and the replacement candidate must be reviewed before its final push.

Narrow recovery case: if a Draft batch was genuinely published as intermediate work and only afterward no further repository-content change proves necessary, do not manufacture a no-op commit just to recreate the normal sequence. Review that exact already-published SHA before Ready and report that it was previously published as an intermediate batch. This is a recovery case, not permission to knowingly push a likely-final candidate before review.

## Ready-for-review gate

An owned PR may move from Draft to Ready only when all applicable conditions are current for the same Candidate HEAD:

- **Scope/fixes complete** — current todo/findings are reconciled; all in-scope blocking bugs, review findings, and failed checks are resolved or rejected as false/not applicable with evidence. Unrelated latent defects remain follow-up items rather than silently expanding the PR.
- **Behavior/fix contract** — right-level/root cause is established; complex stateful/protocol work has the required invariant/state/transition/interleaving map.
- **Local verification** — task/project checks are green for every affected boundary that can be verified, including changed and preserved behavior, and refer to the local Candidate HEAD reviewed below.
- **Reviewer** — before push, final `@reviewer` covers the **entire base-to-local-Candidate-HEAD comparison** and has no unresolved blocking findings. Earlier commit/file/incremental reviews or a review of the older remote PR head do not replace this integrated pass. Large candidates may be reviewed in explicit slices, but every changed file/effective-diff slice must be accounted for and reconciled into one `Coverage: full PR` verdict. OCR, when used, is reconciled into the reviewer verdict under the normal review policy.
- **Published identity** — the exact reviewed Candidate HEAD was pushed unchanged while Draft, and the current remote PR head equals the reviewed SHA.
- **CI/status checks** — all required/task-relevant remote checks available while Draft are complete and successful for that published Candidate HEAD.
- **Provenance** — branch/base/remote state is current and still confirms the remote PR head equals the reviewed Candidate HEAD.
- **PR metadata** — title/body describe the final candidate and actual validation.

If a repository has a required check that cannot run until Ready, do not fabricate a pass or bounce Draft/Ready repeatedly. Report the repository-specific dependency and follow explicit project/user policy for that exception.

## Findings and review cycles

Do not translate each review comment into a separate fix/review cycle. Aggregate current review comments, failed checks, tester evidence, reviewer findings, OCR findings when present, and todo; deduplicate and group them by root invariant/ownership before assigning new mutation.

During implementation batches, use targeted verification. Reserve the expensive final whole-PR reviewer pass for the local Candidate HEAD immediately before its final push unless independent review is specifically needed earlier to choose the next safe design direction.

A final reviewer `changes required` verdict keeps the PR Draft. OCR findings, when used, are inputs to that verdict. Fix in bounded batches, rerun affected local checks, establish a new local candidate, and repeat the final whole-PR reviewer pass before pushing that replacement candidate.

If remote CI fails after the reviewed Candidate HEAD is pushed and a repository-content fix is required, the fix creates a new candidate. Return to the local candidate sequence: fix -> local verification -> whole-PR review -> push exact reviewed SHA -> identity check -> remote CI.

## Normal ordering

1. resolve PR URL/ownership/state/base/head and collect the current findings set;
2. convert owned Ready PR to Draft when implementation/update begins;
3. implement bounded batches under the orchestrator delegation contract;
4. collect implementation-local evidence during ordinary Draft iteration and run independent `@tester` only at meaningful integration checkpoints as useful/required; remote CI remains a separate published-candidate layer;
5. when implementation is complete, commit the intended final state locally and designate that exact SHA as Candidate HEAD;
6. run final applicable **local** verification for Candidate HEAD;
7. run final `@reviewer` over **base -> local Candidate HEAD before push**; OCR is reviewer-selected unless explicitly required;
8. resolve reviewer findings locally; every repository-content change establishes a new candidate and returns to steps 6-7;
9. push the exact reviewed Candidate HEAD while still Draft;
10. verify `remote PR HEAD == reviewed Candidate HEAD`; on mismatch stop/reconcile provenance, and do **not** re-run full review merely because the expected SHA was pushed unchanged;
11. run required remote CI/status checks for that SHA; if a repository-content fix is needed, return to step 5;
12. refresh provenance and final PR metadata;
13. mark the owned PR Ready;
14. if new repository-content work later resumes, convert it back to Draft first.

## Report

Any user-facing report about a specific PR includes:

```text
PR: <canonical URL>
State: Draft | Ready
Candidate HEAD: <sha | not established>
Reviewed Candidate: <same sha | not reviewed>
Remote HEAD: <sha | unavailable>
Candidate identity: match | mismatch | not published
Reviewer: <status>
OCR: <status when used/required | not used>
Checks: <status>
PR body: updated | unchanged | drafted | skipped — <reason>
```
