---
title: "OpenEden OpenDollar"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, stablecoin, real-world-assets, treasuries, defi]
aliases: ["USDO", "OpenDollar", "Open Dollar"]
entity_type: protocol
headquarters: "Bermuda (OpenEden Digital, BMA-licensed)"
website: "https://openeden.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[stablecoin]]", "[[real-world-assets]]", "[[treasuries]]", "[[tokenization]]", "[[tokenized-treasuries]]", "[[ondo-u-s-dollar-token]]", "[[midas-mtbill]]"]
---

# OpenEden OpenDollar

**OpenEden OpenDollar** (ticker **USDO**) is a **yield-bearing, US-dollar [[stablecoin]] backed by tokenized US Treasury bills**, issued by OpenEden Digital ("OED"), a Bermuda Monetary Authority (BMA) licensed digital-asset issuer. It is deployed on [[ethereum|Ethereum]] and [[base|Base]]. Unlike a conventional non-interest-bearing stablecoin, USDO is a **rebasing** token: holders accrue the yield earned on the underlying [[treasuries]] portfolio directly as a growing wallet balance, making it a [[real-world-assets]] (RWA) instrument as much as a payment dollar. The real-world asset it represents is a reserve of short-dated US government debt — primarily T-bills and reverse repurchase agreements.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

