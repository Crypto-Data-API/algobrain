---
title: "Exchange API Key Security"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [ai-trading, trading-bots, risk-management, exchange, deployment, crypto]
aliases: ["API Key Security", "API Key Management", "Key Scoping", "Withdrawal-Disabled Keys"]
domain: [risk-management, market-microstructure]
prerequisites: ["[[bot-architecture]]", "[[broker-api]]"]
difficulty: intermediate
related:
  - "[[bot-architecture]]"
  - "[[bot-risks-and-pitfalls]]"
  - "[[position-reconciliation]]"
  - "[[deployment]]"
  - "[[broker-api]]"
  - "[[exchange-api-reference]]"
  - "[[proof-of-reserves]]"
  - "[[binance]]"
---

# Exchange API Key Security

Exchange API key security is the practice of provisioning, scoping, storing, and rotating the credentials a bot uses to trade on a centralized exchange so that a leaked or compromised key causes **bounded, recoverable damage** instead of a drained account. It is pure downside protection: a key grants a program the ability to move real money, and the entire discipline is about ensuring that ability is exactly as large as the strategy needs and no larger. The recurring lesson from crypto history — leaked keys drained within minutes by automated scanners, and the **3Commas breach (2022–2023)** in which tens of thousands of exchange API keys were exposed and used to force loss-making trades that pumped illiquid pairs — is that keys are attacked constantly and the only reliable defense is to make a stolen key nearly worthless.

> Key security is the precondition for [[position-reconciliation]] (an unexplained diff can be the first sign of a compromised key) and a component of the [[bot-kill-switch-design|kill switch]] (key-compromise is a global-flatten trigger).

## Permission scoping: least privilege

Every exchange key carries a permission set. Grant the **minimum** required and nothing else:

| Permission | Grant when | Danger if leaked |
|---|---|---|
| **Read / view** | Always fine — needed for [[position-reconciliation]], balances, fills | Information leak only (positions visible); no fund movement |
| **Spot & margin trade** | The bot places spot/margin orders | Attacker can trade your account — **wash/pump-and-dump** your balance into illiquid pairs (the 3Commas attack pattern), but cannot withdraw |
| **Futures / derivatives trade** | The bot trades perps/futures | Attacker can open leveraged losing positions; margin blow-up risk |
| **Withdrawal / transfer** | **Almost never for a bot** | Attacker drains funds directly to their own address — total loss |
| **Enable internal transfer / universal transfer** | Only if the strategy genuinely moves funds between sub-accounts | Attacker shuffles funds toward a withdrawal-enabled surface |

**The single most important rule: disable withdrawal permission on trading keys.** A bot virtually never needs to withdraw. With withdrawal disabled, the worst a stolen key can do is *trade* your account — bad, but survivable and detectable — rather than *empty* it. Almost every catastrophic-total-loss API incident traces to a key that had withdrawal enabled when it did not need to.

## IP allowlisting

Bind each key to the fixed IP address(es) it will actually call from (your VPS/cloud egress IP):

- A stolen key is useless from any other IP — the exchange rejects the request. This single control neutralizes most opportunistic key theft (leaked-in-logs, committed-to-git, phishing dumps).
- On **Binance**, an IP-restricted (allowlisted) key does not expire, while an unrestricted key expires after 90 days — the platform actively pushes you toward allowlisting.
- Requires a **static egress IP** (elastic IP / NAT gateway); design the infrastructure for it. If the bot must run from a dynamic IP, that is a signal to add a static-IP proxy rather than to skip the allowlist.

## Withdrawal-address allowlisting (defense in depth)

If a key *must* have withdrawal (rare — e.g., an automated treasury sweep), pair it with an **exchange-side withdrawal address allowlist** so funds can only ever go to pre-registered addresses you control, typically with a time-locked cooldown when a new address is added. This converts "drain to attacker" into "move to my own cold wallet," which is not a loss.

## Sub-accounts: blast-radius isolation

Use exchange **sub-accounts** to compartmentalize:

- **One sub-account (and key) per strategy or per risk domain**, so a compromised or malfunctioning key affects only that sub-account's capital, not the whole book.
- Keep the **bulk of capital in a funding/master account** with **no active API keys**, sweeping only the working capital each strategy needs into its sub-account.
- Sub-accounts also cleanly separate P&L and [[position-reconciliation|reconciliation]] per strategy and prevent one bot's manual/automated activity from polluting another's state.

The principle mirrors network segmentation: assume any single key *will* eventually leak, and design so that event is contained rather than fatal.

## Secrets storage

Where the key material lives is as important as how it is scoped:

