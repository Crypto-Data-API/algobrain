---
title: "High-Frequency Trading: A Practical Guide — Irene Aldridge (2013)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [education, book, hft, market-microstructure, low-latency, algorithmic]
related:
  - "[[high-frequency-trading]]"
  - "[[market-microstructure]]"
  - "[[low-latency-trading]]"
  - "[[co-location]]"
  - "[[market-making-strategy]]"
  - "[[order-flow-scalping]]"
  - "[[fix-protocol]]"
  - "[[flash-boys]]"
  - "[[statistical-arbitrage]]"
---

## Overview

**High-Frequency Trading: A Practical Guide to Algorithmic Strategies and Trading Systems** by Irene Aldridge bridges the gap between [[high-frequency-trading|HFT]] theory and practice. The first edition appeared in 2010 and a substantially expanded second edition in 2013. Where [[algorithmic-and-high-frequency-trading]] provides the stochastic-calculus foundations, Aldridge focuses on operational reality: infrastructure requirements, strategy taxonomy, risk-management systems, and the regulatory landscape. The book is accessible to readers without a PhD while still covering the strategies and technology stack that define modern HFT, and it is widely used as an entry text by engineers moving into trading.

Aldridge classifies HFT strategies into four categories: market making, [[statistical-arbitrage]], directional (momentum/event), and structural (latency arbitrage). For each, she explains the economic logic, data requirements, infrastructure needs, and risk profile. The book gives particular attention to latency measurement and reduction — breaking down the full stack from network transmission through kernel processing to application logic and exchange matching-engine response.

The practical emphasis extends to topics often skipped in academic treatments: FPGA-based hardware acceleration, [[co-location]] and cross-connect infrastructure, real-time risk monitoring, and the regulatory changes (Reg NMS, MiFID II) that reshaped the competitive landscape. Aldridge also engages the controversies around HFT — whether it improves or harms market quality, the arms-race dynamics, and the conditional withdrawal of liquidity during stress events (the 2010 Flash Crash being the canonical example).

## Key Facts

| Field | Detail |
|-------|--------|
| **Author** | Irene Aldridge — quantitative researcher, managing partner of an HFT software firm |
| **Editions** | 1st edition 2010; expanded 2nd edition 2013 (Wiley Trading) |
| **Strategy taxonomy** | Market making, [[statistical-arbitrage]], directional (momentum), structural (latency arb) |
| **Technical focus** | Latency stack, FPGAs, [[co-location]], tick data, real-time risk |
| **Regulatory coverage** | Reg NMS (US, 2007), MiFID/MiFID II (EU) |
| **Companion book** | [[algorithmic-and-high-frequency-trading]] (the mathematical counterpart) |
| **Journalistic counterpoint** | [[flash-boys]] (Michael Lewis, 2014) |
| **Audience** | Tech-oriented traders, trading-systems engineers, PMs evaluating HFT |
| **Difficulty** | Intermediate; light on heavy math, heavy on systems and operations |

## Core Thesis

HFT is an industrial, infrastructure-bound business as much as a quantitative one. The edge does not come from a single clever signal but from a tightly engineered stack — co-located servers, optimized networks, FPGA acceleration, tick-level data, and real-time risk controls — wrapped around a small number of repeatable strategy archetypes. Profit per trade is tiny; the statistical edge compounds across enormous volume and very high win rates. Whoever measures and minimizes [[low-latency-trading|latency]] across every layer, and survives the regulatory and risk constraints, wins.

## Structure and Section Themes

| Section | Theme |
|---------|-------|
| **HFT landscape & evolution** | History, players, and how Reg NMS / fragmentation created the modern HFT ecosystem |
| **Strategy taxonomy** | The four categories — market making, stat arb, directional, structural — with economics and risk profiles |
| **Market microstructure & data** | Order-book dynamics, tick data, and the patterns visible only at high frequency |
| **The latency stack** | Network, kernel, application, and matching-engine components; how to measure and cut each |
| **Infrastructure & hardware** | [[co-location]], cross-connects, proximity hosting, FPGA acceleration |
| **Risk management & monitoring** | Real-time position limits, automatic kill switches, circuit breakers |
| **Regulation & market quality** | Reg NMS, MiFID II, and the liquidity-provision debate |

## Key Concepts and Takeaways

