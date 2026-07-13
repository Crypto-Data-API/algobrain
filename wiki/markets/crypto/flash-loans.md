---
title: "Flash Loans"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [crypto, defi, arbitrage, derivatives]
aliases: ["Flash Loans", "Flash Loan", "Flashloan"]
related: ["[[defi]]", "[[arbitrage]]", "[[liquidity-pools]]", "[[aave]]", "[[liquidation]]"]
domain: [defi]
difficulty: advanced
---

A flash loan is an uncollateralized loan in [[defi|decentralized finance]] that must be borrowed and repaid within a single blockchain transaction. Because Ethereum-style transactions are atomic -- they either fully succeed or revert entirely, leaving no trace -- a lender can hand over millions of dollars with no collateral, confident that if the borrower fails to repay (plus a fee) by the end of the transaction, the entire operation is unwound as if it never happened. Flash loans are a uniquely DeFi primitive with no analogue in traditional finance, and they are the engine behind a large share of on-chain [[arbitrage|arbitrage]], collateral swaps, and -- notoriously -- many of the largest DeFi exploits.

## Overview

In conventional lending, a loan is risky because the borrower might default and disappear with the money. Flash loans eliminate default risk through **atomicity**: the borrow, the use of funds, and the repayment all happen in one transaction. The lending protocol's smart contract checks, at the end of execution, that it has been made whole (principal + fee). If not, the [[evm|EVM]] reverts every state change in the transaction, so the loan effectively never occurred. The lender therefore takes essentially zero credit risk, which is why no collateral is required.

Flash loans were popularized by **[[aave|Aave]]**, which launched the feature in January 2020. **dYdX**, **[[uniswap|Uniswap]]** (via "flash swaps"), **Balancer**, and **MakerDAO** offer similar facilities. Fees are small -- Aave historically charged 0.09% of the borrowed amount, later reduced to 0.05% -- making flash loans cheap relative to the size of capital they unlock.

### Providers Compared

| Provider | Primitive | Typical fee | Notes |
|----------|-----------|-------------|-------|
| **[[aave|Aave]]** | `flashLoan` (multi-asset) | 0.05% | Pioneered the feature (Jan 2020); deepest liquidity; supports a batch of assets in one call |
| **[[uniswap]]** (v2/v3) | "flash swap" | swap fee (0.30% / tiered) | Borrow either token of a pair; repay in either token or the other side of the pair |
| **Balancer** | Vault flash loan | 0% (protocol fee) | Free flash loans from the shared Vault; popular with searchers for that reason |
| **dYdX** (v3) | `Operate` with deposit/withdraw | ~0% (gas only) | Historically near-free; widely used in early flash-loan exploits |
| **MakerDAO** | DAI flash mint | 0% (governance-set) | Mints/burns DAI directly rather than lending reserves -- enormous size, capped by a per-tx ceiling |

The DAI **flash mint** is a notable variant: instead of lending existing reserves, MakerDAO mints fresh DAI for the duration of the transaction and burns it on repayment, so the available size is bounded only by a governance ceiling rather than by pool depth.

## How Flash Loans Work

A flash loan transaction packs four steps into one atomic call:

1. **Borrow** -- the contract requests, say, 10,000,000 USDC from a lending pool.
2. **Execute logic** -- within the same transaction, the borrowed funds are used: swap across DEXs, repay and re-open a loan, liquidate a position, etc.
3. **Repay** -- the principal plus fee is returned to the pool.
4. **Verify** -- the protocol confirms repayment; if the balance check fails, the whole transaction reverts.

```solidity
// Conceptual sketch (Aave-style)
function executeFlashLoan() external {
    uint256 amount = 10_000_000e6;           // 10M USDC
    lendingPool.flashLoan(address(this), USDC, amount, params);
    // protocol calls back into executeOperation() below
}

function executeOperation(address asset, uint256 amount, uint256 fee, ...) external {
    // 1. use `amount` of USDC: arbitrage, liquidation, collateral swap...
    doProfitableThing(amount);
    // 2. repay principal + fee, or the entire tx reverts
    IERC20(asset).approve(address(lendingPool), amount + fee);
}
```

The borrower needs **no upfront capital** beyond the gas fee -- the defining feature that democratizes access to large size, for both legitimate and malicious use.

## Legitimate Use Cases

- **[[arbitrage|Arbitrage]]** -- exploit a price difference for the same asset across DEXs or pools. Borrow USDC, buy ETH cheaply on pool A, sell it dearly on pool B, repay the loan, keep the spread -- all in one transaction, with no personal capital at risk.
- **Collateral swaps** -- atomically replace the collateral backing a loan (e.g. swap ETH collateral for stETH on Aave) without first having to repay the debt out of pocket.
- **Self-[[liquidation]] and debt refinancing** -- close or restructure a leveraged position to avoid an external liquidator's penalty, or migrate debt between protocols to chase a better rate.
- **Liquidations** -- liquidators borrow the funds needed to repay an underwater borrower's debt, seize the discounted collateral, and repay the flash loan from the proceeds, pocketing the [[liquidation|liquidation bonus]] without holding inventory.

These are core components of [[mev|MEV]] and on-chain market-making, allowing small operators to compete with well-capitalized players on equal footing.

### Worked Example: Capital-Free Arbitrage (qualitative)

