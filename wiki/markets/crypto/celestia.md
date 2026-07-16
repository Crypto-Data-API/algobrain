---
title: "Celestia"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, ethereum, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["Celestia Network", "TIA"]
entity_type: protocol
founded: 2023
headquarters: "Decentralized"
website: "https://celestia.org/"
related: ["[[cosmos]]", "[[crypto-markets]]", "[[eigenlayer]]", "[[ethereum]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[narrative-trading]]"]
---

# Celestia

**Celestia** (TIA) is the first [[modular-blockchains|modular blockchain]] **data availability (DA)** network: a [[cosmos|Cosmos]]-SDK chain that publishes and orders rollup data without executing it, letting developers launch chains that outsource DA cheaply. TIA was the flagship of the 2023–2024 "modular blockchain" narrative; for traders it is now primarily a tokenomics-turnaround story — issuance was cut aggressively through 2025 — set against brutal price decay (-98% from ATH) and intensifying DA competition from EigenDA and Avail. Notably, TIA is one of the few alts *up* over the trailing week (+13.7%) even as the broader market sits in an [[crypto-market-regimes|Established Bear Market]] (Fear & Greed 23).

---

## Market Data

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $0.3820 |
| **Market Cap** | $356.2M |
| **Market Cap Rank** | #126 |
| **24h Volume** | $33.3M |
| **24h Change** | +0.14% |
| **7d Change** | +13.68% |
| **Circulating Supply** | 932.5M TIA |
| **Total Supply** | 1.17B TIA |
| **Max Supply** | None (uncapped; disinflationary schedule) |
| **All-Time High** | $20.85 (2024-02-10) — ≈ -98.2% |
| **All-Time Low** | $0.2797 (2026-04-05) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

