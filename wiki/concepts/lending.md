---
title: "Crypto Lending"
type: concept
created: 2026-07-19
updated: 2026-09-05
status: good
tags: [crypto, defi, lending, risk-management, leverage, interest-rates, yield]
aliases: ["DeFi Lending", "CeFi Lending", "Crypto Money Markets", "Crypto Lending Desks"]
domain: [defi, risk-management]
prerequisites: ["[[defi]]", "[[collateral]]", "[[leverage]]"]
difficulty: intermediate
related: ["[[aave]]", "[[morpho]]", "[[compound]]", "[[liquidations]]", "[[defi]]", "[[collateral]]", "[[leverage]]", "[[flash-loans]]", "[[funding-rate-arbitrage]]", "[[cash-and-carry]]", "[[leveraged-yield-farming]]", "[[short-selling]]", "[[voyager-digital]]", "[[blockfi]]", "[[counterparty-risk]]", "[[stablecoins]]", "[[dai]]", "[[makerdao]]"]
---

# Crypto Lending

**Crypto lending** is the practice of borrowing and lending crypto assets for interest, and it comes in two structurally different flavors: **DeFi money markets** (Aave, Morpho, Compound) — overcollateralized, non-custodial, and priced by algorithmic interest-rate curves — and **CeFi lending desks** (Celsius, BlockFi, Voyager) — custodial platforms that pooled deposits and lent them out to institutional borrowers, exposing depositors to counterparty risk they often could not see. Both models set the "price of leverage" in crypto, and both feed a family of trading strategies — borrow-to-short, leveraged yield farming, and cash-and-carry funding — that depend on lending rates behaving in a specific, exploitable way.

## DeFi Money Markets

DeFi lending protocols are **overcollateralized**: every loan must be backed by collateral worth more than the amount borrowed, with no reliance on the borrower's identity or creditworthiness — the collateral itself is the only credit check. [[aave|Aave]], [[morpho|Morpho]], and [[compound|Compound]] are the dominant venues, and while they differ in architecture (Aave and Compound run shared, pooled markets; Morpho runs isolated per-pair markets plus curated vaults on top), the core mechanics are the same across all three.

### Utilization-rate interest curves

Interest rates are not set by a human — they are computed algorithmically from **pool utilization** (the share of supplied liquidity that is currently borrowed). As utilization rises, the borrow rate rises smoothly along a curve until it hits a **kink point** (commonly 80-90% utilization), past which the rate slope steepens sharply — sometimes to triple-digit annualized rates. The kink exists to defend liquidity: if a pool gets too close to fully utilized, suppliers cannot withdraw, so the protocol makes borrowing punitively expensive at exactly the point where a liquidity crunch would otherwise begin. Supply-side yield is a function of the same utilization number (borrow APY × utilization, minus a protocol reserve factor), so lenders earn more precisely when the pool is under more borrowing pressure. This makes DeFi borrow rates a real-time, public read on on-chain leverage demand: a stablecoin borrow rate spiking toward the kink is a classic early tell for a deleveraging episode, because it means traders are aggressively bidding for borrowed capital.

### Health factor and liquidation mechanics

Every borrow position carries a **health factor (HF)** — the ratio of (collateral value × liquidation threshold) to outstanding debt. A health factor above 1 means the position is solvent; once it falls below 1, anyone can trigger a **liquidation**: a bot repays some or all of the unhealthy debt and, in exchange, claims the borrower's collateral at a discount (a liquidation bonus, typically 5-15%). This is fully automated, permissionless, and fast — liquidation bots compete to be first, which is itself a source of on-chain [[mev|MEV]]. See [[liquidations]] for the general mechanics of forced position closure (the perpetual-futures version of the same idea — margin falling below a maintenance threshold — works on an analogous principle, though the collateral-seizure mechanics differ from a DeFi health-factor liquidation).

Two features shape how liquidation risk behaves at scale:

