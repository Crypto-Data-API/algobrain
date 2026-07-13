---
title: "OKX"
type: entity
created: 2026-04-15
updated: 2026-04-21
status: good
tags: [exchange, crypto, derivatives]
entity_type: exchange
aliases: ["OKX", "OKEx"]
founded: 2017
headquarters: "Seychelles (global operations)"
website: "https://www.okx.com"
related: ["[[binance]]", "[[coinbase]]", "[[hyperliquid]]", "[[bybit]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[exchange-api-reference]]"]
---

# OKX

OKX (formerly OKEx) is a global cryptocurrency exchange offering spot, futures, perpetual swaps, options, and DeFi services. One of the top 3 crypto exchanges by derivatives volume globally, with particularly strong presence in Asia.

## Key Facts

| Metric | Value |
|---|---|
| Founded | 2017 |
| Headquarters | Seychelles (HQ), Dubai (VARA license), Hong Kong (licensed) |
| Products | Spot (350+ pairs), USDT-M perps, Coin-M perps, futures, options |
| Daily volume (approx.) | $3-8B (spot + derivatives combined) |
| Fee structure | Tiered maker-taker (8 tiers) |
| Account type | **Unified account** (spot + derivatives share margin) |

## Fee Schedule

| Tier | 30d Volume | Maker | Taker |
|---|---|---|---|
| VIP 0 | < $5M | 0.080% | 0.100% |
| VIP 1 | $5-10M | 0.070% | 0.090% |
| VIP 3 | $50-100M | 0.040% | 0.060% |
| VIP 5 | $500M-1B | 0.020% | 0.040% |
| VIP 8 | > $10B | -0.005% (rebate) | 0.015% |

## Unified Account

OKX's **unified trading account** allows spot, futures, options, and margin positions to share a single margin pool. This provides capital efficiency advantages for arbitrage: unrealized profits on one leg can offset margin requirements on another.

**Arb implication:** For [[funding-rate-arbitrage]], the spot long and perp short can share margin, reducing the total capital locked. However, this also means a loss on one position can liquidate the other — use with caution for market-neutral strategies.

## Execution Mechanics for Arbitrage

### Liquidation Engine

OKX uses a **mark price** system based on multiple exchange index prices (BTC: Binance, Coinbase, Bitstamp, Kraken, Gemini weighted average). Prevents single-exchange manipulation.

**Maintenance margin tiers (BTC USDT-M Perp):**

| Position (USDT) | Maintenance Margin | Max Leverage |
|---|---|---|
| 0 - 50,000 | 0.40% | 125x |
| 50,000 - 200,000 | 0.50% | 100x |
| 200,000 - 2,000,000 | 1.00% | 50x |
| 2,000,000 - 20,000,000 | 2.50% | 20x |
| > 20,000,000 | 5.00% | 10x |

### Auto-Deleveraging (ADL)

OKX implements ADL when the insurance fund cannot cover a liquidation gap. ADL priority is based on **profit ratio and leverage**: the most profitable, highest-leveraged positions are closed first.

**ADL indicator:** Visible on the position panel (5-level light system). If your light is at level 4-5, reduce leverage or take profit to lower ADL priority.

### Insurance Fund

OKX maintains a public insurance fund per contract. Balances are visible on the exchange. Funded by liquidation proceeds exceeding the bankruptcy price.

### Margin Modes

| Mode | Behavior | Available |
|---|---|---|
| **Isolated** | Per-position margin | Yes |
| **Cross** | Shared across positions (within unified account) | Yes |
| **Portfolio margin** | Risk-based margin across correlated positions | Yes (VIP 3+) |

**Portfolio margin** is particularly valuable for arb: a long spot + short perp position under portfolio margin receives reduced margin requirements because the positions hedge each other.

### Position Limits

Position limits are per-contract and tier-based, typically $50-200M for BTC at the lowest leverage tiers. Check `GET /api/v5/public/position-tiers` for current limits.

### Funding Rate

- **Interval:** Every 8 hours (00:00, 08:00, 16:00 UTC)
- **Formula:** Premium index + clamp(interest rate - premium index, -0.05%, 0.05%)
- **Cap:** ±0.75% per period (some contracts)

### Clawback Policy

OKX's terms include socialized loss provisions. If the insurance fund is depleted, losses may be distributed across profitable traders. This has not been invoked historically but exists as a contractual possibility.

## Sources

- OKX official documentation (okx.com/docs)
- [[exchange-api-reference]]
