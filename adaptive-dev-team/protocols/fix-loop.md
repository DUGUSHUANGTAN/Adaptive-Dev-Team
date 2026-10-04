# Fix Loop Protocol

TRIGGER: QA / Reviewer / Integration detects an issue.

FLOW: Issue detected → classify issue → identify the **Original Owner** → route to the Original Owner → Fix → targeted recheck.

## Routing (do not assume a Builder Lead exists)

- The issue goes to the **Original Owner** — the agent that owns the affected work.
- If a **Builder Lead is active** (defined in `roles/builder-lead.md`: assigned when ≥2 Builders are working in parallel), route through the Builder Lead for coordination.
- If **no Builder Lead is active**, route directly to the Original Owner.
- Missing optional roles are skipped. Never create a Builder Lead (or any role) just to satisfy this flow.

## Reviewer Boundary

- The Reviewer does not rewrite the implementation by default.
- The Reviewer returns the issue with: location, evidence, severity, and the required outcome.
- The Owner decides between fixing and escalating with technical evidence (`protocols/conflict-resolution.md`).

## Recheck

- The recheck is **targeted**: it verifies the specific fix, not a full re-review.
- Recheck evidence is recorded with the issue.

COMPLETION: issue fixed + targeted recheck passed + evidence recorded.
ESCALATE IF: the Owner cannot fix it, or the fix changes a shared interface → `protocols/escalation.md`.
