---
title: "Compound"
type: entity
created: 2026-04-15
updated: 2026-06-10
status: good
tags: [crypto, defi, ethereum]
entity_type: protocol
founded: 2017
headquarters: "San Francisco, California, USA"
website: "https://compound.finance"
aliases: ["Compound", "Compound Finance", "Compound Protocol"]
related: ["[[defi]]", "[[yield-farming]]", "[[ethereum]]", "[[aave]]", "[[lending]]", "[[governance-tokens]]"]
---

Compound is a [[defi|decentralized finance]] lending and borrowing protocol built on [[ethereum|Ethereum]], founded by Robert Leshner and Geoffrey Hayes in 2017 and launched on mainnet in September 2018. It allows users to supply crypto assets to earn interest or borrow against their deposited collateral, with interest rates determined algorithmically based on supply and demand. Compound pioneered the concept of liquidity mining when it launched its COMP governance token distribution in June 2020, catalyzing the "DeFi Summer" boom.

## How It Works

### Supplying (Lending)
Users deposit supported assets (ETH, USDC, DAI, WBTC, etc.) into Compound's smart contracts. In return, they receive **cTokens** — interest-bearing tokens that represent their claim on the underlying deposit plus accumulated interest. For example, depositing USDC yields cUSDC. The cToken's exchange rate against the underlying asset increases over time as interest accrues, meaning the cTokens are continuously redeemable for a growing amount of the base asset.

### Borrowing
Users who have supplied collateral can borrow other assets up to their collateral factor (typically 60-80% of the collateral's value, depending on the asset). Borrowers pay a variable interest rate that adjusts per block based on the pool's utilization rate — the ratio of borrowed assets to total supplied assets. Higher utilization means higher rates, incentivizing new suppliers and discouraging additional borrowing.

### Interest Rate Model
Compound uses an algorithmic interest rate model:
- **Low utilization** (plenty of supply, little borrowing) — rates are low to encourage borrowing.
- **High utilization** (most supply is borrowed) — rates spike to attract new suppliers and deter further borrowing.
- A "kink" in the model creates a steep rate increase above a target utilization rate (typically ~80%), ensuring the protocol never runs out of liquidity for withdrawals.

### Liquidation
If a borrower's collateral value falls below the required minimum (due to price movements), their position becomes eligible for liquidation. Any user can repay part of the borrower's debt and receive a share of the collateral at a discount (typically 5-8%), creating an arbitrage incentive that keeps the protocol solvent. This liquidation mechanism is critical to Compound's ability to function without traditional credit checks.

## COMP Governance Token

On June 15, 2020, Compound began distributing COMP tokens to all users who supplied or borrowed on the protocol, proportional to their activity. This was the first major "liquidity mining" program in DeFi and triggered an explosion of similar programs across the ecosystem. Key facts about COMP:

- **Total supply**: 10 million COMP
- **Distribution**: ~42% allocated to protocol users via liquidity mining, ~24% to shareholders of Compound Labs, ~22% to founders and team, ~8% to community governance
- **Governance**: COMP holders can propose and vote on protocol changes, including interest rate models, supported assets, and collateral factors
- **Peak price**: COMP traded above $900 in May 2021 during the DeFi bull market

## Versions

- **Compound v1** (September 2018) — Initial launch, limited asset support.
- **Compound v2** (May 2019) — Introduced cTokens, the composable interest-bearing tokens that became a DeFi primitive. Other protocols could integrate cTokens as yield-bearing collateral.
- **Compound v3 (Comet)** (August 2022) — Complete redesign focusing on a single borrowable asset per market (e.g., USDC), simplifying the risk model and reducing the potential for cascading liquidations. V3 prioritized security and capital efficiency over composability.

## Scale and TVL

Compound's total value locked (TVL) peaked at approximately $12 billion in late 2021 during the broader DeFi and crypto bull market. By 2023-2024, TVL settled in the $2-4 billion range as the market cooled, [[yield-farming|yields compressed]], and competition from [[aave|Aave]] and newer protocols intensified. As of April 2026, TVL stood at roughly **$1.54 billion**, the large majority in Compound III (Comet) markets, with the Ethereum deployment holding ~$1.40B of that total. Compound has slipped well behind [[aave|Aave]] and Morpho in the lending league tables — a long decline from its 2020-2021 leadership.

## Notable Incidents and Governance Events

- **September 2021** — A bug in a governance proposal (Proposal 062) caused the Compound Comptroller contract to incorrectly distribute approximately $80 million in COMP tokens to users. The error could not be immediately patched because governance proposals require a multi-day timelock. Leshner initially tweeted asking users to return the tokens, which drew criticism for contradicting DeFi's "code is law" ethos.
- **July 2024 — "Golden Boys" governance attack** — A whale known as **Humpy** (who had previously executed a similar gauge-capture attack on Balancer in 2022) accumulated COMP on the open market and narrowly passed **Proposal 289**, diverting 499,000 COMP (~$24M, ~5% of the treasury) into a yield vault ("goldCOMP") controlled by his "Golden Boys" group, over broad community objection. After intense backlash, the move was defused through a negotiated compromise that included a COMP staking-rewards product, but the episode became a canonical example of low-turnout DAO governance capture risk.
- **January-March 2025 — Compound Blue (Morpho on Polygon)** — A Gauntlet-led proposal (passed with ~93% of voting weight) launched **Compound Blue**, Morpho-Blue-powered USDC/WETH/USDT/WPOL lending vaults on [[polygon|Polygon]], with $1.5M each in incentives from Polygon and Compound. The vaults went live 2025-03-13 at compound.blue. The move was controversial because it meant Compound deploying a rival's (Morpho's) infrastructure instead of its own stack — widely read as a signal of Compound's diminished engineering momentum.
- **April 2026 — Kelp DAO contagion** — The ~$293M Kelp DAO exploit (2026-04-18) hit Compound directly: attackers used unbacked rsETH as collateral, and roughly 107,000 exploited rsETH remained locked in active Compound positions. See [[2026-04-kelp-stable-sympathy-depeg]].

