---
title: "Ratio Calendar Spread"
type: strategy
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [options, derivatives, volatility, swing-trading]
aliases: ["Ratio Calendar Spread", "Asymmetric Calendar", "Unbalanced Calendar", "Ratio Time Spread"]
related: ["[[calendar-spread]]", "[[diagonal-spread]]", "[[ratio-spread]]", "[[options-greeks]]", "[[theta]]", "[[vega]]", "[[implied-volatility]]", "[[implied-volatility-term-structure]]", "[[volatility-risk-premium]]", "[[short-strangle]]", "[[iron-condor]]", "[[managing-winners]]", "[[trade-repair-and-rolling]]", "[[options-portfolio-construction]]"]
strategy_type: hybrid
timeframe: swing
markets: [stocks, options, index-options]
complexity: advanced
backtest_status: untested
edge_source: [risk-bearing, analytical, behavioral]
edge_mechanism: "Combines a calendar spread (selling near-dated, buying far-dated) with a non-1:1 ratio so the trade is biased deliberately to either credit collection (more shorts) or directional convexity (more longs); the asymmetric ratio expresses a view on volatility term structure and direction simultaneously."
data_required: [options-chain, implied-volatility, implied-volatility-term-structure, earnings-calendar]
min_capital_usd: 10000
capacity_usd: 5000000
crowding_risk: low
expected_sharpe: 1.0
expected_max_drawdown: 0.30
breakeven_cost_bps: 40
---

A **ratio calendar spread** is a calendar spread (long and short options at the same strike but different expirations) constructed with an *unequal* number of contracts on the two legs — 1:2, 2:1, 1:3, or any other deliberate ratio. Unlike a 1:1 calendar (pure vega/term-structure bet), the ratio variant injects an explicit directional or income tilt: more shorts make the spread a *credit-tilted income trade*, more longs make it a *long-volatility / convexity trade*.

## Edge Source

The ratio calendar draws from three of the [[edge-taxonomy]] categories:

1. **Risk-bearing edge** — Selling shorter-dated options collects the [[volatility-risk-premium|volatility risk premium]]. When the ratio is short-heavy (e.g., 1 long / 3 short), the trade is mostly an income structure paying the trader for absorbing near-term tail risk. Index data shows IV exceeds RV roughly 80-85% of the time at 30-day horizons.
2. **Analytical edge** — Selecting the ratio is itself the analytical work. The trader is expressing a view on the *shape* of the [[implied-volatility-term-structure|IV term structure]] and the *path* of the underlying. Getting the ratio wrong (too many longs in calm vol, too many shorts when term structure flips into backwardation) is what kills naive implementations.
3. **Behavioral edge** — Retail traders default to the simplest 1:1 calendar and rarely consider asymmetric ratios. Professional desks harvest this gap by tailoring the ratio to the specific catalyst, vol regime, and directional bias.

## Why This Edge Exists

The structure persists because it is genuinely complex to manage. The non-1:1 ratio creates a Greeks profile that changes shape as the near leg decays — a 1:2 long-heavy calendar starts roughly delta-neutral and becomes a long-options position after the short leg expires, while a 2:1 short-heavy calendar starts as net-short premium and converts to a vertical spread or naked long if managed badly. Most retail platforms do not natively visualise this shape-shifting payoff, and most retail traders cannot model the second-order vega and gamma transitions. The ratio calendar is therefore an "analytical moat" trade: edge accrues to those who can actually run the math.

The other side of the trade is overwhelmingly:

- Single-leg option buyers paying inflated near-term IV
- 1:1 calendar traders who failed to tilt the ratio toward the regime
- Volatility-arbitrage shops that hedged term structure but not direction

## Null Hypothesis

Under random conditions with IV = RV on average and no term-structure premium, the short leg's credit collection would be offset by the long leg's decay, the directional component would have zero expectation, and net P&L would equal -costs. Any consistent profitability must come from either (a) the structural [[volatility-risk-premium|VRP]] in near-dated options, (b) directional alpha in the underlying, or (c) systematic mispricing in the IV term structure that the ratio captures. A ratio calendar with no view on which of these is generating P&L is a coin flip with extra steps.

## Rules

### Variant 1 — Long-Near, Short-Far (Reverse Calendar)

Less common; used when the trader expects near-term IV to *expand* relative to far-term IV (term structure is in steep contango and expected to flatten or invert).

| Component | Specification |
|---|---|
| Long leg | Buy N near-dated options (10-30 DTE) |
| Short leg | Sell M far-dated options (60-120 DTE), where M < N or M > N depending on cost balance |
| Net Greeks at entry | Net long gamma, short vega (front-month vol up = good) |
| Cost | Often a debit if N > M, can be a credit if M > N |

