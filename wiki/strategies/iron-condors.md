---
title: "Iron Condor"
type: strategy
created: 2026-04-15
updated: 2026-06-20
status: excellent
tags: [options, derivatives, risk-management, volatility, swing-trading]
aliases: ["Iron Condors", "IC"]
strategy_type: technical
timeframe: swing
markets: [stocks, options]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "Sells volatility premium to hedgers and speculators who overpay for tail protection; profits when realized volatility is lower than implied"
data_required: [options-chain, implied-volatility, ohlcv-daily]
min_capital_usd: 10000
capacity_usd: 50000000
crowding_risk: high
expected_sharpe: 0.5
expected_max_drawdown: 0.20
breakeven_cost_bps: 20
related: ["[[iron-butterfly]]", "[[credit-spread]]", "[[vertical-spread]]", "[[bull-put-spread]]", "[[bear-call-spread]]", "[[options-greeks]]", "[[theta]]", "[[gamma]]", "[[vega]]", "[[trade-repair-and-rolling]]", "[[wheel-strategy]]", "[[hedging]]", "[[variance-risk-premium]]", "[[implied-volatility]]"]
---

An iron condor is an [[options|options]] strategy that combines a [[bull-put-spread|bull put spread]] and a [[bear-call-spread|bear call spread]] on the same underlying with the same expiration, creating a range-bound position that profits when the underlying stays between the two short strikes. It is a defined-risk, premium-selling structure with mathematically capped maximum loss at entry — the seller is paid a credit up front in exchange for bearing the risk of a large move in either direction.

## Overview

The iron condor is one of the most popular neutral options strategies among income-oriented traders. It expresses the view that the underlying will trade within a defined range over the life of the options. The strategy collects premium from selling both a put spread and a call spread, and that premium is the maximum profit. The maximum loss is the width of either spread minus the total premium collected.

Iron condors are widely used because they offer high probability of profit (typically 60–80% depending on strike selection), defined risk, and benefit from [[theta|time decay]] working in the seller's favor. They are a cornerstone of short-premium portfolios and are commonly traded on broad indices (SPX, RUT, NDX) and high-liquidity stocks.

## Edge source

**Risk-bearing**, with a secondary **behavioral** component (see [[edge-taxonomy]]).

- *Risk-bearing*: the condor seller is paid the [[variance-risk-premium]] — compensation for absorbing the risk that realized volatility exceeds implied volatility. This is the same economic premium earned by insurance underwriters: a steady stream of small payments punctuated by occasional large payouts.
- *Behavioral*: option buyers systematically overpay for out-of-the-money strikes (the "lottery ticket" and "crash insurance" biases), which steepens the volatility smile and fattens the credit available to condor sellers at the wings.

## Why this edge exists

Index [[implied-volatility]] has historically exceeded subsequently realized volatility in the large majority of months — the variance risk premium. The buyers on the other side of an iron condor are (a) institutional hedgers buying OTM puts as portfolio insurance, who are mandated or behaviorally driven to pay above actuarial value for protection, and (b) retail speculators buying OTM calls and puts as cheap leveraged directional bets, who systematically overpay for convexity. Both groups keep "losing" in expectation because they are not trying to win in expectation: hedgers are buying insurance (utility, not expected value), and lottery-ticket buyers exhibit a documented preference for positive skew. The condor seller is the insurer collecting that premium, and the edge persists because the demand for tail protection and leveraged upside is structural, not informational.

The edge is real but modest and crowded: short-premium strategies have proliferated since the 2010s, and the premium available at any given delta has compressed relative to the pre-2008 era.

## Null hypothesis

If implied volatility equaled future realized volatility (no variance risk premium), the iron condor's expected P&L would be exactly zero before costs and negative after costs. A 70%-probability condor would win its small credit 70% of the time and lose its larger max-loss-side amount 30% of the time, summing to zero edge — the high win rate is *not* evidence of edge by itself. The null-hypothesis test for any condor backtest is therefore: does the strategy outperform a delta-equivalent random short-strangle baseline after realistic costs, and does the net P&L exceed what the win/loss ratio alone would mechanically produce under IV = RV?

## Rules

