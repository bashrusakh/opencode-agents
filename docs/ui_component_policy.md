# UI component / MCP / UUPM policy

The root `AGENTS.md` UI rules are normative. This file is the detailed source-selection and design-intelligence reference for UI/web work.

Agents should read the first applicable existing copy of this policy from the active project/OpenCode setup.

## 1. Preserve the user-facing contract

Before choosing a control/component/source, establish the relevant user-facing behavior:

- what the user is trying to do;
- how the user naturally supplies/selects the value;
- where valid values come from;
- which existing project pattern handles the interaction;
- whether the proposal would expose raw/internal/manual values normal users should not need.

Do not map storage/schema/API types directly to raw UI affordances. Preserve the existing affordance class unless the normalized request intentionally changes it.

## 2. Component/source order

Use this order when it fits the project:

1. existing project components, tokens, styles, layout primitives, and design system;
2. official shadcn MCP/default registry when the project is shadcn-compatible and the MCP is actually available;
3. additional public/GitHub shadcn-compatible registries configured through the official shadcn flow;
4. Jpisnice `shadcn-ui-mcp-server` as a secondary/reference source when available;
5. manual implementation when no suitable existing/registry component fits.

Existing project architecture wins. Do not force shadcn into a project that does not use/fit it.

## 3. Availability and fallback

Treat a component/MCP source as available only when visible tools/config/runtime evidence confirms it. Instructions alone do not prove availability.

If a source is unavailable, continue to the next appropriate source without asking. Stop only when the next step itself triggers a root gate, such as secrets/private resources, new config/dependencies, or broad design-system changes.

## 4. Secret/private sources

Never print or hardcode tokens. For a source that requires a secret/private registry/account action not already authorized, follow the root gate and state only the variable/location name, intended action, target source, and material risk — never the secret value.

Public registry use that requires no new secret/config still remains subject to dependency/config-change gates when installing an item would alter the project materially.

## 5. UUPM / UI UX Pro Max

UUPM is design intelligence, not a component MCP server or component source.

Use it only after availability is confirmed. It may inform hierarchy, density, typography, palette, forms/settings, dashboards, responsive behavior, accessibility guidance, and anti-pattern checks.

UUPM guidance is advisory. Current project rules/components, accessibility, implementation constraints, and the user's requested outcome win.

Do not persist UUPM-generated design systems/assets/fonts/dependencies/project-wide theme changes unless that persistence is within the authorized scope.

## 6. UUPM availability

Treat UUPM as available when current runtime/project/user-level evidence exposes the `ui-ux-pro-max` skill/tool or the documented `uipro` CLI integration. Do not assume availability from this package text alone.

Do not install/update UUPM during ordinary UI work. Setup/update belongs to the explicit UUPM setup workflow.

If unavailable or not verifiable, continue without it and report that fact only when it matters to the result.

## 7. Reporting

Report only applicable source decisions. When useful, mention:

- existing/project component source used;
- external MCP/registry source actually used or materially unavailable;
- UUPM guidance actually used/rejected;
- dependency/config/design-system scope changes or gates that affected the task.

Do not emit a fixed checklist full of `skipped` rows.
