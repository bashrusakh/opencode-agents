# UUPM / UI UX Pro Max usage notes

Use UUPM for design intelligence only.

Good uses:
- UI/web redesign plans
- theme direction and tokens
- layout density and visual hierarchy
- forms/settings/admin screens
- dashboard/table guidance
- responsive and accessibility checklists

Do not use UUPM as:
- component MCP
- dependency installer
- permission to create a new design system
- replacement for existing project components
- authority over AGENTS.md / CONTRIBUTING.md

Preferred agent routing:
- ui-web-orchestrator coordinates the flow
- ui-redesign-planner uses UUPM for planning only after availability check
- frontend-ui-implementer applies only approved/relevant guidance
- accessibility-reviewer uses UUPM as an extra checklist


## Availability check for agents

Agents must not assume UUPM is installed. Treat it as available only if a runtime skill is exposed, a project or installed OpenCode `ui-ux-pro-max/SKILL.md` exists, project docs say it is installed, or an allowed `uipro` CLI check succeeds. If unavailable or not checked, continue without UUPM and report that status. Do not install UUPM during normal UI work; use `/uupm-setup` only when setup is requested.
