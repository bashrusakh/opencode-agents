# Changelog

This changelog summarizes user-visible workflow changes. Detailed rationale and before/after behavior for major releases lives under `docs/releases/`.

## v30.00-beta11

Stable-orchestrator restoration over beta10.

- Replaces the beta9/beta10-deduplicated `agents/code-orchestrator.md` with the exact v28.42 file, byte-for-byte.
- Restores the complete proven role-local semantic model rather than another partial routing patch: target identity, discovery cadence, leaf routing, stage economy application, review/test cadence, workflow behavior, evidence freshness, PR lifecycle coordination, and final reporting all return together.
- Keeps every other beta10 runtime/package file unchanged except release/version documentation.
- Adds issue #3512-style semantic analysis as a behavioral regression scenario: explicit repository tracing is `@explore` work even when candidate files are already supplied; orchestrator reconciliation does not absorb specialist investigation.

See [`docs/releases/v30.00-beta11.md`](docs/releases/v30.00-beta11.md).

## v30.00-beta10

Role-local routing regression fix over beta9.

- Restores the explicit `code-orchestrator` leaf-role routing map that stable v28.42 carried locally in the orchestrator prompt.
- Retains the v28.29 discovery cadence: bounded implementation roles may locate nearby code themselves, while separate `@explore` is reserved for materially broad/ambiguous mapping or an explicit discovery/architecture-tracing deliverable.
- Fixes the beta9 behavioral regression where `code-orchestrator` could interpret its evidence-reconciliation responsibility as permission to perform specialist repository tracing itself.
- No other runtime behavior, agent frontmatter/modes/permissions, skills, installers, provenance/Ready semantics, tester/reviewer cadence, commands, or snippets change from beta9.

See [`docs/releases/v30.00-beta10.md`](docs/releases/v30.00-beta10.md).

## v30.00-beta9

Root/role semantic-deduplication and provenance consolidation over beta8.

- Consolidates duplicated pre-edit/publication Git state logic into one root repository-state/provenance contract with separate mutation and publication checkpoints.
- Keeps the owned-PR Draft → Candidate → Ready lifecycle distinct while referencing canonical provenance, verification, fix-placement, and regression contracts instead of restating them.
- Compresses persistent-planning and right-level-fix guidance while preserving plan activation, canonical durable state, authorization, and fix-boundary semantics.
- Removes repeated root semantics from `plan`, `build`, `debugger`, `code-orchestrator`, `reviewer`, `general`, `auditor`, and UI roles; execution-specific behavior remains resident in each owner.
- Moves current-repository freshness mechanics out of `Source of truth` and stray implementation/provenance rules out of Startup into their canonical §§7-8 owners.
- Corrects root OCR skill routing so deterministic delegate preflight and optional/required managed second-model review are distinct.
- Re-runs full ownership/reverse-obligation/activation/semantic-duplication audits across root and all agents; agent frontmatter/modes/permissions, skill source content, installers, and runtime surfaces are unchanged.
- Removes three accidental vendored UUPM `__pycache__/*.pyc` files as packaging-only debris.

See [`docs/releases/v30.00-beta9.md`](docs/releases/v30.00-beta9.md).

## v30.00-beta8

Dead-runtime-surface cleanup over beta7.

- Removes the legacy `snippet/` directory entirely; current OpenCode does not auto-discover it and no resident package contract consumed it.
- Moves the only useful snippet-only human setup detail (default shadcn registry needs no extra `registries` entry) into `docs/ui_mcp_setup.md`; all other snippet semantics were already resident elsewhere.
- Adds the package invariant that every installed runtime file must have a known OpenCode discovery/activation mechanism or deterministic resident consumer; otherwise it is an architecture error and should not ship.
- Updates both installers to back up/prune the seven exact historical package-owned snippet filenames while preserving unrelated files and removing the legacy snippet directory only when empty.
- Leaves `AGENTS.md`, all 15 agents, all 13 skills, semantic routing, gates, verification, provenance/Ready, and review behavior unchanged from beta7.

See [`docs/releases/v30.00-beta8.md`](docs/releases/v30.00-beta8.md).

## v30.00-beta7

Zero-command runtime cleanup over beta6.

