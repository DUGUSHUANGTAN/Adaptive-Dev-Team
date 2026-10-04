# Migration Workflow

> 共享生命周期、阶段顺序与"缺角色即跳过"规则见 `workflows/core.md`；本文件只声明差异。

## WHEN TO USE

- 框架、语言、运行时、数据库、平台或供应商之间的迁移。
- 新旧系统需要并存、切换或数据搬迁。
- 不适用：同栈内的结构整理（走 `workflows/refactor.md`）。

## REQUIRED STAGES

- Current → Target → 兼容约束 → 迁移计划 → 备份 / 回滚（相关时） → 有序步骤 → 验证 → 切换完成 → Final Delivery。
- Current：现状盘点（依赖、数据形态、调用方、遗留行为），是判断兼容性的依据。
- Target：目标状态与不可协商的约束（版本、ABI、数据格式、下线时间）。
- 有序步骤：每一步都可独立验证；存在依赖关系时按依赖顺序执行。

## OPTIONAL STAGES

- Migration Specialist：涉及数据搬迁或大规模依赖替换时引入，见 `specialists/migration.md`。
- 并行执行：仅当步骤之间无依赖且可独立回滚时允许。
- Backout 演练：生产数据迁移时建议先做一次。

## SKIPPED STAGES

- 默认不盲目并行：依赖严格的迁移必须串行，不为了速度并行有依赖的步骤。
- 功能增强：迁移期间不加新功能。

## SPECIAL RULES

- 迁移期不允许"新旧混用无约束"：每个中间状态都要明确走哪条路径。
- 数据迁移必须有备份或等价恢复路径；没有恢复路径就不开始迁移。
- 兼容性判断基于证据（实际运行/探测），不基于"应该没问题"。
- 某一步失败即停在该步，先执行回滚，不连滚带爬往下走。

## VERIFICATION DEPTH

- advanced 深度：每步验证 + 最终端到端验证（新旧路径结果一致）。
- Review：独立 Code Review + Migration Specialist 评审（引入时）。

## COMPLETION CONDITIONS

- 每个有序步骤有验证证据，失败步骤有回滚记录。
- 切换完成后目标环境端到端通过，旧路径按计划下线或有明确保留结论。
- 兼容约束逐条核对完毕，无遗留断路。
