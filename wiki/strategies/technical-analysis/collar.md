---
title: "Collar"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [options, hedging, collar, zero-cost-collar, protective-collar, defined-risk, equity-options, risk-management]
aliases: ["Zero-Cost Collar", "Protective Collar", "Collar Strategy"]
strategy_type: quantitative
timeframe: position
markets: [stocks, options]
complexity: beginner
backtest_status: untested
related: ["[[married-put]]", "[[covered-call]]", "[[risk-reversal]]", "[[vertical-spreads]]", "[[bull-put-spread]]", "[[protective-puts]]", "[[delta]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]", "[[hedging]]"]
---

# Collar

The collar combines a long stock position with a purchased OTM [[put-option]] (to set a floor on losses) and a sold OTM [[call-option]] (to cap the upside and fund the put). When the premium received from the call equals the premium paid for the put, the hedge is known as a **zero-cost collar**. The result is a bounded risk/reward profile that protects existing gains without requiring a cash outlay. It is one of the most popular [[hedging]] structures for long-term equity holders who want to reduce exposure through uncertain periods while keeping their shares.

## Overview

The collar is the combination of two familiar strategies: a [[protective-puts|protective put]] (downside insurance) and a [[covered-call|covered call]] (income/upside cap). Used together, the call premium finances the put premium, creating near-zero-cost protection. The payoff is bounded on both sides — losses are floored at the put strike and gains are capped at the call strike.

Collars are used extensively by corporate executives hedging concentrated stock positions, institutional portfolio managers protecting gains ahead of macro events, and retail investors approaching retirement or liquidity events who cannot afford a large drawdown. (Source: [[recovering-losing-options-positions]])

## Setup

1. **Own 100 shares** of the underlying stock.
2. **Buy 1 OTM put** — typically 5-10% below the current price. This sets the floor on losses.
3. **Sell 1 OTM call** — typically 5-10% above the current price. Premium received funds the put.
4. Both options share the **same expiration** (30-90 DTE). For a zero-cost collar, adjust strikes until the net premium is near zero.

## Payoff Profile

| Scenario | Outcome |
|---|---|
| Stock below put strike | Loss capped at (stock price - put strike), adjusted for net premium |
| Stock between strikes | Shares retained; small net debit or credit from premiums |
| Stock above call strike | Shares called away; upside capped at call strike |

**Max profit** = call strike - stock entry + net credit (if any).
**Max loss** = stock entry - put strike + net debit (if any).

## Worked Example

Stock AAPL at $185. The trader holds 100 shares with a cost basis of $160 and wants to protect the $2,500 unrealized gain through an upcoming FOMC decision.

- **Buy** 1 AAPL $175 put (45 DTE) for $3.00
- **Sell** 1 AAPL $200 call (45 DTE) for $3.00
- **Net cost**: $0.00 (zero-cost collar)

| Outcome | P&L |
|---------|-----|
| AAPL drops to $150 | Loss floored: sell at effective $175. P&L = ($175 - $160) = **+$15/share** (gains preserved) |
| AAPL stays at $185 | Both options expire worthless. P&L = ($185 - $160) = **+$25/share** |
| AAPL rallies to $220 | Called away at $200. P&L = ($200 - $160) = **+$40/share** (missed $20 above $200) |

The collar guarantees the trader keeps at least $15/share of their $25/share gain, regardless of how far AAPL falls. The cost is capping the upside at $40/share.

## When to Use

- You hold a stock with **significant unrealized gains** and want protection through earnings, macro events, or elevated [[implied-volatility]]
- You are willing to **sacrifice upside** in exchange for eliminating downside tail risk
- IV is elevated enough that the sold call richly finances the protective put
- **Concentrated positions**: Executives, founders, or employees with large allocations to a single stock
- **Near retirement or liquidity events**: When a drawdown would be financially devastating due to timing

## Rolling and Adjustments

Collars can be rolled and adjusted, though the mechanics are more involved than single-leg strategies because both the put and call legs need management. See [[trade-repair-and-rolling]] for the general framework.

### Rolling the Collar at Expiration

If the stock is between the strikes at expiration (the most common outcome), both options expire worthless. To maintain protection, the trader rolls the entire collar:

1. **Buy a new OTM put** for the next cycle
2. **Sell a new OTM call** for the next cycle
3. Adjust strikes based on the new stock price and desired protection range

The cost of rolling depends on [[implied-volatility]]: in high-IV environments, the call premium easily finances the put; in low-IV environments, the trader may need to accept a narrower range or pay a small net debit.

### If the Stock Drops to the Put Strike

The put provides protection — the trader can either:
- **Exercise the put** and sell the shares at the put strike (booking the defined minimum profit)
- **Sell the put** for its intrinsic value and hold the shares if the fundamental thesis is intact
- **Roll down**: Buy back the put, sell a new lower-strike put, and roll the call down too to maintain the collar structure at lower levels

### If the Stock Rallies to the Call Strike

The call will be assigned if ITM at expiration. The trader can either:
- **Accept assignment**: Sell shares at the call strike (booking the defined maximum profit)
- **Roll the call up and out**: Buy back the ITM call and sell a higher-strike call at a later expiration for a net debit. This avoids assignment and raises the upside cap, but costs money. Only worthwhile if the trader has strong conviction in continued upside.

### Adjusting the Width

If market conditions change, the trader can widen or narrow the collar:
- **Widen** (move strikes further apart): More room for profit and loss — less restrictive but more risk
- **Narrow** (move strikes closer together): Tighter protection but smaller profit window. Zero-cost collars often require accepting a narrow range.

## Advantages

- Near-zero or zero cost when strikes are balanced properly
- Defined, bounded risk on both sides with no margin surprises
- Simple to construct — excellent first hedging strategy for beginners
- Can overlay any long-term [[buy-and-hold]] position
- Tax-efficient alternative to selling shares (avoids triggering capital gains)

## Disadvantages

- Upside is strictly capped at the call [[strike-price]] — you miss large rallies
- Rolling the collar at expiration incurs transaction costs and potential slippage
- Zero-cost collars often force a narrow profit window between the strikes
- [[theta]] decay on the put erodes value if the stock stays flat (partially offset by call decay)
- Complexity of managing two option legs vs. a single protective put

## Related

- [[protective-puts]] — the downside protection leg of the collar
- [[covered-call]] — the income-generating leg of the collar
- [[married-put]] — same downside protection without selling the call
- [[risk-reversal]] — a related structure without the stock leg
- [[vertical-spreads]] — the building blocks of the collar's option legs
- [[trade-repair-and-rolling]] — rolling and adjustment framework
- [[gamma-risk]] — risk consideration for near-expiry collar management
- [[hedging]] — the broader discipline of portfolio protection

## Sources

- (Source: [[recovering-losing-options-positions]])
- Cross-referenced from [[protective-puts]], [[covered-calls]], [[hedging]]
