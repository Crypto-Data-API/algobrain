---
title: "2026 Hard-Fork Watchlist"
type: news
created: 2026-04-27
updated: 2026-06-12
status: good
tags: [crypto, hard-fork, forecast, watchlist, 2026]
aliases: ["2026 Fork Calendar", "Upcoming Forks 2026"]
event_date: 2026-12-31
markets_affected: [crypto]
impact: medium
verified: false
sources_count: 5
related: ["[[hard-fork]]", "[[fork-airdrop-triangulation]]", "[[fork-futures-spot-basis]]", "[[2022-09-ethereum-merge-fork-arbitrage]]", "[[2026-exploit-target-watchlist]]"]
---

# 2026 Hard-Fork Watchlist

A forward-looking tracker of **chain-split / contentious-fork events** scheduled, debated, or rumored for the 2026 calendar year. Distinct from L2 token launches and protocol airdrops (covered in [[airdrop-farming]]). Companion to the [[2026-exploit-target-watchlist]] (hack/exploit events). For traders, the goal is to **size positions in advance for fork-arb and IOU-basis trades** before pre-fork derivatives markets become efficient.

> **Forward-looking / speculative — read first.** This is a *living watchlist*, not an event record. It is updated quarterly and is intentionally speculative: status assessments reflect **April–June 2026** information, and many events listed may not occur in 2026 (or at all). Each event is classified by *probability of contentious split in 2026* (Low / Medium / High). The historical precedents cited (Steem→Hive 2020, Terra→Luna 2.0 2022, Juno Prop-16 2022, BCH 2018) are verified; the *forward* status of each pending upgrade (Fusaka, Glamsterdam, Firedancer, OP_CAT) changes fast — **verify current state via the linked primary sources before trading.** Listing is not a prediction.

## Bitcoin Ecosystem

### OP_CAT (BIP-420) Activation

| Field | Value |
|-------|-------|
| **Probability of contentious chain-split** | Low |
| **Type** | Soft fork (non-contentious by design; only forks if UASF without miner support) |
| **Status (Apr 2026)** | Activation pathway under active debate; verify current state via Bitcoin Core / mining-pool signaling before trading |

OP_CAT is a re-enabled opcode in Bitcoin script that enables **covenant primitives** — restrictions on how a UTXO can be spent in subsequent transactions. Removed by Satoshi in 2010 (likely due to bugs), re-introduced via BIP-420 by Ethan Heilman, Armin Sabouri, and others.

**Why it matters for traders:**
- Enables Bitcoin-native derivatives, vaults, more sophisticated bridges. New arbitrage surface for any BTC L2 design.
- If activation becomes contentious (UASF without miner support), could trigger first major BTC fork since 2018.
- Soft-fork activations are usually non-contentious — historical precedent (SegWit, Taproot) shows minimal fork-arb opportunity.

**Trade angle (if contentious activation pathway emerges):**
- Pre-fork BTC accumulation on exchanges that historically credit forks (Bitfinex, Kraken).
- Short pre-fork IOU futures if any venue lists them (low probability — exchanges generally hesitant post BCH/BSV).
- Cross-exchange arb on listing speed differential.

**Risk:** Most likely outcome is non-contentious soft-fork activation OR no activation. The fork-arb edge only triggers if a UASF coalition pushes activation against miner consensus — rare since 2017.

**Verify before trading:** Status of OP_CAT activation can change rapidly; check coin.dance signaling and Bitcoin Core release notes.

---

### Bitcoin Knots vs Core Relay-Policy Dispute

| Field | Value |
|-------|-------|
| **Probability of contentious fork in 2026** | Low-Medium |
| **Type** | Could escalate to UASF / hard fork |
| **Status** | Knots client share growing; Core devs split on relay-policy changes |

**Bitcoin Knots** (maintained by Luke Dashjr) has been promoted as a "stricter" alternative to Bitcoin Core, particularly around **relay policy** for non-financial uses (Ordinals, Runes, BRC-20). As of late 2025, Knots usage among non-mining nodes has grown to ~10-15% (estimated; not authoritatively measured).

**Why it matters for traders:**
- Relay-policy changes are not consensus rules — they don't directly cause forks.
- However, the *narrative* of "Bitcoin spam filtering" is escalating.
- If a UASF emerges to enforce stricter relay defaults *as consensus rules*, this would trigger a fork.

