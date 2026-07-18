---
title: "Tokenized Treasuries"
type: concept
created: 2026-07-17
updated: 2026-07-19
status: draft
tags: [crypto, defi, real-world-assets, stablecoins, treasuries, on-chain]
aliases: ["Tokenized T-Bills", "On-Chain T-Bills", "RWA Yield", "Tokenized Money Market Funds"]
domain: [crypto, market-microstructure]
difficulty: intermediate
prerequisites: ["[[stablecoins]]", "[[defi]]"]
---

# Tokenized Treasuries

**Tokenized treasuries** are on-chain representations of short-duration U.S. Treasury instruments — T-bills, money-market funds, and repo facilities — that allow crypto-native wallets and DeFi protocols to earn real-world yield without moving assets off-chain. They are the dominant category within **real-world assets (RWA)** tokenisation and represent the first large-scale convergence of traditional finance yield with DeFi composability. Major products include BlackRock's BUIDL, Ondo Finance's OUSG, Franklin Templeton's BENJI, and Mountain Protocol's USDM.

## How It Works

Tokenized treasury protocols follow a common structure:

1. **Issuer deposits fiat** with a regulated custodian (e.g., BNY Mellon, State Street) and purchases short-duration Treasuries or money market fund units.
2. **Smart contract mints tokens** (e.g., BUIDL, OUSG) that represent a fractional claim on the underlying Treasury portfolio.
3. **Yield accrual mechanism:** Either *rebasing* (the token quantity increases daily to reflect yield — e.g., USDM) or *increasing NAV* (the token price rises while quantity stays fixed — e.g., BUIDL where $1 per token is maintained via stablecoin redemption, with yield distributed as additional USDC).
4. **Redemption:** Token holders can redeem for fiat or stablecoin, subject to KYC/AML requirements and minimum thresholds (typically $10,000–$100,000).
5. **On-chain composability:** Some tokenized treasuries are permissioned (whitelisted wallets only, e.g., BUIDL). Others are more permissive and can be used as DeFi collateral.

**Regulatory wrapper:** All major tokenized treasury products require KYC/AML and are only available to accredited investors or institutional wallets. This limits their DeFi composability relative to stablecoins, which are permissionless.

## Concrete Examples

- **BUIDL (BlackRock/Securitize, launched Mar 2024):** Ethereum-native, Securitize-issued token backed by a BlackRock MMF holding US Treasuries, repos, and cash. Reached $1.5B+ TVL by mid-2024, making it the largest tokenized treasury by AUM. Pays yield as additional USDC to whitelisted wallets. Minimum investment: $5M.
- **OUSG (Ondo Finance, launched Jan 2023):** Backed by BlackRock's SHV ETF (short-term Treasuries). More DeFi-friendly than BUIDL — OUSG is wrapped into rebasing rOUSG for use as DeFi collateral. Minimum: $100k. Also available on Arbitrum and Polygon for lower gas.
- **BENJI (Franklin Templeton, launched 2021):** The earliest large tokenized money market fund. Runs on Stellar and Polygon. The fund itself is registered with the SEC as a money market fund — unusually, the blockchain record is the official record of ownership, not a traditional transfer agent.
- **USDM (Mountain Protocol, 2023):** A rebasing stablecoin backed by short-duration Treasuries. Target of major DeFi protocol integrations (Curve, Morpho) because it rebases yield directly into the token balance — simple to integrate without yield-compounding logic.

## Trading Relevance

Tokenized treasuries are primarily a *treasury management* and *collateral yield* tool rather than a directional trade, but they create specific strategy contexts:

- **Base rate for DeFi yield strategies:** Tokenized treasury yields (currently ~4-5% annualised, tracking Fed Funds rate) set the opportunity cost for DeFi strategies. Any strategy — [[funding-rate-arbitrage]], [[defi-yield-farming]], [[liquidity-mining]] — should be compared against the risk-free on-chain yield from BUIDL/OUSG. If DeFi yield after costs ≤ tokenized T-bill yield, the DeFi strategy is not compensating for its additional risk.
- **[[multi-strategy-crypto-portfolio]] stablecoin reserve yield:** A well-managed crypto book earns yield on its idle stablecoin reserve. Tokenized treasuries (permissioned) or yield-bearing stablecoins backed by Treasuries (USDM, sDAI) allow the reserve to compound at the risk-free rate without additional directional exposure.
- **Carry trade and funding rate comparison:** When BTC perp funding rates exceed tokenized treasury yield by less than the hedging cost, the [[funding-rate-arbitrage]] / [[basis-trade]] loses its attractiveness relative to simply holding BUIDL. Monitoring the spread between funding rates and T-bill yields is a rotation signal between carry strategies.
- **Regulatory and liquidity risk:** Tokenized treasuries depend on off-chain custodians and issuers. A redemption halt (regulatory action against issuer, custodian failure) would cause a depeg event — the on-chain token cannot be redeemed for its claimed value. This is a tail risk analogous to [[stablecoin-depegs]] but with different failure modes (issuer credit vs. algorithmic stability).
- **Arbitrage between tokenized and traditional Treasury yields:** Temporary yield discrepancies between BUIDL/OUSG secondary market prices and the underlying T-bill yield create small arbitrage windows for large KYC'd participants who can both buy on-chain (secondary DEX) and redeem directly with the issuer.

## Related

- [[ondo-finance]] — OUSG issuer; DeFi-focused tokenized treasury
- [[stablecoins]] — the permissionless analogue; lower yield but no KYC
- [[tokenized-assets]] — broader RWA tokenisation category
- [[defi-yield-farming]] — strategies competing with tokenized treasury yields
- [[funding-rate-arbitrage]] — carry strategy that must clear the tokenized T-bill rate as its opportunity cost
- [[multi-strategy-crypto-portfolio]] — stablecoin reserve earns tokenized treasury yield
- [[stablecoin-depegs]] — the analogous tail risk for on-chain yield instruments
- [[basis-trade]] — the crypto carry trade that competes with T-bill yield for capital allocation

## Sources

- General crypto/RWA knowledge; no specific wiki source ingested yet.
