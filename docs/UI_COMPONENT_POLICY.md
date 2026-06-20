# UI component / MCP / UUPM policy

This file is the detailed UI component-source and design-intelligence policy for UI/web work. `AGENTS.md` keeps the mandatory short policy.

Agents should read the first existing detailed UI policy file from:

1. `.opencode/docs/UI_COMPONENT_POLICY.md`
2. `~/.config/opencode/docs/UI_COMPONENT_POLICY.md`
3. `docs/UI_COMPONENT_POLICY.md`

The install scripts copy this file to the matching OpenCode docs directory for global or project-local installs.


## 0. Behavioral contract check

For UI/web work, first preserve the user-facing contract, not the raw schema shape. Before choosing a component, control, MCP source, or implementation path, identify:

- what the user is trying to do
- how the user naturally provides or chooses the value
- where valid values come from: user input, app state, provider/model capabilities, files, existing config, or another source
- which existing project pattern already handles this kind of interaction
- whether the proposed UI would expose raw/internal/manual values that normal users should not need to know

Do not turn guided, capability-derived, state-derived, or project-patterned interactions into raw/manual/editor workflows unless the normalized request explicitly asks for that.

## 1. Source order

For UI/web work, use this source order:

1. existing project components, tokens, styles, layout primitives, and design system
2. official shadcn MCP with the standard shadcn registry
3. official shadcn MCP with GitHub/public shadcn-compatible registries
4. Jpisnice shadcn-ui-mcp-server with GitHub token as secondary/reference MCP
5. manual implementation when no existing or registry component fits

Existing project components always win over external sources. Do not force shadcn into projects that clearly do not use it.

## 2. MCP availability and fallback

Treat an MCP/component source as usable only after it is confirmed by visible tools or config.

- Official shadcn MCP is available only when `shadcn_*` tools are exposed or project/OpenCode config visibly defines it.
- Public/GitHub shadcn MCP is available only when `shadcn_public_*` tools or matching config are exposed.
- Jpisnice MCP is available only when its tools/config are exposed and a local GitHub token is already configured.
- Do not assume an MCP exists from instructions alone.
- If a source level is unavailable, skip to the next source level without asking.
- Ask only when the next source requires secrets, new config, new dependencies, or broad design-system changes.

## 3. Secret-backed sources

Jpisnice/GitHub-token usage is a secret-backed source. Before using a secret-backed source that is not already approved by the current normalized task, stop and state:

- source name
- expected secret variable/location/name, without revealing values
- intended read-only or write action
- target registry/repository/source
- relevant risk

Use the source only when the gated-action rule allows that exact source/action. Never hardcode tokens. Never print token values.

## 4. Registry rules

- Standard shadcn registry use is allowed when official shadcn MCP is available and it fits the project stack.
- GitHub/public shadcn-compatible registries are allowed when the user/project names a public shadcn-compatible registry, or visible tools/config can inspect it without unapproved secrets.
- Jpisnice MCP is allowed for source, demos, metadata, blocks, and cross-framework shadcn variants.
- Local/private/authenticated non-GitHub registry setup is a gated action.
- Registry items that add dependencies, icon sets, fonts, packages, config rewrites, persistent design-system files, or broad design-system changes are gated actions.
- If a registry item conflicts with existing project architecture, stop and report the conflict instead of forcing it in.

## 5. UUPM / UI UX Pro Max

UUPM is design intelligence, not a component source and not an MCP component server.

Use UUPM only after the UUPM availability check confirms it is available. Use it for UI/web redesign plans, density, hierarchy, forms, settings, dashboards, typography, palette, responsive behavior, accessibility guidance, and anti-pattern checks.

UUPM output is advisory. Project rules, existing components, accessibility, implementation constraints, and the user request win.

Do not persist UUPM-generated design-system files, page overrides, assets, fonts, dependencies, or new design-system layers unless that exact persistence is allowed by the gated-action rule.

## 6. UUPM availability check

Treat UUPM as available only when at least one of these is confirmed:

- the current runtime/tool list exposes a skill/tool named `ui-ux-pro-max`, `uupm`, or an explicitly equivalent UI UX Pro Max skill
- the project contains `.claude/skills/ui-ux-pro-max/SKILL.md`, `.opencode/skills/ui-ux-pro-max/SKILL.md`, or `.agents/skills/ui-ux-pro-max/SKILL.md`
- the installed OpenCode skills directory contains `~/.config/opencode/skills/ui-ux-pro-max/SKILL.md`
- project docs state that UUPM is installed and should be used
- the `uipro` CLI is available and checking it is allowed by permissions

Do not assume UUPM is installed. Do not install UUPM during normal UI work. Use `/uupm-setup` only when setup is the normalized deliverable.

If UUPM is unavailable or cannot be checked, continue without it and report `UUPM: not used / not available / not checked`.

## 7. Final UI report requirements

Final UI reports should mention:

- component source used
- MCP source used or skipped
- UUPM status and guidance used/rejected
- registry items adopted/skipped
- gated actions triggered, approved, or avoided
- whether any dependency/config/design-system change was requested or avoided