- Removes the final `/ui-mcp-setup` and `/ui-uupm-setup` custom commands; the package now ships zero slash commands.
- Moves those procedures into `docs/ui_mcp_setup.md` and `docs/uupm_setup.md` as human-facing setup instructions that are not installed into OpenCode runtime.
- Keeps semantic routing as the only package workflow entry layer; setup documentation is explicitly outside coding/runtime correctness.
- Updates installers to back up/prune all 21 historical package-owned command filenames while preserving unrelated user/project commands.
- Removes the stale `role or command` wording from root model policy; no gate, routing intent, role contract, skill, verification, provenance, or Ready semantics otherwise change from beta6.

See [`docs/releases/v30.00-beta7.md`](docs/releases/v30.00-beta7.md).

## v30.00-beta6

Semantic command-layer cleanup over beta5.

- Removes 19 slash-command aliases that duplicated intents already handled by root semantic routing and owning agent contracts.
- Keeps only `/ui-mcp-setup` and `/ui-uupm-setup`, because they provide distinct setup procedures rather than alternate routing prompts; both procedures are now self-contained in the command files.
- Removes the two former setup docs, leaving `docs/` as release history only and eliminating all runtime doc dependencies.
- Adds explicit root routing for accessibility-only review, PR/branch provenance-only inspection, and authorized persistent coding-plan execution/resumption after reverse-auditing removed command intents.
- Updates installers to back up/prune exact obsolete package-owned commands/docs so upgrades do not leave deleted semantics active on disk.
- Does not change protected gates, authority, state identity, implementation/verification, provenance/Ready, agent role boundaries, or skills.

See [`docs/releases/v30.00-beta6.md`](docs/releases/v30.00-beta6.md).

## v30.00-beta5

Policy/document lifecycle cleanup over beta4.

- Removes obsolete/reference-only docs whose runtime semantics are already resident in `AGENTS.md` or owning role prompts and therefore had no justified deterministic consumer.
- Moves the bundled language/framework skill-routing mapping into resident root skill guidance, then removes `docs/language_spec.md`.
- Keeps only the UI MCP and UUPM procedural setup guides outside release history; their explicit setup commands inject guide content deterministically using OpenCode command shell-output expansion with project-local precedence and global fallback.
- Adds a package invariant: every non-release doc must have a concrete deterministic consumer/trigger; otherwise the doc is an architecture error or should not exist.
- Does not change beta4 routing/escalation fixes or protected stable gates, authority, state identity, implementation, verification, provenance, or Ready semantics.

See [`docs/releases/v30.00-beta5.md`](docs/releases/v30.00-beta5.md).

## v30.00-beta4

Correction and policy-ownership audit over beta3.

- Restores generic multi-step coding -> `@code-orchestrator` routing in root because role selection must be known before that role is active.
- Restores missing complexity-escalation signals inside `@code-orchestrator`: cross-layer expansion from an incomplete model, reviewer-detected invariant/model gaps, and the rule that file/diff size alone is not escalation evidence.
- Makes UI source/UUPM behavior self-contained in UI role prompts; removes model-mediated mandatory reads of `ui_component_policy.md`.
- Reclassifies provenance/OCR/output/planning/readiness/UI/verification docs as maintainer ownership references rather than runtime policies; removes their runtime dependencies from agents/commands/snippets.
- Leaves gates, claim authority, state identity, implementation rules, verification, PR provenance, and Ready lifecycle unchanged from stable except the two beta3 stale cross-reference repairs.

See [`docs/releases/v30.00-beta4.md`](docs/releases/v30.00-beta4.md).

## v30.00-beta3

Experimental root semantic deduplication rebuilt directly from stable v28.42.

- Removes duplicated OCR workflow mechanics from root; `agents/reviewer.md` remains the complete mandatory reviewer/OCR runtime contract.
- Replaces detailed root role pipelines (UI, coding/bugfix, tests/docs, PR follow-up, issue, audit, DevOps, release) with a compact role-ownership boundary.
- Relocates only root-unique residue needed by the owning roles: UI-policy locator/quick-redesign semantics, tests/docs-only implementation rules, bug-derived issue drafting details, and release-source handling. Agent frontmatter/modes/permissions and all other role contracts remain unchanged.
- Does not change `commands/*.md`, skills, approval gates, role/capability boundaries, claim authority/semantic correspondence, right-level/mutation/regression core, verification cadence, or PR provenance/Draft/Candidate/Ready semantics.
- Repairs only two root cross-references that pointed to removed workflow sections.

See [`docs/releases/v30.00-beta3.md`](docs/releases/v30.00-beta3.md).

## v28.42

