---
title: "Options Data Sources"
type: reference
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [data, options, opra]
aliases: ["Options Market Data", "OPRA Data"]
related: ["[[data-sources-overview]]", "[[paid-data-providers]]", "[[options-greeks]]", "[[implied-volatility]]"]
---

# Options Data Sources

Where to get options chain data, historical implied volatilities, and greeks for serious research. Options data is the most expensive single category of market data for retail researchers, with no good free option. The reason: OPRA (the consolidated options tape) is voluminous, the redistribution licensing is strict, and computing useful historical IVs requires correct treatment of dividends, interest rates, and corporate actions.

## OPRA: The Source of Truth

The **Options Price Reporting Authority** is the consolidated tape for US listed options. Every option trade and quote on every US exchange flows through OPRA. All paid options data ultimately derives from OPRA — the question is which vendor cleans, indexes, and prices it.

OPRA is enormous: tens of millions of quote updates per day across hundreds of thousands of strikes and expirations. Storing and indexing it is non-trivial.

## Provider Comparison (at a glance)

The table below summarizes the providers detailed in the sections that follow. Price ranges are indicative tiers as described by each vendor at time of writing — confirm current pricing directly, and treat these as orders of magnitude, not quotes.

| Provider | Indicative range | History | Intraday | Calc'd IVs/greeks | Best for |
|---|---|---|---|---|---|
| **OptionMetrics IvyDB** | $10K-$50K+/yr (free to academics via WRDS) | Daily since 1996 | No (EOD only) | Yes | Academic / factor research; the gold standard |
| **ORATS** | ~$199-$999/mo | Deep EOD + intraday | Yes | Yes (surfaces, smiles) | Retail-to-small-fund serious traders |
| **Polygon.io (Options)** | $99-$2000+/mo | OPRA-derived | Yes | Partial (post-process) | Quants wanting raw tape + own IVs |
| **Databento (Options)** | Per-product | Nanosecond OPRA | Yes | No (raw) | Microstructure / HFT-grade research |
| **CBOE LiveVol** | Institutional | Very deep | Yes | Yes | Authoritative CBOE products (SPX, VIX) |
| **IVolatility.com** | $50-$500+/mo | Historical IVs | Limited | Yes | Affordable IVs; quality varies |
| **Bloomberg / Refinitiv** | Institutional terminal | Comprehensive | Yes | Yes | Desks already on the terminal |
| **Yahoo / CBOE.com / Barchart (free)** | Free | None / snapshots | No | No | Spot-checks only; never backtesting |

## Paid Data Providers

### OptionMetrics IvyDB

Range: institutional pricing, often $10K-$50K+/year. Free to academics via WRDS.

**Pros:** **The academic and institutional gold standard.** Daily historical options data going back to 1996, with calculated end-of-day implied volatilities, greeks, surfaces, and dividend forecasts. Used in nearly every published academic paper on options.

**Cons:** Expensive, daily-only (no intraday), end-of-day snapshots only, restrictive licensing.

**Best for:** Anyone doing factor research on volatility, options anomalies, or volatility surface arbitrage. The default for academic-style options research.

### ORATS (Option Research and Technology Services)

Range: ~$199-$999/month for retail-friendly subscriptions.

**Pros:** End-of-day and intraday IVs, calculated greeks, theoretical values, term structures, smiles, fitted surfaces. Web platform plus API. Designed for retail-to-institutional traders.

**Cons:** Less academic-friendly than OptionMetrics; coverage strongest on US listed options.

**Best for:** Retail and small-fund options traders who need calculated IVs and surfaces without the institutional price tag of OptionMetrics. The most accessible serious options data source as of 2024-2026.

### Polygon.io (Options Tier)

Range: $99-$2000+/month depending on plan.

**Pros:** OPRA-derived options chains and trades, modern API, includes underlying stock data. Reasonably priced.

**Cons:** Some calculated fields (IVs, greeks) require post-processing; not as polished as ORATS for analytics.

**Best for:** Quants who want raw OPRA tape and prefer to compute their own IVs and greeks.

