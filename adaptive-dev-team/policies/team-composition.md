# Team Composition Policy

## Minimum Sufficient Team

Scale the team to the task, not the task to the team.

- Recruit only the roles the selected workflow actually requires.
- Add an optional role only when its trigger fires, never "for completeness".
- Re-evaluate composition as scope changes; drop roles whose work is done.

There is **no fixed minimum team formula**. These are all valid:

| Task size | Team |
|---|---|
| Trivial / local fix | 1 Builder |
| Small change | Builder + a review pass |
| Standard feature | Planner (if needed) → Builder → QA or Code Reviewer |
| Complex / multi-module | Full multi-agent team with Builder Lead, Integration, Specialists on trigger |

A Specialist is never required just because a task exists. See "Role Groups" below.

## Role Groups (not competing teams)

Roles, Builders, and Specialists are three layers of one system, not three rival teams:

- **Roles** (`roles/`) — base responsibilities and decision rights: Leader, Planner, Architect, Builder, QA Engineer, Code Reviewer, Acceptance Reviewer, and the other upstream roles. Every task uses at least one Role.
- **Builders** (`builders/`) — the **Builder Role plus a domain specialization** (frontend, backend, database, gameplay, AI/LLM, …). A Builder is a Role specialization, not a separate organization. `roles/builder.md` is the base contract each builder file specializes.
- **Specialists** (`specialists/`) — on-demand experts added only when a specific risk triggers (auth → Security; FPS/latency → Performance; personal data → Privacy; ordered data change → Migration; and so on). A Specialist is **not** a general-purpose reviewer.

Consequences:

- Verification does not have to pass through a Specialist. Builder implements, QA verifies behavior, Code Reviewer reviews quality and correctness, Acceptance Reviewer checks the original request. Specialists join only on trigger, and only their triggered output enters the Definition of Done.
- Do not present Builders or Specialists as if they replaced the base Roles, and do not treat a Reviewer as a Specialist.

## Dynamic Composition Criteria

Agent counts are determined by:

- Complexity and scope of the task
- Required expertise areas actually triggered
- Dependency structure (what can safely run in parallel)
- Timeline and resource constraints
- Quality requirements of the selected workflow

## Builder Lead Trigger

Builder Lead (`roles/builder-lead.md`) is enabled **only** when:

- ≥2 Builders are active, or
- parallel implementation needs a shared interface/merge contract, or
- cross-module coordination is significant.

Skip Builder Lead when there is a single Builder, a local fix, or a trivial task. All workflows, protocols, and examples must follow this rule.

## Preventing Agent Explosion

- Missing optional roles are skipped, never spawned to satisfy a process diagram.
- No duplicate capabilities; one owner per deliverable.
- Prefer the flattest structure that still resolves dependencies.
- Decommission roles when their contribution ends.

## Spawn Depth

- Default: Leader → Roles / Builders.
- Complex parallel work: Leader → Builder Lead → Builders.
- Maximum depth: three levels below the Leader; anything deeper needs explicit justification.
- Do not spawn a coordination layer (Builder Lead) that has only one thing to coordinate.

## Team Growth and Contraction

Expansion triggers: confirmed scope growth, a triggered Specialist domain, parallelizable independent work.

Contraction triggers: completed work, reduced scope, merged capabilities, or coordination overhead exceeding the benefit of another agent.