USDO trades at approximately **$0.997919**, holding its 1:1 USD peg (24h -0.04%, 7d +0.23%), with a market capitalization of roughly **$30.22M** (rank #639). The slight discount to $1.00 is within normal range for a redemption-gated RWA stablecoin whose secondary-market price can drift modestly from net asset value (NAV) between primary mint/redeem windows. As a Treasury-NAV instrument, **price ≈ peg/NAV by design** — rank and market cap are far less meaningful than the integrity of the reserve and redemption machinery.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDO |
| **Peg** | 1 USDO ≈ 1 USD (US dollar) |
| **Type** | Yield-bearing, rebasing RWA stablecoin |
| **Issuer** | OpenEden Digital (OED), BMA-licensed (Bermuda) |
| **Backing** | US Treasury bills + reverse repurchase agreements |
| **Chains** | Ethereum, Base |
| **Market Cap Rank** | #639 |
| **Market Cap** | $30,222,343 |
| **Current Price** | $0.997919 |
| **24h / 7d Change** | -0.04% / +0.23% |
| **Categories** | Stablecoins, USD Stablecoin, Real World Assets (RWA), US Treasury-backed Stablecoin, Ethereum/Base Ecosystem |
| **Website** | [https://openeden.com/](https://openeden.com/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

USDO is issued by OpenEden Digital, the same group behind **TBILL**, OpenEden's tokenized US Treasury-bill vault. The two products are structurally related: TBILL is the underlying tokenized T-bill exposure, and USDO is the dollar-denominated, rebasing stablecoin whose reserves are held in high-quality, liquid assets — primarily US Treasury bills and reverse repurchase agreements (repo). The value proposition is that holders earn the prevailing short-term Treasury yield (a "risk-free rate" passthrough) while retaining a stablecoin-like ~$1.00 unit of account.

Because it is regulated under the Bermuda Monetary Authority rather than the US, USDO is positioned as an offshore, compliance-oriented RWA dollar aimed at institutions and on-chain treasuries seeking dollar yield. As a [[tokenization]] product, its credibility rests on the quality and verifiability of the off-chain reserve portfolio and on the integrity of the mint/redeem process. USDO sits in the same competitive set as other [[tokenized-treasuries]] / yield-bearing dollars such as Ondo's USDY ([[ondo-u-s-dollar-token]]), BlackRock/Securitize BUIDL, and Mountain Protocol USDM.

---

## Architecture — How It Works

### Reserve / collateral model
USDO is backed by a reserve of **short-dated US Treasury bills and reverse repo** held off-chain through OpenEden's regulated structure. The reserve is designed to be 1:1 (or modestly over) against circulating USDO, so each token is a claim on a slice of a high-credit-quality, short-duration dollar portfolio. There is no fractional-reserve or algorithmic component — backing is real-world government paper, not crypto collateral or a seigniorage model.

### NAV / peg mechanism
The reserve's NAV anchors USDO to $1.00. Yield earned on the bills is the economic engine; rather than letting the unit price appreciate, USDO is a **rebasing** token — see below — so its target price stays at $1.00 while the holder's balance grows. The peg is enforced primarily by the **primary mint/redeem channel** (par creation and redemption against reserves), with secondary on-chain liquidity allowing free transfer. When secondary price drifts below $1, eligible arbitrageurs can redeem at par; this is why a small discount (here ~$0.998) can persist when redemption is gated and secondary liquidity is thin.

### Rebasing yield distribution
Rather than appreciating in price, **USDO accrues yield by increasing each holder's token balance over time**, keeping the unit price near $1.00. This makes it composable in [[defi]] applications that expect a stable ~$1 price. The trade-off: rebasing balances complicate tax/accounting (each rebase can be a taxable event in some jurisdictions) and require integrations to handle elastic-supply tokens correctly.

### Mint / redeem & KYC gating
New USDO is minted against USD/reserve deposits and redeemed back to dollars through OpenEden's primary channels, typically **gated by KYC/AML, eligibility checks, and processing windows**. Retail or non-whitelisted holders may be unable to redeem at par directly and must rely on secondary on-chain liquidity instead — a structural reason the market price can sit slightly below $1.00.

### Regulatory wrapper
USDO is issued by **OpenEden Digital, a BMA-licensed entity in Bermuda**. This offshore, regulated wrapper positions it outside the US securities/stablecoin regime while still offering a supervised structure to institutional users. Treatment of the token (security vs. e-money vs. stablecoin) varies by jurisdiction and is a live regulatory question for all yield-bearing RWA dollars.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~30M USDO (expands/contracts with mint/redeem) |
| **Total Supply** | tracks circulating (1:1 reserve-backed) |
| **Max Supply** | Unlimited (backed 1:1 by reserves) |
| **Market Cap / FDV Ratio** | ~1.00 |

Supply tracks reserve inflows and outflows; there is no speculative emission schedule, vesting, or pre-mine. The economic return to holders is the underlying Treasury yield distributed via rebasing, **not** token-price appreciation. Market cap rises and falls with deposits/redemptions rather than with speculation, so it is best read as "assets under tokenization" rather than a valuation.

---

## Comparison vs Peers

| Product | Issuer | Wrapper / Domicile | Yield mechanism | Backing |
|---|---|---|---|---|
| **USDO** (OpenEden) | OpenEden Digital | Bermuda (BMA-licensed) | **Rebasing** balance ($1 price) | US T-bills + reverse repo |
| **USDY** ([[ondo-u-s-dollar-token]], Ondo) | Ondo Finance | US/offshore structure | Accruing NAV (price > $1) | Cash + short Treasuries |
| **BUIDL** (BlackRock/Securitize) | BlackRock / Securitize | US (Reg D / SEC) | Daily dividend (rebase-like) | US Treasuries, repo, cash |
| **USDM** (Mountain Protocol) | Mountain Protocol | Bermuda (BMA-licensed) | **Rebasing** balance ($1 price) | Short-term US Treasuries |
| **mTBILL** ([[midas-mtbill]], Midas) | Midas | Permissioned wrapper | Accruing NAV (price > $1) | Short-dated US T-bills |

USDO's closest design analog is **USDM** (also Bermuda/BMA, also rebasing) — both keep a $1 price and grow balances. The accruing-NAV products (USDY, mTBILL) instead let the unit price rise above $1, which avoids rebase-related tax/accounting friction but breaks the "$1 unit of account" convenience.

---

## How & Where It Trades / Is Used

- **Primary market:** mint/redeem at par through OpenEden, gated by KYC/AML and eligibility; this is the canonical par mechanism.
- **Secondary on-chain liquidity:** modest pools on [[ethereum|Ethereum]] and [[base|Base]]. CoinGecko data shows no major centralized-exchange listings and very thin 24h volume — the token is held to earn yield, not actively traded.
- **Composability:** as a $1-priced rebasing dollar, USDO can in principle be used as collateral or a settlement leg in [[defi]] protocols that support elastic-supply tokens; integrations must handle rebases.
- **Eligibility:** primary access is institution-oriented and KYC-gated; retail typically only touches the token on secondary markets.

---

## Narrative / Category & Catalysts

USDO sits squarely in the **tokenized-Treasury / yield-bearing-stablecoin** narrative — one of the fastest-growing RWA categories. Catalysts and headwinds:
- **Rates:** the entire value proposition is a passthrough of short-term US yields. Higher-for-longer rates make the product attractive; rate cuts erode the yield that draws holders.
- **Institutional tokenization adoption:** growth tracks the broader push to put cash-management instruments on-chain.
- **Regulatory clarity:** a defined stablecoin regime (or a clear security classification) would either expand or constrain the addressable market for yield-bearing dollars.
- **Regime context:** as of 2026-06-22 the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **21 (Extreme Fear)** in an established bear market. Treasury-backed dollars are defensive flight-to-safety instruments in such regimes, but secondary liquidity tends to thin.

---

## History / Timeline

| Date | Event |
|---|---|
| 2026-04-09 | First captured in CoinGecko top-1000 snapshot ([[coingecko-top-1000-2026-04-09]]); listed as a Treasury-backed RWA stablecoin |
| 2026-06-21 | Market snapshot: ~$0.9979, market cap ~$30.22M (rank #639) |

*(Only dated events with sourcing are listed; broader OpenEden launch history is not yet ingested as a wiki source.)*

---

## Risks

- **Depeg risk:** the secondary price can drift below $1 (here ~$0.998) when redemption is gated and on-chain liquidity is thin; non-eligible holders cannot always arbitrage back to par.
- **NAV-gap risk:** the token is only worth its reserve NAV; any discrepancy between attested reserves and actual holdings directly threatens the peg.
- **Redemption-gating risk:** KYC/AML and eligibility requirements mean many holders cannot redeem at par directly, relying on thin secondary markets to exit.
- **Issuer / custodian counterparty risk:** value depends entirely on OpenEden Digital, its custodians, and administrators. On-chain holders cannot independently verify reserves moment-to-moment; they rely on attestations.
- **Yield / rate risk:** the yield is a passthrough of short-term rates and falls if Treasury yields fall; rebasing mechanics complicate tax and accounting treatment.
- **Regulatory risk:** operates under the BMA, not US regulators; classification and treatment vary by jurisdiction and could change.
- **Liquidity risk:** secondary on-chain liquidity (Ethereum/Base) is modest; primary mint/redeem is the canonical par mechanism but is gated and not instantaneous.

---

## Trading / Usage Playbook

- **Treat as a cash-management / yield instrument, not a trade.** USDO is for parking dollars on-chain to earn the T-bill yield via rebasing, not for directional exposure.
- **Mind the rebase mechanics.** Integrations and accounting must handle the growing balance; verify any DeFi protocol supports elastic-supply tokens before using USDO as collateral.
- **Buy at/under NAV, redeem at par.** If eligible, the par mint/redeem channel is the reliable exit; secondary buyers should watch for the small NAV discount.
- **Eligibility first.** Confirm KYC/jurisdiction eligibility before relying on primary redemption — non-whitelisted holders are exposed to thin secondary liquidity.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x8238884ec9668ef77b90c6dff4d1a9f4f4823bfe` |
| Base | `0xad55aebc9b8c03fc43cd9f62260391c13c23e7c0` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://openeden.com/](https://openeden.com/) |
| **Twitter** | [@OpenEden_Labs](https://twitter.com/OpenEden_Labs) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $836.64 |
| **Market Cap Rank** | #639 |
| **24h Range** | $0.9967 — $1.00 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]] / [[base]]
- [[stablecoin]]
- [[real-world-assets]]
- [[treasuries]] / [[tokenized-treasuries]]
- [[tokenization]]
- [[defi]]
- [[ondo-u-s-dollar-token]] — peer tokenized-Treasury dollar
- [[midas-mtbill]] — peer tokenized T-bill

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
