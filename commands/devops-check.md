---
description: "Inspect Docker, systemd, CI, deployment, environment, service logs, permissions, or runtime configuration."
agent: devops
subtask: false
---

Inspect the DevOps/runtime concern for: $ARGUMENTS

Follow the active `AGENTS.md` and devops role contract.

Start with read-only diagnostics and current evidence. Identify the failing layer, relevant config/service/log path, and the smallest operational change if one is actually required.

Apply operational/config changes only when they are clearly within the normalized request and authorization scope. For any proposed change, include focused verification and a realistic rollback/recovery path. Never expose or invent secrets.
