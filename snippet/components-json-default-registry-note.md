# shadcn registry notes

Final stack:

1. Official shadcn MCP + standard shadcn registry.
2. Official shadcn MCP + GitHub/public shadcn-compatible registries.
3. Jpisnice shadcn-ui-mcp-server + GitHub token.

The standard shadcn registry needs no extra `registries` entry in `components.json`.

For GitHub/public registries, use public shadcn-compatible repositories only. Local/private/authenticated registry setup is a gated action.
