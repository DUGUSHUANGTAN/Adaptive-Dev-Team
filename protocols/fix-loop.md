---
title: Fix Loop Protocol
description: "QA/reviewer finds issue → classify → identify original owner → fix → targeted recheck. Don't have reviewers rewrite implementations."
version: "1.0"
status: active
---

# Fix Loop Protocol

When QA or a reviewer finds an issue, there is a structured process for addressing it. The fix loop ensures that problems are properly identified, assigned to the correct owner, fixed correctly, and verified properly.

## Fix Loop Process

### Phase 1: Issue Classification
When an issue is found:
- Classify the issue (bug, improvement, documentation, etc.)
- Assess severity (critical, high, medium, low)
- Assess impact (local, module, system-wide)
- Document the issue clearly

### Phase 2: Identify Original Owner
Find who is responsible for this area:
- Check ownership documentation
- Check task assignments
- Identify the original builder/developer
- Confirm ownership with the team

### Phase 3: Builder Lead Assignment
The builder lead assigns the fix:
- Confirm the original owner is appropriate
- If needed, assign to a different owner
- Provide context and requirements
- Confirm the fix approach

### Phase 4: Original Builder Fix
The original builder (or assigned builder) fixes the issue:
- Understand the issue completely
- Implement the minimal fix
- Test the fix
- Document changes
- Provide verification

### Phase 5: Targeted Recheck
Verify the fix specifically:
- Verify the fix addresses the issue
- Verify no regressions occurred
- Verify quality standards met
- Verify documentation updated
- Confirm approval

## Fix Loop Rules

### Don't Let Reviewers Rewrite Implementation
When a reviewer finds an issue:
- The reviewer should describe the problem
- The reviewer should NOT rewrite the implementation
- The original owner should fix the problem
- Only if the original owner is unavailable should another builder fix it

### Targeted Recheck
The verification must be targeted:
- Focus on the specific issue
- Don't do full regression (unless needed)
- Verify the fix specifically
- Confirm the fix is complete

### Document All Fixes
Every fix must be documented:
- What was fixed
- How it was fixed
- Who fixed it
- How it was verified
- Any implications

### Follow the Loop
The loop must be followed completely:
- Don't skip steps
- Don't assume fixes are complete
- Verify all steps
- Document results
