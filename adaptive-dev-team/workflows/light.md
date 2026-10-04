# Light Workflow

> 共享生命周期、阶段顺序与"缺角色即跳过"规则见 `workflows/core.md`；本文件只声明差异。

## WHEN TO USE

- Trivial fix、typo、小范围局部改动（1-2 个文件）。
- Low risk：不碰数据、安全、公开接口、并发、部署。
- Single owner：一个 Builder 从头改到尾，无跨模块依赖。

## REQUIRED STAGES

- Triage → 选择工作流 → Execute → Verify → Final Delivery。
- Spec / Plan 是行内产物（一句话说明改什么、怎么验），不单列阶段文件。

## OPTIONAL STAGES

- Review：允许一次 separate review pass。
- 该 pass 若由改动者自己执行，必须在交付记录标记 `non-independent self-review`，不得声称为独立评审。
- Integrate：仅当改动意外跨到 2 个模块时补做。

## SKIPPED STAGES

默认跳过，除非风险触发：

- Product Analyst、Architect、Planner、Builder Lead、Integration、Specialist、Acceptance Reviewer。
- 风险触发条件（任一命中即重新 Triage 并升级到 `workflows/standard.md` 或更重）：
  公开 API / 契约变更、数据迁移或删除、认证授权与安全、并发共享状态、跨 3+ 模块、改动超出 2 个文件。

## SPECIAL RULES

- 不 spawn 团队；不建 DAG；不写 Spec/Plan 文档。
- 改动途中范围膨胀，停止并按新范围重新 Triage，不在 light 里硬撑。

## VERIFICATION DEPTH

- light：定向校验即可 —— 一个可运行的最小验证（单测、demo、assert、手动复现步骤）。
- 不要求回归套件、不要求独立评审。

## COMPLETION CONDITIONS

- 改动可运行、无语法/构建错误。
- 有一条可运行证据，或明确记录为非代码改动的等价证据。
- **不要求逐项 `N/A` 记账。** LIGHT 默认静默跳过 Product Analyst / Architect / Planner / Builder Lead / Integration / Specialist / Acceptance Reviewer，不需要输出这些行。
  只在 `workflows/core.md` 的条件成立时补一行理由：省略影响风险、影响验收、某个通常预期的阶段被有意跳过，或用户明确要求审计轨迹。
- 超出 light 边界 → 未完成，升级工作流重跑。
