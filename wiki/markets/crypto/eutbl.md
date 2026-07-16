---
title: "Spiko EU T-Bills Money Market Fund"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bonds, crypto, defi]
aliases: ["EUTBL", "Spiko EUTBL", "Spiko Euro"]
entity_type: protocol
founded: 2023
headquarters: "Paris, France (Spiko)"
website: "https://www.spiko.io"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[spiko-us-t-bills-money-market-fund]]", "[[tokenized-treasuries]]", "[[treasuries]]", "[[treasury-bills]]"]
---

# Spiko EU T-Bills Money Market Fund

**Spiko EU T-Bills Money Market Fund** (EUTBL) is a tokenized, fully-licensed **euro money market fund** — an AMF-regulated French short-term VNAV MMF (sub-fund of the Spiko SICAV) whose shares live on-chain as transferable tokens across seven networks. It invests exclusively in [[treasury-bills|T-bills]] of investment-grade Eurozone states (<6-month maturity, average portfolio maturity <2 months), making EUTBL the leading on-chain euro cash-yield instrument and the euro counterpart to Spiko's [[spiko-us-t-bills-money-market-fund|USTBL]]. It is a [[tokenized-treasuries|tokenized-Treasury]] fund share within the broader [[real-world-assets|RWA]] sector, not a free-floating crypto asset.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price (accruing NAV, USD-quoted)** | $1.21 |
| **Market cap (= AUM on-chain)** | $941.4M |
| **Market-cap rank** | #70 |
| **24h volume** | $0 (primary-market subscriptions/redemptions only) |
| **24h / 7d change** | +0.13% / −0.83% (NAV vs EUR/USD move) |
| **Circulating / total supply** | 779.08M EUTBL |
| **Max supply** | None (open-ended fund) |
| **All-time high** | $1.26 (2026-01-27, USD-quoted) |
| **All-time low** | $1.011 (2024-08-15) |

