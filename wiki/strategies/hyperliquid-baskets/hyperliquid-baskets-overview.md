---
title: "Alfred Hyperliquid Basket Library"
type: overview
created: 2026-06-16
updated: 2026-06-16
status: good
tags: [crypto, perpetuals, hyperliquid, algorithmic, quantitative, market-regime, risk-management, methodology]
aliases: ["Hyperliquid Baskets", "Alfred Baskets", "Trading Baskets", "Basket Library", "Signal Baskets"]
related: ["[[crypto-market-regime-taxonomy]]", "[[regime-strategy-playbook]]", "[[regime-matrix]]", "[[regime-adaptive-strategy]]", "[[multi-strategy-portfolio]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[live-journal]]", "[[hyperliquid]]", "[[2026-06-03-cryptodataapi-14-basket-regime-framework]]"]
---

# Alfred Hyperliquid Basket Library

A **basket** is one self-contained trading sleeve in the Alfred systematic perpetual-futures system on [[hyperliquid|Hyperliquid]]: a defined signal, entry/exit logic, position-sizing rule, and kill criteria, run with its own capital allocation and tracked independently. This page is the index of all **27 baskets**, each documented on its own page following the wiki's standard [[strategies-overview#strategy-page-sections|strategy-page structure]].

> **Not investment advice.** These pages document *how each setup is designed to work* — the edge thesis, rules, and failure modes. Positioning, sizing, and deployment are downstream decisions. Every performance figure on the basket pages is a clearly-labelled **illustrative estimate**, not a backtest result.

## Baskets vs. Regimes — two orthogonal layers

These 27 baskets are **strategies**. They are *not* the same as the **14 regime meta-baskets** in the [[crypto-market-regime-taxonomy|crypto regime taxonomy]] (a [[2026-06-03-cryptodataapi-14-basket-regime-framework|VENTURE AI LABS framework]]), which describe *market states*. The relationship is:

- The **regime taxonomy** answers *"what state is the market in right now?"* (e.g. full bear, funding-extreme, compressed vol, post-cascade).
- The **basket library** answers *"given that state, which sleeve do I deploy?"* — the [[regime-strategy-playbook|regime → strategy mapping]] in concrete form.

Each basket below is tagged with the regime(s) that **gate** it. The central discipline — from [[crypto-market-regime-taxonomy]] and [[regime-adaptive-strategy]] — is that **a basket run in the wrong regime is not merely suboptimal, it is actively harmful**: a [[range-mean-reversion|range-fade]] dies the moment a [[volatility-compression-breakout|vol expansion]] breaks the range; an [[oi-confirmed-trend|OI-trend]] long gets run over by a [[long-liquidation-cascade|downside cascade]]. Detection gates deployment.

## Live status snapshot (2026-06-16)

A point-in-time read of the active book. **Illustrative and already stale** — it shows the shape of deployment, not a current call.

| Basket | Status | Capital | Notes |
|--------|--------|---------|-------|
| [[oi-confirmed-trend]] | **Most active** | $2,375 | 4 open positions |
| [[range-mean-reversion]] | **Most capital-efficient** | 81.1% deployed | 3 long, 1 short |
| [[range-breakout-breakdown]] | **Best-performing active** | 27.4% utilisation | 1 long, 1 short |
| [[trend-pullback-rally-fade]] | Active | up to $2,375 max | matches OI-Confirmed capacity |
| [[crowded-long-funding-fade]] | Armed, not deployed | $0 | 2 open signals, criteria not yet met |

## The 27 baskets

Grouped by function. Each row links the basket page, its dominant [[edge-taxonomy|edge source]], gating regime(s), and typical timeframe.

### Directional & trend
| Basket | Edge | Regime gate | Timeframe |
|--------|------|-------------|-----------|
| [[defensive-majors]] | Risk-bearing | [[macro-trend-regime\|Macro]] risk-off, [[volatility-regime-classification\|vol]] | Position |
| [[full-bear-short-book]] | Structural / behavioral | [[macro-trend-regime\|Full bear]] | Swing–position |
| [[oi-confirmed-trend]] | Behavioral / structural | [[derivatives-native-regime\|Derivs]] + [[technical-structural-regime\|technical]] | Swing |
| [[trend-pullback-rally-fade]] | Behavioral | [[technical-structural-regime\|Technical]] + [[macro-trend-regime\|macro]] | Swing |
| [[major-trend-reclaim-rejection]] | Behavioral / structural | [[technical-structural-regime\|Technical]] | Swing–position |