| Concept | What it means |
|---------|---------------|
| **Four strategy categories** | Market making, [[statistical-arbitrage]], directional (momentum), structural (latency arb) — each with distinct infrastructure and risk requirements |
| **Latency must be measured end-to-end** | Network, kernel, application, and matching-engine components all add to total round-trip time |
| **FPGAs beat software** | Moving strategy logic from CPU to programmable hardware removes OS overhead and shaves critical microseconds |
| **Tick data reveals hidden patterns** | Order-book dynamics, trade clustering, and quote stuffing are visible only at tick resolution — the heart of [[market-microstructure]] |
| **Market making narrows spreads — conditionally** | HFT tightens spreads in normal conditions but may withdraw liquidity in stress; provision is conditional, not guaranteed |
| **The arms race keeps escalating** | From milliseconds (~2005) to microseconds (~2010) to nanoseconds (2015+), each gain costing exponentially more |
| **Regulation reshaped competition** | Reg NMS fragmented US equities across venues, enabling latency arbitrage; MiFID II imposed new obligations on EU HFT firms |
| **Real-time risk is non-negotiable** | A rogue algorithm can lose millions in seconds; live monitoring and automatic circuit breakers are mandatory |
| **High win rate, tiny edge per trade** | Win rates exceed 50% with minuscule average profit per trade; the edge is statistical, realized over volume |
| **Infrastructure is the moat** | [[co-location]], cross-connects, and proximity hosting are foundational — without them, competing is impossible |

## Criticisms and Limitations

- **Author conflict of interest.** Aldridge runs an HFT software/consulting firm, and the book reads at times as broadly favorable to the industry; the market-quality discussion is less critical than the [[flash-boys]] / academic skeptic camp.
- **Ages quickly.** Even the 2013 edition predates major developments — ML/deep learning in HFT, crypto market making, IEX-style speed bumps, and the latest exchange technology — so the latency-arms-race specifics are dated.
- **Breadth over depth.** As a practical survey it covers many topics shallowly; readers wanting the mathematics of optimal market making or execution must turn to [[algorithmic-and-high-frequency-trading]].
- **Some empirical claims questioned.** Certain profitability and market-quality figures in early editions drew academic pushback for sourcing and methodology.
- **Light on real implementation code.** Despite the "practical" label, production-grade systems detail (exact network tuning, kernel bypass, FPGA pipelines) is sketched rather than shipped.

## Who Should Read This

Technology-oriented traders who want to understand HFT infrastructure and strategy types; software engineers moving into trading-systems development; anyone who has read [[flash-boys]] and wants the practitioner's perspective rather than the journalistic one; and portfolio managers evaluating HFT-fund strategies. It pairs naturally with [[algorithmic-and-high-frequency-trading]] for the math and with [[statistical-arbitrage-pole]] for the stat-arb leg of the taxonomy.

## How It Applies to AI Trading

Aldridge's strategy taxonomy (market making, stat arb, directional, structural) is a useful frame for categorizing [[machine-learning]] trading strategies by economic logic and infrastructure needs. The latency-stack breakdown is directly relevant to deploying ML inference in low-latency environments — model-serving time becomes another latency component. FPGA deployment of ML models (quantized neural networks on programmable hardware) extends Aldridge's FPGA discussion to modern AI trading. And the risk-management principles — real-time monitoring, automatic kill switches, position limits — are even more critical for AI systems, where autonomous decision-making can amplify errors at machine speed.

## Rating

**7/10** — The best practical introduction to HFT available in book form. Strong on infrastructure, strategy taxonomy, and operational reality. The 2nd edition (2013) is more current but still misses recent developments (ML in HFT, crypto market making, speed bumps). A good complement to the more mathematical [[algorithmic-and-high-frequency-trading]].

## Related

- [[high-frequency-trading]] — The trading style this book documents
- [[market-microstructure]] — The order-book mechanics HFT exploits
- [[low-latency-trading]] — Core infrastructure and latency optimization
- [[co-location]] — Physical infrastructure for HFT
- [[market-making-strategy]] — The primary HFT strategy type
- [[statistical-arbitrage]] — A second pillar of Aldridge's taxonomy
- [[order-flow-scalping]] — Order-flow analysis in an HFT context
- [[fix-protocol]] — Trading-protocol infrastructure
- [[flash-boys]] — The journalistic counterpoint to this practitioner view
- [[algorithmic-and-high-frequency-trading]] — The mathematical companion book

## Sources

General market knowledge; no specific wiki source ingested yet.
