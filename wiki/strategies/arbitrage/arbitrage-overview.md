---
title: "Arbitrage"
type: index
created: 2026-04-06
updated: 2026-06-20
status: excellent
tags: [arbitrage, strategies, index]
aliases: ["Arbitrage Strategies", "Arb Hub", "Arbitrage Index"]
related: ["[[arbitrage]]", "[[relative-value-arbitrage]]", "[[risk-arbitrage]]", "[[limits-to-arbitrage]]", "[[statistical-arbitrage]]", "[[merger-arbitrage]]", "[[funding-rate-arbitrage]]", "[[cross-exchange-arbitrage]]", "[[volatility-arbitrage]]", "[[arbitrage-monitoring-setup]]", "[[arbitrage-worked-examples]]", "[[arbitrage-parameter-cheatsheet]]"]
---

# Arbitrage

Strategies exploiting price discrepancies across markets, exchanges, or instruments.

Arbitrage is the closest thing to "free money" in trading -- buying an asset where it is cheap and simultaneously selling where it is expensive, locking in a risk-free profit. In practice, true risk-free arbitrage is rare and fleeting, so most arbitrage strategies involve some residual risk (execution, counterparty, regulatory). The best opportunities arise in fragmented markets with multiple venues, which is why crypto -- with hundreds of exchanges and DeFi protocols -- is an arbitrage-rich environment.

For the theoretical foundation of arbitrage, see [[arbitrage|Arbitrage (Concept)]]. For real-world examples of arb mechanisms breaking down, see [[2020-03-bond-etf-dislocation]], [[2022-05-terra-luna-depeg-arb]], and [[2017-2021-kimchi-premium]].

## How to Use This Hub

This page is the **master index** for every arbitrage strategy in the wiki. It is organized into four layers, navigate by what you need:

