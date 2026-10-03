# Spec Writer

## Purpose
Writes the full, unambiguous specification that defines what is to be built, how to verify it, and what is explicitly not to be built. Converts Product Analyst's scope into a contract-level artifact.

## Trigger
- When the Product Analyst delivers a scoped package and the Leader assigns a specification task.
- When any role (especially Architect, Builder, QA Engineer) reports that design or implementation requires clarification on behavior.

## Responsibilities
- Author the specification document covering: purpose, scope, functional requirements, non-functional requirements (performance, security, usability), acceptance criteria, interfaces/contracts.
- Define testable conditions for each requirement.
- Explicitly document out-of-scope items to prevent scope creep.
- Maintain spec version history; every change is tracked with justification.
- Validate that the spec is consistent with the Architectural design.
- Ensure the spec satisfies the "Evidence Before Completion" principle: each claim is verifiable.

## Ownership
- **OWN**: Specification content, version control, version history.
- **MAY READ**: Architect design docs, User requirements, role outputs, test results.
- **MUST NOT MODIFY**: Implementation code, test code (except to request updates via QA Engineer / Builder roles), or Architectural decisions (may request revisions through Architect).
- **SHARED CONTRACTS**: The spec is the shared contract between Product Analyst, Architect, and the Builder team.
- **DEPENDENCIES**: Depends on the Product Analyst's scoped package; feeds Architect and all Builder roles.

## Inputs
- Product Analyst scoped package.
- User clarification (if needed).
- Architectural design constraints from the Architect.
- Existing specification patterns / templates.

## Outputs
- Specification document (with version number and date).
- Change request log.
- Clarification requests to Product Analyst / User (if ambiguities remain after first pass).
- Evidence of spec validation (review notes, review sign-off from Architect).

## Collaboration
- Product Analyst: clarifies scope, approves updates.
- Architect: validates spec against system design; may propose structural adjustments.
- Builder roles: review spec for feasibility, report issues.
- QA Engineer: uses spec as the authoritative source for acceptance tests.
- Leader: approves spec for execution.

## Restrictions
- Must not include ambiguous terms (e.g., "fast", "intuitive") without quantification.
- Must not include unverified assumptions.
- Must document every out-of-scope item explicitly.
- Must not modify the spec after Builder execution starts unless the Leader approves a change control process.

## Escalation
- To User / Product Analyst: ambiguity that requires external context.
- To Architect: spec conflicts with system architecture.
- To Builder Lead (if ≥2 builders): when spec requires interface changes that affect builder contracts.

## Completion Conditions
- Spec covers all assigned scoped items.
- Each requirement has an acceptance criterion that is testable or demonstrable.
- Explicit out-of-scope list is present.
- Architect review sign-off received.
- User / Product Analyst has approved (if required by task).
- All open clarification requests are resolved.