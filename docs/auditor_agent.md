# Auditor agent

`auditor` is the broad read-only repository audit primary role. The active root `AGENTS.md` and `agents/auditor.md` are normative; this page is a usage summary.

Use it for whole-project or cross-module review such as:

- logic/correctness and incorrect assumptions;
- dead, stale, or unreachable code;
- wrong-level fixes and duplicated local patches;
- fragile shared abstractions and architecture drift;
- test/verification gaps;
- UI/API or frontend/backend mismatches;
- security/data-safety concerns;
- practical optimization opportunities supported by evidence.

Primary entry point:

```text
/audit <scope>
```

The auditor does not implement fixes or publish issues/PRs. It may coordinate specialist read-only passes when they materially improve coverage or independence. Related executable/tester questions and independent-review questions should be grouped by meaningful subsystem/invariant boundaries rather than dispatched once per finding; fresh existing evidence should be reused when sufficient. The auditor may run narrow read-only spot-checks to establish a specific finding, but broad executable verification remains a tester boundary and is not repeated when fresh tester/CI evidence already covers it. If a specialist cannot run, the missing coverage is reported rather than silently replaced by the auditor.

For broad/resumable audits, use the root Persistent Planning rules. A read-only audit does not create repository planning artifacts merely to maintain state unless that mutation is separately authorized.

Return one consolidated report with prioritized findings, evidence, confidence/limitations, and the smallest sensible next action for each material issue.