| If you want to... | Go to |
|---|---|
| Understand the theory | [[arbitrage\|Arbitrage (Concept)]], [[limits-to-arbitrage]], [[law-of-one-price]] |
| Browse strategies by category | [[#Comprehensive Arbitrage Taxonomy]] (below) |
| Compare risk / return / capital | [[#Risk / Return / Capital Comparison]] |
| Pick a starting point by skill level | [[#Start Here by Experience Level]] |
| Build the operational stack | [[#Arbitrage Operations & Execution]] → [[arbitrage-monitoring-setup]] |
| See dated, costed example trades | [[arbitrage-worked-examples]] |
| Learn from failures | [[#Notable Arb Failures and Lessons]] |

The deepest companion operational pages are: [[arbitrage-monitoring-setup]] (runnable monitoring code), [[arbitrage-worked-examples]] (dated, costed trades), [[arbitrage-parameter-cheatsheet]] (entry/exit thresholds), and [[arbitrage-backtesting-guide]] (simulation pitfalls).

## Why Arbitrage Persists (and Why It Pays)

If arbitrage were truly free and instantaneous, every gap would close before it could be traded. In reality, gaps persist because **[[limits-to-arbitrage]]** prevent capital from flowing instantly to close them. Understanding *which* limit holds a given gap open tells you whether an "arb" is real edge or a trap:

| Limit to arbitrage | What it is | Strategies it sustains |
|---|---|---|
| **Execution / latency** | Speed gap between seeing and trading | [[cross-exchange-arbitrage]], [[triangular-arbitrage]], [[latency-arbitrage]], [[mev-strategies]] |
| **Capital / funding** | Need balance sheet to hold both legs to convergence | [[cash-and-carry]], [[basis-trading]], [[relative-value-arbitrage]], [[convertible-arbitrage]] |
| **Counterparty / settlement** | Risk one leg fails to deliver | [[funding-rate-arbitrage]], [[cross-chain-arbitrage]], OTC [[merger-arbitrage]] |
| **Regulatory / capital controls** | Capital cannot move across the gap | [[2017-2021-kimchi-premium]], [[gbtc-discount-arbitrage]], [[regulatory-arbitrage]] |
| **Model / convergence risk** | Mean-reversion may not happen on your horizon | [[statistical-arbitrage]], [[pairs-trading]], [[capital-structure-arbitrage]] |
| **Event / deal risk** | Catalyst may not resolve as expected | [[merger-arbitrage]], [[spac-arbitrage]], [[risk-arbitrage]] |

The single most important lesson of arbitrage history (LTCM 1998, the [[2020-03-bond-etf-dislocation|March 2020 ETF dislocation]], the [[2022-05-terra-luna-depeg-arb|Terra/LUNA]] collapse): **the residual risk that keeps a gap open is exactly the risk that detonates the trade in a crisis**. The leg you thought was a hedge becomes the loss. See [[leg-risk]] and [[limits-to-arbitrage]].

## Comprehensive Arbitrage Taxonomy

Every arbitrage strategy in this wiki, organized by category:

### Pure / Deterministic Arbitrage

Strategies where profit is locked in at execution with minimal residual risk.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[cross-exchange-arbitrage]] | Buy on one exchange, sell on another at a higher price | Crypto, FX |
| [[triangular-arbitrage]] | Exploit circular mispricing across three pairs (e.g., BTC/USD, ETH/BTC, ETH/USD) | Crypto, FX |
| [[cash-and-carry]] | Buy spot, sell futures at a premium; collect the basis | Crypto, commodities |
| [[box-spread]] | Combine bull and bear spreads to lock in risk-free rate | Options |
| [[etf-arbitrage]] | Exploit ETF price vs NAV discrepancy via creation/redemption | Equities, bonds |
| [[put-call-parity-arbitrage]] | Exploit violations of C − P = S − Ke^(-rt) in options | Options |
| [[covered-interest-arbitrage]] | Borrow low-rate currency, convert spot, invest abroad, lock forward | FX |

### Funding & Carry Arbitrage

Strategies that earn yield from structural rate differentials while hedging directional exposure.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[funding-rate-arbitrage]] | Long spot / short perps to collect funding payments | Crypto |
| [[basis-trading]] | Exploit spot-futures basis across venues and expirations | Crypto, commodities |
| [[carry-trade]] | Borrow in low-rate currency, invest in high-rate currency | FX, bonds |
| [[staking-yield-arbitrage]] | Earn staking yield while hedging token price risk | Crypto |
| [[calendar-spread]] | Exploit mispricing between near and far-dated contracts | Options, futures |
| [[calendar-spread-arbitrage]] | Pure arbitrage variant exploiting calendar spread mispricings | Options, futures |

### Statistical & Quantitative Arbitrage

Model-driven strategies that exploit probabilistic mean-reversion, not deterministic mispricings.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[statistical-arbitrage]] | Quantitative models on correlated asset divergence | Equities, crypto |
| [[pairs-trading]] | Long one asset, short a correlated peer; bet on convergence | Equities, crypto |
| [[mean-reversion]] | Bet that prices revert to historical averages | All markets |
| [[ornstein-uhlenbeck]] | Model mean-reverting processes for optimal entry/exit | Quant |
| [[long-short-equity]] | Factor-neutral portfolio exploiting relative value | Equities |

### Volatility & Options Arbitrage

Strategies that exploit mispricings in implied vs realized volatility or options structures.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[volatility-arbitrage]] | Trade implied vol vs realized vol divergence | Options |
| [[gamma-scalping]] | Delta-hedge options to capture gamma as realized vol | Options |
| [[dispersion-trading]] | Short index vol, long single-stock vol (or vice versa) | Options |
| [[convertible-arbitrage]] | Long convertible bonds, short underlying equity | Equities, bonds |

### Event-Driven Arbitrage (a.k.a. [[risk-arbitrage|Risk Arbitrage]])

Strategies where the arb opportunity is created by a corporate event or structural catalyst. See [[risk-arbitrage]] for the full taxonomy.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[merger-arbitrage]] | Buy target, short acquirer; bet on deal completion | Equities |
| [[tender-offer-arbitrage]] | Buy shares and tender above market; proration risk | Equities |
| [[spac-arbitrage]] | Buy SPAC below trust value; redeem at trust or ride deal | Equities |
| [[rights-issue-arbitrage]] | Arbitrage discount between rights, new shares, and stock | Equities |
| [[warrant-arbitrage]] | Trade warrants vs underlying equity / call options | Equities |
| [[event-driven-trading]] | Trade around earnings, spin-offs, regulatory decisions | Equities |
| [[dividend-capture]] | Capture dividend payments with hedged positions | Equities |
| [[corporate-action-arbitrage]] | Exploit mispricings around corporate actions (spin-offs, splits, tender offers) | Equities |
| [[dividend-arbitrage]] | Exploit dividend-related mispricings in options or equities | Equities |

### Fixed Income / Relative Value Arbitrage

Classical bond-market arbitrages — LTCM's playbook. Umbrella page: [[relative-value-arbitrage]].

| Strategy | Description | Market |
|----------|-------------|--------|
| [[on-off-the-run-treasury-arbitrage]] | Exploit liquidity premium between newly-issued and seasoned Treasuries | Rates |
| [[swap-spread-arbitrage]] | Trade the spread between interest rate swaps and matched-maturity Treasuries | Rates |
| [[tips-treasury-arbitrage]] | Trade TIPS (inflation-linked) vs nominal Treasuries — breakeven inflation | Rates |
| [[mbs-basis-arbitrage]] | Trade MBS vs Treasuries/swaps hedged for duration and convexity | Mortgages |
| [[cds-bond-basis-arbitrage]] | Long cash bond + buy CDS protection — the negative basis trade | Credit |
| [[capital-structure-arbitrage]] | Trade equity vs debt of same issuer using Merton-model linkage | Equities, credit |

### Cross-Listing / NAV Arbitrage

Strategies exploiting the same economic claim trading at different prices in different wrappers or venues.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[dual-listed-company-arbitrage]] | Royal Dutch/Shell, BHP, Unilever — two listings, one cash flow | Equities |
| [[adr-arbitrage]] | American Depository Receipts vs underlying foreign shares | Equities |
| [[closed-end-fund-arbitrage]] | Trade CEFs against NAV; activist discount-narrowing plays | Equities |

### Macro / Currency Arbitrage

Macro-scale arbitrages around pegs, bimetallic ratios, and central-bank commitments.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[currency-peg-break-arbitrage]] | Bet against defensible pegs — ERM 1992, baht 1997, CHF floor 2015 | FX |
| [[gold-silver-ratio-arbitrage]] | Trade gold/silver ratio at extremes; historical bimetallism | Commodities |

### Classical / Historical Arbitrage (pre-1914 to Bretton Woods)

Strategies from the gold-standard era — the ancestors of modern arb. Context: [[gold-standard-mechanics]], [[telegraph-impact-on-arbitrage]], [[champagne-fairs]], [[medieval-italian-banking]].

| Strategy | Description | Market |
|----------|-------------|--------|
| [[medieval-bill-of-exchange-arbitrage]] | Triangular arb via bills of exchange across [[champagne-fairs|Champagne]] and [[lyon-fairs|Lyon]] fairs (12th-16th c) | FX |
| [[gold-point-arbitrage]] | Ship bullion between mints when FX rate breaches gold points; dominated by [[rothschild-family]] | FX, bullion |
| [[specie-flow-arbitrage]] | Run ahead of Hume's price-specie-flow mechanism during trade-balance adjustment | FX, macro |
| [[mint-parity-arbitrage]] | Exploit slow-moving deviations from mint parity within the gold points band | FX |
| [[shipping-certificate-arbitrage]] | Cash vs futures grain/cotton at CBOT and [[liverpool-cotton-exchange]] 1860s-1920s | Commodities |
| [[bill-broking-arbitrage]] | Pre-modern money market arb — London vs provincial discount rates ([[overend-gurney]], Bagehot) | Money market |
| [[regional-currency-arbitrage]] | Wildcat-era US state bank notes traded at discounts; Suffolk System, Thompson's reporters | Notes, FX |
| [[historical-cable-arbitrage]] | 1920s-30s pound-dollar-franc triangle via transatlantic cable; ancestor of [[latency-arbitrage]] | FX |
| [[grain-futures-basis-arbitrage]] | Early CBOT cash-futures basis; Harper 1866, Leiter 1888, Hutchinson 1897 corners | Commodities |
| [[eurodollar-triangular-arbitrage]] | Reg Q + UK exchange controls created NY-London-Zurich triangle (1957-1986) | FX, money market |

### Triangular Arbitrage Variants

The triangle in different eras and asset classes — see [[triangular-arbitrage]] for the canonical FX statement.

| Variant | Description | Market |
|---------|-------------|--------|
| [[triangular-arbitrage]] | Canonical FX three-leg cycle (e.g. USD-EUR-JPY) | FX |
| [[medieval-bill-of-exchange-arbitrage]] | Cross-fair bill triangulation (12th-16th c) | FX |
| [[historical-cable-arbitrage]] | Transatlantic cable era 1920s-30s | FX |
| [[eurodollar-triangular-arbitrage]] | Reg Q gap + cross-currency hedge 1960s-80s | FX, money market |
| [[crisis-currency-triangular-arbitrage]] | Triangle dislocations during peg breaks (ERM 1992, Asia 1997) | FX |
| [[yen-carry-triangular-arbitrage]] | JPY-USD-AUD/NZD/MXN — modern $1-4T carry industry | FX, bonds |
| [[crypto-spot-perp-futures-triangle]] | Three crypto wrappers of the same underlying | Crypto |
| [[dex-pool-triangular-arbitrage]] | On-chain cyclic AMM arb via [[mev-strategies]] / [[flash-loan-arbitrage]] | DeFi |
| [[multi-leg-arbitrage]] | Generalization to 4, 5, 6+ leg cycles across fragmented liquidity | DeFi |
| [[cross-l2-arbitrage]] | Same asset across Arbitrum/Optimism/Base/zkSync — shared L1, fast bridges | DeFi, L2 |

### Modern Execution-Layer Arbitrage (Intents, Private OFAs, ZK)

Arbitrage strategies built around the post-2023 shift from public mempool to private order-flow auctions, intent-based settlement, and verifiable off-chain computation.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[intent-based-arbitrage]] | Solver-side fills on CoW / UniswapX / 1inch Fusion — CoW match + path arb + cycle arb | DeFi |
| [[private-mempool-arbitrage]] | Backruns via Flashbots Protect / MEV-Share with user kickback | DeFi |
| [[zkml-predictive-mev]] | ML predictions verified on-chain via ZK proofs; conditional MEV bundles | DeFi |
| [[slippage-optimal-pathfinding]] | Methodology: closed-form + iterative routing across mixed AMMs (concept) | DeFi |
| [[mev-burn-economics]] | Concept page — how MEV-Burn EIPs reshape arb economics (concept) | DeFi |

### Tax / Regulatory Arbitrage (including historical frauds)

> Warning: some strategies here are illegal. Documented for historical context.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[regulatory-arbitrage]] | Exploit jurisdictional differences in regulation | All |
| [[cum-ex-dividend-stripping]] | Multi-claim dividend tax refund fraud (illegal — €55B+ European scandal) | Equities |

### Commodity & Energy Arbitrage

Strategies exploiting structural relationships in physical commodity markets.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[crack-spread]] | Trade crude oil vs refined products (gasoline, diesel) | Energy |
| [[crush-spread]] | Trade soybeans vs soybean meal and soybean oil | Agriculture |
| [[spark-spread]] | Trade natural gas vs electricity | Energy |
| [[seasonal-spread-trading]] | Exploit recurring seasonal patterns in commodity spreads | Commodities |

