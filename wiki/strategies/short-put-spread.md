---
title: "Short Put Spread"
type: strategy
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, derivatives, volatility, swing-trading]
aliases: ["Bull Put Spread", "Put Credit Spread", "Vertical Put Credit Spread", "Short Put Vertical"]
strategy_type: quantitative
timeframe: swing
markets: [stocks, options]
complexity: intermediate
backtest_status: cost-corrected
edge_source: [risk-bearing, behavioral, structural]
edge_mechanism: "Sell ATM/ITM put + buy further-OTM put; collect premium on a defined-risk, bullish-biased structure. The seller harvests put-skew variance risk premium with a hard floor on max loss."
data_required: [options-chain, implied-volatility-surface, ivr, ohlcv-daily, earnings-calendar]
min_capital_usd: 5000
capacity_usd: 500000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.25
breakeven_cost_bps: 25
related: ["[[options-premium-selling]]", "[[premium-selling-systematic]]", "[[short-volatility-strategies]]", "[[iron-condor]]", "[[short-strangle]]", "[[cash-secured-puts]]", "[[credit-spread]]", "[[put-spread]]", "[[long-vol-overlay]]", "[[long-vol-vs-short-vol]]", "[[variance-risk-premium]]", "[[vega-budgeting]]", "[[ivr]]", "[[skew]]", "[[itpm-framework]]"]
---

A short put spread (also "bull put spread" or "put credit spread") sells a higher-strike put and simultaneously buys a lower-strike put with the same expiration. The result is a **defined-risk, bullish-biased, short-vol** structure: the trader collects a credit and is profitable if the underlying stays above the short strike at expiration. It is the canonical defined-risk implementation of bullish premium selling, sitting between [[cash-secured-puts]] (capital-intensive, undefined notional) and [[short-strangle]] (capital-efficient, undefined risk). The structure features prominently in [[premium-selling-systematic]] when traders want a directional tilt without naked tail.

## Edge source

**Risk-bearing**, **behavioral**, **structural**.

- Like all premium-selling, the spread captures the [[variance-risk-premium]].
- Specifically harvests the **put-skew premium** -- equity puts are persistently more expensive than calls of equivalent moneyness due to crash insurance demand.
- The defined-risk structure trades expected return for tail control: it surrenders some VRP to cap the tail.

## Why this edge exists

Same persistent buyers as the broader [[options-premium-selling]] family: pension funds, insurance companies, retail crash-protection buyers. The put credit spread specifically is favored by:

- Retail traders who want bullish exposure with defined risk and lower buying-power use than [[cash-secured-puts]].
- Income strategies in 401(k)-style accounts that disallow naked options.
- Allocators running [[itpm-framework|ITPM]]-style books where every position must have explicit max loss for [[risk-budgeting]].

The buyer of the spread (in aggregate, the long-put hedger) does not differentiate between buying a single OTM put and a put spread, so the seller can still extract VRP across the structure.

## Null hypothesis

If implied vol equaled subsequently realized vol AND skew were flat (no crash premium), the spread would earn zero before costs. Under flat skew, the long wing fully offsets the short put on average. Empirically equity skew is steep and persistent, so the seller of the spread harvests both vol-level and skew premium.

## Rules

**Universe:** SPX, SPY, QQQ, IWM as primary; large-cap single names with deep options markets as satellite.

**Entry:**

- **DTE 30-45.**
- **Short put strike:** 20-30 [[delta]] (slightly OTM to ATM, NOT 16-delta -- the wider 20-30 delta short captures more credit at the cost of a higher loss probability, which is the directional-bias intent).
- **Long put strike:** 5-10 delta, typically $5-$10 lower (SPY) or $20-$50 lower (SPX) below the short strike.
- **Net credit:** target at least 25-33% of spread width. Below this, the risk-reward is not worth it.
- **[[ivr]] >= 30** required.
- **No earnings or major macro event** within next 7 days for index; within DTE for single names.
- **Bias:** the short put spread expresses a bullish-to-neutral view. Combine with a short call spread (= [[iron-condor]]) for fully neutral exposure.

