---
title: "Yen Carry Trade"
type: strategy
created: 2026-06-22
updated: 2026-06-22
status: good
tags: [carry-trade, forex, macro, position-trading, leverage, risk-management]
aliases: ["JPY Carry Trade", "Yen Carry", "Japanese Yen Carry Trade"]
strategy_type: fundamental
timeframe: position
markets: [forex]
complexity: advanced
backtest_status: untested
edge_source: [risk-bearing, structural]
edge_mechanism: "Borrow a chronically low-yielding currency (the yen) and invest in higher-yielding assets, earning the interest-rate differential; the return is compensation for bearing the recurring tail risk of a violent, correlated unwind in which the funding currency surges."
data_required: [central-bank-policy-rates, fx-swap-rates, vix, ohlcv-daily]
min_capital_usd: 25000
capacity_usd: 1000000000000
crowding_risk: high
expected_sharpe: 0.6
expected_max_drawdown: 0.40
breakeven_cost_bps: 10
related: ["[[carry-trade]]", "[[forex]]", "[[bank-of-japan]]", "[[interest-rates]]", "[[risk-off]]", "[[vix]]", "[[funding-rate]]", "[[edge-taxonomy]]", "[[tail-risk]]"]
---

# Yen Carry Trade

The yen carry trade is the canonical FX **[[carry-trade]]**: borrow (sell) the Japanese yen — historically the world's lowest-yielding major currency — and use the proceeds to buy higher-yielding currencies, bonds, equities, or other risk assets. The trader earns the **interest-rate differential** as ongoing carry (accruing via FX swap/rollover) and any appreciation of the funded assets. The strategy generates steady income for long stretches and then unwinds catastrophically during [[risk-off]] events, when traders scramble to repay borrowed yen, sending the yen surging and the funded assets crashing simultaneously.

## Edge source

Per [[edge-taxonomy]], the yen carry trade is a **risk-bearing** edge with a **structural** foundation:

- **Risk-bearing** — the carry earner is paid an insurance-like premium for holding a position that loses violently in crises. The steady differential is compensation for absorbing the recurring, correlated crash risk that everyone else wants to shed.
- **Structural** — decades of near-zero (and at times negative) [[bank-of-japan]] policy rates made the yen the world's default funding currency. The persistent rate gap versus higher-yielders is a structural feature of divergent monetary regimes, not a transient mispricing.

This is reinforced by the **forward premium puzzle**: under covered interest parity the rate differential "should" be erased by expected depreciation of the high-yielder, yet empirically high-yielders have *not* depreciated enough on average, leaving the carry profitable far longer than theory predicts.

## Why this edge exists

- **Who is on the other side**: hedgers and investors who *want* to be long yen (or short the high-yielder) — Japanese exporters hedging repatriation, crisis-hedge buyers, and anyone seeking a safe-haven funding currency. They are effectively buying crash insurance; the carry trader sells it.
- **Why they keep paying**: the demand for the yen as a safe haven and the structural rate gap mean the carry trader is compensated continuously for warehousing the risk that, in a panic, the yen rips higher and everyone unwinds at once.
- **Why it isn't free money**: the premium is payment for a genuine, recurring tail event. Periodic violent unwinds (1998, 2008, 2024) transfer years of accumulated carry back to the insurance buyers in a matter of days.

## Null hypothesis

Under covered interest rate parity, the expected return of borrowing yen to fund a higher-yielder is **zero**: the interest differential is exactly offset by expected depreciation of the high-yielding currency. If that held in expectation, the carry trade would earn nothing beyond the risk-free rate. The historical excess return therefore must be either (a) a genuine risk premium for the crash tail, or (b) a behavioral anomaly (the forward premium puzzle). The honest null is that carry returns are *fair compensation for tail risk* — i.e., a strategy that looks like free income in calm samples but has a deeply negatively-skewed true distribution, so that a backtest excluding a major unwind massively overstates the edge.

## Rules

### Entry
1. **Identify a wide, stable differential.** Compare [[bank-of-japan]] policy rate against the target currency's central bank rate. Favor pairs where the differential is large and not about to narrow (e.g., AUD/JPY, MXN/JPY, USD/JPY in high-US-rate regimes).
2. **Risk-on macro filter.** Enter when [[vix]] is low, equities are rising, and credit spreads are tight. Carry thrives in calm.
3. **Go long the high-yielder vs. JPY** and collect the daily swap/rollover.
4. **Avoid entering into BOJ policy-shift risk** — a yen-positive surprise from Tokyo is the single largest threat.

### Exit
1. **Risk-off trigger.** Cut on a [[vix]] spike (e.g., > 25–30), sharp equity selloffs, or widening credit spreads. Unwinds are fast — speed matters more than precision.
2. **Differential narrowing.** Exit if the BOJ signals hikes or the high-yielder's central bank signals cuts.
3. **Hard technical stop.** Never hold a carry position without a stop; the [[tail-risk]] is the whole story.
4. **Event de-risking.** Trim ahead of BOJ meetings, US payrolls/FOMC, elections, and geopolitical flashpoints.