### Crypto-Native Arbitrage

Strategies unique to the blockchain and DeFi ecosystem.

| Strategy | Description | Market |
|----------|-------------|--------|
| [[cross-exchange-arbitrage]] | Price gaps across centralized exchanges (CEXs) | Crypto |
| [[cross-chain-arbitrage]] | Exploit price differences for the same token across different blockchains (L1s, L2s) via bridges | Crypto, DeFi |
| [[mev-strategies]] | Maximal Extractable Value -- front-running, sandwich attacks, liquidations | DeFi |
| [[defi-yield-farming]] | Exploit yield differentials across DeFi protocols | DeFi |
| [[airdrop-farming]] | Earn token distributions by using protocols pre-launch | Crypto |
| [[liquidity-sniping]] | Front-run new token listings for early liquidity advantage | Crypto |
| [[regulatory-arbitrage]] | Exploit jurisdictional differences in crypto regulation | Crypto |
| [[flash-loan-arbitrage]] | Atomic arbitrage using uncollateralized flash loans in DeFi | DeFi |
| [[nft-arbitrage]] | Exploit price discrepancies across NFT marketplaces | Crypto |
| [[leveraged-etf-rebalancing]] | Exploit predictable rebalancing flows in leveraged ETFs | Equities |
| [[gbtc-discount-arbitrage]] | Grayscale trust premium (2017-2021) → discount (2021-2024) arb | Crypto, ETF |
| [[lst-depeg-arbitrage]] | stETH/rETH/cbETH exit-queue depeg trades (June 2022 +6.5% spread) | Crypto, staking |
| [[stablecoin-pair-arbitrage]] | USDC/USDT/DAI spreads around depeg events (SVB March 2023) | Crypto, stables |
| [[liquidation-cascade-arbitrage]] | Front-run / follow liquidations on Aave, Compound, MakerDAO, Liquity | DeFi |
| [[curve-gauge-wars-arbitrage]] | veCRV / vlCVX bribe farming via Votium, Hidden Hand | DeFi, governance |
| [[vampire-attack-arbitrage]] | Farm forked protocol rewards during LP migration (SushiSwap, Blur) | DeFi |
| [[token-unlock-arbitrage]] | Short VC/team cliff unlocks; post-unlock mean reversion | Crypto |
| [[bankruptcy-claim-arbitrage]] | Trade Mt. Gox / FTX / Celsius / Voyager claims at OTC discount | Crypto, distressed |
| [[ai-amplified-exploit-arbitrage]] | Hub strategy for trading AI-driven smart-contract exploits (incident-response → governance-vote → restitution) | Crypto, DeFi |
| [[post-hack-incident-response-arb]] | 0-72h post-disclosure playbook: DEX-CEX dislocation, LST/stable depeg overshoot, perp funding fade | Crypto, DeFi |
| [[governance-restitution-arbitrage]] | Days-to-weeks post-hack: governance-vote arb on frozen-IOUs + OTC restitution-claim arb + bridge-token-discount arb | Crypto, DeFi |
| [[audit-recency-tvl-growth-short]] | Systematic short on protocols with stale audits + rising TVL; quantitative basket | Crypto, DeFi |
| [[compound-fork-donation-short]] | Recurring donation-attack pattern in Compound v2 forks; narrow but reliable cohort short | Crypto, DeFi |
| [[multi-dvn-bridge-config-arbitrage]] | Pair trade: long multi-verifier bridges / short 1-of-1 DVN apps; KelpDAO precedent | Crypto, DeFi |
| [[cross-chain-contagion-hedge]] | Cheap-to-carry tail-risk hedge basket sized to 50× contagion multiplier (KelpDAO ref) | Crypto, DeFi |
| [[synthetic-stablecoin-depeg-arbitrage]] | Mechanism-aware depeg arb on sUSDe / GHO / crvUSD / FRAX / Ethena white-labels + sympathy depegs from contagion events | Crypto, DeFi |
| [[stablecoin-depeg-profit-capture]] | Tactical profit-maximization playbook: 7 capture methods (spot / redemption arb / pair / leveraged borrow / AMM-band / overshoot short / options) with P&L worked examples | Crypto, DeFi |

