---
title: "Calendar Spread"
type: strategy
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [options, calendar-spread, time-spread, horizontal-spread, theta, volatility, neutral]
aliases: ["Time Spread", "Horizontal Spread"]
strategy_type: quantitative
timeframe: swing
markets: [stocks]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, analytical]
edge_mechanism: "Sell expensive near-term implied vol against cheaper longer-term vol, harvesting the variance risk premium concentrated in the front month plus any term-structure mispricing; the front-month buyer overpays for fast-decaying time."
crowding_risk: medium
related: ["[[diagonal-spread]]", "[[butterfly-spread]]", "[[iron-condor]]", "[[implied-volatility]]", "[[theta]]", "[[vega]]", "[[variance-risk-premium]]", "[[the-greeks]]", "[[term-structure]]", "[[edge-taxonomy]]", "[[option-volatility-and-pricing]]"]
---

# Calendar Spread

## Overview

The Calendar Spread -- also called a **time spread** or **horizontal spread** -- involves buying a longer-dated option and selling a shorter-dated option at the **same strike price**. The strategy exploits the fundamental principle that near-term options decay faster than longer-term options (Source: [[book-option-volatility-and-pricing]]). As the short option erodes toward zero, the long option retains more of its value, and the spread widens in the trader's favor. Maximum profit occurs when the underlying is at the strike price at the short option's expiration.

Calendar spreads benefit from two forces: accelerating [[theta]] decay in the short leg, and a rise in [[implied-volatility]] in the back-month option. The ideal scenario is a stock that sits still near the strike while IV in the longer-dated month increases (often ahead of an anticipated event in that cycle). The strategy is hurt by large moves away from the strike and by a collapse in back-month IV. Calendars are a staple of income-oriented options traders and pair naturally with [[butterfly-spread]]s and [[iron-condor]]s in a portfolio approach.

## Edge source

The calendar harvests the **[[variance-risk-premium]]** where it is richest -- the **front month** -- while financing it with a long back-month option that decays more slowly. In the [[edge-taxonomy]] this is a **risk-bearing** edge (short near-term vol) combined with an **analytical** edge in reading the **[[term-structure]]** of volatility: the trade is best when front-month IV is high relative to back-month IV (term structure in [[backwardation]]), or before an event will inflate the back-month leg you are long. You are, on net, **short vol in the front and long vol in the back** -- a relative-value position on the shape of the vol curve.

## Why this edge exists

- **Front-month buyers overpay for fast time decay.** Near-dated options are bought by event traders, gamma scalpers, and lottery players who want immediate exposure; their demand keeps front-month IV bid even though that premium evaporates quickest.
- **Term-structure dislocations** appear around events: pre-earnings, the cycle containing the event prices in extra IV. A calendar long the post-event month and short a pre-event month monetizes the eventual crush of the wrong leg.
- **Theta asymmetry is mechanical**, not behavioral: extrinsic value decays on a square-root-of-time curve, so the 30-day option you sold loses value far faster than the 60-day option you bought (Source: [[book-option-volatility-and-pricing]]).

The edge persists because correctly trading vol term structure requires modeling the back-month IV at a future date -- harder than directional trading, so fewer participants compete it away.

## Null hypothesis

If the vol surface is fairly priced -- front and back IV consistent with no term-structure premium -- the calendar's expected P&L is just **minus costs**. The mechanical theta advantage of the short leg is exactly offset by the long leg's higher price and its own decay, and the apparent "spread widening" is fully priced into the entry debit. Under the null there is no relative-value edge: the trade is a bet on the underlying pinning the strike, with expectancy ≈ −frictions and break-evens that merely reflect fair extrinsic value. A genuine edge requires entering when front IV is *richer* than back IV beyond fair value (or capturing a real event-driven term-structure move).

## Rules / Setup

