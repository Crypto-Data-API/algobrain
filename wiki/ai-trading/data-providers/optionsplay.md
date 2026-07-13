---
title: "OptionsPlay"
type: entity
created: 2026-05-06
updated: 2026-06-10
status: good
tags: [data-provider, options, stocks, education]
entity_type: company
founded: 2013
headquarters: "New York, USA"
website: https://www.optionsplay.com
aliases: ["OptionsPlay Canada"]
related:
  - "[[orats]]"
  - "[[market-chameleon]]"
  - "[[optionstrat]]"
  - "[[unusual-whales]]"
  - "[[etrade]]"
  - "[[charles-schwab]]"
  - "[[options-premium-selling]]"
---

# OptionsPlay

OptionsPlay is an options idea-generation, analytics, and education platform that simplifies multi-leg options strategy selection for retail and self-directed traders. It is sold both as a standalone subscription and -- more commonly -- as a white-labeled tool embedded inside major broker platforms (notably [[etrade]] and [[charles-schwab]]). Launched in 2013 in New York by Mark Engelhardt (CEO), Ramesh Srinivas (CTO), and Tony Zhang (Chief Strategist), with Zhang -- a frequent CNBC Options Action contributor -- serving as the company's public face, the platform's value proposition is that it surfaces ranked trade ideas with pre-built strategy templates, risk graphs, and IV context so users do not have to design structures from scratch.

## Overview

OptionsPlay sits in the "guided-trading" tier of the options ecosystem, between raw analytics tools like [[orats]] or [[market-chameleon]] (which assume the user already knows what they want to test) and order-flow tools like [[unusual-whales]] (which surface unusual activity but do not prescribe a strategy). It answers the question: "Given a directional or neutral view on this ticker, what is a reasonable options structure to express it, and what does the risk look like?"

The platform does this by combining:

- A screener of ranked trade ideas across stocks, ETFs, and indices, refreshed daily
- A strategy builder with pre-configured templates (covered call, cash-secured put, vertical, iron condor, calendar, diagonal, etc.)
- Risk graphs and probability metrics for each suggested structure
- Educational content authored by Tony Zhang and the OptionsPlay research team

## Pricing

- **Standalone subscription**: roughly $25-$100/month depending on tier, with discounted annual plans; tiers gate the screener depth, idea volume, and access to Tony Zhang's research
- **Broker-embedded**: free or heavily discounted for active customers of brokers that license the technology, including [[etrade]] and [[charles-schwab]]; the embedded version is usually rebranded but powered by OptionsPlay
- **Enterprise / B2B**: financial-advisor and broker-dealer tiers with portfolio-overlay tooling, typically priced per seat or under bulk licensing

Most retail users encounter OptionsPlay first inside their broker rather than via direct subscription. That distribution model is the firm's main commercial moat.

## What You Get

- **Top Options Trade Ideas**: ranked list of trade candidates filtered by market view (bullish, bearish, neutral), with each idea pre-mapped to a strategy template and risk graph
- **Strategy builder**: select a ticker and a directional view; the platform proposes specific strikes and expiries and shows max profit, max loss, breakevens, and probability metrics
- **IV rank / IV percentile screening**: identifies elevated-IV tickers suitable for premium-selling and depressed-IV tickers suitable for premium-buying, conceptually similar to [[market-chameleon]]
- **Volume and open-interest filters**: surfaces liquid contracts, helping retail users avoid wide bid-ask spreads
- **Earnings and event tools**: screens stocks with upcoming earnings overlaid with implied move from the options market
- **Education library**: video courses, blog content, and webinars covering strategy mechanics, position management, and risk basics
- **Mobile and web apps**: retail-friendly UX, in contrast to the spreadsheet-heavy feel of institutional tools

## Strengths

- **Lower learning curve** than raw options analytics: a beginner can pick a directional view and get a reasonable structure in under a minute
- **Broker integration**: deep partnerships with [[etrade]] and [[charles-schwab]] mean ideas link directly into the broker's trade ticket, removing copy-paste friction
- **Strategy templates as guardrails**: defaults steer users into defined-risk structures (verticals, iron condors) instead of naked positions, which is appropriate for the target audience
- **Recognizable face**: Tony Zhang's media presence (CNBC Options Action) lends credibility and provides a steady stream of educational content
- **Cross-platform accessibility**: works on web and mobile without a heavy desktop install, unlike [[thinkorswim]] or [[tradestation]]

