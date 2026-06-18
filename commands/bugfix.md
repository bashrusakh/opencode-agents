---
description: Run a full bugfix workflow in one request: investigate, fix, verify, and review when useful.
agent: code-workflow-orchestrator
subtask: false
---

Run the bugfix workflow for: $ARGUMENTS

Do not make the user manually run every agent. Orchestrate the needed subagents, continue automatically through safe stages, and return one consolidated markdown report with green/yellow/red stage status.

Use @explore when the code path is not obvious. Use @tester to reproduce/verify when useful. Use @debugger for root cause and the smallest right-level fix. Use @fix-level-reviewer or @reviewer for non-trivial changes.

Do not commit, push, open PRs, or publish anything unless the user explicitly asked for that action.
