---
description: "Independently review code, a diff/commit/branch/workspace/PR, an implementation result, or a plan; prefer OCR/open-code-review for code review when available and allowed."
agent: reviewer
subtask: false
---

Review: $ARGUMENTS

Follow the active `AGENTS.md` and reviewer role contract. Stay read-only and do not apply fixes or OCR suggestions.

For code/diff/commit/branch/workspace/PR review, prefer the loaded `open-code-review` skill/OCR backend when available and external code sharing is permitted. Follow the current skill/CLI timeout and effort semantics; otherwise perform native read-only review and state why OCR was not used.

Review the actual target/effective diff, prioritize correctness/security/regression/right-level issues over style, verify findings against surrounding code/tests where practical, and separate blocking findings from non-blocking notes. When multiple manifestations share one affected state/lifecycle/protocol invariant, inspect the nearest meaningful sibling cases inside that invariant and group them under the shared root problem instead of emitting a one-comment/one-patch queue. Distinguish current-diff regressions, invariant/design gaps, verification gaps, and latent unrelated findings. A verdict applies only to the reviewed state/diff/Candidate HEAD.

If the target is a PR, include its canonical PR URL in the report. For a final owned-PR readiness review, review the complete base-to-Candidate-HEAD PR as one integrated change even if earlier commits/diffs were reviewed separately. OCR follows reviewer judgment unless user/project policy explicitly requires it.

If no target is supplied, review the current workspace/diff according to the reviewer/OCR default behavior.
