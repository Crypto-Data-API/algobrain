---
title: "Arbitrage Backtesting Guide"
type: strategy
created: 2026-04-21
updated: 2026-07-13
status: excellent
tags: [arbitrage, backtesting, quantitative, strategy-development]
aliases: ["Arb Backtesting", "Multi-Leg Backtesting", "Arbitrage Simulation"]
strategy_type: quantitative
timeframe: scalp|intraday|swing|position
markets: [crypto, stocks, futures, options]
complexity: advanced
backtest_status: untested
related: ["[[backtesting-overview]]", "[[transaction-cost-modeling]]", "[[walk-forward-analysis]]", "[[arbitrage-overview]]", "[[arbitrage-parameter-cheatsheet]]", "[[historical-spread-data]]", "[[leg-risk]]", "[[execution-sequencing]]", "[[data-snooping-and-p-hacking]]", "[[overfitting-detection]]", "[[cryptodataapi]]"]
---

# Arbitrage Backtesting Guide

Standard [[backtesting-overview|backtesting methodology]] assumes single-instrument, single-venue execution. Arbitrage strategies violate every one of these assumptions: they involve **multiple legs, multiple venues, simultaneous execution, and cost structures that depend on the interaction between legs.** A naive backtest that ignores these realities overstates arb returns by 50-200%.

This page covers what makes arb backtesting different and how to do it honestly. It is the arbitrage-specific companion to the general [[backtesting-overview]], [[transaction-cost-modeling]], and [[walk-forward-analysis]] pages — read those first for the universal machinery, then return here for what breaks when you go multi-leg.

## Why arbitrage backtests overstate so badly

A single-instrument momentum backtest that ignores costs overstates returns by perhaps 10-30%. An arbitrage backtest that ignores the realities below overstates by **50-200%** because arb edges live *inside* the cost structure: the gross spread is often the same order of magnitude as the round-trip cost, so small modeling errors flip the sign of the result. The smaller and tighter the spread you are harvesting, the more lethal each unmodeled basis point becomes. This is the practical face of [[limits-to-arbitrage]]: the reason a spread survives is usually that it is barely profitable after honest costs.

## The Seven Deadly Sins — summary

| # | Sin | Naive assumption | Honest correction | Typical overstatement |
|---|---|---|---|---|
| 1 | Mid-price fills | Trade at the mid | Cross the spread (bid/ask) on the taker leg | 0.02-0.50%+ per round trip |
| 2 | Zero inter-leg latency | Both legs at same timestamp | Price leg 2 at `t + latency` | 0.01-0.05%+ in trends, more in vol |
| 3 | Full fills | Entire order at top of book | Walk the [[order-book]] depth | Up to the entire spread on large orders |
| 4 | No failed trades | 100% both-legs-fill | Model [[leg-risk\|leg-failure]] + unwind cost | 15-30% of P&L for HFT arb |
| 5 | Static fees | Today's schedule for all history | Point-in-time fee schedule | Varies; large for multi-year tests |
| 6 | Continuous funding | Smooth funding accrual | Discrete settlement timestamps | Whole-period miss on timing |
| 7 | Survivorship of venues | Use today's exchanges | Only venues live in-period | Fictional results (FTX, Hyperliquid) |

## The Seven Deadly Sins of Arb Backtesting

### Sin 1: Mid-Price Fills

**What it is:** Assuming you can buy and sell at the mid-price (average of bid and ask).

**Why it's wrong:** In arbitrage, you're typically a **taker** on at least one leg — you cross the spread. For a cross-exchange arb: you hit the ask on the buy side and hit the bid on the sell side. The mid-to-mid spread is always wider than the bid-ask spread.

**Correction:**
```python
# WRONG: Mid-price backtest
spread = exchange_B_mid - exchange_A_mid

# RIGHT: Bid-ask backtest
spread = exchange_B_bid - exchange_A_ask  # Net of crossing both spreads
```

**Impact:** On liquid pairs (BTC/USDT), mid-to-mid overestimates by ~0.02-0.05%. On illiquid pairs, by 0.10-0.50%+.

### Sin 2: Ignoring Latency Between Legs

**What it is:** Assuming both legs execute at the same timestamp.

**Why it's wrong:** Even with WebSocket feeds, there is a 10-500ms gap between detecting the opportunity and executing both legs. During this time, the other side's price moves.

