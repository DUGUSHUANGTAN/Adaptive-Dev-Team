---
title: Parallelization Protocol
description: "Parallel execution is encouraged when safe. Safety depends on dependency satisfaction, file isolation, and contract stability."
version: "1.0"
status: active
---

# Parallelization Protocol

The Adaptive Dev Team encourages parallel execution where safe. Parallel execution increases efficiency and reduces delivery time, but it must be done safely to prevent conflicts and errors.

## When Parallel Execution Is Safe (Encouraged)

Parallel execution is safe and encouraged when:

### Independent Modules
When modules are independent (no shared dependencies, no file conflicts, separate interfaces), they can be worked on in parallel.

### Independent Research
When research tasks don't depend on each other's results and don't share resources, they can run in parallel.

### Independent Reviews
When reviews can be performed independently (different components, different reviewers), they can run in parallel.

### Contract Frozen After Agreement
When contracts/interfaces have been finalized and frozen, the parts on either side can work independently (front-end and back-end can work in parallel when API contracts are fixed).

### Independent Features
When features don't interact and don't share code, they can be developed in parallel.

### Independent Test Preparation
When test preparation doesn't affect the code being tested, it can run in parallel with development.

## When Parallel Execution Is NOT Safe (Prohibited)

Parallel execution must NOT occur when:

### Dependencies Not Satisfied
When a task depends on another task that hasn't completed, it must wait.

### Same File Conflict
When multiple agents would modify the same file, parallel execution is not safe.

### Same Core Module Ownership
When multiple agents claim ownership of the same core module, conflicts will occur.

### Architecture Not Resolved
When the architecture hasn't been finalized, parallel work may result in incompatible designs.

### Requirements Not Resolved
When requirements are unclear or changing, parallel work may need to be redone.

### Sequential Migration Steps
When migration requires sequential steps (e.g., database migration must complete before application updates), sequential execution is required.

### Shared Contract Unstable
When shared contracts/interfaces are not stable or finalized, parallel work may cause integration failures.

## Parallelization Verification

Before allowing parallel execution:

1. **Check dependencies**: Verify all dependencies are satisfied
2. **Check file conflicts**: Verify no file conflicts exist
3. **Check ownership**: Confirm clear ownership for all areas
4. **Check architecture**: Verify architecture is resolved
5. **Check requirements**: Confirm requirements are stable
6. **Check contracts**: Verify contracts are frozen (if applicable)
7. **Check migration steps**: Verify sequential requirements (if applicable)

## Parallel Execution Rules

- Always verify safety before parallel execution
- Document which tasks are running in parallel
- Monitor for conflicts
- Have integration plans ready
- Be prepared to stop parallel execution if conflicts occur
