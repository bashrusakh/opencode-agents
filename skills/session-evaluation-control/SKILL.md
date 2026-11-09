---
name: session-evaluation-control
description: Conditional caller-side harness for the one-time post-hoc session-evaluator diagnostic at an established terminal-success boundary. Load only from code-orchestrator at that boundary.
metadata:
  opencode/autoinvoke: "false"
---

# Session Evaluation Control

## Activation boundary

Load this skill only from `code-orchestrator` after the workflow owner has already established a **terminal successful outcome about to be reported**: the normalized goal is satisfied, or an active conditional resource workflow has returned its terminal success/readiness boundary. Do not load or invoke it for intermediate work, routine iterations, pauses, blocked/failed work, or an unsatisfied goal.

This is a post-hoc diagnostic harness, not part of the task acceptance/readiness gate. The terminal state must already be established before this harness runs.

## Evaluator handoff

Invoke `@session-evaluator` once. Pass the exact current orchestrator session ID when already known plus material participating child-session IDs already known from task results, with completeness status when established. Do not perform new session-history discovery merely to populate the handoff. Omit unknown identities or relationships; `session-evaluator` uses `session-evidence` for permitted retrieval.

Do not seed a preferred diagnosis or expected finding. The evaluator owns the post-hoc semantic/compliance diagnosis; this harness owns only terminal activation and caller-side evidence-identity handoff.

## Diagnostic consumption

Treat the evaluator result as diagnostic evidence only. Failure or unavailability of this diagnostic does not change an already-established terminal state, does not reopen completed work, and does not gate final reporting. Preserve a material diagnostic finding only as agent-pack/workflow evaluation evidence, not as new task acceptance authority.

**Consume and reconcile the returned diagnostic before the terminal user-facing report.** Do not leave material findings isolated in the child session, substitute the raw evaluator report for the workflow owner's synthesis, or suppress a confirmed finding merely because the task outcome was successful. Present confirmed material findings concisely by causal root and disposition, with responsible actor/active model when established; disclose only consequential evidence limitations. If no material findings are confirmed, use at most one brief scope-qualified audit-status statement, not a list of passed checks. If the evaluator is incomplete/unavailable or cannot establish material provenance, state that limitation rather than implying a clean audit.

When multiple task-scoped diagnostics are known in the same orchestrator workflow, preserve and reconcile their material findings, task boundaries, provenance, and disposition in the existing workflow context. A later clean task-level audit does not erase earlier confirmed failures. A session-wide summary deduplicates shared causes and distinguishes the models that introduced, continued, or corrected them. Do not invent missing earlier findings or perform new session-history discovery only to assemble this summary.

This reporting duty does not create a new acceptance/readiness gate, force a second audit or repair loop, or require an additional persistent report artifact.