### Entry
1. **Select the strike:** Choose a strike at or near the current price of the underlying (ATM calendar) for a neutral outlook, or slightly OTM for a directional lean.
2. **Sell the front-month option:** Sell a call or put with 20-35 DTE. This is the leg that will decay rapidly.
3. **Buy the back-month option:** Buy the same type (call or put) at the same strike with 45-75 DTE. This is the anchor that retains value.
4. **IV assessment:** Ideally, front-month IV is higher than back-month IV (the "term structure" is in [[backwardation]]). This makes the spread cheaper to enter. The best case is entering before an event in the back month that will inflate that option's IV.
5. **Cost:** The net debit is typically 30-50% of the long option's price.

### Exit
1. **Profit target:** Close when the spread has expanded by 25-50% of the debit paid.
2. **At front-month expiration:** If the underlying is near the strike, the short option expires worthless and the long option retains significant value. Either close the long leg or sell a new short-dated option against it (rolling into a new calendar).
3. **Stop-loss:** Close if the underlying moves more than one standard deviation from the strike, or if the spread narrows to 50% of the debit paid.
4. **IV management:** If back-month IV drops sharply, the long option loses value faster than expected. Consider closing early.

### Position Sizing
Risk the full debit paid. Size so that maximum loss (which is less than the debit in practice, since the long option retains some value) represents no more than 2-4% of the account.

## Implementation pseudocode

```python
def calendar_spread(underlying, chain, otype="call"):
    front = pick_expiration(chain, target_dte=28)   # 20-35 DTE (sell)
    back  = pick_expiration(chain, target_dte=60)   # 45-75 DTE (buy)
    if iv(front) < iv(back):                         # want front >= back (backwardation)
        return None                                  # term structure not favorable
    K = atm_strike(chain, front, underlying.price)   # or slight OTM for a lean
    short_leg = sell(chain.option(otype, front, K))
    long_leg  = buy(chain.option(otype, back,  K))
    debit = long_leg.mid - short_leg.mid
    pos = Calendar(short_leg, long_leg, debit)
    pos.profit_target = debit * 1.35                 # +25-50% on the spread
    pos.stop = debit * 0.50                          # spread halves
    return pos

def manage(pos, mark):
    spread = pos.long_leg.mark - pos.short_leg.mark
    if spread >= pos.profit_target:                  return close(pos)
    if spread <= pos.stop:                           return close(pos)
    if abs(underlying.price - pos.K) > one_sigma:    return close(pos)   # moved too far
    if pos.front_dte <= 0:                           return roll_into_new_calendar(pos)
```

## Example Trade
**Asset:** MSFT trading at $420, 30 DTE front-month, 60 DTE back-month. *(Illustrative hypothetical -- not a real trade or backtest.)*
1. **Sell 1 MSFT $420 call** (30 DTE) at $8.50.
2. **Buy 1 MSFT $420 call** (60 DTE) at $13.00.
3. **Net debit:** $13.00 - $8.50 = **$4.50** ($450 per spread).
4. After 28 days, MSFT is at $418. The front-month call is worth $1.00 and the back-month (now 32 DTE) is worth $9.50.
5. **Spread value:** $9.50 - $1.00 = $8.50. Profit: $8.50 - $4.50 = **$4.00** ($400 per spread, +89%).
6. Alternatively, let the short call expire and sell a new 30 DTE call against the remaining long option.

## Payoff Profile
- **Max profit:** Achieved when the underlying is exactly at the strike at front-month expiration. The short option expires worthless and the long option has maximum extrinsic value. The exact amount depends on remaining IV.
- **Max loss:** Limited to the net debit paid. Occurs when the underlying moves far from the strike in either direction, collapsing the spread to near zero.
- **Break-even points:** Depend on back-month IV at front-month expiration -- cannot be calculated precisely at entry. Generally, the spread is profitable within a range similar to a butterfly.
- **Greeks at entry:** Near-zero [[delta]], positive [[vega]] (benefits from rising IV), positive [[theta]] (net time decay benefit), negative [[gamma]] (Source: [[book-option-volatility-and-pricing]]).

