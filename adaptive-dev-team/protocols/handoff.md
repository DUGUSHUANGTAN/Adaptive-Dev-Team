# Handoff Protocol

Defines the transfer of work between agents and the boundary between internal transfer, acceptance, and delivery.

## Terms (do not conflate)

- **Internal Handoff** — agent → agent, or agent → lead. Means only *the work has been transferred*. It is not acceptance and not delivery.
- **Acceptance** — performed only when the selected workflow requires it. Checks the work against **Original Request + Specification + Acceptance Criteria**. Output: `templates/acceptance-report.md`.
- **Final Delivery** — the deliverable handed to the user. Final Delivery may only happen after required Acceptance has passed.

## Required Order

```
Implementation → Internal Handoff → Integration → Verification / Review → Acceptance (if required) → Final Delivery
```

**FORBIDDEN:** Final Delivery before a required Acceptance. If Acceptance is required by the workflow and has not passed, the work is not delivered.

## Internal Handoff Format

`STATUS (COMPLETE / PARTIAL / BLOCKED / FAILED)` + `SUMMARY` + `CHANGES` + `FILES & MODULES` + `INTERFACES` + `DECISIONS` + `CHECKS PERFORMED` + `KNOWN ISSUES` + `RISKS` + `NEXT OWNER OR NEXT STAGE`.

Template: `templates/handoff-report.md`.

## Completion Condition

A handoff is complete when **the receiver has enough information to continue**.

- No human-style ACK is mandatory.
- If the host supports an ACK, record it; otherwise proceed.
- An absent ACK must never block the flow. The receiver acts on the handoff, or raises a concrete blocker via `protocols/escalation.md`.

TRIGGER: an agent completes its assigned task (or reaches a defined handoff point).
COMPLETION: the handoff report is delivered to the next stage. Route to the Builder Lead only when that role is active (see `roles/builder-lead.md`); otherwise deliver directly to the receiving owner/Leader.
