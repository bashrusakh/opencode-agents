---
description: "Explore the codebase and return grounded facts, file/symbol paths, call paths, and existing implementation patterns."
agent: explore
subtask: false
---

Explore the codebase for: $ARGUMENTS

Follow the active `AGENTS.md` and explore role contract. Stay read-only.

Trace the smallest relevant surface first, then expand only when evidence requires it. Return concrete file/symbol paths, call/data flow, nearby tests/docs, and existing patterns that answer the request. Distinguish verified facts from inference.

Do not implement fixes, run mutation-oriented commands, or turn exploration into a broad audit unless the normalized request actually asks for one.
