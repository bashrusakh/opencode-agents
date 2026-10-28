---
name: change-contract
description: Shared engineering contract for implementation and implementation judgment: behavioral contract, mutation baseline/mechanism, right-level ownership, regression guard, and verification freshness. Load only for an applicable code/config/UI implementation or judgment stage.
metadata:
  opencode/autoinvoke: "false"
---

# Change Contract

## Activation boundary

Load only when the active role is implementing or materially judging code/config/UI behavior and its role contract activates this shared engineering contract. Do not load for unrelated research, metadata-only repository work, public-artifact formatting, or workflow routing.

This skill does not grant mutation authority. Apply root task-semantic authority/evidence semantics to the established outcome and proof claims. Delegated action ceilings and workflow-control/user gates remain external to it.

## Behavioral contract

Before implementing a user-facing UI/config/API/workflow change, establish the behavioral contract rather than mapping schema/storage/API shape directly to user behavior. Identify the natural user/system action, value provider, valid-value domain, nearest existing project pattern, and whether the proposed mechanism would expose raw/internal/manual values not requested by the established outcome. Preserve the existing affordance class unless authority changes it.

## Before mutation

Before the first repository mutation, load `git-provenance` and satisfy its mutation baseline for the actual worktree when repository-state provenance matters. Then inspect the relevant implementation, nearest callers/tests, project conventions, and existing owners. Do not introduce dependencies/generated files/broad rewrites/unrelated cleanup without separate authorization.

For bounded semantic edits to source, tests, config, or documentation, prefer the runtime's **native patch/edit tools** when they are available and safe (use `apply_patch`/`patch` if supported, otherwise the native `edit` tool). Shell text processors, `sed`, `python3`, redirection, and ad-hoc scripts are not alternative editors merely for convenience, shorter commands, line-number targeting, or avoiding exact-match editing. Programmatic mutation is appropriate for genuinely mechanical/bulk transformations, when native editing cannot safely express the change, or when native editing is unavailable. Choose the narrowest reliable mechanism for that case; constrain targets and inspect the resulting diff/state after mutation. Tool choice never widens scope or correctness obligations.

## Right-level implementation boundary

**Complexity/design escalation** means stopping local execution and re-checking the framing when unexpected complexity points to a shared state, lifecycle, protocol, concurrency, persistence, or ownership rule. New selectors, identities, persistence/coordination/ownership rules, accumulating guards, or adjacent interleavings are signals to reassess before expanding the patch. When escalation fires, establish the shared invariant/state/transition/interleaving/ownership model proportional to the risk before resuming implementation; use durable planning when that model needs cross-package/session coordination.

For non-trivial implementation/fix work, choose the narrowest existing owner that can guarantee the established outcome across affected paths/states/callers/boundaries/lifecycle transitions. Trace the root operation and existing owners first. If a local owner cannot guarantee the outcome, move outward or escalate rather than stacking local guards. Moving outward does not strengthen the required product outcome.

Production-grade means correct/maintainable at that boundary. Reuse existing semantics/primitives, keep responsibilities clear, and account for relevant failure/security/concurrency/recovery behavior in proportion to the actual contract/risk. Avoid test-specific branches, duplicate policy, compatibility tricks, speculative abstractions, or temporary workarounds as substitutes for the correct owner. An explicitly accepted temporary workaround remains bounded to its accepted scope.

### Material architectural choice

When repository evidence leaves **materially different viable architectural directions** with consequential differences in long-term ownership/boundaries, extensibility, implementation or migration cost, operational burden, or maintenance risk, that direction is a **user-owned choice** unless already authorized. Before committing work or handing off edits that select one direction, evaluate the distinct viable approaches without imposing a fixed number of options; explain the material tradeoffs, likely cost/risk, limits of the available evidence, and a reasoned recommendation. The user may have relevant project plans or earlier offline decisions absent from the agent's context. Neither apparent short-term complexity nor attractive long-term architecture alone authorizes silently discarding a viable alternative or choosing it on the user's behalf.

A delegated specialist returns that unresolved choice and its evidence to the workflow owner; the workflow owner presents the decision to the user and obtains its authorization before selecting the direction. Respect a direction already chosen by the user unless material contrary evidence warrants proposing a revision; never silently replace it. Keep routine, reversible technical mechanics and a necessary right-level owner/scope change that does not create an independently choosable architectural direction within ordinary implementation authority. Do not manufacture options or user gates when no material architectural choice remains.

