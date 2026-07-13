---
title: "Weather Derivatives Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-06-21
status: excellent
tags: [arbitrage, derivatives, commodities, quantitative]
aliases: ["Weather Arb", "HDD CDD Arbitrage", "Weather Index Arbitrage"]
related: ["[[weather-derivatives]]", "[[carbon-credit-arbitrage]]", "[[seasonal-spread-trading]]", "[[regulatory-arbitrage]]"]
strategy_type: quantitative
timeframe: swing
markets: [weather, energy]
complexity: advanced
backtest_status: live
edge_source: [analytical, informational, structural]
edge_mechanism: "Weather derivatives (CME HDD/CDD contracts, OTC weather options) are priced on historical climatology + forward weather forecasts. Specialist meteorology + statistical-modeling traders systematically beat forward curves by exploiting the diffuse-information edge between insurance providers and energy/agriculture hedgers."
data_required: [weather-station-historical-data, ecmwf-gfs-forecasts, hdd-cdd-pricing, otc-weather-quotes]
min_capital_usd: 5000000
capacity_usd: 500000000
crowding_risk: low
expected_sharpe: 1.2
expected_max_drawdown: 0.3
breakeven_cost_bps: 500
decay_evidence: "Weather derivatives market launched 1997 (Aquila Energy, a UtiliCorp subsidiary; Enron an early participant). CME futures traded since September 1999. Market never grew to mass scale; remains specialist niche. Climate change is increasing both demand and modeling difficulty."
---

# Weather Derivatives Arbitrage

Trading **weather-indexed financial contracts** to capture systematic mispricings between meteorological reality and market-priced forwards. The market is small (CME HDD/CDD futures + OTC bespoke contracts; estimated $5-15B annual notional) but highly specialized — requiring deep meteorology, climate-model expertise, and statistical arbitrage methodology. Pioneered in 1997 by **Aquila Energy** (a UtiliCorp subsidiary — not Enron, though Enron and Koch were early participants); CME launched standardized **Heating Degree Day (HDD)** futures in **September 1999**, with **Cooling Degree Day (CDD)** contracts following.

Active practitioners (current and historical): **Cumulus** (Peter Brewer's London fund, the largest dedicated weather trader), **Nephila** (insurance-linked), **DRW** (weather desk within the prop firm), **Speedwell Weather** (data/analytics and structuring), **Galaxy Weather Trading**, and earlier-era weather-risk carriers **Element Re** (XL Capital's weather unit, early 2000s) and **Glacier Re** (Swiss reinsurer with a weather book).

## The Instruments

Weather derivatives settle against an **index of observed weather** at a named reference station — not a price. The two workhorse indices:

| Index | Definition | Used by |
|-------|------------|---------|
| **HDD (Heating Degree Day)** | `max(0, 65°F − daily mean temp)`, summed over the period | Winter energy demand (heating) |
| **CDD (Cooling Degree Day)** | `max(0, daily mean temp − 65°F)`, summed over the period | Summer energy demand (cooling) |
| **CAT (Cumulative Average Temperature)** | Sum of daily mean temps | European convention |
| **Precipitation / snowfall** | Cumulative mm or inches at a station | Agriculture, ski resorts, construction |
| **ACE (Accumulated Cyclone Energy)** | Integral of storm wind energy over a season | Hurricane / reinsurance overlay |

| Contract attribute | CME HDD/CDD detail |
|--------------------|--------------------|
| **Exchange / launch** | [[cme-group|CME]] — HDD futures September 1999; CDD added shortly after |
| **Reference cities** | A defined set of US (and some European/Asian) weather stations |
| **Tick value** | $20 per index point (monthly futures); seasonal strip products also list |
| **Settlement** | Cash, to the official degree-day index computed from station data (Earth Networks / MDA) |
| **Period** | Monthly and seasonal strips |
| **OTC** | Bespoke station/period/payoff; the larger and more illiquid half of the market |

