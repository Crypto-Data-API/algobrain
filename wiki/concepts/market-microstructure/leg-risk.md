---
title: "Leg Risk"
type: concept
created: 2026-04-20
updated: 2026-04-20
status: good
tags: [market-microstructure, execution, arbitrage, risk-management]
aliases: ["Leg Risk", "Legging Risk", "Execution Risk"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[order-types]]", "[[slippage]]", "[[arbitrage]]"]
difficulty: intermediate
related: ["[[execution-sequencing]]", "[[cross-exchange-arbitrage]]", "[[triangular-arbitrage]]", "[[pairs-trading]]", "[[merger-arbitrage]]", "[[transaction-costs]]", "[[slippage]]", "[[market-impact]]", "[[arbitrage-parameter-cheatsheet]]"]
---

# Leg Risk

Leg risk is the risk that one side ("leg") of a multi-leg trade executes while the other side fails, leaving the trader with an unhedged directional position instead of the intended arbitrage or spread. It is the **single largest operational risk in arbitrage trading** and the primary reason that "risk-free" arbitrage is never truly risk-free in practice.

A [[cross-exchange-arbitrage]] trade has two legs (buy on exchange A, sell on exchange B). A [[triangular-arbitrage]] trade has three. A [[dispersion-trading|dispersion trade]] can have 20+. Every additional leg multiplies the probability that something goes wrong.

## Why Legs Fail

### 1. Price Movement During Execution

The spread that triggered the trade may vanish between the time you detect it and the time your second leg fills. At 50ms latency per exchange, a round-trip takes 100ms+ — during which another arbitrageur or market maker may have moved the price.

**Impact:** The "arb" becomes a directional bet. If you bought on exchange A but the sell price on exchange B has dropped, you hold inventory at a loss.

### 2. Insufficient Liquidity

The order book showed $50,000 of depth at your target price, but by the time your order arrives, other takers have consumed the liquidity. Your order partially fills or fills at a worse price ([[slippage]]).

**Impact:** Partial fills create unbalanced positions. You may be long 1.5 BTC on exchange A but only short 0.8 BTC on exchange B.

### 3. Exchange Downtime or API Failure

Exchanges go offline, API endpoints return errors, WebSocket connections drop, or rate limits trigger. Crypto exchanges have historically experienced outages during high-volatility periods — exactly when arbitrage opportunities are largest.

**Impact:** One leg is open with no ability to close or hedge on the other venue. You're exposed to directional risk until the exchange recovers.

### 4. Rejection or Throttling

Order rejected due to: insufficient margin, position limit reached, self-trade prevention, maintenance mode, or the exchange's risk engine throttling during volatility.

**Impact:** Same as API failure — stranded leg.

### 5. Network Congestion (Crypto-Specific)

On-chain legs (DEX trades, bridge transfers) can fail or delay due to blockchain congestion, gas price spikes, or mempool congestion. Ethereum mainnet transactions can take 12 seconds to 10+ minutes during peak congestion.

**Impact:** For [[cross-chain-arbitrage]] or [[flash-loan-arbitrage]], a delayed bridge can expose you to price movement for minutes or hours.

### 6. Partial Fills

Market orders may fill partially if the order book is thin. Limit orders may never fill at all if the price moves away. This leaves you with a smaller position than intended on one side, creating a net directional exposure proportional to the fill imbalance.

## Measuring Leg Risk

### Fill Rate Metrics

| Metric | Definition | Target |
|---|---|---|
| **Bilateral fill rate** | % of arb attempts where both legs fill completely | > 90% |
| **Partial fill rate** | % of attempts with at least one partial fill | < 20% |
| **Stranded leg rate** | % of attempts where one leg fills, other fails entirely | < 2% |
| **Average fill time** | Time from first leg submission to last leg confirmation | < 500ms (same venue), < 2s (cross-venue) |
| **Slippage per leg** | Actual fill price vs. expected price | < 0.02% (liquid pairs) |

### Dollar Exposure from Leg Failure

```
max_loss = position_size × expected_price_move_during_recovery_time
```

Example: You bought 10 BTC ($672,000) on Binance but the Coinbase sell leg failed. If BTC moves 1% in 5 minutes while you scramble to exit, potential loss = $6,720. This is why position sizing relative to recovery time matters.

## Mitigation Strategies

### 1. Execute the Illiquid Leg First

**Rule:** Always execute the harder, less liquid, or more uncertain leg first. Only execute the easy leg after the hard leg confirms.

| Strategy | Execute First | Execute Second |
|---|---|---|
| [[cross-exchange-arbitrage]] | Illiquid exchange (thinner book) | Liquid exchange (Binance) |
| [[merger-arbitrage]] | Short acquirer (borrow may fail) | Long target (always fillable) |
| [[pairs-trading]] | Short leg (borrow availability uncertain) | Long leg |
| [[convertible-arbitrage]] | Long convert (illiquid OTC) | Short equity (liquid) |
| [[cross-chain-arbitrage]] | Bridge transaction (slow, uncertain) | DEX swap (fast, atomic) |

