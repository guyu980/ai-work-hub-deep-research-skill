# Decision-Relevant Market Sizing

Use only when sizing answers the research question. Choose geography, horizon and depth accordingly; five-year Global and China forecasts are not mandatory. An order-of-magnitude range can be more honest and useful than a detailed model with unsupported inputs.

## Contents

1. Boundary and unit
2. Bottom-up model
3. Scenarios and sensitivity
4. Cross-checks
5. TAM, SAM, and SOM

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
annual revenue = new sales + replacement + recurring revenue per active unit
```

Usage industries:

```text
annual revenue = active users or assets × usage frequency × paid conversion × revenue per use
```

Capacity industries:

```text
annual revenue = deployed capacity × utilization × price per capacity unit
```

Show the driver table, not only final totals. Every driver must be tagged as actual, external forecast, company/source claim, or report assumption.

When modeling both global and China, build them separately rather than assigning an arbitrary share, and reconcile without double counting.

## Scenarios And Sensitivity

Use scenarios or sensitivity when the uncertainty matters. Vary drivers with a causal reason, such as units, penetration, price, utilization or replacement. Do not fabricate scenarios simply to fill rows.

For every model:

- use the requested or decision-relevant forecast horizon;
- show the base-year anchor when available;
- state the largest uncertainty;
- test the material uncertain drivers, without requiring every sensitivity format;
- explain step changes, price declines, and penetration curves;
- avoid precision beyond the quality of inputs.

Use CAGR as a summary of the constructed model, not as the construction method.

## Cross-Checks

Choose the informative cross-checks available:

- top-down industry or adjacent-market share;
- revenue capacity of identified vendors;
- customer capex or product gross-margin envelope;
- component shipment or installed-base constraints;
- manufacturing capacity or supply-chain availability;
- comparable adoption curves;
- expert/customer willingness-to-pay checks.

Explain mismatches. Do not average incompatible estimates.

## TAM, SAM, And SOM

- TAM: all paid demand inside the defined boundary.
- SAM: segments the product and go-to-market can actually serve within the horizon.
- SOM: a capacity-, sales-cycle-, competition-, and pricing-constrained share of SAM.

For project-linked work, derive SOM from design wins, customer conversion, production capacity, sales cycle, price, and retention. A top-down market-share percentage without an operating mechanism is not SOM.

The bundled `forecast_market.py` supports a transparent shipment/BOM driver table. Use a custom model for other economic units and document it in the report.
