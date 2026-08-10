# Source And Evidence Protocol

## Contents

1. Source hierarchy
2. Evidence ledger
3. Conflicts and forecast discipline
4. Citation rules

## Source Hierarchy

Use the strongest available source for each claim:

| Grade | Typical sources | Appropriate use |
| --- | --- | --- |
| A | Standards; regulators; official statistics; peer-reviewed papers; original datasets; filings; contracts or customer confirmation | Mechanisms, definitions, measured results, official totals, verified commercial facts |
| B | Reputable preprints; patents; company technical documentation; industry associations; named expert interviews; strong third-party research with disclosed methods | Recent technical work, product specifications, market structure, model inputs |
| C | Company BP/teaser; vendor benchmark; investor presentation; media report; database summary; unnamed channel check | Leads and claims requiring corroboration |
| D | Aggregator pages; SEO market reports; unsourced charts; reposts; social media claims | Discovery only; do not anchor a decision or forecast |

Peer review does not make a laboratory result commercially proven. A company filing does not make management guidance certain. A reputable third-party report remains one model with its own market definition.

## Evidence Ledger

Maintain a CSV with at least:

```text
claim_id,claim,category,status,evidence_grade,source_type,source_title,source_url,publish_date,accessed_date,geography,definition_or_metric,source_value,report_use,conflict_or_caveat
```

Recommended `status` values:

- `verified`: supported by appropriate original or independent evidence;
- `source_claim`: accurately captured but not independently verified;
- `report_assumption`: introduced by this analysis;
- `open`: material uncertainty or unresolved conflict.

Attach a source to the smallest meaningful claim. Do not use one citation at the end of a long paragraph to imply support for every sentence.

## Conflicts And Forecast Discipline

When sources conflict:

1. Check market boundary, geography, base year, nominal/real currency, shipment versus revenue, gross versus net value, and hardware versus services.
2. Check whether one source is forecasting and another is reporting actuals.
3. Prefer the more original and transparent method, not the larger or newer number by default.
4. Keep unresolved ranges visible.
5. Rebuild the report's own model from observable drivers.

Never average forecasts with incompatible definitions. Never derive false precision from a third-party CAGR.

## Citation Rules

- Cite current public facts with live links when public research was used.
- Include publication dates for time-sensitive claims.
- Label paywalled, excerpt-only, translated, or secondary access.
- Preserve paper version and benchmark conditions.
- Record source language when translation can affect meaning.
- Keep private materials in the project archive; do not expose private file paths or contents in a public repository.
- Treat generated charts as this report's analysis and cite the driver/model file beneath them.
