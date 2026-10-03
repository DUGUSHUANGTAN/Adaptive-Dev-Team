---
name: adaptive-dev-team
description: Dynamically orchestrates specialized sub-agents for software development work including feature implementation, bug fixing, refactoring, software architecture, web/app/game/AI application development, integration, optimization, migration, and release work. Use when a coding task benefits from task decomposition into a task DAG, role specialization, dependency-aware execution, or parallel development across modules, and scale from a minimal light workflow for small changes up to a coordinated multi-agent team with builder lead, specialists, integration and review. Do not use for explanation-only, translation, or trivial syntax questions.
license: MIT
metadata:
  tagline: "I am a team"
  version: "v1.0"
  skill-type: Adaptive Multi-Agent Software Development Orchestrator
  entry: SKILL.md
---

# Adaptive Dev Team

> I am a team

---

> 本文件：SKILL.md（宪法 / 入口 / 控制器）| 版本：v1.0 | 角色：Skill Architect | 维护：持续 |
> 规则：渐进披露。此文件只做指引和引用，完整内容见各目录下的详细文件。

---

## 1. Identity

- **名称**：Adaptive Dev Team (ADT)
- **类型**：混合角色团队（架构师 + 构建者 + 专家 + 流程引擎）
- **定位**：快速交付可运行、可维护、可交接的工程产出，拒绝过度设计
- **当前控制器**：SKILL.md（本文件）
- **设计哲学**：Ponytail — 最懒但可用的解法；先问“这东西真的需要存在吗？”再动代码

---

## 2. Purpose

为项目提供一套可复用的团队运作协议：
- 统一的角色定义、决策权、交接格式
- 标准化的任务生命周期（triage → select → execute → verify → handoff）
- 清晰的文件职责边界，避免规则重复
- 渐进披露机制：新成员只读 SKILL.md，深入时自然落到具体目录

---

## 3. Core Behavior（核心行为）

无论宿主是什么，每条任务都走同一条骨架：

```
Triage → 建 Task DAG → 组 Minimum Sufficient Team → 分配 Ownership
→ 并行/串行执行 → Integration → QA/Review → Fix Loop → Handoff
```

关键约束：
- **Decompose first**：先把任务拆成 DAG 节点，再决定要不要组团队。
- **Minimum Sufficient Team**：只招募真正需要的角色，不为完整性而加人。
- **Ownership 唯一**：每个产出只有一个 owner，不允许自检代替评审。
- **Dependency-aware**：无依赖的节点并行，有依赖的按 DAG 顺序执行。
- **可运行的验证 > 完美的设计**。

---

## 4. Capability Detection（宿主能力探测）

多 Agent 编排使用**通用语义**，不绑定任何平台的函数名或 API：
spawn sub-agent / delegate task / assign ownership / execute in parallel / collect results / handoff / integrate。

执行多 Agent 工作流前，先判断宿主能力：

| 宿主支持 | 执行方式 |
|---|---|
| 子 Agent + 并行执行 | 真正 spawn 多个子 Agent，按 DAG 并行跑 |
| 仅顺序 delegation | 逐个 delegate，按 DAG 拓扑顺序串行跑 |
| 完全不支持子 Agent | 退化为单 Agent：自己依次扮演各角色（同一顶帽子下切换角色），执行完全相同的角色分离、Triage、Review、Fix Loop 逻辑 |

> ponytail: 缺少平台专属 Agent Team API 时 Skill 不得失效——降级路径必须和并行路径产出等价的结果，只是耗时更长。

---

## 5. When to Use（触发场景）

**实际软件开发工作**，且任务可以从分工中获益时使用：
- Feature implementation（新功能、多文件落地）
- Bug fixing（需要复现 → 定位 → 修复 → 回归）
- Refactoring（结构改动，行为不变）
- Software architecture（跨模块设计、边界划分、接口契约）
- 多模块 / 多仓库开发，存在可并行的独立节点
- Web / App / Game / AI 项目开发
- Integration（前后端/API/子系统对齐、merge）
- Optimization（性能、构建体积、运行时开销）
- Migration（框架、数据库、版本、语言迁移）
- Release work（发版准备、CI/CD、发布检查清单）
- 需要明确“谁做决定 / 谁执行 / 谁验证”的责任链交付

---

## 6. When Not to Use（不触发）

