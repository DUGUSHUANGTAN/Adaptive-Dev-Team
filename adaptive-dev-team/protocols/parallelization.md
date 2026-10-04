# Parallelization Protocol

TRIGGER: deciding whether nodes in the Task DAG (`protocols/task-dag.md`) can run concurrently.

RULE: run in parallel **only** when nodes are independent and their write scopes are disjoint.

## SAFE to Parallelize

- Independent modules
- Independent research
- Independent review
- Frontend / Backend **after** the contract is frozen
- Independent features
- Independent test preparation

## FORBIDDEN — Hard Rules

- **Unfinished dependency**: never parallelize while a dependency is incomplete.
- **Same file**: no two agents writing the same file.
- **Same core module**: no two agents owning the same core module.
- Unresolved architecture, unresolved requirements, or an unstable shared contract.
- Ordered migration (must be sequential).

## Decision

Before launching a wave, confirm for each node:
1. All dependencies are complete.
2. Write scopes are disjoint (`protocols/ownership.md`).

If either check fails, serialize the node instead of parallelizing.

COMPLETION: the wave completed with no ownership or interface conflicts, and results integrated per `protocols/integration.md`.

## Failure / Conflict Fallback

- Conflict detected mid-wave → pause the conflicting writer.
- Resolve via `protocols/conflict-resolution.md`.
- Re-run the affected node serially before resuming the wave.
