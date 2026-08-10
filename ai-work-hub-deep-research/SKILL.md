---
name: ai-work-hub-deep-research
description: Use for deep, source-backed research from either an active investment project or a standalone industry, technology, value-chain, or thematic question. Reconstructs system boundaries and technical mechanisms, compares technology routes and substitutes, maps global and China competitors including incumbents and startups, builds transparent five-year global and China market forecasts, produces decision-oriented investment conclusions, creates explanatory diagrams and a readable local HTML report, and routes reusable findings into an optional private AI Work Hub Memory Graph. Trigger for industry reports, sector maps, technical-route studies, competitive landscapes, market sizing, thematic investment research, or project-adjacent deep research; do not use for a short company-only BP screen when ai-work-hub-diligence is sufficient.
---

# AI Work Hub Deep Research

## Operating Contract

Produce an independent investment research view, not a stitched summary of reports.

Hard requirements:

- Define the decision question, scope, competing hypotheses, and market boundary before adopting external conclusions.
- Separate verified facts, source/company claims, third-party forecasts, and this report's assumptions.
- Explain the physical or technical signal chain before comparing product specifications.
- Compare routes on one explicit engineering and commercial framework, including substitutes and the option of using no dedicated component.
- Project five-year technology development separately across research, engineering, manufacturing, standards, product form, and commercial adoption; do not treat paper volume as industry progress.
- Cover global and China competition; include traditional incumbents, startups, OEM self-build, open-source/research ecosystems, and adjacent substitutes where material.
- Build global and China five-year forecasts from visible drivers. Keep TAM, SAM, and SOM separate.
- Use diagrams when they materially improve understanding. Prefer editable SVG or HTML/CSS figures over decorative images.
- Lead the conclusion with an investment view, price discipline when relevant, proof gates, and disconfirming evidence.
- Generate both Markdown and a readable local HTML version unless the user requests chat-only work.
- Retrieve from and write reusable increments to Memory Graph when available, but never copy private workspace content into this public skill repository.

Read the references triggered by the task:

- Always read `references/research-method.md` and `references/source-and-evidence.md`.
- Read `references/technology-and-competition.md` for technical routes or competitor work.
- Read `references/market-sizing.md` before producing any market forecast.
- Read `references/html-and-visuals.md` before making diagrams or HTML.
- Read `references/memory-graph-linkage.md` before graph retrieval or writeback.

## Resolve The Research Mode

Use one of three modes:

| Mode | Source of truth | Default storage |
| --- | --- | --- |
| Project-linked | Existing project folder and its materials | `<workspace_root>/项目/<项目名>/` |
| Standalone industry | Industry research object | `<workspace_root>/行业研究/<行业名>/` |
| Chat-only | Current conversation and supplied sources | Do not create or modify files |

For project-linked work, read the existing project judgment, state, supplied materials, and relevant prior outputs first. The industry report is a separate research deliverable; it must not become a second running project judgment. If the report changes the company view, use `ai-work-hub-diligence` to update the existing judgment and state after the report is finalized.

For standalone work, initialize a standard object when it does not exist:

```bash
python3 <skill_dir>/scripts/init_deep_research.py \
  --workspace-root "<workspace_root>" \
  --industry "<行业名>"
```

For project-linked work:

```bash
python3 <skill_dir>/scripts/init_deep_research.py \
  --workspace-root "<workspace_root>" \
  --industry "<行业名>" \
  --project-name "<项目名>"
```

The initializer refuses to overwrite an existing report or model.

## Run The Research Loop

1. Resolve mode, workspace, deliverables, decision user, time horizon, geography, currency, and market boundary.
2. Retrieve relevant project, sector, technical, valuation, event, and people context from Memory Graph when it exists. Open source cards behind useful matches.
3. Write a pre-research frame: decision question, scope inclusions/exclusions, initial hypotheses, likely substitutes, and facts that would disprove the thesis.
4. Read supplied project materials before external research in project-linked mode. Preserve source claims as claims.
5. Research external evidence using the source hierarchy. Prefer original papers, standards, official statistics, regulatory documents, company filings/product documentation, and reputable industry organizations. Use strong third-party reports as evidence inputs, not conclusion authorities.
6. Maintain the evidence ledger while researching. Record conflicting definitions and numbers instead of silently reconciling them.
7. Reconstruct the system boundary and technical mechanisms; draw the signal chain and route-level diagrams.
8. Compare routes, substitutes, incumbents, startups, OEM self-build, and open ecosystems on a common set of decision variables.
9. Build independent global and China five-year market models with scenarios, sensitivity, and top-down cross-checks.
10. Form the investment view only after the technical, competitive, and market work is complete. State what the market is overestimating and underestimating.
11. Write the Markdown report, render HTML, and inspect the result at desktop and narrow widths.
12. Finalize any project judgment delta through the diligence workflow, then route only reusable increments into Memory Graph. Rebuild and validate its generated indexes.

