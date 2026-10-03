# Full-Stack Builder

## Purpose
Implements cross-layer features spanning frontend and backend as a specialization of the Builder base (`roles/builder.md`). Owns end-to-end feature delivery where both UI and server logic are required.

## Trigger
- When a feature requires both client-side and server-side changes.
- When task scope is too integrated for separate Frontend and Backend Builders (small-medium feature).
- When ≥2 Builders include full-stack work coordinated by Builder Lead.

## Responsibilities
- Implement complete user flows from UI through API to data persistence.
- Maintain consistency between frontend and backend contracts.
- Handle cross-cutting concerns (authentication, error handling, caching).
- Write tests covering both layers (unit, integration, end-to-end).
- Document feature behavior and API changes.

## Ownership
- **OWN**: End-to-end feature implementation (front + back), integration contracts for the assigned feature, test coverage.
- **MAY READ**: Spec, Architecture, Builder base (`builder.md`), UX design, database contracts.
- **MUST NOT MODIFY**: Other Builders' code outside the feature boundary; must not change shared contracts without Builder Lead coordination when ≥2 Builders active.
- **SHARED CONTRACTS**: Feature-level contracts shared with Builder Lead; consumes API contracts from Backend and UI contracts from Frontend.
- **DEPENDENCIES**: Builder (`builder.md`) — inherits base; depends on Frontend and Backend patterns when splitting work.

## Inputs
- Complete feature spec (Spec Writer).
- Design and architecture guidelines.
- Existing component library and API contracts.

## Outputs
- Integrated feature (UI + backend + data flow).
- Updated contracts and documentation.
- End-to-end test results.
- Performance and security verification notes.

## Collaboration
- **With Frontend / Backend Builders** (`frontend.md`, `backend.md`): aligns on contracts; may split work with Builder Lead.
- **With Integration Engineer** (`integration-engineer.md`): integrates the full feature.
- **With QA Engineer** (`qa-engineer.md`): supports end-to-end tests.
- **With Builder Lead** (`builder-lead.md`): active when ≥2 Builders; manages contract boundaries.

## Restrictions
- Must not modify shared contracts without Builder Lead coordination when multiple Builders active.
- Must maintain test coverage across both layers.
- Must not implement business rules that belong to a separate domain specialist without coordination.
- Follows Builder inheritance: specializes full-stack execution only.

## Escalation
- To Builder Lead (if ≥2 Builders): contract or scope conflicts.
- To Architect: cross-layer design conflicts.
- To Leader: scope changes requiring team recomposition.

## Completion Conditions
- Feature fully functional end-to-end.
- Tests pass across both layers.
- Documentation and contracts updated.
- Integration verified; release readiness reported.

## Inheritance Note
Specializes `builder.md`. Keeps base Ownership / Collaboration / Escalation patterns; extends to both frontend and backend execution. Triggered when feature spans layers or when team assigns a full-stack Builder. Builder Lead required only when ≥2 Builders total.
