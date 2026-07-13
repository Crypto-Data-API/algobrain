---
title: "thinkorswim"
type: entity
created: 2026-04-22
updated: 2026-06-21
status: excellent
tags: [options, company, education]
aliases: ["TOS", "Think or Swim", "thinkorswim by TD Ameritrade"]
entity_type: company
founded: 1999
headquarters: "Chicago, IL, USA"
website: "https://www.schwab.com/trading/thinkorswim"
related:
  - "[[tom-sosnoff]]"
  - "[[interactive-brokers]]"
  - "[[tastytrade]]"
  - "[[implied-volatility]]"
  - "[[iron-condor]]"
  - "[[trading-platforms]]"
  - "[[options-position-sizing]]"
  - "[[credit-spread]]"
---

**thinkorswim** (TOS) is an advanced options and equities trading platform originally created by [[tom-sosnoff]] and Scott Sheridan in 1999. It was acquired by TD Ameritrade for approximately $750 million in 2009 and is now part of [[charles-schwab|Charles Schwab]] following Schwab's acquisition of TD Ameritrade in 2020. It is widely regarded as the de facto platform for retail options traders.

## History

thinkorswim was founded as a brokerage firm focused on options trading. [[tom-sosnoff]], an options trader and former CBOE market maker, designed the platform to give retail traders the same analytical tools that professional options traders used on exchange floors. Key milestones:

- **1999**: Founded by Tom Sosnoff and Scott Sheridan in Chicago
- **2009**: Acquired by TD Ameritrade for ~$750 million
- **2020**: TD Ameritrade acquired by Charles Schwab; TOS became Schwab's advanced trading platform
- **2023-2024**: Migration of TD Ameritrade accounts to Schwab completed; TOS continued as the premium trading interface
- **2025**: Schwab announced a round of trading-experience enhancements to the thinkorswim suite, including a new Account Display
- **2026**: Schwab added **24/7 cryptocurrency trading** availability on thinkorswim as part of its 2026 retail trading enhancements; thinkorswim remains Schwab's core advanced retail trading suite across desktop, web, and mobile

After selling thinkorswim, Sosnoff went on to create [[tastytrade]] (media/education) and tastyworks (brokerage, later rebranded to tastytrade), applying similar design philosophies.

## Clients and Access

thinkorswim ships as a coordinated suite rather than a single app; the desktop application is the most feature-complete.

| Client | Strengths | Notes |
|--------|-----------|-------|
| **Desktop** (Win/Mac) | Full feature set: thinkScript, Analyze tab, thinkBack, all scanners | Resource-heavy; the reference experience for power users |
| **Web** | Browser access, no install | Reduced feature surface vs desktop |
| **Mobile** (iOS/Android) | Trade entry, position management, charting on the go | Reduced functionality vs desktop |

Access is **brokerage-tied**: a [[charles-schwab|Schwab]] account is required, and there is no standalone platform fee for account holders.

## Feature Reference

| Feature | What it does | Primary use | Related |
|---------|--------------|-------------|---------|
| Options chain | Bid/ask, OI, all five [[greeks]], [[implied-volatility]], PoP per strike | Strike selection | [[iron-condor]], [[credit-spread]] |
| Strategy builder | Click-to-build multi-leg structures with auto max P/L | Spread construction | [[diagonal-spread]], [[iron-butterfly]] |
| Analyze tab | Graphical risk/reward, what-if scenarios, portfolio Greeks | Risk visualization | [[delta-hedging]], [[vega-hedging]] |
| thinkBack | Historical options-chain replay | Manual backtesting | [[vix]], earnings studies |
| thinkScript | Proprietary scripting for indicators, scans, alerts | Custom automation/scanning | [[iv-rank-and-iv-percentile]] |
| paperMoney | Full-feature simulated trading | Practice / strategy testing | [[options-position-sizing]] |
| Stock/Option/Spread Hacker | Multi-criteria scanners | Idea generation | [[implied-volatility]] |

## Core Features

### Options Chain Analysis

The options chain in TOS is one of the most detailed available to retail traders. It displays:

- Real-time bid/ask prices with volume and open interest
- All five [[greeks]] (Delta, Gamma, Theta, Vega, Rho) per strike
- [[implied-volatility]] per strike and expiration
- Probability of profit (PoP) and probability of touching
- Theoretical values based on user-adjustable pricing models

