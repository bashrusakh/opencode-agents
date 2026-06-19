# UI UX Pro Max / UUPM setup for OpenCode agents

Purpose: install UI UX Pro Max / UUPM as UI/web design intelligence for OpenCode workflows.

UUPM is not a component MCP server. It is used for design-system reasoning, layout density, visual hierarchy, palette, typography, forms, dashboards, responsive behavior, anti-patterns, and accessibility/pre-delivery checklists.

## Final role in this stack

```text
UI workflow:
  /ui-redesign
    -> ui-web-orchestrator
      -> ui-ux-auditor
      -> ui-redesign-planner + UUPM only after availability check
      -> frontend-ui-implementer + UUPM-derived plan when it was clearly adopted by the planner
      -> accessibility-reviewer
      -> tester

Component sources:
  1. Existing project components
  2. Official shadcn MCP + standard shadcn registry
  3. Official shadcn MCP + GitHub/public shadcn-compatible registries
  4. Jpisnice shadcn-ui-mcp-server + GitHub token
  5. Manual implementation

Design intelligence:
  UUPM / UI UX Pro Max
```

## Install option A: UUPM CLI

Use this when you want UUPM to install/configure the assistant integration itself.

```bash
npm install -g uipro-cli
cd /path/to/project
uipro init --ai opencode
```

Before running this in an existing repository:

```bash
git status --short
find . -maxdepth 3 \( -name 'AGENTS.md' -o -path './.opencode/*' -o -path './.claude/*' \) -print
```

After installation:

```bash
git status --short
find . -maxdepth 4 \( -iname '*uupm*' -o -iname '*ui-ux*' -o -path './.opencode/*' -o -path './.claude/*' \) -print
```

Report any files created or modified before continuing.

## Install option B: project-local skill/reference only

Use this when the project should keep UUPM files local and reviewable.

```bash
mkdir -p .opencode/skills
# Install UUPM using its documented OpenCode method or copy the generated skill/reference files here.
```

Do not guess the file layout. If the CLI generated a different structure, preserve it and report what was created.

## Install option C: global user-level install

Use this only when the normalized deliverable is global UUPM availability across projects.

Expected location for local user skills in this setup:

```text
~/.config/opencode/skills/
```

Back up any existing skill with the same name before replacing it.

## Agent usage rules

Allowed to use UUPM directly:

```text
ui-web-orchestrator
ui-ux-auditor
ui-redesign-planner
frontend-ui-implementer
accessibility-reviewer
```

Do not use UUPM directly for ordinary bugfix/review/test/devops work unless the normalized deliverable targets it for UI/design guidance.

## Availability check for agents

Agents must not assume UUPM is installed. Treat it as available only if a runtime skill is exposed, a project or installed OpenCode `ui-ux-pro-max/SKILL.md` exists, project docs say it is installed, or an allowed `uipro` CLI check succeeds. If unavailable or not checked, continue without UUPM and report that status. Do not install UUPM during normal UI work; use `/uupm-setup` only when setup is requested.

## Gated actions

Stop and ask before applying UUPM guidance that requires:

- new dependencies
- new fonts
- new assets
- icon library changes
- animation library changes
- generated persistent design-system files
- broad scope rewrite
- project-wide theming change outside the requested scope
- API/data/auth/routing behavior changes

No approval is needed for read-only UUPM lookup or for applying guidance that only changes local layout, spacing, density, hierarchy, accessible labels, focus states, or responsive behavior within the existing project style system.

## Final report format

```markdown
## UUPM setup / usage report

✅/⚠️/❌ Installed or available:
✅/⚠️/❌ Files changed:
✅/⚠️/❌ UUPM used for:
✅/⚠️/❌ Gated-action checks triggered:

Notes:
- ...
```