### Databento (Options)

Range: per-product pricing.

**Pros:** Nanosecond-precision OPRA tape, normalized schema, modern API.

**Cons:** Pay-per-product can add up; focused on serious quant infrastructure.

**Best for:** Microstructure research on options, HFT-grade research.

### CBOE LiveVol

Range: institutional. Direct from the exchange.

**Pros:** Authoritative source for CBOE-listed products including SPX, VIX, and many proprietary indices. Very deep history.

**Cons:** Expensive, complex licensing.

### IVolatility.com

Range: $50-$500+/month tiers.

**Pros:** Affordable historical IVs, options scanners, web platform plus data downloads.

**Cons:** Quality varies; less rigorous than OptionMetrics or ORATS.

### iVolatility / Trade Alert / Trade Volume / SqueezeMetrics

Various retail/intraday-focused options analytics shops with subscription products.

### Bloomberg / Refinitiv

Both provide options data as part of their broader institutional terminals. Expensive but comprehensive.

## Free Sources (Limited)

### Yahoo Finance Option Chains

Free via `yfinance` and the Yahoo web frontend.

**Pros:** Free, easy, broad ticker coverage.

**Cons:** **Snapshots only — no historical depth**. Quotes can be stale or wrong. Greeks and IVs are not provided. Cannot be used for any backtesting.

**Use for:** Spot-checking current chains. Never for research.

### CBOE.com

Some free EOD data for SPX, VIX, and select products on the CBOE website.

**Pros:** Authoritative, free.

**Cons:** Limited products, manual download, no API.

### NASDAQ.com / Marketwatch / Barchart

Free chain views of current options. No historical depth, no greeks, no API.

## Data Required for Honest Options Backtesting

A complete options backtest dataset includes:

1. **Bid and ask** for every strike and expiration at every snapshot
2. **Last trade and volume** (less reliable than NBBO quotes for stale options)
3. **Open interest** by strike
4. **Underlying price** at the same timestamp
5. **Risk-free rate curve** at each date (for IV calculation)
6. **Forward dividend schedule** for each underlying (for IV calculation)
7. **Borrow rate** for the underlying (matters for in-the-money puts and synthetic positions)
8. **Corporate action history** for the underlying (splits, dividends, mergers, ticker changes — all of which affect option contract terms)
9. **Calculated implied volatilities** at each strike (or the inputs to compute them yourself)
10. **Calculated greeks** (delta, gamma, vega, theta, rho)

Free sources provide at most #1, #2, and #3 — and even those are stale snapshots. Anything serious requires a paid source.

## Implied Volatility Computation Pitfalls

If you're computing IVs yourself from option prices, watch out for:

1. **Dividend handling.** The Black-Scholes formula needs the present value of dividends paid before expiration. Wrong dividend → wrong IV → wrong everything. Many vendors do this incorrectly.

2. **American vs. European pricing.** Most US listed options are American, but Black-Scholes assumes European. For deep ITM options especially, the early-exercise premium matters and Black-Scholes underestimates value.

3. **Risk-free rate selection.** Use the term-matched OIS or Treasury rate, not a single fixed rate.

4. **Bid-ask vs. mid-price.** IVs computed from bid prices, mid prices, and ask prices differ. Be consistent and document which you use.

5. **Bad inputs at expiration boundaries.** Options very close to expiration with very low time value have unstable IV estimates.

6. **Missing strikes.** Some chains have gaps where strikes don't trade. Fitting smiles requires interpolation choices.

## Storage and Indexing

Options data is voluminous. For SPY alone, OPRA generates 100K+ quote updates per day across all strikes and expirations. A multi-year historical dataset for the full universe runs into tens of terabytes.

Options storage best practices:
- Parquet partitioned by date and root symbol
- Compressed with zstd
- Index on (date, root, expiration, strike, side)
- Store snapshots (e.g., end-of-minute) rather than every quote update if you can sacrifice latency
- Compute IVs and greeks once and store them rather than recomputing

