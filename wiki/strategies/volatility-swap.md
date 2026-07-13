---
title: "Volatility Swap"
type: strategy
created: 2026-06-22
updated: 2026-06-22
status: good
tags: [volatility, derivatives, quantitative, options, risk-management]
aliases: ["Vol Swap", "Realized Volatility Swap"]
strategy_type: quantitative
timeframe: position
markets: [options, stocks, futures]
complexity: advanced
backtest_status: untested
edge_source: [risk-bearing, structural]
edge_mechanism: "An OTC forward on realized volatility paying (realized vol − strike) × notional; sellers harvest the variance/volatility risk premium because the strike (implied vol) systematically exceeds subsequent realized vol, in exchange for bearing crash convexity."
data_required: [realized-volatility, implied-volatility-surface, otc-quotes]
min_capital_usd: 100000
capacity_usd: 5000000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.35
breakeven_cost_bps: 15
related: ["[[variance-swap]]", "[[realized-volatility]]", "[[implied-volatility]]", "[[volatility-trading]]", "[[delta-hedged-options]]", "[[gamma-scalping]]", "[[variance-risk-premium]]", "[[edge-taxonomy]]"]
---

# Volatility Swap

A volatility swap is an over-the-counter (OTC) forward contract that pays the difference between the **[[realized-volatility]]** of an underlying over the contract life and a fixed **volatility strike** (set at inception near prevailing [[implied-volatility]]), multiplied by a vega notional. It lets a trader take a *direct, pure* position on realized volatility without holding and continuously [[delta-hedged-options|delta-hedging]] an options book. Its close cousin, the **[[variance-swap]]**, pays on realized *variance* (vol squared) rather than vol; the difference in payoff — linear in vol vs. linear in variance — produces a **convexity** distinction that is the central nuance of the instrument.

## Edge source

Per [[edge-taxonomy]], the (typical short) volatility swap is a **risk-bearing** edge with a **structural** basis:

- **Risk-bearing** — selling a vol swap (receiving fixed strike, paying realized) earns the **[[variance-risk-premium]]**: implied vol set at strike has, on average and especially for indices, exceeded subsequent realized vol. The seller is paid for bearing the risk that realized vol explodes.
- **Structural** — persistent hedging demand for protection keeps implied vol (and hence achievable strikes) elevated relative to realized. The vol-swap seller monetizes that demand directly, without the path-dependent slippage of running a delta-hedged options book.

## Why this edge exists

- **Who is on the other side**: hedgers and long-vol/tail funds that *buy* volatility as insurance and are willing to overpay for it; dealers who warehouse and recycle the exposure.
- **Why they keep paying**: like all insurance, long-vol buyers accept a negative expected carry in exchange for protection that pays in crashes. The vol-swap seller collects that premium.
- **Why it isn't free money**: the seller has a short-convexity, fat-left-tail payoff. A single volatility explosion can repay years of collected premium. (And because a vol swap is *less* convex than a variance swap, the seller of a vol swap is exposed differently in the tail — see below.)

## Vol swap vs. variance swap (the convexity point)

