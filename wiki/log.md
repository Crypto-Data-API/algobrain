---
title: "Wiki Operations Log"
type: index
created: 2026-07-13
updated: 2026-07-19
status: good
tags: [meta, log]
---

Chronological, append-only record of all wiki operations. Newest entries at the top.

## 2026-07-19 — Batch B11-2 (Final): Schema Upgrade of Remaining 24 STRATEGY Pages + 4 Equity-Prose Cleanups

### Task 1 — 24 STRATEGY pages upgraded to buildable schema

Each page received: extended frontmatter (`edge_source`, `edge_mechanism`, `data_required`, `min_capital_usd`, `capacity_usd`, `crowding_risk`, `expected_sharpe`, `expected_max_drawdown`, `breakeven_cost_bps`, `kill_criteria`); any missing schema sections from the 16-section standard (`## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`); `updated: 2026-07-19`; `status: review` if previously `good`. All new content is crypto-scoped (perps/Deribit/DVOL/funding). VIX-named pages (`vix-calls`, `quantitative/vix-trading`) explicitly state no tradeable DVOL future exists in crypto and frame everything via Deribit spot options.

**Upgrade type: frontmatter only (page already had full schema sections)**
- [[options-income]] — added extended frontmatter fields only
- [[options-premium-selling]] — added extended frontmatter fields only
- [[premium-selling-systematic]] — added extended frontmatter fields only
- [[quantitative/tail-risk-hedging]] — added extended frontmatter fields only (expected_sharpe: -0.3 labeled honest negative standalone)

