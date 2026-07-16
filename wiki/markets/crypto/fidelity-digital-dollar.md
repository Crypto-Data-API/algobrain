---
title: "Fidelity Digital Dollar"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, money-market-fund, real-world-assets]
aliases: ["FIDD", "Fidelity Digital Dollar"]
entity_type: protocol
headquarters: "United States (Fidelity Digital Assets)"
website: "https://www.fidelitydigitalassets.com/stablecoin"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[money-market-fund]]", "[[real-world-assets]]", "[[stablecoin]]", "[[tokenization]]", "[[treasuries]]"]
---

# Fidelity Digital Dollar

**Fidelity Digital Dollar** (ticker **FIDD**) is a US-dollar-denominated tokenized cash product issued by **Fidelity Digital Assets, National Association** — a subsidiary of Fidelity Investments — deployed on [[ethereum|Ethereum]] as an ERC-20. The real-world asset it represents is a reserve of US-dollar cash and short-term, high-quality money-market instruments held at the regulated Fidelity entity. It is positioned as a tokenized money-market / "digital dollar": a token backed 1:1 by that off-chain reserve and redeemable 1:1 for US dollars, with the on-chain price tracking the $1 backing. Functionally it behaves like a [[real-world-assets|real-world asset]] wrapper over a cash / money-market base rather than a free-floating crypto token. As of 2026-06-21 it traded at **$1.00**, ranked **#464** by market capitalization with a market cap of **~$48.86M**.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

