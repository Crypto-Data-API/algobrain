---
title: "YLDS"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, regulation, treasuries, stablecoin]
aliases: ["YLDS", "Figure YLDS"]
entity_type: protocol
founded: 2025
headquarters: "Issuer: Figure Certificate Corp (Figure Technology Solutions), San Francisco, USA"
website: "https://www.figuremarkets.com/c/ylds"
related: ["[[crypto-markets]]", "[[solana]]", "[[stablecoins]]", "[[stablecoin]]", "[[real-world-assets]]", "[[tokenized-treasuries]]", "[[ousg]]", "[[yield]]"]
---

# YLDS

**YLDS** is the first **SEC-registered, yield-bearing [[stablecoin]]** — a USD-pegged digital certificate issued by Figure Certificate Corp (a Figure Markets/Figure Technology Solutions subsidiary) that pays **SOFR minus 0.50%**, accrued daily and paid monthly. Launched February 2025 on the Provenance blockchain, it is a landmark for the regulated-stablecoin/[[real-world-assets|RWA]] sector: a stablecoin that is legally a public security, transferable peer-to-peer, and now deployed across Provenance, [[solana]] and Stellar. Its issuer's parent, Figure Technology Solutions, trades on Nasdaq as **FIGR**.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price** | $0.9997 (tight ±10bp peg; yield delivered via accrual, not price) |
| **Market cap (= supply at par)** | $574.9M |
| **Market-cap rank** | #93 |
| **24h volume** | $2.74M |
| **24h / 7d change** | −0.01% / −0.01% |
| **Circulating / total supply** | 575.05M YLDS |
| **Max supply** | None (open-ended; mint/redeem at $1) |
| **All-time high** | $1.001 (2026-02-13) |
| **All-time low** | $0.9992 (2025-11-16) |

