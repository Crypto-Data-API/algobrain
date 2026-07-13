---
title: "Barchart"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [data-provider, options, futures, commodities, stocks]
aliases: ["Barchart.com", "Barchart Solutions", "cmdtyView"]
related: ["[[orats]]", "[[market-chameleon]]", "[[finviz]]", "[[yahoo-finance]]", "[[unusual-whales]]", "[[cot-data]]", "[[commodity-data-sources]]", "[[options-flow-analysis]]", "[[futures-data-sources]]"]
entity_type: company
website: "https://www.barchart.com"
founded: 1995
headquarters: "Chicago, USA"
---

# Barchart

**Barchart** is a long-running market-data and analytics provider founded in 1995 and headquartered in Chicago. It operates a free public site at barchart.com and a tiered paid product line (Barchart Premier, Barchart Pro, and an enterprise data services arm). Barchart is best known among options traders for its **free options screener** and among commodity and futures traders for its deep coverage of agricultural, energy, and metals contracts. Its cross-asset breadth makes it a useful complement to deeper options-specialist tools like [[orats]] or [[market-chameleon]].

## Overview

Barchart sits in an unusual product niche. The free tier is one of the most generous in the industry — offering an options screener with filtering by IV rank, volume, OI, premium, and technicals; futures pages with COT data; and free commodity quotes — while the paid tiers compete with [[finviz]], [[yahoo-finance]], and the lower end of professional terminals. The company also runs a B2B data-services arm (Barchart Solutions) that provides market data to media outlets, agribusiness firms, and brokerages.

Asset coverage spans **equities, futures, options, forex, crypto, and cash commodities**. The futures and commodities depth is unusual among retail-focused platforms — Barchart maintains contract-level pages for grain, livestock, energy, and metals contracts that are typically only available through dedicated futures vendors.

## cmdtyView and 2026 Developments

Barchart's flagship professional product is **cmdtyView**, a commodity trading and risk platform serving global commodity traders, merchandisers, brokers, and analysts, with market pricing, fundamentals, news, and workflow tools spanning CME Group, ICE, B3, SGX, and Euronext listed markets plus thousands of spot and physical (cash) markets. Key 2026 developments:

- **April 1, 2026** — Barchart announced expanded physical-commodity research capabilities in cmdtyView, adding deeper access to global fundamental, economic, and trade data for supply-chain analysis (Barchart press release)
- **April 22, 2026** — Barchart launched **Carl**, an AI assistant embedded directly in cmdtyView, aimed at accelerating price discovery, trading, and market research across the platform's commodity data ecosystem (Barchart/PR Newswire)

These moves reinforce Barchart's positioning as the dominant data layer for North American agribusiness — the same data many traders consume indirectly via broker apps and farm-management software.

## Pricing

| Tier | Approximate Cost | What You Get |
|------|------------------|--------------|
| **Free (Barchart.com)** | $0 | Free options screener (limited columns), 15-20 min delayed quotes, basic charts, futures and commodity pages, COT reports |
| **Barchart Premier** | ~$30-60/mo (sometimes promoted lower) | Real-time data on US exchanges, expanded options screeners with proprietary indicators, advanced technical indicators, custom watchlists, screener saves |
| **Barchart Pro** | ~$100/mo+ | Streaming real-time futures and equities, full screener customization, API tier, priority support |
| **Barchart Solutions (enterprise)** | Custom | Data licensing, embedding API, white-label feeds for brokers and agribusinesses |

Pricing is sometimes promoted aggressively (annual discounts, bundle deals). The free tier alone is one of the most useful free options tools available — many retail traders use it for daily screening without ever upgrading.

## Free Options Screener

Barchart's **free options screener** is the feature that drives most of its retail options-trader user base. Filterable by:

- **Volatility metrics** — IV rank, IV percentile, IV vs HV.
- **Volume and OI** — high-volume options, unusual volume vs OI ratios, open-interest changes.
- **Premium and pricing** — bid-ask, last, volume-weighted average premium.
- **Technical filters** — moving-average crosses, RSI, MACD on the underlying.
- **Earnings and dividend dates** — proximity-to-earnings filtering for IV-crush plays.
- **Strategy presets** — covered calls, cash-secured puts, vertical spreads, iron condors, with pre-configured columns.

