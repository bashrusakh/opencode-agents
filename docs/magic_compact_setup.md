# Magic Compact setup for OpenCode

This is a **manual setup reference**, not OpenCode runtime policy. The agent-pack installers do not install the external plugin or copy this document into `~/.config/opencode` / `.opencode/`.

Magic Compact is an external context-compression plugin: https://github.com/aerovato/magic-compact

The bundled runtime skill `skills/magic-compact/SKILL.md` governs semantic trigger/usage behavior after the plugin is available. Installation remains an explicit tooling/configuration change.

## Agent installation procedure

1. Confirm that the user requested/authorized Magic Compact installation or update. Inspect the installed OpenCode CLI and current plugin state:

   ```bash
   opencode plugin --help
   opencode plugin list
   ```

2. Use the syntax supported by the installed OpenCode version. Current OpenCode CLI documentation exposes package-plugin installation as:

   ```bash
   opencode plugin add magic-compact
   ```

   The Magic Compact upstream README also documents the older OpenCode form:

   ```bash
   opencode plugin magic-compact --global
   ```

   Prefer local `opencode plugin --help` over assuming either form.

3. Only if the actual install fails with `No versions available`, apply the upstream troubleshooting override using the local CLI's supported command shape. Upstream currently shows:

   ```bash
   NPM_CONFIG_MIN_RELEASE_AGE=0 opencode plugin magic-compact --global
   ```

4. Do not pre-emptively delete caches. Upstream also suggests clearing `~/.cache/opencode/packages/magic-compact*` in some failure cases; because deletion is destructive, inspect the exact matching entries first and keep cleanup scoped only to Magic Compact under the applicable gate.

5. Verify installation from the runtime rather than from exit status alone:

   ```bash
   opencode plugin list
   ```

   Reload/restart OpenCode if the current session does not pick up newly installed plugins. Confirm that the runtime exposes the expected Magic Compact surfaces: `/magic-compact`, `/magic-trim` (OpenCode), `/magic-stats` (OpenCode), and the `read_omitted_content` tool after content has been omitted.

## Usage model

Do not compact on a timer or fixed turn count. The agent pack defines a semantic **context-pressure condition** in root `AGENTS.md`. When that condition is met, use the bundled `magic-compact` skill:

- historical bulky tool I/O is the main pressure -> prefer `/magic-trim [N]`;
- broader settled assistant history is the pressure and a semantic stage boundary is reached -> consider `/magic-compact [N]`;
- unresolved exact reasoning/evidence still matters -> do not compact yet.

If slash commands are user-entry-only in the active OpenCode surface, the agent should request the selected command once rather than claim it executed compaction itself.

## Sources checked for this package release

- Magic Compact upstream README: https://github.com/aerovato/magic-compact
- OpenCode plugin CLI documentation: https://opencode.ai/v2/docs/cli/commands/
- OpenCode plugin documentation: https://opencode.ai/v2/docs/plugins
