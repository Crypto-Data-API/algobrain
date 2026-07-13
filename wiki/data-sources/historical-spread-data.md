---
title: "Historical Spread & Basis Data Sources"
type: reference
created: 2026-04-20
updated: 2026-06-20
status: excellent
tags: [data, arbitrage, backtesting, crypto, options, futures, meta]
aliases: ["Spread Data", "Basis Data Sources", "Funding Rate History", "Historical Arbitrage Data"]
related: ["[[data-sources-overview]]", "[[crypto-data-sources]]", "[[paid-data-providers]]", "[[free-data-sources]]", "[[arbitrage-overview]]", "[[funding-rate-arbitrage]]", "[[cross-exchange-arbitrage]]", "[[cash-and-carry]]", "[[volatility-arbitrage]]", "[[pairs-trading]]", "[[transaction-cost-modeling]]", "[[exchange-api-reference]]", "[[market-chameleon]]", "[[merger-arbitrage]]", "[[etf-arbitrage]]"]
---

# Historical Spread & Basis Data Sources

Arbitrage backtesting requires historical data on the *spreads themselves* — not just individual asset prices. A backtest that reconstructs spreads from two separate price feeds often underestimates slippage, misses synchronization issues, and overstates profitability. This page catalogs where to find pre-computed or properly synchronized spread, basis, and funding rate time series. It is the [[arbitrage-overview|arbitrage]]-focused companion to [[paid-data-providers]] and [[free-data-sources]]; for the options-analytics layer over OPRA see [[market-chameleon]], and for the broader catalog see [[data-sources-overview]].

> **Pricing & coverage disclaimer:** Cost figures and history-depth ranges below are ballpark, drawn from vendor pages and community reports circa 2024-2026, and change frequently. Confirm current pricing, coverage, and history depth on each vendor's own site before relying on them.

## Master Summary by Spread Type

The page is organized by spread family. The table below is the index: for each arbitrage data need, the cheapest viable source, the best-quality source, and the single most dangerous pitfall. Detailed per-family tables follow.

| Spread / data type | Cheapest viable source | Best-quality source | Most dangerous pitfall | Feeds strategy |
|---|---|---|---|---|
| Crypto funding rates | Exchange APIs (free) / Coinglass Pro (~$50) | Tardis.dev / Kaiko | Predicted vs settled rate; interval mismatch (1h vs 8h) | [[funding-rate-arbitrage]] |
| Crypto spot-futures basis | Coinglass / exchange APIs | Tardis.dev (synced) / Kaiko | Sub-second timestamp mismatch → phantom basis | [[cash-and-carry]] |
| Cross-exchange differentials | DIY from exchange APIs | Tardis.dev (L2 books) / Kaiko | No free pre-computed series; fee regime drift | [[cross-exchange-arbitrage]] |
| Options IV surfaces | Deribit (crypto) / CBOE (VIX) | OptionMetrics IvyDB / ORATS | Mid vs bid/ask overstates fills by half-spread | [[volatility-arbitrage]] |
| ETF premium/discount | ETF.com / provider sites | Bloomberg / Refinitiv | NAV vs market-price timestamp drift | [[etf-arbitrage]] |
| Merger-arb spreads | SEC EDGAR (terms only) | Bloomberg MA / SDC Platinum | Snapshot-at-announcement ≠ spread time series | [[merger-arbitrage]] |
| Commodity spreads | CME / EIA / USDA | Norgate / CSI / Bloomberg | Roll gaps in raw contracts → phantom signals | [[crack-spread]], [[crush-spread]] |

Many of these vendors are profiled in more general terms in [[paid-data-providers]]; this page focuses specifically on their fitness for *spread/basis/funding* reconstruction.

## Crypto Funding Rates

### Free Sources

| Source | Coverage | Granularity | History Depth | Access |
|---|---|---|---|---|
| **Coinglass** (coinglass.com) | Binance, OKX, Bybit, dYdX, Hyperliquid, 10+ venues | Per-settlement (8h or 1h) | 2-3 years | Free web dashboard, API requires paid plan |
| **Exchange APIs** (direct) | Single venue each | Per-settlement | Varies (1-3 years typically) | Free REST API. See [[exchange-api-reference]] |
| **Laevitas** (laevitas.ch) | Major perp venues | Per-settlement | 1-2 years | Free dashboard, API on paid plans |
| **Velo Data** (velo.xyz) | Major perp venues | Per-settlement | 1-2 years | Free tier available |

