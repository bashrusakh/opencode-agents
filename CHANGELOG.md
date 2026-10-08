# Changelog

This changelog summarizes user-visible workflow/documentation changes. Detailed notes for retained releases live under `docs/releases/`.

## v30.31 beta

- Makes `session-evaluator` request `session.list` with an explicit large limit before reconstructing the completed workflow tree; `all: true` is used only to include archived sessions.
- Allows `session-evaluator` to read OpenCode-managed `~/.local/share/opencode/tool-output/*` spill files when large session results are materialized there.
- Requires descendant discovery through `parentID` before treating child-session evidence as unavailable.
- Reads each participating session with `session.messages` using `all: true` without incompatible `limit`/`last` selectors.
- Marks only still-missing branches `unverified` instead of substituting orchestrator summaries for unavailable child histories.

See [`docs/releases/v30.31-beta.md`](docs/releases/v30.31-beta.md).

## v30.30 beta

- Replaces the package-owned `session_trace` wrapper with OpenChamber-native `session.list` and `session.messages` evidence collection in `session-evaluator`.
- Keeps the evaluator focused on semantic decision boundaries and instruction compliance without requiring raw tool-call traces.
- Removes `tools/session_trace.js` from the package and adds installer cleanup for that obsolete package-owned tool on upgrade.
- Updates README runtime/install/validation documentation for the OpenChamber-native evaluation path.

See [`docs/releases/v30.30-beta.md`](docs/releases/v30.30-beta.md).

## v30.29 beta

- Adds a fresh semantic prompt audit of root `AGENTS.md` and every agent file to mandatory release validation.
- Rewords the root behavioral-contract check to establish the contract without requiring a separate summary artifact.
- Consolidates repeated fallback wording in `general` and removes a redundant implementation prohibition in `project-planner`.
- Removes an arbitrary `3–7` next-action quota from `auditor` and a non-accessibility sticky-save-layout reminder from `a11y-reviewer`.
- Replaces a near-verbatim `tester` copy of root shared-path regression coverage with a direct root §7.3 reference.
- Makes `session-evaluator` neutral about whether a violation exists while preserving its evidence/classification requirements.
- Consolidates the owned-PR final-candidate lifecycle in `code-orchestrator` so the detailed sequence has one canonical home.
- Cleans README/changelog release prose and places the changelog overview directly under the document title.

See [`docs/releases/v30.29-beta.md`](docs/releases/v30.29-beta.md).

## v30.28 beta

- Audits and rewrites `README.md` against the shipped runtime/package surface, including the correct 16-agent / 18-skill / diagnostic-tool topology.
- Adds official OpenAI, Anthropic, DeepSeek, and Z.ai/GLM prompt/evaluation methodology references and separates them from OpenCode runtime/API references.
- Removes duplicated README upstream links, trims release/documentation listings that duplicated `CHANGELOG.md`, and keeps the changelog overview text in one canonical location.
- Rechecks README claims about install surfaces, persistent planning, PR/review flow, skills, and `session-evaluator` against the actual archive.

See [`docs/releases/v30.28-beta.md`](docs/releases/v30.28-beta.md).

## v30.27 beta

- Adds experimental `session-evaluator` for post-hoc semantic compliance audits of completed `code-orchestrator` sessions and their child-agent calls.
- Adds read-only `session_trace` access to the parent/child session tree and projected message timelines so the evaluator uses the observable trace instead of an orchestrator-authored summary.
- Adds one temporary post-completion trigger; evaluator findings are diagnostic evidence only and cannot reopen, modify, or gate completed work.
- Classifies findings as instruction violation, ambiguity, gap, execution error, or justified decision, with `unverified` reserved for evidence limits; prompt changes are proposed only for confirmed reusable instruction weaknesses.
- Uses time-local instruction provenance for the audit: current instruction text is not applied retroactively when the historical governing rule cannot be established.
- Excludes `session-evaluator` diagnostic sessions from the audited workflow tree so retries do not contaminate the trace.

See [`docs/releases/v30.27-beta.md`](docs/releases/v30.27-beta.md).

