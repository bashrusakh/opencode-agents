# Changelog

## v31.8 beta

Unifies the pre-implementation solution search with **evidence-triggered correct-fix reassessment**. The subject is whether the selected fix meets end-to-end acceptance, not merely whether its implementation follows a technical specification. If material contrary evidence arises during investigation, implementation, verification or review, the workflow owner revisits only the unsupported premises—including the issue/spec interpretation, user/product outcome, root cause, fix level, scope or architecture—before further dependent implementation. One discriminating prospective counterexample suffices; repeated patch failure is not a prerequisite.

- Scope may widen technically as necessary for the same authorized result; explicit user-owned exclusions, chosen mechanisms and product outcomes remain binding until an authorized decision revises them.
- No ritual re-evaluation of adequate fixes, no new mandatory planning step, no new ST traces, no role/permission/skill changes. Existing release-gate anchors updated to match the installed wording.

See `docs/releases/v31.8-beta.md`.

## v31.7 beta

Corrects the closed two-option comparison accidentally introduced in v31.6. **Before design/scope commitment or the first edit-capable handoff**, `code-orchestrator` must consider materially different plausible ways of achieving the established outcome, not just causal repair with/without a guard. If neither or none is adequate, revisit the root-cause model and right-level technical/architectural owner instead of force-fitting a local patch. A two-state safeguard comparison remains one illustrative diagnostic, not a mandatory exhaustive candidate set.

- Explicit constraints and product authority are unchanged: technical widening inside the accepted outcome follows the existing right-level rule; a required change to user-owned acceptance or exclusions goes back for a decision.
- No new role, stage, permission, ST trace or workflow-path scenario. Only existing gate anchors were updated to check the corrected runtime wording.
- All non-orchestrator agent bodies and all skills remain unchanged.

See `docs/releases/v31.7-beta.md`.

## v31.6 beta

Clarifies the **pre-implementation** combined-design assessment from v31.5 without changing its decision authority or adding a new workflow stage.

- `code-orchestrator` compares two *hypothetical* end states **before selecting implementation scope or delegating edits**: causal repair without a proposed additional restriction versus the same repair with it. This is not a post-implementation check.
- The resulting questions distinguish whether the safeguard still addresses a hazard from whether it burdens ordinary permitted behavior. Existing user authority and escalation rules remain unchanged; no new product policy or approval gate is introduced.
- The v31.5 global source-to-spec guidance and independent reviewer contract remain canonical for their own audiences; no semantic duplicate is added. Existing regression assertions now track the clarified wording. No new ST trace.

See `docs/releases/v31.6-beta.md`.

## v31.5 beta

Initial-specification acceptance and pre-handoff scope reconciliation over v31.4.

- Runtime `AGENTS.md` now makes source-to-spec drafting preserve the distinction between outcome, authoritative constraints, and alternative suggested remedies, rather than promoting all remedies into simultaneous requirements.
- `code-orchestrator` now checks interacting mechanisms **before** freezing the fix design/scope or delegating mutation: does the primary repair make a required safeguard redundant, and does the safeguard impair an ordinary permitted path?
- Explicit user/product constraints remain binding. When evidence shows an unresolved material product tradeoff, report it and obtain the owner's decision before implementing the disputed full mechanism set; do not silently discard a requirement or invent a new mandatory review stage. Already-accepted tradeoffs are not reopened ritualistically.
- Existing reviewer independence, right-level scope expansion, permissions, role boundaries and installed skill content unchanged. No new ST-* scenarios were added; existing release gates are regression safety checks, not a substitute for runtime instructions or model replay.

See `docs/releases/v31.5-beta.md`.

## v31.4 beta

Historical release notes and per-version audits live in the release bundle archive, not the runtime/source pack. Old paths below are archival references, not in-package links.



Semantic product-impact review and slim distribution over v31.3.

- Requires the workflow owner and independent reviewer to check whether a new protective restriction still addresses a real risk after the **combined** change, and whether it interrupts ordinary permitted use; do not derive real-world prevalence from a single fixture.
- User-authorized constraints remain binding: when a protection requirement conflicts with the broader acceptance outcome, surface the decision instead of silently overriding it or treating its matching tests as proof that the tradeoff is good. The tester remains a verification owner, not product-policy arbiter.
- Adds ST-150 and ST-151 plus workflow-path and destructive mutation coverage for guard-premise errors and legitimate explicitly accepted tradeoffs.
- Distribution now retains only the current release note; historical notes and protocol audit snapshots are delivered as a separate archive in the release bundle. CHANGELOG retains the canonical history. Consolidates the orphaned role-contract rubric into the semantic manual.
- No changes to agent frontmatter/permissions, vendor skills, runtime role topology, or PR lifecycle ownership.

Fresh independent model replay of ST-150..ST-151 is not claimed by this beta.

Detailed current release: `docs/releases/v31.4-beta.md`. Archived docs are separately available in the release bundle.

## v31.3 beta

Weak-model robustness hardening over v31.2 for terminal compliance diagnosis and explicit managed-review methods.

- Makes `session-evaluator` fail closed for material instruction-compliance areas whose governing historical contract cannot be established. Equivalent-looking tests/reviews/workflow layers cannot substitute for the missing contract, and a material `unverified` area cannot be normalized into `Compliant overall`.
- Clarifies that an explicit managed-OCR requirement constrains the **review method/evidence source**, not the **review owner**. When final whole-change review belongs to `@reviewer`, OCR is passed into that reviewer stage; direct OCR cannot replace it, and OCR failure/waiver waives only the method unless governing authority separately changes the stage.
- Adds generalized semantic-design guidance for compliance under missing contracts and method-vs-owner separation.
- Adds ST-148 and ST-149 plus destructive workflow-path mutations for inferred-compliance laundering and OCR-method ownership transfer.
- Keeps agent permissions/frontmatter, role topology, vendor skill content, PR lifecycle ownership, and existing review/OCR provider mechanics unchanged.

Fresh isolated behavioral replay of ST-148..ST-149 is not claimed unless separately executed.

See `docs/releases/v31.3-beta.md` (archived) and `docs/contract-protocol-audit-v31.3.md` (archived).

## v31.2 beta

Semantic evidence-consumption and public-report provenance hardening over v31.1.

- Extends the v31.1 closure-adjudication regression so an unqualified specialist `complete`/`no blocker` cannot launder representative/narrow evidence into broader domain/owner/invariant closure merely because the producer reports confidence. Runtime ownership remains in `code-orchestrator`; no new producer checklist is added.
- Strengthens `repository-workflow` so the evidentiary state of a public issue/ticket/report must match the state claimed by that report. Current-code/root-cause/file/line claims require authoritative evidence for that current target state; stale local code is not a substitute.
- Preserves precedence/action ceilings: when the freshness step required for a stronger public claim is unavailable or forbidden by project/user authority, the workflow narrows the report to supported symptom/reproduction/version propositions or stops the unsupported claim instead of bypassing the boundary. Explicitly historical/local/pinned reports remain bound to their intended state and do not force current-upstream refresh.
- Adds ST-146 and ST-147 plus destructive workflow-path mutations for representative-evidence laundering and stale-report-diagnosis laundering.
- Keeps agent permissions/frontmatter, vendor skill content, role topology, PR lifecycle ownership, and git-provenance mechanics unchanged.

Fresh isolated behavioral replay of ST-146..ST-147 is not claimed unless separately executed.

See `docs/releases/v31.2-beta.md` (archived) and `docs/contract-protocol-audit-v31.2.md` (archived).

## v31.1 beta

Consumer-side closure adjudication hardening over v31.0:

- treats specialist completion/closure conclusions as proposition-scoped claims rather than workflow state;
- requires `code-orchestrator` to compare claimed closure breadth with the assignment and evidence actually returned before closing a broader parent proposition;
- keeps material residual risks, unsupported classes, coverage limits, and unresolved owner/model questions live even when a specialist labels its bounded package complete;
- documents the reusable design principle **producer completion != consumer acceptance** without requiring the parent to redo specialist work;
- adds workflow-path mutation coverage and ST-145 for narrow-evidence -> broad-closure laundering;
- keeps permissions/frontmatter, vendor skill content, role topology, and PR lifecycle ownership unchanged.

Fresh isolated behavioral replay of ST-145 is not claimed unless separately executed.

See `docs/releases/v31.1-beta.md` (archived) and `docs/contract-protocol-audit-v31.1.md` (archived).

## v31.0 beta

Behavioral orchestration hardening from a clean v30.100 owned-PR session:

- adds an explicit **Correction / stabilization** owned-PR state: locally green/committed/targeted-reviewed correction packages are not Candidate HEADs by themselves; final whole-PR review is the exit gate from the combined stabilization state rather than a discovery loop after every fix;
- requires owner reassessment before another Candidate promotion when the next whole review exposes a materially related blocker in the same owner/invariant family;
- prevents Ready sequencing from implicitly waiving missing review/evidence prerequisites: an action order such as push -> CI -> Ready is not itself a prerequisite waiver;
- generalizes delegated mutation authority across all task-relevant state: a child cannot rebind target identity, resource topology/ownership, or relocate pre-existing workflow state outside its action boundary merely as execution convenience; lifecycle reconciliation does not create mutation authority;
- adds workflow-path/static/mutation regressions and ST-142..ST-144 for Ready-without-whole-review, correction-package promotion churn, and delegated task-state drift;
- keeps agent permissions/frontmatter and vendor skill content unchanged.

Fresh isolated behavioral replay of ST-142..ST-144 is not claimed unless separately executed.

See `docs/releases/v31.0-beta.md` (archived) and `docs/contract-protocol-audit-v31.0.md` (archived).

## v30.100 beta

Terminology-only cleanup of pack-controlled conditional skills; runtime semantics and residency boundaries are unchanged.

- Renamed `workflow-entry` -> `workflow-control`.
- Renamed `implementation-contract` -> `change-contract`.
- Renamed `terminal-semantic-eval` -> `session-evaluation-control`.
- Renamed `code-host-workflow` -> `repository-workflow`.
- Normalized active capability IDs and pack-owned skill H1 headings to the same domain -> capability naming scheme.
- Historical release documents retain the names used by those releases.
- Permissions/frontmatter and vendor skill content are unchanged.

See `docs/releases/v30.100-beta.md` (archived) and `docs/contract-protocol-audit-v30.100.md` (archived).

## v30.99 beta

- Corrected role/pack-skill references after the root residency split: Startup/Update, routing/fallback, review cadence, user gates, and current-target freshness now point to their actual conditional owners.
- Removed the dangling `debugger` reference to deleted root §7; delegated scope now references root §2.4 while implementation/regression/verification reference `implementation-contract`.
- Added `reference-integrity-audit.py` + selftest and release-gate integration across all roles and pack-controlled skills; vendor-advisory content remains untouched.
- Permissions/frontmatter, vendor skills, role topology, and workflow semantics are unchanged.

See `docs/releases/v30.99-beta.md` (archived) and `docs/contract-protocol-audit-v30.99.md` (archived).

## v30.98 beta

Conditional code-to-UI routing residency plus end-to-end workflow-path validation:

- adds non-autoinvoked pack-owned `ui-routing-control` for the code-to-UI discriminator and bounded `ui-orchestrator` / direct `ui-implementer` handoff;
- removes detailed UI direction selection from resident `code-orchestrator`, leaving only conditional activation/consumption;
- preserves delegated multi-stage UI ownership by returning leaf results plus updated target/state/evidence to `ui-orchestrator` for further UI-stage selection instead of letting the code owner invent the remaining UI chain;
- strengthens initial bugfix handoff with exact symptom/reproduction evidence, governing expected behavior/invariant, affected boundary, target/mutation identity, and non-binding suspected remediation;
- adds workflow-path release gates covering 18 end-to-end routes across code orchestration, UI, code-host resources, review, verification, semantic/trajectory controllers, terminal diagnostics, audit, planning, build, and external research;
- extends conditional skill-mediated topology/handoff auditing so UI edges remain visible without keeping UI procedure resident in `code-orchestrator`;
- keeps agent permission/frontmatter policy and bundled third-party/vendor skill content unchanged.

Fresh isolated behavioral replay of ST-138..ST-141 is not claimed unless separately executed.

See `docs/releases/v30.98-beta.md` (archived) and `docs/contract-protocol-audit-v30.98.md` (archived).

## v30.97 beta

Conditional terminal diagnostic residency for `code-orchestrator`:

