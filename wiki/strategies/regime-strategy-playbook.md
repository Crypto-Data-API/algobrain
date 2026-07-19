---
title: "Regime → Strategy Playbook"
type: index
created: 2026-06-03
updated: 2026-07-19
status: good
tags: [strategies, crypto, market-regime, regime-detection, quantitative]
aliases: ["Regime Strategy Playbook", "Regime to Strategy Mapping", "Crypto Regime Playbook"]
related: ["[[crypto-market-regime-taxonomy]]", "[[regime-matrix]]", "[[regime-adaptive-strategy]]", "[[market-regime-detection-ml]]", "[[crypto-perp-backtesting-pitfalls]]", "[[hyperliquid]]", "[[cryptodataapi]]"]
---

# Regime → Strategy Playbook

The [[crypto-market-regime-taxonomy|14-basket regime taxonomy]] is only useful if each detected regime maps to a concrete, deployable strategy. This page is that bridge: for every basket it lists the **wiki strategy pages that are the natural play** when that regime is active, plus the **coverage gaps** where the wiki names a regime but lacks a dedicated strategy for it. It is the operational companion to the taxonomy and to [[regime-matrix]] (the six-dimension, asset-agnostic strategy-by-regime matrix).

The governing principle from the framework: **a strategy is only valid inside the regime it is gated to.** A [[funding-rate-arbitrage|funding-carry]] harvest that prints in a calm [[basis-carry-regime|healthy-basis]] regime gets run over by a [[liquidity-depth-regime|depth-withdrawal cascade]]; a [[range-trading|range fade]] with the highest hit-rate in chop is a guaranteed loser the instant a [[volatility-regime-classification|vol expansion]] breaks the range. Detect first, then deploy only what is gated to the detected state.

> **Backtesting note.** Regime gating must be validated **point-in-time** — the regime label at decision time can only use data that had closed by then (no peeking at the bar/flow that defines the regime in hindsight). See [[crypto-perp-backtesting-pitfalls]] (regime-aware windowing), [[regime-adaptive-strategy]] (the gating meta-strategy), and [[market-regime-detection-ml]] (detection machinery). All strategy slugs below were verified to exist in the wiki at time of writing.

## The Mapping

