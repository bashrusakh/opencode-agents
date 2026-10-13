# Contract / protocol audit — v30.84 beta

## Scope

v30.84 changes no role topology. It tightens only the existing `code-orchestrator -> trajectory-auditor` longitudinal control relation introduced in v30.83.

The motivating distinction is between two independent axes:

- **local finding severity/provenance** — blocking vs report-only, introduced vs pre-existing, inside vs outside a leaf assignment;
- **trajectory relevance** — whether the evidence materially falsifies or weakens the same semantic policy/representation/ownership model being corrected.

The second axis must not be erased by the first.

## `code-orchestrator` contract

The workflow owner now treats materially convergent counterexamples to one classifier/normalizer/policy boundary as cumulative trajectory evidence even when individual leaves report them as `report-only`, `pre-existing`, or locally `out-of-scope`.

When those counterexamples keep expanding materially different representations/classes, a fresh trajectory audit is required before:

- another representative-specific edit-capable correction under the same policy model; or
- a readiness/publication transition that would treat the affected boundary as sufficiently closed.

This is semantic clustering, not a count trigger. Unrelated residual notes remain direct-flow counterexamples.

On `reassess`, the orchestrator must frame the bounded read-only reassessment around the unresolved owner/representation/invariant or strategy question. Existing files/functions/call sites are implementation evidence, not a required solution boundary unless stronger authority says otherwise.

## `trajectory-auditor` contract

The auditor accumulates semantically relevant counterexamples across correction/review transitions and explicitly separates local severity/provenance from abstraction quality. It may classify the chain `clustered` when different representations/classes converge on one policy model, but clustering does not prove the architecture is wrong and does not mandate a helper/refactor.

The auditor still judges only the proposed next transition and cannot review code as a substitute for `reviewer`, fix as `debugger`, select architecture as `project-planner`, mutate state, or classify pack defects as `session-evaluator`.

## Anti-overreach

The new trigger does not promote every residual note into a blocker. Multiple low/pre-existing findings concerning different owners/invariants, or evidence-backed independent defects, do not establish a shared abstraction problem.

## Regression evidence

The semantic-transition suite now contains 96 cases. ST-95 covers same-policy report-only/pre-existing/out-of-scope counterevidence; ST-96 is the unrelated-residual anti-overreach control. Static guards and the high-risk handoff profile bind the new trigger/reassessment semantics. Behavioral replay remains separate evidence.
