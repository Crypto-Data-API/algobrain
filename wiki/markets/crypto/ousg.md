---
title: "OUSG"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, bonds, treasuries, defi]
aliases: ["OUSG", "Ondo Short-Term US Government Treasuries"]
entity_type: protocol
founded: 2023
headquarters: "Decentralized (issuer: Ondo Finance, New York)"
website: "https://ondo.finance/ousg"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[solana]]", "[[real-world-assets]]", "[[blackrock]]"]
---

# OUSG

**OUSG** (Ondo Short-Term US Government Treasuries) is a [[tokenized-treasuries|tokenized short-term US Treasuries]] fund issued by [[ondo-finance|Ondo Finance]] (ticker OUSG; native on [[ethereum|Ethereum]], also Solana/Polygon/Ondo Chain), one of the founding products of the [[real-world-assets|real-world-asset (RWA)]] tokenization sector. It gives KYC'd qualified investors on-chain exposure to the "risk-free" [[treasury-bills|T-bill]] rate, with the bulk of the portfolio now held via institutional money-market funds including [[blackrock|BlackRock]]'s BUIDL. For traders, OUSG is not a speculation vehicle (its NAV accretes at roughly the T-bill [[yield]]) but a key barometer of institutional RWA adoption and the on-chain cash-management stack.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price (NAV/token)** | $115.61 — all-time high; rises monotonically as yield accrues |
| **Market cap** | $479.13M |
| **Market-cap rank** | #106 |
| **24h volume** | $0 (transfer-restricted; no open secondary market — by design) |
| **Circulating supply** | 4.14M OUSG |
| **Total supply** | 4.14M OUSG |
| **Max supply** | None (open-ended fund) |
| **24h change** | 0.00% |
| **7d change** | +0.06% (≈ weekly T-bill carry) |
| **All-time high** | $115.61 (2026-06-18) — ATH is structural by construction |
| **All-time low** | $95.09 (2023-03-22) — currently +21.6% |

