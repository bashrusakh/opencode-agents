# project-auditor

`project-auditor` is a read-only full-project review orchestrator.

Use it for:

- broad logic review
- dead/stale code sweep
- wrong-fix-level search
- duplicated local patch search
- test gap review
- UI/API mismatch review
- config/CI/deploy impact review
- practical optimization review

Primary command:

```text
/project-audit <scope>
```

Examples:

```text
/project-audit whole repo, focus on logic bugs and dead code
/project-audit admin UI + backend API, focus on wrong-level fixes and duplicated behavior
/project-audit current PR branch, check project-wide side effects and stale code
```

The agent must not edit files or create commits. It should return one consolidated report with confirmed findings, hypotheses, dead/stale code, wrong-level fixes, test gaps, and prioritized next actions.
