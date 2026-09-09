---
description: "Handle follow-up work for an existing PR: aggregate comments/checks/findings, keep owned work-in-progress PRs Draft, coordinate bounded fixes, verify the final candidate, and move to Ready only after the final gate."
agent: code-orchestrator
subtask: false
---

Handle follow-up for the existing PR: $ARGUMENTS

Follow the active `AGENTS.md` and code-orchestrator contract.

Treat the existing PR branch/base as the task context. First resolve the canonical PR URL, author/ownership, Draft/Ready state, head/base, effective diff, current review comments, failed/pending checks, and known todo. Build one current findings set before dispatching fixes; deduplicate/group related findings by invariant rather than processing comments as a one-fix-at-a-time queue.

For a confirmed **owned PR** with implementation/update work in scope, keep the PR Draft during active iteration. If it is currently Ready, convert it back to Draft before the first changed diff is pushed/updated remotely (preferably before the first implementation batch when the status tool is available) when updating that PR is already authorized. If status mutation is temporarily unavailable, local work may continue but do not publish changed PR content while it remains Ready. Read-only review/planning does not change PR state, and non-owned/ambiguous PRs are never auto-converted.

Coordinate bounded investigation/implementation/verification stages under the code-orchestrator delegation contract. If repeated findings reveal a shared state/lifecycle/protocol invariant or require new architectural concepts, stop local patching and trigger complexity/design escalation before further implementation.

Do not re-run expensive final review after every intermediate batch. Use task-relevant verification during batches. When implementation and in-scope blockers are complete, push the final intended commits while the PR is still Draft and establish that remote head as the Candidate HEAD. Run applicable final local/CI checks, then require `@reviewer` to review the **entire base-to-Candidate-HEAD PR** as one integrated change; OCR is reviewer-selected unless explicitly required. Resolve blockers, refresh affected evidence, synchronize metadata/provenance, and only then move an owned PR to Ready.

Keep follow-up work on the existing PR branch by default. Do not create a separate branch/PR unless that is explicitly the intended workflow. Push/update/comment only when the exact publication action is already authorized by the root gate.

The final report must include the canonical PR URL; for owned PRs also include Draft/Ready state and Candidate HEAD when established.
