---
title: "Alpha Homora"
type: entity
created: 2026-04-22
updated: 2026-06-10
status: good
tags: [crypto, defi, leverage]
entity_type: protocol
aliases: ["Alpha Finance Lab", "ALPHA"]
founded: 2020
headquarters: "Decentralized (Thailand-based team)"
website: "https://alphafinance.io"
related: ["[[defi]]", "[[yield-farming]]", "[[defi-yield-farming]]", "[[leveraged-yield-farming]]", "[[impermanent-loss]]", "[[leverage]]"]
---

Alpha Homora is a leveraged [[yield-farming]] protocol built on [[ethereum]] and BNB Chain that allows users to borrow funds to amplify their liquidity provider positions by 2-3x. Developed by Alpha Finance Lab (later rebranded to Alpha Venture DAO), the protocol enables farmers to earn significantly higher yields on LP positions by borrowing additional capital from lenders, while lenders earn interest by supplying assets to the borrowing pool. The ALPHA governance token is used for protocol governance.

## How Alpha Homora Works

The protocol operates with two sides:

### For Yield Farmers (Borrowers)
1. **Select a farm:** Choose an LP pool on supported DEXs (Uniswap, SushiSwap, PancakeSwap, Curve, etc.)
2. **Choose leverage:** Deposit collateral and borrow additional assets at 2-3x leverage
3. **Amplified position:** The protocol opens a leveraged LP position on behalf of the user. A $10,000 deposit at 3x leverage creates a $30,000 LP position
4. **Amplified yields:** If the base APY is 20%, the leveraged APY is roughly 60% minus borrowing costs (typically 10-20%), netting ~40-50%
5. **Liquidation risk:** If the collateral value drops below the maintenance threshold (due to price movement or [[impermanent-loss]]), the position is liquidated

### For Lenders
1. **Supply assets:** Deposit ETH, stablecoins, or other supported tokens into lending pools
2. **Earn interest:** Receive lending yields (5-15% APY during high-demand periods) paid by leveraged farmers
3. **Low risk relative to farming:** Lenders do not face impermanent loss, though they bear smart contract risk and potential bad debt from liquidation failures

## Trading Relevance

- **Amplified yields:** 50-200% APY achievable on popular farm positions, far exceeding unleveraged farming
- **Capital efficiency:** Leverage lets smaller portfolios access yields typically requiring much larger capital
- **Lending yields:** The lending side offers relatively safe 5-15% yields on stablecoins and ETH
- **Liquidation dynamics:** Forced liquidations during market crashes create cascading sell pressure and can be exploited by liquidation bots

## Current Status (as of June 2026)

Alpha Homora is best treated as a **legacy protocol**. The team behind it has rebranded twice — Alpha Finance Lab → Alpha Venture DAO (2022) → **Stella** (2023) — with the same ALPHA token carrying over. Stella is a leveraged-strategies protocol marketed around "0% cost to borrow," deployed on Ethereum, Arbitrum, Avalanche and BNB Chain; the team's focus and development effort moved there, while Alpha Homora positions persist in maintenance mode (a status page remains at homora.alphaventuredao.io). At its peak Alpha Homora reached roughly **$1.9B TVL** as the first leveraged yield-farming protocol; current TVL is a small fraction of that. The 2021 exploit's bad debt also fueled a long-running 2023 dispute in which Iron Bank froze Alpha Homora accounts and demanded the protocol "take ownership" of the debt — a cautionary case study in DeFi counterparty/composability risk. Traders should treat ALPHA as a low-liquidity small-cap governance token tied to Stella's traction, not to Alpha Homora usage.

## The $37M Exploit (February 2021)

In February 2021, Alpha Homora suffered one of DeFi's largest exploits at the time:

- **Attack vector:** The attacker exploited a vulnerability in Alpha Homora V2's integration with Iron Bank (Cream Finance), using flash loans to manipulate the borrowing mechanism
- **Damage:** Approximately $37.5 million was drained from the protocol
- **Aftermath:** The exploit created significant bad debt in Iron Bank/Cream Finance, leading to prolonged disputes between the two protocols over who bore responsibility
- **Lessons:** The exploit highlighted the risks of composability in DeFi -- when multiple protocols interact, vulnerabilities at integration points can be catastrophic

## Supported Farms and Chains

Alpha Homora V2 supports leveraged farming on:

- **Ethereum:** Uniswap V2/V3, SushiSwap, Curve, Balancer LP positions
- **BNB Chain:** PancakeSwap, MDEX LP positions
- **Avalanche:** Trader Joe, Pangolin LP positions

Leverage levels typically range from 2x-3x depending on the asset pair risk tier. Stablecoin-stablecoin pairs allow higher leverage (up to 3x) while volatile pairs may be limited to 2x.

## Risks

- **Liquidation risk:** Leveraged positions face liquidation during sharp price moves or IL spikes. At 3x leverage, a relatively modest adverse price move can trigger liquidation
- **Smart contract risk:** Compounded by multiple protocol interactions (Alpha Homora + underlying DEX + underlying farm)
- **Impermanent loss amplification:** [[impermanent-loss]] is amplified proportionally to leverage -- 3x leverage means 3x IL
- **Borrowing cost variability:** Interest rates fluctuate with utilization; during high demand, borrowing costs can exceed farming yields
- **Bad debt risk:** If liquidations fail to execute quickly enough during crashes, the protocol can accumulate bad debt that affects lenders

## Related

- [[leveraged-yield-farming]] -- the strategy Alpha Homora enables
- [[defi-yield-farming]] -- the broader yield farming strategy category
- [[impermanent-loss]] -- amplified by leverage in Alpha Homora positions
- [[leverage]] -- the core mechanism for amplifying both returns and risks
- [[defi]] -- the decentralized finance ecosystem
- [[smart-contract-risk]] -- the primary risk vector, especially at protocol integration points

## Sources

- General knowledge -- protocol mechanics, exploit postmortem, and market data
- [Alpha Homora status page (Alpha Venture DAO)](https://homora.alphaventuredao.io/status)
- [Iron Bank tells Alpha Homora to 'take ownership' of its bad debt (The Block, 2023)](https://www.theblock.co/post/216832/iron-bank-tells-alpha-homora-to-take-ownership-of-its-bad-debt)
- [Stella (previously Alpha Venture DAO) — CoinGecko](https://www.coingecko.com/en/coins/stella)
- [Stella: the Leveraged Strategies Protocol With 0% Cost to Borrow (Medium)](https://medium.com/@stellaxyz_/stella-the-leveraged-strategies-protocol-with-0-cost-to-borrow-bad4f89d5cd3)
- Verified via web search, 2026-06-10
