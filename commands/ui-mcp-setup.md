---
description: "Configure the UI MCP stack: official shadcn MCP with standard registry, official shadcn MCP with GitHub/public registries, and Jpisnice shadcn-ui-mcp-server with GitHub token."
agent: devops
subtask: false
---

## Behavioral Contract Check

For any user-facing UI/config/API/workflow behavior change, do not implement only the data plumbing. Before planning or editing, summarize:

- user-facing action
- value source
- valid-value domain
- existing project pattern to inspect
- whether raw/internal/manual values would be exposed to normal users

Do not derive behavior directly from schema/storage/API type. Preserve the existing affordance class unless the normalized request explicitly asks for a raw/manual/editor workflow.

Configure the local UI MCP stack for OpenCode: $ARGUMENTS

Use `docs/UI_MCP_INSTALL_FOR_AGENT.md` as the source of truth.

Do not overwrite existing config without backups. Configure official shadcn MCP as the primary MCP engine using the standard shadcn registry. Allow official shadcn MCP to use GitHub/public shadcn-compatible registries. Configure Jpisnice shadcn-ui-mcp-server as secondary/reference MCP with a GitHub token via local secret. UI UX Pro Max/UUPM is configured separately by `/uupm-setup` and is design intelligence only. Local/private/authenticated registry setup is a gated action.

Return one consolidated markdown report with green/yellow/red stage status and exact commands/results.
