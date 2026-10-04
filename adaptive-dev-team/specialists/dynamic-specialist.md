# Dynamic Specialist

## ROLE
Dynamic Specialist — task-level created expert with defined scope. Created only when an existing specialist or builder role cannot cover the task's unique expertise requirement.

## PURPOSE
Enable the team to compose experts dynamically for tasks requiring a non-standard domain (e.g., a specific physics simulation, a custom hardware interface, a niche regulatory framework) without creating permanent roles.

## WHY REQUIRED
Projects encounter unpredictable expertise needs. Creating a permanent specialist for a one-time need violates Minimum Sufficient Team. Dynamic creation allows precise, temporary expertise injection with explicit contract.

## OWNERSHIP
- **OWN**: The specific expert domain assigned by the Leader; delivers the defined output for the task; has independent ownership of the expert review / deliverable.
- **MAY READ**: Implementation, spec, architecture, related role outputs.
- **MUST NOT MODIFY**: Implementation code (unless explicitly assigned as a spike with delivery plan); must define its own ownership boundary.
- **SHARED CONTRACTS**: The Dynamic Specialist's deliverable is a shared contract with the requesting role and Leader; must include explicit scope boundary.
- **DEPENDENCIES**: The task requiring the expertise (from Leader); implementation to review; spec for scope.

## INPUTS
- Task description from Leader defining the exact expertise needed.
- Implementation / design artifacts to review or inform.
- Spec / requirements for context.
- Access to specialized resources (tools, references, experts outside team).

## OUTPUTS
- Concrete, verifiable deliverable (not a report of "I looked at it"). Examples: validated model, benchmark result, design recommendation, compliance evidence, domain audit.
- Scope-definition document (what was reviewed / solved, what was excluded).
- Recommendation or verification evidence with reproducible conditions.

## RESTRICTIONS — DYNAMIC CREATION RULES
- **Independent domain required**: Must define a distinct, independent expertise area (e.g., "PCA9685 calibration", "custom shader graph validation"). No overlap with existing roles unless explicitly justified.
- **Independent ownership required**: The Dynamic Specialist owns its deliverable; does not report to or modify code owned by another Builder without coordination.
- **Concrete deliverable required**: Must produce something verifiable (evidence, number, recommendation with justification). No vague outputs like "Feedback provided" or "Looked at code".
- **No vague roles allowed**: Prohibited names / descriptions include: Helper, Extra Developer, Support, Assistant, Generalist, Extra Pair of Hands, Bonus Expert, Second Opinion (without defined scope). Every Dynamic Specialist must have a role name that reflects the exact domain (e.g., "Physics Sim Validation Specialist", "Custom Hardware Interface Reviewer").
- **Time-bound by default**: Created for the task; if the task ends, the role ends unless the Leader extends with new justification.
- **Must be defined explicitly by the Leader**: Before creation, the Leader must document: ROLE, PURPOSE, WHY REQUIRED, OWNERSHIP, INPUTS, OUTPUTS, DEPENDENCIES, RESTRICTIONS, COMPLETION CONDITION. No implicit or ambiguous creation.

## DEPENDENCIES
- Leader (creates role with explicit contract).
- Requesting role (defines need; validates output).
- Implementation / design artifacts (to review or inform).

## COMPLETION CONDITION
- Concrete, verifiable deliverable produced and delivered to requesting role.
- Scope explicitly documented (what was included / excluded).
- Evidence reproducible or archived.
- No vague output; if no concrete finding is needed, the role should not have been created.
- Role ends when deliverable is accepted or explicitly deferred with justification.
