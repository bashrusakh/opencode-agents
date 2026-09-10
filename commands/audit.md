---
description: "Run a broad read-only project/repository audit for logic bugs, dead code, wrong fix levels, duplicate logic, test gaps, UI/API mismatches, security/data-safety risks, and practical optimization opportunities."
agent: auditor
subtask: false
---

Audit the project/repository for: $ARGUMENTS

Follow the active `AGENTS.md` and the auditor role contract. This command is read-only: do not implement fixes or publish issues/PRs as part of the audit.

Cover the areas that are relevant to the requested scope, including:
- core flows, logic, and incorrect assumptions;
- dead/stale/unreachable code and duplicated local fixes;
- wrong-level fixes or fragile shared abstractions;
- UI/API or frontend/backend drift;
- auth, permissions, security, and data-safety risks;
- test/verification gaps;
- practical optimization opportunities supported by evidence.

Use specialist audit/verification passes only when they materially improve coverage or independence. Batch related tester/reviewer questions by subsystem or invariant instead of invoking a specialist once per finding, and reuse fresh existing evidence when it already answers the audit question. The auditor may use narrow read-only spot-checks for a specific finding, but should not duplicate a broad tester boundary or rerun fresh tester/CI coverage. For broad or resumable work, follow the root Persistent Planning rules without creating repository plan files in a read-only workflow unless separately authorized.

Return one consolidated report with prioritized findings, evidence, confidence/limitations, and the smallest sensible next action for each material issue.
