---
title: "Bull Put Spread"
type: strategy
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [options, bull-put-spread, put-credit-spread, credit-spread, bullish, defined-risk]
aliases: ["Put Credit Spread"]
strategy_type: quantitative
markets: [stocks]
complexity: beginner
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "A short put-credit spread sells overpriced downside insurance: it harvests the variance/volatility risk premium plus equity put-skew, taking the other side of investors and funds who systematically overpay for downside protection."
crowding_risk: medium
related: ["[[bear-call-spread]]", "[[bull-call-spread]]", "[[iron-condor]]", "[[vertical-spreads]]", "[[theta]]", "[[variance-risk-premium]]"]
---

# Bull Put Spread

## Overview

The Bull Put Spread (also called a **Put Credit Spread**) is a bullish, defined-risk strategy that collects a net credit at entry. The trader sells a higher-strike [[put-option]] and simultaneously buys a lower-strike put at the same expiration. The sold put generates premium while the bought put limits the maximum loss. The position profits when the underlying stays above the short put strike through expiration, allowing both options to expire worthless and the trader to keep the full credit. It is one of the most widely traded credit spread structures due to its simplicity and favorable risk/reward in bullish or neutral markets.

## Setup

1. **Sell 1 put** at a strike near or slightly below the current stock price (the higher strike).
2. **Buy 1 put** at a lower strike to define the maximum risk. The width between strikes determines the max loss.
3. **Same expiration** -- typically 30-45 DTE to benefit from accelerating [[theta]] decay.
4. **Net credit received** = premium from sold put minus premium paid for bought put.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock above short put strike at expiry | Both puts expire worthless; keep full credit |
| Stock between the two strikes | Partial loss; short put is ITM, long put provides floor |
| Stock below long put strike | Max loss = spread width minus credit received |

**Max profit** = net credit received. **Max loss** = (higher strike - lower strike) - net credit. **Break-even** = short put strike - net credit.

## Edge source

Per the [[edge-taxonomy]], the bull put spread is primarily a **risk-bearing** edge with a **behavioral** overlay. By selling a put-credit spread you collect the [[variance-risk-premium]]: implied volatility tends to trade above subsequently realised volatility, so the put you sell is, on average, priced richer than the moves that actually occur. The additional behavioral component is the equity **put skew** — investors systematically overpay for downside protection — so OTM puts are especially rich. The long lower-strike put converts unlimited risk into defined risk while sacrificing a little of the premium.

## Why this edge exists

The other side is the buyer of downside protection: long-only funds hedging portfolios, retail traders buying puts, and crash-averse investors. They are willing to pay more than the actuarially fair price for insurance because losses hurt more than equivalent gains help (loss aversion) and because hedges have negative expected return but positive utility. The market-maker who buys your short put lays that risk off into the dealer complex. As a net seller of insurance, you earn the premium most of the time and pay out in the (rarer) selloffs — a positive-expectancy but negatively-skewed payoff. The edge is real but **not free**: it is compensation for bearing left-tail risk, and it is moderately **crowded** (premium-selling is a popular retail and fund strategy), which compresses the premium.

## Null hypothesis

Under the null (no variance risk premium, options fairly priced), a short put-credit spread has expected P&L ≈ **−costs**: the credit collected exactly compensates for expected payouts, and you are left paying commissions and bid/ask. The strategy's *entire* edge is the assumption that implied > realised volatility on average. If that premium is absent or already arbitraged away in a name, you are simply selling fairly-priced lottery tickets and lose the frictions. A high win rate is NOT evidence of edge — credit spreads win most of the time by construction (you can win small often and lose big occasionally); only positive expectancy net of the rare max losses proves edge.

## Rules

- **Direction / thesis**: bullish-to-neutral; you expect the underlying to stay above the short put strike.
- **Strike selection**: sell the short put around delta 0.16–0.30 (≈70–84% probability OTM) — a common premium-selling sweet spot — at or below a support level. Buy the long put 1–5 strikes lower to define risk.
- **Width**: chosen so max loss fits position sizing. Collect a credit of roughly **⅓ of the width** (e.g., $0.33 credit on a $1 wide spread) so reward:risk is ~1:2 with a high win probability.
- **DTE**: 30–45 days — the zone of accelerating [[theta]] decay; many programs target ~45 DTE entry.
- **IV environment**: enter when IV rank is elevated (richer premium); avoid selling cheap premium in low-IV regimes.
- **Exit / management**: take profit at **50% of max credit** (the classic tastytrade-style rule). Manage/roll at **21 DTE** to reduce end-of-life [[gamma]] and [[pin-risk]]. Roll the spread out (and down) for a credit if tested, only while the bullish thesis holds.
- **Position sizing**: max loss per spread = (width − credit) × 100; risk ≤ 1–3% of the account per position and cap aggregate short-premium exposure.

## Implementation pseudocode

```python
def manage_bull_put_spread(spot, neutral_to_bullish, iv_rank, chain):
    if not neutral_to_bullish or iv_rank < 30:   # only sell premium when it is rich
        return None
    short_put = chain.put(delta=-0.20, dte=45)            # ~80% OTM probability
    long_put  = chain.put(strike=short_put.strike - width, dte=45)
    credit = short_put.bid - long_put.ask
    if credit < 0.30 * width:                             # not paid enough for the risk
        return None
    pos = open_spread(sell=short_put, buy=long_put, credit=credit)

    while pos.open:
        value = pos.mark()                                # cost to buy back
        if value <= 0.50 * credit:                        # captured 50% of max profit
            close(pos); break
        if pos.dte <= 21:                                 # manage/roll near expiry
            roll_or_close(pos); break
        if value >= 2.0 * credit and short_put.itm:       # tested hard -> defined-risk stop
            close(pos); break
        if early_assignment_risk(pos.short_put):          # deep ITM near ex-dividend
            close(pos); break
```