**Upgrade type: frontmatter + missing schema sections**
- [[combinations/stop-hunting-and-liquidity-sweeps]] — added full extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[combinations/structural-forced-selling]] — added full extended frontmatter + all schema sections + equity-prose cleanup (Task 2 concurrent)
- [[combinations/trend-plus-tail-hedge]] — added full extended frontmatter + all schema sections + equity-prose cleanup (Task 2 concurrent)
- [[conversion-reversal-arbitrage]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[delta-hedged-options]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[fundamental-analysis/news-trading]] — added extended frontmatter + all schema sections + equity-prose cleanup (Task 2 concurrent)
- [[quantitative/vix-trading]] — added full extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; explicit "no tradeable DVOL future" statement
- [[tail-hedging]] — added extended frontmatter + `## Capacity limits`, `## What kills this strategy` (page already had Edge source, Null hypothesis, Kill criteria)
- [[vix-calls]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## Kill criteria (numeric)`; explicit "no VIX call analog in crypto" statement preserved
- [[zero-dte-options]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[technical-analysis/0dte-trading]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[technical-analysis/options-selling]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[technical-analysis/turtle-trading]] — added extended frontmatter + `## Edge source`, `## Null hypothesis` (renamed from existing "## Edge and Mechanism"), `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[technical-analysis/channel-breakout]] — added full extended frontmatter + all schema sections; markets updated to [crypto,futures,forex]; `## Getting the Data`, `## Related` added
- [[technical-analysis/macd-crossover]] — added full extended frontmatter + all schema sections; markets updated to [crypto,forex]; `## Getting the Data`, `## Related` added
- [[technical-analysis/opening-range-breakout]] — added full extended frontmatter + all schema sections; markets updated to [crypto,futures]; crypto adaptation (08:00 UTC Deribit pseudo-open); equity SPY example preserved as labeled TradFi context; `## Getting the Data`, `## Related` added
- [[technical-analysis/rate-of-change]] — added full extended frontmatter + all schema sections; markets updated to [crypto,forex]; AAPL example replaced with BTC/USDT perp example (AAPL preserved as labeled TradFi context); `## Getting the Data`, `## Related` added
- [[technical-analysis/rsi-divergence]] — added extended frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; `## Getting the Data` already present; funding-rate as confirmation layer added
- [[technical-analysis/support-resistance-breakout]] — added full extended frontmatter + all schema sections; markets updated to [crypto,forex]; `## Getting the Data`, `## Related` added; liquidation cascade mechanism documented
- [[technical-analysis/volatility-breakout]] — added full extended frontmatter + all schema sections; markets updated to [crypto,futures]; ES example replaced with BTC perp example (ES preserved as labeled TradFi context); `## Getting the Data`, `## Related` added

### Task 2 — Equity-prose cleanup in 4 pages

Residual equity framing in OLD prose reworked to crypto-primary; equity/TradFi references retained as brief labeled historical context only:

- [[combinations/structural-forced-selling]] — markets=[stocks,bonds] → [crypto,futures]; edge source and "Why It Persists" sections reworked to crypto-primary (perp auto-liquidation, FTX contagion, negative funding cascades); equity examples converted to "TradFi Context (Historical Reference Only)"
- [[combinations/trend-plus-tail-hedge]] — Component Strategies table reworked to crypto perps + Deribit OTM puts + straddles; Implementation reworked to crypto; explicit "VIX calls: no crypto equivalent; use Deribit straddles" note added; equity SPX/VIX example preserved as labeled historical context
- [[fundamental-analysis/news-trading]] — markets updated to [crypto,forex]; rules reworked to BTC perps + funding repricing; ES futures example (SPX short at 5175) replaced with BTC perp example; equity/NFP references labeled as TradFi context
- [[combinations/expiration-and-rebalancing-flows]] — markets=[stocks,futures,crypto] → [crypto,futures]; "The Edge" section reworked to Deribit OpEx pinning as primary + equity rebalancing as labeled TradFi context; "Why It Persists" reworked to crypto market-maker hedging as primary; flow calendar table reworked to crypto events (Deribit monthly/quarterly OpEx, CME BTC roll, on-chain vault rolls) with equity calendar as labeled TradFi context; end-of-month SPX rebalance strategy replaced with Deribit OpEx pinning + CME basis roll strategies; ES futures example replaced with Deribit quarterly OpEx example; "Real-World Examples" reworked to crypto examples (Deribit Dec 2023 OpEx, March 2022 OpEx) with equity examples (TSLA S&P addition, Russell reconstitution) as labeled TradFi context; explicit note added that VIX futures roll trade does not port to crypto (no DVOL future)

### Wire-up

- `wiki/log.md` — this entry prepended
- `.claude/b11-classification.md` — all 24 B11-2 pages marked `yes (B11-2)` in the B11 column; tally updated to reflect all 34 STRATEGY pages fully upgraded

### Files touched (26 total)

24 strategy pages upgraded + `wiki/log.md` + `.claude/b11-classification.md`

### B11 completion status

All 34 STRATEGY-class pages in the B11 triage list now have complete extended frontmatter and all required schema sections. No STRATEGY pages with missing `edge_source:` remain from the original 99-page triage.

---

## 2026-07-19 — Batch B11: Triage + First Schema Upgrades (99 pages missing edge_source)

### Triage counts (all 99 `type: strategy` pages lacking `edge_source:`)

| Class | Count | Action |
|-------|-------|--------|
| GUIDE | 25 | `type: strategy` → `type: reference` |
| STRUCTURE | 40 | Left as-is (Wave 3 deliberate design, content untouched) |
| STRATEGY | 34 | 10 upgraded; 24 remain for future batches |

Full per-page classification with rationale: `.claude/b11-classification.md`

### Task 2 — GUIDE pages retyped (25 pages: `type: strategy` → `type: reference`)

`algorithmic/black-litterman`, `algorithmic/cppi`, `algorithmic/portable-alpha`, `algorithmic/risk-budgeting`, `arbitrage/arbitrage-backtesting-guide`, `arbitrage/arbitrage-correlation-matrix`, `arbitrage/arbitrage-live-performance`, `arbitrage/arbitrage-monitoring-setup`, `arbitrage/arbitrage-parameter-cheatsheet`, `arbitrage/arbitrage-seasonality`, `arbitrage/arbitrage-worked-examples`, `arbitrage/etf-arbitrage`, `arbitrage/multi-venue-capital-management`, `arbitrage/regulatory-arbitrage`, `combinations/core-satellite-portfolio`, `combinations/multi-strategy-portfolio`, `combinations/risk-on-risk-off-framework`, `combinations/volatility-targeting`, `fundamental-analysis/crack-spread`, `fundamental-analysis/crush-spread`, `fundamental-analysis/seasonal-spread-trading`, `fundamental-analysis/spark-spread`, `position-trading/carry-trade`, `position-trading/dollar-cost-averaging`, `technical-analysis/options-strategies`

Only the `type:` field was changed; all content preserved.

### Task 3 — 10 STRATEGY pages upgraded to buildable schema

Each page received: extended frontmatter (`edge_source`, `edge_mechanism`, `data_required`, `min_capital_usd`, `capacity_usd`, `crowding_risk`, `expected_sharpe`, `expected_max_drawdown`, `breakeven_cost_bps`, `kill_criteria`); missing schema sections (`## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`); `updated: 2026-07-19`; `status: review` where previously `good`.

- [[5-percent-otm-put-overlay]] — added full frontmatter edge fields; page already had all 16 schema sections
- [[trend-following-cta]] — added frontmatter + `## Edge source`, `## Why this edge exists`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; added `crypto` to markets; new sections crypto-scoped (perp liquidation cascade as structural counterparty); existing CTA/commodities prose preserved
- [[nft-arbitrage]] — added frontmatter + `## Edge source`, `## Why this edge exists`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`
- [[alternative-data-alpha]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`, `## Getting the Data (CryptoDataAPI)`; crypto on-chain/social framing added to new sections only; existing equity examples preserved
- [[asymmetric-barbell]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; crypto barbell adaptation (Deribit puts + stablecoin yield) added to new sections only
- [[cross-asset-signals]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`, `## Getting the Data (CryptoDataAPI)`; DXY-BTC relationship and funding-rate as cross-asset signal documented in new sections
- [[expiration-and-rebalancing-flows]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`, `## Getting the Data (CryptoDataAPI)`; Deribit OpEx pinning and quarterly BTC futures roll added in new sections; existing equity flow calendar preserved
- [[gamma-exposure-trading]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`, `## Getting the Data (CryptoDataAPI)`; crypto GEX via Deribit OI and greeks.live documented in new sections
- [[multi-timeframe-confluence]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; on-chain/funding as third confluence axis noted in new sections
- [[regime-adaptive-strategy]] — added frontmatter + `## Edge source`, `## Null hypothesis`, `## Capacity limits`, `## What kills this strategy`, `## Kill criteria`; CryptoDataAPI regime taxonomy mapped (10-state) in new sections; VIX → DVOL translation noted

**Residual equity framing note:** `combinations/structural-forced-selling`, `combinations/trend-plus-tail-hedge`, and `fundamental-analysis/news-trading` are STRATEGY-class but remain equity/futures-framed in their existing content. New sections will need crypto reframing when they are upgraded in a future batch.

### Remaining 24 STRATEGY pages still needing upgrade (next batches)

`combinations/stop-hunting-and-liquidity-sweeps`, `combinations/structural-forced-selling`, `combinations/trend-plus-tail-hedge`, `conversion-reversal-arbitrage`, `delta-hedged-options`, `fundamental-analysis/news-trading`, `options-income`, `options-premium-selling`, `premium-selling-systematic`, `quantitative/tail-risk-hedging`, `quantitative/vix-trading`, `tail-hedging`, `technical-analysis/0dte-trading`, `technical-analysis/channel-breakout`, `technical-analysis/macd-crossover`, `technical-analysis/opening-range-breakout`, `technical-analysis/options-selling`, `technical-analysis/rate-of-change`, `technical-analysis/rsi-divergence`, `technical-analysis/support-resistance-breakout`, `technical-analysis/turtle-trading`, `technical-analysis/volatility-breakout`, `vix-calls`, `zero-dte-options`

### Files touched (37 total)

25 GUIDE pages retyped + 10 STRATEGY pages upgraded + `wiki/log.md` + `.claude/b11-classification.md`

## 2026-07-19 — Batch B10+B12: Example Trades + Concept Stub Expansions

### Task 1 — Added `## Example trade` sections to 10 strategy pages

Each section uses concrete round-trip numbers (entry trigger values, position size, fees/funding/slippage, exit, net P&L), labelled "illustrative, round numbers — not a backtest," matching each page's own rules/thresholds.

- [[perp-dex-aggregation]] — $500k BTC-perp long split across Hyperliquid/Orderly/dYdX; waterfall-split routing, funding shift, 24h exit; shows $11k slippage saving vs single-venue fill
- [[prediction-market-strategies]] — Complement arbitrage on Polymarket; Yes + No at $0.98 total; $490 deployed, $500 guaranteed, ~33% annualised net of gas; resolves capital-lockup cost
- [[tao-validator-delegation]] — 100 TAO across RoundTable21/Datura/YumaGroup; flat TAO price; ~22% APY blended; 121.3 TAO after 1 year; alpha redemption slippage included
- [[mev-execution-guide]] *(guide framing → "## Worked example")* — Back-run MEV on Ethereum: $20k position, $360 gross, 90% builder bid, $34 estimated net / $14 actual net after competition; illustrates bid-compression economics end-to-end
- [[swap-spread-arbitrage]] — Modern negative-spread trade: pay-fixed 10Y IRS at 2.82%, long $100M Treasury at 3.00%, repo-financed; +$274/day carry; 12-month exit with spread normalisation to −5 bps; +$202,900 net on ~$5M equity deployed
- [[triangular-arbitrage]] — USDT→BTC→ETH→USDT on Binance, $68k capital, $211 gross, $81 fees, $130 net in ~200ms; partial-fill risk scenario included
- [[vampire-attack-arbitrage]] — Hypothetical ForkSwap launch; $100k LP entry; 7-day boost harvest schedule (day-by-day price/revenue table); +$11,655 net after gas, slippage, IL; 607% annualised during window
- [[contrarian-extremes]] — BTC Jan 2023 post-FTX; composite score table; 4-tranche entry $16,500–$18,500; exit at composite 45 / BTC $27,800 on Mar 15; +$18,140 net including funding carry; ~7:1 realized R:R
- [[dca-technical-hybrid]] — 10-week BTC DCA at $500/week; week-by-week log with RSI/MA signals; hybrid avg cost $59,150 vs vanilla DCA $61,260; −3.4% cost-basis improvement on $5,000 deployed
- [[multi-strategy-crypto-portfolio]] — One weekly rebalance cycle on $500k book; full sleeve drift table, rebalance trades across Hyperliquid/Binance/Bybit/DEX, stressed heat check (0.525× vs 1.25× cap), rebalance friction $246 (0.049% of NAV)

**Judgment call — mev-execution-guide:** Confirmed as a companion guide (not a single-strategy page) based on page content ("This page covers *how to actually execute*"). Added `## Worked example` (guide framing) rather than `## Example trade` (strategy framing), consistent with the page's own structure.

### Task 2 — Expanded 12 stub concept pages to draft status

Each page expanded to 300-500 words: clear definition, how it works, concrete examples with real names/dates, **Trading relevance** subsection linking 2-4 relevant strategy pages, Related section. All set `status: draft`, `updated: 2026-07-19`. Existing frontmatter fields preserved; approved tags only.

- [[layer-1]] — Base blockchain definition; PoW vs PoS; Bitcoin/Ethereum/Solana/Avalanche examples; links [[cross-chain-arbitrage]], [[mev-strategies]], [[on-chain-analysis]], [[jito-solana-mev-arbitrage]]
- [[depin]] — DePIN mechanics; Helium/Filecoin/Render/Hivemapper examples; emission-schedule arb; links [[vampire-attack-arbitrage]], [[on-chain-analysis]], [[multi-strategy-crypto-portfolio]]
- [[crypto-fear-and-greed-index]] — 6-component composite; score interpretation; March 2020 (score 8), Jan 2023 (score 6), Nov 2021 (score 84) examples; links [[contrarian-extremes]], [[funding-rate-arbitrage]], [[multi-strategy-crypto-portfolio]], [[prediction-market-strategies]]
- [[gamefi]] — Three-layer economy; AXS/SLP mechanics and collapse; StepN, Gods Unchained; links [[vampire-attack-arbitrage]], [[governance-token]], [[multi-strategy-crypto-portfolio]]
- [[liquidations]] — Margin lifecycle; cascade mechanics; Black Thursday, May 2021, FTX 2022; links [[liquidation-cascade-arbitrage]], [[contrarian-extremes]], [[funding-rate-arbitrage]], [[mev-execution-guide]]
- [[governance-token]] — Voting mechanics; UNI, COMP, AAVE, CRV, MKR examples; links [[curve-gauge-wars-arbitrage]], [[vampire-attack-arbitrage]], [[governance-restitution-arbitrage]], [[liquidity-mining]]
- [[privacy-coins]] — XMR ring signatures/RingCT; ZEC zk-SNARKs; Dash CoinJoin; ransomware shift to Monero; exchange delistings; links [[on-chain-analysis]], [[contrarian-extremes]], [[multi-strategy-crypto-portfolio]]
- [[mev]] — MEV supply chain; sandwich/backrun/liquidation/JIT types; Flashbots, MakerDAO $8.3M Black Thursday, Jito on Solana; links [[mev-execution-guide]], [[mev-strategies]], [[liquidation-cascade-arbitrage]], [[flash-loan-arbitrage]]
- [[play-to-earn]] — Four-component P2E economy; sustainability condition; Axie/StepN/Gods Unchained/Pixels; scholarship model; links [[vampire-attack-arbitrage]], [[governance-token]], [[multi-strategy-crypto-portfolio]]
- [[tokenized-treasuries]] — BUIDL/OUSG/BENJI/USDM mechanics; yield accrual types; $1.5B BUIDL; links [[funding-rate-arbitrage]], [[multi-strategy-crypto-portfolio]], [[basis-trade]], [[defi-yield-farming]]
- [[zero-knowledge-proofs]] — ZK-SNARK vs ZK-STARK; ZK-rollups; Zcash/StarkEx/zkSync/Polygon zkEVM; ZKML; links [[cross-l2-arbitrage]], [[privacy-coins]], [[zkml-predictive-mev]], [[airdrop-farming]]
- [[ai-agents]] — Infrastructure vs narrative tokens; ElizaOS/AIXBT/Fetch.ai/ai16z examples; links [[ai-agent-strategies]], [[prediction-market-strategies]], [[multi-strategy-crypto-portfolio]], [[on-chain-flow-trading]]

### Files touched
22 files modified (10 strategy pages + 12 concept pages + this log).

## 2026-07-19 — Batch B8b: Program Completion — 4 New Combination Strategy Pages + Final Matrix Convergence

- Pages created (4 pages covering 5 cells):
  - [[vol-scaled-carry-sizing]] — MULTI-CELL (funding carry × vol targeting AND basis × vol targeting): unified framework that sizes carry books to a constant daily-risk budget using the carry P&L stream's realized volatility (not spot price vol) as the sizing denominator; cold-start proxy: carry vol ≈ 15% of spot vol for funding carry, ≈ 8% for basis/C&C; recalibrate after 10+ days of actual carry P&L history; rebalance when target notional differs ≥ 15% from current; bounds: 0.5×–4× portfolio capital for funding carry, 0.5×–3× for basis; key insight: carry books at maximum notional when vol is highest (= highest risk), vol-scaling forces the book smaller at peak-carry / peak-risk regimes; composable with carry-with-tail-hedge (tail hedge on vol-scaled base), trend-aware-carry (trend throttle on top of vol-scaled notional), and event-calendar-risk-gating (event pause overrides vol-scaling); explicitly differentiated from carry-with-tail-hedge (fixed book size + hedge; this adjusts book size), trend-aware-carry (directional momentum trigger; this is carry P&L vol), vol-targeted-trend-following (directional P&L stream; this is delta-neutral carry P&L stream), and funding-vs-basis-rotation (instrument selection; this is within-structure sizing)
  - [[oi-gated-pairs]] — stat-arb/pairs × OI filter: pre-entry gate refuses spread entries when short leg shows squeeze preconditions (7d OI change ≥ +15%, 24h OI change ≥ +8%, funding ≤ −0.015%/8h AND L/S ≤ 0.80, or funding ≤ −0.025%/8h unconditionally); mid-trade OI monitor polls every 4h: 50% reduction if 4h OI spike ≥ +4%, full exit if funding crosses −0.010%/8h while OI building or L/S ≤ 0.75 or 7d OI change since entry ≥ +20%; near-threshold size scalar: 75% notional when 7d OI change in [+5%, +8%); re-entry: 48h cooldown + 7d OI change < 5% + funding > 0.00%/8h; the short-leg squeeze (OI spike + crowded negative funding on the shorted leg = forced short-covering cascade) is the canonical pairs killer — the OI gate refuses entries into that precondition and fires an early exit before the 3.5σ stop; composable with correlation-regime-pairs (eligibility pre-filter), vol-balanced-pairs (leg sizing with OI-risk scalar on top), and pairs-with-funding-differential (carry alignment); stat-arb × tail-hedge overlay (calls on shorted leg) documented as refinement footnote here (footnote ⁶³) — not a separate page (Deribit lists only BTC/ETH; OI gate is universally available and structurally superior)
  - [[atr-scaled-grid]] — grid/market-making × vol targeting: spacing = 0.25 × ATR(14, 4h); bounds = reference price ± 2.5 × ATR; per-level notional scales inversely to vol when ATR > 1.5× baseline (notional × baseline_ATR/current_ATR); recalibrates every 4h when ATR changes ≥ 15% or every 48h on schedule; regime kill: ADX(14) > 25 OR BB bandwidth > 80th pct → cancel all orders, do not recalibrate; OI-aware-grid pause (12h OI change ≥ +5%) takes priority over ATR recalibration; additive over regime-gated-grid (binary on/off; fixed spacing when on), oi-aware-grid (OI-build pause; fixed spacing when running), and funding-skewed-grid (inventory bias; this adjusts overall grid scale) — all four are composable; specifically solves the fee-burning-churn problem (too-tight spacing in high-vol → taker-only sweeps → net loss per cycle) and the missed-fill problem (too-wide spacing in low-vol → near-zero fill rate); not just a parameter choice — the geometry adaptation is the combination strategy
  - [[vol-gated-mean-reversion]] — mean-reversion × vol targeting: resolves the fundamental vol-targeting tension for reversion (edge is biggest at moments of highest vol, but naive scaling de-sizes exactly those moments); conditional framework distinguishes HIGH-VOL-GOOD (reversion-favourable flush: funding ≤ −0.015%/8h OR 7d avg ≤ −0.005%/8h AND OI −8%/24h or −12%/48h AND L/S ≤ 0.85 → size at 1.25×) from HIGH-VOL-BAD (continuation risk: funding ≥ +0.010%/8h AND OI +10%/24h → size at 0.30×) from NORMAL-VOL (1.00×) from EXTREME-VOL (RV ≥ 100% → 0.10×); mid-trade reclassification trigger: if HIGH-VOL-GOOD reclassifies to HIGH-VOL-BAD mid-position, exit immediately; signal-agnostic wrapper: applies on top of funding-flush-reversal, oi-flush-reversion, session-aware-mean-reversion, or any reversion signal; explicitly differentiated from vol-targeted-trend-following (uniform vol-scaling on a directional book; this is conditional and counter-trend), session-aware-mean-reversion (session timing; this is vol-regime conditioning), funding-flush-reversal and oi-flush-reversion (define WHEN to enter; this defines HOW MUCH to size those entries), and put-protected-dip-buying (downside via purchased option; this via position sizing)
- Pages updated (3):
  - [[combination-matrix]] — 5 new cells linked (funding carry × vol targeting and basis × vol targeting via vol-scaled-carry-sizing with footnote ⁵⁷; mean-reversion × vol targeting via vol-gated-mean-reversion with footnote ⁵⁸; grid × vol targeting via atr-scaled-grid with footnote ⁶¹; stat-arb × OI filter via oi-gated-pairs with footnote ⁶²); 4 planned cells reclassified non-viable (mean-reversion × cross-venue ⁵⁹; narrative × tail-hedge ⁶⁰; stat-arb × tail-hedge ⁶³; on-chain × tail-hedge ⁶⁴); sentinel × tail-hedge reclassified non-viable ⁶⁵; new footnotes ⁵⁷–⁶⁵ added; counts updated (linked: 61→66, planned: 9→0, non-viable: 50→54); Batch B8b Program Completion section prepended; program-complete note added to counts table
  - [[combinations-overview]] — completion note updated: 66 pages, 0 planned, 54 non-viable; program complete sentence prepended to Primitive × Overlay Coverage section
  - [[log]] (this file) — B8b entry prepended
- Reclassifications (4 cells, honest):
  - Mean-reversion × cross-venue: covered by cross-exchange-arbitrage (routine venue premium/discount reversion) and cross-venue-cascade-dislocation (cascade-driven venue dislocations); separate page would be thin variant of cross-exchange-arb
  - Narrative × tail-hedge overlay: options on specific narrative/memecoin tokens are unavailable on Deribit; proxy BTC/ETH hedges are beta exposure not token-specific tail; risk management via narrative-position-vol-targeting and narrative-crowding-exit
  - Stat-arb × tail-hedge overlay: documented as refinement in oi-gated-pairs (footnote ⁶³); options on shorted leg unavailable for most pairs; OI gate is superior and universally available
  - On-chain × tail-hedge overlay: leverage-stress-tail-hedge already uses OI/market-cap (the canonical on-chain stress metric); overlap is too complete; separate page would be thin variant
- Program completion: 0 planned cells remain. All 120 matrix cells either linked (66) or non-viable (54). Every viable primitive × overlay combination has a page; every non-viable cell has a reasoned footnote (¹–⁶⁵).
- All 4 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure + Getting the Data (CryptoDataAPI); verified CryptoDataAPI endpoints only (derivatives/funding-rates, derivatives/open-interest, derivatives/binance/long-short-ratio, market-data/klines, regimes/current, derivatives/binance/summary); approved tags only; honest about Deribit limitation where applicable (oi-gated-pairs footnote on options); no invented endpoints.


## 2026-07-19 — Batch B8: 5 New Combination Strategy Pages + Part 2 Matrix Convergence

- Pages created (5):
  - [[vol-balanced-pairs]] — stat-arb/pairs × vol targeting: per-leg volatility scaling so both legs of a cointegrated spread contribute equal daily risk; notional_low-vol = total × vol_high / (vol_high + vol_low) using 20-day realized vol; eligibility: 60d rolling correlation ≥ 0.70, cointegration p ≤ 0.05, OU half-life 3–25 days; entry at spread z-score ≥ 2.0 standard deviations; exits: convergence to ≤ 0.5σ, stop at ≥ 3.5σ, regime break (correlation < 0.55 or cointegration p > 0.10), 21-day time exit; weekly vol rebalance if leg vol changes ≥ 15%; optional funding-differential alignment gate composable from pairs-with-funding-differential; explicitly differentiated from correlation-regime-pairs (regime gate, not leg sizing), pairs-with-funding-differential (carry alignment, not vol balance), and vol-targeted-trend-following (portfolio-level sizing on a directional position, not intra-spread leg balance)
  - [[complacency-vol-buying]] — vol buying × sentiment-extreme filter: buy cheap vol/tails when greed extreme + IV cheap + leverage building all pass simultaneously; Gate 1: Fear & Greed ≥ 75 for ≥ 3 days; Gate 2: DVOL ≤ 35th pct 52w AND ≤ 90% of 30d avg; Gate 3: 7d avg 8h funding ≥ +0.030%/8h OR OI ≥ 70th pct 30d; instrument: OTM put 10–15% OTM DTE 28–45 [if funding ≥ 0.050%/8h] or ATM straddle DTE 21–35 [if funding 0.030–0.050%/8h]; budget 1.0–2.0% of portfolio; exits: 1.5× profit target, DVOL +20 vol-pt spike, F&G normalises to ≤ 50 without ≥ 5% price decline, DTE − 7 time exit; symmetric complement of post-panic-vol-selling (sells vol after fear spike — this buys vol at greed top); explicitly differentiated from leverage-stress-tail-hedge (OI/funding-stress-gated, not sentiment-gated; fires when structural stress metrics exceed objective thresholds), event-vol-buying (calendar-driven direction-agnostic straddles, not sentiment-driven crash insurance), and long-options-trend-expression (bullish call in confirmed trend, not crash insurance at greed extreme)
  - [[narrative-crowding-exit]] — narrative/event × funding filter: exit discipline for any narrative long using funding + OI crowding as the distribution signal; Gate 1: 8h funding ≥ +0.050%/8h AND 7d avg ≥ +0.030%/8h; Gate 2: OI ≥ 75th pct of 30d OR 7d OI change ≥ +20%; optional Gate 3 triple-confirmation: L/S ≥ 1.60; actions: Gate 1+2 (full exit), Gate 1 only (65% trim + 6% trailing stop on residual), Gate 1+2+3 (triple-confirmation immediate full exit); re-entry requires funding ≤ +0.020%/8h AND OI dropped ≥ 15% from peak AND narrative still active; entry-strategy-agnostic (works with any narrative entry source); explicitly differentiated from narrative-with-trend-confirmation (entry gate — this is the exit gate, they are sequential and complementary), crowded-long-funding-fade (enters a directional short; this exits a long), and contrarian-extremes (whole-market sentiment fade; this is token-specific narrative crowding)
  - [[unlock-cascade-watch]] — liquidation plays × unlock/event calendar: monitor OI/funding/liquidation structure around cliff unlocks ≥ 3% of circulating supply; risk classification: HIGH [OI ≥ 75th pct AND 7d funding ≥ +0.030%/8h], MODERATE [OI 50th–75th or funding +0.015–0.030%/8h], LOW [no action]; de-risk existing longs to 25% [HIGH] or 50% [MODERATE] of normal size by T − 7; cascade-fade order staging (GTC limit buys) at −8% [30%], −14% [40%], −20% [30%] of T − 1 close when OI ≥ 70th pct AND funding ≥ +0.025%/8h AND price not already −8% pre-unlock; cascade confirmed: 1h liq volume ≥ 2× 7d avg; post-fill target 8–15% recovery, stop −10% below lowest fill; cancel unfilled orders 10 days post-unlock; explicitly differentiated from unlock-short-with-crowding-gate (directional short into unlock — this is de-risk + cascade-fade), unlock-aware-momentum (momentum book pause without cascade-fade or explicit liquidation-structure monitoring), unlock-pair-hedge (beta-neutral pair structure), and liquidation-cascade-fade (general cascade fade without event-calendar anchor)
  - [[event-calendar-risk-gating]] — MULTI-CELL (grid × unlock/event, funding carry × unlock/event, vol selling × unlock/event, also basis × unlock/event): systematic pause/de-size framework for passive/mechanical strategies around scheduled binary events; event taxonomy: Tier 1 [full halt ±3 days] = halvings, ETF/regulatory decisions, major hard forks, unlocks ≥ 10% supply; Tier 2 [50–75% size reduction ±2 days] = 4–9% unlocks, FOMC when macro correlation active, major EIPs; per-strategy: grid [60% reduction T2; halt = cancel all orders + flatten inventory; resume: DVOL −15 pts from event peak AND price in grid range], carry [50% reduction T2; halt = close short-perp leg; resume: funding within 30% of pre-event level], short-vol [75% reduction T2; halt = CLOSE all short options positions; resume: DVOL −20 pts from event peak]; explicitly differentiated from event-vol-buying (TRADES the event by buying vol; this AVOIDS the event by pausing passive books), regime-gated-grid (lagging ADX/Bollinger-based regime detection; this is forward-looking calendar-based), and trend-aware-carry (trend-based carry scaling; this is event-date-based halt regardless of trend state)
- Pages updated (2):
  - [[combination-matrix]] — 8 new cells linked (7 from B8 pages + basis × unlock/event covered by event-calendar-risk-gating); 29 planned cells reclassified as non-viable (Part 2 honest convergence, footnotes ²⁴–⁵⁶); new footnotes ²³–⁵⁶ added; counts updated (existing: 53→61, planned: 38→9, non-viable: 9→50); Batch B8 section prepended
  - [[log]] (this file) — Batch B8 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates confirmed additive. No backups deployed.
- Backup evaluation: `vol-scaled-carry-sizing` (funding carry × vol targeting) and `oi-gated-pairs` (stat-arb × OI filter) remain `planned` — not yet written. `vol-balanced-pairs` (B7 backup) promoted to B8 primary ✓.
- Part 2 matrix convergence: 29 `planned` cells reclassified as `—` after honest per-cell review. Reclassified categories: basis row 4 cells (OI filter, trend gate, sentiment, session); liquidation plays 3 cells (trend gate, vol targeting, sentiment); narrative 2 cells (cross-venue, session); vol selling 2 cells (cross-venue, session); vol buying 4 cells (funding filter, vol targeting, cross-venue, session); grid 2 cells (cross-venue, sentiment); stat-arb 3 cells (trend gate, sentiment, session); on-chain 3 cells (vol targeting, cross-venue, session); sentiment 5 cells (OI filter, vol targeting, cross-venue, unlock/event, session). 9 genuine `planned` gaps remain.
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete illustrative round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related); verified CryptoDataAPI endpoints only (derivatives/funding-rates, derivatives/open-interest, derivatives/binance/long-short-ratio, market-data/klines, market-intelligence/dvol-history, market-intelligence/liquidations, sentiment/fear-greed, regimes/current, on-chain/whale-score, on-chain/exchange-flows); honest about Deribit options API requirement (complacency-vol-buying, event-calendar-risk-gating notes); approved tags only; event-calendar-risk-gating honest that token unlock calendar data is NOT in CryptoDataAPI.


## 2026-07-19 — Batch B7: 5 New Combination Strategy Pages

- Pages created (5):
  - [[funding-window-timing]] — funding carry × session/time filter: peri-settlement timing overlay; enters 40–50 min before 8h CEX funding settlements (00:00/08:00/16:00 UTC) or 10–15 min before Hyperliquid hourly settlements when |funding| ≥ 0.015%/8h, OI ≥ 60th percentile of trailing 30d, and no cascade in progress (1h liq volume < 2× 7d avg); captures pre-settlement repositioning drift from large participants positioning on the receiving side of the payment; exits 5–15 min post-settlement; stop at 0.8% adverse; HL hourly variant (0.5% of portfolio, 10–15 min window) is a smaller, more frequent, less-crowded complement; explicitly differentiated from hl-vs-cex-funding-divergence (rate spread not settlement timing), funding-skewed-grid (continuous centre adjustment), funding-rate-harvest (multi-period carry not peri-settlement scalp), and session-overlap-momentum (geographic session, not funding timestamp)
  - [[grid-with-tail-hedge]] — grid/market-making × tail-hedge overlay: OTM put budgeted from grid income; budget = min(20% of trailing 14d net grid P&L, 0.8% of grid notional); buy 10–15% OTM put, DTE 21–35, only when DVOL ≤ 70th pct 52w; grid halts on ADX > 25 or 12h OI change > +3% (mirrors oi-aware-grid runtime check); put payoff provides partial offset in gap-through-the-ladder event; stop at 22% combined drawdown; income-financing pattern adapted from carry-with-tail-hedge; explicitly differentiated from regime-gated-grid, oi-aware-grid, funding-skewed-grid (gate WHEN/HOW the grid runs — this caps the loss WHEN those gates fail or fire late)
  - [[sentiment-positioning-divergence]] — sentiment × funding filter: "talk vs money"; two setups: (1) washout long (all three gates): Fear & Greed ≤ 20 for ≥ 2 days AND funding ≤ −0.005%/8h AND L/S ≤ 0.90 AND at least one higher low on daily — longs have been flushed, shorts paying carry, stated panic coincides with actual washout; 3% of portfolio, 1.5× leverage, stop = new 10d low, exit when F&G ≥ 45 AND funding ≥ +0.01%/8h; (2) incomplete-cap avoidance/short (Fear & Greed ≤ 20 AND funding ≥ +0.010%/8h AND L/S ≥ 1.10): stated panic but longs still paying — do NOT enter long; explicitly differentiated from contrarian-extremes (sentiment alone), crowded-short-funding-fade (positioning alone), funding-flush-reversal (single-signal funding extreme), and smart-money-vs-crowd-divergence (on-chain vs positioning, not stated sentiment vs positioning)
  - [[long-options-trend-expression]] — vol buying/tail hedge × trend gate: express confirmed trends via long calls or call spreads on Deribit instead of futures when IV is cheap; trend gate (uptrend): daily close ≥ 12% above EMA50 + 4h RSI ≥ 58 in ≥ 3/5 bars + 7d avg funding ≥ 0.015%/8h; IV-cheap gate: DVOL ≤ 90% of 30d avg OR 20d RV ≥ DVOL + 5 vol pts OR DVOL ≤ 40th pct 52w; instrument: 10–15% OTM call or call spread, DTE 35–55, DTE-time-exit at DTE-7; budget 2% of portfolio; eliminates stop-wicking failure mode (option cannot be stopped out by spike vs trend); profit exit at 2× premium; explicitly differentiated from trend-following-cta (futures + stop), vol-targeted-trend-following (size scaling not instrument switch), event-vol-buying (calendar-driven straddle), and trend-aligned-premium-selling (sells options when IV elevated — structural complement: sell when rich, buy when cheap)
  - [[cross-venue-cascade-dislocation]] — liquidation plays × cross-venue: HL-Binance BTC perp price spread ≥ 0.5% during cascade (1h liq volume ≥ 3× 7d avg); enter long HL (dislocated) + short Binance (reference), equal notional 2.5% per leg; exit on spread ≤ 0.1% (reconvergence) or 15-min time limit; stop if spread widens to ≥ 1.5%; emergency close if one leg fills but other doesn't within 30s; edge: HL HLP vault architecture creates mechanical price dislocation vs Binance mark-price system during concentrated liquidation; explicitly differentiated from liquidation-cascade-arbitrage (DeFi MEV on-chain bonus — entirely different mechanism), hl-vs-cex-funding-divergence (steady-state funding spread not cascade price gap), and cross-exchange-arbitrage (continuous normal-market arb not event-triggered)
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked: funding carry × session/time ([[funding-window-timing]] with footnote ¹⁷), liquidation plays × cross-venue ([[cross-venue-cascade-dislocation]] with footnote ¹⁸), vol buying × trend gate ([[long-options-trend-expression]] with footnote ¹⁹), grid × tail-hedge ([[grid-with-tail-hedge]] with footnote ²⁰), sentiment × funding filter ([[sentiment-positioning-divergence]] with footnote ²¹); 1 backup cell resolved: mean-reversion × trend gate → [[pullback-trading]] ²² (higher-timeframe-reversion-gate backup confirmed already covered); counts updated (existing: 47→53, planned: 44→38); footnotes ¹⁷–²² added; Batch B7 section prepended
  - [[log]] (this file) — Batch B7 entry prepended
- Candidates skipped (0 of 5 primaries): all five primaries confirmed additive. No backups deployed.
- Backup evaluation: `higher-timeframe-reversion-gate` (mean-reversion × trend gate backup) confirmed covered by [[pullback-trading]] and [[trend-pullback-rally-fade]] — both document HTF-trend-gated mean-reversion entries. Matrix cell updated to reference [[pullback-trading]]. `vol-balanced-pairs` (stat-arb × vol targeting) remains planned.
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete illustrative round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related); verified CryptoDataAPI endpoints only (funding-rates, hyperliquid/funding-rates, open-interest, liquidations, long-short-ratio, fear-greed, dvol-history, klines, binance/summary, mark-price, regimes/current); honest about Deribit options API requirement (grid-with-tail-hedge, long-options-trend-expression); approved tags only.


## 2026-07-19 — Batch B6: 5 New Combination Strategy Pages

- Pages created (5):
  - [[put-protected-dip-buying]] — mean-reversion × tail-hedge overlay: post-capitulation dip-buy (spot or perp long) entered simultaneously with a 15–20% OTM protective put on Deribit; the put converts the infinite-downside stop into a contractual floor that cannot gap through; entry trigger is any of three capitulation methods (funding-flush [funding < −0.02%/8h for 24h], OI-flush [OI −15% from 5d peak], or on-chain+sentiment [whale spike + Fear & Greed ≤ 20]); put capped at 2.5% of notional; max loss = floor width + put premium; explicitly differentiated from leverage-stress-tail-hedge (pre-crash put accumulation without simultaneous long) and cascade-monetization-rotation (lifecycle rotation structure)
  - [[oi-aware-grid]] — grid/market-making × OI filter: grid paused when 12h OI change ≥ +5% OR 24h change ≥ +8% (rapid OI accumulation signals directional leverage entering = breakout fuel); grid resumes after OI stabilises below +3%/12h for 6 consecutive hours (minimum 12h pause); leading-indicator gate that fires 4–24 hours before the breakout vs regime-gated-grid's lagging ADX/ATR indicators; also gated on flat funding [−0.03%, +0.05%/8h] and ADX ≤ 25 for normal run conditions
  - [[narrative-position-vol-targeting]] — narrative/event × vol targeting: each narrative/memecoin position sized to a fixed 1%-of-portfolio daily-vol risk budget (notional = budget / daily_vol); 5% single-position cap; 25% portfolio notional heat cap and 2.5% aggregate daily-vol cap across concurrent narrative positions; vol-targeted stop = 2.5× daily risk budget below entry; explicitly differentiated from vol-targeted-trend-following (large-cap BTC/ETH trend book) — this page targets the high-vol-dispersion narrative sub-book (RV range 80%–500%+ annualised)
  - [[smart-money-vs-crowd-divergence]] — on-chain flow × funding filter: long entry requiring all five simultaneous gates: whale score ≥ 65 (accumulating); 24h exchange outflow top-quartile OR 7d net outflow; funding ≤ 0.00%/8h; long/short ≤ 0.95; at least one higher low on daily (no consecutive lower lows); exit when funding ≥ +0.02% AND L/S ≥ 1.05, or whale score drops below 50 for 2 days; explicitly differentiated from smart-money-orderflow-combo (order-flow second leg, intraday) and crowded-short-funding-fade (positioning alone, no on-chain gate)
  - [[low-leverage-vol-selling]] — vol selling × OI filter: sell BTC strangle (25d put + 15d call) ONLY when OI/MC ≤ 2.0% (no leverage) AND funding flat [−0.01%, +0.02%/8h] AND long/short balanced [0.90–1.20] AND DVOL ≥ 45th percentile AND IV−RV ≥ 5 vol pts; live OI/MC monitoring — exit if OI/MC rises above 2.8% while position open (leverage rebuilding); structural inverse of leverage-stress-tail-hedge; fourth distinct vol-selling entry regime: leverage-ABSENCE gate
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked: mean-reversion × tail-hedge overlay ([[put-protected-dip-buying]] with footnote ¹⁴), grid × OI filter ([[oi-aware-grid]]), narrative × vol targeting ([[narrative-position-vol-targeting]]), vol selling × OI filter ([[low-leverage-vol-selling]] with footnote ¹⁵), on-chain flow × funding filter ([[smart-money-vs-crowd-divergence]] with footnote ¹⁶); counts updated (existing: 42→47, planned: 49→44); footnotes ¹⁴–¹⁶ added; Batch B6 section prepended
  - [[log]] (this file) — Batch B6 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates confirmed additive. No backups used.
- Vol-selling differentiation note: [[low-leverage-vol-selling]] (vol selling × OI filter) is explicitly differentiated in its lead from all three prior vol-selling combos: funding-conditioned-vol-selling (HIGH funding), post-panic-vol-selling (post-event fear extreme), and trend-aligned-premium-selling (trend-selected wing). The four vol-selling combos now cover four distinct entry regimes: leverage-absent, leverage-crowded-long, post-crash-fear, and trend-selected.
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete illustrative round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related), verified CryptoDataAPI endpoints only (open-interest, funding-rates, long-short-ratio, whale-score, exchange-flows, dvol-history, klines, liquidations, sentiment, regimes/current), honest about Deribit options API requirement (put-protected-dip-buying and low-leverage-vol-selling), approved tags only.


## 2026-07-19 — Batch B5: 5 New Combination Strategy Pages

- Pages created (5):
  - [[trend-aware-carry]] — funding carry × trend gate: carry book (short perp / long spot) that scales to 60% then 30% deployment when a strong uptrend is confirmed (BTC ≥ 15% above SMA20, 4h RSI ≥ 70, 7d funding ≥ 0.05%/8h); reduces exposure to funding-flush and basis-blowout risk without paying option-premium costs; re-enters in tranches over 3 days after trend normalises; explicitly differentiated from carry-with-tail-hedge (permanent hedge overlay, not a sizing throttle)
  - [[post-panic-vol-selling]] — vol selling × sentiment-extreme filter: enter short-vol (sell 25-delta BTC put) only after a panic spike when all five stabilisation gates pass simultaneously (Fear & Greed ≤ 20 for 2 days; DVOL ≥ 85th percentile AND +20 vol-pt spike from 5d ago; 24h RV rolling over from ≥ 80 vol-pt peak; 12h liquidation volume < 1.5× 7d avg; no new 7-day low in last 4h candle); harvests the fear-premium mean-reversion post-stabilisation; explicitly differentiated from funding-conditioned-vol-selling (fires on pre-crash bullish crowding, not post-crash fear)
  - [[cascade-monetization-rotation]] — liquidation plays × tail-hedge overlay: two-leg lifecycle strategy: accumulate 10-delta OTM puts during stress build-up using leverage-stress-tail-hedge entry rules; monetise when cascade fires (≥12% price drop OR DVOL +25pts with $500M+ 6h liquidations); rotate 60% of gross payoff into cascade-fade perp long within 4 hours when CVD is flattening, liquidation decelerating, and price ≥ 10% below pre-cascade level; the combination is the capital rotation (fade capital comes from tail-hedge payoff, not additional committed capital)
  - [[unlock-pair-hedge]] — stat-arb/pairs × unlock/event calendar: beta-hedged long-short pair expressing token cliff unlock shorts (≥ 3% of circulating supply) as short-unlocking-token perp / long-sector-peer perp at hedge ratio = 1/beta; strips BTC/sector beta to isolate idiosyncratic supply-shock component; enter 6 days before unlock, exit 10 days post-unlock; explicitly differentiated from unlock-short-with-crowding-gate (outright directional short with crowding filter — not beta-neutral)
  - [[trend-aligned-premium-selling]] — vol selling × trend gate: sell puts in confirmed uptrends (price ≥ 10% above SMA20, 4h RSI ≥ 60, funding ≥ 0.02%/8h), sell calls in confirmed downtrends (≥ 8% below SMA20, RSI ≤ 45, funding ≤ 0); trend selects which wing to sell rather than whether to sell; DVOL ≥ 50th percentile also required; explicitly differentiated from funding-conditioned-vol-selling (funding crowding trigger in any regime direction) and post-panic-vol-selling (post-crash fear trigger)
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked: funding carry × trend gate ([[trend-aware-carry]]), vol selling × sentiment-extreme filter ([[post-panic-vol-selling]]), liquidation plays × tail-hedge overlay ([[cascade-monetization-rotation]] with footnote ¹³), stat-arb/pairs × unlock/event calendar ([[unlock-pair-hedge]]), vol selling × trend gate ([[trend-aligned-premium-selling]]); counts updated (existing: 37→42, planned: 54→49); footnote ¹³ added; Batch B5 section prepended
  - [[log]] (this file) — Batch B5 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates confirmed additive. No backups used.
- Vol-selling differentiation: [[post-panic-vol-selling]] (vol selling × sentiment-extreme) and [[trend-aligned-premium-selling]] (vol selling × trend gate) are in distinct cells; their leads explicitly differentiate from each other and from [[funding-conditioned-vol-selling]].
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete illustrative round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related), verified CryptoDataAPI endpoints only (klines, funding-rates, open-interest, dvol-history, liquidations, long-short-ratio, fear-greed-index, regimes/current), honest about Deribit options API requirement (consistent with all B3-B4 vol pages), approved tags only.


## 2026-07-19 — Batch B4: 5 New Combination Strategy Pages

- Pages created (5):
  - [[correlation-regime-pairs]] — stat-arb/pairs × regime gate: pairs/stat-arb book operated only while the pair's cointegrating relationship is demonstrably active (rolling 30d correlation ≥ 0.70, ADF cointegration p ≤ 0.10, OU half-life 3–45 days); flatten immediately on correlation breakdown below 0.60 rather than averaging into a structurally broken spread; composable with pairs-with-funding-differential's funding-differential gate as a second layer
  - [[event-vol-buying]] — vol buying × unlock/event calendar: buy ATM straddles or OTM strangles on Deribit ahead of scheduled binary-outcome catalysts (Bitcoin halvings, SEC ETF decision deadlines, major Ethereum hard forks, significant token unlocks, regulatory votes) when ATM IV on the catalyst expiry is within 10% of its 30-day trailing DVOL average (event not yet priced); exit on +20 vol-point IV expansion or within 48h post-event; the long-side event counterpart to funding-conditioned-vol-selling
  - [[session-aware-mean-reversion]] — mean-reversion × session/time filter: RSI/VWAP/Bollinger-band mean-reversion with session-conditional parameter table (peak / Asia-overnight / weekend / session-transition); lower RSI threshold and lower VWAP deviation required in thin sessions; session-open transition windows (+0.2× size bonus); explicitly NOT a cascade strategy (that is off-hours-liquidation-playbook); the routine daily drift-and-revert that occurs without liquidation spikes
  - [[leverage-stress-tail-hedge]] — vol buying/tail hedge × OI filter: standalone OTM put accumulation strategy (no carrier book) triggered when all three leverage-stress gates are simultaneously elevated (BTC OI/market-cap ≥ 3.0%, 7d-average 8h funding ≥ 0.04%, long/short ratio ≥ 1.8); exit on crash payoff (≥12% price drop), DVOL expansion (+25 vol points), or stress deactivation; differentiated from carry-with-tail-hedge (hedge secondary to a carry book) and convex-tail-hedge-arbitrage (vol-cheapness triggered)
  - [[spot-led-momentum-filter]] — momentum × cross-venue: momentum entries conditioned on three simultaneous cross-venue flow-origin signals (Coinbase premium ≥ 0.05% sustained ≥ 2 of 3 hours; 8h funding ≤ 0.03%; spot volume ≥ 1.2× 7d avg AND OI 3d growth ≤ 15%); spot-led moves reflect real capital inflow; perp-led moves are leverage that mean-reverts; differentiated from funding-filtered-momentum which gates on funding LEVEL, not flow ORIGIN
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked (stat-arb × regime gate, vol buying × event calendar, mean-reversion × session filter, vol buying × OI filter, momentum × cross-venue); session-aware-mean-reversion also placed in momentum × session filter cell (footnote ¹² added); counts updated (existing: 32→37, planned: 59→54); footnote ¹² added; Batch B4 section prepended
  - [[log]] (this file) — Batch B4 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates confirmed additive. spot-led-momentum-filter assessed against funding-filtered-momentum and confirmed distinct (flow origin vs funding level). No backups used.
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete illustrative round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related), honest about Deribit options API requirement (consistent with funding-conditioned-vol-selling), verified CryptoDataAPI endpoints only (coinbase-premium, funding-rates, open-interest, dvol-history, klines, liquidations, long-short-ratio, regimes/current), approved tags only.


## 2026-07-19 — Batch B3: 5 New Combination Strategy Pages

- Pages created (5):
  - [[funding-vs-basis-rotation]] — basis/cash-and-carry × funding filter: allocation-layer strategy that switches the carry book between perp-funding carry (long spot, short perp) and dated-futures basis carry (long spot, short quarterly) depending on which annualised yield is higher net of costs; hysteresis prevents churn; always market-neutral and always earning the fatter of the two available carry streams
  - [[funding-conditioned-vol-selling]] — vol selling × funding filter: sell BTC/ETH options on Deribit only when perp funding is elevated (≥ 0.03%/8h confirming a leveraged-retail crowd driving IV richness) AND DVOL percentile is in the 40th–90th range AND IV−RV > 5 vol points; funding adds information beyond the DVOL-percentile gate by identifying *why* the surface is rich (leverage-crowd demand vs. genuine macro uncertainty); call-wing tilt when funding ≥ 0.05%/8h
  - [[off-hours-liquidation-playbook]] — liquidation plays × session/time filter: session-conditional extension of the cascade-fade strategy; applies different entry thresholds, minimum cascade sizes, position-size multipliers, target reversion ranges, and slippage budgets depending on session window (US/EU peak, Asia/overnight, weekend); off-hours cascades travel further per dollar of forced flow in thin books — the session layer concentrates risk where the reversion edge is amplified
  - [[narrative-with-trend-confirmation]] — narrative/event × trend gate: enter narrative/theme trades only after price structure confirms (20-day channel high breakout or higher-low above 50-day SMA), avoiding the pioneer-penalty regime where a correct narrative precedes the capital flow by weeks; dual-exit discipline (narrative decay OR trend break, whichever fires first) prevents sitting through secondary distribution
  - [[onchain-capitulation-confluence]] — on-chain flow × sentiment-extreme filter: bottom-fishing entry for BTC that requires BOTH an on-chain capitulation signal (exchange-inflow top-decile spike, SOPR ≤ 0.97 for 5+ days, or MVRV-Z ≤ 0) AND Fear & Greed ≤ 20 for 2+ consecutive days; the dual-signal confluence addresses the two failure modes of single-signal bottom fishing — fear without on-chain selling (correction, not bottom) and on-chain selling without sentiment extreme (distribution, not capitulation)
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked (basis × funding filter, vol selling × funding filter, liquidation plays × session filter, narrative × trend gate, on-chain flow × sentiment filter); counts updated (existing: 27→32, planned: 64→59); footnote ¹¹ added; Batch B3 section prepended
  - [[log]] (this file) — Batch B3 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates confirmed additive. The two backup candidates (correlation-regime-pairs, session-aware-mean-reversion) were not needed.
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead with explicit differentiation from nearest neighbors + Edge source + Why this edge exists + Null hypothesis + Rules + Pseudocode + Indicators + Example trade with concrete round-trip numbers + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data (CryptoDataAPI) + Related), verified CryptoDataAPI endpoints only (no invented paths), honest about DVOL/SOPR gaps requiring external sources, kill criteria with numeric triggers, approved tags only.


