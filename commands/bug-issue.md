---
description: "Verify a described bug and draft or open a factual, actionable issue without inventing root cause."
agent: code-orchestrator
subtask: false
---

Handle the bug-derived issue request for: $ARGUMENTS

Follow the active `AGENTS.md` and code-orchestrator contract.

Before drafting or opening an issue:
- resolve the state the report applies to; when it claims current upstream/default/base behavior, refresh the authoritative remote ref and record its SHA before inspecting code; do not treat an older local checkout as current;
- verify the reported behavior against that resolved target state and available evidence;
- inspect the affected path deeply enough to separate confirmed facts from hypotheses;
- search existing issues/PRs when repository access supports it and avoid duplicates;
- do not invent a root cause that has not been established.

In the result, state the verified target as `<ref @ sha>` when a remote/current-state ref was used, or `local workspace` when that was explicitly the target. If freshness could not be established, say so and do not present the issue as verified against current upstream.

If the normalized deliverable is a draft, return the issue text without publishing. If opening/updating the issue is clearly in scope, apply the root authorization gate; before publication, confirm the authoritative target SHA is still current enough for the claim, and if it moved, re-check the affected applicability evidence before publishing the verified non-duplicate issue.

Do not fix repository code unless a separate implementation deliverable is also clearly requested.