## Arbitrage by Edge Source

Mapping the taxonomy onto the [[edge-taxonomy|five edge sources]] clarifies *what you are actually being paid for* and where the edge decays first:

| Edge source | Mechanism | Representative arbs | Decay driver |
|---|---|---|---|
| **Latency / structural speed** | Be first to the gap | [[cross-exchange-arbitrage]], [[triangular-arbitrage]], [[latency-arbitrage]], [[mev-strategies]], [[flash-loan-arbitrage]] | Faster competitors, co-location, private order flow |
| **Risk-bearing / carry** | Get paid to hold a hedged position to convergence | [[cash-and-carry]], [[funding-rate-arbitrage]], [[basis-trading]], [[merger-arbitrage]], [[convertible-arbitrage]] | More capital chasing the same carry |
| **Informational / analytical** | Model relationships others misprice | [[statistical-arbitrage]], [[pairs-trading]], [[capital-structure-arbitrage]], [[volatility-arbitrage]], [[dispersion-trading]] | Crowding, factor commoditization |
| **Structural / segmentation** | Same claim trapped in different wrappers/venues | [[etf-arbitrage]], [[adr-arbitrage]], [[dual-listed-company-arbitrage]], [[closed-end-fund-arbitrage]], [[gbtc-discount-arbitrage]] | Wrapper convergence, ETF conversion |
| **Regulatory / jurisdictional** | Exploit rules that block capital flow | [[regulatory-arbitrage]], [[2017-2021-kimchi-premium\|capital-control premia]], [[covered-interest-arbitrage]] | Rule changes, controls lifted |

