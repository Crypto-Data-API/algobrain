---
title: "Algorithmic Trading"
type: concept
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [algorithmic, quantitative, market-microstructure, backtesting, machine-learning]
domain: [market-microstructure, technical-analysis]
prerequisites: ["[[market-microstructure]]", "[[backtesting]]", "[[order-types]]"]
difficulty: intermediate
aliases: ["Algo Trading", "Automated Trading", "HFT"]
related: ["[[backtesting]]", "[[risk-management]]", "[[market-microstructure]]", "[[arbitrage]]", "[[data-providers]]", "[[algorithmic-overview]]"]
---

# Algorithmic Trading

Algorithmic trading is the use of computer programs to execute trades automatically based on predefined rules, mathematical models, or machine learning signals. It accounts for the majority of volume in modern equity and [[forex]] markets and is increasingly prevalent in crypto. This page covers the field as a concept; the catalog of specific algorithmic strategies in this wiki lives at [[algorithmic-overview]].

## Brief History

- **1970s-80s — program trading:** the NYSE's DOT/SuperDOT order-routing systems enabled computerized basket trading. Portfolio insurance — a rules-based dynamic hedging program — was widely blamed for amplifying the 1987 crash ([[black-monday-1987]]).
- **2001 — decimalization:** US equities moved from fractional (1/16) to penny pricing, collapsing spreads and creating the economics for high-frequency [[market-making]].
- **2005-2007 — Regulation NMS:** the SEC's order-protection rule (adopted 2005, implemented 2007) forced routing to the best displayed quote across venues, fragmenting US equity markets and rewarding speed.
- **~2009 — HFT peak share:** high-frequency trading reached an estimated peak of roughly 60% of US equity volume around 2009; commonly cited estimates since then put algorithmic execution at well over half of US equity volume.
- **May 6, 2010 — the Flash Crash:** the Dow fell roughly 1,000 points (~9%) intraday and recovered most of it within minutes, an event tied to a large algorithmic sell program interacting with HFT liquidity withdrawal.
- **August 1, 2012 — Knight Capital:** a botched software deployment fired errant orders for ~45 minutes, losing approximately $440M and forcing the firm's sale — the canonical operational-risk case study for algo trading.
- **2018 — MiFID II:** the EU imposed formal requirements on algorithmic traders (testing, kill switches, audit trails under RTS 6), the first comprehensive regulatory regime for the practice.
- **2020s — crypto and retail:** algorithmic trading became dominant on crypto exchanges (market making, [[arbitrage]], [[mev-strategies|MEV]]) and accessible to retail via broker APIs and platforms like QuantConnect.

## Major Categories

### Execution Algorithms
Designed to fill large orders with minimal market impact. TWAP (Time-Weighted Average Price) spreads orders evenly over time. VWAP (Volume-Weighted Average Price) weights execution to match market volume patterns. Iceberg orders hide true size. [[implementation-shortfall]] algorithms balance impact cost against the risk of price drift while waiting. Execution algos do not seek alpha — they minimize the cost of trades decided elsewhere.

### High-Frequency Trading (HFT)
Exploits microsecond-level speed advantages for [[arbitrage]], market making, and latency arbitrage. HFT firms invest heavily in co-location, network infrastructure, and FPGA hardware. They provide [[liquidity]] but are controversial for their speed advantage over retail traders. Michael Lewis's *Flash Boys* (2014) brought the latency-arbitrage debate to a mainstream audience and contributed to the launch of IEX and its speed-bump design.

### Signal-Based / Systematic
Uses quantitative models to generate buy/sell signals from price data, [[indicators]], fundamental data, alternative data, or [[sentiment]] analysis. Strategies range from simple moving average crossovers to complex machine learning models. Includes [[trend-following-cta|CTA trend following]], [[factor-investing]], and [[momentum]] systems run at daily-to-monthly horizons where speed matters far less than signal quality.

### Statistical Arbitrage
Identifies pricing inefficiencies between related assets using statistical models. [[pairs-trading|Pairs trading]], [[mean-reversion]], and cross-exchange [[arbitrage]] fall into this category. See [[stat-arb]].

## Key Components

1. **Signal generation**: Identify trade opportunities via models or rules.
2. **Risk management**: [[position-sizing]], [[stop-loss]] logic, portfolio-level controls, and pre-trade risk checks (fat-finger limits, max position, max order rate).
3. **Execution**: Route orders efficiently to minimize [[slippage]] and market impact.
4. **Backtesting**: Test strategies against historical data before deploying capital. Critical to avoid [[overfitting]] — see [[overfitting-detection]] and [[walk-forward-analysis]].
5. **Monitoring and kill switches**: live systems need automated shutoffs on anomalous behavior; the Knight Capital loss is the standard cautionary example of deploying without one.

