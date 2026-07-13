---
title: "Trading Strategies"
type: overview
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [methodology, education, options, volatility]
aliases: ["Strategy Catalog", "Strategies"]
related: ["[[edge-taxonomy]]", "[[regime-matrix]]", "[[live-journal]]", "[[strategy-development-overview]]", "[[failure-modes]]", "[[multi-strategy-portfolio]]", "[[kelly-for-strategies]]", "[[market-impact-models]]", "[[barbell-portfolio]]"]
---

# Trading Strategies

Comprehensive catalog of trading strategies across all markets and timeframes. A trading strategy is a systematic set of rules for entering, managing, and exiting positions. This section organizes strategies by approach — from technical analysis and fundamental analysis to quantitative methods, algorithmic execution, and various timeframe-based categories. The goal is not to crown a single "best" strategy but to understand the trade-offs and find approaches that match your capital, time, skill set, and risk tolerance.

For a portfolio-level view, start with [[multi-strategy-portfolio]] to see how professionals combine uncorrelated strategies. [[regime-adaptive-strategy]] shows how to adjust your approach as market conditions change. And [[moving-average-crossover]] is the simplest possible systematic strategy — a good place to learn the mechanics before adding complexity.

## What Distinguishes the Strategy Families

Every strategy in this catalog should be classifiable by its **edge source** ([[edge-taxonomy]]): behavioral, structural, informational, analytical, latency, or risk-bearing. The categories below differ mainly in *which* edges they harvest, *how fast* they trade, and *what* they demand of the trader:

| Family | Dominant edge sources | Typical timeframe | Capital / data demands | Suits |
|---|---|---|---|---|
| Technical analysis | Behavioral, structural | Minutes–weeks | Low; OHLCV + indicators | Discretionary chart traders |
| Fundamental analysis | Analytical, behavioral | Weeks–years | Low–high; filings, macro data | Patient researchers |
| Quantitative | Analytical, behavioral (anomalies) | Days–months | Medium; clean historical data, stats skill | Model builders |
| Algorithmic | All six, incl. latency | Microseconds–months | Medium–high; engineering + infrastructure | Coders |
| Day trading | Structural, behavioral | Seconds–hours | PDT minimums; real-time L2/tape | Full-time screen traders |
| Swing / position trading | Behavioral, risk-bearing | Days–months | Low; end-of-day data | Part-time traders |
| Arbitrage | Structural, latency | Instant–weeks | Varies wildly; multi-venue access | Detail-obsessed operators |
| Combinations | Portfolio-level (diversification) | All | Enough capital to run several sleeves | Allocators |

Which strategies work in which market conditions is mapped in the [[regime-matrix]]; anything actually deployed is tracked in the [[live-journal]]. The methodology for producing and validating new strategies lives in [[strategy-development-overview|strategy development]].

## How to Use This Hub

This page is a *map*, not a recommendation. The intended path through it:

| If you want to… | Go to |
|---|---|
| Understand *why* a strategy could work | [[edge-taxonomy]] — the five-plus-one edge sources |
| See which strategies fit the current market | [[regime-matrix]] / [[regime-strategy-playbook]] |
| Combine several strategies into a book | [[multi-strategy-portfolio]] → [[kelly-for-strategies]] |
| Size positions and cap risk | [[position-sizing]], [[kelly-for-strategies]], [[atr-position-sizing]] |
| Check whether an edge survives costs | [[market-impact-models]], [[transaction-cost-modeling]], [[slippage]] |
| Validate a new strategy before trusting it | [[strategy-development-overview]], [[overfitting-detection]] |
| Know when to retire one | [[failure-modes]], [[when-to-retire-a-strategy]] |
| Track what is actually live | [[live-journal]] |

Every strategy page in this catalog should carry an [[edge-taxonomy|edge source]], a [[backtest-status|backtest status]], a [[strategy-capacity|capacity]] estimate, and [[when-to-retire-a-strategy|kill criteria]] in its frontmatter. A strategy that cannot name its edge or its capacity is a hypothesis, not a strategy.