*Note: token market cap ($479M, down from ~$666M at the April 2026 snapshot as float contracted to 4.14M tokens) measures only the OUSG token directly; Ondo reports much larger underlying AUM (>$1.1B by late 2025) across the OUSG/BUIDL stack. The "price" of an [[real-world-assets|RWA]] NAV token is not a market-driven quote — it tracks accrued [[treasury-bills|Treasury]] interest, so a near-zero 24h move and an ever-rising ATH are normal. Macro backdrop: [[crypto-fear-and-greed-index|Fear & Greed]] 23 ("Established Bear Market") — OUSG is uncorrelated to crypto risk sentiment; if anything, bear regimes increase demand for on-chain cash parking.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | OUSG |
| **Market Cap Rank** | #106 (token mcap $479.13M, 2026-06-20) |
| **AUM / TVL** | >$1.1B underlying AUM reported by late 2025; $479M token market cap at 2026-06-20 (down from ~$666M at the April snapshot) — figures vary by tracker depending on whether they count the token or full fund AUM |
| **Underlying assets** | Majority held in [[blackrock|BlackRock]]'s tokenized MMF **BUIDL** (formerly iShares SHV ETF), plus small USDC/USD liquidity sleeve; all short-dated US government paper |
| **Sector** | [[real-world-assets|Real World Assets (RWA)]], [[tokenized-treasuries|Tokenized Treasuries]] |
| **Chains** | [[ethereum|Ethereum]] (native), Solana, Polygon; Ondo Chain (Ondo's institutional L1, launched by 2026) |
| **Supply mechanics** | Open-ended fund; supply expands/contracts with subscriptions and redemptions; NAV/token accretes with [[yield]] (no max supply) |
| **Access** | KYC/AML-gated; qualified purchasers only; transfer-restricted token |
| **Redemption** | Instant mint/redeem in USDC directly with Ondo (no order-book exit) |
| **Website** | [https://ondo.finance/ousg](https://ondo.finance/ousg) |

---

## Overview

OUSG is a tokenized short-term US Treasuries fund, overseen and managed by Ondo Capital Management, a subsidiary of Ondo Finance. Originally the significant majority of the portfolio was held in the iShares Short Treasury Bond ETF (NASDAQ: SHV); the portfolio has since migrated so that the majority of assets sit in BlackRock's tokenized money-market fund **BUIDL**, alongside a small portion of USDC and USD for liquidity purposes.

OUSG brought exposure to the US Treasury rate on-chain for the first time (subscriptions opened early 2023). It delivers a stable, predictable return with deep liquidity, investing only in instruments backed by secure, stable, liquid securities of the kind the world's largest institutions hold.

OUSG was developed alongside two other fund tokens, OSTB and OHYG, by Ondo Finance, a DeFi software development firm founded by ex-Goldman Sachs staff. Ondo launched in August 2021; its first product was Ondo Vaults, a structured-finance protocol on Ethereum, followed by Liquidity-as-a-Service (LaaS) facilitating over $210M in liquidity. As DeFi yields compressed in 2022, Ondo sunset Vaults and LaaS ("Ondo V1") and announced Ondo V2 — the tokenized funds — in January 2023 (Nathan Allman).

**What OUSG is used for:** investors who pass KYC/AML screening and sign subscription documents hold tokens representing fund ownership; tokens can be transferred between whitelisted investors and composed into smart-contract arrangements (lending, collateral). Transfer restrictions ensure tokens cannot reach non-qualified holders.

---

## Mechanism & Backing

| Dimension | Detail |
|---|---|
| **Underlying assets** | Short-dated US government securities, the majority now held via [[blackrock|BlackRock]]'s tokenized money-market fund **BUIDL** (originally the iShares Short Treasury Bond ETF, SHV), with a small USDC/USD sleeve for instant redemption liquidity |
| **Yield source** | The "risk-free" short-term [[treasury-bills|US T-bill]] rate (front of the curve), net of fund fees. OUSG passes this through by **NAV accrual** — the token's price grinds upward rather than paying a coupon — so the realized return tracks the prevailing T-bill [[yield]] (qualitative; do not assume a fixed APY) |
| **Custody** | Fund assets held with institutional custodians; BUIDL itself is administered within BlackRock/Securitize infrastructure. OUSG is structured as fund-ownership tokens, not a debt note |
| **Redemption** | Instant mint/redeem against USDC directly with [[ondo-finance|Ondo]]; no reliance on a secondary order book |
| **KYC / permissioning** | KYC/AML-gated, qualified-purchasers only; the token is transfer-restricted to a whitelist, so it cannot reach retail or non-qualified holders. This is the key contrast with Ondo's general-access [[ondo-us-dollar-yield|USDY]] note |
| **Regulatory wrapper** | Managed by Ondo Capital Management (Ondo Finance subsidiary); marketed as a securities offering to qualified purchasers, distinct from a payment [[stablecoins|stablecoin]] |

> **Why it is not a stablecoin:** OUSG is a yield-bearing fund token whose NAV rises with accrued interest, not a $1-pegged payment instrument. Compare [[first-digital-usd|FDUSD]]/[[global-dollar|USDG]] (pegged, no yield to holder) vs OUSG/USDY/[[hashnote-usyc|USYC]] (NAV-accruing, yield-bearing).

---

## Major News & Events (2025-2026)

- **2025-09** — Ondo launched **Ondo Global Markets**, extending tokenization from Treasuries to US stocks and ETFs; by October 2025 it held ~$320M TVL as the tokenized-securities market doubled to nearly $700M.
- **Late 2025** — OUSG TVL surpassed **$1.1B**; BlackRock's BUIDL became the dominant underlying holding.
- **By 2026** — Ondo launched **Ondo Chain**, a Layer 1 optimized for institutional tokenized assets, and partnered with State Street and Galaxy Asset Management on a $200M-seeded tokenized fund ("SWEEP") slated for 2026.
- Chain footprint expanded across Ethereum, Solana and Polygon (sister product USDY also on Mantle, Sui, Aptos).

---

## Tokenomics

See the **Market Data** block above for the authoritative supply/price/market-cap snapshot (2026-06-20: 4.14M OUSG, $115.61/token, $479.13M mcap, MC/FDV = 1.00). Structural notes:

- **Open-ended fund**: no max supply; tokens mint on subscription and burn on redemption, so float (4.14M tokens, down from 5.80M in April 2026) tracks net qualified-investor demand.
- **NAV-accrual price**: by construction every fresh print is an all-time high; "price history" is just compounded T-bill carry, not market discovery.
- **1y change** ≈ short-term [[treasury-bills|Treasury]] yield net of fees (a few percent), with ATL $95.09 (2023-03-22) reflecting the early NAV base.

---

## Platform & Chain Information

**Native Chain:** Ethereum

| Chain | Address |
|---|---|
| Ethereum | `0x1b19c19393e2d034d8ff31ff34c81252fcbbee92` |
| Solana | `i7u4r16TcsJTgq1kAG8opmVZyVnAKBwLKu6ZPMwzxNc` |
| Polygon PoS | `0xba11c5effa33c4d6f8f593cfa394241cfe925811` |

---

## Exchange Listings

OUSG does not trade on open exchanges — it is a transfer-restricted security minted/redeemed directly with Ondo (instant mint/redeem in USDC). Secondary trading is effectively nil ($0 24h volume at the April 2026 snapshot). This is by design.

---

## Trading Relevance

- **Not a directional trade**: OUSG returns ≈ T-bill yield; there is no upside beta. Its relevance is as **infrastructure and signal**, not as a position.
- **RWA sector barometer**: OUSG TVL growth (with BUIDL, BENJI, and Figure's [[ylds|YLDS]]) tracks institutional adoption of tokenized cash — the key input for the RWA narrative basket that drives tokens like ONDO (Ondo's governance token, a separate, freely traded asset).
- **On-chain rates signal**: when DeFi-native yields fall below the OUSG/T-bill rate, capital rotates out of DeFi lending into tokenized Treasuries; the spread between on-chain stablecoin lending rates and the OUSG yield is a risk-appetite indicator.
- **Collateral layer**: OUSG/BUIDL-style assets are increasingly accepted as derivatives-margin collateral at institutional venues — a structural change to crypto market plumbing worth tracking.

---

## Peer Comparison — tokenized US Treasury / MMF products

| Product | Issuer | Underlying | Access | Size (2026-06-20) | Notes |
|---|---|---|---|---|---|
| **OUSG** | [[ondo-finance|Ondo]] | T-bills via [[blackrock|BUIDL]] | Qualified purchasers (permissioned) | $479M token mcap (#106) | Instant USDC mint/redeem |
| [[ondo-us-dollar-yield|USDY]] | Ondo | T-bills + bank deposits | Non-US, general access | $2.16B (#42) | Retail-accessible note, not a fund |
| [[hashnote-usyc|USYC]] | [[circle|Circle]]/Hashnote | T-bills + repo | Institutional (permissioned) | $3.07B (#31) | Largest tokenized Treasury; derivatives collateral |
| BUIDL | [[blackrock|BlackRock]]/Securitize | T-bills + repo | Institutional | multi-$B | OUSG's main underlying holding |
| BENJI | Franklin Templeton | Gov MMF | Broad | ~$1B+ | Regulated US MMF on-chain |
| [[spiko-us-t-bills-money-market-fund|USTBL]] | Spiko | T-bills (EU MMF wrapper) | All investors (EU) | $170M (#191) | EU-regulated, retail-accessible |

---

## Risks

- **Issuer / manager risk**: OUSG depends on [[ondo-finance|Ondo]] (Ondo Capital Management) and, transitively, on [[blackrock|BlackRock]]/Securitize for the BUIDL underlying. Operational failure or mismanagement at either layer is a direct holder risk.
- **Custodial risk**: fund assets sit with institutional custodians; OUSG is a claim on a fund, so the chain is token → fund → custodian → underlying T-bills. A break anywhere up that chain is the exposure.
- **Regulatory risk**: tokenized securities sit in evolving US/global frameworks; OUSG mitigates by gating to qualified purchasers and restricting transfers, but rule changes could constrain access, composability, or redemption.
- **Liquidity risk**: there is **no secondary market** ($0 24h volume). All exits are redemptions in USDC with Ondo — fast in normal conditions, but redemption capacity is the binding constraint in stress, not an order book.
- **Smart-contract / chain risk**: multi-chain deployment (Ethereum, Solana, Polygon, Ondo Chain) adds bridge and contract surface.
- **Rates risk**: NAV accrual tracks the front end of the curve; aggressive Fed cuts compress the yield and the relative appeal versus zero-yield [[stablecoins]].

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ondo.finance/](https://ondo.finance/) |
| **Twitter** | [@OndoFinance](https://twitter.com/ondofinance) |
| **Discord** | [https://discord.com/invite/YzhZaFbB92](https://discord.com/invite/YzhZaFbB92) |
| **GitHub** | [https://github.com/ondoprotocol/tokenized-funds](https://github.com/ondoprotocol/tokenized-funds) |
| **Docs** | [https://docs.ondo.finance/qualified-access-products/ousg](https://docs.ondo.finance/qualified-access-products/ousg) |

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[solana]]
- [[real-world-assets]]
- [[blackrock]]
- [[ylds]]
- [[stablecoins]]
- [[treasuries]]

---

## Sources

- CoinGecko / cryptodataapi.com market snapshot, 2026-06-20 (price/supply/market-cap baseline); earlier baseline (Source: [[coingecko-top-1000-2026-04-09]])
- Ondo Finance — OUSG product page: https://ondo.finance/ousg
- Ondo Finance docs — OUSG overview: https://docs.ondo.finance/qualified-access-products/ousg/overview
- RWA.xyz — OUSG asset tracker: https://app.rwa.xyz/assets/OUSG
- CCN — How Ondo Finance turns US Treasuries into yield tokens: https://www.ccn.com/education/crypto/ondo-finance-tokenized-us-treasuries-ousg-usdy/
- Stablecoin Insider — Top 10 tokenized treasury funds 2026: https://stablecoininsider.org/top-10-tokenized-treasury-funds-in-2026-buidl-benji-and-the-highest-yielding-on-chain-options/
- Web verification, 2026-06-10.
