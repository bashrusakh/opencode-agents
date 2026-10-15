---
name: session-evaluation-control
description: Conditional caller-side harness for the one-time post-hoc session-evaluator diagnostic at an established terminal-success boundary. Load only from code-orchestrator at that boundary.
metadata:
  opencode/autoinvoke: "false"
---

# Session Evaluation Control

## Activation boundary

Load this skill only from `code-orchestrator` after the workflow owner has already established a **terminal successful outcome about to be reported**: the normalized goal is satisfied, or an active conditional resource workflow has returned its terminal success/readiness boundary. Do not load or invoke it for intermediate work, routine iterations, pauses, blocked/failed work, or an unsatisfied goal.

This is temporary beta instrumentation, not part of the task acceptance/readiness gate. The terminal state must already be established before this harness runs.

## Evaluator handoff

Invoke `@session-evaluator` once. Pass the exact current orchestrator session ID when already known plus material participating child-session IDs already known from task results, with completeness status when established. Do not perform new session-history discovery merely to populate the handoff. Omit unknown identities or relationships; `session-evaluator` uses `session-evidence` for permitted retrieval.

Do not seed a preferred diagnosis or expected finding. The evaluator owns the post-hoc semantic/compliance diagnosis; this harness owns only terminal activation and caller-side evidence-identity handoff.

## Diagnostic consumption

Treat the evaluator result as diagnostic evidence only. Failure or unavailability of this diagnostic does not change an already-established terminal state, does not reopen completed work, and does not gate final reporting. Preserve a material diagnostic finding only as agent-pack/workflow evaluation evidence, not as new task acceptance authority.