## 2026-07-19 — Batch B2: 5 New Combination Strategy Pages

- Pages created (5):
  - [[pairs-with-funding-differential]] — stat-arb/pairs × funding filter: perp-expressed pairs where the funding differential between legs agrees with the spread z-score direction; earns both mean-reversion of the spread and structural carry for being on the non-crowded leg
  - [[funding-flush-reversal]] — mean-reversion × funding filter: dip-buy only after funding has sustained below −0.02%/8h for 24h+, confirming leveraged-long deleveraging is complete and shorts are now the crowded, carry-paying party
  - [[unlock-aware-momentum]] — momentum × unlock/event calendar: momentum book that freezes new longs 5 days before and closes all longs 2 days before cliff unlock events, re-entering after supply digestion with post-unlock momentum re-confirmation
  - [[funding-skewed-grid]] — grid/market-making × funding filter: perp grid whose inventory allocation is biased toward the funding-receiver side (earn both spread and carry simultaneously); skew rebalances when funding direction flips
  - [[oi-flush-reversion]] — mean-reversion × OI filter: dip-buy only after OI has declined ≥ 15% from its 5-day peak, confirming leveraged deleveraging is substantially complete before entering the mean-reversion long
- Pages updated (2):
  - [[combination-matrix]] — 5 new cells linked (mean-reversion × funding filter, mean-reversion × OI filter, momentum × unlock/event calendar, grid × funding filter, stat-arb × funding filter); cell counts updated (existing: 22→27, planned: 69→64); Batch B2 section added
  - [[log]] (this file) — Batch B2 entry prepended
