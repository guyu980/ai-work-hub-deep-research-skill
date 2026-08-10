#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from html import escape
import os
from pathlib import Path
import re
from urllib.parse import quote


REMOTE_PREFIXES = ("http://", "https://", "mailto:", "#", "data:")


def output_url(value: str, source_dir: Path, output_dir: Path) -> str:
    value = value.strip()
    if value.startswith(REMOTE_PREFIXES):
        return escape(value, quote=True)
    path = Path(value)
    if path.is_absolute():
        return escape(path.as_uri(), quote=True)
    resolved = (source_dir / path).resolve()
    relative = os.path.relpath(resolved, output_dir)
    return escape(quote(relative, safe="/:._-?#=%&"), quote=True)


def render_inline(text: str, source_dir: Path, output_dir: Path) -> str:
    tokens: dict[str, str] = {}

    def stash(value: str) -> str:
        key = f"@@HTMLTOKEN{len(tokens)}@@"
        tokens[key] = value
        return key

    text = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        lambda m: stash(
            f'<img src="{output_url(m.group(2), source_dir, output_dir)}" '
            f'alt="{escape(m.group(1), quote=True)}">'
        ),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: stash(
            f'<a href="{output_url(m.group(2), source_dir, output_dir)}">'
            f"{escape(m.group(1))}</a>"
        ),
        text,
    )
    text = re.sub(
        r"`([^`]+)`",
        lambda m: stash(f"<code>{escape(m.group(1))}</code>"),
        text,
    )
    text = escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    for key, value in tokens.items():
        text = text.replace(key, value)
    return text


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_table_separator(line: str) -> bool:
    cells = table_cells(line)
    return bool(cells) and all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells
    )


def is_block_start(lines: list[str], index: int) -> bool:
    line = lines[index]
    if not line.strip():
        return True
    if re.match(r"^#{1,6}\s+", line) or line.startswith(">"):
        return True
    if line.startswith("```") or re.fullmatch(r"\s*(?:---+|\*\*\*+)\s*", line):
        return True
    if re.match(r"^(?:[-*]|\d+\.)\s+", line):
        return True
    if index + 1 < len(lines) and "|" in line and is_table_separator(lines[index + 1]):
        return True
    return False


def consume_list(
    lines: list[str],
    index: int,
    source_dir: Path,
    output_dir: Path,
) -> tuple[str, int]:
    ordered = bool(re.match(r"^\d+\.\s+", lines[index]))
    pattern = r"^(\d+)\.\s+(.+)$" if ordered else r"^[-*]\s+(.+)$"
    tag = "ol" if ordered else "ul"
    items: list[str] = []
    start = None
    while index < len(lines):
        match = re.match(pattern, lines[index])
        if not match:
            break
        if ordered:
            number, item = int(match.group(1)), match.group(2)
            if start is None:
                start = number
        else:
            item = match.group(1)
        items.append(f"<li>{render_inline(item, source_dir, output_dir)}</li>")
        index += 1
        if (
            index + 1 < len(lines)
            and not lines[index].strip()
            and re.match(pattern, lines[index + 1])
        ):
            index += 1
    start_attr = f' start="{start}"' if ordered and start not in (None, 1) else ""
    return f"<{tag}{start_attr}>\n" + "\n".join(items) + f"\n</{tag}>", index


def markdown_to_html(markdown: str, source_dir: Path, output_dir: Path) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue

        if line.startswith("```"):
            language = line[3:].strip()
            code: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            class_attr = f' class="language-{escape(language, quote=True)}"' if language else ""
            out.append(f"<pre><code{class_attr}>{escape(chr(10).join(code))}</code></pre>")
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            out.append(
                f"<h{level}>{render_inline(heading.group(2), source_dir, output_dir)}</h{level}>"
            )
            index += 1
            continue

        if re.fullmatch(r"\s*(?:---+|\*\*\*+)\s*", line):
            out.append("<hr>")
            index += 1
            continue

        if line.startswith(">"):
            block: list[str] = []
            while index < len(lines) and lines[index].startswith(">"):
                block.append(lines[index][1:].lstrip().rstrip())
                index += 1
            rendered = "<br>".join(
                render_inline(item[:-2] if item.endswith("  ") else item, source_dir, output_dir)
                for item in block
            )
            out.append(f"<blockquote><p>{rendered}</p></blockquote>")
            continue

        if re.match(r"^(?:[-*]|\d+\.)\s+", line):
            rendered, index = consume_list(lines, index, source_dir, output_dir)
            out.append(rendered)
            continue

        if index + 1 < len(lines) and "|" in line and is_table_separator(lines[index + 1]):
            headers = table_cells(line)
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and lines[index].strip() and "|" in lines[index]:
                rows.append(table_cells(lines[index]))
                index += 1
            table = ["<table>", "<thead><tr>"]
            table.extend(
                f"<th>{render_inline(cell, source_dir, output_dir)}</th>" for cell in headers
            )
            table.extend(["</tr></thead>", "<tbody>"])
            for row in rows:
                padded = row + [""] * max(0, len(headers) - len(row))
                table.append(
                    "<tr>"
                    + "".join(
                        f"<td>{render_inline(cell, source_dir, output_dir)}</td>"
                        for cell in padded[: len(headers)]
                    )
                    + "</tr>"
                )
            table.extend(["</tbody>", "</table>"])
            out.append("\n".join(table))
            continue

        paragraph = [line.strip()]
        index += 1
        while index < len(lines) and not is_block_start(lines, index):
            paragraph.append(lines[index].strip())
            index += 1
        out.append(
            f"<p>{render_inline(' '.join(paragraph), source_dir, output_dir)}</p>"
        )
    return "\n".join(out)


def first_h1(markdown: str) -> str | None:
    for line in markdown.splitlines():
        match = re.match(r"^#\s+(.+)$", line)
        if match:
            return re.sub(r"[*_`]", "", match.group(1)).strip()
    return None


def remove_first_h1(markdown: str) -> str:
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if re.match(r"^#\s+", line):
            del lines[index]
            break
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a deep-research Markdown file as local HTML.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--title")
    parser.add_argument("--subtitle", default="Source-backed industry research and investment analysis")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--template", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = args.input.resolve()
    output = args.output.resolve()
    template = (
        args.template.resolve()
        if args.template
        else Path(__file__).resolve().parents[1] / "assets" / "report-template.html"
    )
    markdown = source.read_text(encoding="utf-8")
    title = args.title or first_h1(markdown) or source.stem
    article_markdown = remove_first_h1(markdown)
    article_html = markdown_to_html(article_markdown, source.parent, output.parent)
    html = template.read_text(encoding="utf-8")
    replacements = {
        "{{TITLE}}": escape(title),
        "{{SUBTITLE}}": escape(args.subtitle),
        "{{DATE}}": escape(args.date),
        "{{ARTICLE_HTML}}": article_html,
    }
    for token, value in replacements.items():
        html = html.replace(token, value)
    unresolved = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
    if unresolved:
        raise SystemExit(f"unresolved template tokens: {', '.join(unresolved)}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
