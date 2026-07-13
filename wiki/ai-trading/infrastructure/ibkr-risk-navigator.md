---
title: "IBKR Risk Navigator"
type: source
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [risk-management, options, derivatives, technology]
aliases: ["Risk Navigator", "IBKR Risk Navigator", "IB Risk Navigator"]
source_type: data
source_url: "https://www.interactivebrokers.com/en/trading/risk-navigator.php"
confidence: high
related:
  - "[[options-concentration-risk]]"
  - "[[options-stress-testing]]"
  - "[[risk-management]]"
  - "[[beta-weighted-delta]]"
  - "[[options-greeks]]"
---

IBKR Risk Navigator is Interactive Brokers' built-in real-time portfolio risk and stress-testing tool, included free with any IBKR Pro account. It aggregates Greeks across an entire multi-asset portfolio (equities, options, futures, forex, bonds, mutual funds), shows beta-weighted delta exposure, runs single-name and market-wide stress scenarios, and decomposes risk by sector and by underlying. For IBKR clients running options books up to ~$5M-$10M of risk, Risk Navigator is often the only portfolio risk tool they need — the alternative is paying for a third-party system or building custom reports in Python.

## Pricing Tier

Free for any IBKR Pro account. There is no separate license fee. IBKR Lite users have access to a more limited version. Risk Navigator runs as a desktop application (TWS module) and as a web component within Client Portal.

## What It Produces

- **Real-time aggregated Greeks**: portfolio-wide net delta, gamma, vega, theta updated as positions and underlying prices move
- **Beta-weighted delta**: every position's delta converted to SPX-, NDX-, or QQQ-equivalent shares; shows the book's true market exposure
- **Sector exposure**: breakdown by GICS sector with notional and risk contribution
- **Underlying view**: groups all positions by underlying ticker, showing per-underlying Greeks rollup
- **Stress test scenarios**: pre-built and custom shocks
  - SPX +/- 5%, 10%, 15%, 20%
  - VIX +50%, +100%, +200%
  - Single-underlying shocks (e.g., NVDA -20%)
  - IV +/- shock by underlying or portfolio-wide
  - Time-decay forward (Greeks at +1 day, +1 week, +1 month)
- **Custom scenarios**: user-defined multi-leg shocks (e.g., "SPX -10%, VIX +30%, USD +5%, oil -10%")
- **Margin impact preview**: how the portfolio's margin requirement changes under each scenario
- **Concentration view**: positions ranked by contribution to portfolio risk
- **What-If trades**: simulate adding a new position and see the resulting Greeks / margin / stress P&L before placing the trade

## How It's Used in Practice

A typical IBKR options trader's daily workflow:

1. Open Risk Navigator in TWS at the start of the session
2. Check beta-weighted delta to SPX — is the book within target range?
3. Check net vega — short or long, and is the magnitude within budget?
4. Run the standard SPX -10%, VIX +50% stress scenario — what's the worst-case P&L?
5. Look at the underlying view — is any single ticker contributing >15-20% of risk?
6. Look at the sector view — is the book over-concentrated in semis / mega-cap tech?
7. For any new trade considered: use What-If to see how it changes the above

For active options traders running 20-100 positions, this workflow takes 5-10 minutes daily and catches most concentration problems before they become drawdowns.

## Relationship to Options Concentration Risk

Risk Navigator is the most accessible tool referenced in [[options-concentration-risk]] for the average serious options trader. It directly addresses several concentration dimensions:

- **Single-name concentration**: the underlying view groups positions by ticker and shows per-underlying Greeks
- **Sector concentration**: the GICS sector breakdown directly visible
- **Beta-weighted delta**: handles the index/beta concentration dimension
- **Vol regime concentration**: net vega is aggregated and visible
- **Stress testing**: the SPX +/- and VIX shock scenarios directly probe the "everything correlates in stress" failure mode

What Risk Navigator does *not* do well:

- **Factor decomposition**: no Barra-style style-factor breakdown; sector is the deepest grouping
- **Earnings cluster detection**: no built-in calendar view of earnings dates across positions
- **Custom correlation regimes**: stress tests use IBKR's default correlation assumptions; you cannot easily inject "stress correlation = 0.85"
- **Scenario history**: limited ability to save and compare scenarios over time
- **Vega-by-tenor**: net vega is a single number; no built-in term-structure breakdown of vega across DTE buckets

## Strengths

- **Free**: included with IBKR Pro at no extra cost
- **Real-time**: Greeks update with the market; not end-of-day batch
- **Multi-asset**: handles options, equities, futures, FX, bonds in one rollup
- **What-If**: pre-trade analysis of margin and risk impact is genuinely useful
- **Stress menu**: covers most of the scenarios a discretionary trader actually runs
- **Beta-weighted delta**: the headline metric for market exposure is built-in and well-implemented
- **Margin integration**: shows how stress scenarios affect margin requirements, not just P&L

## Limitations

- **IBKR-only**: works only on IBKR-held positions; if you have accounts at multiple brokers, Risk Navigator misses them
- **No factor models**: stops at sector-level decomposition; for true factor concentration analysis you need barra / axioma / northfield or a custom build
- **Scenario flexibility**: pre-built scenarios are useful, but truly bespoke multi-factor stress (e.g., "AI sector unwind + USD strengthening + rates +50bps") requires manual setup
- **UI**: TWS interface is dense and dated; learning curve for new users
- **Limited historical backtest**: the tool shows current state and stress; it does not back-test the same book through past stress regimes
- **Options-only depth**: extensive but not as deep as dedicated options-portfolio tools like [[deribit-position-builder]] or [[optionnet-explorer]] for crypto / equity options respectively

## Compared to Alternatives

| Tool | Strength | Weakness |
|------|----------|----------|
| **IBKR Risk Navigator** | Free, real-time, broad asset coverage | No factor models, IBKR-only |
| [[thinkorswim]] Beta-Weighted | Similar idea on TD/Schwab platform | TD-only |
| tastytrade portfolio Greeks | Good for tasty-style books | Less stress-testing depth |
| [[bloomberg-terminal]] PORT/MARS | Institutional standard | $24K/year |
| Custom Python | Maximum flexibility | Build cost |

For most serious options traders on IBKR, Risk Navigator is the first stop and often the only stop needed.

## Related

- [[options-concentration-risk]] — Risk Navigator is a primary tool for measuring concentration
- [[options-stress-testing]] — the stress-test functionality
- [[options-portfolio-construction]] — the broader workflow Risk Navigator supports
- [[beta-weighted-delta]] — the headline metric Risk Navigator computes
- [[options-greeks]] — what Risk Navigator aggregates
- [[risk-management]] — broader risk-management context
- [[thinkorswim]] — competing tool on TD / Schwab side

## Sources

- Interactive Brokers Risk Navigator product documentation
- IBKR TWS user guide and Risk Navigator help files
- Referenced in [[options-concentration-risk]] as the default IBKR-side concentration tool
