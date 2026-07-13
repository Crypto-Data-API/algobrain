---
title: "Sei"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi, altcoins]
aliases: ["SEI", "Sei Network", "Sei V2", "Giga"]
entity_type: protocol
founded: 2022
headquarters: "Decentralized (Sei Labs: San Francisco, USA)"
website: "https://www.sei.io"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[aptos]]", "[[hyperliquid]]", "[[solana]]", "[[stablecoins]]"]
---

# Sei

**Sei** (SEI) is a high-performance, parallelized-EVM Layer 1 purpose-built for trading and exchange-style applications, launched on mainnet in August 2023. Its two defining 2025-2026 stories are the **Giga upgrade** — an Autobahn-consensus rewrite targeting ~200,000 TPS and sub-400ms finality, with mainnet rollout targeted for H1 2026 — and its selection as one of **two finalist chains (alongside [[aptos|Aptos]]) for Wyoming's WYST**, the first US state-issued stablecoin, which drove an ~85% weekly SEI rally when announced. For traders, SEI is a high-beta "trading chain / institutional-rails" narrative play with a persistent token-unlock overhang (MC/FDV ≈ 0.67), trading ~95% below its ATH in the 2026 [[crypto-market-regimes|Established Bear Market]] (Fear & Greed 23).

---

## Market Data

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $0.05491 |
| **Market Cap** | $369.8M |
| **Market Cap Rank** | #123 |
| **24h Volume** | $28.8M |
| **24h Change** | +1.89% |
| **7d Change** | +0.30% |
| **Circulating Supply** | 6.73B SEI |
| **Total Supply** | 10.0B SEI |
| **Max Supply** | None (uncapped) |
| **All-Time High** | $1.14 (2024-03-16) — ≈ -95.2% |
| **All-Time Low** | $0.04470 (2026-03-31) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

