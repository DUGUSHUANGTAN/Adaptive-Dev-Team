# Agent Budget Policy

## Core Principle: Scale Agents with Task Size

Agent budgets must match the task scope. Do not over-allocate resources for small tasks or under-allocate for critical ones.

## Budget Rules by Task Size

### Trivial (1 agent / 1–2 agents max)
- Small bugs, documentation updates, minor configurations
- **Rule**: Use 1–2 agents
- **Justification required** for more than 2

### Small (1–3 agents)
- Feature additions, process improvements, moderate refactoring
- **Rule**: Use 1–3 agents
- **Expansion allowed** if specialist expertise needed

### Medium (2–5 agents)
- Complex features, integration work, multi-system changes
- **Rule**: Use 2–5 agents
- **Expansion allowed** with clear ownership assignments

### Large (4–8 agents)
- Major features, greenfield work, production releases
- **Rule**: Use 4–8 agents
- **Hierarchical team permitted** with justification

### Critical / Large Greenfield (4+ agents, hierarchical allowed)
- Large-scale greenfield development
- Critical production changes
- **Rule**: Hierarchical structure permitted
- **Requirement**: Each agent must have proven value
- **Depth limit**: Leader → Builder Lead → Builders (max 2 levels below leader)

## Adjustment Rules

### These are not hard limits
- If the task clearly requires more specialists, expand the budget
- If the budget exceeds the need, reduce agents
- Always justify any deviation from the guidelines

### Spawn Depth Rules
- **Default**: Leader → Specialists
- **Complex development**: Leader → Builder Lead → Builders
- **Maximum depth**: 3 levels from leader
- **Justification required** for any deeper hierarchy

## Budget Verification

Before spawning agents:
- Confirm task size category
- Check if sufficient agents already exist
- Verify no duplicate roles
- Confirm ownership is clearly assigned
- Check that the budget matches the dependency graph