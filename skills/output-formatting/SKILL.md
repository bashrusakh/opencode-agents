---
name: output-formatting
description: Use for substantial PR/issue/release/review/public Markdown where destination-specific formatting materially matters. Root AGENTS.md remains authoritative.
---

# Output formatting

Conditional operational policy for substantial public/user-facing artifacts. Root authority/gates remain authoritative.

For any text shown to the user or published outside the agent runtime, optimize for readability, not just correctness. This applies to final answers, PR comments, PR bodies, issue bodies, release notes, changelog entries, review comments, handovers, plan artifacts, and Markdown docs.

No AI wall of text: write briefly, clearly, accessibly, and with enough structure to skim. Avoid excessive chatter, filler, self-justification, and long dense paragraphs.

Default to target-aware portable Markdown unless the destination requires another format. Use the richest safe subset the target reliably supports:

- GitHub/GitLab PRs, issues, releases, and reviews: structured Markdown with short headings, bullets, code fences, links, and tables only when they improve comparison/status.
- OpenCode CLI, Hermes, Telegram, terminals, and chat relays: compact Markdown/plain text with short headings, bullets, and fenced code blocks; avoid raw HTML, oversized tables, deeply nested lists, and GitHub-only formatting when the target may not render it.
- Plain-text channels: keep the same structure using short labels, bullets, and code blocks when possible.

Do not send dense wall-of-text paragraphs when the content contains multiple reasons, decisions, risks, steps, validation results, or evidence. If the answer can be short, keep it short. Lead with the information the reader can act on: completed work -> result first; blocked/user-decision work -> blocker plus required next action first; user-executed procedures -> first executable step first. Do not invent a next action when the requested work is complete. Prefer:

- clear sections for context/reason/validation/conclusion/next action when useful
- bullets for multiple findings/reasons/status items
- numbered steps only when the reader must perform an ordered multi-step procedure
- fenced code blocks for commands, logs, file paths, config snippets, and exact proposed text
- explicit conclusion when closing, rejecting, deferring, superseding, or approving work

Public comments should be concise, factual, skimmable, and easy to understand without rereading the whole thread.