> Earlier snapshot: 2026-04-09 (CoinGecko) price $0.0549, mcap $369.6M, rank #114.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SEI |
| **Chain** | Own Layer 1 — parallelized EVM (Sei V2), Twin-Turbo consensus; Giga upgrade in progress |
| **Sector** | L1 / DeFi infrastructure; "trading chain" positioning |
| **Rank tier** | #123, $369.8M cap, $0.05491 (2026-06-20) |
| **Supply mechanics** | 6.73B circulating of 10B total (MC/FDV ≈ 0.67) — ongoing unlocks are a structural overhang |
| **Backers** | Multicoin, Coinbase Ventures, Delphi, Circle Ventures, OKX Ventures; in the World Liberty Financial portfolio |
| **Giga targets** | ~200,000 TPS, sub-400ms finality via Autobahn consensus + async execution (whitepaper 2025-05-19) |
| **Website** | [https://www.sei.io](https://www.sei.io) |

---

## Overview

Sei is a high-performance Layer 1 blockchain that scales the EVM with parallelized execution, enabling faster transactions, low fees, and seamless smart contract deployment while maintaining full Ethereum compatibility. Sei's design optimizes for exchange-style workloads (order matching, oracle-heavy DeFi), positioning it as "the chain for trading."

The **Giga upgrade** — detailed in a whitepaper published **2025-05-19** — is the next architectural leap: a new **Autobahn consensus protocol** with parallel block proposal and asynchronous execution, targeting **200,000+ TPS with sub-400-millisecond finality**, aiming to make Sei the fastest EVM-compatible L1 with web2-class performance. Mainnet rollout has been targeted for **H1 2026**. (Sources: Sei Giga whitepaper; CoinMarketCap AI updates, 2026.)

---

## Protocol & Technology

Sei's architecture is engineered end-to-end for *trading latency and throughput*, distinguishing it from general-purpose L1s:

- **Parallelized EVM (Sei V2)** — Sei runs a fully [[ethereum|Ethereum]]-compatible EVM but executes non-conflicting transactions **in parallel** across cores (optimistic parallelization with dependency detection), rather than the EVM's default sequential execution. Solidity contracts and standard Ethereum tooling work unchanged, but throughput scales with hardware. This is the same broad idea as [[aptos|Aptos]]'s Block-STM and [[solana|Solana]]'s Sealevel, applied to the EVM.
- **Twin-Turbo consensus** — Sei's v2 consensus combines *Intelligent Block Propagation* (only block hashes/metadata are gossiped first; full data is reconstructed from mempool) and *Optimistic Block Processing* (validators begin executing a block before consensus fully finalizes it), cutting time-to-finality.
- **Giga / Autobahn (in progress)** — the next-gen consensus rewrite separating block *proposal* from *execution* (asynchronous execution) and parallelizing block proposal across validators, targeting **200k+ TPS and sub-400ms finality**. Mainnet rollout targeted H1 2026; as of June 2026 it remains a rollout-in-progress, not a completed mainnet upgrade — slippage past mid-2026 is itself a trading signal.
- **Exchange-optimized design** — native price oracles, frequent-batch-auction-style matching support, and a focus on order-matching workloads underpin the "chain for trading" positioning.
- **[[cosmos|Cosmos SDK]] origin + [[proof-of-stake]]** — Sei began as a Cosmos-SDK chain and retains CometBFT-style PoS consensus, with the EVM layered on top in V2.

> Sei competes in the "parallelized execution" cohort alongside [[solana|Solana]], Monad, and [[hyperliquid|Hyperliquid]]'s HyperEVM — all racing toward exchange-grade throughput on smart-contract platforms.

---

## 2025–2026 Developments

- **2025-05-19 — Giga whitepaper** published (Autobahn consensus, async execution, 200k TPS / <400ms finality targets); mainnet rollout targeted H1 2026 — as of June 2026 it remains a rollout-in-progress, not yet a fully completed mainnet upgrade.
- **2025 — Wyoming WYST stablecoin pilot**: the Wyoming Stable Token Commission named **Sei and Aptos the final two candidate chains** for WYST, the first US state-issued stablecoin. Sei scored 30 points in the technical evaluation — above Avalanche, Ethereum and Algorand, behind only Aptos. SEI surged ~85% on the week of the news. WYST itself is fiat-backed and deployed via LayerZero's OFT standard. (Sources: Blockworks; crypto.news; coinedition.)
- **Institutional / policy positioning**: SEI appears in the World Liberty Financial portfolio; the WYST shortlisting cemented a "regulated US public-sector rails" narrative unusual among mid-cap L1s.
- **Price reality check**: despite the narratives, SEI made a cycle low of $0.0485 on 2026-03-31 (-95% from its March 2024 ATH of $1.14), weighed by L1 competition and continuous supply unlocks.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 6.73B SEI |
| **Total Supply** | 10.00B SEI |
| **Max Supply** | None (uncapped) |
| **Market Cap** | $369.8M |
| **FDV (on total supply)** | ≈ $549M |
| **MC / FDV** | ≈ 0.67 |

**Dilution flag.** ~3.27B SEI (≈33% of total supply) is yet to circulate, released on a multi-year unlock schedule covering team, investors, ecosystem, and foundation allocations. This is a *structural overhang*: MC/FDV ≈ 0.67 means roughly one-third of eventual supply will dilute holders as it vests. Rallies mechanically meet new supply at unlock cliffs — check the unlock calendar before swing longs ([[token-unlocks]]). SEI is a [[proof-of-stake]] gas/staking/governance token; staking emissions reward validators and delegators while diluting non-stakers.

---

## Valuation Framework

As a trading-focused L1, SEI's fundamentals tie to network usage and the realization of its institutional narratives (no invented values — pull live):

- **DeFi TVL** — value locked in Sei DeFi; a proxy for capital actually using the chain.
- **DEX / perp volume on Sei** — directly relevant given the "trading chain" thesis.
- **Network fees / REV** — transaction fees as the value-capture signal.
- **Daily active addresses / transactions** — adoption breadth.
- **Stablecoin supply on-chain** — settlement activity; especially relevant if WYST or other regulated stablecoins deploy.
- **Unlock schedule (MC vs FDV)** — the supply side; 0.67 MC/FDV is a headwind to factor into any valuation.

The bull case: Giga delivers exchange-grade performance and WYST/institutional rails drive real usage. The bear case: throughput is increasingly commoditized ([[solana|Solana]], Monad, [[hyperliquid|HyperEVM]]) and unlock dilution caps upside.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.14 (2024-03-16) |
| **All-Time Low** | $0.04470 (2026-03-31) |
| **Price (2026-06-20)** | $0.05491, mcap $369.8M, rank #123, ≈ -95.2% vs ATH |
| **24h Change (2026-06-20)** | +1.89% |
| **7d Change (2026-06-20)** | +0.30% |
| **Event move** | ~+85% week on Wyoming WYST finalist news (2025) |

> SEI is high-beta and event-driven; trades just ~23% above its all-time low (2026-06-20). Check live data before trading.

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1, parallelized EVM)

