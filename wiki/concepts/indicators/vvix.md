---
title: "VVIX (Cboe VVIX Index)"
type: concept
created: 2026-05-06
updated: 2026-06-11
status: good
tags: [volatility, indicators, options, risk-management, derivatives]
aliases: ["VVIX", "Cboe VVIX Index", "VIX of VIX", "Volatility of VIX"]
related: ["[[vix]]", "[[vol-of-vol]]", "[[volatility-trading]]", "[[volatility-risk-premium]]", "[[vix-calls]]", "[[vix-trading]]", "[[volga]]", "[[volmageddon]]"]
domain: [indicators, risk-management]
prerequisites: ["[[vix]]", "[[implied-volatility]]"]
difficulty: advanced
---

The **Cboe VVIX Index** measures the expected 30-day [[implied-volatility|implied volatility]] of the [[vix|VIX]] itself -- the implied volatility of VIX options. Often nicknamed "vol of vol," VVIX is calculated using the same model-free methodology as the VIX, but applied to the chain of options written on the VIX index rather than on SPX.

## Overview

The Cboe began publishing VVIX in 2012 (with backfilled history to 2007). It exists because VIX itself trades through a deep options market, and the prices of those VIX options reveal how volatile traders expect the VIX to be over the next month. VVIX is therefore a second-order volatility measure: a statement about the *jumpiness of fear*, not the level of fear itself.

VVIX is essential context for anyone trading VIX options or derivatives, because the implied volatility of VIX options is structurally much higher than that of SPX options (VIX itself is a far more volatile underlying than SPX), so VVIX numbers dwarf VIX numbers in absolute terms.

## Calculation Methodology

VVIX uses the same generalized variance-swap formula that produces the VIX, applied to:

- **Near-term and next-term VIX options** (Cboe-listed European-style options on the VIX index)
- **Out-of-the-money VIX puts and calls** across all liquid strikes
- **A weighted aggregation** that emphasizes options closest to the VIX forward price

The output is annualized in percentage-volatility terms. Because VIX has its own term structure (front-month VIX futures vs. spot VIX), VVIX implicitly references the volatility of the *forward* VIX, not the spot index.

## Interpretation

| VVIX Range | Interpretation |
|------------|----------------|
| Below 80 | Compressed vol-of-vol; very calm options-on-VIX market |
| 80-100 | Below-average; benign regime |
| 100-120 | Typical / long-run average |
| 120-150 | Elevated; jumpy VIX expected |
| 150+ | Crisis-level vol-of-vol; sharp regime change underway or anticipated |

The long-run average sits near 90-100. VVIX rarely falls below 70 even in extended low-VIX regimes, reflecting the persistent convexity premium embedded in VIX options.

## VVIX vs VIX

VVIX and VIX are correlated but distinct -- they measure different moments of different distributions:

- **VIX** = expected magnitude of SPX moves over 30 days
- **VVIX** = expected magnitude of VIX moves over 30 days

Common decoupling patterns:

- **VIX rises, VVIX falls** -- orderly volatility expansion. Markets are selling off in a measured way; the VIX path itself is smooth even though SPX vol is rising
- **VIX flat, VVIX rises** -- calm spot markets but increased optionality on VIX itself, often a precursor to regime change as traders bid VIX calls
- **Both rise** -- acute stress; the typical crisis pattern
- **VIX high but VVIX low** -- post-crisis, normalized fear; high but stable vol

The VVIX/VIX ratio is itself watched as a signal -- elevated ratios mark complacent markets where VIX is cheap but vol-of-vol is being bid.

## Trading Applications

**VIX option pricing.** VVIX is the headline number that traders use to gauge whether VIX call ladders, [[vix-calls|VIX calls]], or VIX put spreads are rich or cheap. Because VIX options are typically the underlying instrument for tail-hedging programs, VVIX directly drives the cost of tail insurance.

**Vol-of-vol trades.** Sophisticated funds run dedicated vol-of-vol books that go long or short VVIX exposure via VIX option structures (e.g., VIX butterflies, condors, calendar spreads).

**Regime detection.** Quantitative funds use VVIX as a regime filter. Compressed VVIX often coincides with crowded short-vol positioning -- a setup that historically precedes vol shocks like February 2018.

**Calibrating short-vol programs.** Systematic VIX-selling funds (writing VIX calls, selling VIX futures) reduce exposure when VVIX is depressed, since reflexive vol-of-vol expansion is the principal kill-mechanism for these strategies.

## VVIX in Crisis

- **February 2018 ("[[volmageddon]]")** -- VVIX exploded above 180 as VIX more than doubled in a single session, wiping out short-vol ETPs. The pre-event VVIX had been compressed in the 80-90 range, reflecting the crowded short-vol regime
- **March 2020 (COVID)** -- VVIX peaked near 210 as VIX rose to 82 and VIX option markets dislocated. The persistence of elevated VVIX through April-May 2020 reflected enduring uncertainty about the VIX path
- **August 2024** -- VVIX spiked above 170 during the early-August yen-carry-unwind volatility burst as VIX briefly touched 65 intraday

In each case, VVIX gave a sharper, earlier signal of regime change than VIX-level changes alone.

## Portfolio Use

For a professionally managed options portfolio, VVIX is used to:

- **Time VIX call ladders** -- buying VIX calls when VVIX is depressed makes the convexity premium cheaper
- **Calibrate [[options-premium-selling|vol-selling programs]]** -- avoiding short-vol positions when VVIX is suppressed *and* VIX term structure is steep [[contango|contango]] (a known crowded-trade signature)
- **Size [[volatility-risk-premium|VRP]] harvesting** -- the spread between VVIX and realized vol-of-VIX is itself harvestable, but rare and requires tight execution
- **Cross-asset signals** -- compare VVIX with single-name OVX (oil VIX) and GVZ (gold VIX) volatility-of-volatility to detect macro regime shifts

## Limitations

- **Liquidity dependency** -- VIX options markets, while deep, can become illiquid in the far wings, distorting VVIX during stress events
- **Methodology artifacts** -- like VIX itself, VVIX uses a strike-truncation rule that can introduce step changes when far-OTM strikes drop in or out of the calculation
- **Forward VIX, not spot** -- because VIX options settle to forward VIX (front-month VIX futures), VVIX does not directly measure spot-VIX vol
- **Limited history** -- robust VIX option data only extends back to ~2007, limiting backtests and regime studies
- **No direct tradable** -- there is no widely available VVIX ETF or futures contract; exposure must be manufactured through baskets of VIX options

## Related

- [[vix]] -- the underlying volatility index whose options drive VVIX
- [[volatility-trading]] -- the broader strategy family that uses VVIX as an input
- [[volatility-risk-premium]] -- the persistent IV-RV spread that VVIX helps quantify on the second-order surface
- [[vix-calls]] -- VIX call options whose pricing depends directly on VVIX
- [[vix-trading]] -- general VIX-product trading strategies
- [[implied-volatility]]
- [[volatility-of-volatility]]
- [[volmageddon]]

## Sources

- Cboe VVIX Index methodology documentation (Chicago Board Options Exchange)
- Mele, A. and Obayashi, Y., "The Price of Fixed Income Market Volatility" (2015) -- general framework for variance-swap-based volatility indices
