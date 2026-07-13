---
title: "Sygnum FIUSD Liquidity Fund"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, real-world-assets, money-market-fund]
aliases: ["FIUSD", "Sygnum FIUSD"]
entity_type: protocol
headquarters: "Zurich, Switzerland (Sygnum Bank)"
website: "https://www.sygnum.com/"
related: ["[[crypto-markets]]", "[[real-world-assets]]", "[[tokenization]]", "[[money-market-fund]]", "[[ethereum]]"]
---

# Sygnum FIUSD Liquidity Fund

**Sygnum FIUSD Liquidity Fund** (FIUSD) is a tokenized [[real-world-assets|real-world asset]] (RWA): an on-chain wrapper representing units of an institutional **USD money-market fund**. Specifically, it tokenizes **Fidelity International's Institutional Liquidity Fund (ILF) — USD Fund, Class G Accumulating** — with **Sygnum Bank** (a regulated Swiss/Singapore digital-asset bank) acting as token issuer. The token's price tracks the per-unit NAV of that off-chain [[money-market-fund]], which is why each FIUSD trades around **$11,921** (a high unit NAV inherited from the underlying fund-share denomination, not a typical $1 stablecoin). As of 2026-06-21 it traded at **$11,921.35**, ranked **#475** by market capitalization with a market cap of **~$47.66M**.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FIUSD |
| **Market Cap Rank** | #475 |
| **Market Cap** | $47,657,504 (~$47.66M) |
| **Current Price** | $11,921.35 |
| **24h Change** | 0.00% |
| **7d Change** | +0.07% |
| **Underlying asset** | Fidelity ILF — USD Fund, Class G Acc (USD money-market fund) |
| **Issuer** | Sygnum Bank |
| **Yield treatment** | Accumulating share class — yield reflected in rising NAV |
| **Categories** | Arbitrum Ecosystem, ZkSync Ecosystem, Real World Assets (RWA) |
| **Website** | [https://www.sygnum.com/](https://www.sygnum.com/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

FIUSD tokenizes **Fidelity International's Institutional Liquidity Fund (ILF) — USD Fund, Class G Accumulating** money-market fund. **Sygnum Bank** — a regulated digital-asset bank headquartered in Zurich with a Singapore presence — is the token issuer and arranges the link between the on-chain token and the off-chain fund units.

The token is a **wrapper**: each FIUSD is a tokenized claim on units of the underlying [[money-market-fund]]. Its on-chain price therefore tracks the fund's **per-unit NAV**, not crypto supply/demand. Because the underlying is an **accumulating** ("Acc") share class, distributions are reinvested into NAV, so the unit price rises gradually over time (its all-time low of $11,251.76 on 2025-01-21 reflects an earlier, lower NAV base, not a de-peg).

FIUSD belongs to the **tokenized money-market fund / tokenized cash** branch of [[real-world-assets|real-world assets]] — a category distinct from both algorithmic and crypto-collateralized [[stablecoin|stablecoins]]. Rather than minting a new dollar unit, it puts an *existing regulated fund share* on-chain. That distinction drives everything about how it behaves: the unit price is whatever the fund administrator strikes as NAV, the yield is the fund's underlying T-bill / repo carry net of fund fees, and the holder list is gated to investors who can legally hold the underlying fund. This is the same structural template used by [[blackrock-buidl|BlackRock's BUIDL]] (tokenized via Securitize), Franklin Templeton's BENJI, and Ondo's [[ondo-finance|OUSG]] — though FIUSD differs in that it inherits the underlying fund's four-digit per-share denomination rather than re-basing to $1.00.

---

## How the token works

- **Underlying asset / backing:** Units of the Fidelity ILF USD money-market fund (a portfolio of short-term, high-quality USD instruments — T-bills, repo, commercial paper, bank deposits). Each token is backed by fund units held in the off-chain structure.
- **Yield treatment — accrual via accumulating class:** The Class G *Accumulating* share class reinvests income, so yield shows up as rising NAV per token rather than a separate payout. This explains the four-digit unit price and the slow upward drift.
- **Mint / redeem (primary market):** Issuance and redemption are **permissioned** and run by Sygnum Bank for eligible, KYC'd / onboarded clients (typically institutional and professional investors), subscribing and redeeming against fund NAV. This is not a permissionless mint.
- **Settlement chains:** Deployed on **zkSync** (native) and **Arbitrum One** (see Contract Addresses below).
- **Off-chain dependency:** Value depends on the underlying Fidelity fund, on Sygnum's custody/issuance machinery, and on the legal wrapper connecting token to fund units.

