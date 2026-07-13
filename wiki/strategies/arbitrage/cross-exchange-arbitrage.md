---
title: "Cross-Exchange Arbitrage"
type: strategy
created: 2026-04-06
updated: 2026-04-07
status: good
tags: [arbitrage, crypto, cross-exchange, latency, market-neutral, high-frequency, dex, cex]
aliases: ["Exchange Arb", "Spatial Arbitrage", "Inter-Exchange Arbitrage"]
strategy_type: algorithmic
timeframe: scalp|day
markets: [crypto]
complexity: advanced
backtest_status: untested
related: ["[[triangular-arbitrage]]", "[[funding-rate-arbitrage]]", "[[cash-and-carry]]", "[[mev-strategies]]", "[[order-book]]", "[[slippage]]", "[[book-statistical-arbitrage-pole]]"]
---

# Cross-Exchange Arbitrage

## Overview

Cross-exchange arbitrage exploits price differences for the same asset across different trading venues. In crypto markets, where hundreds of centralized exchanges ([[cex]]) and decentralized exchanges ([[dex]]) operate independently with fragmented [[liquidity]], the same token can momentarily trade at different prices. The arbitrageur buys on the exchange where the price is lower and simultaneously sells on the exchange where the price is higher, capturing the spread as profit.

This is conceptually the simplest form of arbitrage, but in practice it is fiercely competitive (Source: [[book-statistical-arbitrage-pole]]). Latency (speed) is the dominant factor -- whoever detects and executes the discrepancy first wins. Professional arbitrageurs use co-located servers, custom WebSocket connections, and sub-millisecond execution engines. Profit margins are razor-thin (often fractions of a basis point), requiring high volume and low fees to generate meaningful returns. The strategy serves a vital market function: it keeps prices synchronized across venues, improving overall [[market-efficiency]].

## Rules

### Entry
1. **Monitor prices across exchanges:** Maintain real-time price feeds (via WebSocket APIs) for the target asset on all relevant venues -- [[binance]], [[coinbase]], [[kraken]], [[okx]], [[bybit]], [[uniswap]], [[hyperliquid]], and others.
2. **Detect a spread:** When the bid on Exchange A exceeds the ask on Exchange B (after accounting for fees), an arbitrage opportunity exists.
3. **Execute simultaneously:** Buy on the cheaper exchange and sell on the more expensive exchange. Both orders should be submitted within milliseconds of each other.
4. **Account for all costs:** Transaction fees (maker/taker), withdrawal fees, network gas fees (for DEX/CEX arbs), and [[slippage]] must be subtracted from the gross spread. Only execute if the net spread is positive.

### Exit
1. **Immediate completion:** Unlike other strategies, there is no "holding period." The trade is complete once both legs fill. The profit is realized instantly.
2. **Rebalancing:** After multiple arbs in the same direction, capital accumulates on one exchange and depletes on another. Periodically transfer funds to rebalance.
3. **Inventory management:** If one leg fills but the other does not (leg risk), close the open position at market immediately to avoid directional exposure.

### Position Sizing
Size each arb based on the available liquidity at the quoted prices. Do not attempt to arb more size than the order book can support -- [[slippage]] will eliminate the profit. Typically, keep capital pre-positioned on 3-5 exchanges.

## Indicators Used
- **Bid-ask spreads** across exchanges -- the primary signal. Real-time monitoring is essential.
- [[order-book]] depth -- determines the maximum size that can be arbed without moving the price.
- **Fee schedules** -- maker/taker fees vary by exchange and VIP tier. Must be factored into every calculation.
- **Network congestion** -- for cross-chain or CEX-to-DEX arbs, blockchain gas fees and confirmation times affect profitability.
- [[slippage]] estimates -- model the expected fill price at various trade sizes based on order book depth.
- Latency metrics -- measure round-trip times to each exchange API; lower latency = higher fill probability.

## Example Trade
**Asset:** SOL trading at $178.50 ask on Coinbase, $179.10 bid on Binance.
1. **Gross spread:** $179.10 - $178.50 = $0.60 per SOL (0.34%).
2. **Fees:** Coinbase taker fee: 0.06% ($0.107). Binance taker fee: 0.04% ($0.072). Total fees: $0.179.
3. **Net spread:** $0.60 - $0.179 = **$0.421 per SOL (0.24%)**.
4. **Execute:** Buy 500 SOL on Coinbase at $178.50. Sell 500 SOL on Binance at $179.10.
5. **Gross profit:** 500 x $0.421 = **$210.50**.
6. **Duration:** 200 milliseconds from detection to execution. By the time slower participants detect the spread, it has already closed.
7. **Rebalancing:** Capital is now shifted -- more SOL on Coinbase, more USDT on Binance. Transfer as needed.

## Performance Characteristics
- **Win Rate:** 80-95% per attempted trade (when the spread is confirmed before execution). Failed fills reduce the effective win rate.
- **Profit Factor:** 2.0-5.0 on successful executions. The absolute profit per trade is small, but volume is high.
- **Best Market Conditions:** High [[volatility]], large price dislocations (news events, liquidation cascades), new token listings, low-liquidity pairs.
- **Worst Market Conditions:** Calm, efficient markets where spreads are consistently within fee thresholds. Increased competition from faster bots compresses margins to zero.

## Advantages
- **Market-neutral:** No directional exposure; profits are locked in at execution
- **Near-instant:** Trades complete in milliseconds to seconds; capital is not tied up
- **Exploits real inefficiency:** Price discrepancies across venues are a genuine, observable market imperfection
- **Improves markets:** Arbitrageurs perform a public good by synchronizing prices and improving [[market-efficiency]]
- **Scales with infrastructure:** Better technology (faster feeds, lower latency) directly translates to more captured opportunities

## Disadvantages
- **Speed arms race:** Dominated by professional firms with co-located servers and custom hardware; retail traders are at a severe disadvantage
- **Thin margins:** Profit per trade is often < 0.1%, requiring massive volume to generate meaningful returns
- **Leg risk:** If one side fills but the other does not, you are left with unhedged directional exposure
- **Capital fragmentation:** Must pre-position capital on multiple exchanges, increasing counterparty risk and reducing capital efficiency
- **Exchange risk:** Funds sitting on centralized exchanges are vulnerable to hacks, insolvency, or withdrawal freezes
- **Diminishing opportunities:** As crypto markets mature and more arbitrageurs enter, price discrepancies shrink and persist for shorter durations (Source: [[book-statistical-arbitrage-pole]])

## Sources

- [[book-statistical-arbitrage-pole]] — Pole (2007) covers the theoretical foundations of statistical arbitrage including cross-market price discrepancy exploitation, the competitive dynamics that compress arbitrage margins, and the statistical framework for identifying profitable opportunities

## See Also
- [[cross-chain-arbitrage]] -- the multi-blockchain variant; exploits price gaps across different chains via bridges
- [[triangular-arbitrage]] -- arbitraging price inconsistencies across three related pairs on a single exchange
- [[mev-strategies]] -- on-chain arbitrage in DeFi, exploiting DEX price discrepancies
- [[funding-rate-arbitrage]] -- a slower, carry-based crypto arbitrage strategy
- [[order-book]] -- understanding depth and liquidity is critical for execution
- [[slippage]] -- the primary cost that erodes cross-exchange arb profits
- [[market-efficiency]] -- the economic principle that arbitrage enforces
