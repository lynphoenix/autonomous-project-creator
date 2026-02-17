# App Spec 编写指南

本文档帮助你编写高质量的项目需求文档，确保 AI Agent 能够构建出符合预期的应用。

---

## 完整模板

复制以下模板，填写你的项目信息：

```text
# 项目名称
[你的项目名称]

## 一句话描述
[用一句话描述这个项目是什么，解决什么问题]

## 技术栈

### 前端
- 框架：[React / Vue / Next.js / 其他]
- 语言：[TypeScript / JavaScript]
- 样式：[Tailwind CSS / CSS Modules / Styled Components]
- UI组件库：[shadcn/ui / Ant Design / Material UI / 无]
- 状态管理：[React Query / Zustand / Redux / Context]

### 后端
- 框架：[Express / FastAPI / NestJS / 其他]
- 语言：[TypeScript / Python / Go / 其他]
- 数据库：[PostgreSQL / MySQL / SQLite / MongoDB]
- 认证：[JWT / OAuth / Session / 无]

### 其他
- 部署：[Vercel / AWS / Docker / 本地]
- API风格：[REST / GraphQL / tRPC]

## 用户角色

### 角色1：[角色名称，如：普通用户]
- 可以做什么
- 不能做什么

### 角色2：[角色名称，如：管理员]
- 可以做什么
- 不能做什么

## 核心功能（按优先级排序）

### P0 - 必须有（MVP）

#### 功能模块1：[模块名称，如：用户认证]

1. [具体功能，如：用户注册]
   - 输入：邮箱、密码、确认密码
   - 验证：邮箱格式、密码强度
   - 成功后：跳转到登录页
   - 错误提示：邮箱已存在、密码不匹配

2. [具体功能，如：用户登录]
   - 输入：邮箱、密码
   - 验证：账号存在、密码正确
   - 成功后：跳转到首页，保存登录状态
   - 错误提示：账号不存在、密码错误
   - 记住我功能

#### 功能模块2：[模块名称]

...

### P1 - 应该有

...

### P2 - 可以有

...

## 页面结构

### 页面列表
1. `/` - 首页
2. `/login` - 登录页
3. `/register` - 注册页
4. `/dashboard` - 仪表盘
5. `/settings` - 设置页
...

### 导航结构
- 顶部导航：Logo、搜索、用户菜单
- 侧边栏：主导航菜单
- 底部：版权信息

## UI 设计规范

### 颜色
- 主色：#3B82F6（蓝色）
- 次色：#10B981（绿色）
- 警告：#F59E0B（橙色）
- 错误：#EF4444（红色）
- 背景：#FFFFFF / #F3F4F6
- 文字：#1F2937 / #6B7280

### 布局
- 最大宽度：1280px
- 侧边栏宽度：240px
- 内容内边距：24px
- 响应式断点：sm(640px) / md(768px) / lg(1024px) / xl(1280px)

### 字体
- 标题：Inter / 系统字体
- 正文：Inter / 系统字体
- 代码：JetBrains Mono

### 组件规范
- 按钮：圆角 8px，高度 40px
- 输入框：圆角 8px，高度 40px
- 卡片：圆角 12px，阴影
- 表格：斑马纹，悬停高亮

## API 接口设计

### 通用规范
- 基础路径：`/api/v1`
- 认证方式：Bearer Token (JWT)
- 返回格式：
  ```json
  {
    "success": true,
    "data": {},
    "message": "操作成功"
  }
  ```
- 错误格式：
  ```json
  {
    "success": false,
    "error": {
      "code": "VALIDATION_ERROR",
      "message": "邮箱格式不正确"
    }
  }
  ```

### 接口列表

#### 认证相关
- `POST /api/v1/auth/register` - 用户注册
- `POST /api/v1/auth/login` - 用户登录
- `POST /api/v1/auth/logout` - 用户登出
- `GET /api/v1/auth/me` - 获取当前用户

#### [模块名称]相关
- `GET /api/v1/xxx` - 获取列表
- `POST /api/v1/xxx` - 创建
- `GET /api/v1/xxx/:id` - 获取详情
- `PUT /api/v1/xxx/:id` - 更新
- `DELETE /api/v1/xxx/:id` - 删除

## 数据模型

### User（用户）
```json
{
  "id": "uuid",
  "email": "string, unique",
  "password": "string, hashed",
  "name": "string",
  "role": "enum: user, admin",
  "createdAt": "datetime",
  "updatedAt": "datetime"
}
```

### [模型名称]
```json
{
  "id": "uuid",
  "field1": "type",
  "field2": "type",
  "createdAt": "datetime",
  "updatedAt": "datetime"
}
```

## 非功能性需求

### 性能
- 页面首屏加载 < 2秒
- API 响应时间 < 200ms
- 支持 100 并发用户

### 安全
- 密码加密存储（bcrypt）
- JWT Token 过期时间 7天
- XSS 防护
- CSRF 防护
- SQL 注入防护

### 兼容性
- 浏览器：Chrome、Firefox、Safari、Edge（最新两个版本）
- 移动端：iOS Safari、Android Chrome
- 屏幕尺寸：320px - 1920px

### 可访问性
- 语义化 HTML
- ARIA 标签
- 键盘导航支持
- 颜色对比度符合 WCAG AA

## 验收标准

### 功能验收
- 所有 P0 功能正常工作
- 用户流程端到端测试通过
- 边界情况处理正确

### UI 验收
- 符合设计规范
- 响应式布局正确
- 无明显 UI bug

### 性能验收
- Lighthouse 评分 > 80
- 无控制台错误
- 无内存泄漏

## 不在范围内

以下功能本期不做：
- [功能1]
- [功能2]

## 参考资源

- 设计稿：[链接]
- API 文档：[链接]
- 竞品参考：[链接]
```

