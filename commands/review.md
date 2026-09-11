---
description: "Independently review code, a diff/commit/branch/workspace/PR, an implementation result, or a plan; prefer OCR/open-code-review for code review when available and allowed."
agent: reviewer
subtask: false
---

Review: $ARGUMENTS

Follow the active `AGENTS.md` and reviewer role contract. Stay read-only and do not apply fixes or OCR suggestions. If the requested review target is current upstream/default/base, establish/consume the fresh authoritative ref and bind the verdict to that exact state.

For code/diff/commit/branch/workspace/PR review, prefer the loaded `open-code-review` skill/OCR backend when available and external code sharing is permitted. Follow the current skill/CLI timeout and effort semantics; otherwise perform native read-only review and state why OCR was not used.

Review the actual target/effective diff, prioritize correctness/security/regression/right-level issues over style, consume fresh implementation/tester/CI evidence where available, and separate blocking findings from non-blocking notes. Use only narrow non-destructive spot-checks when needed to confirm a specific finding; do not repeat a broad verification matrix merely because reviewer can run checks. When multiple manifestations share one affected state/lifecycle/protocol invariant, inspect the nearest meaningful sibling cases inside that invariant and group them under the shared root problem instead of emitting a one-comment/one-patch queue. Distinguish current-diff regressions, invariant/design gaps, verification gaps, and latent unrelated findings. A verdict applies only to the reviewed state/diff/Candidate HEAD.

If the target is a PR, include its canonical PR URL. For an ordinary review, inspect the requested remote PR state. For the **final owned-PR readiness review**, target the freshly resolved **Base SHA + local Candidate HEAD before push** and review that complete comparison; do not substitute another base or an older remote head. OCR follows reviewer judgment unless user/project policy explicitly requires it.

If no target is supplied, review the current workspace/diff according to the reviewer/OCR default behavior.
