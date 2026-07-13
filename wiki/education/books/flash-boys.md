---
title: "Flash Boys — Michael Lewis (2014)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [education, book, hft, market-microstructure, history]
aliases: ["Flash Boys", "Flash Boys: A Wall Street Revolt"]
related:
  - "[[high-frequency-trading]]"
  - "[[low-latency-trading]]"
  - "[[co-location]]"
  - "[[front-running]]"
  - "[[market-making-strategy]]"
  - "[[dark-pool-trading]]"
  - "[[market-microstructure]]"
  - "[[trading-and-exchanges]]"
---

**Flash Boys: A Wall Street Revolt** by Michael Lewis (2014) is a narrative investigation into [[high-frequency-trading]] and modern U.S. equity market structure. It follows Brad Katsuyama, a trader at RBC Capital Markets, who discovers that his orders are filled at worse prices the instant he tries to execute across multiple exchanges — and slowly uncovers a system in which the fastest firms exploit speed and information advantages to trade ahead of slower participants. Katsuyama goes on to found IEX, an exchange engineered with a 350-microsecond "speed bump" to neutralize the latency edge.

## Key Facts

| Field | Detail |
|-------|--------|
| **Author** | Michael Lewis (also *Liar's Poker*, *The Big Short*, *Moneyball*) |
| **Published** | March 31, 2014 (W. W. Norton) |
| **Genre** | Narrative non-fiction / financial journalism |
| **Central figure** | Brad Katsuyama (founder of IEX) |
| **Key venue** | IEX — the "Investors Exchange," with a 350-microsecond speed bump |
| **Key technology** | Spread Networks' Chicago–NJ fiber line; microwave towers; [[co-location]] |
| **Era covered** | Roughly 2007–2014, post-Reg NMS fragmentation |
| **Aftermath** | Catalyzed a public HFT debate; a 60 Minutes segment; SEC and NY AG scrutiny |

## Core Thesis

Lewis argues that fragmentation of U.S. equity trading across dozens of public exchanges and private [[dark-pool-trading|dark pools]] — accelerated by Regulation NMS (2005/2007) — created structural opportunities for the fastest traders to extract value from everyone else. The book's central, contested claim is that the stock market is "rigged" in favor of HFT intermediaries who profit from speed rather than from price discovery, and that this can be fixed by redesigning market structure rather than by adding regulation.

## Chapter / Section Themes

- **Hidden in plain sight.** Spread Networks builds an $300M+ ultra-straight fiber route from Chicago to New Jersey to shave milliseconds off the Chicago–NY round trip.
- **Brad's problem.** Katsuyama at RBC notices that visible liquidity vanishes the moment he routes a large order — his fills move against him.
- **Ronan's problem.** Telecom specialist Ronan Ryan explains the physical, latency-driven nature of the advantage ([[co-location]], cross-connects, microwave).
- **Tracking the predators.** The mechanics of [[front-running|latency/electronic front-running]]: detect a large order hitting one exchange, race to the others, and trade ahead.
- **Putting a face on HFT.** Sergey Aleynikov, the Goldman Sachs programmer prosecuted over source code, illustrates how opaque and high-stakes the arms race had become.
- **How to take billions from Wall Street.** The economics of [[dark-pool-trading|dark pools]], maker-taker rebates, and order-type gaming.
- **An army of one / the spider and the fly.** Katsuyama builds IEX and Thor (an order router that synchronizes arrival times) and recruits allies to launch a fairer exchange.

## Key Concepts / Takeaways

| Concept | Takeaway |
|---------|----------|
| **Latency arbitrage** | Speed differences across fragmented venues are themselves an exploitable edge (see [[low-latency-trading]]). |
| **Electronic front-running** | Detecting a large order on one venue and racing to others to trade ahead — technically legal, ethically contested ([[front-running]]). |
| **Co-location** | Placing servers next to the matching engine yields measurable, monetizable microsecond advantages ([[co-location]]). |
| **Speed bump (IEX)** | A deliberate 350µs delay (coiled fiber) that neutralizes the latency edge for predatory strategies. |
| **Dark pools** | Off-exchange venues marketed as protective but sometimes opened to the very HFT flow they claimed to shield ([[dark-pool-trading]]). |
| **Maker-taker / rebates** | Exchange fee structures incentivize order-type gaming and venue routing decisions. |
| **Market fragmentation** | Reg NMS split trading across many venues, creating the cross-venue races the book documents. |
| **Order-type proliferation** | Exotic order types created interactions that advantaged the fastest, most knowledgeable participants. |

## Criticisms / Limitations

- **One-sided portrayal.** Many practitioners and academics argue HFT also *narrowed spreads* and *added liquidity*; Lewis underweights these benefits. Some HFT is benign market making (see [[market-making-strategy]]).
- **"Rigged" overstates it.** Critics (and even some sympathetic reviewers) say the headline claim conflates legal speed advantages with illegal manipulation. Cliff Asness and others published rebuttals.
- **Retail impact is small.** The harm described falls mostly on large institutional orders; for small retail orders, payment-for-order-flow and price improvement complicate the picture.
- **Hero narrative.** The book frames Katsuyama/IEX as unambiguous good guys, glossing over IEX's own commercial incentives.
- **Snapshot in time.** Written in 2014; tick-size pilots, IEX's exchange approval (2016), and later rule changes have since shifted the landscape.

## Who Should Read This

Anyone building trading systems who needs to understand what happens between placing an order and getting a fill. Retail traders who want to understand why execution can be worse than expected. Anyone curious about the infrastructure and microstructure layer of modern markets. Read it for the accessible narrative, then read [[trading-and-exchanges]] for the rigorous treatment.

## How It Applies to AI Trading

Flash Boys is directly relevant to execution algorithms, [[market-making-strategy]], and [[low-latency-trading]]. The structural issues Lewis describes — latency advantages, smart order routing, information leakage in [[dark-pool-trading]], and exchange fee structures — determine the real-world cost of implementing any strategy. A brilliant alpha signal is worthless if your execution is consistently anticipated. Even if you are not building HFT systems, the concepts explain *why your fills look the way they do* and how to design execution logic (arrival-time synchronization, venue selection, passive vs. aggressive posting) that protects your alpha. These are the practical, cost-side counterparts to the [[market-microstructure]] theory in [[trading-and-exchanges]].

## Rating

**8/10** — Engaging narrative that makes complex market structure accessible. Somewhat one-sided in its portrayal of HFT, but the structural insights are essential knowledge. Read it for the market microstructure education, not as the final word on HFT.

## Related

- [[high-frequency-trading]] — The practice at the center of the book
- [[low-latency-trading]] — The technology arms race Lewis describes
- [[co-location]] — Core infrastructure advantage in HFT
- [[front-running]] — The electronic/latency form Lewis documents
- [[market-making-strategy]] — How HFT firms profit from providing liquidity
- [[dark-pool-trading]] — Alternative venues and their hidden dynamics
- [[market-microstructure]] — The field these issues belong to
- [[trading-and-exchanges]] — Academic deep dive into the concepts Lewis popularizes

## Sources

General market knowledge; no specific wiki source ingested yet.
