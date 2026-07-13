---
title: "Bear Call Spread"
type: strategy
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [options, bear-call-spread, call-credit-spread, credit-spread, bearish, defined-risk]
aliases: ["Call Credit Spread"]
strategy_type: quantitative
markets: [stocks]
complexity: beginner
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "A short call-credit spread sells upside calls that are, on average, richer than realised moves: it harvests the variance/volatility risk premium and takes the other side of call buyers (retail upside speculation, covered-call demand), accepting tail risk on a strong rally."
crowding_risk: medium
related: ["[[bull-put-spread]]", "[[bear-put-spread]]", "[[iron-condor]]", "[[vertical-spreads]]", "[[theta]]", "[[variance-risk-premium]]"]
---

# Bear Call Spread

## Overview

The Bear Call Spread (also called a **Call Credit Spread**) is a bearish, defined-risk strategy that collects a net credit at entry. The trader sells a lower-strike [[call-option]] and buys a higher-strike call at the same expiration. The sold call generates premium while the bought call caps the maximum loss. The position profits when the underlying stays below the short call strike, allowing both options to expire worthless. It is the bearish mirror image of the [[bull-put-spread]] and a core building block of the [[iron-condor]].

## Setup

1. **Sell 1 call** at a strike near or slightly above the current stock price (the lower strike).
2. **Buy 1 call** at a higher strike to cap the risk. Spread width determines maximum loss.
3. **Same expiration** -- typically 30-45 DTE for optimal [[theta]] decay.
4. **Net credit received** = premium from sold call minus premium paid for bought call.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock below short call strike at expiry | Both calls expire worthless; keep full credit |
| Stock between the two strikes | Partial loss; short call is ITM, long call provides ceiling |
| Stock above long call strike | Max loss = spread width minus credit received |

**Max profit** = net credit received. **Max loss** = (higher strike - lower strike) - net credit. **Break-even** = short call strike + net credit.

## Edge source

Per the [[edge-taxonomy]], the bear call spread is primarily a **risk-bearing** edge with a **behavioral** overlay. Selling a call-credit spread harvests the [[variance-risk-premium]]: implied volatility generally exceeds subsequently realised volatility, so the call you sell is, on average, priced richer than the moves that occur. The behavioral overlay is the steady demand from upside speculators (retail call buyers, lottery-ticket OTM call demand) who push call premiums above fair value. The long higher-strike call caps the otherwise-unlimited upside risk of a naked short call.

## Why this edge exists

Your counterparties are call buyers: speculators betting on a rally, momentum chasers, and (indirectly) the dealer complex that warehouses the risk. Out-of-the-money calls attract persistent demand from people seeking convex upside, and that demand inflates premium relative to the actuarially fair value. As the seller you collect that premium most of the time and pay out on the (rarer) sharp rallies. Unlike the put side, equity call skew is usually flatter (skew favors puts), so the call-side VRP is generally **thinner** than the put-side premium of a [[bull-put-spread]] — meaning the edge is real but smaller and more sensitive to costs. The strategy is moderately **crowded** among premium sellers.

## Null hypothesis

Under the null (no variance risk premium, fairly priced calls), the short call-credit spread has expected P&L ≈ **−costs**: the credit just offsets expected payouts and you are left paying commissions and bid/ask. The entire edge rests on implied > realised volatility (and on call demand inflating premium). As with all credit spreads, a high win rate is automatic by construction and is NOT evidence of edge; only positive expectancy net of the occasional max loss demonstrates a real premium. If neither VRP nor call-demand premium is present in a name, you are selling fair lottery tickets and bleeding frictions.

## Rules

- **Direction / thesis**: bearish-to-neutral; you expect the underlying to stay below the short call strike (often below a resistance level).
- **Strike selection**: sell the short call around delta 0.16–0.30 (≈70–84% probability OTM), at or above resistance. Buy the long call 1–5 strikes higher to define risk.
- **Width**: sized so max loss fits position sizing; target a credit of roughly **⅓ of the width** (reward:risk ~1:2 with high win probability).
- **DTE**: 30–45 days — the accelerating [[theta]] zone.
- **IV environment**: enter when IV rank is elevated for richer premium; call-side premium is generally thinner than put-side, so be stricter on minimum acceptable credit.
- **Exit / management**: take profit at **50% of max credit**; manage/roll at **21 DTE** to limit end-of-life [[gamma]] and [[pin-risk]]. Roll up-and-out for a credit only while the bearish/neutral thesis holds. Watch ex-[[dividend]] dates for early [[assignment]] on the short call.
- **Position sizing**: max loss per spread = (width − credit) × 100; risk ≤ 1–3% of the account per position; cap aggregate short-call (upside-tail) exposure.

## Implementation pseudocode

```python
def manage_bear_call_spread(spot, neutral_to_bearish, iv_rank, chain):
    if not neutral_to_bearish or iv_rank < 30:   # only sell premium when it is rich
        return None
    short_call = chain.call(delta=0.20, dte=45)           # ~80% OTM probability
    long_call  = chain.call(strike=short_call.strike + width, dte=45)
    credit = short_call.bid - long_call.ask
    if credit < 0.30 * width:                             # call-side VRP is thin; demand a real credit
        return None
    pos = open_spread(sell=short_call, buy=long_call, credit=credit)

    while pos.open:
        value = pos.mark()                                # cost to buy back
        if value <= 0.50 * credit:                        # captured 50% of max profit
            close(pos); break
        if pos.dte <= 21:                                 # manage/roll near expiry
            roll_or_close(pos); break
        if value >= 2.0 * credit and short_call.itm:       # tested hard -> defined-risk stop
            close(pos); break
        if early_assignment_risk(pos.short_call):          # deep ITM near ex-dividend
            close(pos); break
```

