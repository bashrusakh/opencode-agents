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

Do **not** require the final reviewer or a separate tester pass after every intermediate batch. Use implementation-local evidence by default during mutation batches; group independent `@tester` verification at meaningful integration/candidate boundaries when independence materially adds confidence or policy requires it. Remote CI is a separate evidence layer. Intermediate publication is only for work that is explicitly still in progress or needs remote CI/status evidence. Once the orchestrator believes the current batch may be final repository content, stop using the intermediate path and hold/freeze it locally for Candidate HEAD review before push. Delegate preflight follows the code-review policy when compatible OCR is available; managed OCR remains reviewer-selected unless user/project policy explicitly requires it.

## Candidate HEAD

When intended implementation and in-scope bugfixes are complete:

1. commit the final intended state as **Candidate HEAD**;
2. refresh and record the authoritative **Base SHA**;
3. run final local validation and whole-PR `@reviewer` against **Base SHA -> Candidate HEAD**;
4. refresh Base SHA before PR publication. If it moved, apply the base-drift rule below before reusing evidence;
5. push the exact reviewed Candidate HEAD while Draft and require matching remote head;
6. run remote CI/status, refresh Base SHA again, reconcile drift, then refresh provenance/metadata.

**Base-drift rule:** final evidence is bound to Base SHA + Candidate HEAD. A moved base makes affected evidence stale by default; retain it only when the recomputed effective diff and affected integration context are proven unchanged. Otherwise refresh affected validation/review before publication or Ready. A push alone does not stale evidence when this pair remains valid.

Narrow recovery case: if a Draft batch was genuinely published as intermediate work and only afterward no further repository-content change proves necessary, do not manufacture a no-op commit just to recreate the normal sequence. Review that exact already-published SHA before Ready and report that it was previously published as an intermediate batch. This is a recovery case, not permission to knowingly push a likely-final candidate before review.

## Ready-for-review gate

An owned PR may move from Draft to Ready only when all applicable conditions are current for the same reviewed Base SHA + Candidate HEAD:

- **Scope/fixes complete** — current todo/findings are reconciled; all in-scope blocking bugs, review findings, and failed checks are resolved or rejected as false/not applicable with evidence. Unrelated latent defects remain follow-up items rather than silently expanding the PR.
- **Behavior/fix contract** — right-level/root cause is established; complex stateful/protocol work has the required invariant/state/transition/interleaving map.
- **Local verification** — task/project checks are green for every affected boundary and refer to the reviewed Base SHA + Candidate HEAD.
- **Reviewer** — before push, final `@reviewer` covers the **entire reviewed-Base-SHA-to-Candidate-HEAD comparison** with no unresolved blocking findings.
- **Published identity** — remote PR head equals the reviewed Candidate HEAD and base drift since review/publication is reconciled.
- **CI/status checks** — all required/task-relevant remote checks available while Draft are complete and successful for that published Candidate HEAD.
- **Provenance** — current Base SHA, reviewed Base SHA, Candidate HEAD, and remote head are known and reconciled.
- **PR metadata** — title/body describe the final candidate and actual validation.

If a repository has a required check that cannot run until Ready, do not fabricate a pass or bounce Draft/Ready repeatedly. Report the repository-specific dependency and follow explicit project/user policy for that exception.

## Findings and review cycles

Do not translate each review comment into a separate fix/review cycle. Aggregate current review comments, failed checks, tester evidence, reviewer findings, OCR findings when present, and todo; deduplicate and group them by root invariant/ownership before assigning new mutation.

During implementation batches, use targeted verification. Reserve the expensive final whole-PR reviewer pass for the final Base SHA + Candidate HEAD pair before publication unless independent review is needed earlier to choose the next safe direction.

A final reviewer `changes required` verdict keeps the PR Draft. OCR findings, when used, are inputs to that verdict. Fix in bounded batches, rerun affected local checks, establish a new local candidate, and repeat the final whole-PR reviewer pass before pushing that replacement candidate.

If remote CI fails after the reviewed Candidate HEAD is pushed and a repository-content fix is required, the fix creates a new candidate. Return to the local candidate sequence: fix -> local verification -> whole-PR review -> push exact reviewed SHA -> identity check -> remote CI.

## Normal ordering

1. resolve PR URL/ownership/state/base/head and collect the current findings set;
2. convert owned Ready PR to Draft when implementation/update begins;
3. implement bounded batches under the orchestrator delegation contract;
4. collect implementation-local evidence during ordinary Draft iteration and run independent `@tester` only at meaningful integration checkpoints as useful/required; remote CI remains a separate published-candidate layer;
5. establish Candidate HEAD and refresh/record Base SHA;
6. run final local validation and whole-PR `@reviewer` against that Base+Head pair;
7. refresh/reconcile Base SHA before PR publication;
8. push the exact reviewed Candidate HEAD while Draft and verify remote head identity;
9. run required remote CI/status checks;
10. refresh/reconcile Base SHA and provenance again;
11. mark the owned PR Ready;
14. if new repository-content work later resumes, convert it back to Draft first.

## Report

Any user-facing report about a specific PR includes:

```text
PR: <canonical URL>
State: Draft | Ready
Reviewed Base: <ref@sha | not reviewed>
Candidate HEAD: <sha | not established>
Reviewed Candidate: <same sha | not reviewed>
Remote HEAD: <sha | unavailable>
Candidate identity: match | mismatch | not published
Reviewer: <status>
OCR: <status when used/required | not used>
Checks: <status>
PR body: updated | unchanged | drafted | skipped — <reason>
```
