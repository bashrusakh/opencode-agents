---
name: implementation-contract
description: "Shared engineering contract for implementation and implementation judgment: behavioral contract, mutation baseline/mechanism, right-level ownership, regression guard, and verification freshness. Load only for an applicable code/config/UI implementation or judgment stage."
metadata:
  opencode/autoinvoke: "false"
---

# Implementation Contract

## Activation boundary

Load only when the active role is implementing or materially judging code/config/UI behavior and its role contract activates this shared engineering contract. Do not load for unrelated research, metadata-only repository work, public-artifact formatting, or workflow routing.

This skill does not grant mutation authority. Apply root task-semantic authority/evidence semantics to the established outcome and proof claims. Delegated action ceilings and workflow-entry/user gates remain external to it.

## Behavioral contract

Before implementing a user-facing UI/config/API/workflow change, establish the behavioral contract rather than mapping schema/storage/API shape directly to user behavior. Identify the natural user/system action, value provider, valid-value domain, nearest existing project pattern, and whether the proposed mechanism would expose raw/internal/manual values not requested by the established outcome. Preserve the existing affordance class unless authority changes it.

## Before mutation

Before the first repository mutation, load `git-provenance` and satisfy its mutation baseline for the actual worktree when repository-state provenance matters. Then inspect the relevant implementation, nearest callers/tests, project conventions, and existing owners. Do not introduce dependencies/generated files/broad rewrites/unrelated cleanup without separate authorization.

Choose the narrowest reliable mutation mechanism. Constrain targets before bulk/programmatic transformation; use transforms only for understood mechanical changes, not as a substitute for semantic understanding. Inspect the resulting diff/state after mutation. Tool choice never widens scope or correctness obligations.

## Right-level implementation boundary

**Complexity/design escalation** means stopping local execution and re-checking the framing when unexpected complexity points to a shared state, lifecycle, protocol, concurrency, persistence, or ownership rule. New selectors, identities, persistence/coordination/ownership rules, accumulating guards, or adjacent interleavings are signals to reassess before expanding the patch. When escalation fires, establish the shared invariant/state/transition/interleaving/ownership model proportional to the risk before resuming implementation; use durable planning when that model needs cross-package/session coordination.

For non-trivial implementation/fix work, choose the narrowest existing owner that can guarantee the established outcome across affected paths/states/callers/boundaries/lifecycle transitions. Trace the root operation and existing owners first. If a local owner cannot guarantee the outcome, move outward or escalate rather than stacking local guards. Moving outward does not strengthen the required product outcome.

Production-grade means correct/maintainable at that boundary. Reuse existing semantics/primitives, keep responsibilities clear, and account for relevant failure/security/concurrency/recovery behavior in proportion to the actual contract/risk. Avoid test-specific branches, duplicate policy, compatibility tricks, speculative abstractions, or temporary workarounds as substitutes for the correct owner. An explicitly accepted temporary workaround remains bounded to its accepted scope.

## Regression guard

When a change modifies existing/shared behavior, verify both the intended change and nearest behavior that must remain stable. Before editing, identify the changed behavioral contract and closest preserved invariant. For materially stateful/shared behavior, build a compact case-to-verification map proportional to risk across relevant states/transitions/consumers/boundaries/input shapes; do not enumerate an arbitrary cross-product.

When practical in the project's existing test layer, establish a discriminating failing regression case before the fix. Tests support but do not define the product contract; conflicting tests/requirements/evidence must be resolved rather than alternated until green.

After editing, verify the intended case and nearest preserved/representative unaffected behavior. A shared primitive/helper/service/parser/state/API wrapper/composable change also needs representative affected consumers or the applicable existing suite. One new passing test is not sufficient when the changed owner affects materially different consumers/states. If automated regression coverage is impractical, state why and perform the smallest meaningful preservation check.

## Verification freshness

Evidence must support the exact current claim/state, not an earlier diff/ref/worktree. A mutation that can affect prior evidence stales that evidence unless unchanged effective behavior/state is established. Prefer narrow relevant checks first and broader checks when risk/scope requires them; never weaken tests/validation or hide failures to claim success.

For non-trivial verification planning, evidence freshness, blocked-check handling, or broad readiness claims, load `verification-strategy`. Generated caches/build outputs from ordinary verification are effects to reconcile only when project policy or workflow-created-resource ownership makes them material.

## Judgment consumption

Reviewer/tester/planner/auditor roles may use this contract read-only to judge fix level, preserved behavior, regression coverage, and evidence freshness. Doing so does not authorize them to mutate or turn a review hypothesis into task-semantic authority.
