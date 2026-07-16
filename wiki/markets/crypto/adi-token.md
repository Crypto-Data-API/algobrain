---
title: "ADI"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, ethereum, regulation]
aliases: ["ADI", "ADI Chain", "ADI Foundation"]
entity_type: protocol
founded: 2024
headquarters: "Abu Dhabi, UAE"
website: "https://token.adi.foundation/"
related: ["[[chainlink]]", "[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[stablecoins]]", "[[zksync]]"]
---

# ADI

**ADI** (ticker **ADI**) is the native gas token of **ADI Chain**, an [[ethereum|Ethereum]] Layer 2 built on [[zksync|zkSync]]'s zkStack by the Abu Dhabi-based ADI Foundation — founded by Sirius International Holding, the digital arm of IHC (International Holding Company, one of the world's largest listed investment companies) — and positioned as the first institutional L2 for stablecoins and [[real-world-assets|real-world assets]] in the MENA region. The token is issued as an ERC-20 on [[ethereum|Ethereum]] (contract `0x8b14…caea`) and serves as the gas/settlement asset for ADI Chain. Its flagship use case is settlement for **DDSC, the UAE dirham-backed stablecoin licensed by the UAE Central Bank**, making ADI one of the cleanest listed proxies on state-backed Gulf blockchain adoption — but also an extreme **low-float, high-FDV** instrument where roughly 92% of supply was still locked at the April 2026 snapshot, so the price reflected an unlock-heavy bet on future adoption rather than circulating fundamentals.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ADI |
| **Market Cap Rank** | ~#118 tier (April 2026 snapshot) |
| **Market Cap / FDV** | ~$360M cap but **~$4.5B FDV** — only 8% of supply circulating (April 2026 snapshot, approximate) |
| **Stack** | zkSync zkStack zero-knowledge L2 with the GPU-accelerated Airbender prover; modular Layer 3s for national/enterprise deployments |
| **Sponsor** | ADI Foundation (Abu Dhabi), founded by Sirius International Holding / IHC |
| **Flagship asset** | DDSC dirham stablecoin (IHC + First Abu Dhabi Bank), UAE Central Bank-licensed, live Feb 2026 |
| **Categories** | Infrastructure, Layer 2 |
| **Website** | [https://token.adi.foundation/](https://token.adi.foundation/) |

---

## Architecture & How It Works

ADI Chain is an [[ethereum|Ethereum]] Layer 2 developed by the ADI Foundation to support government, enterprise, and institutional digital infrastructure. The design centres on a regulated, ZK-secured settlement layer rather than a general-purpose DeFi chain:

- **zkSync zkStack base.** ADI Chain is built on [[zksync|zkSync]]'s **zkStack** — the modular, open-source framework that powers zkSync's "Elastic Chain" ecosystem of ZK-rollups. Choosing zkStack gives ADI Chain Ethereum-anchored security with validity proofs (rather than the fraud-proof / challenge-window model of optimistic rollups), shared standards for bridging, and a path to interoperate with other zkStack chains.
- **Airbender prover.** Proof generation runs on the **Airbender** prover, marketed as a GPU-accelerated zero-knowledge prover that compresses batches of L2 transactions into succinct validity proofs verified on [[ethereum|Ethereum]]. GPU acceleration is the throughput/latency lever: it shortens proof times so the chain can settle fast and cheaply while inheriting L1 security.
- **Modular Layer 3s for sovereign/enterprise deployments.** Above the L2, ADI Chain exposes **modular Layer 3** capabilities that let a nation, ministry, bank, or enterprise spin up a compliant, region-specific chain (its own permissioning, KYC/AML, and data rules) that still settles down to ADI Chain and ultimately [[ethereum|Ethereum]]. This is the "sovereign deployment" pitch — each L3 is a tailored jurisdictional instance rather than a one-size-fits-all public network.
- **DDSC dirham-stablecoin settlement.** The flagship workload is **DDSC**, a UAE dirham-pegged [[stablecoins|stablecoin]] initiated by IHC and First Abu Dhabi Bank and licensed by the UAE Central Bank, which went live on ADI Chain in February 2026 (Source: Decrypt). DDSC settlement is the concrete, regulated use case that distinguishes ADI from speculative L2s — it ties on-chain throughput to a state-sanctioned payment instrument.
- **Real-world workloads.** Beyond payments, ADI Chain targets **e-invoicing, land/property registries, tokenized RWAs, and enterprise payments** — government-grade record-keeping where verifiable, tamper-evident settlement matters more than open composability. The Foundation frames a long-horizon goal of onboarding one billion people by 2030.

ADI is the network's **native gas token**: it pays for transaction execution and proof settlement on ADI Chain, the role analogous to ETH on Ethereum or to the stack token on other zkStack chains.

---

## History & Timeline (2025–2026)

*Real dated events only.*

- **21 Aug 2025** — ADI Chain testnet launched (Businesswire).
- **Dec 2025** — Sirius International Holding announced a strategic partnership with **Crypto.com** to integrate ADI Chain and explore listing digital assets from the Sirius ecosystem (tokenized RWAs, stablecoins).
- **Late 2025** — ADI token launched/listed; ATL $0.9754 on 10 Dec 2025.
- **Feb 2026** — **DDSC dirham-backed stablecoin went live on ADI Chain**, initiated by IHC and First Abu Dhabi Bank and licensed by the UAE Central Bank (Decrypt).
- **Mar 2026** — official **Chainlink partnership** to integrate CCIP and the Chainlink platform across ADI Chain, supporting stablecoin and tokenization strategy across the Middle East, Africa and Asia.
- **2026** — Ledger hardware-wallet support added; H2O Hospitality partnership for blockchain payments in UAE travel/consumer sectors.
- Token roughly 4.6x'd from the Dec 2025 ATL to the $4.55 ATH on 3 Apr 2026.

---

## How & Where It Trades

- **Spot venues:** [[kraken|Kraken]] (ADI/USD), KuCoin (ADI/USDT), and Crypto.com Exchange (ADI/USD — note the Sirius–Crypto.com integration partnership announced Dec 2025), plus **Uniswap V3** on [[ethereum|Ethereum]] (ADI/USDC). It is a centralised-listing token with an on-chain DEX path rather than a deep, multi-venue market.
- **Liquidity:** Thin — roughly **~$0.5M/day** volume at the April 2026 snapshot. That is light for the rank, so slippage and gap risk are real on size, and the quoted price rests on a small actively-traded float.
- **Derivatives:** No major perpetual-futures market is evident — effectively **spot-only**.
- **Low-float overhang:** With ~8% circulating (MC/FDV ≈ 0.08), the tradable supply is small and rallies can be sharp on thin volume — but the same thin float means future unlocks land on a shallow book. Treat both directions as low-float-amplified.

---

## Narrative, Category & Catalysts

- **Narrative baskets:** UAE/Gulf **state-adoption** plays; **institutional L2 / [[real-world-assets|RWA]]** infrastructure; **regulated-stablecoin rails** ([[stablecoins|stablecoin]] settlement). ADI trades on government-/institution-partnership headlines far more than on crypto-native flow, which gives it idiosyncratic, news-driven beta relative to the broad market.
- **Why it stands out:** A *live, licensed* sovereign-adjacent stablecoin (DDSC, UAE Central Bank) plus an IHC-scale backer make ADI one of the cleaner listed proxies on Gulf blockchain adoption — a genuinely differentiated story versus generic L2 tokens.
- **Key catalysts to watch:** DDSC adoption/volume metrics; new sovereign/enterprise **Layer 3** deployments; further IHC/Sirius-ecosystem announcements; [[chainlink|Chainlink]] CCIP integration progress (cross-chain stablecoin/RWA reach); new exchange listings; and — critically — the **token unlock/vesting schedule**.

---

## Risks

- **Extreme low-float / FDV overhang (dominant risk):** ~92% of supply locked at snapshot; ~$4.5B FDV vs ~$360M MC. Future unlocks add sell-side supply onto a thin book; headline market cap materially overstates realisable value.
- **Narrative-vs-adoption gap:** Price is driven by partnership headlines and a "billion users by 2030" vision; the gas-token value accrual only materialises if real DDSC volume, registries, and L3 deployments scale into recurring on-chain demand. The bridge from announcements to throughput is unproven.
- **Single-sponsor concentration:** Direction, funding, and credibility hinge on the **ADI Foundation / Sirius / IHC** axis. Strong for execution and regulatory standing, but it concentrates governance and counterparty risk in one backer rather than a decentralised community.
- **Regulatory dependency:** The thesis leans on UAE state/central-bank sanction. That is a tailwind today but ties the token's fate to a specific jurisdiction's policy and to DDSC's continued licensing.
- **Thin liquidity / exit risk:** ~$0.5M/day volume and spot-only venues make exits in size difficult and price discovery fragile.

---

## Trading Playbook (bear / Extreme-Fear regime)

As of **2026-06-24** the macro backdrop is hostile — crypto Fear & Greed **22 (Extreme Fear)**, market-health 28/100 (BEARISH), and a long-horizon **Established Bear Market** regime (BTC ≈ $62.6k, ETH ≈ $1.66k). For a low-float, narrative-driven L2 token, that environment is the least forgiving:

- **Default stance: caution / avoid chasing.** Low-float narrative tokens are the first to de-rate in risk-off conditions; the ~$4.5B FDV is hard to defend when liquidity dries up. Do not buy strength on a partnership headline without a liquidity plan.
- **Treat rallies as exit liquidity, not trend confirmation** while float remains ~8% and unlocks are pending — thin books make spikes mean-revert.
- **Unlock calendar is the master variable.** Map vesting/unlock dates before any position; rising circulating supply into weak demand is the canonical low-float failure mode.
- **Catalyst-driven only, small size:** if traded at all here, frame it as an event play around DDSC-volume or sovereign-L3 milestones with hard risk limits, not a buy-and-hold — and size for the ~$0.5M/day liquidity, not the headline market cap.
- **Hard invalidations:** confirmed large unlock with no matching adoption; loss/erosion of UAE regulatory standing for DDSC; or volume collapsing further toward illiquidity.

---

## Tokenomics & Supply

| Metric | Value (April 2026 snapshot) |
|---|---|
| **Circulating Supply** | 80.00M ADI (8%) |
| **Total Supply** | 1,000.00M ADI |
| **Max Supply** | 1,000.00M ADI |
| **Fully Diluted Valuation** | $4.48B |
| **Market Cap / FDV Ratio** | 0.08 |

**The low float is the single most important fact about ADI.** At the April 2026 snapshot only **80M of 1,000M ADI (8%)** was circulating, producing a ~$360M market cap against a **~$4.5B fully diluted valuation** (MC/FDV ≈ 0.08). In practice this means the market was capitalising the entire 1B-token supply at roughly the prevailing spot price while **~92% of tokens remained locked** — held by the Foundation, IHC/Sirius, team, and ecosystem allocations under a vesting schedule.

The structural consequence: any future emission/unlock adds sell-side supply against a thin circulating base, so even a flat fundamental story can translate into price decay as locked tokens vest. Newly-listed, government-narrative L2 tokens with single-digit float are precisely the cohort where headline market cap most overstates realisable value. **Watch the unlock/vesting schedule and the float percentage** as the dominant valuation variable — more than any product metric. (No fully-disclosed, dated unlock calendar is captured here; treat the 92% locked figure as the key overhang and verify the schedule before sizing.)

---

## Value Accrual & Governance

- **Gas token economics.** ADI accrues value primarily as the **gas/settlement asset** of ADI Chain — every transaction, DDSC transfer, e-invoice write, or L3 settlement consumes ADI for fees. Demand for the token is therefore a function of *actual on-chain activity* on ADI Chain and its Layer 3s, not just speculation. In a low-utilisation phase the fee sink is small; the bull case requires sovereign/enterprise workloads (DDSC volume, registries, L3 deployments) to scale into real, recurring gas demand.
- **Ecosystem alignment.** As the native asset, ADI is the unit in which ecosystem incentives, validator/prover rewards, and L3 settlement are denominated, aligning network participants with the chain's growth.
- **Governance.** ADI Chain is steered by the **ADI Foundation** (a single, IHC/Sirius-anchored sponsor) rather than by broad on-chain token-holder governance — closer to a consortium/enterprise model than a decentralised DAO. This concentrates direction-setting in one well-capitalised backer (a strength for execution and regulatory standing, a weakness for credible neutrality and decentralisation).

---

## Comparison vs Competitors

ADI competes for the "institutional / RWA / regulated-stablecoin rail" narrative. Its closest comparables are other zkStack chains and institution-backed L1/L2s with a flagship regulated asset.

| Project | Stack / type | Primary backer | Flagship asset / use case | Float profile |
|---|---|---|---|---|
| **ADI Chain (ADI)** | [[zksync\|zkSync]] zkStack ZK-rollup L2 + modular L3s | ADI Foundation / Sirius / IHC (Abu Dhabi) | **DDSC** UAE dirham stablecoin; sovereign/enterprise registries | Extreme low float (~8% circ at snapshot; MC/FDV ≈ 0.08) |
| **[[zksync\|zkSync (ZK)]]** | Native zkStack / Elastic Chain hub | Matter Labs | General-purpose ZK-rollup; ZK-stack interoperability hub | Larger float; broad public ecosystem |
| **Other RWA / institutional L1-L2s** | Varies (app-chains, permissioned L2s) | Varies (banks, asset managers) | Tokenised T-bills, funds, regulated stablecoins | Often low-float, foundation/VC-heavy |
| **Regional regulated-stablecoin rails / CBDC pilots** | Permissioned or hybrid chains | Central banks / national banks | Domestic-currency stablecoin / CBDC settlement | Typically no public token or tightly controlled |

**Read:** ADI's differentiation is the **state-backed Gulf flagship** (DDSC + UAE Central Bank licensing + IHC scale) and the zkStack base it shares with [[zksync|zkSync]]. Its disadvantage versus a hub like zkSync is float and decentralisation; its advantage versus generic RWA L2s is a live, regulated, sovereign-adjacent stablecoin already in production. See [[real-world-assets]] and [[stablecoins]] for the category.

---

## Price History

| Metric | Value (April 2026 snapshot) |
|---|---|
| **All-Time High** | $4.55 (2026-04-03) |
| **All-Time Low** | $0.9754 (2025-12-10) |
| **30d Change** | +45.48% |

---

## Platform & Chain Information

**Native Chain:** Ethereum (ERC-20); gas token of ADI Chain (zkSync zkStack L2)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x8b1484d57abbe239bb280661377363b03c89caea` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Kraken | ADI/USD |
| KuCoin | ADI/USDT |
| Crypto.com Exchange | ADI/USD |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | ADI/USDC | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://token.adi.foundation/](https://token.adi.foundation/) |
| **Twitter** | [@ADIChain_](https://twitter.com/ADIChain_) |
| **Telegram** | [adifoundation](https://t.me/adifoundation) (10,628 members) |
| **Discord** | [https://discord.com/invite/adi-foundation](https://discord.com/invite/adi-foundation) |
| **GitHub** | [https://github.com/ADI-Foundation-Labs](https://github.com/ADI-Foundation-Labs) |
| **Docs** | [https://docs.adi.foundation/](https://docs.adi.foundation/) |

---

## Related

- [[ethereum]], [[zksync]] — underlying stack
- [[chainlink]] — CCIP/interop partner (Mar 2026)
- [[stablecoins]] — DDSC dirham stablecoin settlement
- [[real-world-assets]], [[kraken]]
- [[crypto-markets]], [[crypto-narratives-overview]]

---

## Sources

- CoinGecko market data snapshot, 2026-04-09 (CoinGecko top-1000 ingest)
- ADI Foundation — https://www.adi.foundation/
- Businesswire, "Abu Dhabi-based ADI Foundation Launches Testnet of 'ADI Chain'" (2025-08-21) — https://www.businesswire.com/news/home/20250821599488/en/
- Decrypt, "Dirham-Backed Stablecoin DDSC Launches on ADI Chain, Licensed by the UAE Central Bank" — https://decrypt.co/357832/dirham-backed-stablecoin-ddsc-launches-on-adi-chain-licensed-by-the-uae-central-bank
- Crypto.com, "Sirius International Holding and Crypto.com Partner to Integrate ADI Chain" — https://crypto.com/en/company-news/sirius-international-holding-and-cryptocom-partner-to-integrate-adi-chain
- PR Newswire, "ADI Foundation and Chainlink Announce Official Partnership..." — https://www.prnewswire.com/news-releases/adi-foundation-and-chainlink-announce-official-partnership-to-accelerate-stablecoin-and-tokenization-strategy-across-the-middle-east-africa-and-asia-302701809.html
- Verified via web search, 2026-06-10: DDSC live Feb 2026, Chainlink partnership Mar 2026, Sirius/IHC origin, Crypto.com partnership Dec 2025

## Overview

ADI Chain is an Ethereum Layer 2 developed by the ADI Foundation to support government, enterprise, and institutional digital infrastructure. It is built on zkSync’s zkStack and powered by the Airbender prover, which delivers GPU accelerated zero knowledge proofs for fast, low cost, and secure transactions. The chain includes modular Layer 3 capabilities that let nations and enterprises deploy compliant, region specific systems for payments, e invoicing, land registries, and stablecoins. ADI Chain aims to bridge traditional systems with modern blockchain architecture and onboard one billion people by 2030.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 125.33M ADI |
| **Total Supply** | 1,000.00M ADI |
| **Max Supply** | 1,000.00M ADI |
| **Fully Diluted Valuation** | $6.98B |
| **Market Cap / FDV Ratio** | 0.13 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.56M |
| **Market Cap Rank** | #72 |
| **24h Range** | $6.96 — $7.10 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
