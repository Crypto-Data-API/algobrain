---
title: "XT Stablecoin XTUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoin]
aliases: ["XT Stablecoin", "XT.com USD", "XTUSD"]
entity_type: protocol
headquarters: "Centralized (exchange-issued)"
website: "https://www.xtusd.pro/main"
related: ["[[crypto-markets]]", "[[stablecoin]]"]
---

# XT Stablecoin XTUSD

**XTUSD** is a U.S.-dollar [[stablecoin]] issued by the **XT.com** cryptocurrency exchange. It is designed to trade at ~$1.00 and serve as a settlement, trading-pair, and on-platform unit of account within the XT.com ecosystem. As an *exchange-issued* stablecoin it is centralized: holders rely on a single corporate counterparty (XT.com) to honor redemptions and maintain backing — a materially different risk profile from decentralized or independently-audited stablecoins. It ranks **#612** by market capitalization. The closest analogues are other **exchange-native dollars** (Binance's historical BUSD, Bybit/OKX house stablecoins) rather than independent issuers like [[usdc|Circle's USDC]].

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* XTUSD trades at **$0.999395 — effectively on-peg (≈$1.00)** — with market cap **$32,784,566**, **-0.00% (24h)** and **-0.01% (7d)**, holding the peg even as broader sentiment is fearful (BTC $64,508; Fear & Greed 21 / Extreme Fear).

---

## What XTUSD Is

XTUSD is a dollar-pegged token whose role is to provide a stable settlement asset inside the XT.com exchange — used for trading pairs, on-platform payments, and as a place to park value without leaving the venue. Functionally it behaves like other exchange-native stablecoins (a centralized issuer mints tokens nominally backed by reserves and pledges 1:1 redemption). Its market cap of ~$32.8M tracks circulating supply (~$1.00 each), and FDV equals market cap (MC/FDV ≈ 1.00), as is normal for a backed stablecoin where supply expands/contracts with mints and redemptions.

## Architecture — peg mechanism and counterparty model

Like all fiat-collateralized stablecoins, XTUSD's peg holds only as long as the market trusts the issuer to back and redeem tokens at $1.

- **Collateral / reserve model:** XTUSD is presented as a **fiat-collateralised dollar** — tokens minted against reserves held by the exchange. There is **no public, independently-audited proof of reserves** cited here, so backing composition (cash vs T-bills vs other) and adequacy **cannot be verified from this page**. Functionally, holders are extending **unsecured credit to XT.com**.
- **Peg / stability mechanism:** the mechanism is **centralized and trust-based** — *not* algorithmic, over-collateralized, or bridge-backed. The exchange acts as the redeemer of last resort: it mints when dollars come in and pledges to redeem at $1. The peg has held tightly in practice (24h range ~$0.9994–$1.00), but this is **issuer-discretion stability**, which can break suddenly under a redemption run.
- **Mint / redeem & gating:** mint/redeem is intermediated by XT.com (typically requiring an XT.com account and KYC). There is no permissionless on-chain redemption against a transparent reserve; the redemption guarantee is a corporate promise, gated by the exchange's processes and solvency.
- **Yield:** none is documented here — XTUSD is a settlement/parking unit, not a yield-bearing token.

> **Note on historical data:** CoinGecko's record shows an anomalous "all-time high" of ~$42 (2023) that reflects early data/ticker artifacts rather than a real $42 stablecoin price; treat XTUSD as a ~$1.00 peg asset.

## Competitive position & comparison

XTUSD competes with the dominant fiat-backed stablecoins and with other exchange-issued dollar tokens. Its utility is largely **confined to the XT.com venue**; it lacks the cross-platform liquidity, integrations, and reserve transparency of the market leaders. That confinement is the core limitation: an exchange stablecoin is only as useful — and only as safe — as the exchange behind it.

| Token | Issuer / type | Reserve transparency | Liquidity / reach | Counterparty |
|---|---|---|---|---|
| **XTUSD** | XT.com exchange-issued | **None verified here** | Thin, mostly on XT.com | Single exchange (XT.com) |
| **[[usdt\|USDT]]** | Tether (independent) | Quarterly attestations | Deepest in crypto | Tether (diversified venues) |
| **[[usdc\|USDC]]** | Circle (regulated) | Monthly attestations | Very deep, broad DeFi | Circle (regulated) |
| **BUSD** (historical) | Paxos/Binance, exchange-aligned | Regulated (NYDFS) until wind-down | Was deep on Binance | Paxos/Binance |

The instructive comparison is **BUSD**: even a *regulated, attested* exchange-aligned dollar was wound down by regulatory action — XTUSD carries the exchange-concentration risk **without** BUSD's transparency or regulatory standing.

---

## Risks (centralized stablecoin)

