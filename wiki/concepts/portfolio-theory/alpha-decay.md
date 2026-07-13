---
title: "Alpha Decay"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, quantitative, algorithmic, backtesting]
aliases: ["Alpha Decay", "Edge Decay", "Signal Decay", "Factor Crowding"]
related: ["[[alpha]]", "[[alpha-model]]", "[[edge-taxonomy]]", "[[overfitting-detection]]", "[[when-to-retire-a-strategy]]", "[[multi-factor-portfolio]]", "[[market-microstructure]]", "[[crowding-risk]]", "[[crowding]]", "[[efficient-market-hypothesis]]", "[[sharpe-ratio]]"]
domain: [portfolio-theory]
prerequisites: ["[[alpha]]"]
difficulty: intermediate
---

**Alpha decay** is the erosion of a trading strategy's [[alpha|excess return]] over time as the edge it exploits is competed away. Almost every genuine edge is finite: once a profitable pattern is discovered, published, or crowded into by enough capital, the very act of exploiting it pushes prices toward fair value and removes the inefficiency. Alpha decay is therefore the dynamic, real-world mechanism behind the [[efficient-market-hypothesis]] — markets are not born efficient, they are *made* efficient by arbitrageurs eroding each edge they find. Distinguishing structural decay from a normal drawdown is one of the hardest and most consequential problems in active management.

## Two Distinct Phenomena

The term covers two related but different things:

1. **Intra-trade alpha decay (signal half-life).** A single forecast has a horizon over which its predictive power persists. A short-term reversal signal might decay over hours; a value signal over years. The **half-life** of a signal — how long until half its predictive content is gone — determines holding period and turnover, and trades against transaction cost: a fast-decaying signal needs cheap, fast execution to capture before it dies.

2. **Strategy/factor alpha decay (edge erosion).** A whole strategy's profitability declines over months and years as competitors arbitrage it. This is the existential threat to a live book.

## Signal Half-Life and the Cost Trade-off

The cleanest quantitative handle on intra-trade decay is the **half-life** — the holding period over which a signal loses half its predictive power, usually estimated from the decay of the [[information-coefficient]] (the rank correlation between forecast and subsequent return) as the horizon lengthens. Half-life dictates turnover, and turnover dictates how much cost the signal must clear to stay profitable.

| Signal family | Typical half-life | Turnover | Cost sensitivity |
|---------------|-------------------|----------|------------------|
| Order-flow / microstructure | seconds–minutes | extreme | only viable with rebates / co-location |
| Short-term reversal | hours–days | very high | needs cheap, fast execution |
| Cross-sectional momentum | weeks–months | moderate | tolerant of normal costs |
| Value / quality | quarters–years | low | very tolerant of costs |

The faster a signal decays, the more of its gross alpha is consumed by [[slippage]] and fees. A signal with a one-day half-life and a 5 bps edge is worthless if round-trip costs are 8 bps; the same gross edge at a one-year half-life is highly profitable. This is why decay analysis and transaction-cost analysis must be done together.

## Why Edges Decay

- **Publication.** McLean and Pontiff (2016) documented that the average academically-published anomaly's return falls by ~58% *after* publication — direct evidence of arbitrageurs trading away the edge once it is known.
- **Crowding.** When many funds run the same signal, positioning becomes a one-sided trade. Forced deleveraging then produces sharp, correlated drawdowns — the August 2007 "quant quake," when crowded equity market-neutral books unwound simultaneously, is the canonical example of [[crowding-risk]] (see also [[crowding]]).
- **Regime change.** The behavioral or structural cause of an edge ([[edge-taxonomy]] mechanism) can simply disappear — a rule change, a new market participant, a shift in microstructure (decimalization, the rise of [[market-microstructure|HFT market-making]]).
- **Capacity exhaustion.** As AUM grows, market impact eats the edge; the strategy hits its capacity limit and net alpha goes to zero even though gross alpha persists.

## The McLean–Pontiff Result, Quantified

The single most cited evidence for strategy-level decay comes from McLean and Pontiff (2016), who replicated 97 published anomalies and tracked their returns across three periods:

