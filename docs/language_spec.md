# Language spec

Use installed skills as focused guidance after Startup/normalization. Agents should check project-visible guidance and the skills OpenCode advertises. When a matching skill is selected or required, load it through OpenCode's native skill mechanism when available, or read its `SKILL.md` before implementation/review; naming it does not count as skill use. Load referenced skill files only when relevant. If the selected skill cannot be found, report it as unavailable instead of pretending it was used.

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

Select by normalized target, files, manifests, and project context, not by trigger words alone.

Skills are advisory only. They do not override project `AGENTS.md`, `CONTRIBUTING.md`, Startup checkpoint, gated-action rules, existing tooling, minimal focused diff, OCR/review policy, PR readiness/body sync, or PR branch provenance.

Use existing project commands first.

Do not introduce or tighten formatters, linters, strict compiler flags, coverage thresholds, sanitizers, dependencies, or build-system config unless explicitly requested or approved.

Mention skill usage briefly when useful and in final reports for code work:

```text
Skill: python-pro. Tooling: existing pytest/ruff commands.
```
