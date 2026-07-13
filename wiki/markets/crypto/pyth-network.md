---
title: "Pyth Network"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi]
aliases: ["PYTH"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://pyth.network/"
related: ["[[crypto-markets]]", "[[solana]]", "[[defi]]", "[[ethereum]]", "[[bitcoin]]", "[[hyperliquid]]", "[[chainlink]]"]
---

# Pyth Network

**Pyth Network** (ticker: PYTH) is a decentralised oracle network, native to [[solana]] but distributed across 50+ blockchains, designed to provide real-time financial market data (prices for crypto, equities, FX, and commodities) to decentralised applications (dApps). It sources first-party price data directly from major trading firms, exchanges, and market makers, and delivers low-latency, "pull"-based oracle feeds for mission-critical [[defi]] systems. PYTH is the network's governance token. Pyth is the second-largest oracle by integrations and total value secured, competing most directly with [[chainlink|Chainlink]].

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #136 |
| **Market Cap** | $290,377,707 (~$290.4M) |
| **Current Price** | $0.03687584 |
| **Fully Diluted Valuation** | $368,734,446 (~$368.7M) |
| **Market Cap / FDV** | ~0.79 |
| **24h Volume** | $15,677,631 (~$15.68M) |
| **24h Change** | +4.48% |
| **7d Change** | -2.03% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: with the market in **extreme fear** (Fear & Greed = 23) and an **Established Bear Market** regime as of 2026-06-20, PYTH trades at ~$0.0369, ranked #136, up ~4.5% over 24h but down ~2% on the week — a small relief bounce off a fresh all-time low ($0.0296, 2026-06-06) rather than a trend change. As a small-cap, lower-liquidity DeFi infrastructure token (24h volume ~$15.7M), PYTH is highly sensitive to thin order books and risk-off rotation out of altcoins, and remains ~97% below its March 2024 ATH of $1.20. MC/FDV near 0.79 means ~21% of supply is still locked, leaving structural unlock overhang. PYTH is correlated with the broader [[solana]] ecosystem and altcoin risk appetite.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PYTH |
| **Asset class** | Oracle / DeFi infrastructure governance token |
| **Native chain** | [[solana]] (Pythnet appchain; feeds delivered cross-chain to 50+ networks) |
| **Categories** | Infrastructure, Decentralized Finance (DeFi), Oracle, Analytics, Solana Ecosystem, Neon Ecosystem, Manta Network Ecosystem, Multicoin Capital Portfolio, GMCI DeFi Index, Delphi Ventures Portfolio, GMCI Index |
| **Website** | [https://pyth.network/](https://pyth.network/) |

> *Live price/market-cap/rank figures live in the single [Market Data](#market-data) snapshot above (2026-06-20); other sections reference that block rather than restating stale numbers.*

---

## Overview

Pyth Network is a decentralised oracle network that provides real-time financial market data to decentralised applications (dApps) across multiple blockchains. It allows developers to secure smart contracts with reliable, low-latency market data from institutional sources, and to build apps with high-fidelity oracle feeds designed for mission-critical systems.

Pyth's key differentiator is its **first-party data model**: rather than scraping public APIs or relying on third-party node operators (the [[chainlink|Chainlink]] approach), it aggregates price contributions directly from trading firms, exchanges, and market makers who publish their own proprietary data on-chain. It uses a **pull oracle** design — consumers request and pay for a fresh price update on demand, rather than the oracle continuously pushing prices — which is well suited to high-frequency, cross-chain use. Pyth's feeds underpin derivatives, lending, and perp protocols across the [[solana]] and EVM ecosystems.

### Use case / narrative / category

PYTH sits in the **oracle / DeFi infrastructure** category. Investment narratives around it center on: (1) growth in on-chain derivatives and perp DEXs that need fast, accurate price feeds; (2) expansion into traditional-finance market data via **Pyth Pro** (a large off-chain TAM historically dominated by Bloomberg/Refinitiv); and (3) the broader [[solana]] ecosystem cycle, given Pyth's Solana-native roots. As a governance token, PYTH's value accrual depends on adoption of paid data services and the governance/fee/staking mechanisms voted in by holders.

---

## Protocol & Technology

Pyth's architecture is built to push institutional-grade market data on-chain with minimal latency and to make it consumable on any chain.

### Pull-oracle design

Unlike "push" oracles (e.g. classic [[chainlink|Chainlink]] data feeds) that write prices to a destination chain on a fixed heartbeat/deviation schedule, Pyth uses a **pull (on-demand) model**:

- Publishers continuously stream prices into **Pythnet** (Pyth's dedicated Solana-based appchain), where they are aggregated into a single price plus a **confidence interval** per feed.
- The aggregated price is made available off-chain; a consumer dApp **pulls** the latest signed price and submits ("posts") it to its own chain only when it needs it, paying a small update fee.
- This shifts the gas/update cost to the moment of use, enables sub-second update frequency, and scales to 50+ chains without the oracle pre-paying to push every feed to every chain.

The **confidence interval** is a distinctive feature: each feed reports not just a price but a band reflecting publisher dispersion/uncertainty, which protocols can use to widen spreads or pause during volatile/illiquid conditions.

### First-party publishers

Pyth's data comes from **first-party publishers** — trading firms, exchanges, and market makers (e.g. major HFT shops and venues) who publish their own proprietary prices directly, rather than third-party nodes scraping public APIs. This is the core architectural bet versus [[chainlink|Chainlink]]: data closer to the source, with named, reputationally-accountable contributors, and the basis for **Oracle Integrity Staking** (publishers/stakers are economically accountable for accuracy).

### Cross-chain delivery (Wormhole)

Prices aggregated on Pythnet are attested and relayed cross-chain via **Wormhole**, allowing the same first-party price to be consumed on Solana, Ethereum and EVM L2s, and many non-EVM chains. This makes Pyth chain-agnostic infrastructure spanning the [[ethereum]], [[solana]], and broader multichain ecosystems.

### Feed coverage

Pyth provides feeds across multiple asset classes — **crypto, US/global equities, ETFs, FX, and commodities/metals** — making it one of the broadest cross-asset oracle networks and the bridge into the TradFi market-data narrative.

### Products beyond core price feeds

| Product | What it does |
|---|---|
| **Price Feeds** | Core real-time pull oracle: crypto, equities, FX, commodities, with confidence intervals. |
| **Pyth Pro** | Institutional/TradFi market-data subscription product — Pyth's push into the off-chain, paid market-data TAM (the Bloomberg/Refinitiv-style business). Key long-term value-accrual lever. |
| **Express Relay** | A marketplace connecting protocols (e.g. lending) to searchers/liquidators, reducing MEV extraction and giving protocols access to priority liquidation flow. |
| **Entropy** | On-chain verifiable randomness (VRF) for gaming, NFTs, and lotteries — extends Pyth beyond pricing. |
| **Benchmarks** | Historical price data for backtesting, settlement, and dispute resolution. |
| **Oracle Integrity Staking (OIS)** | Staking layer that economically backs feed accuracy; PYTH stakers delegate to publishers and share rewards/slashing tied to data quality. |

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 7,874,981,857 (~7.875B PYTH) |
| **Total Supply** | 10,000,000,000 (10.00B PYTH) |
| **Max Supply** | 10,000,000,000 (10.00B PYTH) |
| **Market Cap / FDV** | ~0.79 |
| **FDV** | $368,734,446 (~$368.7M, see [Market Data](#market-data)) |

- **Dilution flag** — circulating supply (~7.875B) is ~79% of the 10B max (MC/FDV ~0.79), so ~2.1B PYTH remains locked. Scheduled unlocks (originally distributed across publisher rewards, ecosystem growth, protocol development, community/launch, and private allocations with cliffs/vesting) represent ongoing structural sell pressure, though the locked share is far smaller than at launch.
- **Governance** — PYTH is a governance token: holders vote on data-fee parameters, feed listings/update fees, reward distribution, and protocol upgrades via the Pyth DAO.
- **Value accrual** — driven by (1) **on-chain update fees** paid by dApps pulling prices, (2) **Pyth Pro** subscription revenue from institutional/TradFi consumers, and (3) **Oracle Integrity Staking**, where PYTH is staked to/delegated against publishers to back data accuracy and earn rewards (with slashing risk). Whether and how this revenue routes to token holders is a governance-dependent, evolving question — the central debate for PYTH's fundamental value.

---

## Ecosystem & Use Cases

Pyth feeds are consumed by hundreds of protocols across many chains:

- **Perp DEXs / derivatives** — fast, low-latency feeds are critical for perpetual-futures and options venues that mark positions and trigger liquidations in real time (a category where the pull model's sub-second freshness is a genuine edge).
- **Lending / money markets** — collateral valuation and liquidation triggers depend on accurate prices; confidence intervals let protocols pause or widen during stress.
- **Stablecoins / synthetics** — peg monitoring and minting/redemption pricing.
- **Cross-asset apps** — equities/FX/commodity feeds enable tokenized-RWA and TradFi-bridging products.

Heaviest usage clusters in the [[solana]] ecosystem (Pyth's home) and across [[ethereum]] L2s and other EVM chains reached via Wormhole.

---

## Market Structure & Derivatives

- **Spot venues** — listed on major CEXs including Binance, Kraken, Upbit (KRW), Bitget, KuCoin, and Crypto.com Exchange; DEX spot on Solana (Orca and others).
- **Derivatives** — **PYTH-PERP on [[hyperliquid|Hyperliquid]]** is the principal on-chain perpetuals venue; perps are also offered on major CEX derivatives desks. Funding rates and open interest should be monitored for positioning/leverage signals; specific live funding/OI values are not stated here to avoid fabrication — pull them from the venue at trade time.
- **Liquidity caveat** — at ~$15.7M 24h volume, PYTH is a thin small-cap; size trades carefully and expect slippage in risk-off tape.

### Exchange Listings

#### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PYTH/USDT | N/A |
| Kraken | PYTH/USD | N/A |
| Upbit | PYTH/KRW | N/A |
| Bitget | PYTH/USDT | N/A |
| KuCoin | PYTH/USDT | N/A |
| Crypto.com Exchange | PYTH/USD | N/A |

#### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | PYTH-PERP | Perpetual |
| Orca | HZ1JOVNIVVGRGNIIYVEOZEVGZ58XAU3RKWX8EACQBCT3/SO11111111111111111111111111111111111111112 | Spot |

---

## Valuation Framework

PYTH has no claim on a hard NAV; value is a function of network adoption and how much of it routes to the token. Metrics to track:

| Metric | Why it matters |
|---|---|
| **Number of price feeds** | Breadth of coverage (crypto/equities/FX/commodities); proxy for product surface. |
| **Total Value Secured (TVS)** | Aggregate value of positions/collateral relying on Pyth feeds; the core "demand" metric and the head-to-head vs [[chainlink|Chainlink]]. |
| **Publisher count** | Number of first-party data contributors; depth/decentralization of the data layer. |
| **On-chain update-fee volume** | Direct, usage-linked protocol revenue from pull updates. |
| **Pyth Pro subscriptions/revenue** | The TradFi/off-chain market-data TAM — the biggest long-term value lever if it gains traction. |
| **PYTH staked in OIS** | Economic security backing data accuracy; staking participation signals holder conviction and reduces float. |
| **Chains integrated** | Distribution moat (50+ via Wormhole). |

The bull case is "the AWS of market data" capturing both on-chain fees and a slice of the multi-billion-dollar TradFi data market; the bear case is that fees stay small, value accrual to the token stays ambiguous, and unlocks outpace demand.

---

## Trading Playbook

- **Narrative driver** — PYTH trades as **oracle/DeFi-infra beta** layered on **[[solana]] ecosystem beta**. It tends to rip on Solana-DeFi and perp-DEX volume narratives and bleed in risk-off altcoin tapes (current regime).
- **Catalysts to watch** — Pyth Pro adoption/revenue updates, OIS staking milestones, new chain/feed integrations, TVS overtaking or losing ground vs [[chainlink|Chainlink]], and major perp/derivatives protocols adopting (or dropping) Pyth.
- **Structural headwinds** — ~2.1B locked PYTH (MC/FDV ~0.79) and ongoing unlocks; ambiguous token value accrual; thin liquidity.
- **Levels** — fresh ATL $0.0296 (2026-06-06) is the key support; ATH $1.20 is a distant reference. Current ~$0.0369 print is a bounce within an established downtrend, not a confirmed reversal.
- **Venue** — [[hyperliquid|Hyperliquid]] PYTH-PERP for liquid directional/leveraged exposure; CEX spot for the cleaner book.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.20 (2024-03-16) |
| **Current vs ATH** | ~-97% |
| **All-Time Low** | $0.02962831 (2026-06-06) — current cycle low |
| **Prior ATL (historical)** | $0.0368 (2026-03-28) — superseded by the June 2026 low |
| **24h Change** | +4.48% |
| **7d Change** | -2.03% |

> See the single [Market Data](#market-data) snapshot for current price/market-cap/rank.

---

## History

- **2021** — Pyth launches on [[solana]], pioneering the first-party-publisher oracle model with a network of trading firms and market makers.
- **Nov 2023** — PYTH token generation event and airdrop to early users/integrators; CEX listings follow.
- **2024-03-16** — PYTH prints its all-time high of $1.20 during the early-2024 alt rally.
- **2024-2025** — Cross-chain expansion via Wormhole to 50+ networks; broadening into equities, FX, and commodities feeds; rollout of Express Relay and Entropy; **Oracle Integrity Staking** goes live to economically back feed accuracy.
- **2025-2026** — Launch/positioning of **Pyth Pro** to attack the institutional TradFi market-data market; PYTH grinds down with the broader altcoin bear.
- **2026-06-06** — New all-time low of $0.0296 amid the Established Bear Market and extreme-fear regime.

---

## Competitive Positioning

| Oracle | Model | Chains | Token | Edge / positioning |
|---|---|---|---|---|
| **Pyth Network** | Pull, first-party publishers | [[solana]] native + 50+ via Wormhole | PYTH | Low-latency, sub-second feeds; named institutional publishers; confidence intervals; cross-asset (crypto/equities/FX/commodities); Pyth Pro into TradFi data |
| **[[chainlink]]** | Push, third-party node operators | Ethereum/EVM-first, very broad | LINK | Incumbent; largest TVS and integrations; CCIP, Proof of Reserve, VRF, Automation; deepest enterprise/TradFi partnerships |
| **RedStone** | Pull (modular), supports many chains | Multichain | RED | Gas-efficient modular feeds; strong in LST/LRT and long-tail assets |
| **Chronicle** | Push, scalable verification | Ethereum/EVM | (none/native) | MakerDAO-origin; gas-optimized, used heavily by Sky/Maker ecosystem |
| **API3** | First-party (dAPIs), OEV auctions | Multichain | API3 | First-party via "Airnode"; Oracle Extractable Value capture returned to dApps |

Pyth's clearest structural advantage is latency + first-party data for high-frequency consumers (perp DEXs), plus the cross-asset/Pyth Pro TradFi angle; [[chainlink|Chainlink]] retains the incumbency, broadest integration footprint, and enterprise relationships.

---

## Platform & Chain Information

**Native Chain:** Solana (Pythnet appchain; feeds relayed cross-chain via Wormhole)

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `HZ1JovNiVvGrGNiiYvEozEVgZ58xaU3RKwX8eACQBCt3` |
| Neon Evm | `0x0575dd4afd93b7522fee4e0179f243eca3856137` |
| Manta Pacific | `0x90e95735378a31bfad2dcd87128fbb80ffeb6917` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://pyth.network/](https://pyth.network/) |
| **Twitter** | [@PythNetwork](https://twitter.com/PythNetwork) |
| **Telegram** | [Pyth_Network](https://t.me/Pyth_Network) (10,678 members) |
| **Discord** | [https://discord.com/invite/PythNetwork](https://discord.com/invite/PythNetwork) |
| **GitHub** | [https://github.com/pyth-network/](https://github.com/pyth-network/) |
| **Whitepaper** | [https://pyth.network/whitepaper_v2.pdf](https://pyth.network/whitepaper_v2.pdf) |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

- **Token unlock / dilution** — circulating supply (~7.875B) is below the 10B max (MC/FDV ~0.79), so scheduled unlocks of the remaining ~2.1B represent ongoing structural sell pressure.
- **Oracle competition** — Pyth competes with entrenched incumbents (notably [[chainlink|Chainlink]]) and challengers (RedStone, Chronicle, API3) for oracle market share; losing integrations would impair fee/adoption-driven value accrual.
- **Smart-contract / oracle-integrity risk** — DeFi protocols depend on oracle correctness; price-feed manipulation, stale/laggy data, or contract bugs could cascade into protocol losses and reputational damage.
- **Value-accrual ambiguity** — how on-chain fees, Pyth Pro revenue, and OIS rewards ultimately benefit PYTH holders is governance-dependent and still evolving; usage growth may not translate to token value.
- **Liquidity & volatility** — as a small cap with low 24h volume (~$15.7M), PYTH is prone to slippage, thin order books, and sharp moves; PYTH-PERP on [[hyperliquid|Hyperliquid]] is the liquid derivatives venue.
- **Ecosystem beta & macro/regime risk** — PYTH is correlated with the [[solana]] ecosystem and broad altcoin risk appetite, leaving it exposed to the prevailing **Established Bear Market** and extreme-fear (Fear & Greed = 23) conditions as of 2026-06-20.

---

## Related / See Also

- [[crypto-markets]]
- [[solana]]
- [[ethereum]]
- [[defi]]
- [[chainlink]] — primary oracle competitor
- [[hyperliquid]] — PYTH-PERP venue
- [[bitcoin]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot, 2026-06-20 (cryptodataapi.com / CoinGecko)
- Pyth Network whitepaper v2 — https://pyth.network/whitepaper_v2.pdf
- Pyth Network docs — https://docs.pyth.network/
