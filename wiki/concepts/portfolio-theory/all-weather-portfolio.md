---
title: "All-Weather Portfolio"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [portfolio-theory, risk-management, market-regime, commodities, bonds]
aliases: ["All-Weather Portfolio", "all-weather", "All Weather", "Bridgewater All Weather"]
related: ["[[ray-dalio]]", "[[bridgewater-associates]]", "[[risk-parity]]", "[[asset-allocation]]", "[[diversification]]", "[[dragon-portfolio]]", "[[rebalancing]]", "[[correlation-breakdown]]"]
domain: [portfolio-theory]
prerequisites: ["[[risk-parity]]", "[[asset-allocation]]"]
difficulty: intermediate
---

The **All-Weather Portfolio** is an asset allocation strategy developed by [[ray-dalio]] at [[bridgewater-associates]], designed to perform well across all economic environments -- growth, recession, inflation, and deflation. It is the retail-accessible expression of Bridgewater's institutional All Weather strategy, launched in 1996 and built on the firm's [[risk-parity]] framework.

Built on [[risk-parity]] principles, the strategy balances exposure to [[stocks]], [[bonds]], [[commodities]], and inflation-linked assets so that no single economic regime dominates portfolio performance.

## Target Allocation

The simplified retail version of the All-Weather Portfolio, as popularized by Tony Robbins after interviewing [[ray-dalio]], uses the following allocation:

| Asset Class | Allocation |
|---|---|
| U.S. stocks (total market) | 30% |
| Long-term U.S. Treasury bonds (20+ years) | 40% |
| Intermediate-term U.S. Treasury bonds (7-10 years) | 15% |
| Gold | 7.5% |
| Commodities (broad basket) | 7.5% |

The heavy bond allocation (55% total) may seem counterintuitive, but it reflects the [[risk-parity]] insight that bonds are less volatile than stocks. By allocating more capital to bonds, each asset class contributes roughly equal risk to the portfolio.

## The Four Economic Environments

Dalio's key insight is that asset prices are driven by two variables -- growth and inflation -- each of which can come in higher or lower than the market already expects. That produces a 2x2 grid of four "economic seasons," and every asset is biased toward one quadrant:

| | Growth rising | Growth falling |
|---|---|---|
| **Inflation rising** | Equities, commodities, EM debt | Commodities, gold, inflation-linked bonds (TIPS) |
| **Inflation falling** | Equities, corporate credit | Nominal government bonds (long duration) |

The thesis is that the *future* mix of these environments is unknowable, so rather than forecast it, you hold roughly equal **risk** exposure to each quadrant. Whichever season arrives, the assets that thrive in it offset the assets that suffer.

## The Risk Parity Foundation

By balancing *risk* across these regimes rather than allocating by *dollar amount*, the portfolio avoids concentration in any single economic outcome. The mechanism is [[risk-parity]]: because bonds are far less volatile than equities, an equal-dollar split would leave equity risk dominating the portfolio (a 60/40 portfolio is roughly 90% equity *risk* despite being 60% equity *capital*). The All-Weather construction allocates more capital to low-volatility assets (and, in the institutional version, applies [[leverage]] to bonds) so that each asset class contributes a comparable share of total portfolio variance. The result targets a smoother return path and a higher [[sharpe-ratio]] than a conventional equity-heavy allocation -- in exchange for trailing in equity bull markets.

## Historical Performance

The All-Weather Portfolio has delivered steady but unspectacular returns -- typically underperforming a 60/40 stock/bond portfolio during bull markets but significantly outperforming during drawdowns. It experienced notably smaller losses during the [[2008-global-financial-crisis]] and the 2020 COVID crash. The strategy struggled in 2022 when both stocks and bonds fell simultaneously, challenging the assumption of negative stock-bond correlation.

The 2022 episode exposes the strategy's key vulnerability: it assumes the stock-bond correlation is reliably negative. When inflation surges and central banks hike aggressively, stocks and bonds fall together ([[correlation-breakdown]]), and the heavy bond allocation that normally cushions equity drawdowns instead amplifies losses. Christopher Cole's [[dragon-portfolio]] is a direct critique, arguing All Weather is implicitly long the "secular disinflation" regime of 1981-2021 and under-hedged against inflationary and stagflationary tail risks.

## Trading and Portfolio Relevance

- A practical template for investors who want a low-maintenance, [[rebalancing|periodically rebalanced]] allocation that does not depend on forecasting the macro cycle.
- The risk-parity lens generalizes: budget by risk contribution, not capital, and treat correlation regimes -- not just expected returns -- as the central design variable.
- The 2022 failure is a live lesson in [[correlation-breakdown]]: any "all-weather" claim is only as good as the correlation assumptions it embeds.

## Related

- [[ray-dalio]]
- [[bridgewater-associates]]
- [[risk-parity]]
- [[asset-allocation]]
- [[diversification]]
- [[dragon-portfolio]] -- a tail-hedged alternative critiquing All Weather
- [[correlation-breakdown]] -- the stock-bond correlation risk that hurt All Weather in 2022

## Sources

- Dalio, Ray, and Bob Prince. "The All Weather Strategy" / "Engineering Targeted Returns and Risks." Bridgewater Associates (2011).
- Robbins, Tony. *Money: Master the Game* (2014) -- the popularized retail allocation drawn from a Dalio interview.
- Cole, Christopher. "The Allegory of the Hawk and Serpent." Artemis Capital (2020) -- critique of risk-parity / All Weather and the [[dragon-portfolio]] alternative.
