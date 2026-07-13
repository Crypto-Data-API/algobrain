---
title: "Other Notable Stablecoins"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [crypto, stablecoin, defi]
aliases: ["Other Stablecoins", "Stablecoin List"]
related: ["[[stablecoins]]", "[[usdc]]", "[[usdt]]", "[[dai]]", "[[usds]]", "[[ethena-usde]]", "[[frax]]", "[[gho]]", "[[bfusd]]", "[[defi]]", "[[binance]]", "[[aave]]", "[[regulation]]", "[[stablecoin-regulation]]", "[[stablecoin-yields]]"]
domain: [crypto, defi]
difficulty: intermediate
---

Beyond the dominant [[usdt|USDT]], [[usdc|USDC]], and [[dai|DAI]], dozens of other [[stablecoins]] serve various niches -- from exchange-specific tokens to fully decentralised alternatives to non-USD denominated coins. This page catalogues notable stablecoins that do not yet warrant individual pages, grouped by category.

> **Reference hub.** This is a catalog and comparison page, not a single tradeable asset — it carries no live price block. For peg mechanics and the largest names, follow the wikilinks to dedicated pages: [[usdc]], [[dai]], [[ethena-usde]], [[frax]], [[usds]], [[gho]]. Macro context (qualitative, 2026-06-21): broad crypto is in an **Established Bear Market** with the Crypto Fear & Greed Index around **23 ("Extreme Fear")** — stress regimes are precisely when peg robustness and reserve quality get tested, so the peg-mechanism taxonomy below is the most decision-relevant lens.

## Peg-Mechanism Taxonomy

Every stablecoin's risk profile flows from *how* it holds its peg. The four broad archetypes:

| Mechanism | How the peg is held | Primary risk | Examples |
|---|---|---|---|
| **Fiat-collateralised (off-chain reserves)** | 1:1 cash + short-dated T-bills held by a custodian/issuer; redeemable at par | Issuer/custodian solvency, regulatory seizure, attestation quality | [[usdc]], [[usdt]], [[pyusd]], USDP, RLUSD, FDUSD, TUSD |
| **Crypto-overcollateralised (on-chain)** | Locked crypto collateral > value minted; liquidations defend the peg | Collateral crash + liquidation cascade, oracle failure, smart-contract bugs | [[dai]], [[usds]], LUSD, [[gho]], crvUSD, [[frax\|FRAX (current, fully-backed)]] |
| **Delta-neutral / synthetic** | Long spot hedged with short perps; peg backed by collateral + funding-rate basis (not fiat) | Funding inversion (negative carry), exchange/custody risk, basis blowout | [[ethena-usde\|Ethena USDe]] (and the same engine behind [[bfusd]]) |
| **Algorithmic / undercollateralised** | Supply expands/contracts via a paired token or seigniorage; little/no hard backing | Reflexive death-spiral (mint-and-redeem loop unwinds) | UST/Terra (**collapsed 2022**), early FRAX (since abandoned) |

The post-2022 consensus, after the [[terra-luna-collapse|Terra/Luna collapse]], is that **pure algorithmic designs do not survive stress** — capital migrated decisively toward fiat-collateralised and overcollateralised models, with delta-neutral synthetics ([[ethena-usde|USDe]]) as the notable newer category that carries its own distinct (funding-dependent) risk rather than reserve risk.

## Centralised Fiat-Backed Stablecoins

### BUSD (Binance USD)

- **Issuer**: Paxos Trust Company (for [[binance|Binance]])
- **Peak market cap**: ~$22 billion (November 2022) -- was the #3 stablecoin
- **Status**: **Winding down.** In February 2023, NYDFS ordered Paxos to stop minting new BUSD, citing unresolved issues with Paxos's relationship with Binance. The [[sec|SEC]] also issued a Wells notice to Paxos alleging BUSD was an unregistered security.
- **Lesson**: Demonstrated that stablecoin issuers face direct regulatory risk -- a regulator can effectively kill a $22B stablecoin with a single order. Binance subsequently promoted [[usdt|USDT]] and FDUSD as replacements.

