---
title: "Circle USYC"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, ethereum, treasuries, defi]
aliases: ["USYC", "Hashnote USYC", "Hashnote International Short Duration Yield Fund"]
entity_type: protocol
founded: 2023
headquarters: "Cayman Islands (fund); issuer owned by Circle, USA"
website: "https://usyc.hashnote.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[circle]]", "[[blackrock-usd-institutional-digital-liquidity-fund]]", "[[tokenized-treasuries]]"]
---

# Circle USYC

**Circle USYC** (USYC) is a [[tokenized-treasuries|tokenized money market fund]] — the on-chain share class of the Hashnote International Short Duration Yield Fund, which holds short-term [[treasury-bills|U.S. Treasury bills]] and runs repo/reverse-repo. Native on [[ethereum|Ethereum]] (also BNB Chain and Solana). [[circle|Circle]] (issuer of [[usdc|USDC]]) acquired Hashnote and USYC on 2025-01-21 alongside a strategic partnership with trading firm DRW/Cumberland. By mid-2026 USYC had become the **largest [[tokenized-treasuries|tokenized U.S. Treasury]] product**, at roughly **$3.07B market cap (rank #31, 2026-06-20)** — overtaking [[blackrock-usd-institutional-digital-liquidity-fund|BlackRock's BUIDL]] — driven primarily by its use as **yield-bearing collateral for institutional crypto derivatives trading**.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price (NAV/token)** | $1.13 — NAV-accruing; rises with compounded short-rate yield |
| **Market cap** | $3.07B |
| **Market-cap rank** | #31 |
| **24h volume** | ~$0.56M (negligible — permissioned; subscription/redemption, not order-book) |
| **Circulating supply** | 2.723B USYC |
| **Total supply** | 2.723B USYC (MC/FDV = 1.00) |
| **Max supply** | None (mints/burns with fund subscriptions) |
| **All-time high** | $1.13 (2026-05-30) |
| **All-time low** | $1.026 (2024-12-05) — currently +9.7% |

*Note: USYC is a NAV-accrual token — its "price" is compounded front-end [[treasury-bills|T-bill]] yield, not market discovery; 24h price/volume fields are sparse on trackers because it is permissioned and barely trades on the open market. Supply has grown from ~2.39B / $2.68B (rank #37) at the April 2026 snapshot to ~2.72B / $3.07B (rank #31) by 2026-06-20. Macro backdrop: [[crypto-fear-and-greed-index|Fear & Greed]] 23 ("Established Bear Market") — uncorrelated to crypto risk sentiment; USYC growth tracks institutional collateral demand, not the price tape.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USYC |
| **Type** | [[tokenized-treasuries|Tokenized money market fund]] ([[real-world-assets|RWA]] / tokenized T-bills) — NAV-accruing token, price slowly rises with yield |
| **AUM / Market Cap** | $3.07B at rank #31 (CoinGecko, 2026-06-20); ~$2.9B (RWA.xyz, 2026-06-09); ~$2.68B / rank #37 at the April 2026 snapshot |
| **Sector rank** | #1 tokenized Treasury product by AUM (June 2026), in a tokenized-Treasury market of ~$14.8B total |
| **Issuer** | Hashnote (acquired by [[circle|Circle]], Jan 2025) |
| **Underlying assets** | Short-term [[treasury-bills|U.S. Treasury Bills]] + repo/reverse-repo (Hashnote International Short Duration Yield Fund Ltd., Cayman) |
| **Chains** | [[ethereum|Ethereum]] (native), BNB Chain, Solana, plus Circle-supported expansion |
| **Yield mechanism** | Accrues short-term Fed-rate returns via T-bills + repo; redeemable near-instantly to/from [[usdc|USDC]] |
| **Access** | Permissioned / institutional — no retail spot listings |
| **Categories** | Tokenized Assets, [[real-world-assets|Real World Assets (RWA)]], Tokenized Treasury Bills (T-Bills) |
| **Website** | [https://usyc.hashnote.com/](https://usyc.hashnote.com/) |

---

## Overview

USYC is the on-chain representation of the Hashnote International Short Duration Yield Fund Ltd., which invests in short-term U.S. Treasury Bills and performs repo/reverse-repo activities as the underlying asset of the USYC token. USYC earns short-term Fed-rate returns; tokenization enables rapid (near-instant) subscription/redemption against USDC, on-chain transparency, and composability while maintaining regulatory and credit controls.

It is a **NAV token**, not a [[stablecoins|stablecoin]]: the price grinds upward as yield accrues (from ~$1.03 in late 2024 to ~$1.13 by mid-2026), so "price action" is essentially the compounded [[treasury-bills|T-bill]] yield.

---

## Mechanism & Backing

| Dimension | Detail |
|---|---|
| **Underlying assets** | Short-term [[treasury-bills|U.S. Treasury Bills]] plus repo/reverse-repo, held in the Hashnote International Short Duration Yield Fund Ltd. (Cayman Islands) |
| **Yield source** | Front-end U.S. rate (Fed-rate-linked T-bill + repo income), passed through by **NAV accrual** — the token price compounds upward rather than paying a coupon. Realized return tracks the prevailing short rate net of fees (qualitative — not a fixed APY) |
| **Wrapper** | An offshore (Cayman) money-market-style fund; USYC is the on-chain share class. Now [[circle|Circle]]-owned, paired with [[usdc|USDC]] convertibility |
| **Custody** | Fund assets held with institutional custodians; the on-chain token represents fund ownership |
| **Redemption** | Near-instant subscription/redemption against [[usdc|USDC]] — the USDC convertibility is the feature that makes USYC usable as fast-cycling collateral |
| **KYC / permissioning** | **Permissioned, institutional only** — no retail spot listings; access via Circle/Hashnote subscription and institutional custody integrations (e.g. Binance institutional / BNB Chain) |
| **Regulatory wrapper** | Cayman fund structure; marketed to institutions, distinct from a payment stablecoin and from US-registered MMFs |

> **Not a stablecoin:** USYC is a yield-bearing fund token whose NAV rises with accrued interest. Compare pegged, no-yield [[stablecoins]] ([[first-digital-usd|FDUSD]], [[global-dollar|USDG]]) vs accumulating yield tokens (USYC, [[ousg|OUSG]], [[ondo-us-dollar-yield|USDY]]).

### 2025–2026 developments

- **2025-01-21** — Circle announced the acquisition of Hashnote and USYC; USYC had **$1.52B deployed** as of 2025-01-15 (Circle press release). The deal paired USYC with USDC convertibility and a DRW/Cumberland distribution partnership.
- **2025–2026** — USYC adopted as **off-exchange / institutional derivatives collateral**, most notably on **Binance / BNB Chain**, letting institutions post yield-bearing T-bill exposure as margin instead of idle stablecoins. This collateral use is credited as the main growth driver.
- **H1 2026** — USYC overtook BUIDL to become the largest tokenized Treasury fund (~$2.2B in early 2026 reports, **$3.07B / rank #31 by 2026-06-20**), in a tokenized U.S. Treasury market that crossed **$14.79B total value (2026-06-09, RWA.xyz)**.

---

## Trading Relevance

- **Not a trading vehicle itself** — negligible volatility (24h volume ~$0.5M in spot terms). Its relevance is **structural**: it is the benchmark "on-chain risk-free rate" instrument.
- **Collateral plumbing signal**: growth in USYC supply is a direct read on institutional appetite for yield-bearing margin on derivatives venues (Binance institutional, prime brokers). Rapid USYC mints often accompany rising institutional open interest.
- **RWA narrative basket**: USYC, [[blackrock-usd-institutional-digital-liquidity-fund|BUIDL]], Ondo USDY/OUSG, Franklin BENJI form the tokenized-Treasury complex — the leading [[narrative-trading]] basket for the RWA theme. Tradable proxies for the theme are tokens like ONDO, since USYC itself is permissioned.
- **Rates exposure**: USYC yield tracks the front end of the U.S. curve; Fed cuts compress its carry advantage versus zero-yield stablecoins and can slow inflows.

---

## Tokenomics

See the **Market Data** block above for the authoritative snapshot (2026-06-20: 2.723B USYC, $1.13/token, $3.07B mcap, rank #31, MC/FDV = 1.00). Structural notes:

- **Supply tracks AUM**: no max supply; tokens mint/burn with fund subscriptions, so USYC float is a direct read on institutional collateral demand (~2.39B in April 2026 → ~2.72B by 2026-06-20).
- **NAV-accrual price**: ATH $1.13 (2026-05-30), ATL $1.026 (2024-12-05); the ~+3–4% 1y "return" is just compounded short-rate yield, not capital appreciation.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x136471a34f6ef19fe571effc1ca711fdb8e49f2b` |
| Binance Smart Chain | `0x8d0fa28f221eb5735bc71d3a0da67ee5bc821311` |
| Solana | `7LWanZteUKtvFjv4MHYgKXXdAuCQYFPJysL9pxxdRQGn` |

---

## Exchange Listings

USYC is a **permissioned institutional product** — no retail spot listings. Access is via Circle/Hashnote subscription (USDC in/out) and it is held as collateral at institutional venues (Binance institutional / BNB Chain custody integrations).

---

## Peer Comparison — tokenized US Treasury / MMF products

| Product | Issuer | Wrapper | Access | Size (2026-06-20) | Distinguishing use |
|---|---|---|---|---|---|
| **USYC** | [[circle|Circle]]/Hashnote | Cayman MMF (T-bills + repo) | Institutional | **$3.07B (#31)** | Derivatives margin / collateral |
| [[blackrock-usd-institutional-digital-liquidity-fund|BUIDL]] | [[blackrock|BlackRock]]/Securitize | US fund (T-bills + repo) | Institutional | multi-$B | Former #1; OUSG's underlying |
| [[ondo-us-dollar-yield|USDY]] | [[ondo-finance|Ondo]] | Note | Non-US general access | $2.16B (#42) | Retail-accessible yield dollar |
| [[ousg|OUSG]] | Ondo | Fund (via BUIDL) | Qualified purchasers | $479M (#106) | Composable on-chain cash |
| [[spiko-us-t-bills-money-market-fund|USTBL]] | Spiko | EU MMF | Retail + professional (EU) | $170M (#191) | EU-regulated retail access |

> USYC's moat is **collateral utility**: its near-instant [[usdc|USDC]] convertibility and acceptance as off-exchange margin on institutional venues (Binance institutional / BNB Chain) let funds post yield-bearing T-bill exposure instead of idle stablecoins — the mechanical reason it overtook BUIDL.

---

## Risks

- **Issuer / acquirer risk**: USYC now sits inside [[circle|Circle]] (post-Jan-2025 Hashnote acquisition); holder fortunes are tied to Circle's solvency, the DRW/Cumberland partnership, and continued operation of the Cayman fund.
- **Custodial risk**: fund assets held with institutional custodians; the chain is token → Cayman fund → custodian → T-bills/repo. Repo counterparty risk is an added layer vs a pure T-bill fund.
- **Regulatory risk**: a Cayman fund marketed to institutions; cross-border tokenized-securities and stablecoin rules ([[genius-act|GENIUS Act]], [[mica|MiCA]]) could constrain its structure or US-facing distribution.
- **Collateral-cascade risk**: because USYC is widely used as derivatives margin, a redemption stress or NAV question could propagate into forced deleveraging on the venues that accept it — a systemic, not idiosyncratic, exposure.
- **Liquidity risk**: permissioned, near-zero secondary volume — all exits are USDC redemptions; redemption capacity is the binding constraint in stress.
- **Rates risk**: NAV accrual tracks the front of the U.S. curve; Fed cuts compress its carry advantage over zero-yield [[stablecoins]] and can slow inflows.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://usyc.hashnote.com/](https://usyc.hashnote.com/) |
| **Docs** | [Circle developers — USYC overview](https://developers.circle.com/tokenized/usyc/overview) |
| **Twitter** | [@Hashnote_Labs](https://twitter.com/Hashnote_Labs) |

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[circle]] / [[usdc]]
- [[blackrock-usd-institutional-digital-liquidity-fund]] — chief competitor (BUIDL)
- [[tether-gold]] — fellow RWA/tokenized-asset product
- [[narrative-trading]] — RWA basket
- [[binance]]

---

## Sources

- Circle press release, "Circle Announces Acquisition of Hashnote and USYC" (2025-01-21) — https://www.circle.com/pressroom/circle-announces-acquisition-of-hashnote-and-usyc-tokenized-money-market-fund-alongside-strategic-partnership-with-global-trading-firm-drw
- RWA.xyz tokenized Treasuries dashboard (snapshot 2026-06-09) — https://app.rwa.xyz/treasuries
- The Defiant, "Circle USYC largest T-bill fund, $2.9 billion" (2026) — https://thedefiant.io/converge/cefi/circle-usyc-largest-t-bill-fund-2-9-billion-cxpol7
- Phemex News, "Circle's USYC becomes largest tokenized US Treasury product at $2.2 billion" — https://phemex.com/news/article/circles-usyc-becomes-largest-tokenized-us-treasury-product-at-22-billion-66374
- CryptoSlate, "BlackRock just lost control of the $10B tokenized treasury market to Circle" (Jan 2026) — https://cryptoslate.com/blackrock-just-lost-control-of-the-10b-tokenized-treasury-market-to-circle-for-one-simple-mechanical-reason/
- CoinGecko / cryptodataapi.com market snapshot, 2026-06-20 ($3.07B mcap, rank #31, $1.13 NAV); earlier baseline CoinGecko top-1000 (2026-04-09)
- Verified via Perplexity sonar, 2026-06-10