| Period | Anomaly return (relative to in-sample) | Interpretation |
|--------|----------------------------------------|----------------|
| Original in-sample (paper's own window) | 100% (baseline) | The published, possibly overfit, figure |
| Out-of-sample, *before* publication | ~74% (≈26% lower) | Genuine but partly statistical-bias inflated |
| Post-publication | ~42% (≈58% lower than in-sample) | Arbitrageurs trading away the known edge |

The ~26% in-sample-to-out-of-sample drop is mostly statistical (data-mining / [[overfitting-detection|overfitting]]); the *additional* drop after publication is the genuine decay caused by capital crowding in. Crucially, the strongest post-publication decay appeared in anomalies that were cheapest to arbitrage (high-liquidity, low-cost stocks) — exactly what an arbitrage-driven story predicts.

## Worked Example: Spotting Decay vs Noise

Suppose a strategy backtested at a [[sharpe-ratio|Sharpe]] of 1.2. After 12 months live it is running at a realized Sharpe of 0.3. Is that decay or bad luck? With a true Sharpe of 1.2, the standard error of a one-year Sharpe estimate is roughly `sqrt((1 + 0.5·1.2²)/252) ≈ 0.08` on a *daily* basis, but on an *annual* sample the estimate is far noisier — a single year's Sharpe can easily land a full point below the truth by chance. A 0.9 gap over one year is suggestive but not yet statistically decisive; the same gap sustained over 2–3 rolling years, or a realized [[information-coefficient]] below half the backtest IC, is the threshold most desks treat as real decay and a trigger for [[when-to-retire-a-strategy|kill criteria]].

## Trading and Portfolio Relevance

- **Monitoring.** The primary defense is comparing *realized* Information Coefficient / Sharpe to the backtested expectation on a rolling basis. A sustained, statistically-meaningful gap is the early-warning signal of decay, not noise.
- **Kill criteria.** Decay monitoring feeds directly into [[when-to-retire-a-strategy|retirement rules]] — pre-committed numerical conditions (e.g. rolling 12-month Sharpe < 0, or realized IC below half the backtest IC) for cutting a strategy before it bleeds.
- **Diversification of edges.** Because any single edge decays, durable returns come from a *portfolio* of weakly-correlated edges, continuously researched and replaced — the [[alpha-model]] pipeline is a treadmill, not a finished product.
- **Beware backtest overfit.** Apparent decay is sometimes evidence the edge was never real — a backtest artifact that "works" in-sample and immediately fails live. See [[overfitting-detection]]: a strategy that decays the instant it goes live was probably overfit, not crowded out.

## How Traders Manage Alpha Decay

- **Treat research as a treadmill.** Budget continuous research capacity to replace decaying signals; a desk that stops researching is on a glide path to zero alpha.
- **Diversify across decay rates.** Hold a mix of fast (high-Sharpe, low-capacity) and slow (lower-Sharpe, high-capacity) signals so the book is not synchronized to one decay clock.
- **Stagger and obscure.** Some desks split execution, randomize timing, and avoid publishing or discussing live signals to slow the crowding that accelerates decay.
- **Pre-commit kill criteria.** Define numerical retirement rules *before* deployment (rolling Sharpe floor, IC floor, max drawdown) so the decision to cut is not made emotionally mid-drawdown — see [[when-to-retire-a-strategy]].
- **Distinguish decay from regime.** A signal can be temporarily dormant (wrong regime) rather than dead. Conditioning monitoring on regime ([[market-regime]]) avoids retiring a sound edge during an unfavorable but transient environment.

## Common Pitfalls

- **Confusing a drawdown with decay** — cutting a sound strategy at the bottom of a normal losing streak.
- **Confusing decay with overfit** — concluding "the edge was crowded out" when it never existed; only out-of-sample-validated strategies can truly *decay*.
- **No baseline expectation** — without a backtested Sharpe/IC and its sampling error, there is nothing to compare realized performance against, so decay is undetectable.
- **Ignoring net-of-cost capacity** — gross alpha can look healthy while net alpha has already decayed to zero through market impact at the fund's current AUM.

## Related

- [[alpha]] — what decays
- [[alpha-model]] — the engine whose signals decay
- [[edge-taxonomy]] — the edge mechanisms that erode
- [[crowding-risk]] — the main accelerant of factor decay
- [[overfitting-detection]] — distinguishing decay from a never-real edge
- [[when-to-retire-a-strategy]] — acting on decay with kill criteria

## Sources

- McLean, R. David, and Jeffrey Pontiff. "Does Academic Research Destroy Stock Return Predictability?" *Journal of Finance* (2016).
- Khandani, Amir, and Andrew Lo. "What Happened to the Quants in August 2007?" *Journal of Investment Management* (2007).
- Harvey, Campbell, Yan Liu, Heqing Zhu. "...and the Cross-Section of Expected Returns." *Review of Financial Studies* (2016) — multiple-testing and the fragility of published factors.