- adds non-autoinvoked pack-owned `terminal-semantic-eval` for the one-time terminal `session-evaluator` activation/handoff and diagnostic non-gating semantics;
- leaves `code-orchestrator` with only the already-established-terminal-success activation hook, so intermediate code-orchestrator sessions do not carry child-session-ID/retrieval/diagnostic procedure;
- keeps `session-evaluator` as the post-hoc semantic/compliance diagnosis owner and `session-evidence` as the retrieval-mechanics owner;
- moves `terminal_session_evaluator_handoff` semantic ownership from the resident orchestrator to the conditional skill and adds a `terminal-diagnostic` residency audience;
- extends residency/static/selftests and ST-136..ST-137 so evaluator procedure cannot leak back into the resident caller or become a completion/readiness gate;
- keeps agent permission/frontmatter policy and bundled third-party/vendor skill content unchanged.

Fresh isolated behavioral replay of ST-136..ST-137 is not claimed unless separately executed.

See `docs/releases/v30.97-beta.md` (archived) and `docs/contract-protocol-audit-v30.97.md` (archived).

## v30.96 beta

Conditional code-host resource residency for `code-orchestrator`:

- adds non-autoinvoked pack-owned `code-host-workflow` for existing-PR follow-up, issue/ticket/report handling, release/host publication, host template/metadata discovery, and resource-specific reporting;
- leaves `code-orchestrator` with only the code-host route/activate/consume discriminator, so ordinary bugfix/tests/docs/local implementation sessions do not carry PR/issue/release procedure;
- keeps `pr-readiness` as the sole owner of Owned-PR Draft/Candidate/Ready lifecycle and `git-provenance` as the ref/SHA/worktree owner;
- removes PR-template/readiness/reporting procedure from generic `workflow-entry`, which remains the primary routing/authorization/publication gate;
- extends runtime-residency auditing with conditional-resource audience plus forbidden-activator-family checks, blocking resource procedure copied back into the resident orchestrator;
- adds whole-pack ownership/skill-control coverage for the new resource owner and ST-134..ST-135 for non-resource non-activation and code-host/pr-readiness composition;
- keeps agent permission/frontmatter policy and all bundled third-party/vendor skill content unchanged.

Fresh isolated behavioral replay of ST-134..ST-135 is not claimed unless separately executed.

See `docs/releases/v30.96-beta.md` (archived) and `docs/contract-protocol-audit-v30.96.md` (archived).

## v30.95 beta

Semantic-preservation hardening after the v30.94 residency split:

- restores universal non-trivial hypothesis/counter-framing semantics and required-skill-unavailable blocking in root without returning caller/implementation procedure to universal residency;
- restores `Broad scope` plus `clear/likely/ambiguous/unclassified` consequence semantics in `workflow-entry`;
- restores PR-template host-metadata fallback and visual-evidence blocked/verify-destination behavior in the primary publication contract;
- restores anti-artificial-freshness reconfiguration policy in `delegation-control`;
- restores the canonical complexity/design-escalation trigger and shared invariant/state/transition/interleaving/ownership-model obligation in `implementation-contract`;
- makes `pr-readiness` the canonical owner of the `Owned PR` definition and makes `code-orchestrator` load that definition before ownership-dependent PR-state decisions;
- extends the residency gate with **required resident semantic families**, so release checks fail both when conditional procedure leaks back into root and when relocation silently drops a load-bearing invariant;
- adds ST-130..ST-133 for relocation preservation; fixes the duplicated debugger wording found during the old→new semantic walk;
- keeps agent permission/frontmatter policy and all bundled third-party/vendor skill content unchanged.

Fresh isolated behavioral replay of ST-130..ST-133 is not claimed unless separately executed.

See `docs/releases/v30.95-beta.md` (archived) and `docs/contract-protocol-audit-v30.95.md` (archived).

## v30.94 beta

Runtime-residency split of the always-loaded root without changing permissions or third-party skills:

- shrinks global `AGENTS.md` from the mixed universal+workflow-owner contract into a universal semantic kernel; primary-entry, delegation-caller, and implementation/judgment procedure now live in three pack-owned conditional skills: `workflow-entry`, `delegation-control`, and `implementation-contract`;
- marks all three shared control skills `opencode/autoinvoke: "false"` and activates them explicitly from role contracts according to the **current invocation** rather than agent capability alone; `mode: all` roles skip primary/caller contracts while delegated;
- moves request normalization, Startup/Update, approval/publication gates, durable-planning activation and workflow-final reporting to `workflow-entry`; generic handoff/routing/fresh-child/review-cadence/resource-reconciliation to `delegation-control`; and mutation/regression/verification-freshness engineering procedure to `implementation-contract`;
- keeps universal authority/evidence, capability/assignment boundaries, skill/vendor containment, continuity, communication, and evidence-bound final claims in root;
- adds a separate runtime-residency/audience manifest, audit and selftest so a correct semantic owner cannot justify leaking conditional procedure into every role's standing context;
- updates semantic ownership, section placement, handoff/static oracles and skill control for the new conditional-owner graph instead of requiring old root-local copies;
- adds ST-127..ST-129 for ownership-vs-residency, delegated `mode: all` activation, and exact implementation-contract activation;
- leaves all 19 agent permission/frontmatter blocks and all 13 vendor skill subtrees byte-identical to v30.93.

Fresh isolated behavioral replay of ST-127..ST-129 is not claimed unless separately executed.

See `docs/releases/v30.94-beta.md` (archived) and `docs/contract-protocol-audit-v30.94.md` (archived).

## v30.93 beta

Whole-pack skill ownership/type hardening without modifying bundled third-party skills:

- adds a closed-world `skill-control` manifest/audit/selftest for all 22 bundled skill entrypoints: 9 pack-controlled and 13 vendor-advisory; vendor subtrees are SHA-256 guarded and remain byte-identical to v30.92;
- expands semantic ownership from 15 to 28 declared capabilities so pack-owned skills become first-class owner/consumer nodes rather than opaque conditional text;
- extends typed-domain coverage into declared pack skills and registers `resource-lifecycle` terminal states plus owned-PR lifecycle states;
- moves the canonical contemporaneous provenance-receipt schema to root §2.2.1; `code-orchestrator` produces/references it and `session-evidence` consumes it without redefining the fields;
- compacts `persistent-planning` to fallback representation/resume/work-package mechanics while root §2.3 retains activation and canonical-state ownership;
- compacts `graymatter-memory` to GrayMatter identity/query/checkpoint/write/correction mechanics while root retains memory authority/activation/freshness/durability semantics;
- compacts `verification-strategy` to layer selection, batching/cadence, tester activation, and blocked-boundary handling while root retains universal evidence validity/freshness rules;
- keeps Alibaba/Jeffallan/UUPM skill bytes unchanged and strengthens only pack-owned containment: reviewer consumes deterministic OCR preflight mechanics without accepting vendor host-review method, managed OCR activation stays reviewer-owned, and UUPM install/persist/default/source-of-truth directives remain advisory under `ui-component-sources`;
- adds ST-123..ST-126 for pack-skill second-owner regression, skill-side typed collision, vendor containment, and root↔skill ownership composition.

Agent permission/frontmatter policy is intentionally unchanged.

Fresh isolated behavioral replay of ST-123..ST-126 is not claimed unless separately executed.

See `docs/releases/v30.93-beta.md` (archived) and `docs/contract-protocol-audit-v30.93.md` (archived).

## v30.92 beta

Typed semantic-domain hardening and root/orchestrator placement cleanup:

- keeps `unverified` exclusively in the evidence/verification-status domain and changes the trajectory-auditor missing-primary-evidence workflow verdict to `insufficient-evidence`;
- adds a typed semantic-domain manifest/audit/selftest that inventories durable evidence/relation/verdict literals, discovers role verdict enums, and rejects one literal reused across incompatible domains;
- expands cross-layer semantic ownership from 9 to 15 declared capabilities, including fresh-review isolation, review activation/reuse, user-decision binding, publication authorization, failed-fix reset, and issue/PR workflow mechanics;
- adds an exact root/orchestrator section-placement map plus audit/selftest so new or moved material sections require an explicit owner/reference/specialization classification;
- removes remaining root-owned policy restatements from `code-orchestrator` for fresh-review isolation, review cadence, user-decision binding, publication authorization, and failed-fix reset while preserving role-local construction/consumption method;
- moves detailed issue/ticket/report mechanics out of root normalization and colocates them with `Existing PR follow-up` under the orchestrator's `Workflow behavior`; `pr-readiness` remains the canonical owner of the owned-PR Draft/Candidate/Ready lifecycle;
- updates old handoff/static test oracles that had required duplicated fresh-review policy in the orchestrator; edge tests now accept inherited root policy and reject contradictory caller steering instead;
- adds ST-121 (typed state-domain collision) and ST-122 (issue/PR workflow-placement ownership).

Permission/frontmatter policy is intentionally unchanged in this release.

Fresh isolated behavioral replay of ST-121/ST-122 is not claimed unless separately executed.

See `docs/releases/v30.92-beta.md` (archived) and `docs/contract-protocol-audit-v30.92.md` (archived).

## v30.91 beta

Generic cross-layer semantic-ownership control plane:

- promotes canonical ownership from a design-checklist principle into a manifest-driven release gate over material shared contracts;
- declares canonical owner plus downstream `reference` / `consume` / `specialize` relations for the current root↔orchestrator↔reviewer/skill shared semantic graph;
- rejects a consumer that becomes a second consistent definition of a shared contract, including paraphrased handoff-schema duplication, even when role executability and behavior would otherwise remain green;
- adds synthetic anti-gaming selftests proving clean owner references and legitimate specialization still pass while a paraphrased duplicate, missing activation, or owner drift fails;
- clarifies that role executability is **inherited shared contract + role-local method**, so evals must not force consumers to repeat root/skill-owned vocabulary merely to obtain PASS;
- adds ST-120 for the failure class where static/behavioral correctness hides duplicate semantic ownership.

Fresh isolated behavioral replay of ST-120 is not claimed unless separately executed.

See `docs/releases/v30.91-beta.md` (archived) and `docs/contract-protocol-audit-v30.91.md` (archived).

## v30.90 beta

Decision-boundary hardening plus root/orchestrator semantic-owner deduplication:

- adds an explicit downstream **decision boundary** for independent judgments so a Candidate review pass cannot be laundered into Ready/merge/release authorization whose prerequisites were not adjudicated;
- keeps review reuse: the same still-valid whole-Candidate verdict may feed later lifecycle gates without ceremonial re-review, while each gate still evaluates its own prerequisites;
- makes root the canonical owner for shared specialist handoff shape, decision-space preservation, generic mutation concurrency, task-semantic authority/evidence definitions, generic evidence freshness, routing defaults, and common final-report fields;
- compacts `code-orchestrator` to workflow-owner execution/consumption semantics: owner-model reconstruction state, routing discriminators, parent-hypothesis guard, whole-review construction/consumption, readiness reversal, controller use, and code-workflow-specific terminal evaluator mechanics;
- moves the temporary `session-evaluator` invocation procedure to its actual workflow owner while leaving only a root activation pointer;
- adds ST-119 and structural guards for review-verdict → lifecycle-gate laundering;
- fixes the prior validation wording that reported Unicode character counts as bytes.

No fresh isolated behavioral replay is claimed unless separately executed.

See `docs/releases/v30.90-beta.md` (archived) and `docs/contract-protocol-audit-v30.90.md` (archived).

## v30.89 beta

Whole-scope review, handoff-quality, owner-hypothesis, and fresh-memory-continuity hardening:

- requires final whole-PR/whole-change review to receive a whole authoritative acceptance model rather than only the latest fix/risk slice; structural `Coverage: full PR` no longer compensates for omitted semantic acceptance areas;
- prevents `code-orchestrator` from promoting qualified/slice-limited reviewer verdicts into whole readiness and distinguishes structural diff coverage, semantic acceptance-model coverage, and separately deferred executable/live proof;
- prevents parent-generated technical inferences or one-layer compatibility observations from becoming `preserve`/`required` constraints or test oracles without stronger authority or discriminating end-to-end evidence;
- treats a related material blocker after a readiness/publication claim as owner-reassessment evidence before another local fix/review/Ready cycle; repeated reopenings widen the reassessment instead of resetting confidence after each local pass;
- strengthens generic specialist handoff ergonomics: packets must be minimally sufficient, reconstructable, and readable rather than serialized/overcompressed session dumps that blur baseline, scope, authority, or evidence state;
- clarifies GrayMatter continuity: a fresh independent child does not resume the parent's long-running workstream through checkpoint/memory recovery. Memory capability may remain enabled; actual injected/retrieved steering still contaminates the fresh review;
- updates `pr-readiness`, `session-evaluator`, the semantic design checklist, handoff/static guards, and adds ST-113…ST-118 for these failure classes.

