---
title: "tastytrade Platform (Tastyworks)"
type: entity
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, company, education, futures]
entity_type: company
founded: 2017
headquarters: "Chicago, IL, USA"
website: "https://tastytrade.com"
aliases: ["Tastytrade Platform", "Tastyworks", "tastyworks", "tastytrade desktop"]
related:
  - "[[ig-group]]"
  - "[[thinkorswim]]"
  - "[[optionnet-explorer]]"
  - "[[options-premium-selling]]"
  - "[[probability-of-profit]]"
  - "[[options-greeks]]"
  - "[[theta-targeting]]"
  - "[[vega-budgeting]]"
  - "[[options-buying-power-reduction]]"
  - "[[short-strangle]]"
  - "[[iron-condor]]"
  - "[[delta]]"
  - "[[theta]]"
  - "[[implied-volatility]]"
---

The tastytrade platform is the order-entry, charting, and analytics software published by the tastytrade brokerage (formerly tastyworks), distinct from the tastytrade media network and the parent legal entity. It exists in three coordinated clients — a Windows/Mac **desktop** application, a **web platform** at tastytrade.com, and **iOS/Android mobile** apps — all sharing a single account and order book. The platform is purpose-built for [[options-premium-selling|options-premium sellers]] and exposes a distinct vocabulary of features built around that worldview: the Trade tab, Curve mode, [[probability-of-profit|Probability of Profit]] (POP), real-time theta/day, the Follow feed and copy-trade, [[options-buying-power-reduction|buying-power reduction]] previews, and a one-click Quick Roll function. The brokerage business behind the platform was sold by Tom Sosnoff and Scott Sheridan to [[ig-group|IG Group]] in **2021 for approximately $1 billion**.

## Overview

The platform launched as **tastyworks** in early 2017 to give viewers of the tastytrade media network a place to execute the trades being discussed on air. The split branding (tastyworks the broker, tastytrade the network) persisted for several years; following the 2021 IG Group acquisition the brand was unified and the broker was renamed **tastytrade** in 2022, with the media network retaining "tastylive" branding in some contexts.

Where most retail platforms are built around a watchlist and chart with options bolted on, the tastytrade platform inverts that — the **options chain is the central UI element**, with stock charting, watchlists, and account views arranged around it. Every order-entry interaction shows the [[options-greeks|Greeks]], [[probability-of-profit|POP]], theta-per-day, and [[options-buying-power-reduction|buying-power reduction]] (BPR) live, before the order is sent. This bias is editorial as much as technical: the platform is opinionated software for premium sellers, in the same way tastytrade's curriculum is opinionated.

The three clients are tightly aligned. The **desktop** is the most feature-complete (preferred by full-time traders); the **web** platform covers ~90% of desktop functionality without an install; the **mobile app** handles trade entry, position management, and Quick Roll but defers complex multi-leg construction to desktop or web.

| Client | Coverage | Best for | Multi-leg construction |
|--------|----------|----------|------------------------|
| **Desktop** (Win/Mac) | Full feature set | Full-time traders, complex books | Full |
| **Web** (tastytrade.com) | ~90% of desktop, no install | Most day-to-day use from a browser | Full |
| **Mobile** (iOS/Android) | Entry, management, Quick Roll | On-the-go position management | Limited (defers to desktop/web) |

## Key Features / Capabilities

The table summarizes the platform's signature features; each is detailed below.

| Feature | What it surfaces | Why it matters to a premium seller | Related |
|---------|------------------|-----------------------------------|---------|
| Trade tab | Chain with strike-by-strike Greeks, credit, [[probability-of-profit\|POP]], [[options-buying-power-reduction\|BPR]] | The single options-native workspace | [[short-strangle]], [[iron-condor]] |
| Curve mode | Expiry + T+0 P&L curve, break-evens | Visual sanity check before submit | [[optionnet-explorer]] (richer grid) |
| Theta/day widget | Portfolio aggregate [[theta]] per day in dollars | Canonical [[theta-targeting]] number | [[vega-budgeting]] |
| Beta-weighted delta | Whole-book [[delta]] beta-weighted to SPY | One equity-equivalent risk number | [[delta]] |
| IV rank / percentile | Per-chain [[implied-volatility]] regime | Trade-selection filter (≥ 50 default) | [[iv-rank-and-iv-percentile]] |
| Quick Roll | One-click roll to next cycle, pre-filled combo | Expresses *manage at 50% / 21 DTE* | tastytrade research |
| Follow / copy-trade | Live trades of on-air researchers | Social learning + auto-replication | — |
| Strategy presets | One-click 16-delta strangle, 30-delta vertical, etc. | Speed of construction | [[short-strangle]] |

