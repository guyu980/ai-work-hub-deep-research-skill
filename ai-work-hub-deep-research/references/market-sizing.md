# Economic Analysis And Market Sizing

Build an independent economic analysis when market scale, cost advantage, adoption or value capture is central to the research question. Do not substitute a quoted market forecast for the analytical work. Choose the economic unit, geography and horizon to fit the question; a five-year table or TAM/SAM/SOM labels are not required. A defensible range can be more useful than a precise point estimate, but deriving that range still requires evidence, clear drivers and checks against real constraints.

## Contents

1. Boundary and unit
2. Bottom-up model
3. Customer and supplier economics
4. Scenarios, sensitivity and counterfactuals
5. Cross-checks and reconciliation
6. TAM, SAM, and SOM

## Boundary And Unit

Write a one-sentence market definition before calculating. Specify:

- product or service included;
- customer and paid transaction;
- new shipments, installed base, replacement, usage, seats, capacity, or another unit;
- hardware, software, services, NRE, maintenance, and internal OEM production treatment;
- definitions for the geographies actually modeled;
- nominal currency, FX, and exact forecast years.

Avoid double counting bundled components, channel revenue, internal transfer value, and services already included in product ASP.

## Bottom-Up Model

Use the model that matches the economic unit.

Shipment/BOM industries:

```text
hardware revenue = addressable units × paid penetration × BOM or ASP
total revenue = hardware revenue + software + service + NRE + maintenance
```

Installed-base industries:

```text
ending installed base = prior base + additions - retirements
annual revenue = new-unit revenue + replacement revenue
               + average billable active units × annual recurring revenue per unit
```

Usage industries:

```text
annual revenue = active users or assets × annual uses per user or asset
               × paid fraction of uses × realized price per paid use
```

Capacity industries:

```text
annual revenue = deployed capacity × utilization × realized revenue per utilized capacity-year
```

Show the driver table, not only final totals. Every driver must be tagged as actual, external forecast, company/source claim, or report assumption.

Keep the time and aggregation basis explicit. For recurring charges, use the average billable base over the period or calculate by billing interval, not an unadjusted year-end stock. If capacity prices are quoted per hour or month, include the corresponding time factor. Define whether additions and new-unit revenue include replacements so the same sale is not counted twice.

When modeling both global and China, build them separately rather than assigning an arbitrary share, and reconcile without double counting.

Segment where buyers, usage, price or adoption constraints differ materially. Explain the bridge from today's observed base to the forecast: eligible customers, conversion, deployment pace, usage, price and replacement as relevant. Do not apply one penetration curve to unlike segments merely to simplify a spreadsheet.

Document definitions, formulas and source-to-input transformations so another analyst can reconstruct the decisive calculations. Save a model or calculation file when the analysis is substantial; a small transparent calculation can remain in the report. Check units, stock/flow consistency and arithmetic, not just whether the final number looks plausible.

## Customer And Supplier Economics

Market growth does not establish a worthwhile purchase or a profitable supplier. Build the economics relevant to the thesis at both levels:

- **Customer:** compare the current alternative with the proposed system at an equivalent useful outcome. Include the cost drivers that matter, such as purchase, integration, utilization, labor, energy, errors, downtime and replacement. Distinguish savings available in principle from savings a customer can actually realize. Identify the adoption threshold, payback or budget constraint where useful. Estimated customer value is not automatically the price a supplier can charge.
- **Supplier:** connect paid volume and realized price to gross profit and the costs needed to sell, customize, deliver and support the product. Examine whether reuse, scale or learning improves later units, and whether falling prices or service burden offsets that improvement. Use ranges when cost visibility is limited; do not fabricate private margins.
- **Industry profit distribution:** explain which layers retain bargaining power as cost falls or standards improve. Distinguish more spending on a capability from a larger profit pool for the companies under consideration. Examine bundling, substitutes, customer self-build, concentration and switching costs where they influence price.

Use [technology-and-competition.md](technology-and-competition.md) to connect claimed technical gains to these economic quantities. A faster component or higher benchmark score does not itself establish better system economics.

## Scenarios, Sensitivity And Counterfactuals

Test the uncertain drivers that could change the conclusion. Vary them with a causal reason, such as adoption, price, utilization, replacement, delivery cost or customer savings. Use scenarios for different mechanisms and sensitivity for uncertainty within a mechanism. Do not fabricate scenarios simply to fill rows.

For every model:

- use the requested or decision-relevant forecast horizon;
- show the base-year anchor when available;
- state the largest uncertainty;
- test the material uncertain drivers, without requiring every sensitivity format;
- explain step changes, price declines, and penetration curves;
- avoid precision beyond the quality of inputs.

Respect relationships between drivers: lower prices may increase adoption, higher utilization may require more investment, and faster sales may raise support costs. Explain the relationship or show separate conditional cases; independently selecting all favorable assumptions can create an impossible upside case.

Where informative, calculate the threshold at which the judgment reverses: the minimum utilization for cost advantage, maximum delivery effort for acceptable margin, price required to recover acquisition cost, or adoption needed to justify a market claim. Compare that threshold with available evidence rather than declaring the outcome attractive because the base case says so.

Use a counterfactual to isolate what matters. If the new technology were unavailable, what would customers buy, spend or delay? If the main claimed advantage became standard, what would remain scarce and payable? Quantify the material difference when inputs permit. Do not present an illustrative counterfactual as an observed outcome.

Use CAGR as a summary of the constructed model, not as the construction method.

## Cross-Checks And Reconciliation

Challenge the model with evidence derived differently from its construction. Reusing the same industry forecast in both the input and the cross-check does not provide independent support. Choose checks that can actually constrain the answer:

- top-down industry or adjacent-market share;
- revenue capacity of identified vendors;
- customer capex or product gross-margin envelope;
- component shipment or installed-base constraints;
- manufacturing capacity or supply-chain availability;
- comparable adoption curves;
- expert/customer willingness-to-pay checks.

Investigate material mismatches. A demand model above plausible production capacity may imply supply constraints, incorrect units or double counting; a large modeled market alongside small vendor revenues may imply slow adoption, internal production, an incorrect boundary or unobserved suppliers. Determine which explanation fits the evidence and revise the model or judgment. Do not average incompatible estimates or leave contradictory totals side by side without explanation.

Present the resulting range, what drives it and what remains robust across it. If a critical input cannot be bounded, identify which conclusion the model cannot support instead of filling the gap with a precise assumption.

## TAM, SAM, And SOM

- TAM: all paid demand inside the defined boundary.
- SAM: segments the product and go-to-market can actually serve within the horizon.
- SOM: a capacity-, sales-cycle-, competition-, and pricing-constrained share of SAM.

For project-linked work, derive SOM from design wins, customer conversion, production capacity, sales cycle, price, and retention. A top-down market-share percentage without an operating mechanism is not SOM.

The bundled `forecast_market.py` supports a transparent shipment/BOM driver table. Use a custom model for other economic units and document it in the report.
