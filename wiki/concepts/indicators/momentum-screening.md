---
title: "Momentum Screening"
type: concept
created: 2026-04-10
updated: 2026-06-22
status: excellent
tags: [momentum, technical-analysis, quantitative]
aliases: ["momentum screening", "momentum screen", "momentum stock screen", "Momentum Screening"]
domain: [indicators]
prerequisites: ["[[momentum]]", "[[relative-strength]]"]
difficulty: intermediate
related: ["[[relative-strength]]", "[[sector-rotation]]", "[[momentum-investing]]", "[[momentum]]", "[[momentum-anomaly]]"]
---

Momentum screening is the systematic process of filtering a large universe of stocks to identify those exhibiting the strongest price [[momentum]] and supporting fundamental catalysts. Unlike discretionary [[momentum-investing|momentum trading]] — simply buying what has gone up — a structured momentum screen applies multiple quantitative criteria simultaneously to rank and select candidates with the highest probability of continued outperformance.

## Core Screening Criteria

A robust momentum screen typically combines five dimensions:

1. **Price momentum (6-month and 12-month returns)** — The foundational signal. Stocks in the top decile of trailing returns have historically outperformed the bottom decile by 8-12% annually. The 12-month lookback captures intermediate trend persistence, while the 6-month lookback is more responsive to recent acceleration.

2. **[[relative-strength]] vs. market and sector** — Raw returns can be misleading in a strong bull market (everything goes up). Measuring a stock's return relative to the S&P 500 or its GICS sector isolates genuine outperformance from market beta. The relative-strength-rating developed by ibd formalized this into a 1-99 ranking system.

3. **earnings-revision momentum** — Analyst estimate upgrades serve as a fundamental confirmation of price momentum. A stock rising on deteriorating fundamentals is vulnerable to reversal; one rising alongside upward earnings revisions has a fundamental catalyst supporting the move.

4. **Volume confirmation** — Strong momentum on expanding [[volume]] indicates institutional participation. Rising prices on declining volume suggest exhaustion. A 50-day average volume trend filter helps distinguish conviction-driven moves from low-liquidity noise.

5. **Trend confirmation** — Price trading above the [[200-day-ma]] confirms the stock is in a long-term uptrend. This binary filter eliminates stocks in structural downtrends, even if they have strong short-term returns from a dead-cat bounce.

### Criteria at a Glance

| Dimension | Typical signal | Common threshold | What it screens out |
|-----------|----------------|------------------|---------------------|
| Price momentum | 6- and 12-month trailing return | Top decile/quintile of universe | Laggards and chop |
| [[relative-strength]] | Return vs. S&P 500 / sector | RS Rating ≥ 80 | Stocks rising only on market beta |
| earnings-revision | Net analyst estimate upgrades | Positive 1- and 3-month revisions | Price moves with no fundamental catalyst |
| Volume confirmation | 50-day volume trend | Volume rising into the advance | Low-conviction, low-liquidity drifts |
| Trend filter | Price vs. [[200-day-ma]] | Price > 200-day MA | Structural downtrends / dead-cat bounces |

## Composite Scoring and Ranking

Most systematic implementations assign weights to each criterion and compute a composite momentum score. A typical weighting might allocate 30% to price momentum, 25% to earnings revisions, 25% to relative strength, 10% to volume trend, and 10% to the 200-day MA filter. Stocks are ranked by composite score, and the top 10-20% become the investable universe.

### Worked Example: Scoring Three Candidates

*Illustrative, rounded numbers.* Each metric is first converted to a 0-100 percentile rank within the universe, then combined with the weights above (price 30%, earnings revisions 25%, RS 25%, volume 10%, trend 10%):

| Stock | Price mom. (30%) | Earn. rev. (25%) | RS (25%) | Volume (10%) | Trend (10%) | Composite |
|-------|------------------|------------------|----------|--------------|-------------|-----------|
| **AAA** | 95 | 90 | 92 | 80 | 100 | **92.0** |
| **BBB** | 88 | 40 | 85 | 70 | 100 | **74.7** |
| **CCC** | 91 | 88 | 30 | 60 | 0 | **62.2** |

