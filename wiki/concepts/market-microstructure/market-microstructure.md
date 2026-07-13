---
title: Market Microstructure
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - market-microstructure
  - liquidity
aliases:
  - market-microstructure
  - Market Microstructure
domain: [market-microstructure]
prerequisites: ["[[order-book]]", "[[liquidity]]", "[[bid-ask-spread]]"]
difficulty: intermediate
related: ["[[order-book]]", "[[bid-ask-spread]]", "[[market-maker]]", "[[market-making]]", "[[liquidity]]", "[[market-impact]]", "[[slippage]]", "[[high-frequency-trading]]", "[[price-discovery]]"]
---

# Market Microstructure

**Market microstructure** is the study of how exchanges and trading venues operate, how prices are formed, and how orders are executed. It encompasses the mechanics of trading that affect transaction costs, price discovery, and [[liquidity]].

Key topics include [[order-book]] dynamics, [[bid-ask-spread]] formation, [[market-maker]] behavior, [[market-impact]], [[slippage]], and [[high-frequency-trading]].

## What Market Microstructure Covers

Market microstructure research addresses the fundamental mechanics of how trading works:

- **Order books and price discovery** -- how limit orders aggregate into the [[order-book]], how prices form from the interaction of buyers and sellers, and how information is incorporated into prices through trading activity.
- **Market makers and liquidity provision** -- the role of [[market-maker]] firms in providing continuous two-sided quotes, how they manage inventory risk, and how their behavior affects [[bid-ask-spread]] width and market depth.
- **Transaction costs** -- the visible costs (commissions, exchange fees) and hidden costs ([[slippage]], [[market-impact]], timing risk) of executing trades. Understanding total transaction costs is essential for evaluating whether a strategy's edge is real or consumed by friction.
- **Market structure and regulation** -- how exchange rules, order types (limit, market, stop, iceberg), trading venues (lit exchanges, dark pools, internalizers), and regulations (Reg NMS, MiFID II) shape market behavior.

## Why It Matters for Algo Trading

For [[algorithmic-trading]] and systematic strategies, microstructure knowledge is not optional -- it is the foundation upon which execution quality is built. A strategy with a theoretical edge can easily lose money if execution costs are not properly modeled and minimized. Microstructure insights inform decisions about order type selection, execution timing, venue routing, and position sizing.

Understanding microstructure also helps traders recognize signals embedded in order flow -- large hidden orders, spoofing patterns, and shifts in [[liquidity]] -- that can provide short-term directional information.

## Related

- [[order-book]]
- [[bid-ask-spread]]
- [[market-maker]]
- [[liquidity]]
- [[market-impact]]
- [[slippage]]
- [[high-frequency-trading]]
- [[algorithmic-trading]]
- [[price-discovery]]
- [[market-making]]

## Sources

- Maureen O'Hara, *Market Microstructure Theory* (Blackwell, 1995) — the foundational academic text
- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* (Oxford University Press, 2003)
- Ananth Madhavan, "Market microstructure: A survey," *Journal of Financial Markets* 3(3), 2000
- Albert S. Kyle, "Continuous auctions and insider trading," *Econometrica* 53(6), 1985 — the canonical model of informed trading and price impact
- SEC, "Regulation NMS" (2005); ESMA, "MiFID II" (2018) — the regulatory architecture shaping modern market structure
