#!/usr/bin/env python3
from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import textwrap


def lines(text: str, width: int) -> list[str]:
    result: list[str] = []
    for paragraph in str(text).splitlines() or [""]:
        result.extend(textwrap.wrap(paragraph, width=width) or [""])
    return result


def text_block(x: float, y: float, values: list[str], css_class: str, line_height: int) -> str:
    spans = []
    for index, value in enumerate(values):
        dy = 0 if index == 0 else line_height
        spans.append(f'<tspan x="{x:.1f}" dy="{dy}">{escape(value)}</tspan>')
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{css_class}">' + "".join(spans) + "</text>"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a simple labeled research flow as editable SVG.")
    parser.add_argument("--input", required=True, type=Path, help="JSON diagram specification")
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    spec = json.loads(args.input.read_text(encoding="utf-8"))
    nodes = spec.get("nodes") or []
    edges = spec.get("edges") or []
    if not nodes:
        raise SystemExit("diagram requires at least one node")
    ids = [str(node.get("id", "")) for node in nodes]
    if not all(ids) or len(ids) != len(set(ids)):
        raise SystemExit("node ids must be non-empty and unique")

    direction = spec.get("direction", "horizontal")
    if direction not in {"horizontal", "vertical"}:
        raise SystemExit("direction must be horizontal or vertical")
    node_width = int(spec.get("node_width", 220))
    node_height = int(spec.get("node_height", 128))
    gap = int(spec.get("gap", 74))
    margin = 60
    title_height = 92
    note_height = 70
    if direction == "horizontal":
        width = margin * 2 + len(nodes) * node_width + (len(nodes) - 1) * gap
        height = title_height + node_height + note_height
        positions = {
            node["id"]: (margin + index * (node_width + gap), title_height)
            for index, node in enumerate(nodes)
        }
    else:
        width = margin * 2 + node_width
        height = title_height + len(nodes) * node_height + (len(nodes) - 1) * gap + note_height
        positions = {
            node["id"]: (margin, title_height + index * (node_height + gap))
            for index, node in enumerate(nodes)
        }

    accent = spec.get("accent", "#087f73")
    warm = spec.get("accent_warm", "#b55d24")
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(str(spec.get("title", "Research flow")))}</title>',
        f'<desc id="desc">{escape(str(spec.get("description", "Labeled flow diagram")))}</desc>',
        "<defs>",
        f'<marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{accent}"/></marker>',
        "</defs>",
        "<style>",
        f'.title{{font:700 25px Inter,PingFang SC,sans-serif;fill:#17201e}} .label{{font:700 17px Inter,PingFang SC,sans-serif;fill:#17201e}} .detail{{font:14px Inter,PingFang SC,sans-serif;fill:#5f6b67}} .edge{{font:12px Inter,PingFang SC,sans-serif;fill:{warm}}} .note{{font:12px Inter,PingFang SC,sans-serif;fill:#68716e}}',
        "</style>",
        '<rect width="100%" height="100%" rx="18" fill="#fffdf9"/>',
        text_block(margin, 42, lines(spec.get("title", "Research flow"), 70), "title", 30),
    ]

    for edge in edges:
        source = str(edge.get("from", ""))
        target = str(edge.get("to", ""))
        if source not in positions or target not in positions:
            raise SystemExit(f"edge references unknown node: {source} -> {target}")
        sx, sy = positions[source]
        tx, ty = positions[target]
        if direction == "horizontal":
            x1, y1 = sx + node_width, sy + node_height / 2
            x2, y2 = tx, ty + node_height / 2
        else:
            x1, y1 = sx + node_width / 2, sy + node_height
            x2, y2 = tx + node_width / 2, ty
        parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{accent}" stroke-width="2.5" marker-end="url(#arrow)"/>'
        )
        label = edge.get("label")
        if label:
            parts.append(text_block((x1 + x2) / 2, (y1 + y2) / 2 - 8, lines(label, 18), "edge", 15))

    for node in nodes:
        x, y = positions[node["id"]]
        focal = bool(node.get("focal", False))
        fill = spec.get("focal_fill", "#dff2ed") if focal else "#f5f2eb"
        stroke = accent if focal else "#d7d8d0"
        parts.append(
            f'<rect x="{x}" y="{y}" width="{node_width}" height="{node_height}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="{2 if focal else 1}"/>'
        )
        label_lines = lines(node.get("label", node["id"]), 16)
        detail_lines = lines(node.get("detail", ""), 24)
        parts.append(text_block(x + 18, y + 32, label_lines, "label", 22))
        detail_y = y + 32 + max(1, len(label_lines)) * 22 + 8
        parts.append(text_block(x + 18, detail_y, detail_lines[:3], "detail", 19))

    note = str(spec.get("note", "Source/assumption: report analysis."))
    parts.append(text_block(margin, height - 34, lines(note, 110), "note", 16))
    parts.append("</svg>")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(parts), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
