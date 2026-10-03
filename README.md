# Adaptive Dev Team

**"I'm a team"**

Adaptive Multi-Agent Software Development Orchestrator.

A meta-skill that analyzes your development task and dynamically assembles the right
multi-agent team — from a single Builder for a one-liner to a hierarchical hierarchy
of Builders, Specialists, and Reviewers for a production system.

![Adaptive Dev Team Skill](https://img.shields.io/badge/Skill-Adaptive--Dev--Team-blue)

## How it works

1. **Triage** — Task type, complexity, risk, blast radius
2. **Team composition** — Minimum sufficient team, dynamically chosen
3. **Task DAG** — Dependencies and parallel waves
4. **Execute** — Delegation contracts, ownership, handoff
5. **Integration & QA** — Cross-module checks, regression
6. **Done** — Evidence-backed completion per workflow depth

## Installation

Copy the `Adaptive-Dev-Team/` directory into your skills folder and reference
`SKILL.md` as the entry point. The skill follows progressive disclosure: start with
`SKILL.md`, load sub-modules (`roles/`, `workflows/`, `protocols/`) only when needed.

## Project structure

- `SKILL.md` — Main controller and entry point
- `roles/` — 13 core roles (Leader, Architect, Builder Lead, etc.)
- `builders/` — 14 builder types (Frontend, Backend, AI/LLM, etc.)
- `specialists/` — 10 specialist roles (Security, Performance, etc.)
- `workflows/` — 10 workflow profiles (Light, Standard, Production, etc.)
- `protocols/` — 10 collaboration protocols (Delegation, Integration, Escalation, etc.)
- `policies/` — 7 governance policies (Agent Budget, Stop Conditions, DoD, etc.)
- `templates/` — 7 report templates
- `examples/` — 4 example workflows
- `scripts/` — Validation scripts

## Development

This repository uses Git for version control. Contributions are tracked through
local commits; this is a self-contained skill package.

## License

MIT License — see `LICENSE` file.
