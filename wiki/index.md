---
title: "AlgoBrain — Index"
type: index
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [index, meta]
---

# AlgoBrain — Index

A comprehensive, LLM-maintained knowledge base for crypto trading strategy: crypto, blockchain, DeFi, trading, algorithms, and markets — with macro and AI context.

## Categories

### Markets
- [[markets-overview|Markets Overview]] — Crypto, Forex, Commodities, Options, Futures, Bonds (macro context for crypto)

#### Commodities
- Hub pages: [[commodities]], [[commodities-overview]], [[commodity-trading]]
- Key markets: [[crude-oil]], [[gold]], [[copper]], [[corn]], [[coffee]], [[natural-gas]]
- Key concepts: [[contango]], [[backwardation]], [[roll-yield]], [[cot-report-analysis]], [[commodity-seasonality-patterns]]
- Key strategies: [[crack-spread]], [[crush-spread]], [[commodity-momentum]], [[commodity-carry-strategy]], [[trend-following-cta]]
- Comparisons: [[commodity-futures-vs-etfs]], [[physical-vs-paper-commodities]]
- Data: [[commodity-data-sources]]

#### NFTs
- Hub page: [[nft]] — Non-fungible token market history, collections, marketplaces
- Protocols & asset classes: [[bitcoin-ordinals]] (replaces former ordinals.md; [[ordi]] is the token)
- Standards: [[erc-721]], [[erc-998]]
- Infrastructure events: [[dencun-upgrade]] (March 2024 — Ethereum upgrade, L2 gas economics)
- Marketplaces: [[opensea]], [[blur]], [[magic-eden]], [[looksrare]], [[rarible]], [[tensor]], [[sudoswap]], [[x2y2]], [[nifty-gateway]]
- Protocol infrastructure: [[seaport]], [[nftfi]], [[blend]], [[benddao]]
- Aggregators & analytics: [[genie]], [[gem-nft]], [[rarity-tools]], [[openrarity]], [[trait-sniper]], [[rarity-sniper]], [[moby-gg]], [[nft-price-floor]], [[dappradar]], [[zerion]]
- Phygital / RWA: [[courtyard]], [[veve]], [[floor-xyz]]
- Creators & teams: [[ponderware]] (MoonCats)
- Strategies & concepts: [[nft-trading]], [[nft-arbitrage]], [[nft-archaeology]]
- Concepts: [[nft-rarity-scoring]], [[nft-floor-price]], [[nft-aggregators]], [[nft-royalty-enforcement]], [[nft-lending]], [[phygital-nfts]]

### Strategies
- [[strategies-overview|Strategies Overview]] — Technical, Fundamental, Quantitative, Algorithmic, Day Trading, Swing Trading
- [[regime-matrix|Strategy Regime Matrix]] — Which strategies work in which market conditions
- [[live-journal|Live Strategy Journal]] — Production strategies and their lifecycle history
- [[hyperliquid-baskets-overview|Hyperliquid Basket Library]] — The 27 live signal baskets (Defensive Majors, OI-Confirmed Trend, funding fades, liquidation rides, breakout/range, macro-flow, event sleeves), each a full strategy page gated to a [[crypto-market-regime-taxonomy|market regime]]
- Live bot strategies (excellent coverage): [[funding-rate-arbitrage]], [[stock-perp-oracle-basis]], [[liquidation-cascade-fade]], [[rsi-mean-reversion]], [[moving-average-crossover]], [[grid-trading]]
- Price-action / order-flow strategies: [[volume-profile-trading-strategy|Volume Profile Trading Strategy]] (value-area rotation, LVN breakouts, naked-POC retests) · [[arc-strategy|ARC (Area·Range·Candle)]] (box/swing levels + range filter + John Wick candle entries)
- Crypto options & flow strategies: [[crypto-options-volatility-selling|Crypto Options Volatility Selling]] (Deribit BTC/ETH short vol, DVOL-gated, no §1256) · [[crypto-options-dispersion|Crypto Options Dispersion]] (index vs single-name IV, correlation mean-reversion) · [[etf-flow-directional|ETF Flow Directional]] (spot-ETF net-flow momentum, not the arb) · [[crypto-beta-rotation|Crypto Beta Rotation]] (DXY/Nasdaq risk-on/off de-beta overlay) · [[bitcoin-halving-cycle-timing|Bitcoin Halving Cycle Timing]] (MVRV/NUPL/realized-price cycle zones)
- AI/Macro themes:
  - [[crypto-ai-recession-shorts|Crypto AI Recession Shorts]] — BTC dominance long, alt + mining-equity + COIN shorts; expresses dispersion not direction

