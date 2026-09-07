---
description: "Install or configure the supported UI MCP stack for OpenCode using the package setup guide."
agent: devops
subtask: false
---

Configure the UI MCP stack for OpenCode: $ARGUMENTS

Follow the active `AGENTS.md`, devops role contract, and the applicable installed/project `ui_mcp_install_for_agent.md` as the setup source of truth.

Inspect existing OpenCode/project configuration first. Preserve unrelated settings and do not overwrite config, credentials, or registry definitions blindly. Treat secrets/private registry/account actions according to the root gate.

Configure only the UI MCP components requested/supported by the setup guide. Keep UI UX Pro Max/UUPM separate: it is design intelligence, not the component MCP server.

Report exactly what was detected, changed, left unchanged, and how the resulting MCP setup was verified.
