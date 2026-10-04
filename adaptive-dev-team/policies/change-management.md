# Change Management

Local change → re-run only the affected tasks.
Architecture-impacting change → Architect → Planner → affected Builders.
Requirement-level change → Requirements / Spec → downstream stages.
No full rebuild unless the architecture requires it.

## Change History

Change history belongs to version control, not to the skill's runtime reference material:

- Repository history is the authoritative record: `git log` / `git diff`.
- A repository hosting this skill may also keep release notes of its own. That is the distributor's choice, is optional, and is **not** a runtime dependency: this skill is fully functional when only its own directory is present, and it reads no file outside its root.
- `references/` is optional runtime reference material (external standards, knowledge links). It is **not** a changelog and must not be required to exist.

## Scope of This Policy

This policy governs changes made **inside a project using Adaptive Dev Team**. Changes to the skill's own files follow `SKILL.md` §16.