### Strategy Development
- [[strategy-development-overview|Strategy Development]] — Methodology for *producing* new strategies
- [[edge-taxonomy|Edge Taxonomy]] — The six sources of trading edge
- [[hypothesis-to-backtest-workflow|Hypothesis → Backtest Workflow]] — End-to-end research pipeline
- [[research-checklist|Research Checklist]] — 20 questions before any backtest
- [[overfitting-detection|Overfitting Detection]] — Walk-forward, CPCV, sensitivity
- [[curve-fitting|Curve Fitting]] — The act that produces overfitting; forms and defenses
- [[data-snooping-and-p-hacking|Data Snooping & P-Hacking]] — Multiple testing correction
- [[failure-modes|Strategy Failure Modes]] — How strategies die in the wild
- [[strategy-monitoring|Strategy Monitoring & Alerting]] — Dashboard design, alert thresholds, kill criteria operationalization
- [[arbitrage-opportunity-map|Arbitrage Opportunity Map]] — Cross-wiki synthesis of explicit, implicit, and hidden arbitrage opportunities
- [[arbitrage-overview|Arbitrage Hub]] — 45+ arbitrage strategies, from cash-and-carry to MEV to historical LTCM relative value
  - Fixed income / relative value: [[relative-value-arbitrage]], [[on-off-the-run-treasury-arbitrage]], [[swap-spread-arbitrage]], [[tips-treasury-arbitrage]], [[mbs-basis-arbitrage]], [[cds-bond-basis-arbitrage]]
  - NAV / fund structure: [[closed-end-fund-arbitrage]], [[etf-arbitrage]]
  - Macro / FX: [[covered-interest-arbitrage]], [[currency-peg-break-arbitrage]], [[gold-silver-ratio-arbitrage]]
  - Options parity: [[put-call-parity-arbitrage]]
  - Historical blowups: [[cum-ex-scandal]], [[archegos-blowup-2021]]
  - Classical / gold-standard era: [[gold-point-arbitrage]], [[specie-flow-arbitrage]], [[mint-parity-arbitrage]], [[bill-broking-arbitrage]], [[shipping-certificate-arbitrage]], [[regional-currency-arbitrage]], [[historical-cable-arbitrage]], [[grain-futures-basis-arbitrage]]
  - Historical entities: rothschild-family, baring-brothers, jay-cooke-co, overend-gurney, [[liverpool-cotton-exchange]]
  - Historical context: [[gold-standard-mechanics]], [[telegraph-impact-on-arbitrage]]
  - Crypto / DeFi: [[gbtc-discount-arbitrage]], [[lst-depeg-arbitrage]], [[stablecoin-pair-arbitrage]], [[liquidation-cascade-arbitrage]], [[curve-gauge-wars-arbitrage]], [[vampire-attack-arbitrage]], [[token-unlock-arbitrage]], [[bankruptcy-claim-arbitrage]]
  - Crypto arb history: [[2013-2014-mtgox-premium-arbitrage]], [[2020-09-sushiswap-vampire-attack]], [[2021-08-poly-network-exploit]], [[2021-ohm-ponzi-arbitrage]], [[2021-2022-gbtc-discount]], [[2022-06-steth-depeg]], [[2023-03-usdc-svb-depeg]]
  - Triangular variants: [[triangular-arbitrage]], [[medieval-bill-of-exchange-arbitrage]], [[eurodollar-triangular-arbitrage]], [[crisis-currency-triangular-arbitrage]], [[yen-carry-triangular-arbitrage]], [[crypto-spot-perp-futures-triangle]], [[dex-pool-triangular-arbitrage]]
  - Triangular arb history: [[champagne-fairs]], [[medieval-italian-banking]], [[1992-black-wednesday-erm-crisis]], [[1994-tequila-crisis]]
  - Modern execution-layer: [[intent-based-arbitrage]], [[private-mempool-arbitrage]], [[multi-leg-arbitrage]], [[cross-l2-arbitrage]], [[zkml-predictive-mev]], [[slippage-optimal-pathfinding]], [[mev-burn-economics]]
  - Archegos cluster: [[archegos-blowup-2021]], [[bill-hwang]], [[block-trade-flipping-arbitrage]], [[prime-broker-cascade-trading]], [[total-return-swap]]
  - Distressed / credit: [[distressed-debt-arbitrage]], [[bankruptcy-claim-arbitrage]]
  - Historic triangular FX wins: [[1987-andy-krieger-nzd-short]], [[1998-08-russia-ruble-default]], [[1999-01-brazil-real-devaluation]], [[2001-12-argentina-convertibility-break]], [[2015-01-snb-swiss-franc-unpeg]], [[2018-08-turkish-lira-crisis]], [[2022-09-uk-mini-budget-crisis]], [[2024-08-yen-carry-unwind]]
  - Historic crypto triangular wins: [[2013-04-cyprus-banking-crisis-btc-pump]], [[2017-08-bitcoin-cash-fork-arbitrage]], [[2017-12-cme-bitcoin-futures-launch]], [[2020-03-12-black-thursday-crypto]], [[2022-06-three-arrows-blowup]], [[2022-11-ftx-collapse-arbitrage]]
  - Crypto triangular strategies: [[wrapped-asset-triangular-arbitrage]], [[fork-airdrop-triangulation]], [[restaking-token-arbitrage]]
  - Exotic crypto arb (2024-2025): [[polymarket-prediction-market-arbitrage]], [[pendle-pt-yt-arbitrage]], [[pump-fun-bonding-curve-sniping]], [[uniswap-v4-hooks-arbitrage]], [[velodrome-aerodrome-bribe-arbitrage]], [[bitcoin-runes-brc20-arbitrage]], [[babylon-bitcoin-staking-arbitrage]], [[jito-solana-mev-arbitrage]], [[ai-agent-token-arbitrage]], [[hyperliquid-hlp-basis-arbitrage]]
  - Edge-of-wiki gold: [[sports-betting-arbitrage]], [[matched-betting-arbitrage]], [[parallel-market-currency-arbitrage]]
  - AI-exploit cluster (2026): [[ai-amplified-exploit-arbitrage]], [[post-hack-incident-response-arb]], [[governance-restitution-arbitrage]], [[2026-exploit-target-watchlist]], [[ai-vulnerability-discovery]], [[smart-contract-vulnerability-taxonomy]], [[ai-auditor-arms-race]], [[insurance-as-unreliable-signal]], [[frontier-models-and-crypto-exploits]], [[2026-04-07-claude-mythos-project-glasswing]]
  - AI-exploit derived strategies (2026): [[audit-recency-tvl-growth-short]], [[compound-fork-donation-short]], [[multi-dvn-bridge-config-arbitrage]], [[cross-chain-contagion-hedge]], [[mythos-release-window-exploit-short]]
  - AI-exploit operational playbook: [[exploit-arb-implementation-guide]]
  - April 2026 incident post-mortems: [[2026-04-01-drift-protocol-exploit]], [[2026-04-18-kelp-layerzero-exploit]], [[2026-01-20-makina-finance-exploit]]
  - June 2026 AI-discovered bug: [[2026-06-05-zcash-orchard-counterfeiting-bug]] (Opus 4.8 finds ZEC Orchard counterfeiting flaw; ZEC −38%)
  - Exploit attack-vector concept pages: [[solana-durable-nonce-governance-attacks]], [[rpc-poisoning]], [[dvn-compromise-patterns]], [[donation-attacks]], [[move-clmm-vulnerability-class]]
  - Tier-1 exploit-watchlist protocols: [[jupiter-lend]], [[hyperevm]], [[megaeth]]
  - **Legendary trade case studies (2026 batch):** [[2020-03-ackman-pandemic-cds-trade]] (100× CDS), [[2007-2008-burry-subprime-cds-trade]] (subprime Big Short), [[2006-09-amaranth-natural-gas-blowup]] (Arnold vs Hunter), [[1815-rothschild-waterloo-info-arbitrage]]
  - **Pattern-extraction synthesis:** [[fastest-profitable-trades]] — common architecture across history's largest single trades
  - **Derived strategies from legendary trades:** [[counterparty-stress-arbitrage]] (Arnold framework), [[convex-tail-hedge-arbitrage]] (Ackman/Burry framework), [[information-arbitrage]] (Rothschild→HFT→on-chain framework)
  - **Supporting trader entities (2026 batch):** [[john-arnold]], [[brian-hunter]]
  - Synthetic stablecoin depeg arb (mechanism-specific): [[synthetic-stablecoin-depeg-arbitrage]] (companion to [[stablecoin-pair-arbitrage]])
  - Stablecoin depeg profit-capture playbook: [[stablecoin-depeg-profit-capture]] (7 tactical methods)
  - Stablecoin depeg history & case studies: [[stablecoin-depeg-history]] (master timeline 2014-2026), [[2017-2020-tether-banking-premium]], [[2020-03-dai-black-thursday]], [[2023-02-busd-wind-down]], [[2026-04-kelp-stable-sympathy-depeg]]
  - Rogue-trader / scandal cluster: [[1995-sumitomo-copper-scandal]], [[1991-salomon-treasury-auction-scandal]], [[2008-01-socgen-kerviel-rogue-trade]]