### Funding & liquidation mechanics
| Basket | Edge | Regime gate | Timeframe |
|--------|------|-------------|-----------|
| [[crowded-short-funding-fade]] | Behavioral / risk-bearing | [[derivatives-native-regime\|Derivs]] + [[basis-carry-regime\|basis]] | Swing |
| [[crowded-long-funding-fade]] | Behavioral / risk-bearing | [[derivatives-native-regime\|Derivs]] + [[basis-carry-regime\|basis]] | Swing |
| [[funding-rate-harvest]] | Structural / risk-bearing | [[basis-carry-regime\|Carry/basis]] | Swing |
| [[short-liquidation-squeeze]] | Structural / latency | [[derivatives-native-regime\|Derivs]] + [[liquidity-depth-regime\|depth]] | Scalp–intraday |
| [[long-liquidation-cascade]] | Structural / latency | [[derivatives-native-regime\|Derivs]] + [[liquidity-depth-regime\|depth]] | Scalp–intraday |
| [[post-liquidation-rebound]] | Behavioral / structural | [[derivatives-native-regime\|Derivs]] + [[security-black-swan-regime\|shock]] | Scalp–swing |

### Reversal, exhaustion & flow-microstructure
| Basket | Edge | Regime gate | Timeframe |
|--------|------|-------------|-----------|
| [[distribution-post-peak-short-book]] | Behavioral / informational | [[technical-structural-regime\|Technical]] + [[on-chain-regime\|on-chain]] | Swing |
| [[oi-price-exhaustion]] | Behavioral / structural | [[derivatives-native-regime\|Derivs]] + [[technical-structural-regime\|technical]] | Swing |
| [[liquidity-vacuum-momentum]] | Structural / latency | [[liquidity-depth-regime\|Depth]] + [[technical-structural-regime\|technical]] | Scalp |

### Range, breakout & volatility
| Basket | Edge | Regime gate | Timeframe |
|--------|------|-------------|-----------|
| [[breakout-and-retest]] | Behavioral / structural | [[technical-structural-regime\|Technical]] + [[volatility-regime-classification\|vol]] | Swing |
| [[range-breakout-breakdown]] | Behavioral / structural | [[technical-structural-regime\|Technical]] + [[volatility-regime-classification\|vol]] | Intraday–swing |
| [[failed-breakout-failed-breakdown]] | Behavioral | [[technical-structural-regime\|Technical]] + [[liquidity-depth-regime\|depth]] | Intraday–swing |
| [[range-mean-reversion]] | Behavioral / structural | [[technical-structural-regime\|Technical]] + [[volatility-regime-classification\|vol]] | Intraday–swing |
| [[volatility-compression-breakout]] | Structural / behavioral | [[volatility-regime-classification\|Vol]] + [[technical-structural-regime\|technical]] | Swing |

### Macro, flow & breadth
| Basket | Edge | Regime gate | Timeframe |
|--------|------|-------------|-----------|
| [[breadth-and-momentum-divergence]] | Analytical / behavioral | [[macro-trend-regime\|Macro]] + [[bitcoin-cycle-regime\|BTC cycle]] | Swing |
| [[global-liquidity-expansion-contraction]] | Analytical / informational | [[crypto-macro-correlation-regime\|Macro corr]] + [[institutional-flow-regime\|flow]] | Position–long-term |
| [[macro-event-pump]] | Informational / behavioral | [[event-catalyst-regime\|Event]] + [[policy-shock-regime\|policy]] | Intraday–swing |
| [[etf-and-institutional-flow]] | Informational / structural | [[institutional-flow-regime\|Flow]] + [[on-chain-regime\|on-chain]] | Position |

### Event & idiosyncratic
| Basket | Edge | Regime gate | Timeframe |
|--------|------|-------------|-----------|
| [[exchange-listing-delisting]] | Informational / latency | [[event-catalyst-regime\|Event]] | Scalp–intraday |
| [[token-unlock-supply-event]] | Informational / structural | [[event-catalyst-regime\|Event]] + [[on-chain-regime\|on-chain]] | Swing |
| [[cross-sectional-relative-value]] | Analytical / structural | [[derivatives-native-regime\|Derivs]] (market-neutral) | Swing |
| [[meme-coin-cycle]] | Behavioral | [[meme-speculative-regime\|Meme/spec]] | Swing |

