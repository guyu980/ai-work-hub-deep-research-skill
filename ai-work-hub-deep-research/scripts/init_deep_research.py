#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from datetime import date
import json
from pathlib import Path
import re


def safe_name(value: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|\r\n]+", "_", value).strip(" ._")
    if not cleaned:
        raise ValueError("industry or project name resolves to an empty filename")
    return cleaned


def write_new(path: Path, content: str) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_csv_new(path: Path, headers: list[str], rows: list[list[str]] | None = None) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows or [])


def report_outline(industry: str, today: str, project_name: str | None) -> str:
    context = f"项目关联：{project_name}" if project_name else "研究模式：独立行业研究"
    return f"""# {industry}行业研究报告

> 日期：{today}
> {context}
> 状态：研究框架已初始化，结论待证据和模型完成后填写。

## Part I｜判断框架

### 1. 执行摘要与投资判断

#### 1.1 当前核心判断

#### 1.2 最强反方观点与判断改变条件

### 2. 研究问题、范围与证据边界

#### 2.1 决策问题与研究对象

#### 2.2 市场定义、地区、时间与排除项

#### 2.3 事实、来源观点、外部预测与本报告假设

## Part II｜技术基础、路线与发展趋势

### 3. 系统边界与底层技术原理

#### 3.1 用户任务与完整信号链

#### 3.2 关键物理/技术机制

### 4. 技术路线、差异与优劣势

#### 4.1 路线对比总表

#### 4.2 各路线原理与工程权衡

#### 4.3 替代路线与“不采用专用产品”的方案

#### 4.4 路线选择

### 5. 未来五年技术发展趋势

#### 5.1 研究前沿与工程瓶颈迁移

#### 5.2 制造、成本、标准与接口

#### 5.3 数据、算法、控制与产品形态

#### 5.4 五年里程碑、领先指标与失败信号

## Part III｜市场规模与产业经济性

### 6. 全球与中国未来五年市场规模

#### 6.1 市场边界与自下而上公式

#### 6.2 全球模型与预测过程

#### 6.3 中国模型与预测过程

#### 6.4 保守、基准和乐观情景

#### 6.5 敏感性与 Top-down 交叉校验

#### 6.6 TAM、SAM 与 SOM

### 7. 需求节奏、价值链与商业模式

## Part IV｜竞争格局与创业窗口

### 8. 全球与中国竞争格局

#### 8.1 传统厂商

#### 8.2 成熟专业厂商与研究生态

#### 8.3 全球与中国创业公司

#### 8.4 OEM 自研与替代方案

### 9. 竞争关键变量、创业机会与整合路径

## Part V｜投资结论与后续验证

### 10. 投资机会地图与估值含义

### 11. 项目定位与证明门槛

### 12. 最终结论、访谈与后续资料清单

### 13. 主要来源、证据说明与模型文件
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize a project-linked or standalone industry research object.")
    parser.add_argument("--workspace-root", required=True, type=Path)
    parser.add_argument("--industry", required=True)
    parser.add_argument("--project-name")
    parser.add_argument("--date", default=date.today().isoformat())
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    workspace = args.workspace_root.resolve()
    industry = safe_name(args.industry)
    project = safe_name(args.project_name) if args.project_name else None
    if project:
        root = workspace / "项目" / project
    else:
        root = workspace / "行业研究" / industry
    originals = root / "原始资料"
    parsed = root / "解析文本"
    outputs = root / "输出文档"
    figures = outputs / "行业研究图示"
    for folder in (originals, parsed, outputs, figures):
        folder.mkdir(parents=True, exist_ok=True)

    stem = f"{args.date}_{industry}"
    report = outputs / f"{stem}_行业研究报告.md"
    evidence = parsed / f"{stem}_研究证据台账.csv"
    market = parsed / f"{stem}_市场规模测算输入.csv"
    state = outputs / f"{stem}_研究状态.json"

    write_new(report, report_outline(industry, args.date, project))
    write_csv_new(
        evidence,
        [
            "claim_id", "claim", "category", "status", "evidence_grade",
            "source_type", "source_title", "source_url", "publish_date",
            "accessed_date", "geography", "definition_or_metric",
            "source_value", "report_use", "conflict_or_caveat",
        ],
    )
    write_csv_new(
        market,
        [
            "scenario", "geography", "segment", "year", "currency",
            "addressable_units", "paid_penetration", "hardware_bom",
            "software_service_ratio", "fx_to_cny", "units_source",
            "penetration_source", "price_source",
        ],
    )
    write_new(
        state,
        json.dumps(
            {
                "schema_version": 1,
                "industry": args.industry,
                "project_name": args.project_name,
                "mode": "project-linked" if project else "standalone-industry",
                "research_date": args.date,
                "status": "initialized",
                "report": str(report.relative_to(root)),
                "evidence_ledger": str(evidence.relative_to(root)),
                "market_model_input": str(market.relative_to(root)),
                "html": None,
                "memory_graph_sync": "not_started",
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
    )
    print(root)
    print(report)
    print(evidence)
    print(market)
    print(state)


if __name__ == "__main__":
    main()
