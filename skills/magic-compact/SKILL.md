---
name: magic-compact
description: Use when the root context-pressure condition is met or the user explicitly requests Magic Compact setup/usage. Covers trigger evaluation, trim-vs-compact choice, omitted-content recovery, and safe OpenCode installation. Root AGENTS.md remains authoritative.
---

# Magic Compact context hygiene

Magic Compact is an external OpenCode plugin. This skill defines when context reduction is justified and how to choose the least-destructive mechanism. It does not make compaction periodic and does not grant permission to install external tooling.

Upstream: https://github.com/aerovato/magic-compact

## Goal before mechanism

Treat context hygiene as a semantic goal: preserve the active task's reasoning quality by reducing settled historical context that no longer needs to remain verbatim. Do not start from the command name.

The root **context-pressure condition** is the trigger. Evaluate it opportunistically at a natural semantic boundary (for example after a completed exploration, implementation, verification, or review stage) or when the runtime reports context pressure. Do not run extra tools merely to measure context, and never trigger only because a session is old, long, or has reached a fixed number of turns.

Before reducing context, identify what the active stage still depends on exactly: unresolved hypotheses, authoritative constraints, current state/ref/SHA identity, pending/failed tool activity, user decisions not yet reflected in durable state, and evidence whose wording or provenance still matters. A reduction path must preserve or make recoverable what remains material.

## Choose the path

Prefer the least semantic transformation that satisfies the context-hygiene goal:

1. **No reduction** when the root trigger is absent, evidence of pressure is uncertain, or exact unresolved history is still materially required.
2. **`/magic-trim [N]` first** when pressure is primarily bulky completed tool I/O. Upstream currently labels this OpenCode command experimental. Trim does not summarize ordinary user/assistant messages. Choose `N` by the active unresolved stage: preserve recent tool I/O that is still materially useful rather than using a ritual fixed value.
3. **`/magic-compact [N]`** when pressure materially persists beyond tool I/O, or settled assistant-turn history itself dominates the active working context, and a natural semantic boundary has been reached. Preserve enough recent assistant turns to keep the unresolved stage exact; do not compact across active reasoning merely to save tokens.

User messages are preserved verbatim by Magic Compact, but assistant turns can be summarized. Therefore authoritative user intent is safer than workflow-derived reasoning across compaction; still keep unresolved authority/provenance/state questions out of a compaction boundary until they are reconciled.

If the current runtime exposes a native executable command surface for these commands, use it within the active role/gates. If the commands are available only as user-entered OpenCode commands, do **not** pretend to have executed them: ask once for the exact command that matches the selected path and continue after the resulting session state is visible.

## Omitted content

Magic Compact can expose `read_omitted_content` for pruned tool input/output. Use it only when the exact omitted material is still needed and cannot be more correctly reproduced from current state.

For mutable repository/runtime evidence, prefer a fresh read/re-run against the current state identity over resurrecting stale cached output. Retrieval restores old evidence; it does not make that evidence fresh.

## Installation / update

Installing or updating Magic Compact changes external tooling/global OpenCode configuration and remains subject to root gates. Do it only when the normalized user request authorizes that setup action.

1. Inspect the local CLI contract and current state first:

   ```bash
   opencode plugin --help
   opencode plugin list
   ```

2. Use the plugin syntax actually supported by that installed OpenCode version. Current OpenCode documentation uses:

   ```bash
   opencode plugin add magic-compact
   ```

   Magic Compact's upstream README also documents the older compatible form:

   ```bash
   opencode plugin magic-compact --global
   ```

   Do not guess between forms; follow local `--help`.

3. If the install specifically fails with `No versions available`, upstream documents this retry:

   ```bash
   NPM_CONFIG_MIN_RELEASE_AGE=0 opencode plugin magic-compact --global
   ```

   Adapt only the command shape required by the local CLI; do not set the environment override pre-emptively.

4. Upstream also documents clearing matching Magic Compact package cache entries as troubleshooting. Cache deletion is destructive: inspect the exact matching entries first and do not delete them silently or broaden cleanup beyond Magic Compact.

5. Verify the installed state with the local plugin-list/config surface and, in a fresh/reloaded OpenCode runtime if needed, verify that `/magic-trim`, `/magic-compact`, `/magic-stats`, and `read_omitted_content` appear as expected. A successful package command alone is not proof that the current session loaded the plugin.

## Failure handling

If Magic Compact is unavailable, installation is not authorized, command execution is user-only, or compaction would endanger unresolved reasoning/evidence, continue without pretending context reduction occurred. Report the precise limitation only when it materially affects the task.
