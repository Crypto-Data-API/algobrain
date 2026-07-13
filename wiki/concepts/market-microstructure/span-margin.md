---
title: "SPAN Margin"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [margin, leverage, market-microstructure, risk-management, futures, options, derivatives]
aliases: ["SPAN", "Standard Portfolio Analysis of Risk", "SPAN Margin", "CME SPAN", "SPAN 2"]
related: ["[[portfolio-margin]]", "[[reg-t-margin]]", "[[long-vol-vs-short-vol]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[xiv-velocity-shares]]", "[[ljm-preservation-and-growth]]", "[[vix-futures]]", "[[short-strangle]]", "[[variance-swaps]]", "[[leverage]]", "[[forced-liquidation]]", "[[gap-risk]]", "[[cme-group]]", "[[ice]]", "[[clearing-house]]", "[[initial-margin]]", "[[maintenance-margin]]", "[[risk-management]]"]
domain: [risk-management, market-microstructure, derivatives]
prerequisites: ["[[futures]]", "[[options]]", "[[leverage]]"]
difficulty: advanced
---

**SPAN** (**Standard Portfolio Analysis of Risk**) is the risk-array-based portfolio margining methodology developed by the [[cme-group|Chicago Mercantile Exchange]] in 1988 and now used by virtually every major futures exchange and clearing house in the world to set initial margin requirements on portfolios of futures and futures-options. SPAN computes the worst plausible one-day loss across a fixed grid of price-and-volatility scenarios, plus inter-month and inter-product spread credits, and sets margin equal to that worst-case scenario.

## Overview

Pre-SPAN, futures margins were "strategy-based" -- exchanges defined fixed margin amounts for specific position structures (a long future, a short future, a long calendar spread, a short straddle, etc.) and summed the requirements across positions. The system was conservative but capital-inefficient: a portfolio long one future and short an offsetting future of similar risk paid full margin on both legs, even though the net risk was small.

SPAN introduced **portfolio-level scenario analysis**. Instead of margining each position independently, the system revalues the entire portfolio across **16 standard scenarios** of price and volatility moves, identifies the worst loss, and sets margin equal to that loss (with adjustments for cross-product correlation and concentrated short-option exposure). This produces materially lower margin requirements for hedged or diversified portfolios -- and is the structural reason futures markets allow much higher gross leverage than [[reg-t-margin|Reg-T equity accounts]].

SPAN is now the global standard. CME, ICE, Eurex, JSE, ASX, and most other major derivatives clearing houses use SPAN or close derivatives of it. The methodology is licensed from CME Group; exchanges configure their own scenario grids and parameters within the SPAN framework.

## How It Works

SPAN computes initial margin as the maximum of three components:

```
SPAN_margin = max(0,
    Scanning_Risk + Inter_Month_Spread_Charge + Concentrated_Short_Charge
    - Inter_Commodity_Spread_Credit
) + Net_Option_Premium
```

### 1. Scanning Risk: the 16 standard scenarios

The core of SPAN is the **risk array**: a grid of 16 hypothetical price/volatility moves applied to each contract. The grid combines:

- **7 levels of price change**: -3, -2, -1, 0, +1, +2, +3 "scanning ranges" (the scanning range is set per-contract, e.g., $5,000 for a S&P 500 e-mini equivalent, scaled to ~3 standard deviations)
- **2 levels of volatility change**: vol up, vol down (typical ranges +/-10-15% relative)
- **An "extreme move" pair**: -2x scanning range and +2x scanning range, with each weighted at **35%** (rationale: these are tail scenarios the portfolio could plausibly experience but are less likely than the main 14)

The 16 scenarios are:

| # | Price move | Vol move |
|---|---|---|
| 1 | 0 | up |
| 2 | 0 | down |
| 3 | +1/3 | up |
| 4 | +1/3 | down |
| 5 | -1/3 | up |
| 6 | -1/3 | down |
| 7 | +2/3 | up |
| 8 | +2/3 | down |
| 9 | -2/3 | up |
| 10 | -2/3 | down |
| 11 | +1 | up |
| 12 | +1 | down |
| 13 | -1 | up |
| 14 | -1 | down |
| 15 | +2 (35% weighted) | unchanged |
| 16 | -2 (35% weighted) | unchanged |

