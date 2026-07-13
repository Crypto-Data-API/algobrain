---
title: "Execution Sequencing"
type: concept
created: 2026-04-20
updated: 2026-04-20
status: good
tags: [market-microstructure, execution, arbitrage, algorithmic]
aliases: ["Execution Sequencing", "Order Sequencing", "Multi-Leg Execution"]
domain: [market-microstructure]
prerequisites: ["[[order-types]]", "[[leg-risk]]", "[[slippage]]"]
difficulty: advanced
related: ["[[leg-risk]]", "[[cross-exchange-arbitrage]]", "[[triangular-arbitrage]]", "[[pairs-trading]]", "[[transaction-costs]]", "[[market-impact]]", "[[order-management-systems]]", "[[arbitrage-parameter-cheatsheet]]"]
---

# Execution Sequencing

Execution sequencing is the discipline of determining **which leg to execute first, with what order type, and how to handle partial fills and failures** in multi-leg arbitrage trades. While [[leg-risk]] describes what can go wrong, execution sequencing describes how to minimize it through systematic order management.

## Core Principle: Hardest Leg First

The universal rule of multi-leg execution: **execute the most uncertain, least liquid, or hardest-to-fill leg first.** Only commit to the easy leg after the hard leg confirms.

This asymmetry is the foundation of all arb execution. The easy leg (selling BTC on Binance, buying a liquid large-cap) is always available. The hard leg (borrowing a hard-to-borrow stock, filling on an illiquid DEX, getting a fill on a thinly-traded options contract) may not be.

## Sequencing Templates by Strategy

### Cross-Exchange Arbitrage (2 Legs, Speed-Critical)

```
1. DETECT: Spread exceeds min_threshold on both order books
2. VALIDATE: Check depth ≥ min_depth on both sides
3. LEG 1 (taker): IOC order on ILLIQUID venue at limit = current best price - slippage_buffer
4. CONFIRM: Wait for fill confirmation (timeout: 2 seconds)
   - Full fill → proceed to LEG 2
   - Partial fill → proceed to LEG 2 with adjusted size matching partial
   - No fill → abort, no exposure
5. LEG 2 (taker): IOC order on LIQUID venue at limit = current best price + slippage_buffer
6. CONFIRM: Wait for fill confirmation (timeout: 2 seconds)
   - Full fill → SUCCESS, log and monitor
   - Partial fill → PROBLEM, attempt fill remainder with wider limit
   - No fill → EMERGENCY, unwind LEG 1 at market
7. RECONCILE: Verify both legs balance in notional within 2% tolerance
```

**Why illiquid first:** If the illiquid leg fails, you have zero exposure. If the liquid leg failed, you'd be stranded on the illiquid venue where unwinding is expensive.

### Triangular Arbitrage (3 Legs, Ultra-Speed-Critical)

```
1. DETECT: Circular profit > min_threshold across A→B→C→A
2. EXECUTE ALL THREE simultaneously as IOC orders
   - This is NOT sequential — all three legs fire at once
   - Any unfilled leg creates directional exposure in 2 currencies
3. RECONCILE (within 500ms):
   - All 3 filled → SUCCESS
   - 2 of 3 filled → HEDGE: convert stranded currency via 4th trade (accepting loss)
   - 1 of 3 filled → UNWIND: reverse the single filled leg immediately
   - 0 of 3 filled → no exposure, monitor for next opportunity
```

**Why simultaneous:** With 3 legs and sub-second windows, sequential execution virtually guarantees the last leg sees a different price. Fire all at once and handle mismatches.

### Pairs Trading (2 Legs, Minutes-Tolerant)

```
1. SIGNAL: Z-score crosses entry threshold (|z| > 2.0)
2. LEG 1 (hard): SHORT leg
   a. Check borrow availability and rate
   b. If hard-to-borrow (HTB): locate borrow first, then short
   c. Use LIMIT order, work the order over 1-5 minutes
   d. If borrow unavailable → ABORT entire trade
3. LEG 2 (easy): LONG leg
   a. Execute only after LEG 1 fill confirmed
   b. Match notional to LEG 1 × hedge_ratio
   c. LIMIT order, work over 1-5 minutes
4. VERIFY: Net beta exposure ≈ 0, sector exposure ≈ 0
```

**Why short first:** Borrow availability is the binding constraint. Long positions are always available. If borrow dries up mid-trade, you don't want to be stuck long-only.

### Merger Arbitrage (2 Legs, Hours-Tolerant)

```
1. SIGNAL: Deal announced, spread > min_threshold
2. LEG 1 (hard): SHORT acquirer (for stock deals)
   a. Locate borrow, confirm rate is acceptable
   b. Enter short at or near current price
   c. Size based on deal exchange ratio
3. LEG 2 (easy): LONG target
   a. Buy target shares at current market price
   b. Size = acquirer_short_shares / exchange_ratio
4. MONITOR: Track deal progress daily
5. EXIT: Close both legs on deal close date or if deal breaks
```

