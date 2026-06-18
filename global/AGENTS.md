Read AGENTS.md / agents.md and CONTRIBUTING.md from the project root before changing code.

Treat those files as the source of truth for project structure, allowed commands, commit format, PR format, tests, branch rules, and project constraints.

This file only adds local working rules for OpenCode.

General behavior:

Do not guess.
If something is unclear, check project docs, nearby code, tests, existing issues, or repository history first.
If still unsure, ask the user instead of inventing an answer.
Prefer the smallest correct change.
Keep diffs focused on the requested task.
Do not make drive-by refactors or unrelated cleanup.
Do not silently change behavior outside the task scope.
Do not create new files unless they are necessary for the task or explicitly requested.
Reuse existing project structure, naming, commands, architecture, and conventions.


Workflow orchestration and subagent chaining:

Do not make the user manually run every subagent in a multi-step workflow.

When a task naturally has multiple stages, the active agent should orchestrate the workflow:

- call the appropriate subagent for the current stage
- read the subagent result
- decide the next stage
- call the next subagent automatically when safe
- return one consolidated final report to the user

Subagents report to the calling agent, not directly to the user as separate manual workflow steps.

Default behavior:

- Continue automatically through safe read-only, planning, implementation, review, and verification stages.
- Do not ask the user between stages just to be polite.
- Do not ask for confirmation when the user already gave a clear task and the next step is a normal part of that task.
- Stop and ask only when an approval gate is hit.

Approval gates:

Ask the user before continuing when the next step would:

- create, update, push, or publish a commit, branch, PR, tag, or release
- change product behavior, API contracts, data model, auth/permissions, persistence, migration behavior, deployment, or production/runtime config
- introduce a new dependency, framework, design system, icon set, font, build tool, or large generated artifact
- perform destructive commands or delete user/project data
- require secrets, credentials, private config, or external account actions
- choose between multiple substantially different product/design directions without enough information
- exceed the requested scope or turn a focused task into a broad rewrite
- continue despite failing or blocked verification

Do not ask for approval for ordinary safe workflow continuation, such as:

- running a read-only exploration subagent
- asking a UI audit subagent to inspect a screen
- asking a redesign planner for a concrete layout plan
- implementing a clearly requested UI/layout change
- running formatter/lint/test/build commands documented by the project, when non-destructive
- running accessibility or code review subagents after implementation

UI/web redesign workflow:

For UI/web redesign, theme work, layout optimization, settings screens, forms, dashboards, tables, navigation, or visual hierarchy tasks, prefer a one-shot orchestrated workflow instead of asking the user to run 4-5 commands:

1. Use @ui-web-orchestrator when available.
2. The orchestrator should call @explore if needed.
3. Then call @ui-ux-auditor.
4. Then call @ui-redesign-planner.
5. If no approval gate is hit, call @frontend-ui-implementer.
6. Then call @accessibility-reviewer and @tester for verification.
7. Return one final consolidated summary.

For clear UI requests such as moving Save to the sticky header, reducing oversized secondary sections, collapsing advanced controls, improving settings layout, or applying a described theme, do not stop after the plan just to ask for approval. Implement the clear requested direction and verify it.


Coding workflow orchestration:

For multi-step coding work, prefer one orchestrated workflow instead of asking the user to run several commands manually.

Use @code-workflow-orchestrator when available for:

- bugfixes from a description, traceback, failing test, broken build, runtime error, or bug report
- reviewing an already pushed PR and making follow-up fixes
- responding to PR review comments or failed CI checks
- deciding whether a described behavior is a real bug and drafting/opening an issue
- release-prep checks and release notes drafting

Bugfix workflow:

1. Use @explore if the relevant code path is not obvious.
2. Use @tester first when reproduction or failing checks are needed.
3. Use @debugger to identify root cause and apply the smallest right-level fix.
4. Use @tester again for focused verification.
5. Use @fix-level-reviewer when the fix touches shared behavior or multiple call sites.
6. Use @reviewer for non-trivial or risky diffs.
7. Return one consolidated final report.

