---
title: "Commodity Curve Roll Yield Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, commodities, futures, carry, academic-research]
aliases: ["Roll Yield Anomaly", "Commodity Backwardation Premium", "Erb-Harvey Anomaly"]
domain: [anomalies]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[carry-anomaly]]", "[[time-series-momentum]]"]
---

# Commodity Curve Roll Yield Anomaly

The shape of the commodity futures curve — specifically, whether the curve is in *backwardation* (front contracts priced higher than deferred) or *contango* (deferred higher than front) — systematically predicts subsequent futures returns. Commodities in backwardation earn positive roll returns, while commodities in contango bleed as they roll down their own curves. Erb & Harvey (2006) formalized this into a cross-sectional commodity carry strategy.

## What

For a universe of commodity futures (typically the liquid WTI, Brent, natural gas, heating oil, copper, aluminum, gold, silver, corn, wheat, soybeans, cattle, hogs, sugar, cocoa, coffee, cotton), compute each commodity's *roll yield*:

```
roll_yield = (front_price − second_month_price) / front_price  (annualized)
```

Positive roll yield = backwardation, negative = contango. Rank commodities monthly, long the top quartile (most-backwardated) and short the bottom quartile (most-contango). Erb-Harvey's long-short portfolio earned roughly 10% annualized in their sample.

## Original Paper

Erb, C. & Harvey, C. (2006) "The Strategic and Tactical Value of Commodity Futures" — *Financial Analysts Journal*. Extended by Gorton & Rouwenhorst (2006) and Miffre & Rallis (2007).

## Mechanism

- **Hedging pressure (Keynes's Theory of Normal Backwardation)** — commodity producers are natural short-hedgers; to clear the market, speculators must go long and demand a risk premium. When producers hedge aggressively the curve is in backwardation and speculators earn a larger premium.
- **Inventory / storage costs** — commodities with low inventories are in backwardation (spot scarcity); commodities with high inventories are in contango (storage costs priced in). Low-inventory states predict higher future spot prices because inventories revert.
- **Physical convenience yield** — holders of physical inventories earn a convenience yield from being able to meet unexpected demand, which shows up as backwardation in the curve.

All three mechanisms point the same direction: backwardation is a signal of positive expected returns.

## Edge Category

**Structural** (hedging pressure) + **analytical** (the curve shape is an observable signal).

## Replication Status

Replicated widely. Commodity carry is now a standard factor in multi-asset hedge funds and is the primary systematic commodity strategy alongside commodity momentum. Asness-Moskowitz-Pedersen (2013) confirm it as part of "Value and Momentum Everywhere."

## Decay History

Compressed since the 2000s commodity boom. The 2010s were particularly difficult for commodity carry because most commodities were in persistent contango (post-ZIRP + shale oil abundance). Post-2020 the strategy has recovered somewhat.

## Current Viability

Tradeable by systematic commodity funds. Capacity is moderate (billions, not tens of billions) because commodity futures markets are smaller than equity or FX. Typically combined with [[time-series-momentum]] in a composite strategy — commodity trend-following ETFs (e.g., the original DBC vs. enhanced-roll DBE) directly capture this effect.

## Related Strategies

- [[carry-anomaly]] — this is the commodity expression of carry
- [[time-series-momentum]] — classic commodity trend-following, highly complementary
- Enhanced-roll commodity index products that tilt toward backwardated contracts

## Sources

- Erb & Harvey (2006) "The Strategic and Tactical Value of Commodity Futures"
- Gorton & Rouwenhorst (2006) "Facts and Fantasies about Commodity Futures"
- Miffre & Rallis (2007) "Momentum Strategies in Commodity Futures Markets"
- Asness, Moskowitz, Pedersen (2013) "Value and Momentum Everywhere"

## Related

- [[anomalies-overview]]
- [[carry-anomaly]]
- [[time-series-momentum]]