| # | Basket | Natural strategies (gated to this regime) | Coverage |
|---|--------|-------------------------------------------|----------|
| 1 | [[macro-trend-regime\|Macro Trend]] | [[trend-following-cta]], [[moving-average-crossover]], [[turtle-trading]], [[supertrend]], [[donchian-channel-breakout]], [[managed-futures]], [[momentum-rotation]] | Strong |
| 2 | [[bitcoin-cycle-regime\|BTC Cycle]] | [[dollar-cost-averaging]], [[buy-and-hold]], [[value-averaging]], [[momentum-investing]] | Partial — no halving/cycle-timing play |
| 3 | [[meme-speculative-regime\|Meme / Speculative]] | [[memecoin-sniping]], [[pump-fun-bonding-curve-sniping]], [[token-migration-sniping]], [[telegram-bot-trading]], [[social-arbitrage]], [[sentiment-trading]] | Strong |
| 4 | [[derivatives-native-regime\|Derivatives-Native]] | [[funding-rate-arbitrage]], [[liquidation-cascade-fade]], [[liquidation-cascade-arbitrage]], [[hl-vs-cex-funding-divergence]], [[stop-hunting-and-liquidity-sweeps]] | Strongest |
| 5 | [[event-catalyst-regime\|Event / Catalyst]] | [[event-driven-trading]], [[news-trading]], [[token-unlock-arbitrage]], regulatory-approval-arbitrage | Partial — mostly arb-framed |
| 6 | [[crypto-macro-correlation-regime\|Macro Correlation]] | [[risk-on-risk-off-framework]], [[cross-asset-signals]], [[macro-relative-value]] | Partial — no crypto-beta-vs-DXY/Nasdaq play |
| 7 | [[on-chain-regime\|On-Chain]] | [[on-chain-flow-trading]], [[miner-capitulation-bottom]], [[on-chain-smart-money-tracking]], [[copy-trading]] | Now covered |
| 8 | [[basis-carry-regime\|Carry / Basis]] | [[basis-trading]], [[funding-rate-arbitrage]], [[cash-and-carry]], [[carry-trade]], [[stablecoin-yield]], [[hyperliquid-hlp-basis-arbitrage]] | Strong |
| 9 | [[liquidity-depth-regime\|Liquidity / Depth]] | [[market-making-strategy]], [[jit-liquidity]], [[liquidity-sniping]], [[implementation-shortfall]], [[slippage-optimal-pathfinding]] | Partial — provision/execution, not gating |
| 10 | [[institutional-flow-regime\|Institutional Flow]] | [[gbtc-discount-arbitrage]], [[etf-arbitrage]], [[structural-forced-selling]], [[expiration-and-rebalancing-flows]] | Partial — no flow-following directional play |
| 11 | [[security-black-swan-regime\|Security / Black Swan]] | [[stablecoin-depeg-profit-capture]], [[post-hack-incident-response-arb]], [[cross-chain-contagion-hedge]], [[counterparty-stress-arbitrage]], [[tail-risk-hedging]] | Strong |
| 12 | [[policy-shock-regime\|Geopolitical / Policy]] | [[crypto-policy-shock-trading]], [[news-trading]], [[regulatory-arbitrage]], regulatory-approval-arbitrage, [[event-driven-trading]] | Now covered |
| 13 | [[volatility-regime-classification\|Volatility]] (overlay) | [[volatility-targeting]], [[volatility-breakout]], [[long-volatility-strategies]], [[short-volatility-strategies]], [[straddle-strangle]], [[gamma-scalping]], [[tail-risk-hedging]] | Strong |
| 14 | [[technical-structural-regime\|Technical / Structural]] (overlay) | [[range-trading]], [[grid-trading]], [[mean-reversion]], [[bollinger-band-reversion]], [[rsi-mean-reversion]], [[breakout-strategies]], [[vwap-trading]], [[supply-demand-zones]] | Strong |

## Coverage Gaps (candidate new strategy pages)

The taxonomy names regimes the wiki cannot yet *trade* with a dedicated page. In rough priority:

- ~~**On-chain (basket 7)**~~ — **filled 2026-06-03**: [[on-chain-flow-trading]] (exchange flows / dry powder / dormancy / whale accumulation as directional signals) and [[miner-capitulation-bottom]] (hash-ribbon late-bear bottoming) now cover the directional on-chain plays. Mechanics in [[on-chain-analysis]] / [[whale-trade]].
- ~~**Policy shock (basket 12)**~~ — **filled 2026-06-03**: [[crypto-policy-shock-trading]] now provides the crypto-policy directional playbook (pro-crypto order / ban / tariff / rate-print signatures), distinct from generic [[news-trading]] / [[regulatory-arbitrage]].
- **BTC cycle (basket 2)** — generic accumulation only; no halving / cycle-top timing play tied to [[bitcoin-halving]] or MVRV. (Partly addressed by [[miner-capitulation-bottom]] on the bottoming side.)
- **Macro correlation (basket 6)** — no crypto-beta-vs-[[dxy|DXY]]/Nasdaq rotation strategy; relies on equity-side cross-asset pages.
- **Liquidity / depth (basket 9)** — has liquidity-provision and execution pages but no "OI-vs-depth size-filter / depth-withdrawal" *gating* strategy.
- **Institutional flow (basket 10)** — arb-framed only ([[gbtc-discount-arbitrage]], [[etf-arbitrage]]); no ETF-flow-following directional page.

## Relationship to the Six-Dimension Matrix

