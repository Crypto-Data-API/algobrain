---
title: "Market Regime"
type: concept
created: 2026-07-01
updated: 2026-10-17
status: review
tags: [market-regime, regime-detection, quantitative, risk-management]
aliases: ["Market Regime", "Market Regimes", "Trading Regime", "Regime"]
domain: [portfolio-theory, market-regime]
prerequisites: ["[[volatility]]", "[[correlation]]", "[[market-cycles]]"]
difficulty: intermediate
related: ["[[market-cycles]]", "[[regime-detection]]", "[[market-regime-detection-ml]]", "[[volatility-regime]]", "[[correlation-regime]]", "[[regime-matrix]]", "[[regime-strategy-playbook]]", "[[business-cycle]]", "[[risk-on-risk-off-framework]]", "[[sector-rotation]]", "[[mean-reversion]]", "[[trend-following]]", "[[asset-allocation]]", "[[vix]]", "[[cryptodataapi]]"]
---

A **market regime** is a persistent statistical "state" of a market — a stretch of time during which the behaviour of returns (their trend, volatility, correlation, and risk appetite) is broadly consistent, before shifting to a qualitatively different state. Regimes are the reason a strategy that prints money for two years can quietly stop working: its edge was conditional on a regime that ended. Identifying which regime you are in, and sizing for the possibility that it changes, is one of the central problems of quantitative and discretionary trading alike.

## Regime vs Cycle

"Regime" and "[[market-cycles|market cycle]]" are related but not identical:

- A **[[market-cycles|market cycle]]** describes the recurring four-phase *progression* — accumulation, markup, distribution, markdown — and the sentiment arc that accompanies it.
- A **regime** describes the current *statistical state* (e.g. "low-volatility uptrend," "high-volatility risk-off") without committing to where you are in a repeating sequence. Regimes can persist, recur out of order, or skip phases.

In practice the cycle is the discretionary, narrative lens (Wyckoff, Dow Theory) and the regime is the quantitative lens that [[regime-detection]] and [[market-regime-detection-ml]] try to label statistically.

## The Main Regime Axes

Most regime frameworks classify markets along a few largely independent axes:

| Axis | Two poles | Typical signal |
|------|-----------|----------------|
| **Direction / trend** | Bull vs bear; trending vs ranging | Price vs long moving averages; ADX; higher-highs structure |
| **Volatility** | Low-vol calm vs high-vol stress | Realised vol, [[vix|VIX]], [[volatility-regime]] classification |
| **Risk appetite** | [[risk-on-risk-off-framework\|Risk-on vs risk-off]] | Credit spreads, cyclicals-vs-defensives, USD, gold |
| **Correlation / dispersion** | High vs low cross-asset correlation | [[correlation-regime]]; average pairwise correlation |
| **Liquidity / flow** | Ample vs tightening | Funding, central-bank balance sheet, breadth |

A useful shorthand crosses the first two axes into four quadrants — **quiet bull, volatile bull, quiet bear, volatile bear** — each of which rewards a different playbook (see [[regime-matrix]]).

## Why Regimes Matter

Different edges live in different regimes:

- **Trending / low-vol bull** rewards [[trend-following]], [[momentum]], breakout, and short-volatility strategies.
- **Range-bound / mean-reverting** regimes reward [[mean-reversion]], premium selling, and fading extremes.
- **High-vol risk-off** regimes reward defensives, long volatility, [[tail-risk]] hedges, and reduced gross exposure.
- **Correlation spikes** (everything moves together) destroy diversification exactly when it is needed, so risk parity and pairs trades degrade in high-correlation regimes.

Because edges are *conditional*, regime awareness is really about **strategy selection and position sizing**: turning a strategy up when its regime is present and down when it is not, rather than trying to run one static system through every environment (see [[regime-strategy-playbook]]).

## How Regimes Are Identified

- **Rule-based thresholds.** Simple, transparent labels: price above/below the 200-day average for trend; VIX above/below a threshold for vol; credit spreads widening for risk-off.
- **Statistical models.** Hidden Markov models (HMMs), Gaussian mixture models, and change-point detectors infer a latent regime variable from returns, volatility, and breadth features — the core of [[market-regime-detection-ml]].
- **Macro overlays.** Mapping regimes to the [[business-cycle]] (expansion, slowdown, recession, recovery) and to monetary policy, which drives [[sector-rotation]].

## Crypto-Specific Regime Axes

The generic axes above carry over to crypto, but crypto adds several axes of its own that often matter more for strategy selection:

