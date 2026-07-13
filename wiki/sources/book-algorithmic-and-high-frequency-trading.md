---
title: "Algorithmic and High-Frequency Trading — Cartea, Jaimungal, Penalva (2015)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, hft, market-microstructure, algorithmic, market-making]
aliases: ["Algorithmic and High-Frequency Trading"]
related: ["[[market-making-strategy]]", "[[low-latency-trading]]", "[[order-flow-scalping]]", "[[slippage]]", "[[implementation-shortfall]]", "[[algorithmic-and-high-frequency-trading]]"]
source_type: book
source_author: "Alvaro Cartea, Sebastian Jaimungal, Jose Penalva"
source_date: 2015
confidence: high
claims_count: 12
---

Cartea, Jaimungal, and Penalva's *Algorithmic and High-Frequency Trading* is the most mathematically rigorous academic treatment of HFT and algorithmic trading strategies. Using stochastic optimal control theory, the authors derive optimal strategies for market making (Avellaneda-Stoikov), optimal execution (Almgren-Chriss), and latency arbitrage. The book provides the theoretical foundations underlying modern electronic market making and institutional execution.

## Key Claims

1. [HIGH] Optimal market making can be formulated as a stochastic control problem maximizing expected utility of terminal wealth subject to inventory risk and adverse selection — the Avellaneda-Stoikov framework.

2. [HIGH] The Avellaneda-Stoikov model provides the mathematical foundation for optimal bid-ask quoting — the market maker widens spreads as inventory grows to manage risk, producing a closed-form solution for quote placement.

3. [HIGH] Optimal execution (Almgren-Chriss framework) minimizes the tradeoff between market impact (from trading too aggressively) and timing risk (from trading too passively) for large institutional orders.

4. [HIGH] Market makers manage adverse selection risk by adjusting quotes based on order flow toxicity — the VPIN (Volume-Synchronized Probability of Informed Trading) metric quantifies this risk in real time.

5. [HIGH] The Order Flow Imbalance (OFI) is a powerful predictor of short-term price changes — it measures the net aggressive order flow pressure at the top of the [[order-book]].

6. [HIGH] Latency [[arbitrage]] profits are a function of speed advantage and price correlation across venues — as the speed differential shrinks, latency arbitrage profits converge to zero.

7. [HIGH] Queue position in the limit order book determines fill probability and is a key strategic asset for [[market-making-strategy]] — earlier queue position provides higher fill rates on favorable orders.

8. [HIGH] High-frequency strategies face diminishing returns as competition drives latency advantages toward zero — the arms race has moved from milliseconds to microseconds to nanoseconds.

9. [HIGH] The maker-taker fee model creates incentives that shape order flow and market quality — rebates for liquidity provision and fees for liquidity taking influence the economics of [[market-making-strategy]].

10. [HIGH] Spoofing detection uses statistical patterns in order placement and cancellation rates — abnormally high cancel-to-fill ratios and layering patterns indicate manipulative intent.

11. [HIGH] Optimal liquidation schedules (TWAP, VWAP, [[implementation-shortfall]]) minimize execution costs for large orders — the choice depends on the trader's risk aversion and urgency.

12. [HIGH] Microstructure noise (bid-ask bounce, discrete tick sizes) biases high-frequency [[volatility]] estimates upward — standard realized volatility estimators must be adjusted for these effects.

## Concepts Referenced

- [[market-making-strategy]]
- [[low-latency-trading]]
- [[order-flow-scalping]]
- [[slippage]]
- [[implementation-shortfall]]
- [[co-location]]
- [[order-book]]
- [[arbitrage]]
- [[volatility]]
- [[adverse-selection]]
- [[vpin]]

## Pages Backed

- [[market-making-strategy]] — Avellaneda-Stoikov optimal quoting framework, inventory management, adverse selection risk
- [[low-latency-trading]] — latency arbitrage mechanics, diminishing returns from speed competition
- [[order-flow-scalping]] — OFI as short-term price predictor, VPIN for toxicity measurement
- [[slippage]] — Almgren-Chriss market impact model, execution cost minimization
- [[implementation-shortfall]] — optimal execution benchmarks (TWAP, VWAP, IS)
- [[co-location]] — infrastructure requirements for competitive HFT
- [[algorithmic-and-high-frequency-trading]] — primary source for education/book page