- Candidates skipped (0 of 5 primaries): all five primary candidates were confirmed additive (no existing page covered the same combination × primitive pair)
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure (lead + Edge source + Why this edge + Null hypothesis + Rules + Pseudocode + Indicators + Example trade + Performance + Capacity + What kills it + Kill criteria + Advantages + Disadvantages + Sources + Getting the Data + Related), CryptoDataAPI endpoints verified against B1 exemplars, kill criteria with numeric triggers, differentiation sentences in lead paragraphs, approved tags only.


## 2026-07-18 — Batch B1: Combination Matrix + 5 New Combination Strategy Pages

- Pages created (7):
  - [[combination-matrix]] — primitive × overlay coverage matrix (22 existing, 69 planned, 9 non-viable cells)
  - [[combinations-overview]] — category overview with Dataview table and combination families
  - [[funding-filtered-momentum]] — momentum entries gated by non-consensus (flat/negative) funding
  - [[regime-gated-grid]] — grid trading activated only inside confirmed low-vol range regimes
  - [[carry-with-tail-hedge]] — funding carry book with budgeted OTM put overlay financed from carry income
  - [[unlock-short-with-crowding-gate]] — token unlock supply-event short filtered for non-crowded entry conditions
  - [[vol-targeted-trend-following]] — crypto-native trend following with volatility-targeted position sizing
