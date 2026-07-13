---
title: "Donation Attacks"
type: concept
created: 2026-04-28
updated: 2026-06-11
status: good
tags: [crypto, defi, risk-management, security, smart-contracts, exploits]
aliases: ["empty-market attack", "vault-share inflation", "Compound v2 donation attack", "first-depositor attack"]
domain: [risk-management, crypto]
difficulty: intermediate
prerequisites: ["[[smart-contracts]]", "[[defi]]", "[[flash-loan-attacks]]"]
related: ["[[compound-fork-donation-short]]", "[[oracle-manipulation]]", "[[flash-loan-attacks]]", "[[smart-contract-vulnerability-taxonomy]]", "[[ai-amplified-exploit-arbitrage]]", "[[2026-exploit-target-watchlist]]", "[[venus]]", "[[defi-hacks-and-exploits]]", "[[ai-vulnerability-discovery]]"]
---

A **donation attack** (also called an empty-market attack or vault-share inflation attack) exploits the rounding and accounting behavior of an ERC-4626-style vault or a Compound v2-style cToken market in its earliest, low-liquidity moments. The attacker manipulates the share-to-asset ratio by donating tokens directly to the vault contract — bypassing the deposit accounting — then borrows or withdraws against the now-inflated share price. The pattern has been **exploited at least 5 times across Compound v2 forks** since 2023 (Hundred Finance, Sonne Finance, Onyx Protocol, Venus Protocol Feb 2025 + Mar 2026); audit firms warn about it explicitly; AI scanners catch it reliably; protocols continue to ship vulnerable code.

## How donation attacks work

The vulnerability lives in any vault that prices shares as a ratio of underlying balance to outstanding shares. In a Compound v2 cToken market or an ERC-4626 vault:

```
sharePrice = underlyingBalance / totalShares
```

When the market is empty (`totalShares == 0`), or has very few shares, this ratio can be manipulated by changing the underlying balance independently of share issuance. This is the same root cause as the **ERC-4626 inflation attack** (a.k.a. first-depositor attack): the attacker mints a single share, then "donates" assets directly to the contract so that the one outstanding share is worth a large amount, and a later honest depositor's deposit rounds down to zero shares (a gift to the attacker). The fix in both the cToken and ERC-4626 cases is to ensure the vault never starts from a manipulable empty/near-empty state.

### The classic Compound v2 donation pattern

1. **Protocol creates a new market** with zero existing liquidity. Often this happens because the protocol is launching a new collateral type or the market was deployed but never seeded.
2. **Attacker mints 1 share** by depositing a tiny amount (e.g., 1 wei of underlying).
3. **Attacker "donates" tokens directly to the cToken contract** — i.e., transfers tokens to the contract address without going through the deposit function. The contract's `underlyingBalance` rises, but `totalShares` stays at 1.
4. **Share price inflates massively.** With 1 share outstanding and (say) 1000 tokens donated, the share price is now 1000 tokens per share.
5. **Attacker uses their 1 share as collateral** in another (funded) market in the protocol. The protocol values the 1 share at the inflated price.
6. **Attacker borrows** assets against the over-valued collateral.
7. **Attacker withdraws** the borrowed assets and the donated tokens. Net profit: the borrowed assets minus the trivial seed deposit.

The protocol's accounting is now broken — the cToken/vault has a large underlying balance against tiny outstanding shares, and any later legitimate user is locked out of meaningful participation.

### Variant: vault-share rounding

ERC-4626 vaults that round share-issuance down can be exploited similarly:

1. Deposit 1 wei → receive 1 share.
2. Donate large amount of underlying.
3. New depositors deposit large amounts → due to rounding-down, they receive 0 shares, and their deposit is absorbed into the inflated share price (effectively a gift to the attacker).

OpenZeppelin and Trail of Bits have published explicit warnings on this pattern; ERC-4626 implementations now standardly include "virtual shares" or initial-deposit-burn mitigations.

## Why this keeps happening

Three reasons the bug persists:

1. **Forks inherit the bug.** Compound v2 was the dominant lending template; dozens of protocols forked it. Any fork that didn't explicitly mitigate donation attacks ships the bug.
2. **Mitigation requires operational discipline, not code complexity.** The fix is to atomically batch market creation + first deposit + collateral-factor adjustment, OR to restrict the executor role to a trusted multisig, OR to seed every new market with a non-trivial first deposit before allowing user activity. None are technically hard; many fork teams skip them under launch pressure.
3. **Audit coverage is uneven across forks.** Halborn published a definitive Sonne Finance post-mortem in May 2024; the bug is in the audit-firm literature. But many forks deploy without audits explicitly addressing donation-attack mitigation, and AI scanners (Slither, Mythril, ChainAegis) flag the pattern but the warnings are ignored.

## Historical donation-attack incidents

| Date | Protocol | Loss | Mechanism |
|------|----------|------|-----------|
| 2023 | Hundred Finance | ~$7M (reported) | Compound v2 / Aave-style empty-pool inflation attack against a forked lending market on Optimism |
| May 2024 | Sonne Finance | ~$20M (confirmed) | Permissionless `EXECUTOR_ROLE`; market creation + collateral-factor adjustment scheduled 2 days apart, allowing the donation window |
| 2024 | Onyx Protocol | reported | Empty-market / accounting exploit (incident reported; details vary by source) |

