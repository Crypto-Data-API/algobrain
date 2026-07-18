---
title: "StraitsX XUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, regulation, stablecoins, defi]
aliases: ["XUSD"]
entity_type: protocol
headquarters: "Singapore (StraitsX)"
website: "https://www.straitsx.com/xusd"
related: ["[[crypto-markets]]", "[[depeg]]", "[[ethereum]]", "[[regulation]]", "[[stablecoin]]", "[[usdc]]", "[[xsgd]]", "[[binance]]", "[[stablecoin-depeg-profit-capture]]", "[[stablecoin-pair-arbitrage]]"]
---

# StraitsX XUSD

**StraitsX XUSD** (XUSD) is a fiat-backed, USD-pegged [[stablecoin]] issued by **StraitsX**, a **Singapore-based** payments-infrastructure provider. Each XUSD is intended to be backed 1:1 by US dollar reserves, and StraitsX has positioned XUSD to comply with **Singapore's Monetary Authority (MAS) stablecoin regulatory framework**, bridging ASEAN payments with a dollar-denominated settlement asset. It is the USD counterpart to StraitsX's Singapore-dollar coin **XSGD**.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

## Market Snapshot (2026-06-21)

| Field | Value |
|---|---|
| **Ticker** | XUSD |
| **Price (USD)** | $0.999996 (on peg) |
| **Market Cap Rank** | #481 |
| **Market Cap** | $46,615,459 |
| **24h Change** | +0.02% |
| **7d Change** | -0.01% |
| **Currency tracked** | US dollar (USD) |

Unlike the FX-pegged coins [[frankencoin]], [[brz]], and [[brla-digital-brla]], XUSD targets the US dollar, so a price of **~$1.0000** is the peg holding tightly. The near-zero 24h/7d moves confirm a stable peg.

## Issuer & Jurisdiction

XUSD is issued by **StraitsX** (operated by the Xfers/StraitsX group), **Singapore-based**, working within the **Monetary Authority of Singapore's (MAS)** stablecoin regulatory approach. StraitsX holds **Major Payment Institution (MPI) licences** from MAS covering most regulated payment services (including e-money issuance, money transfers, and digital-payment-token services), and XUSD has been acknowledged by MAS as compliant with its stablecoin regulatory framework. This regulated, single-jurisdiction posture differentiates XUSD from purely decentralized stablecoins and aligns it with the compliance-first model also seen in [[usdc]]. StraitsX additionally issues a Singapore-dollar stablecoin (**XSGD**), making XUSD its USD counterpart and giving it a dual SGD/USD product line for ASEAN settlement.

## Architecture — How It Works

### Reserve & collateral model
XUSD is **fiat-collateralised**: reserves are intended to be held at **at least 100% of outstanding tokens in circulation**, in cash and cash-equivalent instruments at **regulated institutions**, subject to **independent external audit**. StraitsX has partnered with **DBS** (a major Singapore bank) for cash management and custody of the reserve assets — a notable strength, since reserve-bank quality is the single biggest driver of fiat-backed peg safety.

### Regulatory wrapper & jurisdiction
The MAS framework imposes specific requirements on single-currency stablecoins (full reserve backing, redemption at par, audit, capital), and XUSD is explicitly designed around it. The Singapore wrapper plus DBS custody gives XUSD a comparatively strong regulatory and counterparty profile for a coin of its size.

### Peg & redemption mechanism
The peg is held by **1:1 mint on USD deposit and redemption at par**, plus secondary-market arbitrage. Full-reserve backing and a defined redemption right are the core peg-stability mechanism.

### Mint / redeem, KYC gating, on/off-ramp rails
- **Mint:** Verified users mint XUSD by depositing USD through StraitsX's regulated ramp after **KYC**.
- **Redeem:** XUSD is redeemable for USD via StraitsX, supporting round-trip settlement.
- **Rails:** StraitsX's payments infrastructure (and its SGD product XSGD) provides the fiat on/off-ramp into the ASEAN banking system.

## Tokenomics & Supply

XUSD is supply-elastic and mint-on-deposit: circulating supply expands and contracts with USD deposits and redemptions rather than following an emission schedule, with reserves held at ≥100% of circulation. There is no native yield to holders. Snapshot market cap was ~$46.6M.