## What Goes Wrong

- **Overfitting**: the dominant failure mode — strategies tuned to historical noise that evaporate live. See [[failure-modes]].
- **Operational/deployment risk**: Knight Capital (2012, ~$440M) was a deployment error, not a model error.
- **Crowding and regime change**: many algos share signals; the August 2007 "quant quake" saw simultaneous deleveraging across stat-arb funds produce multi-sigma losses in days.
- **Liquidity illusion**: algorithmic liquidity can withdraw in milliseconds, as in the 2010 Flash Crash — depth on the book is not depth in a crisis.
- **Cost underestimation**: naive backtests that ignore fees, spread, and impact routinely turn live-negative; see [[transaction-costs]].

## Regulation

- **US**: SEC Market Access Rule 15c3-5 (2010) requires pre-trade risk controls on direct market access; Reg SCI (2014) imposes systems-integrity requirements on key market infrastructure.
- **EU**: MiFID II (2018) RTS 6 requires algo testing, annual self-assessment, kill functionality, and audit trails; market-making algos face quoting obligations.
- **Spoofing and manipulation**: layering/spoofing via algorithms is illegal (Dodd-Frank §747); the 2015 prosecution of Navinder Sarao linked spoofing to the Flash Crash.

## Why It Matters for Traders

Even discretionary traders benefit from understanding algorithmic trading, because algorithms are their counterparties. Knowing how execution algos, HFT market makers, and systematic funds behave helps explain [[order-flow]], [[liquidity]] patterns, and sudden price moves. Practical implications: avoid resting obvious stop clusters (algos hunt them), expect mean reversion after liquidity-vacuum spikes, and recognize that quoted depth understates true crisis liquidity.

## Getting the Data (CryptoDataAPI)

For the crypto side of algorithmic trading, CryptoDataAPI is this wiki's canonical data layer — price/volume for signals, derivatives for perp systems, and the archive for validation.

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000` — Binance spot OHLCV, the raw input for signal-based systems
- `GET /api/v1/market-data/ticker/24hr` — rolling 24h stats per pair
- `GET /api/v1/derivatives/summary?coin=BTC` — funding, OI, and long/short in one call for perp systems
- `GET /api/v1/daily` — the full daily market bundle (health, derivatives, sentiment, macro) in one call

**Historical data:**
- `GET /api/v1/backtesting/klines` — deep OHLCV archive (Binance spot 1h/4h/1d back to 2017-08; 1m only since 2026-03-30)
- `GET /api/v1/backtesting/funding` — funding archive (Hyperliquid hourly since 2023-05)
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time daily snapshots (since 2026-03-02) for lookahead-free validation

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run a crypto algo system end-to-end:

- **Signal** — `GET /api/v1/market-data/klines` supplies the bars that MA-crossover, breakout, and ML signal engines consume; `GET /api/v1/daily` is the one-call hourly refresh for a running system
- **Regime gate** — `GET /api/v1/quant/market` (6-state HMM, 15-min refresh) switches between trend, mean-reversion, and flat books — the systematic answer to the "crowding and regime change" failure mode above
- **Execution** — check `GET /api/v1/liquidity/depth` (depth/spread at 10-100 bps) before sizing orders; quoted depth is not crisis depth, as the Flash Crash section notes
- **Backtest** — `GET /api/v1/backtesting/klines` with point-in-time state from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) — validating against today's labels introduces the lookahead bias this page warns about
- **Tips** — batch per-coin reads via `GET /api/v1/quant/coins/risk` rather than looping symbols; naive backtests that skip fees/spread/impact turn live-negative, so overlay costs before trusting any Sharpe

## Related

- [[algorithmic-overview]] — catalog of algorithmic strategy pages in this wiki
- [[market-microstructure]] — the environment algos operate in
- [[backtesting]] / [[overfitting-detection]] — validation methodology
- [[stat-arb]], [[trend-following-cta]], [[factor-investing]], [[mev-strategies]] — major algorithmic strategy families
- [[implementation-shortfall]], dark-pool-trading — execution-side topics
- [[flash-crash-2010]], [[knight-capital]] — case studies
- [[risk-management]], [[data-providers]]

## Sources

- Well-documented public events: 2010 Flash Crash (joint SEC/CFTC report, Sep 2010), Knight Capital loss of ~$440M (SEC order, Aug 2012), Reg NMS (SEC, 2005), MiFID II RTS 6 (ESMA, 2018), Sarao spoofing prosecution (DOJ, 2015)
- Michael Lewis, *Flash Boys* (2014) — latency arbitrage and IEX
- Aldridge, *High-Frequency Trading* (2nd ed., 2013) — HFT volume-share estimates
