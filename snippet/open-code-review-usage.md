# Open Code Review usage

This pack assumes Alibaba `open-code-review` may already be installed as a skill/plugin. Do not overwrite the user's installed skill or plugin command. The pack integrates with it through `@reviewer` and `/review`.

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
ocr review --audience agent --timeout 10 --background "<project/request context>"
```

Scoped examples:

```bash
ocr review --audience agent --timeout 10 --background "<context>" --commit <sha>
ocr review --audience agent --timeout 10 --background "<context>" --from <base> --to <head>
ocr review --preview
```

Do not run OCR through a 120-second shell/tool timeout. Use at least 10 minutes when the runtime supports command/tool timeouts.

Review-only requests must not auto-apply fixes.