### The Trade tab

The default workspace. A live options chain with strike-by-strike bid/ask, IV per strike, delta, theta, vega, and open interest. Clicking strikes adds them to the order ticket; the ticket dynamically labels the structure (vertical, condor, strangle, butterfly, calendar, diagonal) as it is built. The order ticket displays in real time:

- **Net credit / debit**
- **Probability of Profit ([[probability-of-profit|POP]])** — calculated from the lognormal model conditioned on current IV. The single most visible metric on the order ticket; tastytrade's editorial line is that 70%+ POP setups are the default.
- **Probability of Touch** — chance the underlying touches a short strike before expiration.
- **[[options-buying-power-reduction|Buying-power reduction]] (BPR)** — collateral the trade will tie up. For undefined-risk trades like [[short-strangle|short strangles]], this is the Reg-T or portfolio-margin requirement. For defined-risk trades, it is the max loss.
- **Greeks at trade level** — delta, theta, vega, gamma summed across the legs.
- **Max profit / max loss / break-evens**.

### Curve mode

A graphical view of the structure's P&L curve at expiration plus a "T+0" (today) curve, with strike levels and break-evens marked. Curve mode is the platform's answer to the time-and-price grid in [[optionnet-explorer]]; it is simpler (price axis only, no calendar axis), which is sufficient for the single-expiry structures (verticals, condors, strangles, butterflies) that dominate the tastytrade trader's book. Multi-expiry structures (calendars, diagonals) get a partial curve view but no full 2D grid.

### Theta/day display

A persistent platform widget showing **portfolio aggregate theta per day** in dollar terms. It is calculated across all open options positions and is the canonical reference number for tastytrade-influenced [[theta-targeting|theta-targeted]] traders — *"my theta/day is $87 today"* is a sentence the platform makes natural. Aggregate vega, delta (beta-weighted to SPY by default), and gamma are displayed alongside.

### Follow feed and copy-trade

A social layer where users — typically tastytrade on-air personalities, the "Trade Hub" researchers, and a curated cast of public traders — share their live trades in real time. Other users can:

- **Follow** a trader to see their trades in a feed.
- **Copy-trade** a "follow" — replicate the trader's structures automatically into your own account, scaled to your capital. The copy-trade feature is unusual among US brokers and is one of the platform's distinguishing capabilities.

