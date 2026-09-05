# AI Work Hub Deep Research

[中文说明](README.zh-CN.md)

A Codex skill for independent, source-backed industry and technology research for investment decisions. It can start from an active company project or a standalone research question.

## Question-Driven Research

Choose the modules needed for the decision. The capabilities below are options, not a mandatory checklist: a focused route comparison does not need five-year market forecasts. Use inline sources and a short list of material assumptions; no routine Evidence Ledger, company audit or engineering reproduction. Important research can be extensive, but unrelated sections and tasks are omitted.

The initializer creates a minimal report and state. Project-linked output goes to `输出文档/03_研究与分析/`; market models and figures are created only when useful. Validation checks the modules and artifacts actually requested. Existing detailed models and historical source files remain usable. Model choice belongs in runtime settings, not the skill.

## What It Can Produce

- Technical foundations, signal chains, and route-level mechanism diagrams.
- Consistent comparisons of technology routes, substitutes, and engineering trade-offs.
- Five-year technology-development milestones across research, engineering, manufacturing, standards, product form, and adoption.
- Global and China competitive landscapes covering incumbents, startups, OEM self-build, and substitutes.
- Auditable five-year global and China market forecasts with scenarios, sensitivity, and explicit driver sources.
- Decision-oriented investment views, proof gates, disconfirming evidence, and valuation implications.
- A responsive local HTML report with SVG figures and working relative links.
- Optional retrieval from and writeback to the private AI Work Hub Memory Graph.
- Retrieval and reuse of existing private expert interviews and thematic sources without duplicating them.

The workflow treats papers and reputable third-party reports as evidence inputs, not conclusion authorities. It separates facts, source claims, external forecasts, and the report's own assumptions before rebuilding the analysis.

## Install

```bash
mkdir -p ~/Documents/skills-repos ~/.codex/skills
cd ~/Documents/skills-repos
git clone https://github.com/guyu980/ai-work-hub-deep-research-skill.git
ln -s "$(pwd)/ai-work-hub-deep-research-skill/ai-work-hub-deep-research" \
  ~/.codex/skills/ai-work-hub-deep-research
```

Inspect an existing destination before replacing it. Reload Codex if the Skill does not appear immediately.

## Use

Standalone industry research:

```text
Use $ai-work-hub-deep-research to research industrial tactile sensing, including technical mechanisms, route comparisons, global and China competition, five-year technology trends and market sizing, visuals, and an investment view.
```

Project-linked research:

```text
Use $ai-work-hub-deep-research for this project. Read the project materials first, then independently reconstruct the industry and show what the company must prove.
```

Chat-only research:

```text
Use $ai-work-hub-deep-research, but keep the work in chat and do not create files.
```

## Companion Skills

- `ai-work-hub-diligence` owns the evolving company judgment, project state, and follow-up diligence.
- `ai-work-hub-memory-graph` ingests and lightly analyzes non-project interviews or thematic sources, then retrieves and stores sparse reusable project, sector, technical, valuation, event, and people knowledge.

`知识来源/` is a research input layer, not a fourth report mode. Use this Skill only when the user explicitly requests deep research or a formal systematic report; bounded external checks stay in the source workflow; the original source and its core note remain in one source folder. The deep-research report remains a separate deliverable. A project judgment changes through the diligence workflow after the report is finalized.

## Repository Boundary

This public repository contains only reusable instructions, scripts, references, and templates. Never commit real BPs, transcripts, customer information, project judgments, credentials, model files containing private data, or generated Memory Graph contents.

License: [MIT](LICENSE)
