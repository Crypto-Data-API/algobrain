---
title: "Market Making"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [market-microstructure, liquidity, algorithmic]
aliases: ["market-making", "Market Making"]
domain: [market-microstructure]
prerequisites: ["[[market-maker]]", "[[bid-ask-spread]]", "[[liquidity]]", "[[order-book]]"]
difficulty: advanced
related: ["[[market-maker]]", "[[bid-ask-spread]]", "[[liquidity]]", "[[order-types-overview]]", "[[market-microstructure]]", "[[depth-of-market]]", "[[high-frequency-trading]]"]
---

Market making is the practice of continuously quoting both buy and sell prices for a security, profiting from the [[bid-ask-spread]] while providing [[liquidity]] to other market participants. A [[market-maker]] takes on inventory risk in exchange for the spread. Referenced in ITPM content as one of the core functions of institutional trading desks at banks like [[goldman-sachs]], [[morgan-stanley]], and [[commerzbank]].

## How Market Making Works

A market maker posts a bid (the price at which they will buy) and an ask (the price at which they will sell) simultaneously. The difference between these two prices is the [[bid-ask-spread]], which represents the market maker's gross revenue per round-trip transaction. For example, if a market maker quotes a bid of $100.00 and an ask of $100.05, they earn $0.05 for each share they buy and subsequently sell. In practice, market makers execute thousands or millions of such transactions daily, and the cumulative spread income can be substantial. However, the market maker bears the risk that the asset moves against their accumulated inventory before they can offset it -- this is inventory risk, the central challenge of the business.

## Inventory Risk Management

When a market maker buys more shares than it sells (or vice versa), it accumulates a directional position. If the price moves adversely, the unrealized loss on inventory can exceed the spread revenue earned. Sophisticated market makers manage this risk by dynamically adjusting their quotes: widening the spread or shifting the mid-price away from the side where they have excess inventory. They also hedge using correlated instruments (e.g., hedging single-stock inventory with index futures) and employ real-time risk limits that automatically flatten positions when exposure thresholds are breached. The Avellaneda-Stoikov model (2008) formalized optimal quote placement as a function of inventory, volatility, and time horizon.

## Types of Market Makers

**Designated Market Makers (DMMs)** have formal obligations to maintain continuous quotes and orderly markets for assigned securities. On the NYSE, DMMs (formerly called specialists) are required to step in as buyer or seller of last resort during periods of imbalance. In exchange, they receive informational advantages such as seeing the [[depth-of-market|order book]] and incoming order flow. **Electronic market makers** operate on fully electronic venues without formal obligations but compete on speed and sophistication. Firms like Citadel Securities, Virtu Financial, and Jane Street dominate modern electronic market making, deploying sophisticated algorithms that adjust quotes in microseconds based on order flow signals, volatility changes, and cross-asset correlations. Citadel Securities alone handles roughly 25-30% of all US equity volume. **OTC market makers** operate in less transparent dealer markets (bonds, swaps, FX forwards) where they negotiate prices bilaterally.

## Market Making in Options

Options market making is particularly complex because each underlying has dozens or hundreds of strikes and expirations, creating a high-dimensional inventory management problem. Options market makers must manage exposure across all [[greeks]] simultaneously -- not just directional (delta) risk but also [[implied-volatility|volatility]] (vega), time ([[theta-decay|theta]]), and convexity (gamma) risk. This is the world described extensively in ITPM's institutional trading curriculum, where banks' derivatives desks run large short-gamma, short-vega books and hedge continuously.

## Economics and Competition

Market making has become increasingly competitive and technology-driven. Bid-ask spreads have compressed dramatically over the past two decades due to decimalization (2001), Reg NMS (2005), and the rise of [[high-frequency-trading|high-frequency trading]]. Average US equity spreads are now 1-2 cents for liquid large-caps, down from 12.5 cents (1/8th of a dollar) in the pre-decimalization era. This compression means market makers must process far higher volumes to generate comparable revenue, favoring firms with the fastest technology and lowest operating costs.

## Related

- [[market-maker]] — the participant (this page covers the activity)
- [[bid-ask-spread]] — the spread that generates market maker revenue
- [[liquidity]] — the service market makers provide
- [[depth-of-market]] — the order book market makers populate
- [[market-microstructure]] — the broader study of how markets function
- [[high-frequency-trading]] — technology-driven evolution of market making

## Sources

- Marco Avellaneda and Sasha Stoikov, "High-frequency trading in a limit order book," *Quantitative Finance* 8(3), 2008 — the foundational inventory/quote-placement model
- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* (Oxford University Press, 2003)
- Maureen O'Hara, *Market Microstructure Theory* (Blackwell, 1995)
- Sheldon Natenberg, *Option Volatility and Pricing* (McGraw-Hill, 2nd ed., 2014) — options market making and the Greeks
- SEC, "Regulation NMS" (2005) and the history of decimalization (2001) — drivers of spread compression
