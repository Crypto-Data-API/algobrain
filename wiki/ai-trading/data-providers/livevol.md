---
title: "LiveVol (Cboe LiveVol Pro and Cboe DataShop)"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [data-provider, options, volatility, derivatives]
entity_type: company
founded: 2009
headquarters: "San Francisco, California, USA"
website: "https://datashop.cboe.com"
aliases: ["LiveVol", "LiveVol Pro", "Cboe LiveVol", "LiveVol Inc"]
related:
  - "[[cboe-livevol]]"
  - "[[cboe-global-markets]]"
  - "[[opra]]"
  - "[[orats]]"
  - "[[optionmetrics]]"
  - "[[databento]]"
  - "[[polygon-io]]"
  - "[[volatility-surface]]"
  - "[[options-premium-selling]]"
  - "[[theta-targeting]]"
---

LiveVol is the brand under which [[cboe-global-markets|Cboe Global Markets]] sells institutional options analytics and historical [[opra|OPRA]]-sourced data, with two principal product surfaces: the **LiveVol Pro** web-based analytics terminal and the **Cboe DataShop** historical-data storefront. Originally an independent San Francisco company founded in 2009 by a group of options traders, LiveVol Inc.'s data and analytics platforms (Livevol Core, Livevol Pro, Livevol X, and Livevol Enterprise) were acquired by CBOE Holdings in a deal announced 2 June 2015 and completed 7 August 2015, becoming the foundation of Cboe's now-unified market-data and analytics business. The deeper history, parent-company context, and licensing terms are covered in [[cboe-livevol]]; this page focuses on the LiveVol product lineage, the LiveVol Pro UI, the feature surface, and pricing tiers.

## Overview

LiveVol Inc. was launched in 2009 to fill a gap in the post-2008 options market: institutional desks and proprietary trading firms wanted a real-time options analytics terminal with [[volatility-surface|volatility-surface]] visualisation, sweep and large-print detection, and a unified historical archive of trades and quotes — but none of the existing institutional platforms were optimised for an options-first workflow. The founding team — a group of options traders and trading-floor technologists, per Cboe's own retrospective — built LiveVol Pro as an options-native web terminal with an emphasis on the [[opra]] tape and the surface dynamics derived from it. Catherine Clay, an early user and investor in the product, joined LiveVol in 2010 as Chief Strategy Officer and was CEO at the time of the Cboe acquisition.

By 2015 LiveVol had been adopted by enough hedge funds, prop desks, and academic researchers that CBOE Holdings — which already operated the largest US options exchanges — acquired the company's data and analytics platforms to consolidate its market-data position (announced 2 June 2015, completed 7 August 2015; Livevol Core, Livevol Pro, Livevol X, and Livevol Enterprise were included). After the acquisition, the LiveVol product line was folded into Cboe's data business; Catherine Clay rose into senior leadership at Cboe — Executive Vice President of Global Digital and Data Solutions, then EVP and Global Head of Derivatives — making the LiveVol acquisition one of the more successful "leadership-stays" data-vendor deals of the period. In October 2025, S&P Global announced Clay would leave Cboe to become CEO of S&P Dow Jones Indices effective 1 November 2025, succeeding Dan Draper. Today the LiveVol brand encompasses the LiveVol Pro web terminal, the Cboe DataShop historical archive (which embeds and extends the original LiveVol historical product), and a suite of EOD and intraday summary feeds, all sitting within Cboe's Data and Access Solutions division alongside the Hanweck risk analytics (acquired February 2020) and [[trade-alert|Trade Alert]] flow analytics (acquired June 2020).

## Key Features / Capabilities

### LiveVol Pro (the web terminal)

LiveVol Pro is the user-facing options analytics platform. The core feature surface:

- **Real-time volatility surface** — full skew and term-structure visualised across strikes and expiries, updated tick-by-tick, with the ability to overlay historical surfaces for comparison.
- **Order-flow tab** — large-print tracker, sweep detector, and customer-vs-firm classification of trades derived from [[opra]] reporting fields.
- **Strategy scanner** — pre-built filters for opportunities across spreads, strangles, [[iron-condor|iron condors]], [[calendar-spread|calendars]], [[diagonal-spread|diagonals]], butterflies, and other multi-leg structures.
- **Real-time Greeks and IV** — delta, gamma, vega, theta, and Black-Scholes IV computed against contemporaneous risk-free rate and dividend inputs, available across all listed US equity, ETF, and index options.
- **Historical replay** — step through past sessions tick-by-tick or in compressed time, useful for training, post-mortems, and academic research.
- **Position-monitoring** — load actual or hypothetical positions and track aggregate Greeks against the live tape (institutional alternative to tools like [[optionnet-explorer]] for in-house desks).
- **Earnings calendar** — integrated event calendar with implied-move and historical-realised-move overlays.

### Cboe DataShop (the data side)

DataShop is the storefront for all Cboe-owned market data, of which the LiveVol historical archive is the largest options-data segment:

- **Tick-level options trades and quotes** — from [[opra]], reaching back to roughly 2004 for deep history.
- **End-of-day options chains** — open, high, low, close, volume, open interest for every listed US contract.
- **Pre-computed IV and Greeks** — calculated using Cboe's pricing model with contemporaneous inputs, saving downstream users a non-trivial amount of pricing-engine work.
- **Open-Close volume data** — customer/firm/market-maker breakdowns of opening and closing transactions.
- **Underlying reference data** — aligned equity and index prices for clean backtests.

## Pricing & Access

LiveVol pricing is institutional and opaque relative to retail data vendors, but commonly cited tiers:

- **LiveVol Pro web terminal** — roughly **$300–$700/month per user** depending on the bundle of real-time exchange-data entitlements and feature set. Real-time OPRA entitlements alone can add several hundred dollars per month per user under standard exchange fees.
- **EOD options data** — historical end-of-day chains run from roughly **$2,000 to $10,000+** as one-time purchases or annual subscriptions depending on the depth and breadth of the archive.
- **Tick history** — multi-terabyte tick-level archives are firmly in the **five-to-six-figure annual range** for full coverage with redistribution rights.
- **Open-Close volume** — separately licensed, mid-four-figure annual cost typical.
- **Academic licensing** — reduced-rate research-only access available, often via institutional subscriptions held by university libraries.
- **Real-time exchange feeds** — licensed under Cboe's market-data agreements separately from DataShop, with non-display fees, derived-product fees, and redistribution surcharges that escalate quickly.

There is no free or trial tier comparable to the consumer data vendors. Procurement runs through Cboe's enterprise sales process with the standard data-vendor paperwork and audit requirements.

## Strengths & Weaknesses

**Strengths:**

- **Canonical data source** — Cboe operates the largest US options exchanges and ingests the full [[opra]] tape, so LiveVol is the reference dataset against which other vendors are benchmarked.
- **Deep history** — tick coverage back to ~2004 spans 2008, the 2010 flash crash, 2015–16, [[volmageddon|2018 Volmageddon]], 2020 COVID, and 2022 rates shock.
- **Pre-computed analytics** — IV and Greeks are stored alongside the raw quotes, saving downstream computation.
- **Audit-grade integrity** — exchange-owned data processes meet the standards required for academic publication and regulatory work.
- **LiveVol Pro is options-native** — the terminal is purpose-built for options analytics in a way Bloomberg and Refinitiv terminals are not.

**Weaknesses:**

- **Cost** — institutional pricing is out of reach for most solo traders; even individual LiveVol Pro seats with real-time entitlements often run $700+/month.
- **Procurement friction** — paperwork and audit cycles typical of exchange-owned vendors slow onboarding for small firms.
- **Licensing constraints** — redistribution and derived-product creation are tightly controlled; the data cannot be embedded in commercial products without separate negotiation.
- **Workflow tooling** — the terminal is excellent for analytical inspection but does not optimise for a packaged "screener-to-execution" workflow the way [[orats]] or [[market-chameleon]] do.
- **US-options focus** — international options data is patchier; non-US markets are not the primary coverage.
- **Two-product complexity** — terminal and DataShop are separately priced and entitled, which adds confusion for buyers expecting a single bundle.

