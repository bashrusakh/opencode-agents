# OCR / Open Code Review Policy

The root `AGENTS.md` and the bundled `open-code-review` skill are normative. This page describes how `@reviewer` uses Alibaba `ocr` as the preferred backend for code/diff review when it is installed and external sharing is allowed.

OCR is the review engine; `@reviewer` remains the scope, privacy, judgment, false-positive filtering, and final-verdict layer.

## Applicability

For code, diff, commit, branch, workspace, or PR review, prefer OCR when available and permitted. Do not force OCR onto plan/text/UI-copy critique or other non-code review.

OCR is locally read-only, but it may send code/diffs/context to its configured LLM provider. The root external-sharing gate controls that action.

Do not emit a second Startup merely because OCR is about to run. Use the one Startup for the current reviewer/workflow invocation.

## Environment and fallback

When needed, check availability/configuration with the current CLI, for example:

```bash
which ocr
ocr llm test
```

If OCR is unavailable, not configured, fails for a non-transient reason, or external sharing is not authorized, fall back to native read-only review and state why. Do not install OCR, configure providers, or request/store credentials as part of ordinary review.

## Invocation

Load and follow the current `open-code-review` skill. Use agent-friendly output and concise request/business context:

```bash
ocr review --audience agent --background "<project/request context>"
```

Use scoped flags such as `--commit`, `--from`, `--to`, or `--preview` when they match the target.

Do not hardcode a package-level OCR timeout. Follow the loaded skill/current CLI `--timeout` and effort/review-round semantics, and set the surrounding tool/shell timeout to at least the effective review-group budget with reasonable headroom. Do not kill a healthy review with a short outer timeout such as 120 seconds.

For large output, follow the skill guidance to preserve the complete review rather than truncating with `head`/`tail`.

## Fix policy

Review-only work never applies OCR suggestions automatically. A fix requires a separately normalized implementation deliverable and an implementation-capable role. Existing authorization for that implementation scope is respected; do not invent an extra approval ritual.

## Reviewer post-processing

After OCR, the reviewer should:

- verify material findings against surrounding code/tests where practical;
- filter obvious false positives and low-value nits;
- preserve precise file/line references;
- classify material findings by severity (`critical`, `high`, `medium`, with low notes only when useful);
- add judgment for right-level placement, regression risk, behavioral contracts, project rules, security/data/API concerns, and missing verification;
- issue a verdict tied to the reviewed effective diff/state.

A later change that affects reviewed behavior makes the affected review evidence stale.

## Suggested output

```md
## Code Review Results

**Scope:** ...
**Backend:** OCR | native fallback
**Verdict:** pass | pass with notes | changes required

### Critical / High / Medium
- **`path/file.ts:42`** — finding
  - Why it matters: ...
  - Suggested direction: ...

### Evidence / policy checks
- Right-level fix: ...
- Regression/preserved behavior: ...
- Behavioral contract: ...
- Verification gaps: ...
```

Omit empty severity sections.
