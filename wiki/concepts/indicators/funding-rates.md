---
title: "Funding Rates"
type: concept
created: 2026-04-07
updated: 2026-07-19
status: good
tags: [crypto, perpetual-futures, market-microstructure]
aliases: ["Funding Rate", "Perp Funding"]
domain: [market-microstructure, crypto]
prerequisites: ["[[perpetual-futures]]", "[[futures]]"]
difficulty: intermediate
related: ["[[perpetual-futures]]", "[[funding-rate-arbitrage]]", "[[binance]]", "[[basis-trading]]", "[[crypto-overview]]", "[[cryptodataapi]]"]
---

Funding rates are periodic payments exchanged between holders of long and short positions in [[perpetual-futures|perpetual futures]] contracts. They serve as the mechanism that anchors perpetual futures prices to the underlying [[spot-trading|spot]] price, replacing the expiration-based convergence used by traditional [[futures|futures contracts]].

## How Funding Works

Unlike traditional futures that converge to spot at expiration, perpetual futures never expire. Funding rates create an economic incentive for the perp price to track spot:

- **Positive funding rate**: The perp trades above spot (contango). Longs pay shorts. This discourages further long positions and incentivizes shorting, pushing the perp price down toward spot.
- **Negative funding rate**: The perp trades below spot (backwardation). Shorts pay longs. This discourages further shorting and incentivizes going long, pushing the perp price up toward spot.

## Calculation

Most exchanges (including [[binance|Binance]], [[bybit|Bybit]], and [[dydx|dYdX]]) settle funding every **8 hours** (00:00, 08:00, 16:00 UTC). The funding rate is typically composed of two components:

1. **Interest rate component**: A fixed rate representing the cost of borrowing the base vs. quote currency (usually small, ~0.01% per 8 hours)
2. **Premium/discount component**: Based on the difference between the perp price and the spot index price

**Annualized funding** = 8-hour rate x 3 x 365. A 0.01% per-8-hour rate annualizes to approximately 10.95%.

## Trading Applications

### Funding Rate Arbitrage
[[funding-rate-arbitrage|Funding rate arbitrage]] is a market-neutral strategy: go long spot and short the perpetual (or vice versa) to collect funding payments while maintaining delta neutrality. During bull markets, annualized funding yields can exceed 30-50%.

### Sentiment Indicator
Funding rates serve as a real-time measure of market [[sentiment-analysis|sentiment]] and positioning:
- **Elevated positive funding** (>0.05% per 8hr): Excessive bullish leverage -- historically precedes corrections
- **Deeply negative funding** (<-0.03% per 8hr): Excessive bearish leverage -- often marks local bottoms
- **Neutral funding** (~0.01%): Balanced positioning

### Carry Trade
Traders can systematically harvest funding by taking the paying side. When funding is persistently positive, shorting the perp while holding spot generates consistent yield.

## Risks

- **Funding rate reversals**: Rates can flip direction rapidly during volatile markets, turning a profitable carry trade into a losing position
- **Exchange risk**: Funding is paid/received on centralized exchanges, exposing traders to [[counterparty-risk|counterparty risk]]
- **Liquidation risk**: Leveraged positions can be liquidated before funding is collected
- **Opportunity cost**: Capital locked in funding arbitrage cannot be deployed elsewhere

## Historical Context

Funding rates were popularized by [[bitmex|BitMEX]] when it launched the first perpetual swap (XBTUSD) in 2016. The mechanism was so successful that virtually every crypto [[derivatives]] exchange adopted it. During the 2021 bull market, [[bitcoin|BTC]] funding rates regularly exceeded 0.1% per 8 hours (annualized ~36%), creating massive arbitrage opportunities.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding rates (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange open interest
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=BTC` — all-in-one derivatives overview (markdown format available)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding-rate history
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI, long/short)
- `GET /api/v1/backtesting/funding` — deep funding archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Fetch** — `GET /api/v1/derivatives/funding-rates?coin=BTC` for the live cross-exchange read (exposed as the `get_funding_rates` MCP tool); `GET /api/v1/derivatives/summary?coin=BTC` bundles funding, OI, and long/short in one call
- **Signal** — annualize the 8-hour prints (rate × 3 × 365) and z-score against a trailing window rather than using raw absolute thresholds; extremes are regime-dependent
- **Backtest** — `GET /api/v1/backtesting/funding` — Hyperliquid hourly funding since 2023-05; Binance daily funding (with mark price + OI) only since 2026-03-30
- **Tip** — before fading extreme funding, confirm crowding with `GET /api/v1/derivatives/binance/long-short-ratio`; funding alone flips sign quickly, but funding plus a stretched account L/S ratio is the persistent one-sided-positioning read

## Related

- [[perpetual-futures]] -- The instrument that uses funding rates
- [[funding-rate-arbitrage]] -- Strategy to profit from persistent funding
- [[basis-trading]] -- Related concept in traditional futures markets
- [[binance]] -- Largest perpetual futures exchange by volume

## Sources

- Funding rate mechanics are documented across exchange documentation and crypto [[market-microstructure]] literature
