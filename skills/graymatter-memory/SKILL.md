---
name: graymatter-memory
description: Use only when root continuity semantics or an active workflow/role contract activates GrayMatter recall. Owns GrayMatter identity, query, checkpoint, durable-write, correction, and tool-call mechanics; root owns memory authority/durable-vs-transient policy and the active judgment contract owns independence/isolation.
---

# GrayMatter Memory

Apply root source-of-truth/continuity semantics first and any active role/delegation isolation contract. This skill supplies GrayMatter-specific mechanics only and does not redefine memory authority, activation, fresh-judgment isolation, or what counts as durable versus transient state.

## Identity

For **durable project memory**, use a stable `agent_id`: the repository root directory name verbatim. Add a stable `-<role>` suffix only when multiple long-lived agents in the same repository genuinely need separate role memory. Facts intended for every agent in the project belong to `__shared__`.

For **transient checkpoints**, use a **distinct task-scoped `agent_id`** of the form `<repository-root-name>--checkpoint--<task-key>`, where `<task-key>` is an established, stable, non-sensitive task identifier (for example `pr-151`, `issue-140`, or an existing canonical plan ID). Keep this key stable across sessions, models, worktree changes, and revisions; do not key by current SHA, timestamp, transient phase, or role turnover. Keep checkpoint identity separate from the durable-memory identity so one PR/task does not overwrite another's latest checkpoint. If no unambiguous task key is available, establish one in the authorized canonical task state before relying on scoped checkpoint recovery; never guess a key or load another task's state by repository name alone.

## Recall and checkpoint procedure

When root continuity semantics or the active workflow contract activates continuity for the **current role/workflow**, call `checkpoint_resume` with the **task-scoped checkpoint `agent_id`** when resuming unfinished work. Confirm the returned state identifies the same project and task before using it. Reconcile its phase, pending work, decisions, blockers, review dispositions, next safe action, and state-bound evidence against the current canonical task state and actual repository/ref/SHA/worktree; changed identities invalidate affected verification/review claims. A missing, mismatched, unverifiable, or stale checkpoint is **not** permission to resume from its assertions: recover from the canonical task state and current evidence instead, or surface the missing task identity. Do not silently fall back to the latest repository-wide checkpoint. For other authorized recall, search under the **durable project/role `agent_id`** and `__shared__` with a focused task/question query rather than an unstructured keyword bag. If no checkpoint exists, continue normally.

For a fresh independent-judgment child, apply the active role/delegation isolation contract: do not use GrayMatter to reconstruct the parent task/history. Missing authority stays an authority gap.

At workflow-owner material-progress boundaries (and before stopping unfinished work), when GrayMatter continuity is active and available, call `checkpoint_save` with the **task-scoped checkpoint `agent_id`** and concise reconstructable `state`: established task key and project identity, authorized goal, current work package/phase, completed versus pending work, material decisions and adjudicated findings, blockers, repository state identity, evidence that remains valid versus requires rechecking, and the next safe action. Include references instead of transcripts or large tool/child outputs. Avoid a save for every routine minor edit. A successful tool response is required before claiming a checkpoint was stored.

## Durable-write and correction mechanics

When root/role policy permits a durable conclusion to be stored, write it atomically and specifically with `memory_add`. For a correction, search for the exact old fact if necessary, then use `memory_reflect` to update or forget it so stale and corrected variants do not remain simultaneously live in recall. Do not copy raw tool output into durable memory merely because it was retrieved.

## Tool contract

Use the current GrayMatter tool schema exposed by the runtime. Typical calls are:

- `memory_search(agent_id, query[, top_k])`
- `memory_add(agent_id, text)`
- `memory_reflect(action, agent_id[, text, target])`
- `checkpoint_save(agent_id[, state])`
- `checkpoint_resume(agent_id)`