- [[hyperliquid-perp-trading-map|Hyperliquid Perp Trading Map]] — Comprehensive strategy map for trading perpetual futures on Hyperliquid
- [[asterdex-perp-trading-map|AsterDEX Perp Trading Map]] — Strategy map for AsterDEX perps with head-to-head Hyperliquid comparison

- **Strategy-Creation Toolkit (gap-fill, Jul 2026)** — full plan in [[coverage-gaps]]:
  - Idea generation: [[crypto-idea-generation]] (inversion-based hypothesis mining), [[crypto-signal-library]] (signal→endpoint→transform→edge primitive index)
  - Feature engineering: [[feature-engineering-crypto]], [[feature-selection-trading]], [[fractional-differentiation]], [[information-coefficient]], [[signal-orthogonalization]] (BTC-beta neutralisation), [[composite-alpha-blending]]
  - ML labeling & pipeline: [[triple-barrier-labeling]], [[meta-labeling]], [[ml-crypto-price-prediction]]
  - Crypto backtest validation: [[crypto-data-quality]], [[regime-conditional-validation]], [[crypto-short-history-statistical-power]], [[crypto-forward-testing]], [[probability-of-backtest-overfitting]]
  - Execution & sizing: [[cross-venue-execution-crypto]], [[thin-market-execution]], [[funding-aware-position-sizing]], [[liquidation-price-aware-sizing]], [[crypto-portfolio-heat]]
  - Portfolio & live ops: [[multi-strategy-crypto-portfolio]], [[paper-to-live-promotion]], [[bot-kill-switch-design]], [[position-reconciliation]], [[exchange-api-key-security]], [[proof-of-reserves]]
  - New archetypes: [[hyperliquid-market-making]], [[loss-versus-rebalancing]], [[crypto-options-volatility-selling]], [[crypto-options-dispersion]], [[etf-flow-directional]], [[bitcoin-halving-cycle-timing]], [[crypto-beta-rotation]]
  - Rewritten to buildable specs: [[concentrated-liquidity]], [[jit-liquidity]], [[market-making-strategy]], [[mev-strategies]], [[defi-yield-farming]]

### DeFi (Decentralised Finance)
- [[defi|DeFi Hub]] — Core architecture, protocol categories, glossary, strategies, market state, security, regulation
- Key concepts: [[automated-market-maker]], [[defi-lending]], [[impermanent-loss]], [[loss-versus-rebalancing]], [[liquidity-pools]], [[smart-contracts]]
- Strategies: [[defi-yield-farming]], [[mev-strategies]], [[crypto-yield-stack]], [[concentrated-liquidity]], [[jit-liquidity]], [[leveraged-yield-farming]], [[cross-chain-yield-farming]]
- Protocols: [[uniswap]], [[aave]], [[makerdao]], [[lido]], [[hyperliquid]], [[curve-finance]], [[pendle]], [[jupiter-exchange-solana|Jupiter]], [[eigenlayer]], [[beefy-finance]], [[thorchain]], [[alpha-homora]]
- Concepts: [[restaking]]
- Comparisons: [[centralized-vs-decentralized-finance]], [[cefi-yield-vs-defi-yield]]
- Security: [[defi-hacks-and-exploits]], [[smart-contract-vulnerability-taxonomy]], [[ai-vulnerability-discovery]], [[ai-auditor-arms-race]], [[insurance-as-unreliable-signal]]

#### Low-Cap Crypto / Memecoin Trading
- Master playbook: [[low-cap-crypto-trading-map|Low-Cap Crypto Trading Map]] — Solana memecoin meta strategy stack
- Strategies: [[memecoin-sniping]], [[sniping]], [[pump-fun-bonding-curve-sniping]], [[token-migration-sniping]], [[jito-bundle-sniping]], [[telegram-bot-trading]], [[on-chain-smart-money-tracking]]
- Sniper bots / terminals: [[axiom-pro|Axiom]], [[bonkbot]], [[trojan-bot|Trojan]], [[maestro-bot|Maestro]], [[banana-gun]], [[photon-sol|Photon]], [[gmgn|GMGN]], [[bullx|BullX]]
- Launchpads: [[pump-fun|Pump.fun]], [[letsbonk|LetsBonk.fun]], [[believe|Believe]], [[moonshot|Moonshot]], [[heaven-launchpad|Heaven]], [[sunpump|SunPump]] (TRON)
- Launchpad comparison: [[pump-fun-vs-letsbonk-vs-believe-vs-moonshot-vs-heaven|Pump.fun vs LetsBonk vs Believe vs Moonshot vs Heaven]]
- Venues: [[pump-fun]], [[pumpswap]], [[raydium]], [[jupiter-exchange-solana|Jupiter]]
- Concepts: [[bonding-curve-analysis]], [[market-cap-level-trading]]
- Risk frameworks: [[rug-detection-checklist]], [[holder-concentration-analysis]], [[rug-pulls]]
- Analytics: [[birdeye]], [[dex-screener]], [[gmgn]], [[bitquery]], [[dune-analytics]]

