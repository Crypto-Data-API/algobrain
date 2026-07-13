---
title: "OptionAlpha"
type: entity
created: 2026-05-03
updated: 2026-06-10
status: good
tags: [company, options, education, automated-trading]
entity_type: company
founded: 2012
headquarters: "United States"
website: "https://optionalpha.com"
aliases: ["Option Alpha", "OptionAlpha"]
related: ["[[options]]", "[[options-premium-selling]]", "[[iron-condors]]", "[[short-strangle]]", "[[backtesting]]", "[[probability-of-profit]]", "[[automated-trading]]", "[[tastytrade]]"]
---

OptionAlpha is a U.S.-based [[options]] education platform and bot-trading service founded in 2012 by Kirk Du Plessis. The company began as a free-and-paid educational site oriented toward defined-risk premium selling and was later expanded with an in-house automated trading product that allows retail traders to deploy rule-based options strategies without writing code. Alongside [[tastytrade]], OptionAlpha is one of the most widely cited retail education brands for systematic [[options-premium-selling]].

## Overview

OptionAlpha started as a content site producing video courses, podcasts, written guides, and trade examples focused on retail options trading. The editorial focus is similar to [[tastytrade]] -- high-probability, premium-selling structures such as [[iron-condors]], credit spreads, and [[short-strangle|short strangles]] -- but with a stronger emphasis on defined-risk trades suitable for smaller accounts and a more structured, course-driven curriculum.

In the early 2020s, OptionAlpha launched an automated trading platform that connects to a supported broker and executes pre-defined strategies on the user's behalf. This product, often referred to simply as "the bots," was the company's pivot from a pure education business to a software-and-education hybrid. The bots are a no-code rule builder rather than a general-purpose [[algorithmic-trading]] framework: users assemble decisions, scans, and order constructors out of pre-built blocks.

## Products

### Education
- **Free content**: Long-running blog and podcast covering options theory, the Greeks ([[delta]], [[theta]], [[gamma]], [[vega]]), strategy mechanics, position sizing, and trade management
- **Course library**: Structured tracks for beginners through to multi-leg and portfolio-level construction, organized in tiered membership
- **Trade alerts and watchlists**: Idea generation aligned with the platform's strategy templates

### Automated Bots
The bot product is the platform's defining feature. Key characteristics:

- **No-code rule building**: Strategies are assembled from "decision," "scan," and "action" blocks rather than written in code, lowering the barrier for traders without a programming background
- **Pre-built templates**: A library of ready-made bots implementing common strategies including [[iron-condors]], strangles, credit spreads, calendars, and earnings plays
- **Scheduled execution**: Bots run on schedules (e.g., scan for setups daily before the close) rather than tick-by-tick, which is appropriate for the swing/positional time horizons of premium selling
- **Capital and risk limits**: Per-bot allocation caps, position counts, and exposure limits configurable by the user
- **Broker integration**: Executes through a connected brokerage account; check the OptionAlpha site for current supported brokers
- **Backtesting**: Limited historical replay of bot logic, though, like all retail-grade [[backtesting]] tools, results should be treated cautiously due to data limitations and survivorship of underlyings

### Strategy Library
A widely shared catalog of canonical retail premium-selling structures with documented entry rules, profit targets, and management criteria. The library is heavily reused (and re-shared) across retail communities even by traders who do not subscribe to the bot product.

## Business Model

OptionAlpha's revenue comes from tiered subscriptions to the platform. Education-only access historically existed at a lower price point, while access to the bots and full strategy library sits at higher tiers. The company is not a broker and does not earn commissions or payment for order flow; bot trades route through the user's own brokerage. Pricing tiers and tier names have changed over time.

## Why Traders Use It

- Traders who want a structured options curriculum from beginner to intermediate level
- Premium sellers who want to automate mechanical entries, profit-taking, and management without coding
- Smaller-account traders attracted to the platform's emphasis on defined-risk strategies
- Traders looking for a starter strategy library to adapt rather than building from scratch

## Limitations

- The bot platform is no-code and rule-based; traders who need machine learning, custom indicators, or tick-level logic will outgrow it quickly
- Strategy templates lean heavily on premium selling, sharing the well-known regime risk of that style: short-vol books can suffer outsized drawdowns in volatility shocks, and the templates do not always include hedges sized appropriately for tail events
- [[backtesting|Backtests]] available inside the platform are subject to standard retail-grade caveats (limited [[probability-of-profit]] modeling, simplified fill assumptions, no full chain history for some periods)
- Subscription costs can be material relative to the small account sizes the platform targets, particularly at higher tiers
- Like any automated-trading service, latency, broker outages, and API hiccups can cause executions that diverge from the modeled strategy

## Related

- [[options]] -- the platform's entire focus
- [[options-premium-selling]] -- the strategic worldview underpinning most templates
- [[iron-condors]] -- a flagship defined-risk template
- [[short-strangle]] -- an undefined-risk template available to qualifying accounts
- [[backtesting]] -- the bot platform includes a basic backtester
- [[probability-of-profit]] -- a key trade-construction metric in the curriculum
- [[automated-trading]] -- the broader category the bot product belongs to
- [[tastytrade]] -- a comparable retail education brand with a brokerage instead of bots
- [[delta]], [[theta]], [[gamma]], [[vega]] -- the Greeks emphasized throughout the curriculum

## Sources

- (Source: [[2026-04-22-gap-finder-options-portfolios]])
- [Option Alpha official site](https://optionalpha.com)
- [Option Alpha automated trading platform](https://optionalpha.com/automation)