### Volatility Arbitrage (2+ Legs, Delta-Hedge Ongoing)

```
1. SIGNAL: IV-RV spread exceeds threshold
2. LEG 1: Options position (buy/sell straddle or strangle)
   a. LIMIT orders on options — wide bid-ask requires patience
   b. May take minutes to hours to fill in illiquid names
3. LEG 2: Delta hedge with underlying
   a. Execute AFTER options fill confirmed
   b. Calculate delta from filled strikes and quantities
   c. Use MARKET or IOC on liquid underlying
4. ONGOING: Re-hedge delta daily or when |delta| > threshold
   - Each re-hedge is a mini execution event with its own cost
```

## Partial Fill Management

Partial fills are inevitable in arbitrage. The system must handle four scenarios:

### Scenario 1: First Leg Partially Fills

**Action:** Proceed with second leg sized to match the partial fill.
```
leg_2_size = leg_1_filled_quantity × hedge_ratio
```
The unfilled portion of leg 1 is simply abandoned (IOC handles this automatically). You have a smaller but properly hedged position.

### Scenario 2: Second Leg Partially Fills

**Action:** Unbalanced position. Three options:
1. **Retry:** Send another order for the unfilled portion with a more aggressive price
2. **Reduce leg 1:** Unwind part of leg 1 to match leg 2's fill
3. **Accept imbalance:** If imbalance is < 5% of total notional, accept and monitor

**Decision tree:**
```
if unfilled_pct < 5%:
    accept imbalance, monitor
elif unfilled_pct < 20%:
    retry with 2× slippage tolerance
else:
    unwind leg 1 to match, or unwind everything
```

### Scenario 3: Fill Price Worse Than Expected

**Action:** Recalculate expected P&L with actual fill prices. If P&L is still positive, proceed. If negative, consider unwinding immediately rather than hoping the spread converges.

### Scenario 4: Fill Arrives After Timeout

**Action:** Late fills are dangerous — you may have already initiated unwind logic. The system must track fill states and prevent double-execution:
```
states: PENDING → FILLED | TIMEOUT | PARTIALLY_FILLED
if state == TIMEOUT and late_fill_arrives:
    if unwind_already_executed:
        close late fill immediately (you have accidental double exposure)
    else:
        proceed as if normal fill
```

## Order Type Decision Matrix

| Situation | Recommended Order Type | Why |
|---|---|---|
| Taker leg, speed-critical | IOC with price limit | Fills immediately or cancels; limit prevents slippage beyond threshold |
| Maker leg, cost-critical | LIMIT_MAKER or POST_ONLY | Guarantees maker fee (rebate on some venues) |
| All-or-nothing requirement | FOK | Prevents partial fills entirely — useful when partial creates unacceptable imbalance |
| Patient entry (pairs, vol arb) | LIMIT (GTC) with timer | Work the order; cancel if not filled within time window |
| Emergency unwind | IOC with wide limit (or MARKET as last resort) | Priority is speed of exit, not price optimization |
| On-chain (DEX) | Swap with slippage tolerance | Set max slippage; transaction reverts if exceeded |

## Concurrency and Race Conditions

Multi-leg arb systems must handle concurrent execution carefully:

### The Double-Execution Problem
If two arb opportunities trigger simultaneously and share a leg (e.g., both use BTC on Binance), the system may overcommit capital. Solution: maintain a **position lock** per venue per asset. Only one arb can claim a venue's capital at a time.

### The Stale Price Problem
WebSocket feeds update at different speeds. Exchange A's price may be 200ms newer than exchange B's. An apparent arb may be a stale-price artifact. Solution: timestamp all prices and reject arb signals where any price is older than a **staleness threshold** (typically 500ms-2s depending on strategy speed).

### The Order ID Tracking Problem
When orders fly across multiple venues, tracking which order belongs to which arb attempt requires a robust **order ID mapping system**. Every order must tag: arb_id, leg_number, venue, timestamp, expected_fill, actual_fill, status.

## Performance Monitoring

Track these metrics to evaluate execution quality:

| Metric | Formula | Target |
|---|---|---|
| **Implementation shortfall** | Expected P&L - Actual P&L | < 20% of gross spread |
| **Fill ratio** | Filled quantity / Attempted quantity | > 95% |
| **Bilateral completion rate** | Both-legs-filled / Attempted arbs | > 90% |
| **Average slippage** | |Actual price - Expected price| / Expected price | < 0.02% (liquid pairs) |
| **Unwind loss rate** | Losses from stranded-leg unwinds / Total P&L | < 10% of gross P&L |
| **Time to completion** | Last fill timestamp - Detection timestamp | < 500ms (speed arb), < 5min (stat arb) |

## Sources

- [[leg-risk]]
- [[arbitrage-overview]]
- [[cross-exchange-arbitrage]]
- [[transaction-costs]]
- [[order-management-systems]]
- [[slippage]]
