---
title: "Aztec"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, ethereum]
aliases: ["AZTEC"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://aztec.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[zero-knowledge-proofs]]", "[[perpetual-futures]]"]
---

# Aztec

**Aztec** (ticker **AZTEC**) is a privacy-first Layer 2 ([[layer-2|L2]]) on [[ethereum]], built around [[zero-knowledge-proofs|zero-knowledge]] cryptography to let developers build applications that protect user privacy. The AZTEC token is the network asset. Unlike the memes in this section, Aztec is an infrastructure protocol with a genuine technical thesis: client-side proving and privacy-preserving smart contracts.

---

## Architecture — how it works

Aztec is a **privacy ZK-rollup** on [[ethereum]]. Two design choices set it apart from mainstream L2s like [[arbitrum|Arbitrum]] or [[base|Base]]:

### Privacy via client-side proving

In a normal rollup, all state is public — anyone can read every balance and transaction. Aztec's central innovation is **client-side proving**: a user's own device generates a [[zero-knowledge-proofs|zero-knowledge]] proof that a transaction is valid (correct signatures, sufficient balance, rules followed) *without revealing the inputs*. The rollup verifies the proof and updates an encrypted state. The result is **programmable privacy** — confidential balances and transaction details, with public verifiability of correctness. Aztec's model distinguishes **private state** (encrypted notes, UTXO-style, known only to the owner) from **public state** (account-style, like normal EVM), and lets a single contract span both, with calls able to move between the private and public domains.

### ZK-rollup settlement & DA

As a ZK-rollup, Aztec posts **validity proofs** to Ethereum L1: every batch of L2 transactions is accompanied by a succinct proof that the new state root follows correctly from the old one. Unlike [[optimistic-rollup|optimistic rollups]] (which assume validity and rely on a fraud-proof challenge window), a ZK-rollup's state is mathematically verified at settlement — there is **no withdrawal challenge delay** of the optimistic kind, and security reduces to the soundness of the proving system plus Ethereum's own consensus for [[data-availability|data availability]]. Aztec publishes the data/commitments needed for state reconstruction to Ethereum, so the chain inherits Ethereum-grade DA and settlement while adding a privacy layer on top.

### Decentralized sequencing & proving

A long-standing challenge for privacy rollups is decentralizing the **sequencer** (who orders transactions) and **prover** (who generates the rollup proof) without breaking privacy. Aztec's design targets a permissionless network of sequencers and provers rather than a single operator — the degree to which this is live and trust-minimized at any point is the key thing to verify, as with all L2s, centralized sequencing remains a common interim posture.

### The proving stack: PLONK and Noir

Aztec's cryptography lineage is its deepest moat. The team authored **PLONK (2019)**, a universal SNARK with a single reusable trusted setup, and built **Noir**, a Rust-like language for writing ZK circuits (see History below). These let developers write private smart contracts without hand-rolling cryptography.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | AZTEC |
| **Current Price** | $0.01491233 |
| **Market Cap** | $43,850,738 |
| **Market Cap Rank** | #496 |
| **24h Volume** | $2,439,406 |
| **24h Change** | -0.33% |
| **7d Change** | -8.01% |

Market backdrop on this date was bearish: the [[fear-and-greed-index|Fear & Greed Index]] read **22 ("extreme fear")** in an established bear market. AZTEC was roughly flat on the day but down ~8% over the week — a comparatively soft week. 24h turnover of ~$2.4M against a ~$44M cap is on the thin side (low relative volume).

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~2.96B AZTEC |
| **Total Supply** | ~10.35B AZTEC |
| **Max Supply** | 10.35B AZTEC |
| **Market Cap / FDV Ratio** | ~0.29 |

The MC/FDV ratio of ~0.29 is the key tokenomics caveat: only roughly a quarter of total supply is reflected in circulating market cap, implying a large future emission/unlock schedule. Fully-diluted valuation is several times the market cap, so prospective token unlocks are a material dilution consideration relative to fully-circulating memes — this is a structural overhang to monitor.

### Value accrual & governance

AZTEC's value channels are the standard L2 set, weighted toward infrastructure rather than speculation: **sequencer/proving fees** (the network's economic engine, paid in AZTEC and dependent on real transaction volume), **staking** by sequencers/provers to participate in (and be slashed for misbehaving in) the decentralized network, and **governance** over protocol parameters and the treasury. Because privacy applications are still early, fee revenue is nascent; with ~71% of supply not yet circulating, much of any near-term staking reward is emission-funded. The durable bull case is that *confidential* DeFi/payments become large enough that sequencer fees and staking demand outgrow the unlock schedule.

