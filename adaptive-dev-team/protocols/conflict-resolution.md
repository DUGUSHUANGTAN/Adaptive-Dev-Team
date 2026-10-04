# Conflict Resolution Protocol

DEFINITION: How conflicting positions are resolved into an evidence-backed decision.
TRIGGER: Two or more agents hold incompatible positions on a requirement, architecture, ownership, interface, or review outcome.

## Conflict Types

| Conflict | Source | Authority | Resolution |
|---|---|---|---|
| **Requirement Conflict** | User requirement vs. accepted Specification | Accepted Spec governs; the Leader is the authority (with Spec Writer / Product Analyst). Only the User can change the requirement. | Update the Spec through `roles/spec-writer.md`; record the change. |
| **Architecture Conflict** | Two implementations/designs diverge from or contradict the architecture | Architect (`roles/architect.md`); unresolved or scope-changing → Leader | Architect issues an ADR (`templates/decision-record.md`); Builders comply. |
| **Ownership Conflict** | Overlapping write scopes or disputed ownership | Builder Lead if active; otherwise Leader (rules in `protocols/ownership.md`) | Assign a single writer or split the boundary; document new boundaries. |
| **Interface Conflict** | Agents disagree on a shared interface/contract | Integration Owner (`roles/integration-engineer.md`) + affected module owners; unresolved → Architect → Leader | Freeze the contract, update both sides, re-run cross-module checks. |
| **Reviewer vs Builder** | Reviewer rejects; Builder disputes | The Authority for the underlying conflict type (Architecture → Architect; Requirement → Leader; Interface → Integration Owner) | See process below. |

## Reviewer vs Builder Process

1. **Reviewer** submits: **Issue** (what is wrong), **Evidence** (reproduction/output), **Severity**, **Required outcome**.
2. **Builder** either:
   - **Fix** — apply the fix and request a targeted recheck (`protocols/fix-loop.md`), or
   - **Escalate with technical evidence** — explain why the review is incorrect, incomplete, or conflicts with a constraint.
3. The **corresponding Authority** decides. The decision is recorded; both parties comply.

## Common Rules

- Every resolution is evidence-backed; claims without evidence do not win.
- Exactly one decision record per conflict (`templates/decision-record.md`).
- No silent override: whoever disagrees must escalate rather than bypass.
- Resolve before resuming parallel execution when the conflict affects shared work.

COMPLETION: a recorded decision plus updated ownership/interface/requirements as applicable.