## Edge-Source Crosswalk

The same edge can be harvested by many strategies; this crosswalk routes from the *reason a trade should work* ([[edge-taxonomy]]) to representative pages in the catalog:

| Edge source | What it exploits | Representative strategies |
|---|---|---|
| Behavioral | Predictable human error / overreaction | [[momentum-investing]], [[mean-reversion]], [[sentiment-trading]], [[social-arbitrage]] |
| Structural | Rules, flows, constraints of other participants | [[premium-selling-systematic]], [[leveraged-etf-rebalancing]], [[stat-arb]], [[managed-futures]] |
| Informational | Knowing something sooner or processing it better | [[news-trading]], [[alternative-data-alpha]], [[earnings-volatility-trading]] |
| Analytical | Superior modeling of the same public data | [[equity-long-short]], [[macro-relative-value]], [[cta-strategies]] |
| Latency | Being faster to act | [[arbitrage-overview]], [[conversion-reversal-arbitrage]] |
| Risk-bearing | Being paid to hold risk others shed | [[short-volatility-strategies]], [[cash-secured-puts]], [[stablecoin-yield]] |

A strategy harvesting a *risk-bearing* edge (selling insurance) and one harvesting a *behavioral* edge (fading overreaction) fail in opposite regimes — which is exactly why combining them across [[kelly-for-strategies|correlation-adjusted]] sleeves smooths the book.

## Start Here

- [[multi-strategy-portfolio]] — combining strategies for smoother, more robust returns
- [[regime-adaptive-strategy]] — adapting to bull, bear, and sideways markets
- [[moving-average-crossover]] — the simplest trend-following strategy and a great starting point

## Subcategories

- [[technical-analysis-overview|Technical Analysis]] — Chart patterns, indicators, price action, and the options-structure library
- [[fundamental-analysis-overview|Fundamental Analysis]] — Financial statements, valuations, macro, and event-driven catalysts
- [[quantitative-overview|Quantitative]] — Statistical and mathematical approaches: mean reversion, anomalies, vol models
- [[algorithmic-overview|Algorithmic]] — Automated trading systems, from factor portfolios to MEV and DeFi automation
- [[day-trading-overview|Day Trading]] — Intraday strategies: scalping, VWAP, order flow, market making
- [[swing-trading-overview|Swing Trading]] — Multi-day to multi-week holds
- [[position-trading-overview|Position Trading]] — Long-term directional trades, carry, and accumulation
- [[arbitrage-overview|Arbitrage]] — Price-discrepancy exploitation across 100+ catalogued variants
- [[combinations-overview|Combinations]] — Strategy overlays and portfolio-level blends; entry point: [[multi-strategy-portfolio]]

## Alt-Data & Information-Edge Strategies

- [[social-arbitrage]] — [[chris-camillo]]'s methodology: detect consumer-trend inflections on social media before sell-side research catches up
- [[alternative-data-alpha]] — Institutional version using paid feeds (satellite imagery, credit cards, app data)
- [[sentiment-trading]] — Contrarian and momentum approaches on aggregated sentiment indicators
- [[news-trading]] — Event-driven execution on headlines and earnings

## Top-Level Strategy Pages

Pages that live directly in this section rather than a subcategory, grouped by theme.

### Options — Income & Premium Selling

- [[covered-call-strategy]] — Selling calls against stock you own for recurring premium
- [[covered-calls]] — Companion page on covered-call mechanics and variants
- [[cash-secured-puts]] — Selling puts backed by cash, to earn premium or acquire stock cheaper
- [[credit-spread]] — Defined-risk premium selling via short option + further-OTM long
- [[credit-spreads]] — Companion page on credit-spread construction and management
- [[short-put-spread]] — Bullish defined-risk put credit spread
- [[iron-condors]] — Range-bound premium selling with wings on both sides
- [[options-income]] — Overview of income-generation approaches with options
- [[income-strategies]] — Broader income-strategy survey across instruments
- [[options-premium-selling]] — The short-premium approach and its risk profile
- [[premium-selling-systematic]] — Rules-based, mechanical premium-selling program
- [[zero-dte-options]] — Same-day-expiry options trading and its distinct risk dynamics
- [[tastytrade-mechanics]] — The tastytrade playbook: high-probability premium selling mechanics
- [[managing-winners]] — Exit discipline for short-premium trades (e.g. close at 50% max profit)

