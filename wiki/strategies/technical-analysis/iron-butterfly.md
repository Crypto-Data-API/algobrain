---
title: "Iron Butterfly"
type: strategy
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [options, iron-butterfly, premium-selling, neutral, defined-risk, credit, pinning]
aliases: ["Iron Fly", "Ironfly"]
strategy_type: quantitative
timeframe: swing
markets: [stocks]
complexity: intermediate
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "Selling an ATM straddle wrapped in protective wings harvests the variance/volatility risk premium most aggressively: ATM options carry the largest premium, so the iron fly is the highest-credit defined-risk way to bet that realised volatility will undershoot the implied move."
crowding_risk: medium
related: ["[[iron-condor]]", "[[butterfly-spread]]", "[[straddle-strangle]]", "[[calendar-spread]]", "[[vertical-spreads]]", "[[variance-risk-premium]]", "[[implied-volatility]]", "[[the-greeks]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[pin-risk]]", "[[assignment]]", "[[edge-taxonomy]]"]
---

# Iron Butterfly

## Overview

The Iron Butterfly is a **defined-risk, credit** options strategy that combines a short [[straddle-strangle|ATM straddle]] with long OTM protective wings. Specifically, you **sell 1 ATM call and 1 ATM put** at the same strike, then **buy 1 OTM call** above and **buy 1 OTM put** below to cap the risk. The result is a position that collects a large credit and achieves maximum profit if the underlying pins exactly at the short strike at expiration.

Compared to the [[iron-condor]], the Iron Butterfly has a **tighter profit zone but collects significantly more premium**. The short strikes are at-the-money rather than out-of-the-money, so the probability of max profit is lower, but the credit-to-width ratio is much higher. The Iron Butterfly is essentially the credit version of the [[butterfly-spread]] -- same payoff shape, opposite entry (credit vs. debit). This strategy thrives in **low-volatility, range-bound** environments and is popular on high-IV-rank names where the ATM straddle premium is rich.

## Edge source

Per the [[edge-taxonomy]], the iron butterfly is primarily a **risk-bearing** edge with a **behavioral** overlay. It is the most concentrated way to sell the [[variance-risk-premium]] in a defined-risk wrapper: because the short straddle is *at-the-money*, it collects the richest premium on the chain, betting that realised volatility over the holding period will undershoot the [[implied-volatility]] priced into the ATM straddle. The behavioral overlay is the persistent demand for both downside protection (put skew) and upside speculation (call demand) that keeps option premiums elevated. The two long OTM wings convert the unlimited short-straddle risk into defined risk. Structurally it is a short-[[vega]], positive-[[theta]], short-[[gamma]] position — see [[the-greeks]].

## Why this edge exists

The counterparties are option *buyers*: portfolio hedgers paying for protection, speculators buying lottery-ticket convexity, and the dealer complex warehousing the residual. ATM options command the largest absolute premium, and across history implied volatility has, on average, exceeded subsequently realised volatility — so the ATM straddle seller is overpaid for the moves that actually occur, in exchange for accepting concentrated risk around the strike. The iron fly captures the most premium per trade of any defined-risk credit structure, but it also has the *narrowest* profit zone, so it pays for that premium with a much lower probability of reaching max profit than an [[iron-condor]]. The edge is real but **moderately crowded** (premium-selling is popular), and it is precisely a bet against the move that the rich ATM premium is pricing.

## Null hypothesis

Under the null (no variance risk premium, options fairly priced), the iron butterfly has expected P&L ≈ **−costs**: the large credit collected exactly offsets the expected payout from the underlying's typical move around the ATM strike, leaving commissions and four-leg bid/ask as a guaranteed drag. Because the structure rarely pins exactly and usually settles somewhere along the tent, a *large* credit alone is NOT evidence of edge — the whole thesis rests on realised volatility being lower than the implied move priced into the ATM straddle. If IV ≈ realised (or IV < realised) for a name, the iron fly is a fairly-priced bet whose expectancy is just the frictions, and the high [[gamma]] near expiry makes those frictions and slippage especially punishing.

## Rules / Setup

### Entry
1. **Sell 1 ATM call and 1 ATM put** at the strike nearest the current price. This is the short straddle core.
2. **Buy 1 OTM put** at a lower strike to protect the downside. Typical width: 5-20 points depending on the underlying.
3. **Buy 1 OTM call** at an upper strike, same distance from ATM as the put wing for a balanced fly.
4. **Credit:** The net credit should be 50-75% of the wing width. Higher credits improve the break-even range.
5. **Expiration:** 30-45 DTE. Shorter expirations maximize [[theta]] but increase [[gamma]] risk.
6. **IV environment:** IV rank > 40 is ideal. The higher IV is, the more premium the ATM straddle generates.

