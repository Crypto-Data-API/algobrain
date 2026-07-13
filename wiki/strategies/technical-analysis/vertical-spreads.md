---
title: "Vertical Spreads"
type: strategy
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [options, vertical-spread, bull-call, bear-put, credit-spread, debit-spread, defined-risk]
strategy_type: quantitative
timeframe: swing
markets: [stocks, crypto]
complexity: beginner
backtest_status: untested
edge_source: [analytical, risk-bearing, behavioral]
edge_mechanism: "Vertical spreads split into two families: debit spreads monetise an analytical directional forecast cheaply with defined risk; credit spreads harvest the variance/volatility risk premium and skew by selling overpriced options against buyers of insurance and speculation."
crowding_risk: medium
related: ["[[bull-call-spread]]", "[[bear-put-spread]]", "[[bull-put-spread]]", "[[bear-call-spread]]", "[[iron-condor]]", "[[butterfly-spread]]", "[[covered-call]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[implied-volatility]]", "[[variance-risk-premium]]", "[[edge-taxonomy]]"]
---

# Vertical Spreads

## Overview

Vertical spreads are the **building blocks** of most multi-leg options strategies. A vertical spread involves buying and selling two options of the same type (both calls or both puts), same expiration, but different [[strike-price]]s. The result is a **defined-risk, defined-reward** directional bet. There are four primary variants:

- **Bull Call Spread** (debit): Buy lower-strike call, sell higher-strike call. Profits when price rises.
- **Bear Put Spread** (debit): Buy higher-strike put, sell lower-strike put. Profits when price falls.
- **Bull Put Spread** (credit / "put credit spread"): Sell higher-strike put, buy lower-strike put. Profits when price stays above the short strike.
- **Bear Call Spread** (credit / "call credit spread"): Sell lower-strike call, buy higher-strike call. Profits when price stays below the short strike.

Debit spreads pay upfront and profit from directional moves. Credit spreads collect [[premium]] upfront and profit from [[theta]] decay and the underlying staying away from the short strike.

## Setup

1. **Choose direction:** Bullish = bull call or bull put spread. Bearish = bear put or bear call spread.
2. **Select strikes:** The short strike defines your directional target; the long strike defines your protection. Typical width: 1-5 strikes apart.
3. **Expiration:** 30-45 DTE for credit spreads (maximize [[theta]] decay). 45-60 DTE for debit spreads (give the move time to develop).
4. **Risk/reward:** Max risk = spread width - credit received (credit spreads) or net debit paid (debit spreads). Max profit = credit received or spread width - debit paid.

## Payoff Profile

| Variant | Max Profit | Max Loss | Break-Even |
|---|---|---|---|
| Bull call spread | Width - debit | Debit paid | Lower strike + debit |
| Bear put spread | Width - debit | Debit paid | Upper strike - debit |
| Bull put spread | Credit received | Width - credit | Short strike - credit |
| Bear call spread | Credit received | Width - credit | Short strike + credit |

## Edge source

Per the [[edge-taxonomy]], vertical spreads split into two edge families:

- **Debit spreads** ([[bull-call-spread]], [[bear-put-spread]]) — primarily an **analytical** edge (a directional forecast) plus a little risk-bearing. You are a net premium *buyer* (net long [[vega]], net short [[theta]]). They do NOT primarily harvest the [[variance-risk-premium]]; the edge must come from a correct view, with the offsetting short leg cheapening the bet in exchange for capped upside.
- **Credit spreads** ([[bull-put-spread]], [[bear-call-spread]]) — primarily a **risk-bearing** edge with a **behavioral** overlay. You are a net premium *seller* (net positive [[theta]], net short [[vega]]) harvesting the [[variance-risk-premium]] and the skew/insurance demand of option buyers.

So the family spans three edge categories depending on construction: analytical (debit), risk-bearing and behavioral (credit).

## Why this edge exists

For **debit** spreads, the counterparty is a market-maker; the trade only pays if your directional view beats the implied distribution priced into [[the-greeks]]. There is no inherent edge in being long premium — the edge is the forecast.

