---
title: "Algorithmic Trading"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [market-microstructure, quantitative, algorithmic]
aliases: ["algo trading", "Algorithmic", "Algorithmic Trading", "Algo Trading", "automated trading"]
domain: [market-microstructure, quantitative]
prerequisites: ["[[market-microstructure]]", "[[order-types-overview]]"]
difficulty: intermediate
related: ["[[high-frequency-trading]]", "[[execution-algorithms]]", "[[quantitative-trading]]", "[[jim-simons]]", "[[market-structure]]", "[[citadel]]", "[[arbitrage]]", "[[market-microstructure]]", "[[market-maker]]", "[[backtesting]]"]
---

# Algorithmic Trading

Algorithmic trading is the use of computer programs to execute trades based on predefined rules, mathematical models, or machine learning signals. It encompasses everything from simple execution algorithms that minimize market impact to [[high-frequency-trading|high-frequency trading (HFT)]] strategies that operate in microseconds. HFT is the fastest *subset* of algorithmic trading — not a synonym for it; most algorithmic trading (execution algos, statistical arbitrage, systematic trend-following) operates on horizons of seconds to weeks, far slower than HFT.

## Categories

- **Execution Algorithms**: TWAP (time-weighted average price), VWAP (volume-weighted average price), and iceberg orders designed to execute large orders with minimal market impact. Used by institutional traders to manage [[liquidity]] cost.
- **Statistical Arbitrage**: Identifying and exploiting short-term mispricings between related securities using quantitative models. Pioneered by firms like [[jim-simons]]' Renaissance Technologies.
- **Market Making**: Algorithms that continuously provide [[liquidity]] by quoting buy and sell prices, profiting from the [[bid-ask-spread]]. [[citadel]] Securities and Virtu Financial are dominant players.
- **High-Frequency Trading (HFT)**: Ultra-low-latency strategies that profit from speed advantages, often holding positions for milliseconds. HFT firms invest heavily in co-located servers, microwave towers, and custom hardware.
- **Momentum/Trend Following**: Algorithms that detect and follow price [[trend|trends]] using technical signals, often operating on intraday to multi-week timeframes.

## Infrastructure

Successful algorithmic trading requires robust infrastructure: reliable data feeds, low-latency execution, backtesting frameworks, risk controls, and monitoring systems. The barrier to entry has decreased with cloud computing and open-source tools, but competing with top firms like Renaissance and [[citadel]] at the highest levels remains extraordinarily capital- and talent-intensive.

## Trading Relevance

Algorithmic trading now accounts for an estimated 60-80% of U.S. equity volume. Any human trader is effectively competing against algorithms, making it essential to understand how they operate — their tendency to provide [[liquidity]] in calm markets and withdraw it during stress, their impact on [[market-structure]], and the patterns they create. For aspiring quant traders, understanding the fundamentals of strategy development, [[backtesting]], and execution is the entry point to this domain.

## Related

- [[flash-crashes]] — algorithmic feedback loops are the core amplifier of every flash crash
- [[flash-crash-2010]] — an institutional sell algorithm triggered the original crash
- [[volmageddon-2018]] — forced ETP rebalancing algorithms caused the VIX to spike
- [[high-frequency-trading]] — the fastest subset of algorithmic trading
- [[spoofing]] — algorithms used for illegal order manipulation
- [[market-manipulation]] — broader context for algorithmic abuse
- [[market-maker]] — algorithmic market making as primary liquidity source
- [[jim-simons]] — pioneer of quantitative algorithmic strategies
- [[citadel]] — dominant algorithmic market maker
- [[market-structure]] — how algos shape modern market structure

## Sources

- Aldridge, I. — *High-Frequency Trading: A Practical Guide to Algorithmic Strategies and Trading Systems*
- Cartea, Á., Jaimungal, S. & Penalva, J. — *Algorithmic and High-Frequency Trading* (Cambridge)
- Chan, E. — *Algorithmic Trading: Winning Strategies and Their Rationale*
- Johnson, B. — *Algorithmic Trading & DMA: An Introduction to Direct Access Trading Strategies* (execution algorithms: VWAP, TWAP, implementation shortfall)
