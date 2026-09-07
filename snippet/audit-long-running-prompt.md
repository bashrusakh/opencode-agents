# Long-running audit prompt

Use this when a broad read-only audit needs resumable state.

```text
Audit <project/scope> in read-only mode.

Follow the active AGENTS.md and auditor contract. Use Persistent Planning semantics because the audit is broad/resumable, but do not create or modify repository plan files merely to hold audit state unless that file mutation is separately authorized.

If an existing plans/<plan>/ applies, read its current canonical state. Otherwise use checkpoint/runtime state for continuation.

Use specialist read-only passes only when they materially improve coverage or independence. If a specialist cannot run, report that coverage as blocked/missing rather than performing its prohibited role yourself.

Return a compact consolidated digest with prioritized findings, evidence, limitations, and next actions. Do not implement fixes or publish issues/PRs as part of the audit.
```