A practical retail setup: ORATS or Polygon EOD data → parquet on local SSD or R2 → queried via DuckDB. ~1TB of storage covers several years.

## How Trading and AI Systems Consume This Data

Different consumers need different slices of the options dataset. Matching the source to the use case avoids overpaying for data you won't use:

| Consumer | What it needs | Typical source tier | Notes |
|---|---|---|---|
| Backtest / research engine | Point-in-time EOD chains + calc'd IVs/greeks, survivorship-free | OptionMetrics / ORATS | Needs the full 10-item dataset below; vintage data matters |
| Live signal generation | Current chains + fresh IVs near-real-time | ORATS / Polygon / LiveVol | Latency tolerance modest for EOD/swing systems |
| Microstructure / execution research | Full NBBO quote tape, nanosecond timestamps | Databento / LiveVol | Volume and storage dominate cost |
| Risk / [[options-risk-budgeting]] | Greeks per position, surface for scenario re-pricing | ORATS / Bloomberg | Feeds [[gamma-pnl]] and vega attribution |
| LLM / AI analysis layer | Summarized surfaces, [[put-call-ratio]], skew, term structure as features | Derived from any tier | Feed *computed features*, not raw OPRA tape, to the model |

For an AI or LLM-driven workflow, the practical pattern is to **pre-compute features** (skew, term structure, [[implied-volatility]] rank, [[put-call-ratio]], realized-vs-implied spread) from a clean source and store them as compact, model-friendly tables. Pushing raw OPRA quote updates at a model is both expensive and low-signal; the value is in the derived volatility-surface and sentiment features.

## Data-Quality Caveats

Beyond the IV-computation pitfalls above, the most common ways options datasets mislead:

1. **Stale/crossed quotes.** Illiquid strikes carry quotes that haven't updated, sometimes with the bid above the ask. Filter on quote age and sanity-check the book before computing IV.
2. **Snapshot timing mismatch.** The option snapshot and the underlying snapshot must share a timestamp. A few seconds of skew between them corrupts the IV — a frequent error with free sources.
3. **Survivorship in the option universe.** Delisted underliers, expired roots, and changed multipliers (post-split) silently vanish from reconstructed series. See [[survivorship-bias]] and the corporate-action requirement (#8 below).
4. **Reconstructed vs vintage series.** Vendors that "improve" historical data (better dividend forecasts, refit surfaces) change history. Long backtests of [[volatility-arbitrage]] or [[gamma-scalping]] strategies should use point-in-time vintages, not the latest reconstruction.
5. **Settlement/SOQ quirks.** Index products (SPX, VIX) settle on special opening quotes, not the listed close — naive EOD joins misprice the last day.

## Recommended Stack

### Personal research, no budget
Use Yahoo for spot checks. Accept that you cannot do honest options backtesting. Focus research on strategies that don't require options.

### Personal research with budget
**ORATS** at $199-$499/month is the entry point. Provides daily IVs, greeks, surfaces with good API access.

### Serious retail
**ORATS or Polygon Options** + custom IV computation pipeline + parquet storage. ~$500-$1500/month.

### Institutional / academic
**OptionMetrics IvyDB** (via WRDS if academic, direct otherwise) for historical research. **CBOE LiveVol** or **Refinitiv** for live and intraday.

## Sources

- OptionMetrics documentation
- ORATS user guide
- [[book-options-volatility-and-pricing]] — Natenberg on what data you actually need for serious options work

## Related

- [[data-sources-overview]]
- [[paid-data-providers]]
- [[options-greeks]]
- [[implied-volatility]]
- [[volatility-arbitrage]]
- [[gamma-scalping]]
- [[gamma-pnl]] — consumes greeks for P&L attribution
- [[put-call-ratio]] — a derived sentiment feature from options flow
- [[volatility-skew]]
- [[options-risk-budgeting]] — downstream consumer of greeks and surfaces
- [[survivorship-bias]] — a key options-universe data-quality risk
- [[lookahead-bias]] — point-in-time / vintage-data concern
