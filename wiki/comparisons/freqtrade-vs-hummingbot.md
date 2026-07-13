---
title: Freqtrade vs Hummingbot
type: comparison
created: 2026-04-07
updated: 2026-04-07
status: good
tags:
  - crypto-bots
  - open-source
  - algorithmic-trading
  - market-making
subjects:
  - "[[freqtrade]]"
  - "[[hummingbot]]"
comparison_dimensions:
  - focus
  - strategies
  - backtesting
  - exchanges
  - dex-support
  - community
  - deployment
related:
  - "[[custom-python-bots]]"
  - "[[market-making]]"
  - "[[algorithmic-trading]]"
---

# Freqtrade vs Hummingbot

## Overview

[[freqtrade]] and [[hummingbot]] are the two most popular open-source crypto trading bot frameworks. While both are Python-based and community-driven, they target different trading styles. Freqtrade is a general-purpose strategy framework built for momentum, mean-reversion, and ML-driven strategies with strong backtesting. Hummingbot specializes in market making and arbitrage, with unique DEX support through its Gateway module. Choosing between them depends on your strategy type and whether you need decentralized exchange connectivity.

## Comparison Table

| Dimension | Freqtrade | Hummingbot |
|---|---|---|
| **Primary Focus** | General strategy framework | Market making and arbitrage |
| **Strategy Types** | Momentum, mean-reversion, ML, any | Market making, arb, cross-exchange |
| **Backtesting** | Built-in, robust, with hyperopt | Limited, strategy-specific |
| **Supported Exchanges** | 30+ CEXs via CCXT | 20+ CEXs + DEX via Gateway |
| **DEX Support** | No | Yes (Uniswap, dYdX, etc.) |
| **Language** | Python | Python (Cython core) |
| **UI** | FreqUI web dashboard | Hummingbot Dashboard |
| **Community Size** | Large (8K+ GitHub stars) | Large (7K+ GitHub stars) |
| **Learning Curve** | Moderate | Moderate-High |
| **Deployment** | Docker, self-hosted | Docker, self-hosted |
| **Strategy Development** | Python classes, indicators | Script-based, connectors |
| **Data Download** | Built-in data download tools | Via exchange connectors |

## Key Differences

**Strategy Philosophy** is the core divergence. [[freqtrade]] is strategy-agnostic: you write Python classes that define entry/exit logic using any indicators, ML models, or custom signals. It provides the infrastructure (data, execution, risk management, backtesting) and you supply the alpha. [[hummingbot]] is strategy-opinionated: it ships with built-in market making and arbitrage strategies that you configure and tune. You can write custom scripts, but the architecture favors its core use cases.

**Backtesting Capability** is Freqtrade's standout advantage. Its backtesting engine supports multi-pair testing, hyperparameter optimization (hyperopt), walk-forward analysis, and detailed performance reporting including profit/loss, drawdown, and trade-by-trade analysis. Hummingbot's backtesting is more limited and focused on simulating its built-in strategies rather than arbitrary custom logic.

**DEX Support** is Hummingbot's unique strength. Its Gateway module connects to decentralized exchanges like Uniswap, PancakeSwap, and dYdX, enabling market making and arbitrage across both centralized and decentralized venues. Freqtrade operates exclusively on centralized exchanges via CCXT. For traders interested in DeFi liquidity provision or cross-venue arbitrage, Hummingbot is the only open-source option.

**Strategy Development Workflow** differs in structure. Freqtrade strategies are Python classes with defined methods (`populate_indicators`, `populate_entry_trend`, `populate_exit_trend`) and integrate naturally with pandas, TA-Lib, and ML libraries. Hummingbot uses a script-based approach with connector abstractions that handle order management. Freqtrade's approach is more flexible; Hummingbot's is more opinionated but faster for its supported strategy types.

**Exchange Coverage** overlaps significantly for centralized exchanges but Freqtrade's CCXT integration gives it broader CEX support. Hummingbot compensates with its DEX connectivity, offering a combined CEX+DEX footprint that no other open-source bot matches.

**Community and Ecosystem** are both healthy. Freqtrade has an active Discord with strategy sharing, a strategy repository, and comprehensive documentation. Hummingbot has a foundation-backed governance model, liquidity mining campaigns that incentivize market making, and an active community around its core use cases.

## When to Use Each

**Choose [[freqtrade]] when** you want to develop, backtest, and deploy custom trading strategies -- momentum, mean-reversion, ML-based, or any other approach on centralized exchanges. Best for traders who value robust backtesting, hyperparameter optimization, and full flexibility in strategy design.

**Choose [[hummingbot]] when** your primary interest is market making, cross-exchange arbitrage, or any strategy that requires DEX connectivity. Best for traders who want to provide liquidity on decentralized exchanges, capture spreads across venues, or participate in Hummingbot's liquidity mining programs.

**Use both when** you backtest and develop alpha signals in Freqtrade, then consider Hummingbot for execution on DEXs or for dedicated market-making operations alongside your directional strategies.

## Verdict

[[freqtrade]] is the better general-purpose crypto bot framework. Its backtesting, strategy flexibility, and development workflow make it the default choice for most algorithmic crypto traders. [[hummingbot]] wins for market making and is the only serious open-source option for DEX trading bots. They are complementary rather than competing: Freqtrade for directional alpha on CEXs, Hummingbot for market making and DEX liquidity strategies.
