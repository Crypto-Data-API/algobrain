---
title: "DeFi Lending"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [defi, crypto, yield]
aliases: ["DeFi Lending", "Decentralized Lending"]
domain: [crypto, defi]
prerequisites: ["[[defi]]", "[[smart-contracts]]"]
difficulty: intermediate
related: ["[[aave]]", "[[defi]]", "[[impermanent-loss]]", "[[stablecoins]]", "[[yield-farming]]", "[[liquidation]]"]
---

DeFi lending enables permissionless borrowing and lending of [[crypto-overview|crypto]] assets through [[smart-contracts|smart contracts]], eliminating the need for traditional financial intermediaries like banks. It is one of the foundational pillars of [[defi|decentralized finance]], with leading protocols managing tens of billions in total value locked (TVL).

## How It Works

### Supplying (Lending)
Users deposit crypto assets into a lending protocol's liquidity pool and earn interest. The interest rate is determined algorithmically based on supply and demand (utilization rate):
- **Low utilization** (few borrowers relative to depositors): Low interest rates
- **High utilization** (heavy borrowing demand): High interest rates, incentivizing more deposits

Suppliers receive yield-bearing tokens (aTokens on [[aave|Aave]], cTokens on [[compound|Compound]]) that represent their deposit plus accrued interest.

### Borrowing
Users pledge collateral (deposit one asset) to borrow another. All DeFi loans are **over-collateralized** -- borrowers must deposit more value than they borrow:
- Typical collateral factor: 50-80% (deposit $1000, borrow $500-$800)
- Borrowers pay variable interest rates
- No credit checks, KYC, or approval process -- anyone with collateral can borrow

### Liquidation
If a borrower's collateral value drops below the required threshold (the "liquidation threshold"), anyone can repay part of the debt and claim the collateral at a discount (typically 5-10%). This mechanism ensures protocol solvency.

**Liquidation cascades**: During sharp market downturns, falling prices trigger liquidations, which create selling pressure, which causes further price drops and more liquidations. The March 2020 ("Black Thursday") crash and November 2022 [[ftx|FTX]] collapse both triggered massive DeFi liquidation cascades.

## Major Protocols

| Protocol | Chain | TVL (approx.) | Key Innovation |
|---|---|---|---|
| [[aave|Aave]] | Multi-chain | $10B+ | Flash loans, multi-chain deployment |
| [[compound|Compound]] | Ethereum | $3B+ | Pioneered algorithmic interest rates |
| MakerDAO | Ethereum | $8B+ | Issues [[stablecoins|DAI]] stablecoin via collateralized debt positions |
| Venus | BNB Chain | $1B+ | Compound fork on BNB Chain |
| Spark (Maker) | Ethereum | $2B+ | MakerDAO's direct lending frontend |

## Use Cases for Traders

1. **Leveraged trading**: Deposit [[ethereum|ETH]], borrow [[stablecoins|USDC]], buy more ETH -- effectively creating a leveraged long position without a centralized exchange
2. **Short selling**: Deposit stablecoins, borrow the asset you want to short, sell it, buy back later at a lower price
3. **Yield generation**: Supply idle assets to earn passive yield (typically 1-10% APY on stablecoins, variable on volatile assets)
4. **Capital efficiency**: Use deposited assets as collateral to access liquidity without selling (tax-advantaged in some jurisdictions)
5. **Flash loans**: Borrow any amount with zero collateral, as long as the loan is repaid within the same transaction. Used for [[arbitrage]], [[liquidation]] hunting, and collateral swaps

## Risks

- **[[smart-contracts|Smart contract]] risk**: Bugs or exploits can drain protocol funds. Multiple DeFi lending protocols have been hacked
- **Oracle risk**: Lending protocols rely on price oracles (Chainlink, etc.) to determine collateral values. Oracle manipulation can enable exploits
- **Liquidation risk**: Volatile [[collateral]] can be liquidated during flash crashes, even if the position would have recovered
- **Governance risk**: Protocol parameters (interest rates, collateral factors) can be changed via governance votes, potentially disadvantaging existing users
- **Systemic risk**: Heavy rehypothecation (using borrowed assets as collateral elsewhere) creates interconnected risk across DeFi

## Related

- [[aave]] -- Largest DeFi lending protocol by TVL
- [[defi]] -- The broader decentralized finance ecosystem
- [[stablecoins]] -- Most-borrowed assets in DeFi lending
- [[impermanent-loss]] -- A related DeFi risk concept (applies to AMMs, not lending)
- [[yield-farming]] -- Strategy that often involves lending protocols

## Sources

- DeFi lending mechanics are documented in protocol whitepapers and crypto research literature