---

## Ecosystem & Use Cases

- **DeFi / DEXes** — spot and perp DEXes optimized for Sei's low-latency execution; the chain's reason for being.
- **Trading / exchange-style apps** — order-matching, oracle-heavy markets, and high-frequency on-chain workloads.
- **Institutional / regulated rails** — the WYST shortlisting and World Liberty Financial association position SEI for US public-sector/institutional stablecoin and RWA flows.
- **EVM dApps** — full Ethereum compatibility means any Solidity app can deploy with standard tooling, drawing from the EVM developer base.
- **Stablecoins** — a potential WYST deployment (or other regulated [[stablecoins]]) would anchor settlement activity on-chain.

---

## Market Structure & Derivatives

### Spot venues (centralized)

| Exchange | Pair |
|---|---|
| [[binance|Binance]] | SEI/USDT |
| [[kraken|Kraken]] | SEI/USD |
| Upbit | SEI/KRW |
| Bitget | SEI/USDT |
| KuCoin | SEI/USDT |
| Crypto.com Exchange | SEI/USDT |

### Derivatives / DEX

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | SEI-PERP | Perpetual |
| Binance / Bybit / OKX | SEI-PERP | Perpetual (CEX) |

- **Liquidity**: deep spot on Binance/Upbit; Korean (Upbit SEI/KRW) flow is significant in SEI. 24h volume ~$28.8M (2026-06-20).
- **Perps / funding / OI**: SEI-PERP on [[hyperliquid|Hyperliquid]] and major CEX futures allow basis and short expression. Funding/OI are worth tracking around unlock cliffs and the dated Giga/WYST catalysts.

---

## Trading Playbook

