Adaptive Dev Team v1.0 — Release Notes
=========================================

Name: Adaptive Dev Team
Tagline: "I'm a team"
Skill Type: Adaptive Multi-Agent Software Development Orchestrator

What it does
------------
Dynamically analyzes software development tasks (Task Type, Complexity, Risk,
Blast Radius, Domains, Parallel Potential) and assembles the minimum sufficient
agent team. Supports Light (1-2 agents) through Production (full hierarchy with
Specialists, Security, Performance, DevOps) workflows.

Key features
------------
- Dynamic team composition based on Triage Engine
- 13 core roles (Leader, Architect, Builder Lead, QA, Reviewer, etc.)
- 14 Builder types (Frontend, Backend, AI/LLM, Game AI, Graphics-3D, etc.)
- 10 Specialist roles (Security, Performance, Accessibility, SRE, Migration, etc.)
- 10 Workflow profiles (Light, Standard, Advanced, Production, Bugfix, Refactor,
  Migration, Optimization, Research-heavy, Release)
- 10 Collaboration protocols (Delegation, Ownership, Parallelization, Handoff,
  Integration, Escalation, Conflict Resolution, Fix Loop, Task DAG, Triage)
- 7 Governance policies (Team Composition, Agent Budget, Context Management,
  Quality Gates, Stop Conditions, Change Management, Definition of Done)
- Progressive Disclosure: SKILL.md is entry/controller; sub-files loaded on demand
- Evidence Before Completion: no claim without verification
- Sub-Agent enforcement for medium+ / multi-module / parallel-potential tasks,
  with graceful degradation on hosts that lack sub-agent support
- Agent Skills Specification compliant entry (name/description/metadata)

Structure
---------
Adaptive-Dev-Team/
├── SKILL.md              (entry + progressive disclosure controller)
├── roles/                 (13 roles)
├── builders/              (14 builders)
├── specialists/           (10 specialists + dynamic-specialist rules)
├── workflows/             (10 workflow profiles)
├── protocols/             (10 collaboration protocols)
├── policies/              (7 governance policies)
├── templates/             (7 report templates)
├── examples/              (4 example workflows)
├── scripts/               (validation script)
└── references/            (optional reference material)

Requirements
------------
- Any agent host: parallel sub-agents, sequential delegation, or single-agent
  execution all supported (roles are simulated in-process when unavailable)
- Git for version control
- Standard library only (no external dependencies)

Installation
------------
Copy Adaptive-Dev-Team/ into your skills folder. Reference SKILL.md as entry point.
Use progressive disclosure: read only SKILL.md + relevant sub-file for the task type.

License
-------
MIT License — see LICENSE file.
