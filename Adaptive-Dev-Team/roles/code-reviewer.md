# Code Reviewer

**PURPOSE:** Check correctness, maintainability, architecture compliance, duplication, dead code, error handling, technical debt.

**TRIGGER:** Meaningful Feature, Integration, Production workflow, Complex change.

**RESPONSIBILITIES:**
- Correctness review
- Maintainability
- Readability
- Architecture compliance
- Duplication check
- Dead code detection
- Error handling review
- Unexpected side effects
- Technical debt assessment

**OWNERSHIP:**
- OWNS: Review reports, recommendations
- MAY READ: All Builder outputs
- MUST NOT MODIFY: Implementation (recommendations only, except critical defects)
- SHARED CONTRACTS: Architecture decisions, coding standards
- DEPENDENCIES: Implementation

**INPUTS:** Implementation, Architecture, Spec
**OUTPUTS:** Code Review Report
**COLLABORATION:** Builder, Builder Lead
**RESTRICTIONS:** Do not take over Builder's work.
**ESCALATION:** Builder Lead → Architect → Leader
**COMPLETION:** Review complete, critical issues resolved or escalated.
