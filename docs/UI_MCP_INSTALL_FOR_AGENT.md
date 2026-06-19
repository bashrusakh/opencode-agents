# UI MCP setup for OpenCode agents

Final stack:

1. Official shadcn MCP + standard shadcn registry.
2. Official shadcn MCP + GitHub/public shadcn-compatible registries.
3. Jpisnice shadcn-ui-mcp-server + GitHub token.

Do not set up a local shadcn registry/mirror.
Private/authenticated non-GitHub registry setup is a gated action unless the normalized deliverable targets it.
Do not hardcode tokens in repo files.

## Source order for UI work

Use this order:

1. Existing project components, tokens, theme files, and layout primitives.
2. Official shadcn MCP with the standard shadcn registry.
3. Official shadcn MCP with GitHub/public shadcn-compatible registries.
4. Jpisnice shadcn-ui-mcp-server as secondary/reference MCP for source, demos, metadata, blocks, and cross-framework shadcn variants.
5. Manual implementation when no existing/registry component fits.

Ask for approval before adding new dependencies, icon sets, font packages, broad config rewrites, or a new design-system layer.

## Step 1 — Backup current OpenCode config

Before editing config:

```bash
mkdir -p ~/.config/opencode/backups
cp -a ~/.config/opencode/opencode.json ~/.config/opencode/backups/opencode.json.$(date +%Y%m%d-%H%M%S) 2>/dev/null || true
cp -a ~/.config/opencode/opencode.jsonc ~/.config/opencode/backups/opencode.jsonc.$(date +%Y%m%d-%H%M%S) 2>/dev/null || true
```

## Step 2 — Configure official shadcn MCP

Use OpenCode local MCP config with the official shadcn command. The exact config file may differ by setup; keep existing keys and merge carefully.

Example JSONC fragment:

```jsonc
{
  "mcp": {
    "shadcn": {
      "type": "local",
      "command": ["npx", "-y", "shadcn@latest", "mcp"],
      "enabled": true,
      "timeout": 10000
    }
  }
}
```

The standard shadcn registry needs no extra `components.json` registry entry.

## Step 3 — Enable GitHub/public registries for official shadcn MCP

For public GitHub registries, prefer the official shadcn registry/GitHub flow.

Rules:

- Only use public shadcn-compatible registries.
- Private repositories or authenticated private registry URLs are gated sources unless the normalized deliverable targets them.
- Validate that registry items fit the current project stack before installing.
- Do not install items that introduce dependencies/config rewrites without approval.

A public GitHub registry can be used via shadcn-compatible `owner/repo/item` references or configured registry namespaces when the project needs them.

## Step 4 — Configure Jpisnice shadcn-ui-mcp-server

Jpisnice is the secondary/reference MCP. Use it for:

- component source code
- demos and usage examples
- metadata/dependencies
- blocks
- React/Svelte/Vue/React Native shadcn variants
- fallback lookup when official shadcn MCP is insufficient

Use a GitHub token for rate limits. Do not commit the token.

Recommended local secret:

```bash
export GITHUB_PERSONAL_ACCESS_TOKEN=ghp_xxx
```

Example JSONC fragment:

```jsonc
{
  "mcp": {
    "shadcn_public": {
      "type": "local",
      "command": [
        "sh",
        "-lc",
        "test -n \"$GITHUB_PERSONAL_ACCESS_TOKEN\" || { echo \"GITHUB_PERSONAL_ACCESS_TOKEN is required for shadcn_public MCP\" >&2; exit 1; }; npx -y @jpisnice/shadcn-ui-mcp-server --github-api-key \"$GITHUB_PERSONAL_ACCESS_TOKEN\""
      ],
      "enabled": true,
      "timeout": 15000
    }
  }
}
```

The server name `shadcn_public` is intentional so its tools are separate from the official `shadcn` MCP tools.

## Step 5 — Optional UI UX Pro Max / UUPM skill

Use it only as design intelligence for:

- visual hierarchy
- density
- palette
- typography
- settings screens
- forms
- dashboards
- responsive behavior
- accessibility checklist

Do not let it create persistent design-system files unless the normalized deliverable targets it for a reusable project design system.

## Step 6 — Verify

After setup:

```bash
opencode
```

Then verify MCP tools are visible in OpenCode. Tool names are usually prefixed by the MCP server name, for example `shadcn_*` and `shadcn_public_*` depending on the configured server name.

## Final report format

```md
| Check | Status | Notes |
|---|---|---|
| OpenCode config backed up | ✅/⚠️/❌ | ... |
| official shadcn MCP configured | ✅/⚠️/❌ | ... |
| standard shadcn registry available | ✅/⚠️/❌ | ... |
| GitHub/public registry flow documented | ✅/⚠️/❌ | ... |
| Jpisnice MCP configured with token | ✅/skipped/⚠️/❌ | ... |
| local/private registry avoided | ✅/⚠️/❌ | ... |
| MCP tools visible in OpenCode | ✅/⚠️/❌ | ... |
```

Do not claim completion if OpenCode config was not backed up or MCP visibility was not verified.
