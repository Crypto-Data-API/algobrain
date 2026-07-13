---
title: "Bybit"
type: entity
created: 2026-04-15
updated: 2026-04-21
status: good
tags: [exchange, crypto, derivatives]
entity_type: exchange
aliases: ["Bybit"]
founded: 2018
headquarters: "Dubai, UAE (VARA licensed)"
website: "https://www.bybit.com"
related: ["[[binance]]", "[[okx]]", "[[coinbase]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[exchange-api-reference]]"]
---

# Bybit

Bybit is a global cryptocurrency exchange specializing in derivatives trading. Founded in 2018, it rapidly grew to become one of the top 3 crypto derivatives exchanges by volume, known for competitive fees and a clean trading interface.

## Key Facts

| Metric | Value |
|---|---|
| Founded | 2018 |
| Headquarters | Dubai (VARA license), Singapore (MAS oversight) |
| Products | Spot (500+ pairs), USDT perps, Inverse perps, futures, options |
| Daily volume (approx.) | $5-15B (spot + derivatives combined) |
| Fee structure | Tiered maker-taker (VIP 0 to Pro 5) |
| Account type | **Unified Trading Account** (optional) |

## Fee Schedule

| Tier | 30d Volume | Maker | Taker |
|---|---|---|---|
| VIP 0 | < $2M | 0.100% | 0.100% |
| VIP 1 | $2-5M | 0.060% | 0.080% |
| VIP 3 | $25-50M | 0.020% | 0.040% |
| Pro 3 | $200-500M | 0.005% | 0.025% |
| Pro 5 | > $2B | 0.000% | 0.020% |

## Unified Trading Account (UTA)

Bybit's optional UTA merges spot, derivatives, and options into a single margin account. Similar to OKX's unified account. Capital efficiency improves for hedged positions (e.g., spot long + perp short for [[funding-rate-arbitrage]]).

**Caution:** Cross-margining in UTA means one blowup position can affect all others. For arb, use isolated margin on individual positions unless you're on portfolio margin.

## Execution Mechanics for Arbitrage

### Liquidation Engine

Bybit uses a **mark price** based on a spot index (weighted average of major exchanges including Binance, Coinbase, Kraken). Liquidation triggers when mark price crosses the liquidation price.

**Maintenance margin tiers (BTC USDT Perp):**

| Position (USDT) | Maintenance Margin | Max Leverage |
|---|---|---|
| 0 - 100,000 | 0.50% | 100x |
| 100,000 - 500,000 | 1.00% | 50x |
| 500,000 - 2,000,000 | 2.50% | 20x |
| 2,000,000 - 10,000,000 | 5.00% | 10x |
| > 10,000,000 | 10.00% | 5x |

**Liquidation process:** Bybit uses a **partial liquidation** system — it reduces the position progressively rather than closing it entirely at once. This reduces market impact from liquidation cascades.

### Auto-Deleveraging (ADL)

Bybit implements ADL when the insurance fund cannot cover a liquidation loss. ADL ranking is based on: profit percentage (higher profit = higher priority for ADL closure) and leverage ratio.

**ADL indicator:** 5 lights on the position panel. Levels 4-5 mean you're at high risk of being auto-deleveraged.

### Insurance Fund

Bybit maintains a public insurance fund per contract. The fund absorbs losses from liquidated positions that are closed at worse than bankruptcy price. Insurance fund balance is publicly visible on Bybit's website.

**Historical adequacy:** Bybit's insurance fund has generally maintained adequate reserves, but extreme volatility events (e.g., March 2020 COVID crash) tested reserves significantly.

### Margin Modes

| Mode | Behavior | Available |
|---|---|---|
| **Isolated** | Per-position margin, losses capped | Yes (default) |
| **Cross** | Shared margin across all positions | Yes |
| **Portfolio margin** | Risk-based, correlated-position offsets | Yes (UTA required, VIP tier) |

**Recommendation for arb:** Use **isolated margin** unless you specifically need portfolio margin offsets for complex multi-leg strategies.

### Position Limits

Bybit enforces tiered position limits based on the risk limit setting. Each risk limit tier increases maximum position size but also increases maintenance margin. Default risk limits are typically:
- BTC: Up to $200M at lowest leverage
- ETH: Up to $100M
- Altcoins: $5-50M depending on liquidity

### Funding Rate

- **Interval:** Every 8 hours (00:00, 08:00, 16:00 UTC)
- **Formula:** Average premium index + clamp function
- **Cap:** ±2% per period (some contracts have lower caps)
- **Hyperliquid comparison:** Bybit 8-hour settlement vs. Hyperliquid 1-hour. Always annualize before comparing rates

### Clawback / Socialized Loss

Bybit's terms include provisions for socialized loss distribution if the insurance fund is depleted. The mechanism reduces winning traders' profits proportionally. This has not been invoked but remains a contractual risk.

### Notable for Arbitrage

- **Copy trading integration:** Bybit's copy trading feature means some flow is from "followers" who create predictable order patterns — potentially exploitable for orderflow-based strategies
- **Launchpad events:** New token launches on Bybit create temporary price dislocations vs. other exchanges
- **Spot-perp basis:** Bybit's perp market is deep enough for [[cash-and-carry]] and [[funding-rate-arbitrage]] at institutional scale

## Sources

- Bybit official documentation (bybit-exchange.github.io/docs)
- [[exchange-api-reference]]
