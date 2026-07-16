---
title: "USDA"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["USDA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://alphapartner.vip/"
related: ["[[bnb]]", "[[crypto-markets]]", "[[stablecoins]]"]
---

# USDA

**USDA (USDA)** is a USD-pegged [[stablecoins|stablecoin]] issued by the **AP Web3 / Alpha Partner ("AP") ecosystem**, deployed on the [[bnb|BNB Chain]]. It is marketed as a compliant, cross-chain payments stablecoin anchored 1:1 to the US Dollar, with claimed FDIC-style deposit protection and regulatory compliance. As of the latest snapshot it ranks **#299** by market capitalization. (This is the "USDA-3" wiki slug — the AP-issued USDA on BNB Chain, distinct from other tokens that share the "USDA" ticker.)

> **Disambiguation:** This **AP Web3 USDA (BNB Chain, fiat-backed marketing)** is a *different asset* from **Avalon Labs' BTC-backed USDa** at [[usda-2]] (a crypto-collateralised CDP stablecoin) and from Angle's USDA. Same ticker, unrelated issuers — do not merge their histories, contracts, or de-peg events.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Detail |
|---|---|
| **Ticker** | USDA |
| **Peg target** | US Dollar (~$1.00) |
| **Issuer / chain** | AP Web3 (Alpha Partner) — BNB Chain |
| **Current price** | $0.967311 |
| **Market cap** | $84.13M |
| **Market cap rank** | #299 |
| **24h volume** | $563,270 |
| **Circulating supply** | 86.97M USDA |
| **Total supply** | 86.97M USDA |
| **24h change** | +1.33% |
| **7d change** | -2.14% |
| **All-time high** | $1.19 (2025-12-21) |
| **All-time low** | $0.590562 (2025-10-09) |

**Genuine de-peg note:** USDA is trading at **$0.9673 — roughly 3.3% below its $1 target**, recovering (+1.3% on the day) after falling -2.1% over the week. This is an actual peg deviation, not an FX artifact, and the token has a history of instability: an ATH of $1.19 and an ATL of **$0.59** (2025-10-09, a severe de-peg) show the peg has broken hard in the past. The current ~3% discount and the volatile history are material risk signals.

---

## Architecture — peg & backing mechanism

USDA is presented as a fiat-backed, compliance-oriented stablecoin. Based on issuer marketing materials (claims that should be **independently verified** — they are not confirmed in this wiki):

- **Claimed collateral / reserve model**: 1:1 with US Dollar reserves, described as "regularly audited" and held in secure reserves. No independent proof-of-reserves attestation is cited here, so the **true reserve composition and adequacy are opaque**.
- **Claimed FDIC protection**: the issuer markets FDIC-style insurance on holdings up to applicable limits — an unusual claim for a stablecoin that warrants skepticism, since FDIC insurance ordinarily applies to *bank deposits*, not to token holders, and pass-through coverage has strict conditions. **Treat as unverified marketing.**
- **Claimed regulatory compliance**: issued by a "regulated entity within the AP Web3 ecosystem" — again, asserted by the issuer, not independently confirmed.
- **Peg / redemption mechanism**: a fiat-backed stablecoin's peg is normally defended by **issuer mint/redeem at $1** (arbitrageurs buy below $1 and redeem at par; mint above $1). USDA's **persistent sub-$1 price and prior collapse to $0.59** indicate that this redemption/arbitrage loop has **not** reliably held the peg — the clearest evidence that the backing/redeemability is not functioning like a robust fiat-collateralised dollar.
- **Mint / redeem & gating**: redemption mechanics and any KYC/whitelisting are issuer-controlled and not transparently documented; holders depend entirely on AP's willingness and ability to honour par redemption.

> The marketing claims above (audits, FDIC protection, compliance) come from the issuer and are **not independently confirmed** in this wiki. The on-chain price behavior (current ~3% discount, prior drop to $0.59) is the more reliable signal and is **inconsistent with a robustly backed, freely redeemable $1 stablecoin.** Where issuer claims and price action conflict, weight the price action.

### Comparison vs peer dollars

| Token | Issuer / model | Reserve transparency | Peg track record |
|---|---|---|---|
| **USDA (AP Web3)** | AP / Alpha Partner, claimed fiat-backed | **None verified** (issuer claims only) | **Weak** — currently ~3% below peg; ATL $0.59 |
| **[[usdt]]** | Tether, fiat + T-bills | Quarterly attestations | Strong; brief stress de-pegs only |
| **[[usdc]]** | Circle, cash + short T-bills | Monthly attestations, regulated | Strong; one notable SVB de-peg (2023), recovered |
| **[[busd]]** (historical) | Paxos/Binance, fiat-backed | Regulated (NYDFS) | Strong until wind-down |

USDA's distinguishing feature versus established fiat dollars is the **absence of verified reserve backing combined with a demonstrably broken peg history** — it should be treated as a high-risk, possibly under-backed token rather than a [[usdt]]/[[usdc]]-grade dollar, despite the marketing framing.

---

## How / where it trades

USDA trades primarily on the [[bnb|BNB Chain]]; no major centralized-exchange listings are evident in the snapshot data.

- **24h volume (~$563K)** is modest and concentrated on-chain (BNB-Chain DEX liquidity). Treat liquidity as thin.
- **DeFi composability** is minimal — this is not a widely-integrated collateral or quote asset across major DeFi; it lives inside the AP/Alpha Partner ecosystem and BNB-Chain pools.
- The discount to $1 combined with limited liquidity means **exits at par are not guaranteed**; sellers may have to accept below-peg prices, and large sells could push price down further.

---

## Narrative / category & catalysts

USDA's framing is **"compliant, insured, cross-chain payments dollar"** within the AP Web3 / Alpha Partner ecosystem. In practice its category is best described as a **single-ecosystem, thinly-traded, unverified-backing stablecoin** — closer to an exchange/ecosystem token than to a mainstream fiat dollar.

- **Catalysts (upside, if real):** independent proof-of-reserves / a credible audit; genuine regulatory licensing; CEX listings that deepen liquidity — any of which would materially de-risk the peg claim.
- **Catalysts (downside):** the discount widening, a repeat of the 2025-10 collapse, or regulatory action against overstated FDIC/compliance marketing. Aggressive insurance claims that prove inaccurate are themselves a legal/reputational hazard.

---

## History / Timeline

| Date | Event |
|---|---|
| **2025-10-09** | All-time **low ~$0.590562** — a **severe de-peg** (~41% below par); the defining risk event. |
| **2025-12-21** | All-time **high ~$1.19** — a substantial *above*-peg dislocation, itself a sign of a broken/illiquid peg (a working $1 stablecoin should not trade to $1.19). |
| **2026-06-21** | Trades **~$0.9673** (≈3.3% below peg), +1.3% on the day after −2.1% on the week — an **active, ongoing sub-peg discount**. |

> **De-peg flag:** both extremes are real economic dislocations, not data artifacts — the $0.59 low **and** the $1.19 high both indicate a peg that does not hold tightly in either direction. The current ~3% discount is consistent with that pattern.

---

## Trading playbook

- **Do not treat as a par-stable dollar.** USDA is ~3% below peg with a history of breaking to $0.59 *and* $1.19. It is not a safe place to park value; the headline "stablecoin" label overstates its reliability.
- **Backing is the whole question.** The actionable risk is whether reserves exist and redemption works at par. Until an independent attestation appears, weight the **price action over the marketing** — and the price action says under-backed/illiquid.
- **Discount-buyers beware.** A "buy the discount, redeem at $1" trade only works if par redemption is actually open and honoured; the persistent discount suggests it is not freely available to the open market. Thin liquidity also means any sizeable exit prints below quote.
- **Macro framing (2026-06-23).** The market is in **Extreme Fear** (Fear & Greed 21; market-health 29/100, bearish) — precisely the environment in which weaker, opaquely-backed stablecoins de-peg as confidence and liquidity contract. USDA is squarely in that vulnerable bucket.

---

## Risks

- **De-peg risk (active)**: USDA is currently below peg (~$0.97) and has previously collapsed to $0.59 — the highest-priority risk on this page. The peg is demonstrably not rock-solid.
- **Issuer / custodial risk**: backing, reserves, and the FDIC/compliance claims are issuer-controlled and unverified here; if reserves are inadequate or claims overstated, holders bear the loss.
- **Transparency risk**: lack of independently confirmed reserve attestations makes the true collateral position opaque.
- **Liquidity risk**: thin volume on a single chain makes large redemptions difficult and amplifies de-peg moves.
- **Regulatory risk**: aggressive compliance/insurance marketing can attract regulatory scrutiny; misrepresented protections are a legal and reputational hazard.
- **Macro backdrop**: the broader market is in an "Established Bear Market" (Fear & Greed Index 23), an environment in which weaker stablecoins are more prone to de-pegging as confidence and liquidity contract.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 86.97M USDA |
| **Total Supply** | 86.97M USDA |
| **Max Supply** | 111.00M USDA |
| **Market Cap / FDV Ratio** | ~1.00 |

---

## Platform & Chain Information

**Native Chain:** BNB Chain

### Contract Addresses

| Chain | Address |
|---|---|
| BNB Chain | `0x17eafd08994305d8ace37efb82f1523177ec70ee` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://alphapartner.vip/](https://alphapartner.vip/) |
| **Twitter** | [@APalphalabs](https://twitter.com/APalphalabs) |
| **Telegram** | [AlphaPartners1](https://t.me/AlphaPartners1) |

---

## Related

- [[stablecoins]] — category overview
- [[usdt]], [[usdc]] — established fiat-backed peers (verified reserves)
- [[usda-2]] — *unrelated* Avalon BTC-backed USDa (same ticker, different issuer)
- [[bnb]] — host chain
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDA |
| **Market Cap Rank** | #1372 |
| **Market Cap** | $6.79M |
| **Current Price** | $1.00 |
| **Categories** | Stablecoins, USD Stablecoin, Fiat-backed Stablecoin |
| **Website** | [https://www.anzens.com/](https://www.anzens.com/) |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.85 (2025-11-16) |
| **Current vs ATH** | -79.25% |
| **All-Time Low** | $0.5298 (2025-10-10) |
| **Current vs ATL** | +89.89% |
| **24h Change** | +0.59% |
| **7d Change** | +0.62% |
| **30d Change** | +0.48% |
| **1y Change** | +0.28% |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $49,220.00 |
| **Market Cap Rank** | #1372 |
| **24h Range** | $0.9917 — $1.01 |
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

---
