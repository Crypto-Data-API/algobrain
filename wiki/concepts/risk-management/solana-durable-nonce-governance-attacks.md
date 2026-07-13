---
title: "Solana Durable-Nonce Governance Attacks"
type: concept
created: 2026-04-28
updated: 2026-06-11
status: good
tags: [crypto, defi, risk-management, governance, exploits, solana]
aliases: ["Durable Nonce Attack", "Pre-Signed Governance Tx", "Solana Nonce Abuse"]
domain: [risk-management, crypto]
difficulty: advanced
prerequisites: ["[[solana]]", "[[smart-contracts]]", "[[governance-attacks]]"]
related: ["[[governance-attacks]]", "[[2026-04-01-drift-protocol-exploit]]", "[[smart-contract-vulnerability-taxonomy]]", "[[ai-amplified-exploit-arbitrage]]", "[[2026-exploit-target-watchlist]]", "[[ai-vulnerability-discovery]]", "[[lazarus-group]]"]
---

A Solana **durable-nonce governance attack** uses Solana's durable-transaction feature to pre-sign multisig-approved transactions that can be held and submitted later, decoupled from the network's normal short-lived blockhash. Once an attacker obtains enough pre-signed approvals — typically through long-running social engineering against multisig signers — they can execute a malicious governance action atomically at the moment of their choosing, with no fresh re-validation required from the signers. The [[2026-04-01-drift-protocol-exploit|Drift Protocol exploit]] (April 1, 2026, $285-286M) is the canonical case, attributed to the [[lazarus-group|DPRK / UNC1069]] threat-actor cluster.

## What durable nonces are

Solana transactions normally include a `recent_blockhash` that expires after ~150 blocks (~60 seconds). A signed transaction whose blockhash has expired is rejected by validators. This short window protects against replay and stale-state attacks, but also forces signers to approve transactions in a tight time-window relative to execution.

**Durable nonces** decouple transaction lifetime from blockhash freshness. A signer creates a `Nonce Account` on-chain that holds a network-tracked value; transactions reference the nonce instead of a recent blockhash. The transaction can be signed at time T and submitted at T+days/weeks/months — the only constraint is that the nonce account hasn't been advanced.

The feature exists for legitimate reasons: cold-storage signing flows, pre-authorized treasury operations, batch-signed governance ceremonies. But it converts a "sign now, execute now" multisig flow into a "sign now, execute later" flow — and attackers can collect pre-signed approvals across weeks before triggering them.

## The attack pattern

1. **Long-running social engineering** against multisig signers (typically 6+ months). Tactics from the Drift case: fake Zoom meetings, AI-deepfaked executives, multi-week impersonation across Telegram / LinkedIn / Slack, malicious npm packages and GitHub repos targeting developer machines. Same TTPs as documented in [[lazarus-group]].
2. **Compromise of a sufficient quorum of signing keys** — through malware, supply-chain compromise of the signers' devices, or coercion of the humans behind the keys.
3. **Stage durable-nonce-anchored transactions** that, once executed, will: enable malicious collateral assets, modify oracle config, grant attacker-controlled multisig roles, or directly drain treasury.
4. **Execute atomically**. Because the transactions are pre-signed and durable-nonce-anchored, the attacker submits them at the moment of their choosing — typically when the protocol's defenders are off-shift and on-chain monitoring is thin.
5. **Drain funds** before defenders can pause the protocol or rotate signers. In the Drift case the full $285M drain landed before the governance team could respond.

This is a **governance-layer compromise**, not a smart-contract bug. The protocol's code worked exactly as designed; the multisig signers approved transactions that, by the time they executed, drained the protocol.

## Why durable-nonce flows magnify the risk

Without durable nonces, an attacker who compromises a signer's machine still has to push the malicious transaction through within ~60 seconds of getting the signature — a short window in which the human signer might notice, the protocol team might detect anomalous outflow, or other defenders might intervene.

Durable-nonce signing flows extend that window indefinitely:

- A signer can be deceived into signing a transaction that *looks legitimate today* (e.g., during a fake "treasury rotation ceremony" arranged by a deepfaked CFO) but only executes later.
- The attacker can wait for the most opportune moment — Saturday 4am UTC, during a market-wide volatility spike, while the security team is at a conference — to fire the pre-signed payload.
- Multiple signers can be compromised independently over months; each contributes one signature to a quorum that activates only when all signatures are collected.

The feature is doing exactly what it was designed to do; the failure mode is operational/procedural, not protocol-level.

## Drift case (April 1, 2026)

See full post-mortem at [[2026-04-01-drift-protocol-exploit]]. Summary:

