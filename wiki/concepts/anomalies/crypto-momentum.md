---
title: "Crypto Momentum Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, crypto, momentum, academic-research]
aliases: ["Bitcoin Momentum", "Cryptocurrency Momentum Effect"]
domain: [anomalies]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[momentum-anomaly]]", "[[time-series-momentum]]"]
---

# Crypto Momentum Anomaly

Cryptocurrency returns exhibit strong momentum at multiple horizons — past winners continue to outperform past losers both in time series (each coin predicting its own future returns) and in cross section (relative ranking predicting relative future returns). The effect is larger than in equity markets and remains one of the most robust alpha sources in systematic crypto trading.

## What

Two measurable forms:

- **Time-series momentum** — if bitcoin's return over the past 1-week to 3-month window was positive, its subsequent return is also positively biased. The Sharpe of a simple time-series momentum strategy on BTC has been substantially higher than buy-and-hold across most samples.
- **Cross-sectional momentum** — rank the top ~50 liquid cryptocurrencies on their prior 4-12 week returns. Long the top quintile, short the bottom quintile. Liu & Tsyvinski (2018) documented this formally with ~1% per week return spreads in some lookback specifications.

## Original Paper

Liu, Y. & Tsyvinski, A. (2018, 2021) "Risks and Returns of Cryptocurrency" — *Review of Financial Studies*. Follow-up cross-sectional work by Liu, Tsyvinski, Wu (2019) and Shen, Urquhart, Wang (2020).

## Mechanism

- **Slow information diffusion** — crypto markets are dominated by retail investors who absorb information more slowly than institutional equity investors. Price trends reflect ongoing awareness rather than immediate repricing.
- **Network effects and adoption dynamics** — crypto projects with rising usage attract more attention, more liquidity, and more capital in a self-reinforcing cycle. Prices trend because fundamentals trend.
- **Limited arbitrage / short constraints** — most crypto exchanges have limited short-selling infrastructure, so overpriced coins cannot be arbitraged away efficiently
- **Funding-rate feedback** — perpetual futures funding rates amplify trend dynamics: long-biased funding pushes new longs to pay longs, reinforcing the trend until funding becomes unsustainable

## Edge Category

**Behavioral** (slow diffusion, narrative extrapolation) + **structural** (limited arbitrage).

## Replication Status

Replicated across multiple academic samples and heavily validated by practitioner / hedge fund backtests. One of the few crypto anomalies with solid published evidence.

## Decay History

Mild decay as systematic crypto funds grow. BTC-only momentum has compressed; cross-sectional momentum across altcoins has held up better but is noisier because of survivorship bias and exchange-level liquidity issues.

## Current Viability

Directly tradeable by systematic crypto funds and retail traders with appropriate infrastructure:

- **BTC time-series momentum** — simple and robust, but Sharpe has fallen as BTC matures
- **Cross-sectional altcoin momentum** — higher returns, higher volatility, requires liquidity filters and survivorship-aware backtests
- **Combined with trend-following on funding rates and basis** for additional alpha

**Risks:** crypto momentum strategies experience extreme drawdowns in sharp regime changes (Luna collapse, FTX failure). Position sizing and vol targeting are essential.

## Related Strategies

- [[momentum-anomaly]] — equity analog
- [[time-series-momentum]] — time-series version, applied to crypto
- [[crypto-funding-rate-anomaly]] — complementary
- Systematic crypto trend-following funds

## Sources

- Liu & Tsyvinski (2018, 2021) "Risks and Returns of Cryptocurrency" — *Review of Financial Studies*
- Liu, Tsyvinski, Wu (2019) "Common Risk Factors in Cryptocurrency"
- Shen, Urquhart, Wang (2020) cross-sectional tests
- Hubrich (2017) "'Know When to Hodl 'Em'" — early practitioner crypto momentum analysis

## Related

- [[anomalies-overview]]
- [[momentum-anomaly]]
- [[time-series-momentum]]
- [[crypto-funding-rate-anomaly]]
