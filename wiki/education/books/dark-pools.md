---
title: "Dark Pools — Scott Patterson (2012)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [education, book, hft, market-microstructure, electronic-trading, history]
related:
  - "[[dark-pools]]"
  - "[[high-frequency-trading]]"
  - "[[market-microstructure]]"
  - "[[low-latency-trading]]"
  - "[[co-location]]"
  - "[[market-making-strategy]]"
  - "[[flash-boys]]"
  - "[[the-quants]]"
---

**Dark Pools: The Rise of the Machine Traders and the Rigging of the U.S. Stock Market** by Scott Patterson (2012) chronicles the transformation of American equity markets from human floor exchanges into the fragmented, algorithmic, high-speed electronic system that exists today. Patterson — who also wrote [[the-quants]] — structures the narrative around Josh Levine, a self-taught programmer who in the 1990s built **Island ECN**, the first fully electronic stock exchange, out of frustration with the slow, opaque NASDAQ dealer system. Island proved electronic matching was faster and cheaper than human market makers and set in motion the chain of innovation and disruption that produced modern [[high-frequency-trading]] and [[dark-pools|dark-pool]] market structure.

## Key Facts

| Field | Detail |
|-------|--------|
| **Author** | Scott Patterson (*Wall Street Journal*; author of [[the-quants]], 2010) |
| **Published** | 2012 |
| **Publisher** | Crown Business |
| **Full subtitle** | *The Rise of the Machine Traders and the Rigging of the U.S. Stock Market* |
| **Central figure** | Josh Levine, creator of Island ECN |
| **Topic** | Electronic market structure: ECNs, [[dark-pools]], [[high-frequency-trading]], fragmentation |
| **Pivotal regulation** | Reg NMS (2005) and the NBBO / order-protection rule |
| **Defining event** | The May 6, 2010 [[flash-crash|flash crash]] |
| **Companion book** | [[flash-boys]] (Michael Lewis, 2014); [[trading-and-exchanges]] (Larry Harris, academic) |

## Core Thesis

The electronic-markets revolution was driven by **technologists and entrepreneurs, not regulators or incumbent exchanges** — and regulation followed innovation, often with unintended consequences. Idealists like Josh Levine set out to democratize markets and break the dealers' grip; their tools were then captured and weaponized by [[high-frequency-trading]] firms. The result is a market that is cheaper in commissions and more accessible, but also more fragmented, more opaque, and potentially more fragile — a structure in which speed itself confers a structural, two-tiered advantage. Patterson's provocative subtitle ("rigging") frames the question of whether ordinary investors are systematically disadvantaged by the machinery they cannot see.

## Three Developments That Reshaped Markets

1. **ECNs and alternative trading systems.** Electronic communication networks (Island and successors) competed with the nyse and nasdaq, fragmenting liquidity across dozens of venues and ending open-outcry floor trading.
2. **Dark pools.** Off-exchange venues created so institutions could trade large blocks without revealing intentions — but increasingly populated by HFT firms exploiting the very opacity the pools were meant to provide (dark-pool-trading).
3. **Regulatory response (Reg NMS, 2005).** The order-protection rule forced brokers to route to the venue showing the best displayed price (the NBBO), which inadvertently *deepened* fragmentation and created the cross-venue latency-arbitrage opportunities HFT now harvests.

## Chapter / Section Themes

- **The Island origin story.** Levine, Datek, and the building of an electronic order book that undercut NASDAQ dealers.
- **The dealer fight.** The SOES "bandits," NASDAQ's resistance, and the regulatory battles that legitimized electronic matching.
- **Fragmentation and the rise of ECNs.** How liquidity scattered across competing venues and exchanges demutualized and went public.
- **The machine traders.** The emergence of [[high-frequency-trading]] firms, [[co-location]], proprietary feeds, and the [[low-latency-trading|speed]] arms race.
- **Dark pools and order flow.** Internalization, payment for order flow, and the conflicts created when retail flow is sold to wholesalers.
- **Artificial intelligence on Wall Street.** Patterson's look at adaptive/AI-driven trading systems (e.g., the "Star" project he profiles) — markets run by code with limited human oversight.
- **The flash crash.** The May 6, 2010 collapse and what it revealed about algorithmic liquidity vanishing under stress.

## Key Concepts and Takeaways

