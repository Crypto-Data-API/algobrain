---
title: "Pionex"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [ai-trading, trading-bots, crypto, exchange]
entity_type: company
website: "https://www.pionex.com"
related:
  - "[[three-commas]]"
  - "[[binance]]"
  - "[[bot-risks-and-pitfalls]]"
  - "[[freqtrade]]"
---

# Pionex

**Pionex** is a cryptocurrency exchange with 16 built-in free trading bots. Unlike [[three-commas|3Commas]] or other external bot platforms that connect via API, Pionex integrates the bots directly into the exchange -- no subscription fees, no API key setup, just exchange trading fees (0.05% maker/taker).

---

## Overview

Launched in 2019, backed by Sequoia China and Gaorong Capital, Pionex aggregates [[liquidity]] from [[binance|Binance]] and Huobi. The value proposition: free bot access for everyone, targeting beginners who want automation without [[freqtrade]]'s technical setup or [[three-commas|3Commas]]'s subscription cost. Licensed as MSB in the US, 1M+ users.

---

## Key Features

| Bot Type | Description |
|---|---|
| **Grid Trading Bot** | Buy low/sell high within a price range automatically |
| **Leveraged Grid Bot** | Grid trading with up to 5x leverage |
| **Infinity Grid Bot** | Grid bot with no upper price limit (never misses upside) |
| **DCA Bot** | Recurring buys at fixed intervals for accumulation |
| **Smart Trade** | Set take-profit, stop-loss, and trailing orders |
| **Rebalancing Bot** | Maintain target portfolio allocations automatically |
| **Spot-Futures Arbitrage** | Earn [[funding-rate]] by going long spot, short perpetual |
| **Martingale Bot** | Aggressive DCA strategy (higher risk) |
| **TWAP Bot** | Time-weighted execution for large orders |

---

## How to Use

1. **Sign up** at pionex.com or download the mobile app
2. **Deposit** crypto or buy with fiat
3. **Choose a bot** and configure parameters (or use AI-suggested settings based on historical [[volatility]])
4. **Start**: Bot runs 24/7; monitor via app dashboard
5. **Close**: Stop bot and release funds at any time

---

## Strengths and Weaknesses

**Strengths**: Completely free bots -- only pay standard exchange fees (0.05%). Extremely beginner-friendly with mobile-first design. AI-suggested parameters lower the barrier to entry. Spot-futures arbitrage bot is a unique low-risk strategy. No API key management hassles since bots are native. 16 bot types cover most common strategies.

**Weaknesses**: Limited to Pionex's own exchange -- cannot use bots on [[binance|Binance]] or other platforms. Fewer trading pairs than major exchanges. No custom strategy development (use [[freqtrade]] or [[custom-python-bots]] for that). Grid bots lose money in strong downtrends. Centralized exchange with custody risk. No advanced [[backtesting-pitfalls|backtesting]] or [[walk-forward-optimization|walk-forward analysis]].

---

## Example

Setting up a Grid Bot for ETH/USDT:

- **Pair**: ETH/USDT
- **Lower price**: $2,800
- **Upper price**: $3,600
- **Grid count**: 100 (grids every ~$8)
- **Investment**: $1,000
- **Mode**: Arithmetic (equal spacing) or Geometric (percentage spacing)

The bot places 100 buy/sell orders across the $2,800-$3,600 range. Each time price moves through a grid level, it buys low and sells high, capturing the spread. Works well in ranging markets but [[bot-risks-and-pitfalls|loses money]] if price drops below $2,800 and stays there.

---

## See Also

- [[three-commas]] -- Subscription-based bot platform with more customization
- [[freqtrade]] -- Open-source bot framework for custom strategies
- [[bot-risks-and-pitfalls]] -- Grid bot risks and common failures
- [[binance]] -- Exchange whose liquidity Pionex aggregates
