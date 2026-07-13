---
title: "Deribit Position Builder"
type: entity
created: 2026-05-07
updated: 2026-06-10
status: good
tags: [crypto, options, derivatives, risk-management, company]
entity_type: company
website: "https://pb.deribit.com"
aliases: ["Deribit Position Builder", "Deribit PB"]
related:
  - "[[deribit]]"
  - "[[crypto-options]]"
  - "[[bitcoin-options]]"
  - "[[ethereum-options]]"
  - "[[laevitas]]"
  - "[[paradigm]]"
  - "[[portfolio-greeks-aggregation]]"
  - "[[theta-targeting]]"
  - "[[vega-budgeting]]"
  - "[[options-premium-selling]]"
  - "[[implied-volatility]]"
  - "[[options-greeks]]"
  - "[[short-strangle]]"
  - "[[iron-condor]]"
---

The Deribit Position Builder is the free web-based options analytics tool published by [[deribit|Deribit]], the dominant exchange for crypto options. It lets traders construct hypothetical or real options portfolios in BTC, ETH, and SOL, aggregate the [[options-greeks|Greeks]] across all positions, and visualise P&L under arbitrary spot, IV, and time scenarios. Because Deribit clears roughly **80–90% of global crypto-options volume** and runs the canonical BTC and ETH IV indices (DVOL), the Position Builder is — in practice — the default portfolio-analytics tool for the entire crypto-options community, in much the same way [[tastytrade-platform|tastytrade]]'s curve view is for retail equity options.

## Overview

Deribit launched in 2016 as a Netherlands-based exchange specialising in BTC futures and options; ETH options followed, and SOL options in 2024. The exchange's options orderbook has been the deepest in crypto since at least 2018, and as of 2024–2026 Deribit consistently accounts for ~85% of global BTC and ETH options open interest, with the remainder split across CME (institutional, larger contract size, much smaller OI), [[okx]], [[bybit]], and a handful of DeFi options protocols.

### Coinbase acquisition (2025)

On **8 May 2025**, [[coinbase|Coinbase]] announced it would acquire Deribit for approximately **$2.9 billion** — about $700 million in cash plus 11 million Coinbase Class A shares — making Coinbase the most comprehensive global crypto-derivatives platform. At announcement, Coinbase cited roughly **$30 billion of open interest** on Deribit and over $1 trillion in cumulative annual trading volume; contemporaneous analyses put Deribit's share at **87%+ of BTC options and ~94% of ETH options**. The deal has since been reported completed, with Deribit continuing to operate its exchange and tooling (including the Position Builder at `pb.deribit.com`) under Coinbase ownership as of June 2026. For traders the practical takeaways are: (a) the Position Builder and Deribit's public API remain free and live; (b) the DVOL indices and Deribit IV surface remain the de facto crypto-vol reference; and (c) venue/counterparty risk now rolls up to a US-listed public company ([[coinbase|COIN]]), which changed the institutional-acceptability calculus for many desks.

The Position Builder (URL: `pb.deribit.com`) is hosted as a separate web property from the main exchange. It is **free** to use, requires no Deribit account login (though logged-in users get account-position auto-import), and runs entirely client-side after initial chain data loads. Its existence is one of the reasons Deribit's gravitational pull on the crypto-options ecosystem is so strong: traders price up trades on Deribit's tool, decide structures using Deribit's IV surface, and then — naturally — execute on Deribit.

## Key Features / Capabilities

