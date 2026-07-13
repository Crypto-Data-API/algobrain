---
title: "Cash-Secured Put"
type: strategy
created: 2026-04-07
updated: 2026-06-22
status: excellent
tags: [options, income, value-investing]
aliases: ["Cash-Secured Puts", "Cash Secured Put"]
strategy_type: technical
timeframe: swing
markets: [stocks, options]
complexity: beginner
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "Get paid the put premium (a risk-bearing variance premium) for committing to buy a stock you already want at a price you already like; the buyer overpays for downside insurance you are happy to underwrite."
crowding_risk: medium
related: ["[[put-options|put-option]]", "[[covered-call]]", "[[wheel-strategy]]", "[[value-investing]]", "[[protective-put]]", "[[the-greeks]]", "[[theta]]", "[[implied-volatility]]", "[[variance-risk-premium]]", "[[edge-taxonomy]]"]
---

# Cash-Secured Put

A **cash-secured put** involves selling a [[put-options|put option]] while holding enough cash in the account to purchase the underlying stock at the strike price if assigned. The seller collects the option [[premium]] as immediate income and is willing to buy the stock at the strike price -- effectively getting paid to wait for a lower entry.

## Overview

The cash-secured put is a popular income and entry strategy favored by value-oriented investors. Rather than placing a limit buy order and waiting, the trader sells a put at their desired entry price and collects premium for the commitment. If the stock stays above the strike, the put expires worthless and the trader keeps the premium. If the stock falls below the strike, the trader is assigned and buys the stock at an effective cost basis of (strike price - premium received).

Warren Buffett has famously used this approach. In 2008, Berkshire Hathaway sold puts on the S&P 500 and other indices, collecting billions in premiums while expressing willingness to own at lower prices.

The cash-secured put is the first half of the [[wheel-strategy]] cycle: sell puts until assigned, then sell [[covered-call|covered calls]] on the acquired shares until called away, then repeat.

## Edge source

The CSP combines a **risk-bearing** edge with a **behavioral** one (see [[edge-taxonomy]]). The risk-bearing component is the same **[[variance-risk-premium]]** every option seller harvests: implied vol prices above realized, so the put premium overpays for the downside protection it provides. The behavioral / structural component is **willingness-to-own**: because you genuinely want the stock at the strike, the "risk" of assignment is not a risk to you -- it is the plan. You are paid to do something you would do for free (place a buy order lower).

## Why this edge exists

- **Hedgers** buy puts as portfolio insurance and are price-insensitive; they knowingly overpay for protection, which is the premium you collect.
- **Put skew**: demand for downside protection persistently lifts OTM put IV above the statistically fair price.
- **The plan-vs-risk asymmetry**: a put buyer fears the stock falling; a willing owner *welcomes* buying lower. Both sides can be satisfied -- the buyer offloads a tail they dislike, you accept an outcome you wanted anyway -- and you are paid the spread for taking it.

The edge persists because most market participants who want downside protection are structurally short of natural sellers, and because disciplined willingness-to-own is rarer than it sounds (most sellers panic if actually assigned in a falling market).

## Null hypothesis

With no edge, the put is priced fairly and the expected P&L equals **minus costs**. The strategy degenerates into a synthetic limit buy order with a small premium that exactly compensates for the foregone upside if the stock rallies and the downside if it falls -- expectancy ≈ −frictions. The high win rate (OTM puts usually expire worthless) is, as with all short-vol, a product of negative skew: many small premium wins funding occasional large losses when the stock craters well below the strike. A real edge requires net-of-cost expectancy above zero once those assignment-in-a-crash losses are fully counted -- and crucially requires that the assigned stock was actually one worth owning.

## Rules

**Strike & DTE selection**
- Sell an **OTM put** at a strike equal to your genuine desired entry price. **Delta 0.20-0.35** balances premium income against assignment probability (lower delta = safer, less premium).
- **30-45 DTE** to capture the steepest [[theta]] decay.
- Prefer **elevated IV rank** -- richer premium for the same strike.

**Entry**
- **Only on stocks you want to own.** This is the load-bearing rule; never sell puts on a name you would not buy outright.
- Hold cash equal to (strike x 100) per contract -- the "cash-secured" component.

**Management & exit**
- If the stock stays above the strike: let the put expire (or close at ~50% of max profit), then sell the next put.
- If the stock approaches the strike near expiration: either **accept assignment** (you wanted the stock) or **roll** down/out for a credit to defer.
- If assigned: own the stock at (strike - premium) and pivot to selling [[covered-call|covered calls]] (the [[wheel-strategy]]).

**Sizing**
- Risk is (strike - premium) x 100 per contract if the stock goes to zero. Size as if you are buying the stock outright -- because you might be.

## Implementation pseudocode

