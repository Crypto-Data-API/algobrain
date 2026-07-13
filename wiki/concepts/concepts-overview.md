---
title: "Trading Concepts"
type: index
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [concepts, index]
---

# Trading Concepts

Core theoretical and practical concepts underlying all trading activity.

Every trading strategy rests on a foundation of concepts -- from how an order book matches buyers and sellers, to how [[risk-management-overview|risk management]] keeps you in the game, to how indicators like [[rsi|RSI]] and [[macd|MACD]] distill price action into actionable signals. This section is the conceptual backbone of the wiki.

If you are new to trading, start with [[perpetual-futures]] to understand the most-traded crypto instrument, [[risk-management-overview]] to learn why capital preservation matters more than returns, and [[technical-analysis-overview]] to see how chart-based analysis works in practice.

## Start Here

- [[perpetual-futures]] -- The dominant crypto derivatives instrument explained
- [[risk-management-overview]] -- Why managing risk is the most important skill
- [[technical-analysis-overview]] -- Reading charts, patterns, and indicators

## Subcategories

### Risk Management

The discipline of identifying, assessing, and controlling potential financial losses. Without risk management, even the best strategy leads to ruin. Covers [[position-sizing]], [[stop-loss]] strategies, [[value-at-risk]], [[maximum-drawdown]], [[drawdown-management]], [[hedging]], [[derisking]], [[leverage]] control, and the mathematics of [[risk-of-ruin]].

- **Overview**: [[risk-management-overview|Risk Management (Full Guide)]]
- **Hub page**: [[risk-management]]
- **Key pages**: [[position-sizing]], [[stop-loss]], [[kelly-criterion]], [[leverage]], [[hedging]], [[derisking]], [[value-at-risk]], [[maximum-drawdown]], [[drawdown-management]], [[counterparty-risk]], [[liquidity-risk]], [[model-risk]], [[tail-risk]], [[black-swan]], [[options-position-sizing]]

### Portfolio Theory

How to combine assets and strategies into portfolios that optimize risk-adjusted returns. Spans classical [[modern-portfolio-theory]], the [[efficient-frontier]], [[diversification]], asset allocation frameworks like [[risk-parity]] and the [[all-weather-portfolio]], and practical tools like [[portfolio-rebalancing]] and [[dollar-cost-averaging]].

- **Overview**: [[portfolio-theory-overview]]
- **Key pages**: [[modern-portfolio-theory]], [[efficient-frontier]], [[diversification]], [[correlation]], [[kelly-criterion]], [[risk-parity]], [[portfolio-construction]], [[portfolio-rebalancing]], [[sharpe-ratio]], [[sortino-ratio]], [[alpha]], [[capital-asset-pricing-model]], [[strategy-correlation-matrix]], [[when-to-retire-a-strategy]]

### Technical Indicators

Mathematical transformations of price and volume data used to identify trends, momentum, overbought/oversold conditions, and potential entry/exit signals. Includes oscillators ([[rsi]], [[macd]], stochastic), trend indicators (moving averages, ADX), volume indicators (OBV, VWAP), and [[volatility]] measures ([[vix]], Bollinger Bands, ATR).

- **Overview**: [[indicators-overview]]
- **Key pages**: [[rsi]], [[macd]], [[vix]], [[implied-volatility]], [[iv-rank-and-iv-percentile]], earnings-calendar, [[bollinger-bands]], [[atr]]

### Market Microstructure

How markets actually work at the mechanical level: [[order-books]], [[bid-ask-spread|bid-ask spreads]], [[market-makers]], [[slippage]], [[market-impact]], [[high-frequency-trading]], [[payment-for-order-flow]], and exchange mechanics. Understanding microstructure is essential for anyone whose strategy edge depends on execution quality.

- **Overview**: [[market-microstructure-overview]]
- **Key pages**: [[order-books]], [[bid-ask-spread]], [[market-makers]], [[slippage]], [[market-impact]], [[high-frequency-trading]], [[order-flow]], [[spread]], [[circuit-breakers]], [[spoofing]], [[liquidity-sweeps]]

### Behavioral Finance

