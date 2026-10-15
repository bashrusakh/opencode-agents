---
name: ui-routing-control
description: Conditional bridge from code workflow ownership into the UI domain. Distinguishes settled UI implementation from unresolved presentation/interaction direction and defines the bounded handoff to ui-orchestrator or ui-implementer. Load only when code-orchestrator must route a material UI stage.
metadata:
  opencode/autoinvoke: "false"
---

# UI Routing Control

## Activation boundary

Load this skill only from `code-orchestrator` when the active code/repository workflow reaches a **material UI-domain routing decision**. Do not load it for non-UI code work, generic review/testing, metadata-only resource handling, or after a UI leaf/stage has already been unambiguously selected by the caller.

This skill owns only the bridge from the code workflow into the UI domain. `ui-orchestrator` owns internal UI stage selection and reconciliation; `ui-implementer` owns focused UI repository mutation; `delegation-control` owns generic handoff, subagent-generation, fallback, and mutation-parallelism semantics.

## Direction discriminator

Distinguish a **settled user-visible outcome** from an **unresolved presentation/interaction direction** before choosing the UI route.

A functional requirement alone does not make the UI outcome settled when satisfying it still requires choosing among materially different layout, information hierarchy, disclosure, interaction, or error-state treatments. User feedback that rejects the current treatment without adopting a replacement also leaves the presentation/interaction direction unresolved.

Do not invent a missing UI/product direction and pass it downstream as established authority.

## Route to the UI domain

When the material presentation/interaction direction is unresolved or the UI work requires coordinated multi-stage judgment, delegate the bounded UI domain to `@ui-orchestrator`. Pass the UI domain/problem, inherited target/state identity, behavior scope, action level, publication boundary when relevant, material constraints/evidence, and whether UI stage selection is delegated. The code orchestrator remains workflow owner and dispatches any bounded leaf assignments returned by delegated UI orchestration. Cross-layer architecture change, broader product redesign, publication-state change, or another user-owned material direction returns to the code workflow owner.

When the material presentation/interaction choice is already established by the user, an adopted plan, or a sufficiently specific existing project pattern and only focused UI implementation mechanics remain, route directly to `@ui-implementer`. Pass the established user-visible outcome, target/mutation state, material constraints, and preserved behavior. Do not preselect files/layout mechanics merely to make the handoff deterministic.

## Result boundary

A delegated `ui-orchestrator` result may select or return the next bounded UI stage inside the delegated domain, but it does not transfer whole-workflow ownership or authorize cross-layer scope/publication changes. After the parent dispatches a returned UI leaf, if the delegated UI domain still requires stage selection or reconciliation, pass the leaf result plus exact updated target/state and material UI evidence back to `@ui-orchestrator` for the next UI-domain decision; do not infer the remaining UI chain in `code-orchestrator`. A direct `ui-implementer` result is implementation evidence for the code workflow owner; it does not substitute for any independent verification/review/readiness stage that later applies.