No fresh isolated behavioral model replay is claimed by this release unless separately executed.

See `docs/releases/v30.89-beta.md` (archived) and `docs/contract-protocol-audit-v30.89.md` (archived).

## v30.88 beta

Fresh-review capability-versus-context clarification:

- distinguishes mere availability of memory/connectors/tools/permissions from task-specific content actually exposed in model-visible context; capability availability alone does not contaminate a fresh review;
- forbids speculative blocking or integration reconfiguration merely because prior context could theoretically be retrieved; actual task-specific judgmental/investigative content must be observed before freshness is treated as contaminated;
- tells fresh reviewers not to proactively retrieve prior-task/session memory for context enrichment and to use authoritative user/task/project records rather than recalled memory for task semantics;
- preserves the hard stop when prior findings, fix history, expected weak points, investigative plans, or equivalent steering are actually injected or retrieved into the reviewer context;
- adds ST-111/ST-112 and static/handoff guards for both sides of the distinction: available recall capability is non-contaminating, actually exposed prior-task steering remains contaminating.

No change is made to GrayMatter availability, memory-tool permissions, reviewer read-only permissions, targeted partial re-review, publication lifecycle, or the v30.87 investigative-context isolation rule. Fresh isolated behavioral replay remains separate evidence and is not claimed unless actually run.

See `docs/releases/v30.88-beta.md` (archived) and `docs/contract-protocol-audit-v30.88.md` (archived).

## v30.87 beta

Fresh whole-change review investigative-context isolation hardening:

- defines fresh-review independence by the function of information exposed to the reviewer, not by headings, formatting, or placement;
- prohibits parent-derived investigative direction in fresh whole-change handoffs, including prior-fix-derived risk maps, named investigative surfaces, method/checklist decomposition, suggested probes/edge cases, test/stress recipes, expected findings, and claimed-clean areas;
- keeps authoritative task/acceptance propositions and exact authority-required review constraints, but requires recoverable provenance and forbids parent-added investigative elaboration;
- makes parent provenance labels locators rather than proof of authority and requires unresolved authority to remain unresolved instead of being laundered through the handoff;
- makes `reviewer` derive affected surfaces, risk model, investigation strategy/order, probes, and coverage method independently from the authoritative contract and actual Candidate;
- expands semantic transition scenarios to ST-110 with generic methodology-seeding and provenance-laundering regressions while preserving targeted/partial re-review semantics.

No runtime semantic change is made to implementation/debug/test/UI roles, controller activation, publication lifecycle, or the v30.85 accountable-owner model. Fresh isolated behavioral replay remains separate evidence and is not claimed unless actually run.

See `docs/releases/v30.87-beta.md` (archived) and `docs/contract-protocol-audit-v30.87.md` (archived).

## v30.86 beta

Fresh whole-change review independence hardening:

- removes parent-authored `Focus` / recent-fix / risk-checklist / test-recipe framing from fresh whole-change/final reviewer assignments; authoritative required behavior stays in the task contract, established mechanisms stay separately labelled implementation constraints, and review history remains in orchestrator state until post-review reconciliation;
- allows user- or project-policy-requested review emphasis only with provenance and only as additive/non-exhaustive emphasis; it cannot become the whole-review plan or scope;
- makes `reviewer` defend fresh judgment-context isolation: if a nominally fresh whole-change assignment already exposes prohibited prior findings/fix history/expected checks, the context is contaminated and reviewer must request a clean fresh assignment instead of claiming an independent whole-change verdict;
- preserves targeted/partial re-review semantics: a known finding and discriminating reproduction may define that partial scope, but the result cannot stand in for final fresh whole-PR review;
- adds a dedicated high-risk `code-orchestrator -> reviewer` handoff profile, raising high-risk profiles from 16 to 17, and adds ST-107/ST-108 for recent-fix Focus rejection and explicit user/project emphasis preservation.

`pr-readiness` semantics are unchanged: after `changes required`, a corrected Candidate gets a new final Base→Candidate whole-PR review; a separate targeted re-review is optional, not required. Therefore recent-fix history does not need to be seeded into the final whole-PR reviewer.

No runtime semantic change is made to implementation/debug/test/UI roles, skills, publication policy, or the v30.85 owner/control-plane model. Fresh isolated behavioral replay remains a separate evidence class and is not claimed unless actually run.

See `docs/releases/v30.86-beta.md` (archived) and `docs/contract-protocol-audit-v30.86.md` (archived).

## v30.85 beta

Accountable workflow-owner control plane:

- strengthens `code-orchestrator` from stage coordinator into the accountable owner of the user-authorized engineering outcome, with a bounded `ingest -> reconcile -> update whole-task model -> decide -> delegate` loop before material downstream transitions;
- makes specialist next-role/mechanism/remediation recommendations non-binding inputs rather than workflow transitions, and permits narrow direct read-only factual reconciliation when another agent hop would add no value;
- moves repeated-correction, same-policy-counterexample, fix-level/ownership-model and completion-risk patterns to **owner self-reassessment first**; `trajectory-auditor` becomes a second opinion only for a concrete residual longitudinal question after that reassessment (or explicit user request);
- narrows `semantic-checkpoint` to residual authority-sensitive semantic propositions after owner reconciliation or explicit policy-mandated independent judgment, rather than routine technical owner/fix-level/abstraction changes under settled behavior;
- extends `session-evaluator` with workflow-owner quality checks for parent synthesis, task-model continuity, specialist pass-through, and controller over/under-use;
- adds a high-risk `code-orchestrator -> semantic-checkpoint` handoff profile, strengthens the trajectory-auditor edge, adds owner/control-plane core capabilities to contract audit, and expands semantic transition scenarios to ST-106;
- hardens the synthetic contract suite so explicit `specialist pass-through` and `controller-first` orchestrator mutations now fail promotion.

No runtime semantic change is made to implementation/debug/review/test/UI roles, skills, root authority/evidence semantics, publication policy, or installer control flow beyond the v30.85 identity.

Fresh isolated behavioral replay remains a separate evidence class and is not claimed unless actually run.

See `docs/releases/v30.85-beta.md` (archived) and `docs/contract-protocol-audit-v30.85.md` (archived).

## v30.84 beta

Policy-boundary trajectory synthesis:

- makes `code-orchestrator` preserve semantically convergent `report-only`, `pre-existing`, and locally `out-of-scope` counterexamples when they weaken the same classifier/normalizer/policy boundary, instead of discarding them from workflow-level reasoning;
- requires fresh trajectory audit before another representative-specific mutation or a readiness/publication transition when such cumulative same-policy counterevidence indicates the current abstraction model is no longer safely assumed closed;
- makes `reassess` handoffs ask for the unresolved owner/representation/invariant or strategy model while treating current files/functions/call sites as evidence, not a preselected solution boundary;
- keeps the rule non-prescriptive: neither orchestrator nor trajectory-auditor mandates a helper/refactor/architecture;
- adds ST-95 for same-policy residual counterexamples and ST-96 as the unrelated-low-note anti-overreach control.

No runtime semantic change is made to `debugger`, `reviewer`, `build`, `tester`, `semantic-checkpoint`, `session-evaluator`, UI roles, skills, or root authority/evidence semantics.

Fresh isolated behavioral replay remains a separate evidence class and is not claimed unless actually run.

See `docs/releases/v30.84-beta.md` (archived) and `docs/contract-protocol-audit-v30.84.md` (archived).

## v30.83 beta

Longitudinal trajectory auditing:

- adds read-only `trajectory-auditor` for mid-workflow cumulative task-anchor/progress checks without taking workflow, implementation, review, planning, or post-hoc diagnostic ownership;
- makes `code-orchestrator` retain a task anchor for non-trivial multi-stage work and trigger trajectory audit only on evidence-shaped cumulative-risk boundaries rather than turn/fix counts;
- detects local-success/global-nonprogress chains, hypothesis laundering, acceptance erosion, scoped-evidence overclaim, and clustered correction boundaries while preserving staged-work, isolated-fix, and independent-defect counterexamples;
- adds distinct trajectory verdicts `continue | reanchor | reassess | checkpoint-required | unverified`, with semantic propositions still routed to the existing `semantic-checkpoint`;
- adds a dedicated role-executability profile, a high-risk `code-orchestrator -> trajectory-auditor` handoff profile, synthetic negative handoff coverage, and ST-85…ST-94.

No runtime semantic change is made to `build`, `debugger`, `reviewer`, `tester`, `semantic-checkpoint`, `session-evaluator`, UI roles, skills, publication policy, or installer control flow beyond the new role being installed as part of the normal agents directory.

Fresh isolated behavioral replay remains a separate evidence class; this release records it only if actually run.

See `docs/releases/v30.83-beta.md` (archived) and `docs/contract-protocol-audit-v30.83.md` (archived).

## v30.82 beta

Debugger falsification-loop hardening:

- strengthens only `agents/debugger.md` at runtime: non-trivial bugfixes now concretize the relevant root §7.3 case map before selecting the fix and use materially different representatives to falsify the diagnosis/fix model;
- makes target-environment/external-grammar/API/tool/runtime conditions part of the evidence when they are material to the claim, so a convenient local surrogate cannot silently stand in for the target semantics;
- requires debugger to reset or escalate when an assignment premise, fixture, mechanism/constraint, or remediation conflicts with stronger behavior/evidence instead of implementing it merely because the handoff was explicit;
- adds a pre-return falsification gate that rejects correlated self-tests as closure when they share the implementation assumption and requires evidence gaps to remain explicit for unclosed established classes;
- adds ST-80…ST-84 covering contradictory debugger handoffs, target-environment fidelity, non-reproducing diagnosis, correlated reviewer evidence for external semantics, and opaque provider failures promoted too early into fix recipes.

No runtime semantic change is made to `build`, `reviewer`, `code-orchestrator`, root policy, permissions, topology, skills, or installer control flow. Their new scenarios are regression evidence for already-owned behavior, not new owners or duplicated policy.

Fresh isolated behavioral replay of ST-01…ST-84 remains separate evidence and is not claimed by static/contract/package validation.

See `docs/releases/v30.82-beta.md` (archived) and `docs/contract-protocol-audit-v30.82.md` (archived).

## v30.81 beta

UI routing discriminator hardening:

- fixes a `code-orchestrator` routing gap between already-good `@ui-orchestrator` and direct `@ui-implementer` handoffs;
- makes a known functional requirement insufficient by itself to classify a UI outcome as settled when material layout/information-hierarchy/disclosure/interaction/error-state choices remain;
- routes rejected-but-not-replaced UI treatments through the bounded UI workflow owner instead of letting the code orchestrator invent the replacement and launder it as an implementation recipe;
- preserves direct focused `@ui-implementer` work when the user, an adopted plan, or a sufficiently specific existing project pattern has already settled the material UI treatment;
- adds a high-risk `code-orchestrator → ui-orchestrator` handoff profile, a synthetic negative selftest, static ownership guards, and ST-79 with a direct-implementation preservation counterexample.

Fresh isolated behavioral replay of ST-01…ST-79 remains separate evidence and is not claimed by static/contract/package validation.

See `docs/releases/v30.81-beta.md` (archived) and `docs/contract-protocol-audit-v30.81.md` (archived).

## v30.80

- Promotes the validated v30.80 beta candidate to stable.
- Runtime semantics, role permissions, skills, installer behavior, and licensing are unchanged from the beta candidate.
- Updates the pack version marker, installer receipt identity, and current-release documentation links to stable `v30.80` / `docs/releases/v30.80.md`.
- Fresh isolated behavioral replay of ST-01…ST-78 remains separate evidence and is still not claimed by this promotion.

See `docs/releases/v30.80.md` (archived) and `docs/contract-protocol-audit-v30.80.md` (archived).

## v30.80 beta

Semantic ownership, discovery, installer-safety, and licensing hardening:

