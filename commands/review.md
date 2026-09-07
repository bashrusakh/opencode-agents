---
description: "Independently review code, a diff/commit/branch/workspace/PR, an implementation result, or a plan; prefer OCR/open-code-review for code review when available and allowed."
agent: reviewer
subtask: false
---

Review: $ARGUMENTS

Follow the active `AGENTS.md` and reviewer role contract. Stay read-only and do not apply fixes or OCR suggestions.

For code/diff/commit/branch/workspace/PR review, prefer the loaded `open-code-review` skill/OCR backend when available and external code sharing is permitted. Follow the current skill/CLI timeout and effort semantics; otherwise perform native read-only review and state why OCR was not used.

Review the actual target/effective diff, prioritize correctness/security/regression/right-level issues over style, verify findings against surrounding code/tests where practical, and separate blocking findings from non-blocking notes. A verdict applies only to the reviewed state/diff.

If no target is supplied, review the current workspace/diff according to the reviewer/OCR default behavior.
