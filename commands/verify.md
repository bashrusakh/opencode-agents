---
description: "Independently verify the current project state with relevant tests, linters, builds, smoke checks, and preserved-behavior evidence without fixing failures."
agent: tester
subtask: false
---

Verify the current state for: $ARGUMENTS

Follow the active `AGENTS.md` and tester role contract. Do not fix source/config/tests or weaken checks to obtain a pass.

Discover applicable verification from project guidance/configuration. Run the smallest checks that directly exercise the requested behavior first, then broaden only when shared behavior/risk requires it. Report exact commands and actual outcomes.

Tie every verification claim to the current effective state/diff. If a check cannot run or fails, report the blocker/failure rather than editing around it. Do not claim broader coverage than the checks actually provide.
