---
title: "Liquidity Sweeps"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [technical-analysis, market-microstructure, liquidity, order-types]
aliases: ["liquidity sweep", "stop hunt", "stop-hunting", "Stop Hunting", "liquidity grab", "liquidity raid"]
domain: [market-microstructure, technical-analysis]
difficulty: intermediate
related: ["[[smart-money-concepts]]", "[[order-blocks]]", "[[liquidity]]", "[[break-of-structure]]", "[[market-maker]]", "[[order-flow]]"]
---

A liquidity sweep is a price move that extends beyond a significant swing high or swing low to trigger clustered stop-loss orders, providing [[liquidity]] for institutional participants to fill large positions at favorable prices. In [[smart-money-concepts]] trading, liquidity sweeps are viewed as engineered moves by "smart money" to access pools of resting orders before reversing price in the intended direction.

## The Mechanics

Every stop-loss order becomes a market order when triggered. Stop-losses below swing lows are sell stops; when triggered, they become market sell orders. Stop-losses above swing highs are buy stops; when triggered, they become market buy orders. Institutions needing to accumulate a large long position benefit from triggering sell stops below support -- the cascade of market sell orders provides the volume they need to buy without pushing price up against themselves.

This is the same mechanism described in detail in [[stop-hunting-and-liquidity-sweeps]], but viewed here through the lens of individual trade setups rather than as a standalone strategy.

## Types of Liquidity

### Buy-Side Liquidity (BSL)

Buy-side liquidity refers to buy stop orders resting above swing highs, equal highs, and resistance levels. Short sellers place stop-losses above these levels, and breakout traders place buy stops to enter above them. When price sweeps above these levels, it triggers this pool of buy orders. In a bearish context, institutions use the resulting buying pressure to fill short positions at higher prices before reversing price downward.

### Sell-Side Liquidity (SSL)

Sell-side liquidity refers to sell stop orders resting below swing lows, equal lows, and support levels. Long traders place stop-losses below these levels. When price sweeps below, it triggers a cascade of sell orders. In a bullish context, institutions use this selling pressure to accumulate long positions at lower prices before reversing price upward.

## Identifying Liquidity Pools

Not all swing highs and lows hold equal liquidity. The richest pools tend to form at:

- **Equal highs and equal lows**: when price makes two or more swing points at nearly the same level, stops cluster densely just beyond. These "clean" levels are obvious targets because every trader sees the same level
- **Trendline liquidity**: stops placed beyond ascending or descending trendlines accumulate over time as more traders reference the same line
- **Round numbers**: psychological levels like $50,000 in BTC or 1.3000 in EUR/USD attract both stops and limit orders
- **Session highs and lows**: the previous day's high, the Asian session low, or the weekly high/low are levels where stops naturally cluster
- **Range boundaries**: the longer a consolidation range holds, the more stops accumulate just beyond its edges

## Judas Swings

A Judas swing is a specific type of liquidity sweep that occurs at the open of a trading session, particularly the London or New York open. Price initially moves in the opposite direction of the session's true intent -- sweeping liquidity above or below the Asian session range -- before reversing sharply. The name reflects the deceptive nature of the move: it "betrays" early-session traders who entered in the direction of the initial push.

In [[smart-money-concepts|ICT methodology]], Judas swings are a key setup. Traders wait for the initial sweep at the session open, observe a [[break-of-structure]] in the opposite direction, then enter with the reversal targeting the opposing liquidity pool.

## Sweeps and Reversals

The relationship between liquidity sweeps and reversals is central to SMC trading. A sweep that is followed by strong displacement (impulsive candles, [[fair-value-gaps]], and a [[break-of-structure]]) signals that institutions have filled their orders and price is now moving in the intended direction. Conversely, a sweep that leads to sustained price continuation beyond the swept level is not a sweep at all -- it is a legitimate breakout.

Key confirmation signals after a sweep:

- A [[break-of-structure]] on the lower timeframe in the opposite direction of the sweep
- Formation of an [[order-blocks|order block]] at the reversal point
- Creation of a [[fair-value-gaps|fair value gap]] as price moves away from the sweep level
- [[order-flow]] data showing [[absorption]] or [[delta-divergence]] at the swept level

## Trading Relevance

Liquidity sweeps are actionable in two opposite ways, and conflating them is the most common error:

- **As an entry signal.** A trader can wait for price to sweep an obvious pool (equal highs/lows, prior-day extreme, round number), then enter *with* the reversal once a [[break-of-structure]] confirms — targeting the opposing liquidity pool as the exit. The stop sits just beyond the sweep wick, giving an asymmetric risk/reward because the swept level should not be revisited if institutions have genuinely absorbed the orders.
- **As a stop-placement warning.** Because clustered stops *are* the liquidity being targeted, placing a stop at the textbook level (just under the swing low, just over the round number) is placing it exactly where a sweep is most likely to hit. The defensive lesson is to place stops beyond the *next* structural level, or to size positions so that being swept is survivable.

It is important to treat sweeps as a probabilistic, microstructure-grounded read, not a guaranteed reversal. A sweep that produces continuation rather than reversal is simply a [[breakout]] — the only reliable distinction is post-sweep displacement and structure, not the sweep itself. The underlying mechanism (resting stops becoming market orders that provide fills for larger participants) is real and venue-agnostic; the [[smart-money-concepts|SMC]] framing around it is interpretive overlay.

## Related

- [[smart-money-concepts]] -- the methodology that frames liquidity sweeps as institutional tools
- [[stop-hunting-and-liquidity-sweeps]] -- detailed strategy page covering stop hunting mechanics and trade implementation
- [[liquidity]] -- the broader concept of market liquidity that sweeps exploit
- [[order-blocks]] -- zones that often form at the point of reversal after a sweep
- [[fair-value-gaps]] -- imbalances created by the displacement move following a sweep
- [[break-of-structure]] -- the structural confirmation that a sweep has led to a genuine reversal
- [[market-maker]] -- entities that benefit from and often facilitate liquidity sweeps

## Sources

- Michael J. Huddleston (ICT). *Inner Circle Trader* mentorship materials — origin of the Judas swing, buy-side/sell-side liquidity, and liquidity-sweep terminology in retail SMC trading.
- Harris, Larry. *Trading and Exchanges: Market Microstructure for Practitioners* (2003) — the underlying microstructure of stop orders, stop runs, and the conversion of triggered stops into market orders.
- Osler, Carol L. "Stop-Loss Orders and Price Cascades in Currency Markets." *Journal of International Money and Finance* 24(2), 2005 — empirical evidence that clustered stop orders produce predictable price cascades, the documented mechanism behind sweeps.
