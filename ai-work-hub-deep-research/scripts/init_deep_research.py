#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from datetime import date
import json
from pathlib import Path
import re


def safe_name(value: str) -> str:
    cleaned = re.sub(r'[\\/:*?"<>|\r\n]+', "_", value).strip(" ._")
    if not cleaned:
        raise ValueError("industry or project name resolves to an empty filename")
    return cleaned


def write_new(path: Path, content: str) -> None:
    with path.open("x", encoding="utf-8") as handle:
        handle.write(content)


def report_outline(industry: str, today: str, project_name: str | None) -> str:
    context = f"项目关联：{project_name}" if project_name else "研究模式：独立主题研究"
    return f"""# {industry}研究报告

> 日期：{today}
> {context}
> 状态：研究框架，尚未形成结论。

## 1. 决策问题与研究边界

明确本次要回答的问题，按需选择分析模块、地区与时间范围。

## 2. 当前判断

形成结论后填写，说明决定性依据与对行动的影响。

## 3. 核心分析

围绕问题展开相关机制、竞争、商业或估值分析；不为无关模块建空章节。

## 4. 反对理由与关键不确定性

说明最有力的替代解释及可能改变结论的信息。后续动作仅在有价值时提出。

## 5. 主要来源与必要模型

关键来源在正文就近引用；这里保留简洁索引及重要假设或口径差异。
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize a minimal project-linked or standalone research report.")
    parser.add_argument("--workspace-root", required=True, type=Path)
    parser.add_argument("--industry", required=True)
    parser.add_argument("--project-name")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--with-market-model", action="store_true",
                        help="Create a shipment/BOM input CSV only when this model is needed.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    date.fromisoformat(args.date)
    workspace = args.workspace_root.resolve()
    industry = safe_name(args.industry)
    project = safe_name(args.project_name) if args.project_name else None
    root = workspace / "项目" / project if project else workspace / "行业研究" / industry
    if project and not root.is_dir():
        raise SystemExit("Project not found; resolve the existing project before initializing linked research.")
    outputs = root / "输出文档"
    if project:
        outputs = outputs / "03_研究与分析"
    stem = f"{args.date}_{industry}"
    report = outputs / f"{stem}_行业研究报告.md"
    state = outputs / f"{stem}_研究状态.json"
    market = outputs / f"{stem}_市场规模测算输入.csv" if args.with_market_model else None
    targets = [report, state] + ([market] if market else [])
    for target in targets:
        if target.exists():
            raise FileExistsError(f"refusing to overwrite existing file: {target}")
    for folder in (root / "原始资料", root / "解析文本", outputs):
        folder.mkdir(parents=True, exist_ok=True)
    write_new(report, report_outline(industry, args.date, project))
    if market:
        with market.open("x", encoding="utf-8-sig", newline="") as handle:
            csv.writer(handle).writerow([
                "scenario", "geography", "segment", "year", "currency",
                "addressable_units", "paid_penetration", "hardware_bom",
                "software_service_ratio", "fx_to_cny", "units_source",
                "penetration_source", "price_source",
            ])
    write_new(state, json.dumps({
        "schema_version": 1, "industry": args.industry,
        "project_name": args.project_name,
        "mode": "project-linked" if project else "standalone-industry",
        "research_date": args.date, "status": "initialized",
        "report": str(report.relative_to(root)),
        "market_model_input": str(market.relative_to(root)) if market else None,
        "html": None, "memory_graph_sync": "not_started",
    }, ensure_ascii=False, indent=2) + "\n")
    for target in targets:
        print(target)


if __name__ == "__main__":
    main()
