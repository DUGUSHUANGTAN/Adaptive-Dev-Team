# Core Lifecycle

所有工作流共享的唯一生命周期定义。本文件是真相来源；`workflows/<name>.md` 只声明差异，不重抄本文件。

## Stage Pipeline

```
Triage → 选择工作流 → 按需 Spec/Plan → Execute → 必要时 Integrate
→ 按深度 Verify → 按深度 Review → 必要时 Accept → Final Delivery
```

| Stage | 目的 | 何时执行 |
|---|---|---|
| Triage | 判定任务性质、风险、范围、owner | 永远 |
| 选择工作流 | 从 `workflows/` 选定一个主工作流 | 永远 |
| Spec | 明确交付物与验收标准 | 需求不明确或 Medium+ |
| Plan | 拆 Task DAG、定依赖与并行 | 多节点或多人 |
| Execute | 产出代码 / 文档 / 配置 | 永远 |
| Integrate | 合并跨模块产出、对齐接口契约 | 产出跨越 2+ 模块或 2+ owner |
| Verify | 可运行的校验（test / demo / assert） | 按工作流声明深度 |
| Review | 独立评审（正确性、质量） | 按工作流声明深度与风险 |
| Accept | 用户或验收者确认验收标准 | 按工作流声明深度 |
| Final Delivery | 交付 + 证据记录 | 永远 |

## Role Skip Rule

缺少的可选角色直接跳过，不为了流程强行生成角色。

- 只在 `REQUIRED STAGES` 或无触发条件命中时招募对应角色。
- 角色缺失不阻塞流程：由最近的已有 owner 承担。
- **跳过不需要逐项记账。** 默认保持安静；只有当下列任一条件成立时，才在交付记录里写一行 `理由`：
  - 该省略**影响风险**（例如没做本该做的安全审查）；
  - 该省略**影响验收**（例如验收标准依赖某个未跑的检查）；
  - 一个**通常预期的阶段被有意跳过**（不是"本工作流默认不需要"，而是"本来该有却跳过了"）；
  - 用户**明确要求**审计轨迹。
- 不适用时写"待补"是禁止的（会产生虚假欠账）；什么都不写是允许的，也是 LIGHT 的默认。
- 单 Builder 场景不创建 Builder Lead（见 `policies/team-composition.md`）。
- 宿主不支持子 Agent 时，按 `SKILL.md` §4 降级为单 Agent 的 role-separated passes（Planning / Implementation / Review）。这是 fallback：流程形状保持完整，但**不提供独立评审**，Review Pass 必须标记为 `non-independent self-review`，不得声称为与多 Agent 独立评审等价。

## Verification Depth

| 深度 | Verify | Review | Accept |
|---|---|---|---|
| light | 定向校验（单测 / 手动 demo / assert） | 允许 separate review pass，必须标记 non-independent self-review | 用户自验收 |
| standard | 功能 + 回归 | 独立 Code Review | 用户确认 |
| advanced | 逐节点验证 + 集成验证 | 独立 Code Review + 集成检查 | 必要时 Acceptance Reviewer |
| production | 各触发专家各自的验证 | 独立 Review + 触发专家 Review | Acceptance Reviewer |

## Shared Rules

- Ownership 唯一，写范围互斥，见 `protocols/ownership.md`。
- Verify / Review 失败回到 Execute，走 `protocols/fix-loop.md`。
- 完成判定以 `policies/definition-of-done.md` 为准，证据优先于声明。
- 跨工作流任务选一个主工作流，其余降级为阶段，不并行套用两套骨架。
- 工作流选择依据各文件 `WHEN TO USE`；无法判定时回退 `workflows/standard.md`。
