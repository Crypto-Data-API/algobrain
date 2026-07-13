---
title: "Gamma Scalping"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [options, gamma, delta-hedging, volatility, market-neutral, dynamic-hedging, market-making]
aliases: ["Gamma Trading", "Long Gamma Scalping", "Delta-Neutral Gamma Trading"]
strategy_type: quantitative
timeframe: day|swing
markets: [stocks, crypto]
complexity: advanced
backtest_status: untested
related: ["[[straddle-strangle]]", "[[volatility-arbitrage]]", "[[delta]]", "[[gamma]]", "[[theta]]", "[[implied-volatility]]", "[[option-volatility-and-pricing]]"]
---

# Gamma Scalping

## Overview

Gamma scalping is an advanced, market-neutral [[options]] strategy that profits from the dynamic relationship between [[gamma]] and [[theta]]. The trader buys options (establishing a long [[gamma]] position, typically through a [[straddle-strangle|straddle or strangle]]) and then continuously delta-hedges by trading the underlying asset. Each time the underlying moves, the position's [[delta]] shifts due to gamma, and the trader scalps that delta back to neutral by buying low and selling high in the underlying.

The core insight is elegant: **long gamma positions become longer when the price rises and shorter when it falls**, creating a natural "buy low, sell high" dynamic when you hedge back to delta-neutral (Source: [[book-option-volatility-and-pricing]]). The strategy profits when **realized volatility exceeds implied volatility** -- that is, when the actual price moves generate more hedging profit than the daily [[theta]] decay costs (Source: [[book-option-volatility-and-pricing]]). It is the bread-and-butter strategy of professional options [[market-maker]]s and volatility traders.

## Rules

### Entry
1. **Buy an ATM [[straddle-strangle|straddle]]** (or strangle) to establish a long gamma position. ATM options have the highest gamma.
2. **Delta-hedge to neutral:** Immediately offset any net delta by buying or selling shares/futures of the underlying. The combined position should have near-zero delta.
3. **Select expiration carefully:** Shorter-dated options have higher gamma (more sensitivity to moves) but also higher [[theta]] (faster decay). 14-30 DTE is a common sweet spot.
4. **Enter when implied vol is low relative to expected realized vol.** If you believe the stock will move more than the options market implies, gamma scalping has a positive expected value.

### Exit
1. **Re-hedge at fixed intervals or fixed delta thresholds:** Common approaches include hedging every $1 move in the underlying, every hour, or whenever delta exceeds +/-0.30.
2. **Daily P&L tracking:** Compare the scalping profits (from delta-hedging trades) against the theta decay. If realized vol is consistently below implied, the strategy is losing money -- exit.
3. **Close before expiration:** Gamma becomes extreme in the final days (gamma risk), and hedging costs spike. Close the position 3-5 days before expiry.
4. **Profit target:** Exit when cumulative scalping profits exceed the original premium paid by a satisfactory margin (e.g., 20-50% of the initial debit).

### Position Sizing
Risk the total premium paid (straddle cost) per position. This should be no more than 2-3% of the account. Transaction costs from frequent hedging trades must be factored into the sizing calculation.

## Indicators Used
- [[gamma]] -- the core Greek; measures how much delta changes per $1 move in the underlying. Higher gamma = more scalping opportunities.
- [[theta]] -- the daily cost of holding the long options position. The "hurdle rate" that scalping profits must exceed.
- [[delta]] -- tracked continuously; hedged back to zero after each scalp.
- [[implied-volatility]] vs. [[realized-volatility]] -- the fundamental comparison. Profitable when realized > implied.
- [[vega]] -- exposure to changes in IV. A rise in IV benefits the position; a fall hurts.
- [[atr]] -- estimates expected daily range to gauge whether scalping will cover theta.

## Example Trade
**Asset:** SPY trading at $520, 21 DTE
1. **Buy 1 SPY $520 straddle** for $12.00 ($1,200 total). Position is approximately delta-neutral.
2. **Day 1:** SPY rallies to $525. The position now has +30 delta (gamma effect). Sell 30 shares of SPY at $525 to return to delta-neutral. Scalp profit: locked in ~$150 from the delta shift.
3. **Day 2:** SPY drops to $518. The position now has -40 delta. Buy 40 shares at $518. The previously sold 30 shares at $525 represent a $210 profit. Scalp profit: ~$280 cumulative from underlying trades.
4. **Daily theta cost:** Approximately $50/day. After 2 days of active moves, scalping profit ($280) exceeds theta cost ($100). Net gain: +$180.
5. **After 14 days:** If SPY continues moving ~$5/day, cumulative scalping profits: ~$1,800. Cumulative theta decay: ~$700. Close the straddle for remaining value (~$300). **Net profit: ~$1,400.**
6. If SPY had been calm (moving $1-2/day), scalping profits would not cover theta, and the trade would lose.

## Performance Characteristics
- **Win Rate:** 40-55%. Depends heavily on whether realized vol exceeds implied vol during the holding period.
- **Profit Factor:** 1.5-3.0 in volatile markets. Below 1.0 in calm markets.
- **Best Market Conditions:** High-realized-volatility environments. Markets with frequent intraday swings. Periods where options are cheaply priced relative to actual movement.
- **Worst Market Conditions:** Low-realized-volatility environments where the underlying barely moves. Theta eats the position alive.

## Advantages
- **Market-neutral:** Profits do not depend on price direction, only on the magnitude of movement
- **Systematic "buy low, sell high":** Gamma creates a mechanical edge in the underlying hedging trades
- **Exploitable edge:** When realized vol exceeds implied vol, the strategy has a genuine statistical advantage
- **Scales well:** Professional desks run gamma scalping across hundreds of underlyings simultaneously

## Disadvantages
- **High transaction costs:** Frequent hedging trades generate substantial commission and slippage costs
- **[[theta]] decay is relentless:** If the underlying does not move enough, the premium bleeds away daily
- **Requires continuous monitoring:** Cannot be set and forgotten; hedging decisions are constant
- **Execution-dependent:** The choice of hedging frequency and thresholds materially impacts returns
- **Complex P&L attribution:** Difficult for beginners to separate scalping profits from theta losses and IV changes
- **Capital intensive:** Straddles are expensive, and the underlying hedging trades require additional capital/margin

## See Also
- [[straddle-strangle]] -- the option structure used to establish the long gamma position
- [[volatility-arbitrage]] -- the broader framework of trading implied vs. realized volatility
- [[delta]] -- the Greek being continuously hedged
- [[gamma]] -- the core Greek that drives the strategy's mechanics
- [[theta]] -- the daily cost that scalping profits must overcome
- [[market-maker]] -- professional participants who use gamma scalping as a core trading method

## Sources
- [[book-option-volatility-and-pricing]] — Natenberg devotes extensive coverage to dynamic hedging, the gamma-theta trade-off, and the mechanics of delta-neutral gamma trading that form the foundation of this strategy
