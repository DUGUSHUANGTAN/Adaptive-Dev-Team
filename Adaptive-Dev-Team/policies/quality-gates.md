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

### Definition of Done
- All acceptance criteria met
- All quality gates passed
- Evidence presented for completion
- Peer review completed
- Testing completed
- Documentation updated
- Code reviewed