- Pages updated (1):
  - [[strategies-overview]] — added [[combination-matrix]] link alongside [[combinations-overview]] in the Subcategories list
- Candidates skipped (3 of 8 assessed):
  - `onchain-confirmed-breakout` — high overlap with [[on-chain-flow-trading]] and [[smart-money-orderflow-combo]]; noted in matrix
  - `sentiment-regime-rotation` — high overlap with [[contrarian-extremes]], [[crypto-beta-rotation]], [[regime-adaptive-strategy]]; noted in matrix
  - `pairs-with-funding-differential` — partial overlap with [[pairs-trading]] and [[hl-vs-cex-funding-divergence]]; deferred to next batch
- All 5 new strategy pages: type=strategy, strategy_type=hybrid, markets=[crypto], backtest_status=untested, full 16-section structure, CryptoDataAPI data section with verified endpoints only, kill criteria, wikilinks to primitives and neighbors.


## 2026-07-16 12:47 — Batch Import: Top 2376 Cryptocurrencies (CoinGecko)

- Source: [[coingecko-top-1000-2026-07-16]]
- Type: data (API batch import)
- Pages created (1339): [[united-stables]], [[spiko-amundi-overnight-swap-fund-eur]], [[pudgy-penguins]], [[peanut-2-2]], [[coco-2]], [[spark-usdc]], [[tradable-apac-diversified-finance-provider-sstn]], [[lido-earn-eth]], [[safo]], [[tradable-latam-fintech-sstn]], [[alpha-bulgaria-warrants]], [[genius-3]], [[tradable-na-third-party-online-merchant-sstn]], [[manadia]], [[tradable-latam-middle-market-lender-sstl]], [[tradable-latam-middle-market-lender-sstl]], [[nexus-4]], [[saturn-dollar]], [[tradable-singapore-fintech-ssl]], [[cash-cat]] ... and 1319 more
- Pages merged (1037): [[bitcoin]], [[ethereum]], [[usdt]], [[bnb]], [[usdc]], [[xrp]], [[solana]], [[tron]], [[figure-heloc]], [[hype]] ... and 1027 more
- Data points per coin: 20 (metadata, market data, tokenomics, social, developer, exchange listings)
- Confidence: HIGH (official CoinGecko API data)