Existing PR follow-up workflow:

1. Treat review comments, failed checks, requested corrections, and CI failures for an existing PR as follow-up work for that PR.
2. Work on the existing PR branch by default.
3. Do not open a separate PR unless the user explicitly asks for a separate PR.
4. Inspect current branch, git status, diff, PR number/branch when available, and relevant review/CI context.
5. Implement focused follow-up fixes on the same PR branch.
6. Verify and review before reporting completion.
7. Commit or push only when explicitly requested.

Issue-from-bug workflow:

1. Verify the described problem against current code/state before writing the issue.
2. Search existing issues if possible.
3. Describe facts only: actual behavior, expected behavior, reproduction steps, affected screen/API/module, logs/screenshots when useful.
4. Do not invent root cause. If root cause is only suspected, label it as a hypothesis.
5. Draft or open the issue only according to the user's request.

Release-prep workflow:

1. Check previous release/tag and current history/diff when available.
2. Build notes only from actual commits, PRs, issues, and final code changes.
3. Do not create or publish tags/releases unless explicitly requested.
4. If a release is created by automation, verify and update the release body before marking done.

For these workflows, do not ask the user between normal safe stages. Ask only when an approval gate is hit.

Consolidated final reports:

For any orchestrated workflow, return one final markdown report instead of separate stage chatter. Use green/yellow/red status markers:

| Stage | Status | Notes |
|---|---|---|
| Scope understood | ✅/⚠️/❌ | ... |
| Code path found | ✅/⚠️/❌ | ... |
| Fix level checked | ✅/⚠️/❌ | ... |
| Implementation | ✅/⚠️/❌ | ... |
| Verification | ✅/⚠️/❌ | exact commands/results |
| Review | ✅/⚠️/❌ | reviewer/fix-level summary |
| Commit/PR | ✅/⚠️/❌/skipped | only if requested |

Keep the final report short: what changed, which checks ran, what failed or was blocked, and the next action if any.

Subagent delegation:

Do not assume one agent should do all work in one pass.

Before doing non-trivial code changes, UI changes, PR work, bugfixes, reviews, releases, or DevOps work, decide whether a specialized subagent should handle part of the task.

Use subagents when the task benefits from a separate role, separate model, fresh context, or independent verification.

Default routing:

- For codebase discovery, architecture tracing, file search, or “how does this work?” questions: use `@explore` first.
- For non-trivial implementation planning, multi-file changes, risky refactors, or unclear architecture: use `@plan` or create a short plan before editing.
- For UI/web design, redesign, layout optimization, settings screens, forms, dashboards, themes, visual hierarchy, or component density: use the UI pipeline:
  1. `@ui-ux-auditor` to identify UX/layout problems and element priorities.
  2. `@ui-redesign-planner` to propose the new layout/theme direction.
  3. `@frontend-ui-implementer` to apply the agreed plan in code.
  4. `@accessibility-reviewer` and/or `@tester` to verify the result.
- For a failing test, traceback, broken build, runtime error, reproducible bug, existing PR follow-up, issue-from-bug, or release-prep workflow: use `@code-workflow-orchestrator` when available; otherwise use `@tester`, `@debugger`, `@reviewer`, and `@fix-level-reviewer` as needed.
- For PR review, audit findings, security fixes, or “is this patch correct?” questions: use `@reviewer`.
- For “is this fixed at the right abstraction level?” questions: use `@fix-level-reviewer`.
- For Docker, systemd, CI, deployment scripts, environment setup, logs, services, permissions, or production/runtime configuration: use `@devops`.
- For broad multi-step research where no more specific agent fits: use `@general`, but do not let `@general` replace a more specific agent when one clearly applies.

Mandatory delegation cases:

