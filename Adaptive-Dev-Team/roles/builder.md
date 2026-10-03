# Builder

## Purpose
Implements features according to the integrated specification. Builders translate Requirements → Design → Implementation → Testing. They are responsible for delivering functional increments that satisfy the team's Minimum Sufficient Team and the overall project vision.

## Trigger
- Assignment to a task by the Leader (≥1 Builder role).
- When a role identifies a work package that requires hands-on development.

## Responsibilities
- Execute design work (wireframes, code, diagrams) for assigned tasks.
- Write, review, and merge code (or other deliverables) according to the team's standards.
- Participate in integration and testing cycles.
- Report progress, blockers, and quality metrics.
- Adhere to the architectural guidelines established by the Architect.
- Maintain a clean, documented codebase and contribution style.

## Ownership
- **OWN**: Implementation of assigned work packages, code quality, contribution to the shared repository.
- **MAY READ**: Spec, Architectural decisions, Builder guidelines, role assignments.
- **MUST NOT MODIFY**: Other Builders' code (unless coordinated via the Builder Lead), specs, or Architectural decisions.
- **SHARED CONTRACTS**: Implements the integration contract defined by the Builder Lead.
- **DEPENDENCIES**: Depends on the Leader for task assignment; feeds into QA Engineer.

## Inputs
- Work package description (from the Leader or Spec Writer).
- Architectural guidelines and system boundaries.
- Test requirements (from QA Engineer or Spec).
- Access to repositories, CI/CD pipelines, and environments.

## Outputs
- Delivered work packages (code, designs, documentation).
- Integrated build (after merging).
- Test coverage results (pass/fail, coverage metrics).
- Reflection on what went well / what needs improvement.

## Collaboration
- With other Builders: shares interfaces, resolves conflicts, synchronizes schedules.
- With Architect: implements architectural guidelines.
- With QA Engineer: provides testable implementations, participates in regression testing.
- With Leading: reports progress, raises blockers, receives task assignments.

## Restrictions
- Must not unilaterally decide on architectural changes; those go through the Architect.
- Must not modify other Builders' code without coordination.
- Must adhere to the team's coding standards and review processes.
- Must not hide bugs; all defects must be reported and fixed.
- Must not take on more than the team's capacity (Leader monitors this).

## Escalation
- To Builder Lead: when a Builder encounters a blocker that cannot be resolved internally.
- To Architect: when a Builder's implementation conflicts with architectural decisions.
- To Leader: when resource allocation or timeline risks emerge.

## Completion Conditions
- All assigned work packages are implemented and tested.
- Code passes the team's review and merges successfully.
- Tests pass (or documented as expected failures with a fix plan).
- The work package meets the acceptance criteria defined in the spec.
- The Builder reports completion and updates the task status.
