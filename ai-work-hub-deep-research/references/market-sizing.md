# Five-Year Global And China Market Sizing

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
- global and China definitions;
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

Build global and China separately. Do not derive China as an arbitrary percentage of global unless that share has a causal model. Reconcile China into global without double counting.

## Scenarios And Sensitivity

Create conservative, base, and upside scenarios. Vary only drivers with a causal reason. Typical drivers include units, penetration, ASP/BOM, service ratio, replacement cycle, utilization, and FX.

For every model:

- include five annual forecast years;
- show the base-year anchor when available;
- state the largest uncertainty;
- run at least one one-way sensitivity and one combined downside/upside scenario;
- explain step changes, price declines, and penetration curves;
- avoid precision beyond the quality of inputs.

Use CAGR as a summary of the constructed model, not as the construction method.

## Cross-Checks

Use at least two:

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
