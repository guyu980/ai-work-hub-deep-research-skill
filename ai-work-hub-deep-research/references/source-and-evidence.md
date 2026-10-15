# Source And Evidence Protocol

## Contents

1. Source hierarchy
2. Read the evidence behind the conclusion
3. Proportionate source notes
4. Precision and conflicting evidence
5. Citation rules

## Source Hierarchy

Use the strongest available source for each claim:

| Grade | Typical sources | Appropriate use |
| --- | --- | --- |
| A | Standards; regulators; official statistics; peer-reviewed papers; original datasets; filings; contracts or customer confirmation | Mechanisms, definitions, measured results, official totals, verified commercial facts |
| B | Reputable preprints; patents; company technical documentation; industry associations; named expert interviews; strong third-party research with disclosed methods | Recent technical work, product specifications, market structure, model inputs |
| C | Company BP/teaser; vendor benchmark; investor presentation; media report; database summary; unnamed channel check | Attributed inputs and leads; corroborate where decisive or materially conflicting |
| D | Aggregator pages; SEO market reports; unsourced charts; reposts; social media claims | Discovery only; do not anchor a decision or forecast |

Peer review does not make a laboratory result commercially proven. A company filing does not make management guidance certain. A reputable third-party report remains one model with its own market definition.

Source grades are a starting guide, not a universal credibility score. Evaluate directness, method, scope, incentives and recency for the particular claim. A current customer account may establish a purchase that an older industry report cannot; an official product page establishes what the vendor advertises, not independent performance. Do not request contracts or customer access merely because they appear in the hierarchy.

## Read The Evidence Behind The Conclusion

For decisive sources, read enough of the original material to understand how its conclusion was obtained and whether it supports the report's use. Search snippets, abstracts and secondhand summaries are navigation aids, not adequate substitutes when the main thesis depends on the omitted details.

- **Technical literature:** inspect the method, system setup, baseline, evaluation conditions, results and limitations. Distinguish a proposed mechanism, simulation, controlled experiment and field result. Check whether the reported improvement survives the task, scale, latency, cost or operating constraints relevant to the study. Read relevant contrary findings or subsequent work when they affect interpretation.
- **Products and deployments:** identify what is available, what was announced, what has actually been deployed and for which task. Separate capability from adoption, pilots from repeat procurement and technical success from commercial economics.
- **Financial and industry data:** inspect definitions, coverage, period, units and estimation method. Trace a consequential chart to its underlying dataset or original table when available. A market-report headline does not establish a reliable denominator.
- **Interviews and company materials:** preserve the speaker's scope and context, separating firsthand observations from estimates, aspirations and sales claims. Attribute usable inputs instead of either treating them as confirmed facts or discarding them for lacking an audit.

Seek genuinely different evidence for conclusions that span several domains. Technical feasibility, customer demand and retained pricing power require different observations. Several articles quoting one press release, several reports reusing one estimate, or several agents summarizing one paper are one evidence lineage. Identify that dependence before calling the conclusion corroborated.

Research should include serious alternatives and disconfirming evidence, not only sources naming the preferred technology. Historical failures, customer self-build, slower adoption or a cheaper substitute may explain the industry better than the latest positive announcement. Do not mechanically balance evidence when one interpretation is substantially better supported.

## Proportionate Source Notes

Keep citations near key claims and distinguish sourced facts, attributed opinions and analyst assumptions in the report. Use the central-question evidence map described in [research-method.md](research-method.md) to track what the study can and cannot establish. No routine claim-by-claim CSV or repeated provenance labels. A short table is useful when conflicting estimates, model inputs or competing interpretations materially affect the conclusion.

Company statements and expert observations can be used as attributed inputs. Independent confirmation is warranted for material conflicts or decisive claims, not for every number. A faithful transcript establishes the speaker's statement, not the underlying business result.

For a decisive claim with only one available source, state the limitation and assess the conclusion's dependence on it. A standard's published text need not have a second source to establish its provisions; a company's unique forecast cannot become verified demand through repetition. Legacy ledgers may remain linked to historical reports. Do not generate new ones unless the user explicitly requests detailed evidence auditing.

## Precision And Conflicting Evidence

Reconcile the quantities that carry the argument before calculating or comparing them. Preserve original units and periods in working notes, show necessary conversions, and distinguish actuals, announced plans and forecasts. Check arithmetic and whether the comparison uses equivalent system boundaries or performance conditions. The required precision is highest where an error could reverse the route preference, economic result or investment view; it is not a demand to audit every background fact.

When sources conflict:

1. Check market boundary, geography, base year, nominal/real currency, shipment versus installed base, revenue versus contract value, gross versus net value, and hardware versus services. For performance claims, compare workload, baseline, hardware, quality target and operating conditions.
2. Check whether one source is forecasting and another is reporting actuals.
3. Trace the discrepancy to method, coverage, timing or incentives; read the relevant source details instead of choosing the convenient result.
4. Prefer the more direct and transparent evidence for the question, not the larger, newer or more numerous estimate by default.
5. Recalculate on a comparable basis where feasible. For economic claims, rebuild from observable drivers and test the remaining range.
6. Explain what the unresolved difference changes. If it does not alter the judgment, show why; if it does, narrow or condition the conclusion.

Never average forecasts with incompatible definitions. Never derive false precision from a third-party CAGR. A material unresolved contradiction should trigger another research pass or a revised conclusion, not disappear into a generic disclaimer.

## Citation Rules

- Cite current public facts with live links when public research was used.
- Include publication dates for time-sensitive claims and distinguish the date of the underlying event or measurement.
- Label paywalled, excerpt-only, translated, or secondary access.
- Preserve paper version and decisive benchmark conditions; provide page, table or section pointers where they make the result meaningfully easier to inspect.
- Record source language when translation can affect meaning.
- Keep private materials in the project archive; do not expose private file paths or contents in a public repository.
- Treat generated charts as this report's analysis and cite the underlying sources and driver/model file beneath them. Identify conceptual diagrams and illustrative numbers explicitly.