Because settlement is on a weather index, there is **no carry, no storage, and no physical** — the entire P&L is the difference between the forward-priced expectation and the realized index. That makes forecast skill the only durable input.

## Edge Source

**Analytical** + **informational** + **structural**.

- **Analytical:** Stat-arb on weather-station data + climate models is genuinely difficult; few traders have meteorological expertise.
- **Informational:** Public weather forecasts (ECMWF, GFS, JMA) update 4-6 times daily; market repricing lags.
- **Structural:** Most market participants are *hedgers* (energy utilities, agricultural producers, ski resorts, insurance companies) — they're price-takers, not arbitrageurs.

## Why This Edge Exists

Weather derivatives are inherently illiquid:

- **Bespoke OTC contracts** — utility A wants to hedge "JFK winter HDD vs 30-year normal" — requires customized contract.
- **Reference indexes vary** — HDD measured at LaGuardia vs JFK can differ by 50-200 degree-days per winter.
- **Cataclysmic-event risk** — single storm or hurricane can move the entire winter HDD by ~10-15%.
- **Re-insurance overlap** — many weather-derivatives buyers also use insurance products; fragmented capital.

Counterparty:
- Hedgers (utilities, agricultural producers) accepting "fair" pricing.
- Insurers re-selling weather risk.
- Speculators with sub-optimal models.

The arb: specialist desks model weather *better* than the market price implies, take the other side, and run portfolios across many weather indexes for diversification.

## Null Hypothesis

Under no-edge conditions, the forward HDD/CDD price equals the ensemble-forecast-implied expectation plus a hedger risk premium, and a trader's "proprietary" model signal has zero out-of-sample correlation with (settlement − forward). In that world the strategy's P&L is not alpha at all — it is simply the risk premium earned for selling weather insurance to utilities and farmers, which looks like steady income punctuated by catastrophic seasons (a short-tail-risk beta, replicable by mechanically writing weather protection with no model). Two tests distinguish edge from premium-collection: (1) does the model's fair value beat a naive blend of 10-year climatology + latest public ECMWF/GFS ensemble mean on out-of-sample settlement prediction (it must — those inputs are free and already in the price)? (2) is P&L positive *conditional on* seasons where the position was against the hedger flow, not just with it? If neither holds, returns are risk-bearing compensation, not analytical arbitrage.

## Variants

| Variant | Description | Period |
|---------|-------------|--------|
| **HDD/CDD vs forecast** | Compare forward HDD curves to ensemble weather forecasts; trade the spread | Days-weeks |
| **City-pair arb** | Pair trade between two cities' winter HDDs (e.g., NYC vs Boston) | Months |
| **Seasonal climatology arb** | Trade against market over-reactions to recent extreme weather | Seasonal |
| **El Niño / La Niña positioning** | Use ENSO forecasts to position regional-temperature derivatives | 6-12 months |
| **Hurricane-season options** | Trade Atlantic hurricane-energy indexes (ACE) | Hurricane season |
| **Snowfall derivatives** | Specific to ski resorts and northeast US winter retail | Winter season |
| **Crop-yield basis** | Combine weather derivatives with grain futures for crop-failure hedge | Growing season |

## Rules

1. **Build/license weather modeling capability** (ensemble forecasts, downscaling, climate models).
2. **Universe screening:** identify pricing dislocations between CME futures, OTC quotes, and your model's fair-value.
3. **Contract design:** for OTC trades, specify reference station, period, payoff structure precisely.
4. **Position sizing:** small per-contract (these are illiquid); diversify across multiple weather indexes.
5. **Continuous re-marking:** as forecasts update, mark positions to model.
6. **Settlement:** physical settlement against weather-station reference data.

## Implementation Pseudocode

