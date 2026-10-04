# Optimization Workflow

> 共享生命周期、阶段顺序与"缺角色即跳过"规则见 `workflows/core.md`；本文件只声明差异。

## WHEN TO USE

- 性能、内存、构建体积、启动时间、查询耗时等量化开销的优化。
- 已有（或可建立）可测量的指标，能判断改前改后差异。
- 不适用：尚未定义目标的"让它变快"（先走 `workflows/research-heavy.md` 立项）。

## REQUIRED STAGES

- 定义目标指标 → 尽可能建立基线 → 定位瓶颈 → 优化 → 对比 → 回归检查 → Final Delivery。
- 目标指标必须先量化（数值 + 测量方式 + 环境），否则不进入 Execute。
- 基线尽可能建立；确实无法测量时，记录原因并选一个可复现的替代度量。
- 对比必须同环境、同数据、同测量方法。

## OPTIONAL STAGES

- Performance Specialist：热点平台、大规模改动或高成本优化时引入，见 `specialists/performance.md`。
- Review：独立评审，确认没有为指标牺牲正确性。
- Integrate：优化跨越 2+ 模块时执行。

## SKIPPED STAGES

- 无目标指标的优化：直接跳过，不凭直觉改代码。
- 功能扩展：优化任务不夹带新功能。

## SPECIAL RULES

- "感觉更快了"不算完成；必须有可比对的数值或可复现的度量差异。
- 一次只改一个变量，便于归因；多变量混合改动无法证明哪个生效。
- 不得以正确性、可读性或边界安全换取性能；这些属于不可简化项。
- 瓶颈定位先于优化：不做未定位的猜测式微调。

## VERIFICATION DEPTH

- standard 深度：优化前后对比 + 回归检查（原有功能不退化）。
- 涉及热路径重写时追加独立 Code Review。

## COMPLETION CONDITIONS

- 目标指标达成，或有明确记录的未达成结论与原因。
- 对比数据可复现，环境/数据集/测量方式已记录。
- 回归检查通过，无正确性或边界行为退化。