For each scenario, every position in the portfolio is revalued (using a pricing model -- Black for futures options, etc.) and the **portfolio-level P&L** is computed. The **scanning risk** is the maximum loss across the 16 scenarios.

### 2. Inter-month spread charge

Because scanning risk treats different expirations as perfectly correlated within a product, calendar spreads are over-credited. SPAN adds back a charge for net long/short imbalances across expiration months, scaled by an "inter-month spread charge" parameter set per product.

### 3. Inter-commodity spread credit

Conversely, SPAN gives credits for offsetting positions in correlated products (e.g., long crude oil vs short heating oil). The credit is a percentage of the lesser leg, set by the exchange based on historical correlation.

### 4. Concentrated short option charge

For deeply OTM short options, the standard scanning range may not capture the actual tail loss. SPAN adds a separate "concentrated short option" charge to ensure short-option-heavy portfolios are not under-margined.

### 5. Net option value

Long options have positive value; short options have negative value. SPAN credits long-option value to margin (you have collateral) and adds short-option value to margin (you owe premium). This is also the reason long-option positions in SPAN accounts can be capital-efficient.

## SPAN vs Reg-T vs Portfolio Margin

| Dimension | [[reg-t-margin|Reg-T]] | [[portfolio-margin|Portfolio Margin (TIMS)]] | SPAN |
|---|---|---|---|
| **Used for** | Equity options accounts <$110K, retail | Equity options accounts >$110K (US) | Futures and futures-options accounts globally |
| **Methodology** | Strategy-based: fixed % per position | Risk-based: Theoretical Intermarket Margining System (TIMS) computes worst-case across price/vol scenarios | Risk-array-based across 16 scenarios |
| **Scenario grid** | None (formulaic) | -15% to +15% in 1% steps for equities; -8% to +6% for indices | -3 to +3 scanning ranges plus 2 extreme-move scenarios, each at 2 vol levels |
| **Cross-product offsets** | Limited / none | Within "product groups" | Inter-commodity credits available |
| **Typical leverage on short index strangle** | ~5-7x notional | ~6-10x | ~8-15x |
| **Re-margining cadence** | End of day | End of day, plus intraday triggers | Multiple times daily; some exchanges intra-session |
| **Short-vol leverage in calm regime** | Restrictive | High | Highest |
| **Re-pricing in stress** | Static | Steps up via portfolio-margin model | Sharp ratchets via parameter-set updates |
| **Account minimum** | None | $110K equity (US PM accounts) | Per-broker (typically $25K+) |

Critical distinctions in practice:

- **Reg-T** treats each position individually with a strategy-rule book. A short SPX put requires margin = 20% of underlying - OTM amount + premium (or 10% of strike). It does not credit any portfolio-level offset.
- **Portfolio margin** (run by [[options-clearing-corporation|OCC]] under the TIMS framework, used by retail US equity-option brokers above the $110K threshold) shocks the underlying across a defined grid of price moves at constant vol, then scenarios with vol up/down, and takes worst-case. It is roughly twice as efficient as Reg-T but follows a different scenario philosophy than SPAN.
- **SPAN** is risk-array based across both price and vol simultaneously; it gives **the largest leverage** in calm regimes and is the dominant methodology for futures.

A short SPX strangle that requires ~$30K of buying power under Reg-T might require ~$15K under TIMS portfolio margin and ~$5K-$8K of [[vix-futures]]-equivalent SPAN margin -- which is part of why so much retail short-vol activity has migrated from equity options to futures-options venues.

## Why SPAN Allows Higher Calm-Regime Leverage

Three structural reasons SPAN is the most permissive of the three:

