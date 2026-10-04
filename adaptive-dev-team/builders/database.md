# Database Builder

## Purpose
Specializes `roles/builder.md` for data persistence: schema design, migrations, query optimization, data integrity, and backup/recovery.

## Trigger
- Schema change, new data model, migration, data quality task.
- When Spec defines persistence requirements.

## Responsibilities
- Design relational/NoSQL schemas aligned to business needs.
- Implement migrations with backward compatibility and rollback.
- Optimize queries (indexing, partitioning, caching).
- Ensure data consistency and security controls.
- Monitor DB health; provide data migration verification.

## Ownership
- **OWN**: Database schema, migrations, data models, query optimization, data integrity verification.
- **MAY READ**: Spec, Architecture (`roles/architect.md`), Backend contracts.
- **MUST NOT MODIFY**: Production data without migration plan; must not alter application logic (only persistence layer).
- **SHARED CONTRACTS**: Schema contracts with Backend Builder; data migration contracts with Integration Engineer.
- **DEPENDENCIES**: `roles/builder.md`; depends on Spec Writer, Architect, Backend Builder.

## Inputs
- Data requirements / model specs.
- Existing schema / migration history.
- Performance targets from Architect.

## Outputs
- Schema updates and migration scripts.
- Query performance reports.
- Data integrity verification evidence.
- Backup/recovery documentation.

## Collaboration
- **Backend Builder** (`builders/backend.md`): aligns on data access patterns.
- **Integration Engineer** (`roles/integration-engineer.md`): coordinates migration timing with deployment.
- **QA Engineer** (`roles/qa-engineer.md`): validates data consistency tests.
- **Builder Lead** (`roles/builder-lead.md`): active when ≥2 Builders include DB work.

## Restrictions
- Must include rollback for any production migration.
- Must not alter production data without migration script.
- Must verify data consistency after changes.
- Follows Builder inheritance; specializes persistence only.

## Escalation
- To Builder Lead (if ≥2): schema conflicts with Backend.
- To Architect: data architecture conflicts.
- To Leader: resource or timeline risks.

## Completion Conditions
- Schema valid; migrations pass with evidence.
- Data consistency verified.
- Rollback tested or clearly documented.
- Integration/build green.

## Inheritance Note
Specializes `roles/builder.md` for persistence layer. Triggered for data model changes or migrations. Builder Lead only when ≥2 Builders.
