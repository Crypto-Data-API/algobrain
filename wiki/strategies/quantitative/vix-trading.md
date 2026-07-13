---
title: "VIX Trading"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [vix, volatility, vix-futures, contango, roll-yield, short-volatility, long-volatility, mean-reversion, quantitative]
aliases: ["VIX Trading Strategy", "Volatility Trading", "Short Vol", "VIX Futures Trading"]
strategy_type: quantitative
timeframe: swing|position
markets: [stocks]
complexity: advanced
backtest_status: untested
related: ["[[tail-risk-hedging]]", "[[garch-volatility]]", "[[regime-detection]]", "[[dispersion-trading]]", "[[options]]"]
---

# VIX Trading

## Overview

VIX trading involves taking positions in VIX futures and exchange-traded products (ETPs) to profit from changes in market volatility expectations. The VIX -- the CBOE Volatility Index -- measures 30-day implied volatility of S&P 500 options and is often called the "fear gauge." But you **cannot trade the VIX index directly**. Instead, traders use VIX futures, VIX options, and ETPs like VXX (long vol), UVXY (2x long vol), and SVXY (short vol) to express volatility views.

The single most important structural feature of VIX markets is **contango** -- the tendency for VIX futures to trade above the VIX spot index. Because volatility is mean-reverting (spikes are temporary and revert to a long-run average of ~15-20), the futures curve is typically upward-sloping. This creates **roll yield decay** for long volatility positions: as a VIX futures contract approaches expiration, it converges downward toward the lower spot VIX, causing long vol ETPs to lose value over time. Conversely, short volatility positions **harvest this roll yield**, earning a steady income in calm markets.

This structural decay has made short volatility one of the most popular (and dangerous) strategies in modern markets. SVXY and similar products printed steady returns in low-vol regimes -- until they didn't. The February 2018 "Volmageddon" event saw XIV (inverse VIX ETP) lose 96% in a single day when VIX spiked from 17 to 50 and the entire short-vol complex imploded. The lesson: short vol is "picking up pennies in front of a steamroller" -- consistent small gains punctuated by catastrophic losses.

## How It Works

### VIX Term Structure
- **Contango (normal):** VIX futures > VIX spot. Occurs ~80% of the time. Short vol strategies profit from roll yield.
- **Backwardation (fear):** VIX spot > VIX futures. Occurs during market stress (crashes, crises). Long vol strategies profit; short vol strategies suffer catastrophic losses.

### Roll Yield Mechanics
VIX ETPs hold futures contracts and must roll them monthly. In contango, they sell expiring (cheaper) contracts and buy deferred (more expensive) contracts -- buying high, selling low. This creates a structural drag of roughly 5-10% per month on long-VIX ETPs like VXX. Over time, VXX has lost 99.9%+ of its value due to this persistent decay.

Short-vol ETPs (SVXY) earn this roll yield: they sell deferred (expensive) contracts and buy expiring (cheap), profiting from the convergence. But when contango flips to backwardation, the roll yield reverses and losses compound rapidly.

### Mean Reversion
VIX is one of the most reliably mean-reverting instruments in finance. Spikes above 30-40 almost always revert within days to weeks. This creates opportunities to **sell VIX spikes** (short VIX futures or buy SVXY after fear events) with high win rates. However, the magnitude of the spikes that don't revert (2008, 2020) can be portfolio-ending for overleveraged positions.

## Rules / Application

### Short Volatility (Harvesting Roll Yield)
1. **Enter short VIX futures** or **buy SVXY** when the VIX term structure is in steep contango (front-month future / VIX spot ratio > 1.05).
2. Hold through the contango, collecting roll yield as futures converge to spot.
3. **Exit immediately** when contango flips to backwardation (term structure inverts) -- this signals a regime change to fear.
4. **Position size conservatively:** Never allocate more than 5-10% of portfolio to short vol. The asymmetric risk (small gains, huge losses) demands small positions.
5. **Hard stop:** Exit if VIX rises above 30 (or if VIX futures rise more than 20% in a single session).