- **Catalyst pair**: the two dated catalysts are (1) **Giga mainnet activation** (targeted H1 2026 — slippage past mid-2026 is itself a signal) and (2) **WYST pilot outcome** — Wyoming choosing Sei over [[aptos|Aptos]] (or splitting deployment) would be a structural re-rate; losing to Aptos removes the narrative. Position around announcements, not the drift.
- **Narrative baskets**: parallelized-EVM / "trading chain" basket (vs [[solana]], Monad, [[hyperliquid]]'s HyperEVM) and the "US-regulated rails / state stablecoin" basket. SEI also carries World Liberty Financial political-flow association — headline-sensitive both ways. See [[narrative-trading]].
- **Unlock overhang**: MC/FDV 0.67 with ongoing unlocks means rallies meet mechanical supply; check the unlock calendar before swing longs ([[token-unlocks]]).
- **ATL proximity**: ~23% above the all-time low (2026-06-20); the March low is the structural support reference in this [[crypto-market-regimes|Established Bear Market]].
- **Relative-value**: SEI vs [[aptos|APT]] is a natural pair given the head-to-head WYST competition and overlapping parallelized-execution thesis ([[pairs-trading]]).

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.sei.io](https://www.sei.io) |
| **Twitter** | [@SeiNetwork](https://twitter.com/SeiNetwork) |
| **Reddit** | [https://www.reddit.com/r/Sei_Network/](https://www.reddit.com/r/Sei_Network/) |
| **Telegram** | [seinetwork](https://t.me/seinetwork) |
| **Discord** | [https://discord.com/invite/Sei](https://discord.com/invite/Sei) |
| **GitHub** | [https://github.com/sei-protocol](https://github.com/sei-protocol) |
| **Whitepaper** | [https://github.com/sei-protocol/sei-chain/blob/main/whitepaper/Sei_Whitepaper.pdf](https://github.com/sei-protocol/sei-chain/blob/main/whitepaper/Sei_Whitepaper.pdf) |

---

## Competitive Positioning

| Chain | Niche | Execution model | Token vs SEI (2026-06-20) | Notes |
|---|---|---|---|---|
| **Sei** | "Trading chain," parallelized EVM | Parallel EVM + Twin-Turbo/Giga | rank #123, ~$370M cap, MC/FDV 0.67 | WYST finalist; unlock overhang |
| [[aptos]] | Move L1, "global trading engine" | [[move-language|Move]] + Block-STM | rank #99, larger cap | Direct WYST rival; parallel-execution peer |
| [[solana]] | High-throughput L1 | Sealevel parallel | far larger | The throughput benchmark; deep DeFi |
| [[hyperliquid]] | Vertically-integrated perp DEX/L1 | HyperEVM | far larger | Absorbing trader mindshare Sei targets |
| Monad | Parallelized EVM L1 | Optimistic parallel EVM | newer entrant | Direct parallel-EVM competitor |

SEI's edge is end-to-end trading optimization plus the regulated-rails (WYST) narrative; its central competitive threat is [[hyperliquid|Hyperliquid]]'s vertically-integrated exchange, which has captured much of the on-chain-trading mindshare Sei was built to win.

---

## Risks

- **Unlock dilution** — ~33% of supply uncirculated (MC/FDV 0.67); a persistent structural headwind ([[token-unlocks]]).
- **Execution / timeline risk** — Giga is a rollout-in-progress; delays past H1 2026 are a negative signal.
- **Narrative-dependency** — much of SEI's premium rests on WYST and institutional rails; an adverse WYST outcome removes a core thesis.
- **Intense competition** — [[solana|Solana]], [[hyperliquid|Hyperliquid]], Monad, and [[aptos|Aptos]] all contest exchange-style workloads.
- **Political-flow sensitivity** — World Liberty Financial association makes SEI headline-sensitive in both directions.
- **Bear-market beta** — high-beta event-driven alt in an [[crypto-market-regimes|Established Bear Market]] (Fear & Greed 23), ~95% below ATH.

> Data disclaimer: market figures are point-in-time (2026-06-20). Crypto is volatile and high-risk; nothing here is investment advice. Verify against live data before trading.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[aptos]] (WYST rival finalist / parallel-execution peer)
- [[solana]]
- [[hyperliquid]]
- [[move-language]]
- [[proof-of-stake]]
- [[stablecoins]]
- [[token-unlocks]]
- [[narrative-trading]]
- [[pairs-trading]]
- [[crypto-market-regimes]]
- [[l1-l2-rotation]]

---

## Sources

- CoinGecko / cryptodataapi.com market snapshot, 2026-06-20 (current price, market cap, supply, ATH/ATL)
- CoinGecko top-1000 snapshot, 2026-04-09 (market data baseline)
- Blockworks — "Gaming-focused chain Sei surges 85% on the week — why?" (Wyoming WYST) — https://blockworks.com/news/sei-chain-surges-wyoming-tech
- crypto.news — "SEI price surges as Wyoming selects Sei Network for WYST stablecoin" — https://crypto.news/sei-price-surges-as-wyoming-selects-sei-network-for-wyst-stablecoin/
- coinedition — "SEI Price and Volume Surge After Wyoming Taps Network for Stablecoin Project" — https://coinedition.com/wyoming-selects-sei-network-stablecoin/
- Sei Network on X — Wyoming Stable Token Commission finalist announcement — https://x.com/SeiNetwork/status/1935846324932325857
- CoinMarketCap AI — Sei latest updates (Giga rollout targeting 200k TPS / sub-400ms finality, H1 2026) — https://coinmarketcap.com/cmc-ai/sei/latest-updates/
- Sei Giga whitepaper (2025-05-19) and Sei whitepaper — https://github.com/sei-protocol/sei-chain
- Messari — Sei Network profile — https://messari.io/project/sei-network/profile
- Web search verification via Perplexity/WebSearch, 2026-06-10.