For the full framework see [[edge-taxonomy]]; for why these edges survive at all, [[limits-to-arbitrage]].

## Risk / Return / Capital Comparison

> **Note on returns:** The figures below are *illustrative orders of magnitude* drawn from general market knowledge, not guaranteed or backtested results. Realised returns depend heavily on fee tier, capital scale, latency, and regime. Always cross-check against [[arbitrage-live-performance]] and [[arbitrage-worked-examples]] before sizing real capital.

| Strategy | Risk Level | Expected Return | Capital Required | Time Horizon | Complexity |
|----------|-----------|----------------|-----------------|-------------|-----------|
| [[cross-exchange-arbitrage]] | Low | 0.1-2% per trade | Medium | Seconds-minutes | Medium |
| [[cross-chain-arbitrage]] | Medium | 0.1-1% per trade | Medium-High | Seconds-minutes | High |
| [[triangular-arbitrage]] | Low | 0.01-0.5% per loop | Medium-High | Seconds | High |
| [[cash-and-carry]] | Low | 5-25% APR | High | Days-months | Low |
| [[funding-rate-arbitrage]] | Low-Med | 10-40% APR | Medium | Days-weeks | Medium |
| [[pairs-trading]] | Medium | 5-15% annual | Medium | Days-weeks | High |
| [[statistical-arbitrage]] | Medium | 10-30% annual | High | Hours-days | Very High |
| [[merger-arbitrage]] | Medium | 5-15% annualized | High | Weeks-months | Medium |
| [[volatility-arbitrage]] | Medium-High | Variable | High | Days-weeks | Very High |
| [[convertible-arbitrage]] | Medium | 6-12% annual | Very High | Weeks-months | High |
| [[mev-strategies]] | Medium-High | Variable (high) | Low-Medium | Blocks | Very High |
| [[defi-yield-farming]] | High | Variable | Medium | Days-months | Medium |