## 2026-07-14 — Second-tier options/quant/charting crypto re-scope (Wave 4)

Re-scoped ~56 more crypto-relevant pages from equity framing to crypto (9 parallel Opus agents), finishing the technique/structure upgrade the user requested. Options spreads & structures (bull/bear verticals, credit/calendar/ratio spreads, straddles/strangles, 0DTE, cash-secured puts, long-call/put, put-call parity) → crypto structure theory on Deribit. Vol strategies (premium-selling, long/short-vol, tail hedges, and the VIX pages reframed to DVOL — honestly flagging crypto has no tradeable VIX-future/ETP analog). Crypto-applicable quant (mean-reversion, pairs, stat-arb, Ornstein-Uhlenbeck, Kalman, Bollinger-reversion, regime-detection) rebuilt to the buildable schema (all `untested`, Sharpes revised down for crypto). Price-action methods (gap/pullback/London-breakout = strategies; ICT/SMC/triple-screen = concept frameworks). Duplicate stubs redirected (vertical-spreads, iron-condors, calendar-spread root, cash-secured-put, delta-hedging/gamma-scalping strategy copies). Created [[dvol]] (Deribit Volatility Index) for 16 inbound links; stripped stray equity tags from ~60 already-crypto pages; redirected iron-fly→iron-butterfly.

