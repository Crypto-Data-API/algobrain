---
title: "Market Regime"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [market-regime, regime-detection, quantitative, risk-management]
aliases: ["Market Regime", "Market Regimes", "Trading Regime", "Regime"]
domain: [portfolio-theory, market-regime]
prerequisites: ["[[volatility]]", "[[correlation]]", "[[market-cycles]]"]
difficulty: intermediate
related: ["[[market-cycles]]", "[[regime-detection]]", "[[market-regime-detection-ml]]", "[[volatility-regime]]", "[[correlation-regime]]", "[[regime-matrix]]", "[[regime-strategy-playbook]]", "[[business-cycle]]", "[[risk-on-risk-off-framework]]", "[[sector-rotation]]", "[[mean-reversion]]", "[[trend-following]]", "[[asset-allocation]]", "[[vix]]"]
---

A **market regime** is a persistent statistical "state" of a market — a stretch of time during which the behaviour of returns (their trend, volatility, correlation, and risk appetite) is broadly consistent, before shifting to a qualitatively different state. Regimes are the reason a strategy that prints money for two years can quietly stop working: its edge was conditional on a regime that ended. Identifying which regime you are in, and sizing for the possibility that it changes, is one of the central problems of [[quantitative-equity|quantitative]] and discretionary trading alike.

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

## Regime Persistence and Transitions

Regimes are **sticky** — volatility clusters, trends persist — which is what makes them useful. But the money is made and lost at the **transitions**, which are abrupt, asymmetric (vol spikes up faster than it falls), and only cleanly visible *after the fact*. Any regime label is a lagging, probabilistic estimate, so the practical discipline is to act on imperfect signals near suspected turns rather than waiting for confirmation that arrives too late.

## Common Pitfalls

- **Overfitting the regime map.** With enough free parameters you can carve history into regimes that "explain" every drawdown and forecast none. Keep the number of states small and economically motivated.
- **Lookahead bias.** Labelling regimes with data that would not have been available in real time inflates backtests catastrophically. Regime signals must be strictly causal.
- **Treating regimes as periodic.** Like [[market-cycles]], regimes have no fixed clock; assuming a regime "is due" to flip is the classic error.
- **Single-axis tunnel vision.** A market can be a "bull" on price while breadth and correlation quietly signal a regime change underneath.

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
