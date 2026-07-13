---
title: "Yield Curve Trading"
type: strategy
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [bonds, fixed-income, yield-curve, steepener, flattener, butterfly, treasury, interest-rates, macro, duration]
aliases: ["Curve Trading", "Yield Curve Strategies", "Steepener Trade", "Flattener Trade", "Butterfly Trade"]
strategy_type: fundamental
timeframe: swing|position
markets: [bonds]
complexity: advanced
backtest_status: untested
edge_source: [analytical, informational, risk-bearing]
edge_mechanism: "Relative-value and macro-forecasting edge: the trader bets that the realized path of the curve will differ from the path priced by forwards, harvesting the gap between expected curve moves and the carry/roll the market charges for holding the position."
data_required: [treasury-yields, futures-prices, dv01-by-tenor, repo-rates]
min_capital_usd: 100000
capacity_usd: 1000000000
crowding_risk: medium
related: ["[[macro-trading]]", "[[interest-rate-risk]]", "[[duration]]", "[[treasury-bonds]]", "[[yield-curve]]", "[[dv01]]", "[[carry-trade]]"]
---

# Yield Curve Trading

Yield curve trading takes positions on expected changes in the **shape** of the [[yield-curve]] -- the relationship between bond yields and their maturities -- rather than on the overall direction of interest rates. Curve traders express views on how different maturities move *relative to each other*: the front end versus the long end, or the "belly" versus the "wings." Properly constructed, these trades are [[duration]]-neutral, insulating them from parallel shifts in rates so that P&L derives only from curve-shape changes. They are a staple of fixed-income hedge funds, bank treasury desks, relative-value funds, and [[macro-trading|macro]] traders.

## Overview

The three primary trade structures:

- **Steepeners** -- bet the curve steepens (the long-end yield rises more than the short-end, or the short-end falls more). A **bull steepener** comes from the front-end falling fast (e.g., the Fed cutting); a **bear steepener** from the long-end rising fast (inflation/term-premium fears).
- **Flatteners** -- bet the curve flattens or inverts (the 2s10s spread narrows). A **bear flattener** from front-end hikes; a **bull flattener** from long-end rallying on recession pricing.
- **Butterfly (fly)** -- bet on **curvature**: long the wings (e.g., 2Y and 30Y) and short the belly (10Y), or the reverse, sized so the position is both duration- and slope-neutral, isolating the convexity of the curve.

Each leg is sized by [[dv01]] (dollar value of a basis point) so the structure is neutral to the risk it is *not* trying to capture.

## Edge source

Per [[edge-taxonomy]], curve trading blends three edges:

- **Analytical** -- correctly modeling [[duration]], [[dv01]], roll-down, carry, and the relative richness/cheapness of tenors versus a fitted curve.
- **Informational / forecasting** -- a differentiated read on the path of monetary policy and inflation versus what forwards already price.
- **Risk-bearing** -- earning the term premium and carry for holding curve risk others wish to shed; some steepener/flattener returns are compensation for bearing duration-shape risk, not pure alpha.

## Why this edge exists

The market prices an expected curve path into **forward rates**. A curve trade profits only if the *realized* curve differs from that forward-implied path. The counterparties are: hedgers (corporate treasurers, mortgage servicers, pensions) who trade the curve to manage liability duration regardless of price; index and passive bond funds rebalancing mechanically; and policymakers/forecasters whose consensus is sometimes wrong at turning points. The persistent-loser dynamic is weaker here than in behavioral anomalies -- much of curve P&L is **risk premium and carry**, which is why crowding_risk is only **medium**: consensus curve trades (e.g., "steepener after the Fed pivot") do get crowded and can unwind violently.

## Null hypothesis

Under no edge, the curve evolves exactly as forwards imply, so every duration-neutral curve trade earns only its **carry and roll-down** minus financing -- a return fully explained by the term-premium/carry the market already offered, with no excess. A steepener that merely matches the forward-implied steepening makes nothing beyond (often negative) carry. The trader must beat the forwards, net of [[transaction-costs]], roll, and repo financing, to claim an edge.

## Rules

- **Steepener:** long short-tenor (2Y) + short long-tenor (10Y), [[dv01]]-weighted; profits as 2s10s widens.
- **Flattener:** short 2Y + long 10Y, [[dv01]]-weighted; profits as 2s10s narrows/inverts.
- **Butterfly:** long 2Y & 30Y wings + short 10Y belly (or reverse), neutral to both level and slope; profits from curvature change.
- **Sizing:** equalize [[dv01]] across legs to neutralize parallel shifts; track and budget **carry** (it can be negative and dominate over short horizons).
- **Instruments:** CME Treasury futures (TU/2Y, FV/5Y, TY/10Y, US/30Y, UB ultra), cash Treasuries (funded in [[repo-rates|repo]]), or interest-rate swaps. Futures are favored for liquidity and capital efficiency; manage the quarterly **roll**.

## Implementation pseudocode

```python
# 2s10s steepener, DV01-neutral, futures-based
target_dv01 = 10_000          # $ per bp of curve move
front = futures("TU")         # 2Y
back  = futures("TY")         # 10Y

n_front = target_dv01 / front.dv01_per_contract        # long
n_back  = target_dv01 / back.dv01_per_contract         # short (equal DV01)

go_long(front, n_front)
go_short(back, n_back)

# daily monitoring
while position_open:
    pnl_curve = (d_spread_2s10s_bps) * target_dv01     # the bet
    pnl_carry = roll_down(front,back) - financing()    # bleed/gain while waiting
    if calendar_near_expiry(front, back):
        roll_contracts()                               # manage quarterly roll
```