- Adds one canonical mutation-mechanism rule under the implementation policy.
- Bounded source changes prefer native file edit/patch capabilities when they safely express the intended mutation, while deterministic scripted/bulk transformations remain allowed when materially better suited or necessary.
- Broad textual replacement is explicitly not a substitute for semantic/structural understanding. Scripted or bulk mutation must constrain its target set before execution and inspect the resulting diff afterward.
- Tool choice cannot widen authorized scope or correctness obligations. No tool blacklist, mandatory edit pipeline, role routing change, or permission change is introduced.
- README current-version/install-path/footer references are normalized to v28.42.

See [`docs/releases/v28.42.md`](docs/releases/v28.42.md).

## v28.41

- Synchronizes the package-maintained `open-code-review` skill with current Alibaba OCR managed-review behavior while preserving the existing host-review/delegate architecture.
- Managed review no longer spends a common-path tool call probing `ocr` availability/version before execution; installation handling is entered only after an actual command-not-found failure.
- `--max-tokens-budget` now documents the current per-LLM-round enforcement, no-new-group behavior after exhaustion, and bounded final round for submitting pending findings.
- `--max-tools` now documents the current template default of `100`, the `1`-`49` clamp to `50`, and that the resolved override only takes effect above the template default.
- The normal OCR skill metadata now identifies Alibaba plus the package-maintained integration rather than implying the extended skill text is verbatim upstream.
- Delegate capability probing, authoritative changed-set reconciliation, review-only mutation boundaries, and managed-OCR escalation policy are unchanged.

See [`docs/releases/v28.41.md`](docs/releases/v28.41.md).

## v28.40

- `build` changes from `mode: primary` to `mode: all`, preserving direct focused implementation while making the documented orchestrator -> build route runtime-valid.
- `plan` changes from `mode: primary` to `mode: all`; its existing `task: deny` keeps delegated planning leaf-only.
- `ui-orchestrator` changes from `mode: primary` to `mode: all`. As primary it dispatches UI specialists; when delegated it may select and prepare leaf assignments but returns them to the workflow-owning parent for dispatch instead of creating grandchildren.
- Focused, already-understood UI implementation routes directly to `ui-implementer`; UI design/audit/redesign or coordinated multi-stage UI work continues through `ui-orchestrator`.
- `debugger` remains a specialized `mode: subagent`, `task: deny` root-cause/fix leaf; it is not a generic implementation substitute.
- The packaged `auditor` remains primary-only and no longer describes an impossible nested-dispatch mode.
- No `subagent_depth` increase or permission broadening is introduced.

## v28.39

v28.39 cleans README release-history duplication; agent behavior is unchanged from v28.38.

- README now contains only the current bundle's release summary.
- `CHANGELOG.md` is the single README entry point for release history.
- The README documentation map lists only the current release note plus durable policy/reference docs.
- Historical release notes remain available under `docs/releases/` but are no longer repeated in the README map.

See [`docs/releases/v28.39.md`](docs/releases/v28.39.md).

## v28.38

v28.38 fixes contract-authority inheritance from referenced artifacts.

- Authority now attaches to individual claims, not automatically to the issue/PR/plan/comment/test/doc/task that contains them.
- A referenced artifact may establish scope and may contain normative requirements, but container, heading, repetition, confidence, or placement alone do not elevate a statement into the behavioral contract.
- Material acceptance claims must derive authority from current normalized user intent or project-local authoritative rules before implementation/planning/review treats them as requirements; an explicit current instruction may elevate a referenced artifact or selected parts.
- Claim authority and evidentiary support are separate: system evidence can support or refute a claim but cannot by itself make that claim a requirement.
- Issue/report-derived bugfixes explicitly keep unestablished claims as evidence/hypotheses instead of silently adopting proposed mechanisms or derived acceptance wording.
- Reviewer normalizes claim authority before applying semantic correspondence, preventing a self-confirming loop where an artifact's own proposed mechanism becomes both requirement and proof.

See [`docs/releases/v28.38.md`](docs/releases/v28.38.md).

## v28.37

v28.37 generalizes the v28.36 premise-validation rule around semantic correspondence instead of enumerating classes of mechanisms or bugs.

- Correctness claims must state the semantic property/outcome first; implementation facts and mechanisms are evidence rather than the contract itself.
- A proxy counts as proof only when its correspondence to the claimed semantic property is established from actual system behavior.
- Review establishes the specific evidence-to-semantics inference being used and checks for ordinary valid behavior where the same technical evidence would not justify the claimed semantic conclusion; reverse inference is proved separately only when the change relies on it.
- Reviewer, planner, and orchestrator keep implementation details as hypotheses until that correspondence is established.
- Tester/verification policy now asks whether the observed test result actually justifies the production conclusion being claimed, instead of maintaining a taxonomy of special cases.
- Existing v28.35 OCR delegation, v28.34 fix-boundary, and v28.31-v28.33 freshness/state/base-drift rules are unchanged.

