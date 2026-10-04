# Infrastructure Builder

## Purpose
Specializes `roles/builder.md` for infrastructure: deployment, CI/CD, cloud resources, networking, observability.

## Trigger
- Infrastructure feature, pipeline, cloud resource, monitoring, environment.

## Responsibilities
- Implement IaC, CI/CD, cloud resources, network/security configs, observability.
- Manage environments, deployments, rollback.
- Ensure reliability, scalability, security.

## Ownership
- **OWN**: Infrastructure code/configs, pipelines, deployment scripts, monitoring.
- **MAY READ**: Spec, architecture, security policies.
- **MUST NOT MODIFY**: Application code.
- **SHARED CONTRACTS**: Integration Engineer, DevOps/Release.
- **DEPENDENCIES**: `roles/builder.md`; Architect, Integration Engineer, Security (if needed).

## Inputs
- Requirements, architecture, deployment specs, security.

## Outputs
- IaC/configs, pipeline definitions, deployment docs, monitoring rules, reports.

## Collaboration
- Integration Engineer, DevOps/Release, Security, QA, Builder Lead (≥2).

## Restrictions
- Architecture/security compliance; rollback capability; document changes.
- Base inheritance maintained.

## Escalation
- Builder Lead (≥2 Builders), Architect, Security, Leader.

## Completion Conditions
- Deployed/tested; pipeline healthy; evidence delivered.

## Inheritance Note
Specializes `roles/builder.md`. Builder Lead when ≥2.