## Start Here by Experience Level

### Beginner -- Learn the Foundations

Start with strategies that have clear mechanics and lower complexity:

1. **[[cash-and-carry]]** -- The simplest arb to understand. Buy spot, sell futures, earn the basis. Start here.
2. **[[funding-rate-arbitrage]]** -- The most popular retail arb in crypto. Long spot, short perps, collect funding.
3. **[[cross-exchange-arbitrage]]** -- Conceptually simple (buy low, sell high across exchanges), though execution requires infrastructure.
4. **[[arbitrage]]** (concept) -- Understand the theoretical foundation before deploying capital.

### Intermediate -- Add Complexity and Edge

Once you understand the basics, expand to strategies with more moving parts:

5. **[[triangular-arbitrage]]** -- Requires speed and precision but teaches you about market microstructure.
6. **[[pairs-trading]]** -- Your entry point into statistical arbitrage; learn cointegration and z-scores.
7. **[[merger-arbitrage]]** -- Event-driven arb that requires fundamental analysis skills.
8. **[[basis-trading]]** -- Multi-leg trades across expirations and venues.
9. **[[crack-spread]]** / **[[crush-spread]]** -- Commodity arbs that teach you about structural relationships.

### Advanced -- Quantitative and Structural Edge Required

These strategies require significant infrastructure, capital, or quantitative skill:

10. **[[statistical-arbitrage]]** -- Full quant models, factor analysis, and portfolio construction.
11. **[[volatility-arbitrage]]** / **[[gamma-scalping]]** -- Deep options knowledge and Greeks management.
12. **[[convertible-arbitrage]]** -- Complex multi-asset hedging across equity and credit.
13. **[[mev-strategies]]** -- Requires blockchain engineering, mempool analysis, and Solidity/smart contract skills.
14. **[[dispersion-trading]]** -- Correlation trading with sophisticated vol surface analysis.

## Arbitrage Operations & Execution

Resources for moving from strategy understanding to live deployment:

