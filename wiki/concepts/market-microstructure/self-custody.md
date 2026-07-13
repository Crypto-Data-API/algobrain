---
title: "Self-Custody"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [crypto, defi, risk-management]
aliases: ["self-custodial", "non-custodial", "not your keys not your coins", "self-custody wallet"]
domain: [market-microstructure]
prerequisites: ["[[blockchain]]"]
difficulty: beginner
related: ["[[blockchain]]", "[[defi]]", "[[decentralized-exchanges]]", "[[ftx]]", "[[smart-contracts]]", "[[counterparty-risk]]", "[[rehypothecation]]"]
---

# Self-Custody

**Self-custody** means holding your own private keys and maintaining direct control over your cryptocurrency assets, rather than entrusting them to a third party like a centralized exchange. The principle is captured by the maxim: **"Not your keys, not your coins."**

---

## How It Works

Cryptocurrency ownership is determined by control of **private keys** -- cryptographic secrets that authorize transactions. Self-custody involves storing these keys yourself using:

| Method | Description | Security Level |
|---|---|---|
| **Hardware wallets** | Dedicated devices (Ledger, Trezor) that store keys offline | Highest |
| **Software wallets** | Desktop or mobile apps (MetaMask, Phantom, Rabby) | Moderate |
| **Paper wallets** | Private keys printed or written on physical media | High (if stored securely) |
| **Multi-sig wallets** | Require multiple key holders to approve transactions | Highest (institutional grade) |

**Seed phrases** (12 or 24 words) serve as the master backup for most wallets. Losing your seed phrase with no other backup means permanent, irrecoverable loss of funds.

---

## Why Self-Custody Matters for Traders

The collapses of [[ftx|FTX]], [[blockfi|BlockFi]], [[voyager-digital|Voyager]], and Celsius in 2022 demonstrated the catastrophic risk of custodial platforms. Billions in customer funds were frozen or lost when these entities became insolvent.

Self-custody enables:
- **No counterparty risk** -- assets cannot be frozen, seized, or lost due to exchange insolvency
- **Direct [[defi]] access** -- interact with [[decentralized-exchanges|DEXs]], lending protocols like [[aave]], and on-chain strategies
- **Transparency** -- verify holdings on-chain at any time

---

## Tradeoffs

- Self-custodied assets require personal responsibility for security (phishing, malware, physical theft)
- No customer support or password recovery -- errors are irreversible
- [[smart-contracts|Smart contract]] interaction carries its own risks (approvals, exploits)

---

## See Also

- [[ftx]] -- Cautionary tale of custodial exchange failure
- [[defi]] -- Financial services accessible via self-custodial wallets
- [[decentralized-exchanges]] -- Trading venues for self-custodied assets
- [[blockchain]] -- The infrastructure enabling trustless ownership
- [[counterparty-risk]] -- The risk self-custody eliminates
- [[rehypothecation]] -- How exchanges reused customer funds (the FTX failure mode)

## Trading Tradeoff: Custody vs. Execution

For active traders, self-custody and execution efficiency pull in opposite directions. Centralized exchanges offer deep order books, leverage, and instant settlement but reintroduce [[counterparty-risk]] and [[rehypothecation]] exposure — the trader's balance is an IOU, not on-chain assets. The common professional pattern is to hold the long-term treasury in self-custody (hardware or multi-sig) and keep only active trading float on exchanges, sweeping profits off-venue. On-chain alternatives ([[decentralized-exchanges|DEXs]], perps DEXs) preserve self-custody during trading but trade off liquidity, speed, and smart-contract risk.

## Sources

- Nakamoto, Satoshi. "Bitcoin: A Peer-to-Peer Electronic Cash System" (2008) — basis of key-based ownership.
- Antonopoulos, Andreas M. "Mastering Bitcoin" (2nd ed., O'Reilly, 2017), chapters on keys, addresses, and wallets.
- US bankruptcy court filings, FTX (2022) and Celsius (2022) — customer-asset loss precedents driving self-custody adoption.