EUTBL is a **NAV-accrual** token: its USD-quoted "price" ($1.21) reflects both accrued Eurozone T-bill yield and the EUR/USD exchange rate, which is why the 7d change can be negative even though the fund earns positive euro yield (a EUR/USD move). The meaningful figure is **supply × price ≈ AUM (~$941M)** — consistent with RWA.xyz reporting EUTBL around the $1B total-asset-value mark in mid-2026. 24h volume is $0 because shares are subscribed/redeemed via Spiko's primary market, not traded secondary. Macro backdrop: "Established Bear Market", Fear & Greed ~23.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | EUTBL |
| **Asset class** | Tokenized money market fund (RWA / tokenized T-bills), EUR-denominated |
| **Regulation** | EU MMF Regulation; managed under French AMF supervision; short-term VNAV structure |
| **Fund AUM** | ~$941M (CoinGecko, June 2026 snapshot, rank #70); RWA.xyz reports ~$1.0B total asset value mid-2026 |
| **Yield mechanism** | Accumulating NAV — token price drifts up with Eurozone T-bill yield (≈ €STR; +8.07% trailing year at April 2026 snapshot, reflecting 2024–25 euro rates) |
| **Supply mechanics** | Supply tracks subscriptions/redemptions (primary-market fund flows), not a fixed issuance schedule |
| **Chains** | Ethereum, Polygon PoS, Base, Arbitrum, Starknet, Stellar, Etherlink |
| **Website** | [https://www.spiko.io](https://www.spiko.io) |

---

## Overview

Spiko EU T-Bills Money Market Fund is a fully-licensed EUR money market fund operating under the EU regulatory framework. It only invests in Treasury Bills issued by the strongest Eurozone Member States with less than 6 months maturity and keeps its maximum average portfolio maturity under 2 months.

Spiko (the issuer) is a Paris-based fintech founded in 2023 by Paul-Adrien Hyppolite and Antoine Michon with the explicit goal of closing the cash-yield gap between Europe and the US — bringing money-market yields to businesses and individuals whose bank deposits earn ~0%. The fund's shares are issued natively as tokens, redeemable T+0/T+1 in fiat or stablecoins.

## Mechanism & Backing

| Dimension | EUTBL design |
|---|---|
| **Underlying assets** | T-bills of the strongest Eurozone Member States, <6-month maturity, average portfolio maturity <2 months — minimal duration, high-grade sovereign credit |
| **Regulatory wrapper** | Sub-fund of the Spiko SICAV; an **AMF-supervised French short-term VNAV money market fund** under the EU Money Market Fund Regulation — a fully regulated MMF, not an unregistered offshore vehicle |
| **Yield source / NAV** | Income from the euro T-bill ladder accrues into NAV; token price drifts up ≈ €STR (the fund tracked roughly +8% over the trailing year at the prior snapshot, reflecting 2024–25 euro rates). Net yield ≈ short euro T-bill rate minus fund fees — qualitative, moves with ECB policy |
| **Custody / admin** | Regulated MMF custody/administration under the SICAV structure; shares mirrored on-chain as transferable tokens |
| **Redemption** | Primary-market subscription/redemption with Spiko, settled T+0/T+1 in fiat or stablecoins |
| **KYC / permissioning** | KYC required to mint/redeem via Spiko; tokens are transferable on-chain, broadening reach versus fully allowlisted institutional funds like [[blackrock-usd-institutional-digital-liquidity-fund|BUIDL]] |

As a VNAV MMF, EUTBL is **not pegged to €1** — its value floats with accrued yield, distinguishing it from non-yielding euro stablecoins ([[euro-coin|EURC]], [[stasis-eurs|EURS]]). It is the euro leg of Spiko's two-fund line (EUTBL + [[spiko-us-t-bills-money-market-fund|USTBL]]).

## Major News & Events (2025–2026)

- **2025-07 — $22M Series A** led by Index Ventures (with White Star Capital, Frst, Rerail, Bpifrance, Blockwall) after reaching **~$400M AUM in its first year**; Spiko projected $1B AUM by end-2025.
- **2025–2026 — AUM growth**: combined Spiko funds (EUTBL + USTBL) passed the $1B mark; EUTBL alone reached ~$1.03B total asset value by mid-2026 (RWA.xyz), making it the dominant tokenized **euro** treasury product — a category where it has far less competition than dollar funds (BUIDL, BENJI, OUSG).
- **Multichain expansion**: deployments extended to Starknet, Stellar and Etherlink alongside the original Ethereum/Polygon/Base/Arbitrum set.
- **ATH NAV** $1.26 (2026-01-27 snapshot, USD-quoted — reflects both accrued yield and EUR/USD).

---

## Peer Comparison — tokenized cash / treasury funds

| Fund | Currency | Underlying | NAV model | Regulation | Approx. size |
|---|---|---|---|---|---|
| **EUTBL** | EUR | Eurozone T-bills <6m | NAV-accrual | French AMF / EU MMFR (VNAV MMF) | ~$941M (#70) |
| [[spiko-us-t-bills-money-market-fund|USTBL]] | USD | US T-bills | NAV-accrual | Spiko sister fund | Smaller leg |
| [[blackrock-usd-institutional-digital-liquidity-fund|BUIDL]] | USD | US T-bills, repo | Flat $1.00 | US security (Reg D/S) | ~$2.38B (#40) |
| [[janus-henderson-anemoy-treasury-fund|JTRSY]] | USD | 0–3m US T-bills | NAV-accrual | BVI pro fund | ~$869M (#75) |
| [[euro-coin|EURC]] / [[stasis-eurs|EURS]] | EUR | Cash reserves | Flat €1.00 stablecoin | E-money / various | Varies |

EUTBL is effectively unrivalled as a **regulated, on-chain euro-yield** product — dollar tokenized-Treasury funds are crowded (BUIDL, BENJI, OUSG, USYC), but EUTBL faces far less euro competition, its main alternatives being non-yielding euro stablecoins.

---

## Platform & Chain Information

**Native Chain:** Ethereum (multichain issuance)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xa0769f7a8fc65e47de93797b4e21c073c117fc80` |
| Polygon PoS | `0xa0769f7a8fc65e47de93797b4e21c073c117fc80` |
| Base | `0xa0769f7a8fc65e47de93797b4e21c073c117fc80` |
| Etherlink | `0xa0769f7a8fc65e47de93797b4e21c073c117fc80` |
| Stellar | `CBGV2QFQBBGEQRUKUMCPO3SZOHDDYO6SCP5CH6TW7EALKVHCXTMWDDOF` |
| Arbitrum One | `0xcbeb19549054cc0a6257a77736fc78c367216ce7` |
| Starknet | `0x4f5e0de717daa6aa8de63b1bf2e8d7823ec5b21a88461b1519d9dbc956fb7f2` |

---

## Exchange Listings

No CEX or perp listings — EUTBL is acquired/redeemed via Spiko's primary market (KYC required) and held as an on-chain cash-management instrument; 24h secondary volume is effectively zero. This is normal for tokenized MMFs, not a red flag.

---

## Trading Relevance

- **Narrative basket**: [[real-world-assets]] / tokenized treasuries — the fastest-growing institutional crypto vertical of 2024–2026. EUTBL is the benchmark **euro-yield** leg; [[spiko-us-t-bills-money-market-fund|USTBL]] is the dollar leg.
- **Use for traders**: on-chain euro cash parking with T-bill yield — a yield-bearing alternative to non-interest-bearing EUR stablecoins ([[euro-coin|EURC]], [[stasis-eurs|EURS]]); usable as a treasury asset and increasingly as collateral in DeFi integrations.
- **Macro angle**: EUTBL NAV growth tracks ECB short rates — its yield is a live read on €STR; the EUR/USD pair drives its USD-quoted "price" as much as yield does.
- **Signals**: RWA.xyz fund flows into EUTBL/USTBL are a useful gauge of institutional euro-vs-dollar on-chain cash allocation.
- **Risks**: regulatory (MiCA/MMF interplay), redemption-gate tail risk common to all MMFs, and platform concentration on Spiko.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.spiko.io](https://www.spiko.io) |
| **GitHub** | [https://github.com/spiko-tech/contracts](https://github.com/spiko-tech/contracts) |
| **Docs** | [https://docs.spiko.xyz](https://docs.spiko.xyz) |

---

## Developer Activity

| Metric | Value (2026-04-09 snapshot) |
|---|---|
| **GitHub Stars** | 13 |
| **GitHub Forks** | 2 |
| **Pull Requests Merged** | 48 |
| **Contributors** | 6 |

---

## Risks

| Risk | Assessment |
|---|---|
| **Issuer / manager** | Moderate — Spiko is a young (2023) fintech, though the fund itself is a regulated AMF MMF with institutional custody/admin |
| **Underlying credit / duration** | Low — investment-grade Eurozone sovereign T-bills, <2-month average maturity |
| **FX** | Notable for USD-based holders — USD-quoted value carries EUR/USD risk; the euro yield is earned in euros |
| **Smart-contract / multichain** | Moderate — deployed across 7 networks; bridge and token-contract risk |
| **Regulatory** | Moderate — MiCA / EU MMF Regulation interplay for tokenized fund shares is still maturing |
| **Liquidity / redemption** | Moderate — par redemption depends on euro T-bill liquidity; MMF redemption-gate tail risk; platform concentration on Spiko's primary market |
| **De-peg** | N/A in the stablecoin sense — VNAV by design; risk is NAV impairment, not peg break |

---

## See Also / Related

- [[spiko-us-t-bills-money-market-fund]] — sister USD fund (USTBL)
- [[ustbl-tokenized-u-s-treasury-bill]] — tokenized US T-bill coverage
- [[real-world-assets]], [[tokenized-treasuries]], [[treasury-bills]] — sector pages
- [[blackrock-usd-institutional-digital-liquidity-fund]], [[janus-henderson-anemoy-treasury-fund]] — peer tokenized-Treasury funds
- [[euro-coin]], [[stasis-eurs]] — non-yielding euro stablecoin alternatives
- [[ondo-finance]] — competing tokenized-treasury issuer (USD)
- [[ethereum]] — primary issuance chain

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- Spiko, "Spiko raises $22M led by Index Ventures, after hitting $400M AUM in first year" — https://www.spiko.io/blog/spiko-raises-22m-led-by-index-ventures
- The Block, "Spiko raises $22 million in Series A funding round to scale tokenized money market funds" (2025-07) — https://www.theblock.co/post/363096/spiko-raise
- RWA.xyz EUTBL asset page — https://app.rwa.xyz/assets/EUTBL
- Spiko Euro fund page — https://www.spiko.io/spiko-euro
- Web verification (WebSearch + Perplexity), 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 816.91M EUTBL |
| **Total Supply** | 818.59M EUTBL |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $990.14M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.26 (2026-01-27) |
| **Current vs ATH** | -4.09% |
| **All-Time Low** | $1.01 (2024-08-15) |
| **Current vs ATL** | +19.63% |
| **24h Change** | +0.41% |
| **7d Change** | +0.30% |
| **30d Change** | -1.01% |
| **1y Change** | +0.44% |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $0.00000000 |
| **Market Cap Rank** | #65 |
| **24h Range** | $1.20 — $1.21 |
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