## Default Report Spine

Adapt the structure to the sector, but preserve the logic:

```text
Executive judgment
Research question, scope, definitions, and evidence boundaries
Industry system boundary and value chain
Technical foundations and signal chain
Technology-route mechanisms, differences, advantages, and limitations
Five-year technology development: bottlenecks, milestones, standards, cost, and product form
Route selection and likely convergence
Global and China market-sizing model
Demand sequence, willingness to pay, and business models
Global and China competitive landscape
Incumbent advantages, startup windows, substitutes, and likely consolidation
Investment opportunity map and valuation implications
Project positioning and proof gates, when project-linked
Disconfirming signals and final conclusion
Sources, evidence notes, and model files
```

Number headings consistently: Part labels are structural containers; chapters use integers; sections and subsections use full hierarchical numbers such as `3.2` and `3.2.1`.

## Market Model

Create an auditable driver table. A minimum bottom-up model is:

```text
hardware revenue(segment, geography, year)
  = addressable units × paid penetration × hardware BOM

total revenue
  = hardware revenue × (1 + software/service/NRE ratio)
```

Use `scripts/forecast_market.py` when the model fits this driver form. Adapt the model explicitly when installed base, replacement cycles, utilization, transaction value, capacity, seats, or consumption are the correct units. Do not force every industry into shipment × BOM.

Every forecast must include:

- global and China rows;
- five annual forecast years;
- base, conservative, and upside scenarios unless there is a reason not to;
- source-or-assumption tags for units, penetration, price/BOM, service ratio, FX, and replacement;
- at least one material sensitivity;
- a top-down reasonableness check without averaging incompatible definitions;
- separate TAM, SAM, and SOM logic.

## Visuals And HTML

Create only figures that answer a named research question. A substantial technical-industry report will usually need:

- system boundary or signal chain;
- route mechanism diagrams or labeled cross-sections;
- route comparison matrix and selection tree;
- competitive landscape by layer or positioning axes;
- market-sizing driver tree and forecast chart;
- investment thesis, proof-gate, or risk map.

Use `scripts/render_flow_svg.py` for simple process/signal-chain figures, and custom SVG for mechanisms that require a physical cross-section. Every figure must have a title, labels, units where relevant, and a source/assumption note.

Render the Markdown report:

```bash
python3 <skill_dir>/scripts/render_report.py \
  --input "<report.md>" \
  --output "<report.html>" \
  --title "<report title>" \
  --subtitle "<decision context>"
```

The renderer uses the bundled responsive template and keeps local links portable relative to the output file.

## Investment Judgment

Separate three questions:

1. Is the industry or capability becoming necessary, and for which tasks?
2. Which layer or route is most likely to capture durable value?
3. Is the current company and price an attractive way to express that view?

For project-linked work, use the diligence vocabulary: `投 / 继续推进 / 暂缓 / 不投`, followed separately by participation, position, and price view. Distinguish a good company from a good current deal. Do not convert press coverage, strategic interest, framework orders, or a hot financing market into proof.

State the strongest opposing case, the evidence that would change the conclusion, and the next interviews or data requests needed to resolve the remaining uncertainty.

## Memory Graph Linkage

Use the companion `ai-work-hub-memory-graph` skill when `<workspace_root>/Memory Graph/` exists.

- Retrieve before final route and investment judgments.
- Finalize the report first.
- Keep company-specific details in the project object.
- Put repeated market structure in the sector map, technical mechanisms and benchmarks in technical themes, reusable financing evidence in valuation anchors, durable cross-project changes in event cards, and independently important experts in people cards.
- Update existing objects when possible. Do not create the same fact in several cards.
- Rebuild indexes; never hand-edit JSONL caches.

## Completion Check

Before declaring the research complete, verify:

1. The decision question, market boundary, geography, time horizon, and exclusions are explicit.
2. Facts, claims, forecasts, and report assumptions are distinguishable and traceable.
3. The report explains mechanisms before route rankings.
4. Five-year technology trends distinguish research signals, engineering milestones, manufacturing/cost, standards, product form, and commercial adoption.
5. Competitor coverage includes global, China, incumbents, startups, substitutes, and OEM/self-build where material.
6. Global and China five-year models reconcile to their driver tables and include scenarios and sensitivity.
7. Every important figure communicates a research relationship and has a source/assumption note.
8. The investment view includes downside, disconfirming evidence, price discipline, and proof gates.
9. Markdown numbering is hierarchical; ordered lists do not restart accidentally in HTML.
10. HTML has a working table of contents, no unresolved template tokens, and no missing local assets.
11. Memory Graph retrieval/writeback and validation completed when available, or the exact failure is reported.

Run the bundled validator:

```bash
python3 <skill_dir>/scripts/validate_research.py \
  --report "<report.md>" \
  --evidence-ledger "<evidence.csv>" \
  --market-model "<market-model.csv>" \
  --html "<report.html>"
```