[[regime-matrix]] rates strategies across six asset-agnostic dimensions (Trending Up/Down, Sideways/Chop, High Vol, Low Vol, Risk-Off). The 14 baskets are the **crypto-specific, perps-native states** that compose with those dimensions:

- **Trending Up / Down** ← baskets 1 (macro-trend) & 2 (BTC cycle); basket 6 (macro-correlation) modulates direction.
- **Sideways / Chop** ← chop side of basket 14 (technical) + calm side of basket 8 (basis-carry).
- **High Vol** ← basket 13 expansion + the fragility detectors 4 & 9 firing + shocks 5/11/12.
- **Low Vol** ← basket 13 compression; the carry-harvest regime (8 + chop-side 14).
- **Risk-Off** ← baskets 11 (black-swan) & 12 (policy) + the downside-cascade alignment of 4 + 9; basket 10 outflows reinforce it.
- **No clean six-dim analog** — baskets 3 (meme), 7 (on-chain), 10 (institutional flow) are crypto-native information/flow states that cut across the grid rather than sitting on it.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/regimes/current` — current long-horizon market regime (10-state taxonomy)
- `GET /api/v1/quant/market` — HMM regime probabilities, 4h/24h horizons (15-min refresh)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/liquidity/regime/score` — liquidity fragility composite (0-100)

**Historical data:**
- `GET /api/v1/quant/timeline` — daily market regime labels, 2019-now
- `GET /api/v1/quant/regimes/history` — full 6-regime Parquet download (2020-yesterday)
- `GET /api/v1/quant/history` — point-in-time probability records for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/regimes/current"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes) · [long-term regimes](https://cryptodataapi.com/regimes) · [strategy baskets](https://cryptodataapi.com/trading-strategy-baskets)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can operate this playbook as its core loop — this page is the wiki-side counterpart of the API's recommended four-step agent cycle:

- **Detect** — `GET /api/v1/regimes/current` (10-state cycle label) + `GET /api/v1/quant/market` (6-state HMM probabilities, 15-min refresh); overlay the fragility detectors `GET /api/v1/volatility/regime/score` and `GET /api/v1/liquidity/regime/score` for baskets 13 and 9
- **Select** — `GET /api/v1/trading-strategy-baskets` (50 pre-mapped baskets in 6 groups) maps the detected state to deployable universes, mirroring the mapping table above
- **Size** — `GET /api/v1/quant/coins/risk?horizon=24h` returns per-coin regime, probability buckets, and vol-target multipliers across 180+ coins in one batched call
- **Backtest the gating** — point-in-time only: `GET /api/v1/quant/regimes/history` (hourly HMM probabilities since 2020, Pro Plus) and `GET /api/v1/backtesting/daily-snapshots` (full payload since 2026-03-02) supply regime labels as they stood at decision time — the requirement flagged in the backtesting note above
- **Tips** — treat near-threshold probability readings as *transitional* and cut gross rather than flipping strategies; poll the cached `GET /api/v1/daily` bundle hourly between full loop runs
- **Prompt library** — the "Market Regime Detection" prompt (Pro tier, [prompt library](https://cryptodataapi.com/prompts)) is a drop-in interpretation layer between the regime feed and this playbook's strategy switches

## Related

- [[crypto-market-regime-taxonomy]] — the 14-basket regime definitions this maps from
- [[regime-matrix]] — the six-dimension strategy-by-regime matrix
- [[regime-adaptive-strategy]] — the gating meta-strategy that switches between these plays
- [[market-regime-detection-ml]] — how the regime label is produced
- [[crypto-perp-backtesting-pitfalls]] — why gating must be tested point-in-time
- [[market-regime]] — the general concept of regime-conditional strategy validity
- [[edge-taxonomy]] — how each gated strategy's edge is classified
- [[risk-management]] — sizing and kill-switch discipline that backs regime gating

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the regime framework (#meta); strategy mappings are the wiki's own, drawn from existing strategy pages