### FDUSD (First Digital USD)

- **Issuer**: First Digital Trust (Hong Kong)
- **Market cap**: ~$3B+ (2024)
- **Backing**: US Treasuries and cash deposits
- **Role**: Rose rapidly on [[binance|Binance]] after BUSD wind-down. Binance offers zero-fee trading on FDUSD pairs, incentivising adoption
- **Concerns**: Less regulatory clarity than US-based issuers. Incorporated in British Virgin Islands despite Hong Kong operations. Limited usage outside Binance
- **March 2025**: Faced brief de-peg concerns after Justin Sun alleged reserve inadequacy; First Digital denied claims and initiated legal action

### TUSD (TrueUSD)

- **Original issuer**: TrustToken / Prime Trust
- **Market cap**: Declined significantly from ~$3B peak
- **Status**: Lost transparency credibility in 2023 after auditor Prime Trust collapsed and was placed into receivership. Subsequently, control shifted to Justin Sun / Tron ecosystem. Reserve transparency deteriorated -- attestation reports delayed or incomplete
- **Lesson**: Stablecoin trust depends heavily on auditor/custodian integrity. When Prime Trust failed, TUSD's entire trust framework collapsed

### USDP (Pax Dollar)

- **Issuer**: Paxos Trust Company
- **Market cap**: ~$500M-1B
- **Formerly**: PAX (rebranded to USDP in 2021 to avoid confusion with Paxos the company)
- **Regulation**: NYDFS-regulated trust company -- same regulatory framework as BUSD and [[pyusd|PYUSD]]
- **Niche**: Smaller but among the most regulated stablecoins. Used in some institutional settlement applications

### RLUSD (Ripple USD)