## v30.26 beta

- Treats material decisions about framing, required behavior, scope, ownership, invariants, and fix level as claims subject to the existing root authority/evidence checks.
- Reuses the existing counterexample and hypothesis rules for those decisions instead of adding a second self-review loop.

See [`docs/releases/v30.26-beta.md`](docs/releases/v30.26-beta.md).

## v30.25 beta

- Renames the package planning agent from `plan` to `project-planner` to avoid collision with OpenCode's shipped `plan` agent and its restricted project-edit policy.
- Updates current routing/handoff references to `@project-planner` while keeping repository planning writes limited to the existing authorized plan-artifact paths.
- Adds installer migration cleanup that backs up and removes the obsolete package-owned `agents/plan.md` on upgrade before installing `project-planner.md`.

See [`docs/releases/v30.25-beta.md`](docs/releases/v30.25-beta.md).

## v30.24 beta

- Makes the root necessity test explicit: judge a technical consequence against the established outcome, not against a broader rule inferred during planning, implementation, testing, or review.
- Strengthens `code-orchestrator` handoff salience by naming material claims that are still only evidence or hypotheses and forbidding their promotion to acceptance during delegation.

See [`docs/releases/v30.24-beta.md`](docs/releases/v30.24-beta.md).

## v30.23 beta

- Simplifies root `AGENTS.md` and all 15 role prompts using the current OpenAI guidance for lean prompts, plain language, direct statements, and one canonical home per instruction.
- Rewrites the authority-provenance rule with shorter direct wording while keeping the distinction between authoritative requirements, evidence, and necessary technical consequences.
- Compacts `code-orchestrator`, `reviewer`, tester, implementation, audit, and UI role wording so role files focus on role-specific decisions instead of restating root policy.
- Splits dense PR/readiness and delegation instructions into shorter decision steps and removes redundant prompt scaffolding.

See [`docs/releases/v30.23-beta.md`](docs/releases/v30.23-beta.md).

## v30.22 beta

- Makes claim authority explicit: derived reasoning, review findings, inferred invariants, tests, and prior agent decisions remain evidence unless they trace to authoritative intent/rules or a necessary consequence of them.
- Allows necessary cross-layer implementation work without escalation when it is required to satisfy an established outcome and does not strengthen the required behavior or authority.
- Prevents implementation/review invariant expansion from becoming its own authority for wider downstream fixes.
- Binds right-level boundary expansion to the established outcome under root §2.2.1.

See [`docs/releases/v30.22-beta.md`](docs/releases/v30.22-beta.md).

## v30.21 beta

- Tightens root intent/follow-through wording and makes the framing counter-check explicitly internal so it does not become a user-facing option ritual.
- Renames root §7.2 to `Right-level implementation boundary` so feature work and bugfixes share the same solution-level discipline.
- Consolidates repeated gate, ambiguity, skill-authority, and delegation-fallback wording into their canonical root sections.
- Adds a public-writing rule that changelog entries list actual changes while preservation/regression evidence belongs in validation or release-audit material.
- Cleans historical changelog entries that only described unchanged behavior.
- Corrects the README installer-validation path label from `command/doc/skill` to `command/doc/snippet`.

See [`docs/releases/v30.21-beta.md`](docs/releases/v30.21-beta.md).

## v30.20 beta

- Compacts the `code-orchestrator` implementation-prohibition block to the role-specific invariant plus canonical root §2.5 instead of repeating the full alternate-editor/fallback policy.
- Compacts the reviewer finding-classification list without removing any category or changing verdict semantics.

See [`docs/releases/v30.20-beta.md`](docs/releases/v30.20-beta.md).

## v30.19 beta

- Removes three duplicate root reminders whose canonical behavior already exists in request normalization / Startup policy.
- Removes the repeated delegated `Leaf boundary` boilerplate from role files; all roles still load the root contract and root §5 remains canonical.
- Replaces four role-local mutation-mechanism restatements with concise references to canonical root §7.1.1.

See [`docs/releases/v30.19-beta.md`](docs/releases/v30.19-beta.md).

## v30.18 beta

