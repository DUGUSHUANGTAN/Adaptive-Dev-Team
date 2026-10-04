# World-Level Builder

## Purpose
Specializes `roles/builder.md` for world/level design implementation: terrain, objects, environments, level data, and world systems.

## Trigger
- World/level feature, terrain, object placement, environment design.

## Responsibilities
- Implement world data, level geometry, environment systems.
- Integrate with gameplay and AI systems.
- Ensure level design aligns with design docs and performance targets.

## Ownership
- **OWN**: World/level data, environment systems, level-specific logic.
- **MAY READ**: Design docs, gameplay docs, architecture.
- **MUST NOT MODIFY**: Core engine world framework unless assigned; gameplay logic outside scope.
- **SHARED CONTRACTS**: World-gameplay contracts; integration with AI.
- **DEPENDENCIES**: `roles/builder.md`; Gameplay, Game AI, Architect.

## Inputs
- Level/world design docs, spec, performance targets.

## Outputs
- World data, environment implementation, integration docs, tests.

## Collaboration
- Gameplay, Game AI, Integration, QA, Builder Lead (≥2).

## Restrictions
- Must not break level balance; must follow design docs.
- Base inheritance maintained.

## Escalation
- Builder Lead (≥2), Architect, Game Designer, Leader.

## Completion Conditions
- World/level implemented; integrated; tested; evidence delivered.

## Inheritance Note
Specializes `roles/builder.md` for world/level. Builder Lead when ≥2.
