---
title: "Regulation NMS"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [market-microstructure, regulation]
aliases: ["Reg NMS", "Regulation NMS", "Reg Nms", "National Market System", "NBBO"]
related: ["[[best-execution]]", "[[execution-quality]]", "[[payment-for-order-flow]]", "[[dark-pools]]", "[[smart-order-routing]]", "[[bid-ask-spread]]", "[[high-frequency-trading]]"]
domain: [market-microstructure]
prerequisites: ["[[order-book]]", "[[bid-ask-spread]]"]
difficulty: intermediate
---

# Regulation NMS

**Regulation NMS (National Market System)** is the SEC's foundational framework governing the structure of US equity markets. Adopted on 9 June 2005 and effective 29 August 2005, it ties together the dozens of competing exchanges and trading venues into a single "national market system" by requiring that orders receive the best available displayed price, that quotes be fairly accessible, and that consolidated price data be published. It is the single most important rulebook shaping how US stocks trade.

## Overview

Before Reg NMS, fragmentation across exchanges meant an order could be executed on one venue at a worse price than was simultaneously displayed on another. Reg NMS was designed to enforce price priority across venues and to modernise market-data dissemination. It is the regulatory backbone behind the concept of [[best-execution]] and the consolidated **National Best Bid and Offer (NBBO)** — the highest displayed bid and lowest displayed offer across all protected venues.

## Core Rules

- **Rule 611 — Order Protection (Trade-Through) Rule**: trading centres must not execute trades at prices inferior to a *protected quotation* displayed by another venue. A quote is "protected" only if it is immediately and automatically accessible. This is the rule that enforces price priority across fragmented venues.
- **Rule 610 — Access Rule**: requires fair, non-discriminatory access to quotations and caps the access fees venues can charge (historically $0.003 per share). It also bars locking or crossing of automated quotations.
- **Rule 612 — Sub-Penny Rule**: prohibits displaying, ranking, or accepting orders in increments smaller than $0.01, except for stocks priced below $1.00. This standardised the minimum tick.
- **Market Data Rules (Rules 601/603)**: govern the consolidation, distribution, and display of quote and last-sale data, and the joint industry plans (SIPs) that allocate market-data revenue.

## 2024 Amendments

In September 2024 the SEC adopted the most significant overhaul of Reg NMS since 2005, addressing complaints that the framework had not kept pace with sub-penny price competition and odd-lot trading:

- **Variable tick sizes** — introduced sub-penny quoting increments ($0.005) for the most liquid, tick-constrained stocks, narrowing the gap between displayed and achievable prices.
- **Lower access-fee caps** — reduced the maximum exchange access fee (toward $0.001 per share) to better align displayed and net prices.
- **Round-lot redefinition and odd-lot transparency** — redefined "round lot" by price tier and added the best odd-lot quote to consolidated market data, improving visibility for retail-sized orders.

(Source: Perplexity sonar synthesis of SEC release 34-51808 and the September 2024 amendments — to be replaced with a stored source summary on ingestion.)

## Trading Relevance

Reg NMS shapes everything about how US equity orders are routed and filled. The Order Protection Rule is why brokers must use [[smart-order-routing]] to scan all venues for the NBBO. The access-fee cap created the **maker-taker** rebate model that incentivises [[high-frequency-trading|HFT]] liquidity provision. Critics argue the trade-through rule entrenched fragmentation and fuelled the growth of [[dark-pools]] and [[payment-for-order-flow]], since venues compete on rebates and routing rather than pure price. For any US equity trader, understanding the NBBO and protected quotes is essential to interpreting fills and execution-quality (Rule 605/606) reports.

## Related

- [[best-execution]] — Reg NMS underpins the US best-execution obligation
- [[execution-quality]] — measured against the NBBO that Reg NMS defines
- [[smart-order-routing]] — required to comply with the Order Protection Rule
- [[payment-for-order-flow]] — a controversial offshoot of the post-Reg NMS structure
- [[dark-pools]] — off-exchange venues operating within the Reg NMS framework
- [[high-frequency-trading]] — shaped by the maker-taker fee model

## Sources

- SEC, *Regulation NMS Adopting Release* (Release No. 34-51808, 9 June 2005) — Rules 610, 611, 612
- SEC, market-structure amendments adopting release (September 2024) — tick sizes, access-fee caps, round lots
- FINRA Rule 5310 (Best Execution) and Rules 605/606 disclosure requirements
