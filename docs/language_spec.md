# Language and framework skill guidance

The active root `AGENTS.md` is normative. This file lists the bundled specialist skills and their intended targets.

When the normalized target matches a skill, load it through the OpenCode skill mechanism when available, or read its `SKILL.md`. Merely naming a skill does not count as using it. Load referenced files only when relevant.

| Target | Skill |
|---|---|
| Python | `python-pro` |
| TypeScript | `typescript-pro` |
| Go | `golang-pro` |
| C++ | `cpp-pro` |
| Rust | `rust-engineer` |
| React | `react-expert` |
| Vue | `vue-expert` |
| Security-sensitive code | `secure-code-guardian` |
| Playwright / E2E | `playwright-expert` |
| API design / OpenAPI | `api-designer` |
| Code/diff review | `open-code-review` when OCR is available and allowed |
| UI/UX design intelligence | `ui-ux-pro-max` when available and relevant |

Select by actual files, manifests, project context, and requested outcome rather than trigger words alone.

Skills are advisory. They do not override project-local rules, agent role boundaries, authorization gates, existing tooling, right-level/regression requirements, review/privacy policy, or Git/PR discipline.

Use existing project commands and conventions first. Do not introduce or tighten formatters, linters, compiler flags, coverage thresholds, dependencies, or build-system settings merely because a skill recommends them.

If a relevant selected skill is unavailable, report that fact instead of pretending it was used.