For **credit** spreads, the counterparty is the buyer of options: investors paying up for downside protection (put skew) and speculators chasing convex upside (call demand). Implied volatility tends to exceed realised volatility, so the seller collects a structural premium for bearing tail risk. This premium is real but **moderately crowded** (premium-selling is a popular retail/fund activity), which has compressed it over time.

## Null hypothesis

Under the null (options fairly priced, no directional edge, no variance risk premium), every vertical spread has expected P&L ≈ **−costs** (commissions + bid/ask, plus the skew/VRP slice the side you take pays or fails to collect). The risk-neutral expectation of any defined-risk structure equals roughly its cost. For credit spreads in particular, a high win rate is automatic by construction (small frequent wins, rare large losses) and is **not** evidence of edge — only positive expectancy net of the occasional max loss proves a real premium. A spread program that fails to beat breakeven net of frictions is observing the null.

## Rules

Family-level guidance; see each child page for specifics.

- **Pick the family by IV and direction**: bullish + low IV → [[bull-call-spread]] (debit); bullish + high IV → [[bull-put-spread]] (credit). Bearish + low IV → [[bear-put-spread]] (debit); bearish + high IV → [[bear-call-spread]] (credit).
- **Strike selection**: debit spreads — long leg ATM-to-slightly-ITM (delta ~0.45–0.65), short leg at the price target. Credit spreads — short leg ~delta 0.16–0.30 (≈70–84% OTM), long leg 1–5 strikes further out for protection.
- **Width**: 1–5 strikes; debit ≤ ~⅔ of width, or credit ≥ ~⅓ of width.
- **DTE**: 30–45 DTE for credit spreads (maximise [[theta]]); 45–60 DTE for debit spreads (give the move time).
- **Management**: credit spreads — take profit at **50% of max credit**, manage/roll at **21 DTE**. Debit spreads — take profit at **50–75% of max profit**; close before the short leg goes deep ITM near ex-dividend dates ([[assignment]] risk).
- **Sizing**: risk ≤ 1–3% of the account per spread; cap aggregate correlated short-premium (tail) exposure.

## Implementation pseudocode

```python
def choose_vertical(direction, iv_rank, chain, width):
    if direction == "bullish":
        if iv_rank < 30:   # buy cheap premium
            return bull_call_spread(chain, width)      # debit, analytical edge
        else:              # sell rich premium
            return bull_put_spread(chain, width)       # credit, VRP edge
    else:  # bearish
        if iv_rank < 30:
            return bear_put_spread(chain, width)       # debit, analytical edge
        else:
            return bear_call_spread(chain, width)      # credit, VRP edge

def manage(pos):
    if pos.is_credit:
        if pos.captured >= 0.50 * pos.max_profit: close(pos)
        elif pos.dte <= 21:                       roll_or_close(pos)
        elif pos.loss >= 2.0 * pos.credit:        close(pos)   # defined-risk stop
    else:  # debit
        if pos.value >= 0.70 * pos.max_profit:    close(pos)
        elif pos.dte <= 2:                        close(pos)   # avoid expiry gamma/pin
        elif pos.loss >= 0.60 * pos.debit:        close(pos)
```

## Example trade

*Illustrative hypothetical with round numbers — not a recommendation or backtest.*

One debit and one credit example on stock XYZ at **$100**, 45 DTE:

**Bull call spread (debit, bullish, low IV):** Buy $100 call $4.00, sell $105 call $1.80. Net debit **$2.20**; width $5.00; max profit **$2.80**; max loss **$2.20**; break-even **$102.20**; R:R ≈ 1.3:1.

**Bull put spread (credit, neutral-bullish, high IV):** Sell $95 put $1.50, buy $90 put $0.50. Net credit **$1.00**; width $5.00; max profit **$1.00**; max loss **$4.00**; break-even **$94.00**; R:R ≈ 1:4 (high win probability).

| Structure | Net | Max profit | Max loss | Break-even | Profits when |
|---|---|---|---|---|---|
| Bull call (debit) | −$2.20 | $2.80 | $2.20 | $102.20 | XYZ rises to ≥ $105 |
| Bull put (credit) | +$1.00 | $1.00 | $4.00 | $94.00 | XYZ stays ≥ $95 |

The debit example pays a small cost for an asymmetric directional payoff; the credit example collects premium for a high-probability, negatively-skewed payoff.

