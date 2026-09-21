# Changelog

This changelog summarizes user-visible workflow changes. Detailed notes for retained releases live under `docs/releases/`.

## v30.8 beta

- Clarifies the root provenance pointer: `git-provenance` owns the canonical detailed policy, while root §8 binds it to repository-state workflows.
- Replaces the approximate `~45 KB` validation note with a stable `<50 KiB` compact-root target.
- Normalizes `git-provenance` and `pr-readiness` extracted subsection headings from H4 to H2.
- No runtime behavior, routing, permissions, policy semantics, cleanup behavior, skill inventory, or installer behavior changes.

See [`docs/releases/v30.8-beta.md`](docs/releases/v30.8-beta.md).

## v30.7 beta

- Adds an explicit `Pack version: v30.7 beta` marker inside root `AGENTS.md` so installed rule files can be identified directly.
- Renumbers the remaining visual-evidence subsection from `§8.3` to `§8.1` after earlier subsection compaction.
- Moves the changelog summary directly under the changelog title and removes the stray extra blank line around the v30.4/v30.2 boundary.
- No agent behavior, routing, permissions, policy semantics, skill inventory, or installer behavior changes.

See [`docs/releases/v30.7-beta.md`](docs/releases/v30.7-beta.md).

## v30.6 beta

- Removes the bundled server-incompatible GitHub binary-upload integration and all associated package references and runtime policy hooks.
- Removes the integration's skill directory and the dedicated historical beta note that documented it.
- Bundled skill inventory is now 18 skills: 13 specialist/advisory and 5 workflow/policy skills.
- Keeps visual-evidence publication transport-agnostic: use only an already-available authorized mechanism; otherwise preserve local evidence and report publication blocked.
- Keeps resource cleanup, gated remote deletion, v30.5 policy linkage, routing topology, and role permissions unchanged.

See [`docs/releases/v30.6-beta.md`](docs/releases/v30.6-beta.md).

## v30.5 beta

- Completes §2.1.1 with the full bundled skill inventory, separating specialist/advisory routing from conditional workflow/policy skills.
- States that all roles inherit the root skill catalog and that triggered policy skills must actually be loaded for the applicable stage without widening authority.
- Restores explicit entry-routing vs delegation-routing defaults after v30.4 compaction and keeps `@code-orchestrator` / `@auditor` out of delegation targets.
- Makes current-upstream provenance and owned-PR provenance/readiness skill dependencies explicit.
- Repairs stale v30.4 role references to removed root subsections in `build` and `ui-orchestrator`.
- Keeps agent set, plan permissions, fallback semantics, cleanup policy, and installer behavior unchanged.

See [`docs/releases/v30.5-beta.md`](docs/releases/v30.5-beta.md).

## v30.4 beta

- Compacts root `AGENTS.md` from 75,493 bytes to ~45 KB while preserving resident authority/gate/routing invariants.
- Moves detailed Git provenance, PR readiness, verification cadence, resource lifecycle, and output formatting mechanics into bundled conditional policy skills.
- Keeps role files and execution topology unchanged from the preceding beta.

See [`docs/releases/v30.4-beta.md`](docs/releases/v30.4-beta.md).

## v30.2 beta

Beta resource-lifecycle and visual-evidence release built on v30.1 beta.

- Adds one canonical workflow-created resource lifecycle: creation creates cleanup ownership, and final completion requires reconciliation to `cleaned`, `intentionally retained`, `cleanup blocked`, or `ownership transferred`.
- Tracks related resources independently so removing a worktree does not silently imply its local branch, remote ref, process, or hosted evidence resource is also reconciled.
- Allows ordinary cleanup of current-workflow-owned local disposable resources when safe, while remote/published/shared destructive cleanup remains subject to the applicable gate unless that teardown was already authorized.
- Keeps visual-evidence publication separate from repository-hosting state; gist/temporary branch/ref hosting is not an implicit fallback.
- Requires post-publication attachment verification and resource reconciliation for local screenshots, temporary execution workspaces/processes, and any fallback hosting resources.
- Keeps v30.1 routing, execution-topology, fallback, authorization, and plan-path semantics unchanged.

See [`docs/releases/v30.2-beta.md`](docs/releases/v30.2-beta.md).

## v30.1 beta

Beta semantic-policy alignment release built on v30.00.

