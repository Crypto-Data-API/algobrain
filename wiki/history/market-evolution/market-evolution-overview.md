---
title: "Market Evolution"
type: overview
created: 2026-04-06
updated: 2026-06-12
status: good
tags: [history, market-evolution, market-microstructure]
aliases: ["Market Evolution", "Evolution of Financial Markets", "History of Market Structure"]
related: ["[[champagne-fairs]]", "[[medieval-italian-banking]]", "[[medieval-bill-of-exchange-arbitrage]]", "[[high-frequency-trading]]", "[[automated-market-maker]]", "[[defi]]", "[[etf]]", "[[market-microstructure]]"]
---

# Market Evolution

How financial markets have evolved over time — from medieval fairs and open-outcry pits to electronic order matching, high-frequency trading, and on-chain decentralized exchanges. Understanding this arc helps a trader see *why* current market structure exists, where its fragilities lie, and where the next dislocation (and edge) is likely to appear.

The throughline is constant: each generation of infrastructure removes a friction (distance, time, intermediation cost, counterparty trust), which compresses spreads and expands access — and in doing so creates a new, faster failure mode. Cheaper, faster, more fragmented markets are not unambiguously "better"; they relocate risk rather than eliminate it. The [[flash-crash-2010|2010 flash crash]], the [[flash-crash-2015-etf|2015 ETF crash]], and [[volmageddon|Volmageddon]] are all symptoms of structures that worked beautifully until liquidity was tested.

## The Arc

### 1. Periodic fairs and bill-of-exchange finance (~1180–1600)

Long-distance European commerce was settled at recurring trade fairs. The [[champagne-fairs|Champagne Fairs]] (c. 1180–1320) and their successors at Lyon, Geneva and Bruges introduced a *settlement cycle* — a dedicated "payments" phase where bills of exchange came due — and a collectively negotiated cross-rate table (the *conto*). This is the direct ancestor of T+2 settlement, bilateral netting, and rate fixings. [[medieval-italian-banking|Italian banking houses]] (Bardi, Peruzzi, later the Medici) ran multi-branch networks that netted positions on internal books and shipped specie only when imbalances exceeded transport cost — the medieval analogue of [[gold-point-arbitrage|gold-point arbitrage]]. See [[medieval-bill-of-exchange-arbitrage]].

### 2. Permanent exchanges and open outcry (1600s–1990s)

Continuous trading at fixed venues (Amsterdam 1602, London, the NYSE under the 1792 Buttonwood Agreement) replaced periodic fairs. Price discovery happened in physical pits via open outcry, with human specialists and market makers holding affirmative obligations to quote. This structure was slow and high-cost but resilient: a designated specialist absorbed inventory in stress rather than withdrawing.

### 3. Electronic matching and decimalization (1990s–2000s)

Electronic order books (Nasdaq's evolution, ECNs, the NYSE hybrid) displaced the floor. **Decimalization** (US equities, 2001) cut the minimum tick from 1/16 of a dollar to one cent, collapsing spreads and the economics of traditional market-making — and opening the door for fast, automated liquidity providers to dominate.

### 4. High-frequency and algorithmic trading (2000s–present)

[[high-frequency-trading|HFT]] firms replaced obligated specialists as the marginal liquidity providers, competing on latency. Markets fragmented across dozens of venues and dark pools, stitched together by [[smart-order-routing|smart order routing]]. The key structural change: modern market makers have *no obligation to quote* and reduce risk by withdrawing — which is exactly what produced the [[flash-crash-2010|2010 flash crash]]. See [[market-microstructure]].

### 5. The ETF and passive revolution (1993–present)

Exchange-traded funds ([[etf]]), beginning with SPY in 1993, democratized diversified exposure and added a new liquidity layer dependent on an arbitrage mechanism rather than intrinsic depth. The [[flash-crash-2015-etf|August 2015 ETF flash crash]] exposed the catch: ETF liquidity is *borrowed* from the underlying, and breaks precisely when it is most needed.

### 6. DeFi and automated market makers (2017–present)

[[defi|Decentralized finance]] rebuilt trading, lending and derivatives on public blockchains. [[automated-market-maker|Automated market makers]] (Uniswap and successors) replaced the order book entirely with constant-function liquidity pools, and replaced trusted intermediaries with code. This removes counterparty and settlement risk in the traditional sense while introducing new ones: smart-contract exploits, MEV/front-running, and oracle manipulation. It is, in a sense, a return to the bill-of-exchange idea — value transfer without a central counterparty — implemented in software.

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/history/market-evolution"
WHERE type != "index" AND type != "overview"
SORT updated DESC
```

## Gaps to Fill

Forward links flagging pages this section should eventually contain:

- Open outcry → electronic trading transition (standalone page)
- Decimalization (2001) and its effect on spreads and market-making
- The rise of retail trading (discount brokers → zero-commission → meme era)
- Regulation evolution (Reg NMS, MiFID II, the consolidated audit trail)

## Related

- [[champagne-fairs]] · [[medieval-italian-banking]] · [[medieval-bill-of-exchange-arbitrage]] — the origins of settlement, netting and FX arbitrage
- [[high-frequency-trading]] · [[market-microstructure]] — modern electronic structure
- [[etf]] · [[flash-crash-2015-etf]] — the passive-product layer and its fragility
- [[defi]] · [[automated-market-maker]] — on-chain market structure
- [[flash-crash-2010]] · [[volmageddon]] — what happens when new structures are stress-tested

## Sources

- Peter Spufford, *Money and Its Use in Medieval Europe* (1986) — medieval fair and banking infrastructure.
- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* (2003) — the standard reference on the transition from floor to electronic markets.
- Michael Lewis, *Flash Boys* (2014) and Scott Patterson, *Dark Pools* (2012) — the HFT and fragmentation era.
- SEC Regulation NMS (2005) and decimalization order (2000-2001) — the US regulatory framework that reshaped equity market structure.
