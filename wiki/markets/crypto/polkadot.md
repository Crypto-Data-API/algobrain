---
title: "Polkadot"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives]
aliases: ["DOT", "Polkadot Network"]
entity_type: protocol
founded: 2020
headquarters: "Decentralized (Web3 Foundation: Zug, Switzerland; Parity Technologies)"
website: "https://polkadot.com/"
related: ["[[base]]", "[[crypto-markets]]", "[[ethereum]]", "[[gavin-wood]]", "[[hyperliquid]]", "[[narrative-trading]]", "[[proof-of-stake]]", "[[staking]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[pairs-trading]]"]
---

# Polkadot

**Polkadot** (DOT) is a layer-0 multichain protocol founded by Ethereum co-founder Gavin Wood (Web3 Foundation/Parity), which lets heterogeneous blockchains ("parachains") share pooled security and pass messages trust-free. Once a top-5 asset ($55 ATH, Nov 2021), DOT has been one of the cycle's most severe underperformers — down ~98% from ATH — even as the network ships its largest technical overhaul (Polkadot 2.0 → **JAM**) and got its first **US spot ETF (21Shares TDOT, Nasdaq, 2026-03-06)**.

---

## Market Data

| Metric | Value |
|---|---|
| **Rank** | #51 |
| **Price** | $0.9645 |
| **Market Cap** | $1.63 billion |
| **24h Volume** | $84.34 million |
| **24h Change** | +0.86% |
| **7d Change** | -2.38% |
| **Circulating Supply** | 1,689,529,335 DOT |
| **Total Supply** | 1,689,529,335 DOT |
| **Max Supply** | 2,100,000,000 DOT (hard cap adopted via governance) |
| **All-Time High** | $54.98 (2021-11-04) — currently -98.2% |
| **All-Time Low** | $0.892875 (2026-06-06) — currently +7.96% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** [[crypto-market-sentiment|Fear & Greed]] = **22 (Extreme Fear)**; **Established Bear Market**. DOT printed a **fresh all-time low of $0.8929 on 2026-06-06** — breaking below the prior $1.15 (Feb 2026) low — and now trades just ~8% above it, having slipped to **rank #51** (sub-$2B market cap). It is the single weakest of the six flagships: a layer-0 interop bet that the market has comprehensively de-rated despite the JAM upgrade and a live US ETF.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DOT |
| **Type** | Layer-0 / smart-contract platform; NPoS [[staking]] |
| **Market Cap** | $1.63B, rank #51 (2026-06-20) |
| **ATH / drawdown** | $54.98 (2021-11-04); **~-98%** to a new ATL of **$0.8929 (2026-06-06)** |
| **Supply** | ~1.69B DOT circulating; **2.1B hard cap** adopted via governance (replacing unlimited ~10%/yr inflation) |
| **Founder** | [[gavin-wood\|Gavin Wood]] (Ethereum co-founder; Web3 Foundation / Parity) |
| **ETF** | 21Shares Polkadot ETF (TDOT), Nasdaq, launched 2026-03-06, ~$11M seed, 0.30% fee — first US spot DOT ETF; Grayscale conversion also filed |
| **Major upgrade** | JAM (Join-Accumulate Machine) — Gray Paper v1.0 targeted ~mid-2026; public JAM testnet live Jan 2026 |
| **Categories** | Smart Contract Platform, Layer 0, Proof of Stake, Polkadot Ecosystem |
| **Website** | [https://polkadot.com/](https://polkadot.com/) |

---

## Overview

Polkadot is a platform that allows diverse blockchains to transfer messages, including value, in a trust-free fashion, sharing their unique features while pooling their security — a scalable heterogeneous multi-chain. It is heterogeneous because it makes no assumption about the nature or structure of the chains in the network; even non-blockchain systems can become parachains if they fulfill a set of criteria. Polkadot can be considered a set of independent chains with pooled security and trust-free interchain transactability. Native parachains are typically built with Parity's Substrate SDK.

### 2025–2026 developments

- **Polkadot 2.0 shipped (2024–2025)**: Agile Coretime replaced parachain slot auctions (blockspace bought on demand), plus Async Backing and Elastic Scaling — making blockspace a flexible commodity rather than a 2-year lease.
- **JAM ("Polkadot 3.0")**: Gavin Wood's Join-Accumulate Machine re-architects the relay chain into a decentralized global computer supporting RISC-V execution and smart contracts at the core layer. Gray Paper reached v0.8 in late 2025 with **v1.0 targeted before mid-2026**; first **public JAM testnet launched January 2026**; mainnet upgrade subject to OpenGov referendum, with CoreChain phases through 2026.
- **Tokenomics shift**: governance approved moving from unlimited inflation toward a **2.1B DOT hard cap** with decaying issuance — a structural bull argument repeatedly cited against the price weakness.
- **US ETF**: after repeated SEC delays through 2025 (21Shares, Grayscale filings; decision pushed to Nov 2025 under the new generic listing standards), **21Shares launched TDOT on Nasdaq 2026-03-06** — first US spot Polkadot ETF ($11M seed, 30bps). Inflows have been modest, mirroring other small-cap alt ETFs.
- **Price**: DOT first bottomed at **$1.15 on 2026-02-06**, then broke to a **fresh ATL of $0.8929 on 2026-06-06** — underperformance blamed on legacy slot-auction supply overhang, weak parachain activity/DeFi TVL versus rivals ([[solana|Solana]], L2s), and narrative rotation away from "interop" plays.

---

## Technology & Consensus

Polkadot is a **layer-0 / heterogeneous multichain**: a central **relay chain** provides shared security and cross-chain messaging ([[xcm|XCM]]) to many application-specific chains ("parachains"), typically built with Parity's **Substrate** SDK.

- **Consensus:** **Nominated Proof-of-Stake (NPoS)** — validators secure the relay chain; nominators (DOT stakers) back validators and share rewards/slashing. Block authoring (BABE) and finality (GRANDPA) are separated, giving deterministic finality.
- **Shared security:** parachains rent the relay chain's validator set rather than bootstrapping their own — the core "pooled security" value proposition.
- **Polkadot 2.0 (2024-25):** **Agile Coretime** replaced the old 2-year parachain slot auctions — blockspace ("coretime") is now bought on demand as a flexible commodity. Combined with **Async Backing** and **Elastic Scaling**, this sharply improved throughput and lowered the barrier to launching a chain.
- **JAM ("Polkadot 3.0"):** [[gavin-wood|Gavin Wood's]] **Join-Accumulate Machine** re-architects the relay chain into a decentralized global computer with **RISC-V** execution and smart contracts at the core layer. Gray Paper reached v0.8 in late 2025 with **v1.0 targeted before mid-2026**; the first **public JAM testnet launched January 2026**. Mainnet activation is subject to an OpenGov referendum, with CoreChain phases through 2026. JAM is the central re-rating catalyst — and the central execution risk (complexity/delay).

---

## Tokenomics & Supply Schedule

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.69B DOT |
| **Total Supply** | 1.69B DOT |
| **Max Supply** | 2.10B DOT (hard cap adopted via governance) |
| **MC / FDV** | ~1.00 (against the current circulating base) |

- **From inflation to a hard cap:** DOT historically ran **unlimited ~10%/yr inflation** (funding staking rewards and the treasury). Governance approved a transition toward a **2.1B DOT hard cap with decaying issuance** — a structural bull argument repeatedly cited against the price weakness.
- **Staking:** high participation (~50%+ historically) at ~7-14% nominal yields. Issuance changes under the hard cap directly alter **real yield** and sell-pressure math — a key valuation input.
- **Treasury:** a large on-chain treasury (governed by **OpenGov** referenda) funds ecosystem development; disbursements and unspent-balance burns are effective supply events.
- **No venture unlock overhang** against the current circulating base (MC/FDV ≈ 1.0 vs circulating), though the hard-cap headroom (to 2.1B) is future issuance.

---

## Ecosystem & Use Cases

Polkadot's thesis is **interoperability and shared security** for app-specific chains, but parachain activity and DeFi TVL have lagged rivals badly — the core of the bear case.

- **Notable parachains:** Moonbeam (EVM-compatible smart contracts), Acala (DeFi/stablecoin), Astar, HydraDX/Hydration (DeFi liquidity), Bifrost (liquid staking), Phala (compute).
- **Tooling:** **Substrate** SDK and the **polkadot-sdk** are widely used even outside Polkadot (e.g., some appchains/L2 stacks borrow Substrate components).
- **Cross-chain:** **XCM** for trust-minimized messaging between parachains; bridges to [[ethereum|Ethereum]] and others. Bridged ERC-20 DOT representations trade on Base/Arbitrum/OP/BNB.
- **JAM future:** if delivered, JAM aims to make the relay chain itself a general-purpose execution environment, blurring the parachain/L1 distinction.

---

## Trading Relevance

- **Where it trades**: deep spot everywhere — Binance, Coinbase, Kraken, Upbit (KRW), Bitget, KuCoin, Crypto.com; perps on [[hyperliquid|Hyperliquid]] (DOT-PERP), Binance, Bybit, OKX. ~$135M daily spot volume (April 2026 snapshot). Also bridged ERC-20 representations on Base/Arbitrum/OP/BNB.
- **Narrative basket**: "2017–2021 large-cap dinosaur" basket (with ADA, ATOM) — chronically heavy in alt seasons; traders use DOT/BTC and DOT/SOL ratios as a measure of old-gen vs new-gen rotation. Potential re-rating catalysts: **JAM mainnet referendum**, hard-cap issuance milestones, ETF inflow surprises.
- **ETF angle**: TDOT gives US tradfi access; watch creations/redemptions as a sentiment tell for small-cap alt ETFs generally.
- **Staking/supply**: high staking participation (~50%+ historically) at ~7–14% nominal yields; issuance changes under the hard cap alter real yield and sell-pressure math.
- **Risks**: continued ecosystem attrition, JAM delays/complexity, and the possibility that ETF access without organic demand simply adds exit liquidity.

---

## Market Structure & Derivatives

| Characteristic | Detail |
|---|---|
| **Rank** | #51 |
| **24h Volume** | $84.34M (2026-06-20) |
| **Liquidity** | Deep spot ([[binance]], [[coinbase]], Kraken, Upbit KRW, Bitget, KuCoin, Crypto.com) |
| **Volatility / beta** | High beta; chronic alt-season laggard |
| **Primary spot pairs** | DOT/USDT ([[binance]]), DOT/USD ([[coinbase]], Kraken), DOT/KRW (Upbit) |
| **Primary perp** | DOT-PERP ([[hyperliquid]]) + Binance, Bybit, OKX |
| **ETFs** | 21Shares **TDOT** (Nasdaq, live 2026-03-06); Grayscale conversion filed |

DOT [[funding-rate|funding]]/[[open-interest]] are thin relative to the majors given the small market cap; TDOT creations/redemptions act as a sentiment tell for small-cap alt ETFs generally. In the current Extreme-Fear regime, alt-ETF inflows have been modest. *(Flow magnitudes vary daily and are not quoted here to avoid stale figures.)*

---

## On-chain & Valuation Frameworks

| Metric | What it measures | Trading use |
|---|---|---|
| **Staking ratio / real yield** | % of DOT staked and net-of-issuance yield | Float scarcity + sell-pressure math (changes under hard cap) |
| **Coretime sales** | Demand for parachain blockspace (post-2.0) | Genuine usage signal vs old slot-auction model |
| **Parachain TVL / activity** | Ecosystem health | Tests the interop thesis (historically weak) |
| **Treasury balance / spend** | OpenGov disbursements & burns | Effective supply events |
| **DOT/BTC, DOT/SOL** | Relative strength | Old-gen vs new-gen rotation timing |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $54.98 (2021-11-04) — currently -98.2% |
| **All-Time Low** | $0.8929 (2026-06-06) — currently +7.96% |
| **24h Change** | +0.86% |
| **7d Change** | -2.38% |

> *Price figures as of 2026-06-20 (CoinGecko).*

---

## Platform & Chain Information

**Native Chain:** Polkadot relay chain (the addresses below are bridged ERC-20 representations)

### Contract Addresses (bridged representations)

| Chain | Address |
|---|---|
| Ethereum | `0x196c20da81fbc324ecdf55501e95ce9f0bd84d14` |
| Binance Smart Chain | `0x8d010bf9c26881788b4e6bf5fd1bdc358c8f90b8` |
| Base | `0x8d010bf9c26881788b4e6bf5fd1bdc358c8f90b8` |
| Optimistic Ethereum | `0x8d010bf9c26881788b4e6bf5fd1bdc358c8f90b8` |
| Arbitrum One | `0x8d010bf9c26881788b4e6bf5fd1bdc358c8f90b8` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | DOT/USDT |
| Kraken | DOT/USD |
| Upbit | DOT/KRW |
| Bitget | DOT/USDT |
| KuCoin | DOT/USDT |
| Crypto.com Exchange | DOT/USD |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | DOT-PERP | Perpetual |

### ETFs

| Product | Venue | Launched |
|---|---|---|
| 21Shares Polkadot ETF (TDOT) | Nasdaq | 2026-03-06 |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://polkadot.com/](https://polkadot.com/) |
| **Twitter** | [@Polkadot](https://twitter.com/Polkadot) |
| **Reddit** | [r/Polkadot](https://www.reddit.com/r/Polkadot) |
| **Telegram** | [PolkadotOfficial](https://t.me/PolkadotOfficial) |
| **Discord** | [https://discord.com/invite/polkadot](https://discord.com/invite/polkadot) |
| **GitHub** | [paritytech/polkadot-sdk](https://github.com/paritytech/polkadot-sdk) |
| **Whitepaper** | [Polkadot whitepaper (PDF)](https://polkadot.com/papers/Polkadot-whitepaper.pdf) |

---

## Competitive Positioning

Polkadot competes with other **interop/shared-security** platforms (Cosmos, [[ethereum|Ethereum's]] L2/restaking stack) and, in trading terms, sits in the **"2017-2021 large-cap dinosaur" rotation basket** with [[cardano|ADA]] and ATOM.

| Asset | Rank | Mkt Cap | Consensus | Core thesis |
|---|---|---|---|---|
| **Polkadot (DOT)** | #51 | $1.63B | NPoS (layer-0) | Shared-security multichain; JAM upgrade |
| [[bitcoin\|Bitcoin (BTC)]] | #1 | $1.27T | [[proof-of-work]] | Digital gold |
| [[ethereum\|Ethereum (ETH)]] | #2 | $208B | [[proof-of-stake]] | Modular settlement + L2s (the interop rival) |
| [[solana\|Solana (SOL)]] | #7 | $41.5B | PoH + [[proof-of-stake\|PoS]] | Monolithic high-throughput L1 |
| [[cardano\|Cardano (ADA)]] | #18 | $6.1B | Ouroboros [[proof-of-stake\|PoS]] | Same "old L1" rotation basket |

> Peer market data as of 2026-06-20 (CoinGecko). DOT is the most de-rated of the six flagships — bull case rests on JAM delivery + hard-cap issuance; bear case is chronic ecosystem attrition. Polkadot is often framed as "what Eth2 could have been," given [[gavin-wood|Gavin Wood's]] [[ethereum|Ethereum]] co-founding. See [[narrative-trading]].

---

## Regulatory

- **ETF:** after repeated SEC delays through 2025, **21Shares launched TDOT on Nasdaq (2026-03-06)** — the first US spot Polkadot ETF — under the SEC's newer generic listing standards; a Grayscale conversion is also filed.
- **Securities status:** DOT's earlier engagement with the SEC (including a "morphing token" argument that it had become sufficiently decentralized) is part of its compliance narrative; spot-ETF approval signals eased classification risk.
- **EU:** Web3 Foundation's Swiss base and MiCA apply to service providers.

---

## Risks

- **Ecosystem attrition** — weak parachain activity and DeFi TVL versus [[solana|SOL]]/L2s; the interop narrative has lost mindshare.
- **JAM execution risk** — the upgrade is ambitious and complex; delays or a contentious OpenGov referendum would disappoint.
- **Supply overhang** — legacy slot-auction unlocks and future issuance toward the 2.1B cap.
- **ETF without demand** — TDOT access may simply provide exit liquidity if organic demand stays absent (inflows have been modest).
- **Severe drawdown / liquidity** — ~98% off ATH at a fresh all-time low, sub-$2B cap with thin derivatives liquidity amplifies moves.

> **Risk warning:** Crypto assets are highly volatile and speculative. Nothing here is investment advice. DOT is at a fresh all-time low in the current Extreme-Fear / bear regime; small-cap, low-liquidity dynamics raise execution risk.

---

## Related

- [[crypto-markets]]
- [[ethereum]] — Gavin Wood co-founded it; Polkadot is the "what Eth2 could have been" counterfactual and the interop rival
- [[solana]] / [[cardano]] — L1 peers; ADA shares the "old L1" rotation basket
- [[bitcoin]] — macro anchor
- [[gavin-wood]] — founder
- [[proof-of-stake]] / [[staking]] — consensus and yield
- [[hyperliquid]] / [[funding-rate]] / [[open-interest]] — perp venue & toolkit
- [[narrative-trading]] — legacy-L1 rotation basket
- [[etf]] / [[bitcoin-etf]] — alt-ETF wave context

---

## Sources

- Nasdaq / ETFGI, "21Shares launches Polkadot ETF (TDOT) in the United States" (2026-03-06) — https://etfgi.com/news/stories/2026/03/21shares-launches-polkadot-etf-tdot-united-states ; https://www.nasdaq.com/press-release/21shares-launches-polkadot-etf-tdot-united-states-2026-03-06
- Nasdaq Trader info circular, TDOT trading begin 2026-03-06 — https://www.nasdaqtrader.com/content/newsalerts/2026/InfoCircular/TDOT_Circular_NQ.pdf
- Polkadot Forum, "Polkadot 3.0 — the JAM upgrade" — https://forum.polkadot.network/t/polkadot-3-0-the-jam-upgrade/13834
- Coin Bureau, "Polkadot (DOT) Review 2026: JAM, Hard Cap & The Honest Verdict" — https://coinbureau.com/review/polkadot-dot
- CoinDesk, "21Shares Polkadot ETF plan progresses with Nasdaq filing" (2025-03-18) — https://www.coindesk.com/markets/2025/03/18/21shares-polkadot-etf-plan-progresses-with-nasdaq-filing-for-listing-approval
- CoinGecko top-1000 snapshot (2026-04-09), original auto-generated data
- Verified via web search, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 831.62M DOT |
| **Total Supply** | 881.62M DOT |
| **Max Supply** | 1.00B DOT |
| **Fully Diluted Valuation** | $1.76M |
| **Market Cap / FDV Ratio** | 0.94 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $181,073.00 |
| **Market Cap Rank** | #2405 |
| **24h Range** | $0.00164636 — $0.00222764 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

DOT is a **two-venue liquid market**: tradable on **[[binance]]** (deep DOT/USDT spot plus a **USD-margined perpetual**) and on **[[hyperliquid]]** (**DOT-PERP**, up to ~40-50x leverage). Binance provides the primary spot and stablecoin-margined perp depth used for hedging and cash-and-carry; Hyperliquid supplies transparent on-chain funding, mark, and L2 depth. Because two liquid derivatives venues quote the same asset, **execution and sizing benefit from split routing** (spread limit orders across both books rather than sweeping one), and the pair enables **CEX-vs-DEX funding and basis** trades. That said, DOT is a sub-$2B, rank-~55 alt: order-book depth is **thin relative to the majors**, so large clips move price and funding can swing sharply — size positions to the shallower of the two books and expect wider slippage than BTC/ETH.

### Applicable strategies

- [[cash-and-carry]] — long Binance spot DOT versus short the USD-margined perp to harvest positive basis; two liquid venues make the hedge clean.
- [[funding-rate-harvest]] — collect perp funding on DOT-PERP; small-cap alt funding is more volatile than majors, offering richer (if noisier) carry.
- [[hl-vs-cex-funding-divergence]] — arbitrage funding gaps between Hyperliquid DOT-PERP and Binance's perp, which diverge more on thinly-traded alts.
- [[liquidation-cascade-fade]] — DOT's thin derivatives depth means forced liquidations overshoot; fade the flush and cover into the [[post-liquidation-rebound]].
- [[pairs-trading]] — trade DOT against same-basket old-L1 peers (ADA, ATOM, SOL) via the DOT/BTC and DOT/SOL ratios traders already track for old-gen vs new-gen rotation.
- [[oi-price-exhaustion]] — pair [[open-interest]] with price to time exhaustion in a chronically de-rated, low-float derivatives market prone to crowded positioning.

### Volatility & regime character

DOT is a **high-beta, large-cap "old-L1" altcoin** — an infra/interop (layer-0 shared-security) token, not a memecoin or stablecoin. It carries strong **positive beta to BTC and ETH** and typically **amplifies moves on the downside**: it is the most de-rated of the six flagships (~-98% off ATH, at fresh all-time lows) and a chronic **alt-season laggard**. Its idiosyncratic drivers — JAM upgrade progress, hard-cap issuance milestones, TDOT ETF flows — sit on top of, not instead of, broad crypto-beta. In risk-off / Extreme-Fear regimes it tends to underperform; in alt rallies it can snap higher from a compressed base.

### Risk flags

- **Venue / liquidity concentration** — sub-$2B cap with **thin funding/OI and shallow books**; slippage and gap risk are elevated versus majors, and depth is split across just two derivatives venues.
- **Supply / issuance** — legacy slot-auction supply overhang plus future issuance toward the **2.1B hard cap**; staking-yield and issuance changes shift real float and sell-pressure.
- **Narrative dependence** — the interop thesis has lost mindshare; price is heavily tied to **JAM delivery** and rotation sentiment, so headline/referendum risk is high.
- **Perp funding dislocations** — on a low-liquidity alt, funding can spike and flip fast; crowded positioning and liquidation cascades overshoot both directions.
- **ETF-without-demand** — TDOT access may add exit liquidity rather than organic bid if inflows stay modest.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=DOT` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=DOT` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=DOT&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=DOT&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=DOT"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[base]]

---
