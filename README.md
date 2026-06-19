# OpenCode final config v27

Agents, commands, root `AGENTS.md`, snippets, and UI MCP/UUPM setup notes for OpenCode. This package no longer ships a duplicate `global/AGENTS.md`; the root `AGENTS.md` is the single source for these reusable rules.

## Model routing

```text
build                      -> opencode-go/mimo-v2.5-pro
plan                       -> opencode-go/glm-5.2
explore                    -> opencode-go/mimo-v2.5
general                    -> opencode-go/qwen3.7-plus
reviewer                   -> opencode-go/qwen3.7-plus
fix-level-reviewer         -> opencode-go/qwen3.7-plus
tester                     -> opencode-go/deepseek-v4-flash
debugger                  -> opencode-go/deepseek-v4-pro
devops                    -> opencode-go/mimo-v2.5-pro
code-workflow-orchestrator -> opencode-go/glm-5.2
project-auditor           -> opencode-go/glm-5.2

ui-web-orchestrator        -> opencode-go/glm-5.2
ui-ux-auditor              -> opencode-go/mimo-v2.5
ui-redesign-planner        -> opencode-go/glm-5.2
frontend-ui-implementer    -> opencode-go/mimo-v2.5-pro
accessibility-reviewer     -> opencode-go/deepseek-v4-flash
```

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
normalization selects the route
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
cd opencode_final_config_v27
./install/install-global.sh
```

This installs the root `AGENTS.md` into `~/.config/opencode/AGENTS.md` and copies agents, commands, and docs into OpenCode config.

## Install into a project

```bash
cd your-project
/path/to/opencode_final_config_v27/install/install-project.sh
```

This installs:

```text
AGENTS.md
.opencode/agents/*.md
.opencode/commands/*.md
.opencode/docs/*.md
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

## v27 changes

- Root `AGENTS.md` is the single shipped rules file; no duplicate `global/AGENTS.md`.
- Section 6.2 is now compact and delegates detailed UI/MCP/UUPM policy to `docs/UI_COMPONENT_POLICY.md`.
- Install scripts copy `docs/*.md` into the matching OpenCode docs directory.
- UI agents and UI commands are aligned to read the detailed UI policy file for UI/MCP/component-source and UUPM-guided work.
- Microfixes: unified gated-action wording for separate PRs/releases/registry setup, clarified final-report notes, and normalized ellipses.
