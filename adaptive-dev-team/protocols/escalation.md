# Escalation Protocol

PATH: escalate to the **nearest valid Authority** — never a hardcoded full chain.

Effective chain: Owner/Builder → Builder Lead (only if active) → Architect / Planner (only if present) → Leader → User (only when the decision exceeds the Leader's authority).

Rules:
- Skip absent roles; escalate to the next present authority.
- Do not fabricate a chain to satisfy a diagram.
- Valid example: with no Builder Lead and no Architect, **Builder → Leader is a legal escalation**.
- A role that is present but irrelevant to the decision is also skipped (e.g. an interface conflict with no Architect present goes to the Leader).

STOP GUESSING — stop and escalate when any of these occur:
- Requirement Conflict
- Architecture Conflict
- Missing Dependency
- Ownership Conflict
- Breaking Change
- Unexpected Scope Expansion
- Security Concern
- Critical uncertainty

ESCALATION CONTENT: the issue, evidence, options considered, and the decision needed.

COMPLETION: escalation resolved with a decision record (`templates/decision-record.md`).