**Position sizing:**

- Per-trade max loss capped at **2% of NAV** (smaller than naked structures because spreads are smaller credits).
- Aggregate short vega capped per [[vega-budgeting]] rules.

**Exit:**

- **Close at 50% of max profit** mechanical (or **50-75% for tighter spreads**).
- **Close at 21 DTE** if not at profit target.
- **Stop-loss at 200% of credit collected** (i.e., loss = 2x the credit).
- **Tested-strike management:** if the short strike is breached and trade is still in profit window, may roll spread down + out one time, never more.

## Implementation pseudocode

```python
def short_put_spread_loop(book, market, underlying):
    # 1. Process open spreads
    for trade in book.short_put_spreads:
        if trade.pct_max_profit_realized() >= 0.50:
            book.close(trade, reason="50pct_profit_target")
        elif trade.dte() <= 21:
            book.close(trade, reason="21dte_time_exit")
        elif trade.pnl_dollars() <= -2.0 * trade.credit_collected:
            book.close(trade, reason="2x_credit_stoploss")

    # 2. Entry gate
    if market.ivr(underlying) < 30:
        return
    if market.event_within_7d(underlying):
        return
    if book.short_vega() > book.vega_budget():
        return

    # 3. Build spread
    spot = market.price(underlying)
    short_strike = market.strike_at_delta(underlying, dte=45, delta=-0.25)  # 25-delta short
    long_strike = market.strike_at_delta(underlying, dte=45, delta=-0.07)   # ~7-delta long wing
    credit = market.spread_credit(underlying, 45, short_strike, long_strike)
    width = short_strike - long_strike

    if credit / width >= 0.25:  # at least 25% of width
        max_loss = (width - credit) * 100  # per spread, in dollars
        contracts = min(
            book.nav() * 0.02 / max_loss,        # 2% NAV cap per trade
            book.bp_available() / max_loss,
        )
        book.open_short_put_spread(
            underlying, 45, short_strike, long_strike, contracts
        )
```

## Indicators / data used

- [[options-chain]] with greeks for the underlying.
- [[ivr|IV Rank]] (252-day).
- [[skew]] and term-structure surfaces.
- Earnings/macro event calendars.
- [[realized-volatility]] tracker.
- Portfolio-aggregate vega and delta exposures.

## Payoff & Greeks

The short put spread has a **two-step, capped payoff**: full credit retained above the short strike, a linear loss zone between the strikes, and a flat max-loss floor at and below the long strike. The long wing is what turns the open-ended short-put tail into a known rectangle of risk.

```
Short put spread P&L at expiration

 +credit ┤                       ┌────────────────  (price ≥ Ks: keep full credit)
         │                      /
    0  ──┼─────────────────────/───────────────────
         │                    / breakeven = Ks − credit
 −maxloss┤━━━━━━━━━━━━━━━━━━━━/   (price ≤ Kl: max loss = width − credit)
         └──────────────────────────────────────────
              Kl(long)      Ks(short)
         max_loss = (Ks − Kl) − net_credit     (× 100 per contract)
         breakeven = Ks − net_credit
```

Net Greeks (a defined-risk, bullish-tilted short-vol position):

| Greek | Sign | Comment |
|---|---|---|
| [[delta]] | **positive** (bullish) | the 20-30 delta short strike gives a deliberate long-bias; this is the directional intent vs a neutral [[iron-condor]] |
| [[gamma]] | **negative**, but capped | gamma grows as price approaches the short strike, but the long wing caps how bad it gets near/through Kl |
| [[theta]] | **positive** | the daily income leg; smaller in absolute terms than a naked put because the long wing pays out some theta |
| [[vega]] | **negative**, muted | net short vega, but the long wing offsets a chunk of it — this is why spreads behave better than naked structures in a [[vega]]/IV-shock reprice |

Because the long wing absorbs part of every Greek, the short put spread is a **tamed** version of [[options-premium-selling]]: less credit, less theta, less vega — but a hard, known loss ceiling. The Greeks all sit between a naked [[cash-secured-puts|short put]] and a fully neutral [[iron-condor]]. See [[iv-crush]] for the favourable post-event vega move and [[skew]] for why the put side specifically carries extra premium.