---

## Comparison vs competitor chains

Aztec sits at the intersection of **L2 scaling** and **privacy** — its peer set spans both.

| Network | Type | Privacy model | Differentiator vs Aztec |
|---|---|---|---|
| **Aztec (AZTEC)** | ZK-rollup L2 on Ethereum | Programmable privacy via client-side proving | Confidential smart contracts + PLONK/Noir proving stack |
| **[[zksync\|zkSync]] / [[starknet\|Starknet]]** | ZK-rollup L2s | None (public state) | General scaling, large ecosystems; *no* native privacy |
| **[[zcash\|Zcash]] (ZEC)** | Privacy L1 | Shielded zk-SNARK transactions | Private *payments* only — not a programmable smart-contract platform |
| **[[monero\|Monero]] (XMR)** | Privacy L1 | Ring signatures + stealth addresses | Untraceable payments; no smart contracts; different crypto |
| **Railgun** | Privacy *system* on existing chains | zk smart-contract privacy overlay | Adds privacy to existing EVM chains rather than being its own L2 |

Aztec's distinctive claim is **programmable** privacy at the rollup layer — confidential *applications*, not just private transfers (Zcash/Monero) and not just scaling (zkSync/Starknet). The competitive risk is twofold: general ZK-L2s are far larger and could bolt on privacy, while dedicated privacy coins own the simpler "private payments" use case.

---

## How & Where It Trades

### Spot venues (centralized)

| Exchange | Pair |
|---|---|
| Kraken | AZTEC/USD |
| Upbit | AZTEC/KRW |
| KuCoin | AZTEC/USDT |

### On-chain / DEX

| Exchange | Type |
|---|---|
| Uniswap V3 (Ethereum) | Spot (AZTEC/WETH) |

### Derivatives

| Venue | Instrument | Type |
|---|---|---|
| [[hyperliquid\|Hyperliquid]] | AZTEC-PERP | [[perpetual-futures\|Perpetual]] |

AZTEC has a listed [[perpetual-futures]] market on Hyperliquid. With relatively thin spot turnover, perp funding and open interest can move sharply; specific funding/OI values are not in the current data snapshot and are omitted rather than estimated. Check live funding before holding leveraged exposure.

### Contract Address

| Chain | Address |
|---|---|
| Ethereum | `0xa27ec0006e59f245217ff08cd52a7e8b169e62d2` |

---

## Use Case, Narrative & Category

Aztec is a **privacy / [[zero-knowledge-proofs|zk]] Layer-2** infrastructure play, not a meme. Its thesis is that privacy is foundational financial infrastructure rather than a feature, and that confidential smart contracts on [[ethereum]] will be needed by both crypto-native users and institutions. Categories include Smart Contract Platform, Ethereum Ecosystem, Layer 2 (L2), Privacy Blockchain, and CoinList Launchpad.

Technical and ecosystem highlights (preserved from prior source):