YLDS holds a tight dollar peg by design — unlike NAV-accrual [[tokenized-treasuries]], its **yield is paid out (SOFR − 50bp) rather than capitalized into price**, so the unit price stays ≈$1.00. Supply moves with net subscriptions/redemptions: ~575M at this snapshot, down modestly from ~616M at the April 2026 snapshot; market cap ≈ supply at par. Macro backdrop: "Established Bear Market", Fear & Greed ~23 — a regime in which demand for on-chain cash-yield instruments tends to hold up.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | YLDS |
| **Market Cap Rank** | #93 (~$575M cap, June 2026 snapshot; was ~$616M at the April 2026 snapshot) |
| **Sector** | Yield-bearing stablecoin, RWA, regulated security |
| **Chains** | Provenance (native), Solana (Nov 2025), Stellar (2026-05-05) |
| **Yield** | SOFR − 0.50%, accrues daily, paid monthly in USD or YLDS |
| **Backing** | Securities similar to prime money-market fund holdings |
| **Regulatory status** | SEC-registered public security (Reg A-style registration via Figure Certificate Corp) |
| **Supply mechanics** | Open-ended; mint/redeem at $1; no max supply |
| **Website** | [https://www.figuremarkets.com/c/ylds](https://www.figuremarkets.com/c/ylds) |

> Earlier snapshot (2026-04-09, CoinGecko): rank #88, market cap $615.58M, price $0.9998. Current data in the [[#Market Data]] block above.

---

## Overview

YLDS originated from the need Figure Markets saw for a USD-pegged digital asset that inherently accrues interest, is fully transferable, and has the regulatory clarity of a registered security. Each YLDS is a transferable digital certificate backed by investments similar to those of a prime money market fund.

Timeline:

- **2025-02** — Launched as the industry's first yield-bearing stablecoin registered with the SEC as a public security, native to the Provenance blockchain. Fixed $1 price, daily yield accrual, available to individuals and institutions; transferable peer-to-peer (a key difference from money-market funds and from non-yield stablecoins under the US stablecoin regime, which prohibits interest on payment stablecoins — YLDS sidesteps this by being a registered security).
- **2025-09** — Parent Figure Technology Solutions completed its Nasdaq IPO (ticker **FIGR**), giving the issuer a publicly audited balance sheet.
- **2025-11** — Expanded to [[solana]].
- **2026-05-05** — Live on **Stellar**, its third network — the first deployment of a regulated yield-bearing dollar product on that chain.

---

## Mechanism & Backing

| Dimension | YLDS design |
|---|---|
| **Instrument type** | A **registered public security** (a digital "certificate"), not a payment stablecoin — issued by Figure Certificate Corp and registered with the SEC. This is the legal hook that lets it pay interest |
| **Backing** | Investments similar to a **prime money-market fund** — short-dated, high-grade instruments held by the issuer; each YLDS represents a $1 certificate claim |
| **Yield source** | **SOFR − 0.50%**, accrued daily, paid monthly in USD or in YLDS. Yield flows from the underlying MMF-style portfolio; holder receives a distribution rather than NAV drift |
| **Peg** | Fixed $1.00 unit; mint/redeem at par via Figure Markets. Peg stability comes from short, liquid, high-grade backing plus par redeemability |
| **Regulatory wrapper** | SEC-registered (Reg A-style registration via Figure Certificate Corp); this sidesteps the GENIUS-era US rule that bars *payment-stablecoin* issuers from paying interest |
| **Custody / issuer balance sheet** | Issuer's parent Figure Technology Solutions is Nasdaq-listed (FIGR), giving a publicly audited balance sheet behind the franchise |
| **Transferability** | Peer-to-peer transferable on-chain — a key advantage over money-market-fund shares, which generally are not |

The two compliant routes for yield to reach on-chain dollars are the **registered-security route (YLDS)** and the **tokenized-MMF route** ([[ousg|OUSG]], [[blackrock-usd-institutional-digital-liquidity-fund|BUIDL]]). YLDS is the cleanest example of the former.

---

## Peer Comparison — yield-bearing on-chain dollars

| Product | Issuer | Legal form | Peg / NAV | Yield to holder | Approx. size |
|---|---|---|---|---|---|
| **YLDS** | Figure Certificate Corp | SEC-registered security | Flat $1.00 | SOFR − 0.50%, distributed | ~$575M (#93) |
| [[ousg|OUSG]] | Ondo Finance | Tokenized MMF (security) | NAV-accrual | T-bill yield in NAV | Large |
| [[blackrock-usd-institutional-digital-liquidity-fund|BUIDL]] | BlackRock / [[securitize|Securitize]] | Tokenized MMF (security) | Flat $1.00, yield as tokens | T-bill yield | ~$2.38B (#40) |
| [[usx|eUSX]] / [[ethena|USDe]] | Solstice / Ethena | DeFi yield wrapper | ≈$1.00 | Strategy/funding yield | Varies |
| [[usdc|USDC]] / [[usdt|USDT]] | Circle / Tether | Payment stablecoin | Flat $1.00 | **None to holder** | #1–2 |

YLDS's distinguishing feature is being the first to deliver **interest legally to retail holders** via the registered-security route, while remaining peer-to-peer transferable — a combination payment stablecoins (barred from paying interest) and most MMF shares (not freely transferable) cannot match.

---

## Platform & Chain Information

**Native Chain:** Provenance

| Chain | Address |
|---|---|
| Provenance | `uylds.fcc` |
| Solana | (deployed Nov 2025) |
| Stellar | (deployed 2026-05-05) |

---

## Exchange Listings

YLDS is purchased and redeemed via Figure Markets (USD or stablecoin funding) rather than traded on major third-party exchanges; secondary venue support is limited (~$2.7M daily volume at the June 2026 snapshot). It is a cash-management instrument, not a trading vehicle.

---

## Trading Relevance

- **Not a directional asset** — relevance is structural: YLDS is the regulated template for *interest-bearing* dollars on-chain. Because the GENIUS-era US stablecoin rules bar payment-stablecoin issuers from paying interest, the registered-security route (YLDS) and tokenized-MMF route ([[ousg|OUSG]]/BUIDL) are the two compliant ways yield reaches on-chain dollars — watch which wins flows.
- **Rates proxy**: YLDS yield = SOFR − 50bp; its supply growth is a clean read on demand for on-chain cash parking when DeFi yields compress.
- **Equity kicker**: issuer parent trades as **FIGR** on Nasdaq — a TradFi instrument whose price embeds the market's view on Figure's on-chain lending/stablecoin franchise; FIGR is the tradable expression of the YLDS thesis.
- **Catalysts**: new chain deployments (Stellar was May 2026), integrations into exchanges as collateral, and US regulatory treatment of yield-bearing stablecoins.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.figuremarkets.com/c/ylds](https://www.figuremarkets.com/c/ylds) |
| **Issuer** | Figure Technology Solutions (Nasdaq: FIGR) |
| **SEC filing** | https://www.sec.gov/Archives/edgar/data/1974395/000149315225018198/form497.htm |

---

## Risks

| Risk | Assessment |
|---|---|
| **Issuer / credit** | Moderate — backing is MMF-style high-grade paper; the registered-security wrapper gives disclosure, and parent FIGR is a publicly audited Nasdaq company, but it is a single-issuer franchise |
| **Yield / rates** | Distribution = SOFR − 50bp; falls automatically as the Fed cuts. A low-rate regime erodes the value proposition vs DeFi yields |
| **Regulatory** | Moderate — pioneering legal structure; treatment of yield-bearing on-chain dollars (vs the GENIUS payment-stablecoin regime) is still being tested |
| **Smart-contract / multichain** | Moderate — live on Provenance, [[solana|Solana]] and Stellar; each deployment adds contract/bridge surface |
| **Liquidity** | Thin secondary venues; primary mint/redeem via Figure Markets is the real exit path |
| **De-peg** | Low — short, liquid, high-grade backing + par redemption; peg has stayed within ±10bp since launch |

---

## Related

- [[crypto-markets]]
- [[stablecoins]], [[stablecoin]]
- [[ousg]], [[blackrock-usd-institutional-digital-liquidity-fund]] — tokenized-MMF route to on-chain yield
- [[real-world-assets]], [[tokenized-treasuries]], [[yield]]
- [[solana]]
- [[treasuries]]
- [[regulation]]

---

## Sources

- CoinGecko top-1000 snapshot, 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- Markets Media — Figure Markets launches first SEC-registered yield-bearing stablecoin (Feb 2025): https://www.marketsmedia.com/figure-markets-launches-first-sec-registered-yield-bearing-stablecoin/
- PR Newswire — Figure Markets YLDS launch release: https://www.prnewswire.com/news-releases/figure-markets-launched-industry-first-yield-bearing-stablecoin-as-an-sec-registered-public-security-302381466.html
- Stellar.org — Figure announces launch of YLDS on Stellar (2026-05-05): https://stellar.org/press/figure-announces-launch-of-ylds-on-stellar-network
- The Defiant — Figure YLDS launches on Stellar: https://thedefiant.io/news/defi/figure-ylds-launches-on-stellar
- SEC EDGAR — YLDS form 497: https://www.sec.gov/Archives/edgar/data/1974395/000149315225018198/form497.htm
- Verified via Perplexity (sonar), 2026-06-10.