- **Liquidation cascades** — a sharp market drawdown can push many positions below their health-factor threshold simultaneously; the resulting wave of forced collateral sales adds sell pressure that pushes price down further, triggering the next tranche of liquidations. This is structurally the same feedback loop as a perp liquidation cascade, just running through collateral seizure instead of margin calls.
- **Isolation and risk segmentation** — Aave's isolation mode restricts newer or riskier collateral to backing only stablecoin borrows up to a debt ceiling, and Morpho Blue takes this further by making every market a standalone, isolated collateral/loan pair by design (with curated MetaMorpho vaults sitting on top to diversify risk across markets for depositors who don't want to pick individual pairs themselves). Both are direct responses to the same problem: a bad long-tail collateral asset should not be able to create bad debt across an entire shared pool.

### Flash loans: a side effect of the lending market

**[[flash-loans|Flash loans]]** — uncollateralized loans that must be borrowed and repaid within a single atomic blockchain transaction — exist because DeFi lending pools hold large amounts of idle liquidity that can be lent risk-free as long as repayment is guaranteed by the transaction itself reverting on failure. They are a genuine side effect of the lending-market design, not a separate product: the same liquidity pool that backs ordinary overcollateralized loans is what a flash-loan borrower draws from. Flash loans are used constructively for arbitrage, collateral swaps, and self-liquidation (a borrower closing their own unhealthy position before a liquidation bot claims the bonus), and notoriously as the funding leg for a large share of DeFi exploits, since they let an attacker temporarily command more capital than they could ever collateralize.

## CeFi Lending Desks

Centralized crypto lenders — Celsius Network, BlockFi, Voyager Digital, and Genesis Trading among the largest — offered a fundamentally different, custodial model: depositors handed assets to the platform in exchange for a fixed interest rate (often 8-12% APY, well above anything achievable on a transparent DeFi money market), and the platform then lent those assets to institutional borrowers — market makers, hedge funds, and proprietary trading firms — to generate the yield it paid out. The critical difference from DeFi lending is that **depositors had no visibility into who the platform lent to, at what collateral level, or with what risk controls**. This is pure [[counterparty-risk|counterparty risk]]: the platform, not a smart contract, decided how much leverage and concentration risk to take on depositors' behalf.

That design collapsed catastrophically in 2022. [[terra-luna|Terra/LUNA]]'s implosion in May 2022 triggered the failure of Three Arrows Capital (3AC), a hedge fund that had borrowed heavily and unsecured (or under-secured) from nearly every major CeFi lender. **[[voyager-digital|Voyager Digital]]** had lent 3AC roughly $650M and filed for bankruptcy in July 2022 when the loan defaulted. **[[blockfi|BlockFi]]** survived that first wave only by taking a $400M rescue credit line from FTX — a line that evaporated when FTX itself collapsed in November 2022, forcing BlockFi into bankruptcy weeks later. Celsius Network filed for bankruptcy in the same window after revealing it, too, had taken concentrated, poorly hedged risk with customer deposits. The contagion sequence — Terra/LUNA → 3AC → Voyager/Celsius/Genesis → FTX → BlockFi — is the canonical case study in how interconnected, opaque CeFi lending concentrates and transmits systemic risk across the entire industry, rather than containing it within one insolvent counterparty. See [[voyager-digital]] and [[blockfi]] for the full case histories, including the multi-year bankruptcy and enforcement aftermath.

**The durable lesson**: an above-market, fixed CeFi lending rate is compensation for risk the depositor cannot see or price — if the yield looks too good to be true relative to what a transparent, overcollateralized DeFi market pays for the same asset, the platform is very likely taking on hidden leverage or concentration risk to fund it.

## How Lending Rates Feed Strategy Families

Because DeFi borrow/supply rates are transparent, on-chain, and continuously priced by utilization, they function as an input to several strategy families rather than merely a cost of capital:

