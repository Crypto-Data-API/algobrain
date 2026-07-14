---
title: "Proof of Reserves"
type: source
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [data-provider, crypto, exchange, risk-management, on-chain, counterparty-risk]
aliases: ["PoR", "Proof-of-Reserves", "Merkle Proof of Reserves", "Proof of Solvency"]
source_type: data
source_url: "https://defillama.com/cexs"
source_author: "DefiLlama (aggregator); Nic Carter (proofofreserves.com)"
source_date: 2026-07-14
confidence: medium
claims_count: 8
related: ["[[ftx]]", "[[binance]]", "[[exchange-api-key-security]]", "[[bot-kill-switch-design]]", "[[position-reconciliation]]", "[[cryptoquant]]", "[[nansen]]", "[[glassnode]]", "[[dune-analytics]]", "[[cryptodataapi-market-intelligence]]", "[[cryptodataapi-on-chain]]"]
---

# Proof of Reserves

Proof of Reserves (PoR) is a cryptographic attestation by which a centralized exchange (CEX) publishes evidence that it holds on-chain assets backing customer balances. For a trader running capital on a CEX, PoR is best understood not as a guarantee but as a **counterparty-health monitoring signal** — one live input, alongside on-chain reserve tracking and flow data, for deciding how much capital to trust to a given venue and when to pull it. Its confidence is deliberately marked *medium*: PoR proves something real (the exchange controls certain assets) but leaves the more important question — **are those assets greater than total liabilities?** — largely unproven. It is proof of *reserves*, not proof of *solvency*.

## Why PoR exists: the post-FTX context

Before November 2022, "PoR" was a niche idea advocated by a handful of people (notably Nic Carter, who maintains the `proofofreserves.com` directory). Then **FTX collapsed** — filing Chapter 11 on 11 November 2022 with a customer shortfall later estimated around **$8 billion** — after commingling customer funds with its Alameda trading arm and backing balances heavily with its own illiquid **FTT** token. FTX published no meaningful reserve attestation; customers had no way to see that the reserves were not there.

The immediate industry response was a wave of PoR publications from **Binance, OKX, Kraken, Bybit, Crypto.com, Bitget, KuCoin, Gate.io** and others, plus Vitalik Buterin's November 2022 note *"Having a safe CEX: proof of solvency and beyond"*, which sketched the Merkle-sum-tree-plus-zero-knowledge design that better PoR systems now use. PoR is thus a *reaction* to a specific, catastrophic failure — which is exactly why it must be read as a partial control, not a solved problem.

## How Merkle-proof PoR works

A credible PoR has two halves that must be checked *together*:

1. **Liabilities (Merkle tree of customer balances).** The exchange builds a **Merkle tree** whose leaves are (hashed) customer balances and publishes the **Merkle root**. Each user is given the path from their own leaf to the root, so they can independently verify their balance was **included** in the total the exchange claims to owe — and cannot be quietly omitted. A **Merkle-sum tree** additionally carries the balance sum up the tree so the root encodes total liabilities, not just membership.
2. **Reserves (on-chain asset attestation).** The exchange demonstrates control of on-chain addresses holding assets — historically by moving a nonce amount or signing a message from those wallets — so the public can total the reserves and compare to the claimed liabilities.

**Solvency claim** = reserves (half 2) ≥ liabilities (half 1). Only when both halves are present and reserves cover the summed liabilities does PoR approximate a proof of solvency.

### zk-SNARK / proof-of-solvency PoR

Naive Merkle PoR leaks information (users can infer others' balances) and lets the exchange hide negative balances. The stronger design uses **zero-knowledge proofs** (zk-SNARKs) over a Merkle-sum tree to prove, without revealing any individual balance, that: every user balance is **non-negative**, each user is included, and the **sum of liabilities** equals the value the reserves are checked against. **Binance open-sourced a zk-SNARK PoR ("zkPoR")** system on this principle. This closes the "hidden negative balance" and privacy gaps — but still does **not** address the liabilities the exchange never puts into the tree at all.

## What PoR does and does not prove

| PoR **can** show | PoR **cannot** show |
|---|---|
| The exchange controlled specific on-chain assets **at the snapshot time** | That it still controls them a minute later, or that they were not **borrowed just for the snapshot** |
| That your balance was **included** in the liability tree | That there are **no off-chain / undisclosed liabilities** (loans, debts, obligations, legal claims) |
| (with zk) that all balances are **non-negative** and the liability sum is honest | That reserves are **unencumbered** (not pledged, rehypothecated, or double-counted across entities) |
| A **point-in-time** assets-vs-liabilities comparison | **Real-time** solvency — most attestations are periodic snapshots, not continuous |

The decisive gap is the **liabilities view**. An exchange can hold billions on-chain and still be deeply insolvent through off-chain debt that no Merkle tree captures. This is why PoR is a *screen*, not a *seal*: a passing PoR lowers the probability of an FTX-style asset-absence, but does nothing about the hidden-liability failure mode.

### Known ways PoR is gamed or fails

- **Snapshot borrowing ("window dressing").** Assets borrowed shortly before the attestation timestamp and returned after inflate reserves for the snapshot. Continuous on-chain reserve tracking (below) is the antidote.
- **Own-token reserves.** Reserves composed heavily of the exchange's **own illiquid token** (the FTX/FTT pattern; a concern also raised about other venues' native tokens) are not real coverage — in a run, that token collapses precisely when it is needed.
- **Attestor fragility.** Auditor/attestor involvement has proven unreliable: **Mazars** produced an "agreed-upon procedures" report for Binance in December 2022, then **paused all crypto work and removed the reports**; **Armanino** (which attested Kraken and others) **exited crypto** in early 2023. An attestation is only as durable as the firm standing behind it.
- **No liabilities half.** Some "PoR" pages show only wallet balances (reserves) with no verifiable liability tree — an assets-only figure that says nothing about solvency.