This variant is the rarer "reverse" calendar and benefits from a vol *spike* hitting near-dated more than far-dated — typically right before earnings or a known catalyst.

### Variant 2 — Short-Near, Long-Far (Standard Direction)

The dominant variant. Selling the near, buying the far, with ratio chosen to tilt the structure.

#### Sub-variant 2a — Long-heavy (1:2, 1:3) — Convexity Trade

| Component | Specification |
|---|---|
| Short leg | Sell N near-dated options (20-35 DTE) |
| Long leg | Buy 2N or 3N far-dated options (60-180 DTE) |
| Greeks at entry | Net long vega, long gamma (after near expires), small or net debit |
| P&L profile | Income first (near-leg credit), then a long-options payoff if the underlying moves |

#### Sub-variant 2b — Short-heavy (2:1, 3:1) — Income / Theta Trade

| Component | Specification |
|---|---|
| Short leg | Sell 2N or 3N near-dated options (20-45 DTE) |
| Long leg | Buy N far-dated options (90-180 DTE) as a wing for catastrophic protection |
| Greeks at entry | Net short premium, net short vega, large negative theta cost |
| P&L profile | Steady credit collection bounded by the long-wing protection in a tail event |

The short-heavy variant resembles a [[short-strangle]] with a far-dated catastrophic-loss wing rather than a same-expiration long. It's used when the trader expects the underlying to be range-bound and IV to compress.

### Entry Rules (Common to All Variants)

1. **View first** — Specify the directional, vol, and term-structure view *before* picking the ratio. The ratio is a consequence of the view, not the starting point.
2. **Term-structure check** — Pull front-month and back-month IV. Standard direction (sell near, buy far) requires *contango* (front IV ≤ back IV) for the calendar component to be profitable. If the term structure is inverted (backwardation), the standard direction is fighting the curve.
3. **Catalyst alignment** — If a catalyst (earnings, FOMC, expiration cliff) falls between the two expirations, decide whether the catalyst should be inside the short window (catalyst hits the short leg = collected credit if move is small) or pushed into the long window (catalyst hits the long leg = directional payoff).
4. **Net debit / credit accounting** — Long-heavy ratios usually cost a net debit; short-heavy ratios usually pay a net credit. Size the position by net cash outlay, not contract count.
5. **Position sizing** — 5-10% of capital per trade for long-heavy variants; tighter (2-5%) for short-heavy variants because tail loss in a vol spike can far exceed the credit collected.

### Exit Rules

1. **Short leg target** — Buy back the short leg at 50-85% of max profit (depending on variant; long-heavy uses 75-85%, short-heavy uses 50%).
2. **Long-leg disposition after short closes** — In long-heavy variants, hold or roll the long leg as a directional bet. In short-heavy variants, decide whether to close the wing or leave it as residual protection.
3. **Loss thresholds** — Exit at 2-3x credit received (short-heavy) or 50% premium loss (long-heavy).
4. **Time stop** — Close if the underlying has not moved as expected by the short leg's mid-life (e.g., 50% of DTE elapsed).
5. **Vol regime change** — Term-structure inversion mid-trade is a strong exit signal; the calendar's edge has flipped.

## Implementation Pseudocode

```python
def ratio_calendar_spread(
    underlying: str,
    direction: str,           # "bullish" | "bearish" | "neutral"
    vol_view: str,            # "term_compression" | "term_expansion" | "neutral"
    ratio: tuple[int, int],   # (long_qty, short_qty), e.g. (2, 1) or (1, 3)
    near_dte: int,
    far_dte: int,
    strike_method: str,       # "atm" | "directional_otm"
):
    chain = get_options_chain(underlying)
    iv_term = get_iv_term_structure(underlying)

    # Term-structure precondition for standard direction
    if iv_term.front > iv_term.back * 1.05:
        warn("Backwardation — standard short-near/long-far calendar fights the curve")

    # Select strikes
    if strike_method == "atm":
        strike_short = chain.atm_strike()
        strike_long = chain.atm_strike()
    else:
        strike_short = chain.delta_strike(0.30 if direction == "bullish" else -0.30)
        strike_long = chain.delta_strike(0.40 if direction == "bullish" else -0.40)

    long_qty, short_qty = ratio

    # Build the spread
    legs = [
        Leg(
            action="BUY", strike=strike_long,
            expiry=today + far_dte, qty=long_qty,
            right="C" if direction == "bullish" else "P",
        ),
        Leg(
            action="SELL", strike=strike_short,
            expiry=today + near_dte, qty=short_qty,
            right="C" if direction == "bullish" else "P",
        ),
    ]
    net_cost = sum(l.cost for l in legs)
    return Order(legs=legs, net_cost=net_cost)
```