---

## 快速检查清单

写完后检查是否包含：

- [ ] 技术栈明确（前端/后端/数据库）
- [ ] 用户角色定义清楚
- [ ] 功能按优先级分类（P0/P1/P2）
- [ ] 每个功能有输入、输出、错误处理描述
- [ ] 页面结构和路由定义
- [ ] UI 颜色和布局规范
- [ ] API 接口列表和格式
- [ ] 数据模型定义
- [ ] 非功能性需求（性能、安全）
- [ ] 验收标准

---

## 示例：待办事项应用

```text
# 项目名称
TaskFlow - 个人待办事项管理应用

## 一句话描述
一个简洁高效的个人任务管理工具，帮助用户组织日常工作和生活。

## 技术栈

### 前端
- 框架：React 18
- 语言：TypeScript
- 样式：Tailwind CSS
- UI组件库：shadcn/ui
- 状态管理：React Query + Zustand

### 后端
- 框架：Express
- 语言：TypeScript
- 数据库：SQLite（本地存储）
- 认证：无（本地应用）

## 用户角色

### 用户
- 可以创建、编辑、删除自己的任务
- 可以对任务进行分类和标记优先级
- 可以设置任务截止日期
- 可以标记任务完成状态

## 核心功能

### P0 - 必须有

#### 任务管理
1. 创建任务
   - 输入：标题（必填）、描述（可选）、优先级、截止日期
   - 验证：标题不为空
   - 成功后：任务出现在列表中
   - 错误提示：请输入任务标题

2. 编辑任务
   - 可修改所有字段
   - 实时保存

3. 删除任务
   - 二次确认
   - 删除后不可恢复

4. 标记完成
   - 点击复选框切换状态
   - 完成的任务显示删除线

#### 任务列表
1. 显示所有任务
2. 按状态筛选（全部/进行中/已完成）
3. 按优先级排序
4. 搜索任务

### P1 - 应该有

#### 分类管理
1. 创建分类
2. 任务关联分类
3. 按分类筛选

#### 统计面板
1. 任务完成率
2. 今日/本周任务数量

## 页面结构

1. `/` - 任务列表（主页）
2. `/task/:id` - 任务详情
3. `/categories` - 分类管理

### 导航结构
- 顶部：Logo、搜索框、设置按钮
- 侧边栏：筛选器、分类列表

## UI 设计规范

### 颜色
- 主色：#3B82F6
- 成功：#10B981
- 警告：#F59E0B
- 错误：#EF4444
- 背景：#F9FAFB
- 卡片：#FFFFFF

### 布局
- 三栏布局：侧边栏(240px) + 主内容 + 详情面板
- 任务卡片高度：72px
- 响应式：移动端单栏

### 组件规范
- 任务卡片：圆角8px，悬停阴影
- 按钮：主按钮蓝色，次按钮灰色
- 输入框：灰色边框，聚焦蓝色

## API 接口设计

### 任务相关
- `GET /api/tasks` - 获取任务列表
- `POST /api/tasks` - 创建任务
- `GET /api/tasks/:id` - 获取任务详情
- `PUT /api/tasks/:id` - 更新任务
- `DELETE /api/tasks/:id` - 删除任务
- `PATCH /api/tasks/:id/toggle` - 切换完成状态

### 分类相关
- `GET /api/categories` - 获取分类列表
- `POST /api/categories` - 创建分类
- `PUT /api/categories/:id` - 更新分类
- `DELETE /api/categories/:id` - 删除分类

## 数据模型

### Task（任务）
```json
{
  "id": "uuid",
  "title": "string, required, max 100",
  "description": "string, optional, max 500",
  "priority": "enum: low, medium, high",
  "status": "enum: pending, completed",
  "dueDate": "datetime, optional",
  "categoryId": "uuid, optional",
  "createdAt": "datetime",
  "updatedAt": "datetime"
}
```

### Category（分类）
```json
{
  "id": "uuid",
  "name": "string, required, max 50",
  "color": "string, hex color",
  "createdAt": "datetime"
}
```

## 非功能性需求

### 性能
- 首屏加载 < 1秒
- 任务操作响应 < 100ms

### 存储
- 数据存储在浏览器 localStorage 或本地 SQLite
- 支持导出/导入 JSON

### 兼容性
- Chrome、Firefox、Safari 最新版
- 移动端响应式适配

## 验收标准

- 用户可以完成完整的任务管理流程
- 数据刷新后保留
- UI 美观、操作流畅
- 无控制台错误

## 不在范围内

- 用户账号系统
- 云同步
- 团队协作
- 提醒通知
```

---

## 提示

1. **越详细越好**：官方建议生成 200+ 测试用例，需求文档越详细，生成的测试越准确

2. **具体胜于抽象**：
   - ❌ "用户界面要好看"
   - ✅ "主色 #3B82F6，圆角 8px，卡片有阴影"

3. **包含边界情况**：
   - 空状态显示什么
   - 错误怎么提示
   - 加载状态如何展示

4. **明确的验收标准**：让 Agent 知道什么时候算"完成"