The psychology of trading and investing: why humans systematically make irrational financial decisions, and how to exploit (or protect against) these biases. Covers [[cognitive-biases]], [[loss-aversion]], [[overconfidence]], [[herding]], [[disposition-effect]], [[anchoring]], [[confirmation-bias]], and the broader dynamics of [[market-bubbles]] and [[sentiment]].

- **Overview**: [[behavioral-finance-overview]]
- **Key pages**: [[trading-psychology]], [[cognitive-biases]], [[loss-aversion]], [[overconfidence]], [[disposition-effect]], [[herding]], [[confirmation-bias]], [[anchoring]], [[prospect-theory]], [[survivorship-bias]], [[look-ahead-bias]], [[sentiment]], [[market-bubbles]]

### Options

Concepts specific to options trading: pricing models, the [[greeks]], strategy construction, and risk management for options portfolios. Includes [[implied-volatility]], [[delta-hedging]], [[gamma-scalping]], [[vega-hedging]], [[iv-rank-and-iv-percentile]], [[put-call-parity]], and structures like [[iron-condor|iron condors]], [[iron-butterfly|iron butterflies]], [[credit-spread|credit spreads]], and [[vertical-spread|vertical spreads]].

- **Key pages**: [[implied-volatility]], [[iv-rank-and-iv-percentile]], [[delta-hedging]], [[gamma-scalping]], [[vega-hedging]], [[credit-spread]], [[iron-butterfly]], [[put-call-parity]], [[assignment-and-exercise]], [[options-position-sizing]], [[pin-risk]], [[gamma-squeeze]]

### DeFi and Crypto Concepts

Concepts specific to decentralized finance and cryptocurrency markets: [[perpetual-futures]], funding rates, [[decentralized-exchanges]], [[liquidity-provision]], [[liquid-staking]], [[restaking]], [[smart-contracts]], and the unique risks of [[flash-loan-attacks]], [[rug-pulls]], [[oracle-manipulation]], and [[depeg-risk]].

- **Overview**: [[defi|DeFi Markets]]
- **Key pages**: [[perpetual-futures]], [[decentralized-exchanges]], [[liquidity-provision]], [[liquid-staking]], [[restaking]], [[smart-contracts]], [[smart-contract-risk]], [[flash-loan-attacks]], [[rug-pulls]], [[oracle-manipulation]], [[depeg-risk]], [[stablecoin-depegs]]

### Macroeconomics

Concepts connecting macroeconomic forces to market behavior: [[monetary-policy]], [[inflation]], [[interest-rates]], [[quantitative-easing]], [[fiscal-policy]], [[gdp]], [[employment]], [[fed-policy]], and frameworks for [[macro-analysis]] and [[macro-trading]].

- **Key pages**: [[monetary-policy]], [[inflation]], [[interest-rates]], [[quantitative-easing]], [[fed-policy]], [[business-cycle]], [[leading-indicators]], [[dxy]], [[commodity-macro-linkages]]

### Backtesting and Strategy Validation

Concepts related to testing and validating trading strategies: [[overfitting]], [[survivorship-bias]], [[look-ahead-bias]], [[deflated-sharpe-ratio]], [[probabilistic-sharpe-ratio]], [[walk-forward-analysis]], and the [[sharpe-sortino-calmar|Sharpe/Sortino/Calmar]] performance metrics.

- **Overview**: [[backtesting-overview]]
- **Key pages**: [[overfitting]], [[survivorship-bias]], [[look-ahead-bias]], [[deflated-sharpe-ratio]], [[sharpe-sortino-calmar]], [[walk-forward-analysis]]

## Cross-Cutting Themes

Several concepts span multiple categories:

- **[[volatility]]**: Appears in risk management (position sizing), indicators (VIX, Bollinger Bands), options (implied vol), and portfolio theory (efficient frontier)
- **[[correlation]]**: Central to portfolio construction, risk management, pairs trading, and crisis analysis
- **[[leverage]]**: Affects risk management, margin requirements, position sizing, and strategy capacity
- **[[liquidity-risk|Liquidity]]**: Impacts execution quality (microstructure), portfolio risk (risk management), and DeFi yields

## All Concept Pages

```dataview
TABLE status, difficulty, domain
FROM "wiki/concepts"
WHERE type = "concept"
SORT updated DESC
```
