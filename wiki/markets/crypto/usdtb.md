---
title: "USDtb"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi]
aliases: ["USDTB", "Ethena USDtb"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://usdtb.money/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[ethena]]", "[[ethena-usde]]", "[[stablecoins]]", "[[blackrock-usd-institutional-digital-liquidity-fund]]", "[[tokenized-treasuries]]", "[[genius-act]]"]
---

# USDtb

**USDtb** (ticker **USDTB**) is [[ethena|Ethena]]'s fully-reserved, fiat/treasury-backed [[stablecoin]], launched in December 2024 on [[ethereum|Ethereum]] and [[solana|Solana]] with the majority of reserves held in [[blackrock|BlackRock]]'s tokenized money-market fund [[blackrock-usd-institutional-digital-liquidity-fund|BUIDL]] — at launch the highest BUIDL allocation of any stablecoin (~90%). Its landmark moment came in 2025 when **Anchorage Digital began issuing USDtb in the US, making it the first stablecoin compliant with the [[genius-act|GENIUS Act]]** — a fact that matters to traders as a template for how offshore stablecoins onshore under US federal regulation. Within the Ethena system it also acts as the safety valve: USDe backing rotates into USDtb when perp [[funding-rate|funding]] turns negative.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | USDTB |
| **Current Price** | $0.999761 |
| **Market Cap** | $916.5M |
| **Market Cap Rank** | #72 |
| **24h Volume** | $2.64M |
| **24h Change** | -0.01% |
| **7d Change** | -0.01% |
| **Circulating Supply** | ~916.7M USDTB |
| **Total Supply** | ~916.7M USDTB (MC/FDV = 1.00) |
| **Max Supply** | Uncapped (mint/redeem against reserves) |
| **All-Time High** | $1.057 (2025-09-20), -5.42% from ATH |
| **All-Time Low** | $0.9005 (2025-07-17) |

USDtb holds peg tightly (~$0.9998) with ~$2.6M daily secondary volume — most of its turnover is direct mint/redeem and exchange-collateral use rather than spot trading. Supply (~$917M) sits near the top of its mid-2026 range; rising USDtb share of Ethena's backing remains a clean read on weak/negative perp funding. Macro backdrop: **Established Bear Market**, Crypto [[fear-and-greed-index|Fear & Greed Index]] ≈ 23 (extreme fear) as of 2026-06-21 — peg-stable instruments like USDtb are unaffected directionally but see flight-to-quality inflows in such regimes.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDTB |
| **Type** | Fiat/treasury-backed USD stablecoin (contrast with sister token [[ethena-usde|USDe]], which is synthetic/delta-neutral) |
| **Issuer** | Ethena Labs (offshore); Anchorage Digital Bank (US, GENIUS-compliant issuance since 2025) |
| **Reserves** | Predominantly BlackRock/Securitize BUIDL tokenized money-market fund + cash equivalents |
| **Chains** | Ethereum (native) and Solana |
| **Supply** | ~$917M (CoinGecko, 2026-06-21). ~$866M at the April 2026 wiki snapshot; ~$1.5B at the July 2025 US announcement; sources have varied $0.6–1.05B through mid-2026 |
| **Rank tier** | Top-10 stablecoin by supply; ~#72 overall (2026-06-21) |
| **Website** | [https://usdtb.money/](https://usdtb.money/) |

---

## Overview

USDtb shares characteristics with existing fiat stablecoins such as [[usdc|USDC]] or [[usdt|USDT]], seeking to maintain a stable value pegged to the US dollar by utilizing cash or cash-equivalent reserves. Users are able to transfer USDtb freely and without restriction. USDtb is able to scale without practical constraints given the use of BlackRock's BUIDL as the primary reserve asset, representing the vast majority (~90% at launch) of the overall reserves — the highest BUIDL allocation of any stablecoin.

Strategically, USDtb is Ethena's hedge: when sustained negative funding rates make USDe's delta-neutral basis trade unprofitable, Ethena can rotate USDe's backing into USDtb, making it a structural "insurance policy" for the larger synthetic dollar (it crossed $1B supply in 2025 partly on this role plus exchange-collateral demand).

---

## Major News & Events

- **Dec 2024 — Launch** with BlackRock BUIDL as primary reserve asset.
- **July 2025 — GENIUS Act + Anchorage.** Days after the GENIUS Act (the US federal stablecoin law requiring 1:1 reserves and federal oversight) was signed in July 2025, Ethena announced that **Anchorage Digital Bank** — the only federally chartered crypto bank — would issue the then-**$1.5B** USDtb in the US, making it the **first GENIUS-compliant, federally regulated stablecoin** (CoinDesk, The Block, 2025-07-24).
- **Nov 2025 — Rewards.** Anchorage Digital announced plans to pay "rewards" on Ethena tokens under the GENIUS Act framework (CoinDesk, 2025-11-25).
- **2025 — $1B supply milestone** crossed; supply has since oscillated roughly in the $0.6–1.05B range into mid-2026.

---

## Trading Relevance

- **Not a directional trade** — it is a $1-pegged instrument; the trade-relevant angles are peg deviations, the regulatory template, and what its supply implies about the Ethena complex.
- **Ethena system signal:** rising USDtb share of USDe backing signals negative/weak perp funding — a direct read on the crowded basis trade that drives [[ethena-usde|sUSDe]] yield. Watch USDtb supply on DefiLlama/RWA.xyz as a funding-regime indicator.
- **Regulatory bellwether:** as the first GENIUS-compliant stablecoin, USDtb's onshore growth is a leading indicator for the tokenized-treasury/RWA basket ([[superstate-short-duration-us-government-securities-fund-ustb|USTB]], [[ondo-finance|Ondo]], BUIDL).
- **Peg history:** brief dislocations to $0.90 (2025-07-17) and $1.06 (2025-09-20) on thin venue liquidity — mean-reversion opportunities only for those with mint/redeem access; ~$4M daily volume means secondary-market liquidity is thin.
- **Venues:** primarily minted/redeemed directly and used as collateral; no major CEX spot listings in the April 2026 CoinGecko snapshot.

---

## Mechanism & Backing

USDtb is a **fully-reserved, fiat/treasury-backed** stablecoin — structurally the opposite of its sister token [[ethena-usde|USDe]] (a delta-neutral synthetic dollar). The peg is held 1:1 by reserves rather than by a basis trade:

- **Reserves** — predominantly [[blackrock|BlackRock]]/Securitize [[blackrock-usd-institutional-digital-liquidity-fund|BUIDL]] (a tokenized money-market fund holding US Treasuries and repo), ~90% at launch, plus cash equivalents. This makes USDtb effectively a wrapper on [[tokenized-treasuries|tokenized Treasuries]], scalable without the perp-funding dependency that constrains USDe.
- **Mint / redeem** — whitelisted participants mint and redeem 1:1 against reserves; USDtb is freely transferable for holders.
- **Custody & issuance** — offshore issuance via Ethena Labs; US issuance via **Anchorage Digital Bank**, the only federally chartered crypto bank, under the GENIUS-Act framework (since 2025).
- **System role** — within Ethena, USDtb is the negative-funding hedge: when sustained negative [[funding-rate|funding rates]] make USDe's basis trade unprofitable, backing rotates into USDtb. It is therefore a structural "insurance policy" for the larger synthetic dollar.

**KYC / regulatory.** US issuance is GENIUS-compliant (1:1 reserves, federal oversight, no issuer-paid yield on the payment stablecoin itself); Anchorage announced plans to pay "rewards" on Ethena tokens within that framework (CoinDesk, 2025-11-25). USDtb is the regulatory bellwether for how offshore stablecoins onshore under US law.

---

## Tokenomics

| Metric | Value (2026-06-21) |
|---|---|
| **Circulating Supply** | ~916.7M USDTB |
| **Total Supply** | ~916.7M USDTB |
| **Max Supply** | Unlimited (mint/redeem against reserves) |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.057 (2025-09-20) |
| **All-Time Low** | $0.9005 (2025-07-17) |
| **Market cap** | $916.5M (#72, 2026-06-21) |
| **24h Volume** | $2.64M (2026-06-21) |

---

## Peer Comparison — Reserve-Backed & Synthetic Dollars

| Token | Issuer | Backing model | US-regulated | Notes |
|---|---|---|---|---|
| **USDtb** (this page) | Ethena / Anchorage | Fiat + BUIDL T-bills | Yes (GENIUS) | First GENIUS-compliant stablecoin |
| [[ethena-usde|USDe]] | [[ethena|Ethena]] | Delta-neutral basis | No | USDtb is its negative-funding hedge |
| [[usdc|USDC]] | Circle | Cash + T-bills | Yes | Largest regulated fiat stablecoin |
| [[ripple-usd|RLUSD]] | Ripple (Std. Custody) | Cash + T-bills | Yes (NYDFS) | Payments/institutional focus |
| [[falcon-finance|USDf]] | Falcon Finance | Overcollateralized crypto + RWA | fUSD only | Broader, higher-variance collateral |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xc139190f447e929f090edeb554d95abb8b18ac1c` |
| Solana | `8yXrtJ54jZtE84xEBzTESKuegjcAkAuDrdAhRd8i8n3T` |

---

## Risks

- **De-peg / liquidity risk** — brief dislocations to $0.90 (2025-07-17) and $1.06 (2025-09-20) on thin venue liquidity; secondary markets are shallow (~$2.6M/day), so size requires mint/redeem access.
- **Reserve / custodial risk** — concentration in BUIDL ties USDtb's credit to BlackRock/Securitize and the underlying Treasuries; custodial dependency on Anchorage and Ethena's operational stack.
- **System-contagion risk** — as Ethena's funding hedge, USDtb is correlated to the health of the broader Ethena complex; stress in USDe's basis trade is exactly when USDtb backing scales up.
- **Regulatory risk** — though GENIUS-compliant in the US, the offshore Ethena issuance and any "rewards" features remain subject to evolving stablecoin rules.
- **Smart-contract risk** — mint/redeem and bridge contracts across Ethereum and Solana are an attack surface.

---

## Related

- [[ethena]] — issuer (ENA governance token)
- [[ethena-usde]] — sister synthetic dollar; USDtb is its negative-funding hedge
- [[stablecoins]] / [[stablecoin]] / [[usdc]] / [[usdt]] — competitive set
- [[falcon-finance]] — overcollateralized synthetic-dollar peer
- [[genius-act]] — regulatory framework USDtb pioneered compliance under
- [[blackrock-usd-institutional-digital-liquidity-fund]] — primary reserve asset
- [[tokenized-treasuries]] — underlying asset class of the reserves
- [[superstate-short-duration-us-government-securities-fund-ustb]] — adjacent tokenized-treasury product
- [[crypto-markets]], [[ethereum]], [[solana]]

---

## Sources

- CoinGecko top-1000 snapshot, 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- CoinDesk (2025-07-24): Ethena taps Anchorage to issue $1.5B USDtb under GENIUS Act — https://www.coindesk.com/business/2025/07/24/ethena-taps-anchorage-to-issue-usd1-5b-usdtb-stablecoin-in-u-s-under-genius-act
- The Block: Anchorage Digital to issue first GENIUS-compliant stablecoin with Ethena Labs — https://www.theblock.co/post/364119/anchorage-digital-genius-stablecoin-ethena
- Anchorage Digital announcement — https://www.anchorage.com/insights/anchorage-digital-partners-with-ethena-labs-to-launch-first-genius-compliant-federally-regulated-stablecoin
- CoinDesk (2025-11-25): Anchorage to pay rewards on Ethena tokens — https://www.coindesk.com/business/2025/11/25/anchorage-digital-aims-to-pay-rewards-on-ethena-s-tokens-under-genius-act
- Supply data: RWA.xyz (https://app.rwa.xyz/assets/USDtb), DefiLlama (https://defillama.com/stablecoin/ethena-usdtb), CoinMarketCap — checked 2026-06-10
- Verified via Perplexity sonar + web search, 2026-06-10.
