---
title: Light Workflow
when_to_use: Small, low-risk tasks with clear requirements
team_composition: Lead (1), Developer (1-2), QA (1)
stages:
  - name: Input
description: Analysis, planning, requirements
  - name: Implementation
description: Core development
  - name: Review
description: Testing and QA
  - name: Deployment
description: Release and integration
handoff_points:
  - from: Input to Implementation: Requirements, specs, environment
  - from: Implementation to Review: Working code, tests, docs
  - from: Review to Deployment: QA sign-off, build, release notes
completion_criteria:
  - functional_requirements_met
  - quality_standards_achieved
  - user_acceptance_complete
  - documentation_updated
---
# Light Workflow
Use for small changes with low risk. Single writer per area.