- Treats the first plausible non-trivial framing/fix level as a hypothesis and requires a materially different counter-framing only when it could change the outcome.
- Separates leaf technical implementation freedom from workflow-owner authority over new product/domain semantics, identities, ownership/source-of-truth rules, and destructive boundaries.
- Extends right-level discipline from bug corrections to all non-trivial implementation and defines production-grade behavior operationally without turning it into speculative “enterprise” architecture.
- Makes unexpected selectors/identities/persistence/coordination/guards a signal to re-check framing before design expansion.
- Adds reviewer coverage for technically coherent but unauthorized semantic scope creep.
- README current-version/footer links are corrected and the OpenAI current-model prompting guide used during this policy review is documented as an external design reference.

See [`docs/releases/v30.18-beta.md`](docs/releases/v30.18-beta.md).

## v30.17 beta

- Aligns readiness authority with the root priority hierarchy: pack readiness/verification evidence conditions do not self-elevate above explicit user intent unless they instantiate a higher-priority runtime/role/project constraint.
- Adds semantic non-circular gate handling for evidence whose availability depends on crossing the same lifecycle boundary.
- Replaces the code-orchestrator fixed `remote CI/status -> Ready` sequence with dependency-driven readiness and updates `pr-readiness` to classify host status/evidence by actual availability and authority.

See [`docs/releases/v30.17-beta.md`](docs/releases/v30.17-beta.md).

## v30.16 beta

- Removes the retired-skill migration special case from both installers; installers no longer carry knowledge of previously removed skill directories.

See [`docs/releases/v30.16-beta.md`](docs/releases/v30.16-beta.md).

## v30.15 beta

- Removes the experimental external context-compaction integration from the runtime pack after unacceptable latency in real use.
- Removes its bundled skill, setup/reference document, root activation/trigger semantics, and historical beta release note rather than retaining dead optional policy.
- Adds exact legacy-skill migration cleanup so global/project installs over older betas back up and remove the retired package-owned skill directory without touching unrelated skills.

See [`docs/releases/v30.15-beta.md`](docs/releases/v30.15-beta.md).

## v30.14 beta

- Makes native edit/patch the explicit default for bounded semantic repository edits when available and safe.
- Narrows scripted mutation to genuinely programmatic/mechanical bounded transformations, cases native edit/patch cannot safely express within the intended target set, or runtimes where native edit/patch is unavailable.
- Explicitly rejects convenience rationales such as shorter syntax, line-number targeting, avoiding exact-match friction, or a small number of textual replacements.
- Reinforces the rule in the mutation-capable `build`, `debugger`, `ui-implementer`, and `devops` roles while keeping orchestration handoffs semantic rather than tool-prescriptive.

See [`docs/releases/v30.14-beta.md`](docs/releases/v30.14-beta.md).

## v30.13 beta

- Adds a generic repository-prerequisite gate to owned-PR Ready transitions.
- Treats the unresolved required decision/approval as the blocker rather than the open/closed/linked state of a discussion, issue, RFC, forum, mailing list, or similar external artifact.
- Grounds prerequisite applicability/resolution in authoritative repository policy, maintainer decisions, and current repository/review/status signals; PR metadata may not claim agreement absent authoritative support.

See [`docs/releases/v30.13-beta.md`](docs/releases/v30.13-beta.md).

## v30.11 beta

- Makes the orchestration goal/path split explicit: parent owns semantic outcome/envelope/stage ownership; the selected leaf owns execution-local path/root-cause discovery.
- Narrows `@explore` routing so unknown implementation details do not create an intermediate discovery stage when a bounded implementation/debugging leaf already owns the next action.
- Moves fix-boundary proof from pre-handoff orchestration into the assigned implementation/debugging role under root §7.2; orchestrator keeps acceptance and preserved-behavior ownership.

See [`docs/releases/v30.11-beta.md`](docs/releases/v30.11-beta.md).

## v30.10 beta

