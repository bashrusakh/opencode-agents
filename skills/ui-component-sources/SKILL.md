---
name: ui-component-sources
description: Use when UI work needs a component-source or design-integration choice beyond existing project primitives. Owns the pack-specific external source ordering and related integration constraints; generic UI roles consume this policy.
---

# UI component sources

## Source order

When component sourcing is materially relevant, use this order without treating unavailable integrations as blockers:

1. existing project components/tokens/styles/layout primitives;
2. official shadcn MCP/standard registry;
3. official shadcn MCP with public GitHub-compatible registries;
4. Jpisnice shadcn-ui MCP as a secondary/reference source;
5. manual implementation.

External sources are usable only when current runtime/project evidence shows them visible/configured. Existing project components win. Skip unavailable source levels without asking. Stop only when the next source requires a secret/private registry, new dependency/configuration, generated asset/design-system change, or another root gate. Do not infer availability from setup documentation alone.

## Advisory design integration

UUPM is advisory design input, not a component source or task authority. Use it only when current runtime/project evidence exposes the relevant skill/tool/integration. Project behavior, architecture, accessibility, established components, and task-semantic authority remain governing constraints.

## Role consumption

Planning roles may use this policy to recommend a compatible source. Implementation roles consume the accepted/requested source choice and must not silently choose a different provider or add gated configuration/dependencies. Audit/review roles may inspect whether the chosen external source was applicable and whether its output satisfies the actual project/behavior/accessibility contract; source claims are not proof of the final result.