Suppose ETH trades at 2,000 USDC in [[uniswap|Uniswap]] pool A but 2,030 USDC in a Curve-style pool B, a 1.5% gap left by an imbalance. A searcher with no inventory can capture it atomically:

1. **Flash-borrow** 2,000,000 USDC from [[aave|Aave]].
2. **Buy** ~1,000 ETH in pool A at the cheaper price (the buy itself walks the [[automated-market-maker|AMM]] price up, so realized size is less than the headline gap implies -- [[slippage]] eats part of the spread).
3. **Sell** the ETH into pool B at the higher price.
4. **Repay** 2,000,000 USDC + the ~0.05% fee to Aave.
5. **Keep** the remaining USDC as profit -- net of gas, the fee, and price impact in both pools.

If any step leaves the searcher unable to repay, the whole transaction reverts and the only cost is gas. This is why flash loans turn arbitrage into a near-riskless, capital-free activity that keeps DEX prices tightly aligned -- see [[on-chain-trading]] and [[arbitrage]].

## Flash-Loan Attacks

The same atomicity that makes flash loans safe for lenders makes them a weapon against *other* protocols. Because an attacker can wield tens of millions of dollars for free, they can temporarily distort any state that depends on instantaneous market conditions. Most flash-loan "attacks" are not attacks on the flash loan itself -- they exploit a vulnerability elsewhere, using the loan as cheap, frictionless capital. The flash loan is the amplifier, not the root cause. See [[defi-hacks-and-exploits]] for the broader catalogue.

The classic pattern is **oracle manipulation**: a protocol that reads its prices from a single DEX [[liquidity-pools|pool]] can be fed a false price by a whale-sized swap, then exploited (e.g. borrowing against an inflated collateral value) before the price is arbitraged back -- all atomically.

### Attack Vectors

| Vector | What is abused | Typical defense |
|--------|----------------|-----------------|
| **Oracle manipulation** | Spot price read from a single shallow [[liquidity-pools\|pool]] | TWAP / multi-source oracles ([[chainlink\|Chainlink]]) |
| **Governance capture** | One-block token-balance voting | Vote snapshots, timelocks, vote-escrow |
| **Reentrancy + collateral abuse** | Re-entered callbacks revaluing collateral | Checks-effects-interactions, reentrancy guards |
| **Mint / reward manipulation** | Pool-share or reward math distorted mid-tx | Read-only reentrancy guards, fair-mint accounting |
| **Peg / depeg pressure** | Stable-pool curve pushed off peg | Deeper liquidity, circuit breakers |

### Notable Incidents

| Incident | Year | Approx. loss | Vector |
|----------|------|-------------|--------|
| bZx | 2020 | ~$1M (two attacks) | Oracle manipulation via DEX |
| Harvest Finance | 2020 | ~$24M | Pool price manipulation |
| PancakeBunny | 2021 | ~$45M (paper) | Mint manipulation via flash loan |
| Cream Finance | 2021 | ~$130M | Reentrancy + oracle/collateral abuse |
| Beanstalk | 2022 | ~$182M | Flash-loaned governance vote |
| Euler Finance | 2023 | ~$197M | Donation/liquidation logic flaw (funds later returned) |

The **Beanstalk** exploit (April 2022) is illustrative: the attacker flash-borrowed enough capital to acquire a supermajority of governance tokens, passed a malicious proposal draining the treasury, and repaid the loan -- all in one transaction. The **Euler Finance** hack (March 2023) was one of the largest single DeFi losses, though the attacker ultimately returned most of the funds after negotiation.

## Trading and Market Relevance

- Flash loans collapse the **capital barrier to on-chain arbitrage and liquidations**, making DeFi markets more efficient and keeping DEX prices tightly arbitraged against each other and against CEXs.
- They are a foundational tool of **[[mev|MEV]] searchers**, who bundle flash loans with arbitrage and liquidation logic.
- They shift the security burden onto every protocol that reads on-chain prices: robust **manipulation-resistant oracles** (e.g. [[chainlink|Chainlink]], time-weighted average prices) are the standard defense.

## Risks

- **For lenders/LPs**: negligible credit risk by design, but exposure to smart-contract bugs in the flash-loan implementation itself.
- **For other protocols**: any logic relying on spot DEX prices, single-block snapshots, or governance-by-token-balance is attackable with flash-loaned capital. Defenses include TWAP oracles, multi-source oracles, governance timelocks, and snapshot-based voting.
- **For users**: flash-loan-enabled exploits can drain pools users have deposited into, an under-appreciated [[smart-contract-risk|smart-contract risk]] in DeFi.

## Related

- [[defi]] -- the ecosystem flash loans operate within
- [[arbitrage]] -- the most common legitimate use case
- [[liquidity-pools]] -- the source of borrowable funds and the surface for oracle manipulation
- [[aave]] -- pioneered flash loans in 2020
- [[liquidation]] -- flash loans power capital-free liquidations
- [[mev]] -- flash loans are a core MEV tool
- [[smart-contract-risk]] -- the broader risk category exploited in flash-loan attacks
- [[defi-hacks-and-exploits]] -- catalogue of DeFi exploits, many flash-loan-powered
- [[on-chain-trading]] -- the execution environment where flash-loan arbitrage runs
- [[chainlink]] -- manipulation-resistant oracles, the standard defense

## Sources

- General market knowledge; no specific wiki source ingested yet.
