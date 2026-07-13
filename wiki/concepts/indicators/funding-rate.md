---
title: "Funding Rate"
type: concept
created: 2026-04-06
updated: 2026-07-13
status: good
confidence: medium
tags: [derivatives, crypto, funding-rate, perpetual-futures]
aliases: ["Funding", "Perp Funding", "Funding Payment", "Funding Rate"]
domain: [derivatives, market-microstructure]
prerequisites: ["[[perpetual-futures]]"]
difficulty: intermediate
related: ["[[perpetual-futures]]", "[[open-interest]]", "[[arbitrage]]", "[[market-microstructure]]", "[[cryptodataapi]]"]
---

# Funding Rate

The **funding rate** is a periodic payment exchanged between long and short holders of [[perpetual-futures]] contracts. It is the primary mechanism that keeps the perp price anchored to the underlying [[spot-price]], solving the fundamental problem of how a contract with no expiry date can track its reference asset.

## Why Funding Exists

Traditional [[futures]] converge to [[spot-price]] at expiry through settlement. [[perpetual-futures]] have no expiry, so they need a different convergence mechanism. The funding rate creates an economic incentive:

- When the perp trades at a **premium** to spot, longs pay shorts, discouraging further buying.
- When the perp trades at a **discount** to spot, shorts pay longs, discouraging further shorting.

This self-correcting mechanism is one of the most elegant designs in crypto [[market-microstructure]].

## How Funding Is Calculated

The funding rate has two components. The **interest rate component** is a fixed baseline, usually **0.01% per 8-hour period** (~10.95%/year). The **premium/discount component** is variable, based on price deviation between perp and spot index:

```
Premium Index = (Max(0, Impact Bid - Index) - Max(0, Index - Impact Ask)) / Index Price
Funding Rate = Avg Premium Index + clamp(Interest Rate - Avg Premium Index, -0.05%, 0.05%)
Funding Payment = Position Size x Funding Rate
```

If a trader holds a $100,000 long position and the funding rate is 0.01%, they pay **$10** to shorts per interval.

## Payment Intervals

| Exchange | Interval | Periods/Day |
|----------|----------|-------------|
| [[binance]], Bybit, OKX | 8 hours | 3 |
| [[dydx]], [[hyperliquid]] | 1 hour | 24 |

[[hyperliquid]] and [[dydx]] use hourly funding for more granular price convergence. Each payment is smaller but compounds more frequently.

## Interpreting Funding Rates

| Funding Rate (8h) | Interpretation | Annualized |
|-------------------|----------------|------------|
| 0.0100% | Neutral / baseline | ~10.95% |
| 0.0200% | Mildly elevated, moderate long bias | ~21.9% |
| 0.0500% | Elevated, strong long bias | ~54.75% |
| 0.1000%+ | Extreme, euphoric longs | ~109.5%+ |
| -0.0500% | Strong short bias / fear | ~-54.75% |

**Positive funding** (longs pay shorts) indicates perp price above spot -- bullish [[sentiment]], crowded longs. **Negative funding** (shorts pay longs) indicates perp price below spot -- bearish [[sentiment]] or hedging activity.

## Live Market Data

Current funding rates on [[hyperliquid]] (hourly interval):

| Asset | Funding Rate (1h) | Approx. 8h Equiv. | Signal |
|-------|-------------------|-------------------|--------|
| BTC | 0.000655% | ~0.00524% | Below neutral -- slightly bearish lean |
| ETH | 0.00125% | ~0.01% | Roughly neutral |
| FARTCOIN | 0.00738% | ~0.059% | Elevated -- strong long bias |

The FARTCOIN rate is notably high, indicating aggressive long positioning on that memecoin. Traders holding long positions are paying a significant premium, suggesting crowded bullish [[sentiment]] vulnerable to sharp unwinds. See [[liquidation]].

## Funding Rate Arbitrage

A popular [[arbitrage]] strategy captures funding payments through a delta-neutral position: **short** the perp with high positive funding, **buy** the equivalent on [[spot-markets]], and **collect** funding as the short receives payments from longs. Close both when funding normalizes.

**Risks**: [[liquidation]] if the perp surges before the spot hedge offsets losses, execution [[slippage]], funding rate reversal, and counterparty/smart contract risk.

## Historical Extremes and Sentiment

Funding rates have reached extraordinary levels: during 2021 bull markets, BTC funding exceeded 0.1% per 8h (100%+ annualized). During crashes (May 2021, FTX collapse Nov 2022), funding went deeply negative (-0.1% to -0.3% per 8h).

Many traders use funding as a contrarian [[sentiment]] indicator: extremely positive funding often precedes corrections (overleveraged longs vulnerable to [[liquidation]] cascades), while extremely negative funding can signal bottoms. Divergence between funding and price can signal weakening [[momentum]].

## Common Misconceptions

1. **"Funding is a fee paid to the exchange"** -- It is a peer-to-peer payment between longs and shorts. The exchange takes no cut.
2. **"Positive funding means the market will go down"** -- Mildly positive funding is normal in a healthy uptrend. Only extremes signal overextension.
3. **"You only pay if you hold at the snapshot"** -- True on most exchanges, creating predictable micro-patterns in [[order-flow]] around funding timestamps.
4. **"Funding is the same across exchanges"** -- Rates vary significantly across venues, creating [[arbitrage]] opportunities.
5. **"Low funding means low risk"** -- Neutral funding says nothing about directional risk. Positions can still lose heavily from adverse price movement.

## Further Reading

- [[derivatives-native-regime]] -- funding extremes as a tradeable regime state
- [[basis-carry-regime]] -- funding/basis health as a fragility gauge
- [[crypto-market-regime-taxonomy]] -- the 14-basket crypto regime framework
- [[perpetual-futures]] -- The instrument that uses funding rates
- [[open-interest]] -- Related metric for gauging market positioning
- [[arbitrage]] -- Strategies exploiting funding rate differentials
- [[market-microstructure]] -- Broader context for price mechanisms
- [[liquidation]] -- What happens when leveraged positions fail

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
