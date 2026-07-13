---
title: "Bloomberg Terminal"
type: entity
created: 2026-04-06
updated: 2026-05-07
status: good
tags: [data-provider, institutional, stocks, bonds, forex, commodities]
entity_type: company
website: https://www.bloomberg.com/professional/solution/bloomberg-terminal/
related:
  - "[[koyfin]]"
  - "[[polygon-io]]"
  - "[[tradingview-platform]]"
---

# Bloomberg Terminal

## Overview

The institutional gold standard for financial data. Bloomberg Terminal (commonly just "the Bloomberg") is an integrated platform covering real-time and historical data on every asset class globally -- equities, fixed income, FX, commodities, derivatives, municipals, money markets, and more. Beyond raw data, it bundles analytics, news (Bloomberg News breaks stories that move markets), execution management, messaging (Bloomberg IB chat is Wall Street's de facto communication layer), and research. There is no single product on Earth with comparable breadth and depth of financial information. If you work at a bank, hedge fund, or asset manager, you have a Bloomberg.

## Pricing

- **~$24,000/year** ($2,000/month) per seat -- non-negotiable for single terminals
- Volume discounts for firms with many seats, but still five figures per user
- Two-year contracts are standard
- No free tier, no trial (Bloomberg occasionally offers limited academic access)
- Additional costs for premium data feeds (e.g., Bloomberg Second-by-Second tick data)

## What You Get (vs Free)

- Real-time pricing across every exchange worldwide (not 15-min delayed)
- Proprietary consensus estimates, earnings models, and analyst revisions
- Bloomberg News wire -- headlines that move markets minutes before they hit retail platforms
- BQNT (Bloomberg Quant) environment for Python-based research directly on the terminal
- PORT for portfolio analytics, MARS for risk management, EMSX for execution
- Fixed income analytics (yield curves, spread analysis, OAS) that simply do not exist elsewhere
- Corporate action data, M&A analytics, credit default swap pricing

## Alpha Edge

- **Speed**: Bloomberg headlines move markets. Institutions see breaking news 30-60 seconds before it appears on free platforms. In fast markets, that gap is enormous
- **Consensus estimates**: proprietary EPS/revenue estimates and revisions data powers [[earnings]]-based strategies
- **Fixed income depth**: bond markets are opaque -- Bloomberg is the only source for real-time corporate bond pricing, municipal yields, and structured product analytics
- **FLDS and custom screening**: screen the entire global equity universe on thousands of fields simultaneously
- **Bloomberg Intelligence**: proprietary sector research and thematic analysis

## Key Features

- **BQL (Bloomberg Query Language)**: SQL-like language for pulling custom datasets across millions of securities
- **Bloomberg Chat**: real-time messaging between buy-side and sell-side -- deals get done here
- **Excel Add-in (BDH/BDP)**: pull any Bloomberg data directly into spreadsheets
- **API access**: Bloomberg B-PIPE and Server API for programmatic data feeds into trading systems
- **ALLQ/QR**: real-time quote montages and Level 2 data across exchanges
- **GP**: charting with technical analysis overlays and fundamental comparisons
- **News**: TOP, N, and NH functions for breaking news by topic, sector, or security

## Who Uses It

- Every major investment bank (Goldman, JPMorgan, Morgan Stanley)
- Hedge funds of all sizes (it is the minimum infrastructure for an institutional fund)
- Asset managers, pension funds, insurance companies
- Central banks and government finance ministries
- Corporate treasury departments
- Financial advisors at wirehouses
- Anyone who needs to be taken seriously in institutional finance

If you are a retail trader, Bloomberg is overkill and unaffordable. Look at [[koyfin]] for a Bloomberg-lite experience at 2% of the cost, or [[polygon-io]] for institutional-grade data APIs.

## Options Analytics (OVDV, OVCV, OMON, OVME)

Bloomberg's options analytics suite is one of the main reasons institutional options desks pay the full subscription rather than using a dedicated vol provider like Cboe LiveVol or ORATS. The functions interlock with the rest of the terminal (news, fundamentals, futures curves, fixed income context, cross-asset correlations) so that an options-portfolio decision can be made in a single workspace.

### Core Option Functions

- **OMON** - Options Monitor. Live option chain for any underlying, all listed expirations and strikes, with bid/ask, mid, last, volume, open interest, IV by strike, and full Greeks (delta, gamma, theta, vega, rho). Filter by moneyness, expiration, or strike range. The default starting point for any single-name options analysis.
- **OVDV** - Implied Volatility Surface. 3D and 2D visualization of the IV surface across strike and expiry. Compare current surface vs historical snapshots; identify skew, term structure, and surface dislocations. Supports ATM term structure, fixed-strike term structure, and full surface views.
- **OVCV** - Volatility Cone. Plots current implied volatility at various tenors against historical realized-volatility percentiles for the same tenors. Lets a trader see at a glance whether 30-day IV is rich or cheap relative to its historical range, broken out by tenor (1w, 1m, 3m, 6m, 1y).
- **OVME** - Options Valuation Multi-Engine. Pricing model workbench supporting Black-Scholes, binomial (Cox-Ross-Rubinstein), trinomial, finite-difference, and Monte Carlo. Used for pricing exotics (Asian, barrier, lookback, digital), structured payoffs, and validating model marks. Greeks are computed under the chosen model so a path-dependent payoff is not stuck with Black-Scholes Greeks.
- **HVOL** - Historical Volatility chart. Realized volatility over user-defined window (close-to-close, Parkinson, Garman-Klass, Yang-Zhang estimators) with configurable lookback and frequency. Pairs with OVCV for IV-vs-RV analysis.
- **OSA** - Options Strategy Analyzer. Build a multi-leg structure (single, vertical, butterfly, condor, calendar, custom), see P&L curve at expiry and at any forward date, aggregated Greeks (portfolio delta/gamma/vega/theta), break-evens, max profit, max loss, probability of profit. Supports stress scenarios (price shocks, vol shocks, time decay).
- **VOLC** - Volatility Comparison. Side-by-side IV comparison across underlyings (e.g., AAPL vs MSFT vs SPX) at matched tenors and moneyness. Useful for relative-value vol trades and dispersion analysis.
- **SKEW** - Skew analytics; visualize and chart 25-delta risk reversal, butterfly, and put-call IV differential over time.
- **HIVG** - Historical Implied Volatility. IV time series at a constant moneyness (e.g., 30-day ATM IV) so the trader sees how rich/cheap current IV is relative to its own history.
- **EVTS** - Earnings/event calendar overlay; combine with OMON to see options chains in the context of upcoming catalysts.

### Why Pay for Bloomberg vs Cboe LiveVol or ORATS

Dedicated vol providers like Cboe LiveVol, ORATS, IVolatility, and OptionMetrics offer deeper historical option-chain databases at a fraction of the price (LiveVol Pro and ORATS data subscriptions are typically $100-$600/month vs $24,000/year for Bloomberg). Bloomberg wins for institutional users on integration rather than raw data depth:

- **Macro and news context in one keystroke**. From OMON the trader can hit `N` for news on the underlying, pull the issuer's credit curve, see Fed funds futures curve from WIRP, or check earnings consensus from EE - all without leaving the terminal.
- **Cross-asset coverage**. Equity options, index options, ETF options, futures options, FX options, interest-rate options (swaptions, caps/floors), and credit options (CDS options) are all in one product. Vol-only providers usually cover one or two of these.
- **Custom alerts**. Real-time alerts on IV changes, skew movements, vol breaks (e.g., "alert me when SPX 30-day ATM IV crosses 20"), trade prints, unusual options activity.
- **OMS/EMS pre-trade analytics**. EMSX/AIM ties OSA-style portfolio Greeks directly into the order-management system so a desk can pre-trade-check an order against portfolio limits (delta, vega, gross premium).
- **Portfolio-level Greeks rollup**. PORT and MARS aggregate Greeks across an entire book - including cross-asset positions - and run scenario analysis (parallel vol shifts, term-structure twists, skew steepening) on the combined book.
- **Counterparty integration**. Quotes from sell-side dealers (FXGO for FX options, IBOX for credit) flow directly into Bloomberg analytics, so RFQ-driven institutional flow can be priced and traded in the same workspace.
- **BQuant for vol research**. The BQNT Python environment lets quants pull historical IV surfaces via BQL and run custom vol-surface fitting, dispersion backtests, or vol-arbitrage research without exporting data.

For an [[itpm-trade-construction-playbook|ITPM-style portfolio]] running multi-asset structures - say SPX index credit spreads, single-name earnings butterflies, and rates swaption hedges - Bloomberg's combined coverage is more valuable than the deeper but narrower datasets at LiveVol or ORATS. For pure equity-options retail or small-shop quants, the dedicated providers are far more cost-effective and have better tick-level historical option data.
