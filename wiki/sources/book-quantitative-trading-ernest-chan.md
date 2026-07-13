---
title: "Quantitative Trading — Ernest Chan (2008)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, quantitative, algorithmic, backtesting]
aliases: ["Quantitative Trading", "Quantitative Trading Ernest Chan", "Ernie Chan Quant Trading"]
related: ["[[ml-trading-pipeline]]", "[[backtesting-pitfalls]]", "[[risk-management]]", "[[position-sizing]]", "[[quantitative-trading-ernest-chan]]"]
source_type: book
source_author: "Ernest Chan"
source_date: 2008
confidence: high
claims_count: 10
---

A practical guide for independent quantitative traders, written by Ernest Chan — a former IBM researcher and Morgan Stanley quant who transitioned to running his own algorithmic trading operation. Unlike academic texts, this book focuses on the complete workflow from sourcing strategy ideas to live deployment with real capital. Chan argues that independent quants have structural advantages over large funds (access to low-capacity strategies, lower overhead, faster iteration) and provides a concrete roadmap for building and operating a quantitative trading business. The book is widely considered the best entry point for aspiring systematic traders.

## Key Claims

1. [HIGH] **Academic papers are the best free source of trading strategy ideas**: SSRN, NBER working papers, and published finance journals contain hundreds of strategy ideas with full methodology disclosure. Chan recommends starting with published research rather than inventing strategies from scratch, as academics have already done the theoretical groundwork and statistical testing. (Source: Ernest Chan)

2. [HIGH] **Evaluate strategies on Sharpe ratio, max drawdown, and capacity before coding**: Before investing time in implementation, a strategy idea should pass three filters: (a) Does the reported [[sharpe-ratio|Sharpe ratio]] exceed 2.0? (b) Is the maximum historical drawdown survivable with available capital? (c) Does the strategy's capacity (maximum capital it can deploy without degrading returns) match the trader's capital base? (Source: Ernest Chan)

3. [HIGH] **Survivorship bias, look-ahead bias, and unrealistic transaction costs are the three biggest backtest killers**: Survivorship bias (testing only on stocks that still exist) inflates returns. Look-ahead bias (using data not available at the time of the trade) creates phantom alpha. Unrealistic transaction cost assumptions (zero slippage, no market impact) turn losers into apparent winners. Every backtest must explicitly address all three. (Source: Ernest Chan)

4. [HIGH] **Sharpe ratio is the universal metric for cross-strategy comparison**: Because it normalizes returns by volatility, the Sharpe ratio allows direct comparison between strategies with different return profiles, holding periods, and asset classes. Chan recommends a minimum annualized Sharpe of 2.0 for retail traders (who cannot diversify across many strategies as easily as institutions) to ensure profitability after costs and drawdowns. (Source: Ernest Chan)

5. [HIGH] **Start with minimal capital, verify live matches backtest, then scale**: The correct deployment process is to begin live trading with the smallest viable position size, run for a statistically significant period (typically 3-6 months), compare live results to backtest expectations, and only increase capital after confirming the live-backtest match. This prevents the catastrophic loss of deploying full capital into an untested system. (Source: Ernest Chan)

6. [HIGH] **Execution slippage and commissions can turn a profitable backtest into a losing live strategy**: The gap between backtest assumptions and live execution reality is the primary cause of strategy failure. Market impact (the price movement caused by your own order), queue priority in limit-order strategies, and brokerage commissions must be measured in live trading and fed back into the backtest model. (Source: Ernest Chan)

7. [HIGH] **Kelly criterion provides optimal position sizing given known edge and variance**: The Kelly formula (f* = edge / variance) determines the fraction of capital to risk on each trade that maximizes long-term geometric growth rate. In practice, Chan recommends using "half-Kelly" (50% of the Kelly-optimal fraction) to reduce drawdown severity at the cost of slightly lower long-term growth, since edge and variance estimates contain estimation error. (Source: Ernest Chan)

8. [HIGH] **Independent quants can trade low-capacity strategies that large funds cannot**: A strategy that generates $500K/year in profit with a capacity of $2M is meaningless to a $10B hedge fund but life-changing for an individual trader. This structural advantage means that the best opportunities for independent traders are in small, illiquid niches that institutional capital ignores. (Source: Ernest Chan)

9. [HIGH] **Risk management — drawdown limits and correlation-aware allocation — is non-negotiable**: Every live strategy must have a hard maximum drawdown limit (typically 20-25% of allocated capital) at which the system is shut down and re-evaluated. When running multiple strategies, capital allocation must account for strategy correlations — two strategies that draw down together provide less diversification benefit than two uncorrelated strategies. (Source: Ernest Chan)

10. [HIGH] **The process from idea to live trading is: source, evaluate, backtest, validate, deploy, monitor**: Chan provides a linear, repeatable workflow: (1) Source ideas from academic literature, (2) Evaluate on key metrics before coding, (3) Backtest with realistic assumptions, (4) Validate with out-of-sample testing and paper trading, (5) Deploy with minimal capital, (6) Monitor live performance against backtest benchmarks continuously. Deviation at any stage requires cycling back. (Source: Ernest Chan)

## Concepts Referenced

- [[ml-trading-pipeline]], [[backtesting-pitfalls]]
- [[risk-management]], [[position-sizing]]
- [[sharpe-ratio]], [[kelly-criterion]]
- [[survivorship-bias]], [[look-ahead-bias]]
- [[execution-quality]], [[slippage]]
- [[algorithmic]], [[systematic-trading]]

## Pages Backed

- [[ml-trading-pipeline]] — complete idea-to-deployment workflow for systematic strategies
- [[backtesting-pitfalls]] — survivorship bias, look-ahead bias, and unrealistic cost assumptions
- [[risk-management]] — drawdown limits and correlation-aware capital allocation
- [[position-sizing]] — Kelly criterion and half-Kelly practical implementation
- [[overfitting-in-trading]] — backtest-to-live gap as the ultimate test of overfitting
