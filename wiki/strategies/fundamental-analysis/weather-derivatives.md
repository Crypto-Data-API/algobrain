---
title: "Weather Derivatives"
type: strategy
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [commodities, weather, derivatives, temperature, hedging, cme, hdd, cdd, agriculture, utilities, uncorrelated]
aliases: ["Weather Trading", "Temperature Derivatives", "Weather Futures", "CME Weather Contracts"]
strategy_type: fundamental
timeframe: position|long-term
markets: [commodities]
complexity: advanced
backtest_status: untested
related: ["[[emissions-trading]]", "[[seasonal-spread-trading]]", "[[commodity-trading]]", "[[tail-risk-hedging]]"]
---

# Weather Derivatives

## Overview

Weather derivatives are financial instruments whose payoff is determined by measurable weather variables -- primarily temperature, but also rainfall, snowfall, wind speed, and hurricane events. The CME Group lists weather futures and options based on Heating Degree Days (HDD) and Cooling Degree Days (CDD) for major US and European cities. An HDD measures how cold a day is relative to 65 degrees F (each degree below 65 = 1 HDD), while a CDD measures warmth (each degree above 65 = 1 CDD). These contracts allow utilities, energy companies, agricultural firms, and ski resorts to hedge revenue exposure to weather. For traders and hedge funds, weather derivatives offer a rare source of returns **genuinely uncorrelated** to financial markets -- temperature has no relationship to the S&P 500. This makes them valuable portfolio diversifiers, though the market is niche, illiquid, and requires meteorological expertise.

## How It Works

1. **Analyze weather forecasts:** Use seasonal climate models (NOAA, ECMWF), historical temperature data, and proprietary weather analysis to forecast temperature deviations from normal for specific cities and time periods.
2. **Select the contract:** Choose HDD contracts for winter months (bet on cold/warm winter) or CDD contracts for summer months (bet on hot/cool summer). Contracts are city-specific (e.g., CME New York HDD November).
3. **Take a position:** Go long HDD futures if expecting a colder-than-normal winter (higher HDD = more heating demand). Go short if expecting warmer-than-normal. Each contract pays $20 per HDD point.
4. **Manage the position:** Monitor evolving weather forecasts. Long-range forecasts shift throughout the season, creating trading opportunities as the market reprices.
5. **Settlement:** Contracts settle against actual measured HDD/CDD at the reference weather station. No physical delivery -- pure cash settlement based on realized weather.

## Example

A weather derivatives trader analyzes NOAA's winter outlook and La Nina indicators suggesting a colder-than-normal winter for Chicago. CME Chicago HDD December futures trade at 1,050 (the market's expectation of cumulative December HDDs). Historical average: 1,080. The trader believes La Nina will push the actual to ~1,130. They go long 10 contracts at 1,050. Actual December HDDs come in at 1,120 (colder than market expected but slightly below the trader's forecast). Settlement profit: (1,120 - 1,050) x $20 x 10 = **$14,000.** The trade had zero correlation to the equity market sell-off that occurred simultaneously.

## Advantages

- **True non-correlation** -- weather outcomes have no relationship to stock, bond, or currency markets, providing genuine diversification
- **Quantifiable edge** -- superior weather forecasting (using better models or more data) creates a measurable analytical edge
- **Hedging utility** -- essential risk management tool for energy companies, agriculture, and weather-sensitive businesses
- **Mean-reverting** -- weather tends to revert to seasonal norms, making extreme forecasts less risky than in financial markets
- **Cash-settled simplicity** -- no physical delivery complications; payoff is purely based on measurable data

## Disadvantages

- **Low liquidity** -- weather derivatives markets are thin compared to financial futures; bid-ask spreads are wide and position sizes limited
- **Specialized knowledge required** -- profitable trading demands meteorological expertise beyond standard financial analysis
- **Basis risk** -- the reference weather station may not perfectly represent the geographic area you are hedging or speculating on
- **Limited markets** -- only a small number of cities and weather variables have liquid contracts
- **Model uncertainty** -- long-range weather forecasting remains inherently uncertain; even the best models have significant error margins
- **Niche participant base** -- dominated by a small number of specialized firms (hedge funds, reinsurers, utilities), limiting counterparty diversity

## See Also

- [[emissions-trading]] -- another environmental market strategy where weather affects demand dynamics
- [[seasonal-spread-trading]] -- seasonal patterns are fundamental to weather derivative analysis
- [[commodity-trading]] -- the broader asset class; weather directly impacts agricultural and energy commodities
- [[tail-risk-hedging]] -- weather derivatives can hedge against tail events like extreme cold or hurricanes
