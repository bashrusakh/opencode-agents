# OpenCode final config v27 — model-agnostic variant

Agents, commands, root `AGENTS.md`, `snippet/`, docs, and UI MCP/UUPM setup notes for OpenCode. This package does not ship a duplicate `global/AGENTS.md`; the root `AGENTS.md` is the single shipped rules file.

## Important

OpenCode uses `AGENTS.md` as the rules file. `agent.md` is not the primary OpenCode rules file and may be ignored by OpenCode/OpenChamber tooling.

## Model policy

This variant is provider-neutral:

```text
agents/*.md contain no model: frontmatter
there is no fixed provider-specific role-to-model table
agents use the active OpenCode model/provider from the current session/config/UI
workflow routing still selects the right role/agent, but it does not select a model provider
```

Use this while testing different providers. Change the active model/provider in OpenCode/OpenChamber config or UI; do not edit every agent file.

## Rule model

`AGENTS.md` is structured as:

```text
0. Philosophy and interpretation principles
1. Source of truth
2. Core behavior
3. Request normalization
4. Approval gates
5. Delegation and orchestration
6. Workflow routing
7. Implementation rules
8. Git, commit, PR, issue, and release discipline
9. Final reports
```

Core logic:

```text
normalization selects the workflow route
workflow routing selects the role/subagent/command, not the model provider
confidence decides how far the agent may proceed
gated actions require explicit user intent or explicit approval
right-level correctness wins over minimal diff size when they conflict
```

## UI MCP stack

```text
1. Existing project components/tokens/styles
2. Official shadcn MCP + standard shadcn registry
3. Official shadcn MCP + GitHub/public shadcn-compatible registries
4. Jpisnice shadcn-ui-mcp-server + GitHub token as secondary/reference source
5. Manual implementation
```

Notes:

- Do not assume MCP availability from instructions alone; check visible tools/config.
- If a source level is unavailable, skip to the next level.
- Secret-backed sources are gated actions. Do not hardcode tokens.
- Local/private/authenticated non-GitHub registry setup is a gated action.
- UUPM/UI UX Pro Max is design intelligence only, not a component MCP source.

## Install globally

```bash
cd opencode_final_config_v27_model_agnostic
./install/install-global.sh
```

This installs the root `AGENTS.md` into `~/.config/opencode/AGENTS.md` and copies agents, commands, docs, and snippet files into OpenCode config.

## Install into a project

```bash
cd your-project
/path/to/opencode_final_config_v27_model_agnostic/install/install-project.sh
```

This installs:

```text
AGENTS.md
.opencode/agents/*.md
.opencode/commands/*.md
.opencode/docs/*.md
.opencode/snippet/*
```

## Important commands

```text
/ui-redesign      one-shot UI redesign workflow
/ui-options       UI options without implementation
/ui-mcp-setup     configure UI MCP stack
/uupm-setup       install/configure UUPM guidance
/bugfix           investigate, fix, verify, report
/pr-followup      work on existing PR branch, not a new PR
/issue-from-bug   verify bug and draft/open issue
/release-prep     release notes/checks from real history only
/project-audit    full read-only project audit
```

## Changes from v27 baseline

- Removed all provider-specific `model:` frontmatter from `agents/*.md`.
- Removed the fixed provider-specific role-to-model table and the old routing snippet.
- Added compact model policy to `AGENTS.md` and README.
- Renamed `snippet/` to `snippet/` for OpenChamber/opencode-snippet compatibility.
- Install scripts now copy `snippet/` into `~/.config/opencode/snippet/` or `.opencode/snippet/`.
- Removed install message that asked to verify fixed model IDs.