## Performance characteristics

- **Debit spreads**: net long delta/vega, short theta — need a timely directional move; a favorable IV move helps. Capped upside; expectancy is the quality of the signal minus costs.
- **Credit spreads**: net short vega, positive theta — win most of the time but with negatively-skewed payoff; expectancy is the [[variance-risk-premium]] minus costs minus tail losses.
- **Cost-aware**: 2 legs in and (usually) 2 out → up to four commissions and four bid/ask crossings per round trip — material against small credits/debits. Use mid-price limit orders.
- **No fabricated backtest**: realised results depend on signal quality (debit) and VRP persistence + loss discipline (credit). Under the null both families return ≈ −costs.

## Capacity limits

Effectively unlimited for retail and small-fund size on liquid index ETFs and large-cap single names. Binding constraints are **per-strike open interest and bid/ask width** (thin strikes destroy the thin edge) and, for credit spreads, **aggregate correlated tail exposure** rather than order size. Premium-selling is moderately crowded, compressing the credit-side edge. Not a scalable institutional alpha — a position/risk tool.

## What kills this strategy

- **Debit spreads**: sideways/flat tape ([[theta]] bleed), IV crush after entry, adverse gaps, and capped upside on a big move.
- **Credit spreads**: a sharp adverse gap or trend through the short strike (max loss), volatility expansion before expiry (short [[vega]]), and correlated tail losses when many short-premium positions lose together.
- **Both**: early [[assignment]] on the short leg near ex-dividend dates; end-of-life [[gamma]] and [[pin-risk]] if carried to expiration; edge compression in unfavorable IV regimes.

## Kill criteria

- **Credit spreads**: stop-loss at a debit of **≥ 2× the credit**; take profit at **50% of max credit**; manage/close at **21 DTE**.
- **Debit spreads**: stop-loss at **≥ 60% of the debit**; take profit at **50–75% of max profit**; **hard exit ≤ 2 DTE**.
- **Both**: close immediately on early-assignment risk (short leg deep ITM near ex-dividend) or on thesis invalidation.
- **Portfolio**: cap aggregate short-premium (tail) exposure; cut size if a stress day breaches the risk budget.
- Retire a systematic program if **rolling 12-month net P&L ≤ 0** net of costs — the assumed edge (signal or VRP) is absent.

## When to Use

- You have a **directional opinion** but want defined risk rather than naked exposure.
- [[implied-volatility]] is high (sell credit spreads) or low (buy debit spreads cheaply).
- Vertical spreads serve as legs inside [[iron-condor]], [[butterfly-spread]], and [[iron-butterfly]] structures.

## Advantages
- **Defined risk and reward** -- max loss is known at entry, no margin surprises
- Simple two-leg structure with lower commissions than multi-leg strategies
- Highly versatile -- can express any directional view in any volatility regime
- Reduce the cost of buying options outright by selling an offsetting strike
- The fundamental building block for understanding complex options strategies

## Disadvantages
- **Capped profit** -- even if the underlying moves dramatically in your favor, gains are limited
- Credit spreads have unfavorable risk/reward ratios (risk more than you can make)
- Debit spreads require the stock to move enough to overcome the net cost
- Early [[assignment]] on the short leg is possible, especially near ex-dividend dates

## See Also
- [[iron-condor]] -- two vertical credit spreads combined (one bull put, one bear call)
- [[butterfly-spread]] -- built from two vertical spreads sharing a middle strike
- [[covered-call]] -- a vertical spread equivalent when combined with stock
- [[implied-volatility]] -- determines whether credit or debit spreads are preferable

## Related
- [[bull-call-spread]], [[bear-put-spread]] -- the debit (analytical-edge) members
- [[bull-put-spread]], [[bear-call-spread]] -- the credit (VRP-edge) members
- [[variance-risk-premium]] -- the structural source of the credit-spread edge
- [[the-greeks]], [[theta]], [[vega]], [[delta]] -- the Greeks that drive both families
- [[assignment]], [[pin-risk]] -- key short-leg risks near expiration
- [[edge-taxonomy]] -- classification of the analytical/risk-bearing/behavioral edges

## Sources
General market knowledge; no specific wiki source ingested yet.
