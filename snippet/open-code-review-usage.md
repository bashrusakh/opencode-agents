# Open Code Review usage

This pack bundles two OCR skills with distinct roles:

- `open-code-review-delegate` — deterministic local preflight (`preview` + `rule`), no OCR-side LLM;
- `open-code-review` — managed `ocr review` command contract for an optional/required independent OCR-model pass.

`@reviewer` remains the target/scope/coverage/judgment/final-verdict layer.

## Delegate preflight

For code/diff/commit/branch/workspace/PR review, establish the authoritative target/effective diff first, then use delegation when compatible commands are installed:

```bash
ocr delegate preview [--from <base> --to <head> | --commit <sha>]
ocr delegate rule <reviewable-paths...>
```

Probe each subcommand's `--help` before assuming `--format json`; use text output when an older compatible CLI lacks that flag. Reconcile every delegate reviewable/excluded `(path,status)` entry against the authoritative changed set. OCR exclusions do not silently remove files from reviewer coverage.

Delegation needs no OCR LLM provider and no `ocr llm test`.

## Managed OCR escalation

After the host reviewer completes its own pass, use managed OCR only when explicitly required or when a second independent model pass materially improves confidence:

```bash
ocr review --audience agent --background "<project/request context>" [target args]
```

Load the bundled `open-code-review` skill for current target/output/provider/model/budget/session/timeout semantics. External code-sharing approval and OCR LLM availability apply to managed OCR. If quota/rate/provider failure occurs, preserve the completed host review unless managed OCR itself was mandatory.

Do not emit a second Startup merely because OCR is invoked. Review-only work must not auto-apply fixes; mutation requires a separately normalized implementation deliverable and an implementation-capable role.
