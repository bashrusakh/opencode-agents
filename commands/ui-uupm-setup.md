---
description: "Install or configure UI UX Pro Max / UUPM design-intelligence support for OpenCode using the package setup guide."
agent: devops
subtask: false
---

Install or configure UUPM for OpenCode: $ARGUMENTS

Follow the active `AGENTS.md`, devops role contract, and the applicable installed/project `uupm_install_for_agent.md` as the setup source of truth.

Inspect the existing OpenCode/project setup first. Preserve unrelated configuration and do not overwrite files/config blindly. Prefer the scope requested by the user/project; do not silently turn a project-local setup into a global install.

UUPM is design intelligence, not the component MCP server. Treat persisted generated design-system assets, fonts, dependencies, private resources, or other scope expansion under the root gate.

Report exactly what was detected, changed, left unchanged, and how availability was verified.
