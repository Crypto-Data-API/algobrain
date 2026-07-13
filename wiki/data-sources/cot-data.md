---
title: "CFTC COT Data"
type: concept
created: 2026-04-14
updated: 2026-06-12
status: good
tags: [commodities, data-provider, futures]
aliases: ["COT Data", "CFTC COT Data", "Commitments of Traders Data"]
domain: [data-provider]
prerequisites: ["[[open-interest]]", "[[futures]]"]
difficulty: beginner
related: ["[[cot-report-analysis]]", "[[commercial-hedger-positioning]]", "[[speculative-positioning]]", "[[open-interest]]", "[[cftc]]", "[[commodity-data-sources]]", "[[commodity-free-tools]]", "[[commodities]]"]
---

The CFTC Commitments of Traders (COT) report is a weekly snapshot of futures and options positioning by trader category, providing transparency into who is long, who is short, and how crowded positions have become. It is one of the most valuable free data sources for commodity and futures traders. This page is the **data-source catalog entry** (formats, access, coverage, normalization); for the trading interpretation and signals see [[cot-report-analysis]].

## What It Is

The [[cftc|CFTC]] (Commodity Futures Trading Commission) publishes the COT report every **Friday at 3:30 PM ET**, reflecting positions as of the **prior Tuesday's market close**. This means there is a 3-day reporting lag — the data you see Friday reflects Tuesday's positions.

The report covers all US-traded futures and options contracts where at least **20 reportable traders** hold positions. This includes [[commodities]] (energy, metals, agriculture), [[forex|currencies]], interest rate futures, and equity index futures.

## Report Formats

### Legacy Report

The original format, dividing traders into three categories:

| Category | Description |
|----------|-------------|
| **Commercials** | Entities that use futures to hedge a physical business position (e.g., an oil producer hedging production, a grain elevator hedging inventory). Generally considered "smart money" in commodities. See [[commercial-hedger-positioning]]. |
| **Non-Commercials** (Large Speculators) | Entities trading for profit — hedge funds, CTAs, managed money. See [[speculative-positioning]]. |
| **Non-Reportable** (Small Speculators) | Positions below the CFTC reporting threshold. Calculated as total open interest minus commercials and non-commercials. |

### Disaggregated Report (since 2006)

A more detailed breakdown, available for physical commodity markets:

| Category | Description |
|----------|-------------|
| **Producer/Merchant/Processor/User** | Physical commodity businesses — the true hedgers |
| **Swap Dealer** | Banks and dealers that offset OTC swap exposure in futures — a mix of hedging and speculative positioning |
| **Managed Money** | CTAs, hedge funds, commodity pools — the speculative community |
| **Other Reportable** | Everyone else above the reporting threshold |

The Disaggregated report is generally preferred for commodity analysis because it separates swap dealers (whose positioning can be ambiguous) from pure hedgers and pure speculators.

### Traders in Financial Futures (TFF)

A separate report for financial futures (currencies, Treasuries, equity indices) using categories: dealer/intermediary, asset manager/institutional, leveraged funds, other reportable.

## Key Data Fields

For each trader category, the report provides:

- **Long positions** — number of contracts held long
- **Short positions** — number of contracts held short
- **Spreading positions** — contracts held as part of a spread (long one contract month, short another)
- **Changes from prior week** — net change in each category
- **Percent of open interest** — each category's share of total [[open-interest]]
- **Number of traders** — how many traders are in each category

## How to Access

| Source | Format | Cost | Notes |
|--------|--------|------|-------|
| **CFTC website** (cftc.gov/MarketReports/CommitmentsofTraders) | Bulk CSV/XLS download | Free | Official source, historical data back to 1986 (Legacy) and 2006 (Disaggregated) |
| **Barchart.com** | COT charts + data tables | Free (basic) | Good visualization, easy to read |
| **Quandl / NASDAQ Data Link** | API (JSON/CSV) | Free tier available | Best for programmatic access, clean data |
| **TradingView** | COT indicators | Free (with account) | Overlay COT data on price charts |
| **Investing.com** | COT charts | Free | Basic visualization |

## How to Normalize and Interpret

Raw COT numbers are difficult to compare across time because [[open-interest]] changes as markets grow or contract. Common normalization methods:

### Net Position
**Net position = Long contracts - Short contracts** for a given category. A positive number means the category is net long; negative means net short.

### Percentile of Historical Range
Express the current net position as a percentile of its 3-year (or 5-year) range:

```
Percentile = (Current net - 3yr Low) / (3yr High - 3yr Low) x 100
```

A reading above 90% indicates extreme long positioning; below 10% indicates extreme short positioning. Extremes often correspond to sentiment peaks and troughs.

### Percent of Open Interest
Express net position as a percentage of total open interest to normalize for market size changes:

```
Net % of OI = Net Position / Total Open Interest x 100
```

### Rate of Change
Weekly change in net position captures the speed and direction of positioning shifts. Rapid changes are more significant than gradual drift.

## Coverage

The COT report covers all US-traded futures with 20+ reportable traders, including:

- **Energy**: [[crude-oil|WTI crude]], [[natural-gas|natural gas]], heating oil, gasoline, [[brent-crude|Brent crude]] (ICE)
- **Metals**: [[gold]], [[silver]], [[copper]], [[platinum]], [[palladium]]
- **Grains**: [[corn]], [[wheat]], [[soybeans]], soybean oil, soybean meal
- **Softs**: [[coffee]], [[sugar]], [[cocoa]], [[cotton]]
- **Livestock**: [[live-cattle]], [[lean-hogs]]
- **Currencies**: EUR, JPY, GBP, AUD, CAD, CHF, NZD, MXN
- **Interest rates**: Treasury bonds, notes, bills, Eurodollars/SOFR
- **Equity indices**: S&P 500, Nasdaq 100, Dow, Russell 2000

## Limitations

1. **3-day reporting lag**: Tuesday data released Friday — positions may have already changed, especially in volatile markets
2. **Category ambiguity**: Some traders classified as "commercial" may have speculative motives, and vice versa. Swap dealer positioning in particular can be difficult to interpret.
3. **No OTC coverage**: The COT report only covers exchange-traded futures and options. It does not capture over-the-counter (OTC) positions, which can be substantial in energy and metals markets.
4. **Aggregation**: Each category aggregates many different traders with potentially different strategies and timeframes
5. **Weekly frequency**: In fast-moving markets, weekly data may miss intra-week positioning shifts
6. **Reporting threshold changes**: The CFTC periodically adjusts reporting thresholds, which can shift traders between reportable and non-reportable categories

## Sources

- CFTC Commitments of Traders reports (cftc.gov)
- (Source: [[2026-04-14-commodities-research-framework]])

## Related

- [[cot-report-analysis]]
- [[commercial-hedger-positioning]]
- [[speculative-positioning]]
- [[open-interest]]
- [[cftc]]
- [[commodity-data-sources]]
- [[commodity-free-tools]]
- [[commodities]]
- [[macro-data-sources]]
