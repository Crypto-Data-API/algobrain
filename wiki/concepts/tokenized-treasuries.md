---
title: "Tokenized Treasuries"
type: concept
created: 2026-07-17
updated: 2026-10-17
status: review
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

**Regulatory wrapper:** All major tokenized treasury products require KYC/AML and are only available to accredited investors or institutional wallets. This limits their DeFi composability relative to stablecoins, which are permissionless. *(Review note 2026-10-17: "only accredited investors" is too strong. BENJI, below, is an SEC-registered money market fund, a structure normally open to retail investors who pass KYC. All products do require KYC. Eligibility (accredited, qualified purchaser, non-US only) varies by product.)*

**Market size (dated):** per [[real-world-assets]], tokenized Treasuries and money-market funds were the largest RWA bucket at roughly **$7-10B in early-to-mid 2026**. [[defi-narratives]] records Treasuries growing from ~$10B to ~$13.4B within a ~$26-31B tokenized-RWA market around March 2026. The two pages measure differently; use a live tracker (rwa.xyz) for current figures.

## Concrete Examples

- **BUIDL (BlackRock/Securitize, launched Mar 2024):** Ethereum-native, Securitize-issued token backed by a BlackRock MMF holding US Treasuries, repos, and cash. Reached $1.5B+ TVL by mid-2024, making it the largest tokenized treasury by AUM. Pays yield as additional USDC to whitelisted wallets. Minimum investment: $5M. *(Correction 2026-10-17: the "$1.5B+ by mid-2024" figure conflicts with the rest of the wiki. See Contradictions. BUIDL is also no longer Ethereum-only: it was on five chains by March 2026.)*
- **OUSG (Ondo Finance, launched Jan 2023):** Backed by BlackRock's SHV ETF (short-term Treasuries). More DeFi-friendly than BUIDL — OUSG is wrapped into rebasing rOUSG for use as DeFi collateral. Minimum: $100k. Also available on Arbitrum and Polygon for lower gas.
- **BENJI (Franklin Templeton, launched 2021):** The earliest large tokenized money market fund. Runs on Stellar and Polygon. The fund itself is registered with the SEC as a money market fund — unusually, the blockchain record is the official record of ownership, not a traditional transfer agent.
- **USDM (Mountain Protocol, 2023):** A rebasing stablecoin backed by short-duration Treasuries. Target of major DeFi protocol integrations (Curve, Morpho) because it rebases yield directly into the token balance — simple to integrate without yield-compounding logic. *(Status unverified, 2026-10-17: Mountain Protocol was reported in 2025 to have been acquired by Anchorage Digital, with USDM being wound down. No wiki source confirms this. Check USDM's current redeemability before treating it as a live product.)*
- **sDAI → sUSDS (Sky):** the savings wrapper over Sky's (formerly Maker's) stablecoin. Its yield is largely funded by RWA Treasury holdings, so it behaves as a permissionless, indirect tokenized-T-bill exposure. See [[makerdao]] and [[sky]].

## Trading Relevance

Tokenized treasuries are primarily a *treasury management* and *collateral yield* tool rather than a directional trade, but they create specific strategy contexts:

- **Base rate for DeFi yield strategies:** Tokenized treasury yields (currently ~4-5% annualised, tracking Fed Funds rate) set the opportunity cost for DeFi strategies. Any strategy — [[funding-rate-arbitrage]], [[defi-yield-farming]], [[liquidity-mining]] — should be compared against the risk-free on-chain yield from BUIDL/OUSG. If DeFi yield after costs ≤ tokenized T-bill yield, the DeFi strategy is not compensating for its additional risk.
- **[[multi-strategy-crypto-portfolio]] stablecoin reserve yield:** A well-managed crypto book earns yield on its idle stablecoin reserve. Tokenized treasuries (permissioned) or yield-bearing stablecoins backed by Treasuries (USDM, sDAI) allow the reserve to compound at the risk-free rate without additional directional exposure.
- **Carry trade and funding rate comparison:** When BTC perp funding rates exceed tokenized treasury yield by less than the hedging cost, the [[funding-rate-arbitrage]] / [[basis-trade]] loses its attractiveness relative to simply holding BUIDL. Monitoring the spread between funding rates and T-bill yields is a rotation signal between carry strategies.
- **Regulatory and liquidity risk:** Tokenized treasuries depend on off-chain custodians and issuers. A redemption halt (regulatory action against issuer, custodian failure) would cause a depeg event — the on-chain token cannot be redeemed for its claimed value. This is a tail risk analogous to [[stablecoin-depegs]] but with different failure modes (issuer credit vs. algorithmic stability).
- **Arbitrage between tokenized and traditional Treasury yields:** Temporary yield discrepancies between BUIDL/OUSG secondary market prices and the underlying T-bill yield create small arbitrage windows for large KYC'd participants who can both buy on-chain (secondary DEX) and redeem directly with the issuer.