See [`docs/releases/v28.37.md`](docs/releases/v28.37.md).

## v28.36

v28.36 hardens review and verification against self-confirming implementation assumptions.

- Adds one canonical contract-provenance/premise-validation rule instead of case-specific checks.
- Caller-proposed mechanisms, comments/docs introduced by the same change, new tests, and implementation descriptions are not independent proof of the premise they repeat; current production behavior is evidence, not automatically the desired contract.
- Material correctness guards/state transitions must have their semantic premises traced into production producers/owners/consumers, including unchanged adjacent code when needed.
- Representation-to-semantic mappings such as reference identity versus value equivalence must be established rather than assumed, and reviewers reason through an ordinary valid production transition that could falsify the premise.
- Changed-file coverage is explicitly separated from semantic-proof coverage.
- Tester verifies harness/fixture/mock fidelity for lifecycle/identity/order/ownership/timing-sensitive claims before promoting focused results to production evidence.
- Orchestrator and planner keep authoritative outcomes/invariants distinct from implementation hypotheses when handing work between stages.

See [`docs/releases/v28.36.md`](docs/releases/v28.36.md).

## v28.35

v28.35 makes OCR delegation the deterministic preflight for code-like reviewer runs when compatible OCR is installed, while managed `ocr review` becomes an independent second-model escalation.

- Reviewer binds the authoritative target/effective diff before delegate selection.
- `ocr delegate preview` + `ocr delegate rule` provide LLM-free selection/exclusions/ref metadata and grouped rules.
- Delegate output is reconciled against every authoritative `(path,status)` entry; exclusions cannot silently reduce coverage.
- Host `@reviewer` performs the complete review with its own model and reports explicit coverage.
- Managed OCR runs only when explicitly required or materially useful; quota/rate/provider failure preserves a complete host verdict unless managed OCR was mandatory.
- Bundled `open-code-review` is replaced by the supplied current CLI skill and `open-code-review-delegate` is added.

See [`docs/releases/v28.35.md`](docs/releases/v28.35.md). The historical `docs/ocr_review_policy.md` companion was removed from the current bundle in v30.00-beta5 after its runtime contract became resident.

## v28.34

v28.34 keeps the v28.33 workflow and strengthens right-level fix selection without adding a new stage or case-specific exception.

- Fix selection now starts from the end-to-end acceptance condition for the requested outcome, not from the nearest editable component.
- Before implementation, the chosen ownership/fix boundary must be capable of guaranteeing that condition across materially relevant paths, states, callers, partitions/instances, and lifecycle transitions.
- Local or per-partition guarantees do not count as proof of a system-level invariant unless their composition/aggregate behavior is established.
- If the proposed boundary cannot guarantee the required outcome, the workflow moves the fix level outward or escalates before coding instead of accumulating local patches.
- Planner, orchestrator, debugger, build, and reviewer role guidance now applies the same canonical fix-boundary principle.
- v28.31-v28.33 current-upstream freshness, repository state identity, and PR base-drift handling are retained unchanged.

See [`docs/releases/v28.34.md`](docs/releases/v28.34.md) for the detailed before/after explanation.

## v28.33

v28.33 adds base-drift handling to PR state identity.

- Final validation/review is bound to `Base SHA + Candidate HEAD`.
- Base is refreshed before final review, before PR publication, and before Ready.
- A moved base makes affected evidence stale by default; reuse requires proof that effective diff/integration context is unchanged.
- Reviewer/provenance output records the reviewed Base SHA.

See [`docs/releases/v28.33.md`](docs/releases/v28.33.md). The historical `docs/pr_readiness.md` companion was removed from the current bundle in v30.00-beta5 after its runtime contract became resident.

## v28.32

v28.32 extends current-upstream freshness into end-to-end repository state identity.

- Directly invoked roles own applicable freshness when no parent/orchestrator exists; delegated leaves still consume caller-supplied fresh target context instead of fetching redundantly.
- Authoritative target ref/SHA and intended mutation state survive nested delegation until explicitly changed.
- Static inspection, executable workspace, mutation baseline, verification/review, and publication are distinct state-identity steps that must not be silently mixed.
- Issue/report-derived work resolves its applicability target from issue/project metadata instead of assuming local checkout; publishing a current-state issue rechecks moved target evidence before publication.
- Tester validates executing state for target-bound evidence; mismatched-worktree results are workspace-only/target-unverified.
- Debugger/build/UI implementation refuse to edit a stale or unrelated worktree when the assignment is bound to a current authoritative target.
- `/ui-options` now follows the existing materially-distinct-options policy instead of forcing 2–3 alternatives.

