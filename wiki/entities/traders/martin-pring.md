---
title: "Martin Pring"
type: entity
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [person, technical-analysis, indicators, education, market-regime]
entity_type: person
aliases: ["Martin Pring", "Martin J. Pring"]
website: "https://www.pring.com"
related: ["[[kst]]", "[[know-sure-thing]]", "[[momentum]]", "[[rate-of-change]]", "[[john-murphy]]", "[[intermarket-analysis]]", "[[technical-analysis]]", "[[market-regime]]", "[[sector-rotation]]"]
---

Martin J. Pring is a British-born technical analyst, author, and money manager best known for *Technical Analysis Explained* — often called "the bible of technical analysis" and required reading for the CMT (Chartered Market Technician) Level I exam — and for creating the **[[know-sure-thing|KST (Know Sure Thing)]]** momentum oscillator. His six-stage business-cycle framework remains one of the most widely used top-down models for rotating between [[stocks]], [[bonds]], and [[commodities]].

## Key Facts

| Field | Detail |
|---|---|
| **Full name** | Martin J. Pring |
| **Born** | England (British-born; long based in the United States) |
| **Role** | Technical analyst, author, money manager, educator |
| **Known for** | *Technical Analysis Explained*; the [[know-sure-thing|KST]] oscillator; the six-stage business-cycle model |
| **Firm(s)** | Pring Research (founded 1981); Pring Turner Capital Group (chairman, with Joe Turner) |
| **Publication** | *InterMarket Review* — monthly, since 1984 |
| **Discipline** | [[technical-analysis]], momentum, [[intermarket-analysis]], cycle/regime work |
| **Signature indicator** | [[know-sure-thing|Know Sure Thing (KST)]]; derivative "Special K" |
| **Influence** | Co-shaped the modern technical-analysis curriculum alongside [[john-murphy]] |
| **Website** | https://www.pring.com |

## Career

- **1981**: Founded Pring Research, providing technical research to institutions and individual investors (now pring.com).
- **Since 1984**: Publishes the **InterMarket Review**, a monthly long-term synopsis of the world's major financial markets.
- **Pring Turner Capital Group**: Chairman of the Walnut Creek, California money manager (with Joe Turner), which applies his business-cycle work to client portfolios; he served as strategist for the Pring Turner Business Cycle ETF (DBIZ, launched December 2012, since closed).
- A frequent educator in the technical-analysis community (CMT Association presenter); his textbook has trained several generations of chartists alongside [[john-murphy]]'s intermarket work.

## Key Contributions

### Technical Analysis Explained
First published **1980** (McGraw-Hill), now in its substantially revised **fifth edition (2014)**. Covers trend determination, momentum, cycles, intermarket relationships, and contrary opinion. One of four required books for CMT Level I.

### KST (Know Sure Thing)
A momentum oscillator built from the **smoothed weighted sum of four rate-of-change periods** (short, intermediate, and long lookbacks), designed to capture the cyclical ebb and flow of momentum better than a single-period [[rate-of-change|ROC]]. First described in Pring's 1992 *Technical Analysis of Stocks & Commodities* article "Summed Rate of Change (KST)." See the dedicated page [[know-sure-thing]] for full construction and parameters.

The daily/long-term KST construction uses four [[rate-of-change|ROC]] components, each smoothed and weighted (longer-term components carry more weight):

| Component | ROC period | Smoothing (SMA) | Weight |
|---|---|---|---|
| 1 (short) | 10 | 10 | 1 |
| 2 | 15 | 10 | 2 |
| 3 | 20 | 10 | 3 |
| 4 (long) | 30 | 15 | 4 |

`KST = (ROC1·sma·1) + (ROC2·sma·2) + (ROC3·sma·3) + (ROC4·sma·4)`, with a 9-period SMA of the KST as the **signal line**. **Signals:** KST crossing its signal line, zero-line crossovers, and price/KST divergences. Available on most platforms (StockCharts, TradingView). (Parameter sets vary by timeframe — short-term, intermediate, long-term, and "true" long-term versions all exist.)

### Special K
A derivative indicator that sums short-, intermediate-, and long-term KSTs into a single series intended to peak and trough with the price itself, used to identify primary trend reversals.

### Six-Stage Business Cycle
Pring divides the cycle into six stages defined by the **sequential turning points of [[bonds]], [[stocks]], and [[commodities]]** — bonds bottom first (as the economy weakens and rates fall), then stocks, then commodities (as the recovery matures and inflation builds). The three asset classes peak in the same order on the way down. Each stage favors a different asset mix — an early, practical formulation of regime-based allocation (see [[market-regime]] and [[sector-rotation]]):

