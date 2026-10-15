---
name: ai-work-hub-deep-research
description: Produce a source-backed formal industry, technology or thematic study when deep research or a systematic report is explicitly requested. Explain mechanisms plainly with useful diagrams and interactive visuals, develop reasoned views on trends and value capture, and deliver Markdown plus HTML. Ordinary interviews/sources belong to Memory Graph; company updates belong to Diligence.
---

# AI Work Hub Deep Research

## Scope And Ownership

Answer a defined research or decision question independently. Infer the useful scope, geography, horizon and exclusions from the request; ask only when ambiguity materially changes the work. An explicit deep-research request calls for a substantial professional study. A narrow subject can still require deep analysis; keep its boundary focused without reducing the depth needed to explain it.

- Project-linked: inherit the latest company judgment/state; output under `项目/<name>/输出文档/03_研究与分析/`, not another running judgment.
- Standalone: output under `行业研究/<theme>/`.
- Reusable interviews/thematic inputs: preserve once in `知识来源/` via Memory Graph and link their core notes.
- Chat-only: no file writes.
- Bounded source checks and ordinary interviews: stay in the owning Diligence/Memory Graph workflow, not this Skill.

Read useful existing studies before creating a new report. Compare the decision question, substantive as-of date and changed assumptions, not just filenames. An older study may answer a different question; do not discard it merely because a newer report mentions the same sector.

## Depth And Quality Standard

Prioritize the quality of the answer over speed, brevity or token savings. Treat a formal study as work that should withstand examination by knowledgeable analysts: explain the important mechanisms from first principles where useful, investigate the history and competing routes, reconcile consequential evidence, build independent economic reasoning, and make a supported synthesis. A polished overview, source inventory, abstract trend table or lightly qualified opinion is not a completed deep study. Do not silently reduce a broad request to the easiest few questions.

Use [research-method.md](references/research-method.md) to build the question hierarchy, evidence map and investigation plan. Divide a substantial study into relevant workstreams such as technical mechanisms and limits, customer demand and adoption, competition and industry structure, and economics/value capture. Where delegation is available, parallelize genuinely separable investigation and use a skeptical review of the synthesis. Keep one owner responsible for shared definitions, source checking, conflicting findings, figures and the final argument. Several agents repeating the same source are not independent corroboration.

Work iteratively: synthesize provisional findings, identify the most important contradiction or weak inference, investigate it, and revise the argument and models. Read consequential original sources beyond search snippets and abstracts. Precision means correct definitions, dates, units, comparable conditions and explicit assumptions; unsupported decimal places or confident forecasts add no precision. Professional depth also includes explaining why a plausible alternative is less convincing.

Finish when the central questions have been answered at the requested depth, the material mechanisms and economics are explained, major conflicting evidence and alternatives have been addressed, and the conclusions and visuals survive review. Do not stop merely because a target length, source count, time allowance or output file has been reached. Avoid collecting irrelevant material once the substantive work is complete. If an actual access or execution limit leaves a material gap, identify the affected conclusion and deliver the bounded result honestly rather than labeling incomplete work comprehensive or asking the user to do the remaining analysis.

## Research Loop

1. Read supplied sources, relevant current project files and compact Memory Graph matches.
2. Frame the important questions, central disagreements and competing explanations using [research-method.md](references/research-method.md). Allocate investigation to their importance and uncertainty, and decide what evidence would distinguish them.
3. Research the relevant modules below. Prefer original publications, official documents, filings and authoritative reporting; retain attributed company/expert claims without turning every input into a verification task. Develop explanatory figures alongside the argument, rather than decorating a finished text.
4. Reconcile material differences in definition, period, system boundary or assumptions. Synthesize across findings: explain what has changed, which constraint moves next, how customers and competitors respond, and who can retain value. State the current leaning and strongest challenge. Return to research when a consequential conflict, missing mechanism or weak inference remains.
5. Write and illustrate the analysis for the reader, render HTML unless excluded, then review the argument, explanation and actual visual/interactive output as described below.
6. If it changes a company conclusion, update the same judgment through Diligence. Route reusable changes through Memory Graph's shared writer, revising current synthesis rather than appending every finding.

No default company data room, reproduction, engineering audit or claim-by-claim Evidence Ledger. Quantitative models serve the question; visual explanation is an active part of a substantial technical or industry report, with its form and extent chosen for comprehension.

## Explain And Illustrate

Write for an intelligent reader who need not know the field's vocabulary. Start a difficult mechanism with a concrete task or worked example: what happens, what the new approach changes, why it helps, and what it costs or cannot do. Introduce a necessary technical term after its role is clear. Keep exact distinctions and useful numbers; move specialist detail out of the main explanation when it interrupts understanding. An acronym expansion or glossary does not substitute for explaining the process.

