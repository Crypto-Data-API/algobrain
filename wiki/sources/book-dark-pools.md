---
title: "Dark Pools — Scott Patterson (2012)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, hft, market-microstructure, electronic-trading, history]
aliases: ["Dark Pools", "Dark Pools Patterson"]
related: ["[[low-latency-trading]]", "[[co-location]]", "[[market-making-strategy]]", "[[flash-boys]]", "[[dark-pools]]"]
source_type: book
source_author: "Scott Patterson"
source_date: 2012
confidence: high
claims_count: 10
---

Scott Patterson's *Dark Pools* traces the transformation of US equity markets from human-operated floor exchanges to the fragmented, algorithmic, high-speed electronic system of today. The narrative centers on Josh Levine, the self-taught programmer who built Island ECN — the first fully electronic stock exchange — in 1996, and follows the chain of innovation, regulation, and disruption that made human floor trading obsolete. Patterson documents the rise of electronic communication networks (ECNs), the emergence of dark pools, the passage of Regulation NMS (2005), the ascendancy of high-frequency trading, and the systemic fragility revealed by the May 2010 flash crash. The book provides essential historical context for understanding why modern market structure is fragmented, fast, and complex.

## Key Claims

1. [HIGH] Josh Levine's Island ECN, launched in 1996, was the first fully electronic stock exchange. Built by a self-taught programmer frustrated with NASDAQ's dealer-dominated inefficiency, Island demonstrated that electronic matching was faster, cheaper, and more transparent than human market-making. It democratized market access by eliminating the informational advantages of established dealers. (Source: Scott Patterson)

2. [HIGH] Dark pools emerged because institutional investors (mutual funds, pension funds) needed to trade large blocks without revealing their orders to the public market. Exposing large orders to lit exchanges causes adverse price movement (market impact), so dark pools provided private venues for crossing large orders anonymously. However, many dark pools subsequently invited HFT firms as liquidity providers, compromising the original purpose. (Source: Scott Patterson)

3. [HIGH] The transition from floor-based to electronic trading happened rapidly in the 2000s. The NYSE, which had operated a human open-outcry floor for over two centuries, went predominantly electronic by 2006-2007. The speed of the transition surprised many industry participants who expected a gradual evolution. (Source: Scott Patterson)

4. [HIGH] Regulation NMS (2005) mandated best execution across all trading venues by establishing the "order protection rule" — brokers must route orders to the venue offering the National Best Bid and Offer (NBBO). This fragmented markets across dozens of exchanges and dark pools and created latency arbitrage opportunities exploitable only by the fastest participants, effectively creating the business model for modern HFT. (Source: Scott Patterson)

5. [HIGH] Electronic market makers (algorithmic liquidity providers) replaced human specialists and floor market makers. Algorithms now provide the majority of displayed liquidity in US equities. This produces tighter bid-ask spreads and faster execution in normal conditions but creates fragility when multiple algorithmic providers withdraw quotes simultaneously during market stress. (Source: Scott Patterson)

6. [HIGH] Payment for order flow (PFOF) creates structural conflicts of interest. Retail brokerages sell their customers' order flow to HFT firms and wholesale market makers (such as [[citadel|Citadel Securities]] and Virtu Financial). These firms pay for the flow because retail orders are predominantly uninformed and profitable to trade against — meaning retail investors may receive systematically worse execution than they would in a fully competitive environment. (Source: Scott Patterson)

7. [HIGH] Market fragmentation across 13+ lit exchanges and 40+ dark pools in US equities makes execution quality measurement extraordinarily complex. Determining whether an investor received the best possible execution across all available venues requires real-time data from every venue — a capability that only the most sophisticated participants possess. Complexity benefits intermediaries and disadvantages ordinary investors. (Source: Scott Patterson)

8. [HIGH] The flash crash of May 6, 2010 demonstrated the fragility of algorithmically-dominated markets. The Dow Jones Industrial Average fell nearly 1,000 points in minutes, with individual stocks trading at prices as low as $0.01 and as high as $100,000, before recovering within roughly 30 minutes. The crash occurred when algorithmic liquidity providers simultaneously withdrew their quotes during a period of elevated selling pressure, creating a liquidity vacuum. (Source: Scott Patterson)

9. [HIGH] Speed advantages in electronic markets create a structural two-tiered system. Firms with [[co-location|co-located]] servers, proprietary direct data feeds, and optimized execution code can see and react to market information microseconds before slower participants. This speed differential creates a systematic, repeatable advantage that slower participants — including most institutional and all retail investors — cannot overcome through superior analysis alone. (Source: Scott Patterson)

10. [HIGH] The evolution from floor trading to electronic markets was driven by technology entrepreneurs (Josh Levine, Instinet founders, ECN builders), not by regulators. Regulation — including Reg ATS (1998) and Reg NMS (2005) — followed technological innovation, sometimes with unintended consequences that created new structural problems (fragmentation, latency arbitrage opportunities) while solving old ones (dealer monopoly, wide spreads). (Source: Scott Patterson)

## Concepts Referenced

- dark-pool-trading, [[low-latency-trading]], [[co-location]]
- [[market-making-strategy]], [[market-microstructure]]
- nyse, nasdaq, [[island-ecn]]
- reg-nms, [[payment-for-order-flow]]
- [[flash-crash-2010]], [[algorithmic-trading]]
- [[smart-order-routing]], [[execution-quality]]

## Pages Backed

- [[low-latency-trading]] — speed arms race in electronic markets
- [[co-location]] — infrastructure advantage in the fragmented electronic market
- [[market-making-strategy]] — transition from human specialists to algorithmic market makers
- [[dark-pools]] — primary source for the education/concept page