**Correction:**
```python
# Add latency simulation
LATENCY_MS = 100  # Typical API-to-API latency

# Leg 1 fills at t=0, Leg 2 fills at t=LATENCY_MS
# Use the price at t+LATENCY_MS for Leg 2, not t=0
leg_2_price = get_price_at(timestamp + timedelta(milliseconds=LATENCY_MS))
```

**Impact:** In trending markets, 100ms of latency costs 0.01-0.05% on liquid pairs. In volatile moments (the exact times arbs appear), it costs more.

### Sin 3: Assuming Full Fills

**What it is:** Assuming your entire order fills at the quoted price.

**Why it's wrong:** Order books have limited depth. A 10 BTC market order on an exchange with 2 BTC at the best price will eat through multiple levels.

**Correction:**
```python
# Walk the order book to simulate fill
def simulate_fill(order_book_levels: list, size: float) -> float:
    """Returns average fill price given order book depth"""
    remaining = size
    total_cost = 0
    for price, qty in order_book_levels:
        fill_qty = min(remaining, qty)
        total_cost += fill_qty * price
        remaining -= fill_qty
        if remaining <= 0:
            break
    if remaining > 0:
        return None  # Not enough liquidity — trade cannot execute
    return total_cost / size
```

**Impact:** For orders > 10% of the quoted depth, slippage can consume the entire spread.

### Sin 4: Ignoring Failed Trades

**What it is:** Only counting successful arbs in the P&L, ignoring attempts that failed (one leg filled, other didn't).

**Why it's wrong:** [[leg-risk|Leg risk]] means some percentage of attempts will result in stranded legs that must be unwound at a loss. A backtest showing 100% success rate is lying.

**Correction:**
```python
# Simulate leg failure rate
LEG_FAILURE_RATE = 0.05  # 5% of arb attempts have a leg failure
UNWIND_COST_PCT = 0.10   # Average loss from unwinding a stranded leg (as % of position)

# In P&L calculation
successful_pnl = num_successful * avg_profit_per_arb
failed_pnl = num_attempts * LEG_FAILURE_RATE * avg_position_size * UNWIND_COST_PCT
net_pnl = successful_pnl - failed_pnl
```

**Impact:** At 5% failure rate and 0.10% unwind cost, leg failures reduce total P&L by 15-30% for high-frequency arbs.

### Sin 5: Static Fee Assumptions

**What it is:** Using today's fee schedule for the entire backtest period.

**Why it's wrong:** Exchanges change fee structures. Binance restructured tiers in 2023. Coinbase launched Advanced Trade in 2022 with different fees. Using 2026 fees for a 2022 backtest produces fiction.

**Correction:** Use the fee schedule that was in effect at each point in the backtest. If unavailable, use conservative (higher) estimates for historical periods.

### Sin 6: Ignoring Funding Rate Settlement Mechanics

**What it is:** For [[funding-rate-arbitrage]] backtests, using continuously compounding funding rate instead of discrete 8-hour settlements.

**Why it's wrong:** Funding is paid at settlement (every 8h on most exchanges, every 1h on Hyperliquid). If you enter 1 minute before settlement, you capture the full period's payment. If you enter 1 minute after, you wait 8 hours for the next one.

**Correction:**
```python
# Use discrete settlement timestamps
SETTLEMENT_TIMES = [0, 8, 16]  # Hours UTC (for 8h funding)

def funding_received(entry_time, exit_time, funding_rates: dict) -> float:
    """Calculate exact funding received based on settlement times"""
    total = 0
    for settlement_ts in all_settlements_between(entry_time, exit_time):
        rate = funding_rates.get(settlement_ts, 0)
        total += position_notional * rate
    return total
```

### Sin 7: Survivorship Bias in Exchange Selection

**What it is:** Backtesting on exchanges that exist today but didn't exist (or didn't have the same products) during the backtest period.

**Why it's wrong:** Hyperliquid launched in 2023. You can't backtest a 2021 Hyperliquid arb. FTX existed in 2021 but collapsed in 2022 — including FTX in a 2021 backtest and not modeling the collapse produces misleading results.

**Correction:** Only use venues that were operational during the backtest period. If modeling multi-year periods, account for exchange births, deaths, and product changes.

---

## Arb-Specific Backtest Framework (Python)

### Core Architecture