- Distinguishes workflow-level ambiguity from execution-local ambiguity at delegation boundaries.
- Clarifies that focused implementation can be delegated from a bounded semantic outcome without the orchestrator first discovering exact files/symbols/local mechanics.
- Removes several routing-sensitive undefined qualifiers (`already-understood`, `scope/design is clear`, `obvious`) while retaining semantic judgment for materiality, risk, stage economy, and escalation.

See [`docs/releases/v30.10-beta.md`](docs/releases/v30.10-beta.md).

## v30.9 beta

- Makes the project-local README install example version-agnostic instead of embedding a beta directory name that becomes stale on release rename.

See [`docs/releases/v30.9-beta.md`](docs/releases/v30.9-beta.md).

## v30.8 beta

- Clarifies the root provenance pointer: `git-provenance` owns the canonical detailed policy, while root §8 binds it to repository-state workflows.
- Replaces the approximate `~45 KB` validation note with a stable `<50 KiB` compact-root target.
- Normalizes `git-provenance` and `pr-readiness` extracted subsection headings from H4 to H2.

See [`docs/releases/v30.8-beta.md`](docs/releases/v30.8-beta.md).

## v30.7 beta

- Adds an explicit `Pack version: v30.7 beta` marker inside root `AGENTS.md` so installed rule files can be identified directly.
- Renumbers the remaining visual-evidence subsection from `§8.3` to `§8.1` after earlier subsection compaction.
- Moves the changelog summary directly under the changelog title and removes the stray extra blank line around the v30.4/v30.2 boundary.

See [`docs/releases/v30.7-beta.md`](docs/releases/v30.7-beta.md).

## v30.6 beta

- Removes the bundled server-incompatible GitHub binary-upload integration and all associated package references and runtime policy hooks.
- Removes the integration's skill directory and the dedicated historical beta note that documented it.
- Bundled skill inventory is now 18 skills: 13 specialist/advisory and 5 workflow/policy skills.
- Visual-evidence publication uses only an already-available authorized mechanism; otherwise it preserves local evidence and reports publication blocked.

See [`docs/releases/v30.6-beta.md`](docs/releases/v30.6-beta.md).

## v30.5 beta

- Completes §2.1.1 with the full bundled skill inventory, separating specialist/advisory routing from conditional workflow/policy skills.
- States that all roles inherit the root skill catalog and that triggered policy skills must actually be loaded for the applicable stage without widening authority.
- Restores explicit entry-routing vs delegation-routing defaults after v30.4 compaction and keeps `@code-orchestrator` / `@auditor` out of delegation targets.
- Makes current-upstream provenance and owned-PR provenance/readiness skill dependencies explicit.
- Repairs stale v30.4 role references to removed root subsections in `build` and `ui-orchestrator`.

See [`docs/releases/v30.5-beta.md`](docs/releases/v30.5-beta.md).

## v30.4 beta

- Compacts root `AGENTS.md` from 75,493 bytes to ~45 KB.
- Moves detailed Git provenance, PR readiness, verification cadence, resource lifecycle, and output formatting mechanics into bundled conditional policy skills.

See [`docs/releases/v30.4-beta.md`](docs/releases/v30.4-beta.md).

## v30.2 beta

Beta resource-lifecycle and visual-evidence release built on v30.1 beta.

- Adds one canonical workflow-created resource lifecycle: creation creates cleanup ownership, and final completion requires reconciliation to `cleaned`, `intentionally retained`, `cleanup blocked`, or `ownership transferred`.
- Tracks related resources independently so removing a worktree does not silently imply its local branch, remote ref, process, or hosted evidence resource is also reconciled.
- Allows ordinary cleanup of current-workflow-owned local disposable resources when safe, while remote/published/shared destructive cleanup remains subject to the applicable gate unless that teardown was already authorized.
- Separates visual-evidence publication from repository-hosting state; gist/temporary branch/ref hosting is not an implicit fallback.
- Requires post-publication attachment verification and resource reconciliation for local screenshots, temporary execution workspaces/processes, and any fallback hosting resources.

See [`docs/releases/v30.2-beta.md`](docs/releases/v30.2-beta.md).

## v30.1 beta

Beta semantic-policy alignment release built on v30.00.

