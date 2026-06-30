# Persistent plans layout

Use this layout for long-running or multi-agent work:

```text
plans/<plan>/
  plan.md
  phases/
    phase-1.md
    phase-2.md
  implementation/
    phase-1-impl.md
    phase-2-impl.md
  reviews/
    plan-review.md
    impl-plan-review-phase-1.md
    impl-review-phase-1.md
  todo.md
  handovers/
    session-YYYY-MM-DD.md
```

Rules:

- The plan directory is durable memory.
- Do not create arbitrary agent report markdown files.
- A new agent/session must read `plan.md`, `todo.md`, the active phase, active implementation plan, latest reviews, and latest handover before continuing.
- Use `Blueprint -> Gate -> Execute -> Digest` for broad implementation.
