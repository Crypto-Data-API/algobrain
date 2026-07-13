---
title: "Hummingbot"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [ai-trading, trading-bots, market-making, crypto, open-source]
entity_type: company
website: "https://hummingbot.io"
aliases: ["Hummingbot", "hummingbot"]
related:
  - "[[freqtrade]]"
  - "[[bot-architecture]]"
  - "[[custom-python-bots]]"
  - "[[liquidity]]"
  - "[[arbitrage]]"
---

# Hummingbot

**Hummingbot** is an open-source trading bot framework specializing in market making and arbitrage strategies. It supports both centralized exchanges (CEX) and decentralized exchanges (DEX), making it unique among retail-accessible bot frameworks.

---

## Overview

Founded in 2019 by CoinAlpha, Hummingbot democratizes [[liquidity]] provision and [[arbitrage]] -- strategies traditionally reserved for institutional market makers. Configurable strategy templates let users run sophisticated strategies without coding from scratch. The Gateway module enables DEX connectivity on Ethereum, Polygon, BNB Chain, and others. Free, open source, governed by the HBOT token.

---

## Key Features

| Feature | Detail |
|---|---|
| **Pure Market Making** | Place bid/ask orders around mid-price with configurable spread, order size, and levels |
| **Cross-Exchange Market Making** | Make markets on one exchange, hedge on another |
| **Arbitrage** | Exploit price differences between exchanges |
| **TWAP** | Time-weighted average price execution for large orders |
| **Avellaneda-Stoikov** | Academic market making model with inventory risk management |
| **DEX Support** | Gateway module connects to Uniswap, PancakeSwap, dYdX, and more |
| **Exchange Support** | Binance, Kraken, Gate.io, KuCoin, and 30+ other CEXs |

---

## How to Use

1. **Install**: Docker (recommended) or `conda` environment
2. **Configure**: `create` walks through API keys, pairs, strategy parameters
3. **Select strategy**: Pure market making, cross-exchange, arbitrage, or TWAP
4. **Paper trade**: Validate behavior before going live
5. **Start**: `start` command begins execution; monitor via terminal or Telegram

---

## Strengths and Weaknesses

**Strengths**: Best open-source tool for [[liquidity|market making]] strategies. CEX + DEX support is unique. No coding required for built-in strategies. Academic market making models (Avellaneda-Stoikov) built in. Active community and documentation. Free.

**Weaknesses**: Market making is inherently risky -- inventory risk, adverse selection, and wide spreads in volatile markets can cause losses. DEX gateway can be complex to set up. Not designed for momentum or trend-following strategies (use [[freqtrade]] instead). Performance depends heavily on parameter tuning and market conditions.

---

## Example

```
Strategy: pure_market_making    Exchange: binance
Trading pair: ETH-USDT          Bid/Ask spread: 0.3%
Order amount: 0.1 ETH           Order levels: 3
Order level spread: 0.2%        Inventory skew: enabled
Kill switch: -2%
```

Places three levels of buy/sell orders around mid-price, each 0.2% apart, with 0.3% minimum spread and automatic inventory balancing.

---

## See Also

- [[freqtrade]] -- Open-source crypto bot for momentum/trend strategies
- [[bot-architecture]] -- General trading bot design patterns
- [[arbitrage]] -- Exploiting price differences across venues
- [[liquidity]] -- What market makers provide to the market
- [[bot-risks-and-pitfalls]] -- Risks specific to automated trading
