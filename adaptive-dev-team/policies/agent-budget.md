# Agent Budget Policy

## Core Principle: Scale Agents with Task Size

Budgets match task scope. Do not over-allocate for small tasks or under-allocate for critical ones.

## Budget Rules by Task Size

### Trivial
- Small bugs, docs updates, minor configuration.
- **Rule**: 1–2 agents. More than 2 needs justification.

### Small
- Feature additions, moderate refactoring, process improvements.
- **Rule**: 1–3 agents. A Specialist is added only on trigger.

### Medium
- Complex features, integration work, multi-system changes.
- **Rule**: 2–5 agents with explicit ownership per agent.

### Large
- Major features, greenfield work, production releases.
- **Rule**: 4–8 agents. Hierarchical structure permitted with justification.

### Critical / Large Greenfield
- Large-scale greenfield development, critical production changes.
- **Rule**: Hierarchical structure permitted; every agent must have a proven, distinct contribution.

## Adjustment Rules

- These are guidelines, not hard limits. Expand when a Specialist domain is genuinely triggered; reduce when coordination overhead exceeds the value of an extra agent.
- Justify every deviation in one line.
- A file, a role definition, or a process stage is not a reason to spawn an agent.

## Spawn Depth Rules

- **Default**: Leader → Roles / Builders (one level).
- **Complex parallel work**: Leader → Builder Lead → Builders (two levels).
- **Maximum depth**: three levels below the Leader; deeper requires justification. The canonical statement of this limit lives in `policies/team-composition.md`; keep the two in sync if it ever changes.
- Never add Builder Lead when only one Builder is active (see `policies/team-composition.md` § Builder Lead Trigger).

## Budget Verification

Before spawning any agent:

- Confirm the task size category.
- Confirm the required workflow stages and their depth (`workflows/core.md`).
- Check whether an existing role already covers the work.
- Verify no duplicate or overlapping ownership.
- Confirm ownership is assigned to exactly one agent.
- Confirm the budget matches the dependency graph — not a template.