- **Centralized counterparty risk** — the single most important risk. XTUSD's value depends entirely on XT.com's solvency, honesty, and willingness/ability to redeem at $1. Exchange insolvency or freeze could impair or trap the token.
- **Reserve opacity** — no verified, independent proof-of-reserves is cited; backing composition and adequacy are unconfirmed.
- **Depeg risk** — fiat-backed stablecoins can break their peg under a redemption run, banking-partner failure, or loss of confidence (cf. historical USDC/UST stress events).
- **Concentration/utility risk** — usage is largely tied to one exchange; liquidity outside XT.com is thin, raising exit risk in a stress scenario.
- **Regulatory risk** — exchange-issued stablecoins face rising regulatory scrutiny (reserve, redemption, and disclosure rules) that could force changes or restrict access.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | XTUSD |
| **Market Cap Rank** | #612 |
| **Market Cap** | $32,784,566 |
| **Current Price** | $0.999395 (≈$1.00, on-peg) |
| **24h / 7d Change** | -0.00% / -0.01% |
| **Issuer** | XT.com exchange (centralized) |
| **Categories** | Stablecoins |
| **Website** | [https://www.xtusd.pro/main](https://www.xtusd.pro/main) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 32.80M XTUSD |
| **Total Supply** | 32.80M XTUSD |
| **Max Supply** | 32.80M XTUSD |
| **Fully Diluted Valuation** | $32.80M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $42.29 (2023-03-07) |
| **Current vs ATH** | -97.64% |
| **All-Time Low** | $0.9331 (2023-03-09) |
| **Current vs ATL** | +7.15% |
| **24h Change** | +0.00% |
| **7d Change** | +0.00% |
| **30d Change** | -0.01% |
| **1y Change** | +0.12% |

---

## Platform & Chain Information

**Native Chain:** Multiple chains (see contract addresses below)

### Contract Addresses

| Chain | Address |
|---|---|
| Unknown | `0x1a6131eaf7edd96afa10fc75b0d79dd814d19ed0` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.xtusd.pro/main](https://www.xtusd.pro/main) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.31M |
| **Market Cap Rank** | #602 |
| **24h Range** | $0.9994 — $1.00 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Narrative / category & catalysts

XTUSD belongs to the **exchange-native stablecoin** category — a house dollar whose purpose is to keep trading, settlement, and balances inside one venue (XT.com). It is **utility infrastructure for a single exchange**, not a market-wide settlement asset or a yield product. There is no appreciation narrative; the only "price" events that matter are de-peg/redemption-stress events.

- **Catalysts (relevant):** growth (or distress) of XT.com itself; any move toward a published proof-of-reserves or audit (would de-risk); regulatory developments affecting exchange-issued stablecoins.
- **Tail-risk catalysts:** exchange insolvency, banking-partner failure, or a redemption run — the same failure family that took down weaker stablecoins historically.

---

## History / Timeline

| Date | Event |
|---|---|
| **2023-03-07** | Recorded all-time **high ~$42.29** — a **data/ticker artifact** from a thin early market, *not* a real stablecoin price. |
| **2023-03-09** | Recorded all-time **low ~$0.9331** — a real but minor sub-peg dip during early-market thinness (coincided with the broad USDC/SVB stablecoin stress week). |
| **2026-06-22** | Trades **~$0.9994 (on-peg)**, MC ~$32.8M, flat 24h/7d — holding peg despite **Extreme Fear** in the broader market (BTC ≈ $64,508; Fear & Greed 21). |

> **Data-artifact flag:** the $42.29 ATH is non-economic noise; XTUSD is a ~$1.00 peg asset. The only genuine (mild) historical dip was to ~$0.93 in March 2023.

---

## Trading playbook

- **Venue utility, not a position.** Hold XTUSD only as a settlement/parking unit *while transacting on XT.com.* It has no yield and minimal off-venue liquidity, so there is no reason to hold it elsewhere.
- **Counterparty risk is the whole trade.** The dominant risk is XT.com's solvency and willingness to redeem — not market price. The peg is a corporate promise; size exposure to what you would accept as unsecured credit to the exchange.
- **Don't over-stay in stress.** Exchange-native dollars are the first to gap if the host exchange wobbles, and XTUSD's thin off-venue liquidity (~$3.3M 24h) makes a clean exit hard once confidence cracks. In the current **Extreme Fear** tape (Fear & Greed 21; market-health 29/100, bearish), weaker/opaque stablecoins are the most de-peg-prone — keep balances operational, not strategic.

---

## See Also

- [[crypto-markets]]
- [[stablecoin]]
- [[usdt]], [[usdc]] — independent fiat-backed peers (verified reserves)

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no other specific wiki source ingested yet.