## Weaknesses

- **Idea quality varies**: ranked-idea lists are heuristic and not edge-validated; users should treat them as starting points, not signals
- **Less analytical depth than [[orats]] or [[market-chameleon]]**: no historical volatility-surface research, limited skew analytics, no rigorous backtesting of overlay programs
- **Not a flow tool**: does not surface unusual options activity the way [[unusual-whales]] does
- **Limited customization**: power users hit ceilings quickly because the platform is opinionated about which structures to suggest
- **Embedded-version feature gaps**: the broker-embedded version is usually a subset of the standalone product, so users sometimes need both
- **No serious quant integration**: no API for systematic strategies or portfolio-level Greek monitoring at the level a professional book would require

## ITPM-Style Use Cases

OptionsPlay is not the analytical core of an [[itpm-playbook|ITPM-style]] options portfolio, but it has practical roles:

- **Pre-built strategy templates as a starting point**: when the manager decides "short premium on this name," OptionsPlay's strike/expiry suggestions are a fast-first-pass that can be sanity-checked against deeper tools
- **Covered-call screening**: ranks call-write candidates by premium-to-stock-price and IV rank, useful for income overlays on long equity positions
- **Cash-secured-put candidates**: similar logic on the put side, generating a list of "stocks I would not mind owning at strike X" candidates for [[wheel-strategy|wheel]] or [[options-premium-selling|premium-selling]] programs
- **Earnings-event filtering**: identifies upcoming events that warrant either premium selling (rich IV with intent to fade the move) or premium buying (cheap IV with directional view)
- **Education for junior team members**: clean explanations of strategy mechanics that beat most broker-native education

The mature workflow is to use OptionsPlay for idea sourcing, then validate the structure in [[orats]] or a custom backtester before sizing.

## Brokers and Partners That Embed or Distribute OptionsPlay

- [[etrade]] (Power E*TRADE platform)
- [[charles-schwab]] (rolled in via the legacy E*TRADE relationship and Schwab integrations)
- Fidelity Investments, Merrill Lynch, and Raymond James Financial — distribution and partnership relationships developed by Zhang's team
- Exchange and industry partnerships: Nasdaq, the Options Industry Council (OIC), and the Montreal Exchange (TMX)
- **OptionsPlay Canada**: the company's Canada-focused offering; it powers National Bank Direct Brokerage with OptionsPlay trading technology for Canadian and US derivatives
- Various other Canadian and international broker-dealers under white-label arrangements

The embedded version typically appears branded as "Strategy Optimizer," "Trade Ideas," or similar, but is powered by OptionsPlay infrastructure. This embedded distribution model remains the firm's main commercial moat as of 2026.

## Related

- [[orats]] -- deeper options analytics and historical volatility data; complements OptionsPlay's idea layer
- [[market-chameleon]] -- screening and unusual-activity tools with more depth
- [[optionstrat]] -- visual strategy builder targeting a similar retail audience
- [[unusual-whales]] -- options flow and unusual activity, a different lens on idea generation
- [[etrade]], [[charles-schwab]] -- primary embedded distribution partners
- [[options-premium-selling]] -- core strategy family OptionsPlay screens for via IV-rank filters

## Sources

- OptionsPlay corporate site, About Us: https://www1.optionsplay.com/about-optionsplay (2013 launch, founding team: Engelhardt, Srinivas, Zhang)
- OptionsPlay main site: https://www.optionsplay.com
- Tony Zhang profile (Chief Strategist; partnerships with OIC, Nasdaq, Montreal Exchange, Merrill Lynch, Fidelity, Schwab, Raymond James): https://www.finnotes.org/people/tony-zhang and https://www.linkedin.com/in/optionsgeek
- Tony Zhang author pages and market commentary: https://www.nasdaq.com/authors/tony-zhang, https://articles.stockcharts.com/author/tony-zhang/ (ongoing 2025 output, e.g. credit-spread strategy sessions)
- Tony Zhang CNBC Options Action segments (ongoing)
- Verified via Perplexity and web search, 2026-06-10
