# shadcn registry notes

Preferred UI component-source order when it fits the project:

1. Existing project components/design system.
2. Official shadcn MCP + default registry.
3. Additional public/GitHub shadcn-compatible registries through the official shadcn registry mechanism.
4. Jpisnice `shadcn-ui-mcp-server` as optional secondary/reference source.
5. Manual implementation when no suitable component source fits.

The default shadcn registry does not need an extra `registries` entry in `components.json`.

Additional registries are configured in `components.json` using the current shadcn-compatible format. Private/authenticated registries and secrets are subject to the root gate. Installing a registry item may separately trigger dependency/config-change gates.