| Concept | Takeaway |
|---------|----------|
| Island ECN | The first fully electronic exchange proved matching could be faster, cheaper, more transparent than dealers. |
| Dark pools | Built to shield large institutional orders, but their opacity was exploited by faster, predatory traders (dark-pool-trading). |
| Rapid electronification | The nyse floor gave way to electronic trading in just a few years, not the gradual evolution many expected. |
| Reg NMS unintended effects | Best-execution mandates fragmented markets and birthed cross-venue latency arbitrage. |
| Algorithmic market making | Algos replaced human specialists — tighter spreads, but fragility when liquidity withdraws in unison. |
| Payment for order flow | Selling retail order flow to wholesalers/HFT creates conflicts and can worsen execution prices. |
| Fragmentation opacity | 13+ exchanges and 40+ dark pools make true best-execution nearly impossible to verify. |
| Flash crash (2010) | The Dow fell ~1,000 points in minutes as algo liquidity providers simultaneously pulled quotes. |
| Two-tiered speed market | [[co-location]] + proprietary feeds = microsecond information advantages slower traders cannot overcome. |
| Tech leads, regulation follows | The shift was driven by entrepreneurs; rules adapted afterward, often creating new problems. |

## Criticisms and Limitations

- **Loaded "rigging" framing.** The subtitle is more accusatory than the evidence strictly supports; many microstructure economists argue retail investors today get *better* prices and lower costs than in the dealer era, even if intermediaries also profit.
- **Less polished narrative than [[flash-boys]].** Lewis's competing 2014 book has a sharper point of view and broader readership, though Patterson's is arguably more technically thorough and balanced.
- **Dating.** Published in 2012, before later structural debates (maker-taker reform, the IEX speed bump, retail PFOF scrutiny culminating in the 2021 meme-stock episode) — the regulatory landscape has moved on.
- **Light on the math.** The book describes mechanics journalistically; readers wanting rigorous models should pair it with [[algorithmic-and-high-frequency-trading]] (Cartea, Jaimungal, Penalva) or [[trading-and-exchanges]] (Harris).
- **Ambiguous verdict on HFT.** Patterson documents both the benefits (liquidity, tight spreads) and harms (fragility, opacity) without fully resolving whether HFT is net-positive — which some readers find unsatisfying.

## Who Should Read This

Anyone who wants to understand *why* modern markets look the way they do: why there are so many venues, what dark pools actually are, how HFT works, and why execution quality matters. Traders building execution algorithms or smart order routers will find essential context. A natural companion to [[flash-boys]] — read both for the complete picture, plus [[trading-and-exchanges]] for the academic treatment.

## How It Applies to AI Trading

*Dark Pools* explains the infrastructure layer that sits between an AI model's signal and its actual fill — the [[market-microstructure]] that determines whether alpha survives to the executed price. AI systems that generate brilliant signals but route orders naively hemorrhage edge to better-informed participants. Concrete applications: (1) AI-powered smart order routing that selects venues by historical fill quality and real-time dark/lit liquidity; (2) [[machine-learning|ML]] models that predict when algorithmic liquidity is likely to withdraw (flash-crash-like conditions) to drive defensive sizing; (3) evaluating broker PFOF and execution quality against the alpha it may cost; and (4) designing [[market-making-strategy|market-making]] and execution algos suited to a fragmented, multi-venue world. The book also explains why [[low-latency-trading]] and [[co-location]] exist, informing the build-vs-buy decision on execution speed versus signal quality.

## Rating

**8/10** — A thorough, well-researched history of electronic market structure with strong technical depth and a journalist's eye for character. Slightly overshadowed by [[flash-boys]] in popular awareness but arguably more comprehensive and balanced on HFT. The Josh Levine / Island ECN origin story is genuinely compelling and far less well-known than the IEX story.

## Related

- dark-pool-trading / [[dark-pools]] — The off-exchange venues at the center of the narrative
- [[high-frequency-trading]] — The machine-trading business model the book chronicles
- [[market-microstructure]] — The field that formally studies these dynamics
- [[low-latency-trading]] — The speed arms race electronic markets created
- [[co-location]] — Server-placement advantages that define HFT competitiveness
- [[market-making-strategy]] — How electronic market makers replaced human specialists
- [[flash-boys]] — Michael Lewis's companion narrative on HFT and market structure
- [[the-quants]] — Patterson's earlier book on the quant revolution
- [[trading-and-exchanges]] — Larry Harris's academic treatment of the same topics

## Sources

General market knowledge; no specific wiki source ingested yet.
