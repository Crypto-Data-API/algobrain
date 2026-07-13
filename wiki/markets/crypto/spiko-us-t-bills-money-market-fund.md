---
title: "Spiko US T-Bills Money Market Fund"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, bonds, defi, treasuries]
aliases: ["USTBL", "Spiko US", "Spiko USTBL", "ustbl-tokenized-u-s-treasury-bill"]
entity_type: protocol
headquarters: "Paris, France (Spiko)"
website: "https://www.spiko.xyz"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[spiko-eu-t-bills-money-market-fund]]", "[[eutbl]]", "[[treasuries]]"]
---

# Spiko US T-Bills Money Market Fund

**Spiko US T-Bills Money Market Fund** (USTBL) is a [[tokenized-treasuries|tokenized]] EU-regulated USD money-market fund issued by Spiko (Paris, France), native on [[ethereum|Ethereum]] and deployed across Base, Polygon, Arbitrum, Starknet and Etherlink. It invests exclusively in short-dated [[treasury-bills|US Treasury Bills]] (maturities under six months, average portfolio maturity ≤ two months) and passes the [[yield]] through as a rising NAV. It is the **dollar leg** of Spiko's tokenized-MMF range; the euro counterpart is [[eutbl|EUTBL]]. As a fully licensed UCITS-style MMF accessible to retail and professional investors, USTBL is one of the most regulated retail-accessible [[real-world-assets|RWA]] cash products.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price (NAV/token)** | $1.087 — all-time high; rises with accrued T-bill interest |
| **Market cap** | $170.19M |
| **Market-cap rank** | #191 |
| **24h volume** | $49.95 (negligible — minted/redeemed with the fund, not traded) |
| **Circulating supply** | 156.58M USTBL |
| **Total supply** | 156.58M USTBL (MC/FDV = 1.00) |
| **Max supply** | None (open-ended MMF) |
| **24h change** | 0.00% |
| **7d change** | +0.05% (≈ weekly T-bill carry) |
| **All-time high** | $1.087 (2026-06-18) — ATH is structural |
| **All-time low** | $1.013 (2024-08-20) — currently +7.3% |