### Position sizing
- Keep leverage conservative (≤ 2–5×). Most blowups involve 10×+.
- Risk ≤ 1–2% of capital per position; recognize that diversifying across carry pairs gives little protection because they all unwind together.

## Implementation pseudocode

```python
def yen_carry(pair, boj_rate, target_rate, vix):
    diff = target_rate - boj_rate              # the carry
    if diff <= cost_threshold:                  # not worth it after costs
        return None
    if vix > RISK_OFF_VIX or boj_hike_imminent():
        return None                            # do not initiate into stress
    size = risk_budget(account, max_risk=0.02, leverage<=4)
    go_long(pair, size)                        # e.g. long AUD/JPY
    while holding:
        accrue_swap(diff)                      # daily carry income
        if vix > RISK_OFF_VIX or credit_spreads_widening() or stop_hit():
            close(pair); break                 # unwind fast
        if boj_signals_hike() or target_cbank_signals_cut():
            close(pair); break                 # differential collapsing
```

## Indicators / data used
- **Policy-rate differential** ([[bank-of-japan]] vs. target central bank) and FX swap/forward points.
- **[[vix]]** and other risk-sentiment gauges (credit spreads, equity trend).
- **Commitment of Traders (COT) positioning** — to gauge crowding in JPY shorts.
- **BOJ and Fed/RBA forward guidance and meeting calendars.**
- **Realized and implied yen volatility** — rising vol precedes unwinds.

## Example trade

*Illustrative, round numbers — not a backtest.*

Suppose the target-currency rate is ~4.5% and the BOJ rate is ~0.25%, a ~4.25% annual differential. A trader goes long AUD/JPY at 95.00 with 3× leverage.
- **Carry income**: ~4.25% annualized on the funded notional, credited daily via positive swap.
- **Calm scenario**: over six months AUD/JPY drifts up to 99.00 — the trader earns the carry *plus* the price appreciation, a double win.
- **Unwind scenario**: a global risk-off shock plus a hawkish BOJ surprise sends AUD/JPY from 95.00 toward the high-80s in a couple of weeks. At 3× leverage the price loss can erase years of accumulated carry and threaten the account. This asymmetry — small steady gains, rare large losses — is the defining feature.

## Performance characteristics
- **Return profile**: steady positive carry punctuated by sudden, deep drawdowns — "picking up pennies in front of a steamroller," with strong negative skew and fat left tail.
- **Correlation**: all carry pairs correlate to global risk; diversification fails precisely when needed.
- **Best conditions**: low volatility, expanding global growth, stable/widening differentials, accommodative BOJ.
- **Worst conditions**: crises, sudden BOJ tightening, liquidity squeezes, geopolitical shocks.
- **Cost awareness**: swap spreads, slippage on fast unwinds, and the option-like cost of hedging the tail all erode the gross carry.

## Capacity limits
Essentially the largest carry trade in the world — aggregate yen-funded positions are estimated in the hundreds of billions to trillions of dollars across FX, bonds, and equities. Individual capacity is effectively unconstrained; the binding limit is **[[crowding-risk]]**: the more crowded the trade, the more violent the eventual unwind, because exits are correlated and self-reinforcing.

## What kills this strategy
- **A BOJ policy surprise** that narrows or reverses the differential (yen-positive shock).
- **A risk-off cascade** that forces simultaneous unwinds and a yen squeeze (see [[failure-modes]]).
- **Leverage** — meaningful carry returns usually require leverage, which converts a drawdown into a wipeout.
- **Crowding** — the popularity of the trade makes the steamroller faster.

## Kill criteria
- [[vix]] spikes above ~25–30 → reduce or exit.
- Position drawdown exceeds ~10–15% from peak → cut.
- BOJ signals or delivers an unexpected rate hike → exit the leg.
- The rate differential narrows below your cost-plus-hurdle threshold → close.
- Yen implied volatility breaks out of its recent range to the upside → de-risk.

## Advantages
- Earns income even when the exchange rate is flat (carry accrues daily).
- Historically profitable beyond theory (forward premium puzzle).
- Powerful when combined with trend-following (carry + trend is among the strongest known FX combinations).
- Exploits a durable, structural feature of divergent monetary regimes.

## Disadvantages
- **Severe negative skew and fat tail** — catastrophic, fast unwinds.
- **Correlated risk** — diversification across pairs provides little crisis protection.
- **Leverage-dependent** returns amplify unwind losses.
- **Single-decision exposure** — one BOJ surprise can erase the differential overnight.
- **Crowding** makes the exit door narrow exactly when everyone heads for it.

## Sources
General market knowledge; no specific wiki source ingested yet. The historical yen-carry unwinds (e.g., the 1998 LTCM-era squeeze, the 2008 crisis, and the August 2024 episode following a BOJ hike and global growth scare) are described qualitatively without inventing precise figures.

## Related
- [[carry-trade]] — the general FX carry strategy this is the archetype of
- [[bank-of-japan]] — the central bank whose policy defines the funding leg
- [[forex]], [[interest-rates]] — market and driver
- [[vix]], [[risk-off]] — the risk gauges that govern timing
- [[tail-risk]] — the cost embedded in the carry
- [[edge-taxonomy]] — classification