- fixes `project-planner` attribution so root §2.3 owns persistent-planning activation/canonical-state policy while `persistent-planning` owns fallback representation/resume procedure; an unwritable project canonical plan is read as authority and returned to an authorized writer instead of forking into a parallel plan;
- separates checkpoint workflow verdict (`proceed | hold | insufficient-context`), evidence status (`established | unverified | contradicted`), and proposition relation (`preserved | refined | strengthened | weakened | substituted | indeterminate`);
- deduplicates root-owned weaken/substitute semantics from `semantic-checkpoint` / `session-evaluator` while preserving their role-specific gate/diagnostic actions;
- strengthens `explore` against false negative and inferred-flow success: scoped absence claims, alias/reference/generated/config search, and actual call/data/state relation edges;
- makes package runners that may fetch missing tooling subject to the existing new-tooling gate and makes the managed OCR install path explicitly approval-gated;
- hardens both installers: project-owned `AGENTS.md` is never silently replaced, unknown global `AGENTS.md` blocks before mutation, collisions are backed up, ownership receipts support safe stale cleanup, and filename-only legacy cleanup is replaced with preserve-and-warn unless ownership is proven;
- licenses pack-authored material under MIT with retained GitHub attribution and adds third-party license/notices for established bundled provenance;
- adds ST-76…ST-78 plus installer behavioral selftests and stronger discovery/semantic-gate contract checks.

Fresh isolated behavioral replay of ST-01…ST-78 remains separate evidence and is not claimed by static/contract/package validation.

See `docs/releases/v30.80-beta.md` (archived) and `docs/contract-protocol-audit-v30.80.md` (archived).

## v30.79 beta

Reviewer / managed-OCR independence hardening:

- makes managed OCR explicitly additional independent evidence rather than a substitute for host-review coverage or reasoning;
- requires `@reviewer` to maintain its own authoritative changed/effective-diff ledger even when OCR selects, completes, or comments on the same files;
- separates result evidence into host structural coverage and managed-OCR selected/completed/failed scope, so `OCR coverage ∪ host coverage` cannot be reported as host `full PR` coverage;
- requires host reconciliation of material OCR comments and states explicitly that zero OCR findings do not establish correctness;
- adds a reviewer-specific protocol/selftest guard and ST-75 for the complement-coverage failure class observed in a fresh whole-PR trace;
- updates the Semantic Design Manual with the general owner-coverage rule without changing delegation topology, permissions, or managed-OCR invocation mechanics.

Fresh isolated behavioral replay of ST-01…ST-75 remains separate evidence and is not claimed by static/contract/package validation.

See `docs/releases/v30.79-beta.md` (archived) and `docs/contract-protocol-audit-v30.79.md` (archived).

## v30.78 beta

Orchestrator communication and decision-context hardening:

- adds role-local milestone synthesis so long multi-stage `code-orchestrator` workflows expose meaningful workflow state without narrating every tool call or specialist invocation;
- requires evidence-resolvable factual/technical uncertainty to be resolved before asking the user, while leaving implementation discretion with its owning role;
- makes material user choices self-contained even when the underlying evidence came from hidden child sessions/tool output: affected surface, why it matters, established facts, viable alternatives/consequences, evidence-supported recommendation when available, then the exact proposition;
- adds adversarial/preservation regressions for under-communication, status spam, hidden-context questions, and unnecessary user escalation of evidence-resolvable ambiguity;
- updates the Semantic Design Manual/source-preservation audit with current OpenAI GPT-6 and Anthropic Opus 5.5 guidance that supports these abstractions.

Fresh isolated behavioral replay of ST-01…ST-74 remains separate evidence and is not claimed by static/contract/package validation.

See `docs/releases/v30.78-beta.md` (archived) and `docs/contract-protocol-audit-v30.78.md` (archived).

## v30.77 beta

Delegated-specialist README/topology consistency:

- corrects `README.md` so `## Delegated specialists` reflects actual classified delegation targets rather than only `mode: subagent` roles;
- includes delegated `mode: all` roles (`build`, `project-planner`, `librarian`, `ui-orchestrator`) alongside subagent-only specialists;
- adds a generic release guard that derives the expected delegated-specialist set from `delegation` / `conditional_delegate` edges in the closed-world topology and fails on missing or stale README entries;
- leaves all 18 runtime agent contracts, 22 skill contracts, and the 57-edge runtime topology unchanged from v30.76.

Fresh isolated behavioral replay of ST-01…ST-70 remains separate evidence and is not claimed by this documentation/eval consistency release.

See `docs/releases/v30.77-beta.md` (archived) and `docs/contract-protocol-audit-v30.77.md` (archived).

## v30.76 beta

External technical evidence specialist:

- adds `librarian` as the 18th model-agnostic role, `mode: all`, read-only, owning bounded external product/library/API/upstream propositions with exact version/applicability and inspectable provenance;
- keeps semantic ownership disjoint: `explore` owns repository-local descriptive evidence, `librarian` owns external technical evidence, and `project-planner` owns prospective implementation structure; `general` remains only the unmatched fallback;
- adds direct/top-level routing plus `code-orchestrator -> librarian` and `auditor -> librarian` delegation contracts; leaf roles return adjacent external-evidence needs to the caller rather than spawning a new chain;
- adds an `external_research` contract-audit profile covering target/version binding, source authority/applicability/directness, conflict reconciliation, false-success handling, and bounded result semantics;
- keeps Librarian output human: answer first, strongest applicable sources/provenance, and conflicts/limitations only when material; no mandatory empty report sections;
- expands the closed-world topology from 54 to 57 relations and the semantic-transition suite from ST-01…ST-64 to ST-01…ST-70.

Fresh isolated behavioral replay of ST-01…ST-70 remains separate evidence and is not claimed by static/contract/package validation.

See `docs/releases/v30.76-beta.md` (archived) and `docs/contract-protocol-audit-v30.76.md` (archived).

## v30.75 beta

README navigation deduplication:

- removes repeated explanations that `AGENTS.md` is the canonical workflow-policy surface from `What this pack is`, `Start here`, the documentation map, and footer;
- removes the meta sentence `README is the usage and navigation map` and related narration about policy living outside README;
- keeps a single ownership/navigation table under `Where the rules live`;
- narrows the bottom documentation table to release/design evidence instead of repeating the runtime-policy/agent/skill map;
- preserves `AGENTS.md` mentions that are operational rather than architectural duplication: install paths and the title of an external reference;
- runtime agent/skill contracts and workflow semantics remain unchanged from v30.74.

See `docs/releases/v30.75-beta.md` (archived) and `docs/contract-protocol-audit-v30.75.md` (archived).

## v30.74 beta

Role-contract semantic-shape standardization:

- standardizes substantive role contracts by semantic function — `Ownership → Invocation → Method → Boundaries → Result` — without imposing identical Markdown headings or prompt length;
- audits all 17 current roles against that shape and finds no runtime rewrite necessary: each function already has a clear primary locus;
- adds ST-64 so heading/template conformity cannot substitute for executable role semantics and cosmetic standardization cannot justify duplicate policy;
- records a deferred `librarian` / external-technical-evidence capability TODO for future design, without adding a runtime role in this release;
- runtime agent and skill contracts remain unchanged from v30.73.

See `docs/releases/v30.74-beta.md` (archived) and `docs/contract-protocol-audit-v30.74.md` (archived).

## v30.73 beta

README provenance restoration:

- restores `External integrations` links for external projects used by bundled skills/docs;
- restores `Prompt and evaluation design references` for OpenAI, Anthropic, DeepSeek, and Z.ai/GLM sources used to shape the pack;
- keeps README as a usage/navigation/provenance surface rather than duplicating runtime policy;
- intentionally does not restore the former `Runtime references` section;
- runtime agents, skills, and workflow semantics remain those of v30.72.

See `docs/releases/v30.73-beta.md` (archived).

## v30.72 beta

README current-state cleanup:

- removes the bottom `Current release` changelog-style section from README;
- removes release-delta/meta wording from README so it describes current package usage rather than what changed from the previous version;
- keeps release history and release-specific validation in `CHANGELOG.md` and `docs/releases/`;
- runtime agents, skills, and workflow semantics remain those of v30.71.

See `docs/releases/v30.72-beta.md` (archived).

## v30.71 beta

- Rebuilds README as a usage/navigation map rather than a second workflow policy.
- Makes `code-orchestrator` explicit as the main top-level owner for multi-step coding/PR/bug/release workflows and separates entry owners from delegated specialists.
- Removes duplicated Startup, PR lifecycle, verification cadence, semantic-role procedure, and release-validation policy from README; canonical details remain in `AGENTS.md`, role/skill contracts, and the semantic-design manual.
- Runtime agents/skills are unchanged from v30.70; root semantic policy is unchanged apart from the version marker.
- Makes the README current-release static guard layout-agnostic so it verifies the active release-note link rather than one historical table rendering.

See `docs/releases/v30.71-beta.md` (archived).

## v30.70 beta

- Adds role lifecycle requalification to the existing semantic-design manual: topology/mode/caller expansion, substantive ownership transfer, and advisory→mutation/verdict changes invalidate inherited role PASS and require fresh role/edge audit.
- Adds method-preservation checks for canonical-owner moves and prompt compaction so deduplication cannot delete the only executable procedure while leaving ownership labels intact.
- Makes role-handoff inventory closed-world across every pack-owned root/agent `@role` relation; current topology is 54/54 discovered/classified and both unknown and stale relations fail release.
- Extends role/edge synthetic selftests and static guards for new roles without profiles, unknown/stale edges, lifecycle/manual retention, and inventory anti-gaming.
- Adds ST-61…ST-63; runtime agent contracts are unchanged from v30.69.

See `docs/releases/v30.70-beta.md` (archived) and `docs/contract-protocol-audit-v30.70.md` (archived).

## v30.69 beta

- Repairs every unresolved role-contract finding from the frozen v30.68 audit baseline while keeping `contract-protocol-audit.py` v3 unchanged.
- Adds role-owned execution methods for `a11y-reviewer`, `devops`, `general`, `ui-auditor`, `ui-implementer`, and `ui-planner`, plus explicit conflicting/partial specialist reconciliation in `auditor`.
- Adds end-to-end caller-side invocation contracts in `code-orchestrator`, `ui-orchestrator`, and `auditor` so downstream roles receive the target/state/mode/action/evidence inputs their methods require without upstream recipe anchoring.
- Adds a separate role-handoff edge audit/selftest; release gates now require both role executability and caller→callee compatibility.
- Adds ST-53…ST-60 and manual-checklist coverage for the repaired capabilities and handoff edges.
- Frozen role audit result is **17 PASS / 0 REVIEW / 0 FAIL**; edge audit is **11/11 PASS**. Fresh isolated behavioral replay remains pending.

See `docs/releases/v30.69-beta.md` (archived) and `docs/contract-protocol-audit-v30.69.md` (archived).

## v30.68 beta

- Removes size/sparsity from role status decisions; prompt length is diagnostic only.
- Separates essential non-executable core gaps (`FAIL`) from material gaps in otherwise executable roles (`REVIEW`).
- Adds profile-specific false-success/adversarial challenges and ST-52 severity calibration.
- Synthetic self-tests now require a compact executable discovery role to PASS and an otherwise executable audit orchestrator with missing conflict reconciliation to REVIEW.
- Frozen pre-repair audit result is **6 FAIL / 1 REVIEW / 10 PASS**, exactly matching manual adjudication; runtime agents remain unchanged.

See `docs/releases/v30.68-beta.md` (archived) and `docs/contract-protocol-audit-v30.68.md` (archived).

## v30.67 beta

- Tightens role-contract release gating so expected vocabulary or a shared-policy pointer cannot substitute for an executable role-local method.
- Adds profile-specific core-loop checks, role-local action/decision/sequence evidence, and method-vs-result separation.
- Adds release-blocking `REVIEW` for sparse contracts instead of silently granting PASS or imposing a fixed prompt-size quota.
- Adds synthetic anti-gaming tests proving keyword stuffing fails, generic DevOps safety rules do not replace diagnostic isolation, and a compact executable discovery role is not hard-failed solely for size.
- Adds ST-49…ST-51 and updates the semantic-design manual with the stricter role-executability gate.
- Current audit result is **7 FAIL / 2 REVIEW / 8 PASS**; runtime agent contracts are intentionally unchanged so the detector is evaluated against the same object.

See `docs/releases/v30.67-beta.md` (archived) and `docs/contract-protocol-audit-v30.67.md` (archived).

## v30.65 beta

