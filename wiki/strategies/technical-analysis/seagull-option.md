---
title: "Seagull Option"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [options, seagull, hedging, directional, three-leg, low-cost, forex, corporate-hedging]
aliases: ["Seagull Spread", "Bullish Seagull", "Bearish Seagull"]
strategy_type: quantitative
timeframe: position
markets: [forex, stocks]
complexity: advanced
backtest_status: untested
related: ["[[risk-reversal]]", "[[iron-condor]]", "[[covered-call]]", "[[butterfly-spread]]", "[[implied-volatility]]", "[[delta]]", "[[collar]]"]
---

# Seagull Option

## Overview

The Seagull Option is a **three-leg** options strategy that provides **cheap directional protection** with an asymmetric payoff profile. The **bullish seagull** combines a call spread (buy lower call, sell higher call) with a short put, while the **bearish seagull** combines a put spread (buy higher put, sell lower put) with a short call. The premium collected from the short option finances part or all of the spread, often creating a **zero-cost or near-zero-cost** hedge with capped upside and significant downside exposure from the naked leg.

Seagulls are **extremely popular in [[forex]] corporate hedging** where companies need to protect against adverse currency moves without paying large premiums. The strategy extends the [[risk-reversal]] concept by capping the protective side (turning the long option into a spread), generating enough premium to make the structure cost-free. The tradeoff: protection is capped, and the short option creates risk in the opposite direction.

## Rules / Setup

### Entry
1. **Bullish seagull:** Buy 1 OTM call (strike A), sell 1 further OTM call (strike B), sell 1 OTM put (strike C). All same expiration.
2. **Bearish seagull:** Buy 1 OTM put (strike A), sell 1 further OTM put (strike B), sell 1 OTM call (strike C).
3. **Zero-cost structure:** Adjust the strikes so the credit from the short option equals the debit of the spread. The short put (or call) premium should approximately equal the call spread (or put spread) cost.
4. **Expiration:** 60-180 days for hedging; 30-60 DTE for speculative use.
5. **Strike selection:** In forex, strikes are typically set at key levels or at specific delta targets (e.g., 25-delta wings).

### Exit
1. **Hedging use:** Hold until the hedge is no longer needed (e.g., the currency exposure is realized).
2. **Speculative use:** Close at 50-75% of max profit if the underlying moves toward the long strike.
3. **Manage the naked leg:** If the short option is threatened, buy it back or roll it to limit losses.
4. **Spread cap reached:** If the underlying moves past the short leg of the spread, close to capture the capped gain.

### Position Sizing
In hedging contexts, size to match the exposure being hedged. For speculative use, size the naked leg as you would any naked option: max loss should represent no more than 3-5% of the account.

## Payoff Profile
- **Max profit:** Width of the spread (strike B - strike A). Capped when the underlying is beyond the short leg of the spread.
- **Max loss:** Short option strike x 100 minus any credit. Occurs if the underlying moves sharply through the naked leg.
- **Dead zone:** Between the naked short and the spread, all options expire worthless. P&L equals the net credit or debit.
- **Break-even:** For zero-cost entries, approximately at the long option strike.

## Example Trade
**Asset:** EUR/USD at 1.1000, 90 DTE. A European exporter hedges EUR appreciation with a bullish seagull:
1. **Buy 1 EUR/USD 1.1100 call** at 0.0080. **Sell 1 EUR/USD 1.1300 call** at 0.0030. **Sell 1 EUR/USD 1.0800 put** at 0.0050.
2. **Net cost:** 0.0080 - 0.0030 - 0.0050 = **0.0000** (zero cost).
3. **EUR/USD rises to 1.1250:** Profit = 0.0150 (150 pips of hedged protection).
4. **EUR/USD rises to 1.1400:** Call spread at max value. **Profit: 0.0200** (200 pips, capped).
5. **EUR/USD drops to 1.0700:** Short put costs 0.0100. **Loss: 100 pips.** Below 1.0800, losses grow pip-for-pip.
6. **EUR/USD stays at 1.1000:** All options expire worthless. **P&L: zero.**

## Advantages
- **Zero or very low cost:** The three-leg structure is designed to self-finance, eliminating upfront premium
- **Directional protection:** Provides meaningful hedge or speculative exposure in the desired direction
- **Popular and liquid in forex:** Widely quoted by banks and brokers as standard hedging structures
- **Simple thesis:** Protection between two levels, funded by selling risk on the opposite side
- **Customizable:** Strike selection allows fine-tuning the protection level, cap, and funding source

## Disadvantages
- **Capped profit:** The spread structure limits the maximum gain, unlike an outright long option
- **Naked leg exposure:** The short option creates significant risk if the underlying moves in the opposite direction
- **Not truly risk-free:** Despite zero cost, the trader takes on meaningful risk from the sold option
- **Three-leg execution:** Wider bid-ask slippage across three options, especially in OTC forex markets where transparency is lower

## See Also
- [[risk-reversal]] -- simpler two-leg version without the profit cap
- [[iron-condor]] -- defined risk on both sides for range-bound markets
- [[butterfly-spread]] -- another low-cost structure for specific price targets
- [[jade-lizard]] -- similar three-leg credit structure with different risk characteristics
