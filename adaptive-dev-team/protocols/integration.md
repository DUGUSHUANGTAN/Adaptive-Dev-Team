# Integration Protocol

TRIGGER: ≥2 Builders, parallel waves, or multi-module changes that touch shared interfaces. Single-Builder light tasks skip this protocol; the Builder's own checks are sufficient.

OWNER: Integration Engineer (`roles/integration-engineer.md`) when the trigger applies.

## Order

1. Confirm all upstream Internal Handoffs are received (`protocols/handoff.md`) and dependencies are complete.
2. Freeze / verify the shared interfaces and contracts.
3. Merge or wire the modules together.
4. Run cross-module checks: build, integration tests, contract checks.
5. Emit the integration report (`templates/integration-report.md`).
6. Proceed to Verification / Review (`protocols/handoff.md` order).

RULE: the Integration Owner does **not** refactor Builder work at will. Internal problems in a module return to its Original Owner first.

COMPLETION: build passes + cross-module checks pass + no unresolved interface mismatch + integration report emitted.

## Failure / Conflict Fallback

- Internal bug in one module → return to Original Owner (`protocols/fix-loop.md`).
- Interface disagreement → Interface Conflict in `protocols/conflict-resolution.md`.
- Blocked dependency or breaking change → `protocols/escalation.md`.