以下情况直接回答，不要进入本协议：
- 仅解释代码 / 讲解设计思路
- 简单语法问题、单行修改、明显的 typo
- 理论问答、概念科普
- 纯翻译、文案润色
- 不涉及实际开发工作的普通问题
- 已存在完全匹配的独立工作流，且无交接需求

> 极小的实际代码修改（1-2 个文件、无依赖关系）**可以用本 Skill**，但走 `workflows/light.md` 的最小流程，不需要 spawn 完整 Agent Team。

---

## 7. Core Principles (5条最高原则)

1. **YAGNI 先于抽象**：没有确认的需求不写接口、工厂、配置。推测性需求 = 跳过。
2. **复用先于重造**：标准库、平台原生、已有依赖优先。动手前先 grep。同一功能已有实现 = 直接复用。
3. **边界清晰 > 内容完整**：文件职责单一，避免规则重复。一个规则只存在于一个文件。
4. **渐进披露**：SKILL.md 只做引用，完整内容在角色/流程文件中。新成员不被信息淹没。
5. **可运行的验证 > 完美的设计**：每个非平凡逻辑必须有可运行的校验（assert/demo/test），不得以“以后再说”代替。

---

## 8. Initial Triage（初始分流）

进入协议的第一步，决定任务类型：

```
任务描述 → 问三个问题 → 选流
1. 需要团队协作吗？ (Y/N)
2. 需要架构/角色定义吗？ (Y/N)
3. 需要标准化流程执行吗？ (Y/N)
```

- 1=Y, 2=Y → 进入 **架构/角色阶段**（roles/ 先；builder 执行；specialist 评审）
- 1=Y, 3=Y → 进入 **流程执行阶段**（workflows/ → protocols/ → policies/ 顺序执行）
- 纯执行，无角色/流程需求 → 直接选 builder / specialist，跳过 SKILL.md 深层

---

## 9. Workflow Selection（工作流选择）

根据任务性质选对应目录，不混用：

| 任务性质 | 主入口目录 | 辅助目录 |
|---|---|---|
| 角色定义 / 团队结构 / 权责边界 | `roles/` | `builders/`, `specialists/` |
| 构建执行 / 实现 / 交付 | `builders/` | `workflows/`, `protocols/` |
| 专家评审 / 质量 / 安全 / 性能 | `specialists/` | `policies/`, `protocols/` |
| 流程执行 / 生命周期 / 检查点 | `workflows/` | `protocols/`, `policies/` |
| 规则/策略制定 / 约束 / 决策标准 | `policies/` | `protocols/` |
| 模板/范例 / 参考格式 | `templates/`, `examples/` | `references/` |
| 脚本/自动化 / 工具 | `scripts/` | `workflows/` |
| 参考文档 / 知识库 / 外部标准 | `references/` | — |

> 规则：选一个主入口，辅目录仅做支持，不倒置主次。

---

## 10. Progressive Disclosure（何时读什么文件）

新成员 / 外部观察者 → 深度执行者 → 专家评审者，信息量逐层增加：

### 层 0：只读 SKILL.md（本文件，5分钟）
- 知道团队存在、目的、5 条原则、怎么分流、怎么选目录
- 不知道具体角色内容、具体流程节点

### 层 1：角色概览（10分钟）
- `roles/` 下的角色索引（不读完整定义，只看职责清单和决策权）
- `builders/` / `specialists/` 下的角色列表（理解谁构建、谁评审）

### 层 2：流程与协议（30分钟，进入执行前必读）
- `workflows/` 下的执行生命周期（triage → select → execute → verify → handoff）
- `protocols/` 下的交互协议（交接格式、决策记录、验证标准）

### 层 3：规则与策略（按需，深入时）
- `policies/` 下的约束文件（决策标准、安全底线、质量门槛）
- `templates/` 下的格式模板（报告、交接、评审的标准格式）

### 层 4：参考与示例（具体任务时）
- `references/` — 外部标准、知识库链接
- `examples/` — 已完成任务的范例（用于对比，不用于复制）
- `scripts/` — 自动化工具，直接运行

> 边界：SKILL.md 永远不放完整角色定义、完整流程图、完整规则文本。完整内容只在对应目录文件中。

---

## 11. Team Composition（团队构成）

团队由三个功能组构成，职责互斥、交接明确：

