---
title: "Flash Loan Attacks"
type: concept
created: 2026-04-14
updated: 2026-04-14
status: good
tags: [crypto, defi, risk-management, security, smart-contracts, exploits, flash-loans]
aliases: ["flash loan attack", "flash loan exploit"]
domain: [risk-management, crypto]
difficulty: intermediate
prerequisites: ["[[smart-contracts]]", "[[defi]]"]
related: ["[[smart-contract-risk]]", "[[oracle-manipulation]]", "[[flash-loan-arbitrage]]", "[[2020-02-bzx-flash-loan-attacks]]", "[[2022-04-beanstalk-governance-attack]]", "[[2021-10-cream-finance-exploits]]", "[[defi-hacks-and-exploits]]", "[[smart-contract-vulnerability-taxonomy]]", "[[ai-vulnerability-discovery]]", "[[ai-amplified-exploit-arbitrage]]"]
---

A flash loan attack uses uncollateralized flash loans — loans that must be borrowed and repaid within a single blockchain transaction — to temporarily command massive capital for exploiting DeFi protocols. The attacker borrows millions (or billions) of dollars, manipulates on-chain state (prices, governance votes, collateral ratios), extracts profit, and repays the loan, all atomically. If any step fails, the entire transaction reverts and the attacker loses only gas fees. Flash loan attacks democratized DeFi exploitation: prior to their invention, similar attacks required millions in upfront capital. After [[2020-02-bzx-flash-loan-attacks|bZx]] (February 2020), anyone with knowledge of a vulnerability could exploit it regardless of their personal wealth.

## How Flash Loans Work

Flash loans are offered by protocols like Aave, dYdX, Uniswap, and Balancer. The mechanics:

1. **Borrow**: The protocol transfers tokens to the borrower's contract
2. **Use**: The borrower's contract executes arbitrary logic (trades, deposits, governance votes, etc.)
3. **Repay**: The borrower returns the original amount + a small fee (typically 0.09%)
4. **Atomicity**: If the repayment doesn't happen by the end of the transaction, the entire transaction reverts — as if it never happened

The key insight: within a single transaction, the borrower has access to virtually unlimited capital with zero risk (the loan either completes or reverts entirely). Flash loan pools on Aave hold billions of dollars available for borrowing.

## Attack Categories

### 1. Price Manipulation (Most Common)

Use flash-borrowed capital to move prices on thin-liquidity DEX pools, then exploit protocols that rely on those prices. See [[oracle-manipulation]] for full details.

**Flow**: Borrow → Swap to move price → Exploit protocol reading that price → Repay

**Examples**: [[2020-02-bzx-flash-loan-attacks|bZx]] ($1M), Harvest Finance ($34M), [[2021-10-cream-finance-exploits|Cream Finance]] ($37.5M + $130M)

### 2. Governance Manipulation

Use flash-borrowed governance tokens to pass malicious proposals.

**Flow**: Borrow governance tokens → Vote on malicious proposal → Proposal executes → Treasury drained → Repay

**Example**: [[2022-04-beanstalk-governance-attack|Beanstalk]] ($182M) — attacker flash-borrowed enough Stalk tokens to pass BIP-18, which transferred all protocol funds to the attacker

### 3. Liquidation Manipulation

Use flash-borrowed capital to create artificial liquidation conditions or front-run liquidations.

**Flow**: Borrow → Deposit large amount to change collateral ratios or pool prices → Trigger liquidations at favorable rates → Profit from liquidation bonuses → Repay

### 4. Collateral Inflation / Deflation

Use flash-borrowed capital to temporarily inflate (or deflate) the value of collateral in a lending protocol.

**Flow**: Borrow → Deposit into vault to change share price → Borrow against inflated vault tokens elsewhere → Withdraw → Repay

### 5. Arbitrage (Legitimate Use)

Flash loans also enable legitimate [[flash-loan-arbitrage]] — executing risk-free arbitrage across DEXs without capital requirements. This is not an "attack" but uses the same underlying mechanism.

