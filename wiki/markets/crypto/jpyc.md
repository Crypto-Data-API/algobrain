---
title: "JPYC"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, forex, stablecoins]
aliases: ["JPY Coin", "JPY Coin v1", "JPYC"]
entity_type: protocol
headquarters: "Tokyo, Japan"
website: "https://jpyc.jp/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[forex]]", "[[japanese-yen]]", "[[mica]]", "[[stablecoin]]"]
---

# JPYC

**JPYC** is a **Japanese-yen [[stablecoin]]** issued out of Japan, pegged to the [[japanese-yen|yen (JPY)]] at roughly 1 JPYC = ¥1. It is one of the most prominent yen-denominated stablecoins and is associated with Japan's regulated stablecoin framework, which (following 2023 amendments to the Payment Services Act) permits licensed issuers to offer fiat-backed stablecoins. JPYC is deployed across [[ethereum|Ethereum]], Polygon, Gnosis Chain (xDai), and other networks. It ranks **#870** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

JPYC trades at approximately **$0.0072221** because it tracks the **Japanese yen**, not the US dollar. At a USD/JPY rate near 138-140, one yen is worth about $0.0072 — so a ~$0.0072 quote means **1 JPYC ≈ ¥1**, exactly its intended [[forex]] peg. This is **not a [[depeg]]**: measured against the yen (its real reference asset), JPYC holds at ~¥1.00. Recent moves (24h -0.45%, 7d -0.33%) primarily reflect minor USD/JPY exchange-rate drift, not loss of peg. Market capitalization is roughly **$18.14M** (rank #870).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | JPYC |
| **Peg** | 1 JPYC ≈ 1 JPY (Japanese yen, not USD) |
| **Issuer** | JPYC (Japan) |
| **Backing** | Yen reserves (fiat-backed yen stablecoin) |
| **Market Cap Rank** | #870 |
| **Market Cap** | $18,139,432 |
| **Current Price** | $0.0072221 (≈ ¥1 at prevailing USD/JPY) |
| **24h / 7d Change** | -0.45% / -0.33% |
| **Categories** | Stablecoins, JPY Stablecoin, Polygon/Gnosis Chain/Ethereum Ecosystem |
| **Website** | [https://jpyc.jp/](https://jpyc.jp/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

JPYC is a Japanese stablecoin project pegged to the yen, serving as on-chain yen for payments, [[defi]], and settlement within Japan's crypto ecosystem, and as a vehicle for yen-denominated and USD/JPY [[forex]] exposure on-chain. Japan was an early mover on stablecoin regulation: the revised **Payment Services Act** (amendments effective in 2023) created a licensed regime for fiat-referenced stablecoins, defining them as a form of electronic payment instrument that can only be issued by licensed banks, trust companies, or registered fund-transfer service providers. This positions yen stablecoins like JPYC within a clearer legal framework than exists in many jurisdictions.

The earliest JPYC ("JPYC v1") was structured as a **prepaid payment instrument** under the older prepaid-instrument rules — usable for payments and redeemable for goods/services but with limited cash-out, reflecting how the project predated the full stablecoin licensing regime. The direction of travel for the project has been toward a fully regulated, redeemable fiat-backed yen stablecoin under the 2023 framework.

---

## Architecture — How a Regulated Yen Stablecoin Works

A fiat-backed yen stablecoin follows the same conceptual pipeline as other fiat stablecoins, adapted to Japanese law:

1. **Fiat in.** A user delivers Japanese yen to the issuer (bank transfer or, historically for the prepaid form, purchase of a prepaid balance).
2. **Mint.** The issuer mints an equal amount of JPYC on-chain (1 JPYC per ¥1) to the user's address. Because the unit is ~¥1, token counts are large (billions) — this is a denomination artifact, not inflation.
3. **Reserve / backing.** Under the Payment Services Act stablecoin regime, a licensed issuer must hold backing assets (e.g. yen demand deposits or trust-held assets) sufficient to honor redemption at par; trust-type issuance ring-fences user funds.
4. **On-chain use.** JPYC is a standard ERC-20-style token across Ethereum, Polygon, Gnosis Chain (xDai), and Shiden — transferable and composable for yen-denominated payments and DeFi.
5. **Redemption.** Under the regulated model, holders can redeem JPYC for yen at par; redeemability at par is the legal anchor of the peg. (The legacy prepaid form had narrower redemption.)

The peg therefore rests on **issuer redeemability plus adequate yen backing under Japanese regulation**, not on an algorithm or crypto collateral.

### Peg Mechanism — Why the USD Price Is ~$0.0072

JPYC is a **yen-denominated** stablecoin. Its target is parity with the yen (1 JPYC = ¥1), not the dollar. When quoted in USD it floats with the USD/JPY exchange rate:

- A ~$0.0072 USD quote corresponds to USD/JPY ≈ 138-140 (one yen ≈ $0.0072).
- Changes in the USD quote usually reflect USD/JPY moves, not peg failure.
- To assess peg health, measure JPYC **against the yen**, where it should sit at ~¥1.00.

Holders take on **currency risk** (USD/JPY fluctuation) exactly as they would holding physical yen. For a USD-based observer, JPYC behaves like a tokenized yen cash position.

---

## Tokenomics & Backing

| Metric | Value |
|---|---|
| **Circulating Supply** | ~2.5B JPYC (note: each unit ≈ ¥1, hence the large count) |
| **Max Supply** | Unlimited (minted/burned against yen deposits/redemptions) |
| **Market Cap / FDV Ratio** | ~1.00 |

The very large token count is a function of the unit being ~¥1 (worth ~$0.0072), not a sign of inflation. Supply tracks deposits and redemptions; there is no speculative emission and **no separate governance token** — JPYC is issued by a company under Japanese regulation, not governed by a DAO.

---

## Comparison vs Other Yen / Major-Fiat Stablecoins

Yen stablecoins are a small, regulation-led segment. JPYC's position depends on being among the first to operate under Japan's licensed stablecoin regime.

| Token | Issuer / type | Wrapper / regime | Distinguishing trait |
|---|---|---|---|
| **JPYC** | JPYC (Japan) | Payment Services Act (prepaid → regulated stablecoin) | Most prominent independent yen stablecoin; multi-chain |
| **GYEN** | GMO Trust (US/Japan) | NY trust-issued yen stablecoin | Yen stablecoin from a regulated trust; suffered a brief, well-known mispricing spike at launch |
| **[[monerium-eur-money|EURe]]** | Monerium (EEA) | EMI e-money ([[mica|MiCA]]-aligned) | Euro analogue — same "regulated non-USD stablecoin" thesis, different currency/jurisdiction |
| **[[circle|USDC]] / USDT** | Circle / Tether | USD reserve-backed | USD majors — vastly larger liquidity; JPYC is the yen alternative for FX-neutral yen exposure |

JPYC's differentiator is **currency and jurisdiction**: it gives on-chain users a regulated yen unit (FX-neutral for yen-based users) where the dominant stablecoins are dollar-denominated. Its weakness versus USD majors is liquidity — yen stablecoin volumes are very thin.

---

## How & Where It Trades / Where It's Used

- **On/off-ramp.** Issued and redeemed in Japan against yen; historically also acquirable via the prepaid model for payments.
- **DEX liquidity.** Secondary trading is mainly on **Uniswap V2/V3** (Ethereum) and on Polygon/Gnosis deployments. On-chain liquidity is **very thin** — 24h volumes can be only a few hundred dollars, so even modest trades can slip significantly.
- **Use cases.** Yen-denominated on-chain payments, DeFi, donations and point-style payments in Japan, and FX-neutral yen exposure for Japanese users who want to avoid dollar stablecoins.

---

## Narrative, Category & Catalysts

JPYC sits within the **regulated non-USD stablecoin** narrative alongside euro tokens like EURe. Catalysts:

- **Japanese stablecoin licensing.** Full operation under the Payment Services Act stablecoin regime (banks/trust/fund-transfer issuers) is the key structural catalyst — a compliant, freely redeemable JPYC could see institutional and payments adoption.
- **Tokenized-yen and CBDC backdrop.** Japan's exploration of a digital yen and broader tokenization shapes demand for regulated yen rails.
- **Cross-border / FX use.** Demand for FX-neutral yen settlement and on-chain yen carry-trade exposure tracks USD/JPY and Bank of Japan policy.

---

## History / Timeline

- **JPYC launch era** — JPYC introduced as a yen-pegged token structured as a **prepaid payment instrument** under Japan's prepaid-instrument rules.
- **2022-09-12** — JPYC records its all-time low USD quote of **$0.00020710** (a denomination/illiquidity artifact, not a yen-peg event).
- **2023** — Amendments to Japan's **Payment Services Act** establishing a licensed stablecoin regime take effect, creating the regulated framework toward which the project orients.
- **2025-10-31** — JPYC records its all-time high USD quote of **$0.0156**.

*(Dated price extremes are from the market-data snapshot and reflect USD/JPY and thin-liquidity effects, not yen-peg deviation.)*

---

## Risks & Considerations

- **FX / currency risk:** USD-based holders are exposed to USD/JPY swings. This is inherent to a yen asset, not a stablecoin failure.
- **Depeg (vs yen) risk:** A true depeg would be JPYC trading away from ¥1.00; thin liquidity makes brief off-peg prints possible on small chains/pools.
- **Issuer / reserve risk:** Holder protection depends on the issuer maintaining adequate yen backing and operating within Japan's regulatory regime; the legacy prepaid form had limited cash-out redemption.
- **Liquidity:** On-chain and exchange liquidity is **very thin**; 24h volumes can be negligible, so large trades can slip badly or be impractical.
- **Smart-contract risk:** Standard exposure across the multiple chains where JPYC is deployed.

---

## Trading / Usage Playbook

- **As yen cash on-chain:** Use JPYC to hold/transact yen without dollar exposure; read the USD quote as USD/JPY, not as peg health.
- **For FX exposure:** Long JPYC ≈ long yen vs USD; position against Bank of Japan policy and USD/JPY direction — but note thin liquidity limits size.
- **Execution caution:** Because pools are shallow, prefer issuer redemption for size and use DEXs only for small swaps; check pool depth before trading.
- **Peg monitoring:** Watch JPYC vs ¥1.00 (not vs $1) and issuer redeemability/backing disclosures.

*This is not investment advice; figures above are point-in-time market data, not a valuation.*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.51B JPYC |
| **Total Supply** | 2.51B JPYC |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $18.23M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0156 (2025-10-31) |
| **Current vs ATH** | -53.45% |
| **All-Time Low** | $0.00020710 (2022-09-12) |
| **Current vs ATL** | +3403.81% |
| **24h Change** | -0.83% |
| **7d Change** | +6.25% |
| **30d Change** | +6.96% |
| **1y Change** | +3.86% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x2370f9d504c7a6e775bf6e14b3f12846b594cd53` |
| Xdai | `0x417602f4fbdd471a431ae29fb5fe0a681964c11b` |
| Shiden Network | `0x735abe48e8782948a37c7765ecb76b98cde97b0f` |
| Polygon Pos | `0x6ae7dfc73e0dde2aa99ac063dcf7e8a63265108c` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X2370F9D504C7A6E775BF6E14B3F12846B594CD53/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0X2370F9D504C7A6E775BF6E14B3F12846B594CD53/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://jpyc.jp/](https://jpyc.jp/) |
| **Twitter** | [@jpy_coin](https://twitter.com/jpy_coin) |
| **GitHub** | [https://github.com/jpycoin](https://github.com/jpycoin) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $263.35 |
| **Market Cap Rank** | #886 |
| **24h Range** | $0.00725646 — $0.00742607 |
| **Last Updated** | 2026-04-09 |

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
- [[stablecoin]]
- [[japanese-yen]]
- [[forex]]
- [[depeg]]
- [[monerium-eur-money]]
- [[mica]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
