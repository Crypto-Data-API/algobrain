---
title: "Crypto Narratives — Impact Catalog Overview"
type: overview
created: 2026-06-04
updated: 2026-06-12
status: good
tags: [crypto, market-regime, event-driven, narrative-impact, backtesting]
aliases: ["Crypto Narrative Impact Catalog", "Narrative Backtest Catalog"]
related: ["[[crypto-market-regime-taxonomy]]", "[[event-catalyst-regime]]", "[[policy-shock-regime]]"]
---

A backtester-ready catalog of how recurring **world and market narratives** move crypto
prices. Each narrative is decomposed into *archetypes* (repeatable patterns with a
consistent mechanism), and each archetype is grounded in *historical instances* with
quantified price impact, affected sectors/coins, and source citations. The goal is to let
a backtester recognise a developing narrative, map it to its analog mechanism, and reason
about the likely direction, magnitude, lag, and duration of the move.

> **Scope:** 19 categories · 69 archetypes · 290 historical instances (build 2026-06-04).
> Confidence: 147 high / 103 medium / 40 low. Price moves measured: 121 directly from
> CoinGecko, the rest web/Perplexity-sourced with citations or flagged estimates.
> *(Categories are being deepened one at a time — `regulatory-approvals-policy` and a new
> `bitcoin-dominance-rotation` category added first; Bitcoin events distributed into
> whale-flows, ETF-flows, corporate-treasury, and hacks.)*

> **🧭 Master directory:** [[narratives-by-direction]] — every narrative grouped 🟢 bullish / 🔴 bearish / ⚪ neutral (Part A = the 69 archetype *types*; Part B = all 290 *events* by realized move: 99 up / 157 down / 34 flat). The fastest way to scan "what pumps vs what crashes."
>
> **⚙️ Operational layer (for the trading system):** [[narrative-signals]] — each archetype as a machine-readable signal card with **live detection conditions**, **move-probability priors** (P_up/P_down + magnitude), **PM strategy gates** (enable/disable/tilt/flatten per strategy class, grounded in [[regime-strategy-playbook]]), and **point-in-time backtester gates**. Source: `catalog/narrative-signals.json`. For the Hyperliquid PM (live on/off) and backtester (gates + coin-move probability).

## How to use this catalog

- **Machine-readable:** `wiki/crypto-narratives/catalog/all-narratives.json` is the merged
  dataset (plus one `<category>.json` per category). Rebuild with
  `python tools/build_narrative_catalog.py`.
- **Per-archetype fields a quant consumes:** `mechanism`, `directional_bias`,
  `typical_magnitude_pct`, `typical_lag`, `typical_duration`, `recurrence`,
  `affected_scope`, `leading_signals`, `backtest_features` (concrete computable fields),
  and `analog_mechanisms`.
- **Per-instance fields:** `date`, `date_range`, `trigger`, `price_impacts[]`
  (`asset`, `pct_change`, `window`, `direction`, `measured_by`), `affected_sectors`,
  `affected_coins`, `volume_or_flow_change`, `confidence`, `sources[]`.

## Analog-mechanism map (the generalizable forces)

The key abstraction: many surface-level narratives reduce to the **same underlying force**.
A backtester should tag any new event with one or more of these, then borrow the
distribution of historical outcomes for that force. (Counts = archetypes tagged.)

| Mechanism | Bias | What it is | Fired by (examples) | Archetypes |
|-----------|------|------------|---------------------|-----------:|
| `sentiment-shock` | both | Reflexive risk-on/off repricing on news | macro prints, headlines, hacks, policy | 56 |
| `sell-pressure` | bearish | New sellable supply / forced sellers hit the book | unlocks, estate sales, gov BTC sales | 41 |
| `reflexive-deleveraging` | bearish | Liquidations beget liquidations; collateral spirals | leverage washouts, lender contagion | 37 |
| `dry-powder-injection` | bullish | Idle buying power enters (stablecoins, ETF inflows) | USDT/USDC mints, ETF inflows, easing | 32 |
| `supply-restriction` | bullish | Float removed/locked; issuance cut | halving, staking/locking, vote-locking | 24 |
| `forced-liquidation` | bearish | Margin calls force size onto the market | perp cascades, carry unwinds | 22 |
| `supply-overhang` | bearish | *Anticipated* future supply pre-priced | telegraphed unlocks, dilution, sell-the-news | 9 |
| `contagion` | bearish | Counterparty/credit risk spreads across entities | exchange/lender failures, depegs | 4 |
| `sector-rotation` | both | Capital rotates between cohorts/chains | L1/L2 rotation, AI/meme/DeFi cohorts | 2 |
| `mean-reversion` | both | Positioning extreme snaps back | funding/OI extremes, capitulation | 2 |

