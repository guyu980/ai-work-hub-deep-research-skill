#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlparse


EVIDENCE_COLUMNS = {
    "claim_id", "claim", "category", "status", "evidence_grade", "source_type",
    "source_title", "source_url", "publish_date", "accessed_date", "geography",
    "definition_or_metric", "source_value", "report_use", "conflict_or_caveat",
}
MARKET_COLUMNS = {
    "scenario", "geography", "segment", "year", "currency", "addressable_units",
    "paid_penetration", "hardware_bom", "software_service_ratio", "fx_to_cny",
    "units_source", "penetration_source", "price_source",
}
COVERAGE = {
    "technical foundations": ("技术原理", "技术基础", "底层技术", "系统边界", "信号链", "technical foundation", "system boundary", "mechanism"),
    "technology routes": ("技术路线", "路线对比", "technology route"),
    "technology trends": ("技术发展趋势", "技术趋势", "发展趋势", "technology trend", "development trend"),
    "competition": ("竞争格局", "竞争地图", "competitive landscape"),
    "market sizing": ("市场规模", "market sizing", "market size"),
    "investment judgment": ("投资判断", "投资机会", "investment judgment", "investment view"),
    "sources": ("主要来源", "证据说明", "sources", "evidence notes"),
}


class ReportHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.heading_level: int | None = None
        self.heading_buffer: list[str] = []
        self.headings: list[tuple[int, str]] = []
        self.in_ol = False
        self.current_ol_items = 0
        self.ordered_list_counts: list[int] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"h1", "h2", "h3", "h4", "h5"}:
            self.heading_level = int(tag[1])
            self.heading_buffer = []
        elif tag == "ol":
            self.in_ol = True
            self.current_ol_items = 0
        elif tag == "li" and self.in_ol:
            self.current_ol_items += 1

    def handle_endtag(self, tag: str) -> None:
        if self.heading_level and tag == f"h{self.heading_level}":
            self.headings.append((self.heading_level, "".join(self.heading_buffer).strip()))
            self.heading_level = None
            self.heading_buffer = []
        elif tag == "ol" and self.in_ol:
            self.ordered_list_counts.append(self.current_ol_items)
            self.in_ol = False

    def handle_data(self, data: str) -> None:
        if self.heading_level:
            self.heading_buffer.append(data)


def normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().lower()