## Example trade

*Illustrative hypothetical with round numbers — not a recommendation or backtest.*

Stock XYZ trades at **$100**, IV rank elevated, neutral-to-bullish, 45 DTE:

- **Sell 1 × $95 put** for $1.50
- **Buy 1 × $90 put** for $0.50
- **Net credit** = $1.50 − $0.50 = **$1.00** ($100 per spread)
- **Spread width** = $5.00
- **Max profit** = **$1.00** ($100) when XYZ ≥ $95 at expiry
- **Max loss** = $5.00 − $1.00 = **$4.00** ($400) when XYZ ≤ $90 at expiry
- **Break-even** = $95 − $1.00 = **$94.00**
- **Reward:risk** = 1.00 : 4.00 = **1 : 4** (high win probability, small reward, large tail loss)

Payoff at expiration:

| XYZ at expiry | Short $95 put | Long $90 put | Net | P&L (per spread) |
|---|---|---|---|---|
| $105 | 0 | 0 | keep credit | +$100 (max profit) |
| $95 | 0 | 0 | keep credit | +$100 |
| $94.00 | −$1.00 | 0 | credit − $1.00 | $0 (break-even) |
| $92 | −$3.00 | 0 | credit − $3.00 | −$200 |
| $90 | −$5.00 | 0 | credit − $5.00 | −$400 (max loss) |
| $85 | −$10.00 | +$5.00 | credit − $5.00 | −$400 (capped) |

## Performance characteristics

- **Negatively skewed**: many small wins, occasional large losses up to max loss. High win rate (~70–85% depending on short-strike delta) does NOT imply high expectancy; the rare full losses must be smaller in aggregate than the accumulated credits.
- **Greeks**: net long [[delta]] (bullish), net short [[vega]] (an IV spike in a selloff hurts before expiry), net positive [[theta]] (time decay is your friend). The edge is structurally the [[variance-risk-premium]].
- **Cost-aware**: four commissions/legs per round trip and bid/ask on each leg eat into a $1.00 credit — manage at 50% and use mid limits. Selling cheap (low-IV) spreads usually loses to costs.
- **No fabricated backtest**: realised edge tracks the persistence of the VRP and disciplined loss management; under the null it is −costs (see Null hypothesis).

## Capacity limits

Ample for retail and small funds on liquid index ETFs and large-caps. Constraints: (1) **open interest / bid-ask** at the chosen OTM strikes — thin single-name puts have wide spreads that erase a small credit; (2) **aggregate tail exposure** — the binding limit is portfolio left-tail risk, not order size, because correlated short puts all lose together in a crash. The strategy is moderately **crowded**, so the premium per unit of risk has compressed over time.

## What kills this strategy

- **Sharp gap down** through the long strike: realises max loss with no chance to manage; correlated across many positions in a market-wide selloff (the dominant tail risk for premium sellers).
- **Volatility expansion**: a rising-IV selloff marks the spread to a large unrealised loss even before expiry (short [[vega]]).
- **Over-sizing / over-crowding**: too many correlated short-put spreads turn a single bad day into account-threatening loss — the classic "picking up pennies in front of a steamroller" failure.
- **Early [[assignment]]** on the short put when deep ITM near ex-dividend, converting to unwanted long stock.
- **Edge compression**: a persistently low-IV regime offers premium too thin to cover costs and tail risk.

## Kill criteria

- **Stop-loss at a debit of ≥ 2× the credit received** (or define max loss as the full width) on a tested spread.
- **Take profit at 50% of max credit**; **manage or close at 21 DTE.**
- Close immediately on **early-assignment risk** (short put deep ITM near ex-dividend).
- **Portfolio rule**: if aggregate short-premium exposure or a single selloff drawdown exceeds the risk budget (e.g., >15–20% of the book on a stress day), cut size.
- Retire a systematic put-credit program if **rolling 12-month net P&L ≤ 0** (the VRP has compressed below costs) or if a single uncontrolled tail event breaches the kill drawdown.

## When to Use

- You have a **bullish or neutral** outlook and expect the stock to hold above a certain support level.
- You want to collect [[premium]] income with **defined risk** and no margin surprises.
- [[implied-volatility]] is elevated, making the sold put premium attractive relative to realized moves.
- You prefer a high-probability trade with a capped but limited profit potential.

## Advantages
- Credit received at entry -- you are paid to take the position
- Defined risk with no margin blowup scenarios
- Benefits from [[theta]] decay and [[implied-volatility]] contraction
- Simple two-leg structure that is easy to manage and roll

## Disadvantages
- Max profit is capped at the credit received -- limited upside
- A sharp drop through the spread results in the maximum defined loss
- Requires the stock to stay above the short strike -- early assignment risk if the short put goes deep ITM
- Narrow spreads offer small absolute profits; wide spreads require more capital at risk

## See Also
- [[bear-call-spread]] -- the bearish credit spread counterpart
- [[bull-call-spread]] -- a bullish debit spread alternative
- [[iron-condor]] -- combines a bull put spread and a [[bear-call-spread]]
- [[vertical-spreads]] -- the general category of single-width directional spreads

## Related
- [[variance-risk-premium]] -- the structural source of the credit-spread edge
- [[implied-volatility]], [[theta]], [[vega]] -- the Greeks that drive the position
- [[assignment]], [[pin-risk]] -- key short-leg risks near expiration
- [[edge-taxonomy]] -- classification of the risk-bearing/behavioral edge

## Sources
General market knowledge; no specific wiki source ingested yet.