### Regulatory wrapper

FIUSD sits inside a **bank-grade regulatory perimeter**, which is its core differentiator from DeFi stablecoins. Sygnum Bank holds a Swiss banking licence (FINMA) and a Singapore capital-markets/asset-management presence (MAS), and issues the token as a **regulated securities/fund instrument** rather than an e-money or payment token. The underlying — a UCITS-style institutional money-market fund managed by Fidelity International — is itself a regulated collective-investment vehicle. Net effect: holders are exposed to the same investor-protection regime as a traditional fund share, but with on-chain transferability among whitelisted addresses. This is why mint/redeem is permissioned and KYC-gated — the token is a *regulated fund unit on rails*, not a bearer dollar.

### Yield source vs. peer designs

The yield FIUSD accrues is **pure money-market carry**: short-dated US Treasury bills, repurchase agreements, commercial paper and bank deposits held by the Fidelity ILF fund, minus fund management fees. This is the lowest-risk yield archetype among yield-bearing dollar tokens — there is no delta-neutral basis trade (as in [[ethena-usde|USDe]]), no over-collateralized crypto CDP (as in [[crvusd]] or [[dai|DAI]]), and no protocol-level leverage. The trade-off is that FIUSD's yield floats *down* one-for-one with Fed policy: in the current rate environment the carry is meaningful, but a cutting cycle compresses it directly.

---

## Comparison vs. peer yield-bearing / RWA dollar tokens

| Dimension | **FIUSD** | [[ondo-finance\|OUSG]] | BUIDL (BlackRock) | [[compounding-open-dollar\|cUSDO]] |
|---|---|---|---|---|
| **Backing** | Fidelity ILF money-market fund units (T-bills, repo, CP, deposits) | Short-term US Treasuries / BlackRock funds | Tokenized US Treasury fund (BlackRock) | US T-bills + reverse repo |
| **Issuer / wrapper** | Sygnum Bank (FINMA / MAS) | Ondo Finance | Securitize / BlackRock | OpenEden Digital (BMA-licensed) |
| **Yield mechanism** | Accumulating NAV (price drifts up) | Accumulating / rebasing variants | Daily rebase to $1 + dividend | Compounding into unit value |
| **Unit price** | ~$11,921 (inherits fund denomination) | ~$100+ | $1.00 (rebasing) | ~$1.05 |
| **Access** | Permissioned, institutional KYC | Permissioned (US/global tiers) | Permissioned, institutional | Permissioned issuance |
| **Yield archetype** | Money-market carry | Treasury carry | Treasury carry | Treasury carry |
| **Crypto-market beta** | Effectively zero | Effectively zero | Effectively zero | Effectively zero |

All four are RWA / tokenized-cash instruments with near-zero crypto beta; they compete on regulatory wrapper, distribution reach, redemption mechanics, and fee drag rather than on yield strategy (all are ultimately short-Treasury carry).

---

## Narrative, category & catalysts

FIUSD rides the **tokenized money-market / tokenized Treasury** wave — one of the few crypto narratives validated by traditional finance, with BlackRock, Franklin Templeton, Fidelity and others moving cash products on-chain. Key drivers:

- **Rates:** higher-for-longer short rates keep money-market carry attractive; a Fed cutting cycle compresses the yield FIUSD passes through. As of 2026-06-23 the broader crypto tape is in **Extreme Fear** (Fear & Greed 21, market-health 29/100, bottoming/accumulation regime), which historically *increases* demand for parked-cash RWA instruments as investors de-risk from volatile tokens into yield-bearing dollars.
- **Institutional on-chain treasury:** corporates and funds using tokenized MMFs as collateral and idle-cash management is the structural growth vector.
- **Regulatory tailwind:** clearer stablecoin/tokenized-securities frameworks across the EU (MiCA), Switzerland, Singapore and the US favour bank-issued, fully-reserved instruments like FIUSD over algorithmic designs.

---

## History & timeline

