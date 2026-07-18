---
title: "Idiosyncratic Volatility Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, volatility]
aliases: ["IVOL Anomaly", "Ang-Hodrick-Xing-Zhang Puzzle", "Idiosyncratic Risk Puzzle", "Idiosyncratic Volatility Anomaly"]
domain: [anomalies]
prerequisites: ["[[volatility]]", "[[low-volatility-anomaly]]"]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[low-volatility-anomaly]]", "[[lottery-stock-anomaly]]", "[[max-anomaly]]"]
---

# Idiosyncratic Volatility Anomaly

Stocks with high idiosyncratic volatility (residual variance after controlling for market, size, and value factors) earn *lower* subsequent returns than stocks with low idiosyncratic volatility. This is one of the most disturbing anomalies for rational-pricing theorists: classical finance says idiosyncratic risk should not be priced at all — it can be diversified away — yet it appears to be priced *negatively*.

## What

Estimate each stock's idiosyncratic volatility as the standard deviation of the residuals from a Fama-French three-factor (or four-factor) regression, over a recent rolling window (typically 1-3 months of daily data). Sort stocks into quintiles on IVOL. The quintile with the highest IVOL underperforms the quintile with the lowest IVOL by roughly 1% per month (~12% annualized) in Ang-Hodrick-Xing-Zhang's original sample.

## Original Paper

Ang, Hodrick, Xing, Zhang (2006) "The Cross-Section of Volatility and Expected Returns" — *Journal of Finance*. Follow-up (2009) confirmed internationally.

## Mechanism

Competing explanations:

- **Lottery preference / gambling demand:** high-IVOL stocks are often low-priced, story-driven names with lottery-like return distributions. Investors with preferences for skewness (see [[lottery-stock-anomaly]] and [[max-anomaly]]) overpay for them, depressing expected returns.
- **Limits to arbitrage:** these stocks are hard to short, so the overpricing can't be arbitraged away
- **Short-sale constraints + divergence of opinion** (Miller 1977) — when optimists set the price and pessimists can't short, high-dispersion names are overpriced
- **Retail ownership bias:** retail investors overweight attention-grabbing, volatile stocks (Barber & Odean)

The effect is largely concentrated in small, hard-to-short, high-retail-ownership stocks, which is consistent with the limits-to-arbitrage story.

## Edge Category

**Behavioral** (lottery preferences) + **structural** (short-sale constraints).

## Replication Status

Replicated internationally and over multiple time samples. Survives Hou-Xue-Zhang (2020) replication, though with smaller magnitude than Ang et al.'s original sample. Some researchers (Bali, Cakici 2008; Fu 2009) argue the effect weakens or reverses with different IVOL estimation methods, so there is ongoing debate about measurement.

## Decay History

Some decay, but the effect persists in small caps and hard-to-short names. The long-short portfolio in large caps is less reliable post-publication.

## Current Viability

Primarily useful as a *screen* — avoiding high-IVOL stocks improves the Sharpe of most long-only strategies. Direct long-short implementation is hampered by borrow constraints on the short side.

## Related Strategies

- [[low-volatility-anomaly]] — uses total rather than idiosyncratic volatility; overlapping mechanism
- [[lottery-stock-anomaly]] — similar underlying demand for lottery payoffs
- [[max-anomaly]] — measures the same phenomenon via a different statistic
- Long-only low-vol ETFs (USMV, SPLV) implicitly capture this

## Sources

- Ang, Hodrick, Xing, Zhang (2006, 2009) — original papers
- Bali, Cakici (2008) and Fu (2009) — measurement critiques
- Stambaugh, Yu, Yuan (2015) "Arbitrage Asymmetry and the Idiosyncratic Volatility Puzzle"
- Hou, Xue, Zhang (2020) "Replicating Anomalies"

## Related

- [[anomalies-overview]]
- [[low-volatility-anomaly]]
- [[lottery-stock-anomaly]]
- [[max-anomaly]]
