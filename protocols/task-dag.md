---
title: Task DAG Protocol
description: "Complex tasks must have a dependency graph established before spawning builders. Each node must specify ownership, inputs, outputs, and parallelizability."
version: "1.0"
status: active
---

# Task DAG Protocol

For complex tasks, before any builders are spawned, a dependency graph (DAG - Directed Acyclic Graph) must be established. This ensures proper sequencing, dependency management, and parallelization safety.

## When Required

A Task DAG is required when:
- The task has multiple components
- Multiple agents will work on the task
- There are dependencies between components
- Parallel work is possible
- Integration is required

## Node Specification

Each node in the DAG must include:

### TASK ID
A unique identifier for the task node. Must be consistent across all references.

### OBJECTIVE
What this specific node must achieve within the larger task.

### OWNER TYPE
The type of owner for this node:
- Individual Agent
- Team
- System

### DEPENDENCIES
All tasks that must be completed before this task can start:
- List of dependency task IDs
- Dependency type (hard/soft)
- Dependency verification criteria

### INPUTS
What this task requires to start:
- Files
- Data
- Decisions
- Contracts
- Resources

### OUTPUTS
What this task produces:
- Files
- Data
- Decisions
- Contracts
- Deliverables

### AFFECTED AREAS
What areas are affected by this task:
- Modules
- Components
- Systems
- Interfaces

### ACCEPTANCE CRITERIA
When this task is considered complete:
- Deliverables completed
- Quality standards met
- Verification completed
- Approval received

### PARALLELIZABLE
Can this task run in parallel with other tasks?
- Yes/No
- If yes, with which tasks?
- If no, why not?

## DAG Construction Rules

1. **Identify all tasks**: Break down the complex task into individual tasks
2. **Define dependencies**: Determine which tasks depend on others
3. **Identify parallel tasks**: Find tasks that can run in parallel
4. **Assign owners**: Specify who owns each task
5. **Define inputs and outputs**: Specify what each task needs and produces
6. **Define affected areas**: Identify impact areas
7. **Set acceptance criteria**: Define completion for each task
8. **Document the DAG**: Create a visual or structured representation

## Parallelization Safety

Before allowing parallel execution:
- Verify all dependencies are satisfied
- Check for file conflicts
- Confirm ownership is clear
- Verify contracts are stable
- Confirm no architectural conflicts exist

## DAG Verification

Before spawning builders:
- Verify the DAG is acyclic (no cycles)
- Verify all nodes have complete specifications
- Verify dependencies are valid
- Verify parallel tasks are safe
- Confirm the DAG covers all requirements

## DAG Updates

If the task changes:
- Update the DAG
- Verify the updated DAG is still valid
- Communicate changes to all affected agents
- Re-verify parallelization safety
