---
title: "The DAO Hack (2016)"
type: news
created: 2026-04-14
updated: 2026-04-14
status: good
tags: [news, crypto, defi, hacks, exploits, security, ethereum, history]
event_date: 2016-06-17
markets_affected: [crypto]
impact: high
verified: true
sources_count: 0
related: ["[[reentrancy-attacks]]", "[[smart-contract-risk]]", "[[ethereum]]", "[[defi]]", "[[defi-hacks-and-exploits]]"]
---

The DAO hack was the first major smart contract exploit in crypto history. On June 17, 2016, an attacker exploited a [[reentrancy-attacks|reentrancy vulnerability]] in The DAO — a decentralized investment fund on [[ethereum|Ethereum]] that had raised $150M in ETH — draining 3.6 million ETH (~$60M at the time). The resulting hard fork to recover the funds split Ethereum into two chains: Ethereum (ETH) and Ethereum Classic (ETC), establishing the precedent that "code is law" has limits when enough money is at stake.

## What Was The DAO?

The DAO (Decentralized Autonomous Organization) launched in April 2016 as a crowdfunded investment vehicle built on Ethereum. Token holders could propose and vote on projects to fund. At its peak, The DAO held ~15% of all ETH in circulation — roughly $150M. It was the largest crowdfund in history at that time.

The DAO's smart contract was written in Solidity and deployed to Ethereum mainnet. Despite being reviewed by multiple developers, the code contained a critical reentrancy vulnerability in its `splitDAO` function — the function that allowed investors to withdraw their ETH.

## The Attack

### How Reentrancy Worked

The `splitDAO` function followed a dangerous pattern:

1. Check the caller's balance
2. Send ETH to the caller
3. Update the caller's balance to zero

The flaw: step 2 (sending ETH) triggers the recipient's fallback function *before* step 3 (updating the balance). The attacker deployed a malicious contract whose fallback function called `splitDAO` again, re-entering the function before the balance was zeroed out. Each re-entry sent another round of ETH. This loop drained funds repeatedly from a single balance check.

```
// Simplified vulnerable pattern:
function splitDAO() {
    uint balance = balances[msg.sender];
    msg.sender.call.value(balance)();  // ← attacker re-enters here
    balances[msg.sender] = 0;          // ← never reached during attack
}
```

### Timeline

| Date | Event |
|------|-------|
| 2016-04-30 | The DAO launches, raises $150M in ETH |
| 2016-06-09 | Security researchers publish warnings about reentrancy risk |
| 2016-06-17 | Attacker begins draining The DAO — 3.6M ETH ($60M) siphoned into a "child DAO" |
| 2016-06-17 | Community discovers the attack; ETH price drops from ~$20 to ~$13 (35% crash) |
| 2016-06-17 | Attacker's funds locked in a 28-day holding period (child DAO creation period), giving the community time to respond |
| 2016-07-20 | Ethereum hard fork executes at block 1,920,000 — all DAO funds returned to investors via a refund contract |
| 2016-07-20 | Miners who reject the fork continue on the original chain, now called Ethereum Classic (ETC) |

## Market Impact

- **ETH price**: Dropped ~35% on the day of the hack ($20 → $13), though it recovered within months
- **Ethereum Classic**: The fork created a permanent second chain. ETC peaked at ~$170 in 2021 but remained a fraction of ETH's value
- **Regulatory scrutiny**: The SEC's 2017 "DAO Report" concluded that DAO tokens were securities, establishing the framework that would shape ICO regulation
- **Community split**: The fork divided the Ethereum community philosophically — immutability purists vs. pragmatists willing to intervene to recover stolen funds

## Why It Matters

The DAO hack established several precedents that define DeFi security to this day:

1. **Reentrancy as a vulnerability class.** The attack pattern became the canonical smart contract exploit. Every Solidity developer learns the "checks-effects-interactions" pattern as a direct result of this hack.

2. **Audits are not optional.** The DAO code was reviewed but not formally audited. The hack accelerated the growth of the smart contract auditing industry (Trail of Bits, OpenZeppelin, etc.).

3. **Immutability is a spectrum.** The fork proved that blockchains *can* be rolled back if social consensus demands it — but at the cost of credibility and chain splits.

4. **Time locks save funds.** The 28-day child DAO creation period gave the community time to organize the fork. Modern protocols use time locks for exactly this reason.

5. **"Code is law" has limits.** The philosophical debate between "the attacker followed the code's rules" vs. "the attacker clearly stole funds" remains unresolved and resurfaces with every major exploit.

## Trading Lessons

- The 28-day lock created a known resolution timeline — traders who understood the fork mechanics could position accordingly
- The ETH/ETC fork created a brief arbitrage window as markets priced the two chains — see [[2016-07-ethereum-dao-fork-arbitrage]] for the full triangulation playbook (Poloniex first-listing, Coinbase credit lag, [[replay-attack]] window before EIP-155, ETC philosophy-premium pair trades)
- The hack demonstrated that protocol-level risk can dwarf market risk — a 35% crash from a single contract bug

## Related

- [[reentrancy-attacks]] — the attack vector used in The DAO hack
- [[smart-contract-risk]] — DAO hack is the canonical example of smart contract risk
- [[ethereum]] — the chain that forked to recover funds
- [[defi-hacks-and-exploits]] — master timeline of DeFi exploits
- [[flash-loan-attacks]] — a later evolution of DeFi attack techniques
- [[governance-attacks]] — The DAO itself was an early governance experiment

## Sources

_Content based on public blockchain records, the SEC's 2017 DAO Report, and widely documented community accounts. No raw sources ingested._
