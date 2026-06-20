---
description: Implement an already planned UI/web redesign using the existing frontend architecture.
agent: frontend-ui-implementer
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

Implement the planned UI/web redesign for: $ARGUMENTS

Before editing, read project rules and inspect existing components/styles. Reuse current architecture. Keep the diff focused. New dependencies and new design systems are gated actions.


Read the detailed UI policy file defined in AGENTS.md when it exists.