## Performance characteristics

- **Defined, modest risk; tent-shaped payoff.** Unlike short straddles/strangles the max loss is capped at the debit, so the skew is far more benign. The trade-off is a **narrow profit zone** and reliance on a correct vol-term-structure read.
- **Long vega is double-edged.** Positive [[vega]] helps if back-month IV rises but **hurts on a vol crash** -- a market-wide vol collapse can shrink the long leg and the spread even if the underlying sits still.
- **Sensitive to the IV read, not just price.** P&L depends on the back-month IV at front expiration, which cannot be known at entry -- the hardest part to model. Qualitative -- not a backtested figure.
- **Best around predictable term-structure events** (pre-earnings calendars); worst in trending markets that walk the underlying away from the strike.

## Capacity limits

Moderate. Calendars require liquid options in **two** expirations at the same strike, so capacity is bounded by the thinner of the two months' open interest; back-month strikes are often less liquid and wider. Scales fine for retail and small funds on liquid names and major ETFs/indices, but large size faces double the spread cost (two legs, two expiries) and signaling on the less-liquid back month (medium crowding risk).

## What kills this strategy

- **Large directional move** away from the strike -- both options converge toward intrinsic value, the time-value differential vanishes, and the spread collapses toward zero. The dominant failure mode.
- **Back-month IV collapse** -- a vol crash deflates the long leg faster than the short leg, narrowing the spread.
- **Buying when front IV < back IV** (contango) -- you overpay for the structure and start with no edge.
- **Wrong event timing** -- if the anticipated IV expansion in the back month does not materialize.
- **Pin/assignment risk** on the short leg if it finishes near the strike; some brokers margin the short leg as undefined risk.

## Kill criteria

- Underlying moves more than **one standard deviation** from the strike -> close.
- Spread value falls to **50% of the debit paid** -> stop out.
- Back-month IV drops sharply (e.g. a regime vol crash) and the spread stalls -> close early.
- The anticipated term-structure / event catalyst is invalidated -> exit; the thesis is gone.
- Realized loss on the debit reaches your per-trade 2-4% account limit -> close.

## Advantages
- **Exploits time decay differential:** The short option decays 2-3x faster than the long option near expiration.
- **Benefits from rising IV:** An increase in back-month [[implied-volatility]] expands the spread's value.
- **Defined risk:** Maximum loss is the net debit paid (benign, non-tail skew).
- **Rollable:** After front-month expiration, the long option can be used to establish a new calendar, [[diagonal-spread]], or [[covered-call]]-like structure.
- **Flexible:** Works with calls or puts and can be placed at any strike for neutral or directional positioning.

## Disadvantages
- **Narrow profit zone:** Like a [[butterfly-spread]], the underlying must stay near the strike for the trade to work.
- **Vulnerable to IV collapse:** If back-month [[implied-volatility]] drops, the long option loses value and the spread narrows.
- **Complex P&L modeling:** Profit depends on IV of the back-month option at a future date, which cannot be precisely predicted.
- **Large moves are fatal:** A sharp move in either direction drives both options toward intrinsic value, eliminating the time-value differential.
- **Margin considerations:** Some brokers treat calendars as undefined risk on the short leg, requiring significant buying power.

## See Also
- [[diagonal-spread]] -- same concept but with different strikes, adding a directional component.
- [[butterfly-spread]] -- similar payoff shape with a single expiration cycle.
- [[iron-condor]] -- broader range-bound strategy that collects premium from both sides.
- [[theta]] -- the primary profit driver for calendar spreads.
- [[implied-volatility]] -- rising back-month IV is the calendar trader's best friend.
- [[calendar-spread-arbitrage]] -- pure arbitrage variant exploiting calendar spread mispricings.

## Sources
- [[book-option-volatility-and-pricing]] — Natenberg's detailed analysis of time spreads, the differential theta decay between near-term and far-term options, and the impact of volatility term structure on calendar spread pricing