### Paid Sources

| Source | Coverage | Granularity | History Depth | Cost | Notes |
|---|---|---|---|---|---|
| **Tardis.dev** | 15+ venues, all historical settlements | Tick-level funding events | Full venue history | $59-399/mo | Best for backtesting; reconstructs exact settlement amounts |
| **Kaiko** | 100+ venues | Per-settlement + intraday predicted rates | Full history for major venues | $1K-10K+/mo | Institutional normalization |
| **Coinglass Pro** | All major venues | Per-settlement | Full available history | ~$50/mo | Most accessible aggregated funding data |

### Key Pitfalls

- **Funding interval mismatch:** Binance/OKX/Bybit = 8-hour intervals. Hyperliquid/dYdX = 1-hour intervals. Always annualize before comparing
- **Predicted vs. actual:** Some APIs return the *predicted* next funding rate (which changes continuously) vs. the *settled* rate (fixed at settlement time). Use settled rates for backtesting
- **Sign convention:** Positive = longs pay shorts across all major venues, but verify for smaller exchanges

## Crypto Spot-Futures Basis

### Free Sources

| Source | Coverage | Data Type | History | Access |
|---|---|---|---|---|
| **Coinglass** | Binance, OKX, Bybit quarterly futures | Basis (%) and basis annualized | 2-3 years | Free dashboard |
| **Laevitas** | Major futures venues | Basis curve (term structure) | 1-2 years | Free dashboard |
| **Exchange APIs** | Single venue | Spot price + futures price (reconstruct basis manually) | Varies | Free |

### Paid Sources

| Source | Coverage | Cost | Notes |
|---|---|---|---|
| **Tardis.dev** | Synchronized spot + futures tick data across venues | $59-399/mo | Reconstruct basis at any granularity from raw data |
| **Kaiko** | Pre-computed basis metrics | $1K+ | Institutional grade |
| **Amberdata** | Basis, carry, and term structure analytics | $1K+ | Combined market + on-chain |

### Basis Reconstruction from Raw Data

If no pre-computed basis series is available:
```
basis_pct = (futures_price - spot_price) / spot_price × 100
annualized_basis = basis_pct × (365 / days_to_expiry)
```

**Critical:** Spot and futures prices must be timestamped to the same millisecond. Even 1-second mismatch can create phantom arb signals in a backtest. Use Tardis.dev's synchronized feeds or exchange-level data where both instruments trade on the same matching engine.

## Cross-Exchange Price Differentials

### Free Sources

There is no widely available *free* source of pre-computed cross-exchange spread time series. You must construct them from individual exchange data.

**DIY construction method:**
1. Download historical trade data from each exchange (REST APIs, typically 1000 trades per request)
2. Resample to common time intervals (1-second or 1-minute bars)
3. Compute spread: `spread = bid_exchange_B - ask_exchange_A`
4. Account for fees to compute net spread

### Paid Sources

| Source | Coverage | Cost | Notes |
|---|---|---|---|
| **Tardis.dev** | Full L2 order book history across 15+ venues | $59-399/mo | Best option: reconstruct any cross-venue spread from raw order books |
| **Kaiko** | Cross-exchange reference rates and spreads | $1K+ | Pre-computed cross-venue metrics |
| **CoinRoutes** | Real-time and historical cross-exchange best execution | Institutional pricing | Designed for SOR (smart order routing) analytics |

### The Kimchi Premium (Historical)

For [[2017-2021-kimchi-premium]] research:
- Korean exchange data (Upbit, Bithumb) is available via CoinGecko and CryptoCompare historical APIs
- USD/KRW exchange rate from FRED or Investing.com
- Premium = `(korean_btc_price_in_usd - global_btc_price_usd) / global_btc_price_usd`

## Options Implied Volatility Surfaces

### Free Sources

| Source | Data | History | Limitations |
|---|---|---|---|
| **CBOE** (cboe.com) | VIX index daily close | 1990-present | Index only, not individual IV surfaces |
| **Yahoo Finance** | Options chains (snapshot) | Current day only | No historical surfaces |
| **Deribit API** | Crypto options chains | Limited historical | Good for current crypto vol |

