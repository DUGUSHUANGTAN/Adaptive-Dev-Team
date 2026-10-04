# Delegation Contract

## Core Principles

### Minimum Sufficient Team
- Delegate only necessary work to specific roles
- Keep delegation focused and scoped
- Avoid over-delegation that dilutes ownership

### Dynamic Composition
- Match the delegate role to the task requirements
- Scale delegation to parallel work needs
- Maintain clear accountability lines

### Context Model
- Determine the host context model before delegating (see `policies/context-management.md`)
- **Unknown context model → delegate as Isolated**: pass every required field explicitly
- On a Shared Context Host, references to shared context are allowed but visibility must be guaranteed

## Delegation Contract Fields

Every delegation uses these fields. No field may be silently omitted; write "N/A" plus a reason when a field genuinely does not apply.

| Field | Content |
|---|---|
| **ROLE** | Role file from `roles/` or `builders/` (e.g. `roles/builder.md`, `builders/frontend.md`). Never an invented title. |
| **OBJECTIVE** | Brief, actionable statement of what this delegate must achieve |
| **WHY THIS TASK EXISTS** | Business need, technical requirement, or constraint that created this task |
| **RELEVANT GLOBAL CONSTRAINTS** | Hard limits, safety constraints, critical user requirements, frozen decisions |
| **INPUTS** | Required information, artifacts, and prior outputs the delegate needs |
| **OWNERSHIP** | What this delegate owns and is accountable for |
| **MAY READ** | Files, modules, or systems the delegate may read but not modify |
| **MUST NOT MODIFY** | Files, systems, or components that must not be changed |
| **DEPENDENCIES** | Prerequisites that must be complete before this delegation starts |
| **SHARED INTERFACES** | Contracts/APIs this work consumes or produces and who else depends on them |
| **REQUIREMENTS** | Technical and non-technical requirements for completion |
| **COMPLETION CONDITIONS** | Measurable conditions that define successful completion |
| **EXPECTED OUTPUT** | Deliverable format, location, and content |
| **REPORT FORMAT** | Reporting format (default: `templates/handoff-report.md`) |

OWNERSHIP / MAY READ / MUST NOT MODIFY / SHARED INTERFACES follow the declaration format in `protocols/ownership.md`.

## Delegation Types

### Single Task Delegation
- One role, one objective
- Clear completion criteria
- Direct handoff path

### Parallel Delegation
- Multiple roles, coordinated objectives
- Disjoint write scopes (see `protocols/parallelization.md`)
- Integration planning before kickoff

### Chain Delegation
- Sequential handoffs between roles
- Each delegate builds on previous work
- Clear transition points and dependencies

## Delegation Decision Matrix

Roles are defined once, in the role files. The matrix maps task type → role file; it does not redefine them.

| Task Type | Role File | Parallel Potential |
|---|---|---|
| Simple Bug Fix | `roles/builder.md` + domain builder from `builders/` | None |
| UI Component | `builders/frontend.md` | Medium |
| Database Migration | `builders/database.md` | Low |
| API Development | `builders/backend.md` or `builders/api-integration.md` | Medium |
| Architecture Design | `roles/architect.md` | None |
| Research Project | `roles/researcher.md` | High |
| Performance Tuning | domain builder from `builders/` + `specialists/performance.md` (if risk-triggered) | Medium |

## Role References

Role identities are defined once, not in this protocol:
- **Coordination / review / decision roles**: `roles/leader.md`, `roles/planner.md`, `roles/builder-lead.md`, `roles/architect.md`, `roles/integration-engineer.md`, `roles/code-reviewer.md`, `roles/qa-engineer.md`, `roles/acceptance-reviewer.md`, and the upstream roles
- **Execution roles**: `builders/frontend.md`, `builders/backend.md`, `builders/fullstack.md`, `builders/database.md`, and the other domain builders in `builders/`
- **Risk-triggered expert review**: `specialists/security.md`, `specialists/performance.md`, etc. — added only when a trigger in `policies/quality-gates.md` applies, never as a mandatory step for all verification

QA Engineer is defined in `roles/qa-engineer.md`; the Architect in `roles/architect.md`. Do not re-classify them here.

## Delegation Best Practices

### Pre-Delegation Checklist
- [ ] Task scope is clearly defined
- [ ] Host context model determined; required context fields resolved
- [ ] All dependencies identified and ready
- [ ] Acceptance criteria agreed upon
- [ ] Integration points mapped
- [ ] Escalation path defined (see `protocols/escalation.md`)

### During Delegation
- [ ] Maintain regular communication
- [ ] Track progress against completion conditions
- [ ] Validate work meets standards
- [ ] Adjust scope if needed

### Post-Delegation
- [ ] Review deliverables against completion conditions
- [ ] Conduct integration testing where applicable
- [ ] Hand off per `protocols/handoff.md`
- [ ] Archive delegation records
