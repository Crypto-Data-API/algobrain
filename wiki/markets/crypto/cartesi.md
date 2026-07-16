---
title: "Cartesi"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["CTSI"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://cartesi.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[optimistic-rollup]]", "[[smart-contracts]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Cartesi

**Cartesi** (CTSI) is the utility token of Cartesi, an application-specific [[optimistic-rollup]] execution layer that lets developers build appchain rollups running a full **Linux runtime** while inheriting the security of [[ethereum]]. Its signature component is the **Cartesi Machine**, a deterministic RISC-V virtual machine running Linux, which lets dApps use ordinary programming languages, libraries, and tools instead of being confined to the Ethereum Virtual Machine (EVM). It ranks **#781** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* CTSI trades at **$0.02378002**, market cap **$22,047,039** (rank **#781**), up **+2.14%** over 24h and **+0.44%** over 7 days, in a broad bear-market regime (BTC ~$64,390).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CTSI |
| **Market Cap Rank** | #781 |
| **Market Cap** | $22,047,039 |
| **Current Price** | $0.02378002 |
| **24h Change** | +2.14% |
| **7d Change** | +0.44% |
| **Categories** | Infrastructure, Rollup, Optimistic Rollup, Modular Blockchain, Appchains, Smart Contract Platform, Layer 2 (L2) / Layer 3 (L3), Ethereum Ecosystem |
| **Website** | [https://cartesi.io/](https://cartesi.io/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

About Cartesi (CTSI)

Cartesi enables developers to build appchain rollups with any code, while benefiting from the security of Ethereum. It bridges the gap between traditional software and blockchain by bringing decades of mature operating systems, programming languages, libraries, and tools to decentralized applications.

Cartesi aims to provide the technological foundation from which builders, entrepreneurs, and projects will develop decentralized applications. The Cartesi technology suite is currently comprised of:

Cartesi Rollups: Cartesi Rollups is an app-specific execution environment that can be deployed as a L2, L3, or as sovereign rollups. The combination of an Optimistic Rollups framework and the Cartesi Machine Emulator enables the development of smart contracts and dApps using any package or library that is available for Linux. This allows developers to break free from the scalability limitations of the Ethereum Virtual Machine (EVM), and brings the rise of a new blockchain era to handle real-life and complex use cases.

Cartesi Machine: A RISC-V-based virtual machine (altVM) running Linux OS, enabling complex computations and seamless dApp development by expanding the design space and leveraging 40 years of software programming advancements.

CartesiScan: Cartesiscan is the explorer used for viewing blockchain transactions on Cartesi appchain rollups.

Cartesi Explorer: The Cartesi Explorer is a product that allows CTSI users to interact with the governance system and stake CTSI.

Fraud Proof System - DAVE (following PRT): Dave is a permissionless, interactive fraud-proof system. Cartesi’s algorithm further optimizes the fraud proof mechanism to achieve the best balance between security, decentralization, and activity.

What Makes Cartesi Unique

The infrastructure of the internet took decades to build. With Cartesi, developers gain access to mature operating systems, programming languages, libraries, and tooling — running them inside a verifiable on-chain environment rather than reimplementing everything for the EVM.

---

## Architecture & Consensus

Cartesi is best understood as an **app-specific rollup execution layer** rather than a chain that competes for general-purpose block space. Its defining bet is that the bottleneck for sophisticated dApps is not transaction throughput but **expressiveness** — the inability to run real programming languages, libraries and OS primitives on-chain. Cartesi solves this by moving heavy computation off-chain into a verifiable Linux environment and settling only results (and, if disputed, the minimal disagreement) to a base chain.

- **Optimistic-rollup execution layer:** Cartesi is not a standalone [[layer-1]]; it is an [[optimistic-rollup]]-style execution environment that settles to and inherits security from a base chain (primarily [[ethereum]]). Rollups can be deployed as L2 (settling to Ethereum), L3 (settling to an L2 such as [[arbitrum]] or [[base]]) or as sovereign rollups. Because it is app-specific, each deployment is its own dedicated chain — there is no shared sequencer contention with unrelated dApps.
- **Cartesi Machine:** a deterministic **RISC-V** virtual machine running a real **Linux** OS. RISC-V is an open, mature instruction-set architecture; running Linux inside it lets developers import decades of existing software (Python, C++, Rust, mathematical libraries, databases) instead of reimplementing logic in [[solidity]]. Determinism is what makes the design verifiable: identical inputs always produce identical state, so a single honest party can prove the correct result.
- **Fraud-proof system (Dave / PRT):** Cartesi's interactive fraud proof bisects a disputed computation step-by-step until the two parties disagree on a single RISC-V instruction, which the base chain can then arbitrate cheaply. **Dave** (the successor to the Permissionless Refereed Tournaments / PRT research) generalizes this so that a *single* honest validator can defend the chain against an arbitrary number of dishonest challengers in bounded time — the defining "optimistic" security assumption (computations are assumed valid unless successfully challenged within a window).
- **Off-chain compute, on-chain settlement:** heavy computation runs off-chain inside the Cartesi Machine; only state-root commitments (and, if challenged, succinct dispute steps) touch the base chain. This is what dramatically expands the design space versus on-chain EVM execution — workloads like game engines, ML inference, or complex simulations that are impossible to run within an Ethereum block become feasible.
- **Honeypot / value-scaling:** because each app-rollup posts data and dispute claims to the base layer, **the more economic activity a Cartesi app processes, the more its security budget and base-chain fees scale with usage** — value to CTSI accrues through node staking and the demand for running validators on busy rollups, not through holding state on a monolithic L1.

---

## What the CTSI Token Does

- **Staking & node operation:** CTSI is staked by participants who run nodes and produce/validate blocks for the rollups and the Noether-style data-availability/PoS components, earning rewards.
- **Fees:** CTSI is used to pay for computation/processing services within the Cartesi ecosystem.
- **Governance:** CTSI is used to participate in protocol governance via the Cartesi Explorer.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 909.58M CTSI |
| **Total Supply** | 1.00B CTSI |
| **Max Supply** | 1.00B CTSI |
| **Fully Diluted Valuation** | $31.52M |
| **Market Cap / FDV Ratio** | 0.91 |

A market-cap/FDV ratio of ~0.91 means roughly 91% of the maximum 1B supply is already circulating, so CTSI has **very little future unlock overhang** — a structural advantage over newer, low-float infrastructure tokens (e.g., [[caldera|ERA]] at ~0.17 or [[somnia|SOMI]] at ~0.16). Price is driven by demand/sentiment rather than emissions.

---

## Comparison vs Competing Execution Layers

Cartesi competes in the "alternative-VM / app-specific rollup" niche — projects that move beyond the EVM to enable richer computation. Its closest peers differ in *how* they achieve verifiable off-chain compute:

| Dimension | **Cartesi (CTSI)** | **Arbitrum Stylus** | **RISC Zero / Boundless** | **Movement / MoveVM** |
|---|---|---|---|---|
| **Core idea** | Linux + RISC-V app-rollups, optimistic fraud proofs | WASM (Rust/C) contracts alongside EVM on [[arbitrum]] | Zero-knowledge RISC-V proving (zkVM) | Move-language L1/L2 |
| **Verification** | Interactive fraud proof (Dave) | Inherits Arbitrum fraud proofs | ZK validity proofs | Varies by deployment |
| **Languages** | Anything that runs on Linux | Rust, C, C++ (WASM) | Rust (zkVM guest) | Move |
| **Settlement** | L2/L3/sovereign on [[ethereum]] | L2 on Ethereum | Proof marketplace, any chain | Own / modular |
| **Maturity** | Live framework, niche adoption | Live, large Arbitrum ecosystem | Live proving network | Newer ecosystem |
| **Trade-off** | Cheap general compute, optimistic delay | EVM-coupled, smaller compute envelope | Strong validity guarantees, proving cost | New VM, smaller dev base |

Cartesi's distinct edge is the **breadth of its compute environment** (a full OS) at the cost of optimistic finality delays; ZK approaches like RISC Zero offer faster finality but historically higher proving overhead, while Stylus stays tightly coupled to the EVM. See [[optimistic-rollup]] vs [[zk-rollup|ZK rollup]] for the general trade-off.

---

## How & Where It Trades

- **Spot venues:** CTSI is a long-established, widely listed ERC-20. Deepest liquidity is on **Binance** (CTSI/USDT) and **Kraken** (CTSI/USD), with additional pairs on **Upbit, Bitget, KuCoin, and Crypto.com** (see Exchange Listings). On-chain liquidity is centered on **Uniswap V3** (CTSI/WETH) on [[ethereum]], with bridged versions on [[base]], Polygon, BNB Chain, [[arbitrum]], Optimism and Avalanche.
- **Liquidity profile:** ~$8.6M reported 24h volume against a ~$22M cap means turnover is healthy relative to size, but the order book is thin in absolute terms — large market orders will move price. Treat it as a small-cap: scale in/out, use limit orders.
- **Derivatives:** CTSI perpetuals exist on some venues but open interest is small; this is primarily a **spot-driven** token. There is no deep, liquid futures market to lean on for hedging, so position sizing is the main risk control.
- **Bear-market context:** in the current Established Bear Market (Fear & Greed 21, BTC ~16% below its 200-day MA as of 2026-06-22), low-cap infrastructure tokens like CTSI tend to have **higher beta to BTC** than majors and suffer thinner books — drawdowns can be sharp and gap-prone.

---

## Narrative, Category & Catalysts

Cartesi sits at the intersection of three live narratives: **modular blockchains**, **app-specific rollups / appchains**, and **"beyond the EVM" execution**. Its differentiation — running unmodified Linux software on-chain — resonates most strongly with the appchain and verifiable-compute theses (including AI/ML inference and complex game logic).

**Potential catalysts to watch:**
- Mainnet maturation and adoption of the **Dave** fraud-proof system, which is central to Cartesi's "single honest validator" security pitch.
- Flagship dApps actually shipping on Cartesi rollups (real usage, not just framework releases) — the key missing piece for token demand.
- Broader **verifiable-compute / on-chain AI** narrative rotations, which Cartesi's general-purpose Linux runtime is well-positioned to ride.
- Renewed **modular / appchain** narrative strength (correlated with [[celestia]], [[arbitrum]] Orbit, OP Stack momentum).

**Catalysts that would hurt:** continued bear-market risk-off (small caps bleed first), or the market concluding ZK validity proofs have made optimistic app-rollups obsolete.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.74 (2021-05-09) |
| **Current vs ATH** | -98.19% |
| **All-Time Low** | $0.0213 (2026-03-29) |
| **Current vs ATL** | +47.86% |
| **24h Change** | -4.17% |
| **7d Change** | +40.27% |
| **30d Change** | +32.45% |
| **1y Change** | -35.01% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x491604c0fdf08347dd1fa4ee062a822a5dd06b5d` |
| Base | `0x259fac10c5cbfefe3e710e1d9467f70a76138d45` |
| Polygon Pos | `0x2727ab1c2d22170abc9b595177b2d5c6e1ab7b7b` |
| Binance Smart Chain | `0x8da443f84fea710266c8eb6bc34b71702d033ef2` |
| Arbitrum One | `0x319f865b287fcc10b30d8ce6144e8b6d1b476999` |
| Optimistic Ethereum | `0xec6adef5e1006bb305bb1975333e8fc4071295bf` |
| Avalanche | `0x6b289cceaa8639e3831095d75a3e43520fabf552` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | CTSI/USDT | N/A |
| Kraken | CTSI/USD | N/A |
| Upbit | CTSI/BTC | N/A |
| Bitget | CTSI/USDT | N/A |
| KuCoin | CTSI/USDT | N/A |
| Crypto.com Exchange | CTSI/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X491604C0FDF08347DD1FA4EE062A822A5DD06B5D/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://cartesi.io/](https://cartesi.io/) |
| **Twitter** | [@cartesiproject](https://twitter.com/cartesiproject) |
| **Reddit** | [https://www.reddit.com/r/cartesi/](https://www.reddit.com/r/cartesi/) |
| **Telegram** | [cartesiproject](https://t.me/cartesiproject) (18,040 members) |
| **Discord** | [https://discord.com/invite/Y6qXzM9DeJ](https://discord.com/invite/Y6qXzM9DeJ) |
| **GitHub** | [https://github.com/cartesi/machine-emulator](https://github.com/cartesi/machine-emulator) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 104 |
| **GitHub Forks** | 44 |
| **Commits (4 weeks)** | 7 |
| **Pull Requests Merged** | 168 |
| **Contributors** | 11 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.62M |
| **Market Cap Rank** | #786 |
| **24h Range** | $0.0313 — $0.0338 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History & Timeline

| Date | Event |
|---|---|
| **2020-04** | CTSI initial token sale via **Binance Launchpad**, giving the project early exchange distribution and liquidity. |
| **2021-05-09** | All-time high of **$1.74** during the bull market peak. |
| **2021–2024** | Multi-year drawdown (~98% from ATH) alongside the broader infrastructure-token bear; development shifts to shipping the app-specific rollup framework. |
| **Ongoing** | Research and rollout of the **Dave** interactive fraud-proof system (successor to PRT), Cartesi's "single honest validator" security model. |
| **2026-03-29** | Local all-time low of **$0.0213** during the current Established Bear Market. |

> *Notable events will continue to be added through the wiki's source ingestion workflow.*

---

## Risks

> *Not investment advice. Crypto assets are highly volatile and can go to zero.*

**Technical / protocol**
- **Optimistic-rollup assumptions:** security depends on at least one honest, well-resourced challenger and a sufficiently long dispute window; like all [[optimistic-rollup]] designs, withdrawals/finality involve a challenge delay. ZK validity proofs are a competing paradigm that some believe will displace optimistic designs over time.
- **Complexity surface:** a full Linux + RISC-V runtime is a large and unusual attack surface relative to minimal EVM contracts.

**Adoption / economic**
- **Adoption risk:** the value proposition (Linux-in-a-rollup) is technically compelling but competes in a crowded rollup/modular landscape; meaningful CTSI demand depends on real dApp deployment and on-chain usage, which has lagged the framework's technical readiness.
- **Concentrated development:** developer activity is relatively small (~11 contributors, single-digit commits in recent 4-week windows), a common fragility for niche infrastructure projects.
- **Value-accrual ambiguity:** as an execution-layer token, CTSI's link between network usage and token demand runs through staking/node operation, which is more indirect than gas-coin economics on an L1.

**Market / liquidity**
- **Small-cap volatility & drawdown:** at ~$22M market cap (rank #781) and down ~98% from ATH, CTSI is volatile and thinly traded; in a bear regime it carries high beta to BTC.

---

## Trading Playbook

> *Educational framing, not advice. Sizing and risk control matter more than entries for tokens this small.*

- **Regime read (2026-06-22):** Established Bear Market, Fear & Greed 21 (Extreme Fear). Small-cap infrastructure tokens are out of favor; CTSI is near multi-year lows. This is an accumulation-zone *environment* for conviction holders but also one where things can keep bleeding.
- **What to watch (bullish):** a break of the broad crypto risk-off (BTC reclaiming its 200-day MA, Fear & Greed exiting Extreme Fear), the appchain/modular narrative reigniting, and — project-specific — Dave going live with real app-rollup traffic.
- **What to watch (bearish):** BTC making new local lows (small caps amplify the move), volume drying up further, or a ZK-validity-proof narrative declaring optimistic app-rollups legacy tech.
- **Mechanics:** thin book — use limit orders, scale in/out, size for the possibility of 50%+ drawdowns. There is no liquid perp market to hedge with, so spot position size *is* your risk control.
- **Relative value:** versus low-float peers ([[caldera]], [[somnia]]), CTSI's high circulating ratio (~0.91) means little unlock dilution — a point in its favor for longer holds, offset by weaker recent momentum and adoption.

---

## Trading Profile

### Venues & liquidity

CTSI is tradable on [[binance]] as both **spot** (CTSI/USDT) and a **USD-margined [[perpetual-futures|perpetual]]** contract that exposes [[funding-rate|funding]], open interest and liquidation data — Binance is the primary leveraged venue for the token. It is **not listed on [[hyperliquid]]**, so on-chain perp liquidity that some larger caps enjoy is unavailable here. In practice this concentrates leveraged flow, funding and OI signal in a single venue: derivatives-based strategies must source data from Binance, and any Binance-specific listing, delisting or margin-tier change can abruptly reshape available leverage. Given the small underlying cap and thin book, perp open interest is modest relative to majors; leverage is best kept low and position sizing conservative, since spot depth — not the derivatives market — sets the real slippage floor for larger orders.

### Applicable strategies

- [[funding-rate-harvest]] — collect Binance perp funding on CTSI when the crowd leans one way, sized small given the thin single-venue book.
- [[cash-and-carry]] — pair long Binance spot against the short USD-M perp to lock basis when funding runs persistently positive on this low-cap.
- [[crowded-long-funding-fade]] — fade over-extended longs during narrative-driven CTSI pops when funding and OI spike together on Binance.
- [[liquidation-cascade-fade]] — thin depth makes CTSI prone to sharp liquidation flushes; fade the wick once forced selling exhausts.
- [[oi-confirmed-trend]] — use Binance open-interest expansion to confirm that a CTSI breakout is backed by real leveraged participation rather than a low-liquidity spike.
- [[rsi-mean-reversion]] — small-cap CTSI overshoots in both directions, so oscillator-based reversion around range extremes fits its spot-driven behavior.

### Volatility & regime character

CTSI is a **small-cap infrastructure / rollup token** (rank ~792) with high beta to BTC and to the broader modular/appchain and "beyond-the-EVM" narratives. Moves are reflexive and gap-prone in thin books; it tends to underperform in risk-off regimes (small caps bleed first) and can spike hard on narrative rotations (verifiable compute, on-chain AI, appchains). Correlation to BTC/ETH is high on the downside and looser on the upside, where idiosyncratic catalysts dominate. It is not a memecoin, but its low cap gives it memecoin-like reflexivity during liquidity events.

### Risk flags

- **Venue concentration:** leveraged trading is effectively Binance-only (no [[hyperliquid]]); a single-venue funding/OI feed and exposure to Binance listing or margin-policy changes.
- **Liquidity:** thin absolute spot depth relative to cap — large orders move price; perp OI is small, so hedging capacity is limited.
- **Narrative dependence:** demand hinges on the appchain/modular and verifiable-compute theses and on real dApp adoption, which has lagged the framework's technical readiness.
- **Supply:** minimal unlock overhang (~0.91 circulating/FDV) is a structural positive, so emissions are not a major near-term risk flag.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=CTSIUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=CTSIUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=CTSI` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=CTSI` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=CTSIUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=CTSIUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=CTSI"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[optimistic-rollup]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
