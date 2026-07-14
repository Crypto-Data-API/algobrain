---
title: "Put Spread"
type: strategy
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [options, derivatives, swing-trading, volatility, risk-management]
aliases: ["Put Spread", "Vertical Put Spread", "Bear Put Spread", "Long Put Spread", "Put Debit Spread"]
related: ["[[long-put]]", "[[short-put-spread]]", "[[credit-spread]]", "[[debit-spread]]", "[[protective-puts]]", "[[options]]", "[[implied-volatility]]", "[[theta-decay]]", "[[edge-taxonomy]]"]
strategy_type: technical
timeframe: swing
markets: [options]
complexity: intermediate
backtest_status: naive-backtested
edge_source: [analytical, behavioral]
edge_mechanism: "Expresses a bounded bearish view at lower cost and lower theta bleed than an outright put by selling away the deep-downside payoff the trader does not expect to need; profit comes from being directionally right within a defined range, not from a structural mispricing."
data_required: [options-chain, ohlcv-daily, implied-volatility]
min_capital_usd: 1000
capacity_usd: 5000000
crowding_risk: low
expected_sharpe: 0.3
expected_max_drawdown: 0.40
breakeven_cost_bps: 30
---

A **put spread** (vertical put spread) is a two-leg option position built from a long put and a short put on the same underlying with the same expiry but different strikes. The most common form is the **bear put spread** (a *debit* put spread): buy a higher-strike put and sell a lower-strike put to express a moderately bearish view with a defined, capped cost and a defined, capped payoff. The mirror version — selling the higher-strike put and buying the lower-strike put for a net credit — is a **bull put spread**, documented separately at [[short-put-spread]] and [[credit-spread]]. This page covers the long/debit bear put spread unless noted.

## Edge source
Primarily **analytical** with a **behavioral** overlay (see [[edge-taxonomy]]). The structure does not exploit a persistent statistical anomaly; the "edge," when it exists, comes from a correct directional/volatility view executed with better risk-adjusted economics than an outright [[long-put]]. The behavioral component is that the trader is willing to sell the deep-downside tail (the short leg) that retail buyers chronically overpay for via the put skew, partially financing the long leg.

## Why this edge exists
Outright puts carry rich premium because of the equity **volatility risk premium** and persistent put skew — out-of-the-money puts are bid up by hedgers and crash-fearful buyers. A naked long put therefore fights heavy [[theta-decay]] and an expensive entry. By selling a lower-strike put, the bear put spread recaptures part of that overpriced skew, cutting net cost (often 30-60%) and net theta. The "other side" is the put seller's counterparty: index/single-name hedgers who accept negative expected value on deep puts for insurance. The spread buyer is *not* claiming a free lunch — they cap their own payoff at the short strike in exchange for a cheaper, lower-bleed bearish bet. The edge is therefore conditional on the directional thesis being right within the band; it is not an edge in the standalone, unconditional sense.

## Null hypothesis
Under the null — option prices are fair, no directional edge, no skew premium to harvest — a put spread is a zero-expected-value bet minus transaction costs. Random entries on liquid names would produce a near-coin-flip win rate at the spread's natural breakeven, with realized P&L scattered around the negative of total slippage and commissions. Any persistent positive edge must come from (a) genuine directional skill timing the down-move, or (b) systematic harvesting of overpriced downside skew via the short leg. A backtest that beats this null only on the most-skewed, least-liquid options is likely measuring uncrossable bid-ask, not edge.

## Rules
**Entry**
- Directional thesis: moderately bearish on the underlying over days-to-weeks (a bounded move, not a crash).
- Buy 1 put at strike A (at- or slightly in/out-of-the-money), sell 1 put at strike B (lower), same expiry. Net debit paid.
- Expiry typically 20-60 DTE to balance theta and time for the thesis to play out.
- Prefer entry when implied volatility is moderate-to-elevated (the short leg is then worth more, cheapening the spread); avoid paying up for both legs at low IV unless purely directional.

**Exit**
- Take profit: close for 50-75% of max profit (= width − debit) rather than holding to expiry, to avoid pin/gamma risk.
- Stop: close if the thesis breaks (price rallies through entry level) or the debit is mostly lost; a common rule is exit at ~1.5-2x the credit-equivalent loss or at a chosen % of debit.
- Time stop: manage/roll inside ~7-10 DTE to limit gamma and assignment risk on the short leg.

**Sizing**
- Max loss = net debit per spread × 100 × number of spreads. Size so max loss ≤ 1-2% of account per trade.
- Strike width sets the risk/reward: wider = more max profit but larger debit; narrower = cheaper but lower payoff.

## Implementation pseudocode
```python
def bear_put_spread(underlying, chain, dte=35, width=5):
    # moderately bearish, bounded down-move view assumed upstream
    long_strike  = nearest_strike(chain, underlying.spot)          # ATM-ish long put
    short_strike = long_strike - width                              # lower short put
    long_put  = chain.put(strike=long_strike,  dte=dte)
    short_put = chain.put(strike=short_strike, dte=dte)

    net_debit  = long_put.ask - short_put.bid                       # pay the spread
    max_loss   = net_debit
    max_profit = width - net_debit
    breakeven  = long_strike - net_debit

    if max_profit / max_loss < 1.0:                                 # require >=1:1 R:R
        return None

    contracts = floor((0.01 * account_equity) / (max_loss * 100))   # 1% risk
    enter(buy=long_put, sell=short_put, qty=contracts)

    # management loop
    while open:
        pnl = mark_to_market()
        if pnl >= 0.6 * max_profit * 100 * contracts: close()       # take profit
        elif pnl <= -0.7 * max_loss * 100 * contracts: close()      # stop
        elif dte_now <= 7: close_or_roll()                          # avoid gamma/pin
```