### Crypto Narrative Impact (Backtester Catalog)
- [[crypto-narratives-overview|Crypto Narratives Overview]] — **Backtester-ready catalog**: 19 narrative categories, 69 archetypes, 290 quantified historical instances mapping world/market narratives → crypto price impact. Machine-readable JSON at `wiki/crypto-narratives/catalog/all-narratives.json`.
- [[narratives-by-direction|Narratives by Direction]] — master index of every narrative grouped 🟢 bullish / 🔴 bearish / ⚪ neutral (types + the full 290-event list by realized move)
- [[narrative-signals|Narrative Signals (operational)]] — **for the trading system**: per-narrative detection conditions, move-probability priors, live PM strategy gates, and point-in-time backtester gates. Machine-readable: `catalog/narrative-signals.json`
- Supply & flows: [[token-unlocks]], [[stablecoin-supply]], [[whale-onchain-flows]]
- Cycle & technicals: [[bitcoin-halving]], [[technical-signals]], [[bitcoin-dominance-rotation]]
- Capital & institutions: [[corporate-treasury]], [[spot-etf-flows]], [[macro-events]]
- Regulation: [[regulatory-bans]], [[regulatory-approvals-policy]]
- Risk events: [[exchange-collapses]], [[stablecoin-depegs]], [[hacks-exploits]]
- Sector rotations: [[memecoin-mania]], [[ai-agent-tokens]], [[defi-narratives]], [[l1-l2-rotation]], [[platform-launches]]

### Concepts
- [[concepts-overview|Concepts Overview]] — Risk Management, Portfolio Theory, Market Microstructure, Indicators
- **Core Trading Concepts (plain-English explainers)**:
  - Risk & portfolio: [[risk-reward-ratio]], [[risk-tolerance]], [[calmar-ratio]], [[covariance]], [[expectancy]], [[downside-deviation]], [[treynor-ratio]], [[information-ratio]], [[risk-free-rate]], [[fama-french-three-factor-model]], [[win-rate]], [[tracking-error]]
  - Behavioral finance: [[fomo]], [[sunk-cost-fallacy]], [[recency-bias]], [[gamblers-fallacy]], [[base-rate-neglect]]
  - Technical & strategy: [[overbought-oversold]], [[trendline]], [[gap-trading]], [[pullback-trading]], [[accumulation-distribution]], [[double-top]], [[pivot-points]], [[wedge]], [[advance-decline-line]], [[doji]], [[neckline]], [[measured-move]], [[whipsaw]], [[seasonality]], [[reversal-patterns]]
  - Macro: [[equity-risk-premium]], [[bond-yields-and-stock-prices]], [[inflation-and-stocks]]
  - Market mechanics: [[market-hours]], [[primary-vs-secondary-market]], [[expense-ratio]], [[day-trading-vs-swing-trading-vs-position-trading]]
- **Crypto Market Regimes** — [[crypto-market-regime-taxonomy|14-Basket Regime Taxonomy]] (Hyperliquid-native). Baskets: [[macro-trend-regime]], [[bitcoin-cycle-regime]], [[meme-speculative-regime]], [[derivatives-native-regime]], [[event-catalyst-regime]], [[crypto-macro-correlation-regime]], [[on-chain-regime]], [[basis-carry-regime]], [[liquidity-depth-regime]], [[institutional-flow-regime]], [[security-black-swan-regime]], [[policy-shock-regime]], [[volatility-regime-classification]], [[technical-structural-regime]]. Playbook: [[regime-strategy-playbook|Regime → Strategy Playbook]]. See also [[regime-matrix]], [[market-regime-detection-ml]], [[regime-adaptive-strategy]]
- Arbitrage Execution: [[leg-risk|Leg Risk]], [[execution-sequencing|Execution Sequencing]], [[crowding-indicators|Crowding Indicators]]
- Arbitrage Operations: [[arbitrage-parameter-cheatsheet|Arb Parameter Cheatsheet]], [[multi-venue-capital-management|Multi-Venue Capital Management]]
- Compliance: [[regulatory-risk-map|Regulatory Risk Map]], [[tax-implications-trading|Tax Implications]]
- Live Data: [[arbitrage-live-performance|Arb Performance Tracker]], [[arbitrage-seasonality|Arb Seasonality]], [[arbitrage-competitive-landscape|Competitive Landscape]]
- Portfolio: [[arbitrage-correlation-matrix|Arb Correlation Matrix]]
- DeFi Execution: [[defi-contract-registry|DeFi Contract Registry]], [[mev-execution-guide|MEV Execution Guide]], [[gas-fees|Gas Fees]]
- Implementation: [[arbitrage-monitoring-setup|Monitoring Setup (Code)]], [[arbitrage-backtesting-guide|Arb Backtesting Guide]], [[arbitrage-worked-examples|Worked Examples]]
- [[options-overview|Options Trading]] — Greeks, volatility surface, pricing, 70+ strategy and concept pages
  - New: [[credit-spread]], [[iron-butterfly]], [[gamma-scalping]], [[delta-hedging]], [[vega-hedging]]