- **Multi-leg position construction** — build any combination of BTC, ETH, SOL options and futures positions interactively. Enter strikes, expiries, and quantities or click directly on the live chain to add legs.
- **Auto-import live account positions** — logged-in Deribit users can pull their actual portfolio into the Position Builder with one click, getting instant aggregate-Greeks and P&L visualisation on the real book.
- **Aggregate [[portfolio-greeks-aggregation|portfolio Greeks]]** — delta (in BTC/ETH/SOL terms and USD terms), gamma, vega, theta across all loaded positions. Greeks are computed using Deribit's own pricing model and the live IV surface.
- **P&L visualiser** — graph of portfolio P&L vs spot price at user-selectable future dates and IV levels. Multiple curves can be overlaid (e.g. P&L today, P&L at expiry, P&L in 7 days).
- **What-if scenarios** — adjust IV (parallel shift in vol), spot, and time-to-expiration sliders to instantaneously see how the book responds. Crucial for crypto where overnight vol moves of 5–10 IV points are routine.
- **Margin / collateral preview** — estimates portfolio margin requirements under Deribit's cross-margin and portfolio-margin (PM) regimes, helping traders size structures within available collateral.
- **Implied-vol surface display** — Deribit's calibrated surface across strikes and expiries; useful as a cross-check on third-party tools like [[laevitas]] or [[amberdata]].
- **DVOL overlay** — Deribit's BTC and ETH volatility indices (analogous to VIX) are displayed alongside the surface, giving regime context.
- **Save and share scenarios** — saved layouts can be reloaded later; shareable URLs encode a position layout for community discussion.
- **Free, no subscription** — all features are available without paying anything; revenue accrues to Deribit indirectly through the orderflow it captures.

## Pricing & Access

- **Free** — no subscription, no paywall, no ads. Available at `pb.deribit.com`.
- **No account required** for basic use; logged-in Deribit account holders unlock auto-import of live positions and margin previews keyed to their actual collateral.
- **Web-based, runs in any modern browser**; no install. Mobile browsers work but the dense layout favours desktop.
- **API access** to the underlying chain and Greeks data is provided via Deribit's public API (also free, with rate limits). Many third-party crypto-options dashboards (including [[laevitas]] and [[paradigm]]) consume the same feed.

There is no paid tier. Deribit makes its money on options trading commissions and futures funding spreads; the Position Builder is a tool to attract and retain options flow.

## Strengths & Weaknesses

**Strengths:**

- **Free** — uniquely so among options analytics of comparable depth in any asset class.
- **Canonical for crypto** — uses Deribit's own surface and pricing, which is the de facto reference for BTC and ETH options.
- **Live position auto-import** — a feature most retail equity-options analytics charge for or do not offer at all.
- **Multi-asset Greeks** — handles BTC, ETH, SOL, and futures legs in a single book, including cross-asset spreads (e.g. BTC vs ETH vol pairs).
- **DVOL context** — the volatility-index overlay gives instant regime framing.
- **Fast** — client-side rendering after data load means scenario sliders respond instantly.
- **Open API** — the Deribit data feed under it is freely accessible for power users who want to build their own tools.

**Weaknesses:**

- **Deribit-only** — does not aggregate positions from CME, [[okx]], or DeFi protocols. Traders running cross-venue books must combine views manually or use [[laevitas]] / custom tooling.
- **No backtester** — the tool is for current-portfolio analysis and forward what-if; there is no historical replay or strategy backtest.
- **No alerts or automation** — purely an analytical viewer; trading decisions and order placement happen back on the exchange.
- **Surface is Deribit's** — competing pricing models or surfaces cannot be plugged in.
- **Crypto-only** — equity, futures, and FX options traders gain nothing here.
- **UI is dense** — the layout assumes familiarity with options Greeks and crypto-options conventions (BTC delta vs USD delta, etc.); not a beginner tool.
- **Web property, not in-exchange** — context-switches required between `pb.deribit.com` and the main `app.deribit.com` order-entry interface.

## How Practitioners Use It

A typical crypto-options-trader workflow:

1. **Plan a new structure.** A trader wanting to sell a 30-DTE 1-month [[short-strangle|short strangle]] on BTC opens the Position Builder, clicks the relevant strikes on the chain, and enters the size. The tool immediately shows aggregate Greeks: delta in BTC and USD, theta per day in USD, vega per IV point in USD.
2. **Stress-test the structure.** Move the spot slider ±10% and the IV slider ±15 points to see the worst-case P&L. Crypto IV moves are larger and faster than equity IV moves, so this stress-test is more important than its equity-options analogue.
3. **Combine with existing positions.** Auto-import the existing book; ONE-style aggregate views of the combined book reveal whether the new strangle adds or offsets vega and gamma. Crypto-options traders frequently run multi-expiry, multi-strike books where naive position-by-position views miss the netting.
4. **Check margin headroom.** The margin preview confirms the new position fits within available collateral under Deribit's portfolio-margin regime — important because crypto-options margin can swing materially with spot moves.
5. **Execute on the main Deribit platform.** Position Builder is read-only / planning; orders are placed in `app.deribit.com` or via API.
6. **Daily monitoring.** Re-auto-import the live book once a day (or after each adjustment); review aggregate Greeks against [[theta-targeting|theta targets]] and [[vega-budgeting|vega budgets]]. For a [[options-premium-selling|premium-selling]] book, the Position Builder is the single source of truth for portfolio Greeks.
7. **Cross-check with third-party tools.** Sophisticated traders compare the Position Builder's surface and Greeks with [[laevitas]] or in-house models to detect calibration drift; in practice the differences are small for the active part of the surface.