| Axis | Poles | Typical signal | Strategies most exposed |
|------|-------|----------------|-------------------------|
| **Leverage / positioning** | Crowded long ↔ crowded short ↔ flat | [[funding-rate]] level and persistence, [[open-interest]] vs price, long/short ratio | [[crowded-long-funding-fade]], [[crowded-short-funding-fade]], [[oi-price-exhaustion]], [[oi-confirmed-trend]] |
| **Liquidation / deleveraging** | Orderly ↔ cascade | Realized [[liquidations]] bursts, liquidity fragility | [[long-liquidation-cascade]], [[post-liquidation-rebound]] |
| **Breadth / alt rotation** | BTC-led ↔ broad alt participation | Altcoin breadth, BTC dominance | [[breadth-and-momentum-divergence]], [[meme-coin-cycle]] |
| **Sentiment** | Extreme fear ↔ extreme greed | [[crypto-fear-and-greed-index]] | [[contrarian-extremes]], [[sentiment-positioning-divergence]] |
| **Cycle phase** | Accumulation → markup → distribution → markdown | Long-horizon regime label | [[distribution-post-peak-short-book]], [[full-bear-short-book]], [[defensive-majors]] |
| **Event / policy** | Quiet ↔ catalyst-dense | Event calendar, policy headline flow | [[macro-event-pump]], [[etf-and-institutional-flow]] |

Two crypto features make regime work harder than in TradFi. First, the market trades 24/7 and regime shifts often start in thin weekend or Asia-session liquidity (see [[2025-10-crypto-liquidation-cascade]]). Second, leverage is visible and reflexive: funding and OI *are* the regime as well as describing it, because the positioning they measure is what gets liquidated at the transition.

### Which strategies switch on which regime

The canonical mapping is [[regime-matrix]]; the operational version is [[regime-strategy-playbook]] and [[regime-adaptive-strategy]]. Range regimes switch on [[range-mean-reversion]] and [[range-trading]]. Calm high-vol-premium regimes favour [[options-premium-selling]] and [[short-volatility-strategies]]. Trend regimes favour [[oi-confirmed-trend]], [[major-trend-reclaim-rejection]] and [[liquidity-vacuum-momentum]]. Carry ([[funding-rate-harvest]]) is a positioning-regime trade more than a direction trade. The [[multi-strategy-crypto-portfolio]] uses these labels to set sleeve weights.

## Regime Persistence and Transitions

Regimes are **sticky** — volatility clusters, trends persist — which is what makes them useful. But the money is made and lost at the **transitions**, which are abrupt, asymmetric (vol spikes up faster than it falls), and only cleanly visible *after the fact*. Any regime label is a lagging, probabilistic estimate, so the practical discipline is to act on imperfect signals near suspected turns rather than waiting for confirmation that arrives too late.

## Common Pitfalls

- **Overfitting the regime map.** With enough free parameters you can carve history into regimes that "explain" every drawdown and forecast none. Keep the number of states small and economically motivated.
- **Lookahead bias.** Labelling regimes with data that would not have been available in real time inflates backtests catastrophically. Regime signals must be strictly causal.
- **Treating regimes as periodic.** Like [[market-cycles]], regimes have no fixed clock; assuming a regime "is due" to flip is the classic error.
- **Single-axis tunnel vision.** A market can be a "bull" on price while breadth and correlation quietly signal a regime change underneath.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/regimes/current` — current long-horizon market regime (10-state taxonomy)
- `GET /api/v1/quant/market` — HMM regime probabilities, 4h/24h horizons (15-min refresh)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/liquidity/regime/score` — liquidity fragility composite (0-100)

**Historical data:**
- `GET /api/v1/quant/timeline` — daily market regime labels, 2019-now
- `GET /api/v1/quant/regimes/history` — full 6-regime Parquet download (2020-yesterday)
- `GET /api/v1/quant/history` — point-in-time probability records for backtests
- `GET /api/v1/regimes/history?from=2024-01-01` — committed long-horizon regime transitions, with the exact commit instant and run length (Pro Plus). Use the commit time, not the first sample that observed the change, so labels stay causal.

**Other regime axes:** `GET /api/v1/regimes` (current label plus the full taxonomy), `GET /api/v1/event/regime/score`, `GET /api/v1/policy/regime/score`, `GET /api/v1/meme/regime/score`, `GET /api/v1/security/regime/score`, and `GET /api/v1/sentiment/fear-greed` for the sentiment axis.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/regimes/current"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Related

- [[market-cycles]] — the four-phase discretionary counterpart
- [[regime-detection]] / [[market-regime-detection-ml]] — quantitative labelling
- [[volatility-regime]] / [[correlation-regime]] — single-axis regime views
- [[regime-matrix]] / [[regime-strategy-playbook]] — mapping regimes to strategies
- [[risk-on-risk-off-framework]] — the risk-appetite axis
- [[business-cycle]] — the macro backdrop regimes ride on
- [[asset-allocation]] / [[sector-rotation]] — how allocations shift across regimes

## Sources

- Hidden-Markov and regime-switching methods in finance follow Hamilton (1989), "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle," *Econometrica*.
- Ang & Bekaert (2002), "International Asset Allocation with Regime Shifts," *Review of Financial Studies* — regime-dependent correlations and allocation.