**Trade angle (if escalates):**
- Long BTC + short BCH/LTC pair (BCH and LTC have historically benefited from BTC contention).
- Monitor Knots-vs-Core node share via [coin.dance](https://coin.dance/nodes) or similar.

**Risk:** Most likely 2026 outcome is continued debate without formal split. The dispute is more cultural than technical.

---

### Drivechain (BIP-300/301)

| Field | Value |
|-------|-------|
| **Probability of contentious fork in 2026** | Very Low |
| **Type** | Soft fork |
| **Status** | Long-debated; no current activation pathway |

Paul Sztorc's BIP-300/301 proposes a soft fork to enable **trustless sidechains** on Bitcoin. Has been debated since 2017; not currently on any roadmap for activation. Listed here for completeness.

**Trade angle:** Watch for any formal activation pathway announcement; if it emerges, the implications are large (Bitcoin-native L2 ecosystem).

---

## Ethereum Ecosystem

### Fusaka Upgrade (Q1-Q2 2026 expected)

| Field | Value |
|-------|-------|
| **Probability of contentious fork in 2026** | Very Low |
| **Type** | Non-contentious hard fork (planned upgrade) |
| **Status** | Scheduled; testnet activation in late 2025 |

Ethereum's Fusaka upgrade combines Osaka (EVM features) and Fulu (consensus features). Expected components: PeerDAS for full data availability sampling, EOF (EVM Object Format), additional precompiles. **Non-contentious — no minority refusing the upgrade.**

**Why it matters for traders:**
- *Negative case study* — a planned upgrade does NOT create fork-arb opportunity, despite the technical "hard fork" label.
- However, **gas economics changes** can shift validator/staking economics → indirect L2 / staking-token impact.
- PeerDAS fully unlocks blob scaling → further L2 transaction-cost reduction.

**Trade angle:**
- Long L2 ecosystem tokens (ARB, OP, BASE) into the activation as transaction costs drop further.
- Long Lido / Rocket Pool LSTs if validator economics improve.
- *No fork-arb trade* — the upgrade has no minority chain.

---

### Glamsterdam (post-Fusaka, late 2026)

| Field | Value |
|-------|-------|
| **Probability of contentious fork in 2026** | Very Low |
| **Type** | Non-contentious hard fork (planned upgrade) |
| **Status** | Specifications in flux |

Successor upgrade to Fusaka; specifications still being finalized. Likely to include: account abstraction native support, additional execution-layer changes, possible Verkle tree migration.

**Trade angle:** Same as Fusaka — no fork-arb; indirect L2/staking impact.

---

## Solana Ecosystem

### Firedancer Mainnet Rollout

| Field | Value |
|-------|-------|
| **Probability of contentious fork in 2026** | Very Low |
| **Type** | Client diversification (NOT a chain-split by design) |
| **Status (Apr 2026)** | Rollout in progress (Frankendancer + Firedancer); full validator-share TBD — verify via Solana validator dashboard |

Firedancer is Jump Crypto's alternative Solana validator client. Until Firedancer, Solana ran on a single-client monoculture (Solana Labs's `agave` client) — a major systemic risk.

**Why it matters for traders:**
- *Reduces* fork risk on Solana by client diversification (no longer single point of consensus failure).
- Could **trigger** fork events if clients disagree on edge-case validation rules — historically the case for Ethereum (geth vs nethermind disagreements caused minor splits).

**Trade angle:**
- *Indirect:* Long SOL into Firedancer activation as a "reduced systemic risk" thesis.
- Watch for any client-disagreement events post-launch — would create brief MEV / arb opportunities on the validator-software boundary.

---

### Solana Emergency Restart Risk (ongoing)

| Field | Value |
|-------|-------|
| **Probability of contentious fork in 2026** | Low (chain-restart events expected; not contentious splits) |
| **Type** | Validator-coordinated chain restart (not a true fork) |
| **Status** | Recurring pattern; multiple restarts 2021-2024 including May 2024 |

Solana has restarted ~10 times since launch. These are *not* chain-split forks (no minority chain persists); they're validator-coordinated rollbacks to recover from network outages. Listed for completeness as **fork-adjacent risk events**.

**Trade angle:**
- Brief MEV / arbitrage during restart freeze (centralized exchanges suspend, on-chain DEXes freeze, perpetual funding rates spike).
- Long-only liquidations frozen during restart — short-vol on Solana derivatives during restart announcements.

---

## Cosmos Ecosystem

### Cosmos Hub Governance Disputes (ongoing)

| Field | Value |
|-------|-------|
| **Probability of contentious fork in 2026** | Medium |
| **Type** | Chain-by-chain governance forks |
| **Status** | Multiple active disputes (Atom 2.0, fee market, ICS) |

