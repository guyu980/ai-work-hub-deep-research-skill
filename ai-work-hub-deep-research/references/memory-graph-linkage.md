# Memory Graph Linkage

Use the companion `ai-work-hub-memory-graph` skill and its live schema before changing structured objects.

## Retrieve Before Research Conclusions

Query the industry name, aliases, technical routes, value-chain layer, business model, important companies, and relevant valuation terms. Open useful source cards rather than relying on index summaries. When `<workspace_root>/知识来源/` exists, search relevant core notes as a private source layer before external research.

Use retrieved context to find:

- prior projects and counterexamples;
- sector structure and recurring bottlenecks;
- technical mechanisms, benchmarks, and proof methods;
- valuation anchors and financing regimes;
- durable events and independently important experts.

Retrieval is context, not authority. Recheck time-sensitive claims.

Use the question and business/technical mechanisms, not just sector names. Retrieval also covers running judgments and structured GitHub radar candidates; use them as source pointers, not permission to open a new diligence task. Preserve observation dates and distinguish old research snapshots from current project decisions.

## Route After The Report Is Final

| Research increment | Direct destination |
| --- | --- |
| Current company view or company-specific evidence | Project folder/state and project card through diligence |
| Reusable expert interview or thematic source | Its single `知识来源/` source folder; link it from the report and graph objects |
| Repeated market structure, adoption sequence, or value-capture view | Existing sector map |
| Mechanism, route comparison, benchmark, bottleneck, or validation method | Existing technical theme |
| Reusable financing or price comparison | Existing valuation anchor |
| Durable external change affecting several projects or a sector | Event card when it meets the graph threshold |
| Independently important founder, scientist, professor, or operator | People card when it meets the graph threshold |
| Useful but unsafe to route | Review queue, if supported by the live graph |
| Low-signal or one-off detail | Report archive only |

Do not duplicate one finding across several new cards. Update existing objects when possible. Keep source detail in `知识来源/`, report analysis and citations in the report archive, and only compressed reusable conclusions in graph cards. A source does not need a graph card or source index.

## Completion

After writeback:

1. Refresh project headers from finalized state when applicable, then reread the card and update its substance. The sync script does not rewrite prose.
2. Rewrite affected current-understanding sections using the same-type structure in the graph schema. Use `write_graph.py` with expected hashes, rereading and merging on conflict. The batch writer rebuilds once; no rebuild is needed for read-only work.
3. Validate the graph.
4. Report validation failures explicitly.
5. Keep all private graph data outside the public Skill repository.

Keep operating metrics and valuations comparable: period, unit, actual/forecast and source near the fact; equity, debt and acquisition consideration in separate groups. Current project prices/decisions stay in the single project judgment. A research snapshot may retain its dated recommendation without becoming a parallel current decision.
