---
title: "Seasonality"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [stocks, commodities, behavioral-finance, market-regime]
aliases: ["Seasonal Patterns", "Seasonal Effects", "Market Seasonality"]
domain: [behavioral-finance, market-microstructure]
prerequisites: ["[[market-anomalies]]"]
difficulty: beginner
related: ["[[calendar-effects]]", "[[calendar-effects-anomalies]]", "[[commodity-seasonality-patterns]]", "[[seasonal-spread-trading]]", "[[arbitrage-seasonality]]", "[[market-anomalies]]", "[[behavioral-finance]]", "[[sector-rotation]]"]
---

**Seasonality** is the tendency for an asset's returns, volatility, or supply/demand to follow recurring patterns tied to the time of year, month, week, or day rather than to price action or fundamentals. It is one of the oldest documented families of [[market-anomalies]], and it spans two quite different mechanisms: **calendar effects** in financial assets (driven by fund flows, taxes, and behaviour) and **physical seasonality** in commodities (driven by weather, harvests, and demand cycles). This page is the hub; the detailed treatments live in [[calendar-effects]] and [[commodity-seasonality-patterns]].

## The Two Kinds of Seasonality

| | Financial / calendar seasonality | Physical / commodity seasonality |
|---|---|---|
| **Driver** | Fund flows, tax rules, [[behavioral-finance|behaviour]], mandatory rebalancing | Weather, planting/harvest cycles, heating/cooling demand |
| **Examples** | January Effect, Sell in May, Santa Claus Rally, turn-of-month | Natural-gas winter demand, grain harvest lows, gasoline summer-driving season |
| **Durability** | Decays as it is arbitraged; sticky only where structural flows persist | More durable — rooted in real-world supply chains |
| **Detail page** | [[calendar-effects]], [[calendar-effects-anomalies]] | [[commodity-seasonality-patterns]], [[seasonal-spread-trading]] |

## Equity Calendar Effects (summary)

The most documented equity patterns — covered in full at [[calendar-effects]] — include the **January Effect** (small caps rebound after December tax-loss-harvesting selling), the **Sell in May / Halloween Indicator** (the Nov–Apr half historically beats May–Oct), the **Santa Claus Rally** (the last five sessions of December plus the first two of January), the **turn-of-month effect**, and quarter-end **window dressing**. Many have weakened as they became widely known; those tied to durable structural [[fund-flows]] (payrolls, pensions, mandatory rebalancing) have held up better than those tied to pure sentiment.

## Commodity Seasonality (summary)

Physical commodities carry the strongest, most persistent seasonality because real supply and demand move with the calendar — see [[commodity-seasonality-patterns]]. Natural gas and heating oil firm into winter; gasoline and electricity peak with the summer driving and cooling seasons; grains (corn, soybeans, wheat) tend to bottom around harvest and firm in the lean season; livestock (lean hogs, cattle) follow breeding and slaughter cycles. These patterns underpin [[seasonal-spread-trading]] and weather-driven [[arbitrage-seasonality|seasonal arbitrage]].

## Why Seasonality Is Tradeable but Treacherous

- **It is a [[market-anomalies|conditional anomaly]], not a guarantee.** A pattern that holds "on average" over decades can fail for several years in a row; sample sizes are tiny (only ~100 Januaries of clean data exist).
- **Decay and crowding.** Once a calendar edge is published and arbitraged, its [[edge-taxonomy|edge]] erodes. Commodity seasonality decays less because it is anchored to physical reality.
- **Overfitting risk.** With enough calendar slices, spurious patterns appear by chance — seasonality is a classic [[overfitting]] trap. Demand a plausible *mechanism* (a flow, a tax, a weather driver), not just a backtested curve.
- **Best used as an overlay.** Seasonality is typically a low-conviction timing tilt layered on top of a primary strategy, sized small, rather than a standalone system.

## Related

- [[calendar-effects]] — full treatment of equity calendar anomalies
- [[commodity-seasonality-patterns]] — physical commodity seasonal cycles
- [[seasonal-spread-trading]] — trading the calendar spread between contract months
- [[market-anomalies]] — the broader family seasonality belongs to

## Sources

No dedicated source summary yet — this hub consolidates material already documented in [[calendar-effects]], [[calendar-effects-anomalies]], and [[commodity-seasonality-patterns]]. Add a source citation when a specific reference is ingested.