## Indicators / Data Used

- Options chain with full Greeks (delta, gamma, vega, theta) per strike per expiration
- [[implied-volatility-term-structure|IV term structure]] (front month, mid, back month)
- IV rank or IV percentile of the underlying
- Earnings and corporate event calendar
- Forward dividend schedule (for ratio calls on dividend payers)
- Expected catalyst dates relative to near and far expirations

## Payoff & Greeks

The ratio calendar's payoff is the defining feature that makes it harder to manage than a vertical: because the two legs expire at *different times*, there is no single static payoff diagram. The shape shown below is the **at-near-expiration** payoff (the moment the short leg dies and the structure collapses to a residual long-options position). Before that moment the marks are driven by the difference in [[theta]] decay rates and the relative [[vega]] of the two tenors.

Long-heavy (1:2) calendar, near-leg expiration payoff (call version, ATM short strike K):

```
   P&L
    |                                   *
    |                                  *   <- long back-month legs run after
    |                                 *       short leg dies -> uncapped upside
    |              ___               *
    |            /     \           *
    |          /         \       *
  0 +--------/-------------\----*--------------  spot at near expiry
    |       /  (credit zone  \  
    |      /   around K)       \   <- net debit drag if spot runs far
    |    (debit) ____________ K _____________
```

Net Greeks evolve in two phases. The table contrasts the two dominant tilts:

| Greek | Long-heavy 1:2 (convexity) | Short-heavy 2:1 (income) |
|---|---|---|
| [[delta]] | Small near entry; grows toward the long-leg direction after the short dies | Small near entry; converts to a directional short if a side is breached |
| [[gamma]] | Slightly short before near-expiry (short near-leg gamma dominates), flips **long** once the short leg expires | Net short — the income killer; a gap move past the short strikes hurts before the far wing helps |
| [[theta]] | Mildly negative early (paying for the long back-month), turns the residual into a pure time-decay liability after the short closes | **Positive** — the whole point; collects more near-leg decay than the single far leg pays |
| [[vega]] | Net **long** — benefits from a rise in back-month [[implied-volatility]] / term-structure steepening | Net **short** — benefits from IV compression; hurt by a vol spike until the far wing offsets |

The single most important fact: a long-heavy ratio calendar is **short gamma / long vega before the near expiry and long gamma / long vega after it**. Misreading which phase you are in is the classic way to mis-hedge this structure (see "What Kills This Strategy"). The [[volatility-risk-premium|VRP]] is harvested through the negative-theta-to-positive-theta transition of the near leg, while the term-structure view is expressed through net vega.

## Example Trade

**Long-heavy 1:2 ratio calendar on AAPL, bullish thesis, contango term structure.**

- 5 February 2026: AAPL trading at $185. Near-month (Mar) IV at 22%, back-month (May) IV at 26% — contango.
- Earnings on May 1 — within back-month, after front-month.
- Trade: SELL 1 AAPL March $190 call at $3.50, BUY 2 AAPL May $190 calls at $5.50 each.
- Net cost: -$3.50 + $11.00 = $7.50 debit per spread (plus commissions).
- 28 February: AAPL drifts to $187, March $190 call decays to $0.85. Buy back for $0.85 (75% credit captured = $2.65). Banked credit: $2.65.
- Position now: long 2 AAPL May $190 calls at adjusted basis of ($11.00 - $2.65) = $8.35 / 2 = $4.175 each.
- Earnings beat on May 1 sends AAPL to $200. May $190 calls jump to $13.00. Close at $26.00 total. Net P&L: $26.00 - $8.35 = $17.65 = +211% on the adjusted basis (+235% on the initial $7.50 debit).

## Performance Characteristics

Indicative expectations for liquid US large-caps and index options, derived from published calendar-spread research and the persistent [[volatility-risk-premium|VRP]] (estimates with a realistic cost overlay — no verified composite backtest exists for the ratio variant; `backtest_status: untested`):

- Long-heavy variant (1:2): ~60-65% win rate, profit factor ~1.4-1.6, [[sharpe-ratio|Sharpe]] 0.8-1.2 net of costs. Average winners are larger than average losers because the long leg's convexity caps the downside at the net debit.
- Short-heavy variant (2:1): ~78% win rate, much smaller average winner relative to average loser, profit factor 1.2-1.4, Sharpe 0.5-0.8 with tail-risk overlay required.
- Costs: 2-bps per trade for liquid SPX/SPY/QQQ; 5-15 bps for single names with mid-market crossing.
- Drawdown profile: long-heavy variants drawdown -10 to -15% in low-vol regimes (theta drag dominates); short-heavy variants drawdown -25 to -40% in vol-spike regimes (the wing far-leg is insufficient).