```python
"""arb_backtester.py — Multi-leg arbitrage backtest engine"""
import pandas as pd
import numpy as np
from dataclasses import dataclass

@dataclass
class ArbTrade:
    timestamp: pd.Timestamp
    strategy: str
    leg_1_venue: str
    leg_1_side: str     # "buy" or "sell"
    leg_1_price: float  # Actual fill price (not mid)
    leg_1_qty: float
    leg_1_fee: float
    leg_2_venue: str
    leg_2_side: str
    leg_2_price: float
    leg_2_qty: float
    leg_2_fee: float
    latency_ms: float
    success: bool       # Did both legs fill?
    unwind_cost: float  # If success=False, cost to unwind
    gross_pnl: float
    net_pnl: float

class ArbBacktester:
    def __init__(self, data: dict, fees: dict, latency_ms: float = 100):
        """
        data: {exchange_name: DataFrame with columns [timestamp, bid, ask, bid_size, ask_size]}
        fees: {exchange_name: {"maker": 0.0004, "taker": 0.0006}}
        latency_ms: simulated execution latency between legs
        """
        self.data = data
        self.fees = fees
        self.latency_ms = latency_ms
        self.trades = []

    def detect_spread(self, timestamp, symbol, buy_venue, sell_venue, min_spread):
        """Detect if an arbitrageable spread exists at given timestamp"""
        buy_data = self.data[buy_venue].loc[timestamp]
        sell_data = self.data[sell_venue].loc[timestamp]

        ask = buy_data["ask"]   # Price to buy (cross the ask)
        bid = sell_data["bid"]  # Price to sell (hit the bid)

        spread = (bid - ask) / ask

        buy_fee = self.fees[buy_venue]["taker"]
        sell_fee = self.fees[sell_venue]["taker"]
        net_spread = spread - buy_fee - sell_fee

        return net_spread if net_spread > min_spread else None

    def simulate_execution(self, timestamp, buy_venue, sell_venue, size):
        """Simulate multi-leg execution with latency and partial fills"""
        # Leg 1: Buy (executes immediately)
        leg_1_data = self.data[buy_venue].loc[timestamp]
        leg_1_price = leg_1_data["ask"]  # Taker: cross the ask
        leg_1_fill = min(size, leg_1_data["ask_size"])  # Partial fill possible

        # Leg 2: Sell (executes after latency)
        latency_offset = pd.Timedelta(milliseconds=self.latency_ms)
        leg_2_ts = timestamp + latency_offset
        # Find nearest available timestamp
        leg_2_data = self.data[sell_venue].iloc[
            self.data[sell_venue].index.get_indexer([leg_2_ts], method="nearest")[0]
        ]
        leg_2_price = leg_2_data["bid"]  # Taker: hit the bid
        leg_2_fill = min(leg_1_fill, leg_2_data["bid_size"])

        # Handle imbalance
        success = (leg_2_fill / leg_1_fill) > 0.95  # >95% fill = success
        actual_qty = min(leg_1_fill, leg_2_fill)

        gross_pnl = actual_qty * (leg_2_price - leg_1_price)
        fees = (actual_qty * leg_1_price * self.fees[buy_venue]["taker"] +
                actual_qty * leg_2_price * self.fees[sell_venue]["taker"])
        net_pnl = gross_pnl - fees

        if not success:
            # Unwind stranded portion
            stranded_qty = leg_1_fill - leg_2_fill
            unwind_cost = stranded_qty * leg_1_price * 0.001  # ~0.1% unwind penalty
            net_pnl -= unwind_cost
        else:
            unwind_cost = 0

        trade = ArbTrade(
            timestamp=timestamp, strategy="cross_exchange",
            leg_1_venue=buy_venue, leg_1_side="buy",
            leg_1_price=leg_1_price, leg_1_qty=leg_1_fill,
            leg_1_fee=actual_qty * leg_1_price * self.fees[buy_venue]["taker"],
            leg_2_venue=sell_venue, leg_2_side="sell",
            leg_2_price=leg_2_price, leg_2_qty=leg_2_fill,
            leg_2_fee=actual_qty * leg_2_price * self.fees[sell_venue]["taker"],
            latency_ms=self.latency_ms, success=success,
            unwind_cost=unwind_cost, gross_pnl=gross_pnl, net_pnl=net_pnl,
        )
        self.trades.append(trade)
        return trade
```

### Backtest Validation Checklist