- [[macroeconomics|Macroeconomics Hub]] — Monetary Policy, Fiscal Policy, GDP, Employment, Inflation, Credit Cycles, Currency Dynamics
- [[backtesting-overview|Backtesting]] — Validation, costs, performance metrics
  - Backtesting methods: [[vectorized-backtesting]], [[event-driven-backtesting]], [[trading-system-deployment]]
  - Backtesting frameworks: [[backtrader-framework|Backtrader]], [[vectorbt|VectorBT]], [[zipline-framework|Zipline]], [[backtesting-py|Backtesting.py]], [[pybroker|PyBroker]], [[quantconnect|QuantConnect]], [[pyalgotrade|PyAlgoTrade]]
  - Validation & overfitting: [[in-sample-vs-out-of-sample]], [[walk-forward-analysis]], [[purged-kfold-cv]], [[overfitting]], [[overfitting-detection]], [[deflated-sharpe-ratio]]
  - Optimization: [[optuna|Optuna]], [[optimization-objectives]], [[execution-model-differences]]
  - Low-timeframe (1m/3m/5m/15m): [[bar-resolution-selection]], [[intrabar-fill-modeling]], [[microstructure-noise-low-timeframe]], [[multiple-timeframe-analysis]], [[overfitting]]
  - Analytics: [[pyfolio]], [[quantstats|QuantStats]]
  - Market-making: [[hummingbot|Hummingbot]]
  - Crypto-perp pitfalls: [[crypto-perp-backtesting-pitfalls]], [[hyperliquid-backtesting]], [[auto-deleveraging]], [[liquidation-cascade-modeling]], [[point-in-time-data]], [[market-regime-detection-ml]], [[2025-10-crypto-liquidation-cascade]]
- [[anomalies-overview|Market Anomalies]] — Library of documented inefficiencies
- Technical Analysis Foundations: [[dow-theory]], [[intermarket-analysis]], [[multiple-timeframe-analysis]], [[sector-rotation]]
- Technical Indicators: [[indicators-overview|Indicators Overview]], [[rsi]], [[macd]], [[bollinger-bands]], [[ichimoku]], [[donchian-channels]], [[williams-percent-r]], [[aroon]], [[chaikin-money-flow]], [[money-flow-index]], [[mcclellan-oscillator]], [[arms-index]], [[point-and-figure]]
- Crisis Alpha & Tail Risk: [[crisis-alpha]], [[convexity]], [[dragon-portfolio]], [[trend-plus-tail-hedge]], [[tail-risk-hedging]], [[asymmetric-barbell]]
- Dealer flow & gamma: [[gamma-exposure]] (GEX + gamma-flip + crypto-perp/liquidation analog & data spec, Jun 2026), [[dealer-gamma-hedging]], [[gamma-squeeze]], [[options-pinning]], [[max-pain]]
- Options market-structure cluster:
  - Vol products: [[vix-options]], [[vix-futures]], [[variance-swap]], [[variance-swaps]]
  - Settlement/microstructure: [[assignment-risk]], [[options-pinning]], [[liquidity-evaporation]], [[clob]]
  - Deep dives: [[max-pain]], [[gamma-exposure]]
- Options-Risk-Budgeting cluster (gap-fill, May 2026):
  - Hub: [[options-risk-budgeting]]
  - Higher-order Greeks: [[beta-weighted-delta]], [[gamma-pnl]], [[volga]], [[vol-of-vol]], [[non-linear-payoff]]
  - Options structures: [[long-call]], [[long-put]], [[vix-call]], [[long-dated-options]], [[interest-rate-options]]
  - Vol concepts: [[correlation-regime]], [[volatility-spike]], [[vol-regime-detection]], [[skew]] (disambig hub)
  - Hedging/scenario: [[book-dynamic-hedging]], [[scenario-analysis]], [[historical-stress-test]], earnings-announcement
  - Factors: [[low-vol-factor]], [[momentum-factor]], [[size-factor]], [[value-factor]]
  - Stub upgrade: [[risk-off]] (full rewrite)
- Theta-Targeting cluster (gap-fill, May 2026):
  - Hub: [[theta-targeting]]
  - Decay/time metrics: [[time-to-expiration]], [[theta-decay-curve]], [[theta-realisation-ratio]], [[gamma-to-theta-ratio]], [[gamma-explosion]]
  - Vol regimes: [[volatility-regime]], [[volatility-regime-switching]], [[volatility-term-structure]], [[volatility-risk-premium-decay]]
  - Foundations: [[black-scholes-model]], [[options-buying-power-reduction]], [[probability-of-touch]]
  - Strategy structures: [[strangle]], [[iron-fly]], [[zero-dte-options]], [[managing-winners]]
  - Macro: [[fomc-meetings]], [[diversification-in-options]]
  - Tooling: [[optionnet-explorer]], [[deribit-position-builder]], [[tastytrade-platform]]
  - Stub upgrades: [[expected-shortfall]] (full rewrite), [[pin-risk]] (full rewrite), [[options-income]] (full rewrite)
- Crypto Intraday Session Liquidity cluster (gap-fill, May 2026):
  - Sessions framework: [[crypto-trading-sessions]] (hub — Asia/London/NY/LNY overlap), [[session-overlap-liquidity]], [[crypto-weekday-weekend-etf-era]] (ETF-era extension of [[btc-weekend-effect]])
  - Derivatives intraday: [[funding-by-hour]] (intraday cadence companion to [[funding-rate]]), [[spot-vs-derivatives-volume-ratio]] (regime indicator)
  - Strategy: [[session-overlap-momentum]] (fades failed late-Asia breakouts into the LNY overlap)
  - Institutional anchors: [[coinbase-prime]], [[cme-bitcoin-futures]]
  - Flow data sources: [[whale-alert]], [[token-unlocks]]
