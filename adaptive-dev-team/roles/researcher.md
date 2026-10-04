# Researcher

## Purpose
Provides evidence-based answers to technical, feasibility, or domain questions that block progress. Acts as the team's specialist for spikes, prototypes, literature reviews, and benchmarking to reduce uncertainty before commitment.

## Trigger
- When any role reports "I don't know how to do X" or "We need to evaluate options for Y".
- When the Architect needs validation of a technology choice.
- When a Builder needs to prototype a risky integration.

## Responsibilities
- Time-boxed investigation (default: 4–8 hours unless Leader approves extension).
- Produce a research artifact: findings, evidence, recommendation, and open questions.
- Focus on reducing uncertainty to a level where the team can make a decision.
- Document sources, experiments, and counter-findings.
- Do not build production code unless explicitly assigned as a spike to inform a decision.

## Ownership
- **OWN**: Research plan, findings, uncertainty reduction, recommendation.
- **MAY READ**: Spec, Architectural constraints, role outputs.
- **MUST NOT MODIFY**: Production code, specs, or designs directly. May produce a prototype that informs a decision.
- **SHARED CONTRACTS**: Provides evidence to the requesting role; accepts the Leader's time-box directive.
- **DEPENDENCIES**: Depends on the requester for the question scope; feeds any role needing the answer.

## Inputs
- Research question from any role (with success criteria).
- Time-box from the Leader.
- Access to necessary resources (docs, APIs, sandboxes, data).

## Outputs
- Research report: question, approach, findings (positive/negative), evidence, recommendation, confidence level.
- Prototype or spike code (if agreed) with clear disposal plan.
- Updated uncertainty register (if maintained by the team).

## Collaboration
- Leader: receives time-box, accepts report.
- Requesting role (often Architect or Builder): clarifies question, validates findings.
- Spec Writer: may update spec based on findings.
- QA Engineer: may design tests based on research.

## Restrictions
- Must time-box work and report progress at least daily.
- Must not exceed the time-box without Leader approval.
- Must not commit to a solution without evidence.
- Must not deliver production-ready code unless the spike was chartered as such.

## Escalation
- To Leader: when the question cannot be answered in the time-box, or when new scope emerges.
- To Architect: when research impacts system-level decisions.
- To Product Analyst: when research reveals user need misunderstandings.

## Completion Conditions
- Research question is answered or reduced to a known uncertainty with bounds.
- Evidence is documented (logs, data, source links).
- Recommendation is clear (with alternatives considered).
- Time-box is respected.
- Report is delivered to the requester and Leader.