See [`docs/releases/v28.32.md`](docs/releases/v28.32.md). The historical `docs/git_branch_provenance_policy.md` companion was removed from the current bundle in v30.00-beta5 after its runtime contract became resident.

## v28.31

v28.31 fixes stale-code analysis when a workflow must decide whether an issue/behavior still exists in the current upstream/default/base state.

- Current-upstream claims now require a freshly resolved authoritative remote ref + SHA before code is treated as current.
- The primary/orchestrator performs the freshness fetch once and passes the target ref/SHA to specialists; leaf roles do not independently fetch by default.
- A stale local checkout may be used only as comparison/history evidence when it differs from the authoritative target; it cannot silently stand in for current upstream.
- Read-only `git fetch` is explicitly separated from `pull`/rebase/reset/checkout, so freshness checks do not mutate the working tree.
- `/bug-issue` and issue-originated bugfix diagnosis now resolve the report target first and verify current-upstream applicability against the fetched authoritative ref; explicitly local-workspace reports remain local.

See [`docs/releases/v28.31.md`](docs/releases/v28.31.md). The historical `docs/git_branch_provenance_policy.md` companion was removed from the current bundle in v30.00-beta5 after its runtime contract became resident.

## v28.30

v28.30 keeps the v28.29 role/verification cadence and adds four targeted workflow-hygiene rules without adding a new skill or mandatory stage.

- A failed root-cause fix that leaves the same material failure now resets hypothesis confidence before another similar mutation is authorized.
- Orchestrators resolve safe non-gated uncertainty from evidence and batch compatible blocking user decisions; existing approval gates are unchanged.
- User-facing output now leads by state: result first when complete, blocker/action first when blocked, first executable step first for user-run procedures.
- Numbered steps are reserved for ordered human procedures rather than findings, options, status, or internal workflow diagrams.
- README Candidate/verification diagrams now explicitly show the optional/required Candidate-level `@tester` checkpoint before the final reviewer.

See [`docs/releases/v28.30.md`](docs/releases/v28.30.md) for the detailed before/after explanation.

## v28.29

v28.29 keeps the v28.28 orchestration/PR lifecycle and corrects verification cadence across implementation, testing, review, UI, and audit roles.

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
- The v28.28 review-before-push Candidate HEAD lifecycle remains unchanged.

See [`docs/releases/v28.29.md`](docs/releases/v28.29.md). The historical `docs/verification_strategy.md` companion was removed from the current bundle in v30.00-beta5 after its runtime contract became resident.

## v28.28

v28.28 keeps the v28.27 routing/role model and makes long-running multi-agent and PR workflows more deterministic.

- Orchestrators now explicitly own scope, stage order, escalation, findings, and publication; specialists own execution details only inside delegated boundaries.
- Related state/lifecycle/protocol/concurrency/persistence findings escalate to one shared invariant model instead of repeated one-comment/one-patch loops.
- Reviewer findings are grouped by underlying invariant and final owned-PR readiness requires a whole-change base-to-local-Candidate-HEAD verdict.
- Owned PRs use a Draft → local Candidate HEAD → review → push exact reviewed SHA → remote checks → Ready lifecycle. Intermediate Draft repair pushes still do not require final review after every batch, and the final full review is not repeated merely because the unchanged reviewed SHA was pushed.
- Failing/blocked required verification may coexist with authorized Draft repair work but still blocks Ready/merge/release/completion.
- Nested orchestrators may choose child stages only when that authority was explicitly delegated.
- PR reports include the canonical PR URL; owned-PR readiness reports also include state and Candidate HEAD.
- OCR remains reviewer-selected unless user/project policy explicitly requires it.
- Agent modes/permissions and bundled UUPM content were not broadened/changed by this policy release.

See [`docs/releases/v28.28.md`](docs/releases/v28.28.md) for the detailed before/after explanation.

## v28.27

v28.27 consolidated the model-agnostic behavioral contract around semantic routing, hard role boundaries, evidence freshness, correct Git base semantics, safer test/review behavior, and command/docs consistency.

Earlier release history is not reconstructed here; use the repository/package history where available.
