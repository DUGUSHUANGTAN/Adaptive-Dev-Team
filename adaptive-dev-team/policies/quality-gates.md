# Quality Gates Policy

## Core Principle: Evidence-Based Quality Assurance

Quality gates are triggered based on evidence of work impact, not on arbitrary rules. Each gate has clear triggers and requirements.

## QA Engineer Trigger Conditions

### Meaningful Feature
- New feature implementation
- Significant enhancement
- Any code with meaningful business impact

### Bug Fix with Regression Risk
- Bug fixes that modify core functionality
- Changes to previously stable code
- Any fix affecting multiple components

### Integration
- Any integration work (APIs, services, databases)
- Multi-component interactions
- Cross-system dependencies

### Medium+ Change
- Changes affecting 2+ files
- Changes touching core modules
- Changes affecting shared services

### User-Facing Behavior
- UI/UX changes
- API endpoint changes
- Any change affecting end-user experience

## Code Reviewer Checklist

### Correctness
- Functional requirements met
- Edge cases handled
- Error conditions addressed

### Maintainability
- Clear structure and organization
- Appropriate abstractions
- Avoidance of complexity smells

### Readability
- Meaningful names and variables
- Logical flow
- Comments where needed

### Architecture Compliance
- Follows approved patterns
- No anti-patterns
- Proper separation of concerns

### Duplication
- No code duplication
- Shared logic through proper channels

### Dead Code
- No unused code
- No commented-out code in production
- Remove obsolete features

### Error Handling
- Comprehensive error handling
- Graceful degradation
- Clear error messages

### Unexpected Side Effects
- No unintended consequences
- No performance degradation
- No security vulnerabilities

### Technical Debt
- Debt is tracked and managed
- No new debt introduced without justification
- Debt reduction is a priority

## Acceptance Reviewer Trigger Conditions

### Large Feature
- Major new functionality
- System-wide changes
- Significant architectural shifts

### Greenfield Development
- New system or major subsystem
- First implementation of a core concept

### Production Impact
- Changes affecting production systems
- High-impact user-facing changes
- Critical system modifications

### Complex Requirements
- Requirements with many interdependencies
- Requirements with novel technical challenges
- Requirements with high business complexity

## Specialist Gate Triggers (only when fired)

A Specialist gate is **not** part of every task. It exists only when its trigger fires:

- **Security Specialist**: auth, authorization, session handling, secrets, external input, network boundary, dependency or supply-chain change.
- **Performance Specialist**: a quantified performance target exists, or a regression is suspected.
- **Accessibility Specialist**: user-facing UI change.
- **Privacy & Compliance Specialist**: personal data is collected, stored, transferred, or deleted.
- **Migration Specialist**: schema, data, or platform migration.
- **SRE / DevOps Specialist**: production deployment, release readiness, monitoring change.
- **Domain Expert**: domain-specific rules or terminology are involved.

If the trigger does not fire, the Specialist does not join and is not a completion blocker. Specialists are not generic reviewers: QA, Code Reviewer, and Acceptance Reviewer are base Roles (`roles/`) that run at the depth the selected workflow requires — see `workflows/core.md`.

## Verification Process

### From Original Request
- Cross-reference all requirements
- Verify all acceptance criteria are addressed
- Check for scope creep

### From Specification
- Verify implementation matches spec
- Check for deviations or omissions
- Ensure all edge cases are covered

### From Acceptance Criteria
- Direct verification against criteria
- Automated tests where applicable
- Manual verification for complex scenarios

## Gate Completion

### Definition of Ready
- All requirements understood
- All dependencies identified
- All relevant context available
- Acceptance criteria defined
- The workflow and its required stage depth are selected (`workflows/core.md`)

### Definition of Done
Completion depth is **dynamic** and defined by `policies/definition-of-done.md`. Do not apply the production checklist to a light task:

- **Light**: requested change implemented + targeted check + no obvious regression.
- **Standard**: requirements implemented + appropriate QA/review + known issues reported.
- **Advanced**: integration complete + QA + review + acceptance when required.
- **Production**: the above plus only the triggered Specialist gates and release readiness.

No claim of "done" without evidence at the selected depth. A gate that was never triggered must not be reported as passed or as blocking.
