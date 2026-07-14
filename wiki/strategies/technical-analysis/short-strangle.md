---
title: "Short Strangle"
type: strategy
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [options, short-strangle, premium-selling, theta-gang, neutral, undefined-risk]
strategy_type: quantitative
timeframe: swing
markets: []
complexity: advanced
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "Sell out-of-the-money implied volatility on both wings to hedgers and tail-buyers; collect the variance risk premium over a wide range in exchange for bearing undefined gap risk."
crowding_risk: high
related: ["[[short-straddle]]", "[[straddle-strangle]]", "[[iron-condor]]", "[[jade-lizard]]", "[[theta]]", "[[vega]]", "[[implied-volatility]]", "[[variance-risk-premium]]", "[[the-greeks]]", "[[edge-taxonomy]]"]
---

# Short Strangle

## Overview

The Short Strangle sells an OTM [[call-option]] and an OTM [[put-option]] at different strikes with the same expiration. By placing both short strikes away from the current price, the trader creates a **wider profit zone** than the [[short-straddle]] at the cost of collecting less total premium. The position profits when the underlying stays between the two strikes, letting [[theta]] decay erode both options to zero. It is a staple of premium-income strategies in **high-IV-rank** markets. Like the straddle, the risk is **undefined** -- a large move in either direction produces losses that can far exceed the credit collected.

## Edge source

Like the [[short-straddle]], the strangle harvests the **[[variance-risk-premium]]**: a **risk-bearing** edge (paid an insurance premium for absorbing tail risk) layered on a **behavioral** edge (buyers overpay for OTM convexity / lottery payoffs). See [[edge-taxonomy]]. The strangle differs only in *where* on the distribution you sell vol -- the OTM wings -- giving a wider no-loss zone and a higher headline win rate, but the same fundamental short-tail exposure.

## Why this edge exists

The counterparties keep paying for the same reasons as in any short-vol trade:

- **Hedgers** buy OTM puts as cheap crash insurance and are price-insensitive about it; the implied vol on those wings (the "skew") trades persistently above realized.
- **Tail / lottery buyers** bid up far-OTM calls and puts hoping for an outsized move, overweighting small probabilities.
- **Structural demand for protection** exceeds the natural supply of sellers, so the clearing price of OTM vol sits above the fair price.

The strangle seller is the willing insurer of both wings. The premium is real and recurring; the cost is that you eventually pay a large claim when a genuine move occurs.

## Null hypothesis

With no edge, the OTM call and put are priced fairly and the expected P&L equals **minus costs**. The strategy then becomes a wide bet whose ~85% win rate is purely a function of the breakevens being far away -- it conveys no expectancy. Under the null, the rare losses are proportionally larger (because the strikes are far out, a breach implies a big move), so the negative skew is even more pronounced than the straddle's. A genuine edge requires net-of-cost expectancy above zero *after* the tail losses are fully counted, not a flattering win-rate statistic.

## Rules

**Strike & DTE selection**
- Sell the OTM call near **~16 delta** (roughly one standard deviation above price) and the OTM put near **~16 delta** below. Lower delta = wider, safer, less premium.
- **30-45 DTE** for optimal [[theta]] acceleration with room to manage.
- Enter at **elevated IV rank** (e.g. IVR > 50) so the OTM premiums are rich relative to the expected move.

**Entry**
- Range-bound, non-trending underlying; no binary catalyst inside the window.
- Net credit should give an acceptable return on buying-power reduction (a common heuristic is ~1/3 of strike width as credit on an undefined strangle, but treat this as a guideline, not a rule).

**Management & exit**
- **Profit target**: close at ~50% of max credit.
- **Defense**: roll the untested side toward price to recenter, roll out in time for a credit, or convert to an [[iron-condor]] by buying protective wings if risk needs capping.
- **Time stop**: manage/close at ~21 DTE before gamma dominates.

**Sizing**
- Undefined risk: size on a **2-3 sigma stress gap**, not on margin. Keep single-position stress loss small (e.g. < 1-2% of account).

## Implementation pseudocode

```python
def short_strangle(underlying, chain, call_delta=0.16, put_delta=0.16):
    if iv_rank(underlying) < 50:
        return None
    if event_in_window(underlying, dte=45):
        return None
    exp  = pick_expiration(chain, target_dte=35)        # 30-45 DTE
    call = sell(strike_by_delta(chain.calls(exp), call_delta))
    put  = sell(strike_by_delta(chain.puts(exp),  put_delta))
    credit = call.mid + put.mid
    position = Strangle(call, put, credit)
    position.profit_target = 0.50 * credit
    position.time_stop_dte = 21
    return position

def manage(position, mark):
    if position.pnl >= position.profit_target:   return close(position)
    if position.dte <= position.time_stop_dte:   return close_or_roll(position)
    if tested_side_breached(position):           return roll_untested_side(position)
    if risk_too_large(position):                 return convert_to_iron_condor(position)
```

