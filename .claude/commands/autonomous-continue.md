#!/usr/bin/env python3
"""
自主项目继续命令

继续之前暂停的自主开发项目。
"""

import os
import sys
import argparse
from pathlib import Path

# 添加插件根目录到 Python 路径
plugin_root = Path(__file__).parent.parent
sys.path.insert(0, str(plugin_root))


def main():
    parser = argparse.ArgumentParser(
        description="继续已存在的自主开发项目",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "project_dir",
        nargs="?",
        default="./autonomous_project",
        help="项目目录路径 (默认: ./autonomous_project)"
    )

    args = parser.parse_args()

    project_dir = Path(args.project_dir).resolve()

    # 检查项目是否存在
    if not project_dir.exists():
        print(f"错误: 项目目录不存在: {project_dir}")
        print("")
        print("请先创建项目:")
        print(f"  autonomous-create --project-dir {args.project_dir}")
        sys.exit(1)

    # 检查是否有 feature_list.json
    feature_list = project_dir / "feature_list.json"
    if not feature_list.exists():
        print(f"错误: 未找到 feature_list.json，这不是有效的自主项目")
        sys.exit(1)

    print(f"继续项目: {project_dir}")
    print("")

    # 获取配置
    model = os.environ.get("ANTHROPIC_MODEL")

    # 构建命令
    cmd = [sys.executable, "-c", f"""
import sys
sys.path.insert(0, "{plugin_root}")
from autonomous_agent_demo import main
from client import create_client

client = create_client(Path("{args.project_dir}").resolve(), model={repr(model)})
main(project_dir="{args.project_dir}", client=client)
"""]

    # 执行
    import subprocess
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n\n已暂停。再次运行相同命令以继续开发。")
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)


if __name__ == "__main__":
    main()
