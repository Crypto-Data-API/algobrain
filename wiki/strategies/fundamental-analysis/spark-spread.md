---
title: "Spark Spread"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [spark-spread, natural-gas, electricity, power-generation, energy, commodity-spread, utility]
aliases: ["Spark Spread Trading", "Power Generation Margin", "Gas-to-Power Spread"]
strategy_type: fundamental
timeframe: swing|position
markets: [commodities]
complexity: intermediate
backtest_status: untested
related: ["[[crack-spread]]", "[[crush-spread]]", "[[seasonal-spread-trading]]", "[[event-driven-trading]]", "[[basis-trading]]"]
---

# Spark Spread

## Overview

The spark spread represents the **power generation margin** -- the theoretical profit a gas-fired power plant earns by converting natural gas (fuel input) into electricity (output). Trading the spark spread means taking positions in natural gas and electricity markets to profit from changes in this generation margin. When the spark spread is wide, power plants are profitable; when it narrows or goes negative, it is uneconomical to run gas plants, and they may shut down.

The spark spread is a critical concept in **energy markets** and electricity trading. It is analogous to the [[crack-spread]] in petroleum (crude to gasoline/diesel) and the [[crush-spread]] in agriculture (soybeans to meal/oil). The key difference is that electricity cannot be economically stored, making the spark spread highly sensitive to real-time supply/demand conditions, weather, and grid constraints.

The formula accounts for the **heat rate** of the power plant -- how efficiently it converts gas BTUs to electricity MWh. A more efficient plant (lower heat rate) has a wider spark spread at the same gas and power prices. Traders, utilities, and independent power producers (IPPs) all trade spark spreads -- utilities to hedge generation margins, IPPs to lock in profits, and speculators to profit from expected changes in energy market dynamics.

## How It Works

### Spark Spread Calculation
**Spark Spread ($/MWh) = Electricity Price ($/MWh) - [Natural Gas Price ($/MMBtu) x Heat Rate (MMBtu/MWh)]**

Where:
- **Electricity Price:** Locational marginal price (LMP) at the relevant node or hub (e.g., PJM Western Hub, ERCOT North).
- **Natural Gas Price:** Henry Hub or regional basis (e.g., Transco Zone 6 for the Northeast).
- **Heat Rate:** Thermal efficiency of the plant. Typical gas turbines: 7,000-10,000 BTU/kWh (7-10 MMBtu/MWh). Combined-cycle plants are more efficient (~7,000) than simple-cycle peakers (~10,000).

**Example:** Power at $45/MWh, gas at $3.50/MMBtu, heat rate 8,000 BTU/kWh (8 MMBtu/MWh).
Spark spread = $45 - ($3.50 x 8) = $45 - $28 = **$17/MWh**.

### Dark Spread (Coal Variant)
The **dark spread** is the coal-fired equivalent: Electricity Price - (Coal Price x Heat Rate). As coal plants retire and gas dominates, the spark spread has become more important. The **clean spark spread** subtracts carbon emission costs (EU ETS, RGGI) from the standard spark spread.

### Key Market Dynamics
- Electricity is **not storable** (at scale), so the spark spread can swing wildly with real-time demand (heat waves, cold snaps) and supply (plant outages, transmission congestion).
- **Merit order effect:** Power plants are dispatched in order of marginal cost. Gas plants typically set the marginal price, so the spark spread reflects the marginal generator's economics.
- In markets with high renewable penetration (ERCOT, CAISO), spark spreads can collapse during high solar/wind output (the "duck curve") and spike during low renewable periods.

## Rules / Application

### Going Long the Spark Spread (Expecting Wider Margins)
1. **Buy electricity futures** (or power forwards) at the relevant hub for the target delivery month.
2. **Sell natural gas futures** at the corresponding gas hub, sized by the heat rate. For a 8,000 BTU/kWh plant: sell 8 MMBtu of gas per 1 MWh of power.
3. **Rationale:** Profit if power prices rise faster than gas (demand surge, plant outages, low renewable output).
4. **Timing:** Enter ahead of peak demand seasons (summer for cooling load, winter for heating-driven power demand in gas-heated regions).