### 2. Use Appropriate Order Types

| Order Type | When to Use | Leg Risk Implication |
|---|---|---|
| **IOC (Immediate-or-Cancel)** | Taker leg on liquid venues | Fills what's available, cancels rest — prevents stale orders |
| **FOK (Fill-or-Kill)** | When partial fills are unacceptable | Either full fill or no fill — prevents imbalance |
| **LIMIT_MAKER** | When you want guaranteed maker fee | Rejected if would immediately fill — use on patient leg |
| **MARKET** | Never recommended for arb | Unlimited slippage; use IOC with a price limit instead |
| **LIMIT (GTC)** | Patient leg in slower arbs (merger arb) | Risk of stale orders; set time limits |

### 3. Atomic Execution (Where Possible)

Some venues support atomic multi-leg execution:
- **DEX flash loans:** All legs execute in a single blockchain transaction or revert entirely. Zero leg risk. See [[flash-loan-arbitrage]]
- **Exchange batch orders:** Some exchanges support multi-order submission. Not atomic, but reduces timing gap
- **Smart order routers:** Route to multiple venues simultaneously

### 4. Pre-Position Capital on Both Venues

For [[cross-exchange-arbitrage]], eliminate transfer delays by maintaining capital on both exchanges. Execute buy and sell simultaneously without moving funds. Rebalance periodically (daily/weekly) when no arb is active.

This eliminates withdrawal time as a leg risk factor but introduces [[counterparty-risk]] from holding capital on multiple venues. See [[multi-venue-capital-management]].

### 5. Timeout and Auto-Unwind

Every arb bot must have an **automatic unwind** procedure for stranded legs:

```
if leg_1 filled AND leg_2 not filled within TIMEOUT:
    attempt leg_2 with aggressive pricing (taker, wider limit)
    if still not filled within EMERGENCY_TIMEOUT:
        unwind leg_1 at market
        log failure, pause strategy, alert
```

**Recommended timeouts:**
- Cross-exchange arb: 2-5 seconds (initial), 10-30 seconds (emergency)
- Triangular arb: 500ms (initial), 2 seconds (emergency)
- Pairs trading: 30 seconds (initial), 5 minutes (emergency)
- Merger arb: 1-5 minutes (initial), end of day (emergency)

### 6. Position Size Relative to Recovery Time

Size positions so that the maximum expected adverse move during the recovery window is within your risk budget:

```
max_position = risk_budget / (volatility × sqrt(recovery_time_in_days))
```

For a $100,000 arb portfolio with 1% risk budget per trade, and BTC annualized vol of 60%:
- 30-second recovery: max position ≈ $100,000 × 0.01 / (0.60 × sqrt(30/86400/365)) ≈ very large (vol is negligible over seconds)
- 10-minute recovery: max position starts to matter for volatile assets
- 1-hour recovery (bridge delay): position must be significantly smaller

### 7. Hedging Stranded Legs

If a leg is stranded and the unwind will take time, consider an **interim hedge** on a third venue:
- Stranded long BTC on Binance? Short BTC perps on Hyperliquid as interim hedge while resolving the Coinbase issue
- This converts leg risk into [[basis-risk]] (spot-perp basis) which is smaller than outright directional risk

## Leg Risk by Strategy Type

| Strategy | Number of Legs | Leg Risk Severity | Primary Failure Mode |
|---|---|---|---|
| [[cross-exchange-arbitrage]] | 2 | High | API failure, price movement |
| [[triangular-arbitrage]] | 3 | Very High | Speed — any leg delay kills the trade |
| [[funding-rate-arbitrage]] | 2 | Low | Legs execute independently; no timing pressure |
| [[cash-and-carry]] | 2 | Low | Same as funding rate — no speed requirement |
| [[pairs-trading]] | 2 | Medium | Borrow availability for short leg |
| [[merger-arbitrage]] | 2 | Medium | Borrow availability, deal terms change |
| [[dispersion-trading]] | 10-20+ | Very High | Partial fills across many names |
| [[flash-loan-arbitrage]] | 2-5 | Zero | Atomic — reverts if any leg fails |
| [[cross-chain-arbitrage]] | 2-3 | Very High | Bridge delays, chain congestion |
| [[volatility-arbitrage]] | 2+ | Medium | Options liquidity, wide spreads |

## Historical Leg Risk Failures

- **Knight Capital (2012):** A software bug caused one leg of the firm's market-making system to send orders without proper cancellation logic. Lost $440 million in 45 minutes from runaway unhedged positions
- **Flash crashes:** During the 2010 and 2015 flash crashes, many arb bots stopped quoting because one leg's exchange halted or quote feeds lagged, leaving stranded positions on the other side
- **FTX collapse (2022):** Arbitrageurs with capital on FTX lost their entire exchange-side leg when withdrawals were frozen. Pre-positioned capital became [[counterparty-risk]]

## Sources

- [[arbitrage-overview]]
- [[cross-exchange-arbitrage]]
- [[transaction-costs]]
- [[failure-modes]]
- [[counterparty-risk]]
- [[slippage]]