- Fixes cross-role handoff contamination: upstream plans/checkpoints/reviews no longer become binding mutation recipes merely because they are technically plausible or were returned by a specialist.
- Clarifies root mechanism ownership: implementation/design mechanisms are selected by the role/authority that owns that choice; other roles may propose only non-binding hypotheses unless authority requires the mechanism.
- Narrows `semantic-checkpoint` to semantic authorization of a mutation boundary; `proceed` no longer certifies implementation/design adequacy or recommends forwarding the candidate/checkpoint report unchanged.
- Reconstructs edit-capable handoffs from established outcome/constraints/evidence; correction handoffs to `@debugger` carry the defect/invariant/evidence rather than reviewer/tester patch recipes.
- Adds matching protection for UI plan/audit → implementation handoffs and evaluator diagnostics.
- Extends semantic regression/static guards for cross-role recipe laundering and correction-handoff anchoring.


## v30.64 beta

- Strengthens `build` with a contract-derived falsification pass across every materially relevant already-established case class, rather than relying on the requested case plus one nearby negative.
- Requires representative probes to come from the behavioral contract/owning abstraction; multiple self-authored tests sharing the same implementation assumption do not establish closure.
- Keeps the case map proportional to risk: no arbitrary cross-product expansion and no invented semantic classes.
- Adds six trace-derived, domain-neutral builder regression scenarios ST-38…ST-43.

See `docs/releases/v30.64-beta.md` (archived).

## v30.63 beta

- Strengthens `build` first-pass implementation quality without adding a new root semantic owner: checkpoint/handoff approval is authorization for a semantic boundary, not an implementation recipe or correctness proof.
- Adds a role-local pre-edit implementation-proof gate: establish required outcome, exact implementation constraints, the narrowest existing owner/primitive, nearest preserved behavior/invariant, and affected callers/states before semantic mutation.
- Adds mandatory pre-return implementation self-review of the exact final diff/state plus changed-and-preserved verification; a green focused case no longer suffices when the implementation proof includes uncovered preserved behavior or shared consumers.
- Adds ST-36/ST-37 and static guards for blind handoff-mechanism execution and returning a locally green but implementation-locally detectable regression.

See `docs/releases/v30.63-beta.md` (archived).

## v30.62 beta

- Prevents a returned `@build` package from entering a blind review-fix loop: once valid independent reviewer/tester/CI/reproduction evidence establishes a concrete product-code defect requiring correction, the next mutation is routed as bugfix/root-cause work to `@debugger`.
- Keeps build-local self-correction valid before the package is returned and keeps purely mechanical non-bug/tests/docs corrections with their normal owner.
- Adds a build-side reroute boundary so an incorrectly assigned post-return confirmed defect is rejected instead of being absorbed as another ordinary build iteration.
- Adds ST-35 and static guards for build→review FAIL→same-build looping and preserves existing reset/escalation behavior when a debugger fix is rejected or findings converge on one invariant.

See `docs/releases/v30.62-beta.md` (archived).

## v30.61 beta

- Separates authoritative implementation constraints from candidate correctness: a selected mechanism constrains the solution but is not evidence of adequacy and does not waive unaccepted collateral regressions or tradeoffs.
- Hardens fresh reviewer handoffs so mechanism choices are passed only as proposition-scoped `implementation constraint` facts, never as accepted-design/correctness framing.
- Makes reviewer independence explicit for requested mechanisms and accepted tradeoffs, strengthens wrong-fix-level/workaround reporting, and adds general material performance/resource regression review beyond only contended-lock paths.
- Adds ST-33/ST-34 and owner-specific static guards for mechanism-as-correctness laundering and functionally-green performance/resource regressions.

See `docs/releases/v30.61-beta.md` (archived).

## v30.60 beta

- Adds root-owned judgment-context isolation for fresh independent specialist judgments, beyond merely using a fresh child-session identity.
- Makes fresh whole-change/final reviewer handoffs omit prior reviewer/OCR verdicts/findings, expected verdicts, fix-delta summaries, claimed-clean areas, and CI/test pass/fail framing until post-review reconciliation.
- Keeps targeted re-review valid only as an explicitly partial/incremental judgment that cannot satisfy a fresh whole-scope review stage.
- Extends `session-evaluator`, the semantic-design manual, ST-32, and static policy guards for independent-judgment context contamination.
- Adds a generic release-identity consistency guard and fixes a stale README footer version inherited from earlier betas.

See `docs/releases/v30.60-beta.md` (archived).

## v30.59 beta

- Restores `open-code-review-delegate` as mandatory deterministic preflight for code/diff/commit/branch/workspace/PR reviewer runs when the delegate skill establishes compatible local OCR delegation.
- Makes the fallback explicit: unavailable delegation is recorded and reviewer continues with native preflight; reviewer may not skip a compatible delegate merely because it appears unnecessary or low-risk.
- Keeps managed `open-code-review` / `ocr review` as a separate independent-model escalation.
- Adds ST-31 and an owner-specific static guard for the mandatory delegate-preflight contract.

See `docs/releases/v30.59-beta.md` (archived).

## v30.58 beta

- Generalizes the existing reviewer authoritative-domain operational check from value/parser/representation narrowing to accepted/supported behavior-domain narrowing by any non-authoritative operational surface.
- Makes packaging/build/release matrices explicit examples of evidence that cannot silently redefine the governing supported domain.
- Leaves root authority, qualifier, fallback, exact-candidate, and read-back policy unchanged; this is a reviewer-salience/runtime-operationalization refinement, not a new platform-specific policy.
- Keeps the 30-case semantic transition suite unchanged and strengthens the static reviewer guard for the generalized runtime wording.

See `docs/releases/v30.58-beta.md` (archived).

## v30.57 beta

- Classifies the motivating review miss as primarily execution/model failure and deliberately avoids adding another runtime reviewer/root rule before current-candidate replay demonstrates a remaining prompt gap.
- Broadens ST-24 from parser-only narrowing to any narrower non-authoritative operational/convenience surface that is incorrectly treated as the governing behavior domain.
- Adds ST-29 for exact Base/Candidate-bound review evidence freshness and ST-30 for mutation receipt versus authoritative post-mutation read-back.
- Updates semantic-design eval guidance; runtime agent/skill semantics remain unchanged from v30.56 apart from the root version marker.

See `docs/releases/v30.57-beta.md` (archived).

## v30.56 beta

- Defines specialist assignments as task-specific specialization of the selected standing role contract rather than replacement role definitions.
- Prevents call-site prompts from waiving/redefining role-owned obligations or verdict semantics and prevents partial diagnostics from being consumed as full-stage completion.
- Extends `session-evaluator` to audit assignment/role-contract composition.
- Expands semantic transition regressions from 27 to 28 cases with ST-28.

See `docs/releases/v30.56-beta.md` (archived).

## v30.55 beta

- Adds reviewer-owned composition checks for independently coexisting projections/refinements, including order/early-return paths that can silently erase an orthogonal projection.
- Promotes authoritative accepted-domain preservation into reviewer runtime methodology without duplicating the root evidence-fidelity owner.
- Extends fallback/recovery review to validate the semantic success postcondition of earlier stages whose reported success suppresses fallback.
- Expands semantic transition regressions from 25 to 27 cases with dedicated projection-composition and false-semantic-success fallback scenarios.

See `docs/releases/v30.55-beta.md` (archived).

## v30.54 beta

- Preserves exact provenance for material user decisions obtained through interactions that are not retrievable downstream, without promoting receipts or caller summaries into new authority.
- Adds reviewer-owned shared-state mutator composition checks for reconstruction/reconciliation behavior and reachability proof for claimed fallback/recovery paths.
- Expands semantic transition regressions from 21 to 25 cases; authoritative-domain oracle and counterexample-convergence scenarios remain eval-only probes of existing general rules.
- Adds trace reproducibility metadata requirements for a future executable replay runner without changing the user-visible Startup contract.

See `docs/releases/v30.54-beta.md` (archived).

## v30.53 beta

- Adds reviewer-owned bidirectional counterexample checks for material guard/classifier invariants.
- Makes actual candidate effects, not issue framing alone, determine review depth while keeping implementation authority bounded.
- Adds conditional call-chain cost tracing for changed work under contended critical resources.
- Expands semantic transition regressions from 18 to 21 cases and adds static/mutation guards for the new reviewer obligations.

See `docs/releases/v30.53-beta.md` (archived).

## v30.52 beta

- Allows the already-required `session-evidence` skill for `semantic-checkpoint` and `session-evaluator` without otherwise changing their permission policy.
- Makes static semantic guards owner-specific so documentation/manual text cannot satisfy assertions about missing active runtime guards.
- Adds effective-permission regression coverage for mandatory role→skill dependencies.
- Makes the temporary semantic-transition eval contract explicit about injected intermediate faults and separates proposition relation from evidence-state transitions.
- Extends the Semantic Design Manual release checklist with runtime-dependency reachability and owner-specific static-oracle checks.

See `docs/releases/v30.52-beta.md` (archived).

## v30.51 beta

- Migrates all pack-owned agent frontmatter to OpenCode V2 `permissions` rules with V2 action names while preserving the existing permission-policy intent.
- Corrects blocker/replacement semantics and evidence-vs-product-choice authority boundaries.
- Relayers owned-PR lifecycle, temporary-resource lifecycle, and UI component-source integration to one canonical owner each.
- Adds `ui-component-sources` as a pack-owned conditional integration skill without changing the established source order.
- Expands end-to-end semantic transition traces from 16 to 18 cases and adds executable static schema/ownership regression guards.

See `docs/releases/v30.51-beta.md` (archived).

## v30.50 beta

- Adds an isolated end-to-end semantic transition trace eval across the complete applicable workflow path.
- Requires each material semantic delta in replay to record what changed, why it changed, its cause/source, and the authority/evidence sufficient for that exact transition.
- Adds 16 synthetic adversarial/preservation scenarios, including two incident-independent regressions derived from observed source-authority/report-state and verification-qualifier failures.
- Extends the Semantic Design Manual and release checklist so per-file/cross-layer static audits do not substitute for fresh semantic-path replay.

See `docs/releases/v30.50-beta.md` (archived).

## v30.49 beta

- Separates task-semantic/product authority from action/policy precedence without changing the existing precedence hierarchy.
- Makes terminal `session-evaluator` instrumentation explicitly non-gating when the diagnostic invocation is unavailable or fails.
- Adds the conditional `session-evidence` skill as the single owner of OpenChamber session-history retrieval/pagination mechanics and removes those procedures from semantic role prompts.
- Removes OCR CLI/provider procedure duplication from `reviewer`; review integrations are consumed through their owning skills.
- Makes `pr-readiness` the single owner of the reusable owned-PR lifecycle/readiness sequence.
- Extends semantic release checks to cross-layer ownership, gating consistency, provider/API/CLI mechanism leakage from semantic roles, and finding ownership/provenance triage.

See `docs/releases/v30.49-beta.md` (archived).

## v30.48 beta

- Replaces the remaining evaluator-specific `PASS`/`BLOCK` proof labels with proposition-based evidence semantics.
- Generalizes semantic terminology validation to any origin-specific literal semantic state/value, not only presentation/color examples.
- Adds a rename-counterfactual release check for incidental local status/value names.

See `docs/releases/v30.48-beta.md` (archived).

## v30.47 beta

- Replaces presentation-specific success/failure color metaphors in active semantic/runtime guidance with outcome-based wording.
- Adds a generic Semantic Design Manual guard against deriving portable policy from incidental UI/status presentation.
- Adds presentation-neutral terminology validation alongside the existing semantic ownership/duplication checks.
- Corrects the stale root pack-version marker that still identified v30.45.

See `docs/releases/v30.47-beta.md` (archived).

## v30.46 beta

- Makes verification evidence proposition-scoped and requires material preconditions, qualifiers, scope, and oracle semantics to survive translation into tests/reproductions/benchmarks/traces/review evidence.
- Separates structural, behavioral, and evidentiary coverage; full file/diff review no longer implies full proof coverage.
- Makes reported success/failure from verification artifacts support product claims only after evidence-validity/causality checks, with proportional negative controls when they materially improve discrimination.
- Adds role-specific proof-obligation preservation and evidence-laundering detection without introducing another verification stage.

See `docs/releases/v30.46-beta.md` (archived).

## v30.45 beta

- Preserves the user's open decision space when exploratory/planning/architectural/diagnostic work is delegated; parent-originated candidate solutions remain non-exhaustive unless authority closes the choice set.
- Adds explicit proposition-preservation classification and treats materially different same-goal replacements as semantic substitution rather than ordinary implementation refinement.
- Makes semantic-checkpoint require separate authority or an established blocker before a candidate substitutes an established material proposition.
- Extends session-evaluator delegation and semantic-delta audits to detect parent-narrowed choice sets and unsupported substitutions.

