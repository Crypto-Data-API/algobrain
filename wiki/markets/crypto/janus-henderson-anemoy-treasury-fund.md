---
title: "Janus Henderson Anemoy Treasury Fund"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, treasuries]
aliases: ["Anemoy LTF", "Anemoy Liquid Treasury Fund", "JTRSY"]
entity_type: protocol
founded: 2024
headquarters: "British Virgin Islands (fund); Centrifuge protocol"
website: "https://www.anemoy.io/funds/jtrsy"
related: ["[[blackrock-usd-institutional-digital-liquidity-fund]]", "[[centrifuge]]", "[[crypto-markets]]", "[[ethereum]]", "[[ondo-finance]]", "[[ondo-us-dollar-yield]]", "[[real-world-assets]]", "[[tokenized-treasuries]]", "[[treasury-bills]]"]
---

# Janus Henderson Anemoy Treasury Fund

**Janus Henderson Anemoy Treasury Fund** (JTRSY) is a tokenized BVI professional fund holding **0–3 month US [[treasury-bills|Treasury bills]]**, issued on-chain via the [[centrifuge|Centrifuge]] protocol with Janus Henderson as sub-investment manager — one of the largest [[tokenized-treasuries|tokenized-Treasury]] funds (~$0.87B, mid-2026), competing directly with [[blackrock-usd-institutional-digital-liquidity-fund|BlackRock's BUIDL]] and [[ondo-finance|Ondo's]] [[ousg|OUSG]]. It is significant to traders not as a tradable token (it has essentially zero secondary volume) but as institutional **on-chain cash-management infrastructure** and a barometer of TradFi adoption of the [[real-world-assets|RWA]] sector.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price (accruing NAV)** | $1.11 |
| **Market cap (= AUM on-chain)** | $868.7M |
| **Market-cap rank** | #75 |
| **24h volume** | $0 (subscribed/redeemed at NAV; no secondary market) |
| **24h / 7d change** | +0.04% / +0.09% (yield accrual) |
| **Circulating / total supply** | 784.57M JTRSY |
| **Max supply** | None (mint/redeem at NAV) |
| **All-time high** | $1.11 (2026-06-19 — NAV makes new highs as yield accrues) |
| **All-time low** | $1.085 (2025-11-13) |