## Indicators / data used

[[treasury-yields|Treasury yields]] by tenor (2/5/10/30Y), the 2s10s and 3m10y spreads, [[dv01]]/key-rate durations, futures prices and conversion factors, [[repo-rates]] (for cash/funded trades and carry), Fed funds futures / SOFR futures for policy-path expectations, and inflation breakevens.

## Example trade

A macro trader expects the Fed to cut aggressively over 6 months while long-term inflation expectations stay anchored -- a **bull steepener** setup. Current 2s10s spread: **20 bps**. They go long $10M [[dv01]]-equivalent 2Y futures and short $10M DV01-equivalent 10Y futures (DV01-neutral). Over 4 months the Fed cuts 75 bps; the 2Y yield falls 90 bps while the 10Y falls only 40 bps, so 2s10s widens from 20 → **70 bps**, a 50 bps move. Gross P&L: 50 bps × $10,000/bp = **$500,000**. *(Illustrative round numbers.)* Against this, subtract **negative carry** on the steepener (short the higher-yielding long end), roll costs across the quarterly futures expiry, and execution -- which is where many "right" curve calls still lose money.

## Performance characteristics

Curve trades are **slow-moving, carry-dominated, and convex in tail regimes**. Over short horizons, **carry frequently dominates the directional bet** -- a steepener can be correct on direction yet bleed if the move is slow and carry is negative. Returns are typically modest on capital without leverage, which is why relative-value desks run them levered. Frame performance qualitatively: the edge is realized over weeks-to-months and is highly sensitive to the cost overlay below.

| Cost / friction | Where it bites | Mitigation |
|-----------------|----------------|-----------|
| **Carry / roll-down** | Steepeners often have negative carry; bleeds daily while waiting | Budget carry up front; prefer positive-carry structures or short holding periods |
| **Futures roll** | Quarterly contract roll incurs spread + basis shift | Roll in liquid windows; monitor calendar spreads |
| **Repo / financing** | Cash-Treasury legs financed in [[repo-rates|repo]]; specials raise cost | Use futures; watch for specialness on the cheapest-to-deliver |
| **Bid-ask / [[slippage]]** | Two (or three, for flies) legs each cross the spread | Trade liquid on-the-runs; use spread/curve order types |
| **Basis risk** | Futures-to-cash and CTD optionality | Track basis; hedge with appropriate contract |

## Capacity limits

Very high: Treasury futures and the cash market are among the deepest, most liquid markets globally, so capacity runs into the billions before [[market-impact]] dominates (capacity_usd estimate is order-of-magnitude). The binding constraints are **balance sheet / financing** (repo capacity, margin), not order size in normal conditions; capacity shrinks sharply in stress (e.g., March 2020 Treasury basis dislocation).

## What kills this strategy

See [[failure-modes]]. Realistic killers:

- **Carry bleed** -- a correct-but-slow view drowned by negative carry and roll.
- **Crowded-trade unwind** -- consensus steepener/flattener positioning reverses sharply on a data/policy surprise.
- **Forward-rate efficiency** -- the curve moves as forwards already implied; no excess over carry.
- **Funding / basis stress** -- repo specialness, futures-cash basis blowouts, margin spikes force deleveraging at the worst time.
- **Model/duration error** -- mis-sized [[dv01]] reintroduces unintended level exposure.

## Kill criteria

See [[when-to-retire-a-strategy]]. Exit or pause when:

- Cumulative negative carry has consumed the expected curve P&L before the thesis plays out.
- The policy/inflation thesis is invalidated (e.g., the Fed reverses guidance).
- Position [[dv01]] drifts from neutral beyond a set tolerance.
- Rolling drawdown on the curve book breaches the desk's risk limit.

## Advantages

- **Duration-neutral** -- insulated from parallel rate moves; pure curve-shape expression.
- **Precise macro tool** -- trades monetary policy/economic outlook without outright rate bets.
- **High liquidity** -- Treasury futures/swaps are top-tier liquid.
- **Capital efficient** -- low futures margin relative to notional.

## Disadvantages

- **Carry costs** -- steepeners often bleed while waiting.
- **Basis & roll risk** -- futures-cash basis and quarterly roll add cost/complexity.
- **Slow-moving** -- months to play out; demands patience and conviction.
- **Crowded trades** -- consensus views unwind sharply.
- **Complexity** -- duration weighting, roll, repo, and carry management require specialist expertise.

## Sources

General fixed-income market knowledge ([[dv01]]/duration mechanics, carry/roll, CME Treasury futures conventions, repo financing); no specific wiki source ingested yet. See [[interest-rate-risk]] and [[duration]] for the foundational analytics.

## Related

- [[yield-curve]] -- the term structure this strategy trades
- [[duration]] / [[dv01]] -- the risk metrics used to size legs neutral
- [[interest-rate-risk]] -- the foundational risk concept
- [[treasury-bonds]] -- the primary instruments
- [[repo-rates]] -- financing for cash-Treasury legs; source of carry
- [[carry-trade]] -- carry/roll is central to curve-trade P&L
- [[macro-trading]] -- the broader framework for policy/economic themes
- [[edge-taxonomy]] -- analytical + informational + risk-bearing edges
- [[transaction-costs]] / [[slippage]] / [[market-impact]] -- the execution overlay