### Exit
1. **Profit target:** Close at 25-50% of max profit. Because the position is very sensitive to price movement near expiration, early profit-taking is critical.
2. **Stop-loss:** Close if the loss exceeds 1.5-2x the original credit received.
3. **Time management:** If the price is near the center strike in the final 7 days, [[theta]] accelerates rapidly. If the price has moved to a wing, close to limit further loss.
4. **Adjustment:** If the price drifts, consider converting to an [[iron-condor]] by buying back the tested ATM leg and selling a new OTM option.

### Position Sizing
Max loss = wing width - credit received. Risk no more than 3-5% of the account per iron butterfly. The high credit collected means max loss is smaller than a comparable iron condor.

## Payoff Profile
- **Max profit:** The total net credit received. Occurs when the underlying is exactly at the short strike at expiration.
- **Max loss:** Wing width minus net credit. Occurs when the underlying is at or beyond either wing strike.
- **Break-even (upper):** Short strike + net credit.
- **Break-even (lower):** Short strike - net credit.
- **Greeks at entry:** Near-zero [[delta]], strongly negative [[vega]], positive [[theta]], negative [[gamma]].

## Implementation pseudocode

```python
def manage_iron_butterfly(spot, expect_low_realized_vol, iv_rank, chain, wing):
    if not expect_low_realized_vol or iv_rank < 40:   # only sell rich ATM premium
        return None
    short_call = chain.call(strike=atm(spot), dte=40)
    short_put  = chain.put(strike=atm(spot),  dte=40)
    long_call  = chain.call(strike=atm(spot) + wing, dte=40)   # upper wing
    long_put   = chain.put(strike=atm(spot) - wing,  dte=40)   # lower wing
    credit = (short_call.bid + short_put.bid) - (long_call.ask + long_put.ask)
    if credit < 0.50 * wing:           # credit-to-width below 50% -> not worth the pin risk
        return None
    pos = open_iron_fly(short_call, short_put, long_call, long_put, credit)

    while pos.open:
        value = pos.mark()             # cost to close
        if value <= 0.50 * credit:     # captured ~25-50% of max profit -> take it
            close(pos); break
        if pos.loss >= 1.5 * credit:   # defined-risk stop
            close(pos); break
        if pos.dte <= 21 and abs(spot - pos.center) > wing * 0.5:
            close(pos); break          # drifted toward a wing with rising gamma
        if pos.dte <= 7:
            close(pos); break          # never carry ATM shorts into expiry-week gamma/pin
        if early_assignment_risk(pos.short_call) or early_assignment_risk(pos.short_put):
            close(pos); break
```

## Example Trade

*Illustrative hypothetical with round numbers — not a recommendation or backtest. Note: with balanced wings the net credit is always LESS than the wing width; a credit exceeding the width would imply a risk-free arbitrage and does not occur in practice.*

**Asset:** QQQ trading at **$450**, 40 DTE, IV rank ~55, expecting a quiet range. Wings **$20** wide ($430 / $450 / $470):

1. **Sell 1 × $450 call** at $9.00
2. **Sell 1 × $450 put** at $8.50
3. **Buy 1 × $470 call** at $2.50
4. **Buy 1 × $430 put** at $2.00
- **Net credit** = ($9.00 + $8.50) − ($2.50 + $2.00) = **$13.00** ($1,300 per iron fly)
- **Wing width** = $20.00
- **Max profit** = **$13.00** ($1,300) when QQQ pins exactly at $450 at expiry
- **Max loss** = $20.00 − $13.00 = **$7.00** ($700) when QQQ ≤ $430 or ≥ $470 at expiry
- **Break-even (upper)** = $450 + $13.00 = **$463.00**
- **Break-even (lower)** = $450 − $13.00 = **$437.00**
- **Reward:risk** = 13.00 : 7.00 ≈ **1.86 : 1** (but max profit requires a near-perfect pin)

Payoff at expiration:

| QQQ at expiry | Short straddle value | Long wings value | Net cost to close | P&L (per fly) |
|---|---|---|---|---|
| $430 | $20.00 | $0.00 | $20.00 | −$700 (max loss) |
| $437.00 | $13.00 | $0.00 | $13.00 | $0 (lower break-even) |
| $450 | $0.00 | $0.00 | $0.00 | +$1,300 (max profit, perfect pin) |
| $452 | $2.00 | $0.00 | $2.00 | +$1,100 |
| $463.00 | $13.00 | $0.00 | $13.00 | $0 (upper break-even) |
| $470 | $20.00 | $0.00 | $20.00 | −$700 (max loss) |

In practice you would not hold to expiry — closing at, say, QQQ near $452 a few days early to bank ~$1,100 (~85% of max) avoids the final-week [[gamma]]/[[pin-risk]].

