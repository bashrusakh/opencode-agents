# Contract / protocol audit — v30.90 beta

## Scope

v30.90 changes no role topology. It adds a generic independent-judgment decision boundary and compacts duplicated semantics between `AGENTS.md` and `agents/code-orchestrator.md`.

## Canonical ownership after compaction

- **Root:** shared specialist packet schema/ergonomics, decision-space preservation, task-semantic authority/evidence algebra, generic mutation concurrency, shared freshness/evidence policy, generic routing defaults, publication gates, and common final-report contract.
- **Code orchestrator:** workflow-owner synthesis, owner-model reconstruction fields, code-workflow routing discriminators, parent-hypothesis guard, controller invocation/consumption, whole-review construction/consumption, readiness-reversal reassessment, and terminal semantic-evaluator handoff mechanics.
- **Reviewer:** independent investigation and verdict bounded to actual target/evidence/decision claim.
- **PR readiness:** owned-PR lifecycle gate and prerequisites; reviewer evidence is consumed as one gate input.

This removes the high-overlap clusters identified in the v30.89 semantic duplication audit rather than creating cross-file summary restatements.

## Decision boundary

An independent judgment now carries a downstream decision boundary distinct from target identity and judgment scope. Ambiguous umbrella wording such as `final` or `before publication` cannot establish a lifecycle transition whose prerequisites were not adjudicated. A still-valid whole-Candidate review may be reused at later gates; reuse does not imply authorization.

## Guard changes

- ST-119 specifies the review-verdict/lifecycle-gate laundering failure class.
- static policy checks cover the root/orchestrator/reviewer/pr-readiness composition.
- role-handoff audit no longer requires `code-orchestrator` to duplicate the root-owned generic handoff field list; it checks root-contract activation plus workflow-specific reconstruction state instead.
- topology remains closed-world and unchanged.

## Evidence boundary

Static/contract/handoff/package evidence does not equal behavioral replay. Fresh isolated replay is not claimed unless actually executed.