- **Issuer**: Ripple Labs
- **Launched**: December 2024
- **Market cap**: Growing (early stage)
- **Backing**: USD deposits and US Treasuries, with regular attestations
- **Significance**: Ripple entering the stablecoin market adds competition from a company with extensive cross-border payment infrastructure and banking relationships. RLUSD is available on both XRPL (Ripple's native blockchain) and [[ethereum|Ethereum]]

## Decentralised / Protocol-Native Stablecoins

### FRAX

- **Protocol**: Frax Finance
- **Mechanism**: Originally a **partially algorithmic, partially collateralised** stablecoin. After the [[terra-luna-collapse|Terra/Luna collapse]] demonstrated the failure of algorithmic designs, FRAX moved to a **100% collateral ratio** in early 2023
- **Evolution**: Frax v2/v3 expanded into adjacent products:
  - **frxETH / sfrxETH**: Liquid [[staking]] derivative for Ethereum
  - **sFRAX**: Yield-bearing stablecoin backed by US Treasuries (~5% APY)
  - **FPI**: Inflation-pegged stablecoin (pegged to CPI, not $1)
  - **frxUSD**: New fully-backed stablecoin replacing FRAX
- **Market cap**: ~$600M-1B
- **Governance**: veFXS (vote-escrowed FXS) model inspired by Curve

### LUSD (Liquity USD)

- **Protocol**: Liquity
- **Mechanism**: The **purist decentralised stablecoin** -- ETH-only collateral, 110% minimum collateral ratio, no governance, fully immutable smart contracts
- **Key properties**:
  - No governance token voting on parameters -- all rules are hardcoded and cannot be changed
  - Cannot add new collateral types -- ETH only, forever
  - No admin keys -- the protocol cannot be upgraded or shut down by anyone
  - One-time 0.5% borrowing fee (no ongoing interest)
- **Market cap**: ~$200-500M
- **Trade-off**: Maximum decentralisation at the cost of flexibility and capital efficiency
- **Liquity v2**: In development, will add multi-collateral support and user-set interest rates, departing from v1's immutable philosophy

### GHO

- **Protocol**: [[aave|Aave]] (Aave DAO)
- **Launched**: July 2023
- **Mechanism**: Minted by Aave borrowers using their existing Aave collateral. Users who borrow GHO pay a GHO-specific interest rate set by Aave governance (separate from regular Aave borrow rates)
- **Market cap**: ~$100-200M (early stage)
- **Unique features**:
  - stkAAVE holders get discounted GHO borrow rates, incentivising Aave token staking
  - "Facilitators" -- entities authorised by Aave governance to mint GHO under specific conditions
- **Significance**: GHO allows Aave to capture the stablecoin issuance revenue (stability fees) that previously flowed to external stablecoins

### crvUSD

- **Protocol**: Curve Finance
- **Launched**: May 2023
- **Mechanism**: Uses a novel **"soft liquidation"** mechanism called LLAMMA (Lending-Liquidating AMM Algorithm). Instead of sudden liquidation at a threshold, borrower collateral is **continuously rebalanced** between the collateral asset and crvUSD through an AMM. If the collateral price drops, the position gradually converts to crvUSD; if it recovers, it converts back. This reduces the shock of hard liquidations.
- **Market cap**: ~$100-200M
- **Collateral**: ETH, WBTC, wstETH, sfrxETH, tBTC
- **Trade-off**: Soft liquidation is innovative but means borrowers experience gradual value loss during price declines rather than sudden liquidation

### USDe (Ethena) — synthetic dollar

- **Protocol**: [[ethena|Ethena]] (has its own page: [[ethena-usde]])
- **Mechanism**: A **delta-neutral synthetic dollar** — backed by spot crypto (ETH, BTC, LSTs) hedged with an equal short in perpetual futures. The peg is held not by fiat reserves but by the offsetting positions plus the [[funding-rates|funding-rate]] basis. sUSDe (staked USDe) passes the funding + staking yield through to holders
- **Why it matters here**: USDe became one of the largest non-fiat-backed dollar tokens, and the *same delta-neutral engine* powers Binance's [[bfusd|BFUSD]] margin asset. It is the flagship of the synthetic/delta-neutral archetype in the taxonomy above
- **Key risk**: **funding inversion** — in sustained negative-funding regimes the carry turns negative, and the backstop/insurance fund must absorb the bleed. Not a reserve-risk product; a basis-risk product. See [[stablecoin-yields]]

### USDS (Sky / ex-MakerDAO)

- **Protocol**: Sky (the rebranded MakerDAO); has its own page: [[usds]]
- **Mechanism**: The successor/upgrade to [[dai|DAI]] under the Sky rebrand — crypto-overcollateralised, with a savings rate (sUSDS) analogous to sDAI's DSR
- **Significance**: Represents the largest decentralised-stablecoin lineage migrating to a new brand and token while keeping the overcollateralised model

## Non-USD Stablecoins

### EURC (Euro Coin by Circle)

- **Issuer**: [[circle|Circle]]
- **Denomination**: Euro (EUR)
- **Regulation**: Positioned for MiCA compliance as an E-Money Token. Growing significantly as European regulation favours [[stablecoin-regulation|MiCA]]-compliant issuers
- **Market cap**: Growing but small (~$100M range)
- **Significance**: If MiCA-compliant euro stablecoins gain traction, they could reduce Europe's dependence on USD-denominated crypto. USDC/EURC pair on DEXs functions like a 24/7 forex market

### EURe (Monerium)

- **Issuer**: Monerium (Iceland-based, EU-regulated)
- **Denomination**: Euro (EUR)
- **Regulation**: Licensed as an EMI under EU regulation
- **Niche**: Focuses on on-chain euros with IBAN connectivity -- bridges traditional banking and DeFi

### XSGD and XIDR

- **Issuer**: Xfers / StraitsX (Singapore)
- **XSGD**: Singapore dollar stablecoin
- **XIDR**: Indonesian rupiah stablecoin
- **Regulation**: XSGD is issued under MAS (Monetary Authority of Singapore) regulation
- **Significance**: Important for Southeast Asian crypto markets. Singapore's "MAS-regulated stablecoin" framework gives XSGD a regulatory advantage. See [[stablecoin-regulation]]

### Non-USD Market Size

Euro, Singapore dollar, and other non-USD stablecoins collectively represent **less than 1%** of the total stablecoin market capitalisation. The overwhelming dominance of USD-denominated stablecoins reflects both the US dollar's role as global reserve currency and the crypto market's dollar-centric structure.

## Yield-Bearing Stablecoins

A growing category of stablecoins that pass underlying yield through to holders, rather than retaining it like [[usdc|USDC]] and [[usdt|USDT]]:

| Stablecoin | Protocol | Yield Source | Approximate APY | Notes |
|-----------|----------|-------------|----------------|-------|
| **sDAI** | MakerDAO | DSR (US Treasuries, stability fees) | 5-8% | See [[dai]] |
| **sFRAX** | Frax Finance | US Treasuries, DeFi yield | 4-5% | |
| **USDY** | Ondo Finance | Tokenised US Treasuries | 4-5% | Requires KYC, 40-day lockup |
| **USDM** | Mountain Protocol | US Treasuries | 4-5% | ERC-20 rebasing token |
| **stEUR** | Angle Protocol | Euro money market yield | 3-4% | Euro-denominated |

**Regulatory concern**: Yield-bearing stablecoins may be classified as **securities** by the [[sec|SEC]] and other regulators, since they offer a return on investment. This creates a regulatory distinction between "payment stablecoins" (no yield, likely regulated as money transmission) and "yield-bearing stablecoins" (potential securities). See [[stablecoin-regulation]].

For strategies on earning yield with stablecoins, see [[stablecoin-yields]].

## Summary Table

| Stablecoin | Type | Market Cap | Status | Regulatory Risk |
|-----------|------|-----------|--------|----------------|
| BUSD | Centralised | Declining | Winding down | Killed by NYDFS |
| FDUSD | Centralised | ~$3B | Active (Binance) | HK/BVI based |
| TUSD | Centralised | Declining | Trust issues | Lost auditor |
| USDP | Centralised | ~$500M | Stable | NYDFS-regulated |
| RLUSD | Centralised | Growing | New (2024) | Ripple-backed |
| FRAX | Hybrid→Collateralised | ~$600M | Active/evolving | Moderate |
| LUSD | Decentralised | ~$200-500M | Immutable | Minimal (no issuer) |
| GHO | Decentralised (Aave) | ~$100-200M | Growing | Moderate |
| crvUSD | Decentralised (Curve) | ~$100-200M | Active | Moderate |
| USDe | Delta-neutral synthetic | Large | Active | Basis/funding risk |
| USDS | Decentralised (Sky) | Large | Active (DAI successor) | Moderate |
| EURC | Centralised (EUR) | ~$100M | Growing | MiCA-positioned |

> *Market-cap figures above are approximate orders of magnitude carried from earlier ingestion, not a live 2026-06-21 snapshot. This is a catalog hub; verify current caps on the dedicated coin pages or a live data source before trading.*

## Related

- [[stablecoins]] -- Stablecoin market overview
- [[usdc]] -- Second-largest stablecoin
- [[usdt]] -- Largest stablecoin
- [[dai]] -- Largest decentralised stablecoin
- [[usds]] -- Sky's DAI successor
- [[ethena-usde]] -- Delta-neutral synthetic dollar
- [[frax]] -- Hybrid → fully-collateralised stablecoin
- [[gho]] -- Aave's native stablecoin
- [[pyusd]] -- PayPal's stablecoin
- [[bfusd]] -- Binance margin asset using the same delta-neutral engine as USDe
- [[binance]] -- BUSD/FDUSD primary exchange
- [[aave]] -- GHO issuer
- [[defi]] -- DeFi ecosystem
- [[stablecoin-regulation]] -- Regulatory landscape
- [[stablecoin-yields]] -- Earning yield on stablecoins
- [[terra-luna-collapse]] -- Catalyst for algorithmic stablecoin failures

## Sources

- General crypto market knowledge; no specific wiki source ingested yet.
