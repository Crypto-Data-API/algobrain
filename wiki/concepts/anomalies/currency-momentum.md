---
title: "Currency Momentum"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, forex, momentum, macro, academic-research]
aliases: ["FX Momentum", "Cross-Currency Momentum"]
domain: [anomalies, forex]
prerequisites: ["[[momentum-anomaly]]", "[[carry-anomaly]]"]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[momentum-anomaly]]", "[[time-series-momentum]]", "[[carry-anomaly]]"]
---

# Currency Momentum

Currencies that have strengthened over a recent lookback window (typically 1-12 months) continue to strengthen in the subsequent month, while weakening currencies continue to weaken. This is the FX analog of [[momentum-anomaly]] and has been documented across both developed and emerging market currencies. It is one of two major FX anomalies (alongside carry) that survives out-of-sample and forms the backbone of most systematic FX hedge fund strategies.

## What

For a basket of ~20 currencies quoted against the USD, rank each month on its return over the prior 3-12 months. Long the top-quintile currencies, short the bottom-quintile currencies, equal-weight within quintiles. Rebalance monthly. Menkhoff, Sarno, Schmeling, Schrimpf (2012) report annualized excess returns of ~6-9% with Sharpe ratios of 0.5-1.0 depending on the lookback and rebalancing conventions.

## Original Paper

- Okunev & White (2003) "Do Momentum-Based Strategies Still Work in Foreign Currency Markets?" — *Journal of Financial and Quantitative Analysis*
- Menkhoff, Sarno, Schmeling, Schrimpf (2012) "Currency Momentum Strategies" — *Journal of Financial Economics*
- Moskowitz, Ooi, Pedersen (2012) time-series momentum paper includes FX

## Mechanism

- **Delayed response to macroeconomic fundamentals** — central bank policy changes, inflation surprises, and terms-of-trade shifts are absorbed gradually into exchange rates
- **Limits to arbitrage in emerging market FX** — the effect is strongest in currencies with higher trading costs, consistent with incomplete arbitrage
- **Investor underreaction / sluggish information diffusion** — same mechanism hypothesized for equity momentum (Hong-Stein, Barberis-Shleifer-Vishny)
- **Carry-momentum interaction** — momentum currencies tend to also have positive carry, so some of the premium overlaps with the [[carry-anomaly]]

Menkhoff et al. found that currency momentum and carry are largely *independent* — combining them improves risk-adjusted returns meaningfully.

## Edge Category

**Behavioral** (underreaction) + some **structural** (transaction-cost-driven limits to arbitrage).

## Replication Status

Replicated across multiple samples, lookback windows, and currency universes. It has held up in developed-market FX but with decaying magnitude, and remains stronger in emerging market currencies (which are harder and more expensive to trade).

## Decay History

Some decay since Okunev-White (2003) and especially post-2008. Developed-market FX momentum is weaker than it was in 1990s data. Emerging market FX momentum has held up better.

## Current Viability

Tradeable by systematic FX funds, with capacity in the low billions. Typically combined with [[carry-anomaly]] and [[time-series-momentum]] in a composite systematic FX strategy.

## Related Strategies

- [[momentum-anomaly]] — equity analog
- [[time-series-momentum]] — time-series version, applied to FX
- [[carry-anomaly]] — complementary, low correlation
- Systematic FX hedge fund strategies

## Sources

- Okunev & White (2003) — first major FX momentum paper
- Menkhoff, Sarno, Schmeling, Schrimpf (2012) — canonical reference
- Asness, Moskowitz, Pedersen (2013) "Value and Momentum Everywhere"
- Moskowitz, Ooi, Pedersen (2012) time-series momentum

## Related

- [[anomalies-overview]]
- [[momentum-anomaly]]
- [[time-series-momentum]]
- [[carry-anomaly]]
