---
description: "Handle follow-up work for an existing PR: review comments, failed checks, requested fixes, implementation, verification, and optional commit/push when the gated-action rule allows that exact action."
agent: code-workflow-orchestrator
subtask: true
---

Run the existing-PR follow-up workflow for: $ARGUMENTS

Treat this as follow-up work for the existing PR by default. Work on the same PR branch. Creating a separate PR is a gated action; proceed only when separate-PR creation is the clear normalized deliverable and the gated-action rule allows it.

Inspect current branch/status/diff and PR context. If PR metadata is unavailable, report the missing source instead of guessing. Orchestrate the needed subagents. Continue automatically through safe stages. Return one consolidated markdown report with green/yellow/red stage status.

Commit or push only when the gated-action rule allows that exact commit/push/update action.
