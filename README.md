# AI Work Hub Deep Research

[中文说明](README.zh-CN.md)

**Formal industry and technology research.** For explicitly requested deep research or systematic reports, choose technical, competitive and economic analysis for the decision, with Markdown and browsable HTML.

## Install And Update

Ask Codex to install the Skill from this repository and inspect any existing installation first. A Git checkout plus one symlink keeps personal and shared versions on the same source:

```bash
mkdir -p ~/Documents/skills-repos ~/.codex/skills
cd ~/Documents/skills-repos
git clone https://github.com/guyu980/ai-work-hub-deep-research-skill.git
ln -s "$(pwd)/ai-work-hub-deep-research-skill/ai-work-hub-deep-research" ~/.codex/skills/ai-work-hub-deep-research
```

Inspect an existing destination instead of overwriting it or creating duplicate Skills. Python scripts require Python 3.10+; Graph locking supports macOS/Linux. Reload Codex after installation. To update:

```bash
cd ~/Documents/skills-repos/ai-work-hub-deep-research-skill
git pull --ff-only
```

The symlink uses the updated source directly. Keep the private workspace separate.

## Daily Use

```text
Use $ai-work-hub-deep-research to study this technology, focusing on route trade-offs, customer value and investment opportunities.
Independently reconstruct this project's industry and the assumptions supporting or challenging its current view.
Keep the study in chat only.
```

Reuse current project reasoning, prior research and expert sources. Mechanisms, competition, market models, technology trends and valuation are optional modules selected for the question, not mandatory five-year forecasts or audits. Important studies can be extensive without claim-by-claim ledgers or default engineering reproduction.

Project reports go under `输出文档/03_研究与分析/`; standalone studies under `行业研究/<theme>/`. Initialization creates only the minimal report/state. Models and figures are on demand; responsive HTML uses the existing restrained cardinal-red design.

Reports are dated research snapshots. Routine later news updates current Graph/project understanding, not every historical HTML. Regenerate for a consequential or requested revision; retain older studies that answer different questions.

```bash
python3 ai-work-hub-deep-research/scripts/render_report.py --input "<report.md>" --output "<report.html>" --title "<title>"
python3 ai-work-hub-deep-research/scripts/validate_research.py --report "<report.md>" --html "<report.html>"
```

## How The Skills Connect

[Diligence](https://github.com/guyu980/ai-work-hub-diligence-skill) owns current company decisions; [Memory Graph](https://github.com/guyu980/ai-work-hub-memory-graph-skill) owns non-project sources and cross-project synthesis; [Deep Research](https://github.com/guyu980/ai-work-hub-deep-research-skill) owns explicitly requested formal studies. Companions are optional and installable separately. Authorized intelligence tasks discover; Skills do not schedule themselves.

This repository contains generic mechanisms, scripts and fictional examples only. Real projects, knowledge, reports, watchlists, delivery destinations and credentials remain private. Contribute via PR for maintainer review. Model selection belongs in runtime settings.

[Agent instructions](ai-work-hub-deep-research/SKILL.md) · [MIT License](LICENSE)
