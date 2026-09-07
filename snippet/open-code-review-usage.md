# Open Code Review usage

This pack vendors the upstream Alibaba `open-code-review` skill. Keep package-local policy outside that upstream `SKILL.md`; refresh the skill from upstream rather than editing it locally.

`@reviewer` is the policy/judgment layer. For code/diff/commit/branch/workspace/PR review, prefer OCR when installed and external code sharing is allowed.

```bash
ocr review --audience agent --background "<project/request context>"
```

Scoped examples:

```bash
ocr review --audience agent --background "<context>" --commit <sha>
ocr review --audience agent --background "<context>" --from <base> --to <head>
ocr review --preview
```

Do not emit a second Startup merely because OCR is invoked. Do not hardcode a package timeout: follow the loaded skill/current CLI `--timeout` + effort/review-round semantics, and give the surrounding tool/shell call at least the effective review-group budget with reasonable headroom. Never kill a healthy review with a short cap such as 120 seconds.

Review-only work must not auto-apply fixes. A fix requires a separately normalized implementation deliverable and an implementation-capable role.
