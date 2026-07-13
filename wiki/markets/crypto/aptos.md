---
title: "Aptos"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, defi]
aliases: ["APT", "Aptos Network"]
entity_type: protocol
founded: 2021
headquarters: "Palo Alto, USA (Aptos Labs); network decentralized"
website: "https://aptosfoundation.org"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[solana]]", "[[hyperliquid]]", "[[sui]]"]
---

# Aptos

**Aptos** (APT) is a high-performance [[proof-of-stake]] Layer 1 [[blockchain]] built on the [[move-language|Move language]] and Move VM by the ex-Meta team behind Diem (mainnet launched October 2022). Despite a brutal multi-year price decline, the network's fundamentals diverged sharply upward in 2025-26 — DeFi TVL crossed $1B, stablecoin supply hit records, and APT became one of the first tokens formally classified as a digital commodity under CFTC oversight (March 2026). That price/fundamentals divergence is the core APT trading story, and as of June 2026 the token trades within cents of its all-time low against an [[crypto-market-regimes|Established Bear Market]] backdrop (Fear & Greed 23 — extreme fear).

---

## Market Data

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $0.6353 |
| **Market Cap** | $528.5M |
| **Market Cap Rank** | #99 |
| **24h Volume** | $43.2M |
| **24h Change** | +2.19% |
| **7d Change** | -4.95% |
| **Circulating Supply** | 832.1M APT |
| **Total Supply** | 1.20B APT |
| **Max Supply** | 2.10B APT |
| **All-Time High** | $19.92 (2023-01-26) — ≈ -96.8% |
| **All-Time Low** | $0.6097 — APT trades just ~4% above its ATL |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

