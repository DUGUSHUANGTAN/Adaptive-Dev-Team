# Bugfix Workflow

> 共享生命周期、阶段顺序与"缺角色即跳过"规则见 `workflows/core.md`；本文件只声明差异。

## WHEN TO USE

- 已存在的行为错误、回归、崩溃、数据不一致。
- 症状可观察，根因尚未确认。
- 不适用：新功能、结构重写（分别走 `workflows/standard.md` 与 `workflows/refactor.md`）。

## REQUIRED STAGES

- Reproduce → 确定 scope / root cause → 指派 owner → Fix → 定向回归 → Final Delivery。
- Reproduce 必须先于 Fix：无法复现时只能交付"未复现 + 已收集证据"，不得声称修复。
- 定向回归：原先失败的用例转成回归用例并通过，同时验证同根因的其他调用方无回归。

## OPTIONAL STAGES

- Spec / Plan：多根因、跨模块时补一份轻量拆解。
- Review：按风险触发独立评审（碰安全、数据、并发、公开契约时必做）。
- Integrate：修复跨越 2+ 模块时执行。

## SKIPPED STAGES

- 完整架构流程：小 bug 不走 Architect / Planner / Builder Lead / Parallel Builders。
- Product Analyst、Acceptance Reviewer：默认跳过，除非用户可见的严重缺陷或明确要求。
- 修复期间的功能增强：一律拆成独立任务，不进本流程。

## SPECIAL RULES

- 修根因，不修表象：先 grep 目标函数的所有调用方，在共享点加守卫优于逐调用方打补丁。
- 同一根因的所有调用路径一次修完，不留下"兄弟调用"继续带病运行。
- 禁止顺手重构、升级依赖、改格式；这些改动会污染回归归因。
- 复现失败 → 走 `protocols/escalation.md`，不猜测性提交。

## VERIFICATION DEPTH

- 按风险的 standard 深度：复现用例 + 相关调用方回归。
- 高风险（安全/数据/并发）追加独立 Code Review。

## COMPLETION CONDITIONS

- 复现用例可稳定复现修复前行为，并在修复后通过。
- 受影响的调用方全部验证过，无新增回归。
- 未复现或未闭环根因的，不得标记完成。