## Where to get it

| Source | What it provides | Notes |
|---|---|---|
| **DefiLlama — CEX Transparency** (`defillama.com/cexs`) | Real-time **on-chain reserves** per exchange, asset breakdown, **% held in own token**, clean/"suspicious" flags | Free; tracks the *reserves* half continuously — the best defense against snapshot-borrowing. Assets only, not liabilities |
| **Individual exchange PoR pages** | Merkle-tree self-verification + reserve attestations (Binance zkPoR, OKX, Kraken, Bybit, Bitget, Crypto.com) | The liabilities half lives here; check the attestation date and whether a liability tree exists |
| **[[nansen]]** | PoR dashboards / wallet-labelled reserve tracking | Wallet-level attribution of exchange holdings |
| **[[cryptoquant]]** | Exchange **reserve** and flow data, per-exchange | Strong exchange-flow granularity |
| **[[glassnode]]** | Aggregate exchange balances | Macro on-chain context |
| **proofofreserves.com** (Nic Carter) | Directory of which exchanges publish PoR and how | Reference for methodology and coverage |

## Using PoR as a live-risk input

PoR and its sibling on-chain reserve feeds turn counterparty health into a **quantifiable, automatable gate** on how much capital a bot trusts to each venue — complementing [[exchange-api-key-security|key security]] (which bounds loss from *your* compromise) with a bound on loss from *the venue's* failure. Practical wiring:

- **Venue-exposure gate.** Cap capital per venue as a function of its coverage ratio and reserve trend; reduce the cap when on-chain reserves fall sharply, when the % in the exchange's **own token** rises, or when a large sustained **net outflow** appears (the on-chain tell of a bank run — as preceded FTX).
- **Staleness / attestor trigger.** Treat a **stale PoR** (no fresh attestation on schedule), a **removed report**, or an **attestor exit** as a de-risking signal — pull working capital toward self-custody or a healthier venue.
- **Black-swan escalation.** Feed a venue-health deterioration into the [[bot-kill-switch-design|kill switch]] as a counterparty trigger — flatten and withdraw from the affected venue before a withdrawal halt makes exit impossible.
- **Corroborate, do not trust blindly.** Cross-check a published PoR against continuous DefiLlama/[[cryptoquant]] reserve tracking; a healthy snapshot contradicted by steady on-chain outflows is a warning, not reassurance.

The honest framing: PoR meaningfully lowered the odds of a silent, total FTX-style asset-absence, and continuous reserve tracking closes the snapshot-gaming gap — but no available attestation closes the hidden-liability gap. Self-custody remains the only elimination of CEX counterparty risk; PoR is risk **management**, not risk removal.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI does not publish exchange PoR attestations, but it serves the **reserves-and-flows half** of the signal — the continuous, on-chain measures that catch snapshot-gaming and bank-run outflows between (or instead of) formal attestations:

**Live data:**
- `GET /api/v1/market-intelligence/exchange-balance` — aggregate exchange BTC balance + flow (reserve-trend signal)
- `GET /api/v1/on-chain/stablecoin-reserves` — CEX stablecoin reserves (ETH/Tron/BSC); the dry-powder / coverage side
- `GET /api/v1/on-chain/exchange-flows/{symbol}` — per-exchange CEX inflow/outflow, 1h–7d windows (net-outflow / bank-run tell)
- `GET /api/v1/on-chain/exchange-flows/spike-alerts` — real-time large transfers (>=$1M), whale deposits/withdrawals
- `GET /api/v1/security/regime` — recent hacks/depegs + Security Stress score, as a counterparty black-swan overlay

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/on-chain/exchange-flows/BTC"
```

Auth: `X-API-Key` header. Catalogs: [[cryptodataapi-market-intelligence]], [[cryptodataapi-on-chain]].

## Related

- [[ftx]] — the collapse that made PoR mainstream; the hidden-liability / own-token failure archetype
- [[binance]] — reference implementation (Merkle + open-sourced zk-SNARK zkPoR)
- [[exchange-api-key-security]] — the complementary control (your access vs the venue's solvency)
- [[bot-kill-switch-design]] — where a counterparty-health trigger flattens and withdraws
- [[position-reconciliation]] — venue-truth accounting the PoR gate sits above
- [[cryptoquant]] / [[nansen]] / [[glassnode]] / [[dune-analytics]] — on-chain reserve and flow data sources
- [[cryptodataapi-on-chain]] / [[cryptodataapi-market-intelligence]] — the CryptoDataAPI reserve/flow endpoints

## Sources

- DefiLlama CEX Transparency dashboard (https://defillama.com/cexs) — continuous on-chain reserve tracking, own-token share, per-exchange breakdown.
- Nic Carter, `proofofreserves.com` — directory and methodology reference for exchange PoR.
- Vitalik Buterin, "Having a safe CEX: proof of solvency and beyond" (19 November 2022) — Merkle-sum-tree + zero-knowledge design.
- Binance zk-SNARK Proof of Reserves (zkPoR) — open-sourced privacy-preserving PoR (public docs / repo).
- FTX Chapter 11 filing, 11 November 2022; ~$8B customer shortfall (widely reported) — the motivating failure.
- Mazars (December 2022 Binance agreed-upon-procedures report, subsequently paused/removed) and Armanino (crypto exit, early 2023) — evidence of attestor fragility.