> Earlier snapshots: April 2026 (CoinGecko) price $0.2949, market cap $266.50M, rank #143; June 2026 prior quote ~$0.32.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TIA |
| **Sector** | [[modular-blockchains|Modular blockchain]] / data availability layer; [[cosmos|Cosmos]] ecosystem, [[proof-of-stake|PoS]] L1 |
| **Market Cap** | $356.2M, rank #126 (2026-06-20); +13.7% on the week |
| **Supply** | 932.5M circulating; max supply uncapped but issuance sharply reduced (see tokenomics) |
| **Inflation** | ~7.2% → ~5.0% (Lotus/v4, mid-2025) → ~2.5% (Matcha/v6, Nov 2025), declining ~6.7%/yr toward 1.5% floor |
| **All-Time High** | $20.85 (2024-02-10); ATL $0.2797 (2026-04-05) |
| **Website** | [https://celestia.org/](https://celestia.org/) |

---

## Overview

Celestia separates consensus and data availability from execution. Rollups post transaction data as blobs; light nodes verify availability via data-availability sampling (DAS). Backers include Polychain, Blockchain Capital, Galaxy Digital, Delphi Ventures, Coinbase Ventures and YZi Labs (ex-Binance Labs). Notable DA customers have included Ethereum-aligned rollups and appchains in the Arbitrum Orbit / OP Stack ecosystems (e.g., Eclipse and Manta Pacific were prominent early integrations).

---

## Protocol & Technology

Celestia is the canonical implementation of the [[modular-blockchains|modular blockchain]] thesis: it unbundles the blockchain stack into **execution**, **settlement**, **consensus**, and **data availability (DA)** — and provides *only* consensus + DA. It does not run smart contracts or execute transactions itself.

- **Data availability (DA) layer** — rollups and appchains post their transaction data to Celestia as **blobs** (arbitrary data namespaced per chain). Celestia orders the data and guarantees it was *published and available* — without caring what the data means. Execution happens elsewhere (on the rollup), so Celestia scales DA throughput independently of execution.
- **Data Availability Sampling (DAS)** — Celestia's core innovation. Instead of every node downloading every block, **light nodes** download tiny random samples of each block's erasure-coded data. With enough independent samples, the network can probabilistically guarantee the *entire* block is available with very high confidence — even though no single light node has the whole block. This lets DA capacity (and block size) grow with the number of light nodes rather than being bottlenecked by full-node bandwidth — a fundamentally different scaling curve from monolithic chains.
- **2D Reed-Solomon erasure coding + Namespaced Merkle Trees (NMTs)** — block data is erasure-coded into a 2D grid so that any sufficiently large fraction of samples can reconstruct it; NMTs let each rollup retrieve only its own namespace's data without downloading the whole block.
- **[[cosmos|Cosmos SDK]] + CometBFT [[proof-of-stake]]** — consensus is Tendermint-style BFT with instant finality; TIA is staked for security and used to pay blob fees. Native [[cosmos|IBC]] interoperability connects Celestia to the Cosmos ecosystem.
- **Blob fee market** — rollups pay for DA in TIA per byte of blob space; this is Celestia's native demand/value-accrual mechanism (the closest thing to "revenue").

> Celestia popularized the modular-vs-monolithic framing. The competing approaches are Ethereum's *integrated* DA (blobs via EIP-4844 directly on L1), [[eigenlayer|EigenLayer]]-based EigenDA (restaking-secured), and Avail. See [[modular-blockchains]] for the broader design space.

### 2025–2026 developments — the tokenomics pivot

TIA's core bear case was high inflation (~8% initial) dumping on a falling price. The DAO/community responded with successive issuance cuts:

- **Mid-2025 (v4 "Lotus" upgrade, CIP-29)** — inflation cut by 33%, from ~7.2% to ~5.0%; also locked staking rewards for locked tokens (CIP-31), disabled auto-claims (CIP-30), and added native TIA interoperability (Hyperlane-based cross-chain TIA).
- **Nov 2025 (v6 "Matcha" upgrade, CIP-41)** — inflation cut again to ~2.5%, continuing to decay ~6.7% per year toward a 1.5% terminal floor.
- **2025–2026 — "Proof of Governance" (PoG) debate** — a proposed framework (championed by researchers incl. Kairos Research) to replace inflationary security with governance-elected validators, potentially cutting issuance ~20x to ~0.25% and opening a path to net-deflationary TIA if DA fee burn exceeds issuance. Still a proposal, not implemented, as of June 2026.
- **Price**: ATL $0.2797 on 2026-04-05; recovered to $0.3820 by 2026-06-20 (+13.7% on the week — see Market Data) as the issuance cuts took effect.

### Competitive position

DA is now a three-way fight: Celestia vs **EigenDA** (built on [[eigenlayer|EigenLayer]] restaking) vs **Avail**, with Ethereum's own blob capacity (EIP-4844 and successors) compressing DA pricing from above. DA fee revenue across the sector remains small relative to token valuations — the central open question for TIA's long-term value accrual.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 932.5M TIA |
| **Total Supply** | 1.17B TIA |
| **Max Supply** | None (uncapped; disinflationary schedule post-Lotus/Matcha) |
| **Market Cap** | $356.2M |
| **FDV (on total supply)** | ≈ $447M |
| **MC / FDV** | ≈ 0.80 |

**Dilution flag.** ~238M TIA (≈20% of total supply) is yet to circulate — largely residual insider/VC and ecosystem allocations. Unlock-driven supply was a *dominant* negative through 2024–2025 (large tranches hitting a falling price). The TIA tokenomics-turnaround story is the successive issuance cuts:

- **Initial design** — high inflation (~8% start, ~7.2% effective) on an uncapped supply; the core bear case was emissions dumping on a falling price.
- **Mid-2025 — v4 "Lotus" upgrade (CIP-29)** — inflation cut ~33%, from ~7.2% to ~5.0%; locked staking rewards for locked tokens (CIP-31), disabled auto-claims (CIP-30), and added native TIA interoperability (Hyperlane-based cross-chain TIA).
- **Nov 2025 — v6 "Matcha" upgrade (CIP-41)** — inflation cut again to ~2.5%, decaying ~6.7%/yr toward a 1.5% terminal floor.
- **2025–2026 — "Proof of Governance" (PoG) debate** — a proposed framework (championed by researchers incl. Kairos Research) to replace inflationary security with governance-elected validators, potentially cutting issuance ~20x to ~0.25% and opening a path to *net-deflationary* TIA if DA fee burn exceeds issuance. Still a proposal, not implemented, as of June 2026.

Post-Matcha, the inflation drag is far smaller, changing the stake-and-hedge carry math (staking yield fell with issuance). TIA is used to pay blob/DA fees and is staked to secure consensus.

---

## Valuation Framework

DA-layer valuation hinges on whether blob fee demand can ever justify the token. Metrics to track (live; no invented values):

- **Blob/DA fee revenue (TIA and USD)** — bytes of blob space sold × fee rate. The fundamental demand signal; sector-wide DA revenue remains small relative to token valuations — the central open question for TIA's value accrual.
- **DA throughput / blobs posted** — how much data rollups actually push to Celestia.
- **Active rollups / appchains using Celestia DA** — customer count and concentration; wins/losses vs EigenDA and Avail.
- **Net issuance** — inflation minus any fee burn; PoG could flip this negative.
- **Staking ratio and staking yield** — affects liquid float and carry.

The bull thesis: as the rollup economy grows, DA demand compounds and (under PoG) TIA turns deflationary. The bear thesis: Ethereum's own blob capacity (EIP-4844 and successors) keeps compressing DA prices from above, capping external DA fee revenue.

---

## Market Structure & Derivatives

- **Spot venues**: deep CEX spot — Binance, Upbit (TIA/KRW), Kraken, Bitget, KuCoin, Crypto.com. 24h volume ~$33.3M (2026-06-20). Korean (Upbit) flow is a meaningful share — watch kimchi-premium-style dislocations.
- **Derivatives**: TIA-PERP on [[hyperliquid|Hyperliquid]] and major CEX futures (Binance, Bybit, OKX).
- **Perps / funding / OI**: track funding and OI around tokenomics-upgrade votes and DA customer news. TIA has historically been a high-beta vehicle for the modular-blockchain narrative.

---

## Trading Playbook

- **Narrative basket**: "[[modular-blockchains|modular blockchain]]" / DA infrastructure; historically high beta to alt-L1 rotations. See [[narrative-trading]].
- **Tokenomics re-rating**: the issuance-cut sequence (Lotus → Matcha → potential PoG) is the central re-rating thesis; PoG adoption would be the biggest single catalyst.
- **Relative strength signal**: TIA's +13.7% week (2026-06-20) stands out against an [[crypto-market-regimes|Established Bear Market]] — relative-strength traders watch whether the tokenomics narrative is decoupling TIA from beta.
- **ATL base**: ATL $0.2797 (2026-04-05); price ~37% above it. The April low is the key support reference.
- **Catalysts**: Proof-of-Governance adoption, major rollup DA wins/losses vs EigenDA/Avail, Ethereum blob-capacity upgrades (bearish for external DA pricing), further CIP tokenomics changes.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $20.85 (2024-02-10) |
| **All-Time Low** | $0.2797 (2026-04-05) |
| **Price (2026-06-20)** | $0.3820, ≈ -98.2% vs ATH |
| **24h Change (2026-06-20)** | +0.14% |
| **7d Change (2026-06-20)** | +13.68% |
| **1y Change (to Apr 2026)** | -87.34% |

---

## Platform & Chain Information

**Native Chain:** Celestia (Cosmos SDK); TIA representations on IBC chains

| Chain | Address |
|---|---|
| Secret | `secret1s9h6mrp4k9gll4zfv5h78ll68hdq8ml7jrnn20` |
| Cosmos Hub (IBC) | `ibc/D79E7D83AB399BFFF93433E54FAA480C191248FC556924A2A8351AE2638B3877` |
| Osmosis (IBC) | `ibc/D79E7D83AB399BFFF93433E54FAA480C191248FC556924A2A8351AE2638B3877` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | TIA/USDT |
| Kraken | TIA/USD |
| Upbit | TIA/KRW |
| Bitget | TIA/USDT |
| KuCoin | TIA/USDT |
| Crypto.com Exchange | TIA/USD |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | TIA-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://celestia.org/](https://celestia.org/) |
| **Twitter** | [@CelestiaOrg](https://twitter.com/CelestiaOrg) |
| **Telegram** | [CelestiaCommunity](https://t.me/CelestiaCommunity) (~13,900 members, Apr 2026) |
| **Discord** | [https://discord.com/invite/YsnTPcSfWQ](https://discord.com/invite/YsnTPcSfWQ) |
| **GitHub** | [celestiaorg/celestia-node](https://github.com/celestiaorg/celestia-node) (995 stars, 98 contributors — Apr 2026) |
| **Docs** | [https://docs.celestia.org/learn/TIA/overview/](https://docs.celestia.org/learn/TIA/overview/) |

---

## Ecosystem & Use Cases

- **Rollup DA backend** — Celestia's core use case: serve as the cheap data-availability layer for L2 rollups and appchains in the [[ethereum|Ethereum]]-aligned (Arbitrum Orbit, OP Stack) and sovereign-rollup ecosystems. Early prominent integrations included **Eclipse** (SVM rollup) and **Manta Pacific**.
- **Sovereign rollups** — chains can run their own execution/settlement while using Celestia purely for ordering + availability, a model Celestia pioneered.
- **Rollup-as-a-Service (RaaS)** — RaaS providers offer one-click rollup deployment with Celestia DA as a default option.
- **Native interoperability (Hyperlane)** — post-Lotus, TIA can move cross-chain.
- **Light-node accessibility** — DAS lets resource-light devices verify availability, broadening who can run infrastructure.

---

## Competitive Positioning — DA Layers

| DA layer | Security model | Relationship to Ethereum | Token / status (2026-06-20) | Notes |
|---|---|---|---|---|
| **Celestia (TIA)** | Sovereign [[proof-of-stake|PoS]] + DAS | External / alt-DA | rank #126, ~$356M cap | First-mover; full DAS; modular pioneer |
| **EigenDA** | [[eigenlayer|EigenLayer]] restaking (ETH-secured) | Ethereum-aligned restaking | part of EigenLayer | Inherits Ethereum economic security via restaking |
| **Avail** | Sovereign PoS + DAS (Polygon-origin) | External / alt-DA | separate token | Direct modular-DA competitor |
| **Ethereum blobs (EIP-4844+)** | Ethereum L1 consensus | *Integrated* DA | [[ethereum|ETH]] | Compresses external DA pricing from above |

The DA market is a three-way alt-DA fight (Celestia vs EigenDA vs Avail) with Ethereum's own blob capacity acting as a price ceiling. DA fee revenue across the entire sector remains small relative to token valuations — the existential question for all of them.

---

## Risks

- **Value-accrual risk** — DA fee revenue is tiny vs market cap; it is unproven that blob fees can ever justify the token.
- **Ethereum blob competition** — EIP-4844 and successors keep cutting Ethereum's own DA cost, squeezing external DA pricing (bearish for TIA fees).
- **Alt-DA competition** — EigenDA (restaking-secured) and Avail contest the same rollup customers.
- **Residual unlocks** — ~20% of supply uncirculated; insider/VC tranches still matter despite the issuance cuts.
- **PoG is unproven** — the deflation thesis depends on a governance change that is still only a proposal.
- **Bear-market beta** — high-beta modular-narrative alt in an [[crypto-market-regimes|Established Bear Market]] (Fear & Greed 23), trading ~98% below ATH.

> Data disclaimer: market figures are point-in-time (2026-06-20). Crypto is volatile and high-risk; nothing here is investment advice. Verify against live data before trading.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[cosmos]]
- [[modular-blockchains]]
- [[proof-of-stake]]
- [[eigenlayer]]
- [[hyperliquid]]
- [[narrative-trading]]
- [[crypto-market-regimes]]

---

## Sources

- CoinGecko / cryptodataapi.com market snapshot, 2026-06-20 (current price, market cap, supply, ATH/ATL)
- Celestia blog — "Introducing the Lotus upgrade: native TIA interop and reduced issuance": https://blog.celestia.org/lotus/
- Celestia docs — Staking, governance & supply: https://docs.celestia.org/learn/TIA/staking-governance-supply/
- BeInCrypto — "Celestia Upgrade Matcha Cuts Inflation — Can TIA Turn Deflationary?": https://beincrypto.com/celestia-upgrade-and-proof-of-governance-a-turning-point-for-tia/
- Leap Wallet — "Celestia's Lotus Upgrade: reduced inflation and native interoperability": https://www.leapwallet.io/blog/celestia-s-lotus-upgrade-what-tia-holders-need-to-know-about-reduced-inflation-and-native-interoperability
- Kairos Research on Proof-of-Governance: https://x.com/Kairos_Res/status/1970095954717004250
- CoinGecko — Celestia: https://www.coingecko.com/en/coins/celestia (June 2026 market data; April 2026 snapshot from CoinGecko top-1000 export 2026-04-09)
- Perplexity verification attempted 2026-06-10 (sonar; tokenomics details cross-checked via web search)

## Trading Profile

### Venues & liquidity

TIA is a genuine two-venue derivatives market. On [[hyperliquid|Hyperliquid]] it trades as **TIA-PERP** with leverage up to ~40-50x; on **Binance** it trades as both **spot (TIA/USDT)** and a **USD-margined perpetual**, alongside futures on Bybit and OKX. This gives TIA deep, liquid order books on both a top-tier CEX and the leading on-chain perp DEX — a meaningfully better microstructure than most rank-~100+ alts, which typically live on a single venue. Two-venue availability means order-book depth is aggregated across CEX and DEX, tightening effective spreads and allowing larger clip sizes with less slippage; it also enables cross-venue execution (route/split between Binance and Hyperliquid) and hedged structures (spot on Binance vs perp on either venue). Practically: mid-cap depth is respectable but still thin relative to majors, so scale in and avoid resting large market orders during low-liquidity hours; the dual listing is what makes funding/basis relative-value trades executable at all.

### Applicable strategies

- [[funding-rate-harvest]] — TIA-PERP funding oscillates with narrative-driven positioning; harvest positive funding by holding spot on Binance and shorting the perp when funding is persistently rich.
- [[hl-vs-cex-funding-divergence]] — with a live Binance perp and Hyperliquid TIA-PERP, funding can diverge between venues; capture the spread by going long the cheaper-funded leg and short the richer-funded one.
- [[cash-and-carry]] — hold Binance spot TIA against a short perp to lock the basis; the dual-venue spot+perp availability makes this cleanly executable for a mid-cap.
- [[narrative-trading]] — TIA is a pure modular-blockchain / data-availability narrative vehicle; trade around Proof-of-Governance votes, tokenomics-upgrade catalysts, and DA-customer wins/losses.
- [[token-unlock-supply-event]] — ~20% of supply is uncirculated with residual insider/VC tranches; position around scheduled unlocks and issuance-schedule changes that historically dumped on a falling price.
- [[oi-confirmed-trend]] — combine Hyperliquid open-interest and funding to confirm whether a TIA move is backed by genuine positioning or is a thin, liquidation-prone squeeze.

### Volatility & regime character

TIA is a **high-beta infrastructure altcoin** — a rank-~119 modular-blockchain/DA token that behaves as a leveraged expression of alt-L1 and "modular narrative" risk appetite. It carries elevated realized volatility, strong positive beta to BTC and especially ETH (it is Ethereum-aligned DA infrastructure and rotates with the broader alt-L1 complex), and it amplifies both up- and down-moves relative to majors. Idiosyncratic drivers (tokenomics cuts, PoG debate, DA-competition headlines) can temporarily decouple it from beta, but in aggregate it trades as a high-beta alt that leads on the way up in risk-on phases and bleeds hard in risk-off/bear regimes.

### Risk flags

- **Narrative dependence** — value is tied to the modular-DA thesis; DA fee revenue is tiny vs market cap, so sentiment/narrative shifts (EigenDA/Avail competition, Ethereum blob-pricing pressure) drive price more than fundamentals.
- **Residual unlocks / emissions** — ~20% of supply uncirculated; insider/VC tranches and the (declining but still positive) issuance schedule remain overhang risks.
- **High-beta bear-market exposure** — trades ~98% below ATH in an Established Bear Market; drawdowns are severe and fast.
- **Perp funding dislocations** — narrative-driven crowding can push TIA-PERP funding to extremes and trigger liquidation cascades on 40-50x leverage; monitor OI and funding across both venues.
- **Venue/liquidity concentration** — despite two-venue depth, mid-cap liquidity thins quickly off Binance/Hyperliquid; Korean (Upbit) flow can drive kimchi-premium-style dislocations.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=TIA` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=TIA` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=TIA&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=TIA&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=TIA"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]

---