| Approach | Security | Use for |
|---|---|---|
| **Hard-coded in source / committed to git** | Catastrophic — scanners find public-repo keys in minutes | **Never** |
| **Plaintext config / logs** | Poor — keys leak via backups, log aggregation, screenshots | Never; scrub keys from logs |
| **Environment variables** | Baseline acceptable for a single VPS | Small setups; still exposed to anything that can read the process env |
| **Secrets manager** (AWS Secrets Manager, GCP Secret Manager, HashiCorp Vault) | Good — encrypted at rest, access-controlled, audit-logged, rotatable | Production bots |
| **KMS / HSM-backed signing** | Best — the private key never leaves the hardware boundary; the bot asks the HSM to *sign* requests rather than holding the secret | High-value operations; venues supporting asymmetric keys |

**Asymmetric API keys change the storage problem.** Binance and others now support **Ed25519 (and RSA) API keys**: the exchange stores your *public* key, and the bot signs each request with a private key that can live inside an **HSM/KMS** and never be transmitted or stored in plaintext. Unlike an HMAC secret (which both sides hold and which is exposed the moment either side leaks), an asymmetric private key can be kept in hardware — strongly preferred for meaningful capital.

Operational hygiene regardless of backend: never log full keys; scrub them from error reports and crash dumps; keep them out of shell history and environment dumps; and treat any third-party platform you paste keys into (the 3Commas lesson) as a full trust delegation of everything those keys can do.

## Key rotation and revocation drills

Keys are not set-and-forget:

- **Rotate on a schedule** (e.g., quarterly) and **immediately** on any suspected exposure, staff change, or third-party incident. Support **overlapping validity** (issue new, cut over, revoke old) so rotation causes no downtime.
- **Practice revocation** — a *revocation drill* rehearses the emergency response *before* you need it: revoke a key, confirm the bot fails safe (halts, does not trade blind), issue a replacement, and restore service. A revocation path first exercised during a live breach is one you are debugging mid-incident (same lesson as the [[bot-kill-switch-design|kill-switch drill]]).
- **Inventory every key**: which key, which sub-account, which permissions, which IP, which host, last rotated. You cannot secure keys you have lost track of.
- **Alert on key-level anomalies**: a request from an unexpected IP, a permission you did not grant appearing, or an [[position-reconciliation|unexplained position change]] should trigger revocation and a global flatten.

## Provisioning checklist

```
[ ] Withdrawal permission DISABLED (unless a specific, justified need)
[ ] Only the trade scopes actually used (spot/margin/futures) enabled; nothing extra
[ ] IP allowlist set to the bot's static egress IP(s)
[ ] Withdrawal-address allowlist configured IF withdrawal is unavoidable
[ ] Key issued to a dedicated sub-account, not the master/funding account
[ ] Bulk capital held in a keyless funding account; only working capital swept in
[ ] Secret stored in a secrets manager or HSM/KMS — never in code, config, or logs
[ ] Asymmetric (Ed25519) key with HSM-held private key for material capital
[ ] Rotation schedule set; revocation drill rehearsed and documented
[ ] Key inventoried; anomaly alerting wired to revocation + kill switch
```

## Relationship to counterparty risk

Key security protects *your access*; it does not protect *the exchange's solvency*. Even a perfectly-scoped, withdrawal-disabled, IP-locked key is worthless if the venue itself fails (see [[ftx]]) — the funds it protects are still custodied by the exchange. Key hygiene and **counterparty monitoring** (see [[proof-of-reserves]]) are complementary layers: the first bounds loss from *your* compromise, the second bounds loss from *the venue's*.

## Related

- [[bot-architecture]] — where key handling sits in the system
- [[bot-risks-and-pitfalls]] — "key management" and "the leaked key" failures this closes
- [[position-reconciliation]] — unexplained state changes as a compromise signal
- [[bot-kill-switch-design]] — key-compromise as a global-flatten trigger
- [[deployment]] — static-IP and secrets infrastructure
- [[broker-api]] / [[exchange-api-reference]] — the API surface keys authenticate to
- [[proof-of-reserves]] — the counterparty-solvency layer key security does not cover
- [[binance]] — reference venue for IP-restriction expiry rules and Ed25519 keys

## Sources

- 3Commas API key breach (2022–2023) — mass exposure of exchange API keys used to force loss-making trades; canonical case for withdrawal-disabled, IP-allowlisted keys.
- Binance API key documentation — IP-restriction / 90-day expiry behavior and Ed25519 asymmetric key support (public docs).
- General knowledge of production secrets-management and exchange-security practice; synthesized with this wiki's [[bot-risks-and-pitfalls]] page. No raw external source ingested yet.
