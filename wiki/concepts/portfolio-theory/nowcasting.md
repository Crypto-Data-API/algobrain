---
title: "Nowcasting"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [macro, quantitative, machine-learning, event-driven]
aliases: ["Nowcasting", "Now-casting", "Nowcast"]
domain: [macroeconomics, quantitative]
prerequisites: ["[[gdp]]", "[[economic-indicators]]"]
difficulty: intermediate
related: ["[[gdp]]", "[[nonfarm-payrolls]]", "[[cpi-release]]", "[[pmi]]", "[[leading-indicators]]", "[[economic-indicators]]", "[[recession-indicators]]", "[[sahm-rule]]", "[[fomc-meetings]]", "[[macro-analysis]]", "[[alternative-data]]", "[[kalman-filter]]", "[[machine-learning]]", "[[yield-curve]]"]
---

**Nowcasting** is the estimation of the present (or very recent past and near future) state of an economic variable — most commonly current-quarter [[gdp|GDP]] growth — before the official statistic is released, by continuously updating a model as higher-frequency data arrive. The term, borrowed from meteorology ("forecasting the weather right now"), reflects the fact that official macro data are published with long lags (US GDP arrives ~4 weeks after quarter-end), so investors and central banks build statistical models that synthesize the steady drip of monthly and weekly releases into a real-time estimate. The best-known public examples are the **Atlanta Fed's GDPNow** and the **New York Fed's Staff Nowcast**.

## Overview

The core problem nowcasting solves is the **ragged edge** of macro data: at any given moment, dozens of indicators have been released for overlapping but non-aligned periods, at mixed frequencies (daily, weekly, monthly, quarterly), with different publication lags. A nowcast fuses these into a single coherent estimate of the not-yet-published target and updates it each time a new data point lands. Where a forecast looks months or quarters ahead, a nowcast is concerned with the *current* period and shrinks its error as more of that period's data become known.

## How It Works

Several statistical architectures are used:

- **Dynamic factor models (DFMs)** — the dominant academic approach (Giannone, Reichlin, Small, 2008). Many noisy indicators are assumed to be driven by a small number of unobserved common factors capturing the business cycle. A **[[kalman-filter|Kalman filter]]** handles the mixed frequencies and missing observations on the ragged edge, extracting the common factor and mapping it to the target (e.g. GDP). The NY Fed Staff Nowcast is a DFM.
- **Bridge / MIDAS regressions** — regress the low-frequency target (quarterly GDP) on high-frequency predictors using mixed-data-sampling (MIDAS) weighting, "bridging" monthly indicators to the quarterly figure.
- **Accounting/bottom-up models** — GDPNow mimics the BEA's own GDP construction, building up the components (consumption, investment, net exports, government) from their source monthly indicators (retail sales, industrial production, trade balance, construction spending) and summing them.
- **Machine-learning ensembles** — gradient-boosted trees and neural nets trained on wide feature sets including [[alternative-data]]; flexible but harder to interpret and prone to [[overfitting]].

A key behavioral property: as the quarter progresses and more data arrive, the nowcast's **revision variance falls** and the estimate converges toward the eventual official print. Early in the quarter the nowcast is mostly model prior; by the end it is mostly hard data.

## Inputs

Typical nowcast inputs, in rough order of release within a month:

- **Surveys / soft data** (timely, noisy): [[pmi|ISM/S&P Global PMIs]], regional Fed surveys (Empire State, Philly Fed), consumer confidence
- **Labor**: [[nonfarm-payrolls|nonfarm payrolls]], jobless claims (weekly — very timely), JOLTS
- **Activity / hard data**: retail sales, industrial production, durable goods, housing starts, trade balance, construction spending
- **Prices**: [[cpi-release|CPI]], PCE deflator (feed real-vs-nominal conversion)
- **Alternative / real-time**: card-spending aggregates, mobility data, electricity demand, shipping/port volumes, web-scraped prices — increasingly used to nowcast at weekly or daily resolution

## Trading & Portfolio Relevance

- **Front-running the official print**: a credible nowcast lets a macro trader position ahead of GDP, payrolls, or inflation releases, and — more usefully — frames whether a given monthly release is a *surprise* relative to the model-implied trajectory rather than relative to the static consensus.
- **Recession timing**: nowcasts feed [[recession-indicators|recession monitors]]; a sharply deteriorating GDPNow alongside the [[sahm-rule|Sahm Rule]] and an inverted [[yield-curve|yield curve]] is a higher-conviction recession signal than any single indicator.
- **Fed reaction-function modeling**: because the [[fomc-meetings|FOMC]] is data-dependent, a nowcast of growth and inflation is implicitly a nowcast of the policy path — useful for trading [[fed-funds-futures|Fed funds futures]] and front-end rates.
- **Event-vol context**: knowing the nowcast-implied expectation for [[nonfarm-payrolls|NFP]] or [[cpi-release|CPI]] sharpens the read on how an options surface should react to the print (see the event-vol mechanics on those pages).
- **Caveats**: nowcasts are revised heavily early in the quarter and can be badly wrong at turning points (they extrapolate momentum and lag regime breaks); soft-data inputs are noisy; and the "wisdom" is only as good as the indicator mix. GDPNow's wide early-quarter swings are a standing reminder to treat the estimate as a distribution, not a point.

## Notable Public Nowcasts

- **Atlanta Fed GDPNow** — accounting/bottom-up GDP nowcast, updated several times a week as components release; widely watched and freely published.
- **New York Fed Staff Nowcast** — DFM-based; was a flagship public nowcast (publication paused in 2021, methodology remains a reference standard).
- **St. Louis Fed Economic News Index**, **Cleveland Fed inflation nowcasting** — sector- and inflation-specific nowcasts.
- **Private sector**: bank research desks and macro funds run proprietary nowcasts, often augmented with [[alternative-data]].

## Related

- [[gdp]] — the most common nowcast target
- [[economic-indicators]], [[leading-indicators]] — the input universe
- [[nonfarm-payrolls]], [[cpi-release]], [[pmi]] — high-frequency inputs and targets
- [[recession-indicators]], [[sahm-rule]] — downstream uses
- [[yield-curve]] — complementary recession signal
- [[fomc-meetings]], [[fed-funds-futures]] — the policy path nowcasts inform
- [[macro-analysis]] — the broader discretionary framework
- [[alternative-data]] — newer high-frequency inputs
- [[kalman-filter]] — the engine of dynamic factor nowcasts
- [[machine-learning]] — ML-based nowcasting approaches

## Sources

- Giannone, D., Reichlin, L., Small, D. (2008). *"Nowcasting: The Real-Time Informational Content of Macroeconomic Data."* *Journal of Monetary Economics* 55 (4): 665–676.
- Bańbura, M., Giannone, D., Modugno, M., Reichlin, L. (2013). *"Now-Casting and the Real-Time Data Flow."* *Handbook of Economic Forecasting*, Vol. 2A.
- Federal Reserve Bank of Atlanta — *GDPNow methodology and data.* https://www.atlantafed.org/cqer/research/gdpnow
- Federal Reserve Bank of New York — *Nowcasting Report (Staff Nowcast methodology).*
- Higgins, P. (2014). *"GDPNow: A Model for GDP 'Nowcasting'."* FRB Atlanta Working Paper 2014-7.
