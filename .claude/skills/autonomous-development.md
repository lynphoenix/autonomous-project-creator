# Autonomous Development - 自主开发技能

使用 Claude 驱动的自主编码代理从规范文档自动构建完整的应用程序。

## 何时使用

当您需要从规范文档自动创建应用程序时，使用此技能：

- **创建新项目**: "帮我创建一个待办事项应用"
- **继续开发**: "继续开发之前的项目"
- **查看进度**: "查看项目开发进度"

## 工作流程

### 1. 创建项目

告诉 Claude 您想创建什么项目：

```
"我想创建一个博客系统"
```

Claude 会：
1. 引导您创建项目规范
2. 初始化项目结构
3. 开始自主开发

### 2. 继续开发

如果开发被中断，只需说：

```
"继续开发博客系统项目"
```

Claude 会从中断处继续工作。

### 3. 查看进度

随时查看项目状态：

```
"查看项目进度"
```

## 环境配置

首次使用前需要设置环境变量：

```bash
# 必填：API 密钥
export ANTHROPIC_API_KEY='your-api-key-here'

# 可选：自定义 API 端点
export ANTHROPIC_BASE_URL=https://api.anthropic.com

# 可选：指定模型
export ANTHROPIC_MODEL=claude-sonnet-4-5-20250929
```

## 编写规范

在 `prompts/app_spec.txt` 中创建项目规范：

```markdown
# 项目名称

## 描述
简要描述项目目的和功能。

## 技术栈
- 前端: React + TypeScript
- 后端: Python + FastAPI
- 数据库: PostgreSQL

## 功能优先级

### P0 (核心功能)
- 用户注册/登录
- 创建/编辑文章
- 评论系统

### P1 (重要功能)
- 文章搜索
- 标签分类
- 用户个人资料

### P2 (增强功能)
- 文章分享
- 邮件通知
- 深色模式

## 测试要求
- 单元测试覆盖率 > 80%
- E2E 测试覆盖核心流程
```

## 命令参考

| 命令 | 说明 |
|------|------|
| `autonomous-create` | 创建新项目 |
| `autonomous-continue` | 继续开发 |
| `autonomous-status` | 查看进度 |

## 常见问题

**Q: 开发过程可以暂停吗？**
A: 可以，按 `Ctrl+C` 暂停，下次使用 `autonomous-continue` 继续。

**Q: 可以使用自定义 API 吗？**
A: 可以，设置 `ANTHROPIC_BASE_URL` 环境变量。

**Q: 项目保存在哪里？**
A: 默认在 `./autonomous_project`，可通过 `--project-dir` 指定。