Cosmos's modular architecture (each "zone" is a sovereign chain) makes governance-driven forks more frequent than monolithic chains. Cosmos Hub specifically has had repeated proposals for major changes (Atom 2.0 rejection 2022, ICS replicated security launch 2023, fee-market debates 2024-2025).

**Watchlist for 2026:**
- **Atom 2.0 v2 proposal** (rumored).
- **ICS chain participation** — if a major partner chain (Stride, Neutron) splits over governance.
- **Juno Network** had a significant governance split in 2022 (Whale-stake slashing, Proposal 16); similar events possible for other Cosmos zones in 2026.

**Trade angle:**
- Long ATOM stake on Stride / pStake LST and pair-trade against ATOM — capture yield + governance token dynamics.
- Monitor governance proposal forums (Cosmos Hub Discourse, Commonwealth).

---

## Polkadot / Substrate Ecosystem

### Polkadot 2.0 (Asynchronous Backing live, 2025)

| Field | Value |
|-------|-------|
| **Probability of contentious fork in 2026** | Very Low |
| **Type** | Non-contentious upgrade |
| **Status** | Async backing live; Coretime active |

Polkadot's transition to elastic scaling and Coretime is technically complex but non-contentious. No fork-arb opportunity expected.

**Trade angle:** Indirect — DOT's auction model has been replaced with Coretime; this affects parachain-token economics. No direct fork-arb.

---

## NEAR / Aurora / Aptos / Sui

| Chain | Fork Probability 2026 | Notes |
|-------|----------------------|-------|
| NEAR | Very Low | Roadmap focused on chain abstraction; no contentious splits planned |
| Aurora (EVM on NEAR) | Very Low | Aurora has had its own AURORA token (Sep 2022); future spin-offs possible but not scheduled |
| Aptos | Low | Single client (aptos-core); monoculture risk but no fork pressure |
| Sui | Low | Mysticeti upgrade complete; no fork pressure |

---

## Tron / EOS / BSC

| Chain | Fork Probability 2026 | Notes |
|-------|----------------------|-------|
| Tron | Very Low | Justin Sun-controlled; unilateral governance |
| EOS | Low-Medium | Long-running EOS Network Foundation vs Block.one disputes; chain-swap rumored multiple times |
| BNB Chain | Very Low | Binance-controlled; centralized governance |

---

## Trader Action Items

For 2026, the **highest-probability fork-arb opportunities** are:

1. **Cosmos governance-driven chain splits** — Medium probability; multiple active disputes.
2. **Bitcoin OP_CAT contentious activation** — Medium-Low probability; depends on UASF dynamics.
3. **Ethereum non-contentious upgrades** (Fusaka, Glamsterdam) — Negative case studies; no fork-arb but indirect L2/staking impact.
4. **Solana network restarts** — Brief restart-window arb; not chain-split events.

**Most likely 2026 surprise:** A previously-quiet chain having a contentious governance split that wasn't on the public roadmap. Historical pattern suggests 1-2 surprise forks per year (Steem→Hive 2020, Terra→Luna 2.0 2022 were both unexpected). Watchlist sources:

- [coin.dance](https://coin.dance/nodes) — node distribution (Bitcoin Knots/Core)
- Ethereum All-Core-Devs (ACD) calls — official upgrade roadmap
- Cosmos governance forums (Discourse, Commonwealth)
- Solana validator status pages
- Hard-fork tracking aggregators (CoinGecko Forks, Messari)

## Update Schedule

This page is updated quarterly. Last update: **2026-04-27**. Next update: **2026-07-31**.

## Related

[[hard-fork]] · [[fork-airdrop-triangulation]] · [[fork-futures-spot-basis]] · [[2017-08-bitcoin-cash-fork-arbitrage]] · [[2022-09-ethereum-merge-fork-arbitrage]] · [[2020-03-steem-hive-fork-arbitrage]] · [[2022-05-terra-luna-2-fork-arbitrage]] · [[ethereum]] · [[bitcoin]] · [[solana]]

## Sources

- Bitcoin Improvement Proposal 420 (OP_CAT) — Ethan Heilman et al.
- Ethereum Foundation: "Fusaka Upgrade Specifications" (2025).
- Jump Crypto: Firedancer development blog (2024-2025).
- Cosmos Hub governance forum (forum.cosmos.network).
- Polkadot Wiki — Asynchronous Backing documentation.
