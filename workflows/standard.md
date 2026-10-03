---
title: Standard Workflow
when_to_use: Medium complexity, multi-component tasks with moderate risk
team_composition: Architect (1), Senior Devs (2-3), QA (1), Product (1)
stages:
  - name: Planning
description: Requirements, timeline, risk
  - name: Design
description: Architecture, contracts
  - name: Development
description: Implementation
  - name: Integration
description: Testing, validation
  - name: Deployment
description: Release
handoff_points:
  - Planning → Design: Spec, timeline
  - Design → Development: Design docs, contracts
  - Development → Integration: Code, tests
  - Integration → Deployment: QA sign-off
completion_criteria:
  - requirements_fulfilled
  - quality_gates_passed
  - deployed
---
# Standard Workflow
Use for medium-complexity tasks requiring coordination.