*Dating note:* "~4-5% annualised" is a 2024-25 figure. Tokenized T-bill yields reset with the front end of the US curve, so read the live yield rather than this page.

### Strategies that use the T-bill rate as a hurdle or a leg

- [[stablecoin-yield]] — stablecoin yield stacking, where tokenized T-bills are the risk-free floor.
- [[dollar-carry-trade]] — macro context. The FX carry trade keys off the same 3-month US T-bill rate that tokenized Treasuries pay.
- [[delta-neutral-yield-farming]] / [[funding-rate-harvest]] — delta-neutral carry should beat the T-bill yield *after* hedging cost, venue risk and ADL risk (see [[liquidations]]).
- [[rwa-basket]] — the RWA-token sector basket. Its tokens co-move on tokenization news such as new BlackRock funds or T-bill product launches. Holding them is a bet on tokenization *adoption*, not on the T-bill yield itself.
- [[asymmetric-barbell]] — the safe leg of a barbell can be tokenized T-bills instead of idle stablecoins.

**Simple rule of thumb:** carry hurdle = T-bill yield + (hedge cost + expected venue/ADL loss). If annualised funding minus the hurdle is ≤ 0, park the capital in T-bills.

## Contradictions

> **Claim A** (Source: this page, pre-2026-10-17 text, confidence: LOW): BUIDL "reached $1.5B+ TVL by mid-2024, making it the largest tokenized treasury by AUM."
> **Claim B** (Source: [[blackrock]], confidence: MEDIUM): BUIDL "quickly accumulated over $500M", which made it the largest fund at the time.
> **Claim C** (Source: [[securitize]], confidence: MEDIUM): BUIDL was the largest tokenized Treasury fund "through most of 2024-2025 (peaking near $2.9B) before being overtaken by a competitor in early 2026". [[real-world-assets]] gives ~$2.5B by May 2026; [[defi-narratives]] gives $2.24B across 5 chains in March 2026.
> **Resolution**: Claims B and C are favoured. A $1.5B mid-2024 figure would be well ahead of the trajectory the other pages describe. BUIDL is not "the largest" as of 2026 per Claim C. Pending a dated AUM series.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/sentiment/macro` — macro snapshot including a `treasury_yield` field (the T-bill hurdle; confirm tenor in the response)
- `GET /api/v1/sentiment/stablecoins` — stablecoin market cap and 14d/90d flows (the permissionless dollar pool that competes with tokenized T-bills)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding, to compare carry against the T-bill hurdle
- `GET /api/v1/coins/category-groups` — curated **RWA** group (issuer and platform tokens) with price and market cap

**Historical data:**
- `GET /api/v1/backtesting/funding?symbol=BTC&start=2025-01-01` — funding history for carry-vs-T-bill backtests
- `GET /api/v1/sentiment/stablecoins/remote-history?days=365` — daily stablecoin supply history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/sentiment/macro"
```

Auth: `X-API-Key` header. Full endpoint catalogs: [[cryptodataapi-sentiment]], [[cryptodataapi-derivatives]], [[cryptodataapi-backtesting]]. Per-product AUM (BUIDL, BENJI, OUSG) is not served; use rwa.xyz or issuer reports.

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
