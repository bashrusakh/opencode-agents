---
description: Inspect Docker, systemd, CI, deployment, env, service logs, permissions, or runtime configuration.
agent: devops
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

Inspect DevOps/runtime configuration for: $ARGUMENTS

Prefer read-only diagnostics first. Do not run destructive commands. Provide verification and rollback steps for proposed changes.
