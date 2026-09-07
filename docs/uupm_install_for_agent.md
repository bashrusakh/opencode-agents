# UI UX Pro Max / UUPM setup for OpenCode agents

Use this only when UUPM installation/configuration is the normalized deliverable. The root `AGENTS.md` controls authorization, and `docs/ui_component_policy.md` defines UUPM's role in UI work.

UUPM is design intelligence for UI/UX reasoning; it is not the component MCP server.

## Preferred CLI setup

Current upstream CLI package installs the `uipro` command:

```bash
npm install -g ui-ux-pro-max-cli
cd /path/to/project
uipro init --ai opencode
```

Before installing into an existing repository, inspect current Git/OpenCode/skill state. After running the initializer, inspect the exact files it created/changed and preserve its upstream-generated structure rather than guessing a local layout.

Do not run `--force` or overwrite an existing skill/config blindly. If an existing installation is present, compare/update deliberately.

## Project-local vs global

Default to the scope requested by the user/project. Do not silently turn project-local setup into global setup.

For a project-local installation, use the structure generated/documented by the current UUPM OpenCode integration. Do not hand-create guessed wrapper files.

Use a global install only when the deliverable explicitly requires UUPM across projects. Verify the actual target path created by the current CLI/runtime rather than assuming a stale path from older releases.

## Usage boundary

UUPM may be used by UI roles when relevant and available. It should not be pulled into ordinary backend bugfix/review/test/DevOps work unless the requested deliverable genuinely needs UI/design guidance.

Normal UI work must not auto-install or auto-update UUPM. Setup/update is a separate operation.

## Gated scope expansion

Follow the root gate before UUPM-driven work introduces scope not already authorized, including new dependencies, fonts/assets/icon or animation libraries, persistent generated design-system artifacts, broad project-wide theming, or product/API/data/routing changes.

Read-only design guidance within the existing authorized UI scope does not require an extra confirmation ritual.

## Verify

After setup:

- confirm the `uipro` command/integration succeeded;
- confirm OpenCode exposes or can load the resulting `ui-ux-pro-max` skill;
- inspect/report exact files/config changed;
- do not claim availability solely because the CLI command exited successfully if OpenCode cannot see the integration.

## Final report

Report compactly:

- requested scope (project/global);
- detected prior installation;
- install/update command actually run;
- files/config created or changed;
- OpenCode skill visibility/verification;
- any gates/blockers or intentionally skipped scope expansion.
