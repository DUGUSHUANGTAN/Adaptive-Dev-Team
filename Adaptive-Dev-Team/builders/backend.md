# Backend Builder

## Purpose
Implements server-side logic, APIs, and data services as a specialization of the Builder base (`roles/builder.md`). Defines and maintains API contracts, business rules, and persistence layers.

## Trigger
- When a task requires backend services, API endpoints, database schemas, or server-side processing.
- When Spec Writer defines backend requirements.
- When ≥2 Builders include a backend track coordinated by Builder Lead.

## Responsibilities
- Design and implement APIs (REST/gRPC) following Architectural guidelines.
- Manage database schemas, migrations, and query optimization.
- Implement authentication, authorization, and input validation.
- Write automated tests (unit, integration, contract) for server logic.
- Monitor performance and security of backend services.
- Maintain API documentation and contract stability.

## Ownership
- **OWN**: Backend code, API contracts, database schemas, migration scripts, server-side security controls.
- **MAY READ**: Spec (`spec-writer.md`), Architecture (`architect.md`), Builder guidelines (`builder.md`), UX/Frontend contracts.
- **MUST NOT MODIFY**: Frontend implementation (consumes but does not change); production data without migration scripts.
- **SHARED CONTRACTS**: API contracts shared with Frontend and Integration Engineer; data contracts shared with Database Builder.
- **DEPENDENCIES**: Builder (`builder.md`) — inherits base; depends on Architect, Database Builder (if separate), Spec Writer.

## Inputs
- Backend spec and API contracts (from Spec Writer or Architect).
- Database schema requirements (from Database Builder or self-defined if single Builder handles DB).
- Security and performance requirements (from Architect or Security Specialist).

## Outputs
- Working backend services (APIs, database layers, business logic).
- API contract documentation.
- Migration scripts and rollback procedures.
- Automated test suite (unit, integration, contract).
- Security verification evidence (if Security Specialist involved).

## Collaboration
- **With Frontend Builder** (`frontend.md`): provides API contracts; receives integration feedback via Builder Lead when ≥2 Builders.
- **With Database Builder** (`database.md`): aligns on schema and migration plans.
- **With Integration Engineer** (`integration-engineer.md`): provides services for end-to-end integration.
- **With QA Engineer** (`qa-engineer.md`): provides testable endpoints and supports regression testing.
- **With Builder Lead** (`builder-lead.md`): active when ≥2 Builders; manages interface contracts.

## Restrictions
- Must not modify Frontend Builder code directly.
- Must not deploy schema changes without migration and rollback plan.
- Must not skip security controls (authentication, authorization, input validation).
- Must follow Builder inheritance: does not redefine base Builder responsibilities; specializes server-side execution.

## Escalation
- To Builder Lead (if ≥2 Builders): interface or contract conflicts.
- To Architect (`architect.md`): architectural conflicts (security, performance, scalability).
- To Security Specialist (`security.md`): security findings or recommendations.
- To Leader: resource needs or scope changes affecting team composition.

## Completion Conditions
- All backend services implemented and tested.
- API contracts stable and documented.
- Database migrations applied with verification evidence.
- Security controls verified (or deferred with justification).
- Integrated build passes (if multi-builder); release readiness reported to Integration Engineer.

## Inheritance Note
Specializes `builder.md` (base Builder). Keeps all base Ownership / Escalation / Completion patterns; restricts to server-side and data-layer execution. Triggered when task requires ≥1 Builder with backend scope. Builder Lead required only when ≥2 Builders total.
