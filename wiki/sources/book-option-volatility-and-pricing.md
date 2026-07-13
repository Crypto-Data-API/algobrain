---
title: "Option Volatility and Pricing — Sheldon Natenberg (1994)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, options, volatility, derivatives, risk-management]
aliases: ["Option Volatility and Pricing", "Natenberg"]
related: ["[[implied-volatility]]", "[[options-greeks]]", "[[iron-condor]]", "[[covered-call-strategy]]", "[[straddle-strangle]]", "[[butterfly-spread]]", "[[calendar-spread]]", "[[volatility-trading]]", "[[black-scholes]]", "[[options-overview]]", "[[option-volatility-and-pricing]]"]
source_type: book
source_author: "Sheldon Natenberg"
source_date: 1994
confidence: high
claims_count: 12
---

The definitive textbook on options pricing and volatility trading, first published in 1994 and substantially revised in 2014. [[sheldon-natenberg]] — veteran CBOE options trader and educator — provides a comprehensive framework that starts from probability theory and builds through pricing models, volatility analysis, spread strategies, and portfolio risk management. The book's central thesis is that options trading is fundamentally about volatility: the key decision is whether [[implied-volatility]] is mispriced relative to expected future realized volatility. Universally cited by professional options market makers as the foundational text of their discipline.

## Key Claims

1. [HIGH] **Implied volatility is the most important factor in options pricing after the underlying price**: IV represents the market's consensus forecast of future volatility and is the variable options traders must evaluate. A trader who correctly forecasts whether realized vol will exceed or fall short of implied vol has a systematic edge. (Source: [[sheldon-natenberg]])

2. [HIGH] **Options pricing models assume log-normal distribution but real markets have fat tails**: The Black-Scholes model assumes returns are normally distributed, volatility is constant, and hedging is continuous. None of these hold in practice. Real markets exhibit excess kurtosis (fat tails), volatility clustering, and discrete hedging. The model is useful despite being wrong because traders understand and adjust for its limitations. (Source: [[sheldon-natenberg]])

3. [HIGH] **The Greeks quantify an option's sensitivity to various risk factors**: Delta measures sensitivity to underlying price, gamma measures rate of change of delta, theta measures time decay, vega measures sensitivity to implied volatility, and rho measures sensitivity to interest rates. Professional traders manage portfolios in terms of aggregate Greek exposures rather than individual positions. (Source: [[sheldon-natenberg]])

4. [HIGH] **Volatility skew/smile reveals market expectations about tail risk**: Out-of-the-money puts typically trade at higher implied volatility than at-the-money options, reflecting demand for crash protection. The shape of the volatility surface across strikes and expirations encodes the market's collective view on the probability distribution of future returns. (Source: [[sheldon-natenberg]])

5. [HIGH] **Selling options collects theta but requires managing gamma and vega risk**: Short-options positions benefit from time decay (theta) but are exposed to adverse moves in the underlying (gamma risk) and increases in implied volatility (vega risk). Premium-selling strategies are profitable in calm markets but can produce catastrophic losses during volatility spikes. (Source: [[sheldon-natenberg]])

6. [HIGH] **Covered calls sacrifice upside for premium income**: A covered call combines long stock with short calls, generating income from theta decay but capping upside at the strike price. The strategy is appropriate for range-bound or mildly bullish views, not strong directional convictions. It reduces but does not eliminate downside risk. (Source: [[sheldon-natenberg]])

7. [HIGH] **Iron condors profit from low volatility with defined risk and defined reward**: An iron condor sells an out-of-the-money put spread and an out-of-the-money call spread simultaneously, profiting when the underlying stays within a range. Maximum profit equals net premium received; maximum loss equals spread width minus premium. The strategy is a bet that implied volatility is overpriced. (Source: [[sheldon-natenberg]])

8. [HIGH] **Calendar spreads exploit term structure differences in implied volatility**: By selling a near-term option and buying a longer-term option at the same strike, the trader profits from faster time decay in the near-term option and/or an increase in the longer-term option's implied volatility. The strategy exploits the term structure of volatility. (Source: [[sheldon-natenberg]])

9. [HIGH] **Butterfly spreads provide maximum profit at a specific price target with limited risk**: A butterfly combines a bull spread and bear spread sharing a common middle strike. Maximum profit occurs if the underlying expires exactly at the middle strike. The strategy is cheap to initiate (limited debit) and has defined maximum loss, making it efficient for targeting a specific price. (Source: [[sheldon-natenberg]])

10. [HIGH] **Historical vs. implied volatility comparison identifies over/underpriced options**: When implied volatility significantly exceeds historical (realized) volatility, options are statistically "expensive" — selling strategies have a theoretical edge. When implied vol is below historical vol, options are "cheap" — buying strategies are favored. This comparison is the primary analytical framework for volatility traders. (Source: [[sheldon-natenberg]])

11. [HIGH] **Delta-neutral strategies isolate volatility from directional exposure**: By constructing positions with zero (or near-zero) net delta, traders can express pure views on volatility magnitude without taking directional risk. Delta-neutral portfolios are maintained through dynamic hedging — adjusting the hedge as delta changes. (Source: [[sheldon-natenberg]])

12. [HIGH] **Position management (rolling, adjusting Greeks) is as important as trade entry**: Professional options traders spend more time managing existing positions — rolling expirations, adjusting delta hedges, reducing gamma/vega exposure before events — than selecting new trades. The entry is the beginning, not the end, of the trading process. (Source: [[sheldon-natenberg]])

## Concepts Referenced

- [[implied-volatility]], [[realized-volatility]], [[volatility-trading]]
- [[options-greeks]], [[delta-hedging]], [[gamma-risk]]
- [[black-scholes]], [[options-pricing-models]]
- [[iron-condor]], [[covered-call-strategy]], [[straddle-strangle]]
- [[butterfly-spread]], [[calendar-spread]]
- [[volatility-skew]], [[volatility-surface]], [[term-structure]]

## Pages Backed

- [[implied-volatility]] — IV as the central concept in options pricing and trading
- [[options-greeks]] — Greek definitions, interpretation, and portfolio-level management
- [[iron-condor]] — Strategy mechanics, profit/loss profile, and volatility view
- [[covered-call-strategy]] — Strategy mechanics and appropriate market conditions
- [[straddle-strangle]] — Volatility-buying strategy construction and risk profile
- [[butterfly-spread]] — Price-targeting strategy with defined risk
- [[calendar-spread]] — Term structure exploitation and time decay differential
- [[volatility-trading]] — The overarching discipline of trading volatility as an asset
- [[black-scholes]] — Model assumptions, limitations, and practical adjustments
- [[options-overview]] — General options trading framework and strategy taxonomy
