---
title: "Market Chameleon"
type: source
created: 2026-05-05
updated: 2026-06-20
status: excellent
tags: [data-provider, options, options-analytics, earnings, volatility, indicators]
aliases: ["MarketChameleon", "MC"]
related: ["[[options-data-sources]]", "[[iv-crush]]", "[[iv-rank-and-iv-percentile]]", "[[earnings-options-strategies]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[unusual-options-activity]]", "[[optionstrat]]", "[[paid-data-providers]]", "[[data-sources-overview]]", "[[variance-risk-premium]]", "[[itpm-playbook]]"]
source_type: data
source_url: "https://marketchameleon.com"
confidence: high
---

Market Chameleon is a web-based [[options]] analytics platform best known for its earnings volatility data, [[iv-crush]] statistics, and [[iv-rank-and-iv-percentile|IV rank]] screeners across the US listed options universe. It is widely used by retail premium sellers, [[itpm-playbook|ITPM-style]] traders, and earnings-focused short-vol operators who need clean, pre-computed historical IV-vs-HV history and post-earnings move statistics without paying institutional rates for [[options-data-sources|OptionMetrics or ORATS]].

## Overview

Market Chameleon (sometimes abbreviated **MC**) provides pre-packaged options analytics through a browser interface. The platform pulls from OPRA-derived options data and layers calculated fields on top: [[implied-volatility]] history, [[realized-volatility|historical volatility]], IV rank and IV percentile, average post-earnings moves, average IV crush percentages, dividend-adjusted greeks, and unusual-options-activity flags. Unlike [[optionstrat]], which is visualization-first, Market Chameleon is screener- and statistics-first: most workflows start with a sortable table and end with a per-ticker drill-down rather than a payoff diagram.

The platform is targeted at active retail and prosumer options traders. It is not a charting platform, not an execution venue, and not an institutional terminal. Its core value proposition is the *earnings volatility report*, which is difficult to assemble manually and not cleanly available elsewhere at retail price points. Within the broader [[data-sources-overview|data-sources catalog]], Market Chameleon occupies the "analytics layer over OPRA" slot — see [[paid-data-providers]] for the raw-feed vendors (Polygon, Databento, OptionMetrics, ORATS) whose data Market Chameleon effectively pre-processes for non-programmer use.

## Feature Reference Matrix

