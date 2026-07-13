---
title: "3Commas"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [ai-trading, trading-bots, crypto, platform]
entity_type: company
website: "https://3commas.io"
aliases: ["3commas", "Three Commas"]
related:
  - "[[pionex]]"
  - "[[freqtrade]]"
  - "[[bot-risks-and-pitfalls]]"
  - "[[binance]]"
---

# 3Commas

**3Commas** is a cloud-based crypto trading bot platform offering grid bots, DCA bots, and signal bots through a user-friendly web interface. It requires no coding and targets retail traders who want automated strategies without building their own [[bot-architecture|infrastructure]].

---

## Overview

Founded in 2017, 3Commas connects to major exchanges via API ([[binance|Binance]], Coinbase, Kraken, Bybit, OKX). Users configure bots through a visual interface with pre-built strategy types. The SmartTrade terminal adds advanced order types (trailing TP/SL, simultaneous TP+SL) that exchanges lack natively. Subscription-based ($37-79/mo) with 500,000+ registered users.

---

## Key Features

| Feature | Detail |
|---|---|
| **DCA Bots** | Dollar-cost averaging bots that buy dips at preset intervals/levels |
| **Grid Bots** | Place buy/sell orders at grid intervals to profit from range-bound markets |
| **Signal Bots** | Execute trades based on external signals (TradingView webhooks, custom alerts) |
| **SmartTrade** | Advanced trading terminal with trailing TP/SL, concurrent take-profit and stop-loss |
| **Copy Trading** | Follow and auto-copy top-performing traders on the platform |
| **Exchange Support** | Binance, Coinbase, Kraken, Bybit, OKX, KuCoin, and others |
| **Marketplace** | Pre-built bot templates and signal providers |

---

## How to Use

1. **Sign up** at 3commas.io and choose subscription tier
2. **Connect exchange** via API keys (read + trade permissions)
3. **Choose bot type**: DCA, Grid, or Signal
4. **Configure**: Pair, amount, grid levels/DCA steps, take-profit, safety orders
5. **Monitor**: Dashboard shows all active bots and PnL

---

## Strengths and Weaknesses

**Strengths**: No coding required -- fully visual configuration. SmartTrade terminal is genuinely useful even without bots. DCA bots are effective for accumulation strategies. TradingView signal integration enables custom strategies without code. Large user community and marketplace.

**Weaknesses**: Monthly subscription cost ($37-79/mo) adds up, especially for small accounts. [[bot-risks-and-pitfalls|Bot performance]] depends entirely on parameter choices and market conditions -- many users lose money with poorly configured DCA bots in downtrends. Had a security breach in 2022 (API keys compromised). Limited [[backtesting-pitfalls|backtesting]] capabilities compared to [[freqtrade]] or [[quantconnect]]. Less flexibility than custom [[custom-python-bots|Python bots]].

---

## Example

A DCA bot for BTC accumulation: base order $100, 5 safety orders of $150 each at -2% intervals. Take profit at 1.5% from average entry with 0.5% trailing. The bot enters with $100, buys more as price drops, and sells at 1.5% profit from the DCA'd position. Pricing: Pro $37/mo (1 exchange), Expert $79/mo (unlimited), Free tier (SmartTrade only).

---

## See Also

- [[pionex]] -- Exchange with free built-in bots (no subscription)
- [[freqtrade]] -- Free, open-source alternative (requires coding)
- [[bot-risks-and-pitfalls]] -- Risks of automated trading
- [[binance]] -- Most commonly connected exchange
