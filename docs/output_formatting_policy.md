# Public / user-facing output formatting

The root `AGENTS.md` output rules are normative. This page is the compact destination-specific reference for final answers and public/project Markdown.

## Core rule

Correct content must also be easy to skim and act on. Avoid AI wall-of-text output, filler, repeated policy narration, and long dense paragraphs when the content contains multiple findings, decisions, risks, steps, or validation results.

## Default structure

Use target-aware portable Markdown unless the destination requires another format. Prefer:

- one short summary first;
- short headings when they improve navigation;
- bullets for multiple findings/reasons/checks;
- fenced code blocks for commands, logs, paths, config, diffs, or exact proposed text;
- compact tables only when they materially improve comparison/status;
- a clear conclusion or next action when useful.

Do not emit ceremonial sections or rows whose only content is `skipped`.

## Destination guidance

### GitHub / GitLab

Use normal Markdown. For PR/issue/release/review text, make scope, evidence/validation, and conclusion easy to find. Follow project templates when they exist.

### OpenCode CLI / terminals

Use compact Markdown/plain text. Prefer short headings, bullets, and code fences. Avoid raw HTML, wide tables, and deep nesting.

### Telegram / Hermes / chat relays

Use simple portable Markdown/plain text. Keep paragraphs short and avoid GitHub-only formatting.

For a tiny public comment, one short summary plus a few bullets is enough. For larger artifacts, use only the sections that help the target reader understand context, evidence, and the next action.