- Splits routing into entry routing and delegation routing so top-level ownership is not confused with invokable subagent edges.
- Uses agent frontmatter `mode` as the canonical execution-topology source for the OpenCode-specific pack.
- Removes inferred similarity fallback: fallback must be explicitly declared, executable from the current context, and no broader than the current authority/workflow envelope.
- Separates hard/mandatory preconditions from user-authorizable gates and prevents evidence/state/tool availability from becoming implicit authorization.
- Clarifies primary-role reroute behavior in `build`, fallback failure behavior in `code-orchestrator` / `ui-orchestrator`, and keeps delegated UI orchestration leaf-dispatch with the workflow-owning parent.
- Narrows `plan` write permissions to portable canonical planning paths; removes the developer-specific absolute plan path and broad `docs/**` write scope.

See [`docs/releases/v30.1-beta.md`](docs/releases/v30.1-beta.md).

## v30.00

Stable successor to v28.42 focused on a smaller, deterministic runtime surface without changing the package's core correctness model.

- Removes duplicated root/role policy where ownership is deterministic; universal routing, gates, state identity, provenance, right-level correctness, and evidence rules remain resident.
- Ships only the runtime surfaces OpenCode actually consumes: `AGENTS.md`, `agents/`, and `skills/`. Package custom commands and snippets are removed; setup docs remain human-facing only.
- Consolidates repository-state/provenance and Draft → Candidate → Ready semantics while keeping role-specific execution behavior in the owning agents.
- Keeps natural-language semantic routing as the package control surface and preserves historical command intents through resident routing rather than slash-command aliases.
- Restores `agents/code-orchestrator.md` exactly from v28.42 after behavioral testing showed that further deduplication inside that role weakened routing behavior.
- Installers migrate cleanly by backing up/pruning only known package-owned legacy commands, snippets, and obsolete docs while preserving unrelated user/project files.

See [`docs/releases/v30.00.md`](docs/releases/v30.00.md).

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

See [`docs/releases/v28.35.md`](docs/releases/v28.35.md). The historical `docs/ocr_review_policy.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

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

See [`docs/releases/v28.33.md`](docs/releases/v28.33.md). The historical `docs/pr_readiness.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

## v28.32

v28.32 extends current-upstream freshness into end-to-end repository state identity.

- Directly invoked roles own applicable freshness when no parent/orchestrator exists; delegated leaves still consume caller-supplied fresh target context instead of fetching redundantly.
- Authoritative target ref/SHA and intended mutation state survive nested delegation until explicitly changed.
- Static inspection, executable workspace, mutation baseline, verification/review, and publication are distinct state-identity steps that must not be silently mixed.
- Issue/report-derived work resolves its applicability target from issue/project metadata instead of assuming local checkout; publishing a current-state issue rechecks moved target evidence before publication.
- Tester validates executing state for target-bound evidence; mismatched-worktree results are workspace-only/target-unverified.
- Debugger/build/UI implementation refuse to edit a stale or unrelated worktree when the assignment is bound to a current authoritative target.
- `/ui-options` now follows the existing materially-distinct-options policy instead of forcing 2–3 alternatives.

See [`docs/releases/v28.32.md`](docs/releases/v28.32.md). The historical `docs/git_branch_provenance_policy.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

## v28.31

v28.31 fixes stale-code analysis when a workflow must decide whether an issue/behavior still exists in the current upstream/default/base state.

- Current-upstream claims now require a freshly resolved authoritative remote ref + SHA before code is treated as current.
- The primary/orchestrator performs the freshness fetch once and passes the target ref/SHA to specialists; leaf roles do not independently fetch by default.
- A stale local checkout may be used only as comparison/history evidence when it differs from the authoritative target; it cannot silently stand in for current upstream.
- Read-only `git fetch` is explicitly separated from `pull`/rebase/reset/checkout, so freshness checks do not mutate the working tree.
- `/bug-issue` and issue-originated bugfix diagnosis now resolve the report target first and verify current-upstream applicability against the fetched authoritative ref; explicitly local-workspace reports remain local.

See [`docs/releases/v28.31.md`](docs/releases/v28.31.md). The historical `docs/git_branch_provenance_policy.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

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

See [`docs/releases/v28.29.md`](docs/releases/v28.29.md). The historical `docs/verification_strategy.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

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