| Page | Focus |
|------|-------|
| [[arbitrage-parameter-cheatsheet]] | Concrete entry/exit thresholds by strategy with costs baked in |
| [[exchange-api-reference]] | Normalized API endpoints, WebSocket feeds, rate limits across major exchanges |
| [[leg-risk]] | The #1 operational risk in arb: one leg fills, the other doesn't |
| [[execution-sequencing]] | Which leg first, order types, partial fill handling, unwind logic |
| [[multi-venue-capital-management]] | Capital pre-positioning, rebalancing, inventory management across exchanges |
| [[historical-spread-data]] | Where to find funding rate, basis, and spread time series for backtesting |
| [[strategy-monitoring]] | Dashboard design, alert thresholds, kill criteria operationalization |
| [[crowding-indicators]] | How to measure strategy crowding quantitatively — OI ratios, spread compression, AUM-to-volume |
| [[regulatory-risk-map]] | Which strategies are legal where, KYC requirements, compliance mapping |
| [[tax-implications-trading]] | Tax profiles by strategy type — wash sales, Section 1256, DeFi taxable events |
| [[arbitrage-live-performance]] | Current strategy viability — observed returns, Sharpe decay, what's alive vs. dead |
| [[arbitrage-seasonality]] | When strategies are most/least profitable — funding rate cycles, FOMC calendar, M&A clustering |
| [[arbitrage-competitive-landscape]] | Who competes in each arb niche, infrastructure moats, can retail compete? |
| [[arbitrage-correlation-matrix]] | How arb strategies correlate — normal vs. crisis, effective bets, portfolio construction |
| [[defi-contract-registry]] | Smart contract addresses for flash loans, DEX routers, bridges, staking — per chain |
| [[mev-execution-guide]] | Flashbots bundle construction, gas bidding, MEV protection, mempool monitoring |
| [[arbitrage-monitoring-setup]] | Runnable Python code: Telegram alerts, funding monitor, position reconciliation, Grafana dashboard |
| [[arbitrage-worked-examples]] | Dated real-world trades with specific prices, fees, and P&L — funding arb, cross-exchange, merger, flash loan, stETH |
| [[arbitrage-backtesting-guide]] | Seven deadly sins of arb backtesting, multi-leg simulation framework, Python code skeleton |

## Notable Arb Failures and Lessons

Understanding when arbitrage breaks is as important as understanding when it works:

- **[[2020-03-bond-etf-dislocation]]** -- Bond ETF arb mechanism failed during COVID crash (March 2020)
- **[[2022-05-terra-luna-depeg-arb]]** -- Algorithmic stablecoin arb became a $40B death spiral (May 2022)
- **[[2017-2021-kimchi-premium]]** -- 40% crypto premium persisted for months due to capital controls
- **[[2020-2024-bridge-exploits]]** -- $2.5B+ lost to bridge hacks; systemic risk for [[cross-chain-arbitrage]] strategies
- **[[2021-2022-gbtc-discount]]** — Premium → discount flip; -49% at Dec 2022 bottom; closed Jan 2024 with ETF conversion
- **[[2022-06-steth-depeg]]** — stETH to 0.9346 ETH June 13, 2022; 3AC/Celsius forced selling
- **[[2023-03-usdc-svb-depeg]]** — USDC to $0.88 over SVB weekend; Fed/Treasury backstop repegged within days
- **[[2013-2014-mtgox-premium-arbitrage]]** — Mt. Gox premium → discount → collapse Feb 2014; 10-year claim arb pays out 2024
- **[[2020-09-sushiswap-vampire-attack]]** — Forked Uniswap, drained $1B LP, kicked off DeFi Summer
- **[[2021-08-poly-network-exploit]]** — $611M bridge hack RETURNED by "Mr White Hat"; set template for 2022 bridge hack wave
- **[[2021-ohm-ponzi-arbitrage]]** — Olympus DAO (3,3) reflexive Ponzi; $1,415 peak → fork collapse revealed Sifu/Patryn/QuadrigaCX past

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/strategies/arbitrage"
WHERE type != "index"
SORT updated DESC
```

## Related

- [[arbitrage]] — the theoretical concept (law of one price, no-arbitrage pricing)
- [[limits-to-arbitrage]] — why gaps persist; the residual risk that pays you
- [[relative-value-arbitrage]] — umbrella for fixed-income / RV arbs (the LTCM playbook)
- [[risk-arbitrage]] — umbrella for event-driven / merger arbs
- [[statistical-arbitrage]] — model-driven mean-reversion arbs
- [[edge-taxonomy]] — the five edge sources mapped above
- [[leg-risk]] — the #1 operational arb risk (one leg fills, the other doesn't)
- [[arbitrage-monitoring-setup]] — runnable monitoring stack
- [[arbitrage-worked-examples]] — dated, costed example trades
- [[arbitrage-parameter-cheatsheet]] — concrete entry/exit thresholds
- [[arbitrage-backtesting-guide]] — simulation pitfalls

## Sources

General market knowledge; no specific wiki source ingested yet. Return and capital figures in the comparison tables are illustrative orders of magnitude — verify against [[arbitrage-live-performance]], [[arbitrage-worked-examples]], and the individual strategy pages before deploying capital.
