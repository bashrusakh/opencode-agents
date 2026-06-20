---
description: "Handle follow-up work for an existing PR: review comments, failed checks, requested fixes, implementation, verification, and optional commit/push when the gated-action rule allows that exact action."
agent: code-workflow-orchestrator
subtask: true
---

## Behavioral Contract Check

For any user-facing UI/config/API/workflow behavior change, do not implement only the data plumbing. Before planning or editing, summarize:

- user-facing action
- value source
- valid-value domain
- existing project pattern to inspect
- whether raw/internal/manual values would be exposed to normal users

Do not derive behavior directly from schema/storage/API type. Preserve the existing affordance class unless the normalized request explicitly asks for a raw/manual/editor workflow.

## Persistent Planning Mode

For long-running, multi-session, or multi-agent work, use `plans/<plan>/` as durable state. Read existing plan artifacts before continuing. Do not create arbitrary markdown reports. Use compact digests and update canonical plan/docs artifacts when the command is responsible for planning state.

Run the existing-PR follow-up workflow for: $ARGUMENTS

Treat this as follow-up work for the existing PR by default. Work on the same PR branch. Creating a separate PR is a gated action; proceed only when separate-PR creation is the clear normalized deliverable and the gated-action rule allows it.

Inspect current branch/status/diff and PR context. If PR metadata is unavailable, report the missing source instead of guessing. Orchestrate the needed subagents. Continue automatically through safe stages. Return one consolidated markdown report with green/yellow/red stage status.

Commit or push only when the gated-action rule allows that exact commit/push/update action.