- Splits routing into entry routing and delegation routing so top-level ownership is not confused with invokable subagent edges.
- Uses agent frontmatter `mode` as the canonical execution-topology source for the OpenCode-specific pack.
- Removes inferred similarity fallback: fallback must be explicitly declared, executable from the current context, and no broader than the current authority/workflow envelope.
- Separates hard/mandatory preconditions from user-authorizable gates and prevents evidence/state/tool availability from becoming implicit authorization.
- Clarifies primary-role reroute behavior in `build`, fallback failure behavior in `code-orchestrator` / `ui-orchestrator`, and delegated UI orchestration leaf-dispatch with the workflow-owning parent.
- Narrows `plan` write permissions to portable canonical planning paths; removes the developer-specific absolute plan path and broad `docs/**` write scope.

See [`docs/releases/v30.1-beta.md`](docs/releases/v30.1-beta.md).

## v30.00

Stable successor to v28.42 focused on a smaller, deterministic runtime surface.

- Removes duplicated root/role policy where ownership is deterministic; universal routing, gates, state identity, provenance, right-level correctness, and evidence rules remain resident.
- Ships only the runtime surfaces OpenCode actually consumes: `AGENTS.md`, `agents/`, and `skills/`. Package custom commands and snippets are removed; setup docs remain human-facing only.
- Consolidates repository-state/provenance and Draft → Candidate → Ready semantics; role-specific execution behavior stays in the owning agents.
- Maps historical command intents to resident natural-language semantic routing instead of slash-command aliases.
- Restores `agents/code-orchestrator.md` exactly from v28.42 after behavioral testing showed that further deduplication inside that role weakened routing behavior.
- Installers migrate cleanly by backing up/pruning only known package-owned legacy commands, snippets, and obsolete docs while preserving unrelated user/project files.

See [`docs/releases/v30.00.md`](docs/releases/v30.00.md).

## v28.42

- Adds one canonical mutation-mechanism rule under the implementation policy.
- Bounded source changes prefer native file edit/patch capabilities when they safely express the intended mutation, while deterministic scripted/bulk transformations remain allowed when materially better suited or necessary.
- Broad textual replacement is explicitly not a substitute for semantic/structural understanding. Scripted or bulk mutation must constrain its target set before execution and inspect the resulting diff afterward.
- Tool choice cannot widen authorized scope or correctness obligations.
- README current-version/install-path/footer references are normalized to v28.42.

See [`docs/releases/v28.42.md`](docs/releases/v28.42.md).

## v28.41

- Synchronizes the package-maintained `open-code-review` skill with current Alibaba OCR managed-review behavior.
- Managed review no longer spends a common-path tool call probing `ocr` availability/version before execution; installation handling is entered only after an actual command-not-found failure.
- `--max-tokens-budget` now documents the current per-LLM-round enforcement, no-new-group behavior after exhaustion, and bounded final round for submitting pending findings.
- `--max-tools` now documents the current template default of `100`, the `1`-`49` clamp to `50`, and that the resolved override only takes effect above the template default.
- The normal OCR skill metadata now identifies Alibaba plus the package-maintained integration rather than implying the extended skill text is verbatim upstream.

See [`docs/releases/v28.41.md`](docs/releases/v28.41.md).

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

See [`docs/releases/v28.39.md`](docs/releases/v28.39.md).

## v28.38

v28.38 fixes contract-authority inheritance from referenced artifacts.

- Authority now attaches to individual claims, not automatically to the issue/PR/plan/comment/test/doc/task that contains them.
- A referenced artifact may establish scope and may contain normative requirements, but container, heading, repetition, confidence, or placement alone do not elevate a statement into the behavioral contract.
- Material acceptance claims must derive authority from current normalized user intent or project-local authoritative rules before implementation/planning/review treats them as requirements; an explicit current instruction may elevate a referenced artifact or selected parts.
- Claim authority and evidentiary support are separate: system evidence can support or refute a claim but cannot by itself make that claim a requirement.
- Issue/report-derived bugfixes treat unestablished claims as evidence/hypotheses instead of silently adopting proposed mechanisms or derived acceptance wording.
- Reviewer normalizes claim authority before applying semantic correspondence, preventing a self-confirming loop where an artifact's own proposed mechanism becomes both requirement and proof.

