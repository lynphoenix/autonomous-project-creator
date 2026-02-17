# Autonomous Project Creator - 自主项目构建器

由 Claude 驱动的自主编码代理，可以根据规范文档自动构建完整的应用程序。本工具采用双代理模式（初始化器 + 编码代理），跨多个会话系统性地实现功能开发。

## 快速开始

### 方式一：作为 Claude Code Plugin 使用（推荐）

这是最简单的方式，只需安装 plugin，Claude 就能自动使用。

#### 安装步骤

1. **克隆仓库到 Claude plugins 目录**
```bash
# macOS/Linux
cd ~/.claude/plugins
git clone https://github.com/lynphoenix/autonomous-project-creator.git

# 或者克隆到其他位置然后创建符号链接
git clone https://github.com/lynphoenix/autonomous-project-creator.git ~/my-plugins/autonomous-project-creator
ln -s ~/my-plugins/autonomous-project-creator ~/.claude/plugins/autonomous-project-creator
```

2. **安装依赖**
```bash
cd ~/.claude/plugins/autonomous-project-creator
pip install -r requirements.txt
```

3. **配置环境变量**
```bash
# 方式 A: 直接设置环境变量
export ANTHROPIC_API_KEY='your-api-key-here'

# 方式 B: 创建 .env 文件（推荐）
cp .env.example .env
# 编辑 .env 文件，填入您的 API 密钥
```

4. **重启 Claude Code**

#### 使用方法

安装完成后，在 Claude Code 中直接对话：

```
# 创建新项目
"帮我创建一个待办事项应用"

# 继续开发
"继续之前的项目"

# 查看进度
"项目开发到哪了？"
```

Claude 会自动调用 plugin 完成任务。

---

### 方式二：作为独立工具使用

如果您不想使用 plugin 模式，也可以作为独立工具运行。

#### 安装

```bash
# 克隆仓库
git clone https://github.com/lynphoenix/autonomous-project-creator.git
cd autonomous-project-creator

# 安装 Python 依赖
pip install -r requirements.txt
```

#### 配置

```bash
# 设置 API 密钥
export ANTHROPIC_API_KEY='your-api-key-here'

# 可选：使用自定义 API 端点
export ANTHROPIC_BASE_URL=https://api.anthropic.com
export ANTHROPIC_MODEL=claude-sonnet-4-5-20250929
```

#### 运行

```bash
# 交互式创建规范（首次使用推荐）
python create_app_spec.py

# 运行自主开发
python autonomous_agent_demo.py --project-dir ./my_project

# 指定模型
python autonomous_agent_demo.py --project-dir ./my_project --model claude-sonnet-4-5-20250929

# 限制迭代次数
python autonomous_agent_demo.py --project-dir ./my_project --max-iterations 5
```

---

## 功能特性

- **自主开发**: 从文本规范自动构建应用程序
- **多会话支持**: 跨多个会话持续工作，自动跟踪进度
- **安全防护**: 操作系统级沙盒、文件系统限制、Bash 命令白名单
- **浏览器自动化**: 内置 Puppeteer 集成，用于端到端测试
- **灵活配置**: 支持自定义模型、API 端点和功能数量

## 编写规范

在 `prompts/app_spec.txt` 中创建您的应用程序规范，参考 `prompts/APP_SPEC_GUIDE.md` 中的指南。

关键要素：
- 清晰的项目描述
- 技术栈偏好
- P0/P1/P2 功能优先级
- 测试要求
- UI 设计规范

## 项目结构

```
autonomous-project-creator/
├── .claude/
│   ├── plugin.json              # Plugin 配置
│   ├── commands/                # 命令定义
│   │   ├── autonomous-create.md
│   │   ├── autonomous-continue.md
│   │   └── autonomous-status.md
│   └── skills/                  # 技能定义
│       └── autonomous-development.md
├── autonomous_agent_demo.py     # 主入口
├── create_app_spec.py           # 交互式规范生成器
├── agent.py                     # 代理会话逻辑
├── client.py                    # Claude SDK 客户端配置
├── security.py                  # Bash 命令白名单
├── progress.py                  # 进度跟踪
├── requirements.txt             # Python 依赖
├── .env.example                 # 环境变量模板
├── README.md                    # 本文件
└── prompts/
    ├── APP_SPEC_GUIDE.md        # 规范编写指南
    ├── app_spec.txt             # 应用程序规范模板
    ├── initializer_prompt.md    # 首次会话提示
    └── coding_prompt.md         # 后续会话提示
```

