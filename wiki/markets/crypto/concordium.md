---
title: "Concordium"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto]
aliases: ["CCD"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://www.concordium.com/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[real-world-assets]]", "[[staking]]"]
---

# Concordium

**Concordium** (ticker **CCD**) is a **compliance-focused Layer 1 blockchain** founded in 2018 by **Lars Seier Christensen**, the founder of Saxo Bank. Its defining feature is a **protocol-level identity layer**: every account is tied to a real-world identity verified by a third-party identity provider, while transactions remain private on-chain via zero-knowledge proofs, with selective disclosure to authorities only under defined legal conditions. Concordium's thesis is that blockchain reaches its full potential by working *with* regulation rather than against it, branding its programmable, identity-and-policy-aware assets as "Smart Money." CCD is the native [[proof-of-stake]] token of this [[layer-1]] chain, ranked **#426** by market capitalization as of this snapshot.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | CCD |
| **Current Price** | $0.00426674 |
| **Market Cap** | ~$53.84M |
| **Market Cap Rank** | #426 |
| **24h Volume** | ~$111.5K |
| **24h Change** | -0.02% |
| **7d Change** | -3.01% |
| **Fully Diluted Valuation** | ~$61.96M |
| **All-Time High** | $0.149407 (2022-02-10) — **-97.1%** |
| **All-Time Low** | $0.00262306 (2024-07-16) — **+62.7%** |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The market backdrop is bearish: the [[fear-and-greed-index|Crypto Fear & Greed Index]] reads **23 (Extreme Fear)** in an **Established Bear Market**. CCD sits roughly **-97%** below its all-time high of $0.149407 (2022-02-10) and **+63%** above its all-time low of $0.00262306 (2024-07-16). With only ~$0.11M in 24h volume against a ~$54M cap (a turnover of ~0.2% of cap per day), CCD is among the **thinnest-traded** names in this group — a notable liquidity risk where even modest orders move price.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~12.62B CCD |
| **Total Supply** | ~14.52B CCD |
| **Max Supply** | Uncapped (inflationary) |
| **Fully Diluted Valuation** | ~$61.96M |
| **Market Cap / FDV Ratio** | ~0.87 |

CCD has **no fixed maximum supply** — new tokens are minted as block rewards under the protocol's inflation schedule, distributing emissions to validators (bakers) and delegators. The market-cap/FDV ratio near 0.87 indicates most of the currently issued supply is already circulating (~12.62B of ~14.52B total), but ongoing inflation means supply grows over time, so holders must weigh staking yield against dilution. CCD is used for transaction fees (with a stable, predictable fee model denominated in EUR-pegged terms), [[staking]] via baking/delegation, and governance. Concordium's fee design deliberately keeps costs low and predictable to court enterprise users who cannot tolerate volatile gas pricing.

---

## How & Where It Trades

**Spot venues (centralized):**

| Exchange | Pair |
|---|---|
| Kraken | CCD/USD |
| KuCoin | CCD/USDT |

CCD is listed on a relatively small set of CEXs (Kraken and KuCoin among the most prominent), which constrains accessibility and depth.

**Derivatives:** No major [[hyperliquid|Hyperliquid]] perpetual market is recorded for CCD in this snapshot; exposure is effectively **spot-only**. There is no deep derivatives market to express leveraged views, and the very low ~$0.11M daily volume implies meaningful slippage even on modest order sizes. Verify any perp listing live before relying on it; where perps exist, watch [[funding-rate]] and open interest.

### Market structure at a glance

| Dimension | Read |
|---|---|
| **Spot depth** | Thin — a handful of mid-tier CEXs (Kraken, KuCoin) plus on-chain |
| **Daily turnover** | ~$0.11M (~0.2% of market cap) — lowest-tier liquidity |
| **Derivatives** | None material; spot-only exposure |
| **Float quality** | High MC/FDV (~0.87) — limited unlock overhang, but ongoing inflation |
| **Slippage profile** | Severe on size; price discovery dominated by few venues |

---

## Technology & Consensus

Concordium runs its own **Layer 1** chain using a **Proof-of-Stake** consensus (baking and delegation) with a finality layer for fast settlement. Its signature innovation is the **identity-on-chain** design: an Identity Provider verifies a user's real-world identity off-chain and issues credentials that anchor on-chain accounts, while zero-knowledge cryptography keeps transaction details private. An "anonymity revoker" framework allows lawful, conditional disclosure of identity — embedding **programmable compliance** directly in the protocol. Concordium emphasizes peer-reviewed cryptographic research and predictable, low fees. (See [[layer-1]], [[proof-of-stake]].)

---

## Use Case, Narrative & Category

Concordium's category is the **identity / ID-layer Layer 1** for regulated finance. Its narrative targets institutions and enterprises that need privacy *and* compliance — KYC-aware payments, tokenized [[real-world-assets]], and auditable yet private business transactions. CoinGecko category tags include [[layer-1|Layer 1 (L1)]], Decentralized Identifier (DID), Zero Knowledge (ZK), Payment Solutions, Privacy Blockchain, and Privacy Infrastructure. The bet is that regulatory clarity drives demand for chains where identity and policy controls are native rather than bolted on.

---

## Valuation Framing (qualitative)

CCD is best understood as a **venture-style bet on a single, slow-burning thesis**: that regulated institutions will adopt a compliance-native chain. Several qualitative observations frame the risk/reward:

- **Pre-revenue narrative play.** There is no fee-burn or buyback that mechanically links CCD price to usage; value accrual depends almost entirely on *future* enterprise adoption rather than current cash flows. The ~$54M cap prices in skepticism — it is ~97% off ATH and well below the prior-cycle valuations of comparable L1s.
- **Inflationary, so demand must outrun emission.** Unlike hard-capped peers, CCD must generate net new demand simply to hold price flat against ongoing baking emissions.
- **Crowded thesis, thin moat.** "Compliance-native L1" competes with permissioned enterprise chains (Hyperledger, Corda) and with general-purpose L1s adding identity tooling. Concordium's differentiator is protocol-level ID, but adoption proof points remain limited.
- **Liquidity discount.** At ~$0.11M daily volume, CCD trades at a structural liquidity discount; a large holder cannot realise the quoted cap.

The honest read: CCD is a **deep-drawdown, low-liquidity, narrative-dependent micro-cap** whose upside requires the regulatory-adoption thesis to finally convert into real enterprise volume.

---

## Peer Comparison

| Token | Category | Price | Market Cap | Rank | Max Supply | MC/FDV |
|---|---|---|---|---|---|---|
| **Concordium (CCD)** | ID-layer L1 | $0.00427 | ~$54M | #426 | Uncapped | ~0.87 |
| [[qubic-network\|Qubic (QUBIC)]] | Useful-PoW / AI L1 | $4.6e-7 | ~$64M | #378 | 200T | ~0.69 |
| [[polkadot\|Polkadot]] / [[cardano\|Cardano]] | Research-led L1 | — | (large-cap) | — | varies | — |
| Quant (QNT) | Enterprise interop | — | (mid-cap) | — | capped | — |

*CCD's distinguishing axis among L1s is **protocol-level identity + selective-disclosure compliance**, whereas peers compete on throughput, smart-contract ecosystems, or interoperability. See [[layer-1]] for the broader landscape.*

---

## Notable History

- **2018**: Concordium founded by Lars Seier Christensen (founder of Saxo Bank), with a focus on regulation-friendly blockchain infrastructure.
- **2022-02**: CCD reached its all-time high of ~$0.149 (2022-02-10) during the prior cycle peak.
- **2024-07**: CCD bottomed at its all-time low of ~$0.0026 (2024-07-16).
- The project has continued to develop its identity layer, ZK compliance tooling, and "Smart Money" programmable-asset framework.

---

## Risks

- **Very thin liquidity**: ~$0.15M daily volume on a ~$54M cap is the lowest in this group — high slippage and exit risk.
- **Inflationary supply**: An uncapped emission schedule dilutes holders unless offset by demand or staking participation.
- **Adoption risk**: The compliance/identity thesis depends on institutional uptake that has been slow to materialize across the sector.
- **Limited venues**: A small set of exchange listings constrains access and price discovery.
- **Macro / regime risk**: Extreme Fear (index 23) and an Established Bear Market weigh on small-cap tokens.
- **Privacy-vs-compliance positioning**: Its middle-ground design may satisfy neither pure-privacy users nor fully regulated institutions, a persistent go-to-market challenge.

---

## Related

- [[crypto-markets]]
- [[layer-1]]
- [[real-world-assets]]
- [[staking]]
- [[proof-of-stake]]
- [[privacy-coins]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.
