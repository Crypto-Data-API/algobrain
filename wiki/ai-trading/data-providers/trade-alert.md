---
title: "Trade Alert"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [data-provider, options, derivatives]
aliases: ["TradeAlert", "Trade Alert LLC", "Cboe Trade Alert"]
related: ["[[unusual-whales]]", "[[whalestream]]", "[[optionstrat]]", "[[cboe-livevol]]", "[[cboe-global-markets]]", "[[orats]]", "[[market-chameleon]]", "[[opra]]", "[[options-flow-analysis]]"]
entity_type: company
founded: 2005
headquarters: "New York, USA"
website: "https://www.tradealert.com"
---

# Trade Alert

**Trade Alert** is an institutional-grade options analytics platform founded in New York in 2005 by Henry Schwartz and acquired by [[cboe-global-markets|Cboe Global Markets]] in June 2020. After the acquisition it was folded into Cboe's broader trading-analytics stack (alongside [[cboe-livevol|LiveVol]] and Hanweck) and is now operated as part of Cboe's institutional data and analytics business. Trade Alert specializes in real-time options flow analytics, unusual options activity (UOA) detection, and surveillance for buy-side and sell-side institutions.

## Overview

Trade Alert was founded in 2005 by Henry Schwartz, a long-time options-market practitioner and frequent commentator on listed options activity who began his career as a runner on the Cboe trading floor in the 1990s before market-making roles in New York, Frankfurt, and Paris and index-desk leadership at Salomon Brothers and Bear Stearns. The platform's core proposition is taking the full [[opra|OPRA]] consolidated options tape and turning it into actionable institutional flow signals: unusual prints, large block attribution, sweep detection, customer-vs-firm classification, and volatility-weighted flow heatmaps.

On 2 June 2020 Cboe announced the acquisition of Trade Alert (terms undisclosed; funded with cash on hand) as part of a broader push to unify exchange-owned analytics products under its Information Solutions offering. The Trade Alert technology and team were integrated into Cboe's data business and now sit alongside the [[cboe-livevol|LiveVol]] analytics products, the Hanweck risk-analytics line, and the Cboe DataShop distribution channel.

## Acquisition by Cboe (2020)

The June 2020 acquisition completed the consolidation of three previously independent options-analytics businesses under one Cboe umbrella:

- **LiveVol** (acquired 2015) — historical and real-time options data, volatility-surface analytics
- **Hanweck** (acquired February 2020) — real-time options risk and pricing analytics
- **Trade Alert** (acquired June 2020) — real-time flow analytics and unusual-activity surveillance

The combined stack is now sold and supported as Cboe's "Trading Analytics" suite, with Trade Alert specifically retaining its brand for institutional flow surveillance.

## Henry Schwartz at Cboe (2020–2026)

Following the acquisition, Henry Schwartz joined Cboe and serves as **Vice President, Market Intelligence** (current as of 2025), analyzing trends and delivering data-driven insights to banks, market makers, brokers, and proprietary trading firms. He remains one of the most visible public commentators on US options market structure — authoring Cboe's volume and volatility commentary, presenting on the growth of [[0dte-trading|0DTE]] trading (including a data-driven session at HOOD Summit 2025), and publishing analyses such as Cboe's "State of the Options Industry 2025".

## Products and Features

Core capabilities of the Trade Alert platform:

- **Institutional flow heatmaps** — real-time visualizations of where options volume is concentrating across underliers, strikes, and expiries.
- **Unusual options activity detection** — algorithmic flagging of prints that are unusual relative to a contract's typical volume, open interest, and historical flow.
- **Large-trade attribution** — identification of block trades, complex orders, and multi-leg structures, with customer-vs-firm classification where the tape supports it.
- **Sweep and aggressor detection** — surfacing aggressive multi-exchange order routing that signals urgency.
- **Customizable alerts** — programmable triggers on volume thresholds, IV moves, premium spent, and combinations thereof, delivered via desktop UI, email, or API.
- **Historical replay** — ability to step through past sessions for compliance review or research.
- **API access** — institutional API for piping flow signals into proprietary trading systems and dashboards.
- **Surveillance tooling** — features oriented to compliance and best-execution review for broker-dealers and exchanges.

## Customer Base (Institutional Only)

Trade Alert's customers are almost exclusively institutional. Typical accounts include:

- Hedge funds running event-driven, vol-arb, or directional options strategies.
- Proprietary trading firms and market-making desks.
- Broker-dealers monitoring institutional flow and routing decisions for their clients.
- Sell-side derivatives desks watching positioning across the buy side.
- Compliance and surveillance teams within banks, exchanges, and market makers.

