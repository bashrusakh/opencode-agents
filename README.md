# OpenCode final config v28.3 — model-agnostic + behavioral contract

This package is based on `opencode_final_config_v27_model_agnostic` and keeps the v27 file layout intact.

Important: OpenCode uses `AGENTS.md` as the rules file. `agent.md` is not the primary OpenCode rules file and may be ignored.

## What changed from v27 model-agnostic

- Agents remain model-agnostic: no `model:` overrides in `agents/*.md`.
- Model routing remains removed. Workflow routing stays because it chooses roles/agents, not providers/models.
- `Behavioral Contract Check` was added to `AGENTS.md`, `agents/*.md`, `commands/*.md`, and `docs/UI_COMPONENT_POLICY.md`.
- `snippet/` remains singular for OpenChamber / opencode-snippets compatibility.
- No v27 files were intentionally removed.

## Behavioral Contract Check

Before implementing a user-facing UI, config, API, or workflow change, the agent must summarize the behavioral contract:

- what action the user naturally performs
- who or what provides the value
- whether the value is user-authored, system-derived, provider/model-derived, file-derived, state-derived, or selected from known capabilities
- what existing project pattern handles the same kind of action
- whether raw/internal/manual values would be exposed to normal users

Do not map schema/storage/API types directly to UI or workflow behavior. Preserve how users naturally provide or choose the value. Do not expose raw/internal/manual inputs unless the normalized request explicitly asks for a raw/manual/editor workflow.

## Directory layout

```text
AGENTS.md
agents/
commands/
docs/
install/
snippet/
```

## Install globally

```bash
./install/install-global.sh
```

Installs to:

```text
~/.config/opencode/AGENTS.md
~/.config/opencode/agents/
~/.config/opencode/commands/
~/.config/opencode/docs/
~/.config/opencode/snippet/
```

## Install into a project

Run from the repository root:

```bash
/path/to/opencode_model_agnostic_contract_v28_3/install/install-project.sh
```

Installs to:

```text
./AGENTS.md
./.opencode/agents/
./.opencode/commands/
./.opencode/docs/
./.opencode/snippet/
```

## Validation checklist used for this archive

- file manifest compared against v27 model-agnostic base
- no missing files
- no unexpected added files
- YAML frontmatter for agents and commands parsed
- snippet JSONC parsed
- install scripts passed `bash -n`
- no `model:` in `agents/*.md`
- no provider-specific OpenCode Go model IDs
- no provider-specific routing material
- no plural snippet directory
- zip integrity passed
