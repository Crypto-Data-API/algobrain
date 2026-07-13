---
title: Stop Hunting & Liquidity Sweeps
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [combinations, alpha-edge, smart-money, liquidity, stop-hunting, price-action, institutional-trading]
strategy_type: hybrid
markets: [forex, crypto, futures]
complexity: advanced
backtest_status: untested
related: [smart-money-orderflow-combo, contrarian-extremes, structural-forced-selling, cross-asset-signals]
---

# Stop Hunting & Liquidity Sweeps

## The Edge

Every stop loss is someone else's market order. When your stop triggers, you sell at market -- and someone is buying your forced exit. That someone is the counterparty profiting from your pain.

This is not conspiracy theory. It is market microstructure. Large players -- [[market-makers]], proprietary desks, hedge funds -- need liquidity to fill massive orders. A fund wanting to buy 50,000 contracts cannot do so in a thin market without moving price against itself. But if it can push price down 10 ticks to trigger a cascade of retail stop losses, those stops become a wave of market sell orders that the fund absorbs as its entry. Price then reverses because the selling was artificial -- forced, not fundamental.

The edge: instead of being the prey (stop gets hunted), become the predator. Wait for the sweep, let the amateurs get shaken out, then enter with the smart money on the reversal.

## Why It Persists

Retail traders place stops at textbook levels. Every trading course teaches the same thing: stop below the swing low, stop above the swing high, stop below the [[support-and-resistance|support line]], stop at the round number. This creates dense clusters of stop orders at predictable locations that are visible on the [[order-book]] and inferable from chart structure.

Institutions know exactly where these clusters sit. They have access to order flow data, exchange-reported stop concentrations, and decades of pattern recognition. The hunt is rational -- it is the cheapest source of liquidity available. This edge persists because:

1. **Retail education is standardized** -- everyone learns the same stop placement rules
2. **The behavior is self-reinforcing** -- even traders who know about stop hunts still place stops at obvious levels because "that's where the invalidation is"
3. **Institutions NEED liquidity** -- large orders require counterparties, and stop clusters provide them on demand
4. **Algorithms automate the hunt** -- HFT firms run stop-hunting algos 24/7 in forex and crypto

This is the core mechanic underlying [[smart-money-concepts]] and the ICT (Inner Circle Trader) methodology.

## How to Implement

### Step 1: Identify Obvious Stop Clusters

Map where the majority of stops are sitting. Look for:

- **Below swing lows** on the daily/4H chart -- every trend-follower has stops here
- **Above swing highs** in a downtrend -- shorts have stops above recent peaks
- **Below key support zones** -- the more times a level has held, the more stops sit just below it
- **Round numbers** (1.3000 in EUR/USD, $50,000 in BTC) -- psychological levels attract stops
- **Below/above trendlines** -- textbook stop placement

### Step 2: Wait for the Sweep

Do NOT front-run the sweep. Wait for price to:

1. Break below support (or above resistance) -- this triggers the stop cluster
2. Show a **wick** or **spike** that penetrates the level by 5-20 pips / 0.5-2%
3. Demonstrate immediate rejection -- price starts reversing back inside the prior range

Look for confirmation via [[order-flow]] tools: [[absorption]] on the [[footprint-chart]], aggressive buying appearing on the bid, [[delta-divergence]] showing buyers stepping in despite the breakdown.

### Step 3: Enter on Reversal Confirmation

- Enter when the candle **closes back inside** the prior range (above broken support / below broken resistance)
- Use [[candlestick-patterns]] for confirmation: [[bullish-engulfing]], [[hammer]], or [[pin-bar]] on the reversal candle
- Timeframe: 15m or 1H for entry, 4H/daily for structure identification

### Step 4: Stop and Target

- Stop below the sweep low (the wick extreme) -- if that level breaks, the move is real, not a hunt
- Target: the opposite side of the range, or the next liquidity pool above (where shorts have their stops)
- Risk:reward typically 1:2 to 1:4 because entries occur near the extreme of the move

## Example Setup

**BTC/USD -- January 2025 sweep setup:**

1. BTC consolidates between $41,000 (support) and $44,000 (resistance) for two weeks
2. Obvious stop cluster below $40,800 (round number + swing lows + trendline confluence)
3. Sunday night low-liquidity session: price spikes to $40,200 -- a $600 wick below support
4. [[volume-analysis]] shows massive volume on the sweep candle (stops triggering)
5. Price immediately reverses, closing the 1H candle at $41,300 (back inside range)
6. Entry: $41,300 on the close. Stop: $40,100 (below sweep wick). Target: $44,000 (range high)
7. Risk: $1,200. Reward: $2,700. R:R = 1:2.25
8. Price reaches $44,000 within 5 days as the "breakdown" was entirely a liquidity sweep

## Risk Management

- **Only trade sweeps at significant levels** -- not every wick is a hunt. The level must have clear stop-loss logic (obvious swing low/high, round number, high-volume node)
- **Require reversal confirmation** -- a sweep that does not reverse is a genuine breakout. Never fade a breakdown blindly
- **Size conservatively** -- max 2% risk per trade. The setup is high-probability but not infallible
- **Beware of second sweeps** -- sometimes the first reversal is a trap and the real sweep goes deeper. Use the deepest wick as your stop
- **Low-liquidity sessions** increase sweep frequency (Asia session in forex, weekends in crypto) but also increase slippage risk
- Combine with [[volume-profile]] to confirm that the sweep occurred in a low-volume node (price was never supposed to stay there)

## Real-World Examples

- **GBP/USD flash crash (Oct 2016)** -- price swept stops 600+ pips below support in seconds during the Asia session, then reversed nearly the entire move within hours. Traders who bought the sweep made 5x their risk
- **BTC $28,800 sweep (June 2023)** -- months of support at $29,000 created a massive stop cluster below. Price wicked to $28,800, immediately reversed, and rallied to $31,000 within a week
- **E-mini S&P futures** regularly sweep the overnight low by 2-5 points at the NYSE open, triggering stops from overnight session traders, before reversing for the intraday trend
- **Forex "stop hunts" before London open** -- price runs the Asia session high or low by 10-20 pips, triggers stops, then trends in the opposite direction for the London session

The pattern is universal across all liquid markets because the mechanism is structural, not discretionary. Where there are clustered stops, there are institutions ready to harvest them.
