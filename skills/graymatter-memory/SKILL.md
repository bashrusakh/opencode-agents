---
name: graymatter-memory
description: Use only when root continuity semantics or an active workflow/role contract activates GrayMatter recall. Owns GrayMatter identity, query, checkpoint, durable-write, correction, and tool-call mechanics; root owns memory authority/durable-vs-transient policy and the active judgment contract owns independence/isolation.
---

# GrayMatter Memory

Apply root source-of-truth/continuity semantics first and any active role/delegation isolation contract. This skill supplies GrayMatter-specific mechanics only and does not redefine memory authority, activation, fresh-judgment isolation, or what counts as durable versus transient state.

## Identity

Use a stable `agent_id`: the repository root directory name verbatim. Add a stable `-<role>` suffix only when multiple long-lived agents in the same repository genuinely need separate role memory. Facts intended for every agent in the project belong to `__shared__`.

## Recall and checkpoint procedure

When root continuity semantics or the active workflow contract activates continuity for the **current role/workflow**, call `checkpoint_resume` for the applicable `agent_id` first when resuming unfinished work. For other authorized recall, search project memory and `__shared__` with a focused query phrased as the current task/question rather than an unstructured keyword bag. If no checkpoint exists, continue normally.

For a fresh independent-judgment child, apply the active role/delegation isolation contract: do not use GrayMatter to reconstruct the parent task/history. Missing authority stays an authority gap.

Before stopping unfinished work whose transient state must survive, save concise reconstructable state with `checkpoint_save`.

## Durable-write and correction mechanics

When root/role policy permits a durable conclusion to be stored, write it atomically and specifically with `memory_add`. For a correction, search for the exact old fact if necessary, then use `memory_reflect` to update or forget it so stale and corrected variants do not remain simultaneously live in recall. Do not copy raw tool output into durable memory merely because it was retrieved.

## Tool contract

Use the current GrayMatter tool schema exposed by the runtime. Typical calls are:

- `memory_search(agent_id, query[, top_k])`
- `memory_add(agent_id, text)`
- `memory_reflect(action, agent_id[, text, target])`
- `checkpoint_save(agent_id[, state])`
- `checkpoint_resume(agent_id)`
