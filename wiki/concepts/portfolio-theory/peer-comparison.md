---
title: "Peer Comparison"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, valuation]
aliases: ["Comparable Analysis", "Relative Valuation", "Comps", "Comparable Company Analysis", "Comparative Analysis"]
domain: [fundamental-analysis]
prerequisites: ["[[valuation]]", "[[fundamental-analysis]]"]
difficulty: intermediate
related: ["[[price-to-earnings-ratio]]", "[[gics-classification]]", "[[return-on-equity]]", "[[forward-pe]]", "[[valuation]]", "[[fundamental-analysis]]", "[[comparable-company-analysis]]", "[[valuation-multiples]]", "[[dcf-analysis]]"]
---

Peer comparison (also called [[comparable-company-analysis|comparable company analysis]], relative valuation, or "comps") is the practice of evaluating a company's financial metrics against those of similar companies within the same sector or industry. It is one of the most widely used [[valuation]] methodologies in [[fundamental-analysis|fundamental analysis]], both by equity research analysts and portfolio managers. Key metrics compared typically include [[price-to-earnings-ratio|PE ratio]], [[return-on-equity|ROE]], [[gross-margin]], revenue growth, and debt levels. Fred McNaught always benchmarks a company against its [[gics-classification|GICS sector]] peers, arguing that a PE ratio is meaningless in isolation -- a PE of 25 is cheap in one sector and expensive in another. He uses peer comparison as a primary tool alongside [[dcf-analysis|DCF analysis]] to triangulate a company's relative attractiveness.

The core logic is the **law of one price**: similar assets should trade at similar prices. If two companies have nearly identical growth, margins, and risk but one trades at 12x earnings and the other at 18x, the comparison flags a potential mispricing — or, more often, prompts the analyst to ask *what hidden difference justifies the gap*. Comps are fast, market-grounded (they reflect what investors are actually paying *today*), and require fewer assumptions than a [[dcf-analysis|DCF]] — which makes them the everyday workhorse of relative value while DCF supplies the absolute anchor.

## Selecting an Appropriate Peer Group

The quality of a peer comparison depends entirely on the quality of the peer group. Ideal peers share the same industry, business model, geographic exposure, and growth profile. The [[gics-classification|GICS]] (Global Industry Classification Standard) provides a starting framework, but analysts must exercise judgement. For example, Amazon operates in e-commerce, cloud computing (AWS), advertising, and logistics -- comparing it solely to traditional retailers is misleading. Common approaches include: using GICS sub-industry peers as a starting set, then filtering by market capitalisation (comparing a $500M company to a $500B company is rarely useful), geographic revenue mix, and growth stage (high-growth vs mature). A typical peer group contains 5-12 companies.

## Key Multiples and Metrics

The most commonly used multiples in peer comparison include:

- **P/E ratio** ([[price-to-earnings-ratio]]) -- Price to earnings; most widely quoted but distorted by capital structure and accounting policies
- **EV/EBITDA** -- Enterprise value to EBITDA; capital-structure neutral, preferred for comparing companies with different leverage levels
- **P/S (Price to Sales)** -- Used for high-growth or unprofitable companies where earnings multiples are meaningless
- **[[forward-pe|Forward P/E]]** -- Based on consensus earnings estimates, captures expected growth better than trailing P/E
- **EV/Revenue** -- Common in SaaS and technology, where revenue growth rate matters more than current profitability
- **P/B (Price to Book)** -- Used primarily for financials (banks, insurers) where book value is a meaningful proxy for liquidation value

See [[valuation-multiples]] for the full menu. A quick guide to which multiple fits which situation:

| Multiple | Best for | Why / caveat |
|----------|----------|--------------|
| [[price-to-earnings-ratio\|P/E]] | Profitable, stable companies | Most quoted; distorted by leverage, one-offs, accounting |
| [[forward-pe\|Forward P/E]] | Growth names | Uses consensus EPS; captures expected growth, but estimates can be wrong |
| EV/EBITDA | Comparing firms with different leverage | Capital-structure neutral; ignores capex and D&A intensity |
| EV/Revenue | High-growth, pre-profit (SaaS, biotech) | Works when there are no earnings; says nothing about margins |
| P/S (Price/Sales) | Unprofitable or cyclical-trough firms | Ignores profitability entirely — a low P/S can be a value trap |
| P/B (Price/Book) | Banks, insurers, asset-heavy | Book value must be economically meaningful |
| PEG (P/E ÷ growth) | Growth-adjusted screening | Normalises P/E for growth; unreliable at very low or negative growth |

