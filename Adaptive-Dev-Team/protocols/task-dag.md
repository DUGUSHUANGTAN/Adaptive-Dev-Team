# Task DAG Protocol

## Core DAG Principles

### Minimum Sufficient Team
- Only build nodes for tasks that are needed
- Avoid creating unnecessary dependency nodes
- Keep the DAG lean and focused

### Dynamic Composition
- Adjust DAG structure based on task complexity
- Add nodes dynamically as dependencies emerge
- Remove nodes as tasks complete

### Explicit Ownership
- Each node has a single owner type
- Dependencies are explicit and declared
- Parallel paths are clearly marked

## Task DAG Node Structure

### Before Spawn Builders

Every node must include the following fields:

- **Task ID**: Unique identifier for the task
- **Objective**: Brief, actionable statement of what the task accomplishes
- **Owner Type**: Role type responsible for executing this task
- **Dependencies**: List of Task IDs this task depends on
- **Inputs**: Required inputs/dependencies that must be available
- **Outputs**: Expected outputs/deliverables from this task
- **Affected Areas**: Files, modules, or systems touched by this task
- **Acceptance Criteria**: Measurable criteria for task completion
- **Parallelizable**: Boolean - can this task run in parallel with others

## Task DAG Construction

### Node Types

1. **Root Node**: Starting point, no dependencies
2. **Dependent Node**: Requires one or more parent nodes to complete
3. **Parallel Node**: Can run concurrently with other nodes
4. **Synchronization Node**: Waits for multiple nodes before proceeding

### DAG Structure Rules

1. **No Cycles**: DAG must be acyclic - no circular dependencies
2. **No Dangling Nodes**: Every node must be reachable from a root
3. **Clear Boundaries**: Each node has explicit inputs and outputs
4. **Parallelizable Paths**: Independent paths marked for parallel execution

## DAG Construction Template

```
DAG Node: [Node ID]
├── Task ID: [unique-id]
├── Objective: [what this task does]
├── Owner Type: [role type]
├── Dependencies: [list of Task IDs]
├── Inputs:
│   ├── [input 1]
│   └── [input 2]
├── Outputs:
│   ├── [output 1]
│   └── [output 2]
├── Affected Areas:
│   ├── [area 1]
│   └── [area 2]
├── Acceptance Criteria:
│   ├── [criterion 1]
│   └── [criterion 2]
└── Parallelizable: [true/false]
```

## DAG Visualization

### DAG Structure Examples

```
┌─────────────────┐
│ Task ID: ROOT   │  (No dependencies)
└────────┬────────┘
         │
         ├──────────────┐
         │              │
┌────────▼──────┐  ┌────▼──────────┐
│ Task ID: A    │  │ Task ID: B    │  (Parallel paths)
└────────┬──────┘  └────┬──────────┘
         │              │
         └──────┬───────┘
                │
        ┌───────▼────────┐
        │ Task ID: SYNC  │  (Synchronization)
        └────────────────┘
```

## DAG Management

### Node Creation
- Create root nodes from task triage results
- Add dependent nodes as requirements emerge
- Mark parallelizable paths clearly

### Node Execution
- Verify dependencies before node activation
- Track node state (pending, in-progress, completed)
- Update DAG as nodes complete

### DAG Completion
- Verify all root-to-leaf paths complete
- Confirm acceptance criteria met
- Archive DAG for reference

## Parallel Execution Rules

### Parallelizable Nodes
- Independent modules that don't share state
- Separate research paths
- Non-overlapping file writes
- Independent test preparation

### Blocked Nodes
- Nodes with unmet dependencies
- Nodes sharing write locks with active nodes
- Nodes requiring resolved architecture decisions
- Nodes waiting on requirements clarification

## DAG Tools and Utilities

### Visualization
- Use DAG visualization to understand task structure
- Identify critical paths and bottlenecks
- Track parallel execution progress

### Tracking
- Monitor node status in real-time
- Alert on blocked or stalled nodes
- Update dependencies dynamically

## DAG Best Practices

### Before Execution
- [ ] Validate DAG is acyclic
- [ ] Confirm all inputs are available
- [ ] Verify acceptance criteria are clear
- [ ] Identify parallel paths
- [ ] Check ownership assignment

### During Execution
- [ ] Monitor for dependency violations
- [ ] Track parallel execution progress
- [ ] Handle node failures gracefully
- [ ] Update DAG as changes occur

### After Execution
- [ ] Verify all nodes completed
- [ ] Confirm acceptance criteria
- [ ] Archive completed DAG
- [ ] Document lessons learned

## DAG Status Transitions

| Status | Description | Next Action |
|--------|-------------|-------------|
| Pending | Node created, waiting for dependencies | Wait for dependencies |
| In Progress | Dependencies met, work underway | Monitor progress |
| Blocked | Dependency or requirement issue | Escalate or resolve |
| Completed | Acceptance criteria met | Mark for integration |
| Failed | Work could not complete | Retry or reassign |