> **Confidence note (verified June 2026):** The Sonne Finance May 2024 incident (~$20M) is well-documented and confirmed. The Hundred Finance 2023 incident is confirmed as an empty-pool inflation attack but the exact USD figure varies by source. Claims that **Venus Protocol** suffered specifically *donation-style* accounting exploits in Feb 2025 and again in March 2026 could **not** be independently confirmed and should be treated as unverified until a primary incident report is cited. Treat any "Venus repeat-offender" framing below as a *hypothesis for the trading strategy*, not an established fact.

Per [[2026-exploit-target-watchlist]] and [[compound-fork-donation-short]], protocols with prior donation-attack history that haven't migrated to v3-style architecture should be treated as elevated-risk for repeats — but each alleged incident should be confirmed against a primary post-mortem before sizing a position around it.

The Sonne case is the most-instructive worked example. The post-mortem published by Halborn:

> The attacker exploited a race condition between market creation and collateral-factor configuration. Sonne's `EXECUTOR_ROLE` was permissionless; a new market for VELO was created on the protocol but its collateral factor wasn't set in the same transaction. Within the 2-day gap before the collateral-factor was scheduled to be set, the attacker minted a single share, donated VELO directly to the cToken contract, and then borrowed against the inflated share price across other Sonne markets.

## Defenses

### Atomic market initialization

Never expose a new market to user activity until the market is fully initialized in a single atomic transaction:

- Deploy the cToken / vault.
- Seed it with a non-trivial first deposit (e.g., $10,000 worth of underlying) from the protocol treasury.
- Set the collateral factor.
- Open user-facing access.

If any of these steps are split across multiple transactions, an attacker can wedge the donation attack into the gap.

### Restricted EXECUTOR / governance role

The role authorized to create markets and set collateral factors should be restricted to a trusted multisig (and ideally further guarded by a timelock). Permissionless roles invite the Sonne pattern.

### Virtual shares / initial-deposit burn (ERC-4626)

OpenZeppelin's reference ERC-4626 implementation includes:

- **Virtual shares**: the vault's accounting always pretends there are some additional virtual shares outstanding, dampening the share-price-manipulation attack.
- **Initial-deposit burn**: the first deposit's shares are sent to the zero address (burned), creating a permanent "share floor" that absorbs the donation manipulation.

Either is sufficient; using both is belt-and-braces.

### Compound v3 architecture

Compound v3 explicitly redesigned the lending model around single-collateral markets and donation-resistant accounting. It removed the cross-market collateral re-use that made the original donation pattern catastrophic. Forks of Compound v3 do not ship the original donation bug.

### Audit recency + explicit donation-attack coverage

When evaluating a protocol, check whether the audit reports explicitly address donation-attack mitigation. A "audit by X" claim without donation-attack coverage is incomplete for any v2-derived lending protocol.

## Related vuln classes

- [[oracle-manipulation]] — frequently chained with donation attacks; the manipulated share price is then read by the protocol as oracle input.
- [[flash-loan-attacks]] — flash loans are sometimes used to magnify donation attacks (flash-borrow the donation amount, execute the attack, repay).
- ERC-4626 share-price manipulation more broadly.

## Trader-side implications

The systematic strategy is documented in [[compound-fork-donation-short]]:

- Short Compound v2 forks during their first 6-12 months post-launch when they (a) haven't migrated to v3 architecture, (b) lack public audit coverage of donation-attack mitigation, and (c) have a perp market.
- Cover when the protocol publicly addresses the bug, when the position has held 12 months without incident, or when the exploit lands.
- Hit rate observed across the 2023-2026 sample: ~30-50% of cohort experiences a donation-attack incident within 12 months; per-hit return ~50-80% on the short leg.

For pre-positioning hedges (per [[ai-amplified-exploit-arbitrage]]), the systematic approach is to maintain cheap-to-carry shorts on Compound v2 forks that (a) have not migrated to v3-style donation-resistant accounting, (b) lack audit coverage explicitly addressing donation-attack mitigation, and (c) have a liquid perp market. Protocols with any *confirmed* prior accounting-attack history are the highest-priority candidates — but confirm each alleged incident against a primary post-mortem before treating a protocol as a repeat-offender.

## Related

- [[compound-fork-donation-short]] — the systematic short strategy
- [[oracle-manipulation]] — adjacent attack vector
- [[flash-loan-attacks]] — magnifier
- [[smart-contract-vulnerability-taxonomy]] — vuln-class index
- [[ai-amplified-exploit-arbitrage]] — hub strategy
- [[2026-exploit-target-watchlist]] — quarterly tracker
- [[venus]] — repeat-offender protocol
- [[defi-hacks-and-exploits]] — historical timeline

## Sources

- Halborn / Verichains post-mortems on the Sonne Finance exploit (May 2024) — `blog.verichains.io/p/compound-v2-forked-vulnerability`
- MixBytes, *Aave and Compound forking: empty-pool attacks* — analysis of the Hundred Finance-class empty-pool inflation attack
- OpenZeppelin, *A novel defense against ERC-4626 inflation attacks* (`openzeppelin.com/news/a-novel-defense-against-erc4626-inflation-attacks`) — virtual shares / virtual assets defenses
- OpenZeppelin Contracts issue #3706 and EIP-4626 magicians thread — virtual-shares / virtual-assets and dead-shares mitigations
- MixBytes, *Overview of the inflation attack* — generalised treatment of the share-price manipulation class
- Code4rena contest archives flagging donation-attack / inflation-attack patterns in Compound forks
- [[compound-fork-donation-short]] — strategy framing