The product is not retail-facing; pricing, contracts, and onboarding all assume an institutional buyer.

## Pricing

Institutional pricing only. Subscriptions typically start in the **$1,000+/month** range per seat for the base platform and escalate based on data tier (real-time vs delayed), API throughput, surveillance modules, and number of users. Full institutional deployments with multiple seats and API access regularly run into five-figure monthly commitments. Procurement requires the standard Cboe data-vendor onboarding (market-data agreements, audit rights, etc.).

## How It Differs from Retail Flow Tools

Several retail-oriented platforms target a similar conceptual workflow ("watch options flow, find unusual prints"), but the depth, customization, and integration story is materially different:

| Capability | Trade Alert (institutional) | [[unusual-whales]] / [[whalestream]] / [[optionstrat]] (retail) |
|------------|----------------------------|----------------------------------------------------------------|
| **Tape access** | Full OPRA real-time | Generally OPRA via redistributor (sometimes delayed) |
| **Customer vs firm classification** | Yes, where reportable | Limited / inferred |
| **Customizable rules engine** | Deep, scriptable | Limited UI presets |
| **API for integration** | Yes, institutional grade | Yes, but throughput tiers are smaller |
| **Compliance / surveillance features** | Yes, exchange-grade | No |
| **Prime-broker workflow integration** | Yes | No |
| **Pricing** | $1k+/mo per seat | $50-$200/mo |
| **Target user** | Institutional desks | Retail and small-RIA traders |

The retail tools are better for individual traders learning to read flow; Trade Alert is the right tool when a fund needs to integrate flow signals into a production trading or surveillance pipeline.

## ITPM-Style Use Cases

For an [[itpm-playbook|ITPM]]-style options portfolio operating at institutional scale, Trade Alert is one of the standard tools for:

- **Institutional flow surveillance.** Knowing whether the smart money is leaning long or short in a name before sizing a directional or volatility position.
- **Large-print attribution.** Distinguishing genuine institutional positioning from retail noise — a frequent failure mode of retail flow-watching that Trade Alert is built to solve.
- **Multi-leg structure detection.** Identifying when funds are establishing complex spreads (calendars, ratio spreads, jade lizards, etc.) that telegraph a positioning view.
- **Best-execution review.** Compliance teams using historical replay to verify that client orders were routed and filled at competitive prices.
- **Volatility-event positioning.** Tracking where flow concentrates ahead of earnings, FOMC, or macro events to inform tail-hedge and overlay sizing.

For solo traders or smaller firms where the budget does not stretch to Trade Alert, the practical alternative is a retail-flow stack ([[unusual-whales]], [[whalestream]], [[optionstrat]]) paired with [[orats]] or [[market-chameleon]] for analytics depth. The retail stack reproduces a simplified version of the workflow at a fraction of the cost but lacks the institutional-grade attribution and integration.

## Related

- [[unusual-whales]] — retail-oriented options flow tool, frequently used as a Trade Alert substitute by smaller firms
- [[whalestream]] — another retail flow platform
- [[optionstrat]] — retail options strategy and flow visualization
- [[cboe-livevol]] — sister Cboe analytics product covering historical and volatility data
- [[cboe-global-markets]] — parent exchange operator
- [[orats]] — complementary options analytics with deep IV/scanner capabilities
- [[market-chameleon]] — competing options analytics platform
- [[opra]] — underlying consolidated options tape
- [[options-flow-analysis]] — concept page on flow-based trading

## Sources

- PR Newswire, "Cboe Global Markets Acquires Trade Alert, Adding Real-time Alerts and Analytics to Information Solutions Offering", 2 June 2020: https://www.prnewswire.com/news-releases/cboe-global-markets-acquires-trade-alert-adding-real-time-alerts-and-analytics-to-information-solutions-offering-301069140.html (founded 2005 by Henry Schwartz, New York; cash deal, terms undisclosed)
- Traders Magazine, "Cboe Global Markets Acquires Trade Alert": https://www.tradersmagazine.com/departments/technology/cboe-global-markets-acquires-trade-alert/
- Cboe Insights, "Getting to Know Henry Schwartz": https://www.cboe.com/insights/posts/getting-to-know-henry-schwartz/ (career background, VP Market Intelligence role)
- Cboe Insights, "State of the Options Industry 2025": https://www.cboe.com/insights/posts/state-of-the-options-industry-2025/
- Cboe Trading Analytics product documentation (datashop.cboe.com, tradealert.com).
- Options Industry Council and OPRA technical documentation.
- Verified via Perplexity and web search, 2026-06-10