## Significance

Compound is a foundational DeFi protocol that established several patterns adopted across the ecosystem: algorithmic interest rates, composable interest-bearing tokens (cTokens), on-chain governance, and liquidity mining. Its design influenced dozens of lending protocols on [[ethereum|Ethereum]] and other chains. The protocol demonstrated that permissionless, decentralized lending could function at scale without traditional intermediaries, though it also highlighted the risks of smart contract complexity and governance attack vectors.

## Trading Relevance

- **Rates signal**: Compound's supply/borrow rates (especially USDC on Comet) are a live readout of on-chain dollar demand and leverage appetite; spiking borrow rates often coincide with basis-trade and leverage build-ups.
- **Liquidation flow**: large liquidation cascades on Compound/Aave amplify spot selling during sharp drawdowns — relevant to [[liquidation-cascade-fade]]-style strategies and [[defi-lending]] monitoring.
- **COMP as governance-risk beta**: COMP traded in the $40-60 range through mid-2025 (e.g., ~$60 on 2025-06-10, ~$46 by 2025-06-27), far below its $900+ May 2021 peak; governance events (Golden Boys, treasury proposals) have been sharp single-name catalysts.
- **Contagion node**: as the Kelp rsETH incident showed, Compound collateral listings are a transmission channel for collateral-asset exploits into blue-chip DeFi.

## Related

- [[defi]] — the ecosystem Compound operates within
- [[yield-farming]] — strategy popularized by Compound's COMP distribution
- [[ethereum]] — the blockchain Compound is built on
- [[aave]] — Compound's primary competitor in DeFi lending
- [[polygon]] — host chain of Compound Blue (Morpho-powered vaults)
- [[liquidity-pools]] — related DeFi primitive
- [[defi-lending]] — lending-market concepts and signals
- [[2026-04-kelp-stable-sympathy-depeg]] — April 2026 contagion event

## Sources

- DefiLlama, "Compound Finance TVL, Fees & Revenue" — https://defillama.com/protocol/compound-finance (TVL ~$1.54B, April 2026)
- DeSpread Research, "The Compound Finance Governance Attack: A Recap and Its Implications" — https://research.despread.io/compound-finance-governance-attack/
- The Block, "$24 million Compound Finance proposal passed by whale over DAO objections" (July 2024) — https://www.theblock.co/post/307943/24-million-compound-finance-proposal-passed-by-whale-over-dao-objections
- The Block, "Compound adopts Morpho's tech for new Polygon vaults in controversial Gauntlet-led move" (2025) — https://www.theblock.co/post/346161/compound-launches-new-vaults-rival-morpho-controversial-gauntlet-proposal
- crypto.news, "Compound launches Morpho-powered vaults on Polygon" (March 2025) — https://crypto.news/compound-launches-morpho-powered-vaults-on-polygon/
- The Defiant, "What Happened to Compound's Crypto Lending Empire?" — https://thedefiant.io/news/defi/what-happened-to-compound-defi-lender
- Verified via web search, 2026-06-10