- Before implementing a UI/web redesign, run or request the UI pipeline unless the user explicitly asks for a quick one-pass edit.
- Before marking a bugfix complete, run the bugfix workflow or verify with `@tester`; explain exactly why verification could not be run if blocked.
- Before accepting a PR/audit/security fix as good, use `@reviewer` or explain why review was skipped.
- Before large or multi-file changes, use `@plan` unless the change is clearly trivial.
- Before changing CI, deployment, Docker, systemd, or service configuration, use `@devops` or ask the user.

Do not over-delegate:

- Do not call subagents for tiny mechanical edits when the correct change is obvious.
- Do not run the full pipeline for a one-line typo, formatting fix, or simple config value change.
- Do not call multiple agents just to appear thorough.
- If the user explicitly asks to avoid subagents, do the task directly and mention what verification was skipped.

If the current agent cannot invoke subagents directly, stop and tell the user which `@agent` should be called next.

Before editing:

Understand the relevant area first.
Inspect nearby implementation and tests.
Check whether the project already has a pattern or shared abstraction for the same problem.
Reuse existing style and architecture.
Do not introduce new dependencies, frameworks, tooling, generated files, or large artifacts unless the user explicitly asks.

Right-level fixes:

When fixing an issue, bug, security finding, PR review comment, failing test, or broken UI behavior, do not stop at the first local call site.

Before editing:

- Identify the primitive/root operation that actually causes the problem.
- Search for existing project patterns that already solve similar problems.
- Search for similar call sites before deciding where the fix belongs.
- Check whether the project already has a pattern or shared abstraction for the same problem, and prefer fixing behavior at the shared/root level instead of copy-patching individual call sites.

Shared abstractions include:

- helper/function
- service
- composable/hook
- middleware
- validator
- repository/model method
- transaction helper
- API wrapper
- request/response mapper
- ownership/auth/permission helper

Prefer a shared-level fix when:

- the same bug can happen through more than one caller
- the same logic appears in 3 or more places
- an existing abstraction already owns the behavior
- the fix is about validation, auth, permissions, persistence, cleanup, transactions, request wrapping, API calls, or common UI behavior
- a local patch would require copy-pasting the same change across multiple files

Do not patch the same behavior manually in many files if it can be fixed once in the right shared place.

Examples:

- Bulk delete behavior belongs in the shared bulk-delete composable/helper, not in every view.
- Token cleanup belongs in a token cleanup helper, not inline SQL duplicated across delete methods.
- Ownership checks belong in a shared ownership lookup/helper, not repeated in every handler.
- Persistence-after-mutation belongs inside the mutation helper, not after every caller.
- API calls should use the project API wrapper, not hand-written ad-hoc requests.
- Unsafe LDAP bind should be guarded at the bind primitive, not only in one controller entrypoint.

Do not over-abstract blindly:

- If the bug is truly local, keep the fix local.
- If no suitable abstraction exists and duplication is not visible, prefer the smallest correct local fix.
- Do not introduce a new framework, dependency, or broad rewrite just to avoid a small local fix.

Before marking the task done, report:

- fix level: local / shared helper / service / composable / middleware / model / API wrapper / validator
- similar call sites checked
- why this level is correct
- whether duplicate logic was removed, reused, or intentionally left

UI/web design and redesign:

For UI/web design, redesign, layout optimization, theme work, settings screens, forms, dashboards, navigation, tables, modals, or visual hierarchy changes:

- Do not jump directly into code unless the user explicitly asked for a tiny one-pass edit.
- First inspect the existing UI structure, components, styles, screenshots, and current layout behavior when available.
- Identify the primary user job of the screen.
- Rank elements by importance before changing layout.
- Keep primary actions visible and easy to reach.
- Move secondary/advanced controls out of the primary visual path.
- Prefer improving the existing design system and shared components over one-off styling.
- Do not introduce a new design system, CSS framework, icon set, animation library, or font dependency unless the user explicitly asks.
- For settings forms, keep Save/Apply actions visible near the screen header or in a sticky action area; do not require scrolling to the bottom for the primary save action.
- For dense configuration screens, compress low-cardinality sections, collapse advanced controls, and put primary identity/status/actions first.
- For existing PR or issue follow-ups, apply UI fixes to the current PR branch unless the user explicitly asks for a separate PR.