## Example trade

*Illustrative hypothetical with round numbers — not a recommendation or backtest.*

Stock XYZ trades at **$100**, IV rank elevated, neutral-to-bearish (resistance near $105), 45 DTE:

- **Sell 1 × $105 call** for $1.40
- **Buy 1 × $110 call** for $0.45
- **Net credit** = $1.40 − $0.45 = **$0.95** ($95 per spread)
- **Spread width** = $5.00
- **Max profit** = **$0.95** ($95) when XYZ ≤ $105 at expiry
- **Max loss** = $5.00 − $0.95 = **$4.05** ($405) when XYZ ≥ $110 at expiry
- **Break-even** = $105 + $0.95 = **$105.95**
- **Reward:risk** = 0.95 : 4.05 ≈ **1 : 4.3** (high win probability, small reward, large tail loss)

Payoff at expiration:

| XYZ at expiry | Short $105 call | Long $110 call | Net | P&L (per spread) |
|---|---|---|---|---|
| $95 | 0 | 0 | keep credit | +$95 (max profit) |
| $105 | 0 | 0 | keep credit | +$95 |
| $105.95 | −$0.95 | 0 | credit − $0.95 | $0 (break-even) |
| $108 | −$3.00 | 0 | credit − $3.00 | −$205 |
| $110 | −$5.00 | 0 | credit − $5.00 | −$405 (max loss) |
| $115 | −$10.00 | +$5.00 | credit − $5.00 | −$405 (capped) |

## Performance characteristics

- **Negatively skewed**: many small wins, occasional large losses up to max loss. High win rate is structural, not edge.
- **Greeks**: net short [[delta]] (bearish), net short [[vega]] (an IV expansion hurts before expiry), net positive [[theta]] (time decay helps). Edge is the [[variance-risk-premium]] plus call-demand premium.
- **Thinner edge than the put side**: equity skew favors puts, so call-credit premium is usually smaller — costs bite proportionally more. Be selective and use mid limits.
- **No fabricated backtest**: realised edge tracks VRP persistence, call-demand richness, and disciplined loss management; under the null it is −costs (see Null hypothesis).

## Capacity limits

Ample for retail and small funds on liquid index ETFs and large-caps. Constraints: (1) **open interest / bid-ask** at chosen OTM call strikes — thin call series have wide spreads that erase a thin credit; (2) **aggregate upside-tail exposure** — many correlated short-call spreads all lose together in a melt-up or single-name squeeze. Moderately **crowded**; the per-unit premium has compressed. Order size is rarely the binding limit at retail/small-fund scale.

## What kills this strategy

- **Sharp rally / gap up** through the long strike (earnings beat, buyout, short squeeze): realises max loss, correlated across positions in a broad melt-up.
- **Volatility expansion**: a rising-IV rally marks the spread to a large unrealised loss before expiry (short [[vega]]).
- **Single-name squeeze**: short calls on a heavily-shorted name can blow through both strikes violently.
- **Early [[assignment]]** on the short call near ex-[[dividend]] dates, leaving an unwanted short stock position.
- **Edge compression**: thin call-side premium in a low-IV regime fails to cover costs and tail risk.

## Kill criteria

- **Stop-loss at a debit of ≥ 2× the credit received** (or define max loss as the full width) on a tested spread.
- **Take profit at 50% of max credit**; **manage or close at 21 DTE.**
- Close immediately on **early-assignment risk** (short call deep ITM near ex-dividend).
- **Portfolio rule**: if aggregate short-call (upside-tail) exposure or a melt-up drawdown exceeds the risk budget, cut size.
- Retire a systematic call-credit program if **rolling 12-month net P&L ≤ 0** (call-side premium has compressed below costs) or after an uncontrolled squeeze breaches the kill drawdown.

## When to Use

- You have a **bearish or neutral** outlook and expect the stock to stay below a resistance level.
- You want to sell [[premium]] with **defined risk** and predictable margin requirements.
- [[implied-volatility]] is elevated, inflating the sold call premium.
- You want a high-probability trade that profits from time decay and sideways price action.

## Advantages
- Credit received at entry -- immediate income
- Defined risk with no unlimited-loss scenarios
- Benefits from [[theta]] decay and [[implied-volatility]] crush
- Simple two-leg structure that is easy to execute and manage

## Disadvantages
- Max profit is capped at the credit received
- A strong rally through the spread results in the full defined loss
- Early assignment risk on the short call, especially around ex-[[dividend]] dates
- Narrow spreads yield small profits; wide spreads require more risk capital

## See Also
- [[bull-put-spread]] -- the bullish credit spread counterpart
- [[bear-put-spread]] -- a bearish debit spread alternative
- [[iron-condor]] -- combines a bear call spread with a [[bull-put-spread]]
- [[vertical-spreads]] -- the general family of single-width directional spreads

## Related
- [[variance-risk-premium]] -- the structural source of the credit-spread edge
- [[implied-volatility]], [[theta]], [[vega]] -- the Greeks that drive the position
- [[assignment]], [[pin-risk]] -- key short-leg risks near expiration
- [[edge-taxonomy]] -- classification of the risk-bearing/behavioral edge

## Sources
General market knowledge; no specific wiki source ingested yet.
