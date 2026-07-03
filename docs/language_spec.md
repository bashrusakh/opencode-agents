# Language spec

Use installed skills as focused guidance after Startup/normalization.

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

Skills are advisory only. They do not override project `AGENTS.md`, `CONTRIBUTING.md`, Startup checkpoint, gated-action rules, existing tooling, minimal focused diff, OCR/review policy, or PR branch provenance.

Use existing project commands first.

Do not introduce or tighten formatters, linters, strict compiler flags, coverage thresholds, sanitizers, dependencies, or build-system config unless explicitly requested or approved.

Mention skill usage briefly when useful:

```text
Skill: python-pro. Tooling: existing pytest/ruff commands.
```
