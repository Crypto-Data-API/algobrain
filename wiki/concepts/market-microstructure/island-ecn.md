---
title: "Island ECN"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [market-microstructure, history, liquidity, order-types]
aliases: ["Island ECN", "Island", "INET", "Island Electronic Communication Network"]
related: ["[[electronic-communication-network]]", "[[order-book]]", "[[market-microstructure-overview]]", "[[high-frequency-trading]]", "[[reg-nms]]", "[[nasdaq]]", "[[liquidity-provider]]", "[[maker-taker-fees]]"]
domain: [market-microstructure]
prerequisites: ["[[order-book]]", "[[electronic-communication-network]]"]
difficulty: intermediate
---

**Island ECN** was a pioneering electronic communication network (ECN) launched in 1996 by Joshua Levine for the brokerage Datek. It was one of the first venues to display a fully electronic, anonymous, price-time-priority limit order book to the public, and it played a central role in destroying the wide, dealer-controlled spreads of the 1990s Nasdaq market. Island's technology lineage — through its merger into Instinet and rebranding as **INET** — became the core matching engine of the modern [[nasdaq|Nasdaq]] stock market.

## Overview

In the mid-1990s, Nasdaq was a quote-driven dealer market: market makers posted bids and offers, and retail orders were filled at those dealer prices. Academic work (Christie and Schultz, 1994) exposed market makers colluding to keep spreads artificially wide by avoiding odd-eighth quotes. Island, alongside other early ECNs (Instinet, Archipelago, BRUT), let traders post their own limit orders directly against each other, bypassing the dealer spread entirely. A customer could now *be* the bid or offer rather than crossing the dealer's spread.

Island's distinguishing features were radical transparency and speed:

- **Public, real-time order book.** Island broadcast its full depth-of-book for free, when most venues guarded order information. The "Island BookViewer" became iconic among day traders.
- **Anonymous price-time priority.** Orders matched strictly by best price, then arrival time, with no counterparty identity revealed — the template for nearly every modern matching engine.
- **Sub-second matching.** Island's matching engine, written largely by Levine in lean C code, executed in milliseconds at a time when competitors took seconds.
- **Maker-taker pricing.** Island helped popularize the [[maker-taker-fees|maker-taker]] rebate model: pay liquidity providers a rebate, charge liquidity takers a fee. This fee structure underpins much of modern [[high-frequency-trading]] and exchange economics.

## How It Worked

A trader sent a limit order to Island; the order rested in the central limit order book if it did not immediately cross an opposing order. Incoming marketable orders matched against the best-priced resting order, then the next, walking the book by price-time priority. Because Island disseminated its book publicly and matched continuously, it attracted the most price-sensitive, fastest participants — the precursors of today's electronic [[liquidity-provider|liquidity providers]] and proprietary trading firms.

Island operated in regulatory tension with Nasdaq. Under the SEC's 1997 Order Handling Rules, ECN quotes had to be reflected in the public Nasdaq montage, which forced dealer spreads to compress dramatically. Island's order flow grew until it was handling a large share of Nasdaq-listed volume.

## Legacy and Trading Relevance

- **Lineage to INET/Nasdaq.** Island merged with Instinet in 2002 to form INET. Nasdaq acquired INET in 2005, and the INET matching engine became Nasdaq's core trading platform — the same architecture still underpinning [[nasdaq|Nasdaq]] and licensed to dozens of exchanges worldwide.
- **Birthplace of HFT infrastructure.** Island's transparent, fast, fee-incentivized book created the environment in which automated market making and [[high-frequency-trading|HFT]] became viable. The traders who learned to read the Island BookViewer became the first generation of electronic market makers.
- **Microstructure template.** Anonymous central-limit-order-book matching with price-time priority and maker-taker fees — Island's design choices — are now the default microstructure of global equity, futures, and crypto markets.

For a trader, Island matters historically because it explains *why* modern markets look the way they do: tight spreads, a visible [[order-book]], rebate-driven liquidity, and an arms race in latency that culminated in [[reg-nms|Reg NMS]] and the present HFT-dominated structure.

## Related

- [[electronic-communication-network]] — the general venue category Island pioneered
- [[order-book]] — the central data structure Island made public
- [[maker-taker-fees]] — the rebate model Island helped popularize
- [[high-frequency-trading]] — the trading style Island's infrastructure enabled
- [[reg-nms]] — the 2005 regulation that codified the order-protection regime ECNs introduced
- [[nasdaq]] — the market that absorbed Island's matching engine via INET
- [[liquidity-provider]] — the electronic market makers Island attracted

## Sources

- Patterson, Scott. *Dark Pools: The Rise of the Machine Traders and the Rigging of the U.S. Stock Market* (2012) — detailed history of Island, Josh Levine, and the rise of electronic trading.
- Christie, William G., and Paul H. Schultz. "Why Do NASDAQ Market Makers Avoid Odd-Eighth Quotes?" *Journal of Finance* 49(5), 1994 — the study that exposed wide dealer spreads and motivated reform.
- SEC. *Order Execution Obligations* (Order Handling Rules), 1996-1997 — regulatory changes that integrated ECN quotes into the public market.
- Nasdaq / INET corporate history (Instinet-Island merger 2002; Nasdaq acquisition of INET, 2005).