## Historical Losses from Flash Loan Attacks

| Date | Protocol | Amount | Attack Type |
|------|----------|--------|-------------|
| 2020-02 | [[2020-02-bzx-flash-loan-attacks|bZx]] | $1M | Price manipulation |
| 2020-10 | Harvest Finance | $34M | Price manipulation |
| 2020-11 | Value DeFi | $7M | Price manipulation |
| 2021-02 | [[2021-10-cream-finance-exploits|Cream Finance]] | $37.5M | Price manipulation |
| 2021-05 | PancakeBunny | $45M | Price manipulation |
| 2021-10 | [[2021-10-cream-finance-exploits|Cream Finance]] | $130M | Collateral inflation |
| 2022-04 | [[2022-04-beanstalk-governance-attack|Beanstalk]] | $182M | Governance manipulation |
| 2023-03 | [[2023-03-euler-finance-exploit|Euler Finance]] | $197M | Collateral/donation bug |
| | **Cumulative** | **$700M+** | |

## Defenses

### Against Price Manipulation
- Use [[chainlink]] or other decentralized oracle networks instead of spot DEX prices
- Use TWAP oracles with sufficient time windows
- See [[oracle-manipulation]] for detailed defenses

### Against Governance Manipulation
- **Snapshot-based voting**: Determine voting power at the time of proposal creation, not execution — flash-borrowed tokens acquired after the snapshot have zero voting power
- **Time locks**: Require a delay (24-72 hours) between proposal passage and execution, giving the community time to detect and respond
- **Proposal thresholds**: Require a minimum amount of tokens to be held for a minimum duration before submitting proposals

### Against Collateral Manipulation
- Don't accept yield vault tokens or LP tokens as collateral without adjusting their valuation for manipulation risk
- Use time-delayed pricing for exotic collateral
- Cap the maximum borrowing against any single collateral type

### Protocol-Level
- **Reentrancy guards** prevent flash-loan-enabled recursive calls
- **Single-block price limits** cap how much a price can move within one block
- **Withdrawal delays** for large borrows prevent instant extraction of flash-loan-enabled profits

## Why Flash Loan Attacks Continue

1. **Zero risk for the attacker**: A failed exploit costs only gas (~$10-100). A successful one can yield millions.
2. **Composability**: Flash loans enable chaining multiple protocols in a single transaction, creating attack surfaces that no single audit covers
3. **New protocols launch constantly**: Each new lending protocol, DEX, or vault is a potential target if its oracle or collateral design is weak
4. **Flash loan capital keeps growing**: Aave alone has $10B+ available for flash loans — more capital means more manipulation power

## Flash Loans vs. Flash Loan Attacks

Flash loans themselves are a neutral tool. The same mechanism enables:
- **Legitimate arbitrage** (risk-free, improves market efficiency)
- **Self-liquidation** (users closing underwater positions without additional capital)
- **Collateral swaps** (users changing their collateral type in one transaction)
- **Malicious exploitation** (all the attacks described above)

The distinction is in the *use*, not the mechanism. Protocols should not try to "ban" flash loans (they're part of Ethereum's design) but should design their systems to be safe *regardless* of how much capital an attacker can temporarily access.

## Related

- [[flash-loan-arbitrage]] — the legitimate use of flash loans
- [[oracle-manipulation]] — the most common target of flash loan attacks
- [[governance-attacks]] — flash loans enable governance manipulation
- [[smart-contract-risk]] — flash loans amplify existing vulnerabilities
- [[2020-02-bzx-flash-loan-attacks]] — the first major flash loan attacks
- [[2022-04-beanstalk-governance-attack]] — the most expensive governance-via-flash-loan attack
- [[defi-hacks-and-exploits]] — master timeline

## Sources

_Content based on Aave flash loan documentation, public exploit analyses, and academic research on DeFi security. No raw sources ingested._
