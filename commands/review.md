---
description: "Independently review code, a diff/commit/branch/workspace/PR, an implementation result, or a plan; use OCR delegate preflight for code-like review when available and managed OCR only when useful/required."
agent: reviewer
subtask: false
---

Review: $ARGUMENTS

Follow the active `AGENTS.md` and reviewer role contract. Stay read-only and do not apply fixes, OCR comments, or delegate suggestions. If the requested target is current upstream/default/base, establish/consume the fresh authoritative ref and bind the verdict to that exact state.

For code/diff/commit/branch/workspace/PR review, establish the authoritative changed-file/effective-diff set, then load `open-code-review-delegate` and use its deterministic `preview` + `rule` preflight when compatible OCR delegation is available. Reconcile delegate reviewable/excluded entries against the authoritative set; every changed `(path,status)` must be reviewed or explicitly skipped with reason before claiming full coverage. If the delegate capability itself is unavailable, perform equivalent native preflight and state why; do not mask bad-ref/wrong-repo/target-mismatch preview errors as availability fallback.

Perform the actual review with the reviewer model. Managed `ocr review` is a separate optional/required second-model escalation after host review, not the default first step. Run it only when user/project policy requires it or it materially improves confidence; use the current `open-code-review` skill, external-sharing gate, and CLI timeout/output/provider semantics. A quota/rate/provider failure, or setup/upgrade needed only for an optional second pass, does not invalidate or block an already complete host review; ask for setup only when managed OCR itself was explicitly requested/required.

Review the actual target/effective diff, prioritize correctness/security/regression/right-level issues over style, consume fresh implementation/tester/CI evidence where available, and use only narrow non-destructive spot-checks to confirm specific findings. Apply root section 2.2.1 before using stated acceptance criteria, then establish that implementation evidence supports the normalized semantic claims. Group multiple manifestations under the shared affected invariant rather than returning a one-comment/one-patch queue. Distinguish current-diff regressions, invariant/design gaps, verification gaps, and latent unrelated findings.

If the target is a PR, include its canonical PR URL. For the **final owned-PR readiness review**, target the freshly resolved **Base SHA + local Candidate HEAD before push** and review that complete comparison; do not substitute another base or an older remote head.

If no target is supplied, review the current workspace/diff according to the reviewer/delegate default behavior.
