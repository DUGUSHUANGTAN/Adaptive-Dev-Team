# Standard Workflow

> 共享生命周期、阶段顺序与"缺角色即跳过"规则见 `workflows/core.md`；本文件只声明差异。

## WHEN TO USE

- 普通 Feature：单个明确目标，范围中等（约 1-3 个模块）。
- 需求基本清楚，风险已知可控，不需要架构级决策。
- 有明确 owner，可顺序或小规模并行完成。

## REQUIRED STAGES

- Triage → 选择工作流 → Spec（轻量） → Plan（轻量） → Execute → Verify → Review → Final Delivery。
- Spec：一页以内，只写交付物 + 验收标准 + 不做清单。
- Plan：只列节点、依赖、owner，不写甘特图式计划。
- Builder 与 QA / Reviewer 必须分离，不得由构建者自检充当 Verify + Review。

## OPTIONAL STAGES

- Integrate：产出跨越 2 个模块或 2 个 owner 时执行。
- Accept：默认由用户确认；用户未参与时记录确认来源。
- Specialist：仅按 `policies/quality-gates.md` 的触发条件引入。
- Architect：仅当触及模块边界或接口契约时按需引入。

## SKIPPED STAGES

- Builder Lead：单 Builder 时不创建；出现 2+ Builder 时升级到 `workflows/advanced.md`。
- Acceptance Reviewer：默认不设，用户确认即可。

## SPECIAL RULES

- Spec 变更走 `policies/change-management.md`，不在 Execute 中途静默扩大范围。
- 并行仅在节点无依赖时启用，见 `protocols/parallelization.md`。

## VERIFICATION DEPTH

- standard：功能验证 + 回归检查，覆盖 Spec 中的全部验收标准。
- Review：一次独立 Code Review，按 `protocols/handoff.md` 留下记录。

## COMPLETION CONDITIONS

- Spec 全部验收标准逐条有证据勾选。
- QA 功能与回归检查通过。
- 独立 Code Review 完成且问题已闭环。
- 跳过阶段不要求逐项 `N/A` 清单；按 `workflows/core.md` 的条件记录理由。但交付记录应完整到足以支撑 Review —— 审阅者不需要回头追问"这一步到底做了没有"。
