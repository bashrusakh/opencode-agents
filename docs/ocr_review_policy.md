# OCR / Open Code Review Policy

The root `AGENTS.md`, `@reviewer`, and bundled OCR skills are normative together. This page separates two OCR capabilities:

- **delegate preflight** — local deterministic file selection/exclusions/rule resolution; OCR calls no LLM;
- **managed OCR review** — `ocr review` runs an additional OCR-managed LLM review.

`@reviewer` remains the target/scope, privacy, coverage, judgment, false-positive filtering, and final-verdict layer.

## Applicability

For code, diff, commit, branch, workspace, or PR review, run delegate preflight whenever a compatible installed `ocr` exposes delegation commands. Plan/text/UI-copy critique and other non-code review do not need OCR delegation.

Delegation itself does not require an OCR LLM provider/API key and does not send the review to an OCR-side LLM. Managed `ocr review` may send code/diff/context to a configured provider; the root external-sharing gate applies to that managed step.

Do not emit another Startup merely because OCR is used.

## Required order for code-like review

1. Bind the exact authoritative target/state. For final owned-PR review, use the freshly resolved Base SHA + exact local Candidate HEAD.
2. Establish the authoritative changed-file/effective-diff set independently of OCR.
3. Load `open-code-review-delegate` and, when compatible delegation exists, run `ocr delegate preview` for that exact target.
4. Reconcile preview reviewable/excluded entries against the authoritative set using `(path, status)` identity. Every authoritative changed entry must remain accounted for; OCR exclusion is not automatic permission to ignore it.
5. Run `ocr delegate rule` for reviewable paths. Rules are an additional checklist and never override user/project/root requirements.
6. The host `@reviewer` reviews the complete accounted scope with its own model/tools, using bounded batches when needed and not stopping after the first severe finding.
7. After host review, decide whether managed `ocr review` materially adds independent confidence or is explicitly required.
8. Reconcile any managed OCR findings into the host verdict.

If the CLI/delegate capability itself is unavailable, perform native read-only scope discovery/rule loading and report `Delegate: unavailable`. This alone does not block a review. Do **not** use that fallback for `preview` errors that indicate invalid refs, wrong repository, or a target/scope mismatch; those errors challenge state identity and must be resolved before a complete verdict. When preview scope is trustworthy but only delegate rule resolution fails, continue with root/scoped project rules and report the delegate-rule gap.

## Delegate capability handling

Do not run `ocr llm test` before delegation. Check local capability instead:

```bash
which ocr
ocr delegate preview --help
ocr delegate rule --help
```

Use the current `open-code-review-delegate` skill. Prefer `--format json` when the installed subcommand exposes it; otherwise use its default text output. `unknown flag: --format` is a CLI/skill version-skew condition, not a reason to abandon a working text-mode preflight.

Do not silently truncate oversized background files. Preserve task requirements/constraints/acceptance criteria in a faithful concise background summary, or omit OCR background and let the reviewer consume the source context directly.

The documented delegate command boundary is `preview` + `rule`. Do not assume an aggregate `ocr delegate task` command unless the installed CLI itself exposes it.

## Scope and coverage ledger

Preview selection is useful evidence, not the authoritative review target. Keep a ledger across the whole review:

```text
(path, status) -> reviewable | excluded(reason) | native-added -> reviewed | skipped(reason)
```

The `(path, status)` key matters because workspace state can contain distinct entries for the same path. For full-PR coverage, reconcile the ledger against the complete Base-SHA-to-Candidate-HEAD changed set.

A full coverage claim requires every authoritative entry to be accounted for. If OCR excludes generated/config/schema/metadata or another file that may materially affect behavior, the reviewer still decides whether it must be inspected. An unexplained mismatch between authoritative scope and delegate scope blocks `Coverage: full PR`.

## Managed OCR escalation

Managed `ocr review` is intentionally **not** the automatic first step. The reviewer may run it after host review when:

- user/project policy explicitly requires managed OCR;
- security/auth/data/persistence/concurrency/API/schema or similar risk warrants an independent second model pass;
- reviewer confidence is insufficient or evidence conflicts;
- a complex cross-file invariant would materially benefit from another independent reasoning pass.

For routine comprehensible diffs with complete host coverage and sufficient confidence, skip managed OCR.

Before managed OCR, load the current `open-code-review` skill, check the external-sharing gate, and then check/configured LLM availability only as needed. Do not hardcode stale timeout/model/output flags; the bundled skill is the command contract.

If managed OCR fails due to rate limit, quota, provider/model outage, or another non-transient provider problem, do not retry blindly and do not erase completed host-review evidence. If an optional second pass would require OCR installation, CLI upgrade, provider/model configuration, or credentials, do not create a new user gate just to obtain optional evidence; report `Managed OCR: unavailable — <reason>` and keep the host verdict. Ask for setup/upgrade only when managed OCR itself was explicitly requested/required. The overall review is blocked only when required managed OCR cannot run.

## Owned-PR Ready evidence

The final reviewer verdict remains required for an owned PR Candidate under the normal readiness policy. Delegate preflight is the normal deterministic code-review preparation when available, but its availability is not a Ready gate. Managed OCR is additional evidence unless explicitly required.

The delegate ledger and any managed OCR escalation must refer to the same reviewed Base SHA + Candidate HEAD/effective diff as the final verdict. Base/head drift stales affected evidence under the normal state-identity rules. Pushing the exact reviewed head does not by itself require another review.

## Fix policy

Review-only work never applies delegate/OCR suggestions automatically. A fix requires a separately normalized implementation deliverable and an implementation-capable role. Bundled OCR skills do not override the reviewer's `edit/apply_patch: deny` boundary.

## Reviewer post-processing

The reviewer should:

- verify material findings against surrounding code/tests where practical, using narrow spot-checks rather than recreating `@tester`;
- filter obvious false positives and low-value nits;
- preserve precise file/line references when supported by evidence;
- group manifestations that share one affected state/lifecycle/protocol invariant;
- distinguish current-diff blockers from latent/unrelated report-only findings;
- add right-level, regression, behavioral-contract, security/data/API and verification-gap judgment;
- issue a verdict tied to the exact reviewed state/effective diff.

## Suggested output

```md
## Code Review Results

**Scope:** ...
**Delegate:** complete | unavailable — reason
**Coverage:** full | partial — gap
**Managed OCR:** not needed | pass/findings | unavailable/blocked — reason
**Reviewer:** pass | pass with notes | changes required

### Critical / High / Medium
- **`path/file.ts:42`** — finding
  - Why it matters: ...
  - Suggested direction: ...

### Coverage / evidence
- Delegate entries reviewed/skipped: ...
- Right-level fix: ...
- Regression/preserved behavior: ...
- Verification gaps: ...
```

Omit empty severity sections.