### Paid Sources

| Source | Coverage | Cost | Notes |
|---|---|---|---|
| **OptionMetrics IvyDB** | US equities + indices, daily IV surfaces 1996-present | $10K-50K+/year (free via WRDS for academics) | Gold standard. Includes standardized IVs, greeks, forward prices, borrow rates |
| **ORATS** | US equities, IV surfaces, skew, term structure | $199-999/mo | Best retail-accessible option data. Includes historical greeks and IV30/IV60/IV90 metrics |
| **Polygon.io** (options tier) | OPRA-sourced US options data | $200-2000/mo | Raw data — you compute your own IVs and greeks |
| **iVolatility** | US + international, IV surfaces | $100-500/mo | Pre-computed surfaces and skew analytics |
| **Deribit + Tardis.dev** | BTC/ETH options, full order book history | $59-399/mo (Tardis) | Crypto vol surface reconstruction |

### What You Need for Vol Arb Backtesting

A proper [[volatility-arbitrage]] backtest requires:
1. **Strike-level bid/ask** (not mid!) — mid-to-mid backtests overstate fills by half the spread
2. **Underlying price** at the same timestamp as options data
3. **Risk-free rate** (treasury yields or OIS rates)
4. **Forward dividends** (for equity options)
5. **Borrow rates** (for put-call parity and conversion/reversal arb)
6. **Corporate action history** (splits, mergers change strike prices)

OptionMetrics IvyDB provides all of these. Everything else requires assembly.

## ETF Premium/Discount History

### Free Sources

| Source | Data | History |
|---|---|---|
| **ETF.com** | Daily premium/discount for all US ETFs | 1-3 years |
| **Morningstar** | Premium/discount, NAV history | 3-5 years |
| **ETF provider websites** (iShares, Vanguard, SPDR) | Daily NAV and market price | Since inception |

### Paid Sources

| Source | Coverage | Cost |
|---|---|---|
| **Bloomberg Terminal** | Real-time and historical NAV, premium/discount, creation/redemption flows | ~$25K/year |
| **Refinitiv** | Similar to Bloomberg | $5K-50K/year |

### Key Metrics for ETF Arb Research

- **Premium/discount:** `(market_price - NAV) / NAV × 100`
- **Tracking difference:** Fund return vs. index return (annual)
- **Tracking error:** Standard deviation of tracking difference (daily)
- **Creation/redemption basket:** Exact composition required to create/redeem — available from fund providers

## Merger Arbitrage Spread History

### Free Sources

| Source | Data | Notes |
|---|---|---|
| **SEC EDGAR** | Merger filings (8-K, S-4, proxy statements) | Deal terms, not spread time series |
| **CNBC / Bloomberg News** | Deal announcements with initial spreads | Snapshot at announcement only |

### Paid Sources

| Source | Coverage | Cost |
|---|---|---|
| **Bloomberg (MA function)** | Comprehensive deal database with historical spreads, probabilities, timeline | ~$25K/year |
| **Refinitiv / SDC Platinum** | Historical M&A database | Institutional pricing |
| **MergerArb.com** | US/EU deal spreads, updated daily | ~$200/year |
| **WRDS (academic)** | SDC, Capital IQ M&A data | Free for academics |

## Commodity Spreads

### Free Sources

| Source | Data | History |
|---|---|---|
| **CME Group** (cmegroup.com) | Settlement prices for all futures contracts | 10+ years for major contracts |
| **EIA** (eia.gov) | Crude, refined product, natural gas spot and futures prices | 20+ years |
| **USDA** (usda.gov) | Soybean, meal, oil prices for [[crush-spread]] | 20+ years |
| **Quandl/Nasdaq Data Link** | Various commodity futures (some free) | Varies |

### Paid Sources

| Source | Coverage | Cost |
|---|---|---|
| **Norgate Data** | Continuous futures contracts with proper roll methodology | $30-70/mo |
| **CSI Data** | Comprehensive futures history, custom back-adjustment | $50-200/mo |
| **Bloomberg** | Everything | ~$25K/year |

### Spread Construction from Futures