| Date | Event |
|---|---|
| 2025-01-21 | All-time low unit price of $11,251.76 recorded (lower NAV base) |
| 2026-04-08 | All-time high unit price of $11,833.96 |
| 2026-04-09 | First captured in CoinGecko top-1000 listing snapshot (Source: [[coingecko-top-1000-2026-04-09]]) |
| 2026-06-21 | Market snapshot: $11,921.35, ~$47.66M cap, rank ~#475 |

> Only dated, verifiable price/listing events are recorded above. Issuance and corporate milestones will be added as primary Sygnum sources are ingested.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 3,998 FIUSD |
| **Total Supply** | 3,998 FIUSD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $47.31M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $11,833.96 (2026-04-08) |
| **All-Time Low** | $11,251.76 (2025-01-21) |
| **24h Change** | 0.00% |
| **7d Change** | +0.07% |

The minimal volatility is expected: FIUSD tracks a money-market fund's NAV and has effectively no crypto-market beta. It drifts upward as the accumulating fund reinvests income.

---

## How & where it's used

- **Not a trading instrument.** FIUSD has effectively zero secondary on-chain volume; it is an *allocation/holding* product, not a token you scalp. Primary entry and exit are via Sygnum's permissioned subscribe/redeem at fund NAV, on the fund's dealing schedule.
- **Idle-cash and collateral management.** Its natural use is institutional treasury — parking USD on-chain to earn money-market carry while retaining the ability to move whitelisted units across zkSync / Arbitrum for settlement or as collateral within permissioned DeFi venues.
- **DeFi composability is limited** by the permissioned transfer model: only whitelisted addresses can hold it, so it does not freely compose into open AMMs or lending markets the way a permissionless yield token (e.g. [[compounding-open-dollar|cUSDO]], sDAI) can.

## Usage playbook

- **Who it's for:** onboarded institutional / professional investors wanting regulated, fully-reserved on-chain dollar exposure with money-market yield and bank-grade investor protection.
- **Hold thesis:** capture short-Treasury carry with near-zero price risk; preferable to bearer stablecoins for entities needing a regulated wrapper and fund-grade reporting.
- **Watch items:** the Fed path (yield compresses if rates fall), Sygnum issuer health, and the fund's dealing/redemption schedule. Do **not** rely on secondary on-chain liquidity for size — exit via primary redemption.

---

## Platform & Chain Information

**Native Chain:** Zksync

### Contract Addresses

| Chain | Address |
|---|---|
| Zksync | `0x2ab105a3ead22731082b790ca9a00d9a3a7627f9` |
| Arbitrum One | `0xcded6b899edba762d793f44ed295248049440e1e` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.sygnum.com/](https://www.sygnum.com/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $0.00000000 |
| **Market Cap Rank** | #476 |
| **24h Range** | $11,832.79 — $11,833.96 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks

- **Off-chain dependency:** The token is only as good as the underlying Fidelity ILF fund units and the legal structure linking them on-chain. The blockchain cannot settle the real-world fund.
- **Issuer & custody risk:** Reliance on Sygnum Bank as issuer/custodian. While Sygnum is a regulated bank, counterparty failure or operational error could impair backing.
- **Regulatory / transfer restrictions:** Permissioned, KYC-gated, and oriented to institutional/professional investors; eligibility and transferability are jurisdiction-constrained. Tokenized fund units sit in an evolving regulatory regime.
- **Liquidity risk:** Very thin secondary on-chain liquidity (24h volume near zero). Practical exits rely on primary redemption through Sygnum at NAV, on the fund's dealing schedule.
- **Underlying fund risk:** Money-market funds are low- but not zero-risk; a credit event, redemption run, or "breaking the buck" episode in the underlying would flow through to NAV.
- **Smart-contract / bridge risk:** Multi-chain (zkSync, Arbitrum) deployment adds contract and bridge attack surface.

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[real-world-assets]]
- [[tokenization]]
- [[money-market-fund]]
- [[ondo-finance]] — OUSG, peer tokenized-Treasury issuer
- [[compounding-open-dollar]] — cUSDO, peer T-bill-backed yield dollar
- [[yield-bearing-stablecoin]]
- [[stablecoin]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original listing snapshot
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific Sygnum source document ingested yet.