### Strategy Builder

TOS provides templates for constructing multi-leg options strategies directly from the options chain:

- **Vertical spreads**: [[credit-spread|Credit spreads]], debit spreads
- **[[iron-condor|Iron condors]]** and [[iron-butterfly|iron butterflies]]
- **Strangles and straddles**: Volatility plays
- **Calendar and [[diagonal-spread|diagonal spreads]]**: Time-based strategies
- **Custom combos**: Any arbitrary multi-leg structure

Users can click on strikes to build spreads, and the platform automatically calculates max profit, max loss, breakeven points, and probability of profit.

### Analyze Tab (Risk Profile)

The Analyze tab provides graphical risk/reward profiles for any position or portfolio:

- P&L curves at expiration and at any future date
- Greeks exposure across the entire portfolio
- "What-if" scenarios: adjust [[implied-volatility]], underlying price, or time to see how positions respond
- Portfolio-level [[delta-hedging|delta]], [[gamma-scalping|gamma]], [[vega-hedging|vega]], and theta summaries

### thinkBack (Backtesting)

thinkBack allows traders to replay historical options data:

- View historical options chains for any past date
- Test how a strategy would have performed with actual historical prices
- Analyze [[implied-volatility]] behavior around earnings, macro events, and market crashes
- Useful for studying how [[vix|VIX]] spikes affected specific options strategies

### thinkScript (Custom Scripting)

TOS includes a proprietary scripting language called thinkScript for custom indicators, strategies, and alerts:

- Build custom technical indicators and overlay them on charts
- Create automated scanning criteria (e.g., "find stocks where IV Rank > 50 and earnings within 14 days")
- Write conditional alerts based on complex logic
- Share scripts with the community via the thinkScript lounge

### Paper Trading

TOS includes a full-featured paper trading mode (called "paperMoney") that mirrors the live platform:

- Same data feeds, options chains, and analytical tools
- Virtual account with simulated fills
- Useful for testing new strategies without risking capital
- Essential for learning options mechanics before going live

### Market Scanning

- Stock Hacker: scan equities by technical, fundamental, and options criteria
- Option Hacker: scan for options meeting specific Greeks, [[implied-volatility]], or probability criteria
- Spread Hacker: find spreads that meet defined risk/reward parameters

## Trading Applications

### Premium Selling

TOS is particularly well-suited for premium selling strategies popularized by [[tom-sosnoff]] and the [[tastytrade]] methodology:

- Quick construction of [[iron-condor|iron condors]], strangles, and [[credit-spread|credit spreads]]
- [[iv-rank-and-iv-percentile|IV Rank and IV Percentile]] displayed prominently
- Probability of profit calculations guide strike selection
- Portfolio-level Greeks help manage overall exposure

### Earnings Trading

- Earnings calendar integration with options chain
- Historical volatility crush data via thinkBack
- Quick deployment of [[earnings-options-strategies|earnings strategies]] (straddles, strangles, iron condors)

### Portfolio Management

- Real-time portfolio Greeks aggregation
- Margin and buying power impact calculations
- Position-level and portfolio-level risk visualization
- [[beta]]-weighted portfolio delta for market-neutral management

## Automation and Integrations

thinkorswim's automation surface is built around **thinkScript** rather than a general-purpose order API:

- **thinkScript** powers custom indicators, multi-condition scans, and conditional alerts, but it is an *analytical/alerting* language — it is not a transferable algorithmic-execution framework, and scripts do not port to other platforms.
- **Conditional orders** (OCO, OTO, trailing, study-triggered) let traders pre-stage execution logic inside the platform without external code.
- **Schwab developer API** — order routing into Schwab accounts is available through Schwab's API rather than through thinkorswim itself; automation tools commonly bridge signals into Schwab accounts via a webhook layer such as [[traderspost]] or [[trade-automation-toolbox]].
- **Third-party analytics** — traders who want richer historical options backtesting than thinkBack provides often pair TOS with [[optionnet-explorer]] or [[orats]].

For systematic options traders, the common pattern is: generate signals/scan in thinkScript (or externally), then route execution through Schwab's API or a webhook automation layer. See [[trading-automation]] and [[webhook-trading]] for the general architecture.

