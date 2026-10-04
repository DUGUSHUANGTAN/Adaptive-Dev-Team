# Context Management Policy

CORE PRINCIPLE: **Minimum Sufficient Context** — give each agent the minimum it needs to execute its task. Never replicate the full chat history or raw transcripts.

## Host Context Model (determine first)

Before delegating, determine which context model the host uses. Do not assume the sub-agent can see shared context.

| Context Model | Behavior |
|---|---|
| **Shared Context Host** | The sub-agent can see the shared team context. Pass references/pointers to shared facts instead of copies. |
| **Isolated Context Host** | The sub-agent sees only what is explicitly passed. Every required field below MUST be included in the delegation. |
| **Unknown Context Model** | Treat as **Isolated** — pass everything explicitly. Safe default; never assume visibility. |

## Required Explicit Context (Isolated / Unknown Host)

These fields must be passed in the delegation contract (see `protocols/delegation.md`):

- **User Goal** — the user's actual objective
- **Critical Requirements** — requirements that cannot change
- **Safety & Hard Constraints** — limits, prohibitions, non-negotiables
- **Relevant Decisions** — decisions already made that affect this task
- **Relevant Interfaces** — contracts/APIs the task consumes or produces
- **Relevant Files & Paths** — files and code the agent needs
- **Own Task** — the exact task this agent is responsible for
- **Dependencies** — what must exist first; what depends on this task
- **Completion Conditions** — the conditions that define task success

## Shared Context Host

A Shared Context Host may reference shared context instead of copying it. Referencing is valid only for facts the host guarantees the sub-agent can see. If visibility is not guaranteed, pass the fact explicitly. When in doubt, pass it.

## Do NOT Transmit

- Full chat history / raw transcripts
- Unrelated tasks' context or progress noise
- Implementation details the receiver does not need

## Global Facts (shared across the team)

- **Project Goal**: overarching objective of the project
- **Constraints**: hard limits and requirements (deadlines, budgets, technical constraints)
- **Architecture Decisions**: approved decisions and rationale
- **Shared Contracts**: APIs, interfaces, integration agreements
- **Critical User Requirements**: user-facing requirements that cannot change

## Local Implementation Details

Local implementation details remain local:
- Implementation decisions belong to the implementing agent
- Code-specific details are not broadcast
- Progress updates are concise and relevant
- Unresolved questions stay with their owner

## Context Distribution Rules

### When Creating an Agent
1. Determine the host context model (Unknown → Isolated)
2. Identify the agent's task
3. Extract the required context fields above
4. Shared Host: reference shared facts; Isolated/Unknown Host: include them explicitly
5. Verify all dependencies are included

### When Updating Context
1. Check whether the change affects other agents
2. Update only the affected agents' context
3. Preserve the local context of unaffected agents

### Context Churn
- Minimize context updates after an agent starts work
- Batch updates together
- Push only critical changes immediately

## Exceptions

Context expansion is permitted when:
- The task requires cross-domain knowledge
- The architecture changed significantly
- Multiple agents must coordinate closely
- The context is needed for verification

## Verification

Before spawning an agent:
- [ ] Host context model determined (Unknown recorded as Isolated)
- [ ] All required explicit fields present for the model in use
- [ ] No irrelevant context included
- [ ] Dependencies properly declared
- [ ] Necessity of shared references (Shared Host only) confirmed
