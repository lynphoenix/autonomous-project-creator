#!/usr/bin/env python3
"""
App Spec 生成器
===============

交互式引导用户创建高质量的项目需求文档。

用法:
    python create_app_spec.py
    python create_app_spec.py --output my_spec.txt
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path


def ask(question: str, default: str = "", required: bool = True) -> str:
    """交互式提问"""
    prompt = f"\n{question}"
    if default:
        prompt += f" [{default}]"
    prompt += ": "

    while True:
        answer = input(prompt).strip()
        if answer:
            return answer
        if default:
            return default
        if not required:
            return ""
        print("此项为必填，请输入内容")


def ask_multiline(question: str) -> list:
    """多行输入"""
    print(f"\n{question}")
    print("(输入空行结束)")
    lines = []
    while True:
        line = input("  - ").strip()
        if not line:
            break
        lines.append(line)
    return lines


def ask_yes_no(question: str, default: bool = True) -> bool:
    """是/否问题"""
    default_str = "Y/n" if default else "y/N"
    while True:
        answer = input(f"\n{question} [{default_str}]: ").strip().lower()
        if not answer:
            return default
        if answer in ("y", "yes", "是"):
            return True
        if answer in ("n", "no", "否"):
            return False
        print("请输入 y 或 n")


def generate_spec(data: dict) -> str:
    """生成 app_spec.txt 内容"""
    spec = f"""# 项目名称
{data['name']}

## 一句话描述
{data['description']}

## 技术栈

### 前端
- 框架：{data['frontend_framework']}
- 语言：{data['frontend_language']}
- 样式：{data['frontend_style']}
- UI组件库：{data['frontend_ui']}

### 后端
- 框架：{data['backend_framework']}
- 语言：{data['backend_language']}
- 数据库：{data['database']}
- 认证：{data['auth']}

## 用户角色

"""
    for role in data['roles']:
        spec += f"### {role['name']}\n"
        for permission in role['permissions']:
            spec += f"- {permission}\n"
        spec += "\n"

    spec += "## 核心功能\n\n"

    for priority, label in [("p0", "P0 - 必须有（MVP）"), ("p1", "P1 - 应该有"), ("p2", "P2 - 可以有")]:
        features = data.get(priority, [])
        if features:
            spec += f"### {label}\n\n"
            for feature in features:
                spec += f"#### {feature['name']}\n\n"
                spec += f"{feature['description']}\n\n"
                if feature.get('steps'):
                    spec += "**测试步骤：**\n"
                    for i, step in enumerate(feature['steps'], 1):
                        spec += f"{i}. {step}\n"
                    spec += "\n"
            spec += "\n"

    spec += f"""## 页面结构

{data['pages']}

## UI 设计规范

### 颜色
- 主色：{data['primary_color']}
- 次色：{data['secondary_color']}
- 背景：{data['background_color']}

### 布局
- 最大宽度：{data.get('max_width', '1280px')}
- 响应式断点：sm(640px) / md(768px) / lg(1024px) / xl(1280px)

## 非功能性需求

### 性能
- 页面首屏加载 < 2秒
- API 响应时间 < 200ms

### 安全
- 密码加密存储
- XSS 防护
- CSRF 防护

## 验收标准

- 所有 P0 功能正常工作
- 用户流程端到端测试通过
- 符合 UI 设计规范
- 无控制台错误

## 不在范围内

{data.get('out_of_scope', '暂无')}

---
生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    return spec


def main():
    parser = argparse.ArgumentParser(description="App Spec 生成器")
    parser.add_argument("--output", "-o", default="app_spec.txt", help="输出文件名")
    args = parser.parse_args()

    print("=" * 50)
    print("  App Spec 生成器")
    print("  帮助你创建高质量的项目需求文档")
    print("=" * 50)

    data = {}

    # 基本信息
    print("\n【基本信息】")
    data['name'] = ask("项目名称")
    data['description'] = ask("一句话描述项目（解决什么问题）")

    # 技术栈
    print("\n【技术栈】")
    print("\n前端技术:")
    data['frontend_framework'] = ask("框架", "React")
    data['frontend_language'] = ask("语言", "TypeScript")
    data['frontend_style'] = ask("样式方案", "Tailwind CSS")
    data['frontend_ui'] = ask("UI组件库", "shadcn/ui")

    print("\n后端技术:")
    data['backend_framework'] = ask("框架", "Express")
    data['backend_language'] = ask("语言", "TypeScript")
    data['database'] = ask("数据库", "SQLite")
    data['auth'] = ask("认证方式", "JWT")

    # 用户角色
    print("\n【用户角色】")
    roles = []
    while True:
        role_name = ask("角色名称（如：用户、管理员）", required=False)
        if not role_name:
            break
        print(f"  {role_name} 可以做什么？（输入空行结束）")
        permissions = []
        while True:
            perm = input("    - ").strip()
            if not perm:
                break
            permissions.append(perm)
        roles.append({"name": role_name, "permissions": permissions})
        if not ask_yes_no("继续添加角色？", default=False):
            break
    data['roles'] = roles

    # 核心功能
    print("\n【核心功能】")
    print("按优先级输入功能（P0=必须有, P1=应该有, P2=可以有）")

    for priority in ["p0", "p1", "p2"]:
        label = {"p0": "P0（必须有）", "p1": "P1（应该有）", "p2": "P2（可以有）"}[priority]
        if not ask_yes_no(f"是否添加 {label} 功能？", default=(priority == "p0")):
            continue

        features = []
        while True:
            feature_name = ask(f"{label} 功能名称", required=False)
            if not feature_name:
                break
            feature_desc = ask("功能描述", default="...")
            steps = ask_multiline("测试步骤（用户如何验证这个功能）")
            features.append({
                "name": feature_name,
                "description": feature_desc,
                "steps": steps
            })
            if not ask_yes_no("继续添加功能？", default=True):
                break
        data[priority] = features

    # 页面结构
    print("\n【页面结构】")
    pages = ask_multiline("列出主要页面（如：首页、登录页、设置页）")
    data['pages'] = "\n".join(f"- {p}" for p in pages) if pages else "待补充"

    # UI 规范
    print("\n【UI 设计规范】")
    data['primary_color'] = ask("主色调（十六进制）", "#3B82F6")
    data['secondary_color'] = ask("次色调", "#10B981")
    data['background_color'] = ask("背景色", "#F9FAFB")
    data['max_width'] = ask("最大宽度", "1280px")

    # 不在范围内
    print("\n【范围界定】")
    out_of_scope = ask_multiline("本期不做哪些功能？（帮助 Agent 专注）")
    data['out_of_scope'] = "\n".join(f"- {o}" for o in out_of_scope) if out_of_scope else "暂无"

    # 生成文档
    spec_content = generate_spec(data)

    # 保存文件
    output_path = Path(args.output)
    output_path.write_text(spec_content, encoding="utf-8")

    print("\n" + "=" * 50)
    print(f"  ✅ 已生成: {output_path.absolute()}")
    print("=" * 50)
    print("\n下一步:")
    print("  1. 检查并完善生成的文档")
    print("  2. 运行: python autonomous_agent_demo.py --project-dir ./your-project")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n已取消")
        sys.exit(0)
