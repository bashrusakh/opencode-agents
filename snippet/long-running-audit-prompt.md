# Long-running audit prompt

Use this when asking an agent to start or resume a full-project inspection or bug hunt.

```text
Use Persistent Planning Mode.

Task: full-project inspect / bug find for <project>.

Do not create arbitrary markdown reports.
Use `plans/<plan>/` as durable state.
If no plan exists, create one with `plan.md`, phase docs, and `todo.md`.
If a plan exists, read `plan.md`, `todo.md`, the active phase, implementation/review files if present, and latest handover before doing anything else.

Return only a compact digest in chat. Durable findings, progress, decisions, and next steps must be reflected in the canonical plan artifacts.

Before source edits, use Blueprint -> Gate -> Execute -> Digest.
Git operations remain gated.
```
