---
title: "ISM PMI"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [fundamental-analysis, indicators, market-regime, event-driven]
aliases: ["ISM PMI", "ISM-PMI", "Purchasing Managers Index", "ISM Manufacturing", "ISM Services", "PMI"]
domain: [indicators]
prerequisites: ["[[economic-indicators]]", "[[business-cycle]]"]
difficulty: intermediate
related: ["[[economic-indicators]]", "[[business-cycle]]", "[[sector-rotation]]", "[[fed-policy]]", "[[non-farm-payrolls]]", "[[yield-curve]]"]
---

The ISM Purchasing Managers' Index, published monthly by the Institute for Supply Management, is one of the most closely watched [[economic-indicators|leading economic indicators]] in financial markets. It is a diffusion index based on surveys of purchasing managers at over 400 firms, providing an early read on economic momentum before harder data like GDP is available. A reading above 50 indicates expansion; below 50 indicates contraction.

## How the Diffusion Index Is Built

The PMI is a **diffusion index**, not a measure of magnitude. Each surveyed purchasing manager answers whether a given activity (new orders, production, employment, etc.) is *better*, *the same*, or *worse* than the prior month. For each sub-index:

```
Diffusion index = (% reporting "better") + 0.5 × (% reporting "the same")
```

The headline ISM Manufacturing PMI is a weighted composite of five equally weighted sub-indices: New Orders, Production, Employment, Supplier Deliveries, and Inventories. Because answers are directional, the index captures the *breadth* of change across firms — how many companies are improving — rather than the size of the change at any one firm. This is what makes it a timely, leading signal: managers adjust orders and hiring before output and GDP actually move.

## Two Reports

### ISM Manufacturing PMI

Released on the **first business day of each month** (covering the prior month), this is the original and more market-moving of the two reports. It surveys purchasing managers at manufacturing firms across 18 industries. Despite manufacturing representing only about 11% of US GDP, the index is valued because manufacturing is cyclically sensitive and tends to lead the broader economy.

### ISM Services PMI (Non-Manufacturing)

Released on the **third business day of each month**, this covers the services sector, which represents roughly 77% of US GDP. While less historically established (introduced in 1998), it has grown in importance given the services-dominated nature of the modern economy.

## Key Sub-Indices

Each ISM report contains several sub-indices, each providing distinct signals:

| Sub-Index | What It Measures | Trading Significance |
|-----------|-----------------|---------------------|
| **New Orders** | Demand pipeline | Most forward-looking; leads the headline by 1-2 months |
| **Production** | Current output levels | Coincident indicator of manufacturing activity |
| **Employment** | Hiring/firing trends | Previews the monthly [[non-farm-payrolls]] report |
| **Supplier Deliveries** | Supply chain speed | Rising = slower deliveries = strong demand or supply disruption |
| **Inventories** | Stock levels | Rising inventories can signal future production cuts |
| **Prices Paid** | Input cost pressures | Inflation preview; watched closely by the [[fed-policy|Federal Reserve]] |

The **New Orders** sub-index is the single most important component for traders, as it is the most forward-looking measure of economic demand. A divergence between new orders and the headline reading often foreshadows the headline's next move.

## Interpreting Readings

- **Above 50**: Expansion -- the sector is growing
- **Below 50**: Contraction -- the sector is shrinking
- **50 exactly**: No change from the prior month
- **Above 55**: Strong expansion
- **Below 45**: Significant contraction, often consistent with recession

Historical data shows the ISM Manufacturing PMI has a strong track record predicting recessions. When the index falls below 45 and stays there, every instance since 1948 has coincided with a recession as defined by the NBER. The threshold between GDP expansion and contraction is actually closer to 48.7 based on historical correlation -- the economy can still grow even with manufacturing in mild contraction.

## Market Impact

The ISM Manufacturing PMI is released at 10:00 AM ET on the first business day of each month, making it one of the earliest major indicators for the new month. Markets react to the **surprise** -- the difference between the actual reading and the consensus forecast. A beat typically boosts equities and cyclical sectors while pressuring [[bond-market|bonds]] (higher yields). A miss does the opposite.

The Prices Paid sub-index carries additional weight in inflationary environments, as it influences expectations for [[fed-policy|Fed tightening]]. During 2021-2022, Prices Paid readings above 75 contributed to hawkish Fed repricing across the [[yield-curve]].

## Relationship to the Business Cycle

The ISM PMI is a core input in [[business-cycle]] phase identification. In [[sector-rotation]] strategies, a PMI crossing above 50 from below signals early expansion (favor cyclical sectors like Technology and Consumer Discretionary), while a PMI crossing below 50 from above signals contraction (favor defensive sectors like Utilities and Healthcare). The rate of change matters as much as the level -- a PMI at 52 but falling carries different implications than a PMI at 52 and rising.

## Sources

- Institute for Supply Management — *ISM Report On Business* (Manufacturing PMI and Services PMI), official monthly releases and methodology, ismworld.org.
- Federal Reserve Bank of St. Louis (FRED) — ISM Manufacturing PMI historical series and recession-correlation data.
- Conference Board / NBER business-cycle dating documentation — context for the PMI as a leading indicator.

## Related

- [[economic-indicators]] -- broader overview of all indicator categories
- [[business-cycle]] -- the cycle the PMI helps identify
- [[sector-rotation]] -- strategy that uses PMI as a cycle signal
- [[fed-policy]] -- the Fed monitors PMI for policy decisions
- [[non-farm-payrolls]] -- the employment sub-index previews NFP
- [[yield-curve]] -- Prices Paid feeds rate/yield expectations
