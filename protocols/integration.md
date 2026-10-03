---
title: Integration Protocol
description: "Parallel Builder Wave completes with structured integration: Builders → Handoffs → Integration → Cross-module Check → Next Stage."
version: "1.0"
status: active
---

# Integration Protocol

When parallel builders complete their work, the results must be integrated through a structured process. Integration is not just combining code — it's verifying that all parts work together correctly.

## Integration Sequence

### Phase 1: Builders Complete
When all parallel builders complete their tasks:
- Each builder provides a handoff report
- All handoffs are collected
- Dependencies are verified

### Phase 2: Handoff Collection
Collect all handoff reports:
- Verify all builders completed
- Verify all handoffs include required sections
- Identify any issues or concerns
- Note any missing information

### Phase 3: Integration
Perform integration work:
- Combine all code changes
- Verify interfaces match
- Verify contracts are satisfied
- Resolve any conflicts
- Verify all components work together

### Phase 4: Cross-Module Check
Perform cross-module verification:
- Verify interfaces between modules
- Verify data flow
- Verify integration points
- Check for integration errors
- Verify performance

### Phase 5: Next Stage
Proceed to the next stage or complete the task:
- If integration passes, proceed
- If issues found, address and re-check
- Provide final handoff
- Confirm task completion

## Integration Rules

### Integration Agent Rules
- The integration agent must NOT randomly restructure all builder work
- Internal problems must be returned to the original owner
- The integration agent should only combine and verify
- Integration agent should not make unnecessary changes
- Integration agent must verify all interfaces

### Problem Resolution
- If internal problems are found, return to original builder
- If interface problems are found, coordinate with all affected builders
- If integration fails, identify root cause and fix
- If conflicts exist, resolve with all affected agents

### Integration Verification
- Verify all interfaces work correctly
- Verify all contracts are satisfied
- Verify all tests pass
- Verify performance is acceptable
- Verify security is maintained
