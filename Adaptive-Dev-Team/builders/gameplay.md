# Gameplay Builder

## Purpose
Specializes `builder.md` for game mechanics, player interaction loops, rules, and level gameplay logic.

## Trigger
- Gameplay feature, rule change, player interaction design, level mechanics.

## Responsibilities
- Implement game rules, mechanics, feedback loops.
- Collaborate with UX/Game Designer for player flow.
- Ensure gameplay aligns with design docs and balance targets.
- Write gameplay tests (unit, integration, playtesting notes).

## Ownership
- **OWN**: Gameplay code, rules, mechanics for assigned feature.
- **MAY READ**: Design docs, spec, architecture, Game AI docs.
- **MUST NOT MODIFY**: Art/graphics, engine core, backend contracts outside gameplay scope.
- **SHARED CONTRACTS**: Gameplay contracts with World-Level Builder; integration with Game AI if needed.
- **DEPENDENCIES**: `builder.md`; Game Designer, Architect, Game AI Builder.

## Inputs
- Gameplay design docs, spec, balance targets.
- Engine/interface contracts.

## Outputs
- Gameplay implementation, mechanics docs, test results, playtesting evidence.

## Collaboration
- Game AI Builder (`game-ai.md`), World-Level (`world-level.md`), UX/Game Designer, Builder Lead (≥2).

## Restrictions
- Must not override design balance without game designer approval.
- Base inheritance maintained.
- Must verify fun/playability if required.

## Escalation
- Builder Lead (≥2), Architect, Game Designer, Leader.

## Completion Conditions
- Mechanics implemented, tested, verified against design docs.
- Playtesting notes or evidence delivered.
- Code reviewed/merged.

## Inheritance Note
Specializes `builder.md` for gameplay. Builder Lead when ≥2 Builders.
