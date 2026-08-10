# HTML And Visual Grammar

## Contents

1. Figure selection
2. Technical diagrams
3. Quantitative charts
4. HTML requirements

## Figure Selection

Create a figure only when it makes a relationship easier to understand than prose or a compact table. Favor:

- flow for a signal chain, process, or dependency;
- labeled cross-section for a physical mechanism;
- matrix for route or competitor comparisons;
- decision tree for route selection;
- value-chain map for ownership and value capture;
- line, stacked bar, waterfall, or sensitivity chart for quantitative relationships.

Every figure needs a research question, title, labels, source/assumption note, and a one-sentence takeaway in the surrounding text.

## Technical Diagrams

Use editable SVG when possible. Keep a stable visual language:

- left-to-right cause and signal flow;
- one accent color for the focal route;
- muted colors for context and alternatives;
- solid arrows for measured/physical flow;
- dashed arrows for inferred/modelled relationships;
- explicit sensor, algorithm, control, and task-value boundaries;
- short labels and readable type at normal browser zoom.

Do not use generative imagery to explain a mechanism when a labeled diagram is possible. For multiple routes, draw comparable schematics at the same abstraction level.

Use `render_flow_svg.py` for simple chains. Create custom SVG for cross-sections, spatial layouts, or engineering geometry.

## Quantitative Charts

- Put units in axes and labels.
- Distinguish global from China and conservative/base/upside consistently.
- Keep model values traceable to a CSV or workbook.
- Show assumptions or scenario definitions beneath the chart.
- Avoid dual axes unless indispensable.
- Do not hide forecast uncertainty behind smooth curves.

## HTML Requirements

The bundled template is local-first, has no CDN dependency, and uses a restrained Stanford-inspired research palette:

- Cardinal Red `#8C1515` and deep red `#820000` for navigation, hierarchy, and decision emphasis;
- warm white `#F5F4F1`, pearl `#FBFAF8`, charcoal `#2E2D29`, and neutral grey for the reading surface;
- red is an emphasis color, not a full-page decoration; do not introduce gradients, glowing effects, or unrelated accent hues;
- use the same semantic roles in charts and diagrams: cardinal for the focal route or conclusion, charcoal for primary context, and neutral grey for alternatives;
- reserve green and amber for explicitly positive and cautionary data semantics, not decoration.

Preserve:

- responsive article width and typography;
- desktop sidebar and narrow-screen menu;
- generated table of contents;
- scrollable table wrappers on small screens;
- click-to-expand images;
- print styles;
- dark/light theme and font controls;
- working relative links to diagrams, models, and source files.

Render from Markdown using `render_report.py`. Inspect desktop and a narrow viewport in both light and dark themes. Verify heading hierarchy, list numbering, table overflow, local assets, focus states, and unresolved template tokens. Do not ship the HTML if essential diagrams are clipped or unreadable.