## How Practitioners Use It

A typical institutional workflow:

1. **Volatility-surface research.** Quants pull tick or minute-level surfaces from DataShop for selected underlyings across regime windows, calibrate proprietary surface models, and compare predicted vs realised IV evolution to identify systematic mispricings.
2. **Backtesting [[options-premium-selling|premium-selling]] overlays.** A research desk validates a covered-call, [[options-premium-selling|short-strangle]], or [[iron-condor]] program against actual contemporaneous chains rather than synthetic Black-Scholes prices, with realistic slippage modelled from contemporaneous bid-ask spreads.
3. **Order-flow signal mining.** LiveVol Pro's customer-vs-firm classification is fed into systematic positioning models to detect when retail or institutional flow is extreme and likely to reverse.
4. **Live trading on the desk.** Discretionary options traders keep LiveVol Pro open as the primary surface and order-flow monitor, alongside their execution platform (often a separate broker terminal or [[interactive-brokers|TWS]]).
5. **Academic citation.** When a published paper or LP report references options research, "LiveVol" or "Cboe DataShop" as the data source is sufficient to satisfy reviewers — comparable to [[optionmetrics]] in that respect.
6. **[[theta-targeting|Theta-targeted]] book monitoring.** Institutional premium-selling desks load positions into LiveVol Pro for portfolio-Greeks aggregation and stress-test scenarios across IV and spot shocks.

For a [[itpm-trading-philosophy|ITPM]]-style options portfolio operating at institutional scale, LiveVol is one of the natural data backbones. For solo traders or small teams where the budget does not stretch, the practical alternative is a tiered stack: [[orats]] or [[optionmetrics]] for analytical depth, [[databento]] or [[polygon-io]] for cheaper [[opra]]-derived pricing, and Cboe DataShop only for the specific historical slices that require canonical data.

## Related

- [[cboe-livevol]] — companion page covering parent-company context, licensing, and procurement detail.
- [[cboe-global-markets]] — the parent exchange operator since the 2015 acquisition.
- [[opra]] — the consolidated US options tape that LiveVol redistributes.
- [[optionmetrics]] — direct competitor on academic and institutional historical options data.
- [[orats]] — value-added analytics layer on similar underlying data, retail-friendlier pricing.
- [[databento]], [[polygon-io]] — lower-cost OPRA redistributors targeting quant developers.
- [[volatility-surface]], [[volatility-skew]] — primary research subjects for which LiveVol is used.
- [[options-premium-selling]] — strategy family that benefits heavily from LiveVol-quality historical chains.
- [[theta-targeting]] — institutional premium-selling discipline that consumes LiveVol portfolio-Greeks tooling.

## Sources

- CBOE Holdings press release, "CBOE Holdings to Acquire Data and Analytics Platforms of Livevol, Inc.", 2 June 2015: https://ir.cboe.com/news-and-events/2015/06-02-2015/cboe-holdings-acquire-data-and-analytics-platforms-livevol-inc
- PR Newswire mirror of the acquisition announcement (lists Livevol Core, Pro, X, and Enterprise): https://www.prnewswire.com/news-releases/cboe-holdings-to-acquire-data-and-analytics-platforms-of-livevol-inc-300092512.html
- Cboe Insights, "Our Origins: LiveVol's Foundation for Cboe Data and Analytics": https://www.cboe.com/insights/posts/our-origins-live-vols-foundation-for-cboe-data-and-analytics/ (founding by a group of options traders; Clay as early user/investor, later CEO)
- S&P Global press release, "S&P Dow Jones Indices Announces Leadership Succession", 2 October 2025: https://press.spglobal.com/2025-10-02-S-P-Dow-Jones-Indices-Announces-Leadership-Succession (Clay named CEO of S&P DJI effective 1 November 2025)
- Cboe DataShop product catalogue: https://datashop.cboe.com
- Verified via Perplexity and web search, 2026-06-10
- See also [[cboe-livevol]] for parent-company context and licensing detail
