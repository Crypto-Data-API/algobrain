---
title: "Ethereum"
type: entity
created: 2026-04-06
updated: 2026-06-20
status: excellent
tags: [crypto, defi, ethereum, markets]
aliases: ["ETH", "Ether"]
entity_type: protocol
founded: 2015
headquarters: "Decentralized"
website: "https://ethereum.org"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[defi]]", "[[smart-contracts]]", "[[solana]]", "[[proof-of-stake]]", "[[staking]]"]
---

# Ethereum

**Ethereum** (ETH) is the second-largest [[crypto-markets|cryptocurrency]] by market capitalization and the most widely used programmable [[blockchain]]. Conceived by **Vitalik Buterin** in 2013 and launched in July 2015, Ethereum extended [[bitcoin|Bitcoin's]] innovation by introducing [[smart-contracts]] -- self-executing programs that run on a decentralized virtual machine. This made Ethereum the foundation of the entire [[defi|decentralized finance (DeFi)]] ecosystem, NFTs, [[stablecoins]], and thousands of tokens and protocols.

Ethereum is often described as the "world computer" -- a global, permissionless platform for deploying applications that run exactly as programmed without downtime, censorship, or third-party interference.

---

## Market Data

| Metric | Value |
|---|---|
| **Rank** | #2 |
| **Price** | $1,722.91 |
| **Market Cap** | $207.96 billion |
| **24h Volume** | $6.99 billion |
| **24h Change** | +1.53% |
| **7d Change** | +2.82% |
| **Circulating Supply** | 120,683,936 ETH |
| **Total Supply** | 120,683,936 ETH |
| **Max Supply** | None (uncapped; net issuance governed by burn vs staking rewards) |
| **All-Time High** | $4,946.05 (2025-08-24) — currently -65.2% |
| **All-Time Low** | $0.4330 (2015-10-20) — currently +397,820% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** The [[crypto-market-sentiment|Fear & Greed Index]] reads **22 (Extreme Fear)** in an **Established Bear Market**. ETH trades ~65% below its August 2025 ATH — a deeper drawdown than [[bitcoin|BTC]] (-50%), reflecting ETH's higher beta. The [[ethereum#ETH/BTC Ratio|ETH/BTC ratio]] near these levels (~0.027) is historically compressed, a level long-term rotation traders watch for mean reversion.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ETH |
| **Creator** | Vitalik Buterin (co-founders incl. Gavin Wood, Joseph Lubin) |
| **Launch** | July 30, 2015 |
| **Consensus** | [[proof-of-stake]] (since September 2022, "The Merge") |
| **Supply** | No hard cap; net deflationary under high usage via [[#EIP-1559 & the Burn|EIP-1559 burn]] |
| **Block Time** | ~12 seconds |
| **Virtual Machine** | Ethereum Virtual Machine (EVM) |
| **Validator stake** | 32 ETH (or liquid [[staking]] via Lido/Rocket Pool) |
| **Staking Yield** | ~3-5% APR |
| **Website** | [ethereum.org](https://ethereum.org) |

---

## Technology & Consensus

### Smart Contracts & the EVM

At its core, Ethereum is a state machine. The **Ethereum Virtual Machine (EVM)** executes [[smart-contracts]] written in Solidity or Vyper, encoding arbitrary logic from simple token transfers to complex [[defi]] protocols ([[uniswap|DEXs]], [[aave|lending]], [[perpetual-futures|derivatives]]). The EVM is the de facto standard for blockchain development: competing chains ([[bnb|BNB Chain]], [[arbitrum|Arbitrum]], [[polygon|Polygon]], Avalanche) are "EVM-compatible," letting developers redeploy the same code.

### The Merge -- Proof of Stake

On **September 15, 2022**, Ethereum completed "The Merge," moving from [[proof-of-work]] to [[proof-of-stake]]:

- **Energy reduction**: ~99.95% decrease in consumption
- **Validator model**: stake 32 ETH to run a validator, or use liquid [[staking]] (Lido stETH, Rocket Pool rETH)
- **Block production**: validators propose and attest rather than mine
- **Yield**: ~3-5% APR from issuance, priority fees, and MEV

The Merge ended Ethereum mining entirely. A miner-led coalition forked the PoW chain into [[ethereum-pow-iou|Ethereum PoW (ETHW)]], producing one of crypto's largest pre-fork derivative markets -- see [[2022-09-ethereum-merge-fork-arbitrage]] for the canonical [[fork-airdrop-triangulation|fork-arbitrage]] case study.

### The Rollup-Centric Roadmap

Ethereum's base layer processes ~15-30 TPS -- insufficient for mass scale. The roadmap pushes execution to **Layer 2 (L2) rollups** that batch transactions off-chain and post proofs/data to L1 for security. The **Dencun** upgrade (March 2024) introduced **proto-danksharding (EIP-4844 "blobs")**, slashing L2 data-availability costs and dramatically cheapening rollup transactions. Subsequent upgrades (Pectra and beyond) continue raising blob throughput and validator/UX efficiency.

| L2 | Type | Key detail |
|---|---|---|
| **[[arbitrum\|Arbitrum]]** | Optimistic rollup | Largest L2 by TVL; home to [[gmx\|GMX]] and much DeFi |
| **Optimism** | Optimistic rollup | OP Stack / Superchain |
| **Base** | Optimistic rollup (OP Stack) | Built by [[coinbase\|Coinbase]]; major consumer onboarding ramp |
| **zkSync** | ZK rollup | Validity-proof scaling |
| **Starknet** | ZK rollup (STARK) | Cairo-based contracts |

L2 proliferation fragments [[liquidity]] but collapses transaction costs. The trade-off: ETH burn (and thus its deflationary pressure) shifts from L1 to cheaper L2 blob fees, a key valuation debate.

---

## Tokenomics & Supply Schedule

ETH has **no fixed cap**. Net issuance is the balance of two forces: new ETH paid to validators (issuance) minus ETH destroyed by the [[#EIP-1559 & the Burn|EIP-1559 base-fee burn]].

### EIP-1559 & the Burn

Implemented August 2021, **EIP-1559** restructured fees: a **base fee** that is **burned** (permanently destroyed) on every transaction, plus an optional **priority tip**. When network usage is high, the burn can exceed issuance, making ETH **net deflationary** -- the "ultrasound money" thesis. When usage is low (or migrates to L2 blobs), issuance outpaces burn and supply mildly inflates, as has been the case during quieter periods post-Dencun.

### Staking & the Float

- ~30%+ of ETH supply is staked (figure varies); staked ETH is illiquid float, reducing sell-side liquidity.
- **Liquid staking tokens (LSTs)** -- stETH (Lido), rETH (Rocket Pool) -- re-mobilize staked ETH as collateral across [[defi]], creating reflexive leverage and a key systemic dependency (Lido's dominant share is a centralization concern).
- The **staking ratio** is a core valuation input: higher staking = lower liquid float + higher "risk-free" crypto yield benchmark.

### The "Triple-Point" Asset Thesis

ETH is characterized as a "triple-point" asset that is simultaneously a:

1. **Capital asset** — generates [[staking]] yield (~3-5% APR)
2. **Consumable/commodity** — burned as gas for every transaction
3. **Store of value** — net-deflationary supply under high usage

This differentiates ETH from [[bitcoin|BTC]] (pure store of value) and most other cryptoassets.

---

## Ecosystem & Use Cases

Ethereum is the birthplace and home of [[defi|decentralized finance]]; the majority of DeFi innovation originated here, and ETH/stETH are the ecosystem's base collateral.

| Category | Notable protocols |
|---|---|
| **DEXs** | [[uniswap\|Uniswap]], Curve, Balancer |
| **Lending** | [[aave\|Aave]], Compound, Sky (ex-MakerDAO) |
| **Derivatives** | [[dydx\|dYdX]], Synthetix, [[gmx\|GMX]] (on Arbitrum) |
| **Liquid staking** | Lido (stETH), Rocket Pool (rETH), EigenLayer (restaking) |
| **Stablecoins** | USDC ([[coinbase\|Circle]]), USDT ([[tether\|Tether]]), DAI/USDS |
| **Bridges/aggregators** | 1inch, Across, Stargate |

Total value locked (TVL) across Ethereum-based [[defi]] has historically ranged from ~$20B to over $100B -- still the largest of any chain. **Restaking** (EigenLayer) and **real-world-asset (RWA) tokenization** are the dominant newer growth narratives.

---

## Market Structure & Derivatives

| Characteristic | Detail |
|---|---|
| **Rank** | #2 (behind [[bitcoin\|BTC]]) |
| **Liquidity** | Extremely high; second only to BTC |
| **Volatility** | ~1.2-1.5x BTC's annualized vol |
| **Correlation** | ~0.8+ with BTC, with DeFi-narrative alpha |
| **Primary spot pairs** | ETH/USDT ([[binance]]), ETH/USD ([[coinbase]], Kraken) |
| **Primary perp** | ETH-PERP ([[hyperliquid]]) + all major CEX perp venues |

### Spot Ethereum ETFs

US spot **Ethereum ETFs** launched in mid-2024 (issuers including BlackRock **ETHA**, Fidelity, Grayscale). Early products lacked **staking** yield; the staking question (whether issuers can pass through staking rewards) is the key structural catalyst that would close ETH ETFs' yield disadvantage versus direct holding. As with [[bitcoin-etfs|BTC ETFs]], daily net flows are a short-term directional tell; in the current Extreme-Fear regime, alt-ETF flows tend to be muted. *(Flow magnitudes vary daily and are not quoted here to avoid stale figures.)*

### Perpetuals, Funding & Basis

ETH-PERP is the second-highest-volume perp after BTC. ETH [[funding-rate|funding rates]] tend to be **more volatile** than BTC's, creating more frequent [[basis-trade|basis]]/[[arbitrage]] opportunities. [[open-interest]] and [[liquidation]] maps on ETH perps are essential for [[risk-management]] given ETH's higher beta. The **ETH staking yield** acts as a benchmark "risk-free rate" that anchors DeFi lending rates and influences cash-and-carry basis economics.

### ETH/BTC Ratio

The **ETH/BTC ratio** is one of crypto's most watched metrics:

- **Rising ETH/BTC** — risk-on; confidence in smart-contract platforms; potential "alt season"
- **Falling ETH/BTC** — risk-off rotation to BTC; competitive concern vs [[solana|Solana]] and L1/L2 rivals

Historically ~0.01-0.08; the current compressed reading (~0.027) sits in the lower band, a zone rotation traders flag for potential mean reversion.

---

## On-chain & Valuation Frameworks

These describe the metrics; live values are not invented here.

| Metric | What it measures | Trading use |
|---|---|---|
| **Net issuance (burn vs reward)** | Whether ETH is inflating or deflating | Tracks "ultrasound money" thesis health |
| **Fee/burn revenue** | Base fees burned (L1 + blob demand) | Proxy for organic demand/usage |
| **Staking ratio** | % of supply staked | Liquid-float scarcity + yield benchmark |
| **L2 activity** | Tx/TVL on [[arbitrum\|Arbitrum]], Base, Optimism | Ecosystem health & future L1 blob demand |
| **DEX/stablecoin flows** | On-chain economic throughput | Leading indicator for ETH demand |
| **MVRV / realized cap** | Aggregate cost basis vs market cap | Cyclical value zones (as for [[bitcoin\|BTC]]) |

---

## Trading Playbook

- **ETH/BTC pair** — the foundational relative-value/macro barometer; long ETH/BTC into alt-season, fade into risk-off.
- **Burn & issuance regime** — net-deflationary periods (high L1 usage) support the bull thesis; persistent net issuance (post-Dencun lull) is a bear input.
- **Funding/basis** — ETH funding is more volatile than BTC; harvest [[basis-trade|cash-and-carry]] in high-funding regimes; fade extremes.
- **L2 catalysts** — major upgrades (Dencun, Pectra) and L2 metrics catalyze moves; watch blob-fee demand.
- **ETF staking catalyst** — approval of staked ETH ETFs would be a structural re-rating event.
- **Regime sizing** — in the current bear/extreme-fear regime, ETH's higher beta means larger drawdowns than BTC; size accordingly.

---

## History & Cycles

| Date | Event |
|---|---|
| 2013 | Vitalik Buterin publishes the Ethereum whitepaper |
| Jul 2015 | Mainnet launch (Frontier); ICO raised ~$18M |
| 2016 | The DAO hack → contentious fork (ETH vs Ethereum Classic) |
| 2017 | ICO boom; first ETH bull cycle (~$1,400 peak Jan 2018) |
| 2020-21 | DeFi Summer + NFT boom; ETH to ~$4,800 |
| Aug 2021 | London hard fork → EIP-1559 burn |
| Sep 2022 | The Merge → [[proof-of-stake]] |
| Mar 2024 | Dencun (EIP-4844 blobs) cheapens L2s |
| 2024 | US spot ETH ETFs launch |
| Aug 2025 | All-time high $4,946 |
| Jun 2026 | $1,723 — deep bear drawdown (~-65% from ATH) |

---

## Competitive Positioning

ETH competes with other smart-contract platforms ("ETH killers") and, via the ETH/BTC trade, with [[bitcoin|BTC]] for crypto capital.

| Asset | Rank | Mkt Cap | Consensus | Core thesis |
|---|---|---|---|---|
| **Ethereum (ETH)** | #2 | $208B | [[proof-of-stake]] | Programmable settlement + L2 ecosystem; "ultrasound money" |
| [[bitcoin\|Bitcoin (BTC)]] | #1 | $1.27T | [[proof-of-work]] | Digital gold |
| [[solana\|Solana (SOL)]] | #7 | $41.5B | PoH + [[proof-of-stake\|PoS]] | Monolithic high-throughput L1 |
| [[cardano\|Cardano (ADA)]] | #18 | $6.1B | Ouroboros [[proof-of-stake\|PoS]] | Research-driven L1 |
| [[polkadot\|Polkadot (DOT)]] | #51 | $1.63B | NPoS | Layer-0 multichain interop |

> Peer market data as of 2026-06-20 (CoinGecko). The **monolithic vs modular** scaling debate ([[solana|SOL]] vs ETH+L2s) is the central altcoin-L1 narrative. See [[bitcoin-vs-ethereum]].

---

## Regulatory

- **US**: ETH's security-vs-commodity status has been a long-running question; the launch of CFTC-regulated ETH futures and SEC-approved spot ETFs effectively treats ETH as a commodity-like product for ETF purposes, though staking-as-a-service has drawn SEC scrutiny.
- **Staking**: pass-through staking in ETFs and centralized staking products remain the primary regulatory frontier.
- **EU**: MiCA covers ETH-related service providers; stablecoins on Ethereum face specific MiCA stablecoin rules.

---

## Risks

- **Competition** — faster/cheaper L1s ([[solana|SOL]]) and L2 fragmentation can erode L1 fee capture and the burn thesis.
- **L2 value leakage** — if economic activity (and burn) migrates to cheap L2 blobs, ETH's deflationary mechanism weakens.
- **Centralization** — Lido's dominant liquid-staking share and validator/client concentration are systemic concerns.
- **Smart-contract & bridge risk** — DeFi exploits and cross-chain bridge hacks remain recurring loss events.
- **Beta/leverage** — higher volatility than BTC; sharper [[liquidation]] cascades in drawdowns (current regime).
- **Regulatory** — staking-as-a-service classification risk.

> **Risk warning:** Crypto assets are highly volatile and speculative. Nothing here is investment advice. ETH's higher beta means larger drawdowns than BTC in the current Extreme-Fear / bear regime.

---

## Related

- [[bitcoin]] -- Largest crypto; the BTC/ETH relative-value trade
- [[solana]] -- High-throughput competitor L1 (monolithic vs modular)
- [[cardano]] / [[polkadot]] -- Other smart-contract / interop L1 peers
- [[defi]] -- Decentralized finance, built primarily on Ethereum
- [[smart-contracts]] -- The primitive that powers the ecosystem
- [[proof-of-stake]] / [[staking]] -- Ethereum's consensus and yield
- [[arbitrum]] -- Leading Ethereum L2
- [[stablecoins]] / [[tether]] -- Major on-chain settlement assets
- [[hyperliquid]] -- DEX where ETH-PERP is the #2 market
- [[binance]] / [[coinbase]] -- Largest CEX and builder of Base L2
- [[funding-rate]] / [[open-interest]] / [[basis-trade]] -- Derivatives toolkit
- [[crypto-markets]] -- Market landscape overview
- [[bitcoin-vs-ethereum]] -- Detailed two-asset comparison

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original auto-generated entity data
- Market snapshot 2026-06-20 — cryptodataapi.com / CoinGecko (`raw/data/crypto-loop/coingecko-markets.json`); macro backdrop from `raw/data/crypto-loop/_digest.md` (Fear & Greed = 22; Established Bear Market)
- Merge fork-arbitrage case study — [[2022-09-ethereum-merge-fork-arbitrage]] / [[fork-airdrop-triangulation]]
