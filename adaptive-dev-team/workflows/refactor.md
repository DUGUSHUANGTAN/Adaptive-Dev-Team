# Refactor Workflow

> 共享生命周期、阶段顺序与"缺角色即跳过"规则见 `workflows/core.md`；本文件只声明差异。

## WHEN TO USE

- 结构改动、行为不变：抽接口、拆模块、去重、改命名、替换等价实现。
- 可观测行为、公开契约、性能特征都保持不变。
- 不适用：任何会改变外部行为的需求（走 `workflows/standard.md`）。

## REQUIRED STAGES

- 建立 baseline 行为 → 划定重构范围 → 依赖分析 → 实现 → 行为保持校验 → Review → Final Delivery。
- baseline 先于改动：先跑通并记录现有测试/校验结果，作为行为保持的对照。
- 依赖分析：列出受影响调用方与共享数据，决定是否需要分批实施。

## OPTIONAL STAGES

- Spec / Plan：跨模块或跨仓库时补轻量拆解与顺序。
- Integrate：改动横跨 2+ 模块时执行。
- Architect：仅当模块边界或接口契约发生变化时引入。

## SKIPPED STAGES

- Product Analyst：无新需求可分析，跳过。
- 功能开发相关阶段：不得夹带，任何行为变更拆成独立任务。
- Acceptance Reviewer：非用户可见变化时跳过。

## SPECIAL RULES

- 行为保持是硬约束：如果行为必须改变，先停下来拆任务，不在这里"顺便改"。
- 不允许以降低正确性换取结构整洁；边界校验、错误处理不得为简化而删除。
- 分批实施时，每批都必须独立可验证、可回滚，不合并成一个巨型提交。
- 校验缺失时先补 baseline 校验，再开始重构，不靠"看起来一样"。

## VERIFICATION DEPTH

- standard 深度：行为保持校验（对照 baseline）+ 回归检查。
- Review：独立 Code Review，重点看是否有夹带的行为变更。

## COMPLETION CONDITIONS

- baseline 与重构后结果一致（测试/校验对照可复现）。
- 无夹带的行为变更；所有接口契约保持兼容，或已记录兼容性结论。
- Review 确认无隐藏行为改动；被跳过的阶段按 `workflows/core.md` 的条件记录理由（不要求逐项 `N/A` 清单）。