A consolidated view of what the platform exposes, how it is delivered, and which workflow it feeds. (Module availability varies by tier; see [[#Pricing Tiers]].)

| Module | What it delivers | Delivery | Primary workflow |
|---|---|---|---|
| Historical IV vs HV | [[implied-volatility|IV]] and [[realized-volatility|HV]] time series per tenor | Web charts + CSV | [[variance-risk-premium|VRP]] screening |
| IV rank / IV percentile | Universe-wide [[iv-rank-and-iv-percentile|IV rank]] (0-100) | Sortable table + CSV | Premium-selling watchlist |
| Earnings volatility report | Implied move, avg historical move, [[iv-crush|IV crush %]], drift stats | Sortable table + CSV | [[earnings-options-strategies|Earnings trade construction]] |
| Unusual options activity | Volume-vs-OI spikes, sweeps/blocks | Scanner + alerts | [[unusual-options-activity|Flow watching]] |
| Options profit calculator | Multi-leg P&L + greeks + probability-of-profit | Interactive tool | Quick what-ifs |
| Dividend tools | Ex-div calendars, forward dividend schedules | Calendar + table | [[dividend-capture]], short-call early-exercise risk |
| Stock screeners | Technical, gap, PEAD, seasonality screens | Sortable table | Single-name selection |
| Backtest tools (Diamond) | Hypothetical historical performance of simple structures | Interactive | Strategy sanity-check (with [[overfitting-detection|overfitting]] caveats) |

Data egress is via per-screen CSV download on most tiers; there is no full public REST API on lower tiers (see [[#Pricing Tiers]] and [[#Weaknesses]]).

## Core Features

### Historical IV vs HV Charts
- Side-by-side plots of [[implied-volatility|IV30]] (or other tenors) against [[realized-volatility|HV30]] for any underlying
- Visual identification of persistent [[variance-risk-premium|IV-HV spread]] -- a foundational input for short-premium screening
- Historical lookback typically several years on Premium and full history on Diamond (verify current ranges on the site)
- Comparable to ORATS' history charts at a fraction of the price

### IV Rank and IV Percentile Across Underlyings
- IV rank: where current IV sits between its 1-year low and high (0-100)
- IV percentile: percentage of trading days in the last year where IV was below the current level
- Sort the entire optionable universe by either metric to find candidates for premium selling vs premium buying
- Filter by liquidity, sector, market cap, options volume

### Earnings Volatility Report
The headline product. For every upcoming earnings release the platform aggregates:
- **Implied move** -- straddle-derived expected move into the print
- **Average historical move** -- realized move across the last N earnings
- **Average IV crush** -- typical % drop in front-month IV from pre- to post-print
- **Beat/miss/in-line frequencies** -- how often the underlying gapped up, down, or stayed within the implied move
- **Post-earnings drift statistics** -- whether the stock continues, mean-reverts, or chops in the days following
- **Sortable across the universe** -- find the highest IV crush, smallest average move, or biggest implied-vs-realized gap before the print

This dataset is invaluable for [[earnings-options-strategies|earnings-week trade construction]]. Manually computing it requires a clean options-history vendor plus careful corporate-action handling -- exactly what Market Chameleon does for you.

### Unusual Options Activity Scanner
- Flags large block prints, volume-vs-open-interest spikes, and out-of-the-ordinary tenor activity
- Filters by sweep vs block, call vs put, premium size
- Same caveat as every retail flow tool: trades are not signed and attribution to "smart money" is inferential ([[unusual-options-activity]])

### Options Profit Calculator and Strategy Tools
- Multi-leg P&L calculators with greeks
- Probability-of-profit estimates from the IV surface
- Less polished than [[optionstrat]] for visualization but adequate for quick what-ifs while screening

### Dividend Impact Tools
- Forward dividend schedules used for IV calculation
- Ex-dividend calendars cross-referenced with options chains
- Specifically useful for early-exercise risk on short ITM calls and for [[dividend-capture]] screens

### Stock Screeners and Indicators
- Beyond options: technical screeners, gap statistics, post-earnings-announcement-drift screens, seasonality tables
- Useful as a single workbench when you do not want to bounce between three platforms

## Earnings Volatility Report -- Why It Matters

For ITPM-style earnings trades, the operating question is: *is the implied move priced into the front-month straddle larger or smaller than what this name historically does?*

Market Chameleon answers that directly. For each ticker on a given earnings date you see:

| Field | Use |
|-------|-----|
| Implied straddle move | What the market is pricing in |
| Average historical move (last 12 prints) | What the stock typically does |
| Max historical move | Tail size |
| Average IV crush % | How much the front month deflates after print |
| Win rate of long straddle | Historical hit rate of the simplest long-vol play |
| Win rate of short straddle | Historical hit rate of the simplest short-vol play |

A name where the implied move is consistently larger than the historical move, with a high IV crush %, is a structural short-vol candidate. A name where the implied move is consistently smaller than the realized move is a structural long-vol candidate. The platform sorts the entire earnings calendar by these properties.

This is the exact dataset that supports the classic [[short-strangle]] / [[iron-condor]] / [[earnings-options-strategies|earnings short-strangle]] playbook. Doing it without Market Chameleon means reconstructing the table by hand from raw chains -- weeks of work for a result the platform serves in one click.

## IV Rank Screener

The IV rank screener is the second pillar workflow. Typical use:

1. Sort universe by IV rank descending
2. Filter for IV rank > 50 (often > 70)
3. Filter for adequate options liquidity (open interest, volume, bid-ask)
4. Filter for sector, optionable ETF vs single name, market cap
5. Drill into each candidate, look at the IV vs HV chart, and decide whether to deploy a short-premium structure

This is the standard short-vol watchlist construction process and is exactly what tastytrade-style and [[itpm-playbook|ITPM]] approaches teach. Market Chameleon makes the screen one query rather than a manual scrape.

## Pricing Tiers

*The numbers below reflect commonly-cited 2024-2025 pricing; pricing may have changed -- confirm on [marketchameleon.com](https://marketchameleon.com).*

### Free
- Basic stock and ETF data, delayed quotes
- Limited options snapshots
- Useful for spot-checking a single name; insufficient for systematic screening

### Premium (~$59/month, as of 2025 -- verify current)
- Full options analytics
- Historical IV vs HV charts
- Earnings volatility report
- IV rank and IV percentile screener
- Most retail use cases sit here

### Diamond (~$99/month, as of 2025 -- verify current)
- Everything in Premium
- Deeper historical lookback
- Full scanners, alerts
- Backtest tools and stock-and-options ratings
- Aimed at active traders running daily screens

### Annual Discounts
Annual plans typically offer ~15-20% off monthly rates. Check the site for current promotions.

There is no public API on lower tiers; data export is via CSV download from individual screens. Higher tiers may include limited API access -- confirm current capabilities on the site.

## How ITPM-Style Traders Use It

The [[itpm-playbook|ITPM]] approach to earnings is heavily statistics-driven: select underlyings where historical post-earnings behavior matches the structure being deployed, ignore the rest. Market Chameleon is a near-perfect tool for that selection.

### Pre-Earnings Workflow
1. Pull the upcoming earnings calendar for the next 1-2 weeks
2. Filter for liquid optionable names (open interest, tight spreads)
3. Sort by **average IV crush %** descending -- biggest deflation candidates first
4. Within those, filter for **small average historical move** relative to the **implied straddle move** -- short-vol edge
5. Avoid names with a history of large gaps in either direction (high tail risk)
6. Construct [[short-strangle|strangles]] or [[iron-condors|condors]] outside the historical move range
7. Size positions so a 2x historical move move is survivable

### Post-Earnings Workflow
1. Use the post-earnings drift statistics to decide whether to fade the move (mean-reversion candidates) or join it (drift candidates)
2. Avoid names that historically gap and continue -- those eat short-vol structures even after the IV crush has paid

### Watchlist Construction
1. Daily run: sort universe by IV rank > 50, options volume > threshold, market cap > threshold
2. Save to watchlist
3. Re-screen weekly; add new entrants, remove names that have already deflated

### Variance-Risk-Premium Estimation
1. For each name, compute the average IV30 - HV30 spread over the past year
2. Names with a persistently positive spread are structural short-vol candidates
3. Sort the universe and watch the top decile
4. This is the [[variance-risk-premium]] in practical screener form

## How Trading and AI Systems Consume It

Market Chameleon is fundamentally a *human workbench*, not an automation feed, and that shapes how it fits into a systematic or [[ai-trading|AI-driven]] stack:

- **As a research/feature source, not a live feed.** The pre-computed earnings-vol table and IV-rank screen are excellent inputs for *building* a watchlist or labeling a training set, but with no real API on lower tiers, ingestion is CSV-export-and-parse, not a streaming pipeline. For programmatic, latency-sensitive options data, go to the raw vendors in [[paid-data-providers]] (Polygon, Databento OPRA) or [[options-data-sources]].
- **As a labeling layer for earnings models.** The historical implied-move, realized-move, [[iv-crush|IV-crush]], and post-earnings-drift fields are exactly the supervised-learning labels an earnings-vol model needs. Exporting the earnings calendar with these columns gives a clean, dividend-aware dataset that would otherwise require reconstructing IV from raw chains.
- **As a sanity-check oracle.** Even a fully automated pipeline benefits from cross-checking its own computed IV rank / VRP against Market Chameleon's numbers; divergences flag bugs in the in-house [[implied-volatility|Black-Scholes]] inversion or corporate-action handling.
- **Where it stops.** No fitted [[volatility-smile|vol surface]], no intraday tick history, no execution. Systems doing dispersion, vol-arb, or HFT need ORATS / OptionMetrics / direct OPRA instead (see comparison table below).

### Data-Quality Caveats

Same disciplines apply as for any [[paid-data-providers|paid vendor]]:

- **Pre-computed ≠ authoritative.** IV/HV and crush figures are the platform's calculations, not raw OPRA; corner cases (illiquid strikes, post-split contracts, near-expiry options) can read stale or off. Cross-check before sizing up.
- **End-of-day bias.** Most fields are EOD/snapshot. Intraday IV moves and same-day flow nuance are not captured at full fidelity.
- **Survivorship in earnings history.** Historical earnings-move stats are computed on names that still exist; delisted/acquired names drop out, mildly biasing "average historical move" samples. Treat the earnings backtest tool with the usual [[overfitting-detection|backtest-overfitting]] and [[survivorship-bias]] caution.
- **US-listed only.** No European, Asian, or futures-options coverage.

## Strengths

- **Earnings-specific data not easily found elsewhere** -- the IV crush + historical move + drift bundle is the platform's killer feature
- **Reasonable price point** -- a Premium subscription costs less than 1% of an OptionMetrics seat and serves most retail use cases
- **Web UI usable without an API** -- non-programmers can drive the workflow
- **Pre-computed historical IV/HV** -- saves the user from reimplementing dividend-aware [[implied-volatility|Black-Scholes]] inversion
- **Single workbench** -- combines screeners, calendars, earnings, dividends, and basic strategy tools in one site
- **Active product development** -- the platform has been continuously updated since founding

## Weaknesses

- **No real API on lower tiers** -- automation is limited; CSV export is the main data egress
- **Limited intraday data** -- mostly end-of-day and snapshot-based; not for HFT or short-horizon work
- **Not a charting or execution platform** -- you still need TradingView or your broker's frontend for entry
- **Data quality occasionally lags vs OPRA direct** -- corner cases (illiquid strikes, early-expiry options, post-split contracts) sometimes show stale or off readings; cross-check before sizing up
- **Visualization is utilitarian** -- payoff diagrams are functional but less polished than [[optionstrat]]
- **No options surface fitting / vol arb tooling** -- if you need fitted [[volatility-smile|smiles]] and term structures, ORATS is a better fit
- **US-listed only** -- no meaningful coverage of European, Asian, or futures-options markets

## Comparable Tools

| Tool | Positioning vs Market Chameleon |
|------|--------------------------------|
| **ORATS** | More institutional; fitted surfaces, intraday IVs, API-first; ~$200-1000/mo |
| **[[optionstrat]]** | Visualization-first; better for sharing trade ideas; weaker on historical statistics |
| **OptionMetrics IvyDB** | Academic gold standard; expensive; daily-only; no UI to speak of |
| **CBOE LiveVol** | Authoritative for CBOE products; institutional pricing |
| **Volatility.AI** | Newer entrant; ML-flavored vol forecasting; smaller dataset |
| **Tastytrade research tab** | Free with brokerage; good IV rank, weaker on earnings statistics |
| **OptionsPlay** | Idea-generator focused; less depth on historical IV |
| **IVolatility.com** | Older peer; broadly similar features; quality varies |
| **Barchart Premier** | Wider coverage including futures and FX; less options-specific depth |

For most retail premium sellers, the practical comparison is **Market Chameleon vs Tastytrade research tab vs ORATS**. Tastytrade is free if you have an account but lighter on historical statistics. ORATS is more powerful but several times the price. Market Chameleon sits in the productive middle.

## Use Cases for ITPM-Style Workflows

- **Earnings calendar prep** -- weekly review of upcoming prints, sorted by IV crush and historical move profile, to build that week's short-vol candidate list
- **IV rank screening** -- daily sort by IV rank > 50 with liquidity filters to maintain a short-premium watchlist
- **Post-earnings drift studies** -- check whether names continue to gap or mean-revert in the days after a print, before structuring drift trades
- **Variance risk premium estimation** -- compute IV-HV spreads over a 1-year window per name to identify structural short-vol candidates ([[variance-risk-premium]])
- **Dividend-aware short-call screening** -- combine ex-div calendar with short-call screens to avoid early-exercise pitfalls
- **Sector vol comparison** -- pull IV ranks across a sector to find the cheapest and richest names relative to peers
- **Backtesting earnings strategies** -- the platform's earnings backtest tool (Diamond) lets you sanity-check historical hypothetical performance of simple structures, with all the usual [[overfitting-detection|backtest-overfitting]] caveats
- **Pre-trade sizing** -- use historical move statistics to set position size such that a 2x historical move is survivable

## Sources

- [marketchameleon.com](https://marketchameleon.com) -- product documentation and feature pages, as of 2025
- General community usage in r/options, tastytrade forums, and ITPM/short-premium trading communities
- Cross-references with [[options-data-sources]] and [[paid-data-providers]] for context on competing platforms and the raw data vendors underneath

## Related

- [[options-data-sources]] -- broader catalog of options data providers
- [[paid-data-providers]] -- raw-feed vendors (Polygon, Databento, OptionMetrics, ORATS) underneath the analytics layer
- [[data-sources-overview]] -- full data-sources catalog
- [[iv-crush]] -- the headline phenomenon Market Chameleon quantifies
- [[iv-rank-and-iv-percentile]] -- the screener metric the platform exposes universe-wide
- [[earnings-options-strategies]] -- the strategy family the platform is built to support
- [[implied-volatility]] -- pre-computed across the universe by Market Chameleon
- [[realized-volatility]] -- the HV side of the IV-vs-HV charts
- [[unusual-options-activity]] -- a scanner module on the platform
- [[optionstrat]] -- complementary visualization-first tool
- [[short-strangle]] -- the structure most often deployed off the platform's screens
- [[iron-condors]] -- defined-risk variant for the same workflow
- [[variance-risk-premium]] -- the underlying edge that the IV-HV gap measures
- [[itpm-playbook]] -- methodology that this platform supports closely
