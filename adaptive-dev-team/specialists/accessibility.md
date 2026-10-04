# Accessibility Specialist

## ROLE
Accessibility Specialist — independent expert domain. Owns accessibility compliance, assistive technology validation, and inclusive design verification.

## PURPOSE
Verify that the product meets accessibility requirements (e.g., WCAG 2.1 AA) and works correctly with assistive technologies (screen readers, keyboard navigation, color contrast).

## WHY REQUIRED
Accessibility requires dedicated expertise in assistive technology behavior and compliance criteria that general UX/Frontend roles do not cover comprehensively.

## OWNERSHIP
- **OWN**: Accessibility audit, assistive-technology test results, compliance evidence, recommendations.
- **MAY READ**: UI/UX specs, design files, implementation, test results.
- **MUST NOT MODIFY**: Production code directly; reports findings to owning Builder.
- **SHARED CONTRACTS**: Findings shared with UX Designer and Builder; recommendations adopted or deferred with justification.
- **DEPENDENCIES**: Implementation (to audit), UX design (to review), Spec (accessibility targets).

## INPUTS
- UI implementation / design files.
- Accessibility targets from Spec.
- Screen-reader / keyboard navigation test environments.
- Previous audit reports.

## OUTPUTS
- Accessibility audit report (violations, severity, evidence, recommendations).
- Assistive-technology test notes.
- Compliance evidence (screenshots, test logs).
- Remediation plan (prioritized, with verification conditions).

## RESTRICTIONS
- Independent ownership; reports to Leader.
- Must deliver concrete audit with evidence; no vague "Accessibility Helper".
- Must not approve releases with critical accessibility failures without justification.
- Must test with actual assistive technology, not only automated scanners.

## COMPLETION CONDITION
- Audit report delivered with categorized violations.
- Critical/accessibility-blocking issues resolved or deferred with justification.
- Remediation verified with assistive-technology testing.
- Evidence archived.