### Options — Directional & Spreads

- [[long-call]] — Defined-risk bullish exposure via bought calls
- [[long-put]] — Defined-risk bearish exposure via bought puts
- [[call-spread]] — Vertical call structures for capped-cost directional bets
- [[put-spread]] — Vertical put structures for capped-cost downside bets
- [[debit-spread]] — Paying net premium for defined-risk directional spreads
- [[calendar-spread]] — Selling near-dated against longer-dated options to harvest time decay
- [[ratio-calendar-spread]] — Calendar with unequal legs for asymmetric payoff
- [[itpm-ratio-calendar-spread]] — ITPM's institutional take on the ratio calendar
- [[put-tree]] — Multi-strike put structure for cheap downside convexity
- [[leaps]] — Long-dated options as stock substitutes
- [[leaps-strategy]] — Companion page on LEAPS-based portfolio strategies
- [[long-straddle]] — Buying call + put to profit from a large move either way

### Options — Hedging & Volatility

- [[protective-puts]] — Insuring stock positions with bought puts
- [[options-hedging]] — Survey of options-based hedging techniques
- [[hedging-strategies]] — Broader hedging survey across instruments
- [[spx-puts]] — Index put protection for equity portfolios
- [[vix-calls]] — Tail protection via VIX call options
- [[vix-call-spreads]] — Cheaper defined-cost tail hedges with VIX spreads
- [[5-percent-otm-put-overlay]] — Systematic 5% OTM put protection overlay
- [[long-vol-overlay]] — Persistent long-volatility sleeve over a core portfolio
- [[long-volatility-strategies]] — Strategies that profit when volatility rises
- [[short-volatility-strategies]] — Strategies that harvest the volatility risk premium
- [[volatility-trading]] — Trading volatility as an asset class
- [[earnings-volatility-trading]] — Positioning around earnings-driven IV swings
- [[earnings-iv-crush]] — Trading the post-earnings collapse in implied volatility
- [[delta-hedging]] — Neutralizing directional exposure to isolate other Greeks
- [[gamma-scalping]] — Monetizing realized volatility around a delta-hedged options position
- [[conversion-reversal-arbitrage]] — Locking in mispricing between synthetic and actual stock

### Equities & Portfolio

- [[buy-and-hold]] — The passive baseline every active strategy must beat
- [[dca-strategy]] — Dollar-cost averaging into positions on a fixed schedule
- [[value-averaging]] — Path-dependent contribution sizing targeting a value growth path
- [[momentum-investing]] — Buying recent winners; one of the most robust documented anomalies
- [[momentum-stocks]] — Stock-level momentum selection and management
- [[small-cap-momentum]] — Momentum applied to the small-cap universe
- [[equity-long-short]] — Long undervalued / short overvalued equity books
- [[range-trading]] — Buying support and selling resistance in sideways markets
- [[leveraged-etf-rebalancing]] — Exploiting (or avoiding) volatility decay in leveraged ETFs
- [[triple-screen-system]] — Elder's multi-timeframe filter combining trend and oscillator signals
- [[swing-trading]] — General swing-trading methodology page

### Macro & Managed Futures

- [[macro-relative-value]] — Cross-asset rich/cheap trades on macro fundamentals
- [[managed-futures]] — The CTA asset class: systematic futures across markets
- [[cta-strategies]] — Strategy taxonomy within the CTA space
- [[stat-arb]] — Statistical arbitrage: portfolio-level mean reversion at scale

### Crypto & Prediction Markets