Deliberately LEFT as intentional cross-asset reference (not gaps): the historical/TradFi arbitrage encyclopedia (gold-point, medieval bills, treasury/currency/commodity-basis arbs) and TradFi portfolio theory (Black-Litterman, CPPI, factor-investing) — already-thorough theory pages that are cross-asset by design.

## 2026-07-14 — Technique & options-structure theory upgrade (Wave 3)

Upgraded ~58 charting-technique and options-structure pages from thin/equity-framed essays into comprehensive, crypto-scoped theory pages (9 parallel agents). Charting theories (Elliott wave, Fibonacci, Gann, harmonic patterns, Ichimoku, Heikin-Ashi, Renko, point-and-figure, Darvas, Supertrend, Parabolic SAR, supply-demand, breakout, Donchian, volatility-arb) re-typed `strategy`→`concept` with full method coverage. Options structures (iron-condor family, straddles/strangles, spreads, covered/protective/wheel) rewritten to a structure template (construction, payoff, greeks, adjustments, crypto specifics) and re-scoped from `[stocks]`/SPY to crypto/Deribit. Options-theory concepts (Black-Scholes, delta/vega hedging, IV-crush, moneyness, selection frameworks) given crypto grounding. No buildable-alpha schema was bolted onto theory/structure pages. Several duplicate stubs redirected (long-straddle, covered-calls, collar-strategy, protective-puts, concepts/options iron-butterfly + gamma-scalping). All endpoints verified; zero new dangling links.

## 2026-07-14 — Depth-parity rewrites (Wave 2)

Rewrote 24 crypto-native strategy essays from descriptive prose into the buildable strategy schema (full frontmatter + 16-section structure + realistic cost overlays + `## Getting the Data (CryptoDataAPI)`), matching the funding-rate-arbitrage gold standard. Buildable strategy pages rose 215 → 251. Scope drift (equity/commodity tags) removed from latency-arbitrage, calendar-spread-arbitrage, cash-and-carry.

- algorithmic: [[basis-trading]], [[restaking-strategies]], [[points-farming]], [[airdrop-farming]], [[liquidity-sniping]], [[synthetic-asset-trading]], [[intent-based-trading]], [[nft-trading]]
- combinations: [[delta-neutral-yield-farming]], [[crypto-yield-stack]], [[smart-money-orderflow-combo]]
- quantitative: [[sentiment-trading]], [[momentum-rotation]], [[skew-trading]], [[garch-volatility]]
- day-trading: [[order-flow-scalping]], [[scalping]], [[vwap-trading]]
- arbitrage: [[cross-exchange-arbitrage]], [[flash-loan-arbitrage]], [[latency-arbitrage]], [[staking-yield-arbitrage]], [[calendar-spread-arbitrage]], [[cash-and-carry]]
- also created concept pages [[coinbase-premium]] and [[participation-rate]] (filled inbound forward-links).

## 2026-07-14 — Strategy-creation gap-fill (Wave 1)

Filled the value-bearing gaps from the 2026-07-14 strategy-creation gap analysis (see [[coverage-gaps]]): 34 new pages + 5 essay→buildable rewrites + crypto sections on 6 existing pages, authored by 7 parallel agents. Adds the front-of-funnel methodology (idea generation, feature/signal engineering, ML labeling), crypto-specific backtest validation, missing archetypes (on-chain market-making, LVR, crypto options), execution/sizing, and live-ops runbooks. All new/rewritten pages carry the buildable schema and `## Getting the Data (CryptoDataAPI)` sections using only verified endpoints. Sub-clusters below.

### Crypto options, ETF-flow, cycle-timing & beta-rotation strategy cluster

Authored five new crypto strategy pages, each on the full buildable strategy schema (complete frontmatter + 16-section structure + realistic fees/funding/slippage/borrow cost overlay, never a naive backtest), with a `## Getting the Data (CryptoDataAPI)` section using only verified endpoints.

