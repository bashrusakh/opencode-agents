# OpenCode agents final config v6

This pack is focused on code work plus UI/web design/redesign for web apps.

## What is included

Agents:

- `build` — primary implementation agent
- `plan` — read-only planning primary agent
- `explore` — read-only codebase discovery
- `general` — bounded fallback subagent
- `reviewer` — strict code/PR review
- `fix-level-reviewer` — checks wrong abstraction level and copy-patched fixes
- `tester` — verification only, no edits
- `debugger` — root-cause fixes
- `devops` — Docker/systemd/CI/deployment/runtime config
- `ui-ux-auditor` — read-only UI/web UX audit
- `ui-redesign-planner` — read-only UI/web redesign/theme plan
- `frontend-ui-implementer` — implements approved UI/web redesign
- `accessibility-reviewer` — read-only accessibility and interaction check
- `ui-web-orchestrator` — one-shot UI/web workflow coordinator
- `code-workflow-orchestrator` — one-shot coding workflow coordinator for bugfixes, PR follow-ups, issue triage, and release-prep checks

Commands:

- `/ui-audit`
- `/ui-plan`
- `/ui-implement`
- `/ui-check`
- `/ui-redesign`
- `/verify`
- `/debug`
- `/pr-review`
- `/fix-level`
- `/explore-code`
- `/devops-check`
- `/bugfix`
- `/pr-followup`
- `/issue-from-bug`
- `/release-prep`

## Install globally

```bash
cd opencode_final_config_v6
./install/install-global.sh
```

## Install into one project

```bash
cd your-project
/path/to/opencode_final_config_v6/install/install-project.sh
```

## Model check

After install, run `/models` in OpenCode and verify these model IDs exist:

- `opencode-go/mimo-v2.5`
- `opencode-go/mimo-v2.5-pro`
- `opencode-go/glm-5.2`
- `opencode-go/qwen3.7-plus`
- `opencode-go/deepseek-v4-flash`
- `opencode-go/deepseek-v4-pro`

If an ID changed, edit the `model:` line in the relevant agent file.

## Recommended UI/web workflow

For UI/web redesign, settings screens, dashboards, themes, forms, or layout-density problems, use one command by default:

```text
/ui-redesign <screen/problem>
```

The `ui-web-orchestrator` agent calls the UI audit, redesign planning, frontend implementation, accessibility review, and tester agents itself. It should not ask the user between stages unless an approval gate is hit.

Manual step commands are still included for cases where you want to run one stage directly:

```text
/ui-audit <screen/problem>
/ui-plan <screen/problem + audit summary>
/ui-implement <approved plan>
/ui-check <changed screen>
/verify <frontend build/test/lint>
```


## Recommended coding workflows

For multi-step coding work, use one command and let the orchestrator run the safe stages itself:

```text
/bugfix <bug, traceback, failing test, or broken behavior>
/pr-followup <PR number/branch/comment/check failure/requested correction>
/issue-from-bug <bug description or reproduction>
/release-prep <release target or tag range>
```

The `code-workflow-orchestrator` agent calls the needed discovery, debugging, testing, review, and fix-level agents itself. It should not ask the user between normal safe stages.

It must stop for approval gates such as commit/push/PR/tag/release actions not explicitly requested, destructive commands, secrets, new dependencies, broad rewrites, API/data/auth/deploy changes, or blocked verification.

For existing PR follow-up work, the default is: same PR branch, same PR. Do not open a separate PR unless explicitly requested.

## Model routing

Core:

- `build` → `opencode-go/mimo-v2.5-pro`
- `plan` → `opencode-go/glm-5.2`
- `explore` → `opencode-go/mimo-v2.5`
- `general` → `opencode-go/qwen3.7-plus`
- `reviewer` → `opencode-go/qwen3.7-plus`
- `fix-level-reviewer` → `opencode-go/qwen3.7-plus`
- `tester` → `opencode-go/deepseek-v4-flash`
- `debugger` → `opencode-go/deepseek-v4-pro`
- `devops` → `opencode-go/mimo-v2.5-pro`
- `code-workflow-orchestrator` → `opencode-go/glm-5.2`

UI/web:

- `ui-ux-auditor` → `opencode-go/mimo-v2.5`
- `ui-redesign-planner` → `opencode-go/glm-5.2`
- `frontend-ui-implementer` → `opencode-go/mimo-v2.5-pro`
- `accessibility-reviewer` → `opencode-go/deepseek-v4-flash`
- `ui-web-orchestrator` → `opencode-go/glm-5.2`


