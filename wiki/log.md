---
title: "Wiki Operations Log"
type: index
created: 2026-07-13
updated: 2026-07-19
status: good
tags: [meta, log]
---

Chronological, append-only record of all wiki operations. Newest entries at the top.


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