### Entry
- Underlying: high-liquidity index options (SPX, RUT, NDX) or top-tier large caps with penny-wide option markets
- Open at **40–50 DTE** (the sweet spot where theta is meaningful but gamma is still tame)
- Sell short strikes at roughly **15–20 delta** on each side (≈ 60–70% probability the underlying stays inside)
- Buy wings **5–10 points further OTM** (index) to define risk; target a credit of roughly **one-third of the wing width**
- Prefer entries when **IV rank > 30–50** — elevated implied volatility inflates the credit and improves risk/reward
- Avoid expirations that span earnings or known binary events (FOMC, CPI on short-dated condors)

### Exit
- **Profit target**: close at **50% of max profit** to reduce time exposure and gamma risk
- **Loss limit**: close at **2× the credit received** to cap realized losses before max loss is reached
- **Time stop**: close or roll at **~21 DTE** regardless of P&L (see The 21-Day Rule below)

### Position sizing
- Risk no more than **1–2% of portfolio equity** per iron condor (max loss is known at entry, making sizing straightforward) (Source: [[recovering-losing-options-positions]])
- No more than **15–20% of capital** in a single underlying; spread condors across underlyings, sectors, and expirations (Source: [[recovering-losing-options-positions]])

## Implementation pseudocode

```python
# Systematic iron condor on index options
PARAMS = dict(dte_open=45, short_delta=0.16, wing_width=10,
              profit_take=0.50, loss_limit=2.0, dte_close=21,
              risk_per_trade=0.02, min_iv_rank=30)

def daily_scan(portfolio, chain, iv_rank):
    # --- entries ---
    if iv_rank >= PARAMS["min_iv_rank"] and not earnings_within(chain.expiry):
        exp = nearest_expiry(chain, PARAMS["dte_open"])
        sp = strike_at_delta(exp.puts,  -PARAMS["short_delta"])   # short put
        sc = strike_at_delta(exp.calls,  PARAMS["short_delta"])   # short call
        lp, lc = sp - PARAMS["wing_width"], sc + PARAMS["wing_width"]
        credit = mid(sell=[sp, sc], buy=[lp, lc])
        max_loss = PARAMS["wing_width"] - credit
        qty = floor(portfolio.equity * PARAMS["risk_per_trade"] / (max_loss * 100))
        if credit >= PARAMS["wing_width"] / 3 and qty >= 1:
            open_condor(qty, lp, sp, sc, lc, exp)

    # --- exits / management ---
    for pos in portfolio.condors:
        if pos.pnl >= PARAMS["profit_take"] * pos.credit:        close(pos)
        elif pos.pnl <= -PARAMS["loss_limit"] * pos.credit:      close(pos)
        elif pos.dte <= PARAMS["dte_close"]:                     close_or_roll(pos)
        elif breached(pos.short_put) or breached(pos.short_call):
            roll_untested_side(pos)   # collect extra credit against the tested side
```

## Indicators / data used

- **Full options chain** with bid/ask, deltas, and open interest (strike selection and liquidity screening)
- **[[implied-volatility|Implied volatility]] and IV rank/percentile** (entry filter and premium richness gauge)
- **Realized volatility** of the underlying (sanity check that IV > RV — the premium actually exists)
- **Earnings and macro event calendar** (avoid binary events inside the expiration window)
- **Underlying OHLCV** for breach monitoring and trend filters

## Payoff & Greeks

### Payoff sketch (at expiration)

The iron condor is a flat-topped tent: maximum profit (the full net credit) across the entire range between the two short strikes, sloping down to a flat maximum loss outside each long strike. The two breakevens sit inside the long strikes by the amount of credit collected.

```
 P/L
  │        ┌──────────────────┐                ← max profit = net credit
  │       /                    \
 0│──────/──────────────────────\─────────────  spot →
  │     /│                      │\
  │    / │                      │ \
  │___/  │                      │  \___________  ← max loss = wing width − credit
       LP SP                    SC LC
   (long  short            short long
    put)  put              call  call)

  breakevens: SP − credit  and  SC + credit
  profit zone: between the two short strikes (SP … SC)
```

The structure is **delta-neutral at entry, short [[gamma]], short [[vega]], and long [[theta]]** — the canonical short-premium signature. It earns a little every calm day and is exposed to a sudden loss if the underlying trends hard toward either wing.

### Net-Greeks table (at/near entry)