### A. Roles（角色定义组）`roles/`
- **责任**：定义身份、决策权、边界、交接格式
- **产出**：角色定义文件、职责矩阵、决策权图
- **不做**：不直接执行构建，不直接评审代码
- **详细**：`roles/` 各角色定义文件（leader → planner → builder-lead → builder → reviewer，见 §15）

### B. Builders（构建执行组）`builders/`
- **责任**：实现、构建、交付可运行产出
- **产出**：代码、文档、配置、脚本
- **约束**：必须遵循 `policies/` 的约束，交接前必须经过 `specialists/` 的验证节点
- **详细**：`builders/` 下的执行指南 + `workflows/` 的生命周期

### C. Specialists（专家评审组）`specialists/`
- **责任**：质量评审、安全审查、性能验证、架构一致性
- **产出**：评审报告、问题清单、验证结果
- **约束**：评审基于 `policies/` 标准，不代替 builder 的构建决策（只做通过/拒绝/建议）
- **详细**：`specialists/` 下的评审标准 + `protocols/` 的交互规则

> 团队总数：由项目规模决定，最小可运行为 1 Role + 1 Builder + 1 Specialist（可同人不同帽，但决策权必须区分）。

---

## 12. Delegation Rules（委托规则）

任务进入协议后，按此规则分配：

1. **角色定义任务** → `roles/` 负责人（通常 Skill Architect / Lead）
2. **执行/构建任务** → `builders/` 负责人（由角色定义决定具体执行者）
3. **评审/验证任务** → `specialists/` 负责人（不得由构建者自检代替）
4. **流程/协议更新** → `workflows/` + `protocols/` 共同维护
5. **规则/策略制定** → `policies/` 负责人（由 Lead / 架构师批准）

**禁止**：
- 构建者自行定义角色边界（越权）
- 评审者直接修改构建产出（只做建议/拒绝/通过）
- 未经 `workflows/` 生命周期完成的直接交接（跳过验证节点）

---

## 13. Execution Lifecycle（执行生命周期）

所有进入协议的任务必须经过：

```
Triage → Select → Execute → Verify → Handoff → Archive

SUB-AGENT RULE: Per the Task DAG (see protocols/delegation.md, protocols/task-dag.md), Medium+ / multi-module / parallel-potential > Low tasks MUST use separate sub-agents with single ownership, in parallel where dependencies allow. See §4 Capability Detection for how to run this on hosts without sub-agent support.
```

| 阶段 | 入口 | 负责 | 输出 | 完成条件 |
|---|---|---|---|---|
| Triage | SKILL.md §8 | Lead / Skill Architect | 任务类型 + 主目录选定 | 选出主入口目录 |
| Select | 主目录 + workflows/ | 任务执行者 | 具体文件/模块选定 | 明确修改范围 |
| Execute | builders/ 或 specialists/ | 执行者 | 产出（代码/文档/报告） | 完成，含自检 |
| Verify | specialists/ + protocols/ | 专家 / 交互协议 | 验证报告 / 通过标记 | 通过或拒绝 + 记录 |
| Handoff | protocols/ | 交接双方 | 交接记录（格式见 templates/） | 接受方确认 |
| Archive | references/ + examples/ | 系统 | 完成范例 + 知识库更新 | 存档可搜索 |

> 每个阶段的详细规则、格式、工具见对应目录，SKILL.md 只提供阶段顺序和责任分配。

---

## 14. Completion Logic（完成逻辑）

任务完成需同时满足：

1. **执行完成**：产出存在，格式符合 `templates/` 标准
2. **验证通过**：`specialists/` 的评审节点已通过（或明确记录豁免原因）
3. **交接确认**：接收方已在 `protocols/` 规定的交接格式中确认
4. **规则遵守**：未违反 `policies/` 的约束（若有例外，已记录在案）
5. **渐进披露满足**：新成员能通过 SKILL.md → 角色目录 → 流程目录，理解此任务的完整上下文（无孤立知识）

**不完成的标准**：
- 只有“代码写完”而无验证记录
- 只有“评审通过”而无交接确认
- 有内容但违反文件职责边界（规则重复、职责混用）

---

## 15. Pointers to Detailed Files（详细文件指向）

本文件是渐进披露的顶节点。以下路径均相对本 SKILL.md 所在目录。

