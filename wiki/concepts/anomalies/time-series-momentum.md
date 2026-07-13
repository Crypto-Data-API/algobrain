---
title: "Time-Series Momentum"
type: concept
created: 2026-04-10
updated: 2026-04-10
status: good
tags: [anomalies, momentum, time-series, trend-following]
aliases: ["TSMOM", "Trend Anomaly", "Moskowitz-Ooi-Pedersen"]
domain: [anomalies]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[momentum-anomaly]]", "[[trend-following-cta]]", "[[edge-taxonomy]]"]
---

# Time-Series Momentum

The empirical regularity that an asset's *own* past returns predict its *own* future returns over horizons of 1-12 months. Distinct from cross-sectional momentum (which compares assets to each other) and complementary to it. The academic formalization of trend-following CTA strategies that have been run profitably since the 1970s. Documented across asset classes by Moskowitz, Ooi, and Pedersen (2012).

## The Original Finding

**Source:** Moskowitz, Ooi, Pedersen (2012) "Time Series Momentum" — *Journal of Financial Economics*

The setup:
1. For each asset (across futures markets covering equities, bonds, currencies, commodities), compute the return over the past 12 months
2. If positive, go long for the next month; if negative, go short for the next month
3. Size positions to target a constant volatility (e.g., 10% annualized per asset)
4. Equal-weight across all assets

The result: from 1985-2009 across 58 liquid futures contracts, this strategy earned approximately **15% per year with Sharpe of 1.2** — substantially higher than any single asset's standalone Sharpe and much higher than cross-sectional momentum on the same universe.

The strategy is profitable across nearly every sub-sample, regime, and asset class tested.

## What It Says

Past returns predict future returns *for the same asset*. This is a stronger statement than cross-sectional momentum — it doesn't require the asset to outperform its peers, just to continue trending in its own direction.

Time-series momentum is the academic formalization of *trend following*. CTAs and managed futures funds have been running this strategy professionally since the 1970s (see [[turtle-trading]], [[trend-following-cta]]). The Moskowitz-Ooi-Pedersen paper just put it into the academic literature with a clean methodology.

## The Mechanism

The dominant theory: **investor underreaction followed by overreaction**.

1. **Underreaction phase (1-12 months):** when an asset trends, investors gradually update their expectations. The trend continues as more capital flows in.
2. **Overreaction phase (multi-year):** eventually the asset becomes overvalued (or undervalued) relative to fundamentals, and a long-term reversal begins.

This produces the characteristic *return horizon structure*:
- 1-month return: weakly positive (microstructure)
- 1-month to 12-month return: strongly positive (momentum)
- 12-month to 60-month return: negative (long-term reversal — see [[overreaction-anomaly]])

In the [[edge-taxonomy]], time-series momentum is **behavioral** — driven by investor underreaction to information. It also has a small **structural** component from forced flows (trend followers buying once a trend is established creates a feedback loop).

## Replication Status

Time-series momentum has been replicated extensively:
- **Across asset classes** — equities, bonds, FX, commodities
- **Across time periods** — back-tested to 1903 by Hurst, Ooi, Pedersen (2017); positive in nearly every decade
- **Across countries** — works in essentially every developed market
- **Across implementations** — works with different lookback lengths (1, 3, 6, 9, 12 months)

The Hurst-Ooi-Pedersen paper "A Century of Evidence on Trend-Following Investing" extended the test to 110+ years across 67 markets, finding consistent positive Sharpe in nearly every decade.

## Decay History

Time-series momentum has had a difficult post-publication decade. From roughly 2009-2018, the strategy underperformed substantially — many trend-following CTAs posted negative Sharpe over multi-year periods.

Possible causes:
- **Quantitative easing** — central bank intervention suppressed the natural development of trends, particularly in fixed income
- **Crowding** — managed futures AUM grew dramatically in 2010-2014
- **Reduced volatility** — many markets entered low-vol regimes that prevented sustained moves

From 2018-2020 the strategy began recovering, and 2022 was an exceptional year for trend-following due to bond and commodity moves. The decade-long drawdown was the longest in the strategy's history but did not break it.

## The Crisis Alpha Property

A defining feature of time-series momentum: it tends to perform *well* during equity market crises. The mechanism:

1. A crisis begins; equities sell off
2. After 1-3 months, the trend signal turns short on equities
3. The strategy is now short equities (and possibly long bonds/gold) for the duration of the crisis
4. Returns are large because the crisis is also a sustained directional move

This is not perfect — some crises are too fast for the lookback to react, and some crises don't develop into trends. But on average, time-series momentum has been *positively* correlated with crisis returns. This is sometimes called "crisis alpha" and is the main reason institutional investors hold trend-following allocations.

The 2008 financial crisis was a textbook example: most trend-following CTAs had double-digit positive returns in 2008, while the S&P fell 37%. The strategy provided meaningful diversification when the rest of the portfolio needed it most.

## Variations

### Single-Lookback
Use only one lookback period (e.g., 12 months). Simpler, slightly worse Sharpe.

### Multi-Lookback
Average signals from multiple lookback periods (e.g., 1, 3, 6, 12 months). More robust, smoother equity curve. Used by most professional CTAs.

### Volatility Targeting
Size positions to target a constant volatility per asset rather than equal-dollar. Critical for combining across asset classes with very different volatilities.

### Slow vs. Fast Trend
Slow trend (12-month lookback) captures longer trends with less turnover. Fast trend (1-3 months) captures shorter moves with more turnover and larger drawdowns. Combining is more robust than either.

### Cross-Sectional vs. Time-Series
The two are complementary. A combined cross-sectional + time-series momentum strategy has higher Sharpe than either alone, because they respond to different market regimes.

### Pure Trend vs. Carry-Plus-Trend
Trend signals can be combined with carry signals (yield, term-structure) for a more robust strategy. Used by AHL, Winton, AQR, and many other systematic CTAs.

## Current Viability

Time-series momentum is one of the most viable cross-asset anomalies as of 2024-2026. It is:
- Replicated across decades and markets
- Mechanically simple
- Provides crisis alpha (rare and valuable)
- Capacity-rich (can absorb tens of billions per strategy)

The Sharpe is no longer 1.2, but 0.5-0.7 is realistic for a clean implementation. Trend following is one of the few strategies that institutional investors should hold *specifically* for diversification reasons even if they expect a moderate Sharpe.

The right implementation: multi-lookback, multi-asset, vol-targeted, with explicit position limits per asset and per asset class. Combine with carry signals for additional Sharpe.

## Strategies That Implement It

- [[trend-following-cta]] — full CTA implementation
- [[turtle-trading]] — historical trend-following methodology
- [[moving-average-crossover]] — simplest trend signal
- [[donchian-channel-breakout]] — breakout-based trend signal
- [[supertrend]] — modern trend indicator

## Sources

- Moskowitz, Ooi, Pedersen (2012) "Time Series Momentum" — *Journal of Financial Economics*
- Hurst, Ooi, Pedersen (2017) "A Century of Evidence on Trend-Following Investing" — *Journal of Portfolio Management*
- Asness, Moskowitz, Pedersen (2013) "Value and Momentum Everywhere" — *Journal of Finance*
- [[book-trend-following]] — Covel
- [[book-following-the-trend]] — Clenow

## Related

- [[anomalies-overview]]
- [[momentum-anomaly]]
- [[trend-following-cta]]
- [[turtle-trading]]
- [[regime-matrix]]
- [[edge-taxonomy]]
