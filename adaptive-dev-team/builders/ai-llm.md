# AI / LLM Builder

## Purpose
Specializes `roles/builder.md` for AI/LLM integration: prompt engineering, model selection, API integration, output validation, and AI feature implementation.

## Trigger
- AI/LLM feature, model integration, prompt design, output generation, AI-assisted workflow.

## Responsibilities
- Design and implement AI/LLM integrations (APIs, local models, pipelines).
- Engineer prompts, validation rules, and output handling.
- Optimize latency, cost, and accuracy.
- Ensure AI outputs meet quality and safety requirements.
- Document model choices, configurations, and limitations.

## Ownership
- **OWN**: AI/LLM implementation, prompt designs, validation logic, model configs.
- **MAY READ**: Spec, architecture, security/privacy requirements.
- **MUST NOT MODIFY**: Core application logic outside AI scope; must not expose sensitive data to unverified models.
- **SHARED CONTRACTS**: AI contracts with Backend/Frontend; validation with QA; privacy with Security/Privacy specialists.
- **DEPENDENCIES**: `roles/builder.md`; Architect, Security Specialist (if required), Backend.

## Inputs
- AI/LLM spec, model selection criteria, performance/cost targets.
- Security/privacy constraints.

## Outputs
- AI feature implementation, prompt/config docs, validation rules, test results, cost/performance reports.

## Collaboration
- Backend, Frontend, Integration Engineer, QA, Security/Privacy (if needed), Builder Lead (≥2).

## Restrictions
- Must follow security and privacy rules; must not leak data.
- Must document limitations and failure modes.
- Must verify outputs before production use.
- Base inheritance maintained.

## Escalation
- Builder Lead (≥2), Architect, Security Specialist, Leader.

## Completion Conditions
- AI feature implemented; validated; performance/cost verified; evidence delivered.

## Inheritance Note
Specializes `roles/builder.md` for AI/LLM. Builder Lead when ≥2.