- Long-Vol vs Short-Vol cluster (gap-fill, May 2026):
  - Master comparison: [[long-vol-vs-short-vol]]
  - Strategy pages: [[long-volatility-strategies]], [[short-volatility-strategies]], [[options-premium-selling]] (full rewrite), [[premium-selling-systematic]], [[long-vol-overlay]], [[short-put-spread]], [[tastytrade-mechanics]]
  - Funds: [[ljm-preservation-and-growth]], [[longtail-alpha]], [[saba-capital-tail-fund]], [[malachite-capital]], [[catalyst-hedged-futures]], [[xiv-velocity-shares]]
  - Vol-shock events: [[volmageddon]], [[vix-august-2024-spike]], [[covid-crash]], [[black-monday]], [[gfc]], [[long-term-capital-management]]
  - Instruments: [[variance-swaps]], [[vix-futures]], [[span-margin]]
  - Stats / risk concepts: [[negative-skew]], [[gaussian-assumption]], [[sharpe-ratio-pitfalls]], [[ergodicity-economics]], [[geometric-mean]], [[ole-peters]]
  - Microstructure / behavioral: [[gap-risk]], [[liquidity-provider]], [[dopamine-loop]]
  - Source summary: [[safe-haven-spitznagel]]
- Options Pitfalls / TradeStation / Selection cluster (gap-fill, May 2026):
  - Pitfalls: [[options-trading-pitfalls]], [[iv-crush]], [[pin-risk]], [[options-trader-psychology]]
  - TradeStation: [[easylanguage]], [[optionstation-pro]], [[tradestation-options-workflow]]
  - How to pick options: [[options-selection-framework]], [[strike-selection]], [[expiration-selection]], [[options-liquidity-screening]], [[moneyness-selection]]
  - Resolved broken wikilinks: [[straddle]], [[hedging-program-failure-modes]]
- AI Labor & Macro Risk (2025-2026):
  - Foundational cascade: [[ai-layoff-trap]], [[citrini-2028-global-intelligence-crisis]], [[ai-driven-demand-destruction]], [[service-sector-multiplier]], [[capital-vs-labor-asymmetry]], [[skill-bifurcation]], [[wage-compression-vs-job-loss]]
  - Sector/regional: [[tech-hub-concentration-risk]], [[stranded-office-real-estate]], [[junior-analyst-stranding]], [[legal-services-ai-disruption]], [[skilled-trades-wage-boom]], [[ai-data-center-power-demand]]
  - Macro/finance: [[solow-paradox-2026]], [[productivity-j-curve]], [[esrb-ai-systemic-risk-channels]]
  - Policy: [[pigouvian-automation-tax]]
- Behavioral Finance (Taleb cluster): [[survivorship-bias]], [[narrative-fallacy]], [[ergodicity]], [[outcome-bias]], [[hindsight-bias]], [[signal-vs-noise]]
- Behavioral Finance (cognitive biases): [[prospect-theory]], [[loss-aversion]], [[overconfidence-bias]], [[confirmation-bias]], [[anchoring-bias]], [[disposition-effect]], [[herding]]
- Market Microstructure: [[order-flow]], [[absorption]], [[volume-imbalance]], [[footprint-chart]], [[market-profile]], [[volume-profile]]
- Crypto flow & execution signals: [[coinbase-premium]] (US-institutional demand gauge), [[participation-rate]] (POV execution cap)
- FX Microstructure: [[last-look]] (dealer rejection protocol), [[cross-currency-basis-swap]] (CIP deviation / funding-stress signal), [[covered-interest-rate-parity]] (no-arbitrage FX/rates condition), [[settlement-risk]] (Herstatt / principal risk)
- NFT Microstructure: [[nft-rarity-scoring]], [[nft-floor-price]], [[nft-aggregators]], [[nft-royalty-enforcement]], [[phygital-nfts]]
- NFT Risk: [[nft-lending]]
- Hyperliquid On-Chain CLOB cluster (gap-fill, Jun 2026):
  - Protocol primitives: [[hypercore]], [[hyperbft]], [[hip-3-builder-deployed-perps]], [[hlp]]
  - Order-book microstructure & economics: [[hyperliquid-order-book-microstructure]], [[hyperliquid-fee-tiers-and-maker-rebates]], [[hyperliquid-margining-modes]], [[latency-and-mev-on-chain-clob]]
  - Strategy & data/tools: [[hyperliquid-market-making]] (on-chain CLOB be-the-maker; CEX complement [[market-making-strategy]]), [[perp-dex-aggregation]], [[hyperliquid-api-and-sdk]], [[level-4-order-book-data]]
  - Comparable on-chain CLOB: [[econia]] (Aptos)
  - Upgrades: [[hyperevm]] (draft→good), [[orderly-network]] (draft→good)
  - Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]
- Crypto Execution & Perp Sizing cluster (Jul 2026):
  - Execution: [[cross-venue-execution-crypto]] (route a directional order across Binance/Bybit/OKX/Hyperliquid by depth, fee tier, funding), [[thin-market-execution]] (illiquid alt books: depth-sized children, participation caps, iceberg/TWAP), [[smart-order-routing]] (+ crypto-venue routing section)
  - Perp sizing: [[funding-aware-position-sizing]] (funding-adjusted Kelly), [[liquidation-price-aware-sizing]] (size beyond a named-wick stress move)
  - Portfolio-level: [[crypto-portfolio-heat]] (beta-weighted BTC exposure budgeting), [[multi-strategy-crypto-portfolio]] (perp-carry + momentum + on-chain + memecoin sleeves in one book)

### Data Sources
- [[data-sources-overview|Data Sources]] — Free, paid, alternative, crypto, options, macro, news data providers
- [[cryptodataapi|CryptoDataAPI]] — **Canonical data layer for this wiki**: 190+ endpoints for prices, funding, OI, liquidations, regimes, on-chain, sentiment, whale tracking, and backtesting archives
- [[exchange-api-reference|Exchange API Reference]] — Normalized API endpoints for arbitrage across Binance, Coinbase, Hyperliquid, OKX, Bybit, Kraken
- [[historical-spread-data|Historical Spread Data]] — Funding rate, basis, cross-exchange spread, and IV surface data sources for arb backtesting
- [[alternative-me|Alternative.me]] — Crypto Fear & Greed Index (0-100 sentiment gauge, free API)
- [[cryptoquant|CryptoQuant]] — On-chain analytics: exchange flows, whale tracking, SOPR, miner metrics
- [[glassnode|Glassnode]] — On-chain macro indicators: SOPR, MVRV, NUPL, HODL waves, LTH/STH supply
- [[nansen|Nansen]] — Wallet-labeled on-chain analytics; Smart Money cohorts; Polymarket whale tracking
- [[coinglass|Coinglass]] — Derivatives aggregator: funding rates, open interest, liquidations across 25+ venues
- [[token-terminal|Token Terminal]] — Protocol revenue, P/E ratios, fees, yield sustainability metrics
- [[dune-analytics|Dune Analytics]] — Community SQL-based blockchain analytics and dashboards
- [[zapper|Zapper]] — DeFi portfolio tracker and yield aggregator across 30+ chains
- AI/Labor Macro: [[ibkr-forecast-trader|IBKR Forecast Trader]] (recession probability prediction market), [[bls-benchmark-revisions|BLS Benchmark Revisions]] (real labor truth vs reported), [[randstad-job-postings|Randstad Job Postings]] (skilled-trades demand), [[skillit-construction-wages|Skillit Construction Wages]] (data-center labor pricing)

