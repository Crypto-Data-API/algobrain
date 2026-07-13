---
title: "MAX Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, behavioral-finance, volatility]
aliases: ["Bali-Cakici-Whitelaw MAX", "Maximum Daily Return Anomaly", "Extreme Return Anomaly", "MAX Anomaly"]
domain: [anomalies]
prerequisites: ["[[lottery-stock-anomaly]]", "[[idiosyncratic-volatility-anomaly]]"]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[lottery-stock-anomaly]]", "[[idiosyncratic-volatility-anomaly]]", "[[low-volatility-anomaly]]"]
---

# MAX Anomaly

Stocks with the highest single-day returns in the prior month subsequently underperform stocks with low maximum daily returns, by a large and statistically significant margin. The MAX anomaly is the cleanest operationalization of the behavioral "lottery preference" hypothesis: investors are willing to pay a premium for stocks that *could* deliver a huge one-day jackpot, and this overpricing shows up as negative subsequent alpha.

## What

For each stock in each month, compute MAX(n) = the average of the n largest single-day returns in the prior month (typically n = 1 or n = 5). Rank stocks monthly. Long the lowest-MAX decile, short the highest-MAX decile. In Bali, Cakici, Whitelaw (2011), the hedge portfolio earned roughly -1% per month on the high-MAX leg and +0.3% on the low-MAX leg, for a ~1.2% monthly spread (~15% annualized) gross of costs.

## Original Paper

Bali, T., Cakici, N., Whitelaw, R. (2011) "Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns" — *Journal of Financial Economics*.

## Mechanism

- **Lottery preferences** (Barberis & Huang 2008 "Stocks as Lotteries") — investors with cumulative prospect theory preferences overweight small probabilities of large gains, which causes them to overpay for stocks with lottery-like return distributions
- **Skewness preference** — mean-variance investors only care about the first two moments, but real investors also care about positive skewness; stocks with high MAX have high recent positive skewness and are bid up
- **Retail dominance** — the MAX effect is concentrated in retail-heavy stocks, consistent with retail investors being the primary lottery-demand clientele
- **Closely related to [[idiosyncratic-volatility-anomaly]] and [[lottery-stock-anomaly]]** — all three capture roughly the same underlying demand for lottery payoffs

## Edge Category

**Behavioral** (lottery preferences / prospect theory) + **structural** (limits to arbitrage on the short side, since these are often hard-to-borrow names).

## Replication Status

Strongly replicated across markets and lookback windows. One of the cleanest findings in behavioral asset pricing. Survives controls for idiosyncratic volatility, skewness, size, value, and momentum.

## Decay History

Mild decay. The MAX signal remains effective, especially when combined with other quality/IVOL filters. Hedge funds implementing "anti-lottery" short books continue to generate alpha, though the short side is expensive to borrow.

## Current Viability

Tradeable as:

- **A short-book screen** — avoid high-MAX names in long-only equity portfolios; you get a free Sharpe boost
- **A long-only low-MAX tilt** — overweight low-MAX stocks within a large-cap universe
- **A long-short factor** in sophisticated quant portfolios, subject to borrow constraints

## Related Strategies

- [[lottery-stock-anomaly]] — closely related measurement (lottery index)
- [[idiosyncratic-volatility-anomaly]] — MAX and IVOL overlap substantially
- [[low-volatility-anomaly]] — similar underweighting of volatile/speculative names

## Sources

- Bali, Cakici, Whitelaw (2011) "Maxing Out" — original
- Barberis & Huang (2008) "Stocks as Lotteries" — theoretical foundation
- Annaert, De Ceuster, Verstegen (2013) — international replication
- Kumar (2009) "Who Gambles in the Stock Market?" — retail investor evidence

## Related

- [[anomalies-overview]]
- [[lottery-stock-anomaly]]
- [[idiosyncratic-volatility-anomaly]]
- [[low-volatility-anomaly]]
