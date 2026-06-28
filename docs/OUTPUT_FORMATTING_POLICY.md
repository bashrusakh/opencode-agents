# Public / User-Facing Output Formatting Policy

Use this policy whenever an agent writes text for a human or for a public/project artifact: final answers, PR comments, PR bodies, issue bodies, release notes, changelog entries, code-review comments, handovers, plan artifacts, and Markdown docs.

## Core rule

Correct content is not enough. The output must also be easy to skim, quote, and act on.

No AI wall of text: write briefly, clearly, accessibly, and with enough structure to skim. Avoid excessive chatter, filler, self-justification, and long dense paragraphs.

Avoid dense wall-of-text paragraphs when the content contains multiple reasons, decisions, risks, steps, validation results, or evidence.

## Default format

Use target-aware portable Markdown unless the destination requires another format.

Prefer:

- one short summary first
- clear headings for context, reason, validation, conclusion, and next action when useful
- bullets for multiple points
- fenced code blocks for commands, logs, paths, config snippets, diffs, and exact proposed text
- compact tables only when they improve comparison/status and the target supports them
- explicit conclusion when closing, rejecting, deferring, superseding, approving, or recommending work

## Target-specific guidance

### GitHub / GitLab

Use normal Markdown: headings, bullets, code fences, checklists when useful, links, and compact tables. For PR/issue/release text, make the decision and validation easy to find.

### OpenCode CLI / terminals

Use compact Markdown/plain text. Prefer short headings, bullets, and code fences. Avoid raw HTML and wide tables.

### Telegram / Hermes / chat relays

Use simple portable Markdown or plain text. Prefer short paragraphs, bullets, and code fences. Avoid raw HTML, oversized tables, deeply nested lists, and formatting that only works on GitHub.

## Minimum structure for public comments

When posting or drafting a PR/issue/release/review comment, use this shape unless the target/project asks for another one:

```md
Short summary.

### Why / Context
- ...
- ...

### Validation / Evidence
- ...

### Conclusion / Next action
...
```

For very small comments, a one-line summary plus 2–4 bullets is enough.
