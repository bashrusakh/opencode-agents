# UI MCP setup for OpenCode agents

Use this only when UI MCP setup/configuration is the normalized deliverable. The root `AGENTS.md` and `docs/ui_component_policy.md` remain authoritative for gates and UI source selection.

Target stack:

1. official shadcn MCP as the primary registry/component MCP;
2. public/GitHub shadcn-compatible registries through the official shadcn registry mechanism when needed;
3. Jpisnice `@jpisnice/shadcn-ui-mcp-server` as optional secondary/reference MCP;
4. UUPM configured separately as design intelligence, not as the component MCP.

Do not hardcode secrets or overwrite unrelated OpenCode/project config.

## Step 1 — Inspect and back up the target config

Determine whether the requested scope is project-local or user/global before changing anything. Inspect existing OpenCode and `components.json` configuration and preserve unrelated keys.

Before modifying an existing OpenCode config, create a recoverable backup using the project's/user's normal mechanism. Do not claim setup complete if an existing config was overwritten without a recoverable copy.

## Step 2 — Configure official shadcn MCP

Prefer the current official shadcn CLI initializer for OpenCode rather than hand-authoring another client's config shape:

```bash
npx shadcn@latest mcp init --client opencode
```

The shadcn MCP uses the project's `components.json` registry configuration and can work with the default registry plus compatible third-party registries.

After init, inspect the resulting OpenCode config/diff instead of assuming the generated shape. Preserve existing unrelated MCP entries.

For manual/debug reference, the server itself is launched by the shadcn CLI's MCP command:

```bash
npx shadcn@latest mcp
```

Do not run `shadcn init` merely to set up MCP unless the project actually needs shadcn project initialization and that broader project mutation is authorized.

## Step 3 — Additional public/GitHub registries

Configure additional registries through the project's `components.json` using the current shadcn-compatible registry format when the task actually needs them.

Public GitHub registry sources may work without authentication. Private/authenticated registries require the root secrets/private-source gate. Validate registry items against the existing project stack before installation; installing an item may itself trigger dependency/config gates.

## Step 4 — Optional Jpisnice secondary MCP

Current package/source:

```text
@jpisnice/shadcn-ui-mcp-server
```

Basic server invocation:

```bash
npx @jpisnice/shadcn-ui-mcp-server
```

A GitHub token raises GitHub API limits and is recommended when this secondary server will be used heavily. Use the environment variable rather than hardcoding a token:

```bash
export GITHUB_PERSONAL_ACCESS_TOKEN=<local-secret>
npx @jpisnice/shadcn-ui-mcp-server
```

The server also supports an explicit `--github-api-key` option, but do not place literal token values in repository/OpenCode config. If a secret-backed setup is not authorized, leave the secondary server unconfigured or use the non-token mode when that satisfies the requested setup.

Framework/library flags should be chosen from the actual project stack rather than hardcoded globally.

## Step 5 — UUPM remains separate

Use `docs/uupm_install_for_agent.md` only when UUPM setup is separately requested. UUPM provides design intelligence; it does not replace the component MCP.

## Step 6 — Verify

Restart/reload OpenCode as required by the current client and confirm that the configured MCP server(s) are visible and can perform a safe read-only registry query. Inspect the resulting config/diff and report any files changed by setup.

Do not claim completion based only on writing config.

## Final report

Report compactly:

- target scope (project/global);
- config backed up/created;
- official shadcn MCP status;
- additional registry/Jpisnice status when applicable;
- secret/private-source handling when applicable;
- verification result and exact files changed.
