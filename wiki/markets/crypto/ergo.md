---
title: "Ergo"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["ERG", "Ergo Platform"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://ergoplatform.org/en/"
related: ["[[crypto-markets]]", "[[proof-of-work]]", "[[smart-contracts]]", "[[utxo]]"]
---

# Ergo

**Ergo** (ERG) is a [[proof-of-work]] [[layer-1]] smart-contract blockchain built on an **extended UTXO ([[utxo|eUTXO]])** model. Unlike account-based chains such as [[ethereum]], Ergo guards every coin (box) with a program written in **ErgoScript**, a non-Turing-complete contract language whose primitives are **Sigma protocols (Σ-protocols)** — cryptographic proofs that enable ring signatures, threshold signatures, and zero-knowledge–style spending conditions natively. Ergo emphasizes long-term survivability, fair launch, and contractual money. It currently ranks **#877** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As of 2026-06-21 ERG trades at **$0.214978** with a market cap of **$17,893,744** (rank **#877**), roughly flat over 24h (**+0.08%**) and down **-4.64%** over the prior 7 days during an Extreme Fear market (Fear & Greed 22; BTC ~$64,180).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ERG |
| **Market Cap Rank** | #877 |
| **Market Cap** | $17,893,744 |
| **Current Price** | $0.214978 |
| **24h Change** | +0.08% |
| **7d Change** | -4.64% |
| **Consensus** | [[proof-of-work]] — Autolykos v2 (memory-hard, ASIC-resistant) |
| **Accounting Model** | Extended UTXO ([[utxo|eUTXO]]) |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Proof of Work (PoW), Contractual Money |
| **Website** | [https://ergoplatform.org/en/](https://ergoplatform.org/en/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Ergo is a flexible [[layer-1]] protocol focused on providing an efficient, secure and easy way to implement financial contracts. Every coin (box) in Ergo is protected by a program in **ErgoScript**, a powerful and protocol-friendly scripting language based on **Sigma protocols**. Using ErgoScript, users encode the conditions under which coins may be spent: who can spend them, when, under what external conditions, and to whom.

Ergo follows a "survivability" approach — it favors widely-researched, conservative cryptography over novel-but-fragile designs, supports light clients on commodity hardware (NIPoPoWs / "non-interactive proofs of proof-of-work" enable trustless light nodes), and uses a self-amendable protocol so it can adopt new ideas over time without contentious hard forks.

---

## Architecture & Consensus

Ergo's thesis is **contractual money**: a base-layer chain conservative enough to be trusted with value for decades, yet expressive enough to encode rich financial agreements directly into the coins themselves. It pursues this with battle-tested cryptography (Sigma protocols), Bitcoin-lineage accounting (eUTXO), and a fair, no-premine launch. Network value scales with on-chain financial activity — every [[defi]] contract, every box spend, consumes ERG for fees and storage rent.

- **Autolykos (PoW)**: Ergo mines with **Autolykos v2**, a memory-hard [[proof-of-work]] algorithm designed to be ASIC-resistant and GPU-friendly, favoring decentralized mining and discouraging mining-pool centralization (v1 included a *non-outsourceable* puzzle that made pooled mining harder, pushing toward solo/decentralized participation).
- **eUTXO model**: Ergo extends Bitcoin's [[utxo]] model with rich scripting, **data inputs** (read-only references to other boxes, enabling shared oracle state) and **context variables**, giving deterministic, parallelizable transaction validation while still supporting complex [[defi]] logic. This is the same accounting lineage later popularized by [[cardano]], but Ergo shipped it on a working PoW chain first. Determinism means a transaction's validity and fees are known before submission — no failed-but-charged transactions as on account-based EVM chains.
- **Sigma protocols (Σ-protocols)**: ErgoScript compiles spending conditions into Σ-protocol statements — zero-knowledge proofs of knowledge — enabling **ring signatures, threshold (multisig) spends, and privacy-preserving conditions natively at the base layer**, without bolt-on mixers or L2s.
- **NIPoPoWs**: non-interactive proofs of proof-of-work let light clients verify the chain by checking a logarithmic sample of "superblocks," enabling trustless light wallets and bootstrapping on commodity/mobile hardware — a survivability feature few PoW chains have.
- **Storage rent**: long-dormant boxes (untouched ~4 years) can be charged a small "storage rent," recycling abandoned state and providing a **sustainable long-term [[proof-of-work|miner]] incentive once block subsidy declines** — Ergo's answer to Bitcoin's eventual security-budget question.
- **Self-amendable protocol**: miners can vote to adjust certain parameters on-chain, letting Ergo adopt improvements without contentious hard forks.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 83.08M ERG |
| **Total Supply** | 97.74M ERG |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $29.40M |
| **Market Cap / FDV Ratio** | 0.85 |

Ergo has **no premine, no ICO, and no founder/VC allocation** — emission is purely mined, which means there are no scheduled unlock cliffs and no concentrated insider supply waiting to sell. The ~0.85 cap/FDV ratio reflects mined-but-not-yet-emitted coins on the smoothly declining schedule, not a low-float VC structure. This fair-launch profile is a structural differentiator versus venture-backed peers like [[anoma]] or [[caldera]].

---

## Comparison vs Peer Chains

Ergo is most naturally compared to other **UTXO-model smart-contract chains** and to **fair-launch PoW chains**:

| Dimension | **Ergo (ERG)** | **Cardano (ADA)** | **Bitcoin (BTC)** | **Nervos CKB** |
|---|---|---|---|---|
| **Accounting** | Extended UTXO (eUTXO) | Extended UTXO (eUTXO) | UTXO (script-limited) | Cell model (UTXO-like) |
| **Consensus** | PoW (Autolykos v2) | PoS (Ouroboros) | PoW (SHA-256, ASIC) | PoW (Eaglesong) |
| **Smart contracts** | ErgoScript + Σ-protocols | Plutus / Haskell | Limited Script / Taproot | RISC-V (CKB-VM) |
| **Launch** | Fair, no premine | Premine + ICO | Fair, no premine | Premine + sale |
| **Native privacy** | Yes (ring/threshold sigs) | Limited | Limited | Limited |
| **Niche** | Contractual money, [[defi]] | Smart-contract L1 | Store of value | Store-of-value + L1 |

Ergo's combination of **eUTXO expressiveness + fair-launch PoW + native Σ-protocol privacy** is essentially unique: [[cardano]] shares the eUTXO model but is PoS and premined; Bitcoin shares the fair launch and PoW but lacks rich scripting; Nervos shares the modern UTXO+PoW idea but was pre-sold. See [[utxo]] and [[proof-of-work]].

---

## How & Where It Trades

- **Spot venues:** ERG is comparatively under-listed for its age. **KuCoin** (ERG/USDT) is the primary deep CEX pair; historically it has traded on Gate, and on-chain via Ergo-native DEXs (**Spectrum / ErgoDEX**) and the **SigmaFi** lending market. There is **no Binance listing**, which constrains liquidity and discoverability.
- **Liquidity profile:** very thin — reported 24h volume is only on the order of low six figures against a ~$18M cap. ERG is **slippery to trade in size**; spreads widen fast and large orders move the book materially. This is a hold-or-accumulate asset more than an active-trading vehicle.
- **Derivatives:** essentially no liquid perp/futures market. Spot-only; no practical hedging venue, so position sizing is the sole risk control.
- **Self-custody friendly:** because Ergo is a true L1 with light clients (NIPoPoWs), holders can custody natively rather than relying on exchange IOUs.

---

## Narrative, Category & Catalysts

Ergo's narrative is **"contractual money" + fair-launch survivalist chain** — it appeals to a Bitcoin-adjacent, ideologically motivated holder base that values no-premine fairness, conservative cryptography, and self-custody over hype cycles. It is not chasing the throughput or AI narratives; its bet is long-term durability and base-layer [[defi]] (SigmaUSD, SigmaFi, Spectrum).

**Potential catalysts:**
- Growth of Ergo-native [[defi]] (SigmaUSD stablecoin adoption, SigmaFi lending, Spectrum DEX volume) driving real ERG fee demand.
- Renewed interest in **fair-launch / no-VC** narratives during periods of distrust toward insider-allocated tokens.
- Tier-1 exchange listings improving liquidity (a perennial "missing catalyst").
- Cross-chain bridges (e.g., Rosen Bridge) expanding ERG's reach into other ecosystems.

**Headwinds:** the eUTXO + ErgoScript learning curve keeps developer adoption slow, and without major-exchange listings ERG struggles for liquidity and attention even when fundamentals progress.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $18.72 (2021-09-03) |
| **Current vs ATH** | -98.39% |
| **All-Time Low** | $0.0942 (2020-03-13) |
| **Current vs ATL** | +128.2% |
| **24h Change (2026-06-21)** | +0.08% |
| **7d Change (2026-06-21)** | -4.64% |

> *Earlier 30d/1y figures from the 2026-06-12 snapshot are superseded by the 2026-06-21 figures above.*

---

## ERG Token

ERG is the native gas and reward coin of the Ergo chain. It is:

- **Mined** via Autolykos [[proof-of-work]] (fair launch — no pre-mine, no ICO, no founder/VC allocation);
- Used to **pay transaction fees** and storage rent;
- The **collateral and unit of account** for Ergo [[defi]] (e.g., SigmaUSD, a contract-collateralized stablecoin, and the SigmaFi / Spectrum ecosystem).

Supply is capped at ~97.74M ERG via a smoothly declining emission schedule that completed its primary issuance, after which storage rent sustains miner rewards.

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| KuCoin | ERG/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ergoplatform.org/en/](https://ergoplatform.org/en/) |
| **Twitter** | [@Ergo_Platform](https://twitter.com/Ergo_Platform) |
| **Reddit** | [https://www.reddit.com/r/ergonauts/](https://www.reddit.com/r/ergonauts/) |
| **Telegram** | [ergoplatform](https://t.me/ergoplatform) (8,116 members) |
| **Discord** | [https://discord.com/invite/PFYugUgg28](https://discord.com/invite/PFYugUgg28) |
| **GitHub** | [https://github.com/ergoplatform/ergo](https://github.com/ergoplatform/ergo) |
| **Whitepaper** | [https://ergoplatform.org/docs/whitepaper.pdf](https://ergoplatform.org/docs/whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 482 |
| **GitHub Forks** | 172 |
| **Commits (4 weeks)** | 42 |
| **Pull Requests Merged** | 1,012 |
| **Contributors** | 43 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $159,426.00 |
| **Market Cap Rank** | #859 |
| **24h Range** | $0.2991 — $0.3030 |
| **CoinGecko Sentiment** | 67% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## History & Timeline

| Date | Event |
|---|---|
| **2019-07** | Ergo mainnet launches with a fair, no-premine PoW emission. |
| **2020-03-13** | All-time low of **$0.0942** during the COVID crash. |
| **2021-09-03** | All-time high of **$18.72** during the bull market. |
| **2021–2024** | ~98% multi-year drawdown alongside the broad altcoin bear; ecosystem builds out SigmaUSD, SigmaFi, Spectrum DEX. |
| **Ongoing** | Continued protocol development (43 contributors, ~1,000+ merged PRs), Rosen Bridge cross-chain expansion, and primary issuance tailing into the storage-rent era. |

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

> *Not investment advice. Crypto assets are highly volatile and can go to zero.*

**Technical / protocol**
- **PoW security budget**: as a smaller-cap [[proof-of-work]] chain (~$18M), Ergo has a modest hashrate and is theoretically more exposed to 51% pressure than top-tier PoW chains; Autolykos ASIC-resistance helps but does not eliminate this.
- **Long-term emissions/fee model**: sustainability depends on storage rent and transaction fees replacing block subsidy as primary issuance tails off — an unproven equilibrium at scale.

**Adoption / ecosystem**
- **Niche tooling**: the eUTXO + ErgoScript model has a steeper learning curve than EVM [[solidity]], which has constrained developer adoption versus account-based ecosystems.
- **No tier-1 listing / discoverability**: the absence of a Binance listing limits liquidity and mindshare even when the protocol ships.

**Market / liquidity**
- **Thin liquidity**: at rank ~#877 with low daily volume, ERG can be volatile and slippery to trade; exiting size is genuinely difficult.
- **Bear-market beta**: like other small caps, ERG carries high beta to BTC in risk-off regimes.

---

## Trading Playbook

> *Educational framing, not advice.*

- **Regime read (2026-06-22):** Established Bear Market, Extreme Fear (F&G 21). ERG sits near multi-year lows; MVRV-style accumulation conditions across crypto, but small-cap PoW with thin liquidity means patience and tight sizing are essential.
- **Investment vs trade:** ERG is structurally an **accumulate-and-hold / conviction** asset, not a momentum trade — thin books make active trading costly. The bull case is fundamental (fair launch, contractual money, native privacy) and multi-year.
- **What to watch (bullish):** Ergo-native [[defi]] TVL/volume growth (SigmaFi, Spectrum, SigmaUSD peg health), a tier-1 exchange listing, and a broad market rotation toward fair-launch / no-VC narratives.
- **What to watch (bearish):** hashrate declines (security-budget stress), continued absence of liquidity catalysts, or BTC breaking to new lows dragging small caps with it.
- **Mechanics:** trade only with limit orders, expect wide spreads, and assume you cannot exit a large position quickly. Self-custody is well supported via native light clients.

---

## See Also

- [[crypto-markets]]
- [[utxo]]
- [[proof-of-work]]
- [[smart-contracts]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