### Variant fit by market regime

The ratio is a free parameter precisely so it can be tuned to the prevailing [[market-regime]]. Matching the tilt to the regime is the difference between edge and noise:

| Regime / term structure | Preferred tilt | Why |
|---|---|---|
| Steep contango, range-bound underlying | Short-heavy (2:1) | Harvest near-leg [[theta]]; IV compression helps the net-short [[vega]] |
| Contango, directional catalyst expected after near expiry | Long-heavy (1:2) | Net debit funds convex back-month exposure into the catalyst |
| Backwardation (front IV > back IV) | Reverse calendar or stand aside | Standard short-near/long-far fights the curve — see Entry Rule 2 |
| Vol-spike / crisis | Avoid short-heavy entirely | The far wing is too slow to offset a fast gap; tail risk resembles a [[short-strangle]] |

## Capacity Limits

- Per-name capacity is bounded by the open interest at the chosen strikes; for liquid US large-caps this is typically $5-25M of premium.
- Index-options capacity (SPX, NDX) is effectively unlimited for retail and small-institutional sizes.
- For book-level deployment, capacity scales with the diversification of name selection and expiration laddering. A diversified 10-position book on liquid names can run $50-100M before market impact dominates.

## What Kills This Strategy

Drawing from [[failure-modes]]:

1. **Term-structure inversion mid-trade** — A vol spike inverts contango into backwardation; the calendar's structural edge flips. Long-heavy variants get crushed (long-vega leg gets less benefit than the short-vega leg loses) when the curve re-flattens.
2. **Wrong-ratio regime** — Running long-heavy ratios in a steep contango / range-bound regime drains theta; running short-heavy ratios in a vol-spike regime exposes the residual short to catastrophic loss before the wing kicks in.
3. **Liquidity collapse on the back leg** — Single-name back-month options can have wide spreads, particularly on smaller-cap names. Repair operations cost 2-3x the entry slippage.
4. **Pin risk at near-leg expiration** — If the underlying pins close to the short strike on expiration day, gamma explodes. Standard rule: close the short leg before expiration week, never let it run to settlement.
5. **Ratio drift from corporate actions** — Stock splits, special dividends, and mergers adjust contracts non-uniformly across expirations and can leave the ratio mismatched.

## Kill Criteria

- Strategy realised Sharpe < 0 over rolling 6 months → suspend.
- Three consecutive trades close at >2x intended max-loss → reduce size by half and audit ratio selection logic.
- Term-structure regime persistently inverted (front-month IV > back-month for >30 days) → switch from long-heavy to short-heavy variant or pause the strategy.
- See [[when-to-retire-a-strategy]] for the formal retirement framework.

## Advantages

- Highly customisable via ratio choice — one structure expresses many views.
- Can be set up for net credit (income) or net debit (convexity) depending on tilt.
- Carries a positive structural edge from [[volatility-risk-premium|VRP]] in the short leg.
- Long-heavy variant has *capped downside* (the net debit) and uncapped upside on the long leg.
- Lower cost basis than a pure long-options bet because the short leg subsidises premium.

## Disadvantages

- Greeks profile shape-shifts dramatically as the near leg decays — easy to misjudge net exposure.
- Short-heavy variants have the same uncapped tail risk as a [[short-strangle]] until the long-wing provides protection.
- Requires platform support for multi-leg ratio orders; some retail brokers won't allow ratio fills.
- Margin treatment varies by broker; under Reg-T some ratios get treated as naked positions.
- Difficult to model historically because the ratio is a free parameter — backtests are easy to overfit. See [[overfitting-detection]].

## Sources

- [[options-portfolio-construction]] — book-level treatment.
- McMillan, *Options as a Strategic Investment* (5th ed.) — Chapter on calendar and diagonal spreads.
- Natenberg, *Option Volatility & Pricing* — pp. 200-235 on calendar spread Greeks and term-structure.
- Cboe educational materials on calendar and ratio spreads.

## Related

- [[calendar-spread]] — the 1:1 parent structure
- [[diagonal-spread]] — calendar with different strikes
- [[ratio-spread]] — same-expiration ratio (sibling structure)
- [[implied-volatility-term-structure]] — the curve the trade is built on
- [[volatility-risk-premium]] — the structural edge
- [[short-strangle]], [[iron-condor]] — short-vol siblings
- [[managing-winners]], [[trade-repair-and-rolling]] — exit and repair frameworks
- [[options-portfolio-construction]] — fitting ratio calendars into a book
- [[market-regime]] — the regime determines which ratio tilt to run
- [[theta]], [[vega]], [[delta]], [[gamma]] — the Greeks that shape-shift across the near expiry
