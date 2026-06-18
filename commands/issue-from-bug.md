---
description: Verify a described bug and draft or open a factual actionable issue without inventing root cause.
agent: code-workflow-orchestrator
subtask: false
---

Run the issue-from-bug workflow for: $ARGUMENTS

Verify the problem against current code/state before writing the issue. Search existing issues if possible. Use @explore for affected modules. Do not invent root cause; label hypotheses clearly.

Draft or open an issue only according to the user's request. If external GitHub actions are needed and were not explicitly requested, ask before opening.

Return one consolidated markdown report with green/yellow/red stage status and the issue text if drafted.