- **Borrow-to-short** — a trader who wants directional short exposure without a perp venue can borrow the target asset from a money market, sell it immediately on the spot market, and repay the loan later at (hoped-for) lower price, pocketing the difference minus borrow interest. This is the DeFi-native version of a traditional [[short-selling|short sale]], and it is exactly the mechanism liquidation bots and self-liquidators also use in miniature.
- **Leveraged yield farming** — a trader deposits a yield-bearing asset as collateral, borrows against it, swaps the borrowed funds back into the same or a correlated yield-bearing asset, and re-deposits, looping the position multiple times to amplify the underlying yield (and its risk) with borrowed capital. See [[leveraged-yield-farming]] for the full mechanics and the reflexive unwind risk this creates — the Aave-Pendle-Ethena sUSDe looping trade that built up through 2025 and unwound sharply in October 2025 (see [[ethena|Ethena]] and [[synthetic-dollar]]) is a recent, large-scale example.
- **Cash-and-carry / funding-rate strategies** — [[cash-and-carry]] and [[funding-rate-arbitrage|funding-rate arbitrage]] typically need cheap, reliable stablecoin financing to fund the long leg of a basis trade (long spot, short perp, or vice versa). A trader who can borrow stablecoins from a money market at a rate below the annualized funding/basis they expect to collect is running the same core trade banks run in traditional cash-and-carry — lending-market rates set the cost side of that spread, and a rate spike can turn a profitable carry unprofitable overnight.

In all three cases, the DeFi lending market's transparency is the point: because utilization and rates are public and update continuously, they can be monitored as a leverage/leverage-unwind signal in their own right, independent of whether you are a borrower in the trade.

## Getting the Data (CryptoDataAPI)

[[cryptodataapi|CryptoDataAPI]] does not carry on-chain DeFi protocol lending rates (Aave/Compound/Morpho supply and borrow APYs are not part of its schema as of this writing) — for those, DeFi-native sources like the protocols' own dashboards or DefiLlama remain the reference. Its genuinely relevant surface for the lending-linked strategies above is the **funding-rate leg** of cash-and-carry and leveraged-yield-farming trades, via [[cryptodataapi-derivatives|CryptoDataAPI's Derivatives category]]:

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange (Binance + Hyperliquid) perp funding for one coin in a single call, the financing-side counterpart to a stablecoin-borrow-funded carry position
- `GET /api/v1/derivatives/summary?coin=BTC` — combined funding, open interest, and positioning snapshot for sizing the carry leg against borrow cost

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates` — Binance funding history (paged)
- `GET /api/v1/backtesting/funding` — deeper funding archive back to 2020, for backtesting a lending-funded carry strategy

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

## Related

- [[aave]] — largest DeFi money market; health factor, utilization curves, flash loans, isolation mode
- [[morpho]] — isolated lending markets plus curated MetaMorpho vaults
- [[compound]] — the original shared-pool DeFi money market and liquidity-mining pioneer
- [[liquidations]] — general mechanics of forced position closure under leverage
- [[collateral]] — the asset backing every overcollateralized loan
- [[flash-loans]] — uncollateralized, atomic loans enabled by lending-pool liquidity
- [[funding-rate-arbitrage]], [[cash-and-carry]] — strategies financed by lending-market borrow rates
- [[leveraged-yield-farming]] — looped borrowing to amplify yield
- [[short-selling]] — the traditional-finance analogue of borrow-to-short
- [[voyager-digital]], [[blockfi]] — canonical CeFi lending collapses of the 2022 contagion
- [[counterparty-risk]] — the core risk CeFi lending depositors bear that DeFi lending removes
- [[stablecoins]], [[dai]], [[makerdao]] — stablecoins are both a common lending-market asset and, in DAI's case, minted through an overcollateralized lending mechanism themselves
- [[defi]]

## Sources

- [[aave]], [[morpho]], [[compound]] — wiki entity pages for protocol-level mechanics (utilization curves, health factor, isolation mode, isolated markets and vaults)
- [[voyager-digital]], [[blockfi]] — wiki entity pages for the 2022 CeFi lending collapse case histories
- General knowledge of DeFi money-market design (overcollateralization, utilization-based interest curves, liquidation bonuses) and the 2022 CeFi lending contagion sequence, cross-checked against the cited wiki pages
