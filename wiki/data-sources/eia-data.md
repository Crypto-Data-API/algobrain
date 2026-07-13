---
title: "EIA Data Sources"
type: concept
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [commodities, energy, data-provider, meta]
aliases: ["EIA Data Sources", "EIA Data", "Energy Information Administration Data"]
domain: [data-provider]
difficulty: beginner
related: ["[[eia]]", "[[crude-oil]]", "[[natural-gas]]", "[[gasoline]]", "[[heating-oil]]", "[[commodity-data-sources]]", "[[inventory-cycle-analysis]]", "[[commodities]]", "[[coal]]", "[[nuclear-power]]", "[[contango]]", "[[backwardation]]", "[[cot-report-analysis]]"]
---

# EIA Data Sources

The U.S. Energy Information Administration ([[eia|EIA]]) is the statistical and analytical agency within the U.S. Department of Energy. It is the **single most important free data source for energy commodity traders**, providing comprehensive, timely, and market-moving data on petroleum, natural gas, coal, electricity, and renewable energy. Several EIA releases are among the most market-moving data points in all of global commodities trading. (Source: [[2026-04-14-commodities-research-framework]])

## Release Calendar at a Glance

| Report | Cadence | Typical time (ET) | Primary market | Surprise potential |
|--------|---------|-------------------|----------------|--------------------|
| Weekly Petroleum Status Report | Weekly (Wed) | 10:30 AM | [[crude-oil]], [[gasoline]], [[heating-oil]] | Very high |
| Weekly Natural Gas Storage Report | Weekly (Thu) | 10:30 AM | [[natural-gas]] | Very high |
| Short-Term Energy Outlook (STEO) | Monthly (1st-2nd wk) | -- | All energy | Medium |
| Drilling Productivity Report (DPR) | Monthly (~15th) | -- | [[crude-oil]], [[natural-gas]] | Low-medium |
| Monthly Energy Review (MER) | Monthly (~25th) | -- | All energy | Low (revisions) |
| Annual Energy Outlook (AEO) | Annual | -- | Structural | Low |

> Scheduling caveats: a **US federal holiday** pushes the weekly petroleum report to Thursday and the gas-storage report to Friday. Releases can also slip during government shutdowns. Always confirm against the official EIA release schedule rather than assuming the default day.

## Market-Moving Reports

### Weekly Petroleum Status Report

