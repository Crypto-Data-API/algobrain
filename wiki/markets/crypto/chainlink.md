---
title: "Chainlink"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, altcoins]
aliases: ["LINK", "Chainlink Labs"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://chain.link/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[oracle]]", "[[defi]]", "[[aave]]", "[[gmx]]", "[[curve-finance]]", "[[uniswap]]", "[[lido]]", "[[bitcoin]]", "[[hyperliquid]]", "[[pyth-network]]", "[[restaking]]", "[[narrative-trading]]"]
---

# Chainlink

**Chainlink** (LINK) is the industry-standard decentralized oracle network that solves the "oracle problem" by connecting smart contracts with real-world data. Blockchains cannot access external information on their own, so Chainlink acts as a secure bridge, enabling smart contracts to react to real-world events using verified, tamper-proof data. For traders, LINK is the canonical "picks-and-shovels" infrastructure bet on [[defi]] and tokenized real-world assets — virtually every major lending, perps, and stablecoin protocol depends on its price feeds.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Backdrop: the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **22 (extreme fear)** in what is now widely characterized as an **established bear market**. LINK has held up better than most large alts on a 7-day basis (roughly flat) thanks to its institutional pipeline, but remains far below its cycle highs.

| Metric | Value |
|---|---|
| **Price** | $7.95 |
| **Market Cap** | $5,948,100,843 |
| **Market Cap Rank** | #20 |
| **24h Volume** | $190,278,018 |
| **24h Change** | +1.26% |
| **7d Change** | -0.10% |
| **24h Range** | $7.79 – $7.99 |
| **Circulating Supply** | 748,099,970 LINK |
| **Total Supply** | 1,000,000,000 LINK |
| **Max Supply** | 1,000,000,000 LINK |
| **Fully Diluted Valuation** | $7,950,943,828 |
| **Market Cap / FDV** | ~0.75 |
| **All-Time High** | $52.70 (2021-05-10) — **-84.91%** from ATH |
| **All-Time Low** | $0.148183 (2017-11-29) — **+5,264.73%** from ATL |

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LINK |
| **Market Cap Rank** | #20 (2026-06-20) |
| **Market Cap** | $5.95B (2026-06-20) |
| **Price** | $7.95 (2026-06-20); $8.77 at April 2026 snapshot |
| **Chain / Sector** | Ethereum-native ERC-20, deployed on 20+ chains; [[oracle]] / interoperability / RWA infrastructure |
| **Supply Mechanics** | Fixed 1B max supply; ~748M circulating (June 2026); team/treasury holds the remainder |
| **Genesis Date** | 2017-09-16 (ICO raised $32M) |
| **Website** | [https://chain.link/](https://chain.link/) |

---

## Overview

The platform operates through a decentralized network of nodes that fetch, validate, and deliver data to smart contracts. When a contract requests information like a stock price, a committee of independent nodes retrieves and aggregates the data to reach consensus, then delivers a single trustworthy answer. Chainlink offers a suite of services including Data Feeds for asset prices, CCIP for cross-chain token transfers and messaging, Automation for triggering smart contract functions, and Proof of Reserve for verifying asset collateralization.

Chainlink has established itself as critical infrastructure for both DeFi and institutional adoption, with partnerships including Swift, Euroclear, Mastercard, UBS, ANZ, Fidelity International, and J.P. Morgan. Its institutional products include the Chainlink Runtime Environment for tokenized asset workflows, Confidential Compute for privacy-preserving computation, and the Automated Compliance Engine for embedding regulatory rules into smart contracts.

The LINK token is the native asset used to pay node operators for services, fund subscription accounts, and incentivize network security through staking. Node operators stake LINK as collateral, which can be slashed if they provide inaccurate data. Chainlink was co-founded in 2017 by Sergey Nazarov and Steve Ellis, who co-authored the white paper with Ari Juels, and raised $32 million in its September 2017 ICO.

---

## Protocol & Technology

### The oracle problem and Chainlink's architecture

Blockchains are deterministic, isolated state machines: a smart contract cannot natively fetch an off-chain fact (a price, a sports result, weather, a Swift message) without a trusted bridge. That bridge is an [[oracle]], and a single oracle reintroduces a central point of failure. Chainlink's answer is a **Decentralized Oracle Network (DON)**: a committee of independent node operators each fetch a data point from multiple sources, the responses are aggregated (median/weighted), and a single consensus value is written on-chain. Crypto-economic security (staking + slashing + reputation) deters individual nodes from reporting bad data.

### Data delivery models

- **Push (Data Feeds)** — feeds update on-chain when price deviates beyond a threshold or a heartbeat elapses; the classic model powering [[aave|Aave]], [[gmx|GMX]], [[curve-finance|Curve]] liquidations and collateral pricing.
- **Pull / low-latency (Data Streams)** — sub-second, on-demand signed reports the consumer pulls and verifies on-chain, designed to compete with [[pyth-network|Pyth]]'s pull model for perps and high-frequency DeFi (e.g. on-chain equity perps via the 2026 US-equities streams).
- **OCR (Off-Chain Reporting)** — nodes agree off-chain and submit one aggregated transaction, drastically cutting gas vs each node posting separately.

### Service suite

- **VRF (Verifiable Random Function)** — tamper-proof on-chain randomness (gaming, NFT mints, fair selection).
- **Automation (Keepers)** — condition-triggered contract execution (liquidations, limit orders, rebalancing).
- **CCIP** — cross-chain token transfers + arbitrary messaging; Chainlink's bid to be the interop standard (see Core Products).
- **Proof of Reserve** — on-chain attestation of off-chain/cross-chain collateral backing.
- **CRE (Chainlink Runtime Environment)** — orchestration layer for institutional tokenization workflows.
- **Confidential Compute** — privacy-preserving computation inside CRE.

### Security model & staking

Node operators post **LINK as a stake** that can be **slashed** for inaccurate or unavailable data, layering economic penalties on top of reputation. Staking v0.2 (45M LINK) extends this to token holders, who back the network and earn emissions/fee yield. This is conceptually adjacent to (but distinct from) [[restaking]] in the Ethereum ecosystem — both rent out crypto-economic security, but Chainlink's slashing secures oracle correctness rather than consensus.

---

## 2025–2026 Developments

- **Chainlink Reserve (August 2025)** — Chainlink launched a strategic on-chain reserve of LINK, funded by off-chain enterprise revenue and on-chain service fees. This is the first mechanism that converts enterprise revenue into systematic LINK accumulation, a key piece of the "value accrual" bull thesis.
- **Swift + UBS tokenized fund pilot (2025-09-30)** — Chainlink announced a solution letting banks manage digital-asset workflows over existing Swift ISO 20022 messaging: UBS tokenized-fund subscriptions/redemptions were triggered via Swift messages through the Chainlink Runtime Environment (CRE) and Chainlink's Digital Transfer Agent standard.
- **Chainlink Runtime Environment goes live (2025-11-04)** — CRE, the orchestration layer for institutional tokenization, launched with adopters including Swift, Euroclear, UBS, Kinexys by J.P. Morgan, Mastercard, AWS, Google Cloud, Aave's Horizon, and Ondo. A corporate-actions initiative with Swift, Euroclear and 22 market participants runs on CRE.
- **24/5 US Equities Data Streams (January 2026)** — Chainlink launched real-time US equity data feeds for DeFi, opening tokenized-equity and on-chain stock-perp use cases (a direct input to platforms like [[hyperliquid]]-style equity perps).
- **Confidential Compute (early 2026)** — privacy-preserving computation service entered early access within CRE.
- **Scale of usage** — secondary sources (March 2026) cite ~$27T in cumulative transaction value facilitated and ~24 major financial institutions using CRE, with ~45M LINK staked in v0.2 (unverified marketing-adjacent figures; treat as order-of-magnitude).

Despite arguably the strongest institutional pipeline in crypto, LINK price has lagged: **$7.95 on 2026-06-20** vs $8.77 in April 2026 and an ATH of $52.70 (May 2021), -84.9% from ATH. The persistent gap between adoption news flow and price is itself a well-known trading characteristic of LINK ("sell the partnership news").

---

## Core Products and Revenue Streams

### Data Feeds (Price Oracles)

Chainlink's foundational product. Price feeds power the vast majority of DeFi lending, derivatives, and stablecoin protocols. [[aave]], [[gmx]], [[curve-finance]], Synthetix, and hundreds of other protocols depend on Chainlink price feeds for critical operations (liquidations, trade execution, collateral valuation). Revenue comes from subscription fees paid by protocols.

### CCIP (Cross-Chain Interoperability Protocol)

CCIP enables **cross-chain token transfers and arbitrary messaging** between blockchains. This is Chainlink's bid to become the standard for cross-chain communication, competing with bridges like Wormhole, LayerZero, and Axelar. CCIP provides:

- **Token transfers**: Move tokens between chains with Chainlink-level security guarantees
- **Programmable token transfers**: Attach arbitrary instructions to cross-chain token transfers (e.g., "transfer USDC to Arbitrum and deposit into [[aave]]")
- **Cross-chain messaging**: Send arbitrary data between smart contracts on different chains

CCIP revenue is paid in LINK tokens, creating demand for the token beyond oracle services. The institutional adoption potential is significant -- Swift's collaboration with Chainlink specifically targets CCIP for traditional finance interoperability.

### Automation (Keepers)

Chainlink Automation triggers smart contract functions based on conditions (time-based, custom logic, log-based). Use cases include:

- Auto-harvesting yield farming rewards
- Executing limit orders on DEXs
- Rebalancing liquidity positions
- Triggering liquidations
- Automating DAO operations

Revenue: Node operators are paid in LINK for automation execution.

### Proof of Reserve

Verifies the backing of wrapped tokens, stablecoins, and tokenized assets. Critical for maintaining trust in assets like WBTC, USDC, and tokenized securities. Becoming increasingly important as real-world asset (RWA) tokenization grows.

### Staking v0.2

Chainlink launched **staking** for LINK token holders, allowing them to earn yield by securing the network. Key parameters:

- **Pool size**: Initially capped (45M LINK in v0.2), with expansion planned
- **APY**: 4-8% from emissions and eventually from protocol fee revenue
- **Lock-up**: LINK staked in v0.2 has an unbonding period
- **Slashing**: Staked LINK can be slashed if node operators provide inaccurate data, creating a crypto-economic security backstop
- **Significance**: Staking creates token demand (lock-up reduces circulating supply) and aligns LINK holder incentives with network security

### BUILD Program

The BUILD program allows new and established DeFi protocols to access Chainlink services at reduced cost in exchange for committing a portion of their native token supply or network fees to Chainlink. This creates a virtuous cycle: protocols get infrastructure; Chainlink accumulates protocol tokens and fee commitments, diversifying its revenue base.

---

## Oracle Fee Economics and Revenue Model

Understanding Chainlink's revenue model is important for LINK token valuation:

1. **Protocol subscriptions**: DeFi protocols pay for data feeds, automation, VRF (randomness), and CCIP in LINK tokens
2. **Node operator costs**: Nodes are paid in LINK for operating oracle infrastructure; they must maintain uptime and accuracy or face slashing
3. **Fee flow**: Protocol subscription fees → Chainlink network → node operators. The difference between total fees and node operator costs is network revenue
4. **Current economics**: As of early 2024, Chainlink's fee revenue is growing but still partially subsidized by LINK emissions to node operators. Full fee sustainability (where protocol fees cover all node costs) is a key milestone to watch
5. **CCIP expansion**: CCIP is expected to become a significant additional revenue stream as cross-chain activity grows

---

## Trading Strategies and LINK Token Characteristics

### LINK as a DeFi Infrastructure Bet

- **Thesis**: LINK is a beta play on total DeFi activity. As DeFi TVL grows, demand for Chainlink services (price feeds, automation, CCIP) grows, increasing LINK demand from protocol subscriptions
- **Correlation**: LINK tends to outperform during DeFi bull markets and underperform during DeFi-quiet periods. It has moderate beta (~1.2-1.5x) to BTC and higher beta to DeFi-specific rallies
- **Catalysts**: Major CCIP adoption announcements, institutional partnerships (Swift, banks), staking pool expansions, new service launches

### LINK Staking Yield (Low difficulty)

- **Mechanism**: Stake LINK in v0.2 staking pool for emissions-based yield + eventual fee-sharing
- **APY**: 4-8% (verify current rate; may change as pool expands)
- **Capital requirement**: LINK tokens (minimum varies by pool)
- **Difficulty**: Beginner -- stake and earn
- **Risk**: Lock-up period means opportunity cost if LINK price drops; slashing risk (extremely low for passive stakers); yield may compress as more LINK is staked

### Institutional Announcement Trading (Moderate difficulty)

- **Mechanism**: LINK price responds significantly to institutional partnership announcements (Swift, DTCC, major banks). Monitor Chainlink's social channels and blog for announcements; position ahead of or react to major news
- **Risk**: Front-running announcements is speculative; partnerships do not always translate to immediate revenue or token demand; "buy the rumor, sell the news" dynamics are common

### Cross-Chain Activity Correlation Trading (Advanced)

- **Mechanism**: Monitor CCIP usage metrics (transaction count, volume transferred). Rising CCIP usage indicates increasing LINK demand from fee payments. Position LINK ahead of CCIP growth inflection points
- **Data sources**: Dune Analytics CCIP dashboards, Chainlink documentation updates, bridge comparison sites
- **Risk**: CCIP adoption may be slower than expected; competing cross-chain protocols could win market share

---

## Risk Framework

### Token Supply Overhang

LINK has a fixed max supply of 1B tokens, but ~27% remains unlocked and held by the Chainlink team/treasury. Periodic large token releases (for node operator subsidies, partnerships, team compensation) create sell pressure. Monitoring wallet activity of known Chainlink-affiliated addresses is important for managing LINK position risk.

### Oracle Centralization Criticism

Despite being "decentralized," many Chainlink price feeds rely on a relatively small number of node operators (often 10-20 per feed). Critics argue this is insufficient decentralization for the critical infrastructure Chainlink provides. A coordinated node operator failure or collusion could deliver incorrect prices, potentially causing cascading DeFi failures across protocols like [[aave]], [[gmx]], and [[curve-finance]].

### Revenue Sustainability

Chainlink currently subsidizes node operations through LINK emissions. The protocol has not yet reached a state where organic fee revenue fully covers operational costs. If LINK price drops significantly (reducing the value of emission subsidies), node operators may reduce service quality or exit, degrading the network.

### Competition

Oracle competitors include Pyth Network (focused on low-latency DeFi data), API3 (first-party oracles), Band Protocol, and UMA's Optimistic Oracle. While Chainlink dominates market share, competition could compress pricing power over time.

### Dependency Risk

Chainlink is critical infrastructure for hundreds of DeFi protocols. A Chainlink failure would cascade across the entire DeFi ecosystem. This "too big to fail" status is both a strength (protocols cannot easily switch) and a systemic risk (failure would be catastrophic).

---

## Key Metrics

| Metric | Value | Notes |
|---|---|---|
| **LINK Price** | $7.95 (2026-06-20) | See [[chainlink#Market Data\|Market Data]] |
| **LINK Market Cap** | $5.95B | #20 by market cap |
| **Circulating Supply** | 748.10M LINK (of 1B max) | |
| **LINK ATH** | $52.70 (May 2021) | Current: -84.9% from ATH |
| **Protocols Using Chainlink** | 1,000+ across 20+ chains | Verify on chain.link ecosystem page |
| **Data Feed Count** | 1,000+ price feeds across chains | |
| **CCIP Transactions** | Growing; verify on Dune Analytics | |
| **Staking Pool Size** | 45M LINK in v0.2 | Verify on Chainlink staking dashboard |
| **24h Volume** | $190.28M | 2026-06-20 |

---

## Market Structure & Derivatives

- **Spot venues**: LINK is one of the most broadly listed alts — deep books on [[binance|Binance]] (LINK/USDT, the global price-leading pair), Coinbase (LINK/USD), [[kraken|Kraken]], Upbit (LINK/KRW; Korean retail flow), Bitget, KuCoin, Crypto.com. On-chain, LINK/WETH on [[uniswap|Uniswap]] v3 is the reference DEX pool.
- **Perpetuals & funding**: LINK-PERP is a top-tier perp across Binance, Bybit, OKX and on-chain via [[hyperliquid|Hyperliquid]]. Open interest is large enough that LINK funding and OI are watched as alt-risk-appetite gauges. In the current extreme-fear tape, funding has skewed mildly negative/neutral (shorts paying little), consistent with a market that is hedged rather than euphoric.
- **Basis / carry**: persistent contango in calmer regimes lets cash-and-carry desks short perps vs spot; in bear conditions basis compresses and the trade's edge thins.
- **Liquidity profile**: $190M 24h volume on a ~$5.9B cap gives a volume/MCAP turnover around 3% — middling for a large alt, meaning blocks can move price; size entries accordingly.

---

## Valuation Framework

LINK is hard to value on cash flows because oracle fees are still partially emission-subsidized. Useful handles:

- **Protocol fee capture** — total fees paid to the network for Data Feeds, [[oracle|oracle]] services, VRF, Automation and CCIP, minus node-operator compensation. Net network revenue is the true numerator; track it on Token Terminal / Dune.
- **Value-accrual flywheel** — the **Chainlink Reserve** (Aug 2025) converts off-chain enterprise revenue into on-chain LINK accumulation. Reserve inflow rate is the cleanest new fundamental to watch: it is the first mechanism linking enterprise revenue to token demand.
- **CCIP volume × take-rate** — cross-chain value secured × fee bps gives an addressable-revenue estimate as interop scales.
- **Staking-locked supply / float** — staked LINK (45M in v0.2) removes float; a rising staked-supply ratio tightens effective supply.
- **MC/FDV ≈ 0.75** — relatively benign dilution vs peers (only ~25% of max supply outside circulation), but treasury releases remain an overhang (see Risk Framework).
- **Relative multiple** — LINK trades at a premium to pure-play oracle peers like [[pyth-network|Pyth]] on a market-cap basis; bulls justify it with the institutional/CCIP optionality, bears call it priced-for-perfection.

Do not anchor to a single fair-value number — the spread between "infrastructure monopoly" and "subsidized, low-fee utility" valuations is wide and unresolved.

---

## Trading Playbook

- **Infrastructure beta** — treat LINK as levered [[defi|DeFi]]/RWA exposure (~1.2–1.5x BTC beta, higher to DeFi-specific rallies). Long into DeFi-TVL upcycles; trim into euphoria.
- **"Sell the partnership news"** — LINK's defining microstructure quirk: institutional headlines (Swift, banks, CRE adopters) routinely produce a spike that fades. Fade strength on announcements unless accompanied by on-chain Reserve/fee inflection.
- **Reserve-accumulation thesis (longer horizon)** — accumulate if Chainlink Reserve inflows and CCIP fee revenue trend up; this is the structural bull case independent of headline beta.
- **Staking carry** — stake v0.2 for 4–8% emissions yield; size for the lock-up/unbonding period and slashing tail (negligible for passive stakers).
- **Pairs** — LINK vs [[pyth-network|PYTH]] for oracle relative value; LINK vs a DeFi basket ([[aave|AAVE]], [[uniswap|UNI]]) to isolate oracle-specific catalysts.
- **Risk management in extreme fear** — with Fear & Greed at 22, prefer scaling entries and defined-risk structures; alt liquidity is thin and downside gaps are common in established bear markets.

---

## Competitive Positioning

| Oracle / Interop Network | Market Position | Edge vs Chainlink | Chainlink's Edge |
|---|---|---|---|
| [[pyth-network\|Pyth Network]] | #2 oracle; ~$0.1–0.2B-tier cap; Solana-native, multi-chain | Sub-second pull-based feeds; first-party publisher model; cheaper for HFT-style DeFi | Far more integrations; CCIP; institutional pipeline; broader service suite (VRF, Automation, PoR) |
| API3 | Niche; first-party "dAPI" oracles | Data providers run their own nodes (OEV capture, fewer middlemen) | Network effects; integration depth |
| Band Protocol | Cosmos-native oracle | Better fit for Cosmos/IBC | Vastly larger share, more chains |
| RedStone | Modular/pull oracle, fast-growing on LSTs/RWAs | Lightweight, cheap, modular DA model | Maturity, security track record, institutional trust |
| Wormhole / LayerZero (CCIP rivals) | Leading cross-chain messaging | Faster to market; higher current cross-chain volume | Institutional credibility (Swift), security guarantees, programmable token transfers |

Chainlink's moat is **network effects and integration depth**. Switching oracle providers is expensive and risky for DeFi protocols (requires audit, code changes, governance votes). Once a protocol integrates Chainlink, switching costs are high. The institutional partnership pipeline (Swift, banks) is unique among oracle providers and positions Chainlink for the institutional DeFi / tokenized asset wave. See [[pyth-network]] for the leading challenger.

---

## Tokenomics & Supply

> *Authoritative supply/price figures are in the [[chainlink#Market Data\|Market Data]] block (2026-06-20).*

| Metric | Value |
|---|---|
| **Circulating Supply** | 748,099,970 LINK |
| **Total Supply** | 1,000,000,000 LINK |
| **Max Supply** | 1,000,000,000 LINK |
| **Fully Diluted Valuation** | $7,950,943,828 |
| **Market Cap / FDV Ratio** | ~0.75 |

**Emissions & unlocks.** LINK has no public on-chain inflation schedule beyond the fixed 1B cap. The non-circulating ~25% (~252M LINK) is held by Chainlink Labs / the ecosystem and released over time to fund node-operator subsidies, BUILD partnerships, grants and team compensation. These discretionary releases — not a fixed unlock cliff — are the dilution vector to watch (see Risk Framework → Token Supply Overhang). Staking (45M in v0.2) and the Chainlink Reserve work in the opposite direction by removing/absorbing float.

---

## Price History

> *Authoritative current figures are in the [[chainlink#Market Data\|Market Data]] block (2026-06-20). Table below is long-horizon reference.*

| Metric | Value |
|---|---|
| **All-Time High** | $52.70 (2021-05-10) |
| **Current vs ATH** | -84.91% |
| **All-Time Low** | $0.148183 (2017-11-29) |
| **Current vs ATL** | +5,264.73% |
| **24h Change (2026-06-20)** | +1.26% |
| **7d Change (2026-06-20)** | -0.10% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

Chainlink is deployed across 20+ blockchains. LINK token is available on virtually every major chain. See contract addresses section for specific chains.

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LINK/USDT | N/A |
| Kraken | LINK/USD | N/A |
| Upbit | LINK/KRW | N/A |
| Bitget | LINK/USDT | N/A |
| KuCoin | LINK/USDT | N/A |
| Crypto.com Exchange | LINK/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | LINK-PERP | Perpetual |
| Uniswap V3 (Ethereum) | LINK/WETH | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://chain.link/](https://chain.link/) |
| **Twitter** | [@chainlink](https://twitter.com/chainlink) |
| **Reddit** | [https://www.reddit.com/r/Chainlink/](https://www.reddit.com/r/Chainlink/) |
| **Telegram** | [chainlinkofficial](https://t.me/chainlinkofficial) (21,563 members) |
| **GitHub** | [https://github.com/smartcontractkit/chainlink](https://github.com/smartcontractkit/chainlink) |
| **Whitepaper** | [https://research.chain.link/whitepaper-v2.pdf](https://research.chain.link/whitepaper-v2.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 5,703 |
| **GitHub Forks** | 1,538 |
| **Commits (4 weeks)** | 87 |
| **Pull Requests Merged** | 8,258 |
| **Contributors** | 173 |

---

## Trading Characteristics

> *Current figures: see [[chainlink#Market Data\|Market Data]] (2026-06-20).*

| Characteristic | Detail |
|---|---|
| **24h Volume** | $190.28M |
| **Market Cap Rank** | #20 |
| **24h Range** | $7.79 – $7.99 |
| **Volume / MCAP turnover** | ~3.2% |
| **Last Updated** | 2026-06-20 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Ecosystem & Use Cases

- **DeFi backbone** — Chainlink price feeds underpin lending liquidations and collateral valuation ([[aave]], [[compound-governance-token|Compound]]), perp/derivatives execution ([[gmx]], [[hyperliquid]]-style venues), stablecoin pegs ([[curve-finance|crvUSD]]), and LST pricing ([[lido|stETH/ETH]]). A material share of total [[defi]] TVL is secured by Chainlink in some capacity.
- **RWA & tokenization** — Proof of Reserve, CRE and CCIP are the rails for tokenized funds and on-chain securities (UBS, Euroclear, Kinexys/J.P. Morgan corporate-actions pilots).
- **Cross-chain** — CCIP moves tokens + messages between chains with programmable instructions (e.g. bridge-and-deposit-into-[[aave]] in one transaction).
- **Tokenized equities / on-chain stocks** — the 2026 24/5 US-equities Data Streams feed on-chain equity perps and tokenized-stock products.
- **Enterprise / TradFi** — Swift ISO 20022 integration lets banks trigger digital-asset workflows over existing messaging rails.
- **Gaming & NFTs** — VRF for provably fair randomness; Automation for game-state and reward logic.

---

## History

| Date | Event |
|---|---|
| 2017-09 | Whitepaper (Nazarov, Ellis, Juels); ICO raises $32M; LINK ERC-20 launches |
| 2019-05 | Chainlink mainnet (Data Feeds) goes live on Ethereum |
| 2020 | DeFi summer — Chainlink becomes default oracle for Aave, Synthetix, others |
| 2021-05 | LINK all-time high $52.70 |
| 2022 | Staking v0.1 launches; CCIP development announced |
| 2023 | CCIP mainnet early access; Swift cross-chain experiments |
| 2024 | Staking v0.2 (45M LINK); BUILD program expansion |
| 2025-08 | Chainlink Reserve launched (enterprise revenue → on-chain LINK) |
| 2025-09-30 | Swift/UBS tokenized-fund workflows via CRE + ISO 20022 |
| 2025-11-04 | CRE goes live; Swift, Euroclear, UBS, Kinexys, Mastercard adopters |
| 2026-01 | 24/5 US Equities Data Streams launch; Confidential Compute early access |
| 2026-06-20 | LINK $7.95, #20, in an extreme-fear / established-bear-market tape |

---

## Major News & Events

- 2025-08 — Chainlink Reserve announced (on-chain LINK reserve funded by enterprise revenue)
- 2025-09-30 — Swift/UBS tokenized fund workflows via CRE and ISO 20022 messaging
- 2025-11-04 — Chainlink Runtime Environment (CRE) goes live; Swift, Euroclear, UBS, Kinexys (J.P. Morgan), Mastercard among adopters
- 2026-01 — 24/5 US Equities Data Streams launch; Confidential Compute early access slated for 2026

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[defi]] -- Chainlink is critical infrastructure for the DeFi ecosystem
- [[aave]] -- Major consumer of Chainlink price feeds
- [[gmx]] -- Uses Chainlink oracles for trade execution
- [[curve-finance]] -- Uses Chainlink feeds for crvUSD
- [[lido]] -- stETH/ETH price feeds provided by Chainlink
- [[uniswap]] -- v4 hooks can integrate Chainlink oracles
- [[pyth-network]] -- leading oracle competitor (peer comparison above)
- [[oracle]] -- the concept Chainlink operationalizes
- [[restaking]] -- adjacent crypto-economic-security primitive

---

## Sources

- Market data 2026-06-20: cryptodataapi.com / CoinGecko markets snapshot (`raw/data/crypto-loop/coingecko-markets.json`)
- (Source: [[coingecko-top-1000-2026-04-09]])
- (Source: [[2026-04-22-perplexity-defi-trading-strategies-sweep]])
- Chainlink Blog — "Chainlink Runtime Environment Now Live" (2025-11-04): https://blog.chain.link/chainlink-runtime-environment-now-live/
- PR Newswire — "Chainlink Advances Tokenized Fund Workflows With Swift Messaging in Collaboration With UBS" (2025-09-30): https://www.prnewswire.com/news-releases/chainlink-advances-tokenized-fund-workflows-with-swift-messaging-in-collaboration-with-ubs-302570072.html
- The Block — "Chainlink integrates Swift messaging to streamline tokenized fund workflows with UBS": https://www.theblock.co/post/372876/chainlink-swift-tokenized-fund-workflows-ubs-pilot
- CoinMarketCap / CoinGecko Chainlink pages (price, rank, Chainlink Reserve description), checked 2026-06-10
- Verified via Perplexity sonar + web search, 2026-06-10
