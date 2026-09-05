---
name: ai-work-hub-deep-research
description: Use when the user explicitly requests deep research or a formal systematic industry, technology, value-chain or thematic report. Choose the research modules needed for the decision and produce source-backed Markdown and HTML. A single expert interview or source analysis belongs to ai-work-hub-memory-graph; company-only diligence belongs to ai-work-hub-diligence.
---

# AI Work Hub Deep Research

## Purpose And Scope

Produce an independent research view that answers a defined decision question. Go deep on the mechanisms and variables that matter; do not inflate a focused study into a comprehensive industry audit.

Activate only for an explicit deep-research or formal-report request. Ordinary expert interviews, thematic materials and bounded external checks remain in the Memory Graph workflow, with persistence unless the user excludes it.

Start by defining the question, useful deliverable, relevant geography/horizon and exclusions. Infer these from the request where clear; ask only when the ambiguity materially changes the work. Do not require another approval merely to proceed with already requested research.

## Source Ownership

- Project-linked: read the current project judgment, state and relevant sources first. Store research under `项目/<项目名>/输出文档/03_研究与分析/`, never as a second running judgment.
- Standalone: store under `行业研究/<主题>/`.
- Reusable interviews and thematic materials: preserve once in `知识来源/`, then link rather than copy them.
- Chat-only: do not create or modify files.

Initialize only when a new report object is needed:

```bash
python3 <skill_dir>/scripts/init_deep_research.py \
  --workspace-root "<workspace_root>" --industry "<主题>"
```

Add `--project-name "<项目名>"` for project-linked work. The initializer creates a minimal report and state, not an evidence ledger, empty market model or unneeded figure directory. It refuses to overwrite an existing report.

## Choose The Analysis

Select modules by the decision question. A broad industry study can use all of them; a narrow technical or competitive study should omit irrelevant ones.

| Question | Useful work | Read when applicable |
| --- | --- | --- |
| Which route works, where and why? | Mechanism, system boundary, substitutes, engineering trade-offs and bottlenecks | references/technology-and-competition.md |
| Who captures value? | Customer budget, workflow, competition, incumbent/self-build alternatives and commercialization | references/research-method.md |
| How large or valuable can this become? | Causal demand/revenue model, important sensitivities and comparable economics | references/market-sizing.md |
| What would change the view? | Strongest opposing explanation, material source conflicts and decisive uncertainty | references/source-and-evidence.md |
| How does this connect to prior work? | Relevant projects, source notes, sectors, technical and valuation objects | references/memory-graph-linkage.md |
| How should the report communicate? | Only useful figures, Markdown and responsive HTML | references/html-and-visuals.md |

Do not require five-year forecasts, both global and China models, TAM/SAM/SOM, physical signal chains or every competitor category when they do not answer the requested question. Conversely, do not shorten an explicitly requested comprehensive study merely to fit a small template.

## Research Loop

1. Read relevant existing work and supplied sources; retrieve prior knowledge from Memory Graph and core source notes where available.
2. Identify the central explanation, its strongest alternative and the missing information that could change the result.
3. Research the relevant modules. Prefer original publications, official documentation, filings and authoritative reporting. Keep company statements and expert opinions attributed; they can be useful without turning each into an independent verification task.
4. Resolve material conflicts by comparing definitions, conditions and dates. A citation shows provenance, not automatic truth. Do not commission tests, audits, company data rooms or reproduction unless necessary for the question and within the requested scope.
5. Form the current view, explain what supports and challenges it, and identify only useful next actions. Stop expanding when additional detail no longer changes the answer; disclose remaining material limits.
6. Write the report, render HTML unless excluded, and inspect the actual output. Number sections consistently without imposing a fixed chapter count.
7. If a project conclusion changes, update the existing judgment through Diligence. Write only reusable changes to the graph, rewriting current understanding rather than merely appending events.

For independent source searches, parallel work can help. Keep one owning agent responsible for synthesis and shared-file writes; multiple model opinions are not independent evidence.

## Sources And Models

Cite the key facts and judgments near their use; make analyst assumptions visible. Maintain a short sources section and, only when helpful, a table of material conflicting estimates or model inputs. No routine claim-by-claim Evidence Ledger.

When a quantitative model is useful, choose the economic unit, geography and horizon that fit. Use actual inputs where available, label source claims and analyst assumptions, check arithmetic and focus sensitivity on consequential drivers. A five-year global/China model is an option or an explicit deliverable, not a universal requirement.

`forecast_market.py` supports shipment/BOM economics only. Other business models can use their own CSV, spreadsheet or code with documented formulas; never force software or services into a hardware schema.

## Deliverable And Acceptance

A useful report normally includes the decision question, current view, relevant analysis, strongest counterargument, material uncertainties and sources. Organize to fit the reader; do not create empty sections, risk lists or tasks just to fill a template.

Render using the existing visual system:

```bash
python3 <skill_dir>/scripts/render_report.py \
  --input "<report.md>" --output "<report.html>" \
  --title "<report title>" --subtitle "<decision context>"
python3 <skill_dir>/scripts/validate_research.py \
  --report "<report.md>" --html "<report.html>"
```

Add `--market-model "<model.csv>"` only when a model was produced; add `--market-format shipment-bom` for the bundled calculator's format. Use repeated `--require-module` arguments only for modules actually commissioned. Legacy evidence-ledger files can still be checked when explicitly supplied, but are never required or generated by default.

Check that the report answers the question, decisive statements are supported at the stated source level, important calculations reconcile and links/figures render. Automated checks validate structure, not investment reasoning. Rebuild and validate the graph once if it changed, not for a read-only research consultation.

## Privacy

The public skill contains generic methods, tools and fictional examples only. Project material, research, source notes, Memory Graph and private delivery settings stay in the user's workspace.
