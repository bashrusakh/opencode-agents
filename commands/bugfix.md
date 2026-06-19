---
description: "Run a full bugfix workflow in one request: investigate, fix, verify, and review according to normalized intent."
agent: code-workflow-orchestrator
subtask: true
---

Run the bugfix workflow for: $ARGUMENTS

Do not make the user manually run every agent. Orchestrate the needed subagents, continue automatically through safe stages, and return one consolidated markdown report with green/yellow/red stage status.

Use @explore when the code path is not identified. Use @tester when reproduction or verification is needed. Use @debugger for root cause and the smallest right-level fix. Use @fix-level-reviewer or @reviewer for diffs touching shared behavior, security, data handling, API contracts, concurrency, or logic with edge cases/state transitions not obvious from one local function.

Do not commit, push, open PRs, or publish anything unless the gated-action rule allows that exact action.
