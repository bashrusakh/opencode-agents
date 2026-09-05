# Open Code Review usage

This pack vendors the upstream Alibaba `open-code-review` skill for predictable OpenCode discovery. Keep package-local review policy outside the upstream `SKILL.md`; refresh that skill from upstream rather than editing it locally. The pack integrates with OCR through `@reviewer` and `/review`.

Recommended flow:

```text
Startup block
→ normalize review target/scope
→ privacy/gated check
→ OCR when installed and approved
→ reviewer filters OCR output and adds policy judgment
→ readable Markdown verdict
```

Preferred command:

```bash
ocr review --audience agent --background "<project/request context>"
```

Scoped examples:

```bash
ocr review --audience agent --background "<context>" --commit <sha>
ocr review --audience agent --background "<context>" --from <base> --to <head>
ocr review --preview
```

Do not hardcode a stale OCR timeout. Follow the loaded skill/current CLI timeout and effort semantics, and give the surrounding shell/tool call enough time to cover the effective OCR review-group budget with headroom. Never cap it at 120 seconds.

Review-only requests must not auto-apply fixes.
