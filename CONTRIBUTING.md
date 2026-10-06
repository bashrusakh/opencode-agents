# Contributing to opencode-agents

This repository is the OpenCode Agent Pack (v30.17 beta): model-agnostic routing,
strict role boundaries, bounded multi-agent workflows, and a clean PR lifecycle.

## Triage labels

Labels are the source of truth for triage. Apply the correct label when you open an
issue or pull request; triage automation only verifies labels and fills gaps — it does
not overwrite a correct one.

Apply exactly one **type** label:

| Label | Use for |
| --- | --- |
| `bug` | Something is broken or behaves incorrectly. |
| `enhancement` | New functionality or a feature request. |
| `documentation` | Documentation-only change or doc issue. |
| `question` | A usage or support question. |
| `refactor` | Internal change with no behavior change. |
| `ci` | CI, build, or tooling change. |

Automation-managed labels (do not apply by hand):

- `needs-info` — routing/metadata information is missing from the report.
- `duplicate` — already tracked by another issue or pull request.

Triage automation owns the **type** labels above (`bug`, `enhancement`, `documentation`,
`question`, `refactor`, `ci`) plus `needs-info` and `duplicate`. It preserves a correct
type label you applied, fills a clearly missing one, and replaces a clearly incorrect
managed type by removing the wrong label and adding the right one; it does not churn
ambiguous labels.

`confirmed` is **human/verification-owned**, not automation-managed: it is applied by a
maintainer after the report has been reproduced or validated. Do not expect triage
automation to add or remove it.

`priority-*` and other operational labels are maintainer-owned.