For institutional crypto-options desks, the Position Builder is usually used **alongside** in-house tooling rather than as a substitute — but even desks with full quant infrastructure use it for quick checks because it is the fastest way to see what Deribit's own surface implies. For retail and small-shop crypto-options traders, it is functionally **the** portfolio analytics tool, full stop.

## Why Crypto-Options Traders Use It Specifically

Three structural reasons make the Position Builder dominant in crypto in a way no equivalent tool dominates equity options:

1. **Deribit's flow concentration.** When a single venue clears ~85% of global BTC and ETH options volume, the venue's own pricing model becomes the de facto reference. There is no equivalent for SPX options — flow is fragmented across multiple Cboe exchanges and OTC venues, no single venue defines the surface.
2. **No retail equity-options analogue is free with this depth.** [[tastytrade-platform|tastytrade]] and [[thinkorswim]] are free but tied to a brokerage account; standalone tools at this depth ([[optionnet-explorer]], orats, livevol) all charge. The Position Builder being free, no-login, and exchange-canonical is genuinely unusual.
3. **Crypto-options trader sophistication is high but capital deployed is small.** The active retail-and-small-shop crypto-options trader needs institutional-grade analytics on a retail-grade budget. The Position Builder fills that gap exactly.

## Related

- [[deribit]] — the parent exchange and the dominant crypto-options venue.
- [[coinbase]] — owner of Deribit following the ~$2.9B acquisition announced May 2025.
- [[crypto-options]], [[bitcoin-options]], [[ethereum-options]] — the asset class.
- [[laevitas]] — third-party crypto-options analytics, complementary cross-venue view.
- [[paradigm]] — institutional crypto-options OTC platform that integrates with Deribit.
- [[amberdata]] — institutional crypto-options data vendor.
- [[portfolio-greeks-aggregation]] — the core capability the Position Builder provides.
- [[theta-targeting]], [[vega-budgeting]] — disciplines that consume the aggregate Greeks output.
- [[options-premium-selling]] — the strategy class for which the tool is most heavily used.
- [[implied-volatility]], [[options-greeks]] — the analytical primitives.
- [[dvol]] — Deribit's volatility index, displayed in the Position Builder.
- [[short-strangle]], [[iron-condor]] — the structures most commonly planned in it.
- [[tastytrade-platform]], [[optionnet-explorer]] — equity-options analogues.

## Sources

- Deribit Position Builder (https://pb.deribit.com) — live tool and product documentation.
- Coinbase, "Coinbase to acquire Deribit, becoming the most comprehensive global crypto derivatives platform" (8 May 2025) — https://www.coinbase.com/blog/coinbase-to-acquire-deribit-becoming-the-most-comprehensive-global-crypto-derivatives-platform
- Banking Dive, "Coinbase to acquire Deribit in $2.9B deal" — https://www.bankingdive.com/news/coinbase-acquire-deribit-2-point-9-billion-deal-derivatives-options-trump-kraken-ripple-nexo/747625/
- Bankless, "Coinbase completes $2.9B Deribit deal" — https://www.bankless.com/read/coinbase-completes-2-9b-deribit-deal
- Deribit Insights research blog and exchange documentation (https://www.deribit.com).
- Crypto-options market-share reports (Coinglass, Laevitas, Genesis Volatility, Amberdata) tracking Deribit's ~85% share of BTC/ETH options open interest.
- Deribit API documentation — defines the chain, surface, and Greeks endpoints the Position Builder consumes.
- Acquisition terms, market-share figures, and tool status verified via Perplexity (sonar, high search context), 2026-06-10.