| Greek | Sign / magnitude | Behaviour over the trade's life | Implication |
|-------|------------------|---------------------------------|-------------|
| [[delta]] | ≈ 0 (balanced wings) | Drifts toward the tested side as spot approaches a short strike | No directional bias at entry; becomes directional under stress |
| [[theta]] | Positive (small, steady) | Accelerates into the final ~21 days | Time decay is the income; this is why the seller waits |
| [[vega]] | Negative | Largest near entry; shrinks as DTE falls | Profits when [[implied-volatility|IV]] contracts; an IV spike creates immediate unrealised loss even with spot unchanged |
| [[gamma]] | Negative (largest near each short strike and near expiry) | Scales ≈ 1/√t — explodes in the last weeks | The "gamma trap": delta accelerates against you as price nears a short strike |

The primary risk of an iron condor is a large directional move that pushes the underlying through one of the short strikes. Negative [[gamma]] means that as the stock moves toward a short strike, delta accelerates against the position — the "gamma trap" — and the negative-[[vega]] exposure compounds the pain because the move usually arrives with an IV spike. This [[theta]]-positive / [[gamma]]-negative / [[vega]]-negative profile is shared with the [[short-strangle|strangle]] and [[iron-fly|iron fly]]; the condor simply caps the tails with the long wings. See [[managing-winners]] for the discipline that exits before the gamma/theta trade-off turns hostile.

## Example trade

Stock at $100, 45 DTE:
- Buy $90 put for $0.80
- Sell $95 put for $1.80
- Sell $105 call for $1.60
- Buy $110 call for $0.60

**Net credit**: ($1.80 − $0.80) + ($1.60 − $0.60) = **$2.00**
**Max profit**: $2.00 (if stock stays between $95 and $105 at expiry)
**Max loss**: $5.00 (spread width) − $2.00 (credit) = **$3.00** per share
**Breakeven**: $93 on the downside, $107 on the upside

Management path: three weeks later the stock has drifted to $102 and the condor can be bought back for $1.00 — a $1.00 gain, which is 50% of max profit. The 50% profit-take rule says close here rather than hold the remaining $1.00 of premium through the high-gamma final weeks.

## Performance characteristics

- **Win rate**: 60–80% by construction (a function of short-strike delta), but average loss exceeds average win — the P&L distribution is negatively skewed
- **Expected return**: systematic index-condor programs net of costs historically deliver modest single-digit annual returns on allocated capital with **net Sharpe in the ~0.3–0.7 range**; this page assumes **0.5** as the planning figure. CBOE publishes a benchmark (CNDR, the S&P 500 Iron Condor Index) that illustrates the profile: lower volatility than the index, modest absolute returns, and sharp drawdowns in volatility shocks
- **Cost overlay matters**: four legs per entry plus closing trades means **8 option fills per round trip**. On retail commissions (~$0.65/contract) plus realistic slippage (1–5 cents per leg on penny-wide index markets, more on equities), costs commonly consume **10–20% of the gross credit**. The strategy can absorb roughly **20 bps round-trip** on the underlying notional before the edge disappears; wider markets than that make small condors uneconomic
- **Drawdown profile**: long stretches of steady gains interrupted by abrupt losses during volatility spikes — e.g., February 2018 ("Volmageddon") and March 2020 produced multi-month max-loss clusters for short-premium sellers. A **15–25% peak-to-trough drawdown** is a realistic planning assumption for a 1–2%-risk-per-trade program; frontmatter assumes 20%

## Capacity limits

Index options are among the deepest derivatives markets in the world — SPX options alone trade millions of contracts daily — so a systematic condor program scales further than most retail strategies. Practical limits arrive from the OTM wings, not the short strikes: far-OTM long options have thinner markets, and a program rolling **>$50M of notional risk** at the same deltas and tenors will begin moving the wing quotes and paying materially wider spreads. Single-stock condors hit capacity far sooner (low millions per name). Frontmatter capacity assumes $50M for an index-focused program.

## What kills this strategy

- **Volatility regime shift**: a sustained move from low-vol to high-vol regime produces clustered max losses faster than credits can rebuild (Feb 2018, Mar 2020). This is the dominant failure mode (see [[failure-modes]])
- **Variance risk premium compression**: crowding by short-vol funds and systematic premium sellers shrinks the credit available at a given delta until it no longer covers the tail
- **Gamma trap mismanagement**: holding tested condors into the final weeks, where small moves cause violent P&L swings
- **Event risk**: earnings or macro binaries inside the expiration window that gap through a short strike overnight, denying any chance to adjust
- **Cost creep**: on small accounts or wide-market underlyings, commissions and slippage silently consume the entire edge

## Kill criteria

Retire or pause the strategy if any of the following trigger:

