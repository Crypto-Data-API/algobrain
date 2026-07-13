---
title: "tastytrade"
type: entity
created: 2026-05-03
updated: 2026-06-10
status: good
tags: [company, options, education]
entity_type: company
entity_subtype: private
founded: 2011
headquarters: "Chicago, Illinois, USA"
website: "https://tastytrade.com"
parent: "IG Group (LSE: IGG)"
aliases: ["tastytrade", "tastyworks", "tastylive"]
related: ["[[options]]", "[[options-premium-selling]]", "[[iron-condors]]", "[[short-strangle]]", "[[interactive-brokers]]", "[[probability-of-profit]]", "[[ig-group]]"]
---

tastytrade is a retail-focused [[options]] brokerage and financial media network headquartered in Chicago, founded in 2011 by Tom Sosnoff and Scott Sheridan, the same pair who previously co-founded thinkorswim and sold it to TD Ameritrade in 2009. The company combines a low-commission options-centric brokerage with a free, full-day live programming network that has become one of the most influential sources of [[options-premium-selling]] education in retail trading. tastytrade was acquired by IG Group in 2021 for approximately $1 billion and continues to operate under the tastytrade brand following a rebrand from "tastyworks" (the brokerage) and "tastytrade" (the media arm) into a single name around 2022.

## Overview

tastytrade originated as a financial media network ("tastytrade") in 2011, broadcasting live trading content during U.S. market hours. The brokerage subsidiary, originally called "tastyworks," launched in early 2017 to give viewers a place to actually execute the trades being discussed on air. After the IG Group acquisition the two brands were consolidated, with the brokerage renamed to tastytrade and the media arm taking the tastylive name in some contexts.

The company's distinguishing thesis is that retail traders are best served by selling options premium in liquid, high-implied-volatility underlyings, managing trades mechanically by rules rather than discretion, and trading small and frequently rather than swinging for home runs. This worldview pervades both the broker's pricing model and the media network's curriculum.

Famous on-air personalities include Tom Sosnoff, Tony Battista (the long-running "Bootstrappin' in America" / "Market Measures" co-host), Liz Dierking and Jenny Andrews (formerly the "Liz and Jenny" segment), and a rotating cast of researchers and traders. Sosnoff is widely cited in retail circles for popularizing specific rules-of-thumb such as 45-DTE entries, 50% profit targets, and 21-DTE management.

## Brokerage

The tastytrade brokerage is structured around active options traders. Key characteristics:

- **Commission model**: Capped per-leg commissions on options ($1.00 per contract to open, $0 to close as of recent schedules; check current rates), with no commissions on closing trades. This per-leg-but-capped model is favorable for multi-leg strategies like [[iron-condors]] and [[short-strangle|short strangles]] compared to flat per-contract pricing.
- **Platform**: A proprietary desktop and web platform built around the options chain, with strategy-builder tooling for verticals, [[iron-condors]], strangles, butterflies, calendars, and other multi-leg structures. The interface emphasizes [[probability-of-profit]] and Greeks ([[delta]], [[theta]], [[gamma]], [[vega]]) at the point of order entry.
- **Margin**: Offers both Reg-T and portfolio margin (for qualifying accounts) for clients who can meet equity requirements.
- **Markets**: U.S. equities, ETFs, equity options, index options, futures, and futures options. Crypto access has been added and removed at various points; current availability should be confirmed on the website.

The brokerage is generally regarded as cost-competitive for premium-selling and multi-leg strategies but less suited for buy-and-hold equity investors, international markets, or fixed income, where competitors like [[interactive-brokers]] have broader reach.

## Media Network

The tastytrade / tastylive network broadcasts roughly eight hours of live programming every U.S. trading day, available free on the web and via a mobile app. Recurring programs cover live trade walk-throughs, options theory, research segments based on internal backtests, market commentary, and beginner-oriented education. The network's research arm regularly publishes [[backtesting|backtested]] studies on the firm's own platform comparing strategy variants -- e.g., 45-DTE vs 30-DTE entries, managing winners at 50% vs holding to expiration, and the impact of [[volatility|implied volatility rank]] on trade outcomes.

