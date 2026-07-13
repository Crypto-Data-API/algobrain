---
title: "Market Structure"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [market-microstructure, exchange, regulation, order-types]
aliases: ["market structure", "equity market structure", "trading mechanics"]
related: ["[[market-microstructure]]", "[[algorithmic-trading]]", "[[payment-for-order-flow]]", "[[sec]]", "[[robinhood]]", "[[citadel]]", "[[market-fragmentation]]", "[[best-execution]]", "[[smart-order-routing]]"]
domain: [market-microstructure]
prerequisites: ["[[market-microstructure]]", "[[order-types]]"]
difficulty: intermediate
---

# Market Structure

Market structure refers to the rules, systems, and institutions that govern how financial markets are organized, how orders are matched, and how prices are formed. Understanding market structure is essential for any trader who wants to know what actually happens between clicking "buy" and receiving a fill.

## Overview

Modern market structure encompasses exchanges (NYSE, nasdaq, CME), alternative trading systems (dark pools), [[market-maker|market makers]] ([[citadel]] Securities, Virtu), brokers ([[robinhood]], Interactive Brokers), clearinghouses (DTCC, OCC), and the regulatory framework ([[sec]], [[cftc]]) that governs them all.

## Key Components

- **Order Types and Matching**: Exchanges use price-time priority to match limit orders. Understanding order books, [[bid-ask-spread|bid-ask spreads]], and depth of book is foundational to execution.
- **Market Makers**: Firms that provide [[liquidity]] by continuously quoting buy and sell prices, profiting from the spread. In equities, [[citadel]] Securities and Virtu handle a majority of retail order flow.
- **Payment for Order Flow (PFOF)**: Brokers like [[robinhood]] route customer orders to market makers in exchange for payment. This model enables zero-commission trading but raises execution quality questions.
- **Dark Pools**: Private venues where institutional orders are matched without displaying quotes publicly, reducing market impact for large trades.
- **Settlement**: The process of transferring cash and securities after a trade. The U.S. moved from T+2 to T+1 settlement in May 2024, partly in response to the [[gamestop-short-squeeze]] liquidity crisis.

## Trading Relevance

Market structure directly affects execution quality, trading costs, and the strategies available to traders. Understanding how orders are routed, who is on the other side of your trade, and how [[liquidity]] behaves in different conditions is what separates informed traders from those operating blind. In the US, the regulatory backbone is **Regulation NMS** (2005), whose Order Protection Rule (the "trade-through" rule) requires orders to be routed to the venue showing the best displayed price (the National Best Bid and Offer, NBBO) — a major driver of both [[smart-order-routing]] and [[market-fragmentation]] across the dozens of US equity venues. The ongoing debates around PFOF reform, tick-size and access-fee changes, the proposed order-competition rule, and exchange competition make market structure a living, evolving topic that rewards continued study.

## Disambiguation

This page covers market structure in the **microstructure / regulatory** sense — exchanges, routing, settlement, and the rules of order matching. This is distinct from the technical-analysis usage where "market structure" means the sequence of swing highs and lows that defines a trend (higher-highs/higher-lows vs. a [[break-of-structure]]). For that price-action concept see [[break-of-structure]] and [[smart-money-concepts]].

## Sources

- US SEC, *Regulation National Market System (Reg NMS)*, Release No. 34-51808 (2005) — official rule text and adopting release.
- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* (Oxford University Press) — the standard practitioner reference on market structure.
- Maureen O'Hara, *Market Microstructure Theory* (Blackwell).
- SEC market-structure data and the Consolidated Audit Trail (CAT) documentation.