## Regression guard

When a change modifies existing/shared behavior, verify both the intended change and nearest behavior that must remain stable. Before editing, identify the changed behavioral contract and closest preserved invariant. For materially stateful/shared behavior, build a compact case-to-verification map proportional to risk across relevant states/transitions/consumers/boundaries/input shapes; do not enumerate an arbitrary cross-product.

When practical in the project's existing test layer, establish a discriminating failing regression case before the fix. Tests support but do not define the product contract; conflicting tests/requirements/evidence must be resolved rather than alternated until green.

After editing, verify the intended case and nearest preserved/representative unaffected behavior. A shared primitive/helper/service/parser/state/API wrapper/composable change also needs representative affected consumers or the applicable existing suite. One new passing test is not sufficient when the changed owner affects materially different consumers/states. If automated regression coverage is impractical, state why and perform the smallest meaningful preservation check.

### Implementation evidence budget

Keep newly authored tests and code comments proportional to the established behavioral change, **without weakening necessary correctness/security/regression proof**. These are **review-and-authorization thresholds, not quality targets, coverage percentages, automatic failure limits, or reasons to pad production code**. Apply project/user policy when it is more specific; do not replace its required coverage or documentation.

For a non-generated code-change diff, estimate these budgets before producing a large suite, and revisit them as the implementation grows:

- **Test-code budget:** let `P` be changed production **NCLOC** (nonblank, noncomment executable/declarative lines) and `T` be newly written/rewritten test NCLOC, excluding test comments, blank lines, fixtures/data generated by tools, and unchanged pre-existing tests. For each production file, count the larger of added and removed production NCLOC, then sum; a replaced line counts once rather than twice. Without a special case below, the normal self-authorized test budget is `T <= max(250, ceil(1.5 * P))`. This is **test-code volume**, not test coverage: do not infer correctness or an 80%/150% coverage result from this ratio. Use any available project coverage/quality gates separately to judge effective behavior/branches.
- **Production comment density:** for added/rewritten, non-generated production code, count `C` newly authored comment lines and `A` added/rewritten production NCLOC (exclude blanks). Aim for `C / (C + A) <= 15%`; **over 20%** triggers review and authorization of the necessary excess. Do not count Markdown documentation as comments or hide comments in tests/docs merely to alter the ratio. Keep legally required notices, interface documentation, and non-obvious invariants when needed; explain *why* a constraint exists rather than narrating obvious code.
- **Cases without a meaningful denominator:** test-only work, documentation-only changes, generated code, and unusually deletion-led/reorganization work do not inherit a misleading `P`-based ratio or synthetic denominator. Judge new tests against the actual changed behavior, existing coverage, duplicated cases and fixtures; identify any exceptional volume to the workflow owner rather than inventing production lines to meet the formula. Small code changes retain the 250-line floor when the normal ratio is applicable.

Before exceeding a threshold, first consolidate redundant assertions, table-driven cases, duplicate fixtures, and repetitive comments while preserving distinct failure modes, affected consumers, security and concurrency scenarios. If the necessary proof or required public documentation still exceeds the budget, **stop uncontrolled growth** and return the estimated excess and concrete coverage/maintenance rationale to the workflow owner; the owner seeks user authorization before that expansion. A reviewer finding is not an automatic instruction to add another test or comment: establish the distinct uncovered behavior first. Do not suppress required tests, change semantics, split files/PRs artificially, move comments into docs, or pad implementation to game the metric. Avoid a new mandatory reporting ceremony when the thresholds are comfortably met.

## Verification freshness

Evidence must support the exact current claim/state, not an earlier diff/ref/worktree. A mutation that can affect prior evidence stales that evidence unless unchanged effective behavior/state is established. Prefer narrow relevant checks first and broader checks when risk/scope requires them; never weaken tests/validation or hide failures to claim success.

For non-trivial verification planning, evidence freshness, blocked-check handling, or broad readiness claims, load `verification-strategy`. Generated caches/build outputs from ordinary verification are effects to reconcile only when project policy or workflow-created-resource ownership makes them material.

## Judgment consumption

Reviewer/tester/planner/auditor roles may use this contract read-only to judge fix level, preserved behavior, regression coverage, and evidence freshness. Doing so does not authorize them to mutate or turn a review hypothesis into task-semantic authority.
