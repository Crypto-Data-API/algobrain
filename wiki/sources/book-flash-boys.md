---
title: "Flash Boys — Michael Lewis (2014)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, hft, market-microstructure, co-location]
aliases: ["Flash Boys", "Flash Boys Lewis"]
related: ["[[low-latency-trading]]", "[[co-location]]", "[[market-making-strategy]]", "[[flash-boys]]"]
source_type: book
source_author: "Michael Lewis"
source_date: 2014
confidence: high
claims_count: 10
---

Michael Lewis's investigation into [[low-latency-trading|high-frequency trading (HFT)]] and the structural advantages built into US equity markets that benefit the fastest participants at the expense of ordinary investors. The book follows Brad Katsuyama of RBC Capital Markets as he discovers that HFT firms are systematically front-running institutional orders by exploiting speed advantages across fragmented exchanges. Katsuyama's response — founding IEX, an exchange with a built-in speed bump — became a focal point for the debate over market fairness. The book brought [[market-microstructure]] concepts (co-location, latency arbitrage, dark pools) to mainstream public awareness.

## Key Claims

1. [HIGH] **Speed is the ultimate edge in modern electronic markets**: In the post-decimalization, fragmented US equity market, the ability to process and act on information microseconds faster than competitors creates a structural, repeatable edge. HFT firms generate consistent profits not through superior analysis but through superior speed. (Source: Michael Lewis)

2. [HIGH] **Co-location provides measurable, exploitable advantage**: By placing servers physically adjacent to exchange matching engines ([[co-location]]), HFT firms reduce round-trip latency to microseconds. This speed advantage allows them to see and react to orders before slower participants, creating a form of informational advantage that is technically legal but structurally unfair. (Source: Michael Lewis)

3. [HIGH] **Dark pools became HFT hunting grounds**: Dark pools were originally created to allow institutional investors to trade large blocks without market impact. In practice, many dark pools invited HFT firms in as liquidity providers, who then used their speed advantage to detect and trade against the very institutional orders the dark pools were designed to protect. (Source: Michael Lewis)

4. [HIGH] **Structural front-running is technically legal**: HFT firms detect large orders on one exchange (e.g., BATS) and race to other exchanges (e.g., NYSE, Nasdaq) to buy or sell ahead of the arriving order — profiting from the price impact they know is coming. This is not illegal front-running (which requires a fiduciary breach) but achieves a similar economic result through speed. (Source: Michael Lewis)

5. [HIGH] **Market fragmentation creates arbitrage only the fastest can exploit**: The proliferation of 13+ US stock exchanges and dozens of dark pools means that a single stock's price can momentarily differ across venues. Only participants with sub-millisecond connectivity to all venues can consistently capture these discrepancies, creating a speed tax on slower participants. (Source: Michael Lewis)

6. [HIGH] **IEX's 350-microsecond speed bump was designed to neutralize latency advantages**: Brad Katsuyama and his team built IEX with a physical coil of fiber optic cable that delays all incoming orders by 350 microseconds — long enough to prevent HFT speed advantages from functioning, short enough to be imperceptible to human traders. This was a structural solution to a structural problem. (Source: Michael Lewis)

7. [HIGH] **The 2010 Flash Crash exposed the fragility of algorithmically-dominated markets**: On May 6, 2010, the Dow Jones fell nearly 1,000 points in minutes before recovering, wiping out and restoring approximately $1 trillion in market value. The crash demonstrated that markets dominated by algorithmic participants could experience extreme, rapid dislocations when liquidity evaporated simultaneously across automated systems. (Source: Michael Lewis)

8. [HIGH] **Firms spend hundreds of millions on infrastructure for microsecond advantages**: Spread Networks spent $300 million building a fiber optic line from Chicago to New Jersey, shaving 3 milliseconds off communication time. This single project illustrates the scale of investment in latency reduction and the economic value of being faster than competitors, even by microseconds. (Source: Michael Lewis)

9. [HIGH] **Market complexity benefits intermediaries at the expense of end investors**: The proliferation of order types (over 100 on some exchanges), complex rebate structures, and fragmented execution venues creates opacity that sophisticated intermediaries exploit. Simplicity and transparency would benefit end investors but reduce the profit opportunities for HFT and exchanges. (Source: Michael Lewis)

10. [HIGH] **Smart order routing and execution quality directly impact strategy profitability**: How and where orders are routed — through which exchanges, dark pools, and in what sequence — materially affects the price a trader receives. Poor execution routing can cost institutional investors billions annually in adverse selection and information leakage, regardless of the quality of their investment decisions. (Source: Michael Lewis)

## Concepts Referenced

- [[low-latency-trading]], [[co-location]], [[market-microstructure]]
- dark-pool-trading, [[market-making-strategy]]
- [[smart-order-routing]], [[execution-quality]]
- [[market-fragmentation]], [[latency-arbitrage]]
- [[flash-crash-2010]]

## Pages Backed

- [[low-latency-trading]] — comprehensive account of how speed became the dominant edge in equity markets
- [[co-location]] — detailed description of co-location economics and advantages
- [[market-making-strategy]] — HFT market making as a speed-dependent business model
- [[market-microstructure]] — brought microstructure concepts to mainstream awareness