As a $1-pegged dollar token, **price ≈ peg by design** — the disclaimer that it tracks off-chain reserves matters far more than rank or market cap.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FIDD |
| **Market Cap Rank** | #464 |
| **Market Cap** | $48,864,766 (~$48.86M) |
| **Current Price** | $1.00 |
| **24h Change** | -0.01% |
| **7d Change** | +0.09% |
| **Underlying / backing** | US dollar cash & money-market instruments (1:1) |
| **Issuer** | Fidelity Digital Assets, National Association (Fidelity Investments subsidiary) |
| **Yield treatment** | Pegged at ~$1.00 (price stays flat; any yield mechanics handled off-chain) |
| **Chain** | Ethereum (ERC-20) |
| **Categories** | Stablecoins, USD Stablecoin, Ethereum Ecosystem |
| **Website** | [https://www.fidelitydigitalassets.com/stablecoin](https://www.fidelitydigitalassets.com/stablecoin) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

FIDD is pegged 1:1 to the US dollar and is issued by **Fidelity Digital Assets, National Association**, a subsidiary of Fidelity Investments — one of the largest asset managers in the world. Fidelity positions the token as backed by the operational standards of its digital-assets business and the broader Fidelity franchise. Unlike the accruing-NAV products in this RWA cluster ([[midas-mtbill|mTBILL]]), FIDD holds a **constant ~$1.00 price** — a fixed-peg "digital dollar" design rather than a rising-NAV unit.

The token is a **wrapper / claim** on off-chain dollar backing held by the regulated Fidelity entity. Its on-chain price tracks that $1 backing; tight ranges around $1.00 (24h range historically ~$0.998–$1.00) reflect ordinary secondary-market arbitrage around the peg, not crypto-style volatility. Among tokenized dollars, FIDD's distinguishing feature is the **brand-name, US-regulated issuer** — a deliberate contrast to offshore stablecoins and smaller RWA wrappers.

---

## Architecture — How It Works

### Reserve / collateral model
FIDD is backed 1:1 by **US dollars and short-term, high-quality dollar instruments** — the same family of assets a money-market fund holds — held at the regulated Fidelity issuing entity ([[money-market-fund|money-market]] base). There is no fractional reserve or algorithmic component; backing is cash and cash-equivalents.

### Peg mechanism — flat $1
The token's on-chain price is held near **$1.00**; it does not accrue yield into price. Any yield economics are managed off-chain / via the issuer rather than expressed as a rising token NAV. The peg is enforced by the **1:1 primary redemption commitment** (par mint/redeem against reserves) plus secondary-market arbitrage on venues like Kraken and Uniswap V3.

### Mint / redeem & KYC gating
Primary issuance and redemption sit with **Fidelity Digital Assets, National Association** for eligible, onboarded clients, redeemable 1:1 for USD. Public source code for the contract is published (see GitHub link below), an unusual transparency choice for a brand-name issuer. Access to primary mint/redeem is institution-oriented and onboarding-gated.

### Settlement chain & contract
Issued on [[ethereum|Ethereum]] as an **ERC-20 mintable token controlled by the issuer**. The contract being mintable means supply is issuer-managed (minted on deposit, burned on redemption); it also means admin-key control is a residual risk.

### Regulatory wrapper & off-chain dependency
The issuer is a **US-domiciled, regulated national association** under the Fidelity umbrella — a materially different regulatory posture from the Bermuda/BVI wrappers used by USDO and many offshore RWA dollars. Value still depends on Fidelity's reserves, custody, and 1:1 redemption commitment; the blockchain records the claim but cannot enforce delivery of the underlying dollars.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 49.55M FIDD |
| **Total Supply** | 49.55M FIDD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $49.53M |
| **Market Cap / FDV Ratio** | 1.00 |

Supply tracks deposits and redemptions; there is no emission schedule, vesting, or speculative tokenomics. Market cap reflects dollars tokenized rather than a valuation.

---

## Comparison vs Peers

| Product | Issuer | Domicile / wrapper | Peg / yield | Distinguishing feature |
|---|---|---|---|---|
| **FIDD** (Fidelity) | Fidelity Digital Assets, N.A. | US (regulated national association) | Flat $1, yield off-chain | Brand-name US issuer; open-source contract |
| **USDC** (Circle) | Circle | US (state MTLs / MiCA) | Flat $1, no holder yield | Largest regulated fiat stablecoin |
| **USDM** (Mountain Protocol) | Mountain Protocol | Bermuda (BMA) | Rebasing $1 + yield | Yield-bearing dollar |
| **USDO** ([[openeden-open-dollar]]) | OpenEden Digital | Bermuda (BMA) | Rebasing $1 + yield | T-bill-backed rebasing |
| **BUIDL** (BlackRock/Securitize) | BlackRock / Securitize | US (Reg D / SEC) | Dividend (price varies) | Largest tokenized Treasury fund |

FIDD's closest peer in *spirit* is **USDC** (a flat $1, US-regulated, non-yield-bearing dollar from a major institution), distinguished mainly by Fidelity's bank-style national-association wrapper and asset-manager pedigree. It contrasts sharply with yield-bearing dollars (USDM, USDO), which pass through Treasury yield via rebasing.

---

## How & Where It Trades / Is Used

- **Primary market:** 1:1 mint/redeem through Fidelity Digital Assets, N.A. for eligible onboarded clients.
- **Centralized exchange:** listed on **Kraken** (FIDD/USD).
- **Decentralized exchange:** **Uniswap V3 (Ethereum)** FIDD/USDC pool — providing on-chain spot liquidity.
- **Liquidity:** notably deeper than most RWA wrappers in this cluster — CoinGecko shows ~$15.5M 24h volume, reflecting genuine venue presence rather than a held-only token.
- **Composability:** as a flat-$1 ERC-20, FIDD slots cleanly into DeFi as a settlement/collateral dollar without rebase-handling complications.

---

## Narrative / Category & Catalysts

FIDD sits in the **institutional tokenized-dollar / digital-cash** narrative — the entry of brand-name US asset managers into on-chain settlement. Drivers:
- **Institutional adoption:** Fidelity's participation signals mainstream-finance commitment to tokenized cash; growth tracks institutional on-chain settlement demand.
- **Regulatory clarity:** a defined US stablecoin regime would directly benefit a US-regulated issuer like Fidelity, potentially expanding permitted uses.
- **Competition with USDC/USDT:** FIDD competes for the "trusted regulated dollar" niche against incumbents.
- **Regime context:** as of 2026-06-22 the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **21 (Extreme Fear)** in an established bear market. Flat-$1 regulated dollars are defensive parking instruments in such regimes.

---

## History / Timeline

| Date | Event |
|---|---|
| 2026-02-04 | Both ATH ($1.01) and ATL ($0.9942) printed — minor peg deviations on a single date |
| 2026-04-09 | Captured in CoinGecko top-1000 snapshot ([[coingecko-top-1000-2026-04-09]]) |
| 2026-06-21 | Market snapshot: $1.00, market cap ~$48.86M (rank #464) |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.01 (2026-02-04) |
| **All-Time Low** | $0.9942 (2026-02-04) |
| **24h Change** | -0.01% |
| **7d Change** | +0.09% |

As a $1-pegged digital dollar, FIDD shows only minor deviations around its peg; it has essentially no crypto-market beta.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x7c135549504245b5eae64fc0e99fa5ebabb8e35d` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | FIDD/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X7C135549504245B5EAE64FC0E99FA5EBABB8E35D/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.fidelitydigitalassets.com/stablecoin](https://www.fidelitydigitalassets.com/stablecoin) |
| **Twitter** | [@digitalassets](https://twitter.com/digitalassets) |
| **GitHub** | [https://github.com/fidelity/mintable-token-ethereum-contract](https://github.com/fidelity/mintable-token-ethereum-contract) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $15.53M |
| **Market Cap Rank** | #464 |
| **24h Range** | $0.9982 — $1.00 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks

- **Depeg risk:** although tightly held near $1.00, secondary-market stress or reserve doubt could push the price off peg, as the brief $0.9942 print on 2026-02-04 illustrates.
- **NAV / reserve-gap risk:** the peg rests on Fidelity's off-chain dollar reserves and 1:1 redemption commitment. The token cannot self-collateralize on-chain; any reserve shortfall threatens the peg.
- **Redemption-gating risk:** primary 1:1 redemption is available only to eligible onboarded clients; others depend on secondary venues to exit.
- **Issuer & custodian counterparty risk:** concentrated reliance on a single regulated issuer (Fidelity Digital Assets, N.A.). Operational failure, reserve shortfall, or a redemption freeze would threaten the peg.
- **Regulatory risk:** tokenized-dollar / stablecoin-style products face active and shifting regulation; classification and permitted uses can change, and access may be jurisdiction-restricted.
- **Smart-contract risk:** the ERC-20 contract is issuer-controlled (mintable); contract bugs or admin-key compromise are residual risks (mitigated somewhat by published source code).
- **Liquidity risk:** while CEX (Kraken) and DEX (Uniswap V3) venues exist and volume is comparatively healthy, deep size may still depend on primary redemption with the issuer.

---

## Trading / Usage Playbook

- **Use as a settlement/parking dollar, not a trade.** FIDD is a flat-$1 instrument; it has no upside beyond holding par.
- **Favor it where issuer trust matters.** The US-regulated, brand-name wrapper is its core selling point versus offshore or thinly-backed dollars.
- **Arbitrage the peg if it slips.** Eligible participants can mint/redeem at par against the issuer; secondary traders can fade small deviations on Kraken/Uniswap.
- **No yield on-chain.** Unlike USDM/USDO, holding FIDD does not pass through Treasury yield to the wallet — choose accordingly if yield is the goal.

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[real-world-assets]]
- [[tokenization]]
- [[money-market-fund]]
- [[stablecoin]]
- [[openeden-open-dollar]] / [[midas-mtbill]] — peer RWA dollars/wrappers

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original listing snapshot
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific Fidelity source document ingested yet.

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 48.08M FIDD |
| **Total Supply** | 48.08M FIDD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $48.07M |
| **Market Cap / FDV Ratio** | 1.00 |

---
