---
title: "Collar Strategy"
type: strategy
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [options, hedging, collar, protective, equity-options, defined-risk, risk-management]
strategy_type: quantitative
timeframe: position
markets: [stocks, options]
complexity: beginner
backtest_status: untested
edge_source: [risk-bearing]
edge_mechanism: "Not a profit edge but a risk-transfer trade: pay for a downside floor by selling away the upside tail, transferring tail risk to a counterparty who wants it; the 'edge' is cheaper, bounded risk through an uncertain window."
crowding_risk: low
related: ["[[collar]]", "[[protective-put]]", "[[covered-call]]", "[[married-put]]", "[[risk-reversal]]", "[[hedging]]", "[[the-greeks]]", "[[implied-volatility]]", "[[edge-taxonomy]]"]
---

# Collar Strategy

The full strategy guide -- overview, rolling and adjustments, and detailed payoff analysis -- lives on [[collar]]. This page adds the rigorous edge/risk framing. The collar combines **long stock** + a purchased OTM [[protective-put|put]] (downside floor) + a sold OTM [[covered-call|call]] (caps upside and funds the put). When the call premium equals the put premium it is a **zero-cost collar**.

## Edge source

The collar is fundamentally a **risk-bearing / risk-transfer** structure (see [[edge-taxonomy]]), not a return-generating edge. The holder *gives up* expected value -- you sell the right tail (upside above the call strike) to pay for the left-tail floor (the put). It is the equity-hedger's tool: the "edge," if any, is **survivable, bounded risk** through a period of elevated uncertainty, plus a mild structural tilt -- equity put skew means downside puts are expensive, but the call you sell against them is also bid, so a zero-cost collar can often be struck with the floor closer to spot than the cap.

## Why this edge exists

There is a willing counterparty on each leg:

- The **put** you buy is sold by someone harvesting the [[variance-risk-premium]] (a vol seller paid to bear tail risk).
- The **call** you sell is bought by a bullish speculator or a vol/lottery buyer who wants the upside convexity.

You sit in the middle, exchanging an unwanted left-tail for an unneeded right-tail. The trade exists because hedgers (executives with concentrated stock, PMs protecting gains, pre-retirees) value loss-avoidance more than the marginal upside, while speculators value the upside more than you do. Both sides get what they want; the collar is the clearing of those preferences.

## Null hypothesis

If options are fairly priced and the put and call IVs are symmetric, the collar is a **pure risk-reduction with zero expected alpha**: you have simply truncated the return distribution at both ends, and the expected P&L equals long-stock minus the (small) net cost and frictions. Under the null there is no free lunch -- the value is entirely in variance reduction, not in expected return. Any belief that the collar "adds return" is the no-edge baseline failing: it lowers volatility and tail risk, and in exchange lowers expected return by the foregone upside.

## Rules

**Strike & DTE selection**
- Own (or buy) 100 shares per collar.
- **Buy 1 OTM put** ~5-10% below spot -> sets the floor.
- **Sell 1 OTM call** ~5-10% above spot -> funds the put. Adjust strikes until net premium ≈ $0 for a zero-cost collar.
- Both legs **same expiration**, 30-90 DTE; match the expiration to the duration of the risk you are hedging (e.g. through an earnings or macro event).

**Entry**
- Use when you hold an unrealized gain you want to protect through a defined, uncertain window, and are willing to cap upside to avoid paying for the put.

**Management & exit**
- **Roll up** the put (and call) after a rally to lock in more of the gain.
- **Roll out** in time to extend protection.
- If the stock approaches the **call strike**, decide whether to let it be called away (take the capped gain) or roll the call up-and-out to free upside (usually for a debit).
- Remove the collar when the catalyst passes if you want full upside back.

**Sizing**
- One collar per 100 shares; this is a hedge sized to the underlying position, not a standalone speculative bet.

## Implementation pseudocode

```python
def collar(position, chain, put_otm=0.07, call_otm=0.07, dte=45):
    assert position.shares >= 100
    exp  = pick_expiration(chain, target_dte=dte)
    put  = buy(strike_near(chain.puts(exp),  position.price * (1 - put_otm)))
    call = sell(strike_near(chain.calls(exp), position.price * (1 + call_otm)))
    net  = call.mid - put.mid                 # ~0 for a zero-cost collar
    if abs(net) > tolerance:                  # widen call / tighten put to zero it out
        call = sell(adjust_for_zero_cost(chain.calls(exp), put.mid))
    return Collar(position, put, call, net)

def manage(collar, mark):
    if rallied(collar):                       return roll_up(collar.put, collar.call)
    if near_expiry_and_want_protection(collar): return roll_out(collar)
    if near_call_strike(collar):              return let_assign_or_roll_call_up(collar)
```

