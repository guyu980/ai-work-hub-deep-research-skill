# HTML And Visual Explanation

## Design The Explanation Before Finishing The Prose

Formal technology and industry reports should actively use well-designed visuals to explain their difficult ideas. While outlining, identify what the reader needs to **see**: where time is spent, what changes shape or state, which constraint moves, who pays whom, or which condition leads to a different future. Build those figures alongside the reasoning and refer to the same concrete example in the prose. A long text-only report usually leaves useful explanatory work undone.

Use the full visual toolkit when it helps: precise diagrams, illustrated scenes, charts, staged animation, parameter exploration and, where spatial understanding requires it, 3D. Choose by explanatory benefit, not novelty. There is no figure quota or required set of chart types. A handful of strong figures may carry a short study; a complex mechanism may deserve a sequence. A diagram is not successful merely because it converts paragraphs into text boxes and arrows.

| What the reader needs to understand | Useful visual approach | What must be visible |
| --- | --- | --- |
| How a mechanism works | Labeled cutaway, spatial schematic, state sequence, or input/output example | Actual objects or states, the change, and the limiting step |
| Why one route is better under certain conditions | Aligned before/after diagrams, timing lanes, or comparable route panels | The same task, scale and starting conditions; what is gained and what is paid |
| Why progress stalls or the bottleneck moves | Duration/cost decomposition, resource queues, capacity comparisons | What improves, what remains, and why system-level gains differ from component gains |
| How an industry may change | Evidence-to-mechanism map, conditional paths, or scenario small multiples | The trigger, causal link, competing explanation and consequence; no invented calendar certainty |
| Who captures value | Product/data/payment flows, control-point map, or changing purchase bundle | What moves along each connection, who can substitute whom, and where bargaining power could change |
| How assumptions change the answer | Sensitivity plot, parameter slider, scenario switch, or step-by-step animation | The actual relationship being varied, resulting change and boundary where the conclusion flips |

Give a figure a claim-bearing title, concise labels, source/assumption note and useful alt text. Introduce the question before it and state the implication after it; the surrounding paragraph should interpret the figure rather than recite every label. Explain necessary terms in the example before using abbreviations in a legend. Keep one primary reading path and use detail panels when an overview would become crowded.

The completely fictional [receipt workflow example](../examples/receipt-workflow.md) shows a mechanism and a conditional trend through the same task, with editable SVGs and a small local interactive explanation. It demonstrates timing, dependencies and diminishing system gains; its figures are **not industry data or a reusable forecast**.

## Make Diagrams Carry The Explanation

Use shapes, position, length, motion and emphasis to represent the underlying relationship. For example, show work overlapping on a common time axis to explain parallel execution; show a queue growing before a limited resource to explain congestion; show the same object in successive states to explain a physical transformation. A decorative illustration or a sequence of category names does not explain the mechanism.

- Prefer editable SVG for precise schematics and labels; use standard plotting libraries for quantitative figures. Preserve the SVG or plotting source and the data/assumptions needed to reproduce meaningful quantities.
- Use custom SVG for spatial layouts, comparisons and engineering geometry. `render_flow_svg.py` is for simple chains, not a universal diagram generator. Pass the report's palette explicitly when using it; its generic defaults may differ.
- Keep comparable routes at the same abstraction level and scale. Separate component performance from end-to-end outcomes, latency from throughput, and cost per task from total spending.
- Label arrows with their meaning: material, signal, payment, dependency, or hypothesized effect. Explain the line convention locally; a solid arrow alone does not establish that a causal claim is verified. Distinguish observed/source-reported relationships from analyst inference and illustrative assumptions in labels or notes.
- For a trend, show the mechanism and alternative path, not just a row of future-year boxes. Mark a date only when timing has a defensible basis. If the evidence supports direction but not magnitude, use a qualitative diagram without a fabricated numerical axis.
- Professional or AI-generated illustrations can build intuition about a scene, apparatus or physical arrangement. Mark conceptual illustrations as such, check their scientific content, and place precise geometry, quantities and critical labels in controllable diagram layers. An attractive image must not invent evidence or imply measured performance.

## Quantitative And Interactive Views

Use units, denominators, periods and comparable scopes. Keep values traceable to a small source table, CSV, workbook or explicit formula; choose the lightest form that permits checking. Distinguish observations, source claims and scenario assumptions. Show uncertainty or scenario definitions, avoid unnecessary dual axes, and never draw a smooth numerical future from unsupported guesses.

Interaction is useful when readers need to **change something and observe why the answer changes**. A slider should expose a meaningful trade-off or threshold; a scenario switch should reveal the assumptions that differ; an animation should make a sequence or state transition easier to follow. Show the baseline and current inputs, units, bounds, computed result and limitations. Provide reset/pause or step controls as appropriate. Avoid motion that adds no understanding.

Use 3D when 2D obscures an important spatial relationship, geometry, occlusion or motion. Choose a clear default camera, labeled reference frame and useful preset views; allow rotation/zoom without requiring the reader to discover the point by orbiting randomly. Include static key views or a cutaway sequence that explains the same finding. Do not require 3D, a particular library, a remote service or an account for every report.

Preserve a readable static and printable explanation even when adding an interactive HTML companion. Link it from Markdown and keep the decisive evidence and conclusion in the report. The bundled renderer supports ordinary Markdown images and links; it does not execute arbitrary embedded HTML or JavaScript as a Markdown extension. A standalone local HTML companion can contain the interaction. Use local assets and no-CDN implementations when practical; disclose a real runtime dependency if one is necessary.

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

Render from Markdown using `render_report.py`. Inspect the actual result at desktop and narrow widths, in light and dark themes, and in print preview. Check whether figure labels remain readable, relationships survive resizing, local assets load, and important content is not clipped. Dense figures may need simpler panels or a portrait version; click-to-expand is a supplement, not a substitute for a comprehensible inline figure. Verify heading hierarchy, list numbering, table overflow, focus states and unresolved template tokens.

For interactive/3D companions, exercise the controls at meaningful extremes and a decision-changing boundary, check that output matches the stated formula, and inspect the default view as well as static fallback. Check keyboard controls and reduced-motion behavior where relevant. Report structural validation and actual visual inspection separately; file existence does not prove successful rendering.
