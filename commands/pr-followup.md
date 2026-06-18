---
description: Handle follow-up work for an existing PR: review comments, failed checks, requested fixes, implementation, verification, and optional commit/push when explicitly requested.
agent: code-workflow-orchestrator
subtask: false
---

Run the existing-PR follow-up workflow for: $ARGUMENTS

Treat this as follow-up work for the existing PR by default. Work on the same PR branch. Do not open a separate PR unless the user explicitly asks for a separate PR.

Inspect current branch/status/diff and PR context when available. Orchestrate the needed subagents. Continue automatically through safe stages. Return one consolidated markdown report with green/yellow/red stage status.

Commit or push only if the user explicitly asked to commit/push/update the PR branch.