## 工作原理

### 双代理模式

1. **初始化代理（第 1 次会话）**：
   - 读取 `app_spec.txt`
   - 创建包含测试用例的 `feature_list.json`
   - 设置项目结构
   - 初始化 git 仓库

2. **编码代理（第 2 次及后续会话）**：
   - 从上次会话中断处继续
   - 系统性地实现功能
   - 标记测试为通过
   - 提交进度

### 会话管理

- 每次会话使用全新的上下文
- 通过 `feature_list.json` 和 git 提交持久化进度
- 会话间自动继续（3 秒延迟）
- 按 `Ctrl+C` 暂停；运行相同命令恢复

## 配置选项

### 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `ANTHROPIC_API_KEY` | 您的 Anthropic API 密钥 | 必填 |
| `ANTHROPIC_BASE_URL` | API 基础 URL | `https://api.anthropic.com` |
| `ANTHROPIC_MODEL` | 使用的模型 | `claude-sonnet-4-5-20250929` |
| `DISABLE_SANDBOX` | 禁用沙盒（不推荐） | `false` |

### 自定义 API 端点

您可以使用其他兼容的 API 提供商，例如 302.ai：

```bash
# 在 .env 文件中或命令行设置
export ANTHROPIC_BASE_URL=https://api.302.ai
export ANTHROPIC_MODEL=glm-4.7-coding-preview
```

## 安全模型

本工具采用纵深防御安全策略：

1. **操作系统级沙盒**: 隔离的 bash 环境
2. **文件系统限制**: 操作仅限于项目目录
3. **Bash 白名单**: 仅允许特定命令

查看 `security.py` 获取完整的命令白名单。

## 服务器部署

### 在新服务器上快速部署

```bash
# 1. 安装 Claude Code (如果尚未安装)
npm install -g @anthropic-ai/claude-code

# 2. 克隆 plugin 到 plugins 目录
cd ~/.claude/plugins
git clone https://github.com/lynphoenix/autonomous-project-creator.git

# 3. 安装依赖
cd autonomous-project-creator
pip install -r requirements.txt

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入 API 密钥

# 5. 完成！现在可以使用了
claude  # 启动 Claude Code
```

然后在 Claude Code 中说："帮我创建一个项目"

### 在 219 服务器（阿里云）上部署

```bash
# SSH 连接到服务器
ssh root@47.99.75.219

# 安装依赖
pip3 install -r requirements.txt

# 设置 API 密钥
export ANTHROPIC_API_KEY='your-key-here'

# 运行项目
python3 autonomous_agent_demo.py --project-dir ./my_project
```

### 在 H100 服务器上部署

同上 - 本工具基于 Python，可在任何装有 Python 3.10+ 的 Linux 服务器上运行。

## 故障排除

### "首次运行时似乎卡住了"
这是正常的！初始化代理正在生成详细的测试用例。请关注 `[Tool: ...]` 输出。

### "命令被安全钩阻止"
代理尝试了白名单之外的命令。如需要，可将其添加到 `security.py` 的 `ALLOWED_COMMANDS` 中。

### "API 密钥未设置"
确保已导出 `ANTHROPIC_API_KEY`：
```bash
echo $ANTHROPIC_API_KEY  # 应显示您的密钥，不应为空
```

### ModuleNotFoundError: No module named 'claude_code_sdk'
请安装依赖：
```bash
pip install -r requirements.txt
```

## 许可证

MIT License - 详见 LICENSE 文件

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 支持

如有问题或疑问：
- 在 GitHub 上提交 issue
- 查看现有文档 `QUICKSTART.md`
- 参考 `prompts/APP_SPEC_GUIDE.md` 了解规范编写帮助
