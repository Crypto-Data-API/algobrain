---
title: "Bear Put Spread"
type: strategy
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [options, bear-put-spread, put-debit-spread, debit-spread, bearish, defined-risk]
aliases: ["Put Debit Spread"]
strategy_type: quantitative
markets: [stocks]
complexity: beginner
backtest_status: untested
edge_source: [analytical, risk-bearing]
edge_mechanism: "A directional debit spread that monetises a correct view that the underlying will fall to the short strike by expiry; the offsetting short put sells back some long-put vega/theta, so the edge is a bearish forecast cheapened by giving up downside beyond the short strike."
crowding_risk: low
related: ["[[bull-call-spread]]", "[[bear-call-spread]]", "[[vertical-spreads]]", "[[married-put]]", "[[delta]]", "[[option-volatility-and-pricing]]"]
---

# Bear Put Spread

## Overview

The Bear Put Spread (also called a **Put Debit Spread**) is a bearish, defined-risk strategy that pays a net debit at entry. The trader buys a higher-strike [[put-option]] and sells a lower-strike put at the same expiration. The long put provides downside exposure while the short put reduces the overall cost and caps the maximum profit. The position profits when the underlying drops below the long put strike and reaches maximum value when the stock is at or below the short put strike at expiration. It is the bearish mirror image of the [[bull-call-spread]].

## Setup

1. **Buy 1 put** at a strike near or slightly below the current stock price (the higher strike).
2. **Sell 1 put** at a lower strike to reduce cost. Spread width determines the profit cap.
3. **Same expiration** -- 30-60 DTE is typical to balance cost and time for the move.
4. **Net debit paid** = premium for bought put minus premium received from sold put.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock below short put strike at expiry | Max profit = spread width minus debit paid |
| Stock between the two strikes | Partial profit; long put has intrinsic value |
| Stock above long put strike | Max loss = net debit paid; both puts expire worthless |

**Max profit** = (higher strike - lower strike) - net debit. **Max loss** = net debit paid. **Break-even** = higher strike - net debit (Source: [[book-option-volatility-and-pricing]]).

## Edge source

Per the [[edge-taxonomy]], the bear put spread is primarily an **analytical** edge (a bearish directional forecast) with a small **risk-bearing** element. As a *debit* structure you are a net buyer of put premium — net long [[vega]], net short [[theta]] — so it does NOT primarily harvest the [[variance-risk-premium]]; that is the domain of the credit-spread family ([[bear-call-spread]], [[bull-put-spread]]). The point of the spread versus a naked long [[put-option]] is cost reduction and defined exposure: selling the lower-strike put recovers part of the premium and trims vega/theta in exchange for capping how far the profit can run.

## Why this edge exists

The counterparty is a market-maker on the long leg and a put buyer on the short leg. The trade has positive expectancy only if your bearish view beats the distribution already priced into [[implied-volatility]] and [[the-greeks]]. Puts on equity indices and many single names carry a *premium* (the volatility skew / put-skew) because investors pay up for downside protection — which makes buying puts structurally a bit expensive. Your analytical edge (a catalyst, weak fundamentals, a broken technical level) must overcome that built-in cost. Absent a real view, the structure is fair minus frictions and minus the skew premium you pay to be long puts; there is no inherent edge in simply being long a bearish debit spread.

## Null hypothesis

Under the null (no directional edge, options fairly priced including put skew), the expected P&L of a bear put spread is approximately **−(commissions + bid/ask + the slice of skew/variance premium embedded in long put premium)**. The risk-neutral expectation of the structure equals roughly its cost, so realised expectancy is slightly negative after frictions and skew. A series of bear put spreads that fails to beat breakeven net of costs is the null in action — your bearish signal has no edge and you are paying up for downside.

## Rules

- **Direction / thesis**: moderately bearish; you expect the underlying at or below the short strike by expiry, ideally on an identifiable catalyst.
- **Strike selection**: buy the long put at-the-money to slightly in-the-money (delta ≈ −0.50 to −0.70) for higher probability; buy slightly out-of-the-money (delta ≈ −0.35 to −0.45) for cheaper, higher-payoff spreads. Place the short put at or just past your downside target.
- **Width**: 1–3 strikes (~5–10% of spot). Wider = larger max profit and debit; narrower = cheaper but smaller payoff.
- **DTE**: 30–60 days to limit [[theta]] drag on the long leg and give the move time.
- **Cost discipline**: pay no more than ~⅔ of the spread width as debit. Mind put skew — long puts are often richly priced.
- **Entry**: prefer entering when [[implied-volatility]] is low-to-moderate; a post-entry IV spike (common in selloffs) helps the long-vega position.
- **Exit / management**: take profits at 50–75% of max profit. Cut/roll on thesis invalidation. Close before expiry if the short put is deep ITM to avoid early [[assignment]].
- **Position sizing**: risk ≤ 1–2% of the account per spread (max loss = debit × contracts × 100).

## Implementation pseudocode