| Stage | Bonds | Stocks | Commodities | Economy | Bias |
|---|---|---|---|---|---|
| **1** | Bottoming/up | Down | Down | Late contraction | Buy bonds |
| **2** | Up | Bottoming/up | Down | Trough | Add stocks |
| **3** | Up | Up | Bottoming/up | Early recovery | Fully invested in risk |
| **4** | Topping | Up | Up | Expansion | Trim bonds |
| **5** | Down | Topping | Up | Late cycle / inflation | Trim stocks, hold commodities |
| **6** | Down | Down | Topping | Early contraction | Raise [[cash-as-asset|cash]], defensive |

This bond→stock→commodity sequencing is directly implementable as a top-down regime overlay and is the conceptual ancestor of modern [[intermarket-analysis]] and tactical [[sector-rotation]].

## Method

Pring's approach is **weight-of-the-evidence, multi-timeframe technical analysis** rather than reliance on any single indicator:

- **Trend before timing.** Establish the primary trend first (long-term moving averages, the long-term KST), then use shorter-term tools for entries — never fight the dominant trend.
- **Momentum as a leading tool.** Treat momentum oscillators (KST, [[rate-of-change|ROC]]) as early-warning systems; watch for divergences against price as the most reliable reversal clue.
- **Intermarket context.** No market trades in isolation — bonds, stocks, commodities, and the dollar inform each other, the basis of his *InterMarket Review* and his overlap with [[john-murphy]]'s [[intermarket-analysis]].
- **Cycle stage as a filter.** Use the six-stage model to bias asset and sector selection toward what historically leads in the current phase.
- **Psychology and contrary opinion.** Sentiment extremes and crowd behavior (the subject of *Investment Psychology Explained*) are part of the evidence set — discipline and patience are treated as edge.

## Other Books

- *Investment Psychology Explained* (1993)
- *Martin Pring on Market Momentum* (1993)
- *The All-Season Investor* (1992)
- *Introduction to Technical Analysis* (1997) — plus roughly 15 further titles

## Why Pring Matters to Traders

- The KST family gives a concrete, testable momentum framework spanning multiple timeframes — useful raw material for systematic [[momentum]] strategies.
- His business-cycle stage model is a foundational template for regime filters: the bond→stock→commodity sequencing is directly implementable as a top-down overlay.
- *Technical Analysis Explained* codified the discipline's vocabulary; most modern indicator pages (including this wiki's) inherit his definitions.

## Legacy

- **Curriculum standard.** *Technical Analysis Explained* (1st ed. 1980, 5th ed. 2014) is one of the four required texts for the CMT Level I exam, making Pring a default educator for institutional technicians worldwide.
- **A widely-built indicator.** The [[know-sure-thing|KST]] (and "Special K" derivative) is implemented natively in StockCharts, TradingView, and most charting platforms — one of the few named oscillators from the 1990s still in mainstream use.
- **Regime thinking ahead of its time.** The six-stage cycle model anticipated today's [[market-regime]] / [[regime-detection]] and tactical [[sector-rotation]] frameworks by decades, framing allocation as a function of where bonds, stocks, and commodities sit in the cycle.
- **Bridge to intermarket analysis.** Through the *InterMarket Review* and alongside [[john-murphy]], Pring helped move technical analysis from single-chart pattern reading to a multi-market, cross-asset discipline.
- **Caveats.** His work is firmly in the discretionary technical-analysis tradition; the cycle-stage sequencing is a heuristic, not a backtested rule, and like all [[technical-analysis]] is subject to hindsight bias and parameter sensitivity. Treat KST parameter sets as starting points to validate, not gospel.

## Related

- [[know-sure-thing]], [[kst]] — his signature indicator
- [[momentum]], [[rate-of-change]] — building blocks of KST
- [[intermarket-analysis]], [[john-murphy]] — contemporary; intermarket work complements Pring's cycle model
- [[technical-analysis]]
- [[market-regime]], [[regime-detection]], [[sector-rotation]] — modern descendants of the six-stage framework
- [[marc-chaikin]], [[larry-williams]] — fellow indicator creators

## Sources

- Martin J. Pring, *Technical Analysis Explained*, 5th ed. (McGraw-Hill, 2014) — https://www.amazon.com/Technical-Analysis-Explained-Fifth-Successful/dp/0071825177
- StockCharts ChartSchool, "Pring's Know Sure Thing (KST)" — https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/prings-know-sure-thing-kst
- M. Pring, "Summed Rate of Change (KST)," *Technical Analysis of Stocks & Commodities* (1992)
- CMT Association presenter profile, Martin Pring — https://cmtassociation.org/presenter/martin-pring/ (via cmtassociation.org)
- Web research verification, 2026-06-10
