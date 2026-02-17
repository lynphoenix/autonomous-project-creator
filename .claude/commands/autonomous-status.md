#!/usr/bin/env python3
"""
自主项目状态查询命令

显示项目的开发进度和统计信息。
"""

import json
import sys
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="查看项目开发进度",
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
        sys.exit(1)

    # 读取 feature_list.json
    feature_list = project_dir / "feature_list.json"
    if not feature_list.exists():
        print(f"错误: 未找到 feature_list.json")
        sys.exit(1)

    with open(feature_list, "r") as f:
        features = json.load(f)

    # 统计
    total = len(features)
    completed = sum(1 for f in features if f.get("passes", False))
    pending = total - completed
    completion_rate = (completed / total * 100) if total > 0 else 0

    # 显示
    print("=" * 60)
    print(f"项目状态: {project_dir.name}")
    print("=" * 60)
    print(f"总功能数: {total}")
    print(f"已完成: {completed}")
    print(f"待完成: {pending}")
    print(f"完成率: {completion_rate:.1f}%")
    print("=" * 60)
    print("")

    # 显示待完成的功能
    if pending > 0:
        print("待完成功能:")
        for i, f in enumerate(features, 1):
            if not f.get("passes", False):
                status = "🔄" if f.get("in_progress", False) else "⏳"
                print(f"  {status} [{i}] {f.get('subject', '未命名')}")
        print("")

    # 显示最近完成的功能
    if completed > 0:
        print("最近完成的功能:")
        count = 0
        for f in reversed(features):
            if f.get("passes", False):
                print(f"  ✅ {f.get('subject', '未命名')}")
                count += 1
                if count >= 5:
                    break
        print("")


if __name__ == "__main__":
    main()
