---
title: "Beanstalk Governance Attack (2022)"
type: news
created: 2026-04-14
updated: 2026-04-14
status: good
tags: [news, crypto, defi, hacks, exploits, security, governance, flash-loans, stablecoins, history]
event_date: 2022-04-17
markets_affected: [crypto]
impact: high
verified: true
sources_count: 0
related: ["[[governance-attacks]]", "[[flash-loan-attacks]]", "[[smart-contract-risk]]", "[[defi]]", "[[defi-hacks-and-exploits]]"]
---

On April 17, 2022, an attacker used a [[flash-loan-attacks|flash loan]] to temporarily acquire enough governance tokens to pass a malicious proposal on Beanstalk — an algorithmic stablecoin protocol — draining $182M from the protocol's treasury. The Beanstalk attack was the most expensive [[governance-attacks|governance attack]] in DeFi history and demonstrated that on-chain governance without time locks or snapshot-based voting is fundamentally vulnerable to capital-based manipulation.

## How the Attack Worked

### Beanstalk's Governance Design

Beanstalk used a simple on-chain governance model:
- Proposals could be submitted by anyone
- Voting power was proportional to Stalk tokens (earned by depositing in the Silo)
- Proposals required a supermajority (⅔) to pass
- **Crucially**: voting was not snapshot-based — it used *current* token balances, and proposals could be executed immediately upon reaching quorum with no time lock

### The Attack Sequence

The attacker executed the entire exploit in a single Ethereum transaction:

1. **Flash-borrowed** ~$1B from Aave, Uniswap V2, and SushiSwap
2. **Deposited** borrowed funds into Beanstalk's Silo, instantly receiving Stalk governance tokens
3. **Voted** to approve BIP-18 — a malicious "governance proposal" the attacker had submitted earlier
   - BIP-18 contained two components: a fake $250K "donation" to Ukraine (for optics) and a function that would transfer all Beanstalk funds to the attacker's wallet
4. **BIP-18 passed** — the attacker's flash-borrowed Stalk gave them >⅔ voting power
5. **Executed** BIP-18 immediately, draining $182M in various tokens (BEAN, ETH, USDC, LUSD)
6. **Withdrew** from the Silo, repaid all flash loans
7. **Net profit**: ~$80M (after flash loan fees and converting drained tokens)

The attacker donated $250K to the Ukraine Crypto Donation address — the only portion of BIP-18 that was "legitimate."

### Why It Worked

| Design Flaw | How It Was Exploited |
|-------------|---------------------|
| No snapshot voting | Attacker used *current* (flash-borrowed) balances to vote |
| No time lock | Proposal was executed in the same transaction it passed |
| No quorum delay | No minimum time between quorum reached and execution |
| Proposal code not reviewed | BIP-18's malicious `transferFrom` was embedded in complex Solidity |

## The Attacker

The attacker's wallet was funded through [[tornado-cash|Tornado Cash]], making initial tracing difficult. The attacker has never been identified. The on-chain message left was simply the Ukraine donation transaction.

## Aftermath

- **BEAN** stablecoin depegged instantly from $1.00 to ~$0.24
- Beanstalk's TVL dropped from ~$180M to effectively zero
- The protocol paused all operations
- Beanstalk eventually relaunched ("Beanstalk Replanted") with redesigned governance:
  - **Snapshot-based voting** (balances locked at proposal creation time)
  - **7-day time lock** on all governance proposals
  - **Emergency governance** only through a multi-sig with time delay
  - **Code review period** before execution

## Trading Lessons

1. **Governance tokens are attack vectors.** Any governance system where voting power can be temporarily acquired (via flash loans or large borrows) and used to execute proposals immediately is a ticking time bomb.
2. **Time locks are non-negotiable.** A 24-48 hour time lock between proposal passage and execution gives the community time to detect and respond to malicious proposals. Beanstalk had none.
3. **Snapshot voting prevents flash loan governance.** If voting power is based on token balances at the time of proposal *creation* (not execution), flash loans cannot be used to vote.
4. **Read the proposal code.** BIP-18's malicious transfer was visible in the Solidity code for days before the attack. The community did not review it carefully because the surface-level description mentioned a Ukraine donation.

## Related

- [[governance-attacks]] — Beanstalk is the canonical flash-loan governance attack
- [[flash-loan-attacks]] — flash loans provided the capital for the attack
- [[smart-contract-risk]] — governance as an attack surface
- [[defi-hacks-and-exploits]] — master timeline of DeFi exploits

## Sources

_Content based on on-chain transaction analysis, BlockSec/PeckShield reports, and Beanstalk's post-mortem. No raw sources ingested._
