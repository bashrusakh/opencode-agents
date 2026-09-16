# Verification strategy

The pack separates verification by **purpose and boundary** so multi-agent workflows do not re-run the same checks after every small edit.

## Three evidence layers

### 1. Implementation-local evidence

The mutation-capable role (`debugger`, `build`, `ui-implementer`, or another explicitly authorized implementer) runs focused project-documented checks after the affected edit/work package. This is part of implementation quality, not a separate specialist stage.

Typical evidence:

- the originally failing or changed behavior;
- the closest preserved/unaffected behavior;
- a directly relevant suite or representative consumers when a shared primitive changed.

Implementation-local evidence is valid only for the state/diff it checked.

### 2. Independent `@tester` checkpoint

`@tester` is used when **independence adds value**, not because an implementation role returned. Good triggers include:

- an explicit verification/reproduction request;
- a meaningful cross-component/integration/shared/stateful boundary;
- several bounded implementation packages that now form one coherent behavior;
- insufficient or uncertain implementation-local evidence;
- user/project policy requiring an independent pass.

A work-package boundary by itself is **not** a tester trigger.

When invoked, tester receives the complete affected boundary and runs one verification batch: focused changed behavior, preserved behavior, representative consumers/shared suites, and applicable lint/build/smoke checks. The smallest test runs first, but a PASS does not end the assignment while other already-applicable checks remain.

Focused tests count as production evidence only to the extent that the observed result justifies the production conclusion being drawn from it. If the same result could arise from test-only conditions while the claimed production property differs, the evidence remains test-scoped and the production claim is reported as a correspondence gap. Tester may read the necessary producer/consumer code only to establish that inference; this does not become a general code-review pass.

The tester may stop early when a blocker or dependency failure makes later checks meaningless, unsafe, or outside scope. One failing check alone is not a stop condition when other independent applicable checks can still provide distinct useful evidence; collect the coherent failure set in the same invocation. A later repository-content change invalidates only affected evidence.

### 3. Remote CI/status evidence

CI/status checks validate the published candidate in the remote/host environment. They complement local evidence and do not automatically require another local tester run when the Candidate HEAD is unchanged.

## Normal cadence

```text
implementation package A
  -> implementation-local checks
implementation package B
  -> implementation-local checks
meaningful integration boundary
  -> @tester once, if independent verification is useful/required
more implementation
  -> implementation-local checks
stable Candidate HEAD
  -> applicable local validation
  -> optional/required batched @tester checkpoint
  -> whole-change @reviewer
  -> push exact reviewed SHA
  -> remote CI/status
```

For a small local fix with sufficient implementation-local evidence, `@tester` may not be needed at all. For a risky shared/stateful change, an earlier integration checkpoint may be justified before more mutation depends on the result.

## Role separation

- **Implementer** proves its own local change enough to hand it back safely.
- **Tester** independently verifies a complete delegated behavioral boundary.
- **Reviewer** judges correctness/right-level/risk and consumes fresh verification evidence; it may run narrow spot-checks for a specific finding but should not recreate the whole tester stage. Outside explicit review requests and the mandatory final owned-PR Candidate review, invoke it only when independent judgment materially adds value at a stable high-risk boundary, not after every package/commit.
- **Auditor** batches executable verification questions by subsystem/invariant rather than calling tester once per finding; it may use narrow finding-specific spot-checks but does not recreate or repeat a broad tester/CI boundary.
- **CI** validates the published candidate in the remote environment.

The goal is fewer, stronger verification checkpoints — not fewer checks.
