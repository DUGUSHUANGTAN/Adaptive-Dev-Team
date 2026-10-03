# Ownership Protocol

## Core Ownership Principles

### Minimum Sufficient Team
- Assign ownership only to necessary roles
- Keep ownership boundaries clear and minimal
- Avoid overlapping ownership that creates confusion

### Dynamic Composition
- Adjust ownership scope based on team size and task complexity
- Reassign ownership as team composition changes
- Maintain ownership continuity through parallel waves

### Explicit Ownership
- Every write agent must declare ownership boundaries
- Ownership is explicit, not implicit
- Changes require ownership verification

## Ownership Declaration Format

### OWN
[Files, modules, or systems that the agent is responsible for creating/modifying]

### MAY READ
[Files, modules, or systems that the agent can read for context]

### MUST NOT MODIFY
[Files, modules, or systems that must not be changed under any circumstances]

### SHARED CONTRACTS
[Contracts, interfaces, or specifications that multiple agents may modify under coordination]

### DEPENDENCIES
[External systems or modules that this agent's work depends on]

## Ownership Rules

### Single Writer Principle
- Each owned area has exactly one writer during parallel waves
- Multiple writers require explicit coordination and merge planning
- Ownership conflicts must be resolved before parallel execution

### Ownership Transfer
- Ownership transfers require explicit handoff
- Transfer must be documented in handoff report
- Previous owner must verify transfer completeness

### Ownership Boundaries
- Clear boundaries prevent parallel conflicts
- Boundaries defined at file/module level
- Overlapping boundaries require coordination

## Ownership Declaration Template

```markdown
# Agent: [Role Name]

## OWN
- [File/Module 1]
- [File/Module 2]

## MAY READ
- [File/Module 3]
- [File/Module 4]

## MUST NOT MODIFY
- [File/Module 5]
- [File/Module 6]

## SHARED CONTRACTS
- [Contract 1]
- [Contract 2]

## DEPENDENCIES
- [Dependency 1]
- [Dependency 2]
```

## Ownership Conflict Resolution

### Conflict Types
1. **Same File Conflict**: Two agents own overlapping files
2. **Dependency Conflict**: Agent A depends on work Agent B hasn't completed
3. **Contract Conflict**: Two agents modify shared contracts differently
4. **Interface Conflict**: Agents disagree on interface definitions

### Resolution Process
1. **Identify**: Detect ownership conflicts early
2. **Classify**: Determine conflict type and severity
3. **Coordinate**: Engage affected agents in resolution
4. **Decide**: Assign ownership or split work
5. **Document**: Record resolution and new boundaries

## Ownership Best Practices

### Before Parallel Execution
- [ ] All ownership boundaries defined
- [ ] Shared contracts identified and frozen
- [ ] Dependencies mapped and ready
- [ ] Conflict resolution plan in place

### During Parallel Execution
- [ ] Monitor for ownership violations
- [ ] Track shared contract changes
- [ ] Verify dependency satisfaction
- [ ] Maintain communication channels

### After Parallel Execution
- [ ] Verify ownership compliance
- [ ] Resolve any conflicts
- [ ] Update ownership records
- [ ] Document lessons learned

## Ownership Types

### Primary Ownership
- Core responsibility for specific files/modules
- Full modification rights
- Accountability for quality and correctness

### Secondary Ownership
- Supporting role for specific areas
- Limited modification rights
- Coordination with primary owner

### Shared Ownership
- Collaborative responsibility
- Requires coordination
- Changes require consensus

### Read-Only Access
- Information gathering only
- No modification rights
- Context for understanding