## Example trade

*Illustrative hypothetical with round numbers -- not a real trade or backtest.*

Stock XYZ trades at $100, IV rank 65. Sell the 35-DTE 16-delta strangle:

| Leg | Action | Strike | Premium |
|---|---|---|---|
| OTM call | Sell | $110 | $1.50 |
| OTM put | Sell | $90 | $1.50 |
| **Total credit** | | | **$3.00 ($300)** |

- **Max profit** = $300 (both expire worthless with XYZ between $90 and $110).
- **Breakevens** = $113 (up) and $87 (down).
- **Max loss** = unlimited.

| Outcome at expiration | P&L per contract |
|---|---|
| XYZ between $90-$110 | +$300 (full credit) |
| XYZ at $112 (inside upper breakeven) | call worth $2 -> +$100 |
| XYZ at $118 | call worth $8 -> -$500 |
| XYZ gaps to $135 on news | call worth $25 -> **-$2,200** |

Note the wide $90-$110 win zone (high probability) and the brutal tail when it finally breaks.

## Performance characteristics

- **Negative skew, very high win rate.** Wider breakevens than the straddle push the win rate up (often 80-90%) but the loss-when-wrong is correspondingly larger -- the same "**pennies in front of a steamroller**" dynamic.
- **Less premium per trade** than a straddle, so traders are tempted to add size or contracts -- which amplifies tail exposure.
- **Short gamma and short [[vega]].** A vol spike loses money via vega before any theta accrues; a realized move loses via gamma.
- **Correlated tail.** A systemic vol event hits all short strangles simultaneously regardless of underlying diversification.
- Edge is real but thin once spreads, slippage on rolls, and margin cost are netted out. (Qualitative -- not a backtested figure.)

## Capacity limits

Better single-name capacity than the straddle because OTM strikes on liquid names carry decent open interest, but still bounded: deep OTM wings on small caps are thin and gap-prone. Index/ETF strangles (SPX, /ES, RUT) offer the most depth for size. As with all short-vol, the binding constraint is **survivable stress loss**, and crowding into the trade compresses the very premium (especially put skew) that makes it work -- high crowding risk.

## What kills this strategy

- **Large move / gap past a wing** -- the dominant failure mode; undefined loss with no time to hedge on an overnight gap.
- **Vol spike (vega)** that inflates both wings before theta works.
- **Trending market** that walks steadily through one strike (the strangle assumes mean reversion).
- **Over-trading the low premium** -- adding contracts to compensate for thin credit multiplies the tail.
- **Assignment** on an ITM wing leaving an unwanted stock or short-stock position.
- **Entering at low IV rank** -- no premium cushion, breakevens too close.

## Kill criteria

- Modeled 3-sigma stress loss on the position exceeds **2% of account** -> reduce or skip.
- Realized loss reaches **2x the credit collected** -> close.
- Underlying breaches a breakeven on a trending (not mean-reverting) move -> close/defend the tested side.
- Portfolio short-vega exceeds the book limit -> stop adding strangles.
- Strategy-level rolling 6-month net P&L negative after costs -> pause; the premium no longer compensates for the tail.

## Advantages
- Wider profit zone than a [[short-straddle]] -- higher probability of profit.
- Collects premium from both sides of the market.
- Benefits from [[theta]] decay and [[implied-volatility]] contraction simultaneously.
- Flexible strike selection tailors probability and risk/reward.
- Easily defended by rolling or converting to a defined-risk [[iron-condor]].

## Disadvantages
- **Undefined risk** in both directions -- catastrophic losses possible on a large gap.
- **Negatively skewed**: very high win rate hides a thin, tail-exposed expectancy.
- Less premium than a straddle, tempting over-sizing.
- Requires substantial **margin** and careful sizing.
- High [[gamma]] and short [[vega]] near expiration create rapid P&L swings.
- A single large loss event can wipe out many months of premium income.

## See Also
- [[short-straddle]] -- more premium, narrower profit zone, same risk profile.
- [[iron-condor]] -- adds protective wings to define the risk on a strangle.
- [[jade-lizard]] -- a modified strangle that eliminates risk on one side.
- [[straddle-strangle]] -- the long side of the volatility trade.

## Sources
General market knowledge; no specific wiki source ingested yet.
