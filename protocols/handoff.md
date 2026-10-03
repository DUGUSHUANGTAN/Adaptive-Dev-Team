---
title: Handoff Protocol
description: "Every completion requires a structured handoff report including status, changes, interfaces, decisions, and risks."
version: "1.0"
status: active
---

# Handoff Protocol

When an agent completes work (or reaches a milestone), they must provide a structured handoff report. This ensures continuity, transparency, and proper integration with subsequent work.

## Handoff Report Format

Every handoff must include:

### STATUS
One of the following:
- **COMPLETE**: All work completed successfully
- **PARTIAL**: Some work completed, some remains
- **BLOCKED**: Work blocked by external factors
- **FAILED**: Work could not be completed

### SUMMARY
A brief summary of what was accomplished, what was not accomplished, and why.

### CHANGES
All changes made during work:
- Files modified
- Code changes
- Configuration changes
- Documentation updates
- Any other changes

### FILES/MODULES
Specific files or modules that were affected:
- List of files changed
- List of modules affected
- List of components updated

### INTERFACES
Any interfaces that were affected or created:
- API changes
- Contract updates
- Interface specifications
- Any changes to external interfaces

### DECISIONS
Important decisions made during work:
- Design decisions
- Approach decisions
- Trade-off decisions
- Any significant choices

### VERIFICATION
How the work was verified:
- Tests completed
- Review completed
- Validation performed
- Quality checks passed

### KNOWN ISSUES
Any issues or concerns:
- Bugs found but not fixed
- Technical debt created
- Performance concerns
- Security concerns
- Any other issues

### RISKS
Any risks identified:
- Potential problems
- Future issues
- Dependency risks
- Technical risks

### FOLLOW-UP
What needs to happen next:
- Follow-up tasks
- Additional work needed
- Integration required
- Verification needed

### HANDOFF TO
Who receives the handoff:
- Next agent
- Integration agent
- Review team
- Stakeholders
- Any other recipient

## Handoff Rules

- Every agent must provide a handoff when work completes or reaches a milestone
- Handoff reports must include all sections listed above
- Handoff reports must be shared with all relevant team members
- Handoff reports must be referenced in subsequent tasks
- Incomplete handoffs must be followed up