- **6-month social-engineering campaign** by Lazarus / UNC1069 against Drift's Security Council members.
- Signers were deceived into producing pre-signed approvals via durable-nonce-anchored transactions during what they believed were legitimate governance ceremonies.
- On April 1, 2026, the attacker enabled a fake collateral asset and drained $285-286M atomically. Code audits had passed cleanly; the exploit did not require any vulnerability in Drift's smart contracts.
- Drift's recovery vote — pending as of late April 2026 — will set the 2026 norm for whether protocol communities socialize losses from governance-layer compromises (Cetus precedent) or leave victims uncompensated.

## Defenses

### Procedural

- **Live-call signing only for high-value transactions.** Multisig signers should refuse to sign durable-nonce transactions for any operation above a treasury threshold; durable nonces should be reserved for explicitly-low-impact, machine-readable batch operations.
- **Out-of-band confirmation.** Every signature should be confirmed via a second channel (phone call, in-person, hardware-attested) before the durable-nonce window opens.
- **Zoom/Telegram/LinkedIn deepfake awareness training** for all signers. Mandate hardware tokens, not soft-key apps, for signing operations.
- **Periodic key rotation** with mandatory in-person ceremonies; never rotate keys based solely on remote-call instructions.

### Technical

- **Timelock + cancel window** on any transaction enabling new collateral, modifying oracle config, or changing multisig roles. A 24-72h delay between submission and execution gives defenders time to pause.
- **Monitor durable-nonce account activity.** Any transaction referencing a durable-nonce account on a treasury-relevant program should trigger an alert.
- **Limit nonce-account scope.** Only allow durable-nonce transactions on a strictly-scoped subset of the program's instructions, never on collateral / oracle / role-management operations.
- **Anomaly detection on signer devices.** Hardware-attested key-generation; require signing to occur on devices verified by a separate quorum.

## Why audit coverage doesn't help

Standard smart-contract audits cover the on-chain code; they don't cover:

- Signing-flow procedures
- Multisig signer device security
- Operational security against social engineering
- Durable-nonce policies

Per the Drift case — and the broader 2026 trend documented in [[2026-exploit-target-watchlist]] — **governance-layer attacks now exceed code exploits in dollar impact**. Protocols whose marketing leans on "audited by X, Y, Z" without disclosing their signing-flow policies are signaling a false sense of security.

## Trader-side implications

For pre-positioning hedges (per [[ai-amplified-exploit-arbitrage]]), the relevant signal is **operational, not technical**:

- **Signer-rotation cadence.** Protocols that haven't rotated multisig signers in >12 months are higher-risk.
- **Public signer identities.** Doxxed signers are easier social-engineering targets but also have more reputational lock-in. Net effect ambiguous; lean cautious.
- **Durable-nonce policy disclosure.** Protocols that publicly commit to live-call signing for high-value operations are lower-risk; those that don't, or use durable nonces extensively, warrant cheap-to-carry shorts.
- **Single-chain governance dependence.** Solana-based DeFi with thin multisig signer rotation is the immediate exposed surface; analogous patterns exist on EVM (timelock-bypass, signer-compromise) but the durable-nonce primitive is Solana-specific.

## Related

- [[2026-04-01-drift-protocol-exploit]] — the canonical case
- [[governance-attacks]] — broader governance-attack class
- [[lazarus-group]] — DPRK threat actor; UNC1069 cluster
- [[smart-contract-vulnerability-taxonomy]] — vuln-class index
- [[ai-amplified-exploit-arbitrage]] — trader playbook
- [[2026-exploit-target-watchlist]] — quarterly tracker

## Sources

- Drift Protocol post-mortem (April 2026)
- Mandiant attribution analysis on UNC1069 TTPs
- Elliptic / CM Alliance reports on the Drift incident
- [[ai-amplified-exploit-arbitrage]] — Drift example trade tape
- Solana documentation, *Durable & Offline Transaction Signing using Nonces* (docs.solanalabs.com / solana.com/developers) — primitive mechanics: Nonce Account, `AdvanceNonceAccount` instruction, decoupling of transaction validity from the ~150-block recent-blockhash window

> The durable-nonce primitive (Nonce Account decoupling transaction validity from recent-blockhash freshness) is confirmed against Solana's official documentation. The Drift-specific incident details (~$285M, Lazarus/UNC1069 attribution, durable-nonce governance vector) rest on the incident post-mortem and attribution reports cited above and on [[2026-04-01-drift-protocol-exploit]]; treat the dollar figure and attribution as reported-but-evolving until the final restitution vote.
