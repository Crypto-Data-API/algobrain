---
title: "Position Trading Strategies"
type: overview
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [position-trading, trend-following]
aliases: ["Position Trading"]
related: ["[[strategies-overview]]", "[[swing-trading-overview]]", "[[fundamental-analysis-overview]]", "[[edge-taxonomy]]", "[[regime-matrix]]"]
---

# Position Trading

Position trading holds directional trades for weeks to months, based on macro trends, secular themes, and fundamental catalysts that take time to play out. It sits between [[swing-trading-overview|swing trading]] and outright investing on the time spectrum, and is the slowest-turnover style in the strategy catalog.

## What Distinguishes This Family

- **Edge sources** — primarily *risk-bearing* (collecting premia for holding exposure others won't, e.g. carry) and *analytical* (a macro or fundamental thesis the market has not yet priced). See [[edge-taxonomy]]. Behavioral edges also appear: position traders profit from the market's tendency to under-react to slow-moving structural change.
- **Typical timeframe** — weeks to months, sometimes years. Entries and exits are measured in days, not minutes; daily or weekly bars are sufficient.
- **Capital and data requirements** — low infrastructure burden: daily OHLCV, macro data, and fundamentals are enough. No co-location, no intraday feeds. Capital requirements are modest, but position sizing must absorb multi-week drawdowns without forced exits.
- **Who it suits** — traders who cannot watch screens intraday, who have conviction in macro/fundamental analysis, and who can tolerate short-term mark-to-market pain without abandoning a sound thesis. Patience is the operative skill; overtrading is the dominant failure mode.
- **Regime sensitivity** — position trades are heavily regime-dependent: trend and carry strategies bleed in choppy or risk-off regimes. Cross-check entries against the [[regime-matrix]].

## Strategies in This Category

- [[dollar-cost-averaging]] — Systematic accumulation over time that removes entry-timing risk; the simplest position-trading approach.
- [[carry-trade]] — Exploits interest rate differentials across currencies or yield-bearing assets, earning income while holding directional exposure.

### Closely Related Pages Elsewhere in the Catalog

Several position-timeframe strategies live in the main strategies folder:

- [[buy-and-hold]] — The passive benchmark every position strategy must beat.
- [[dca-strategy]] — DCA implementation notes (companion to [[dollar-cost-averaging]]).
- [[value-averaging]] — DCA variant that buys more when prices fall, less when they rise.
- [[momentum-investing]] — Long-horizon momentum applied at the portfolio level.
- [[macro-relative-value]] — Cross-asset macro positioning on relative mispricings.
- [[sector-rotation]] — Rotating exposure across sectors as the business cycle turns.

## All Pages (auto)

```dataview
TABLE status, updated, tags
FROM "wiki/strategies/position-trading"
WHERE type != "index" AND type != "overview"
SORT updated DESC
```

## Coverage Gaps

Topics that still need dedicated pages in this folder: long-horizon trend-following systems (see [[trend-following-cta]] in algorithmic), buy-and-hold vs active position management, and portfolio-level position trading.

## Related

- [[strategies-overview]] — top-level strategy catalog
- [[swing-trading-overview]] — the next-faster timeframe family
- [[fundamental-analysis-overview]] — thesis-driven sibling category
- [[quantitative-overview]] — systematic counterpart to discretionary positioning
- [[edge-taxonomy]] — the five edge categories referenced above
- [[regime-matrix]] — which regimes favor position trades
- [[atr-position-sizing]] — sizing positions to survive multi-week drawdowns