After running any arb backtest, verify:

- [ ] **Bid-ask prices used** (not mid) for all fill simulations
- [ ] **Latency modeled** between legs (minimum 50ms for API-based, 12+ seconds for on-chain)
- [ ] **Partial fills simulated** using order book depth data
- [ ] **Leg failures included** in P&L (5-15% failure rate is realistic)
- [ ] **Fee schedule accurate** for the historical period being tested
- [ ] **Funding settlements discrete** (not continuously compounded)
- [ ] **Exchange availability verified** (venue existed during backtest period)
- [ ] **Walk-forward validated** (see [[walk-forward-analysis]]) — expect 30-50% Sharpe decay from in-sample
- [ ] **Multiple testing corrected** (see [[deflated-sharpe-ratio]]) if testing multiple parameter sets
- [ ] **Cost sensitivity plotted** — Sharpe vs. round-trip cost. At what cost does the strategy die?

---

## Data Requirements by Strategy

| Strategy | Minimum Data | Ideal Data | Source |
|---|---|---|---|
| [[cross-exchange-arbitrage]] | 1-second OHLCV per exchange | Tick-level order book (L2) per exchange, synchronized | [[historical-spread-data\|Tardis.dev]] |
| [[funding-rate-arbitrage]] | Settled funding rates per period + spot prices | Predicted + settled rates + perp mark prices | Coinglass, exchange APIs |
| [[pairs-trading]] | Daily close prices | Intraday (1-min) prices + bid-ask | [[paid-data-providers\|Polygon.io, Norgate]] |
| merger-arbitrage | Daily close prices + deal terms | Intraday + options chains + borrow rates | Bloomberg, SEC EDGAR |
| [[volatility-arbitrage]] | Daily IV surface + underlying price | Intraday IV + bid-ask by strike | ORATS, OptionMetrics |
| [[flash-loan-arbitrage]] | Pool reserves per block | Every swap event + pool state | Dune Analytics, archive node |

---

## The cost stack — what to subtract, by venue type

A round-trip arb cost is a *sum* of components, not a single number. Build the stack explicitly and subtract it from gross before reporting anything. See [[transaction-cost-modeling]] for the general model and [[fees]] for current schedules.

| Cost component | CEX crypto / equities | On-chain (DEX / [[flash-loan-arbitrage]]) | Notes |
|---|---|---|---|
| Maker/taker fee | Per-leg, per-venue schedule | Pool fee tier (e.g. 5/30/100 bps) | Use point-in-time, per-tier |
| Half-spread crossing | Bid-ask / 2 on each taker leg | Baked into AMM [[slippage]] curve | Sin 1 |
| [[market-impact]] / depth slippage | Walk the [[order-book]] | Convex AMM slippage (see [[slippage-optimal-pathfinding]]) | Sin 3 |
| Latency drift | Inter-leg price move | Block-time + reorg risk | Sin 2 |
| Leg-failure / unwind | [[leg-risk]] × unwind cost | Reverted-tx gas (paid even on failure) | Sin 4 |
| Funding / carry | [[funding-rate-arbitrage]] settlements, borrow | n/a (atomic) | Sin 6; also borrow on merger-arbitrage stock deals |
| Gas / priority fee | n/a | Base gas + validator capture (60-90%) | See [[slippage-optimal-pathfinding]] |
| Withdrawal / bridge | Inter-venue transfer + delay | Bridge fee + delay (cross-chain) | Opportunity cost of locked inventory |

The honest net spread is `gross_spread − Σ(applicable rows)`. If that is negative at realistic sizes, the strategy does not exist regardless of how good the gross chart looks — see the cost-sensitivity step below.

## Worked end-to-end methodology

A reproducible arb backtest, in order. Each step maps to a sin or a statistical-rigor concern.

