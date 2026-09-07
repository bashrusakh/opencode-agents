---
description: "Handle follow-up work for an existing PR: comments, failed checks, requested fixes, implementation, verification, review, metadata sync, and authorized publication."
agent: code-orchestrator
subtask: false
---

Handle follow-up for the existing PR: $ARGUMENTS

Follow the active `AGENTS.md` and code-orchestrator contract.

Treat the existing PR branch/base as the task context. Verify current PR metadata, requested changes/comments/check failures, branch provenance, and the effective diff before deciding what work is required.

Coordinate only applicable stages: investigation, implementation by a capable role, verification, independent review, PR-readiness, and PR body/title synchronization. Evidence and review must match the final effective diff.

Keep follow-up work on the existing PR branch by default. Do not create a separate branch/PR unless that is explicitly the intended workflow. Push/update/comment only when the exact publication action is already authorized by the root gate.