- **[[crack-spread]]:** `3 × crude - 2 × gasoline - 1 × heating oil` (3:2:1 ratio)
- **[[crush-spread]]:** `soybean_meal × 0.022 + soybean_oil × 0.11 - soybeans` (per bushel)
- **[[spark-spread]]:** `electricity_price - (natural_gas_price × heat_rate)`
- **Calendar spread:** `front_month_price - back_month_price`

**Critical:** Use *continuous contracts* with proper back-adjustment for backtesting. Raw contract prices have roll gaps that create phantom spread signals. Norgate and CSI both handle this correctly.

## Data Quality Checklist for Arb Backtests

Before trusting any spread backtest, verify:

- [ ] **Timestamp synchronization:** Are both legs timestamped to the same resolution? 1-second mismatch can create phantom arbs
- [ ] **Bid-ask vs. mid:** Are you using bid-ask or mid prices? Mid-to-mid overstates profitability by approximately the full spread
- [ ] **Survivorship bias:** Does your universe include assets that were later delisted? See [[free-data-sources]] for sources that avoid this
- [ ] **Point-in-time data:** Are fundamentals and index constituents as-of the backtest date, or restated? See [[lookahead-bias]]
- [ ] **Fee regime accuracy:** Were fees the same historically as today? (Binance changed fee tiers in 2023; Coinbase restructured in 2022)
- [ ] **Funding rate source:** Are you using predicted rates (pre-settlement) or actual settled rates?
- [ ] **Market hours:** Are you backtesting during hours when both legs were actually tradeable?
- [ ] **Liquidity filter:** Are you assuming fills on assets that had < $10K daily volume at the time?

## How Trading and AI Systems Consume Spread Data

Spread data sits at the research end of the pipeline (see [[paid-data-providers#How Trading and AI Systems Consume Paid Data]]), and the way an automated or [[ai-trading|AI-driven]] system uses it is specific to arbitrage:

1. **Synchronized two-leg ingestion.** The defining requirement is that both legs share a timestamp resolution fine enough that no phantom arb appears. Pipelines either pull a *pre-computed* spread series (Coinglass, Kaiko, ETF.com) or reconstruct it from *synchronized* raw feeds (Tardis L2 books, exchange same-engine data). Reconstructing from two unsynced REST feeds is the classic way to invent edge that does not exist.
2. **Net-of-cost spread, not gross.** A signal layer should compute spreads after fees and (for executable backtests) against bid/ask, not mid. This is where [[transaction-cost-modeling]] plugs in; a gross-spread series is for monitoring, not sizing.
3. **Funding/basis as carry features.** For [[funding-rate-arbitrage]] and [[cash-and-carry]], the settled funding rate and annualized basis become time-series features. Always use *settled*, not *predicted*, rates and annualize before cross-venue comparison (1h vs 8h intervals differ 8x).
4. **Regime-aware fee handling.** Historical fee tiers changed (Binance 2023, Coinbase 2022); an AI backtest that applies today's fees to old data understates costs in early periods. Version the fee schedule alongside the price data.
5. **Reproducibility.** Because vendors silently revise history, snapshot and version each pull. An agentic research loop that re-pulls data between runs can otherwise see its "edge" appear or vanish for non-market reasons.

The practical upshot: for crypto, **Tardis.dev** is the dominant retail-accessible source because its synchronized L2/L3 feeds let you reconstruct *any* spread at *any* granularity from one consistent clock; for options, **OptionMetrics IvyDB** is the only single source that bundles strike-level quotes, underlying, rates, dividends, and borrow needed for a clean [[volatility-arbitrage]] backtest.

## Sources

- General market knowledge; no specific wiki source ingested yet. Vendor coverage, pricing, and history-depth figures are drawn from vendor pages and community reports circa 2024-2026 and should be confirmed at the source.

## Related

- [[data-sources-overview]]
- [[crypto-data-sources]]
- [[paid-data-providers]]
- [[free-data-sources]]
- [[options-data-sources]]
- [[market-chameleon]]
- [[transaction-cost-modeling]]
- [[arbitrage-overview]]
- [[funding-rate-arbitrage]]
- [[cross-exchange-arbitrage]]
- [[cash-and-carry]]
- [[volatility-arbitrage]]
- [[merger-arbitrage]]
- [[etf-arbitrage]]
- [[exchange-api-reference]]
