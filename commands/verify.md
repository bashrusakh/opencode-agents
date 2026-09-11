---
description: "Independently verify the current project state with relevant tests, linters, builds, smoke checks, and preserved-behavior evidence without fixing failures."
agent: tester
subtask: false
---

Verify the current state for: $ARGUMENTS

Follow the active `AGENTS.md` and tester role contract. Do not fix source/config/tests or weaken checks to obtain a pass. If verification is claimed for current upstream/default/base or another named SHA, establish/consume that exact state identity first; a test run from a mismatched worktree is not verification of that target.

Treat this invocation as one complete independent verification batch for the requested/delegated boundary. Discover the full applicable verification set from project guidance/configuration before returning: focused changed behavior, preserved/unaffected behavior, representative consumers/shared suites, and relevant lint/build/smoke checks. Run the smallest checks first, then continue through the already-applicable set inside the affected/delegated behavioral boundary when shared behavior/risk requires it; do not stop after the first PASS or ask for a predictable second tester invocation. One failing check also does not end the batch when other independent applicable checks can still provide distinct useful evidence; collect the coherent failure set before returning unless a blocker/dependency makes the rest meaningless or unsafe. If an invariant/state/interleaving matrix exists, map executed checks to the cases they actually cover. Do not fix missing dependencies/setup or adjacent failures as part of verification; report them to the caller.

Tie every verification claim to the current effective state/diff. If a check cannot run or fails, report the blocker/failure rather than editing around it. Do not claim broader coverage than the checks actually provide.
