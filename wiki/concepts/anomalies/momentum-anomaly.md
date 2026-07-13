---
title: "Momentum Anomaly"
type: concept
created: 2026-04-10
updated: 2026-04-10
status: good
tags: [anomalies, momentum, factor-investing, behavioral-finance]
aliases: ["Cross-Sectional Momentum", "Jegadeesh-Titman", "Momentum Factor"]
domain: [anomalies, factor-investing]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[momentum]]", "[[momentum-rotation]]", "[[time-series-momentum]]", "[[edge-taxonomy]]"]
---

# Momentum Anomaly

The empirical regularity that stocks (and other assets) which have outperformed over the past 3-12 months tend to continue outperforming over the following 3-12 months. Documented across equities, currencies, bonds, commodities, and crypto. One of the oldest and most replicated anomalies in finance, and also one of the most decayed since publication.

## The Original Finding

**Source:** Jegadeesh & Titman (1993) "Returns to Buying Winners and Selling Losers" — *Journal of Finance*

The setup:
1. At the end of each month, rank all US stocks by their return over the previous J months (J ∈ {3, 6, 9, 12})
2. Form a portfolio: long the top decile, short the bottom decile (the "winner-minus-loser" portfolio)
3. Hold for K months (K ∈ {3, 6, 9, 12}), then rebalance

The result: this portfolio earned approximately **1% per month** above the risk-free rate from 1965 to 1989, with the strongest result for J = 6 and K = 6. Sharpe of about 1.0 — extraordinary for a long-short equity strategy.

## What It Says

Past returns predict future returns at intermediate horizons (3-12 months). This is the *opposite* of the [[overreaction-anomaly|long-term reversal]] effect (DeBondt-Thaler), which says that 3-5 year past returns *negatively* predict 3-5 year future returns. The two are reconciled by saying:

- **0-1 month:** mean reversion (microstructure noise)
- **3-12 months:** momentum (underreaction)
- **3-5 years:** reversal (overreaction)

The pattern is consistent across asset classes and remarkably stable across the J=3-12 horizon range.

## The Mechanism

Several theories, all behavioral:

### 1. Underreaction to News
Investors anchor on past prices and underreact to new information. When good news arrives, the price moves but doesn't fully adjust; subsequent gradual repricing produces the momentum effect. (Daniel, Hirshleifer, Subrahmanyam 1998; Barberis, Shleifer, Vishny 1998)

### 2. Disposition Effect
Investors are reluctant to sell losers (because realizing a loss is painful) and quick to sell winners (to "lock in" gains). This creates excess supply of winners and excess demand for losers in the short term, which is gradually corrected as the prices catch up to the news. (Grinblatt & Han 2005)

### 3. Slow Information Diffusion
Information reaches different investors at different speeds. As new information slowly diffuses through the market, prices update gradually. (Hong, Lim, Stein 2000)

### 4. Risk Compensation (Disputed)
Some authors argue momentum is compensation for time-varying risk. This is the conventional-finance defense. Most quant researchers are skeptical because the risk story doesn't predict the specific 3-12 month horizon.

In the [[edge-taxonomy]], momentum is a **behavioral edge**. The losers — the people on the other side — are investors anchoring on past prices and underreacting.

## Replication Status

Momentum has been replicated:
- **Across countries** — Rouwenhorst (1998) found it in 12 European markets
- **Across asset classes** — Asness, Moskowitz, Pedersen (2013) "Value and Momentum Everywhere" found it in equities, bonds, commodities, currencies
- **Across time** — out-of-sample post-1993 returns were positive but smaller than in-sample
- **Across trading frequencies** — daily, weekly, monthly

The replication record is among the strongest of any anomaly. It is not in serious doubt as an empirical fact.

## Decay History

The decay is well-documented:
- Pre-publication (1965-1989): ~1% per month
- Post-publication (1993-2010): ~0.5% per month
- 2010-2020: closer to 0.2-0.3% per month
- 2009 momentum crash: -25% in March 2009, the worst single month in the strategy's history
- 2016 momentum crash: -10% in November 2016 around the US election

The strategy has not died — momentum still earns positive returns most years — but its Sharpe has roughly halved since publication. The decay is consistent with the McLean-Pontiff finding that published anomalies typically lose ~26% of their effect after publication.

## The "Momentum Crash" Problem

A defining feature of momentum that the original Jegadeesh-Titman paper underplayed: occasional catastrophic months where the strategy loses 15-30% in a single period. These crashes have a characteristic structure:

1. The market has fallen sharply
2. The "loser" portfolio is dominated by stocks that fell with the market
3. A sudden risk-on rally lifts the most-beaten-down stocks dramatically
4. The losers (which the strategy is short) explode upward; the winners (which it is long) lag
5. The strategy posts a large loss in days or weeks

Famous crashes: 2002, August 2009 (the worst), November 2016. Each wiped out years of accumulated momentum returns.

The mechanism: momentum becomes *negatively correlated with market beta* during these episodes. Risk parity and other factor-aware strategies have to size momentum carefully because of this tail.

## Variations

### Time-Series Momentum
Instead of cross-sectional ranking, look at each asset's *own* past returns and go long if positive, short if negative. (Moskowitz, Ooi, Pedersen 2012). See [[time-series-momentum]]. Closely related to trend-following CTAs.

### Residual Momentum
Run a regression of returns on factors (market, size, value); the residual is the firm-specific component. Sort on residual past returns instead of total past returns. Reduces the momentum-crash exposure because it's neutral to market beta. (Blitz, Huij, Martens 2011)

### Industry Momentum
Compute momentum at the industry level rather than the stock level. Less crowded than stock-level momentum, similar Sharpe.

### Fundamental Momentum / Earnings Momentum
Use the trend in earnings revisions or earnings growth as the momentum signal instead of price momentum. See [[earnings-momentum]].

### 52-Week High
A simple proxy: stocks near their 52-week high tend to continue rising. (George & Hwang 2004). Captures momentum without explicitly computing returns.

## Current Viability

Momentum is *still* one of the strongest anomalies after decades of arbitrage. The realistic Sharpe is now around 0.4-0.6 for a clean cross-sectional implementation in US large caps after costs. It's higher in smaller caps, international markets, and crypto where less institutional capital has crowded in.

The right way to use momentum today is in a *factor combination*: value + momentum, momentum + quality, momentum with a market-beta neutralization, momentum with explicit crash protection. Standalone cross-sectional momentum has too much tail risk to size meaningfully.

## Strategies That Implement It

- [[momentum-rotation]] — generic momentum factor portfolio
- [[sector-momentum-screen]] — momentum at the sector level
- [[earnings-momentum]] — fundamentals-based variant
- [[trend-following-cta]] — time-series momentum across asset classes
- [[time-series-momentum]] — own-asset momentum

## Sources

- Jegadeesh & Titman (1993) "Returns to Buying Winners and Selling Losers" — *Journal of Finance*
- Asness, Moskowitz, Pedersen (2013) "Value and Momentum Everywhere" — *Journal of Finance*
- Daniel & Moskowitz (2016) "Momentum Crashes" — *Journal of Financial Economics*
- McLean & Pontiff (2016) on anomaly decay
- [[book-quantitative-momentum]] — Gray & Vogel
- [[book-expected-returns-antti-ilmanen]] — comprehensive momentum chapter

## Related

- [[anomalies-overview]]
- [[momentum]]
- [[time-series-momentum]]
- [[momentum-rotation]]
- [[trend-following-cta]]
- [[edge-taxonomy]]
