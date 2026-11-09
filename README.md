<div align="center">

# OpenCode Agent Pack v31.22

### Semantic instruction pack for [OpenCode](https://opencode.ai/)

**Understand the task first. Then organize the work.**

[![Release](https://img.shields.io/badge/Release-v31.22_stable-16a34a?style=for-the-badge)](docs/releases/v31.22.md)
[![OpenCode](https://img.shields.io/badge/OpenCode-Agent_Pack-111827?style=for-the-badge)](https://opencode.ai/)
[![Semantic](https://img.shields.io/badge/Semantic-Task_Normalization-7c3aed?style=for-the-badge)](docs/technical-overview.md)
[![Models](https://img.shields.io/badge/Models-Agnostic-2563eb?style=for-the-badge)](docs/technical-overview.md)

</div>

---

## 🧭 What is it?

**A semantic agent pack that establishes the engineering task from a natural-language request *before* choosing how to implement it.** Tell it what you want fixed, built, or investigated; you do **not** need to prepare a full technical specification.

The workflow owner examines the request and project context to establish the intended outcome, constraints, and evidence for completion. Where the required behavior is genuinely uncertain, it investigates or asks rather than inventing requirements.

**Why not just use role prompts?** Roles such as “coder” and “reviewer” describe *who does the work*. This pack also controls *what the task means*, which decisions are authorized, and how conclusions are supported.

| Ordinary instruction collection | This semantic pack |
|---|---|
| Usually starts from a defined assignment | Establishes the task from the user's request and context |
| Describes role behaviors | Separates task ownership, authority, evidence, and implementation choices |
| Specialists may each interpret the goal | A workflow owner coordinates bounded delegation and reconciles results |

**Expected benefit:** less manual specification, fewer wrong-scope changes, and clearer grounds for claiming completion. These are design goals, **not independently measured gains**. The pack is model-agnostic; it does not automatically choose LLMs.

**Start with [`code-orchestrator`](agents/code-orchestrator.md)** for multi-stage tasks, or [`build`](agents/build.md) for an already-bounded edit.

## ⚙️ Install

Requires [OpenCode](https://opencode.ai/) and Bash. Unpack the release and run:

| Installation | Command |
|---|---|
| **Global** — agents, skills and shared policy | `./install/install-global.sh` |
| **Project-local** — from the target repository | `/path/to/opencode-agent-pack/install/install-project.sh` |

Installers back up replaced files. For projects with their own `AGENTS.md`, install globally first; the project installer preserves the existing project rules. [Installation details →](docs/technical-overview.md#install)

## 🤝 Contributing

Propose changes based on **observed failures or demonstrated instruction problems**, not extra rules “just in case”. Preserve role boundaries, identify the governing contract, and add a regression scenario for reusable failures.

```bash
python3 evals/run-release-gates.py
```

See the [semantic design & release manual](docs/semantic-design-manual.md). Passing the local checks alone does not certify a release.

## 📚 References & acknowledgements

The pack draws on published research, documentation, and open-source projects. These are **design references or upstream sources**, not mandatory runtime dependencies or endorsements. See the [source-to-rule audit](docs/semantic-design-source-audit.md) for provenance.

### Design guidance

| Source | What informed the pack |
|---|---|
| **OpenAI** | [Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering), [skills & prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), [goal-driven Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex), [agent improvement](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop): explicit goals, scoped instructions and evaluation against real traces |
| **Anthropic** | [Agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) and [long-running harnesses](https://www.anthropic.com/engineering/harness-design-long-running-apps): outcome-oriented evaluation and reliable multi-step work |
| **DeepSeek** | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), [code review](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/skills/dsh-code-review/SKILL.md) and [skill design](https://github.com/deepseek-ai/deepseek-harness/blob/master/.agents/notes/archived/feature/2026-07-05-skill-system.md): evidence-based review and conditional instruction loading |
| **Z.ai / GLM** | [Engineering & evaluation](https://z.ai/blog/glm-5.3): long-horizon agent tasks and executable checks |

### Upstream projects and integrations

| Project | Relation to this pack |
|---|---|
| [GrayMatter](https://github.com/angelnicolasc/graymatter) | Optional persistent-memory integration |
| [Alibaba Open Code Review](https://github.com/alibaba/open-code-review) | Upstream review skills; optional second-model review |
| [Jeffallan Claude Skills](https://github.com/Jeffallan/claude-skills) | Upstream specialist skills |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Upstream UI/UX skill assets |

**Explore the implementation:** [Technical overview](docs/technical-overview.md) · [Core rules](AGENTS.md) · [Roles](agents/) · [Skills](skills/) · [Evaluations](evals/) · [Release notes](docs/releases/v31.22.md) · [Changelog](CHANGELOG.md) · [Licenses](THIRD_PARTY_NOTICES.md)
