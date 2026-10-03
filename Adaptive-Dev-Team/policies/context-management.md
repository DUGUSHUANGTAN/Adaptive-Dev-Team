# Context Management Policy

## Core Principle: Minimum Context for Maximum Value

Do not replicate the entire chat history to every agent. Provide each agent only what it needs to execute its task. This reduces noise, prevents information overload, and maintains focus.

## Per-Agent Context (Relevant Context Only)

Each agent receives only the following:

- **Relevant Goal**: The specific goal this agent works toward
- **Relevant Spec**: The specification relevant to this agent's task
- **Relevant Architecture**: The architectural decisions that affect this agent's work
- **Relevant Files**: The files and code blocks needed for execution
- **Relevant Decisions**: The decisions directly related to this agent's task
- **Own Task**: The exact task this agent is responsible for
- **Dependencies**: What this agent depends on and what depends on it
- **Acceptance Criteria**: The conditions that define task success

## Shared Global Facts (Global Context)

The following facts are shared across the entire team:

- **Project Goal**: The overarching objective of the project
- **Constraints**: Hard limits and requirements (deadlines, budgets, technical constraints)
- **Architecture Decisions**: The approved architectural decisions and rationale
- **Shared Contracts**: APIs, interfaces, and integration agreements
- **Critical User Requirements**: User-facing requirements that cannot change

## Local Implementation Details

Local implementation details must remain local:

- Implementation decisions belong to the implementing agent
- Code-specific details are not shared broadly
- Progress updates are concise and relevant
- Unresolved questions remain with the owner

## Context Distribution Rules

### When Creating an Agent
1. Identify the agent's task
2. Extract the relevant context components
3. Omit global context (it is always available)
4. Verify all dependencies are included

### When Updating Context
1. Check if the change affects other agents
2. Update only the affected agents' context
3. Preserve the local context of unaffected agents

### Context Churn
- Minimize context updates after an agent starts work
- Batch context updates together
- Only push critical changes immediately

## Exceptions

Context expansion is permitted when:
- The task requires cross-domain knowledge
- The architecture has changed significantly
- Multiple agents must coordinate closely
- The context is needed for quality assurance

## Verification

Before spawning an agent:
- Confirm the context is complete for the task
- Verify no irrelevant context is included
- Ensure dependencies are properly declared
- Check that global facts are available