See [`docs/releases/v28.38.md`](docs/releases/v28.38.md).

## v28.37

v28.37 generalizes the v28.36 premise-validation rule around semantic correspondence instead of enumerating classes of mechanisms or bugs.

- Correctness claims must state the semantic property/outcome first; implementation facts and mechanisms are evidence rather than the contract itself.
- A proxy counts as proof only when its correspondence to the claimed semantic property is established from actual system behavior.
- Review establishes the specific evidence-to-semantics inference being used and checks for ordinary valid behavior where the same technical evidence would not justify the claimed semantic conclusion; reverse inference is proved separately only when the change relies on it.
- Reviewer, planner, and orchestrator treat implementation details as hypotheses until that correspondence is established.
- Tester/verification policy now asks whether the observed test result actually justifies the production conclusion being claimed, instead of maintaining a taxonomy of special cases.

See [`docs/releases/v28.37.md`](docs/releases/v28.37.md).

## v28.36

v28.36 hardens review and verification against self-confirming implementation assumptions.

- Adds one canonical contract-provenance/premise-validation rule instead of case-specific checks.
- Caller-proposed mechanisms, comments/docs introduced by the same change, new tests, and implementation descriptions are not independent proof of the premise they repeat; current production behavior is evidence, not automatically the desired contract.
- Material correctness guards/state transitions must have their semantic premises traced into production producers/owners/consumers, including unchanged adjacent code when needed.
- Representation-to-semantic mappings such as reference identity versus value equivalence must be established rather than assumed, and reviewers reason through an ordinary valid production transition that could falsify the premise.
- Changed-file coverage is explicitly separated from semantic-proof coverage.
- Tester verifies harness/fixture/mock fidelity for lifecycle/identity/order/ownership/timing-sensitive claims before promoting focused results to production evidence.
- Orchestrator and planner distinguish authoritative outcomes/invariants from implementation hypotheses when handing work between stages.

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

v28.34 strengthens right-level fix selection.

- Fix selection now starts from the end-to-end acceptance condition for the requested outcome, not from the nearest editable component.
- Before implementation, the chosen ownership/fix boundary must be capable of guaranteeing that condition across materially relevant paths, states, callers, partitions/instances, and lifecycle transitions.
- Local or per-partition guarantees do not count as proof of a system-level invariant unless their composition/aggregate behavior is established.
- If the proposed boundary cannot guarantee the required outcome, the workflow moves the fix level outward or escalates before coding instead of accumulating local patches.
- Planner, orchestrator, debugger, build, and reviewer role guidance now applies the same canonical fix-boundary principle.

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

v28.30 adds four targeted workflow-hygiene rules.

- A failed root-cause fix that leaves the same material failure now resets hypothesis confidence before another similar mutation is authorized.
- Orchestrators resolve safe non-gated uncertainty from evidence and batch compatible blocking user decisions.
- User-facing output now leads by state: result first when complete, blocker/action first when blocked, first executable step first for user-run procedures.
- Numbered steps are reserved for ordered human procedures rather than findings, options, status, or internal workflow diagrams.
- README Candidate/verification diagrams now explicitly show the optional/required Candidate-level `@tester` checkpoint before the final reviewer.

See [`docs/releases/v28.30.md`](docs/releases/v28.30.md) for the detailed before/after explanation.

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

See [`docs/releases/v28.29.md`](docs/releases/v28.29.md). The historical `docs/verification_strategy.md` companion was removed from the current bundle in v30.00 after its runtime contract became resident.

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

See [`docs/releases/v28.28.md`](docs/releases/v28.28.md) for the detailed before/after explanation.

## v28.27

v28.27 consolidated the model-agnostic behavioral contract around semantic routing, hard role boundaries, evidence freshness, correct Git base semantics, safer test/review behavior, and command/docs consistency.

Earlier release history is not reconstructed here; use the repository/package history where available.
