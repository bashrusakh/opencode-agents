---
description: "Verify a described bug and draft or open a factual, actionable issue without inventing root cause."
agent: code-orchestrator
subtask: false
---

Handle the bug-derived issue request for: $ARGUMENTS

Follow the active `AGENTS.md` and code-orchestrator contract.

Before drafting or opening an issue:
- verify the reported behavior against current code/state and available evidence;
- inspect the affected path deeply enough to separate confirmed facts from hypotheses;
- search existing issues/PRs when repository access supports it and avoid duplicates;
- do not invent a root cause that has not been established.

If the normalized deliverable is a draft, return the issue text without publishing. If opening/updating the issue is clearly in scope, apply the root authorization gate and publish only the verified non-duplicate issue.

Do not fix repository code unless a separate implementation deliverable is also clearly requested.
