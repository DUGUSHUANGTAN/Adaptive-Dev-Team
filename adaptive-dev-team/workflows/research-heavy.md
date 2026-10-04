# Research-Heavy Workflow

> 共享生命周期、阶段顺序与"缺角色即跳过"规则见 `workflows/core.md`；本文件只声明差异。

## WHEN TO USE

- 未知项多，方案、可行性或技术选型尚未确定。
- 需要先收集证据才能给出实现路径的任务。
- 不适用：方案已定、只需执行的任务（走 `workflows/standard.md`）。

## REQUIRED STAGES

- 未知项 → 研究问题 → 证据收集 → 决策 → 实现 → 适当验证 → Final Delivery。
- 未知项：显式列出"我们不知道什么"，不把假设混进需求。
- 证据收集先于决策：外部资料、原型、基准、现有代码考古都算证据，需可指向来源。
- 决策必须落成记录（见 `templates/decision-record.md`），含被否方案与理由。

## OPTIONAL STAGES

- Prototype：用于验证关键假设，验证完即弃，不直接当交付物。
- Spec / Plan：决策确定后补，用于承接实现。
- Review：实现阶段按风险触发独立评审。

## SKIPPED STAGES

- 先写大段实现再验证假设：禁止，必须证据先行。
- 无依据的深度设计：未知项未收敛前不做详细设计。

## SPECIAL RULES

- Researcher 默认不直接充当最终 Builder；研究结论与实现分离，避免自证。
- 例外：当 Researcher 明显更高效时（例如结论即少量代码改动）可以兼任，但必须在交付记录写明理由。
- 研究结论不得当作既成事实：未验证的假设必须标注为假设。
- 研究有止损线：超过约定预算仍无法收敛时按 `protocols/escalation.md` 上报，不无限深挖。

## VERIFICATION DEPTH

- 按最终产出类型的深度：研究结论本身靠证据充分性评审，实现部分按 `workflows/standard.md` 深度。
- 决策相关假设至少有一条可运行或可复现的验证。

## COMPLETION CONDITIONS

- 每个未知项有结论：已决策、已否证，或明确标记为未解并说明影响。
- 决策记录完整，证据可追溯。
- 实现与验证按产出类型完成；未验证的假设已在交付中显式标注。
