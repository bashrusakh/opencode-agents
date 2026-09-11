---
description: "Run a complete bugfix workflow in one request: investigate, implement the right-level fix, verify changed and preserved behavior, and review when risk warrants it."
agent: code-orchestrator
subtask: false
---

Run the bugfix workflow for: $ARGUMENTS

Follow the active `AGENTS.md` and code-orchestrator contract. Coordinate only the specialist stages that are semantically required; do not make the user invoke agents manually.

Required outcome:
- when the bugfix comes from an issue/report, resolve its applicability target from issue/project metadata rather than assuming local checkout; for current upstream/default/base behavior, resolve/fetch the authoritative target and establish the intended mutation baseline before diagnosis or mutation;
- establish the affected path and root cause before claiming a fix;
- route implementation to an implementation-capable role at the correct abstraction level;
- require implementation-local evidence for the reported failure and closest preserved behavior/invariant;
- invoke `@tester` only when independent verification materially adds confidence or policy/request requires it, and batch all already-applicable checks for the affected boundary into that invocation;
- apply broader representative verification when shared/multi-caller behavior is affected;
- use independent review when the root reviewer criteria apply to the final effective diff;
- if findings start sharing a state/lifecycle/protocol invariant or require materially new protocol concepts, stop one-finding/one-patch iteration and escalate to an invariant/state/interleaving plan with bounded implementation batches.

A failed/unavailable specialist does not transfer its capability to the orchestrator. Mark the affected stage blocked if no equivalent capable role can perform it.

Commit, push, PR, issue, or other publication happens only when that exact action is already authorized under the root gate. If this bugfix is follow-up on an owned PR, apply the root Draft/Candidate/Ready lifecycle: intermediate Draft pushes do not trigger final review, while the final local Candidate HEAD receives the whole-PR reviewer pass **before** its final push.