1. **The scanning ranges are calibrated to roughly 3 standard deviations of recent price moves.** In calm regimes, the parameters are recalibrated downward as recent vol falls, shrinking the scenarios and the resulting margin requirement. A 6-month low-vol regime will see margin requirements drift 30-50% lower than in a normal-vol regime.
2. **Inter-commodity spread credits compress hedge-book margin.** A correlated long/short pair can be margined at a fraction of either leg standalone.
3. **Risk-arrays use parametric pricing models.** Short OTM options that would carry conservative strategy-margin under Reg-T are revalued through a pricing model in SPAN; in calm regimes, that model produces a lower worst-case loss than the fixed Reg-T formula.

## Why SPAN Reprices Margin Sharply in Stress

The mirror image: SPAN can multiply margin requirements 3-5x in a single session during a vol shock.

- **Scanning range expands.** When recent realized vol jumps, the exchange recalibrates the per-product scanning range upward. A move from "calm" to "crisis" parameters can raise scanning range by 50-200%.
- **Vol-shock scenarios reprice short options sharply.** The extreme-move scenarios (#15 and #16) become more punishing as scenario vol expands.
- **Inter-commodity correlations may be revoked.** Some clearinghouses suspend or reduce inter-commodity credits during stress, stripping away portfolio-level offsets.
- **Concentrated-short-option charges activate.** Deep-OTM shorts that did not trigger the concentration charge in calm regimes can do so when vol spikes.

The combination produces the **margin ratchet**: a trader who was calm-regime-leveraged 12x suddenly faces margin requirements that demand they post 3-5x more collateral overnight, often forcing liquidation at the worst possible prices. This is the central mechanism behind:

- **[[volmageddon|February 5-6, 2018]]**: short-VX positions that had margin in the $5K range pre-event saw margin requirements multiply 4-6x as VX SPAN parameters were revised mid-session, contributing to forced liquidations.
- **March 2020 (COVID)**: CME raised initial margin on equity-index futures multiple times in two weeks, in some cases more than doubling requirements.
- **[[vix-august-2024-spike|August 5, 2024]]**: similar ratchet on VX and SPX-options-cleared-as-futures positions.

The lesson, repeated since 1987: **margin in calm regimes is not a measure of risk; it is a measure of recent-history vol**. Sizing positions to maximum allowed margin in calm regimes is a leveraged bet that calm regimes will continue.

## SPAN 2: The 2024-2026 Replacement

CME has been rolling out **SPAN 2** since 2020, with a phased migration of products through 2024-2026. SPAN 2 is a substantial methodological upgrade rather than a parameter recalibration:

- **Filtered Historical Simulation** rather than parametric scenarios. SPAN 2 takes ~7-10 years of historical price/vol changes, scales them by current vol estimates, and revalues the portfolio across thousands of historical-shock scenarios. The 99% (or 99.7%, depending on configuration) VaR across that distribution becomes the margin.
- **Expected Shortfall** option in addition to VaR. SPAN 2 supports configuring margin as Expected Shortfall (average loss in the worst k% tail) instead of single-point VaR -- closer to Basel-style risk metrics.
- **Liquidity-adjusted margining**. SPAN 2 incorporates an explicit liquidity add-on for large positions in less-liquid contracts.
- **Concentration risk** measured continuously rather than at thresholds.
- **More granular treatment of options Greeks and term structure**.

The CME began onboarding products to SPAN 2 in 2020 (commodity products first), expanded through equity-index and interest-rate futures in 2022-2024, and is targeting full migration through 2026. Some reports (industry analyses, 2023-2024) suggest SPAN 2 produces moderately higher base-case margin (~5-15% on average) but better-calibrated stress-case margin, reducing the calm-to-stress ratchet that hurt traders in 2018 and 2024.

ICE Clear runs its own analogous framework (IRM 2 / ICE Risk Model). The European clearing houses (LCH, Eurex Clearing) have been moving toward similar Filtered Historical Simulation models in parallel.

## Failure Modes and Considerations

1. **Parameter staleness.** SPAN parameters are reset by exchanges, typically weekly or monthly, with off-cycle updates during stress. Between resets, fast vol changes can outrun the parameter set, leaving margin under-priced.
2. **Forced liquidation cascades.** When SPAN reprices upward sharply, brokers issue margin calls; clients who cannot meet calls have positions liquidated at market. Liquidations into thin markets (especially overnight in [[vix-futures]]) feed back into prices, triggering further margin increases. The reflexive loop was visible in February 2018 and August 2024.
3. **Cross-product correlation breakdown.** Inter-commodity credits assume historical correlations. In stress, correlations regime-shift (everything sells off together); credits granted in calm become understated risk in stress. Most clearinghouses have automated triggers to reduce or eliminate cross-product credits during regime shifts.
4. **Product-specific quirks.** Some contracts (notably [[vix-futures|VX]]) have non-standard SPAN configurations to account for the underlying being itself a vol measure. Traders must read the specific risk-array parameters per product.
5. **SPAN 2 transition risk.** As products migrate, traders must update infrastructure to consume the new parameter format. Several brokerages reported transitional issues in 2022-2023 as commodity SPAN 2 was rolled out.
6. **Excess SPAN ≠ free capital.** Excess margin in a SPAN account belongs to the trader but cannot reliably fund opportunistic adds in stress, because the same shock that creates the opportunity also reprices the SPAN margin needed to take it. Calm-regime "excess" disappears in the same session that opportunity arises.

## Practical Implications for Traders

For [[short-vol|short-vol]] practitioners, the SPAN ratchet defines the practical leverage ceiling:

- **Size for stress-regime SPAN, not calm-regime SPAN.** A safe rule: assume margin will multiply 3-5x in a vol shock and ensure the account can meet that without forced liquidation.
- **Watch the parameter file.** Exchanges publish SPAN parameter files (".pa2" format) that describe scanning ranges and vol shifts per product. Tracking changes between releases foreshadows upcoming margin changes.
- **Diversify across SPAN-eligible products** to capture inter-commodity credits, but stress-test under correlation breakdown.
- **Maintain explicit excess collateral** -- typically 50-100% of required SPAN -- to absorb the ratchet without selling into a panic.

This is the operational meaning of [[long-vol-vs-short-vol|"short vol is capital-efficient until it isn't"]]: the efficiency is real in calm regimes; the unwind is also real in stress.

## Related

- [[portfolio-margin]] -- the equity-options-account analog (TIMS)
- [[reg-t-margin]] -- the legacy strategy-based US retail framework
- [[long-vol-vs-short-vol]] -- the strategy context where SPAN matters most
- [[volmageddon]], [[vix-august-2024-spike]] -- canonical examples of the SPAN ratchet
- [[xiv-velocity-shares]], [[ljm-preservation-and-growth]] -- vehicles destroyed by the SPAN ratchet
- [[vix-futures]] -- the canonical SPAN-margined product where short-vol concentration risk lives
- [[short-strangle]] -- the structure most affected by SPAN reprice-in-stress
- [[variance-swaps]] -- OTC alternative; not SPAN-margined but follows analogous principles
- [[cme-group]], [[ice]] -- the major exchanges and clearinghouses
- [[clearing-house]] -- institutional context
- [[initial-margin]], [[maintenance-margin]] -- adjacent margin concepts
- [[forced-liquidation]] -- the operational consequence
- [[gap-risk]] -- the risk that SPAN attempts to bound but does not eliminate

## Sources

- CME Group. *SPAN Methodology* (current edition) -- the authoritative methodology document; defines the 16 scenarios, scanning ranges, inter-month and inter-commodity logic.
- CME Group. *SPAN 2 Methodology Whitepaper* (2020-2024 versions) -- describes the Filtered Historical Simulation replacement methodology.
- Options Clearing Corporation. *TIMS Methodology* -- the equity-options portfolio margin framework, contrasted with SPAN.
- US Federal Reserve Regulation T (12 CFR 220) -- the Reg-T framework that governs strategy-based margin in retail US equity accounts.
- Hull, John. *Options, Futures and Other Derivatives* (10th ed.) -- standard textbook treatment of margin methodologies.
- US CFTC and SEC. *Joint Staff Report on the February 5, 2018 VIX Volatility Event* -- documents the role of margin reprice in the Volmageddon cascade.
- Various exchange parameter file releases (.pa2) and risk notices describing margin parameter updates during March 2020, August 2024, and other stress events.
