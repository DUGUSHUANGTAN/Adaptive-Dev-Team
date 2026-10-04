# Adaptive Dev Team

**"I'm a team"**

Adaptive Multi-Agent Software Development Orchestrator.

A meta-skill that analyzes your development task and dynamically assembles the right
multi-agent team — from a single Builder for a one-liner up to a coordinated team of
Builders, Reviewers, and (only when their trigger fires) Specialists.

![Adaptive Dev Team Skill](https://img.shields.io/badge/Skill-Adaptive--Dev--Team-blue)

## How it works

1. **Triage** — Task type, complexity, risk, blast radius
2. **Team composition** — Minimum sufficient team, dynamically chosen
3. **Task DAG** — Dependencies and parallel waves
4. **Execute** — Delegation contracts, ownership, handoff
5. **Integration & QA** — Cross-module checks, regression
6. **Done** — Evidence-backed completion per workflow depth

## Installation

Copy the `adaptive-dev-team/` directory into your skills folder and reference
`SKILL.md` as the entry point. The skill follows progressive disclosure: start with
`SKILL.md`, load sub-modules (`roles/`, `workflows/`, `protocols/`) only when needed.

The skill is **standalone and vendor-neutral**: it declares no runtime dependencies
and reads no file outside its own directory, so copying that one directory is enough.
The only bundled code is the optional validation script, which uses the Python
standard library only.

`SKILL.md` carries Agent Skills-compliant YAML frontmatter:

```yaml
name: adaptive-dev-team
description: Dynamically orchestrates specialized sub-agents for software development work ...
license: MIT
```

The skill directory is `adaptive-dev-team/`, which matches the frontmatter `name`
exactly, as the Agent Skills specification requires — `scripts/check-structure.py`
asserts this on every run. The frontmatter's `license: MIT` matches the root
[`LICENSE`](LICENSE).

> The repository and the release asset keep the product name **Adaptive Dev Team**
> (`Adaptive-Dev-Team.zip`); only the skill directory uses the spec-required
> lowercase slug `adaptive-dev-team`.

## Project structure

The skill package lives in `adaptive-dev-team/` (matches frontmatter `name`):

- `SKILL.md` — Main controller and entry point (frontmatter: `name: adaptive-dev-team`, `license: MIT`)
- `roles/` — 13 core roles (Leader, Architect, Builder Lead, etc.)
- `builders/` — 14 builder types (Frontend, Backend, AI/LLM, etc.)
- `specialists/` — 10 specialist roles (Security, Performance, etc.)
- `workflows/` — shared `core.md` lifecycle + 10 per-workflow delta profiles (Light, Standard, Production, etc.)
- `protocols/` — 10 collaboration protocols (Delegation, Integration, Escalation, etc.)
- `policies/` — 7 governance policies (Agent Budget, Stop Conditions, DoD, etc.)
- `templates/` — 7 report templates
- `examples/` — 4 illustrative, hypothetical examples (not executed)
- `scripts/` — Validation script (`check-structure.py`, standard library only)
- `LICENSE` — bundled copy, so the package is self-contained (see below)

`references/` is **optional** and is not shipped by default; add it only if you have
external reference material to attach.

### Release package layout

The published release ZIP extracts to **exactly one directory** — there are no loose
files at the archive root. Unzip it into your skills folder and it is ready:

```text
skills/
└── adaptive-dev-team/     ← everything, including LICENSE
```

The repository root keeps its own `LICENSE` so GitHub detects the license;
`adaptive-dev-team/LICENSE` is the copy that ships inside the package. The two must
stay identical — `scripts/check-structure.py` reports drift.

## Development

This repository uses Git for version control. Contributions are tracked through
local commits; this is a self-contained skill package.

## License

MIT License — see the root `LICENSE`; the same license ships inside the package at
`adaptive-dev-team/LICENSE`.