```python
def cash_secured_put(watchlist, chain, target_delta=0.30):
    for stock in watchlist:
        if not willing_to_own(stock):          # the critical filter
            continue
        if iv_rank(stock) < 30:                # prefer richer premium
            continue
        exp  = pick_expiration(chain, target_dte=35)   # 30-45 DTE
        put  = strike_by_delta(chain.puts(stock, exp), target_delta)
        if not have_cash(put.strike * 100):
            continue
        order = sell(put)
        order.profit_target = 0.50 * order.credit
        return order

def manage(order, mark):
    if order.pnl >= order.profit_target:        return close(order)
    if approaching_strike(order) and want_stock: return accept_assignment(order)
    if approaching_strike(order):                return roll_down_and_out(order)
    if assigned(order):                          return start_wheel(order)  # sell covered calls
```

## Example trade

*Illustrative hypothetical with round numbers -- not a real trade or backtest.*

You want to own stock XYZ (trading at $52) but would prefer to buy near $50. Sell the 35-DTE $50 put:

| Item | Value |
|---|---|
| Strike | $50 |
| Premium received | $1.50 ($150) |
| Cash secured | $5,000 |
| Effective cost basis if assigned | $48.50 |
| Breakeven | $48.50 |
| Max gain | $150 (put expires worthless) |
| Max loss | $4,850 (XYZ -> $0) |

| Outcome at expiration | Result |
|---|---|
| XYZ above $50 | Put expires worthless -> keep $150 (3% on cash in ~5 weeks); sell another |
| XYZ at $50 | Put expires worthless -> keep $150 |
| XYZ at $48.50 | Assigned at $50, cost basis $48.50 -> roughly breakeven, now own shares |
| XYZ at $40 | Assigned at $50 -> unrealized −$10/share, cushioned $1.50 by premium |

In the good case you earn premium for waiting; in the bad case you own a stock you wanted, just earlier and higher than ideal.

## Performance characteristics

- **Negative skew, high win rate.** Like any short put, most expire worthless; the rare loss is a stock that gaps far below the strike. The premium cushions but does not cap the downside.
- **Best behaved in flat-to-rising, high-IV markets**; worst in a market-wide crash where every put is assigned at once *and* the assigned stocks keep falling.
- **Opportunity cost** of cash collateral is real and should be netted against the premium yield (compare against a risk-free rate).
- Edge is modest after spreads, commissions, and the foregone rally if the stock rips higher (you only keep the premium). Qualitative -- not a backtested figure.
- Behaves much like a [[covered-call]] in payoff (both are short a put synthetically), so it is **not** a diversifier against an existing covered-call/long-equity book.

## Capacity limits

Scales well for retail and small funds since it operates on liquid single names and indices, but capacity is bounded by (a) how much **cash** you are willing to tie up as collateral and (b) the open interest / spread on the chosen strike. At larger size the constraint becomes portfolio concentration -- writing many puts is economically equivalent to a large, leveraged long-equity book that all suffers together in a downturn (medium crowding risk).

## What kills this strategy

- **Crash / gap below strike** on a stock that keeps falling -- assignment at a price now well above market.
- **Selling puts on stocks you do not actually want** -- turns assignment from a plan into a forced bad position.
- **Capital tied up** in collateral with low premium yield (low IV) -- poor return on cash.
- **Early assignment** around ex-dividend or on deep-ITM puts, before your intended timeline.
- **Concentration**: many CSPs in correlated names = a hidden, leveraged long book.

## Kill criteria

- Stock's fundamental thesis breaks (you no longer want to own it) -> close the put immediately, do not accept assignment.
- Assigned position falls **>20% below cost basis** with a broken thesis -> exit the stock per your equity stop, not the options plan.
- Premium yield on collateral drops **below the risk-free rate** (IV too low) -> stop writing; hold cash.
- Aggregate CSP notional (sum of strikes x 100) exceeds your intended max long-equity exposure -> stop adding.

## Advantages
- **Get paid to wait**: collect premium while waiting for a stock to reach your buy price.
- **Lower effective cost basis**: if assigned, your entry is (strike - premium), below the strike.
- **Defined, owner-friendly risk**: the worst case is owning a stock you wanted, at a discount to the strike.
- **High probability of profit**: OTM puts expire worthless more often than not.
- **Composable**: the entry leg of the [[wheel-strategy]].

## Disadvantages
- **Downside exposure**: a crash well below the strike produces substantial losses; the premium is a thin cushion.
- **Negatively skewed** payoff -- high win rate masks tail risk.
- **Opportunity cost**: cash is locked as collateral.
- **Assignment timing risk**: you may be assigned before a known catalyst.
- **Capped upside**: a strong rally leaves you with only the premium.

## The Wheel Strategy Connection

The cash-secured put forms the entry leg of the [[wheel-strategy]]:

1. **Sell cash-secured puts** --> collect premium while waiting to buy
2. **Get assigned** --> now own shares at a discount
3. **Sell covered calls** --> collect more premium on shares you own
4. **Get called away** --> sell shares at a premium, return to step 1

## Related Strategies

- [[covered-call]] -- the complementary strategy for when you own shares
- [[wheel-strategy]] -- the complete cycle combining CSPs and covered calls
- [[protective-put]] -- buying puts for protection (opposite direction)
- [[iron-condor]] -- more complex premium-selling structure
- [[covered-call-vs-cash-secured-put]] -- side-by-side comparison of these two income strategies

## Sources

- (Source: [[book-option-volatility-and-pricing]])