## Comparison vs Other USD / Regional Stablecoins

| | **XUSD** | **[[usdc\|USDC]]** | **[[usdt\|USDT]]** | **XSGD (sibling)** |
|---|---|---|---|---|
| **Peg** | US dollar | US dollar | US dollar | Singapore dollar |
| **Issuer** | StraitsX (Singapore) | Circle | Tether | StraitsX (Singapore) |
| **Regulatory frame** | MAS (Singapore), MPI-licensed, MAS-acknowledged | US/EU regulated, MiCA-aligned EU | Offshore, attestation-based | MAS (Singapore) |
| **Reserve / custody** | ≥100% reserves; DBS custody; external audit | Cash + short T-bills; regulated custody | Cash + T-bills + other | SGD reserves; DBS custody |
| **Chains** | Ethereum, BNB Chain, Solana | Multi-chain | Multi-chain | Ethereum, others |
| **Focus** | ASEAN USD settlement, 24/7 cross-border | Global USD settlement | Global liquidity | ASEAN SGD settlement |
| **Mkt cap (snapshot)** | ~$46.6M | tens of billions | ~$100B+ | smaller |

XUSD's edge is its **MAS-regulated, DBS-custodied** profile for ASEAN dollar settlement; it cannot match the global liquidity of USDC/USDT but offers a clearer single-jurisdiction regulatory story.

## Backing Model & Mint / Redeem (summary)

- **Backing:** **Fiat-backed**, ≥100% against USD reserves (cash and cash-equivalent instruments) held at regulated institutions, with DBS custody and external audit.
- **Mint:** Verified users mint XUSD by depositing USD through StraitsX's regulated ramp after KYC.
- **Redeem:** XUSD is redeemable for USD via StraitsX, supporting round-trip settlement.
- **Chains:** Deployed on [[ethereum]] (first on Ethereum, **February 2024**), BNB Chain, and Solana; tradable on venues including Binance (XUSD/USDT).
- **Use case:** 24/7 cross-border payments and dollar settlement for the ASEAN region.

## How & Where It Trades / Is Used

- **Trading:** Listed on venues including **Binance** (XUSD/USDT) and present across its deployment chains; depth is moderate for a ~$47M-cap coin.
- **Payment corridors:** 24/7 **cross-border USD settlement for ASEAN**, leaning on StraitsX's regulated rails and its SGD sibling XSGD for the regional fiat legs.
- **DeFi composability:** standard multi-chain token (Ethereum, BNB Chain, Solana) usable in DEX/lending, though far shallower than the dollar majors.

## Narrative, Category & Catalysts

XUSD is a **regulated, single-jurisdiction USD stablecoin** built for **ASEAN payments**. Catalysts: Singapore's first-mover MAS stablecoin framework (a credibility magnet for compliant issuers); growth in ASEAN cross-border commerce and remittances; and StraitsX's dual SGD/USD product line enabling local-currency↔dollar settlement. As a dollar peg, XUSD carries **no FX exposure** — its USD value should hold ~$1.00 across regimes — so the 2026 Extreme-Fear/bottoming backdrop affects it mainly through overall stablecoin demand and venue liquidity rather than its peg.

## History / Timeline

- **February 2024** — XUSD smart contract first deployed on [[ethereum|Ethereum]] (ERC-20); StraitsX secured MAS Major Payment Institution licences and launched the XUSD USD-pegged stablecoin.
- Subsequently expanded to **BNB Chain and Solana** and listed on venues including Binance.

## Risks

- **Issuer / reserve-counterparty risk:** As a centrally issued fiat-backed coin, holders rely on StraitsX maintaining full reserves and honoring redemptions; the strength of reserve attestations and DBS custody matters.
- **Regulatory risk:** Singapore's stablecoin regime is still maturing; regulatory changes could affect issuance, redemption, or eligibility.
- **Counterparty / banking risk:** Reserves held with banks or in short-term instruments carry counterparty exposure (a USD stablecoin can [[depeg]] if a reserve bank fails, as seen in past industry episodes — e.g. the USDC/SVB episode).
- **Redemption-gating risk:** Par redemption is KYC-gated through StraitsX's regulated ramp; access frictions or a freeze would impair the peg's arbitrage for non-onboarded holders.
- **Liquidity / concentration risk:** With ~$47M market cap, depth is moderate; large redemptions or a venue outage could cause short-term price dislocation.
- **Smart-contract risk:** Bugs in the token or bridge contracts on any deployment chain could affect supply.