**Worked example of the abstraction (your prompt's cases):** a *token unlock*, a *Tether
mint*, and the *Bitcoin halving* all touch the supply side — but with opposite signs and
timing: an unlock is `sell-pressure` / `supply-overhang` (bearish, pre-priced), a mint is
`dry-powder-injection` (bullish, lagged demand), and a halving is `supply-restriction`
(bullish, slow ~12–18mo). A *whale stablecoin deposit to an exchange* is nominally
`dry-powder-injection` but empirically often coincides with `sell-pressure` — see
[[whale-onchain-flows]] for the counter-intuitive 2026-03 case.

## Categories

| Category | Bias | Arch | Inst | Headline instance |
|----------|------|-----:|-----:|-------------------|
| [[token-unlocks-narrative]] | bearish | 3 | 16 | WLD scheduled unlock −9.8% (−21.9% DD), 2025-07-25 |
| [[stablecoin-supply]] | mixed | 4 | 14 | 2020–21 USDT doubling → BTC +311%; cap record $322B (May-2026) yet BTC −40% YTD (dry powder ≠ timing) |
| [[bitcoin-halving-narrative]] | bullish | 3 | 10 | CYCLE-BREAKER: 2025 = first-ever RED post-halving year (+31% at 1yr vs +300/+567%); ETF flows > supply shock; 2025-26 bear −52% |
| [[bitcoin-dominance-rotation]] | mixed | 2 | 5 | June 2026 = Bitcoin Season (BTC.D ~58.7%, ASI ~49), NOT alt-season |
| [[corporate-treasury]] | mixed | 3 | 20 | MSTR 843,706 BTC + first SALE since 2022 (32 BTC, "never-sell cracks" → BTC −4.5%); SpaceX 18,712 BTC; Bitmine 5.42M ETH |
| [[spot-etf-flows]] | mixed | 3 | 16 | BTC ETF → −14%; ETH/SOL ETFs ≠ floor (SOL −57% post-launch); ZEC +180% on ETF filing |
| [[regulatory-bans]] | bearish | 4 | 14 | China May-2021 crackdown → BTC −38% to −41% |
| [[regulatory-approvals-policy]] | bullish | 6 | 19 | Trump win 2024-11-05 → BTC +52–56% to first $100k; CLARITY 15-9 (2026-05-14) → BTC −5.8% (policy-fatigue) |
| [[whale-onchain-flows]] | bearish | 4 | 17 | German gov sells 49,858 BTC → −17%; 13yr-dormant 909 BTC (wallet≠sell); whales buy $60K dip, sell $74K bounce |
| [[exchange-collapses]] | bearish | 3 | 10 | FTX 2022-11-08 → BTC −22% to ~$15.5k |
| [[stablecoin-depegs]] | bearish | 3 | 11 | UST/LUNA 2022-05 → −98%/−99.99%; USR (Resolv) −80% on AWS-key unbacked mint (2026-03) |
| [[hacks-exploits]] | bearish | 3 | 17 | KelpDAO $292M & Drift $285M (Lazarus); Butter MAPO −96%; Hyperbridge 1B DOT → −4.8% (infinite-mint pattern) |
| [[memecoin-mania]] | mixed | 3 | 15 | TRUMP −79% from peak; Jan-2026 sector +$8B spike-and-fade (PEPE +77% runup → round-trip) |
| [[ai-agent-tokens]] | mixed | 4 | 15 | DeepSeek shock 2025-01-27 tops cohort; TAO +66.5% on Covenant-72B (Mar-2026), then faded |
| [[defi-narratives]] | mixed | 4 | 17 | DeFi Summer 2020; RWA $25-32B + Aave $1B RWA (first lender); Aave −$15B TVL from KelpDAO LRT exploit |
| [[l1-l2-rotation]] | mixed | 4 | 17 | SOL post-FTX revival → +324% (2023); SOL −15.9% June-2026 (debunks "rally" claim) |
| [[technical-signals]] | mixed | 4 | 18 | 2025-10-10 record ~$19B liquidation cascade |
| [[platform-launches]] | bearish | 5 | 24 | Most TGEs farm-and-dump (PUMP −70%); HYPE buyback-flywheel → ATH; SEA adopts buyback model; SPACEX-USDH oracle −45% |
| [[macro-events]] | mixed | 4 | 15 | COVID → −50%; Moody's → $112K ATH; Warsh hawkish Fed-Chair nom → BTC −14%; Feb-2026 −9% on depeg FEAR |

## Reading the bias column

`bias` is the *unconditional* historical tilt, but almost every archetype is
**regime-conditional**: unlocks get absorbed in strong-demand tapes, ETF "sell-the-news"
dips re-rate higher within weeks, and bans in jurisdictions with already-low market share
barely register. The per-page archetype sections document these conditioning variables —
they are the difference between a naive event-study and a tradeable signal.

## Provenance & limitations

- Built by a multi-agent research workflow (`tools/workflows/crypto-narratives.mjs`):
  per-category live web research (WebSearch + Perplexity `sonar`) → adversarial
  verification of headline numbers → page + JSON authoring.
- Recent events (≈ last 365 days) carry CoinGecko-measured moves (`tools/coin_impact.py`,
  `measured_by: coingecko`); older events use web/Perplexity-sourced figures with citation
  URLs and explicit `confidence`. Treat `low`-confidence and `estimate` impacts as
  directional, not precise.
- This catalog is **reference material**, deliberately separate from `wiki/narratives/`
  (the live trading bot's tradeable-thesis reader).

## Related

- [[crypto-market-regime-taxonomy]] — the 14-basket regime framework these narratives map into
- [[event-catalyst-regime]], [[policy-shock-regime]], [[on-chain-regime]] — regime baskets
- [[cryptoquant]] — on-chain flow data source for several leading signals
- [[edge-taxonomy]] — where narrative/event edge sits among the six edge sources