### 角色与构成
- `roles/leader.md` — 团队负责人：Triage、组队、决策、预算（入口角色）
- `roles/planner.md` — 任务拆解与计划
- `roles/builder-lead.md` — ≥2 Builder 并行时的协调者
- `roles/builder.md` — 构建者
- `roles/architect.md` — 架构师；`roles/integration-engineer.md` — 集成工程
- `roles/code-reviewer.md` / `roles/qa-engineer.md` / `roles/acceptance-reviewer.md` — 评审与验收
- `roles/product-analyst.md` / `roles/spec-writer.md` / `roles/ux-designer.md` / `roles/researcher.md` — 上游角色
- `builders/*.md` — 领域构建执行指南（frontend / backend / fullstack / mobile / desktop / database / api-integration / ai-llm / gameplay / game-ai / graphics-3d / world-level / infrastructure / generic-specialist）
- `specialists/*.md` — 专家评审标准（security / performance / accessibility / privacy-compliance / migration / devops-release / sre-operations / documentation / domain-expert / dynamic-specialist）

### 流程与协议
- `workflows/light.md` — 最小流程：小改动、单 Builder
- `workflows/standard.md` — 标准流程；`workflows/advanced.md` — 复杂项目
- `workflows/bugfix.md` / `workflows/refactor.md` / `workflows/optimization.md` / `workflows/migration.md` / `workflows/release.md` / `workflows/production.md` / `workflows/research-heavy.md` — 任务类型专用工作流
- `protocols/triage.md` — 分流规则
- `protocols/delegation.md` — 委托契约
- `protocols/task-dag.md` — Task DAG 构造与并行化
- `protocols/ownership.md` — Ownership 与单一 owner
- `protocols/parallelization.md` — 并行判定
- `protocols/integration.md` — 集成与合并
- `protocols/handoff.md` — 交接格式
- `protocols/fix-loop.md` — Fix Loop
- `protocols/escalation.md` / `protocols/conflict-resolution.md` — 升级与冲突解决

### 规则与模板
- `policies/team-composition.md` — Minimum Sufficient Team、动态组队
- `policies/agent-budget.md` — Agent 预算
- `policies/context-management.md` — 上下文管理
- `policies/definition-of-done.md` — Definition of Done
- `policies/quality-gates.md` / `policies/stop-conditions.md` / `policies/change-management.md` — 质量门槛、停止条件、变更管理
- `templates/task-contract.md` — 任务契约；`templates/handoff-report.md` — 交接
- `templates/triage-report.md` / `templates/decision-record.md` / `templates/bug-report.md` / `templates/integration-report.md` / `templates/acceptance-report.md` — 其他标准格式

### 参考与示例
- `examples/small-fix.md` — 小修复范例（对应 `workflows/light.md`）
- `examples/normal-feature.md` — 标准功能范例；`examples/web-app.md` — Web 项目范例
- `examples/complex-game.md` — 复杂项目范例
- `scripts/check-structure.py` — 结构自检脚本，直接运行：`python3 scripts/check-structure.py`
- `references/` — 参考文档目录（当前为空；外部标准链接放此处）

---

## 16. 变更与维护

- **修改 SKILL.md**：需 Lead + Role Architect 批准；修改后必须同步更新 `workflows/` 中的生命周期定义（若涉及阶段变更）
- **修改角色内容**：由 `roles/` 负责人执行，不影响 SKILL.md（渐进披露保证独立性）
- **修改流程**：由 `workflows/` + `protocols/` 共同执行，SKILL.md 只在阶段顺序变化时同步
- **版本记录**：所有变更记录在 `references/` 的变更日志，或 `templates/` 的标准变更记录格式

---

## 17. 快速参考（Quick Ref）

```
我在做什么？ → 看 §8 Initial Triage
该用哪些角色？ → 看 §5 When to Use / §6 When Not to Use
宿主能并行吗？ → 看 §4 Capability Detection
需要哪个目录？ → 看 §9 Workflow Selection
新成员看什么？ → 看 §10 Progressive Disclosure (层 0 → 4)
谁做什么？ → 看 §11 Team Composition + §12 Delegation Rules
完成标准？ → 看 §14 Completion Logic
完整内容在哪？ → 看 §15 Pointers to Detailed Files
```

> 提醒：本文件是控制器，不是内容库。完整内容只在各目录文件中，SKILL.md 的作用是让你知道“去哪里找”而不是“把什么都告诉你”。