### History
- [[history-overview|History Overview]] — Crashes, Bull/Bear Markets, Notable Trades, Market Evolution
- [[defi-hacks-and-exploits|DeFi Hacks & Exploits]] — $8B+ in exploits: DAO hack, bridge exploits, flash loans, oracle manipulation, rug pulls
- [[flash-crashes|Flash Crashes Hub]] — 2010, 2015 ETF, 2016 GBP, Volmageddon, Crypto Cascades, Market Manipulation

### Entities
- [[entities-overview|Entities Overview]] — Traders, Hedge Funds, Exchanges, Regulators, Protocols
- Technical Analysis Pioneers: [[j-welles-wilder]], [[gerald-appel]], [[john-bollinger]], [[goichi-hosoda]], [[george-lane]], [[larry-williams]], [[donald-lambert]], [[tushar-chande]], [[ralph-nelson-elliott]], [[robert-prechter]], [[munehisa-homma]], [[chester-keltner]], [[sherman-mcclellan]], [[marc-chaikin]], [[joseph-granville]], [[richard-arms]]
- Options Educators & Platforms: [[tom-sosnoff]], tastytrade, optionalpha, optionstrat
- Trading Platforms: [[thinkorswim]], [[ninjatrader]], [[sierra-chart]]
- Tail Risk Practitioners: [[mark-spitznagel]], [[universa-investments]], [[nassim-taleb]]
- Behavioral Finance Pioneers: [[daniel-kahneman]], [[richard-thaler]]
- Market Microstructure Pioneers: [[peter-steidlmayer]]
- Market Makers & HFT: citadel-securities, [[jane-street]], [[jump-trading]]
- Derivatives Exchanges: [[cme-group]]
- Blockchain Security: [[openzeppelin|OpenZeppelin]], [[halborn|Halborn]], [[zellic|Zellic]]
- Blockchain Infrastructure: [[chainstack|Chainstack]]
- Threat Actors: [[lazarus-group|Lazarus Group]]
- Forex/CFD Brokers: oanda, fxcm
- Forex Market Infrastructure: CLS Group (PvP settlement), [[lmax-exchange|LMAX Exchange]] (no-last-look venue), FXall (LSEG RFQ), cTrader (ECN/algo platform), MetaTrader (dominant retail platform), [[dukascopy|Dukascopy]] (historical FX data)
- Social Networks: Meta (Facebook), youtube, tiktok, X (Twitter), [[reddit]], discord, linkedin, Snapchat, pinterest, spotify
- AI Frontier & Research: [[anthropic|Anthropic]] (Claude builder, $380B valuation Feb 2026), [[openai|OpenAI]] (GPT family, capped-profit, MSFT partnership), Citrini Research (publisher of "2028 Global Intelligence Crisis" scenario)
- AI Labor Trap economists: [[brett-hemenway-falk]], [[gerry-tsoukalas]] (Wharton/BU, "AI Layoff Trap" mathematical model)
- Macroprudential regulators: [[esrb|European Systemic Risk Board]] (Dec 2025 AI systemic risk report)

### Artificial Intelligence
- [[artificial-intelligence|Artificial Intelligence]] — AI Companies, Agent Frameworks, DeFAI, AI Narrative

### AI & Trading Technology
- [[ai-trading-overview|AI Trading Overview]] — ML Models, Trading Bots, Backtesting, Data Providers
- Trading Platforms (Order Flow): [[sierra-chart]], [[ninjatrader]], [[atas-platform|ATAS]]
- Trading Platforms (Options): [[thinkorswim]]
- Trading Bots: [[composer-trade|Composer]], [[traderspost|TradersPost]], [[freqtrade]], [[hummingbot]]
- AI Options Trading: [[generative-ai-options-trading|Generative AI for Options Trading]] — LLM copilots, structuring agents, risk narration, surveillance
- ML Pricing: [[deep-learning-option-pricing|Deep Learning for Option Pricing]] — neural surrogates, deep hedging, ML-driven vol surfaces
- Algorithmic options market makers: Optiver, HRT, SIG, IMC, [[drw|DRW]]
- LLMs for Finance: [[claude]], [[gpt-4]], [[llama-fin|Llama-Fin]] — domain-adaptive 8B financial LLM
- AI Companies (LLM/Agent platforms): [[anthropic]], [[openai]], google, [[xai]]
- ML Models (2026 frontier): [[xlstm-ts|xLSTM-TS]] — direction prediction; [[graph-neural-networks-finance|GNNs in Finance]] — cross-asset relationships; [[federated-learning-aml|Federated Learning for AML]]
- Quant Methodology: [[causal-inference-finance|Causal Inference in Finance]] — causal forests, DML; Earnings Surprise Prediction — multimodal LLMs

### Options Concepts
- [[iv-rank-and-iv-percentile|IV Rank & IV Percentile]] — Measuring whether options are cheap or expensive
- [[probability-of-profit|Probability of Profit (PoP)]] — Central premium-selling metric: how brokers compute it, how to use it, its limits
- [[spread-width-selection|Spread Width Selection]] — Sizing the wings on credit spreads and iron condors
- [[put-options|Put Options]] — Comprehensive treatment: anatomy, Greeks, strategies, common mistakes
- [[sabr-model|SABR Volatility Model]] — Stochastic-alpha-beta-rho; industry-standard smile model
- [[unusual-options-activity|Unusual Options Activity]] — Flow-tracking signal; informed-flow detection
- [[order-flow-imbalance|Order Flow Imbalance (OFI)]] — Microstructure short-horizon price predictor

