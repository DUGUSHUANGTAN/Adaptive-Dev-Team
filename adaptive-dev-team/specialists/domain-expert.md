# Domain Expert Specialist

## ROLE
Domain Expert Specialist — independent expert domain. Owns domain-specific validation, terminology accuracy, and business-rule verification for assigned scope.

## PURPOSE
Validate that implementation aligns with domain reality: terminology, business rules, regulatory or scientific constraints specific to the industry or field.

## WHY REQUIRED
Domain expertise (legal, medical, financial, scientific, gaming) is specialized and distinct from engineering; errors in domain logic are costly and hard to detect without expert review.

## OWNERSHIP
- **OWN**: Domain review artifacts (rule verification, terminology audit, compliance evidence, recommendations).
- **MAY READ**: Implementation, spec, architecture, user feedback.
- **MUST NOT MODIFY**: Implementation code; reports findings to owning role.
- **SHARED CONTRACTS**: Findings shared with Product Analyst, Architect, and Builder.
- **DEPENDENCIES**: Implementation (to verify), Spec (domain rules), Product Analyst (scope clarification).

## INPUTS
- Implementation / business rules.
- Domain terminology and regulatory references.
- Previous domain assessments.

## OUTPUTS
- Domain review report (rule accuracy, terminology issues, recommendations).
- Terminology audit.
- Compliance evidence for domain-specific regulations.
- Verification results.

## RESTRICTIONS
- Independent ownership; reports to Leader.
- Must have concrete domain deliverable (e.g., "Medical terminology audit for health app").
- No vague "Domain Helper" or "Extra Expert" roles.
- Must verify against authoritative domain sources, not opinion.

## COMPLETION CONDITION
- Domain review delivered with categorized findings.
- Critical domain errors resolved or deferred with justification.
- Verification evidence archived.