1. **Assemble point-in-time data.** Synchronized L2 [[order-book]] (or pool reserves per block) for every venue, plus the fee schedule *as it existed* on each date (Sins 5, 7). Verify each venue/product actually traded on each date.
2. **Detect on executable prices.** Compute spreads from bid/ask (Sin 1), not mid. Require the spread to survive after subtracting the full cost stack above.
3. **Simulate fills against depth.** Walk the book/AMM curve for the intended size (Sin 3); record the size-dependent fill price, not the touch.
4. **Apply inter-leg latency.** Price the second (and later) legs at `t + latency` using the realistic figure for the venue class — 50ms+ for co-located API, 100-500ms for retail API, one block (~12s ETH L1) for on-chain (Sin 2).
5. **Model leg failure.** Apply a leg-failure rate and the cost of unwinding the stranded leg (Sin 4). Do not silently drop failed attempts.
6. **Apply discrete carry.** For [[funding-rate-arbitrage]] / [[cash-and-carry]], settle funding at exact timestamps (Sin 6); for merger-arbitrage add financing/borrow carry over the hold.
7. **Aggregate honestly.** Net P&L = successful net − failure costs − carry. Report the *net* equity curve only.
8. **Walk-forward validate.** Split into rolling in-sample/out-of-sample windows (see [[walk-forward-analysis]]); expect 30-50% Sharpe decay out-of-sample.
9. **Correct for multiple testing.** If you tried many parameter sets, deflate the Sharpe (see [[deflated-sharpe-ratio]] and [[data-snooping-and-p-hacking]]).
10. **Plot cost sensitivity.** Sharpe vs. round-trip cost in bps. The single most informative arb-backtest chart: it tells you the cost level at which the edge dies and therefore how much execution headroom you have.

## Statistical rigor for arb specifically

Arb strategies are unusually prone to false positives because they are searched combinatorially (many pairs × many venues × many parameters). Beyond the universal cautions in [[data-snooping-and-p-hacking]] and [[overfitting-detection]]:

| Pitfall | Why it bites arb | Mitigation |
|---|---|---|
| Multiple comparisons | Scanning N pairs/venues guarantees some look profitable by chance | [[deflated-sharpe-ratio]]; pre-register the candidate set |
| Cointegration instability | [[pairs-trading]] relationships break out-of-sample | Re-test cointegration walk-forward, not once |
| Cost realism flips sign | Tiny gross edge inverts after honest costs | Cost-sensitivity plot; conservative (high) historical fees |
| Crowding decay | Edge present in-sample, competed away live | Compare early vs. late sub-periods; expect monotone decay |
| Liquidity look-ahead | Sizing on depth you couldn't have known | Use only depth visible at decision time |

## Backtest-to-live reality gap

Even a clean backtest overstates live performance. Carry the standard arb haircuts from [[arbitrage-parameter-cheatsheet]]: assume **30-50% Sharpe degradation** from backtest to live, deploy at ~25% of target capital first, and recalibrate costs quarterly against realized fills. The backtest's job is not to predict returns — it is to *falsify* the strategy cheaply before risking capital, and to bound the cost level at which the edge disappears.

## Getting the Data (CryptoDataAPI)

**Historical archive:**
- `GET /api/v1/backtesting/klines` — OHLCV candle archive
- `GET /api/v1/backtesting/funding` — funding-rate archive
- `GET /api/v1/backtesting/liquidations` — liquidation records archive
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time daily snapshot
- `GET /api/v1/backtesting/archives` — Parquet dataset archive (since 2020)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/symbols"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-backtesting]].

## Related

- [[arbitrage]] · [[arbitrage-overview]] -- the strategy family being tested
- [[arbitrage-parameter-cheatsheet]] -- the thresholds these backtests validate
- [[backtesting-overview]] -- universal backtesting machinery
- [[transaction-cost-modeling]] · [[fees]] · [[slippage]] -- the cost stack
- [[walk-forward-analysis]] · [[deflated-sharpe-ratio]] -- out-of-sample rigor
- [[data-snooping-and-p-hacking]] · [[overfitting-detection]] -- false-positive control
- [[leg-risk]] · [[execution-sequencing]] -- the multi-leg failure modes
- [[historical-spread-data]] -- where to source synchronized data
- [[slippage-optimal-pathfinding]] -- on-chain fill/slippage modeling
- [[cross-exchange-arbitrage]] · [[funding-rate-arbitrage]] · [[pairs-trading]] · merger-arbitrage -- strategies with worked data requirements above
- [[limits-to-arbitrage]] -- why honest costs matter so much

## Sources

- Wiki cross-references: [[backtesting-overview]], [[transaction-cost-modeling]], [[walk-forward-analysis]], [[deflated-sharpe-ratio]], [[historical-spread-data]], [[data-snooping-and-p-hacking]], [[leg-risk]], [[arbitrage-parameter-cheatsheet]].
- General market knowledge; no specific wiki source ingested yet.
