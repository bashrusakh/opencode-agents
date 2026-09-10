---
description: "Handle follow-up work for an existing PR: aggregate comments/checks/findings, keep owned work-in-progress PRs Draft, coordinate bounded fixes, verify the final candidate, and move to Ready only after the final gate."
agent: code-orchestrator
subtask: false
---

Handle follow-up for the existing PR: $ARGUMENTS

Follow the active `AGENTS.md` and code-orchestrator contract.

Treat the existing PR branch/base as the task context. First resolve the canonical PR URL, author/ownership, Draft/Ready state, head/base, effective diff, current review comments, failed/pending checks, and known todo. Build one current findings set before dispatching fixes; deduplicate/group related findings by invariant rather than processing comments as a one-fix-at-a-time queue.

For a confirmed **owned PR** with implementation/update work in scope, keep the PR Draft during active iteration. If it is currently Ready, convert it back to Draft before the first changed diff is pushed/updated remotely (preferably before the first implementation batch when the status tool is available) when updating that PR is already authorized. If status mutation is temporarily unavailable, local work may continue but do not publish changed PR content while it remains Ready. Read-only review/planning does not change PR state, and non-owned/ambiguous PRs are never auto-converted.

Coordinate bounded investigation/implementation/verification stages under the code-orchestrator delegation contract. If repeated findings reveal a shared state/lifecycle/protocol invariant or require new architectural concepts, stop local patching and trigger complexity/design escalation before further implementation. Intermediate Draft pushes are for work that is still explicitly in progress or needs remote CI/status evidence; once the current batch may be final repository content, hold it locally for the final Candidate review instead of publishing it as another intermediate batch.

Do not re-run expensive final review after every intermediate batch. Use proportionate implementation-local verification during mutation batches and group independent `@tester` work at meaningful integration/candidate boundaries rather than after every package. When implementation and in-scope blockers are complete, commit the intended final state locally and establish that exact SHA/effective diff as the Candidate HEAD. Run final applicable local verification, then require `@reviewer` to review the **entire base-to-local-Candidate-HEAD change before push** as one integrated change; OCR is reviewer-selected unless explicitly required. Resolve blocking findings locally and repeat the affected verification plus whole-PR review for every changed candidate. After reviewer pass, push the exact reviewed Candidate HEAD while the PR remains Draft, verify the remote PR head equals that SHA, run required remote CI/status checks, refresh metadata/provenance, and only then move an owned PR to Ready. Do not repeat full review solely because the unchanged reviewed SHA was pushed.

Keep follow-up work on the existing PR branch by default. Do not create a separate branch/PR unless that is explicitly the intended workflow. Push/update/comment only when the exact publication action is already authorized by the root gate.

The final report must include the canonical PR URL; for owned-PR final-candidate/readiness work also include Draft/Ready state, the reviewed Candidate HEAD, current remote HEAD, and whether those SHAs match.
