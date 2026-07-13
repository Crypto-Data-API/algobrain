---
title: "ZKsync"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto]
aliases: ["ZK"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://zksync.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[zk-rollup]]", "[[zero-knowledge-proofs]]", "[[rollups]]", "[[hyperliquid]]", "[[arbitrum]]", "[[starknet]]"]
---

# ZKsync

**ZKsync** (ticker **ZK**) is the governance token of ZKsync Era, an [[ethereum|Ethereum]] [[layer-2|Layer-2]] [[zk-rollup|zk-rollup]] built by Matter Labs that uses [[zero-knowledge-proofs|zero-knowledge proofs]] to batch and verify transactions off-chain while inheriting Ethereum's security. The ZK token, airdropped in June 2024, is used for governance and as a gas/fee currency within the network and its broader "Elastic Chain" of ZK-powered chains. It is a liquid proxy for the [[zk-rollup|zk-rollup]] scaling thesis.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ZK |
| **Market Cap Rank** | #235 |
| **Current Price** | $0.012105 |
| **Market Cap** | $120.81M |
| **24h Volume** | $16.05M |
| **24h Change** | +7.89% |
| **7d Change** | +5.19% |
| **Fully Diluted Valuation** | $254.10M |
| **MC / FDV** | ~0.48 |
| **All-Time High** | $0.320983 (2024-06-17) — now ~-96.2% |
| **All-Time Low** | $0.009578 (2026-06-06) — now ~+26.1% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

ZK bounced ~+7.9% on the day and ~+5.2% on the week off a fresh all-time low set on 2026-06-06 ($0.009578). The recovery is a low-base dead-cat-style bid rather than a trend change: ZK sits ~96% below its June-2024 debut high and trades against a hostile tape — the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** and the long-horizon regime is an **Established Bear Market** as of 2026-06-21. Newer L2 governance tokens with large locked allocations have de-rated heavily against ETH through the bear phase.

---

## Technology & Protocol

ZKsync Era is a general-purpose [[zk-rollup|zk-rollup]] — a [[layer-2|Layer-2]] scaling network that executes transactions off Ethereum mainnet, compresses them into batches, and posts a succinct validity proof (a SNARK) back to Ethereum, which verifies the proof on-chain.

| Property | Detail |
|---|---|
| **Type** | zkEVM (EVM-compatible zero-knowledge rollup) |
| **Builder** | Matter Labs |
| **Settlement layer** | [[ethereum|Ethereum]] L1 |
| **Proof system** | Validity proofs (SNARKs) — no fraud-proof challenge window |
| **Mainnet** | ZKsync Era, March 2023 |
| **Roadmap** | "Elastic Chain" — a network of interoperable ZK chains (ZK Stack) |

The defining advantage of validity ([[zk-rollup|zk-rollup]]) proofs over optimistic rollups is **fast, trustless finality**: withdrawals do not require the ~7-day fraud-proof challenge window that optimistic designs like [[arbitrum|Arbitrum]] and Optimism impose. The tradeoff has historically been proving cost and EVM-compatibility complexity, areas where zkEVMs ([[starknet|Starknet]], Linea, Scroll, Polygon zkEVM, ZKsync) have converged rapidly. Matter Labs' **ZK Stack** lets third parties launch their own ZK chains that settle to and interoperate within the Elastic Chain, positioning ZK as a hub token for an ecosystem rather than a single rollup.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~9.98B ZK |
| **Total / Max Supply** | 21.0B ZK |
| **Market Cap / FDV** | ~0.48 |

The fixed supply is **21 billion ZK** — a deliberate nod to Bitcoin's 21M cap. The June 2024 airdrop distributed roughly two-thirds of the token to users and contributors, but a large share remains allocated to the team, investors, and the ecosystem foundation under multi-year vesting. The sub-0.5 market-cap-to-FDV ratio (~0.48) signals **meaningful future unlock pressure** — only ~48% of the fixed supply is liquid, so vesting cliffs for insiders remain a recurring drag on price, a pattern common across 2024-vintage L2 tokens.

---

## Market Structure & Derivatives

**Centralized spot venues:** Binance (ZK/USDT), Kraken (ZK/USD), Upbit (ZK/KRW — notable Korean retail flow), Bitget, KuCoin, and Crypto.com Exchange.

**On-chain:** ZK trades on DEXs across both ZKsync Era and Ethereum mainnet (the token has bridged representations on both).

**Derivatives:** ZK has a perpetual market on [[hyperliquid|Hyperliquid]] (ZK-PERP) plus perps on the major CEXs. Around scheduled token unlocks, perp funding has historically skewed negative as traders position short into anticipated supply; open interest is moderate but can swell on roadmap or unlock catalysts. The ~$16M of 24h volume against a ~$121M cap is healthy turnover for a mid-cap L2 token, much of it leverage-driven.

---

## Use Case / Narrative / Category

ZKsync is in the **Ethereum Layer-2 / zk-rollup** category. The narrative is that [[zk-rollup|zero-knowledge rollups]] are the long-run end-state for Ethereum scaling — lower fees, faster finality, and validity proofs that avoid the multi-day challenge window of optimistic rollups. Matter Labs frames its roadmap around an "Elastic Chain" network of interconnected ZK chains. The ZK token captures governance over this ecosystem.

| Competitor | Type | Notes |
|---|---|---|
| [[arbitrum|Arbitrum]] (ARB) | Optimistic rollup | TVL leader |
| Optimism / Base | Optimistic rollup | Base dominates L2 activity |
| [[starknet|Starknet]] (STRK) | zk-rollup (Cairo VM) | Direct ZK competitor |
| Linea / Scroll / Polygon zkEVM | zkEVM rollups | Compete on ZK side |
| **ZKsync (ZK)** | zkEVM rollup | Elastic Chain / ZK Stack hub thesis |

Competition is fierce: optimistic rollups dominate on TVL while several zkEVMs compete directly on the ZK side.

---

## Notable History

- **March 2023** — ZKsync Era mainnet launched.
- **June 2024** — The **ZK token airdrop** was one of the most anticipated L2 airdrops; it drew criticism over eligibility criteria and saw a sharp post-listing decline. The all-time high (~$0.321) was set near the June-2024 debut.
- **2024-2026** — Token fell ~96% from ATH as L2 tokens broadly de-rated, supply unlocked, and EIP-4844 blobs compressed L2 fee revenue.
- **2026-06-06** — Fresh all-time low at $0.009578.

---

## Valuation Framing

ZK is best framed as a high-beta bet on (1) zkEVM adoption within the Ethereum scaling stack and (2) the Elastic Chain / ZK Stack ecosystem capturing share against Arbitrum/Base. The qualitative caveat is **value accrual**: governance utility does not directly capture sequencer or MEV revenue, so the token can lag even if the network succeeds technically. With MC/FDV ~0.48, the FDV-implied valuation is roughly double the spot market cap — buyers are paying for tokens that mostly do not yet trade.

---

## Risks

- **Unlock overhang** — low MC/FDV (~0.48) means substantial scheduled supply still to hit the market.
- **L2 competition / fee compression** — many rollups compete for the same activity, and Ethereum's own data-cost reductions (EIP-4844 blobs) compress L2 fee revenue.
- **Token value-accrual ambiguity** — governance utility does not directly capture sequencer/MEV revenue.
- **Bear-market beta** — high-beta infrastructure token in an extreme-fear regime (Fear & Greed = 23).
- **Decentralization timeline** — sequencer and prover decentralization remains a work in progress.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[layer-2]]
- [[zk-rollup]]
- [[zero-knowledge-proofs]]
- [[rollups]]
- [[arbitrum]]
- [[starknet]]
- [[hyperliquid]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.
