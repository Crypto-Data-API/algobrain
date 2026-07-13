---
title: "Crypto Allocation"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [crypto, portfolio-theory, risk-management, bitcoin, asset-allocation]
aliases: ["Crypto Allocation", "Cryptocurrency Allocation", "Crypto Exposure", "Cryptocurrency Exposure", "Crypto Portfolio Allocation"]
related: ["[[asset-allocation]]", "[[portfolio-diversification]]", "[[bitcoin]]", "[[ethereum]]", "[[correlation]]", "[[volatility]]", "[[position-sizing]]", "[[rebalancing]]", "[[risk-parity]]", "[[kelly-criterion]]"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[asset-allocation]]", "[[portfolio-diversification]]"]
difficulty: intermediate
---

Crypto allocation is the deliberate decision of how large a share of a portfolio to assign to cryptocurrencies such as [[bitcoin]] and [[ethereum]], and how to obtain that exposure (spot, ETF, futures, or equities). Because crypto exhibits very high standalone [[volatility]] (annualised vol of roughly 50-80% for Bitcoin versus ~15-20% for the S&P 500), even a small percentage allocation contributes a disproportionate share of total portfolio risk, so sizing must be done on a risk-contribution basis rather than a dollar basis.

## Overview

The central tension of crypto allocation is asymmetry: crypto has historically delivered very high returns with very high risk and a non-trivial probability of catastrophic drawdown (Bitcoin has drawn down more than 80% on at least four occasions since 2011). The allocation question is therefore best framed as "how much can I lose on this sleeve without impairing the rest of the portfolio?" rather than "how much upside do I want?"

Common allocation frameworks:

- **Fixed small percentage** — a static 1-5% allocation, rebalanced periodically. This is the dominant institutional approach (many endowments and model portfolios cap crypto at 1-3%). It caps the maximum loss to the position size while retaining convex upside.
- **Volatility-targeted sizing** — size the position so its risk contribution equals a target (e.g. crypto contributes no more than 10-20% of total portfolio variance). Because crypto vol is ~4x equity vol, a vol-target of equal risk would imply roughly a quarter of the dollar weight of an equity sleeve. See [[risk-parity]] and [[volatility-targeting]].
- **Kelly / fractional-Kelly sizing** — using estimated edge and variance to derive an optimal growth-maximising fraction, then deploying a fraction (typically 1/4 to 1/2 Kelly) given the extreme estimation error in crypto return forecasts. See [[kelly-criterion]].
- **Barbell** — pairing a large safe sleeve (cash, T-bills) with a small high-convexity crypto sleeve, accepting that the crypto portion may go to zero.

## Ways to obtain exposure

The same target allocation can be implemented through very different instruments, each with distinct risk:

- **Spot crypto** held in self-custody or on an exchange — direct exposure plus custody/counterparty risk (see [[self-custody]], [[exchange-risk]]).
- **Spot ETFs** (e.g. US-listed Bitcoin and Ether ETFs approved 2024) — exposure inside a brokerage/superannuation wrapper, with management fees but no key-management burden.
- **Futures and perpetuals** — leveraged or capital-efficient exposure with [[funding-rate]] cost and liquidation risk.
- **Crypto-linked equities** (miners, exchanges, treasury companies like MicroStrategy) — levered, basis-risk-laden proxies that do not track spot one-for-one.

## Trading relevance

- **Correlation is regime-dependent.** Crypto's [[correlation]] to equities is low in calm regimes (a diversification benefit) but spikes toward 1 during liquidity crises (March 2020, the 2022 deleveraging), exactly when diversification is most needed. Allocations sized assuming low correlation can disappoint in tail events.
- **Rebalancing harvests volatility.** Because crypto is so volatile, disciplined [[rebalancing]] back to a fixed target mechanically sells strength and buys weakness, and historically added meaningful rebalancing premium — but also caps the compounding of a runaway bull move.
- **Position sizing dominates instrument selection.** The single largest driver of crypto P&L variance in a diversified book is the allocation percentage, not which coin or venue is chosen. Getting the sizing right matters more than alpha within the sleeve.

## Related

- [[asset-allocation]] — the broader portfolio construction discipline
- [[portfolio-diversification]] — why a crypto sleeve can (sometimes) reduce portfolio risk
- [[position-sizing]] / [[kelly-criterion]] — how to size a high-variance bet
- [[rebalancing]] — capturing the volatility harvest
- [[bitcoin]], [[ethereum]] — the primary allocation assets

## Sources

- Vanguard, BlackRock and Fidelity model-portfolio research notes on digital-asset allocation (1-3% caps).
- Bouri, E. et al. (2017). "On the hedge and safe haven properties of Bitcoin." *Finance Research Letters*.
- CoinMetrics / Bitcoin historical drawdown data.
- Thorp, E. (2006). "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market."