def markdown_headings(markdown: str) -> list[tuple[int, str, int]]:
    result = []
    for line_number, line in enumerate(markdown.splitlines(), 1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            title = re.sub(r"[*_`]", "", match.group(2))
            result.append((len(match.group(1)), title, line_number))
    return result


def markdown_ordered_list_counts(markdown: str) -> list[int]:
    lines = markdown.splitlines()
    result: list[int] = []
    index = 0
    while index < len(lines):
        if not re.match(r"^\d+\.\s+", lines[index]):
            index += 1
            continue
        count = 0
        while index < len(lines):
            if re.match(r"^\d+\.\s+", lines[index]):
                count += 1
                index += 1
                if index + 1 < len(lines) and not lines[index].strip() and re.match(r"^\d+\.\s+", lines[index + 1]):
                    index += 1
                continue
            break
        result.append(count)
    return result


def validate_heading_numbers(headings: list[tuple[int, str, int]], errors: list[str]) -> None:
    chapter: str | None = None
    section: str | None = None
    for level, title, line_number in headings:
        if level == 3:
            match = re.match(r"^(\d+)\.\s+", title)
            if match:
                chapter = match.group(1)
                section = None
        elif level == 4 and chapter:
            match = re.match(r"^(\d+)\.(\d+)\s+", title)
            if not match or match.group(1) != chapter:
                errors.append(f"line {line_number}: section number does not match chapter {chapter}: {title}")
            else:
                section = f"{match.group(1)}.{match.group(2)}"
        elif level == 5 and section:
            match = re.match(r"^(\d+)\.(\d+)\.(\d+)\s+", title)
            if not match or f"{match.group(1)}.{match.group(2)}" != section:
                errors.append(f"line {line_number}: subsection number does not match section {section}: {title}")


def read_headers(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def validate_evidence(path: Path, errors: list[str], warnings: list[str]) -> None:
    headers, rows = read_headers(path)
    missing = sorted(EVIDENCE_COLUMNS - set(headers))
    if missing:
        errors.append(f"evidence ledger missing columns: {', '.join(missing)}")
    if not rows:
        warnings.append("evidence ledger has no data rows")
        return
    allowed_status = {"verified", "source_claim", "report_assumption", "open"}
    for row_number, row in enumerate(rows, 2):
        if row.get("status") and row["status"] not in allowed_status:
            errors.append(f"evidence row {row_number}: unsupported status {row['status']!r}")
        if row.get("status") in {"verified", "source_claim"} and not (row.get("source_url") or row.get("source_title")):
            errors.append(f"evidence row {row_number}: sourced status without source")


def normalize_geography(value: str) -> str | None:
    value = normalized(value)
    if value in {"global", "world", "全球"}:
        return "global"
    if value in {"china", "prc", "中国", "中国大陆"}:
        return "china"
    return None


def validate_market(path: Path, errors: list[str], warnings: list[str]) -> None:
    headers, rows = read_headers(path)
    missing = sorted(MARKET_COLUMNS - set(headers))
    if missing:
        errors.append(f"market model missing columns: {', '.join(missing)}")
        return
    if not rows:
        errors.append("market model has no data rows")
        return
    years: dict[tuple[str, str], set[int]] = {}
    geographies: set[str] = set()
    scenarios: set[str] = set()
    for row_number, row in enumerate(rows, 2):
        geography = normalize_geography(row.get("geography", ""))
        if geography:
            geographies.add(geography)
        scenario = normalized(row.get("scenario", ""))
        scenarios.add(scenario)
        try:
            year = int(row.get("year", ""))
        except ValueError:
            errors.append(f"market row {row_number}: invalid year {row.get('year')!r}")
            continue
        if geography:
            years.setdefault((scenario, geography), set()).add(year)
        for key in ("units_source", "penetration_source", "price_source"):
            if not row.get(key, "").strip():
                warnings.append(f"market row {row_number}: empty {key}")
    if geographies != {"global", "china"}:
        errors.append("market model must include both Global and China geographies")
    scenario_aliases = {
        "base": {"base", "baseline", "基准"},
        "conservative": {"conservative", "downside", "bear", "保守", "悲观"},
        "upside": {"upside", "bull", "optimistic", "乐观"},
    }
    for label, aliases in scenario_aliases.items():
        if not scenarios.intersection(aliases):
            errors.append(f"market model missing {label} scenario")
    for (scenario, geography), values in years.items():
        if len(values) < 5:
            errors.append(f"market model needs at least five years for {scenario}/{geography}; found {len(values)}")


def validate_html(path: Path, markdown: str, errors: list[str]) -> None:
    html = path.read_text(encoding="utf-8")
    unresolved = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
    if unresolved:
        errors.append(f"HTML has unresolved template tokens: {', '.join(unresolved)}")
    if '<nav id="toc"></nav>' not in html or "querySelectorAll('h1:not(.report-cover h1), h2, h3')" not in html:
        errors.append("HTML table-of-contents structure or script is missing")
    parser = ReportHTMLParser()
    parser.feed(html)
    md_counts = markdown_ordered_list_counts(markdown)
    if parser.ordered_list_counts != md_counts:
        errors.append(f"ordered-list rendering differs: markdown={md_counts}, html={parser.ordered_list_counts}")
    html_titles = {normalized(title) for _, title in parser.headings}
    for _, title, line_number in markdown_headings(markdown):
        if normalized(title) not in html_titles:
            errors.append(f"HTML missing Markdown heading from line {line_number}: {title}")
    local_values = re.findall(r'(?:src|href)=["\']([^"\']+)["\']', html)
    for value in local_values:
        if value.startswith(("http://", "https://", "mailto:", "#", "data:", "javascript:")):
            continue
        parsed = urlparse(value)
        target = Path(unquote(parsed.path)) if parsed.scheme == "file" else (path.parent / unquote(value)).resolve()
        if not target.exists():
            errors.append(f"HTML local asset is missing: {value}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a completed deep-research report and its supporting artifacts.")
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--evidence-ledger", type=Path)
    parser.add_argument("--market-model", type=Path)
    parser.add_argument("--html", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    markdown = args.report.read_text(encoding="utf-8")
    headings = markdown_headings(markdown)
    validate_heading_numbers(headings, errors)
    searchable = normalized(markdown)
    for label, terms in COVERAGE.items():
        if not any(term in searchable for term in terms):
            errors.append(f"report coverage missing: {label}")
    if args.evidence_ledger:
        validate_evidence(args.evidence_ledger, errors, warnings)
    else:
        warnings.append("evidence ledger not supplied")
    if args.market_model:
        validate_market(args.market_model, errors, warnings)
    else:
        warnings.append("market model not supplied")
    if args.html:
        validate_html(args.html, markdown, errors)
    else:
        warnings.append("HTML report not supplied")

    print(f"report headings: {len(headings)}")
    print(f"warnings: {len(warnings)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        print(f"errors: {len(errors)}")
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("DEEP RESEARCH VALIDATION PASSED")


if __name__ == "__main__":
    main()
