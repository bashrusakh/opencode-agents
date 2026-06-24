# OCR / Open Code Review Policy

This package treats Alibaba `open-code-review` (`ocr`) as the preferred backend for code, diff, commit, branch, workspace, and PR review when it is installed and allowed.

OCR is a review engine. `@reviewer` is still the policy and judgment layer.

## When to use OCR

Use OCR when semantic normalization selects code-review route and one of these is true:

- the user explicitly requested OCR/Open Code Review;
- the user invoked `@reviewer` for code/diff/PR/branch/commit/workspace review;
- project/user policy says OCR is the default review backend.

Do not use OCR for plan review, issue text review, release-note review, UX copy review, or non-code critique unless the user clearly wants code/diff review.

## Startup and privacy gate

Before running OCR, emit the normal startup checkpoint and state:

- review target/scope;
- mode: read-only unless a separate fix request exists;
- gated: yes/no;
- whether external code sharing is approved.

OCR is read-only for the local repo, but it may send code, diffs, and context to the configured OCR LLM provider. If external code sharing is not already approved by user/project policy, ask first.

## Environment checks

When needed, check:

```bash
which ocr
ocr llm test
```

If OCR is unavailable, not configured, or not approved, fall back to native read-only review and say why. Do not install OCR, configure providers, or set credentials unless the user explicitly asks; installs and secrets are gated actions.

## Invocation

Use agent-friendly output:

```bash
ocr review --audience agent --background "<project/request context>"
```

Use scoped review when the target is known:

```bash
ocr review --audience agent --background "<context>" --commit <sha>
ocr review --audience agent --background "<context>" --from <base> --to <head>
ocr review --preview
```

Prefer `--background` with concise business/request context. Avoid `--audience human` in agent workflows because progress UI can pollute output.

## Fix policy

For review-only requests, do not apply fixes automatically.

If the installed OCR plugin command suggests autonomous fixes, this package's gated-action policy still wins: fixes require a separately normalized fix request, scope confirmation, and normal gated checks.

## Reviewer post-processing

After OCR, reviewer must:

- filter obvious false positives and low-value nits;
- preserve precise file and line references;
- classify findings as High / Medium / Low;
- add policy judgment for right-level fixes, behavioral contract, tests, risky API/schema/config/data/migration changes, and project rules;
- format the result as readable Markdown.

## Output shape

```md
## Code Review Results

**Scope:** ...
**Backend:** OCR / native fallback
**Verdict:** pass / pass with notes / changes required

### High
- **`path/file.ts:42`** — finding
  - Why it matters: ...
  - Suggested fix: ...

### Medium
- ...

### Review policy checks
- Right-level fix: pass/issues
- Behavioral contract: pass/issues/N/A
- Tests/verification: pass/missing/blocked
```