## Performance characteristics

- **Highest credit, narrowest zone**: collects more premium than an [[iron-condor]] but reaches max profit only on a near-perfect pin; most outcomes land partway down the tent. Reward:risk per trade is attractive, but the *probability* of full profit is low.
- **Greeks**: near-zero [[delta]] at entry, strongly short [[vega]] (an IV spike hurts), positive [[theta]] (time decay helps), short [[gamma]] (price movement hurts and accelerates near expiry). Edge is the [[variance-risk-premium]].
- **Cost-aware**: four legs in and four out → up to eight commissions and eight bid/ask crossings per round trip — a heavy drag. ATM strikes are usually liquid, but slippage on a frequent program is material; manage early and use mid limits.
- **No fabricated backtest**: realised edge depends on IV consistently exceeding realised vol and on disciplined early management. Under the null the expectancy is just −costs (see Null hypothesis).

## Capacity limits

Comfortable for retail and small funds on liquid, high-volume underlyings (index ETFs such as SPY/QQQ, mega-cap single names) where ATM strikes are penny-wide with deep open interest. Constraints: (1) **ATM liquidity** — illiquid names have wide ATM spreads that erase the edge; (2) **aggregate short-vega / pin exposure** — many concurrent iron flies all suffer together in a volatility spike, so portfolio tail risk, not order size, is the binding limit. Moderately **crowded** among premium sellers; the per-trade premium has compressed over time.

## What kills this strategy

- **Any decent move**: the narrow profit tent means even a modest trend away from the center erodes or eliminates profit; a move to a wing is the max loss.
- **Volatility expansion**: a rising-IV environment marks the short-vega position to a loss well before expiry.
- **High [[gamma]] near expiry**: in the final week, small price moves create large P&L swings around the ATM short strike.
- **[[pin-risk]]**: at expiration with the underlying near the strike, it is uncertain whether the ATM shorts will be assigned, creating overnight directional risk.
- **Early [[assignment]]**: American-style ATM shorts (especially the call near ex-[[dividend]] or the put when deep ITM) can be assigned early, breaking the hedge.

## Kill criteria

- **Take profit at 25–50% of max credit** — do not chase the perfect pin.
- **Stop-loss when the loss reaches ~1.5× the credit received** (or define max loss as wing width − credit).
- **Manage/close at 21 DTE**, and **hard exit by 7 DTE** if the underlying is near a wing — never carry ATM shorts into expiry-week [[gamma]].
- Close immediately on **early-assignment risk** (short call deep ITM near ex-dividend; short put deep ITM).
- **Portfolio rule**: cut size if a volatility spike pushes aggregate short-vega drawdown past the risk budget.
- Retire a systematic iron-fly program if **rolling 12-month net P&L ≤ 0** net of costs — implied vol is no longer exceeding realised by enough to pay for the pin risk.

## Advantages
- **High premium collected:** The ATM straddle generates significantly more credit than OTM options in an [[iron-condor]]
- **Defined risk:** Wings cap the maximum loss on both sides
- **Superior reward-to-risk ratio:** The credit-to-width ratio is typically 50-75%, better than an iron condor's 25-35%
- **Benefits from [[theta]] and IV crush:** Positive theta and negative vega work in the trader's favor
- **Max profit at a single point:** Simpler thesis than range-based strategies -- you bet on a pin

## Disadvantages
- **Very narrow profit zone:** The break-even range is tighter than an [[iron-condor]] despite the higher credit
- **Low probability of max profit:** The underlying must pin at exactly the ATM strike, which rarely happens
- **High [[gamma]] risk near expiration:** Small price movements create large P&L swings in the final days
- **Assignment risk:** The short ATM options are at high risk of early assignment (American-style options)
- **Requires precise timing:** Best entered 30-45 DTE and closed well before expiration to manage gamma

## See Also
- [[iron-condor]] -- wider profit zone, lower credit; the more popular "cousin" of the iron butterfly
- [[butterfly-spread]] -- the debit version of the same payoff structure
- [[straddle-strangle]] -- the iron butterfly is a risk-defined version of the short straddle
- [[broken-wing-butterfly]] -- asymmetric variant that shifts risk to one side

## Related
- [[variance-risk-premium]] -- the structural source of the iron fly's edge
- [[vertical-spreads]] -- the iron fly is two vertical credit spreads sharing a center strike
- [[the-greeks]], [[theta]], [[vega]], [[gamma]] -- the Greeks that drive the position
- [[pin-risk]], [[assignment]] -- the dominant expiration-week risks
- [[edge-taxonomy]] -- classification of the risk-bearing/behavioral edge

## Sources
General market knowledge; no specific wiki source ingested yet.
