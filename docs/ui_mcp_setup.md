# UI MCP setup for OpenCode

This is a **manual setup reference**, not an OpenCode runtime policy or custom command. The package installers do not copy it into `~/.config/opencode` or `.opencode/`.

Use it when you intentionally want to configure the UI component MCP stack for OpenCode.

The commands below reflect the package procedure at this release. If the tooling has changed since this package was published, confirm the current upstream CLI syntax before making changes.

## Scope and target stack

Decide first whether the setup is project-local or user/global. Inspect the existing OpenCode configuration and, when relevant, the project's `components.json`. Preserve unrelated keys and existing MCP entries.

Recommended stack, in preference order when applicable:

1. official shadcn MCP as the primary registry/component MCP;
2. public/GitHub shadcn-compatible registries through the official shadcn registry mechanism when needed;
3. optional `@jpisnice/shadcn-ui-mcp-server` as a secondary/reference MCP;
4. UI UX Pro Max (UUPM) remains separate design intelligence, not the component MCP.

Do not hardcode secrets or overwrite unrelated configuration. Do not broaden a project-local setup into a global one unless that is intentional.

## Procedure

1. Inspect the current OpenCode/project configuration and choose the intended install scope.
2. Before modifying an existing OpenCode config, create a recoverable backup.
3. Prefer the current official shadcn initializer for OpenCode:

   ```bash
   npx shadcn@latest mcp init --client opencode
   ```

   Do not run broader `shadcn init` merely to set up MCP unless project initialization is separately intended.
4. Inspect the generated config/diff. The shadcn MCP uses the project's `components.json` registry configuration. The default shadcn registry does not need an extra `registries` entry; add compatible public/GitHub registries there only when needed.
5. For manual/debug reference, the shadcn MCP server command is:

   ```bash
   npx shadcn@latest mcp
   ```

6. Configure the optional Jpisnice secondary MCP only when wanted:

   ```bash
   npx @jpisnice/shadcn-ui-mcp-server
   ```

   If a GitHub token is used to raise API limits, pass it through the environment rather than storing a literal token in repository/OpenCode config:

   ```bash
   export GITHUB_PERSONAL_ACCESS_TOKEN=<local-secret>
   npx @jpisnice/shadcn-ui-mcp-server
   ```

   Choose framework/library flags from the actual project stack rather than hardcoding them globally.
7. Configure UUPM separately using [`uupm_setup.md`](uupm_setup.md) when you intentionally want that design-intelligence integration.
8. Reload/restart OpenCode if required, then verify the configured MCP server(s) with a safe read-only registry query. Inspect the resulting config/diff and exact changed files; writing config alone is not proof that setup succeeded.

## Verification checklist

Confirm:

- intended scope (project or global);
- backup exists when existing config was modified;
- official shadcn MCP is visible and responds;
- any additional registry/Jpisnice source is visible when configured;
- secrets are not stored literally in tracked or OpenCode config;
- unrelated configuration is unchanged;
- exact changed files/config are understood.