See `docs/releases/v30.45-beta.md` (archived).

## v30.44 beta

- Makes adoption of a source proposition-scoped instead of inheriting authority for every statement in the source.
- Separates authority, evidence, implementation choice, and adequacy in semantic checkpoint/orchestrator handling.
- Preserves intended, reported, and independently verified action/outcome state across handoffs and retrospective evaluation.
- Makes session-evaluator report completion as reported-but-unverified when execution evidence is missing, rather than rewriting it as intent.

See `docs/releases/v30.44-beta.md` (archived).

## v30.43 beta

- Consolidates Markdown, brevity, and outcome-first writing rules under the root communication owner and removes duplicate generic formatting rules from `output-formatting`.
- Reduces `code-orchestrator` material-decision visibility text to a role-specific application of the root contract.
- Deduplicates repeated authority/evidence wording in gates, delegation, and regression guidance without removing their local behavioral consequences.

See `docs/releases/v30.43-beta.md` (archived).

## v30.42 beta

- Makes material decisions derived from new evidence visible before consequential downstream work while keeping routine execution narration suppressed.
- Requires concise, readable Markdown for free-form agent communication, including specialist assignments and handoffs, unless the destination requires another format.
- Extends session-evaluator diagnostics to detect silent material decision adoption from tool/specialist evidence.

See `docs/releases/v30.42-beta.md` (archived).

## v30.41 beta

- Passes already-known current/participating session IDs from `code-orchestrator` into session-aware read-only judgments.
- Makes `semantic-checkpoint` and `session-evaluator` consume supplied IDs directly and use `session.list` only to resolve missing session identity or parent/child relationships.
- Removes unconditional full-session-list discovery from those active evidence contracts.

See `docs/releases/v30.41-beta.md` (archived).

## v30.40

- Promotes the validated v30.40 beta candidate to stable.
- Updates the pack version marker and current-release documentation links to the stable `v30.40` / `docs/releases/v30.40.md` identity.

See `docs/releases/v30.40.md` (archived).

## v30.40 beta

- Relayers root policy using the Semantic Design Manual: global semantics stay in root; integration/procedural detail moves behind conditional skills.
- Makes GrayMatter recall relevance-triggered rather than mandatory on every task and moves detailed tool mechanics to `graymatter-memory`.
- Removes the static specialist/advisory catalog from root and uses runtime-exposed skill activation metadata.
- Moves persistent-planning file-layout/procedure detail to `persistent-planning` while retaining the durable-state trigger/contract in root.
- Narrows temporary `session-evaluator` instrumentation to terminal successful outcomes: satisfied session goal or final owned-PR readiness; it remains post-hoc and non-gating.
- Condenses mutation-mechanism guidance to target-bounded, understood transformations plus diff/state inspection.
- Bundled skill inventory is now 20 skills: 13 specialist/advisory and 7 workflow/policy skills.

See `docs/releases/v30.40-beta.md` (archived).

## v30.39 beta

- Preserves the v30.38 claim-level authority and semantic-correspondence rules.
- Adds compact user-facing workflow narration: Startup is the only routine pre-tool status, progress updates are material-only, and final/delegated reports omit routine narration and repeated context.
- Withdraws the v30.37 predecessor/ancestor provenance expansion after the observed missing-history failure was traced to OpenChamber `session.messages(all:true)` pagination rather than missing ancestor authority.
- Adds a semantic-design manual plus source-preservation audit for the developer references used to shape the pack.

See `docs/releases/v30.39-beta.md` (archived).

## v30.38 beta

- Makes user authority semantically bounded to the material proposition actually presented for decision.
- Prevents descriptive text, summaries, or handoffs from silently adding independently choosable semantics to a user selection.
- Preserves conditional/fallback qualifications across agent boundaries and requires a blocker or separate authority before weakening an established viable outcome.
- Adds role-specific semantic-delta checks to `code-orchestrator`, `semantic-checkpoint`, and `session-evaluator`.

See `docs/releases/v30.38-beta.md` (archived).

## v30.37 beta

- Extends provenance recovery beyond the current parent session when a workflow is explicitly a continuation/resume or materially depends on earlier authority/evidence.
- Requires `semantic-checkpoint` to follow only the material predecessor/ancestor chain before declaring historical authority unavailable.
- Requires `session-evaluator` to audit material predecessor provenance as well as the current parent and participating descendants, without ritual reads of unrelated prior sessions.
- Keeps continuation wording and parent/child restatements as pointers to recover primary authority, never as substitutes for it.

See `docs/releases/v30.37-beta.md` (archived).

## v30.36 beta

- Makes `semantic-checkpoint` establish retrieval coverage before treating historical user authority or material evidence as absent.
- Reads complete parent user history and full material child histories with `session.messages all: true`, using no incompatible `limit` / `last` selectors.
- Adds explicit recovery from `all + limit/last` usage errors instead of allowing a truncated fallback to drive `unverified`.
- Uses explicit large session discovery plus `parentID` relationships while avoiding ritual reads of unrelated sessions.

See `docs/releases/v30.36-beta.md` (archived).

## v30.35 beta

- Makes subagent session continuity follow assignment continuity rather than agent identity.
- Starts new specialist assignments and independent judgment stages in fresh child sessions by default; explicit child-session continuation is reserved for the same specialist-owned workstream.
- Requires every `semantic-checkpoint` verdict to run in a fresh child session so a later candidate is not anchored by an earlier checkpoint conversation.
- Keeps continuity available for genuine same-workstream investigation/implementation instead of imposing a blanket fresh-session rule on every repeated role call.

See `docs/releases/v30.35-beta.md` (archived).

## v30.34 beta

- Makes `code-orchestrator` consume checkpoint results as a bounded lifecycle decision rather than treating the verdict as a one-bit advisory.
- Keeps `proceed` scoped to the evaluated semantic boundary; optional implementation mechanisms remain hypotheses/options unless independently necessary.
- Requires `hold` / `unverified` blockers to be materially addressed before a revised candidate can be re-checked and before mutation resumes.
- Forbids re-running an unchanged blocked candidate merely to seek a different verdict.
- Keeps post-mutation verification/review independent from pre-mutation semantic authorization.

See `docs/releases/v30.34-beta.md` (archived).

## v30.33 beta

- Adds `semantic-checkpoint` as a separate read-only pre-mutation gate for material semantic decisions after discovery.
- Adds a narrow `code-orchestrator` trigger before edit-capable handoff when discovery is about to become required behavior, acceptance, scope, ownership, invariant, fix level, or product/domain policy.
- Keeps `session-evaluator` post-hoc while separating evidence status from finding classification and tightening `instruction-gap`, `instruction-violation`, and `execution-error` boundaries.
- Prevents checkpoint over-verification by allowing concrete child-session factual findings as evidence and by not requiring post-mutation success evidence before implementation.
- Keeps checkpoint verdicts available to the post-hoc evaluator only as gate-control evidence while preventing checkpoint/evaluator reasoning from becoming task authority.

See `docs/releases/v30.33-beta.md` (archived).

## v30.32 beta

- Distinguishes normative requirements in a user-adopted artifact from factual or implementation claims inside the same artifact.
- Treats adopted outcomes, acceptance criteria, and explicit constraints as established user intent while continuing to verify diagnoses and proposed mechanisms.
- Reframes release semantic checks around general invariants rather than incident-specific fixtures.

See `docs/releases/v30.32-beta.md` (archived).

## v30.31 beta

- Makes `session-evaluator` request `session.list` with an explicit large limit before reconstructing the completed workflow tree; `all: true` is used only to include archived sessions.
- Allows `session-evaluator` to read OpenCode-managed `~/.local/share/opencode/tool-output/*` spill files when large session results are materialized there.
- Requires descendant discovery through `parentID` before treating child-session evidence as unavailable.
- Reads each participating session with `session.messages` using `all: true` without incompatible `limit`/`last` selectors.
- Marks only still-missing branches `unverified` instead of substituting orchestrator summaries for unavailable child histories.

See `docs/releases/v30.31-beta.md` (archived).

## v30.30 beta

- Replaces the package-owned `session_trace` wrapper with OpenChamber-native `session.list` and `session.messages` evidence collection in `session-evaluator`.
- Keeps the evaluator focused on semantic decision boundaries and instruction compliance without requiring raw tool-call traces.
- Removes `tools/session_trace.js` from the package and adds installer cleanup for that obsolete package-owned tool on upgrade.
- Updates README runtime/install/validation documentation for the OpenChamber-native evaluation path.

See `docs/releases/v30.30-beta.md` (archived).

## v30.29 beta

- Adds a fresh semantic prompt audit of root `AGENTS.md` and every agent file to mandatory release validation.
- Rewords the root behavioral-contract check to establish the contract without requiring a separate summary artifact.
- Consolidates repeated fallback wording in `general` and removes a redundant implementation prohibition in `project-planner`.
- Removes an arbitrary `3–7` next-action quota from `auditor` and a non-accessibility sticky-save-layout reminder from `a11y-reviewer`.
- Replaces a near-verbatim `tester` copy of root shared-path regression coverage with a direct root §7.3 reference.
- Makes `session-evaluator` neutral about whether a violation exists while preserving its evidence/classification requirements.
- Consolidates the owned-PR final-candidate lifecycle in `code-orchestrator` so the detailed sequence has one canonical home.
- Cleans README/changelog release prose and places the changelog overview directly under the document title.

See `docs/releases/v30.29-beta.md` (archived).

## v30.28 beta

- Audits and rewrites `README.md` against the shipped runtime/package surface, including the correct 16-agent / 18-skill / diagnostic-tool topology.
- Adds official OpenAI, Anthropic, DeepSeek, and Z.ai/GLM prompt/evaluation methodology references and separates them from OpenCode runtime/API references.
- Removes duplicated README upstream links, trims release/documentation listings that duplicated `CHANGELOG.md`, and keeps the changelog overview text in one canonical location.
- Rechecks README claims about install surfaces, persistent planning, PR/review flow, skills, and `session-evaluator` against the actual archive.

See `docs/releases/v30.28-beta.md` (archived).

## v30.27 beta

- Adds experimental `session-evaluator` for post-hoc semantic compliance audits of completed `code-orchestrator` sessions and their child-agent calls.
- Adds read-only `session_trace` access to the parent/child session tree and projected message timelines so the evaluator uses the observable trace instead of an orchestrator-authored summary.
- Adds one temporary post-completion trigger; evaluator findings are diagnostic evidence only and cannot reopen, modify, or gate completed work.
- Classifies findings as instruction violation, ambiguity, gap, execution error, or justified decision, with `unverified` reserved for evidence limits; prompt changes are proposed only for confirmed reusable instruction weaknesses.
- Uses time-local instruction provenance for the audit: current instruction text is not applied retroactively when the historical governing rule cannot be established.
- Excludes `session-evaluator` diagnostic sessions from the audited workflow tree so retries do not contaminate the trace.

See `docs/releases/v30.27-beta.md` (archived).

## v30.26 beta

- Treats material decisions about framing, required behavior, scope, ownership, invariants, and fix level as claims subject to the existing root authority/evidence checks.
- Reuses the existing counterexample and hypothesis rules for those decisions instead of adding a second self-review loop.

See `docs/releases/v30.26-beta.md` (archived).

## v30.25 beta

- Renames the package planning agent from `plan` to `project-planner` to avoid collision with OpenCode's shipped `plan` agent and its restricted project-edit policy.
- Updates current routing/handoff references to `@project-planner` while keeping repository planning writes limited to the existing authorized plan-artifact paths.
- Adds installer migration cleanup that backs up and removes the obsolete package-owned `agents/plan.md` on upgrade before installing `project-planner.md`.

See `docs/releases/v30.25-beta.md` (archived).

## v30.24 beta

- Makes the root necessity test explicit: judge a technical consequence against the established outcome, not against a broader rule inferred during planning, implementation, testing, or review.
- Strengthens `code-orchestrator` handoff salience by naming material claims that are still only evidence or hypotheses and forbidding their promotion to acceptance during delegation.

See `docs/releases/v30.24-beta.md` (archived).

## v30.23 beta

- Simplifies root `AGENTS.md` and all 15 role prompts using the current OpenAI guidance for lean prompts, plain language, direct statements, and one canonical home per instruction.
- Rewrites the authority-provenance rule with shorter direct wording while keeping the distinction between authoritative requirements, evidence, and necessary technical consequences.
- Compacts `code-orchestrator`, `reviewer`, tester, implementation, audit, and UI role wording so role files focus on role-specific decisions instead of restating root policy.
- Splits dense PR/readiness and delegation instructions into shorter decision steps and removes redundant prompt scaffolding.

