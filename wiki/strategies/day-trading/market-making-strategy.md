---
title: Market Making Strategy
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags:
  - market-making
  - spread-capture
  - inventory-management
  - algorithmic
  - citadel
  - wintermute
  - adverse-selection
strategy_type: scalping
timeframe: scalp
markets:
  - stocks
  - crypto
  - forex
complexity: advanced
backtest_status: untested
related:
  - "[[scalping]]"
  - "[[order-flow-scalping]]"
  - "[[vwap-trading]]"
  - "[[statistical-arbitrage]]"
  - "[[book-trading-and-exchanges]]"
  - "[[book-flash-boys]]"
  - "[[book-algorithmic-and-high-frequency-trading]]"
  - "[[book-high-frequency-trading-aldridge]]"
---

# Market Making Strategy

## Overview

Market making is the strategy of continuously quoting **both a bid (buy) and an ask (sell) price** on an instrument, profiting from the **bid-ask spread** while managing inventory risk. Market makers provide [[liquidity]] to the market, earning the spread as compensation for taking the other side of trades initiated by aggressive participants. This is the core business model of firms like **Citadel Securities**, **Wintermute**, **Jump Trading**, and **Jane Street**. In practice, market making is almost exclusively **algorithmic** -- requiring automated systems that can quote, hedge, and manage risk in milliseconds. The key challenge is **adverse selection**: being picked off by informed traders who trade aggressively because they have directional conviction (Source: [[book-trading-and-exchanges]]). Successful market making requires sophisticated inventory management, hedging, and the ability to distinguish informed from uninformed order flow.

## Rules

### Entry Rules
1. **Spread Quoting:** Continuously place limit buy orders at the bid and limit sell orders at the ask. The goal is to be filled on both sides, capturing the spread. If the bid-ask spread on BTC/USDT is $50,000.00 x $50,000.50, place a bid at $50,000.10 and an ask at $50,000.40 to capture $0.30 per round trip.
2. **Inventory-Aware Quoting:** Skew quotes based on current inventory. If you are long (accumulated too much inventory), lower the ask price to encourage selling and raise the bid to discourage buying. The Avellaneda-Stoikov model formalizes this (Source: [[book-algorithmic-and-high-frequency-trading]]).
3. **Volatility Adjustment:** Widen spreads during high [[volatility]] (wider spreads compensate for higher adverse selection risk) and tighten spreads during calm markets (compete for flow by offering tighter prices).
4. **Queue Priority:** In traditional markets, being first in the order queue at a price level (price-time priority) is critical. Algorithmic systems optimize for queue position.
5. **Hedging:** When inventory accumulates on one side, hedge the directional risk using correlated instruments (e.g., hedge a BTC spot position with BTC perpetual futures, or hedge single-stock exposure with index futures).

### Exit Rules
1. **Round-Trip Completion:** The ideal exit is completing the other side of the trade -- if you bought on the bid, sell on the ask for the spread profit.
2. **Inventory Limits:** Set maximum inventory thresholds (e.g., never hold more than X units net long or short). If the limit is hit, aggressively unwind by crossing the spread (market order to flatten).
3. **End-of-Day Flatten:** Close all positions before the end of the trading session. Market makers do not take overnight risk.
4. **Loss Limit:** If daily P&L drops below a predefined threshold (e.g., -$10,000), stop quoting and flatten all positions. Reassess market conditions.
5. **Toxicity Detection:** If the fill rate on one side is disproportionately high (e.g., getting hit on the bid 80% of the time), informed sellers are targeting you. Widen spreads or pull quotes temporarily.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| Bid-Ask Spread | Real-time | Core profit mechanism |
| Inventory Position | Real-time tracking | Quote skewing and risk management |
| [[volatility]] (realized, 1-min) | Rolling | Dynamic spread adjustment |
| Order Flow Toxicity (VPIN) | Rolling | Detect informed trading / adverse selection |
| Correlation Matrix | Real-time | Hedging instrument selection |
| Funding Rate ([[crypto]]) | 8-hour | Carry component for crypto market making |

## Example Trade

**Setup:** Algorithmic market making on ETH/USDT perpetual futures on a crypto exchange. The current order book shows a bid-ask spread of $3,500.00 x $3,500.80. Your target capture is $0.50 per round trip.

**Entry:** The algorithm places a bid at $3,500.15 and an ask at $3,500.65. The bid gets filled at $3,500.15 (you are now long 10 ETH).

**Management:** Inventory is now +10 ETH. The algorithm skews quotes: new bid at $3,500.05 (lower, to discourage more buying) and ask at $3,500.55 (lower, to encourage selling). Simultaneously, a small hedge is placed by shorting 3 ETH on a correlated venue to reduce directional exposure.

**Exit:** The ask at $3,500.55 gets filled 12 seconds later. Round trip complete: bought at $3,500.15, sold at $3,500.55. Gross profit = $0.40 x 10 ETH = $4.00. The hedge is unwound. Over 1,000 such round trips per day, gross profit accumulates to $4,000 before fees and infrastructure costs.

## Performance Characteristics

- **Win Rate:** 60-75% of round trips are profitable (spread captured); losses come from adverse selection and inventory risk
- **Profit Per Trade:** Tiny -- fractions of a basis point per round trip, but multiplied by thousands of daily trades
- **Trades Per Day:** 500-50,000+ depending on instrument and strategy aggressiveness
- **Best Conditions:** Calm, liquid markets with tight spreads and high volume -- maximum flow with minimum adverse selection
- **Worst Conditions:** Flash crashes, extreme volatility events, one-directional moves where inventory accumulates rapidly on the wrong side
- **Key Metric:** Sharpe ratios for professional market makers often exceed 3.0+ on a daily basis (Source: [[book-high-frequency-trading-aldridge]])

## Advantages

- Profit is generated from spread capture, not directional prediction -- edge does not require forecasting market direction
- Extremely high Sharpe ratio when executed properly with adequate infrastructure
- Market making profits in both rising and falling markets (direction-neutral)
- Provides a valuable service ([[liquidity]] provision) and often receives exchange fee rebates (maker rebates)
- Scales well: firms like Citadel and Wintermute make billions annually from this approach
- Can be combined with [[statistical-arbitrage]] for additional alpha

## Disadvantages

- **Requires algorithmic infrastructure** -- manual market making is essentially impossible in modern electronic markets (Source: [[book-flash-boys]])
- Adverse selection is the existential risk: informed traders systematically pick off your quotes
- Inventory risk can cause catastrophic losses during flash crashes or extreme moves (e.g., the crypto LUNA collapse)
- Infrastructure costs are significant: colocated servers, low-latency data feeds, exchange memberships
- Highly competitive: retail traders cannot compete with Citadel's microsecond latency and billions in capital
- Regulatory complexity: market makers in stocks face obligations (continuous quoting requirements) and scrutiny
- Exchange fee structures can make or break profitability -- even small fee increases eliminate the edge
- Not a viable strategy for individual retail traders; included here for educational understanding of market structure

## Sources

- [[book-trading-and-exchanges]] — the definitive academic treatment of market making, including adverse selection models, inventory management, and the economics of spread capture
- [[book-flash-boys]] — narrative account of how electronic market making evolved and the infrastructure arms race between market-making firms
- [[book-algorithmic-and-high-frequency-trading]] — Cartea et al. (2015) provide the mathematical framework for optimal market making, including the Avellaneda-Stoikov model, inventory risk management, and optimal quoting under adverse selection
- [[book-high-frequency-trading-aldridge]] — Aldridge (2013) covers HFT market making infrastructure, latency considerations, and empirical analysis of market-making profitability across venues