### News & Events
- [[news-overview|News & Events]] — Verified market-moving news and events
- AI Recession Watch (2026): [[2026-03-bls-900k-jobs-revision]]
- AI Finance Push (2026): [[2026-anthropic-blackstone-jv]], [[2026-anthropic-finance-agents-launch]], [[2026-claude-opus-4-7-finance-benchmark]], [[2026-chatgpt-mainstream-adoption]]
- DeFi Infrastructure (2026): [[2026-uniswap-v4-launch]]

### Education
- [[education-overview|Education Overview]] — Books (40 titles), Courses, Resources

### Prediction Markets
- [[prediction-markets|Prediction Markets]] — Concept: event-outcome trading, wisdom of crowds, platform comparison
- [[polymarket|Polymarket]] — Largest decentralized prediction market ($9B valuation, Polygon/USDC)
- [[kalshi|Kalshi]] — CFTC-regulated centralized prediction exchange (~$2B valuation)
- [[predictit|PredictIt]] — CFTC-regulated US political prediction market with $850/user cap
- [[manifold-markets|Manifold Markets]] — Play-money prediction market (mana); leading sentiment indicator
- [[augur|Augur]] — OG decentralized prediction market on Ethereum (REP); largely dormant since 2020
- [[metaculus|Metaculus]] — Non-profit forecasting platform (reputation-based, not real-money); calibration benchmark
- [[polymarket-vs-kalshi|Polymarket vs Kalshi]] — Head-to-head comparison
- [[prediction-market-strategies|Prediction Market Strategies]] — Arbitrage, bias fading, information edge, whale tracking
- [[polymarket-as-crypto-leading-indicator|Polymarket as a Crypto Leading Indicator]] — Using PM event-resolution odds as a signal for spot/perp crypto positioning
- [[prediction-market-calibration|Prediction Market Calibration]] — Brier scores, reliability diagrams, leading-indicator backtest methodology
- [[lmsr|Logarithmic Market Scoring Rule]] — Hanson AMM mechanism underlying Manifold/Augur; why Polymarket chose CLOB instead
- [[oracle-disputes|Oracle Disputes]] — Challenging UMA resolutions; risk and trading strategy
- [[resolution-risk-hedging|Resolution Risk Hedging]] — Hedging prediction-market positions pre-resolution
- [[polymarket-api|Polymarket API]] — Official CLOB/Gamma/WebSocket data and trading APIs
- [[the-block|The Block]] — Crypto research and data terminal with prediction-market coverage
- [[shayne-coplan|Shayne Coplan]] — Polymarket founder

### Comparisons
- [[comparisons-overview|Comparisons]] — Side-by-side analysis of strategies, tools, markets

### Crypto Miners & Treasury Companies
- [[hive-digital-technologies|HIVE Digital Technologies (HIVE)]] — Nordic renewable HPC-pivot miner
- [[microstrategy]] — Largest corporate bitcoin treasury; see [[mstr-bitcoin-treasury-premium-unwind-short]]
- Miners: [[mara]], [[riot-platforms]], [[cleanspark]], [[core-scientific]], [[cipher-mining]], [[bitfarms]], [[hut-8]], [[iren]], [[terawulf]], [[bitdeer-technologies]], [[bit-digital]]

### Funds & Investors
- [[leopold-aschenbrenner|Leopold Aschenbrenner]] — *Situational Awareness* essay author; AI-scaling-thesis hedge fund manager
- [[situational-awareness-lp|Situational Awareness LP]] — ~$13.7B AUM AI-thesis hedge fund; bifurcated long-physical-infra / short-semis-puts structure

### Tax (Australia)
- [[itaa-1997-overview|ITAA 1997 Overview]] — Trading-relevant provisions of the Income Tax Assessment Act 1997
- [[non-commercial-losses-div-35|Non-Commercial Losses (Division 35)]] — Loss-deferral rule, four exception tests, $250k income gate
- [[tr-97-11-carrying-on-a-business|TR 97/11 — Carrying On a Business]] — Eight-indicator test for business vs investment classification
- [[trader-vs-investor-classification-au|Trader vs Investor Classification (AU)]] — Practical guide to revenue vs capital account
- [[commissioners-discretion-s-35-55|Commissioner's Discretion (s 35-55)]] — Escape hatch when Div 35 tests fail
- [[pcg-2021-2-div-35-discretion|PCG 2021/2 — Div 35 Discretion]] — Commissioner's practical approach to s 35-55
- [[smsf-trading-tax-treatment|SMSF Trading Tax Treatment]] — How SMSFs are taxed on trading; sole purpose test; loss handling
- [[lost-or-stolen-crypto-au-tax|Lost or Stolen Crypto — AU Tax]] — CGT event C1/C2 for crypto, ATO evidence requirements, lost vs stolen distinction
- [[self-custody-tax-evidence-checklist|Self-Custody Tax-Evidence Checklist]] — Pre-loss documentation framework for cold-storage holders
- Pre-existing: [[australian-investor-tax]], [[capital-gains-tax-discount]], [[tax-efficient-investing]], [[tax-loss-harvesting-australia]], [[cryptocurrency-tax-australia]], [[stage-3-tax-cuts]]

### Sources
- [[sources-overview|Source Summaries]] — Summaries of all ingested sources

---

## Quick Stats

```dataview
TABLE length(rows) as "Pages"
FROM "wiki"
WHERE type != "index" AND type != "overview"
GROUP BY type
```

## Recently Updated

```dataview
TABLE title, status, updated
FROM "wiki"
WHERE type != "index"
SORT updated DESC
LIMIT 20
```

## Stubs to Expand

```dataview
TABLE title, tags
FROM "wiki"
WHERE status = "stub"
SORT created DESC
```