*Note: USTBL is an accumulating MMF NAV token — its "price" is compounded short-term [[treasury-bills|T-bill]] yield, not market discovery, so flat 24h moves and an ever-rising ATH are normal. Macro backdrop: [[crypto-fear-and-greed-index|Fear & Greed]] 23 ("Established Bear Market") — uncorrelated to crypto risk sentiment; bear regimes tend to *increase* demand for regulated on-chain cash parking.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USTBL |
| **Issuer** | Spiko (Paris, France); fund approved by the French Financial Markets Authority (AMF) |
| **Market Cap Rank** | #191 (2026-06-20) |
| **Market Cap** | $170.19M |
| **Current Price** | $1.087 (NAV-accruing) |
| **Underlying assets** | Exclusively short-dated [[treasury-bills|US Treasury Bills]] (<6mo maturity, avg ≤2mo) |
| **Wrapper** | EU-regulated money-market fund (UCITS-style), retail + professional access |
| **Categories** | Tokenized Assets, [[real-world-assets|Real World Assets (RWA)]], Tokenized Treasury Bills, Polygon / Arbitrum / Base / Starknet / Etherlink / [[ethereum|Ethereum]] Ecosystems |
| **Website** | [https://www.spiko.xyz](https://www.spiko.xyz) |

---

## Overview

The Spiko US T-Bills Money Market Fund is a fully licensed USD money market fund operating under the EU regulatory framework. The fund exclusively invests in [[treasury-bills|United States Treasury Bills]] with maturities of less than six months, maintaining an average portfolio maturity of no more than two months. Approved by the French Financial Markets Authority (AMF), the Spiko US T-Bills Money Market Fund is accessible to all types of investors, both professional and non-professional — a notable contrast with permissioned, qualified-purchaser-only products like [[ousg|OUSG]] and [[hashnote-usyc|USYC]].

---

## Mechanism & Backing

| Dimension | Detail |
|---|---|
| **Underlying assets** | 100% short-dated [[treasury-bills|US Treasury Bills]] (<6 months), average portfolio maturity ≤ 2 months — among the lowest-risk, most liquid instruments available |
| **Yield source** | The short-term US T-bill rate, passed through by **NAV accrual** (the token price drifts up rather than paying a coupon). Realized return tracks the prevailing T-bill [[yield]] net of fund fees (qualitative — not a fixed APY) |
| **Wrapper** | A fully licensed EU money-market fund regulated by the French **AMF** — holders own regulated fund units, with fund-level investor protections rather than a bare note |
| **Custody** | Fund assets held by regulated custodians under the MMF framework; the token is the on-chain share class |
| **Redemption** | Subscribe/redeem directly with Spiko; no reliance on a secondary order book (24h on-chain volume ≈ $0) |
| **KYC / permissioning** | Open to all investor types (retail + professional) subject to Spiko KYC — broader access than US qualified-purchaser products |
| **Regulatory wrapper** | EU MMF regime + AMF approval; this is a securities/fund product, **not** a payment [[stablecoins|stablecoin]] |

> **Not a stablecoin:** USTBL is a yield-bearing MMF NAV token — its price rises with accrued interest. Compare pegged, no-yield [[stablecoins]] ([[first-digital-usd|FDUSD]], [[global-dollar|USDG]]) vs accumulating yield products (USTBL, [[ousg|OUSG]], [[ondo-us-dollar-yield|USDY]], [[hashnote-usyc|USYC]]).

---

## Tokenomics

See the **Market Data** block above for the authoritative snapshot (2026-06-20: 156.58M USTBL, $1.087, $170.19M mcap, MC/FDV = 1.00). Structural notes:

- **Open-ended MMF**: no max supply; tokens mint on subscription and burn on redemption, so float tracks net AUM.
- **NAV-accrual price**: every fresh print is an all-time high; ATL $1.013 (2024-08-20) reflects the early NAV base.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xe4880249745eac5f1ed9d8f7df844792d560e750` |
| Base | `0xe4880249745eac5f1ed9d8f7df844792d560e750` |
| Etherlink | `0xe4880249745eac5f1ed9d8f7df844792d560e750` |
| Polygon Pos | `0xe4880249745eac5f1ed9d8f7df844792d560e750` |
| Arbitrum One | `0x021289588cd81dc1ac87ea91e91607eef68303f5` |
| Starknet | `0x20ff2f6021ada9edbceaf31b96f9f67b746662a6e6b2bc9d30c0d3e290a71f6` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.spiko.xyz](https://www.spiko.xyz) |
| **GitHub** | [https://github.com/spiko-tech/contracts](https://github.com/spiko-tech/contracts) |
| **Whitepaper** | [https://docs.spiko.io/documentation/intro/welcome](https://docs.spiko.io/documentation/intro/welcome) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 13 |
| **GitHub Forks** | 2 |
| **Pull Requests Merged** | 48 |
| **Contributors** | 6 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $49.95 (negligible — fund subscription/redemption, not order-book trading) |
| **Market Cap Rank** | #191 |
| **24h Range** | $1.087 — $1.087 |
| **Last Updated** | 2026-06-20 |

> USTBL is **not a trading vehicle** — secondary on-chain volume is effectively zero by design. Exposure is gained by subscribing to the fund (USD/stablecoin in) and exited by redeeming. The token's value comes from accrued [[treasury-bills|T-bill]] [[yield]], not price action.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Relevance

- **Narrative basket**: [[real-world-assets]] / tokenized treasuries — the fastest-growing institutional crypto vertical of 2024–2026. USTBL is Spiko's **dollar-yield** leg; [[eutbl|EUTBL]] (Spiko EU T-Bills MMF) is the euro counterpart. As of 2025–2026 combined Spiko funds (USTBL + EUTBL) passed the **$1B AUM** mark.
- **Use for traders**: on-chain dollar cash parking with T-bill yield — a yield-bearing alternative to non-interest-bearing USD stablecoins; usable as a treasury asset and increasingly as DeFi collateral.
- **Macro angle**: NAV growth tracks short-term US T-bill yields; an accumulating-NAV instrument (price drifts up with yield rather than paying a coupon).

---

## Peer Comparison — tokenized US Treasury / MMF products

| Product | Issuer | Wrapper | Access | Size (2026-06-20) | Regulatory anchor |
|---|---|---|---|---|---|
| **USTBL** | Spiko | EU MMF (UCITS-style) | **Retail + professional** | $170M (#191) | French AMF / EU MMF |
| [[eutbl|EUTBL]] | Spiko | EU MMF (EUR T-bills) | Retail + professional | $941M (#70) | French AMF / EU MMF |
| [[ousg|OUSG]] | [[ondo-finance|Ondo]] | Fund (T-bills via [[blackrock|BUIDL]]) | Qualified purchasers | $479M (#106) | US securities |
| [[ondo-us-dollar-yield|USDY]] | Ondo | Note | Non-US general access | $2.16B (#42) | Non-US |
| [[hashnote-usyc|USYC]] | [[circle|Circle]]/Hashnote | MMF (T-bills + repo) | Institutional | $3.07B (#31) | Cayman fund |

> USTBL's edge is **regulated retail access in the EU**: it is one of the few tokenized T-bill products an ordinary (non-qualified, non-institutional) investor can hold. Combined Spiko AUM (USTBL + EUTBL ≈ $1.1B by mid-2026) puts it firmly in the second tier of the tokenized-Treasury complex.

---

## Risks

- **Issuer / platform concentration**: USTBL depends entirely on Spiko's operations, smart contracts, and continued AMF authorization — there is no second operator.
- **Regulatory risk**: sits at the intersection of the EU MMF framework, [[mica|MiCA]], and tokenized-securities rules; framework changes could constrain tokenization, access, or redemption.
- **Redemption-gate tail risk**: like all money-market funds, USTBL can in extremis impose redemption gates or fees under MMF liquidity rules — the standard MMF run risk, on-chain.
- **Custodial risk**: fund assets sit with regulated custodians; the chain is token → fund → custodian → T-bills, and a break anywhere up that chain is the exposure.
- **Liquidity risk**: effectively zero secondary market — all exits are fund redemptions, fine in calm markets but capacity-constrained in stress.
- **Multi-chain / smart-contract risk**: deployed across six chains (Ethereum, Base, Polygon, Arbitrum, Starknet, Etherlink), multiplying contract surface.
- **Rates risk**: NAV accrual falls with Fed/T-bill rate cuts, compressing the yield advantage over zero-yield [[stablecoins]].

> **Ticker-collision note:** A separate, unrelated tokenized T-bill product — **NexBridge USTBL** (website nexbridge.io; CoinGecko id `ustbl-tokenized-u-s-treasury-bill`, a much smaller ~$32M / rank #615 token in the snapshot) — also trades under the ticker "USTBL". The NexBridge product is issued and settled on the **Liquid Network** (a Bitcoin layer) / Ordinals, is backed by real US Treasuries verified monthly by Grant Thornton, holds an "A" rating from Particula, and embeds its yield within the token (no staking required); it is the first in a line of regulated digital assets from NexBridge. It is **not** the Spiko fund — the two share only a ticker.

## See Also / Related

- [[eutbl]] / [[spiko-eu-t-bills-money-market-fund]] — sister euro fund (EUTBL)
- [[real-world-assets]] — sector page
- [[treasuries]]
- [[crypto-markets]]
- [[ethereum]] — primary issuance chain

---

## Sources

- CoinGecko / cryptodataapi.com market snapshot, 2026-06-20 ($170.19M mcap, rank #191, $1.087 NAV); earlier baseline (Source: [[coingecko-top-1000-2026-04-09]])
- Spiko docs — https://docs.spiko.io/documentation/intro/welcome
- Web verification, 2026-06-11 (NexBridge USTBL distinguished from Spiko USTBL; NexBridge RID — https://www.ustbl.io/RID/rid.pdf)