See `docs/releases/v30.23-beta.md` (archived).

## v30.22 beta

- Makes claim authority explicit: derived reasoning, review findings, inferred invariants, tests, and prior agent decisions remain evidence unless they trace to authoritative intent/rules or a necessary consequence of them.
- Allows necessary cross-layer implementation work without escalation when it is required to satisfy an established outcome and does not strengthen the required behavior or authority.
- Prevents implementation/review invariant expansion from becoming its own authority for wider downstream fixes.
- Binds right-level boundary expansion to the established outcome under root §2.2.1.

See `docs/releases/v30.22-beta.md` (archived).

## v30.21 beta

- Tightens root intent/follow-through wording and makes the framing counter-check explicitly internal so it does not become a user-facing option ritual.
- Renames root §7.2 to `Right-level implementation boundary` so feature work and bugfixes share the same solution-level discipline.
- Consolidates repeated gate, ambiguity, skill-authority, and delegation-fallback wording into their canonical root sections.
- Adds a public-writing rule that changelog entries list actual changes while preservation/regression evidence belongs in validation or release-audit material.
- Cleans historical changelog entries that only described unchanged behavior.
- Corrects the README installer-validation path label from `command/doc/skill` to `command/doc/snippet`.

See `docs/releases/v30.21-beta.md` (archived).

## v30.20 beta

- Compacts the `code-orchestrator` implementation-prohibition block to the role-specific invariant plus canonical root §2.5 instead of repeating the full alternate-editor/fallback policy.
- Compacts the reviewer finding-classification list without removing any category or changing verdict semantics.

See `docs/releases/v30.20-beta.md` (archived).

## v30.19 beta

- Removes three duplicate root reminders whose canonical behavior already exists in request normalization / Startup policy.
- Removes the repeated delegated `Leaf boundary` boilerplate from role files; all roles still load the root contract and root §5 remains canonical.
- Replaces four role-local mutation-mechanism restatements with concise references to canonical root §7.1.1.

See `docs/releases/v30.19-beta.md` (archived).

## v30.18 beta

- Treats the first plausible non-trivial framing/fix level as a hypothesis and requires a materially different counter-framing only when it could change the outcome.
- Separates leaf technical implementation freedom from workflow-owner authority over new product/domain semantics, identities, ownership/source-of-truth rules, and destructive boundaries.
- Extends right-level discipline from bug corrections to all non-trivial implementation and defines production-grade behavior operationally without turning it into speculative “enterprise” architecture.
- Makes unexpected selectors/identities/persistence/coordination/guards a signal to re-check framing before design expansion.
- Adds reviewer coverage for technically coherent but unauthorized semantic scope creep.
- README current-version/footer links are corrected and the OpenAI current-model prompting guide used during this policy review is documented as an external design reference.

See `docs/releases/v30.18-beta.md` (archived).

## v30.17 beta

- Aligns readiness authority with the root priority hierarchy: pack readiness/verification evidence conditions do not self-elevate above explicit user intent unless they instantiate a higher-priority runtime/role/project constraint.
- Adds semantic non-circular gate handling for evidence whose availability depends on crossing the same lifecycle boundary.
- Replaces the code-orchestrator fixed `remote CI/status -> Ready` sequence with dependency-driven readiness and updates `pr-readiness` to classify host status/evidence by actual availability and authority.

See `docs/releases/v30.17-beta.md` (archived).

## v30.16 beta

- Removes the retired-skill migration special case from both installers; installers no longer carry knowledge of previously removed skill directories.

See `docs/releases/v30.16-beta.md` (archived).

## v30.15 beta

- Removes the experimental external context-compaction integration from the runtime pack after unacceptable latency in real use.
- Removes its bundled skill, setup/reference document, root activation/trigger semantics, and historical beta release note rather than retaining dead optional policy.
- Adds exact legacy-skill migration cleanup so global/project installs over older betas back up and remove the retired package-owned skill directory without touching unrelated skills.

See `docs/releases/v30.15-beta.md` (archived).

## v30.14 beta

- Makes native edit/patch the explicit default for bounded semantic repository edits when available and safe.
- Narrows scripted mutation to genuinely programmatic/mechanical bounded transformations, cases native edit/patch cannot safely express within the intended target set, or runtimes where native edit/patch is unavailable.
- Explicitly rejects convenience rationales such as shorter syntax, line-number targeting, avoiding exact-match friction, or a small number of textual replacements.
- Reinforces the rule in the mutation-capable `build`, `debugger`, `ui-implementer`, and `devops` roles while keeping orchestration handoffs semantic rather than tool-prescriptive.

See `docs/releases/v30.14-beta.md` (archived).

## v30.13 beta

- Adds a generic repository-prerequisite gate to owned-PR Ready transitions.
- Treats the unresolved required decision/approval as the blocker rather than the open/closed/linked state of a discussion, issue, RFC, forum, mailing list, or similar external artifact.
- Grounds prerequisite applicability/resolution in authoritative repository policy, maintainer decisions, and current repository/review/status signals; PR metadata may not claim agreement absent authoritative support.

See `docs/releases/v30.13-beta.md` (archived).

## v30.11 beta

- Makes the orchestration goal/path split explicit: parent owns semantic outcome/envelope/stage ownership; the selected leaf owns execution-local path/root-cause discovery.
- Narrows `@explore` routing so unknown implementation details do not create an intermediate discovery stage when a bounded implementation/debugging leaf already owns the next action.
- Moves fix-boundary proof from pre-handoff orchestration into the assigned implementation/debugging role under root §7.2; orchestrator keeps acceptance and preserved-behavior ownership.

See `docs/releases/v30.11-beta.md` (archived).

## v30.10 beta

- Distinguishes workflow-level ambiguity from execution-local ambiguity at delegation boundaries.
- Clarifies that focused implementation can be delegated from a bounded semantic outcome without the orchestrator first discovering exact files/symbols/local mechanics.
- Removes several routing-sensitive undefined qualifiers (`already-understood`, `scope/design is clear`, `obvious`) while retaining semantic judgment for materiality, risk, stage economy, and escalation.

See `docs/releases/v30.10-beta.md` (archived).

## v30.9 beta

- Makes the project-local README install example version-agnostic instead of embedding a beta directory name that becomes stale on release rename.

See `docs/releases/v30.9-beta.md` (archived).

## v30.8 beta

- Clarifies the root provenance pointer: `git-provenance` owns the canonical detailed policy, while root §8 binds it to repository-state workflows.
- Replaces the approximate `~45 KB` validation note with a stable `<50 KiB` compact-root target.
- Normalizes `git-provenance` and `pr-readiness` extracted subsection headings from H4 to H2.

See `docs/releases/v30.8-beta.md` (archived).

## v30.7 beta

- Adds an explicit `Pack version: v30.7 beta` marker inside root `AGENTS.md` so installed rule files can be identified directly.
- Renumbers the remaining visual-evidence subsection from `§8.3` to `§8.1` after earlier subsection compaction.
- Moves the changelog summary directly under the changelog title and removes the stray extra blank line around the v30.4/v30.2 boundary.

See `docs/releases/v30.7-beta.md` (archived).

## v30.6 beta

- Removes the bundled server-incompatible GitHub binary-upload integration and all associated package references and runtime policy hooks.
- Removes the integration's skill directory and the dedicated historical beta note that documented it.
- Bundled skill inventory is now 18 skills: 13 specialist/advisory and 5 workflow/policy skills.
- Visual-evidence publication uses only an already-available authorized mechanism; otherwise it preserves local evidence and reports publication blocked.

See `docs/releases/v30.6-beta.md` (archived).

## v30.5 beta

- Completes §2.1.1 with the full bundled skill inventory, separating specialist/advisory routing from conditional workflow/policy skills.
- States that all roles inherit the root skill catalog and that triggered policy skills must actually be loaded for the applicable stage without widening authority.
- Restores explicit entry-routing vs delegation-routing defaults after v30.4 compaction and keeps `@code-orchestrator` / `@auditor` out of delegation targets.
- Makes current-upstream provenance and owned-PR provenance/readiness skill dependencies explicit.
- Repairs stale v30.4 role references to removed root subsections in `build` and `ui-orchestrator`.

See `docs/releases/v30.5-beta.md` (archived).

## v30.4 beta

- Compacts root `AGENTS.md` from 75,493 bytes to ~45 KB.
- Moves detailed Git provenance, PR readiness, verification cadence, resource lifecycle, and output formatting mechanics into bundled conditional policy skills.

See `docs/releases/v30.4-beta.md` (archived).

## v30.2 beta

Beta resource-lifecycle and visual-evidence release built on v30.1 beta.

- Adds one canonical workflow-created resource lifecycle: creation creates cleanup ownership, and final completion requires reconciliation to `cleaned`, `intentionally retained`, `cleanup blocked`, or `ownership transferred`.
- Tracks related resources independently so removing a worktree does not silently imply its local branch, remote ref, process, or hosted evidence resource is also reconciled.
- Allows ordinary cleanup of current-workflow-owned local disposable resources when safe, while remote/published/shared destructive cleanup remains subject to the applicable gate unless that teardown was already authorized.
- Separates visual-evidence publication from repository-hosting state; gist/temporary branch/ref hosting is not an implicit fallback.
- Requires post-publication attachment verification and resource reconciliation for local screenshots, temporary execution workspaces/processes, and any fallback hosting resources.

See `docs/releases/v30.2-beta.md` (archived).

## v30.1 beta

Beta semantic-policy alignment release built on v30.00.

- Splits routing into entry routing and delegation routing so top-level ownership is not confused with invokable subagent edges.
- Uses agent frontmatter `mode` as the canonical execution-topology source for the OpenCode-specific pack.
- Removes inferred similarity fallback: fallback must be explicitly declared, executable from the current context, and no broader than the current authority/workflow envelope.
- Separates hard/mandatory preconditions from user-authorizable gates and prevents evidence/state/tool availability from becoming implicit authorization.
- Clarifies primary-role reroute behavior in `build`, fallback failure behavior in `code-orchestrator` / `ui-orchestrator`, and delegated UI orchestration leaf-dispatch with the workflow-owning parent.
- Narrows `plan` write permissions to portable canonical planning paths; removes the developer-specific absolute plan path and broad `docs/**` write scope.

See `docs/releases/v30.1-beta.md` (archived).

## v30.00

Stable successor to v28.42 focused on a smaller, deterministic runtime surface.

- Removes duplicated root/role policy where ownership is deterministic; universal routing, gates, state identity, provenance, right-level correctness, and evidence rules remain resident.
- Ships only the runtime surfaces OpenCode actually consumes: `AGENTS.md`, `agents/`, and `skills/`. Package custom commands and snippets are removed; setup docs remain human-facing only.
- Consolidates repository-state/provenance and Draft → Candidate → Ready semantics; role-specific execution behavior stays in the owning agents.
- Maps historical command intents to resident natural-language semantic routing instead of slash-command aliases.
- Restores `agents/code-orchestrator.md` exactly from v28.42 after behavioral testing showed that further deduplication inside that role weakened routing behavior.
- Installers migrate cleanly by backing up/pruning only known package-owned legacy commands, snippets, and obsolete docs while preserving unrelated user/project files.

See `docs/releases/v30.00.md` (archived).

## v28.42

- Adds one canonical mutation-mechanism rule under the implementation policy.
- Bounded source changes prefer native file edit/patch capabilities when they safely express the intended mutation, while deterministic scripted/bulk transformations remain allowed when materially better suited or necessary.
- Broad textual replacement is explicitly not a substitute for semantic/structural understanding. Scripted or bulk mutation must constrain its target set before execution and inspect the resulting diff afterward.
- Tool choice cannot widen authorized scope or correctness obligations.
- README current-version/install-path/footer references are normalized to v28.42.

See `docs/releases/v28.42.md` (archived).

## v28.41

- Synchronizes the package-maintained `open-code-review` skill with current Alibaba OCR managed-review behavior.
- Managed review no longer spends a common-path tool call probing `ocr` availability/version before execution; installation handling is entered only after an actual command-not-found failure.
- `--max-tokens-budget` now documents the current per-LLM-round enforcement, no-new-group behavior after exhaustion, and bounded final round for submitting pending findings.
- `--max-tools` now documents the current template default of `100`, the `1`-`49` clamp to `50`, and that the resolved override only takes effect above the template default.
- The normal OCR skill metadata now identifies Alibaba plus the package-maintained integration rather than implying the extended skill text is verbatim upstream.

