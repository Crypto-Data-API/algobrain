---
title: "Calendar Spread Arbitrage"
type: strategy
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [arbitrage, calendar-spread, futures, contango, backwardation, term-structure, roll-yield, vix, crypto]
aliases: ["Calendar Arb", "Term Structure Arbitrage", "Futures Spread Arbitrage"]
strategy_type: quantitative
timeframe: swing|position
markets: [futures, crypto, commodities]
complexity: intermediate
backtest_status: untested
related: ["[[contango]]", "[[backwardation]]", "[[vix-trading]]", "[[calendar-spread]]", "[[cash-and-carry]]", "[[funding-rate-arbitrage]]"]
---

# Calendar Spread Arbitrage

## Overview

Calendar spread arbitrage trades price discrepancies between different expiry months of the same [[futures]] contract. The term structure of futures prices -- whether a market is in [[contango]] (later months more expensive) or [[backwardation]] (later months cheaper) -- reflects cost of carry, supply/demand dynamics, and market expectations. When the spread between two expiry months deviates from its fair value, an arbitrage opportunity exists.

This strategy is particularly active in three markets: **VIX futures** (where the steep contango creates persistent roll yield opportunities, famously exploited by shorting products like VXX), **crypto quarterly futures** (where perpetual funding rates and quarterly futures create basis spreads), and **energy/commodity futures** (where storage costs, seasonal demand, and production cycles drive term structure dislocations). Unlike simple directional trades, calendar spreads isolate the term structure component, providing a more controlled and often lower-volatility trade.

## How It Works

The calendar spread trader simultaneously takes opposing positions in two different expiry months of the same underlying:

- **Bull spread (buy front, sell back):** Profits when the front month rises relative to the back month -- i.e., when backwardation steepens or contango flattens.
- **Bear spread (sell front, buy back):** Profits when the back month rises relative to the front month -- i.e., when contango steepens.
- **Roll yield capture:** In persistent contango markets, the front-month futures price converges down to spot as expiration approaches. Shorting front-month futures and rolling to the next month captures this "roll yield" decay.

The fair value of the spread is determined by the cost of carry: interest rates, storage costs (for physical commodities), convenience yield, and dividend yield. When the observed spread deviates from the calculated fair value, the arb is triggered.

## Entry/Exit Rules

### Entry
1. **Analyze term structure:** Map the full futures curve and calculate the spread between target expiry months.
2. **Calculate fair value spread:** Use cost-of-carry model (spot price x (1 + risk-free rate - dividend yield) ^ time).
3. **Detect mispricing:** If the observed spread is significantly wider or narrower than fair value, enter the calendar spread.
4. **Enter the spread:** Buy the relatively cheap contract and sell the relatively expensive one. Use spread orders where available to ensure simultaneous execution.

### Exit
1. **Mean reversion:** Exit when the spread reverts to fair value. This is the primary profit mechanism.
2. **Roll before expiry:** Close the near-month leg before it enters the delivery period (especially for physical commodities). Roll to the next month if the thesis persists.
3. **Stop loss:** If the spread widens against you beyond a predefined threshold (e.g., 2x the initial edge), exit to limit losses.
4. **Time-based exit:** If the spread has not converged within the expected timeframe, close to free capital.

## Example Trade

**Market:** VIX futures. Front-month (May) VIX futures at 16.50. Second-month (June) VIX futures at 19.00. Spread: 2.50 points. Historical average spread: 1.50 points. The contango is steeper than normal.

1. **Sell 10 June VIX futures** at 19.00.
2. **Buy 10 May VIX futures** at 16.50.
3. **Spread: 2.50 points** (short June, long May). Each VIX futures point = $1,000 per contract.
4. **Thesis:** The 2.50-point spread is 1.00 point wider than the historical average. Expect mean reversion to ~1.50.
5. **Over 2 weeks, the spread narrows to 1.60.** Close both legs.
6. **Profit:** (2.50 - 1.60) x $1,000 x 10 contracts = **$9,000**.
7. **Margin required:** ~$5,000 per spread x 10 = $50,000. Return on margin: 18%.

## Risk Management

- **Spread blow-out:** In crisis situations, [[contango]] can steepen dramatically (VIX curve inverts in panic, or oil storage fills up). The spread can move far more than expected. Use stop losses.
- **[[liquidity]] risk:** Back-month contracts may have lower [[liquidity]], resulting in wider bid-ask spreads and higher [[slippage]].
- **Delivery risk:** For physical commodity futures, failing to close before the delivery period can result in actual delivery obligations. Always roll well before expiration.
- **Margin changes:** Exchanges may increase margin requirements during volatile periods, forcing position reduction at unfavorable prices.
- **Model risk:** The fair value calculation depends on assumptions about interest rates, storage costs, and convenience yield that may be incorrect or change.
- **Event risk:** An unexpected supply shock, inventory report, or policy announcement can permanently shift the term structure rather than mean-reverting.

## Advantages
- **Lower volatility** than outright futures positions -- the spread dampens directional market moves
- **Lower margin** -- spread positions typically receive margin relief from exchanges
- **Exploits structural inefficiencies** in term structure that persist across market conditions
- **Works in multiple markets** -- applicable to commodities, VIX, crypto, interest rates, and equity index futures
- **Roll yield is persistent** -- contango in VIX and many commodities provides a recurring source of edge

## Disadvantages
- **Requires specialized knowledge** of term structure dynamics, cost of carry, and seasonal patterns
- **Spread convergence is not guaranteed** -- unlike cash-and-carry arb, the spread can widen further before reverting
- **Lower profit potential** per trade compared to directional positions
- **Execution complexity** -- both legs must be managed simultaneously; leg risk exists if spread orders are not available
- **VIX-specific risk:** The short VIX calendar trade was decimated during the February 2018 "Volmageddon" when VIX spiked from 14 to 50 intraday, blowing out the term structure
- **Capital tied up** for weeks or months while waiting for spread convergence

## Real-World Examples
- **Volmageddon (February 5, 2018):** Short VIX strategies that relied on harvesting contango roll yield (including XIV and similar products) lost 90%+ in a single day when VIX spiked and the term structure inverted violently. XIV was liquidated.
- **Oil contango (April 2020):** WTI crude oil futures traded in extreme contango as storage capacity filled. May futures went negative (-$37) while June traded at $20+. Calendar spread traders who bought back-month and sold front-month captured enormous profits.
- **Crypto quarterly futures:** On [[binance]] and OKX, quarterly Bitcoin futures regularly trade at 5-15% annualized premium to spot. Buying spot and selling quarterly futures (a [[cash-and-carry]] variant) is a popular calendar arb in crypto markets.

## See Also
- [[contango]] -- the upward-sloping futures curve that creates roll yield opportunities
- [[backwardation]] -- the inverted futures curve, common in tight supply markets
- [[vix-trading]] -- VIX-specific term structure strategies
- [[cash-and-carry]] -- a related arbitrage that exploits the basis between spot and futures
- [[funding-rate-arbitrage]] -- the crypto equivalent using perpetual swap funding rates
- [[calendar-spread]] -- the broader concept of trading different expiry months