```python
on forecast_update(forecast_data):
    # ECMWF / GFS / JMA ensemble forecast
    for contract in active_positions + universe:
        market_price = market.price(contract)
        model_fair_value = compute_fair_value(forecast_data, contract.reference_station, contract.period)
        spread = market_price - model_fair_value
        if abs(spread) > min_threshold * vol_adjustment:
            if spread > 0:
                short(contract, kelly_size)
            else:
                long(contract, kelly_size)

on settlement_period_end:
    actual_value = read_weather_station(contract.reference_station, contract.period)
    settle_position(actual_value)
```

## Indicators / Data Used

- ECMWF (European Centre for Medium-Range Weather Forecasts) ensemble forecasts.
- GFS (Global Forecast System, NOAA) ensemble forecasts.
- NOAA Climate Prediction Center (long-range, El Niño/La Niña).
- CME HDD/CDD futures (electronic + reference settlement).
- Weather Risk Management Association (WRMA) market data.
- *Speedwell Weather Derivatives* OTC quote service.

## Example Trades

**Texas February 2021 cold snap (Storm Uri).** ERCOT-area weather derivatives priced typical winter; actual HDD spike was 3-sigma above norm. Specialist weather-derivatives traders short power-area-specific contracts captured massive payouts. Some Texas energy utilities also lost billions on natural-gas contracts simultaneously.

**2023-2024 winter (warm El Niño).** Most heating-degree-day contracts settled below 30-year norms across Northern Hemisphere. Pre-positioned El-Niño-aware traders short HDD positions captured 30-50% on capital deployed.

**California summer 2022 heatwave.** CDD contracts on California cities (Los Angeles, San Francisco) settled 20%+ above forwards. Long CDD positions captured.

**Atlantic hurricane season 2017 (Harvey, Irma, Maria).** ACE (Accumulated Cyclone Energy) reached 224.9 — significantly above norm. Specialist hurricane-derivatives long positions paid out massive returns; insurance/reinsurance layer absorbed most of the cost (estimated $200B+ insured losses).

**California drought-driven snowpack derivatives (recurring).** Snowpack derivatives (Mount Bachelor, Lake Tahoe area) traded systematically below climatological norms during the 2012-2016 California drought; pre-positioned long contracts captured returns.

## Costs and Frictions

This is a **high-friction** strategy — the `breakeven_cost_bps: 500` frontmatter reflects bid-ask spreads measured in whole percent, not basis points, on illiquid OTC weather risk. Cost-aware budgeting must include:

| Cost / friction | Magnitude | Note |
|-----------------|-----------|------|
| **OTC bid-ask** | 2-10% of notional | Bespoke contracts; few counterparties |
| **CME HDD/CDD spread** | Wider than financial futures | Thin order book, $10-50M daily notional |
| **Data + modeling infra** | $1M+/yr | ECMWF/GFS licensing, downscaling compute, meteorology staff (`min_capital_usd: 5,000,000` for that reason) |
| **Credit/counterparty** | ISDA + collateral | OTC counterparty default risk |
| **Basis (station mismatch)** | Variable | Hedger's risk references one station; tradeable contract another |
| **Tail-event capital** | Large | A 3-sigma season can blow through a year of premium |

Because spreads are so wide, the edge must be large and persistent to survive — which is why only specialist desks with proprietary forecast skill (not just access to free public ensembles) can run it.

## Performance Characteristics

> **No fabricated returns.** The figures below are self-reported / press-reported ranges for named funds, not audited or guaranteed, and weather P&L is intrinsically lumpy (years of small premium income punctuated by catastrophic seasons). Treat as illustrative.

Cumulus Weather Fund (largest specialist) reported 12-25% annualized returns 2010-2020 (less data publicly available). Sharpe 0.8-1.5 (consistent with `expected_sharpe: 1.2`). Returns lumpy and event-driven; drawdowns in a bad season can approach the `expected_max_drawdown: 0.3` budgeted in frontmatter.

Insurance-linked weather strategies (Nephila) generate similar but tied to broader catastrophe-bond portfolio.

