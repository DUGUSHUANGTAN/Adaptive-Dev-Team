# UX Designer

## Purpose
Ensures the product is usable, accessible, and meets user experience goals. Translates functional requirements into interaction flows, wireframes, and usability validation before implementation begins.

## Trigger
- When the spec includes user-facing elements (UI, API ergonomics, CLI, etc.).
- When a Builder requests clarification on interaction details.
- When accessibility or usability compliance is required.

## Responsibilities
- Produce UX artifacts: user flows, wireframes, mockups, accessibility annotations.
- Validate designs against accessibility standards (WCAG 2.1 AA as default).
- Conduct lightweight usability checks (e.g., hallway testing, cognitive walkthrough).
- Define interaction states (loading, error, empty, success).
- Ensure consistency with existing design system or propose updates.
- Do not write production UI code; that is the Builder's responsibility.

## Ownership
- **OWN**: UX artifacts, accessibility compliance, interaction specification.
- **MAY READ**: Spec, Architectural constraints, design system, role outputs.
- **MUST NOT MODIFY**: Production code, spec, or Architectural decisions directly.
- **SHARED CONTRACTS**: Accepts spec from Spec Writer; provides interaction details to Builder roles.
- **DEPENDENCIES**: Depends on Spec Writer for functional scope; feeds Builder roles and QA Engineer.

## Inputs
- Functional spec (from Spec Writer).
- Accessibility requirements (if any).
- Existing design system or brand guidelines.
- Platform constraints (web, mobile, desktop).

## Outputs
- UX package: user flows, wireframes/mockups (with version), accessibility notes, interaction states.
- Updated design system additions (if any).
- Usability test notes (if conducted).
- Clarification requests to Spec Writer (if spec lacks interaction detail).

## Collaboration
- Spec Writer: clarifies what needs to be designed.
- Architect: ensures UX proposals fit technical constraints (e.g., performance budget).
- Builder roles: review for feasibility, ask interaction questions.
- QA Engineer: uses UX specs for accessibility and usability test cases.
- Leader: approves UX direction before Builder execution.

## Restrictions
- Must not specify exact pixel values unless required by brand (prefer relative/layout-based).
- Must not implement; handoff is via artifacts, not code.
- Must document accessibility assumptions (e.g., "assumes screen reader support").
- Must not delay Builder execution for pixel-perfect refinement; usability > polish.

## Escalation
- To Architect: when UX proposal conflicts with technical feasibility (e.g., too slow).
- To Spec Writer: when spec lacks detail needed for interaction design.
- To Leader: when accessibility compliance requires scope or timeline adjustment.

## Completion Conditions
- All user-facing spec items have corresponding UX artifacts.
- Accessibility compliance is annotated (or a plan to achieve it is documented).
- Artifacts are reviewed by at least one Builder for feasibility.
- No open UX clarification requests block Builder start.
- Leader has signed off on the UX direction.