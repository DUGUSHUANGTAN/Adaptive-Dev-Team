---
title: Ownership Protocol
description: "Every writer must declare ownership status for their work. Default: one writer per owned area during parallel waves."
version: "1.0"
status: active
---

# Ownership Protocol

Every agent that writes to files or modifies systems must declare their ownership status clearly. This prevents conflicts, ensures accountability, and maintains code integrity.

## Ownership Categories

### OWN
The agent is the primary owner of this area/file/module/system.
- Can modify freely
- Responsible for quality
- Must maintain consistency
- Is the point of contact for this area

### MAY READ
The agent can read this area/file/module/system but should not modify it without permission.
- Can reference for context
- Must not modify without authorization
- Must respect ownership boundaries

### MUST NOT MODIFY
The agent must not modify this area/file/module/system.
- No modifications allowed
- Must work around this area
- Must not cause conflicts

### SHARED CONTRACTS
This is a shared contract/interface that multiple agents may modify, but modifications must follow specific rules.
- Must follow update procedures
- Must notify all affected agents
- Must maintain backward compatibility
- Must be documented

### DEPENDENCIES
This area/file/module/system depends on the agent's work.
- Agent is responsible for maintaining compatibility
- Agent must communicate changes
- Agent must verify compatibility

## Default Principles

### Single Writer Per Owned Area During Parallel Wave
By default, only one agent should have OWN status for any given area/file/module during a parallel execution wave. This prevents:
- File conflicts
- Inconsistent modifications
- Overlapping work
- Integration errors

### Ownership Must Be Explicit
Every agent must declare their ownership status for all files and areas they work with. No implicit ownership.

### Ownership Changes Must Be Communicated
If ownership changes, all affected agents must be notified. Changes must be documented.

### Ownership Is Not Permanent
Ownership can change, but changes must follow proper procedures.

## Ownership Declaration Format

When an agent starts work, they must declare:
- Which areas/files they OWN
- Which areas/files they MAY READ
- Which areas/files they MUST NOT MODIFY
- Which contracts are SHARED CONTRACTS
- Which areas are DEPENDENCIES

## Ownership Rules

1. Every writer must declare ownership status
2. Default is single writer per area during parallel execution
3. Shared contracts must follow update procedures
4. Dependencies must maintain compatibility
5. Ownership changes must be communicated
6. No implicit ownership
