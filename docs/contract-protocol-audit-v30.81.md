# Contract / protocol audit — v30.81 beta

## Scope

v30.81 changes one runtime role contract: `code-orchestrator`. No role permissions, topology edges, UI-role contracts, skills, installer control flow, or licensing semantics change.

The change refines an existing routing boundary rather than adding a new owner:

- direct `@ui-implementer` remains the focused implementation route for a settled user-visible UI outcome;
- `@ui-orchestrator` remains the owner for UI design/audit/redesign/unresolved-direction or multi-stage UI work;
- `code-orchestrator` now has an explicit discriminator preventing a known functional requirement from being mistaken for a settled presentation/interaction direction.

## Handoff composition

The existing generic delegation contract remains unchanged: objective/scope, action level, evidence/result, stop/escalation, relevant state identity, and no upstream recipe laundering.

The existing direct `code-orchestrator → ui-implementer` high-risk contract also remains unchanged: established user-visible outcome, target/mutation state, material constraints, preserved behavior, and no preselected layout/files merely for determinism.

v30.81 adds a complementary high-risk `code-orchestrator → ui-orchestrator` profile. It requires the caller to preserve the distinction between a settled UI outcome and unresolved presentation/interaction direction, route the latter to the UI workflow owner, and avoid inventing the missing UI direction upstream.

## Preservation boundary

The discriminator is deliberately asymmetric but not broad:

- rejecting one current UI treatment without selecting a replacement does **not** establish the replacement;
- materially different presentation/interaction choices keep the direction unresolved;
- an explicit user choice, adopted plan, or sufficiently specific existing project pattern may settle the material UI treatment;
- once settled, direct focused `@ui-implementer` delegation remains valid and no ceremonial `@ui-orchestrator` stage is required.

## Regression evidence

The release gates include:

- role-handoff selftest with a negative unresolved-UI→direct-recipe fixture;
- closed-world edge audit with the new high-risk profile while the relation inventory remains unchanged;
- static policy guard for the runtime discriminator;
- ST-79 for end-to-end semantic replay structure and the direct-implementation preservation counterexample.

These are contract/static regression classes. They do not constitute fresh isolated behavioral replay of ST-01…ST-79.
