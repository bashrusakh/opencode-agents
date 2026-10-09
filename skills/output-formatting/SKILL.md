---
name: output-formatting
description: Use for substantial PR/issue/release/review/public Markdown where destination-specific formatting materially matters. Root AGENTS.md remains authoritative.
---

# Output formatting

Conditional destination-specific formatting policy for substantial public/user-facing artifacts. Root communication, authority, and gate rules remain authoritative.

Choose the richest portable Markdown subset the destination reliably supports:

- GitHub/GitLab PRs, issues, releases, and reviews: short headings, bullets, code fences, links, and tables only when they materially improve comparison or status.
- OpenCode CLI, Hermes, Telegram, terminals, and chat relays: compact portable Markdown; avoid raw HTML, oversized tables, deeply nested lists, and GitHub-only formatting when the target may not render it.
- Plain-text-only channels: use a Markdown-compatible plain-text subset where permitted; when the destination mandates another syntax, follow that required format.

For review/disposition artifacts, make states such as approve, reject, defer, supersede, or blocked explicit when that state materially matters to the destination.