- **PLONK (2019):** Aztec's team developed PLONK, a SNARK-based proving system that is computationally efficient and requires only a single universal trusted setup. PLONK was a major breakthrough adopted and extended across the industry (zkSync, Polygon, Mina and others), spawning an entire family of "PLONKish" proving systems derived from the original 2019 paper.
- **Noir:** Aztec Labs built Noir, a Rust-like programming language for writing zero-knowledge circuits, aiming to make ZK accessible to mainstream developers. It has been cited (per prior source material) as among the fastest-growing developer ecosystems and is used by projects across multiple chains.
- **Institutional attention:** Per prior source material, JPMorgan's Quorum blockchain team was an early institutional tester/evaluator of Aztec's technology, and the project raised a **$100M Series B led by a16z**.

### Catalysts

Plausible **positive catalysts**: mainnet decentralization milestones (permissionless sequencers/provers), growth in Noir developer activity and deployed private apps, institutional/enterprise pilots for confidential settlement, and any broad rotation into the privacy or ZK narratives. Plausible **negative catalysts**: token unlocks landing into thin liquidity, adverse privacy-protocol regulation or exchange delistings (the structural risk for this category), and technical/proving-system vulnerabilities. As a small-cap infrastructure token, AZTEC is also highly sensitive to broad-market regime.

---

## Notable History

- Long history in Ethereum privacy tooling (Aztec Connect and earlier privacy products predate the current network design).
- All-time high near **$0.0399 (2026-02-21)**; all-time low near **$0.0176 (2026-04-05)** — a relatively recent token-trading history with the asset trading between those levels into mid-2026.
- Backed by a $100M a16z-led Series B and built by a team credited with foundational ZK cryptography (PLONK, Noir).

---

## Risks

Aztec is infrastructure, but still carries significant risk:

- **Dilution / FDV overhang** — MC/FDV ≈ 0.29 means large prospective unlocks; emissions could pressure price independent of fundamentals.
- **Adoption / execution risk** — the privacy thesis is long-term; usage, fees, and developer traction must materialize to justify valuation.
- **Regulatory risk** — privacy-preserving and confidential-transaction protocols face heightened regulatory scrutiny in many jurisdictions, a structural overhang distinct from memes.
- **Competition** — the zk/L2 and privacy landscape is crowded; PLONK-derived tech is widely used by competitors.
- **Liquidity risk** — relatively thin spot turnover (~$2.4M/24h) implies higher slippage on size.
- **Macro / regime risk** — the snapshot date sat in "extreme fear" (index 22) within an established bear market, a poor regime for small-cap infrastructure tokens.

---

## Trading playbook (bear / Extreme-Fear, bottoming regime)

Context as of 2026-06-23: market-wide **Extreme Fear** (F&G 21), a transitional **bottoming/accumulation** long-horizon regime, BTC ~16% below its 200-day MA.

- **Character:** Aztec is the closest thing in this cohort to a "real infrastructure" bet — a genuine technical thesis (programmable privacy, PLONK/Noir lineage, a16z backing) rather than a pure narrative token. That makes it more suitable for a *thesis-driven* hold than a momentum trade, but it does not exempt it from small-cap volatility or the dilution overhang.
- **Default stance:** in Extreme Fear, small-cap infra tokens with large FDV overhangs typically underperform; no urgency to chase. If building a position, scale in patiently rather than buying spikes.
- **Watch the perp:** AZTEC has a [[hyperliquid|Hyperliquid]] [[perpetual-futures|perp]]. With thin spot turnover (~$2.4M/24h), funding and OI can swing hard; check live funding before any leveraged or hedged position — extreme funding can itself signal crowded positioning to fade.
- **Invalidation / view change:** a regulatory crackdown on privacy protocols is the category-specific tail risk that could impair the token independent of macro. On the upside, a regime flip out of Extreme Fear plus decentralization/adoption milestones would strengthen the thesis.
- **Risk sizing:** treat dilution (MC/FDV ≈ 0.29) and unlock dates as scheduled risk events; size for the FDV, not just the current cap.

---

## Related

- [[ethereum]]
- [[zero-knowledge-proofs]]
- [[perpetual-futures]]
- [[crypto-markets]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-20 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.