- Pages created:
  - [[crypto-options-volatility-selling]] — selling BTC/ETH vol on Deribit; DVOL-percentile regime gating, inverse vs linear (USDC) settlement, perp-driven skew, no §1256 shelter, strangles/iron-condors sized by DVOL, delta-hedge cadence, vol-shock kill switches (2020-03/LUNA/FTX/2025-10-10) (strategies/quantitative)
  - [[crypto-options-dispersion]] — index (BTC/ETH-major) vs single-name implied-vol dispersion; correlation mean-reversion; Deribit/venue constraints on alt-option liquidity (strategies/quantitative)
  - [[etf-flow-directional]] — trade spot BTC/ETH ETF NET FLOW directionally (flow-momentum, z-score sizing, flow-reversal exit); explicitly distinguished from the [[etf-arbitrage|NAV arb]] (strategies)
  - [[bitcoin-halving-cycle-timing]] — cycle top/bottom timing via [[mvrv]]/[[mvrv-z-score]]/[[nupl]]/[[realized-price]] bands + months-since-halving overlay; accumulation vs distribution zones; long-horizon sizing (strategies/position-trading)
  - [[crypto-beta-rotation]] — crypto-beta vs DXY/Nasdaq risk-on/off regime rotation; de-beta/hedge when [[crypto-macro-correlation-regime|correlation regime]] + DXY trend flip risk-off (strategies/quantitative)
- Endpoints used (all verified): market-intelligence (options/max-pain, etf/{asset}/flows, etf/btc/aum, coinbase-premium, exchange-balance, btc/cycle-indicators, fear-greed-history, liquidations), volatility/regime(+score,+/{symbol}), quant/gex + quant/market, on-chain (dormancy/btc, score, miners/hash-ribbon, whale-score, exchange-flows), regimes/current, policy/regime, liquidity/regime, sentiment/macro, derivatives/funding-rates, market-data/klines + btc-price-history, backtesting/klines. DVOL/IV surface sourced from [[deribit]]/[[greeks-live]] (noted as non-CDA).

### AMM LP economics & market-making cluster

Authored one new concept page and one new strategy page, and rewrote three existing essay-style strategy pages to the full buildable strategy schema (16 sections + strategy frontmatter).

- Pages created:
  - [[loss-versus-rebalancing]] — the LVR framework: LP vs the arbitrageur, LVR vs impermanent loss (path-dependence), markout as the empirical estimator, why LVR is the dominant modern lens on AMM LP profitability, the "hedging removes IL variance but not LVR" insight, CL implications, and LVR-mitigation AMM designs (am-AMM, CoW/FM-AMM, Diamond, dynamic fees, v4 hooks). Populates the near-empty concepts/defi folder. (concepts/defi)
  - [[hyperliquid-market-making]] — be-the-maker on the Hyperliquid on-chain CLOB: two-sided quoting, Avellaneda-Stoikov inventory skew (parameterized with concrete BTC numbers), maker rebates/fee tiers, adverse-selection/markout management, hourly funding exposure of inventory, HLP competitive context, toxic-flow & inventory-blowout kill criteria. Native counterpart to the perps corpus. (strategies/quantitative)
- Pages rewritten (same filenames, restructured to buildable schema):
  - [[concentrated-liquidity]] — Uniswap v3/v4 CL LP as buildable strategy: vol-sized tick-range selection, rebalance triggers, fee-APR vs IL/LVR math, LVR-aware delta-hedge overlay (`delta = x(p)`), links [[loss-versus-rebalancing]], kill criteria. (strategies/algorithmic)
  - [[jit-liquidity]] — mempool-triggered single-block LP spec: uninformed-flow filter, flash-loaned atomic mint→swap→burn bundle, economics gate (fee > gas + tip + single-swap LVR), JIT-resistance decay. (strategies/algorithmic)
  - [[market-making-strategy]] — re-scoped from stocks/forex to crypto CEX (Binance/Bybit); parameterized Avellaneda-Stoikov, thin-alt adverse-selection caveats, VIP/MM-program fee reality, 8h funding on inventory; complement to [[hyperliquid-market-making]]. (strategies/day-trading)
- All pages carry `## Getting the Data (CryptoDataAPI)` sections using only verified endpoints (volatility/regime, market-data & backtesting klines, hyperliquid l2-book/funding/candles, liquidity/depth, derivatives funding/OI, dex trending/token). HL fee schedule and LVR magnitudes verified against Hyperliquid docs and Milionis et al. (2022, arXiv:2208.06046).

### Live-ops infrastructure & buildable-strategy rewrites

Authored four infrastructure concept pages, one data-source page, and rewrote two algorithmic strategy essays to the buildable strategy schema (full frontmatter + 16-section structure + realistic cost overlay).

- Pages created:
  - [[paper-to-live-promotion]] — backtest→testnet→canary→scale promotion ladder with go/no-go gates and canary sizing (concept, `wiki/ai-trading/infrastructure/`)
  - [[bot-kill-switch-design]] — kill-switch/circuit-breaker design: trigger taxonomy, global-flatten vs per-strategy halt, auto vs manual, reduce-only unwind, distinguished from exchange circuit breakers (concept)
  - [[position-reconciliation]] — internal state vs exchange truth; partial fills, funding/fees, WebSocket gaps, restart recovery; reconciliation loop (concept)
  - [[exchange-api-key-security]] — permission scoping, withdrawal-disabled keys, IP allowlists, sub-accounts, HSM/Ed25519 secrets, rotation/revocation drills (concept)
  - [[proof-of-reserves]] — CEX PoR as counterparty-health monitoring signal; Merkle/zk-SNARK PoR, post-FTX context, no-liabilities gap, live-risk wiring (source)
- Pages rewritten (same filenames, buildable strategy schema):
  - [[mev-strategies]] — sandwich/backrun/JIT/DEX-arb each as a spec with infra (Flashbots/Jito, private mempools, priority fees) and gas/competition cost overlay
  - [[defi-yield-farming]] — APR decomposition (fees/emissions/incentives), IL/LVR, delta-hedge overlay, SC-risk-adjusted sizing, rotation and kill rules
- Getting the Data (CryptoDataAPI) sections added where data-mapped (verified endpoints only): backtesting/market-health, security/health, derivatives funding, dex + security, on-chain exchange-flows/reserves.

### Crypto execution & sizing cluster

Authored five new concept pages and one strategy page on crypto execution, perp sizing, and portfolio-level risk aggregation, and extended one existing page.

- Pages created:
  - [[cross-venue-execution-crypto]] — routing a directional order across Binance/Bybit/OKX/Hyperliquid by book depth, fee tier, and funding; depth-proportional allocation; explicitly not arbitrage (concepts/market-microstructure)
  - [[thin-market-execution]] — executing in illiquid alt books: child-order sizing to depth, participation-rate caps, self-impact avoidance, iceberg/TWAP, when not to trade (concepts/market-microstructure)
  - [[funding-aware-position-sizing]] — funding-adjusted Kelly for perps; carry-adjusted drift `μ_eff = μ ∓ φ`; sizing funding-positive vs funding-negative positions (concepts/risk-management)
  - [[liquidation-price-aware-sizing]] — sizing so liquidation sits beyond a 3σ / named-wick stress move; `L ≤ 1/(S+m+β)`; isolated vs cross; buffer & add-margin rules (concepts/risk-management)
  - [[crypto-portfolio-heat]] — aggregate BTC-beta exposure across nominally-different alt longs that converge to ~1.0 in a crash; beta-weighted heat budgeting (concepts/portfolio-theory)
  - [[multi-strategy-crypto-portfolio]] — perp-carry + momentum + on-chain + memecoin sleeves in one book; all-correlated-in-crisis, per-venue caps, stablecoin base, regime-based allocation; full buildable schema (strategies/combinations)
- Pages updated:
  - [[smart-order-routing]] — added "Crypto-Venue Routing" section linking [[cross-venue-execution-crypto]] and [[thin-market-execution]]; kept existing equities/SOR content (no de-scope)
- All new pages carry `## Getting the Data (CryptoDataAPI)` sections using only verified endpoints (liquidity/depth, derivatives & hyperliquid funding, volatility regime, market-data/backtesting klines, on-chain, dex, regimes).

### Crypto backtesting & idea-generation cluster

Authored six new pages and extended two existing ones, filling gaps in the strategy-development and backtesting sections.

- Pages created:
  - [[crypto-idea-generation]] — generative, inversion-based process for mining new crypto strategy hypotheses (strategy-development)
  - [[crypto-data-quality]] — GIGO checklist for crypto backtest data corruption (concepts/backtesting)
  - [[regime-conditional-validation]] — per-regime Sharpe attribution and regime-stratified holdouts across the 14 crypto regimes (concepts/backtesting)
  - [[crypto-short-history-statistical-power]] — tiny effective N, wide Sharpe CIs, MinTRL vs available history (concepts/backtesting)
  - [[crypto-forward-testing]] — testnet vs live-info shadow, champion-challenger, perp-metric reconciliation (concepts/backtesting)
  - [[probability-of-backtest-overfitting]] — PBO via CSCV, crypto framing; resolves an existing red link (concepts/backtesting)
- Pages updated:
  - [[wash-trading]] — added "Backtesting Data-Quality Impact" section (venues to distrust, signal corruption, detection heuristics)
  - [[cryptodataapi-backtesting]] — added "From Archive to Validated Strategy" subsection (survivorship-universe construction + CPCV/DSR/PBO handoff)
- All new pages carry `## Getting the Data (CryptoDataAPI)` sections using only verified endpoints (backtesting archive, quant point-in-time regime history, derivatives/on-chain/hyperliquid feeds).

## 2026-07-13 — Vault created

Vault scoped to crypto-trading ("AlgoBrain"). Removed stock-market entities, stock news, personal/persona pages, and off-scope equity content; retained crypto, blockchain, DeFi, trading, algorithms, markets, macro context, and general AI knowledge. Added CryptoDataAPI data-source documentation and per-page "Getting the Data (CryptoDataAPI)" sections.