> Earlier snapshots: 2026-04-09 (CoinGecko) rank #84, market cap $654.55M, price $0.8238.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | APT |
| **Market Cap Rank** | #99 (2026-06-20) |
| **Market Cap** | $528.5M at $0.6353 (2026-06-20) |
| **Sector** | Layer 1, Smart Contract Platform, [[move-language|Move]] ecosystem |
| **Chain** | Own L1 (Move VM, parallel execution via Block-STM) |
| **Supply mechanics** | 832.1M circulating / 1.20B total / 2.1B max; ongoing staking emissions and investor/foundation unlocks |
| **Regulatory status** | Classified as a digital commodity under CFTC oversight, 2026-03-17 (joint SEC/CFTC rule) |
| **Website** | [https://aptosfoundation.org](https://aptosfoundation.org) |

---

## Overview

Aptos is a high-performance PoS Layer 1 focused on delivering a safe and scalable blockchain. It leverages the Move programming language and Move VM, created and optimized for blockchain use cases. The team comprises the original creators, researchers, designers, and builders of Diem, Meta's abandoned blockchain project. Aptos raised $200M from a16z, Multicoin, Binance (now YZi Labs) and others in 2022, ran devnet/testnet through that year, and launched mainnet in October 2022.

### Leadership and strategy (2025-2026)

- **2024-12-19** — Co-founder and CTO **Avery Ching** replaced Mo Shaikh as CEO of Aptos Labs.
- Under Ching, Aptos repositioned away from "general-purpose L1" toward a **"global trading engine"** thesis: high-throughput execution for payments, stablecoins, RWAs and exchange-style workloads.

### Network fundamentals (2025-2026)

- **DeFi TVL crossed $1B in late 2025** — a ~19x year-over-year increase (Hyperion and other DEXes drove volume); TVL was ~$538M mid-2025 after a 56% surge, then kept climbing.
- **Stablecoin supply hit an all-time high of ~$1.8B in late 2025** (USDT, USDC, USDe, PYUSD), one of the strongest stablecoin footprints outside Ethereum/Solana/Tron.
- **BlackRock's BUIDL** deployed an additional $500M of tokenized assets on Aptos; Ondo's USDY also lives on Aptos — making it a credible RWA venue.
- Daily active addresses grew from ~70k (Jan 2024) to a peak of ~1.8M (Dec 2025).
- **2026** — Confidential APT (privacy-preserving balances) launched on mainnet; **2026-03-17** — APT classified as a digital commodity under the joint SEC/CFTC rule, removing its largest regulatory overhang and opening the door to regulated derivatives.

---

## Protocol & Technology

Aptos is engineered around three pillars that distinguish it from EVM and Solana-style chains:

- **[[move-language|Move language]] and Move VM** — Move is a resource-oriented smart-contract language originally designed at Meta for Diem. Its core innovation is treating digital assets as *resources*: typed values that can never be copied or implicitly discarded, only moved between accounts. This eliminates whole classes of bugs (double-spends, reentrancy, integer-overflow asset loss) at the language level rather than relying on auditing. Aptos uses the original Move dialect (Aptos Move), a sibling to the dialect used by [[sui]].
- **Block-STM parallel execution** — Aptos executes transactions optimistically in parallel across CPU cores, then validates for read/write conflicts using software transactional memory (STM). Conflicting transactions are re-executed; non-conflicting ones commit concurrently. This lets throughput scale with hardware rather than being serialized like the EVM. Block-STM is one of the most-cited pieces of Aptos's "global trading engine" performance thesis.
- **AptosBFT consensus (DiemBFT lineage)** — a pipelined Byzantine-fault-tolerant [[proof-of-stake]] consensus delivering sub-second finality. Validators are selected and weighted by stake; the protocol tolerates up to one-third Byzantine voting power.

Additional infrastructure: a parallelized state-Merkle store (Jellyfish Merkle Tree), modular component design allowing independent upgrades to mempool/consensus/execution, and 2026's **Confidential APT** for privacy-preserving balances. The roadmap under CEO Avery Ching targets higher TPS ceilings and lower latency to support exchange-style and payments workloads.

> Aptos and [[sui]] are the two surviving "Move L1s" from the Diem diaspora; both use Move and parallel execution, but differ in object models (Sui's object-centric model vs Aptos's account model) and consensus. See [[move-language]] for the shared language lineage.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 832.1M APT |
| **Total Supply** | 1.20B APT |
| **Max Supply** | 2.10B APT |
| **Market Cap** | $528.5M |
| **FDV (on max supply)** | ≈ $1.33B |
| **FDV (on total supply)** | ≈ $765M |
| **MC / FDV (vs total)** | ≈ 0.69 |
| **MC / FDV (vs max)** | ≈ 0.40 |

**Dilution flag:** APT's market cap is only ~40% of its fully-diluted value on the 2.1B max supply, and ~69% on the 1.2B total. Roughly 1.27B APT (60% of max) is yet to enter circulation through staking emissions and the investor/foundation unlock schedule. Monthly investor/foundation unlocks have been a persistent supply headwind since 2023 and remain the central pillar of the bear case — every rally must absorb mechanical new supply. Staking emissions (initially ~7% annualized, decaying per schedule) reward validators and delegators while diluting non-stakers.

---

## Valuation Framework

For an L1 like Aptos, fundamental valuation is anchored to *network usage* rather than cash flows. Useful metrics to track (no invented values — pull live from on-chain dashboards):

- **DeFi TVL** — total value locked in Aptos DeFi; crossed $1B in late 2025 (Hyperion and other DEXes). Compare to market cap for a crude "P/TVL" multiple.
- **Stablecoin supply on-chain** — hit ~$1.8B ATH late 2025 (USDT, USDC, USDe, PYUSD); a proxy for settled economic activity and a leading indicator for fee revenue.
- **Network fees / REV** — total transaction fees paid; the closest thing to "revenue." Low fees are good for users but mean the token captures little value unless usage scales massively.
- **Daily active addresses / transactions** — grew from ~70k (Jan 2024) to a peak ~1.8M DAU (Dec 2025).
- **RWA assets on-chain** — BlackRock BUIDL ($500M tokenized assets) and Ondo USDY anchor the RWA thesis.

The central valuation debate: usage metrics (TVL, stablecoins, DAU) sit at or near all-time highs while price sits ~97% below ATH — either a deep-value setup or evidence that L1 token value-capture is structurally broken. See [[real-world-assets]] and [[stablecoins]].

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $19.92 (2023-01-26) |
| **vs ATH (2026-06-20)** | ≈ -96.8% |
| **All-Time Low** | $0.6097 — APT trades just ~4% above its ATL as of 2026-06-20 |
| **24h Change (2026-06-20)** | +2.19% |
| **7d Change (2026-06-20)** | -4.95% |
| **Prior cycle low** | $0.7955 (2026-02-23) — since broken |

APT is grinding along its all-time-low region during the 2026 [[crypto-market-regimes|Established Bear Market]] (Fear & Greed 23). The proximity to ATL is itself a trading reference: a clean breakdown invites momentum shorts, while basers watch for a capitulation/reclaim.

---

## Platform & Chain Information

**Native Chain:** Aptos

| Chain | Address |
|---|---|
| Aptos | `0x1::aptos_coin::AptosCoin` |

---

## Market Structure & Derivatives

### Spot venues (centralized)

| Exchange | Pair |
|---|---|
| Binance | APT/USDT |
| Kraken | APT/USD |
| Upbit | APT/KRW |
| Bitget | APT/USDT |
| KuCoin | APT/USDT |

### Decentralized / derivatives

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | APT-PERP | Perpetual |
| Binance / Bybit / OKX | APT-PERP | Perpetual (CEX) |

- **Liquidity**: deep, top-100 asset — major CEX spot everywhere; 24h spot volume ~$43.2M (2026-06-20), down from ~$74M at the April snapshot as the bear market thins books.
- **Perps / funding / OI**: APT-PERP is liquid on [[hyperliquid|Hyperliquid]] and all major CEX futures. Funding and open interest are worth tracking around unlock dates and the CFTC-driven institutional narrative; the CFTC commodity classification opens the door to regulated US derivatives (potential CME-style products) as future structure.
- **Korean flow**: Upbit APT/KRW is a meaningful share of spot; watch for premium/discount dislocations.

---

## Trading Playbook

- **Narrative baskets**: "Move L1s" (paired with [[sui]] — SUI/APT relative-value is a popular pair trade), stablecoin/payments chains, and RWA venues. APT historically underperforms SUI in risk-on phases; mean-reversion traders watch the ratio. See [[narrative-trading]] and [[pairs-trading]].
- **Fundamentals/price divergence**: usage metrics (TVL, stablecoins, DAU) at all-time highs while price sits ~97% below ATH — either a value setup or evidence that L1 token value capture is broken; this is the central debate to track.
- **ATL proximity**: with price ~4% above the all-time low (2026-06-20), the ATL is a hard technical reference — breakdowns invite momentum shorts, reclaims invite contrarian longs.
- **CFTC commodity classification (2026-03-17)** is a concrete catalyst: regulated US derivatives and easier institutional access. Watch for CME-style products or ETF filings as follow-through.
- **Supply / unlocks**: scheduled investor/foundation unlocks plus staking emissions; unlock-calendar dates are tradable supply events ([[token-unlocks]]). MC/FDV ~0.40 on max supply means structural dilution overhang.
- **Regime context**: the 2026 [[crypto-market-regimes|Established Bear Market]] (Fear & Greed 23) favors mean-reversion fades of rips and tight risk on longs.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://aptosfoundation.org](https://aptosfoundation.org) |
| **Twitter** | [@Aptos_Network](https://twitter.com/Aptos_Network) |
| **Telegram** | [AptosTG](https://t.me/AptosTG) (92,724 members, Apr 2026) |
| **Discord** | [https://discord.com/invite/aptosnetwork](https://discord.com/invite/aptosnetwork) |
| **GitHub** | [https://github.com/aptos-labs](https://github.com/aptos-labs) |
| **Whitepaper** | [Aptos Whitepaper (PDF)](https://github.com/aptos-labs/developer-docs/blob/main/static/papers/Aptos-Whitepaper.pdf) |

---

## Competitive Positioning

Aptos competes across two axes: the narrow "Move L1" race and the broad high-performance L1 race.

| Chain | Niche | Execution model | Token vs APT (rough, 2026-06-20) | Notes |
|---|---|---|---|---|
| **Aptos** | High-throughput Move L1, "global trading engine" | [[move-language|Move]] + Block-STM parallel | rank #99, ~$528M cap | Strong RWA/stablecoin footprint, CFTC commodity status |
| [[sui]] | Object-centric Move L1 | Move + parallel (object model) | direct Move peer | Primary relative-value pair (SUI/APT ratio) |
| [[solana]] | High-throughput L1 | Sealevel parallel (eBPF) | far larger cap | The throughput benchmark; deeper DeFi/memecoin activity |
| [[ethereum]] | Settlement / DeFi base layer | Sequential EVM + L2s | far larger cap | Liquidity and developer gravity |

The bull case is that Move's safety + Block-STM parallelism win exchange-style and payments workloads; the bear case is that [[solana]] already owns high-performance mindshare and Ethereum L2s own DeFi liquidity, leaving Move L1s fighting over a contested middle.

---

## Risks

- **Token value-capture risk** — the core open question: usage at ATHs but price near ATL suggests the market doubts APT accrues value from network activity.
- **Dilution / unlocks** — ~60% of max supply uncirculated; monthly investor/foundation unlocks plus staking emissions create persistent sell pressure ([[token-unlocks]]).
- **Competition** — [[solana]], [[sui]], and Ethereum L2s all contest Aptos's target workloads.
- **Bear-market beta** — high-beta alt in an [[crypto-market-regimes|Established Bear Market]] (Fear & Greed 23); trades near ATL with thin liquidity.
- **Centralization optics** — Aptos Labs and foundation hold significant influence and supply; governance/decentralization is still maturing.
- **Execution risk** — the "global trading engine" repositioning depends on continued throughput gains and ecosystem wins that have yet to translate into token price.

> Data disclaimer: market figures are point-in-time (2026-06-20). Crypto is volatile and high-risk; nothing here is investment advice. Always verify against live data before trading.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[solana]]
- [[sui]] — primary Move L1 peer / relative-value pair
- [[move-language]]
- [[proof-of-stake]]
- [[hyperliquid]]
- [[real-world-assets]]
- [[stablecoins]]
- [[narrative-trading]]
- [[token-unlocks]]
- [[crypto-market-regimes]]

---

## Sources

- CoinGecko / cryptodataapi.com market snapshot, 2026-06-20 (current price, market cap, supply, ATH/ATL)
- CoinGecko top-1000 snapshot, 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- Aptos Labs — Wikipedia (CEO transition): https://en.wikipedia.org/wiki/Aptos_Labs
- Gate/DeepFlow — Avery Ching interview ("global trading engine"): https://www.gate.com/news/detail/15340554
- AInvest — Aptos TVL surge coverage: https://www.ainvest.com/news/aptos-network-tvl-surges-56-28-538-million-2507/
- Everstake — Aptos in 2026 (roadmap, TVL, stablecoins): https://everstake.one/resources/blog/aptos-news-2026
- Traders Union — Confidential APT mainnet launch: https://tradersunion.com/news/market-voices/show/1945087-confidential-apt-mainnet-launch/
- CoinMarketCap — Aptos (June 2026 price/mcap): https://coinmarketcap.com/currencies/aptos/
- Web verification, 2026-06-10.