The network's editorial line is consistent: high-probability, defined- or undefined-risk premium selling in liquid underlyings, with mechanical management. While the studies are useful as a starting point, they share well-known limitations of in-sample backtests on a small set of underlyings during a specific volatility regime, and tastytrade's own researchers have acknowledged this on air.

## Concepts Popularized in Retail

tastytrade did not invent the following concepts, but is largely responsible for their saturation in retail options vocabulary:

- **45-DTE entries**: Opening short-premium positions roughly 45 days to expiration to balance theta decay against gamma risk
- **50% profit target**: Closing winning short-premium trades at half of the credit received rather than holding to expiration
- **21-DTE management**: Closing or rolling short-premium trades when 21 days to expiration is reached, regardless of P&L, to avoid late-cycle gamma risk
- **~70% [[probability-of-profit]] setups**: Selling options at strikes whose statistical probability of finishing out-of-the-money is roughly 70% (typically 30-delta short strikes)
- **"Trade small, trade often"**: Risking a small fraction of account equity per trade and relying on the law of large numbers
- **High [[volatility|IV rank]] sells, low IV rank buys**: Filtering trades by implied volatility rank to favor selling premium when it is rich

## Business Model

tastytrade's revenue mix combines brokerage commissions, payment for order flow on options, interest on idle cash and on margin loans, and advertising / sponsorship on the media network. Following the IG Group acquisition, the company forms part of a larger global derivatives broker, though tastytrade's U.S. business is operationally distinct from IG's CFD-focused operations elsewhere.

## Why Traders Use It

- Active options traders attracted to the cost structure for multi-leg trades
- Newer traders using the free media network as a structured options curriculum
- Premium sellers who want a platform whose order entry, analytics, and educational content are aligned with their strategy
- Traders who want a single ecosystem combining broker, education, and a community

## Limitations

- Narrow product breadth compared to full-service brokers; international markets, bonds, and mutual funds are weak or absent
- Editorial bias toward premium selling; buyers of options and directional traders will find less curriculum tailored to them
- Research segments rely on the firm's own backtests, which are not always reproducible by outside parties
- Customer service and platform reliability have drawn periodic complaints during high-volatility events, as is common across retail options brokers
- Payment-for-order-flow on options is a meaningful revenue line, which some traders view as a conflict of interest

## Trading Relevance & Exposure

tastytrade is not separately listed; it is a wholly owned subsidiary of UK-listed **[[ig-group|IG Group]]** (LSE: IGG), acquired in 2021 for roughly $1 billion. There is no direct equity in tastytrade itself — public-market exposure to its US retail-options franchise comes only via IG Group shares, where tastytrade represents IG's US growth engine and a key part of the group's diversification away from European CFD trading. As a barometer, tastytrade's account growth and options-volume trends are a useful read on US retail-options activity, which correlates with overall equity-market volatility (high VIX regimes tend to lift retail premium-selling activity). Listed comparables/competitors a trader might watch include [[interactive-brokers|Interactive Brokers]] (IBKR), Robinhood (HOOD), and Charles Schwab (which absorbed thinkorswim via TD Ameritrade).

## Related

- [[options]] -- the entire business is built on retail options
- [[ig-group]] -- parent company (LSE: IGG)
- [[options-premium-selling]] -- the strategic worldview promoted by the network
- [[iron-condors]] -- a frequently featured defined-risk premium-selling structure
- [[short-strangle]] -- the canonical undefined-risk premium-selling trade
- [[probability-of-profit]] -- the metric tastytrade emphasizes in trade construction
- [[backtesting]] -- the research style behind tastytrade's "Market Measures" studies
- [[volatility]] -- IV rank and IV percentile are core filters in tastytrade's framework
- [[delta]], [[theta]], [[gamma]], [[vega]] -- Greeks displayed prominently in the platform
- [[interactive-brokers]] -- a more general-purpose competitor

## Sources

- (Source: [[2026-04-22-gap-finder-options-portfolios]])