- [[stablecoin-yield]] — Earning yield on stablecoins across CeFi/DeFi venues
- [[alpha-token-arbitrage]] — Exploiting pricing inefficiencies in exchange alpha/launchpad tokens
- [[bittensor-subnet-rotation]] — Rotating among Bittensor subnets by emissions and fundamentals
- [[tao-validator-delegation]] — Yield via TAO delegation to validators
- [[polymarket-as-crypto-leading-indicator]] — Using prediction-market odds as a crypto signal
- [[prediction-market-strategies]] — Trading approaches on Polymarket-style venues

### Thematic & AI-Cycle Theses

- [[ai-recession-playbook]] — Positioning for an AI-driven economic downturn
- [[ai-sector-rotation-energy-hedge]] — AI beneficiaries long vs energy-constraint hedges
- [[crypto-ai-recession-shorts]] — Short candidates in crypto under an AI-recession scenario
- [[white-collar-ai-displacement-short]] — Shorting sectors exposed to white-collar AI displacement
- [[tech-hub-muni-bond-short]] — Shorting municipal credit of AI-disrupted metro economies
- [[mythos-capability-overhang-vol]] — Volatility positioning around AI capability-release shocks
- [[mythos-release-window-exploit-short]] — Shorting into AI model release windows (Hyperliquid perps)
- [[glasswing-partner-long-basket]] — Long basket of named AI-infrastructure partners

### Risk & Process

- [[atr-position-sizing]] — Sizing positions by volatility (ATR) rather than fixed notional
- [[atr-trailing-stop]] — Volatility-adaptive trailing exits
- [[regime-matrix]] — Master map of which strategies work in which market regimes
- [[regime-strategy-playbook]] — Action plan for switching strategy mix as regimes change
- [[live-journal]] — The deployment journal for strategies actually running

## From Strategy to Book: Sizing, Costs, and Survival

A strategy is only the *signal*. Turning it into a deployable sleeve requires three further layers, each with its own home in the wiki:

| Layer | Question | Where it lives |
|---|---|---|
| Sizing | How much capital does this strategy deserve, given its edge and its correlation to the rest of the book? | [[kelly-for-strategies]], [[position-sizing]], [[multi-strategy-portfolio]] |
| Cost realism | Does the edge survive spread, [[market-impact-models\|market impact]], and fees at the size I want to trade? | [[transaction-cost-modeling]], [[slippage]], [[market-impact-models]], [[strategy-capacity]] |
| Survival | What caps the downside when the edge decays or the regime flips? | [[barbell-portfolio]], [[long-vol-overlay]], [[hedging-program-failure-modes]], [[when-to-retire-a-strategy]] |

The recurring lesson across the catalog: most retail-attractive edges are real but *capacity-limited* — the [[market-impact-models#Capacity Implications|square-root impact law]] eats the alpha well before institutional size — and most short-premium income edges are real but *tail-exposed*, requiring an explicit convex overlay (the [[barbell-portfolio|barbell]] / [[long-vol-vs-short-vol|long-vol-overlay]] logic) to survive the regime in which they break.

## All Strategy Pages

```dataview
TABLE status, strategy_type, timeframe, complexity
FROM "wiki/strategies"
WHERE type = "strategy"
SORT updated DESC
```

## Related

- [[edge-taxonomy]] — the five-plus-one sources of edge every strategy must claim
- [[regime-matrix]] — strategy-vs-regime performance map
- [[live-journal]] — lifecycle tracking for deployed strategies
- [[strategy-development-overview|Strategy development]] — how new strategies get researched, validated, and promoted
- [[failure-modes]] — how strategies die: decay, crowding, regime change, leverage
- [[overfitting-detection]] — separating real edges from backtest artifacts
- [[risk-management-overview|Risk management]] — position sizing, drawdown control, kill criteria
- [[kelly-for-strategies]] — correlation-adjusted capital allocation across sleeves
- [[market-impact-models]] — the cost overlay that caps strategy capacity
- [[barbell-portfolio]] — the survival-first shape a multi-strategy book can take
- [[when-to-retire-a-strategy]] — the kill decision for a decayed sleeve
- [[markets-overview]] — the instruments and venues these strategies trade

## Sources

General market knowledge; no specific wiki source ingested yet. Individual strategy pages carry their own sourced citations.
