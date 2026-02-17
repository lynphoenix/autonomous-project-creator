# Autonomous Coding 快速启动指南

完整的自动化开发流程，从需求到成品。

---

## 快速开始（3步）

### Step 1: 生成需求文档

```bash
cd claude-quickstarts/autonomous-coding

# 方式A: 交互式生成（推荐新手）
python create_app_spec.py

# 方式B: 手动编写（参考模板）
cp prompts/APP_SPEC_GUIDE.md prompts/app_spec.txt
# 然后编辑 app_spec.txt
```

### Step 2: 设置 API Key

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### Step 3: 启动开发

```bash
# 完整运行（直到所有功能完成）
python autonomous_agent_demo.py --project-dir ./my-project

# 或限制迭代次数（测试用）
python autonomous_agent_demo.py --project-dir ./my-project --max-iterations 5
```

---

## 目录结构

```
autonomous-coding/
├── autonomous_agent_demo.py   # 主入口
├── create_app_spec.py         # 需求文档生成器 ← 新增
├── agent.py                   # 会话循环逻辑
├── client.py                  # SDK 客户端配置
├── security.py                # 安全验证
├── progress.py                # 进度追踪
├── requirements.txt           # Python 依赖
│
└── prompts/
    ├── APP_SPEC_GUIDE.md      # 需求文档指南 ← 新增
    ├── app_spec.txt           # 你的需求文档
    ├── initializer_prompt.md  # 初始化提示词
    └── coding_prompt.md       # 编码提示词
```

---

## 使用流程

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: 生成需求文档                                        │
│  $ python create_app_spec.py                                │
│                                                             │
│  项目名称: 任务管理应用                                      │
│  一句话描述: 帮助用户管理日常任务                             │
│  前端框架 [React]:                                          │
│  后端框架 [Express]:                                        │
│  ...                                                        │
│  ✅ 已生成: app_spec.txt                                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 2: 检查并完善需求文档                                  │
│  $ cat prompts/app_spec.txt                                 │
│                                                             │
│  检查项:                                                    │
│  □ 技术栈是否正确                                           │
│  □ 功能是否完整                                             │
│  □ UI 规范是否明确                                          │
│  □ 验收标准是否清晰                                         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 3: 启动自动化开发                                      │
│  $ python autonomous_agent_demo.py --project-dir ./my-app   │
│                                                             │
│  [初始化阶段 - 10-30分钟]                                   │
│  → 生成 200+ 测试用例                                       │
│  → 创建项目结构                                             │
│  → 编写 init.sh                                            │
│                                                             │
│  [开发阶段 - 自动循环]                                      │
│  → 每次会话完成 1-3 个功能                                   │
│  → 自动测试验证                                             │
│  → 自动 git commit                                          │
│  → 3秒后继续下一轮                                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 4: 监控进度                                           │
│                                                             │
│  # 查看测试进度                                             │
│  $ cat generations/my-app/feature_list.json | \             │
│      grep '"passes": true' | wc -l                          │
│                                                             │
│  # 查看进度日志                                             │
│  $ cat generations/my-app/claude-progress.txt               │
│                                                             │
│  # 查看 git 历史                                            │
│  $ cd generations/my-app && git log --oneline -20           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 5: 验收测试                                           │
│  $ cd generations/my-app                                    │
│  $ ./init.sh                                                │
│                                                             │
│  浏览器访问 http://localhost:3000                           │
│  手动测试所有功能                                           │
└─────────────────────────────────────────────────────────────┘
```

---

## 需求文档质量检查清单

运行 `create_app_spec.py` 后，检查生成的文档：

### 必须包含

- [ ] **项目名称和描述** - 清晰说明是什么项目
- [ ] **技术栈** - 前端/后端/数据库明确
- [ ] **用户角色** - 谁使用这个系统
- [ ] **P0 功能列表** - 核心功能，至少 5-10 个
- [ ] **页面结构** - 主要页面和路由

### 建议包含

- [ ] **UI 颜色规范** - 主色/次色/背景色
- [ ] **API 接口设计** - 主要接口列表
- [ ] **数据模型** - 核心数据结构
- [ ] **验收标准** - 怎么算完成

### 可选包含

- [ ] P1/P2 功能 - 后续迭代功能
- [ ] 非功能性需求 - 性能、安全要求
- [ ] 不在范围内 - 明确边界

---

## 常见问题

### Q: 第一次运行要多久？

A: 初始化阶段需要 10-30 分钟，Agent 在生成 200+ 测试用例。输出很少，看起来像卡住了，其实在工作。

### Q: 中途断了怎么办？

A: 直接运行同样的命令，会自动从上次进度继续。

### Q: 怎么知道进度？

A: 查看文件：
- `feature_list.json` - 所有任务和完成状态
- `claude-progress.txt` - 人类可读的进度日志

### Q: 生成质量不满意怎么办？

A: 需求文档越详细，生成质量越好。重新编辑 `app_spec.txt`，然后：
```bash
# 删除旧项目，重新开始
rm -rf generations/my-app
python autonomous_agent_demo.py --project-dir ./my-app
```

### Q: 能改已经生成的代码吗？

A: 可以。Agent 每次会话都会先验证已有功能，发现问题会修复。你也可以手动修改代码，Agent 会尊重你的更改。

---

## 推荐的项目规模

| 项目类型 | 建议功能数 | 预计时间 |
|---------|-----------|---------|
| 学习/实验 | 10-20 | 1-2 小时 |
| 小型应用 | 30-50 | 3-5 小时 |
| 中型应用 | 50-100 | 1-2 天 |
| 大型应用 | 100-200+ | 3-5 天 |

---

## 命令速查

```bash
# 安装依赖
pip install -r requirements.txt

# 生成需求文档
python create_app_spec.py

# 启动开发
python autonomous_agent_demo.py --project-dir ./my-app

# 限制迭代次数
python autonomous_agent_demo.py --project-dir ./my-app --max-iterations 10

# 指定模型
python autonomous_agent_demo.py --project-dir ./my-app --model claude-sonnet-4-5-20250929

# 查看进度
cat generations/my-app/claude-progress.txt
grep '"passes": true' generations/my-app/feature_list.json | wc -l
```

---

## 下一步

1. 运行 `python create_app_spec.py` 创建你的第一个项目
2. 或者直接复制 `prompts/APP_SPEC_GUIDE.md` 中的模板，手动编写需求
3. 运行 `python autonomous_agent_demo.py` 开始自动化开发
