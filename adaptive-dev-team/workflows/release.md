# Release Workflow

> 共享生命周期、阶段顺序与"缺角色即跳过"规则见 `workflows/core.md`；本文件只声明差异。

## WHEN TO USE

- 版本交付、打包、发布准备、Changelog 与发布检查。
- 代码已完成，目标是让一个版本可发布。
- 不适用：发布前仍需写功能（先完成对应功能工作流）。

## REQUIRED STAGES

- 发布范围 → 版本就绪 → 必要检查 → 文档 / Changelog → 打包 → release candidate → 由用户控制远程发布 → Final Delivery。
- 版本就绪：确认所有纳入项已完成并通过各自验证，未完成项移出范围。
- 必要检查：构建、测试、依赖与版本号一致性、许可证与产物完整性。
- release candidate：在本地生成并验证候选产物，验证通过后再交用户决定是否远程发布。

## OPTIONAL STAGES

- DevOps Specialist：涉及 CI/CD、签名、制品仓库时引入，见 `specialists/devops-release.md`。
- Acceptance Reviewer：用户明确要求正式验收时引入。
- 回滚预案：面向生产发布时建议补。

## SKIPPED STAGES

- 自动远程发布：默认跳过，见 SPECIAL RULES。
- 功能开发与重构：release 不做代码改动；发布中发现的缺陷回到对应工作流修复并重新走一遍。

## SPECIAL RULES

- 默认禁止 `git push`、GitHub release 创建、`force push`、tag 上传与生产部署；除非用户明确授权。
- 远程发布动作始终由用户控制；agent 只准备候选产物与发布说明。
- 获批后仍需逐条确认目标（远端、分支、tag），不复用上一次的发布参数。
- 发布检查失败即停止，保持仓库在可发布或可回退状态，不半途推送。

## VERIFICATION DEPTH

- standard 深度：发布检查清单全项通过 + 候选产物在本地可安装/可运行。
- 涉及签名、制品仓库或生产配置时追加 DevOps 评审。

## COMPLETION CONDITIONS

- 发布范围、版本号、Changelog 与文档一致。
- 打包产物验证通过；release candidate 可供用户取用。
- 远程发布仅在用户明确授权后由用户完成，授权记录留在交付记录中。
