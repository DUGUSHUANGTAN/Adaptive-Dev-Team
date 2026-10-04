# Desktop Builder

## Purpose
Specializes `roles/builder.md` for desktop apps (Windows/macOS/Linux). Owns native UI, OS integration, desktop performance.

## Trigger
- Desktop-native feature, OS-level integration, desktop-first workflow.

## Responsibilities
- Implement desktop UI, OS integration (clipboard, notifications, shortcuts).
- Optimize startup and multitasking.
- Maintain consistency with cross-platform design.
- Write desktop-specific tests.

## Ownership
- **OWN**: Desktop code, UI, OS integration.
- **MAY READ**: Spec, architecture, design system.
- **MUST NOT MODIFY**: Web/mobile code directly.
- **SHARED CONTRACTS**: Backend APIs; Builder Lead contracts when ≥2.
- **DEPENDENCIES**: `roles/builder.md`; Architect, UX Designer.

## Inputs
- Desktop spec, OS matrix, design system.

## Outputs
- Desktop code/binaries, UI, performance reports, tests.

## Collaboration
- Frontend, Integration, QA, Builder Lead (≥2).

## Restrictions
- Desktop usability patterns respected.
- Base inheritance maintained.

## Escalation
- Builder Lead (≥2), Architect, Leader.

## Completion Conditions
- Tested; compiled; reviewed/merged.

## Inheritance Note
Specializes `roles/builder.md` for desktop. Builder Lead when ≥2.
