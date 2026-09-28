---
title: "QuantConnect Investment Strategy Library"
type: source
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [backtesting, quantitative, algorithmic, education, open-source, python]
aliases: ["QuantConnect Strategy Library", "QC Strategy Library", "QuantConnect Research Library"]
source_type: article
source_url: "https://www.quantconnect.com/learning/articles/investment-strategy-library"
source_author: "QuantConnect (staff and community contributors)"
source_date: 2026-09-28
confidence: medium
claims_count: 16
related: ["[[quantconnect]]", "[[external-strategy-sources]]", "[[backtesting-pitfalls]]"]
---

# QuantConnect Investment Strategy Library

The **Investment Strategy Library** is [[quantconnect|QuantConnect]]'s free catalog of roughly 75 strategy write-ups, each pairing a short research article with a runnable [[quantconnect|LEAN]] algorithm (Python, some C#) that can be cloned into the QuantConnect cloud IDE. Many entries are ports of academic papers or [[quantpedia|Quantpedia]] strategy descriptions; a newer "Strategies" section (successor to the Quant League, which ended with Q4-2025) hosts community-submitted strategies. Accessed 2026-09-28.

## Summary

The library is organized by asset class: Stocks (~36 entries, out of scope here), ETFs (~20), Commodities (9), Futures & Options (5), Forex (5), and Multi-Asset (5). For a crypto-focused wiki its value is as an **idea source with reference code**, not as evidence: most published backtests are old (many end 2017-2019), run on a single instrument or a small hand-picked universe, and use LEAN's default reality model, which charges **zero fees on crypto, forex and CFDs**. Several articles openly report negative results (Dual Thrust on SPY, Sharpe -0.17; FX skewness risk premia, about -0.33%/yr), which makes the library more honest than most strategy catalogs but also means the reported numbers should be read as illustrations.

## Key Claims

1. The LEAN engine that runs every library algorithm is open source under the **Apache License 2.0**, free to use and extend commercially. [HIGH]
2. LEAN's `DefaultBrokerageModel` sets a zero-fee `ConstantFeeModel` for Forex, CFD and Crypto and the Interactive Brokers fee model for other asset classes; algorithms must set a brokerage model or fee model explicitly to get realistic crypto/FX costs. [HIGH]
3. Library categories (2026-09-28): Stocks, ETFs, Commodities, Futures & Options, Forex, Multi-Asset/Mixed. [HIGH]
4. **Dual Thrust**: range = max(HH-LC, HC-LL) over N=4 days; buy above open + K1·range, sell below open - K2·range, K1=K2=0.5, always-in reversal system. On SPY 2004-01 to 2017-08 it reported Sharpe -0.17 and 41.1% max drawdown. [MEDIUM]
5. **Dynamic Breakout II**: lookback starts at 20 days, scales with the day-over-day change in 30-day close volatility, bounded 20-60; entry needs both a close outside 2σ Bollinger Bands and a break of the N-day high/low; exit on a cross of the N-day SMA. EURUSD 2010-2016 reported ~2.3%/yr, Sharpe 0.31, ~14% max drawdown; GBPUSD lost money. [MEDIUM]
6. **Pairs Trading, Copula vs Cointegration**: Clayton/Gumbel/Frank copulas fitted by Kendall's tau and chosen by AIC; trade when conditional-probability mispricing indices cross 5%/95%. QQQ/XLK 2010-01 to 2019-09 reported 498 trades, 7.06% total profit, Sharpe 0.098, 24.0% drawdown; the cointegration comparison on GLD/DGL 2011-2017 reported Sharpe 0.179, 3.9% drawdown. [MEDIUM]
7. The copula article concludes the copula method gives more trading opportunities than cointegration, though its own Sharpe is lower than the cointegration example (different pairs and periods, so not a like-for-like test). [MEDIUM]
8. **Paired Switching**: hold 100% of whichever of two negatively correlated assets had the higher trailing 90-day return, rebalanced quarterly; no backtest statistics are published. [MEDIUM]
9. **Risk Premia in Forex Markets** (after Lemperiere et al., "Risk Premia: Asymmetric Tail Risks and Excess Returns"): long pairs with trailing return skewness < -0.6, short pairs with skewness > 0.6, weekly rebalance, four pairs (EURUSD, AUDUSD, USDCAD, USDJPY); reported about -0.33% annual return over a decade. [MEDIUM]
10. **Trading with WTI/BRENT Spread**: WTI and Brent CFDs (OANDA), a 20-day SMA of the spread for entry, a one-year linear-regression fair value (retrained monthly) for exit; no performance statistics published. [MEDIUM]
11. **Momentum Effect Combined with Term Structure in Commodities**: 22 commodity futures; sort by annualized roll return into tertiles, split top and bottom by 21-day momentum, long High-roll Winners and short Low-roll Losers, monthly rebalance; no statistics published. [MEDIUM]
12. **Forex Carry Trade**: long the highest-rate currency, short the lowest-rate currency, monthly rebalance. [MEDIUM]
13. **Term Structure Effect in Commodities**: trades the futures curve shape (backwardation vs contango) as a cross-sectional signal. [MEDIUM]
14. Other futures/FX/commodity entries include Commodities Futures Trend Following, Improved Momentum Strategy on Commodities Futures, Momentum Effect in Commodities Futures, Time Series Momentum Effect, Short Term Reversal with Futures, Exploiting Term Structure of VIX Futures, Volatility Risk Premium Effect, Optimal Pairs Trading, Intraday Dynamic Pairs Trading using Correlation and Cointegration, Forex Momentum, Combining Mean Reversion and Momentum in Forex, SVM Wavelet Forecasting, Gold Market Timing and Ichimoku Clouds in the Energy Sector. [HIGH]
15. Several library pages (e.g., Paired Switching, Momentum + Term Structure) are marked "pending review" and carry no backtest statistics. [MEDIUM]
16. QuantConnect announced Quant League is being replaced by a "Strategies" section; Q4-2025 was the final Quant League. [MEDIUM]

## Entities / Concepts / Strategies Mentioned

- Entities: [[quantconnect]]
- Strategies created from this source: [[dual-thrust]], [[dynamic-breakout-ii]], [[copula-pairs-trading]], [[paired-switching]], [[fx-skewness-risk-premia]], [[wti-brent-spread]], [[commodity-momentum-term-structure]]
- Existing pages annotated: [[carry-trade]], [[commodity-carry-strategy]], [[commodity-momentum]], [[currency-momentum]], [[pairs-trading]], [[time-series-momentum]], [[short-term-reversal]], [[vix-trading]], [[volume-oi-conditioned-reversal]], [[dollar-carry-trade]]
- Concepts: [[cointegration]], [[gaussian-copula]], [[skewness]], [[roll-yield]], [[bollinger-bands]], [[survivorship-bias]], [[transaction-costs]]

## Confidence Notes

Confidence is **medium** overall: the strategy descriptions are accurate paraphrases of QuantConnect's own pages, but the performance figures are single-instrument, pre-cost (or zero-fee) backtests from 2017-2019 era research and have not been independently replicated. The licensing and fee-model claims come from QuantConnect's GitHub and documentation and are rated high.

## Related

- [[quantconnect]]
- [[external-strategy-sources]]
- [[backtesting-pitfalls]]
- [[cryptodataapi-backtesting]]
