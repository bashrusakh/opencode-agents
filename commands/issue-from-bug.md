---
description: Verify a described bug and draft or open a factual actionable issue without inventing root cause.
agent: code-workflow-orchestrator
subtask: true
---

Run the issue-from-bug workflow for: $ARGUMENTS

Verify the problem against current code/state before writing the issue. Search existing issues when repo/tooling provides issue access; otherwise report that issue search was not performed. Use @explore for affected modules. Do not invent root cause; label hypotheses clearly.

Draft or open an issue only when the normalized action level includes issue drafting/opening. Ask before external GitHub actions unless the action level clearly includes opening the issue.

Return one consolidated markdown report with green/yellow/red stage status and the issue text if drafted.