## How the baskets fit together

- **Anchors and books.** [[defensive-majors]] is the risk-off anchor that holds when nothing else is firing; [[full-bear-short-book]] and [[distribution-post-peak-short-book]] are its directional opposites (the latter the selective precursor to the former).
- **Trend confirmation vs. exhaustion.** [[oi-confirmed-trend]] and [[oi-price-exhaustion]] are mirror images on the same [[open-interest]] signal — one trades rising OI *with* price, the other fading OI *divergence* from price.
- **Funding spectrum.** [[funding-rate-harvest]] (neutral carry) → [[crowded-short-funding-fade]] / [[crowded-long-funding-fade]] (directional carry + reversion) → [[short-liquidation-squeeze]] / [[long-liquidation-cascade]] (aggressive mechanical-flow rides) → [[post-liquidation-rebound]] (the morning-after mean reversion). They sit on a single axis of funding/liquidation aggression.
- **The breakout quartet.** [[range-breakout-breakdown]] (enter the break), [[breakout-and-retest]] (wait for the retest), [[failed-breakout-failed-breakdown]] (fade the trap), and [[range-mean-reversion]] (assume the range holds) are four mutually-exclusive bets on the *same* range structure — which one is right depends entirely on the [[volatility-regime-classification|vol]] and [[liquidity-depth-regime|depth]] regime. [[volatility-compression-breakout]] front-runs the moment the range resolves.
- **Overlays, not standalone trades.** [[breadth-and-momentum-divergence]] and [[global-liquidity-expansion-contraction]] are best used as **regime filters** that bias the directional baskets rather than as standalone sleeves.
- **Market-neutral diversifier.** [[cross-sectional-relative-value]] is the only dollar-neutral sleeve — it harvests dispersion within a sector and is the natural diversifier to the directional book ([[multi-strategy-portfolio]]).

## Shared Hyperliquid execution realities

Every basket inherits the same venue constraints (detailed on each page):

- **Funding is carry, with a sign.** Positive [[funding-rate|funding]] = longs pay shorts; negative = shorts pay longs. Several baskets are *paid to wait*; others bleed carry — the sign flips the economics, so it is always part of entry logic. See [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation + ADL.** Hyperliquid can liquidate on one mark-price tick and auto-deleverage winners. Held legs are sized to survive a 15–20% adverse move; 2–3x on majors is the ceiling for a position meant to *survive*. See [[hyperliquid-liquidation-engine]].
- **Isolated margin per leg**, so a blow-up on one thin-alt sleeve cannot cascade into the BTC/ETH book.
- **Thin-perp squeeze risk (the [[2025-03-jellyjelly-hlp-attack|JELLY pattern]]).** Low-float, low-OI perps can be pumped to liquidate a short into the HLP vault and trigger a governance force-settle. Per-name caps, volume gates, and a "+30% in <1h on thin volume → cover" guard appear across the aggressive baskets.
- **Transparent on-chain OI / leverage data** (a Hyperliquid edge) lets these baskets read crowding and fragility in near-real-time — see [[hypurrscan]], [[coinglass]].

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the VENTURE AI LABS regime framework these baskets are deployed against.
- [[crypto-market-regime-taxonomy]] — the 14-regime taxonomy and the regime-gating discipline.
- [[regime-strategy-playbook]] — the regime → concrete-strategy mapping these baskets implement.
- [[hyperliquid-funding-rate-microstructure]], [[hyperliquid-liquidation-engine]] — venue mechanics every basket inherits.
- [[edge-taxonomy]], [[failure-modes]] — the edge classification and failure-mode vocabulary each page uses.

## Related

- [[crypto-market-regime-taxonomy]] — market states (the "when")
- [[regime-strategy-playbook]] — regime → strategy mapping
- [[regime-matrix]] — strategy-by-regime performance map
- [[multi-strategy-portfolio]] — combining uncorrelated baskets into a book
- [[live-journal]] — deployment journal for anything actually running
- [[strategies-overview]] — the full wiki strategy catalog