## Example trade

*Illustrative hypothetical with round numbers -- not a real trade or backtest.* (See [[collar]] for a fuller worked example.)

You hold 100 shares of XYZ bought at $80, now at $100, and want to protect the $20/share gain through an event 45 days out:

| Leg | Action | Strike | Premium |
|---|---|---|---|
| $93 put | Buy | $93 | $2.00 |
| $108 call | Sell | $108 | $2.00 |
| **Net cost** | | | **$0.00 (zero-cost collar)** |

- **Floor**: effective worst-case sale at $93 -> locked gain ≥ +$13/share.
- **Cap**: called away at $108 -> max gain +$28/share.

| Outcome at expiration | P&L per share |
|---|---|
| XYZ drops to $70 | Put protects: effective $93 -> **+$13** (vs −$10 unhedged) |
| XYZ at $100 | Both expire worthless -> **+$20** |
| XYZ rallies to $120 | Called away at $108 -> **+$28** (forgo $12 above $108) |

The collar guarantees keeping at least $13 of the $20 gain, at the cost of capping upside at $28.

## Performance characteristics

- **Variance-reducing, return-reducing.** The collar trims both tails; expected return falls along with volatility. It does not generate alpha -- it buys peace of mind and a known floor.
- **Positively shaped risk** (unlike short straddles/strangles): the worst case is *defined and small*. This is the opposite of the negative-skew premium-selling trades.
- **Cost depends on skew.** Equity put skew makes the put pricier than the equidistant call, so a true zero-cost collar usually has its cap closer to spot than its floor -- you give up more upside than downside you protect.
- **Drag in bull markets**: repeatedly capping upside underperforms simple long stock when markets rise, which is most of the time. Qualitative -- not a backtested figure.

## Capacity limits

Effectively unconstrained for any realistic individual or institutional book: it is a hedge laid on top of an existing equity position using liquid listed options (or OTC for very large concentrated holdings). Capacity is governed entirely by the liquidity of the underlying's option chain, not by any crowding in the collar itself (low crowding risk).

## What kills this strategy

- **Strong bull market**: the capped upside causes persistent underperformance vs unhedged stock -- the real long-run cost.
- **Assignment / called-away** at the cap strike forces realization of gains (and a taxable event) you may not have wanted.
- **Skew cost**: in high-put-skew names the cap must be set uncomfortably close to fund the floor.
- **Mismatched expiration**: protection that expires before the risk window leaves you unhedged at the worst time.
- **Dividend / early-assignment risk** on the short call around ex-div.

## Kill criteria

- The hedged risk window has passed and you want full upside -> remove or widen the collar.
- The stock approaches the call strike and you do not want to be called away -> roll the call up-and-out before assignment.
- A zero-cost collar would require a cap **tighter than ~3-5%** above spot (skew too steep) -> the trade gives up too much upside; reconsider a simple [[protective-put]] or reduced position size instead.
- Realized opportunity cost (foregone upside) over multiple rolls exceeds your tolerance -> stop collaring; size down the position instead.

## Advantages
- **Defined, bounded risk** -- a hard floor on losses through the chosen window.
- Often **near-zero cash cost** (zero-cost collar).
- Lets long-term holders stay invested (no need to sell shares / realize gains) while hedged.
- Reduces volatility and tail risk of a concentrated position.

## Disadvantages
- **Caps upside** -- the dominant cost; underperforms long stock in rallies.
- **No alpha** -- a risk-transfer, not a return-generating edge.
- Skew can force an unfavorable cap-vs-floor tradeoff.
- Assignment at the cap can trigger unwanted realization / tax events.
- Requires active rolling to stay aligned with the position over time.

## See Also
- [[collar]] -- the full strategy guide (rolling, adjustments, detailed payoff).
- [[protective-put]] -- the downside-only leg (floor without the cap).
- [[covered-call]] -- the upside-cap-for-income leg (cap without the floor).
- [[married-put]] -- long stock + long put established together.
- [[risk-reversal]] -- the options-only analogue (long call / short put or vice versa).

## Sources
- (Source: [[recovering-losing-options-positions]]) — collar use by executives and portfolio managers for hedging concentrated positions (via [[collar]]).
