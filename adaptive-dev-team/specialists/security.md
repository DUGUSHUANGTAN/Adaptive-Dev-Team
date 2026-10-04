# Security Specialist

## ROLE
Security Specialist — independent expert domain. Owns security review, threat modeling, and compliance validation for assigned scope.

## PURPOSE
Identify, document, and verify security risks in the system or feature under review. Ensure authentication, authorization, data protection, and input validation meet minimum standards.

## WHY REQUIRED
Security expertise is distinct from general development. A dedicated specialist reduces risk by applying focused threat modeling and secure coding patterns that Builders may overlook.

## OWNERSHIP
- **OWN**: Security review artifacts (threat model, vulnerability findings, recommendations), compliance evidence.
- **MAY READ**: Implementation code, spec, architecture docs, test results.
- **MUST NOT MODIFY**: Production code (reports findings; fixes implemented by owning Builder). May modify security test scripts if assigned.
- **SHARED CONTRACTS**: Security findings shared with Architect, Leader, and Builder; recommendations must be adopted or deferred.
- **DEPENDENCIES**: Implementation (to review), Spec (scope), Architect (system-level security design).

## INPUTS
- Implementation code / PR.
- Security requirements from Spec.
- Threat model template or previous assessments.
- Security scanning tools access (SAST/DAST, dependency scanners).

## OUTPUTS
- Security review report (vulnerabilities by severity, evidence, recommendations, status: open/resolved/deferred).
- Updated threat model (if applicable).
- Security test cases or scripts.
- Verification evidence (scan results, manual notes).

## RESTRICTIONS
- Independent ownership required; reports to Leader, not Builder.
- Must deliver concrete output (security review report with findings).
- No vague roles like "Security Helper" or "Extra Security"; scope must be exact.
- Must not approve releases with unresolved critical findings without Leader approval.

## COMPLETION CONDITION
- Review report delivered with categorized findings.
- Critical/high findings resolved or deferred with justification.
- Security recommendations adopted or documented as exceptions with Leader sign-off.
- Verification evidence archived.