When comparing multiples, always adjust for material differences. A company trading at 15x earnings with 20% growth is cheaper than a peer at 12x earnings with 5% growth -- the PEG ratio (P/E divided by growth rate) captures this, though it has its own limitations (PEG of 0.75 vs 2.4 in this case).

> **Worked example — applying a peer multiple.** Suppose a private (or newly-listed) software company earns $80M of net income and you want a quick value. Its five closest public peers trade at forward P/Es of 22x, 25x, 19x, 30x, and 24x — a median of **24x**. Applying the median to earnings gives an implied equity value of $80M × 24 = **$1.92B**. But the target grows revenue 15% vs the peer-group median of 25%, so a slower grower should trade at a *discount* to the median — say 20x, implying ~$1.6B. The mechanical median is the starting point; the qualitative adjustment for growth, margins, and risk is where the analyst earns their keep.

## Adjusting for Differences

No two companies are identical, so raw multiple comparisons must be contextualised. Key adjustments include: **size** (smaller companies typically trade at lower multiples due to liquidity and risk premiums), **growth** (faster-growing companies deserve higher multiples), **profitability** (higher-margin businesses command premiums), **geography** (emerging market exposure may warrant a discount for [[sovereign-risk]]), and **capital structure** (highly leveraged companies may appear cheap on P/E but not on EV/EBITDA). Precedent transactions -- what acquirers have actually paid for comparable companies -- provide another reference point, though transaction multiples typically include a control premium of 20-40% above trading levels.

## How Traders and Investors Use Comps

- **Screening and idea generation.** Ranking a peer set by a multiple surfaces the cheapest and most expensive names quickly; the outliers are where to dig — a stock far below its peers is either a bargain or a value trap, and a stock far above is either a quality premium or froth.
- **Relative-value / pairs trades.** A discounted name relative to a near-identical peer supports a long/short [[pairs-trading|pairs]] position (long the cheap one, short the rich one), neutralising sector beta so the trade depends only on the spread converging.
- **Multiple re-rating thesis.** Much of an equity move is *multiple expansion or compression*, not earnings growth. Traders look for catalysts (margin inflection, capital return, index inclusion, takeover) that could close a peer-multiple gap.
- **M&A and IPO pricing.** Bankers price deals and IPOs off comps (plus a precedent-transaction control premium of ~20-40%); an acquirer trading at a richer multiple than its target can make an accretive cash-and-stock deal.
- **Sanity check on a DCF.** If a [[dcf-analysis|DCF]] implies a multiple wildly out of line with the peer group, one of the two analyses is wrong — comps and DCF are meant to triangulate, per Fred McNaught's approach.

## Limitations

Peer comparison is inherently relative -- it tells you whether a stock is cheap or expensive relative to peers, but if the entire sector is overvalued, a "cheap" stock in the group may still be expensive in absolute terms. During the dot-com bubble, internet stocks trading at 50x revenue looked "cheap" compared to peers at 100x revenue. Peer comparison also struggles with unique companies that have no close comparables (e.g., Berkshire Hathaway, ASML). For this reason, relative valuation should be used alongside absolute valuation methods like [[dcf-analysis|DCF analysis]].

## Sources

- Aswath Damodaran, *Investment Valuation* (3rd ed.) — chapters on relative valuation and the choice of comparable firms and multiples.
- McKinsey & Company (Koller, Goedhart, Wessels), *Valuation: Measuring and Managing the Value of Companies* — guidance on building peer sets and normalising multiples.
- CFA Institute curriculum — Equity Valuation: market-based (price and enterprise value) multiples and the method of comparables.

## Related

- [[valuation]] -- broader valuation concepts
- [[fundamental-analysis]] -- fundamental analysis framework
- [[price-to-earnings-ratio]] -- P/E ratio
- [[return-on-equity]] -- ROE as a quality metric
- [[gics-classification]] -- industry classification for peer selection
- [[forward-pe]] -- forward-looking multiples
- [[comparable-company-analysis]] -- the formal name for the comps method
- [[valuation-multiples]] -- the full catalogue of multiples used in comps
- [[dcf-analysis]] -- absolute valuation complement