See `docs/releases/v28.41.md` (archived).

## v28.40

- `build` changes from `mode: primary` to `mode: all`, supporting both direct focused implementation and the documented orchestrator -> build route.
- `plan` changes from `mode: primary` to `mode: all`; `task: deny` makes delegated planning leaf-only.
- `ui-orchestrator` changes from `mode: primary` to `mode: all`. As primary it dispatches UI specialists; when delegated it may select and prepare leaf assignments but returns them to the workflow-owning parent for dispatch instead of creating grandchildren.
- Focused, already-understood UI implementation routes directly to `ui-implementer`; UI design/audit/redesign or coordinated multi-stage UI work continues through `ui-orchestrator`.
- Removes the impossible nested-dispatch description from `auditor`.

## v28.39

v28.39 cleans README release-history duplication.

- README now contains only the current bundle's release summary.
- `CHANGELOG.md` is the single README entry point for release history.
- The README documentation map lists only the current release note plus durable policy/reference docs.

See `docs/releases/v28.39.md` (archived).

## v28.38

v28.38 fixes contract-authority inheritance from referenced artifacts.

- Authority now attaches to individual claims, not automatically to the issue/PR/plan/comment/test/doc/task that contains them.
- A referenced artifact may establish scope and may contain normative requirements, but container, heading, repetition, confidence, or placement alone do not elevate a statement into the behavioral contract.
- Material acceptance claims must derive authority from current normalized user intent or project-local authoritative rules before implementation/planning/review treats them as requirements; an explicit current instruction may elevate a referenced artifact or selected parts.
- Claim authority and evidentiary support are separate: system evidence can support or refute a claim but cannot by itself make that claim a requirement.
- Issue/report-derived bugfixes treat unestablished claims as evidence/hypotheses instead of silently adopting proposed mechanisms or derived acceptance wording.
- Reviewer normalizes claim authority before applying semantic correspondence, preventing a self-confirming loop where an artifact's own proposed mechanism becomes both requirement and proof.

See `docs/releases/v28.38.md` (archived).

## v28.37

v28.37 generalizes the v28.36 premise-validation rule around semantic correspondence instead of enumerating classes of mechanisms or bugs.

- Correctness claims must state the semantic property/outcome first; implementation facts and mechanisms are evidence rather than the contract itself.
- A proxy counts as proof only when its correspondence to the claimed semantic property is established from actual system behavior.
- Review establishes the specific evidence-to-semantics inference being used and checks for ordinary valid behavior where the same technical evidence would not justify the claimed semantic conclusion; reverse inference is proved separately only when the change relies on it.
- Reviewer, planner, and orchestrator treat implementation details as hypotheses until that correspondence is established.
- Tester/verification policy now asks whether the observed test result actually justifies the production conclusion being claimed, instead of maintaining a taxonomy of special cases.

See `docs/releases/v28.37.md` (archived).

## v28.36

v28.36 hardens review and verification against self-confirming implementation assumptions.

- Adds one canonical contract-provenance/premise-validation rule instead of case-specific checks.
- Caller-proposed mechanisms, comments/docs introduced by the same change, new tests, and implementation descriptions are not independent proof of the premise they repeat; current production behavior is evidence, not automatically the desired contract.
- Material correctness guards/state transitions must have their semantic premises traced into production producers/owners/consumers, including unchanged adjacent code when needed.
- Representation-to-semantic mappings such as reference identity versus value equivalence must be established rather than assumed, and reviewers reason through an ordinary valid production transition that could falsify the premise.
- Changed-file coverage is explicitly separated from semantic-proof coverage.
- Tester verifies harness/fixture/mock fidelity for lifecycle/identity/order/ownership/timing-sensitive claims before promoting focused results to production evidence.
- Orchestrator and planner distinguish authoritative outcomes/invariants from implementation hypotheses when handing work between stages.

See `docs/releases/v28.36.md` (archived).

## v28.35

v28.35 makes OCR delegation the deterministic preflight for code-like reviewer runs when compatible OCR is installed, while managed `ocr review` becomes an independent second-model escalation.

- Reviewer binds the authoritative target/effective diff before delegate selection.
- `ocr delegate preview` + `ocr delegate rule` provide LLM-free selection/exclusions/ref metadata and grouped rules.
- Delegate output is reconciled against every authoritative `(path,status)` entry; exclusions cannot silently reduce coverage.
- Host `@reviewer` performs the complete review with its own model and reports explicit coverage.
- Managed OCR runs only when explicitly required or materially useful; quota/rate/provider failure preserves a complete host verdict unless managed OCR was mandatory.
- Bundled `open-code-review` is replaced by the supplied current CLI skill and `open-code-review-delegate` is added.

See `docs/releases/v28.35.md` (archived). The historical `docs/ocr_review_policy.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

## v28.34

v28.34 strengthens right-level fix selection.

- Fix selection now starts from the end-to-end acceptance condition for the requested outcome, not from the nearest editable component.
- Before implementation, the chosen ownership/fix boundary must be capable of guaranteeing that condition across materially relevant paths, states, callers, partitions/instances, and lifecycle transitions.
- Local or per-partition guarantees do not count as proof of a system-level invariant unless their composition/aggregate behavior is established.
- If the proposed boundary cannot guarantee the required outcome, the workflow moves the fix level outward or escalates before coding instead of accumulating local patches.
- Planner, orchestrator, debugger, build, and reviewer role guidance now applies the same canonical fix-boundary principle.

See `docs/releases/v28.34.md` (archived) for the detailed before/after explanation.

## v28.33

v28.33 adds base-drift handling to PR state identity.

- Final validation/review is bound to `Base SHA + Candidate HEAD`.
- Base is refreshed before final review, before PR publication, and before Ready.
- A moved base makes affected evidence stale by default; reuse requires proof that effective diff/integration context is unchanged.
- Reviewer/provenance output records the reviewed Base SHA.

See `docs/releases/v28.33.md` (archived). The historical `docs/pr_readiness.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

## v28.32

v28.32 extends current-upstream freshness into end-to-end repository state identity.

- Directly invoked roles own applicable freshness when no parent/orchestrator exists; delegated leaves still consume caller-supplied fresh target context instead of fetching redundantly.
- Authoritative target ref/SHA and intended mutation state survive nested delegation until explicitly changed.
- Static inspection, executable workspace, mutation baseline, verification/review, and publication are distinct state-identity steps that must not be silently mixed.
- Issue/report-derived work resolves its applicability target from issue/project metadata instead of assuming local checkout; publishing a current-state issue rechecks moved target evidence before publication.
- Tester validates executing state for target-bound evidence; mismatched-worktree results are workspace-only/target-unverified.
- Debugger/build/UI implementation refuse to edit a stale or unrelated worktree when the assignment is bound to a current authoritative target.
- `/ui-options` now follows the existing materially-distinct-options policy instead of forcing 2–3 alternatives.

See `docs/releases/v28.32.md` (archived). The historical `docs/git_branch_provenance_policy.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

## v28.31

v28.31 fixes stale-code analysis when a workflow must decide whether an issue/behavior still exists in the current upstream/default/base state.

- Current-upstream claims now require a freshly resolved authoritative remote ref + SHA before code is treated as current.
- The primary/orchestrator performs the freshness fetch once and passes the target ref/SHA to specialists; leaf roles do not independently fetch by default.
- A stale local checkout may be used only as comparison/history evidence when it differs from the authoritative target; it cannot silently stand in for current upstream.
- Read-only `git fetch` is explicitly separated from `pull`/rebase/reset/checkout, so freshness checks do not mutate the working tree.
- `/bug-issue` and issue-originated bugfix diagnosis now resolve the report target first and verify current-upstream applicability against the fetched authoritative ref; explicitly local-workspace reports remain local.

See `docs/releases/v28.31.md` (archived). The historical `docs/git_branch_provenance_policy.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

## v28.30

v28.30 adds four targeted workflow-hygiene rules.

- A failed root-cause fix that leaves the same material failure now resets hypothesis confidence before another similar mutation is authorized.
- Orchestrators resolve safe non-gated uncertainty from evidence and batch compatible blocking user decisions.
- User-facing output now leads by state: result first when complete, blocker/action first when blocked, first executable step first for user-run procedures.
- Numbered steps are reserved for ordered human procedures rather than findings, options, status, or internal workflow diagrams.
- README Candidate/verification diagrams now explicitly show the optional/required Candidate-level `@tester` checkpoint before the final reviewer.

See `docs/releases/v28.30.md` (archived) for the detailed before/after explanation.

## v28.29

v28.29 corrects verification cadence across implementation, testing, review, UI, and audit roles.

- Implementation-capable roles now return **implementation-local evidence** as the default post-edit check layer.
- `@tester` is no longer a mechanical stage after every fix/work package/commit; it is an independent checkpoint used when the request, risk, integration boundary, evidence quality, or project policy justifies it.
- One tester invocation now covers the complete already-applicable verification boundary instead of splitting predictable focused/preserved/suite checks across repeated calls; an individual FAIL does not end the batch when independent remaining checks can still add useful evidence.
- Complexity work packages are mutation/scope boundaries first; independent tester checkpoints are placed at meaningful integration boundaries rather than after every package.
- UI orchestration no longer invokes tester merely because runnable frontend checks exist; `ui-implementer` returns local evidence first.
- Reviewer cadence is now explicit: final owned-PR Candidate review remains required; ordinary review runs at stable high-risk boundaries, consumes fresh implementation/tester/CI evidence, and uses only narrow spot-checks instead of repeating broad verification.
- Auditor batches related executable verification questions instead of invoking tester/reviewer once per finding, and its own checks are limited to narrow finding-specific spot-checks rather than duplicating broad tester/CI coverage.
- Added a general stage-economy rule: reuse fresh evidence and re-invoke specialists only when the target/evidence boundary materially changed, prior coverage was incomplete/blocked, or independence itself is required.
- Separate `@explore` is no longer triggered just because the exact bug/UI file is unknown; debugger/implementer may trace within a bounded assignment, while explore is reserved for materially broad/ambiguous mapping. Debugger also reuses fresh caller/tester/CI reproduction evidence instead of mechanically rerunning the same pre-fix failure.
- Accessibility review is also stage-economized: a UI-file/cosmetic edit alone does not trigger `@a11y-reviewer`; use it for materially accessibility-sensitive semantic/interaction changes or explicit policy. When both tester and a11y apply after implementation, functional/integration verification runs first so avoidable fixes do not immediately stale a11y evidence. An explicitly needed pre-implementation a11y consultation is advisory and is not mislabeled as a final implemented-state verdict.
- UI options/plan/audit modes are no longer collapsed into a forced “2–3 options” output; each mode now returns its actual deliverable and options are created only when materially distinct choices exist.
- UI orchestration now states the final reviewer handoff explicitly when root review cadence applies; owned-PR UI Candidates cannot skip the whole-change pre-push review.

See `docs/releases/v28.29.md` (archived). The historical `docs/verification_strategy.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

## v28.28

v28.28 makes long-running multi-agent and PR workflows more deterministic.

- Orchestrators now explicitly own scope, stage order, escalation, findings, and publication; specialists own execution details only inside delegated boundaries.
- Related state/lifecycle/protocol/concurrency/persistence findings escalate to one shared invariant model instead of repeated one-comment/one-patch loops.
- Reviewer findings are grouped by underlying invariant and final owned-PR readiness requires a whole-change base-to-local-Candidate-HEAD verdict.
- Owned PRs use a Draft → local Candidate HEAD → review → push exact reviewed SHA → remote checks → Ready lifecycle. Intermediate Draft repair pushes still do not require final review after every batch, and the final full review is not repeated merely because the unchanged reviewed SHA was pushed.
- Failing/blocked required verification may coexist with authorized Draft repair work but still blocks Ready/merge/release/completion.
- Nested orchestrators may choose child stages only when that authority was explicitly delegated.
- PR reports include the canonical PR URL; owned-PR readiness reports also include state and Candidate HEAD.
- OCR remains reviewer-selected unless user/project policy explicitly requires it.

See `docs/releases/v28.28.md` (archived) for the detailed before/after explanation.

## v28.27

v28.27 consolidated the model-agnostic behavioral contract around semantic routing, hard role boundaries, evidence freshness, correct Git base semantics, safer test/review behavior, and command/docs consistency.

Earlier release history is not reconstructed here; use the repository/package history where available.