- A **variance swap** pays `(σ²_realized − K_var) × variance_notional`. Because the payoff is in variance, it is **convex in volatility**: gains accelerate as realized vol rises. This convexity makes variance swaps easier for dealers to replicate (via a static portfolio of options across strikes) and is why variance swaps are far more liquid than vol swaps.
- A **volatility swap** pays `(σ_realized − K_vol) × vega_notional` — **linear in volatility**, hence *no* convexity. It cannot be statically replicated; dealers must dynamically hedge the "convexity adjustment" between the two, and the vol-swap strike trades slightly below the square root of the variance-swap strike to reflect that (a consequence of Jensen's inequality).
- Practical upshot: a volatility swap gives a cleaner, more intuitive bet on *vol* (no squaring to distort the payoff), but the variance swap's convexity makes it the dealer's preferred, more liquid product, and the long variance position benefits more in extreme moves.

## Null hypothesis

If the volatility strike equals expected future realized volatility, a vol swap has **zero** expected payoff — selling it earns nothing beyond compensation embedded in the strike. Under this null any apparent profit to the seller is simply the [[variance-risk-premium]], i.e., fair payment for the crash tail, and a short-vol-swap book has an expected return near zero once a major volatility event is included in the sample. A backtest that omits a vol explosion will badly overstate the seller's edge, because the true distribution is heavily left-skewed.

## Rules

### Entry
1. **Form a realized-vol view.** Compare the dealer's quoted vol-swap strike (≈ implied vol, minus a convexity adjustment) against your forecast of realized vol.
2. **Sell vol** (receive fixed strike) when you expect realized < strike — the systematic carry case. **Buy vol** when you expect a vol expansion (event, regime shift) the market is underpricing.
3. **Choose tenor and underlying** consistent with the view (e.g., 1–3 month index vol swaps are most common).
4. **Negotiate terms** OTC: vega notional, observation frequency, annualization, and any vol cap (caps limit the seller's tail loss).

### Exit
1. **Hold to maturity** — payoff settles on realized vol over the window.
2. **Unwind early** via an offsetting swap or a replicating options/variance position if the view changes.
3. **Tail stop** — for short positions, exit or hedge if realized vol breaks decisively above strike.

### Position sizing
- Size vega notional to a stressed realized-vol scenario (e.g., vol tripling), not to the expected carry.
- Prefer **capped** vol swaps for short positions to bound the left tail; the cap costs carry but converts an unbounded loss into a known maximum.

## Implementation pseudocode

```python
def short_vol_swap(underlying, tenor, strike_vol, vega_notional, cap=None):
    # short: receive strike, pay realized
    realized = annualized_realized_vol(price_path(underlying, tenor))
    payoff_to_long = (realized - strike_vol) * vega_notional
    if cap is not None:
        payoff_to_long = min(payoff_to_long, (cap - strike_vol) * vega_notional)
    seller_pnl = -payoff_to_long            # we are short the swap
    return seller_pnl

def decide(strike_vol, forecast_vol, hurdle):
    if strike_vol - forecast_vol > hurdle:  # carry rich enough
        return "SELL_VOL"
    if forecast_vol - strike_vol > hurdle:  # cheap vol into a catalyst
        return "BUY_VOL"
    return "PASS"
```

## Indicators / data used
- **Vol-swap / [[variance-swap]] strikes** (dealer quotes) vs. your **[[realized-volatility]]** forecast.
- **[[implied-volatility]] surface** — strikes are anchored to implied; the convexity adjustment links vol- and variance-swap strikes.
- **[[variance-risk-premium]]** estimates — the historical implied-minus-realized gap.
- **Realized-vol estimators** (close-to-close, Parkinson, Garman-Klass) and the contract's specified estimator.

## Example trade

*Illustrative, round numbers — not a backtest.*

A trader sells a 1-month index volatility swap struck at 18% with a vega notional of $50,000 per vol point.
- **Calm scenario**: realized vol comes in at 14%. Payoff to the long = (14 − 18) × $50,000 = −$200,000, so the *seller* earns **+$200,000**.
- **Shock scenario**: a market shock pushes realized vol to 40%. Payoff to the long = (40 − 18) × $50,000 = +$1,100,000, so the seller *loses* **$1,100,000** — many times the calm-case gain. A vol cap (say at 35%) would have bounded that loss. This asymmetry is the whole risk story of short vol.

## Performance characteristics
- **Return profile (short)**: steady positive carry from the variance premium, with rare, severe losses on vol spikes — short-convexity, negatively skewed.
- **Vs. delta-hedged options**: a vol swap delivers a *cleaner* realized-vol exposure with no path-dependent hedging error, but as an OTC product it carries counterparty risk and wider spreads.
- **Best conditions (short)**: persistently elevated implied vol with subdued realized vol.
- **Worst conditions (short)**: regime shifts and crashes where realized vol explodes.

## Capacity limits
Vol swaps are OTC and less liquid than [[variance-swap]]s; capacity is constrained by dealer balance sheet and willingness to warehouse the convexity-adjustment risk. Index underlyings support larger notional than single names. Crowding among short-vol sellers raises systemic fragility — a crowded short-vol complex can amplify a volatility spike as dealers and sellers hedge in the same direction.

## What kills this strategy
- **A volatility explosion** that overwhelms accumulated carry on the short side (see [[failure-modes]]).
- **Counterparty default** on the OTC contract.
- **Liquidity evaporation** preventing early unwind during stress.
- **Crowded short-vol positioning** that turns a vol spike into a cascade.

## Kill criteria
- Realized vol breaches the strike by more than a preset multiple → exit / hedge the short.
- Mark-to-market loss exceeds ~2–3× the contract's expected carry → unwind.
- Counterparty credit deterioration → novate or close.
- For uncapped short positions, any disorderly vol spike → cover immediately.

## Advantages
- **Pure, direct** exposure to realized volatility — no delta-hedging path dependence.
- Clean expression of the [[variance-risk-premium]] for sellers.
- Linear (intuitive) payoff in vol units; caps can bound seller risk.
- Customizable OTC terms (tenor, estimator, observation frequency).

## Disadvantages
- **OTC counterparty risk** and wider spreads vs. listed products.
- **Short-convexity tail** — large losses in vol spikes (sellers).
- **Less liquid** than variance swaps; harder to unwind in stress.
- **No static replication** — the linear-vol payoff is harder for dealers to hedge, embedded in pricing.

## Sources
General market knowledge; no specific wiki source ingested yet.

## Related
- [[variance-swap]] — the convex sibling instrument
- [[realized-volatility]], [[implied-volatility]] — the payoff reference and strike anchor
- [[variance-risk-premium]] — the harvested premium
- [[delta-hedged-options]], [[gamma-scalping]] — the listed-options way to trade realized vol
- [[volatility-trading]] — broader context
- [[edge-taxonomy]] — classification