- Portfolio drawdown from condor book exceeds **20%**
- Rolling **12-month net Sharpe < 0** (the premium is no longer being paid)
- Average collected credit at 16-delta falls below **25% of wing width** for 3+ consecutive months (premium compression — risk/reward no longer viable)
- Two consecutive max-loss clusters (≥3 max losses in a month) without an identifiable, transient volatility event

## Adjustments and rolling

Iron condors require active management when one side is tested (the underlying approaches or breaches a short strike). The key adjustment techniques:

### Rolling the untested side

When one side is breached, institutional traders often roll the *untested* side closer to the stock price to collect additional premium that offsets the tested side's loss. In extreme moves the untested short strike can even be rolled past the tested one, locking in a defined maximum loss while maximizing premium recovery. (Source: [[recovering-losing-options-positions]])

### The 21-Day Rule

Many premium sellers mechanically roll or close iron condors at ~21 DTE. At that point [[theta]] decay accelerates but [[gamma]] risk spikes — small underlying moves cause violent option price swings. Rolling at 21 DTE sidesteps this danger zone. (Source: [[recovering-losing-options-positions]])

### Other adjustments

- **Close the tested side** and let the untested side expire worthless for full profit on that leg
- **Roll out** the entire condor to a later expiration for additional credit
- **Convert to an [[iron-butterfly]]** by moving both short strikes to ATM (concentrates profit zone but increases premium)

See [[trade-repair-and-rolling]] for the complete adjustment framework.

## When to use

- **Range-bound markets**: The ideal environment — low realized volatility, no strong trend
- **High IV environments**: Elevated [[implied-volatility]] inflates the premium collected, improving the risk/reward
- **Earnings avoidance**: Iron condors should generally be placed to expire *before* earnings, not through them, since the binary event can blow through a short strike

## Advantages

- **Defined risk**: Maximum loss is known at entry and cannot exceed spread width minus credit
- **High probability**: Wide short strikes give 60–80% probability of profit
- **Theta positive**: Time decay works in the seller's favor every day
- **Market neutral**: No need to predict direction — only range
- **Capital efficient**: Margin requirement is the max loss of one side only (since both sides cannot lose simultaneously)

## Disadvantages

- **Limited profit**: Maximum gain is capped at the net credit collected
- **Negative gamma**: Large moves accelerate losses as delta shifts against the position
- **Vega risk**: Volatility spikes (even without directional moves) can inflate the value of all four legs, creating unrealized losses
- **Negatively skewed P&L**: average loss exceeds average win; long win streaks breed overconfidence and oversizing
- **Active management required**: Tested condors need timely adjustment decisions
- **Earnings and event risk**: Binary events can overwhelm the structure if not sized and timed properly
- **Crowded trade**: the variance risk premium has compressed as short-vol strategies proliferated

## Sources

- (Source: [[recovering-losing-options-positions]])
- CBOE S&P 500 Iron Condor Index (ticker CNDR) — published benchmark for a systematic SPX iron condor
- Carr, P. & Wu, L. (2009), "Variance Risk Premiums", *Review of Financial Studies* — documents that index implied variance persistently exceeds realized variance
- Israelov, R. & Nielsen, L. (2015), "Covered Calls Uncovered", *Financial Analysts Journal* — decomposition of option-selling returns into the volatility risk premium

## Related

- [[iron-butterfly]] — A narrower variant with both short strikes at ATM
- [[credit-spread]] — The building block of an iron condor
- [[vertical-spread]] — General vertical spread framework
- [[bull-put-spread]] / [[bear-call-spread]] — the two halves of the structure
- [[trade-repair-and-rolling]] — Adjustment and rolling techniques for tested condors
- [[variance-risk-premium]] — the economic source of the edge
- [[theta]] — The time decay that drives iron condor profitability
- [[gamma]] — The risk that accelerates near short strikes and expiration
- [[vega]] — Volatility exposure of the position
- [[edge-taxonomy]] — edge classification framework
- [[wheel-strategy]] — a related premium-selling approach
- [[managing-winners]] — the 50%/21-DTE exit discipline that governs condor P&L
- [[zero-dte-options]] — the same structure traded at same-day-expiry tenors
- [[long-call]] / [[long-put]] — the long-premium counterparties to the condor's short wings
- [[implied-volatility]] — the input that sets the credit and the vega risk
- [[market-regime]] — range-bound, falling-IV regimes are the condor's ideal habitat