Unlike a stablecoin, JTRSY is a **NAV-accrual** token: the unit price drifts steadily upward (now $1.11) as the underlying T-bill yield compounds, so "ATH" is set roughly daily and price has no peg. The relevant figure is **supply × price ≈ AUM (~$869M)**; 24h volume is $0 because shares are subscribed/redeemed at NAV by whitelisted professional investors, not traded. RWA.xyz showed ~$871M total value in June 2026, consistent with this snapshot. Macro backdrop: "Established Bear Market", Fear & Greed ~23.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | JTRSY |
| **AUM / Market Cap** | ~$869M (CoinGecko, June 2026 snapshot, rank #75); ~$871M per rwa.xyz (June 2026) — figures fluctuate with institutional subscriptions/redemptions |
| **Structure** | BVI professional fund, licensed by the BVI Financial Services Commission; non-US Professional Investors only |
| **Holdings** | Short-term US T-bills, 0–3 month remaining maturity (minimal duration risk) |
| **Fees** | 0.25% management fee, 0% performance fee |
| **Token standard** | ERC-7540 (async extension of ERC-4626), issuing ERC-20 fund shares |
| **Chains** | Ethereum, Base, Arbitrum, Avalanche, Plume, and others |
| **Manager** | Anemoy (Centrifuge's web3-native asset manager); Janus Henderson sub-investment manager since 2024 |
| **Website** | [https://www.anemoy.io/funds/jtrsy](https://www.anemoy.io/funds/jtrsy) |

---

## Overview

Anemoy is a Web3-native asset manager powered by Centrifuge, offering investors access to real-world-asset investment opportunities. The fund launched in 2024 as the **Anemoy Liquid Treasury Fund (LTF)**; Janus Henderson — the $380B+ traditional asset manager — became sub-investment manager in 2024, and the fund was renamed **Janus Henderson Anemoy Treasury Fund (JTRSY)** in February 2025 to reflect the deepening partnership. It was an early recipient of a top tokenized-fund rating (announced via Janus Henderson press release).

The fund invests solely in short-term US T-bills (0–3 months remaining maturity), minimizing price and duration risk. Share issuance follows ERC-7540 (an async extension of ERC-4626), with fund shares held as ERC-20 tokens on the investor's chain of choice.

Anemoy's broader tokenized-fund suite includes:

1. Janus Henderson Anemoy Treasury Fund (JTRSY)
2. Janus Henderson Anemoy AAA CLO Fund (JAAA on-chain)
3. Anemoy Tokenized Apollo Diversified Credit Fund
4. Janus Henderson Anemoy S&P 500® Fund

## Mechanism & Backing

| Dimension | JTRSY design |
|---|---|
| **Underlying assets** | Short-term US [[treasury-bills|Treasury bills]], 0–3 month remaining maturity — minimal duration and interest-rate risk; effectively sovereign credit |
| **Regulatory wrapper** | BVI professional fund, licensed by the BVI Financial Services Commission; offered only to non-US **Professional Investors** (not retail, not US persons) |
| **Yield source / NAV** | Income from the T-bill ladder accrues into NAV; the token is a **NAV-accrual share** (unit price rises ~daily) rather than a flat-$1 stablecoin. Net yield ≈ short T-bill rate minus the 0.25% management fee (0% performance fee) — qualitative, varies with rates |
| **Token standard** | ERC-7540 (async extension of ERC-4626), issuing ERC-20 fund shares; async mint/redeem suits T+ settlement of the underlying |
| **Manager** | Anemoy (Centrifuge's web3-native asset manager); **Janus Henderson** ($380B+ TradFi house) as sub-investment manager from 2024 |
| **Custody / settlement** | Issued via the [[centrifuge|Centrifuge]] protocol; subscription/redemption at NAV vs USDC for whitelisted investors |
| **KYC / permissioning** | Whitelist-gated; transfers restricted to onboarded professional investors. No free DEX circulation |

This is the same broad architecture as other institutional [[tokenized-treasuries]] ([[blackrock-usd-institutional-digital-liquidity-fund|BUIDL]], [[ousg|OUSG]], BENJI) — the key differentiators are the Centrifuge issuance rail, the ERC-7540 standard, and the Janus Henderson + Anemoy management pairing.

## 2025–2026 Developments

- **February 2025**: renamed from Anemoy LTF to JTRSY as Janus Henderson took the headline role.
- **2025–2026**: grew into the top tier of tokenized Treasury funds (~$0.9–1.3B), alongside BlackRock's BUIDL, Ondo OUSG, and Franklin Templeton's BENJI — collectively the institutional backbone of the tokenized-Treasury market.
- **May 2026**: derivatives exchange **Grvt integrated Centrifuge yields** (including JTRSY exposure) into its wealth platform — an example of tokenized T-bill funds becoming yield-bearing collateral on trading venues.
- Expanded multi-chain footprint (Ethereum, Base, Arbitrum, Avalanche, Plume).

## Trading Relevance

- **Not a trading vehicle**: JTRSY has effectively **zero secondary-market volume** ($0 24h volume at the June 2026 snapshot); shares are subscribed/redeemed at NAV by whitelisted professional investors. Its "price" (~$1.11) is accruing NAV, not a market price.
- **Why it still matters to traders**:
  - **RWA-sector barometer**: JTRSY AUM growth vs. BUIDL/OUSG is a direct read on institutional tokenization adoption — the fundamental driver behind the RWA [[narrative-trading]] basket (ONDO, CFG, PLUME, etc.).
  - **Centrifuge (CFG) proxy**: JTRSY is Centrifuge's flagship product; its growth is a fundamental input for trading CFG.
  - **Collateralization trend**: integrations like Grvt (May 2026) point to tokenized T-bills replacing stablecoins as exchange margin — a structural shift worth tracking for funding/basis traders.
- **Comparable instruments**: [[ondo-us-dollar-yield|USDY]] (retail-accessible, freely transferable note) vs JTRSY (professional-investor fund shares); BlackRock BUIDL (largest, Securitize-issued).

---

## Peer Comparison — institutional tokenized Treasury funds

| Fund | Issuer / platform | Underlying | NAV model | Investor base | Approx. size |
|---|---|---|---|---|---|
| **JTRSY** | Anemoy / [[centrifuge|Centrifuge]] (Janus Henderson sub-manager) | 0–3m T-bills | NAV-accrual ($1.11) | Non-US pro investors | ~$869M (#75) |
| [[blackrock-usd-institutional-digital-liquidity-fund|BUIDL]] | BlackRock / [[securitize|Securitize]] | T-bills, cash, repo | Flat $1.00, yield as new tokens | Qualified purchasers | ~$2.38B (#40) |
| [[hashnote-usyc|USYC]] | Circle | T-bills / reverse repo | NAV-accrual | Permissioned | ~$2.9B (#1) |
| [[ousg|OUSG]] | Ondo Finance | Holds BUIDL/MMFs | NAV-accrual | Permissioned | Large |
| [[eutbl|EUTBL]] | Spiko | EUR-zone T-bills | NAV-accrual (EUR) | KYC retail+inst. | ~$0.94B (#70) |

JTRSY's niche is being a **professional-investor**, multi-chain, Centrifuge-issued T-bill fund with a recognized TradFi sub-manager — sized in the second tier behind BUIDL/USYC but ahead of most pure-DeFi RWA products.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x8c213ee79581ff4984583c6a801e5263418c4b86` |
| Base | `0x8c213ee79581ff4984583c6a801e5263418c4b86` |
| Plume Network | `0xa5d465251fbcc907f5dd6bb2145488dfc6a2627b` |
| Avalanche | `0xa5d465251fbcc907f5dd6bb2145488dfc6a2627b` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.anemoy.io/](https://www.anemoy.io/) |
| **Twitter** | [@anemoycapital](https://twitter.com/anemoycapital) |
| **GitHub** | [https://github.com/centrifuge](https://github.com/centrifuge) |

---

## Risks

| Risk | Assessment |
|---|---|
| **Issuer / manager** | Low–moderate — Janus Henderson is a major TradFi manager, but the legal issuer is a BVI fund operated via the Anemoy/Centrifuge stack, a thinner operational base than BlackRock/BNY Mellon |
| **Underlying credit / duration** | Low — 0–3 month US T-bills; sovereign credit, negligible duration |
| **Smart-contract / protocol** | Moderate — reliance on Centrifuge contracts and ERC-7540 async-vault logic across multiple chains; bridge and contract risk |
| **Regulatory** | Moderate — BVI professional-fund wrapper; cross-border treatment of tokenized fund shares still evolving; explicitly excludes US persons |
| **Liquidity / redemption** | Moderate — par redemption depends on T-bill liquidity and the async subscription/redemption cycle; no secondary market to exit through |
| **Concentration** | Single-platform (Centrifuge) issuance; AUM sensitive to a small number of institutional allocators |

---

## Related

- [[centrifuge]]
- [[real-world-assets]], [[tokenized-treasuries]], [[treasury-bills]]
- [[blackrock-usd-institutional-digital-liquidity-fund]] — peer (BUIDL)
- [[ousg]] — peer (Ondo OUSG)
- [[eutbl]] — peer (euro T-bill fund)
- [[ondo-finance]]
- [[ondo-us-dollar-yield]]
- [[crypto-markets]]
- [[ethereum]]
- [[narrative-trading]]

---

## Sources

- Anemoy — JTRSY fund page: https://www.anemoy.io/funds/jtrsy (0–3 month T-bills, 0.25% fee, BVI FSC licence, ERC-7540)
- RWA.xyz — JTRSY asset page: https://app.rwa.xyz/assets/JTRSY (~$871M total value, June 2026)
- Janus Henderson — "Janus Henderson Anemoy Treasury Fund Receives Highest Tokenized Fund Rating": https://www.janushenderson.com/en-us/advisor/press-releases/janus-henderson-anemoy-treasury-fund-receives-highest-tokenized-fund-rating/
- Invezz (2026-05-14) — Grvt expands wealth platform with Centrifuge yield integration: https://invezz.com/news/2026/05/14/grvt-expands-wealth-platform-with-centrifuge-yield-integration/
- Etherscan — JTRSY token contract: https://etherscan.io/token/0x8c213ee79581ff4984583c6a801e5263418c4b86
- Web verification, 2026-06-10: AUM, structure, renaming history confirmed.
- (Source: [[coingecko-top-1000-2026-04-09]])

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 782.79M JTRSY |
| **Total Supply** | 782.79M JTRSY |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $868.61M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.11 (2026-07-15) |
| **Current vs ATH** | +0.00% |
| **All-Time Low** | $1.08 (2025-11-13) |
| **Current vs ATL** | +2.29% |
| **24h Change** | +0.01% |
| **7d Change** | +0.07% |
| **30d Change** | +0.28% |
| **1y Change** | +0.00% |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $0.00000000 |
| **Market Cap Rank** | #73 |
| **24h Range** | $1.11 — $1.11 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
