---
title: "Latency"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [market-microstructure, high-frequency-trading, slippage, liquidity]
aliases: ["Latency", "Trading Latency", "Network Latency", "Tick-to-Trade Latency"]
related: ["[[high-frequency-trading]]", "[[latency-arbitrage]]", "[[co-location]]", "[[order-book]]", "[[slippage]]", "[[queue-position]]", "[[liquidity-provider]]", "[[market-microstructure-overview]]"]
domain: [market-microstructure]
prerequisites: ["[[order-book]]", "[[high-frequency-trading]]"]
difficulty: intermediate
---

**Latency** is the time delay between an event occurring and a system responding to it. In trading, it most often means the elapsed time from when market data is generated (a quote update, a trade print) to when a participant's resulting order reaches the exchange's matching engine — the "tick-to-trade" path. In modern electronic markets, latency is measured in microseconds (and increasingly nanoseconds), and small differences determine who wins [[queue-position|queue priority]], who captures fleeting arbitrage, and who is left with stale quotes that get [[adverse-selection|picked off]].

## Overview

Latency is the sum of several stages along the data-and-order round trip:

1. **Market-data latency** — time for the exchange to publish an event and for the participant to receive and decode it (feed-handler latency).
2. **Decision latency** — time for the trading strategy to process the event and decide on an action (strategy compute).
3. **Order-entry latency** — time for the order message to travel from the participant's server to the matching engine and be acknowledged (network + gateway latency).
4. **Exchange internal latency** — time inside the matching engine to process the order and update the book.

The end-to-end figure that matters for a market maker or arbitrageur is **tick-to-trade**: from receiving a market-data tick to having the responding order in the matching engine. State-of-the-art firms achieve single-digit microseconds or below for this path.

## How Latency Is Minimized

The pursuit of low latency drives a multi-billion-dollar infrastructure arms race:

- **[[co-location]]** — placing trading servers in the same data center as the exchange matching engine, eliminating wide-area network distance. Exchanges sell rack space and standardized cable lengths so every co-located participant has equal in-building distance.
- **Faster physical media** — microwave and millimeter-wave radio links travel through air at ~1.5x the speed of light in fiber. The famous Chicago–New Jersey microwave networks shave milliseconds off the futures–equities arbitrage path versus fiber.
- **Hardware acceleration** — FPGAs (field-programmable gate arrays) and custom ASICs process market data and generate orders in hardware, bypassing the operating system. Kernel-bypass networking (Solarflare/OpenOnload, DPDK) avoids the OS network stack entirely.
- **Code and data-structure optimization** — lock-free data structures, cache-aware layouts, and busy-polling rather than interrupts.
- **Proximity to the data source** — for cross-venue strategies, locating between two exchanges to minimize the worst of two paths.

## Where Latency Creates or Destroys Edge

- **[[latency-arbitrage]]** — exploiting the brief window in which one venue's price has moved but another's quote has not yet updated. The fastest participant trades against the stale quote before it is cancelled. This is the purest latency edge.
- **[[queue-position]]** — when the inside price changes, the first order to post at the new level is first in the time-priority queue and fills first. Winning that race depends on latency. A position at the front of the queue earns the [[maker-taker-fees|rebate]] and faces less [[adverse-selection]].
- **Quote staleness / picking off** — a slow [[liquidity-provider|market maker]] whose quotes lag the true price is the *victim*: faster traders hit its stale bid or lift its stale offer before it can cancel. Latency is therefore both an offensive weapon and a defensive necessity.
- **[[slippage]] from delay** — even for slower discretionary traders, the gap between decision and fill (including human reaction, broker routing, and network time) is a hidden latency cost that shows up as slippage versus the price seen on screen.

## Trading Relevance

For an HFT or systematic market-making firm, latency is the single most important infrastructure variable — it directly determines fill rates, adverse-selection exposure, and profitability of speed-sensitive strategies. For a discretionary or swing trader, raw microsecond latency is irrelevant, but the *concept* matters: it explains why retail orders rarely capture fleeting price dislocations, why "the price moved before my order filled" is structural rather than conspiratorial, and why Reg NMS order-protection and the SEC's scrutiny of speed advantages shape execution quality. Understanding latency also clarifies the limits of strategies that assume instantaneous, frictionless execution — backtests that ignore latency systematically overstate returns for any short-horizon edge.

## Related

- [[high-frequency-trading]] — the trading style built around latency advantage
- [[latency-arbitrage]] — the canonical latency-driven strategy
- [[co-location]] — the primary latency-reduction technique
- [[queue-position]] — the asset latency helps win in time-priority books
- [[liquidity-provider]] — agents who must minimize latency to avoid being picked off
- [[slippage]] — the cost slower participants pay from delay
- [[order-book]] — the data structure latency races to act on

## Sources

- Lewis, Michael. *Flash Boys: A Wall Street Revolt* (2014) — popular account of the latency arms race and microwave/co-location infrastructure.
- Aldridge, Irene. *High-Frequency Trading: A Practical Guide to Algorithmic Strategies and Trading Systems* (2nd ed., 2013) — technical treatment of latency components and minimization.
- Budish, Eric, Peter Cramton, and John Shim. "The High-Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response." *Quarterly Journal of Economics* 130(4), 2015 — economic analysis of the latency race and proposed reforms.
- Harris, Larry. *Trading and Exchanges: Market Microstructure for Practitioners* (2003) — foundational microstructure context for order timing and queue priority.
