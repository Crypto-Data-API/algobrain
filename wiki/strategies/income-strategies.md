---
title: "Income Strategies"
type: index
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [options, derivatives, risk-management, volatility]
aliases: ["Income Strategies", "Income Trading", "Yield Strategies", "Cash-Flow Strategies"]
related: ["[[options-income]]", "[[options-premium-selling]]", "[[covered-calls]]", "[[cash-secured-puts]]", "[[stablecoin-yield]]", "[[strategies-overview]]"]
---

**Income strategies** are approaches whose primary objective is to generate recurring cash flow — option premium, dividends, interest, or staking/lending yield — rather than capital appreciation from price moves. They trade some upside (capped gains, assignment risk, or duration/credit risk) for a steadier, more frequent return stream. This is a hub page; each linked strategy has its own detailed page.

## When to use income strategies

- **Range-bound or mildly trending markets.** Most premium-selling income strategies profit from time decay and stable-to-rising prices; they underperform in sharp trends and lose in crashes.
- **You hold underlying assets you are willing to keep or sell at a target price.** Covered calls and cash-secured puts monetize a holding or an entry intention.
- **You want yield enhancement on a portfolio**, accepting that you are short volatility and exposed to tail risk (see [[variance-risk-premium]] and [[volmageddon]]).
- **Not for** strong directional convictions (use directional structures) or for capital you cannot afford to see drawn down in a volatility spike.

Income strategies are overwhelmingly **short-volatility** in character: you collect premium for bearing risk others want to shed. The recurring caution across all of them is that returns look smooth until a tail event delivers a large, correlated loss. Size with that asymmetry in mind.

## Options income (premium selling)

The core family — selling option premium to harvest time decay ([[theta-decay]]) and the [[variance-risk-premium]].

- [[options-income]] — overview of options-based income overlays.
- [[options-premium-selling]] — the systematic premium-selling discipline ("theta gang").
- [[premium-selling-systematic]] — rules-based mechanical premium selling.
- [[covered-calls]] — sell calls against long stock for yield (caps upside).
- [[cash-secured-puts]] — sell puts backed by cash to earn premium or get assigned at a target entry.
- [[wheel-strategy]] — cycle cash-secured puts into covered calls on assignment.
- [[iron-condors]] — defined-risk, market-neutral premium selling.
- [[short-volatility-strategies]] — the broader short-vol category and its tail risks.
- [[zero-dte-options]] — same-day-expiry premium selling (high gamma risk).
- [[managing-winners]] — when to close income trades early to lock gains and reduce risk.

## Equity / dividend income

- [[buy-and-hold]] — long-horizon equity holding, the base layer many income overlays sit on.
- [[dca-strategy]] — dollar-cost averaging to build the income-producing core.

## Fixed income and yield

- [[stablecoin-yield]] — crypto stablecoin lending/staking yield (counterparty and de-peg risk).

## Risk context

Before deploying any income strategy, read:

- [[variance-risk-premium]] — why selling options is positive-carry on average.
- [[long-vol-vs-short-vol]] — the structural trade-off you are taking.
- [[volmageddon]] and [[vix-august-2024-spike]] — how short-vol income blows up.
- [[risk-management]] and [[position-sizing]] — sizing for the tail, not the average.
- [[pin-risk]], [[assignment]], [[gamma-explosion]] — mechanical hazards near expiration.

## Related

- [[strategies-overview]] — full strategy catalog.
- [[short-volatility-strategies]], [[long-volatility-strategies]] — the volatility-direction framing.
- [[regime-strategy-playbook]] — which income approaches fit which market regime.