### Going Short the Spark Spread (Expecting Narrower Margins)
1. **Sell electricity futures.**
2. **Buy natural gas futures** (heat-rate adjusted).
3. **Rationale:** Profit if gas prices rise faster than power (LNG export surge, pipeline disruption) or power prices fall (high renewable output, mild weather).

### Key Drivers to Monitor
- **Weather forecasts:** Temperature is the single biggest driver of electricity demand. Heat waves and polar vortexes cause spark spread spikes.
- **Natural gas storage reports:** Weekly EIA Natural Gas Storage Report. Low storage = higher gas prices = compressed spark spread (unless power prices rise equally).
- **Renewable output:** Solar and wind forecasts for the region. High renewable generation suppresses power prices and spark spreads.
- **Plant outage schedules:** Planned maintenance (spring/fall) and unplanned outages reduce supply, widening spreads.
- **Transmission congestion:** Locational constraints can cause spark spreads to vary dramatically across nodes within the same grid.

## Example

**Setup:** Long spark spread in ERCOT (Texas) entering June ahead of summer heat.

1. **June 1:** ERCOT North Hub power at $38/MWh. Henry Hub gas at $2.80/MMBtu. Heat rate assumption: 8,500 BTU/kWh.
2. **Spark spread:** $38 - ($2.80 x 8.5) = $38 - $23.80 = **$14.20/MWh**.
3. **Enter:** Buy 50 MW of July ERCOT power forwards, sell corresponding gas futures (50 x 8.5 x 24 x 31 = 316,200 MMBtu for the month).
4. **July 15:** A heat wave pushes ERCOT temperatures above 105F. Power spikes to $85/MWh (average for the week). Gas rises modestly to $3.10/MMBtu.
5. **Spark spread during heat wave:** $85 - ($3.10 x 8.5) = $85 - $26.35 = **$58.65/MWh**.
6. **Exit partial position** during the spike. Average exit spark spread: $45/MWh.
7. **Profit:** ($45 - $14.20) x 50 MW x 24 hrs x 7 days = **$1,077,600 for the week** (institutional-scale trade).

## Advantages

- Directly trades **power generation economics** -- a fundamental, well-understood relationship in energy markets
- Strong **seasonal patterns** (summer/winter demand peaks) provide recurring, predictable trade opportunities
- **Weather sensitivity** creates frequent mispricings and volatility that skilled traders can exploit
- Used by utilities and IPPs for hedging, ensuring deep institutional liquidity in the spread
- The spread captures the core economic driver of electricity markets -- the marginal cost of generation
- Can be traded across multiple regions (PJM, ERCOT, CAISO, European hubs) for geographic diversification

## Disadvantages

- **Electricity markets are complex:** Locational marginal pricing, grid congestion, ancillary services, and capacity markets add layers of complexity beyond simple commodity trading
- **Non-storability of electricity** means the spread can exhibit extreme spikes ($10 to $10,000/MWh in ERCOT during Winter Storm Uri 2021) -- position sizing must account for tail risk
- Requires **specialized market access:** electricity futures/forwards are traded OTC or on ICE/NYMEX, not as accessible as equity or FX markets
- **Regulatory risk:** Grid operator rules (ERCOT, PJM) change frequently, affecting pricing mechanisms and spark spread dynamics
- Heat rate assumptions may not match actual plant efficiency, creating basis risk between the traded spread and physical economics
- Large contract sizes and margin requirements make this an **institutional-scale strategy** -- not accessible to most retail traders
- **Renewable energy growth** is structurally compressing average spark spreads while increasing their volatility -- a challenging combination

## See Also

- [[crack-spread]] -- the petroleum refining margin equivalent
- [[crush-spread]] -- the agricultural processing margin equivalent
- [[seasonal-spread-trading]] -- seasonal demand patterns driving spark spread opportunities
- [[event-driven-trading]] -- weather events and policy changes as spark spread catalysts
- [[basis-trading]] -- regional gas and power basis differentials that affect spark spreads