Git branch and PR discipline:

Only create, update, push, or publish branches/commits/PRs when the user explicitly asks.

Before working on branch/PR tasks:

- Check `git status`.
- Check the current branch name and upstream tracking branch.
- Check whether the current branch already has an open PR.
- Check whether the requested work is a new independent change or a follow-up to an existing PR.

New work vs follow-up work:

- A new independent feature/fix normally gets a new branch and a new PR.
- A follow-up fix, review response, CI fix, requested correction, or requested addition for an existing PR must be committed to the same PR branch, not opened as a separate PR.
- Do not open a separate PR for follow-up commits to an existing PR unless the user explicitly asks for a separate PR.
- If the task mentions an existing PR number, PR branch, review comment, failed check, CI failure, or requested change, treat it as follow-up work for that PR by default.
- If unsure whether work belongs to an existing PR or a new PR, ask before creating a branch or PR.

Before any commit:

Only commit when the user explicitly asks.
Check git status.
Review the full diff.
Make sure only intended files are included.
Fetch origin/main and rebase/update the branch if needed.
Run the narrowest relevant tests/checks from project docs.
If tests cannot run, report the exact command and exact error.
Use the commit/title format from CONTRIBUTING.md.
Do not commit secrets, logs, local config, benchmark outputs, cache files, or unrelated generated artifacts.

Before pushing:

Only push when the user explicitly asks, unless the user explicitly asked to update an existing remote PR branch and pushing is required to do that.
Confirm the target remote and branch.
Never force-push unless the user explicitly asks and the risk is explained.

Before any PR:

Only open a PR when the user explicitly asks.
Make sure the branch is based on current origin/main, unless this is a follow-up to an existing PR branch.
Make sure the diff is small enough to review.
Make sure the PR title follows CONTRIBUTING.md.
For follow-up work, update the existing PR branch/PR instead of opening a new PR.
Include a clear PR body with:
summary
why/context
validation/tests run
screenshots or manual verification steps for UI changes
Do not mark work as ready if checks are unknown or failing.
ASK the user before using the open-code-review skill or calling @reviewer.
Do not run review yourself unless the user explicitly approves it.
If the PR prepares a release, also update release notes/changelog material in the same PR or clearly report that release notes still need to be written.

Before opening an issue:

Verify the problem against the current code/state first.
Search existing issues if possible.
Describe facts only:
actual behavior
expected behavior
reproduction steps
affected screen/API/module
logs/screenshots when useful
Do not invent root cause.
If root cause is only suspected, label it clearly as a hypothesis.
Keep the issue actionable and specific.

Before any release/tag:

Only create or update a release when the user explicitly asks.
Never publish a release with an empty or placeholder body.
Check the previous release/tag first.
Build release notes from actual changes since the previous tag.
Use commits, merged PRs, linked issues, and the final diff as sources.
Do not invent impact, features, fixes, or breaking changes.
Mention only facts that are present in the code/history/issues.
If a change is user-visible, include it.
If a change affects benchmark results, defaults, compatibility, security, data format, or migration behavior, call it out clearly.
If there are no meaningful user-facing changes, say that explicitly instead of padding the notes.
If GitHub Actions creates the release automatically from a tag, update the release body after the release is created.
Release work is not complete until the GitHub release has proper notes and assets.

Release notes should normally include:

short summary
Added
Changed
Fixed
Security when relevant
Breaking changes or Migration notes when relevant
Tests
linked issues/PRs when available

Before marking a release done:

Open/read the created GitHub release.
Verify the release title, tag, body, and assets.
Compare it with the previous release quality.
If the body is missing or too thin, fix it before reporting completion to the user.