## Example trade

*Illustrative -- not a recommendation.*

- **Date:** 2026-04-15. SPY = 520, SPY IVR = 35.
- **Trade:** Sell SPY 510 / Buy SPY 500 put spread, 45 DTE.
  - Short SPY 510 put (~25 delta) at $4.50 = $450 credit.
  - Long SPY 500 put (~10 delta) at $1.80 = -$180 cost.
  - **Net credit per spread:** $2.70 = $270.
  - **Spread width:** $10 = $1,000 max loss.
  - **Max loss per spread:** $1,000 - $270 = $730.
  - Credit / width: 27% -> passes the 25% gate.
- **Sizing:** $250K NAV x 2% per-trade cap = $5,000 max loss capacity. $5,000 / $730 = ~6 spreads. Trade 5 spreads to leave headroom = $1,350 credit, $3,650 max loss.
- **Outcome:** SPY drifts to 525 at 25 DTE; spread marked at $1.30 = ~52% of max profit. **Close.**
- **Realized P&L:** $1.40 per spread x 5 x 100 = $700 profit in 20 days. ~19% return on max-loss capital, ~340% annualized if continuously redeployed.

## Performance characteristics

- **Calm-regime gross return:** 6-10% NAV per year on capital allocated to the strategy.
- **Net return (with [[long-vol-overlay]]):** 4-8% NAV.
- **Hit rate:** 70-85% of trades profitable; 75-90% of months profitable.
- **Win/loss ratio:** typical wins are 50% of credit; typical losses are 1.5-2x credit. The structure's "edge" is the gap between win frequency (high) and average loss size (controlled by the long wing).
- **Sharpe (calm regime):** 1.2-2.0.
- **Sharpe (full cycle, defined-risk advantage included):** 0.6-1.0 -- meaningfully better than naked premium structures across cycle because of capped tail.
- **Max drawdown:** 15-25% with discipline; bounded by spread width x position count regardless of vol shock.
- **Worst-day shock:** the spread's max loss is capped, so a [[volmageddon|Feb 2018]]-style event maxes out at the pre-defined position-count loss -- typically 5-15% of NAV for a properly sized book versus 50-100% for the naked equivalent.

### Regime conditioning

The bullish tilt makes this structure more [[market-regime|regime]]-sensitive than a neutral condor:

| [[market-regime\|Regime]] | Behaviour | Action |
|---|---|---|
| Bull / calm uptrend | the ideal tape; short strike never tested | normal sizing |
| High-IVR, range-bound | rich credits, capped tail | best entries |
| Choppy / sideways bear | short strike repeatedly tested; defined-risk losses cluster | reduce size; tighten credit/width gate |
| Sustained downtrend | steady bleed even with defined risk; bullish bias is wrong-footed | stand aside or invert to short call spreads |
| Vol shock | max loss caps the damage — the structure's whole reason to exist | overlay still recommended at portfolio level |

Versus the parent [[options-premium-selling]] and the neutral [[iron-condor]], the short put spread gives up symmetry for a directional bet that the underlying does not fall hard — so a persistent bear market is its specific weakness, not a vol shock (which is capped).

## Capacity limits

- **Index spreads (SPX, SPY, QQQ):** capacity is large but lower than naked strangles because each spread uses defined buying power.
- **Single-name capacity** is much tighter; bid-ask drag on the long wing dominates above $5-20M.
- The capacity-binding constraint is the **long wing's liquidity** -- 5-delta puts can have wide spreads on less-liquid names.

## What kills this strategy

