# Advanced Workflow

> 共享生命周期、阶段顺序与"缺角色即跳过"规则见 `workflows/core.md`；本文件只声明差异。

## WHEN TO USE

- Multi-module 或大型 Feature，工作可拆成可并行节点。
- Parallel builders：2+ 个互不重叠的写范围。
- Architecture change：模块边界、接口契约、数据模型发生变更。

## REQUIRED STAGES

- Triage → 选择工作流 → Spec → Architect（按需） → Planner → Builder Lead → Parallel Builders → Integration → QA → Code Review → Final Delivery。
- Architect 仅在架构变更时必做；纯多模块功能可跳过并记录理由。
- Acceptance：必要时（用户可见、契约变更、跨团队交付）才补 Acceptance Reviewer。

## OPTIONAL STAGES

- Architect：按需，见上。
- Acceptance Reviewer：按需。
- Specialist：按 `policies/quality-gates.md` 触发条件引入，未触发不引入。

## SKIPPED STAGES

- Acceptance Reviewer：低风险、无外部契约时跳过。
- 单 Builder 路径：出现并行 Builder 才需要 Builder Lead，否则降级到 `workflows/standard.md`。

## SPECIAL RULES

- 只有 2+ Builder 时才设 Builder Lead；Builder Lead 不写代码，只做协调与合并判定。
- 写范围必须互斥，Owner 唯一，见 `protocols/ownership.md`。
- 并行按 Task DAG：无依赖才并行，有依赖禁止并行，见 `protocols/task-dag.md` 与 `protocols/parallelization.md`。
- Integration 不得由最后完成的 Builder 独自完成，见 `protocols/integration.md`。

## VERIFICATION DEPTH

- advanced：逐节点验证 + 跨模块集成验证。
- Review：独立 Code Review + 集成检查，两者都不能由构建者自审替代。

## COMPLETION CONDITIONS

- Spec 与架构决策均有可追溯记录。
- 每个并行分支各自验证通过，集成验证通过。
- Code Review 与集成检查问题闭环。
- Acceptance 触发时，最终验收报告为 Pass（见 `templates/acceptance-report.md`）。