The free screener has limits compared with paid options tools: results are capped, columns are fewer, real-time data is delayed, and some advanced filters require Premier. But the floor of "free, useful, broad-coverage options screening" is genuinely competitive — making Barchart a common starting point for retail traders before they upgrade to [[orats]] or [[market-chameleon]].

## Strengths

- **Cross-asset breadth.** Equities, futures, options, forex, crypto, and cash commodities under one platform — useful for traders who watch macro overlays alongside single-name positioning.
- **Free tier depth.** The free options screener and futures pages are unusually capable; many smaller traders never need to pay for an options-screening subscription.
- **Strong futures and commodities coverage.** Barchart was originally built around futures data, and the legacy still shows: grain, livestock, energy, and metals contract pages with deep history are a differentiator vs equity-focused platforms.
- **COT (Commitment of Traders) data.** Free, easy-to-read CFTC COT reports — see [[cot-data]] — with historical charting that many futures traders rely on weekly.
- **Stable history.** Founded in 1995, Barchart has decades of company continuity and a long track record of data quality.
- **Solid mobile experience.** The mobile site and app make it easy to scan free quotes and run quick screens on the go.

## Weaknesses

- **Less options-flow depth than specialists.** Compared with [[unusual-whales]] or [[whalestream]], Barchart's options-flow detection is rudimentary. It surfaces unusual volume but lacks the dedicated flow-attribution and sweep-detection features of flow-specific tools.
- **Less analytical depth than ORATS / Market Chameleon.** No proprietary smoothed IV surface (compare [[orats]]), and scanners are less customizable than [[market-chameleon]].
- **No built-in backtester.** Unlike [[orats]], Barchart does not include an options strategy backtester.
- **Real-time tier needed for active trading.** The free 15-20 min delay disqualifies the free tier for active intraday options work; Premier upgrades resolve this.
- **UI feels dated.** The site is information-dense in a way that some users find cluttered relative to newer competitors.

## Use Cases

- **Commodity and futures overlay.** Traders running a futures program (grains, energy, metals) use Barchart for free quotes, contract specs, and COT positioning.
- **Free options screening.** Retail options traders use the free screener for daily idea generation, particularly for IV-rank-based premium-selling and earnings IV plays.
- **Macro / cross-asset monitoring.** Single dashboard for stocks, bonds, futures, forex, crypto when assembling a macro view.
- **Agribusiness and corporate users.** Barchart Solutions distributes market data into farm-management software, broker apps, and media sites — many traders end up consuming Barchart data without realizing it.
- **Education starting point.** New options traders frequently find Barchart's screener documentation and educational content a soft introduction before paying for [[orats]] or institutional tools.

## Related

- [[orats]] — deeper options-analytics specialist; common upgrade from Barchart's free screener
- [[market-chameleon]] — competing options-analytics platform with stronger flow analytics
- [[finviz]] — equities-focused free screener; less options depth than Barchart
- [[yahoo-finance]] — broader free portal, less options-specific tooling
- [[unusual-whales]] — options-flow specialist, complements Barchart for active flow watching
- [[cot-data]] — Commitment of Traders reports, surfaced free on Barchart
- [[commodity-data-sources]] — broader catalog of commodity data providers
- [[futures-data-sources]] — broader catalog of futures data providers
- [[options-flow-analysis]] — concept page on flow-based trading

## Sources

- Barchart corporate site (barchart.com), product documentation and pricing pages.
- Barchart Solutions product documentation (solutions.barchart.com).
- CFTC Commitment of Traders weekly reports (cftc.gov), redistributed by Barchart.
- Industry comparison reviews of options screeners (multiple, 2023-2025).
- Barchart/PR Newswire, "Barchart's cmdtyView Platform Brings Powerful AI to the Global Commodity Industry" (Apr 22, 2026) — https://www.prnewswire.com/news-releases/barcharts-cmdtyview-platform-brings-powerful-ai-to-the-global-commodity-industry-302749719.html
- Barchart/PR Newswire, "Barchart Expands Physical Commodity Research Capabilities in cmdtyView" (Apr 1, 2026) — https://www.prnewswire.com/news-releases/barchart-expands-physical-commodity-research-capabilities-in-cmdtyview-with-in-depth-access-to-global-fundamental-data-302731064.html
- cmdtyView product page — https://www.barchart.com/solutions/software/cmdtyview
- Verified via web search, 2026-06-10. Note: exact current Barchart Premier pricing is not published in verifiable third-party sources; the table above reflects approximate ranges and should be checked against barchart.com before purchase.