Use [technology-and-competition.md](references/technology-and-competition.md) for technical mechanisms and comparisons, and [html-and-visuals.md](references/html-and-visuals.md) when planning and producing a report. Actively use mechanism drawings, cutaways, step sequences, before/after comparisons, bottleneck maps, value flows and conditional scenario diagrams where they reveal relationships. A substantial report should not default to walls of prose and tables. Choose visual density by explanatory need, without a fixed figure count or a graphic for every section.

Use interaction when changing a parameter, revealing a sequence or comparing scenarios helps the reader reason. Use 3D when spatial arrangement, geometry or motion matters and a flat view conceals it. Keep meaningful defaults, readable labels, explicit assumptions and a static explanation or key frames for print and sharing. Use available illustration, plotting, animation and browser capabilities purposefully; do not require a particular optional tool or external service. The [fictional worked example](examples/receipt-workflow.md) demonstrates one text-and-figure explanation, not the scope or depth of a full study; adapt its method, not its subject or layout.

A trend view must explain more than the conditions for success and failure. Compare the plausible explanations, use evidence to favor or qualify one, connect technical change to adoption and bargaining power, and identify what would reverse the view. A view may agree with consensus; its contribution is the reasoning and consequential distinctions. Mark timing as a dependency or uncertainty when evidence cannot support a calendar date.

## Select Useful Modules

| Decision question | Reference |
| --- | --- |
| Which technical route works, under what constraints and alternatives? | [technology-and-competition.md](references/technology-and-competition.md) |
| Which explanation is better supported; how do trends change adoption and value capture? | [research-method.md](references/research-method.md) |
| What economic scale or value is plausible? | [market-sizing.md](references/market-sizing.md) |
| Which source conflicts/uncertainties matter? | [source-and-evidence.md](references/source-and-evidence.md) |
| What prior work should be reused or revised? | [memory-graph-linkage.md](references/memory-graph-linkage.md) |
| Which diagrams, illustrations, interactions or 3D views help explain the argument? | [html-and-visuals.md](references/html-and-visuals.md) |

Read only relevant references. Do not require five-year/global-China forecasts, TAM/SAM/SOM, physical signal chains or all competitor classes when they do not answer the request.

When a quantitative model helps, choose the economic unit and horizon, mark actuals/source claims/analyst assumptions, check arithmetic and focus sensitivity on meaningful drivers. `forecast_market.py` supports shipment/BOM economics only; use an appropriate model for other businesses.

## Artifacts And Dates

Initialize only a genuinely new report object; the initializer refuses to overwrite a report:

```bash
python3 <skill_dir>/scripts/init_deep_research.py --workspace-root "<root>" --industry "<theme>"
```

Add `--project-name "<name>"` for project-linked work. It creates a minimal report/state, not ledgers, unused models or empty figure folders.

The report is a **dated research snapshot**. Record its actual incorporated information cutoff; formatting, rereading or index rebuilding does not refresh it. Current Graph understanding and company judgments evolve separately. Regenerate the report/HTML for a requested or consequential revision, not every news item. Retain links to useful prior snapshots and explain material assumption changes.

A useful report exposes the question, current view, important mechanisms/economics, strongest counterargument, material uncertainties and sources. Adapt chapters to the reader; omit empty lists and low-value tasks. Cite decisive statements near use, with a concise sources section and only helpful model/conflict tables.

Place each visual beside the claim it explains and keep local assets portable with the report. A standalone interactive companion should be linked from the relevant static figure, with enough information retained in Markdown and print to understand the conclusion. Do not silently replace a durable report with a chat-only visualization or publish it to an external site.

## Acceptance

```bash
python3 <skill_dir>/scripts/render_report.py --input "<report.md>" --output "<report.html>" --title "<title>" --subtitle "<decision context>"
python3 <skill_dir>/scripts/validate_research.py --report "<report.md>" --html "<report.html>"
```

Add model/module arguments only for commissioned artifacts. Legacy ledgers may be checked if explicitly supplied; they are not required or generated by default.

Before delivery, review the substantive coverage against the original request and research questions, then reread the central argument as a reader and an editor. Can the reader explain why the technology works without repeating unexplained terms? Do the major conclusions follow from evidence and a visible causal argument, including the strongest alternative? Does the trend analysis establish a useful current leaning rather than leaving every outcome equally possible? Identify the strongest objection, trace its implication through the conclusion and model, and resolve it or state the material limit. For a substantial study, use an independent skeptical reader when available; otherwise perform an explicit opposing review. Return unresolved substantive issues to research and rewrite affected passages before polishing. Extra headings and caveats do not repair missing analysis.

Inspect actual rendering, figures, links and meaningful arithmetic. Exercise the important controls, including parameter limits and scenario switches, check that the visual and explanation change together, and inspect narrow-screen and static/print fallbacks. Check 3D views and animations for understandable camera positions, labels and motion controls when used. Structure checks cannot establish readability, causal depth or visual accuracy; do not report them as such.

If Graph changed, use its hash-checked writer, validate once and read back current-view sections. Do not change formal company decisions through a report sync or publish private inputs to public Skill repositories.