## Indicators / data used
- Live options chain (bid/ask, greeks) for strike selection and execution.
- Underlying [[ohlcv]] and trend/level analysis for the directional thesis (support/resistance, moving averages).
- [[implied-volatility]] surface / put skew to judge whether the short leg meaningfully cheapens the spread.
- Greeks: net delta (directional exposure), net theta (decay), net vega (volatility exposure — a debit put spread is net long vega but less so than an outright put).

## Example trade
Stock XYZ trades at $102; thesis: drift to ~$95 over the next month.
- Buy the $100 put @ $3.20, sell the $95 put @ $1.40 → **net debit $1.80** ($180 per spread).
- Width = $5 → **max profit = $5 − $1.80 = $3.20** ($320); **max loss = $180**; **breakeven = $98.20**.
- Risk/reward ≈ 1.78:1. On a $20,000 account at 1% risk ($200), trade 1 spread.
- Outcome: at expiry XYZ = $94. Long $100 put worth $6, short $95 put worth $1 → spread worth $5 (full width). P&L = ($5 − $1.80) × 100 = **+$320** (max). Had XYZ stayed above $100, the whole $180 debit is lost.

## Performance characteristics
- **Defined risk, defined reward** — both max loss (debit) and max profit (width − debit) are fixed at entry.
- Win rate depends entirely on directional skill and chosen strikes; the structure itself is roughly zero-sum before costs (confirmed null behavior). Realistic standalone Sharpe for a discretionary directional program is modest (~0.3) with high variance; clusters of losses occur in low-vol, grinding-up regimes.
- Cost drag: round-trip retail commissions are ~$1-3 per 2-leg spread plus ~$1-2 per leg of bid-ask slippage; on a $180 debit that is roughly **10-30 bps** of notional but a larger fraction of premium — manage actively to close, don't always hold to expiry.
- Lower theta and cheaper entry than an outright [[long-put]], at the cost of capped upside and pinned-down convexity.

## Capacity limits
Capacity is bounded by single-name option liquidity, not capital. On liquid large-caps and index options, defined-risk verticals scale to low-eight-figure books per name before bid-ask and open-interest constraints bite; on small/mid-caps, wide spreads and thin open interest cap practical size at tens of thousands of dollars of risk. As a directional/discretionary tool it does not "crowd" in the factor sense.

## What kills this strategy
- **Being wrong on direction** — the underlying rallies or chops sideways and the debit decays to zero. The dominant failure mode (see [[failure-modes]]).
- **Capped upside** — a thesis that is *more* right than expected (a crash through the short strike) earns no extra; the short leg gives the gains back. An outright put or [[put-tree]] would have paid more.
- **Volatility crush** — if IV collapses after entry, both legs lose value; the spread cushions this vs. a naked put but is still net long vega.
- **Pin / gamma risk near expiry** — price settling between strikes at expiry creates uncertain, gamma-heavy outcomes and assignment risk on the short leg.
- **Transaction-cost erosion** — over-trading thin chains turns a fair bet into a guaranteed loser.

## Kill criteria
- Rolling 12-month win rate at chosen breakevens < 40% with payoff ratio < 1.5 (no directional edge → stop).
- Realized average loss per trade exceeds 1.2× planned debit (slippage/management failure).
- Strategy drawdown > 40% of allocated sleeve.
- Average round-trip cost > 30 bps of notional (chosen universe too illiquid → restrict to liquid names or retire).

## Advantages
- Defined, capped risk known at entry; cannot blow up like a naked short option.
- Cheaper and lower theta bleed than an outright [[long-put]].
- Benefits modestly from elevated put skew (the short leg recaptures overpriced premium).
- Margin-efficient: collateral is just the net debit.

## Disadvantages
- Upside capped at the short strike — gives up the convex tail payoff of a long put.
- Still loses the full debit if the directional view is wrong.
- Two legs = double the commissions and bid-ask; profit eroded on illiquid chains.
- No standalone statistical edge — performance lives or dies on directional skill or skew harvesting.

## Sources
- The Options Industry Council (OIC), "Bear Put Spread" — https://www.optionseducation.org/strategies/all-strategies/bear-put-spread
- Montreal Exchange, "Equity Options Strategies — Bear Put Spread" — https://www.m-x.ca/f_publications_en/options_strat12_en.pdf
- CBOE, options strategy education — https://www.cboe.com/education/
- Hull, J. C., *Options, Futures, and Other Derivatives* — vertical spreads chapter.

## Related
- [[long-put]] — the un-spread, fully convex bearish building block
- [[short-put-spread]] / [[credit-spread]] — the credit (bull put) mirror
- [[debit-spread]] — general defined-risk long-spread concept
- [[bull-call-spread]] — bullish debit-spread analogue
- [[protective-puts]] / [[options-hedging]] — when used as a bounded hedge
- [[implied-volatility]] / [[theta-decay]] / [[options-pricing]]
- [[edge-taxonomy]] / [[failure-modes]]