## Trading / Usage Playbook

- **As a dollar instrument:** XUSD is a USD-peg token (no FX exposure) with a **strong regulatory/custody profile** for its size — suited to ASEAN-facing dollar settlement rather than maximal global liquidity.
- **On/off-ramp use:** use StraitsX's MAS-regulated KYC ramp (and XSGD for the SGD leg) for round-trip cross-border settlement.
- **Peg monitoring:** watch for any sustained deviation from $1.00 and the status of the redemption channel; size to venue depth (Binance XUSD/USDT and on-chain pools), not headline cap.

## Trading Profile

### Venues & liquidity
XUSD is a USD-pegged stablecoin traded on [[binance]] (XUSD/USDT), plus on-chain across its Ethereum, BNB Chain, and Solana deployments. It is a **peg / cash-management instrument, not a directional asset** — the profile is about peg stability, backing/reserves, depeg risk, and yield/arbitrage rather than momentum. Because it is a full-reserve fiat-backed dollar coin, there is no directional thesis to lever; the only "trade" is capturing small deviations around $1.00. With a market cap around the mid-hundreds by rank and moderate CEX depth, venue availability is the binding constraint: execution and sizing should track the actual XUSD/USDT book on Binance and on-chain pool depth, not headline cap, since large orders can move a thin book and complicate round-trip arbitrage.

### Applicable strategies
- [[stablecoin-depeg-profit-capture]] — buy XUSD below par when a transient dislocation appears, redeeming or waiting for reversion to $1.00 via StraitsX's par redemption right.
- [[stablecoin-pair-arbitrage]] — trade XUSD against deeper dollar pegs (USDC/USDT) when the XUSD/USDT cross drifts off 1:1 on Binance or on-chain.
- [[mint-parity-arbitrage]] — exploit gaps between secondary-market price and StraitsX's 1:1 mint/redeem for KYC-verified users to pull XUSD back to peg.
- [[stablecoin-yield]] — deploy XUSD in DEX/lending venues across its chains for yield, since the token itself pays no native yield to holders.
- [[synthetic-stablecoin-depeg-arbitrage]] — hedge or construct offsetting positions across XUSD and sibling/peer pegs during broader stablecoin stress events.
- [[carry-trade]] — hold XUSD as the dollar leg against yield-bearing legs, harvesting rate spreads while the peg stays tight.

### Volatility & regime character
XUSD is a fiat-collateralised dollar peg with reserves intended at ≥100% of circulation, DBS custody, and external audit, so day-to-day it trades in a razor-thin band around $1.00 (recent 24h range roughly $0.9999–$1.00). Peg tightness is maintained by par mint/redemption plus secondary-market arbitrage. Its price history shows the peg has not been perfectly static — it has recorded both an all-time low below par and a brief spike above par — indicating that thin liquidity, not the backing model, drives its rare deviations. Regime sensitivity is therefore about overall stablecoin demand and venue liquidity rather than crypto directionality; the coin carries no FX exposure.

### Risk flags
- **Depeg risk** — a fiat-backed dollar coin can [[depeg]] if a reserve bank fails or during liquidity stress (cf. past industry episodes); thin depth amplifies short-term dislocations.
- **Reserve / backing transparency** — holders rely on StraitsX maintaining full reserves and on the quality/frequency of external attestations and DBS custody.
- **Redemption gating** — par redemption is KYC-gated through StraitsX's regulated ramp; access frictions or a freeze impair peg arbitrage for non-onboarded holders.
- **Regulatory** — Singapore's MAS stablecoin regime is still maturing; changes could affect issuance, redemption, or eligibility.
- **Liquidity / concentration** — moderate CEX depth means large redemptions or a venue outage can cause short-term price dislocation.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=XUSDUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=XUSDUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=XUSDUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=XUSDUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

## See Also

- [[stablecoin]]
- [[crypto-markets]]
- [[ethereum]]
- [[usdc]]
- [[xsgd]]
- [[regulation]]
- [[depeg]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