The follow feed surfaces real positions, real fills, and real P&L (with the trader's permission), giving newer users a structured way to see how experienced traders construct and manage trades.

### Quick Roll

A one-click roll button on any open option position. The platform automatically suggests the same strike rolled to the next expiry cycle (or a user-selected target expiry), pre-fills the closing-and-opening combo order, and shows the net credit/debit and updated Greeks for the new position. This is the canonical mechanic for the tastytrade research convention of *managing winners at 50% / managing at 21 DTE* — Quick Roll is the platform expression of that workflow.

### Other notable features

- **Beta-weighted portfolio delta** — the entire book's delta beta-weighted to SPY (or a user-selected benchmark) for a single equity-equivalent risk number.
- **Real-time IV rank and IV percentile** — displayed on every chain header, the canonical filter for tastytrade-style trade selection.
- **One-click strategy presets** — single-click setup of common structures (16-delta strangle, 30-delta vertical, etc.) at user-defined defaults.
- **Active Trader / TT Mobile** — streamlined mobile app for managing existing positions on the go; full chain construction is desktop/web.
- **Crypto** — has been added and removed at various points; as of June 2026 cryptocurrency trading is offered alongside stocks, options, futures, and forex.
- **Portfolio margin** — available to qualifying accounts; meaningfully reduces BPR for defined-risk and well-hedged books.

## Pricing & Access

The platform itself is **free** to use for tastytrade brokerage clients. The cost structure is in the brokerage commissions (verified June 2026):

- **Equity options**: $1.00 per contract to open, **$0 to close**, capped at **$10 per leg**. The asymmetric "close-for-free" pricing is favourable for premium sellers who close at 50% profit.
- **Index options**: tiered, often $1.25 per contract with similar close-for-free treatment on most index products.
- **Futures and futures options**: separate per-contract schedules.
- **Stocks/ETFs**: $0 commission.
- **Account minimum**: **$0** for cash accounts; margin and portfolio margin have equity floors. No annual or inactivity fees.
- **No subscription fee** for the platform; data fees on real-time non-display use are a separate matter.
- **Asset coverage** (2026): stocks, ETFs, options, futures, futures options, cryptocurrencies, and US Treasurys; accounts carry SIPC coverage up to $500,000 (including $250,000 for cash).

The platform is **brokerage-tied** — to use it you must have a tastytrade brokerage account; it is not available standalone like [[optionnet-explorer]] or orats.

## Automation and Integrations

The tastytrade platform is more open to programmatic access than most options-native retail brokers:

- **Developer API** — tastytrade exposes an API for account, market-data, and order operations, enabling external systems to place and manage trades programmatically (subject to the broker's terms and entitlements). This makes it a common target for [[trading-automation|automated]] options workflows.
- **Native copy-trade** — the Follow feed's copy-trade replicates another trader's structures into your account automatically, scaled to your capital — an in-platform automation that most US brokers do not offer.
- **Webhook bridges** — signal sources (e.g. [[tradingview-platform|TradingView]] alerts) can be routed to tastytrade execution through automation layers such as [[traderspost]] or [[trade-automation-toolbox]] where supported, for traders who prefer external signal generation.
- **Third-party analytics pairing** — for capabilities the platform lacks natively, traders pair it with orats (data and backtesting) or [[optionnet-explorer]] (time-and-price P&L grid and historical replay).

A representative systematic pattern: generate or screen ideas externally (or via the API), construct and risk-check in the Trade tab / Curve mode, then place and manage — using Quick Roll and the theta/day widget — within the platform, optionally with execution automated through the API or a webhook bridge. See [[webhook-trading]] and [[trading-automation]] for the general architecture.

## Status and Developments (2025-2026)

- The platform remains active and under continuous development as IG Group's US brokerage arm; tastytrade continued collecting industry awards through 2025, including Benzinga's "Best for Low-Cost Micro Futures in 2025".
- Crypto trading is currently offered alongside stocks, options, futures, and forex (after earlier add/remove cycles), and **US Treasurys** were added to the product set.
- In 2026 tastytrade ran an aggressive customer-acquisition promotion — a "Double Your Commission Rebate" campaign (started 7 April 2026, extended through 30 June 2026) rebating stock-option and ETF-option commissions up to a **$3,000** cap for 30 days after a qualified deposit — a signal of intensified competition for active options traders among retail brokers.

## Strengths & Weaknesses

**Strengths:**

- **Options-native UI** — the chain-centric workspace is genuinely faster for multi-leg trade construction than [[thinkorswim]] or TWS.
- **POP and BPR on every order** — sets the cognitive frame for premium sellers.
- **Aggregate theta/day** — a built-in feature that costs extra or requires custom dashboards on most other platforms.
- **Quick Roll** — the canonical premium-seller management mechanic, one click.
- **Cost structure** — close-for-free pricing aligns with the 50% profit-take rule and removes a friction in active management.
- **Education integration** — the tastytrade media network and the platform speak the same vocabulary; on-air discussion translates directly to the order ticket.
- **Follow / copy-trade** — unusual social layer that meaningfully helps newer traders.
- **Web parity with desktop** — most users can work from a browser without losing functionality.

**Weaknesses:**

- **Editorial bias** — the entire platform assumes you are selling premium. Directional traders and option buyers find less affordance in the UI.
- **Limited charting** — the chart is functional but not a [[tradingview-platform|TradingView]] replacement; serious technical analysts often pair tastytrade with an external chart.
- **No backtester** — there is no equivalent of [[optionnet-explorer]]'s historical replay or orats' Backtests Generator built into the platform.
- **No time-and-price P&L grid** — Curve mode is single-expiry-friendly; serious calendar/diagonal traders still need [[optionnet-explorer]] or similar.
- **Narrow product breadth** — international markets, mutual funds, and bonds are weak or absent compared with interactive-brokers.
- **Customer service / reliability complaints during high-vol events** — periodic outages and slow support are a recurring complaint, common to many retail options brokers.
- **Payment for order flow** — a meaningful revenue line on options, which some traders view as a conflict of interest.
- **Brokerage-tied** — no standalone version; you must open an account to use the platform.

## How Practitioners Use It

A representative discretionary [[options-premium-selling|premium-seller]] workflow:

1. **Filter the universe.** Open the watchlist sorted by IV rank descending; pick names with IV rank ≥ 50 and no upcoming earnings within the next 14 days.
2. **Construct the trade.** In the Trade tab, click the 16-delta short strikes for a 45-DTE [[short-strangle|short strangle]] (or the equivalent [[iron-condor]] for defined risk). The order ticket auto-labels it, computes credit, POP (~70%+), Greeks, and BPR.
3. **Curve check.** Switch to Curve mode to confirm the P&L profile matches expectation; check break-evens against support/resistance on a chart.
4. **Aggregate sanity check.** Glance at the platform's theta/day and beta-weighted delta widgets to confirm the new trade keeps the book within [[theta-targeting|theta target]] and [[vega-budgeting|vega budget]].
5. **Submit.** Place the order; tastytrade's order router executes the multi-leg combo at the natural price or a working limit.
6. **Monitor.** The position appears in the Positions tab with live Greeks, P&L, and percent-of-credit captured. The platform highlights when 50% profit is reached.
7. **Manage.** At 50% profit or 21 DTE, click Quick Roll (to extend the trade) or close. Quick Roll pre-builds the closing-and-opening combo at one click.
8. **Daily portfolio review.** Aggregate theta/day, vega, and beta-weighted delta on the Positions tab serve as the morning health-check. Numbers feed directly into the mental [[theta-targeting]] model.
9. **Optional: follow / copy-trade.** Learners follow on-air researchers' live trades to see real management decisions in real time. Copy-trade pipes those trades automatically into the user's own account at chosen sizes.

For a discretionary income trader within the tastytrade worldview, the platform is the **single workspace** — broker, analytics, education, and social all in one. Traders who need richer historical backtests usually pair it with orats; traders who need richer time-and-price portfolio analysis usually pair it with [[optionnet-explorer]]; traders running a more diversified book often pair it with interactive-brokers for the products tastytrade does not cover.

## Related

- [[ig-group]] — current parent company since the 2021 acquisition.
- [[thinkorswim]] — the platform Tom Sosnoff and Scott Sheridan built first, sold to TD Ameritrade in 2009; the conceptual ancestor of tastytrade.
- [[optionnet-explorer]] — third-party options analytics with a richer time-and-price grid and historical simulator.
- [[traderspost]], [[trade-automation-toolbox]] — webhook automation bridges for routing external signals to execution.
- [[trading-automation]], [[webhook-trading]] — general architecture for automated options execution.
- [[options-premium-selling]] — the strategy class the platform is built around.
- [[probability-of-profit]] — the platform's signature metric.
- [[options-buying-power-reduction]] — collateral preview shown on every order.
- [[theta-targeting]] — discipline that consumes the platform's aggregate theta/day display.
- [[vega-budgeting]] — companion discipline.
- [[short-strangle]], [[iron-condor]] — canonical structures the platform optimises for.
- [[options-greeks]], [[delta]], [[theta]], [[implied-volatility]] — the analytical primitives surfaced throughout.

## Sources

- tastytrade platform documentation and product pages — https://tastytrade.com and https://tastytrade.com/about-us/
- tastytrade "Double Your Commission Rebate" promotion terms (2026) — https://tastytrade.com/double/
- tastytrade newsroom and awards — https://tastytrade.com/newsroom/awards/
- IG Group 2021 acquisition announcement and subsequent integration disclosures (~$1B deal).
- NerdWallet tastytrade review (commission schedule: $1 to open / $0 to close, $10/leg cap, $0 minimum) — https://www.nerdwallet.com/investing/reviews/tastytrade
- tastytrade media network on-air segments demonstrating platform features.
- Retail trader reviews and broker comparison reports (NerdWallet, Investopedia broker reviews, BrokerChooser).
- Commission schedule, promotion details, and active status verified via Perplexity (sonar, high search context), 2026-06-10.
