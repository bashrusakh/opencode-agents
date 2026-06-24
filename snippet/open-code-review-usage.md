# Open Code Review usage

This pack assumes Alibaba `open-code-review` may already be installed as a skill/plugin. Do not overwrite the user's installed skill or plugin command. The pack integrates with it through `@reviewer`, `/review`, and `/pr-review`.

Recommended flow:

```text
Startup checkpoint
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

Review-only requests must not auto-apply fixes.
