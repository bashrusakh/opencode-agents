---
description: "Diagnose and fix a confirmed failure, reproducible bug, failing test/build, traceback, or runtime error."
agent: debugger
subtask: false
---

Debug this failure: $ARGUMENTS

Follow the active `AGENTS.md` and debugger role contract.

Work from evidence: reproduce non-destructively when practical, identify root cause and the correct fix level, implement the smallest correct bugfix, and verify both the changed behavior and the nearest preserved behavior/invariant. Expand verification proportionally when the changed path is shared or stateful.

Do not turn a bugfix into unrelated cleanup or generic feature work. Do not weaken tests/checks merely to obtain a pass.
