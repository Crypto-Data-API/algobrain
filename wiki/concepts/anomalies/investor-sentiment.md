---
title: "Investor Sentiment Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, behavioral-finance, market-regime]
aliases: ["Baker-Wurgler Sentiment", "Sentiment Index Anomaly", "Investor Sentiment", "Investor Sentiment Anomaly"]
domain: [anomalies, behavioral-finance]
prerequisites: ["[[behavioral-finance]]", "[[anomalies-overview]]"]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[lottery-stock-anomaly]]", "[[ipo-underperformance]]", "[[behavioral-finance]]"]
---

# Investor Sentiment Anomaly

Periods of high investor sentiment — measured by an index built from proxies like IPO volume, closed-end fund discounts, NYSE turnover, the equity share of new issues, and the dividend premium — predict *lower* subsequent returns, especially for hard-to-arbitrage stocks (small, young, volatile, unprofitable, non-dividend-paying). Baker & Wurgler (2006) built the first widely-adopted market-wide sentiment index and showed it has robust cross-sectional return-predictive power.

## What

Baker & Wurgler construct a composite sentiment index from six market-based proxies. When sentiment is high, the subsequent 12-month returns of:

- Small caps
- Young firms
- High-volatility firms
- Unprofitable firms
- Non-dividend-payers
- Extreme-growth or extreme-distress firms

are systematically *lower* than the subsequent returns of mature, profitable, dividend-paying, low-volatility firms. When sentiment is low, the pattern partially reverses.

The cross-sectional spread predictable from sentiment is ~1% per month in the original sample.

## Original Paper

Baker, M. & Wurgler, J. (2006) "Investor Sentiment and the Cross-Section of Stock Returns" — *Journal of Finance*. Follow-up: Baker & Wurgler (2007) "Investor Sentiment in the Stock Market" survey.

## Mechanism

- **Noise traders push mispricings** — when sentiment is high, noise traders crowd into speculative, hard-to-value, hard-to-short stocks, pushing prices above fundamentals
- **Limits to arbitrage** — short-selling constraints prevent arbitrageurs from correcting the overpricing in real time; the correction happens over subsequent months as the sentiment wave ebbs
- **Stambaugh, Yu, Yuan (2012, 2015)** extended this to show that *most* cross-sectional anomalies are stronger following high-sentiment periods, because sentiment disproportionately overprices the stocks that anomalies short

## Edge Category

**Behavioral** + **structural** (limits to arbitrage amplify the effect).

## Replication Status

Replicated in US data and internationally. Stambaugh-Yu-Yuan's finding that sentiment amplifies anomaly returns is now a standard ingredient in multi-factor research.

## Decay History

The index itself has held up — the Baker-Wurgler index still predicts cross-sectional returns. The tradeable magnitudes have compressed somewhat as institutional arbitrage has grown, but the short side of most equity anomalies continues to deliver disproportionately after high-sentiment periods.

## Current Viability

Tradeable as:

- A regime signal — increase factor exposures (value, low-vol, quality) after high sentiment; decrease after low sentiment
- A gating feature on individual anomaly strategies — only trade the short side of momentum/value/low-vol after sentiment has spiked
- A macro risk indicator for the broad market (though direct market-timing on sentiment is noisier than cross-sectional applications)

Sophisticated quant funds use sentiment-conditional factor loadings as a standard ingredient.

## Related Strategies

- [[lottery-stock-anomaly]] — disproportionately affected by sentiment swings
- [[ipo-underperformance]] — IPO volume is one of the sentiment proxies
- [[idiosyncratic-volatility-anomaly]] — anchored in limits-to-arbitrage
- Stambaugh-Yu-Yuan sentiment-conditional anomaly strategies

## Sources

- Baker & Wurgler (2006) "Investor Sentiment and the Cross-Section of Stock Returns"
- Baker & Wurgler (2007) survey
- Stambaugh, Yu, Yuan (2012) "The Short of It: Investor Sentiment and Anomalies"
- Stambaugh, Yu, Yuan (2015) "Arbitrage Asymmetry and the Idiosyncratic Volatility Puzzle"

## Related

- [[anomalies-overview]]
- [[lottery-stock-anomaly]]
- [[ipo-underperformance]]
- [[behavioral-finance]]
