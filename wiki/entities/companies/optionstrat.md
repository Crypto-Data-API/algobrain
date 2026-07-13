---
title: "OptionStrat"
type: entity
created: 2026-05-03
updated: 2026-06-10
status: good
tags: [company, options, tools, visualization]
entity_type: company
website: "https://optionstrat.com"
aliases: ["OptionStrat", "Option Strat"]
related: ["[[options]]", "[[options-greeks]]", "[[iron-condors]]", "[[short-strangle]]", "[[probability-of-profit]]", "[[volatility]]", "[[tastytrade]]", "[[optionalpha]]"]
---

OptionStrat is a web-based [[options]] strategy visualizer and payoff-diagram tool that lets users build multi-leg trades and inspect their profit-and-loss profile at expiration and at any point before. The site has become a de facto standard reference for sharing trade ideas in retail communities such as r/options and finance Twitter, where screenshots of OptionStrat payoff diagrams are routinely posted to illustrate proposed trades.

## Overview

OptionStrat provides a browser-based interface in which a trader selects an underlying, picks expirations and strikes, and assembles legs into a single position. The platform then renders a payoff diagram, a Greeks summary, and a probability-of-profit estimate based on the implied-volatility surface of the selected underlying. The service is targeted at retail traders rather than institutional desks, and its design priorities are clarity of visualization and speed of input rather than execution or order routing -- OptionStrat is not a broker.

The tool covers the full range of common multi-leg structures including verticals, [[iron-condors]], butterflies, calendars, diagonals, [[short-strangle|strangles]], straddles, and custom user-built combinations. It supports both single-leg and multi-leg modeling, and toggles between an at-expiration P&L curve and a "today" P&L surface that incorporates time decay and implied-volatility shifts.

## Features

### Strategy Builder and Payoff Diagrams
- Drag-and-drop or pick-from-chain leg construction
- Payoff diagrams at expiration and at any chosen date before expiration
- Implied-volatility shift sliders to stress-test the position against vol expansion or collapse
- Underlying-price sliders and date sliders for "what-if" exploration
- Aggregate position [[options-greeks|Greeks]] (net [[delta]], [[gamma]], [[theta]], [[vega]]) for the whole structure

### Probability of Profit
The platform computes a [[probability-of-profit]] estimate based on the current implied-volatility surface. Because this estimate is implied-vol-derived rather than realized-vol-derived, it should be read as a market-implied probability rather than a forecast.

### Optimizer / Strategy Finder
Given a directional or volatility view (e.g., bullish to a target price by a target date), the optimizer suggests structures that maximize one of several objectives -- maximum return, probability of profit, or risk/reward ratio -- subject to user-set constraints. This is useful as an idea generator, though the suggestions inherit the limitations of the underlying probability model.

### Unusual Options Activity and Flow
Paid tiers include scanners for unusual options activity, large block prints, and other order-flow signals. As with all retail-grade flow tools, attribution of trades to "smart money" is inferential and the signals should be treated as starting points for research rather than executable signals.

### Earnings and Events
Tools for previewing earnings setups, comparing historical post-earnings moves to the implied move priced into the options chain, and constructing earnings-specific structures.

### Sharing
Each constructed strategy can be exported as a shareable URL or image, which is the mechanism behind the platform's heavy use in social media. This made OptionStrat into a community tool more than a private analytical workbench.

## Business Model

OptionStrat operates a freemium model. The core builder and payoff diagrams are available on a free tier with limited features; advanced features such as the probability lab, unusual-activity scanners, and additional history sit behind a paid subscription. The company is not a broker and does not execute trades, earn commissions, or take payment for order flow. Revenue comes from subscription fees and, in some periods, partnerships and affiliate links to brokers.

## Why Traders Use It

- Quickly visualizing a multi-leg structure before committing capital
- Comparing variants of a structure (different strikes or expirations) on the same chart
- Sharing trade ideas with a payoff diagram instead of a wall of text in retail communities
- Sanity-checking a broker's order ticket against a second tool before submitting
- Exploring how a position evolves with changes in implied [[volatility]] and time

## Limitations

- The probability model is implied-volatility-based and assumes lognormal-style price evolution; real distributions have fatter tails, especially around earnings and macro events
- It is a visualization and analysis tool, not an execution venue; positions modeled in OptionStrat must still be entered through a broker, where fills and slippage will differ from the idealized model
- Greeks and P&L are computed from a snapshot of the chain; intraday quote staleness and wide bid-ask spreads in illiquid contracts can make the displayed numbers optimistic
- Unusual-activity scanners do not have signed direction (it is hard to know whether a large print was a buy or a sell) and should not be treated as a directional signal on their own
- The historical depth of options chain data available in the platform is more limited than what professional research vendors provide, which constrains how far back one can backtest or compare current setups to history

## Related

- [[options]] -- the entire product
- [[options-greeks]] -- displayed for every constructed position
- [[iron-condors]] -- a heavily modeled structure
- [[short-strangle]] -- another common multi-leg use case
- [[probability-of-profit]] -- a headline metric in the strategy builder
- [[volatility]] -- the platform exposes IV shifts as a "what-if" lever
- [[tastytrade]] -- a peer in the retail options ecosystem, focused on brokerage and education
- [[optionalpha]] -- a peer focused on education and automated rule-based trading

## Sources

- (Source: [[2026-04-22-gap-finder-options-portfolios]])
- [OptionStrat official site](https://optionstrat.com)
- [OptionStrat strategy builder](https://optionstrat.com/build)