A key diagnostic from the [[#Null Hypothesis|null hypothesis]]: distinguish *alpha* (model beats the public-ensemble-implied fair value out of sample) from *risk premium* (steady income for writing weather protection that periodically detonates). Only the former is genuine arbitrage; the latter is short-tail-risk [[risk-management|beta]] and is replicable without any model.

## Capacity Limits

Per-contract OTC capacity $100K-$50M depending on city/period. CME HDD/CDD futures notional $10-50M daily. Strategy-level capacity ~$500M for largest specialist.

## What Kills This Strategy

- Climate change non-stationarity makes climatological priors unreliable.
- Insurance-market consolidation reduces hedger demand.
- Major loss event triggers regulatory scrutiny.
- Forecasting commoditization compresses analytical edge.

## Kill Criteria

Numerical conditions for retiring or pausing the book (see [[when-to-retire-a-strategy]]):

- **Model loses its edge:** the proprietary fair-value model fails to beat a naive blend of 10-year climatology + latest public ECMWF/GFS ensemble mean on out-of-sample settlement prediction for **2 consecutive seasons** — the public inputs are free and already in the price, so this means there is no alpha.
- **Sustained losing run:** ≥90% of model-driven trades net negative over a rolling 24 months.
- **Drawdown breach:** peak-to-trough drawdown exceeds the `expected_max_drawdown` budget of **30%** in a single season.
- **Spread blowout:** OTC bid-ask widens past ~10% such that even a correct model view cannot clear costs (`breakeven_cost_bps` exceeded structurally).
- **Climatological non-stationarity:** rolling climate baselines shift so fast that historical priors no longer calibrate — i.e., the model's residuals trend rather than mean-revert.

## Advantages

- True diversifier (weather is uncorrelated with market beta).
- ESG-positive (helps utilities, ag producers manage real risk).
- Specialist moat (meteorology + finance combination is rare).

## Disadvantages

- Highly specialized (geophysics + finance + risk-management).
- Tail-risk events can be devastating.
- Illiquid market.
- Requires multi-million-dollar infrastructure (data, computing, modeling).

## Sources

- WRMA (Weather Risk Management Association) annual report.
- CME Group HDD/CDD futures documentation.
- Speedwell Weather Derivatives platform.
- Cumulus Weather Fund / Nephila / Element disclosures (limited).
- *Weather Derivatives: Modeling and Pricing Weather-Related Risk* — Antonis Alexandridis, Achilleas Zapranis (textbook).
- **YouTube: "Weather Derivatives Explained" by various academic finance channels.**
- **YouTube: "Quantitative Climate Finance" lectures by Imperial College, Stanford.**
- **YouTube: "The Climate Risk Show" interviews with practitioners.**
- Verified via Perplexity (sonar), 2026-06-10: 1997 Aquila Energy (UtiliCorp, not Enron) first weather derivative; CME HDD futures launch September 1999, CDD following (cmegroup.com weather derivatives primer; projectfinance.law 2004 weather derivatives review).

## Related

- [[weather-derivatives]] -- the underlying instrument class (HDD/CDD/precip/ACE)
- [[seasonal-spread-trading]] -- adjacent seasonal commodity strategy
- [[seasonality]] -- the climatological-prior concept underneath the trade
- [[commodity-seasonality-patterns]] -- seasonal demand patterns weather drives
- [[carbon-credit-arbitrage]] -- another climate/ESG-adjacent arb
- [[crack-spread]] -- energy processor margin (weather drives the demand side)
- [[lean-hogs]] -- weather affects herd productivity and feed (heat stress, drought)
- [[corn]] / [[soybeans]] -- crop-yield basis trades combine weather + grain futures
- [[regulatory-arbitrage]] -- insurance vs derivative regulatory boundary
- [[risk-management]] -- tail-risk and short-volatility framing
- [[when-to-retire-a-strategy]] -- kill-criteria methodology
- [[cme-group]] -- exchange listing HDD/CDD futures
