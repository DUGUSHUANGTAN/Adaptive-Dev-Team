# Production Workflow

> 共享生命周期、阶段顺序与"缺角色即跳过"规则见 `workflows/core.md`；本文件只声明差异。

## WHEN TO USE

- 面向真实用户/生产环境交付，或带合规、可靠性、可运维性要求的改动。
- 注意：本工作流不等于"advanced + 全部专家"，只按 Trigger 扩编。

## REQUIRED STAGES

- 采用 `workflows/advanced.md` 骨架：Spec → Architect（按需） → Planner → Builder Lead（仅 ≥2 Builders） → Parallel Builders → Integration → QA → Code Review。
- 叠加：每个命中的 Trigger 必须由对应专家完成评审，结果进入 DoD。
- 最后补 Acceptance：Acceptance Reviewer 对验收标准逐条给出 Pass / Partial / Fail。

## OPTIONAL STAGES

| Trigger | 加入的专家 |
|---|---|
| 认证授权、输入边界、密钥、敏感依赖 | Security |
| 热路径、大数据量、延迟/吞吐预算 | Performance |
| 用户界面变更 | Accessibility |
| 个人数据、日志留存、跨境/合规 | Privacy |
| 部署方式、回滚策略、环境配置 | DevOps |
| 可观测性、容量、值班、故障恢复 | SRE |

## SKIPPED STAGES

- 未命中的专家角色：直接跳过，不"顺手跑一遍"。
- Product Analyst：需求已明确时跳过。

## SPECIAL RULES

- Trigger 判定写进交付记录（命中或未命中都记一行），避免"全专家默认上线"。
- 生产改动必须可回滚；无回滚路径时先补回滚路径再 Execute。

## VERIFICATION DEPTH

- production：各触发专家各自的验证 + 集成验证 + 独立 Review + 专家 Review。
- 未触发专家的验证项从 DoD 中删除，而不是标记为未完成。

## COMPLETION CONDITIONS

- 命中的每个 Trigger 都有专家结论，集成验证、独立 Review 通过，回滚路径已验证。
- Acceptance Reviewer 出具 Pass；Partial / Fail 不得交付，见 `protocols/handoff.md`（FORBIDDEN: Final Delivery before a required Acceptance）。
