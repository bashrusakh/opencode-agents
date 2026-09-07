# Persistent plans layout

Use this repository layout only when durable plan-file state is actually in scope and authorized:

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

- The plan directory is durable task/coordination state, not general memory.
- GrayMatter memory stores durable conclusions/preferences; checkpoints store transient unfinished-task state.
- Read-only workflows do not create plan files merely to persist agent state.
- Do not create arbitrary model/agent report Markdown files.
- Resume from the current canonical plan/todo/active phase/implementation/reviews/handover that are relevant to the next step.
- Use `Blueprint -> Gate -> Execute -> Digest` for broad implementation, without turning Gate into a repeated approval ritual for already authorized scope.
