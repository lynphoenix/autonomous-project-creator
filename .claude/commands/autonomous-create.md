#!/usr/bin/env python3
"""
自主项目创建命令

用法:
  autonomous-create                    # 使用默认设置创建项目
  autonomous-create --project-dir my_app  # 指定项目目录
  autonomous-create --model claude-sonnet-4-5-20250929  # 指定模型
"""

import os
import sys
import argparse
from pathlib import Path

# 添加插件根目录到 Python 路径
plugin_root = Path(__file__).parent.parent
sys.path.insert(0, str(plugin_root))

try:
    from claude_code_sdk import ClaudeSDKClient
except ImportError:
    print("错误: 未安装 claude-code-sdk")
    print("请运行: pip install -r requirements.txt")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="创建新的自主开发项目",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  autonomous-create                         # 使用默认设置
  autonomous-create --project-dir my_app    # 指定项目目录
  autonomous-create --max-iterations 10     # 限制迭代次数

环境变量:
  ANTHROPIC_API_KEY          API 密钥（必填）
  ANTHROPIC_BASE_URL         API 端点（可选）
  ANTHROPIC_MODEL            默认模型（可选）
  DISABLE_SANDBOX            禁用沙盒（不推荐）
        """
    )

    parser.add_argument(
        "--project-dir",
        default="./autonomous_project",
        help="项目目录路径 (默认: ./autonomous_project)"
    )
    parser.add_argument(
        "--model",
        default=None,
        help="使用的 Claude 模型 (从环境变量 ANTHROPIC_MODEL 读取默认值)"
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=0,
        help="最大迭代次数，0 表示无限制 (默认: 0)"
    )

    args = parser.parse_args()

    # 检查 API 密钥
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("错误: ANTHROPIC_API_KEY 环境变量未设置")
        print("")
        print("请先设置 API 密钥:")
        print("  export ANTHROPIC_API_KEY='your-api-key-here'")
        print("")
        print("或创建 .env 文件:")
        print("  cp .env.example .env")
        print("  # 然后编辑 .env 文件")
        sys.exit(1)

    # 显示配置信息
    model = args.model or os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-5-20250929")
    base_url = os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com")

    print("=" * 60)
    print("自主项目构建器")
    print("=" * 60)
    print(f"项目目录: {args.project_dir}")
    print(f"使用模型: {model}")
    print(f"API 端点: {base_url}")
    if args.max_iterations > 0:
        print(f"最大迭代: {args.max_iterations}")
    print("=" * 60)
    print("")

    # 导入并运行
    try:
        from autonomous_agent_demo import main as demo_main
        from client import create_client

        project_dir = Path(args.project_dir).resolve()

        # 创建客户端
        print("正在初始化 Claude SDK 客户端...")
        client = create_client(project_dir, model=args.model)

        # 构建参数
        demo_args = [f"--project-dir={args.project_dir}"]
        if args.model:
            demo_args.append(f"--model={args.model}")
        if args.max_iterations > 0:
            demo_args.append(f"--max-iterations={args.max_iterations}")

        print("开始自主开发...")
        print("")

        # 运行主程序
        demo_main(project_dir=str(project_dir), client=client)

    except KeyboardInterrupt:
        print("\n\n已暂停。再次运行相同命令以继续开发。")
    except Exception as e:
        print(f"\n错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
