---
title: "Governance Attacks"
type: concept
created: 2026-04-14
updated: 2026-04-14
status: good
tags: [crypto, defi, risk-management, security, governance, exploits]
aliases: ["governance attack", "governance exploit", "DAO attack", "vote manipulation"]
domain: [risk-management, crypto]
difficulty: intermediate
prerequisites: ["[[smart-contracts]]", "[[defi]]"]
related: ["[[smart-contract-risk]]", "[[flash-loan-attacks]]", "[[2022-04-beanstalk-governance-attack]]", "[[ai-governance-attacks]]", "[[defi-hacks-and-exploits]]", "[[smart-contract-vulnerability-taxonomy]]", "[[ai-vulnerability-discovery]]", "[[ai-amplified-exploit-arbitrage]]", "[[governance-restitution-arbitrage]]"]
---

A governance attack exploits on-chain governance mechanisms to pass malicious proposals that drain treasury funds, modify protocol parameters to favor the attacker, or grant the attacker control over the protocol. DeFi governance systems — which allow token holders to propose and vote on protocol changes — are powerful tools for decentralization but also introduce an attack surface where voting power is capital, and capital can be borrowed. The [[2022-04-beanstalk-governance-attack|Beanstalk attack]] ($182M, 2022) demonstrated the catastrophic potential when governance lacks basic safeguards.

## How Governance Attacks Work

### Prerequisites

Most DeFi governance systems share these components:
- **Governance tokens** that grant voting power proportional to holdings
- **Proposal submission** requiring a minimum token threshold
- **Voting period** where token holders cast votes
- **Execution** when a proposal reaches quorum and passes

An attacker can exploit any of these stages.

## Attack Vectors

### 1. Flash Loan Governance (Capital Attack)

The most dramatic form — use [[flash-loan-attacks|flash loans]] to temporarily acquire voting power:

1. Flash-borrow enough governance tokens to exceed the quorum threshold
2. Vote to pass a malicious proposal
3. If the proposal executes immediately (no time lock), drain the treasury
4. Repay the flash loan

**Prerequisite**: Governance must use *current* token balances (not snapshot-based) and must not have a time lock between passage and execution.

**Example**: [[2022-04-beanstalk-governance-attack|Beanstalk]] ($182M) — the attacker flash-borrowed Stalk tokens, voted, and executed the drain in a single transaction.

### 2. Vote Buying / Bribery

Accumulate voting power without buying tokens by paying existing holders to delegate or vote in the attacker's favor:

- **Direct bribes** via platforms like Votium, Paladin, or Hidden Hand (legitimized for incentive alignment, but the same mechanism enables malicious coordination)
- **Dark pools** — private arrangements with large token holders
- **Vote markets** — protocols that let users sell their voting rights

The cost of renting voting power is far less than buying and holding the tokens.

### 3. Slow Accumulation (Hostile Takeover)

Gradually accumulate governance tokens on the open market until reaching a controlling position, then push through proposals that benefit the acquirer:

- Modify fee structures to redirect revenue
- Change treasury allocation
- Appoint favorable multi-sig signers

This is analogous to a hostile corporate takeover and is generally legal (the attacker is using the system as designed). However, it can harm minority token holders.

### 4. Proposal Poisoning

Submit legitimate-looking proposals with hidden malicious code:

- A proposal titled "Increase liquidity mining rewards" might include a function that also transfers treasury funds
- Complex Solidity code is hard for community members to review
- If the community votes based on the proposal *description* rather than the *code*, malicious payloads can slip through

[[2022-04-beanstalk-governance-attack|BIP-18]] at Beanstalk included a fake "Ukraine donation" alongside the treasury drain function.

### 5. Quorum Exploitation

Some protocols have low quorum thresholds — e.g., a proposal passes if 4% of tokens vote in favor with no opposition. On a quiet governance day, an attacker with a relatively small holding can pass proposals that would fail if more voters participated.

### 6. Delegate Manipulation

Governance delegation allows users to assign their voting power to others. An attacker who compromises or socially engineers prominent delegates can control disproportionate voting power without owning the tokens.

See [[ai-governance-attacks]] for how LLMs and AI agents introduce new governance manipulation vectors.

## Historical Governance Attacks

| Date | Protocol | Amount/Impact | Method |
|------|----------|---------------|--------|
| 2022-04 | [[2022-04-beanstalk-governance-attack|Beanstalk]] | $182M drained | Flash loan + immediate execution |
| 2022-05 | Build Finance DAO | $470K drained | Attacker acquired majority tokens, passed treasury drain proposal |
| 2023-02 | Tornado Cash governance | Attacker took control | Proposal included hidden code that granted attacker 1.2M fake TORN votes |
| 2023-05 | Aragon | DAO threatened | Activist investors attempted hostile governance takeover to liquidate treasury |
| 2024 | Various small DAOs | Ongoing | Low-quorum exploits and proposal poisoning |

## Defenses

### Snapshot-Based Voting
Lock voting power at the time of proposal creation. Tokens acquired after the snapshot (including via flash loans) have zero voting power. This is the single most effective defense against flash loan governance attacks.

### Time Locks
Require a mandatory delay (24-72 hours) between proposal passage and execution. This gives the community time to:
- Review the proposal code
- Organize a counter-vote or emergency pause
- Exit the protocol if the proposal is genuinely malicious

### Optimistic Governance
Proposals execute *unless* vetoed by a guardian multi-sig or community vote within the time lock period. This reduces governance overhead while maintaining a safety valve.

### Proposal Review Periods
Require proposals to be posted for review (e.g., 7 days) before voting begins. Community members, security researchers, and automated tools can analyze the code.

### Delegation with Safeguards
- Delegate revocation with short notice
- Maximum delegation caps
- Transparency dashboards showing delegation concentration

### Quorum Minimums
Set quorum thresholds high enough that a small attacker cannot pass proposals in low-participation periods. Dynamic quorum (adjusting based on recent participation rates) can prevent exploitation during quiet periods.

## Related

- [[2022-04-beanstalk-governance-attack]] — the canonical flash loan governance attack ($182M)
- [[flash-loan-attacks]] — flash loans enable capital-based governance attacks
- [[ai-governance-attacks]] — AI-specific governance manipulation vectors
- [[smart-contract-risk]] — governance as an attack surface
- [[defi-hacks-and-exploits]] — master timeline

## Sources

_Content based on on-chain governance analyses, Beanstalk post-mortem, Tornado Cash governance incident, and governance framework documentation from Compound, Aave, and OpenZeppelin. No raw sources ingested._
