---
description: Install or configure UI UX Pro Max / UUPM design-intelligence support for OpenCode.
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

Install or configure UI UX Pro Max / UUPM for OpenCode: $ARGUMENTS

Use `docs/UUPM_INSTALL_FOR_AGENT.md` as the source of truth.

Do not overwrite existing OpenCode/project config without backups. Prefer project-local installation unless the normalized deliverable targets it for global install. UUPM is design intelligence only, not a component MCP server. Persisting generated design-system files, fonts, assets, or new dependencies is a gated action unless persistence is the normalized deliverable.

Return one consolidated markdown report with green/yellow/red stage status and exact commands/results.