```python
def manage_bear_put_spread(spot, signal_bearish, iv_rank, chain):
    if not signal_bearish or iv_rank > 60:   # avoid buying expensive puts when IV is rich
        return None
    long_put  = chain.put(delta=-0.55, dte=45)        # ATM-ish long
    short_put = chain.put(strike=long_put.strike - width, dte=45)
    debit = long_put.ask - short_put.bid
    if debit > 0.66 * width:                          # reward too small vs risk
        return None
    pos = open_spread(buy=long_put, sell=short_put, debit=debit)

    while pos.open:
        value = pos.mark()
        if value >= 0.70 * pos.max_profit:            # take profit at 70%
            close(pos); break
        if thesis_invalidated() or value <= -0.60 * debit:  # cut a losing thesis
            close(pos); break
        if pos.dte <= 21 and pos.short_leg.itm:       # deep-ITM short put -> assignment risk
            close(pos); break
        if pos.dte <= 2:
            close(pos); break                         # never carry into expiry gamma/pin
```

## Example trade

*Illustrative hypothetical with round numbers — not a recommendation or backtest.*

Stock XYZ trades at **$100**. Moderately bearish into a catalyst, 45 DTE:

- **Buy 1 × $100 put** for $4.00
- **Sell 1 × $95 put** for $1.90
- **Net debit** = $4.00 − $1.90 = **$2.10** ($210 per spread)
- **Spread width** = $5.00
- **Max profit** = $5.00 − $2.10 = **$2.90** ($290) when XYZ ≤ $95 at expiry
- **Max loss** = **$2.10** ($210) when XYZ ≥ $100 at expiry
- **Break-even** = $100 − $2.10 = **$97.90**
- **Reward:risk** ≈ 2.90 : 2.10 ≈ **1.38 : 1**

Payoff at expiration:

| XYZ at expiry | Long $100 put | Short $95 put | Spread value | P&L (per spread) |
|---|---|---|---|---|
| $105 | 0 | 0 | $0.00 | −$210 (max loss) |
| $100 | 0 | 0 | $0.00 | −$210 |
| $97.90 | $2.10 | 0 | $2.10 | $0 (break-even) |
| $95 | $5.00 | 0 | $5.00 | +$290 (max profit) |
| $90 | $10.00 | −$5.00 | $5.00 | +$290 (capped) |

## Performance characteristics

- **Cost drag**: two legs in, usually two out — up to four commissions and four bid/ask crossings per round trip, material against a $2.10 debit. Use mid-price limit orders.
- **Greeks**: net short [[delta]] (bearish), net long [[vega]] (helps in a selloff where IV rises, hurts if vol collapses), net short [[theta]].
- **Skew headwind**: equity put skew makes long puts relatively expensive, a structural drag the directional view must overcome.
- **No fabricated backtest**: realised performance depends on signal quality. With no edge, expectancy ≈ −costs − skew (see Null hypothesis).

## Capacity limits

Effectively unlimited for retail size on liquid underlyings. The constraint is **per-name put liquidity** — trade penny-wide strikes with healthy open interest, avoid illiquid back-month single-name puts where slippage swamps the edge. Index/ETF puts are deepest. Not a capacity-constrained alpha; it is a position tool, not a scalable institutional strategy.

## What kills this strategy

- **Sideways/up drift**: the underlying fails to fall, [[theta]] erodes the long put, you lose the debit.
- **IV crush**: buying expensive puts (post-spike or pre-event) then suffering a vol collapse leaves you underwater even on a small favorable move.
- **Adverse gap up**: realises the full debit loss.
- **Capped downside profit**: a crash earns no more than max profit beyond the short strike.
- **Early [[assignment]]** on the short put if it goes deep ITM near expiry, leaving short stock unexpectedly.

## Kill criteria

- Close at a **loss of ≥ 60% of the debit paid**.
- **Hard exit at ≤ 2 DTE** regardless of P&L to avoid expiration [[gamma]]/[[pin-risk]].
- **Take profit at 50–75% of max profit.**
- Exit immediately on **thesis invalidation** (catalyst resolved bullishly, key support reclaimed).
- Retire a systematic bear-put program if **rolling 6-month net P&L < −1× average debit per trade** — the bearish signal carries no edge.

## When to Use

- You are **moderately bearish** and expect the stock to decline to or past the short put strike by expiration.
- You want defined risk rather than the unlimited exposure of a naked short position.
- [[implied-volatility]] is relatively low, making purchased puts affordable (Source: [[book-option-volatility-and-pricing]]).
- You want a cheaper alternative to buying a standalone protective put via [[married-put]].

## Advantages
- Defined risk -- maximum loss is the debit paid, known at entry
- Lower cost than buying a naked put because the sold put offsets part of the premium
- Simple two-leg structure suitable for beginners
- Benefits from a rise in [[implied-volatility]] after entry

## Disadvantages
- Max profit is capped at the spread width minus the debit -- you miss gains below the short strike
- Requires the stock to move lower; [[theta]] decay works against you if the stock stays flat or rises
- If the stock drops only slightly, the debit may not be fully recovered
- Early assignment risk on the short put if it goes deep ITM near expiration

## See Also
- [[bull-call-spread]] -- the bullish debit spread counterpart
- [[bear-call-spread]] -- a bearish credit spread alternative
- [[married-put]] -- a simpler but more expensive bearish hedge
- [[vertical-spreads]] -- the general family of directional spread strategies

## Sources
- [[book-option-volatility-and-pricing]] — Natenberg covers vertical spread construction, payoff profiles, and the role of implied volatility in determining debit spread cost and value