| Detail | Value |
|--------|-------|
| **Release** | Wednesday, 10:30 AM ET |
| **Markets moved** | [[crude-oil]], [[gasoline]], [[heating-oil]], energy equities |
| **Impact** | One of the most market-moving releases in commodities |
| **URL** | [eia.gov/petroleum/supply/weekly/](https://www.eia.gov/petroleum/supply/weekly/) |

**Key data points:**
- **U.S. crude oil inventories** (headline number) — weekly change vs consensus estimate drives price
- **Cushing, Oklahoma stocks** — WTI delivery point; critical for [[contango]]/[[backwardation]] assessment
- **Gasoline inventories** — seasonal demand tracking for [[gasoline]] market
- **Distillate inventories** — diesel/[[heating-oil]] stocks
- **Refinery utilization** — percentage of refining capacity in use; seasonal maintenance patterns
- **Crude oil imports and exports** — net import position of the U.S.
- **U.S. crude oil production** — weekly estimate (monthly revised figures are more accurate)

**Trading note:** The American Petroleum Institute (API) releases its own estimate on Tuesday evening (4:30 PM ET), which serves as a preview. Significant divergence between API and EIA figures creates additional volatility on Wednesday. See [[inventory-cycle-analysis]] for a framework on trading inventory data.

### Weekly Natural Gas Storage Report

| Detail | Value |
|--------|-------|
| **Release** | Thursday, 10:30 AM ET |
| **Markets moved** | [[natural-gas]] |
| **Impact** | The single most important data point for natural gas pricing |
| **URL** | [eia.gov/naturalgas/storage/](https://www.eia.gov/naturalgas/storage/) |

**Key data points:**
- **Net change in working gas** — injection (build) or withdrawal (draw) for the week
- **Total working gas in underground storage** — absolute level in billion cubic feet (Bcf)
- **Comparison to 5-year average** — deviation from seasonal norm is the critical metric
- **Regional breakdown** — East, Midwest, Mountain, Pacific, South Central (salt/nonsalt)

**Trading note:** Natural gas storage is highly seasonal. The market evaluates the weekly change relative to: (1) consensus forecast, (2) year-ago change, and (3) 5-year average change. Being above or below the 5-year average heading into winter withdrawal season is a key positioning signal for [[natural-gas]] traders.

## Monthly and Periodic Reports

### Short-Term Energy Outlook (STEO)

| Detail | Value |
|--------|-------|
| **Release** | Monthly (typically first or second week) |
| **Coverage** | Supply, demand, price forecasts for all major energy commodities |
| **URL** | [eia.gov/outlooks/steo/](https://www.eia.gov/outlooks/steo/) |

**Key content:**
- U.S. and global supply/demand balance projections for crude oil, natural gas, and refined products
- Price forecasts (WTI, Brent, Henry Hub, retail gasoline)
- U.S. production forecasts by basin
- Consumption forecasts by sector
- Updated monthly with revisions to prior estimates

### Drilling Productivity Report (DPR)

| Detail | Value |
|--------|-------|
| **Release** | Monthly (around the 15th) |
| **Coverage** | Production estimates for major U.S. shale basins |
| **URL** | [eia.gov/petroleum/drilling/](https://www.eia.gov/petroleum/drilling/) |

**Key content:**
- Production per rig by basin (Permian, Eagle Ford, Bakken, Appalachia, Haynesville, Niobrara, Anadarko)
- New well oil and gas production estimates
- Legacy production decline rates
- Drilled-but-uncompleted (DUC) wells count — a leading indicator of future production

### Monthly Energy Review (MER)

| Detail | Value |
|--------|-------|
| **Release** | Monthly (around the 25th) |
| **Coverage** | Comprehensive U.S. energy statistics |
| **URL** | [eia.gov/totalenergy/data/monthly/](https://www.eia.gov/totalenergy/data/monthly/) |

The definitive monthly statistical compilation. Includes production, consumption, imports, exports, inventories, and prices for all energy commodities. More accurate than weekly estimates (which are subject to revision).

### Annual Energy Outlook (AEO)

Long-term (25+ year) projections of U.S. energy markets. Published annually with multiple scenarios. Useful for understanding structural trends (renewable energy growth, EV adoption, natural gas demand) but less relevant for short-term trading.

## API Access

| Detail | Value |
|--------|-------|
| **Base URL** | `https://api.eia.gov/v2/` |
| **Registration** | Free — requires API key (register at [eia.gov/opendata/](https://www.eia.gov/opendata/)) |
| **Rate limits** | Generous for individual use |
| **Formats** | JSON, XML |
| **Documentation** | [eia.gov/opendata/documentation.php](https://www.eia.gov/opendata/documentation.php) |

### Commonly Used API Series

| Series | API Route | Use Case |
|--------|-----------|----------|
| Crude oil inventories | `petroleum/stoc/wstk` | Weekly stock levels |
| Natural gas storage | `natural-gas/stor/wkly` | Weekly storage report |
| Crude oil prices | `petroleum/pri/spt` | Spot and futures prices |
| U.S. crude production | `petroleum/crd/crpdn` | Monthly production by state |
| Natural gas prices | `natural-gas/pri/sum` | Henry Hub and regional prices |
| Refinery utilization | `petroleum/pnp/unc` | Operable capacity utilization |
| Electricity generation | `electricity/rto/fuel-type-data` | Real-time generation by fuel |

### Python Example

```python
import requests

API_KEY = "your_api_key_here"
url = f"https://api.eia.gov/v2/petroleum/stoc/wstk/data/"
params = {
    "api_key": API_KEY,
    "frequency": "weekly",
    "data[0]": "value",
    "facets[product][]": "EPC0",  # Crude oil
    "facets[process][]": "SAE",   # Ending stocks
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "length": 52
}
response = requests.get(url, params=params)
data = response.json()
```

## How Traders Use EIA Data

The numbers themselves rarely matter as much as the **surprise versus consensus**. The reflexive workflow energy traders run on release:

1. **Establish the expectation.** Survey-based consensus (e.g. Bloomberg/Reuters/Platts polls) plus the Tuesday-night **API** preview for petroleum set the bar. The market is already positioned for the expected number.
2. **Trade the deviation.** A larger-than-expected crude **draw** (inventory fall) is bullish; a larger-than-expected **build** is bearish. The same logic runs in reverse for products. For [[natural-gas]], a smaller-than-expected injection (or a larger withdrawal) is bullish.
3. **Anchor to the 5-year average.** Absolute levels are read against the trailing 5-year seasonal band. Stocks below the band into peak demand season (winter heating for gas, summer driving for gasoline) signal tightness; above the band signals surplus.
4. **Decompose the petroleum report.** A headline crude draw driven only by a spike in exports or a refinery-run surge is "lower quality" than a draw driven by genuine demand; sophisticated traders read refinery utilization, implied demand, and the Cushing line, not just the headline.
5. **Map inventories to the curve.** Rising stocks (especially at **Cushing**, the WTI delivery point) push the front of the curve toward [[contango]] (storage rewarded); falling stocks tighten the prompt and push toward [[backwardation]]. The inventory print is therefore a direct read on curve shape, not just flat price. See [[inventory-cycle-analysis]].

### The Consensus / Surprise Quick Map

| Report outcome vs consensus | Crude / products | Natural gas |
|-----------------------------|------------------|-------------|
| Bigger draw / smaller build than expected | Bullish | Bullish (smaller injection / bigger withdrawal) |
| Bigger build / smaller draw than expected | Bearish | Bearish (bigger injection / smaller withdrawal) |
| In line with consensus | Muted; positioning and curve dominate | Muted |
| API and EIA diverge sharply | Elevated two-day volatility | n/a (no API gas preview) |

Inventory surprises also interact with speculative positioning -- pairing the EIA print with the CFTC [[cot-report-analysis|Commitments of Traders]] report shows whether a bullish surprise lands into already-crowded longs (limited upside, squeeze risk) or fresh, light positioning.

## Complementary EIA Tools

- **Today in Energy**: Daily articles with charts on current energy topics — useful for qualitative context
- **State Energy Data System (SEDS)**: State-level energy production, consumption, prices, and expenditures
- **International Energy Statistics**: Global production, consumption, and trade data by country
- **Electricity Data Browser**: Real-time and historical electricity generation, capacity, and pricing data

## Limitations

- Weekly data is estimated and subject to revision — the monthly revised figures are more accurate
- U.S.-centric — EIA covers the U.S. market comprehensively but global coverage is limited (use IEA for global data)
- Production estimates have a significant lag and revision cycle
- Storage data covers reported facilities only — "shadow inventories" (unreported stocks) are not captured
- API can be slow during high-traffic periods (immediately after major releases)
- Government shutdowns and federal holidays delay or suspend releases (see scheduling caveats above)

## Related

- [[eia]] -- the agency itself
- [[crude-oil]] -- primary market moved by the petroleum status report
- [[natural-gas]] -- driven by the weekly storage report
- [[gasoline]] / [[heating-oil]] -- refined products tracked in the petroleum report
- [[inventory-cycle-analysis]] -- framework for trading inventory data
- [[cot-report-analysis]] -- pair inventory surprises with positioning data
- [[contango]] / [[backwardation]] -- how inventory levels map to curve shape
- [[commodity-data-sources]] -- broader catalog of commodity data providers
- [[commodities]] -- commodity markets overview

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])