AAA is the clean leader — strong price momentum *confirmed* by earnings upgrades, RS leadership, volume, and an intact long-term trend. BBB has good price action but weak earnings revisions, flagging a move that lacks a fundamental catalyst. CCC looks momentum-y on raw price (91) but its RS rank is poor (it is only rising with the market) and it sits *below* its 200-day MA — the composite correctly demotes it. This is the whole point of multi-factor screening: any single metric can mislead, but the composite separates durable leadership from beta-driven or catalyst-less noise.

## The Skip-Month Effect

Jegadeesh and Titman (1993) documented that momentum strategies perform better when the most recent month of returns is excluded from the lookback period. This "skip month" adjustment removes the short-term reversal effect (stocks that surged in the last 2-4 weeks tend to mean-revert in the following week). Practically, a 12-month momentum screen should measure returns from month t-12 to month t-1, skipping the most recent month entirely.

## Common Screening Tools

- **ibd MarketSmith** — Proprietary relative-strength-rating, EPS Rating, and Composite Rating combine momentum and fundamental factors in a single interface
- **Finviz** — Free screener supporting performance, analyst recommendation, and technical filters
- **Portfolio123** — Quantitative platform allowing custom multi-factor ranking systems with backtesting
- **Koyfin / Seeking Alpha** — Earnings revision data and relative performance charting

## How Traders Use This

- **Two-layer top-down workflow.** Many practitioners first rank sectors by [[relative-strength]] ([[sector-rotation]]), then run the momentum screen only within the leading sectors. This concentrates capital in groups with institutional sponsorship and avoids "strong stock in a weak group" traps.
- **Watchlist generation, not blind buying.** The screen produces a ranked candidate list; entries are then timed with [[chart-patterns]], pullbacks to moving averages, or [[breakout]] setups rather than buying the open the morning a name appears.
- **Rebalance cadence vs. cost.** Monthly rebalancing is the academic standard, but tighter cadences raise turnover and [[slippage|cost drag]]. Some run a buffered ranking (e.g., buy top 10%, only sell when a holding falls out of the top 30%) to cut churn while preserving the factor exposure.
- **Combine with the skip month.** Apply the t-12 to t-1 lookback (below) so the screen does not chase names that just spiked and are due for a short-term reversal.

## Common Pitfalls and Risks

- **Momentum crashes.** The dominant tail risk: after a sharp market bottom, prior losers rip and prior winners stall, so a momentum book can suffer violent drawdowns (e.g., March 2009, March 2020). Volatility-scaling or a trend/[[200-day-ma]] overlay mitigates but does not eliminate this.
- **Chasing extended names.** Raw price momentum buys what has already run; without the skip month and earnings-revision confirmation, screens load up on stocks near exhaustion.
- **Bull-market mirage.** In broad rallies "everything is up," so raw return screens fill with high-beta junk. [[relative-strength]] vs. benchmark and sector is what separates genuine leadership from beta.
- **Crowding and factor decay.** Momentum is a well-known, heavily-traded factor; crowded positioning can sharpen reversals and compress forward returns.
- **Liquidity and cost drag.** High turnover plus illiquid small caps can quietly erase the paper edge. Constraining the universe (e.g., minimum $500M market cap, minimum 500K average daily volume) and modeling realistic [[transaction-costs]] is essential.
- **Survivorship and look-ahead bias in backtests.** Earnings-revision and fundamental data must be point-in-time; using restated or as-reported figures inflates historical results.

## Related

- [[relative-strength]] — Core screening dimension; isolates leadership from beta
- [[momentum]] / [[momentum-anomaly]] — The underlying effect screens exploit
- [[sector-rotation]] — Often combined with momentum screening in a two-layer approach

## Sources

- Jegadeesh, N. and Titman, S. (1993). "Returns to Buying Winners and Selling Losers." *Journal of Finance* 48 (1) — origin of the skip-month and 6-12 month lookback findings.
- William O'Neil, *How to Make Money in Stocks* (McGraw-Hill, 2009) — the CAN SLIM and Relative Strength Rating screening methodology.
- Wesley Gray and Jack Vogel, *Quantitative Momentum* (Wiley, 2016) — systematic momentum screen construction and composite ranking.
- Gary Antonacci, *Dual Momentum Investing* (McGraw-Hill, 2014) — absolute + relative momentum screening framework.
