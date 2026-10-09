---
name: graymatter-memory
description: Use when GrayMatter memory tools are available and prior unfinished work, user preferences, project conventions, decisions, workarounds, or durable task history can materially affect the current action. Do not load for fresh self-contained work with no material dependency on prior state.
---

# GrayMatter memory and continuity

GrayMatter is optional recall context, not repository authority. Current code, project rules, repository history, and observed tool/runtime state outrank recalled memory when they conflict.

## Identity

Use a stable `agent_id`: the repository root directory name verbatim. Add a stable `-<role>` suffix only when multiple long-lived agents in the same repository genuinely need separate role memory. Facts intended for every agent in the project belong to `__shared__`.

## Relevant recall

Use recall only when it can change the next action.

- When resuming unfinished/long-running work, call `checkpoint_resume` for the applicable `agent_id` first.
- Search project memory and `__shared__` with a focused query when a prior user preference, decision, convention, workaround, or earlier task state could materially affect the task.
- Phrase the query as the current task/question rather than as an unstructured keyword bag.
- Do not perform a memory search merely because the integration exists.

If no checkpoint exists, continue normally. If recalled memory conflicts with current authoritative evidence, verify the current source and update/forget stale memory rather than preserving both as live facts.

## Store only durable conclusions

Use durable memory for atomic, specific, self-contained conclusions that are likely to matter again and are not already authoritative in current code or project documentation.

Appropriate examples:

- a durable user preference;
- an undocumented project-wide convention or security rule;
- a non-obvious decision that future work will need;
- an environment quirk or reusable workaround.

Do not store secrets, credentials, raw transcripts, speculation, large outputs, or temporary progress. Use checkpoints for transient unfinished-work state.

Before stopping unfinished work, save concise reconstructable state with `checkpoint_save`.

## Tool contract

Use the current GrayMatter tool schema exposed by the runtime. Typical calls are:

- `memory_search(agent_id, query[, top_k])`
- `memory_add(agent_id, text)`
- `memory_reflect(action, agent_id[, text, target])`
- `checkpoint_save(agent_id[, state])`
- `checkpoint_resume(agent_id)`

For a correction, search for the exact old fact if necessary, then update or forget it so stale and corrected variants do not remain simultaneously authoritative in recall.
