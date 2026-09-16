---
name: open-code-review
description: >
  Performs AI-powered code review on Git changes using the `ocr` CLI from
  alibaba/open-code-review. Use when the user asks to review code, review
  a pull request, review staged/unstaged changes, review a commit, or
  compare branches for code quality issues. Produces line-level review
  comments and can automatically apply fixes when requested. With appropriate
  review rules, can detect various types of issues including bugs, security
  vulnerabilities, performance problems, and code quality concerns.
license: Apache-2.0
compatibility: >
  Requires the `ocr` CLI installed (via `npm install -g
  @alibaba-group/open-code-review` or GitHub release binary). Review mode
  requires a configured supported LLM provider before first run.
metadata:
  author: alibaba
  homepage: https://github.com/alibaba/open-code-review
  version: "1.0.0"
---

# Open Code Review

A skill for invoking [open-code-review](https://github.com/alibaba/open-code-review) (`ocr`) — an open-source AI code review CLI that reads Git diffs and generates structured, line-level review comments.

This Skill documents the normal `ocr review` workflow. OCR delegation mode is a separate workflow/Skill: in delegation mode OCR performs deterministic file selection and rule resolution while the host agent performs the review itself.

## Workflow

### Step 1: Gather Business Context

Analyze the review target (commits, branch, or changes) to extract concise business context. Pass this context via `--background` or `--background-file` to improve review quality.

### Step 2: Run Code Review

Run the OCR command with appropriate flags. **Always pass business context when available:**

```bash
ocr review --audience agent --background "business context here" [user-args]
```

For longer Markdown context, prefer:

```bash
ocr review --audience agent --background-file /path/to/context.md [user-args]
```

`--background-file` takes precedence over `--background` when both are supplied.

### Review Target

- **Default** (no target arguments): reviews staged, unstaged, and untracked changes (workspace mode)
- **Specific commit**: `--commit <ref>` or `-c <ref>` reviews one commit against its parent
- **Branch/range comparison**: `--from <ref> --to <ref>` reviews the diff between two refs
- **Repository root**: `--repo <path>` runs against another repository root instead of the current directory
- **Exclude paths**: `--exclude <patterns>` adds comma-separated gitignore-style exclusions and merges them with rule-file exclusions
- **Custom rule file**: `--rule <path>` selects an explicit review-rule JSON file

Only one diff mode may be used: either `--from/--to` or `--commit`. `--from` and `--to` must be supplied together.

### Agent Output

Always use `--audience agent` when another agent will consume the result. It suppresses human progress UI and emits the final review summary.

For machine-readable or integration output, `--format` / `-f` supports:

- `text` (default)
- `json`
- `sarif`

For large reviews, use `--output <path>` / `-o <path>` and read the complete file instead of piping stdout through `head` or `tail`:

```bash
ocr review --audience agent --output /tmp/ocr_out.txt -b "context" [user-args]
```

An empty output path or `-` means stdout. A real output file is created lazily, so a failed run does not truncate an existing file before the first write.

If `--output` fails specifically with `unknown flag: --output`, the installed CLI predates that flag. Do not silently fall back to potentially truncated stdout. Ask whether to upgrade with:

```bash
npm i -g @alibaba-group/open-code-review@latest
```

After an approved successful upgrade, rerun with `--output`.

### Model and Review Controls

Use these when the task or environment needs them:

- `--provider <name>` — override the configured LLM provider for this run
- `--model <name>` — override the configured model for this run
- `--effort low|medium|high` — override review effort; default is configured value or `medium`
- `--no-filter` — keep all review comments instead of running OCR's LLM post-filter
- `--concurrency <n>` — max concurrent review groups; default `8`
- `--timeout <minutes>` — timeout per concurrent task; default `15`
- `--max-tools <n>` — max tool-call rounds per subtask; `0` uses the template default, and positive values below `50` are raised to `50`
- `--max-git-procs <n>` — max concurrent Git subprocesses; default `16`
- `--max-tokens <n>` — per-group prompt token ceiling; `0` uses configured or template default
- `--max-tokens-budget <n>` — total input+output token budget for the review; `0` means unlimited
- `--tools <path>` — override the embedded tools configuration with a JSON tools config
- `--preview` / `-p` — show what would be reviewed without running the LLM

When `--max-tokens-budget` is exceeded, OCR stops dispatching new work and reports skipped items as `failed(budget)`. Partial results are still published and the command exits successfully unless every selected item failed.

### Timeout and Effort

Effective timeout per review group is approximately `--timeout` multiplied by the review-round count selected by effort. With the current defaults, `--timeout 15` and `medium` effort (2 rounds) gives a 30-minute group budget; `low`/`high` correspond to 1/3 rounds and therefore approximately 15/45 minutes.

Set any surrounding shell/tool timeout to at least the effective OCR budget plus reasonable headroom.

### Resume and Session Workflow

OCR persists review sessions. Use:

```bash
ocr session list
ocr session show <session-id>
ocr session comments <session-id>
ocr session compare <before-session-id> <after-session-id>
```

`ocr session` also accepts the alias `ocr sessions`; `list` accepts `ls`, and `compare` accepts `diff`.

A session ID from `ocr session list` can be passed to `ocr review --resume <session-id>`, but review resume is supported only for explicit range or commit review. Workspace resume is not supported.

Valid patterns:

```bash
ocr review --audience agent --from main --to feature --resume <session-id>
ocr review --audience agent --commit abc123 --resume <session-id>
```

Do not use `--resume` with `--preview`.

### Common Invocation Patterns

| User says | Command to run |
|-----------|---------------|
| "review my changes" / "review the working copy" | `ocr review --audience agent -b "context"` |
| "review this PR" / "review feature branch" | `ocr review --audience agent -b "context" --from main --to <branch>` |
| "review commit abc123" | `ocr review --audience agent -b "context" --commit abc123` |
| "review with a specific model" | `ocr review --audience agent --provider <provider> --model <model> -b "context"` |
| "resume that branch review" | `ocr review --audience agent --from <from> --to <to> --resume <session-id>` |
| "what would be reviewed?" | `ocr review --preview` |

**On failure:** If `ocr review` exits non-zero (for example because an LLM connection fails), do not retry blindly. Match the failure to the Troubleshooting guidance before rerunning.

### Step 3: Report

OCR output includes structured `severity` (`critical` / `high` / `medium` / `low`) and `category` (`bug` / `security` / `performance` / `maintainability` / `test` / `style` / `documentation` / `other`) on each comment. Present results grouped by severity, discarding `low` severity items that are likely false positives or nitpicks.

### Step 4: Fix

Before applying fixes, check whether the user requested automatic fixes:

- If the user explicitly requested "review and fix" or similar, proceed with automatic fixes when the active agent/project policy allows mutation
- If the user requested review only, do not modify code without separate authorization

When fixing issues and suggestions:

- Focus on critical, high, and medium severity items
- Apply fixes directly only when safe, well-defined, and allowed by the active workflow
- For complex fixes requiring manual intervention, clearly describe what needs to be done
- Do not commit or publish changes unless the active workflow/user authorization permits it

## Output Format

Each comment in OCR's output can contain:

- `path`: file path
- `content`: review comment text
- `start_line` / `end_line`: line range (both `0` means positioning failed)
- `category`: issue category (`bug`, `security`, `performance`, `maintainability`, `test`, `style`, `documentation`, `other`)
- `severity`: issue severity (`critical`, `high`, `medium`, `low`)
- `suggestion_code`: optional fix suggestion
- `existing_code`: optional original code snippet
- `thinking`: optional model reasoning field when emitted by the selected output path/model

Present results grouped by severity using this template:

```markdown
## Code Review Results

**Files reviewed**: N
**Issues found**: X critical, Y high, Z medium

### Critical

- **`path/to/file.java:42`** [bug] — Brief description
  > Recommendation: How to fix

### High

- **`path/to/file.java:26`** [bug] — Brief description
  > Recommendation: How to fix

### Medium

- **`path/to/file.ts:88`** [performance] — Brief description
  > Recommendation: How to fix (if applicable)
```

If no critical, high, or medium severity issues remain after filtering, state: "Review complete — no critical, high, or medium issues found in N files."

### Handling Mispositioned Comments

When `start_line` and `end_line` are both `0`, the comment failed to locate the exact position in the file. In such cases:

1. Read the comment content to understand the issue
2. Examine the target file mentioned in the comment
3. Identify the relevant code section from the comment context
4. Apply a fix only if mutation is in scope and authorized

## Review Rules

OCR already ships with built-in system rules, including language/file-type-specific rules. A custom rule file is optional; do not assume the user must create one before review.

When project-specific rules exist, OCR resolves them in this priority order:

1. `--rule <path>` flag (highest)
2. `<repo>/.opencodereview/rule.json`
3. `~/.opencodereview/rule.json`
4. Built-in system defaults (lowest)

By default, the first matching user rule replaces the matched built-in system rule. Set `merge_system_rule: true` on a rule entry when both the system rule and user rule should be included.

Rule file example:

```json
{
  "rules": [
    {
      "path": "**/*.java",
      "rule": "All new methods must validate required parameters for null",
      "merge_system_rule": true
    },
    {
      "path": "**/*mapper*.xml",
      "rule": "Check SQL for injection risks and missing closing tags"
    }
  ]
}
```

To preview which rule applies to a file before reviewing:

```bash
ocr rules check src/main/java/com/example/Foo.java
```

## Current Default Review Semantics

These defaults come from the current embedded review template, not the scan template:

- `MAX_TOKENS`: `200000` prompt-token ceiling for review
- `MAX_COMPLETION_TOKENS`: `16384` output-token cap
- `MAX_REVIEW_ROUNDS`: `2` before effort overrides are applied
- `PLAN_MODE_LINE_THRESHOLD`: `50`
- `PLAN_MODE_GROUP_LINE_THRESHOLD`: `100`

The plan phase runs when either:

- the largest changed file has at least `50` changed lines; or
- the review group contains at least `2` files and their combined changed lines are at least `100`.

Do not describe the review default as `MAX_TOKENS = 58888`; that value belongs to the current scan template, not the review template.

## Gotchas

- **A supported LLM provider must be configured for `ocr review`** — OCR supports multiple provider/protocol families rather than only Anthropic or generic OpenAI-compatible endpoints. Use the provider commands below instead of assuming one protocol.
- **Working directory matters** — `ocr review` operates on the Git repository at the current directory. Use `--repo /path/to/repo` to run elsewhere.
- **Untracked files are reviewed in workspace mode** — bare `ocr review` includes staged, unstaged, and untracked changes.
- **Workspace resume is unsupported** — `--resume` requires `--from/--to` or `--commit` and a compatible saved session.
- **Plan mode has two default triggers** — 50 changed lines in one file, or 100 combined changed lines across a group of at least two files.
- **Do not pass `--audience human` to an agent consumer** — human mode emits progress UI; use `--audience agent` for agent integration.
- **Comment language defaults to English when unset** — a non-empty configured language string is passed through as the requested response language. For example: `ocr config set language Russian`.
- **Avoid output truncation** — never pipe a large review through `head` or `tail`; use `--output <path>` and read the complete file.

## Validation

After the review completes, verify:

1. The command's actual exit status
2. Whether comments were generated or OCR explicitly reported none
3. Warnings/errors emitted on stderr
4. When a total token budget was used, whether any selected items were skipped as `failed(budget)`
5. When resuming, whether the requested session/range or commit was accepted and the resulting coverage is current

Do not infer a complete successful review merely from partial output.

## Troubleshooting

### `ocr: command not found`

Install the CLI:

```bash
npm install -g @alibaba-group/open-code-review
```

### `unknown flag: --output`

The installed CLI predates `--output`. Do not continue with potentially truncated plain stdout. Ask the user whether to upgrade:

```bash
npm i -g @alibaba-group/open-code-review@latest
```

After an approved successful upgrade, rerun with `--output`.

### `ocr review` fails with an LLM/provider error

Use the built-in provider/model setup first:

```bash
ocr config provider
ocr config model
ocr llm test
```

For non-interactive configuration, use the provider-specific keys documented by OCR, for example:

```bash
ocr config set provider anthropic
ocr config set model claude-opus-4-6
ocr config set providers.anthropic.api_key "$ANTHROPIC_API_KEY"
```

OCR also supports other built-in providers and custom providers/protocols. Do not invent provider names, models, URLs, or credentials. Never hardcode or fabricate API keys.

### Need to inspect a saved review

```bash
ocr session list
ocr session show <session-id>
ocr session comments <session-id>
ocr session compare <before-session-id> <after-session-id>
```

## References

- Full docs: https://github.com/alibaba/open-code-review
- NPM package: https://www.npmjs.com/package/@alibaba-group/open-code-review
- Issue tracker: https://github.com/alibaba/open-code-review/issues