1. **Gap below long strike** -- max loss realizes immediately. A 10%+ overnight gap through the spread maxes the loss.
2. **Selling into compressed VRP** -- low [[ivr]] entries earn too little credit relative to max loss. Trade quality degrades.
3. **Skew shift** -- if equity skew flattens, put spreads become structurally less attractive. Watch [[skew-rank]] alongside IVR.
4. **Discretionary roll-out** -- rolling losing spreads to later expirations multiplies loss size and converts a defined-risk loss into an undefined-time loss.
5. **Pin risk** at expiration -- holding to expiration with the underlying near short strike creates assignment uncertainty. Mechanical 21-DTE close avoids this.
6. **Ex-dividend assignment** on single names -- short ITM puts can be assigned around dividend dates; close before ex-div to avoid.
7. **Overcrowding into 0-7 DTE put credit spreads** -- the recent retail explosion in zero-day put spreads has crowded the very short tenors. Stick to 30-45 DTE.

## Kill criteria

- **Strategy drawdown >= 20%** -> halve size; **>= 30%** -> halt new entries.
- **Rolling 12-month Sharpe < 0** with 9+ months of data -> halt.
- **Average credit / width fall below 20%** for 3+ consecutive months -> compressed VRP/skew; halt and review.
- **Round-trip cost > 30 bps of credit** -> review; > 50 bps -> retire.
- **Loss exceeds 2x credit on more than 30% of trades** in a quarter -> rule set or sizing is broken; halt.

## Advantages

- **Defined risk** -- max loss known at trade entry, eliminating tail-shock catastrophe.
- **Lower buying-power use** than [[cash-secured-puts]] for similar bullish exposure.
- **Permitted in retirement accounts** that disallow naked options.
- **Mechanically simple** -- two-leg structure, easy to enter/manage.
- **Pairs cleanly with short call spreads** to form an [[iron-condor]].
- **Lower vega exposure** than naked equivalents -- behaves better under [[portfolio-margin]] vol-shock repricing.
- Fits cleanly into [[premium-selling-systematic]] rules.

## Disadvantages

- **Lower expected return per dollar of capital** than naked structures (the long wing costs premium).
- **Wins are smaller** -- 50% of credit is a smaller absolute dollar amount than for a naked strangle.
- **Long-wing slippage** can erode credit, especially on single names and in stress.
- **Still negative-skew within max-loss bound** -- losses are 1.5-3x typical wins.
- **Bullish bias** -- in a sustained bear market, the strategy bleeds steadily even with defined risk.
- **Pin and assignment risk** at expiration.

## Sources

- [[tastytrade]] research archive -- credit-spread mechanics and rule-set calibration.
- [[itpm-framework]] -- the defined-risk discipline overlay.
- Carr, Peter and Wu, Liuren. "Variance Risk Premiums" (2009).
- Bondarenko, Oleg. "Why Are Put Options So Expensive?" (2014).
- Cboe research on [[skew]] persistence and put-credit-spread performance.
- [[volmageddon]] and [[vix-august-2024-spike]] post-mortems -- empirical evidence on defined-risk vs naked outcomes.

## Related

- [[options-premium-selling]] -- the parent strategy.
- [[premium-selling-systematic]] -- systematic implementation that includes this structure.
- [[short-volatility-strategies]] -- the category survey.
- [[iron-condor]] -- short put spread + short call spread combined.
- [[short-strangle]] -- the undefined-risk equivalent.
- [[cash-secured-puts]] -- the capital-intensive equivalent.
- [[credit-spread]] / [[put-spread]] -- structural family.
- [[long-vol-overlay]] -- the overlay that turns this into a survivable book.
- [[long-vol-vs-short-vol]] -- the comparison context.
- [[variance-risk-premium]] -- the underlying premium.
- [[vega-budgeting]] -- sizing framework.
- [[skew]] -- secondary edge source.
- [[iron-fly]] -- the high-theta ATM defined-risk sibling.
- [[calendar-spread]] -- the long-vega complement for low-IV regimes.
- [[iv-crush]] -- the post-event vega tailwind for short-premium spreads.
- [[theta]] / [[vega]] / [[gamma]] -- the Greeks that define the structure's profile.
- [[market-regime]] -- regime conditioning for the bullish tilt.
- [[wash-sale-rules-options]] -- tax interaction when rolling losing spreads on single names.
- [[itpm-framework]] -- institutional discipline.
