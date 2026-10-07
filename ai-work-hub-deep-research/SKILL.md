---
name: ai-work-hub-deep-research
description: Produce a source-backed formal industry, technology or thematic study when deep research or a systematic report is explicitly requested. Select analysis for the decision and deliver Markdown plus HTML. Ordinary interviews/sources belong to Memory Graph; company updates belong to Diligence.
---

# AI Work Hub Deep Research

## Scope And Ownership

Answer a defined decision question independently. Infer the useful scope, geography, horizon and exclusions from the request; ask only when ambiguity materially changes the work. An explicit study can be extensive. A focused question does not require an industry audit.

- Project-linked: inherit the latest company judgment/state; output under `项目/<name>/输出文档/03_研究与分析/`, not another running judgment.
- Standalone: output under `行业研究/<theme>/`.
- Reusable interviews/thematic inputs: preserve once in `知识来源/` via Memory Graph and link their core notes.
- Chat-only: no file writes.
- Bounded source checks and ordinary interviews: stay in the owning Diligence/Memory Graph workflow, not this Skill.

Read useful existing studies before creating a new report. Compare the decision question, substantive as-of date and changed assumptions, not just filenames. An older study may answer a different question; do not discard it merely because a newer report mentions the same sector.

## Research Loop

1. Read supplied sources, relevant current project files and compact Memory Graph matches.
2. Identify the central explanation, strongest alternative and consequential uncertainty.
3. Research the relevant modules below. Prefer original publications, official documents, filings and authoritative reporting; retain attributed company/expert claims without turning every input into a verification task.
4. Reconcile material differences in definition, period, system boundary or assumptions. Stop adding detail when it no longer changes the answer; disclose remaining material limits.
5. Write the conclusion and supporting analysis, render HTML unless excluded, and inspect the actual deliverable.
6. If it changes a company conclusion, update the same judgment through Diligence. Route reusable changes through Memory Graph's shared writer, revising current synthesis rather than appending every finding.

No default company data room, reproduction, engineering audit or claim-by-claim Evidence Ledger. Models and visualizations are tools for the question, not mandatory artifacts.

## Select Useful Modules

| Decision question | Reference |
| --- | --- |
| Which technical route works, under what constraints and alternatives? | [technology-and-competition.md](references/technology-and-competition.md) |
| Who buys and captures value; what threatens the thesis? | [research-method.md](references/research-method.md) |
| What economic scale or value is plausible? | [market-sizing.md](references/market-sizing.md) |
| Which source conflicts/uncertainties matter? | [source-and-evidence.md](references/source-and-evidence.md) |
| What prior work should be reused or revised? | [memory-graph-linkage.md](references/memory-graph-linkage.md) |
| How should the report render? | [html-and-visuals.md](references/html-and-visuals.md) |

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

## Acceptance

```bash
python3 <skill_dir>/scripts/render_report.py --input "<report.md>" --output "<report.html>" --title "<title>" --subtitle "<decision context>"
python3 <skill_dir>/scripts/validate_research.py --report "<report.md>" --html "<report.html>"
```

Add model/module arguments only for commissioned artifacts. Legacy ledgers may be checked if explicitly supplied; they are not required or generated by default.

Inspect actual rendering, figures/links and meaningful arithmetic; automated checks do not prove investment reasoning. If Graph changed, use its hash-checked writer, validate once and read back current-view sections. Do not change formal company decisions through a report sync or publish private inputs to public Skill repositories.
