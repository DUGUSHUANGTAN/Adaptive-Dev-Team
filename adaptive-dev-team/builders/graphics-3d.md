# Graphics / 3D Builder

## Purpose
Specializes `roles/builder.md` for 3D graphics, rendering, shaders, visual assets.

## Trigger
- 3D asset, shader, visual effect, rendering feature.

## Responsibilities
- Implement 3D assets, materials, shaders, effects.
- Optimize rendering (draw calls, GPU, LOD).
- Match visual design targets.
- Maintain asset pipeline.

## Ownership
- **OWN**: Graphics assets, shaders, visual implementation.
- **MAY READ**: Design docs, architecture.
- **MUST NOT MODIFY**: Game logic, backend contracts outside scope.
- **SHARED CONTRACTS**: Graphics-world contracts; Builder Lead when ≥2.
- **DEPENDENCIES**: `roles/builder.md`; World-Level, Gameplay, Architect.

## Inputs
- Asset specs, design targets.

## Outputs
- Assets/shaders, docs, performance reports, tests.

## Collaboration
- World-Level, Gameplay, Integration, QA, Builder Lead (≥2 Builders).

## Restrictions
- Must not degrade performance.
- Base inheritance maintained.

## Escalation
- Builder Lead (≥2 Builders), Architect, Leader.

## Completion Conditions
- Assets implemented; performance verified; integrated; evidence delivered.

## Inheritance Note
Specializes `roles/builder.md` for graphics. Builder Lead when ≥2.