## How Traders Use thinkorswim

A representative discretionary options workflow:

1. **Scan** with Stock/Option Hacker or a thinkScript scan (e.g. [[iv-rank-and-iv-percentile|IV Rank]] ≥ 50, no earnings within 14 days).
2. **Build** the structure ([[iron-condor]], [[credit-spread|credit spread]], strangle) directly from the options chain; the platform computes max P/L, break-evens, and probability of profit.
3. **Analyze** the risk profile in the Analyze tab — P&L curves, what-if [[implied-volatility]]/price/time scenarios, portfolio Greeks.
4. **Paper-test** novel ideas in paperMoney before committing capital; study past behavior in thinkBack.
5. **Manage** at the portfolio level using [[beta]]-weighted delta and aggregated [[greeks]] for market-neutral oversight.

The platform's density makes it the de facto choice for serious retail options traders pursuing the [[options-premium-selling|premium-selling]] and [[earnings-options-strategies|earnings]] playbooks associated with [[tom-sosnoff]].

## Competitors

| Platform | Strengths | Weaknesses vs TOS |
|----------|-----------|-------------------|
| [[interactive-brokers\|Interactive Brokers TWS]] | Lower commissions, global markets, API access | Steeper learning curve, less intuitive options UI |
| [[tastytrade]] | Cleaner UI, built for options, lower fees | Fewer charting features, no thinkScript equivalent |
| [[tradingview-platform\|TradingView]] | Best charting, social features, [[pine-script\|Pine Script]] | Limited brokerage integration, weaker options tools |
| [[ninjatrader\|NinjaTrader]] | Superior futures trading, advanced charting | Weak options support |

## Strengths

- Best-in-class options analysis tools for retail traders
- Comprehensive Greeks display and risk visualization
- Powerful scripting language (thinkScript) for customization
- Integrated paper trading for risk-free practice
- Free for Schwab account holders (no platform fee)

## Limitations

- Can be overwhelming for beginners due to feature density
- Desktop application can be resource-heavy
- Mobile version has reduced functionality compared to desktop
- thinkScript is proprietary and not transferable to other platforms
- Execution quality debates after Schwab acquisition

## Related

- [[tom-sosnoff]] -- Creator of thinkorswim
- [[tastytrade]] -- Sosnoff's subsequent platform and media company
- [[tastytrade-platform]] -- the spiritual successor platform built by the same founders
- [[interactive-brokers]] -- Primary competitor for active options traders
- [[charles-schwab]] -- current owner since the 2020 TD Ameritrade acquisition
- [[trading-platforms]] -- Overview of available platforms
- [[optionnet-explorer]] -- third-party analytics often paired with TOS for richer backtesting
- [[traderspost]] -- webhook automation layer that can route signals into Schwab accounts
- [[trade-automation-toolbox]] -- alternative webhook/automation bridge for Schwab order routing
- [[trading-automation]] -- general architecture for automating signals into broker execution
- [[orats]] -- third-party options data and backtesting often paired with TOS
- [[implied-volatility]] -- Core metric displayed throughout TOS
- [[iron-condor]] -- Popular strategy easily built in TOS
- [[options-position-sizing]] -- Position sizing for options trades
- [[iv-rank-and-iv-percentile]] -- Key metrics for strategy selection in TOS

## Sources

- Charles Schwab thinkorswim product pages -- https://www.schwab.com/trading/thinkorswim and https://www.schwab.com/trading/thinkorswim/desktop
- Schwab press release, "Schwab Announces Latest Enhancements to Trading Experience" (2025) -- https://pressroom.aboutschwab.com/press-releases/press-release/2025/Schwab-Announces-Latest-Enhancements-to-Trading-Experience/default.aspx
- Schwab press release, "Schwab Announces Latest Round of Enhancements to Retail Trading Experience" (2026, incl. 24/7 crypto on thinkorswim) -- https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Announces-Latest-Round-of-Enhancements-to-Retail-Trading-Experience/default.aspx
- TD Ameritrade 2009 acquisition coverage (~$750M) and Schwab-TD Ameritrade 2020 merger disclosures.
- Platform status and 2025-2026 developments verified via Perplexity (sonar, high search context), 2026-06-10.
