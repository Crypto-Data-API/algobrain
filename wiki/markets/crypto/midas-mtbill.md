---
title: "Midas mTBILL"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bonds, crypto, real-world-assets, treasuries]
aliases: ["MTBILL", "Midas US Treasury Bills Token"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.midas.app"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[ondo-u-s-dollar-token]]", "[[openeden-open-dollar]]", "[[real-world-assets]]", "[[tokenization]]", "[[tokenized-treasuries]]", "[[treasuries]]"]
---

# Midas mTBILL

**Midas mTBILL** (ticker **MTBILL**) is a tokenized [[real-world-assets|real-world asset]] (RWA): an on-chain wrapper issued by **Midas** that gives holders economic exposure to a portfolio of short-dated **US Treasury Bills**. The real-world asset it represents is a managed book of short-duration US government debt. It is *not* a free-floating crypto asset — its price tracks the net asset value (NAV) of the underlying off-chain T-bill collateral. Because yield is **accrued into the token's NAV** rather than paid out as a separate distribution, MTBILL trades **above $1** and rises gradually as interest accumulates. Its canonical contract lives on [[ethereum|Ethereum]], with deployments across Base, Rootstock, Plume Network, Oasis Sapphire and Etherlink. As of 2026-06-21 it traded at **$1.064**, ranked **#431** by market capitalization with a market cap of **~$53.34M**.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As a Treasury-NAV instrument, **price ≈ NAV by design**; rank and market cap matter far less than the soundness of the off-chain collateral and the redemption process.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MTBILL |
| **Market Cap Rank** | #431 |
| **Market Cap** | $53,344,780 (~$53.34M) |
| **Current Price** | $1.064 |
| **24h Change** | 0.00% |
| **7d Change** | +0.06% |
| **Underlying asset** | Short-dated US Treasury Bills (T-bill NAV) |
| **Issuer** | Midas |
| **Yield treatment** | Accrual into NAV (price > $1) |
| **Categories** | Tokenized Assets, Ethereum Ecosystem, Real World Assets (RWA), Tokenized Treasury Bills (T-Bills), Rootstock Ecosystem, Etherlink Ecosystem, Yield-Bearing Stablecoin, Plume Network Ecosystem, Midas Liquid Yield Tokens, Base Native |
| **Website** | [https://www.midas.app](https://www.midas.app) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Midas US Treasury Bills Token (mTBILL) is a yield-bearing token issued by **Midas** that tracks a portfolio of short-dated US Treasury Bills. It belongs to the [[tokenized-treasuries]] category — one of the largest segments of on-chain RWAs — alongside products from competitors such as [[ondo-finance|Ondo Finance]] (OUSG/USDY), BlackRock/Securitize (BUIDL), and Franklin Templeton (BENJI/FOBXX). Midas markets mTBILL as part of its "Liquid Yield Token" family of permissionless-to-hold, permissioned-to-mint RWA wrappers.

The token is a **wrapper**: each MTBILL is a claim on the off-chain T-bill collateral held by the issuer. Its on-chain price is therefore a function of the **NAV of the underlying bills**, not of crypto supply/demand. Interest earned on the bills is reflected by a steadily rising NAV (an *accruing* design), which is why MTBILL trades above $1.00 and its all-time low ($0.937, 2025-08-10) reflects an earlier, lower NAV base rather than a de-peg event.

---

## Architecture — How It Works

### Reserve / collateral model
mTBILL is backed by a **portfolio of short-dated US Treasury Bills** (and equivalent cash-management instruments) held off-chain by the issuer through a regulated structure. Each token is collateralized 1:1 against NAV — there is no fractional reserve and no crypto collateral. The economic exposure is essentially that of a short-duration government money-market position, wrapped as a transferable ERC-20.

### NAV / yield mechanism — accrual, not rebase
Yield is **reinvested into NAV**, so the *unit price* rises over time while the holder's token count stays constant. This contrasts with rebasing designs (e.g. USDM, OpenEden USDO) where the balance grows and the price stays near $1. The accrual design avoids rebase-driven taxable events on each distribution but means MTBILL is *not* a $1 unit of account — it is a price-appreciating wrapper.

### Mint / redeem & KYC gating
Primary issuance and redemption are **permissioned** — handled by Midas for eligible, KYC'd participants, with redemptions settled against the underlying T-bill NAV. Retail holders typically obtain the token on the **secondary market** (DEX/CEX) rather than minting directly. The redemption channel is the primary mechanism that keeps the on-chain price aligned with NAV.

### Settlement chains
mTBILL is issued cross-chain. The canonical contract lives on [[ethereum|Ethereum]], with deployments also on Base, Rootstock, Plume Network, Oasis Sapphire and Etherlink (see Contract Addresses below). Multi-chain reach broadens distribution but adds bridge/contract attack surface.

### Regulatory wrapper & off-chain dependency
Like all [[real-world-assets|RWA]] tokens, MTBILL depends on the issuer, its custodians, and the operational/legal machinery that holds the actual bills. The token is only as sound as that off-chain structure; the blockchain records the claim but cannot enforce delivery of the underlying securities.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 45.07M MTBILL |
| **Total Supply** | 45.07M MTBILL |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $47.64M |
| **Market Cap / FDV Ratio** | 1.00 |

Supply expands and contracts with mint/redeem flows; there is no emission schedule, vesting, or speculative tokenomics. Market cap is best read as "assets under tokenization." The economic return is the underlying short-term Treasury yield expressed through the rising NAV.

---

## Comparison vs Peers

| Product | Issuer | Yield mechanism | Domicile / wrapper | Notes |
|---|---|---|---|---|
| **mTBILL** (Midas) | Midas | **Accruing NAV** (price > $1) | Permissioned wrapper, multi-chain | T-bill exposure; price appreciates |
| **OUSG** (Ondo) | Ondo Finance | Accruing NAV | US (Reg D) / Securitize rails | Originally BUIDL-backed |
| **BUIDL** (BlackRock/Securitize) | BlackRock / Securitize | Daily dividend (rebase-like) | US (Reg D / SEC) | Largest tokenized Treasury fund |
| **USDY** ([[ondo-u-s-dollar-token]], Ondo) | Ondo Finance | Accruing NAV | Offshore | Tokenized note, $1+ price |
| **USTB** (Superstate) | Superstate | Accruing NAV | US-registered fund | Short-duration Treasury fund |

mTBILL's closest analogs are the **accruing-NAV** products (OUSG, USTB) that let the price rise above $1, as distinct from the rebasing dollars (USDM, USDO) that keep a $1 unit. Versus the giants (BUIDL), Midas competes on multi-chain availability and a leaner permissioned-mint structure rather than on AUM.

---

## How & Where It Trades / Is Used

- **Primary market:** permissioned mint/redeem through Midas for KYC'd, eligible participants, settled at NAV.
- **Secondary market:** DEX/CEX liquidity is thin (CoinGecko shows negligible 24h volume); MTBILL is held to earn yield, not actively traded.
- **Composability:** as a price-appreciating ERC-20, MTBILL can be used as collateral in DeFi venues that accept RWA tokens, though integrations must price it at NAV rather than $1.
- **Eligibility:** minting is institution/KYC-gated; retail access is via secondary markets.

---

## Narrative / Category & Catalysts

mTBILL is a pure-play on the **tokenized-Treasury** narrative. Key drivers:
- **Rates:** NAV growth tracks prevailing short-term US rates — higher rates make the product more attractive; cuts reduce accrual.
- **Institutional tokenization:** category growth follows the broader move to put cash management on-chain; Midas competes by spanning many chains.
- **Multi-chain expansion:** new deployments (Plume, Etherlink, etc.) widen the addressable DeFi surface.
- **Regime context:** as of 2026-06-22 the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **21 (Extreme Fear)** in an established bear market — a regime that favors defensive Treasury-yield instruments even as secondary crypto liquidity thins.

---

## History / Timeline

| Date | Event |
|---|---|
| 2025-08-10 | All-time-low price print of $0.9370 (reflects an earlier, lower NAV base — not a de-peg) |
| 2026-04-08 | All-time-high NAV print of $1.06 |
| 2026-04-09 | Captured in CoinGecko top-1000 snapshot ([[coingecko-top-1000-2026-04-09]]) |
| 2026-06-21 | Market snapshot: $1.064, market cap ~$53.34M (rank #431) |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.06 (2026-04-08) |
| **Current vs ATH** | ~flat |
| **All-Time Low** | $0.9370 (2025-08-10) |
| **24h Change** | 0.00% |
| **7d Change** | +0.06% |

The near-zero daily volatility is expected: the token is a wrapper over T-bill NAV, so it does not move with crypto-market beta. Its price drifts upward as interest accrues rather than oscillating like a typical token.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xdd629e5241cbc5919847783e6c96b2de4754e438` |
| Rootstock | `0xdd629e5241cbc5919847783e6c96b2de4754e438` |
| Plume Network | `0xe85f2b707ec5ae8e07238f99562264f304e30109` |
| Oasis Sapphire | `0xdd629e5241cbc5919847783e6c96b2de4754e438` |
| Base | `0xdd629e5241cbc5919847783e6c96b2de4754e438` |
| Etherlink | `0xdd629e5241cbc5919847783e6c96b2de4754e438` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.midas.app](https://www.midas.app) |
| **Twitter** | [@MidasRWA](https://twitter.com/MidasRWA) |
| **Telegram** | [midasrwa](https://t.me/midasrwa) (1.45M members) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $49.87 |
| **Market Cap Rank** | #431 |
| **24h Range** | $1.06 — $1.06 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks

- **Depeg / NAV-gap risk:** the secondary price can deviate from NAV under stress; the token is only worth its underlying T-bill NAV, and any reserve discrepancy threatens that value directly.
- **Off-chain dependency:** the token's value rests entirely on the off-chain T-bill portfolio. On-chain settlement cannot enforce delivery of the underlying — that is a legal/operational claim against the issuer.
- **Issuer & custody / counterparty risk:** failure, fraud, or mismanagement by Midas or its custodians could break the 1:1 backing. Unlike a US-domiciled fund, an RWA token wrapper may not carry the same investor protections.
- **Redemption-gating / regulatory risk:** primary mint/redeem is permissioned and KYC-gated; eligibility and transferability can be constrained by jurisdiction, and regulatory treatment of tokenized securities remains in flux.
- **Liquidity risk:** secondary on-chain liquidity is thin. Exiting size may require primary redemption through the issuer, which is not instantaneous.
- **Smart-contract / bridge risk:** multi-chain deployment adds bridge and contract-level attack surface.
- **Rate risk:** as a short-duration T-bill product, NAV growth tracks prevailing short-term US rates; falling rates reduce the accrual.

---

## Trading / Usage Playbook

- **Treat as a yield wrapper, not a trade.** mTBILL is for earning the T-bill yield on-chain via rising NAV, not for directional exposure.
- **Price at NAV, not $1.** Any collateral or accounting use must mark the token at its rising NAV; it is not a $1 unit of account.
- **Mint/redeem through the issuer if eligible.** The permissioned NAV redemption channel is the reliable par exit; secondary buyers face thin liquidity.
- **Watch rates.** The accrual rate is a passthrough of short-term Treasury yields — the main driver of expected return.

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[real-world-assets]]
- [[tokenization]]
- [[treasuries]] / [[tokenized-treasuries]]
- [[ondo-u-s-dollar-token]] — peer tokenized-Treasury dollar
- [[openeden-open-dollar]] — peer T-bill-backed stablecoin

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original listing snapshot
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific Midas source document ingested yet.

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 50.77M MTBILL |
| **Total Supply** | 50.77M MTBILL |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $54.14M |
| **Market Cap / FDV Ratio** | 1.00 |

---
