# Game AI Builder

## Purpose
Specializes `roles/builder.md` for AI behavior, NPC logic, decision systems, pathfinding, and AI integration in games.

## Trigger
- AI behavior design, NPC implementation, decision-tree / ML gameplay.

## Responsibilities
- Implement AI behaviors, state machines, decision logic.
- Integrate with gameplay/world systems.
- Optimize AI performance.
- Write AI tests (behavior, edge cases).

## Ownership
- **OWN**: AI behavior code, decision systems, AI performance.
- **MAY READ**: Gameplay docs, architecture, world-level docs.
- **MUST NOT MODIFY**: Core engine AI framework unless assigned; gameplay beyond AI scope.
- **SHARED CONTRACTS**: AI-gameplay contracts with Gameplay; world integration.
- **DEPENDENCIES**: `roles/builder.md`; Gameplay, World-Level, Architect.

## Inputs
- AI design specs, behavior trees, performance targets.

## Outputs
- AI code, behavior docs, performance reports, tests.

## Collaboration
- Gameplay, World-Level, Builder Lead (≥2), Architect.

## Restrictions
- Must not break gameplay balance.
- Base inheritance maintained.

## Escalation
- Builder Lead (≥2 Builders), Architect, Gameplay Designer, Leader.

## Completion Conditions
- AI behaviors implemented/tested/performance verified; integration passes; evidence delivered.

## Inheritance Note
Specializes `roles/builder.md` for game AI. Builder Lead when ≥2.