### Long Volatility (Crash Protection)
1. **Buy VIX call options** or **buy VXX/UVXY calls** when VIX is below 15 (complacency) and you anticipate a risk event.
2. Accept the **time decay cost** -- long vol positions bleed value daily in calm markets.
3. **Exit on VIX spikes** above 25-30 for partial profits, above 40 for full exit.
4. Use as a [[tail-risk-hedging]] overlay: allocate 1-3% of portfolio to long-vol positions as portfolio insurance.

### Mean Reversion Trades
1. After a VIX spike above 30, wait for the first close below the 10-day moving average.
2. **Short VIX futures** or **buy SVXY** targeting a return to VIX 18-22.
3. **Stop-loss:** If VIX makes a new high above the spike peak, exit.
4. **Profit target:** VIX returns to 20 (or the 200-day average).
5. Historical win rate for this setup: ~70-80% over the past 20 years.

## Example

**Setup:** VIX mean-reversion trade after a market selloff.

1. **Day 0:** S&P 500 drops 4% on a geopolitical shock. VIX spikes from 16 to 34. VIX futures (front month) at 29. Term structure inverts to backwardation.
2. **Day 3:** S&P stabilizes. VIX pulls back to 28. Futures remain at 27. Term structure flattens.
3. **Day 5:** VIX closes at 24, below its 10-day MA (26.5). Term structure returns to mild contango. **Enter short:** Sell 2 VIX front-month futures at 24.50.
4. **Day 12:** Fear dissipates. VIX falls to 19. VIX futures at 20. **Exit:** Buy back at 20.
5. **Profit:** (24.50 - 20.00) x 2 contracts x $1,000/point = **$9,000**.
6. The trade worked because the spike was event-driven (geopolitical) rather than structural (recession), and VIX's mean-reverting nature asserted itself within 2 weeks.

## Advantages

- **Structural edge:** VIX contango and mean reversion are well-documented, persistent market phenomena -- not ephemeral alpha
- Short vol strategies produce **consistent income** in calm markets (which represent ~80% of the time)
- VIX mean-reversion trades have **high win rates** (70-80%) after spikes
- VIX products provide **portfolio insurance** -- a small long-vol allocation can offset large equity losses during crashes
- Liquid market: VIX futures trade ~200K contracts/day with tight spreads
- The VIX ecosystem (futures, options, ETPs) offers flexible ways to express volatility views across timeframes

## Disadvantages

- **Catastrophic tail risk:** Short vol strategies can lose 50-100% in a single day during volatility explosions (Volmageddon 2018, COVID March 2020)
- Long vol positions **bleed continuously** in calm markets -- the cost of protection is real and persistent (VXX loses ~60-70% per year from roll decay)
- VIX ETPs are **not a direct proxy for VIX** -- tracking error, roll costs, and rebalancing create significant divergence from the spot index
- **Path dependency:** VIX ETP returns depend heavily on the path of volatility, not just the level -- two identical VIX endpoint values can produce wildly different ETP returns
- Regulatory and structural changes (XIV termination, SVXY leverage reduction from -1x to -0.5x) can alter the payoff profile without warning
- [[regime-detection]] is critical: short vol in a true crisis regime (not just a spike) can be catastrophic, but distinguishing spikes from regime changes is extremely difficult in real-time
- The popularity of short-vol strategies has compressed the roll yield premium over time, reducing expected returns

## See Also

- [[tail-risk-hedging]] -- long-vol portfolio insurance strategy
- [[garch-volatility]] -- volatility forecasting to time VIX entries
- [[regime-detection]] -- identifying whether a VIX spike is a temporary event or a regime change
- [[dispersion-trading]] -- another volatility strategy comparing index vs single-stock vol
- [[options]] -- the underlying instruments from which VIX is derived
