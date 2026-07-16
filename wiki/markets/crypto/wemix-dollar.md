---
title: "WEMIX Dollar"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoin]
aliases: ["WEMIX Dollar", "WEMIX USD", "WEMIX$"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.wemix.com/en"
related: ["[[collateralization]]", "[[crypto-markets]]", "[[depeg]]", "[[gamefi]]", "[[stablecoin]]"]
---

# WEMIX Dollar

**WEMIX Dollar** (WEMIX$) is the USD-pegged [[stablecoin]] of the **WEMIX** blockchain ecosystem, a [[gamefi|gaming-focused]] (GameFi) layer-1 platform developed by South Korea's Wemade. WEMIX$ is designed to serve as the dollar-denominated unit of account inside the WEMIX gaming and DeFi economy — used for in-game settlement, liquidity provision, and as a stable trading pair within the ecosystem's native DEX and DeFi services.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, WEMIX$ trades at **$0.971286**, ranking **#985** by market capitalization with a market cap of **$14,141,910**, down **-0.97% over 24h** and **-0.41% over 7 days**. At roughly **2.9% below $1.00**, WEMIX$ is exhibiting a **mild soft discount** rather than a severe de-peg — a thin-liquidity stablecoin drifting modestly under par. This is worth noting honestly: it is not holding a tight peg, but it is also far from a collapse, and the discount is small enough to be explained by limited arbitrage depth and ecosystem-specific demand rather than a backing failure.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | WEMIX$ |
| **Market Cap Rank** | #985 |
| **Market Cap** | $14,141,910 |
| **Current Price** | $0.971286 (~2.9% soft discount to $1.00) |
| **24h / 7d Change** | -0.97% / -0.41% |
| **Ecosystem** | WEMIX (Wemade gaming blockchain) |
| **Categories** | Stablecoins, Gaming (GameFi), WEMIX Ecosystem |
| **Website** | [https://www.wemix.com/en](https://www.wemix.com/en) |

> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot); price/rank/cap above updated 2026-06-22.*

---

## Overview

WEMIX$ is the stable settlement asset of the WEMIX ecosystem, the blockchain network built by Korean game publisher **Wemade** (best known for the MIR franchise). The broader WEMIX stack includes the WEMIX3.0 layer-1 chain, the WEMIX PLAY game-publishing platform, and the WEMIX.Fi DeFi suite; WEMIX$ functions as the dollar-pegged leg of that DeFi and gaming economy, alongside the volatile native [[gamefi|GameFi]] gas/utility token WEMIX.

### Backing and peg mechanism

WEMIX$ is intended to track $1.00 through a collateralized model maintained within WEMIX.Fi: it is issued against on-chain reserves of other crypto-assets (including stablecoins and ecosystem tokens) held by the protocol, with an arbitrage/redemption design meant to keep market price near par. Because the protocol's own materials are the primary public source for reserve composition and the live reserve figures are not independently verified here, **specific reserve amounts and the precise collateral basket are left qualitative** in this page rather than stated as hard numbers. The key point for a reader is that, like other [[collateralization|collateral-backed]] stablecoins, WEMIX$ depends on the value and liquidity of its reserves and on functioning arbitrage to hold peg.

In design terms WEMIX$ is a **crypto-collateralized, ecosystem-local stablecoin** rather than a fiat-reserve-backed one. That places it in the same broad family as [[dai|DAI]] (over-collateralized, multi-asset) and algorithmic/hybrid designs, and away from fully fiat-backed coins like [[usdc|USDC]] or [[tether|USDT]] whose backing is off-chain bank reserves and short-dated Treasuries. The practical consequences:

- **Peg defense relies on arbitrage, not redemption-at-bank.** There is no fiat off-ramp that lets an arbitrageur reliably buy under-par WEMIX$ and redeem it for exactly $1 from a regulated issuer. Peg correction depends on in-ecosystem mint/redeem incentives and DEX arbitrage, which are only as strong as the depth of WEMIX.Fi liquidity.
- **Reflexivity to the WEMIX token.** If any portion of reserves is held in the volatile native WEMIX token (or other ecosystem assets), the backing value falls precisely when the ecosystem is stressed — the classic correlated-collateral weakness that has broken other ecosystem stablecoins.
- **No independent attestation surfaced here.** Unlike [[usdc|USDC]] (monthly attestations) or [[tether|USDT]] (quarterly), no third-party reserve attestation for WEMIX$ is ingested in this wiki, so backing rests on protocol disclosure.

### Comparison vs other stablecoin designs

| Stablecoin | Backing model | Peg-defense mechanism | Reserve transparency | Peg behavior (as of 2026-06-24 context) |
|---|---|---|---|---|
| **WEMIX$** | Crypto-collateralized, ecosystem-local (WEMIX.Fi reserves) | In-ecosystem mint/redeem + DEX arbitrage | Protocol disclosure only (no independent attestation surfaced) | Mild soft discount (~$0.97), thin liquidity |
| **[[usdc|USDC]]** | Fiat reserves (cash + short Treasuries) | Issuer redemption at $1 via regulated rails | Monthly third-party attestations | Tight peg, deep liquidity |
| **[[tether|USDT]]** | Mixed fiat/Treasury/other reserves | Issuer redemption (large minimums) | Quarterly attestations | Tight peg, deepest liquidity |
| **[[dai|DAI]]** | Over-collateralized crypto + RWA | Maker vaults, liquidations, PSM arbitrage | Fully on-chain, public | Tight peg, broad DeFi integration |

The table makes WEMIX$'s position clear: it is structurally closer to DAI than to USDC/USDT, but **without** DAI's deep liquidity, public over-collateralization data, and broad cross-protocol integration — which is why it can drift a few percent under par where DAI does not.

### On the current ~2.9% discount

The 2026-06-22 price of $0.971286 represents a **mild soft discount**, consistent with:

- **Thin liquidity:** WEMIX$ is a small, ecosystem-local stablecoin (market cap ~$14.1M) with limited venues, so even modest sell pressure can move price a few percent without deep arbitrage to snap it back.
- **Concentration in one ecosystem:** demand is largely internal to WEMIX gaming/DeFi, so price reflects ecosystem sentiment more than a broad fiat-redemption backstop.

This is a discount to watch, not a [[depeg]] crisis — but it does mean WEMIX$ should not be treated as a 1:1 dollar equivalent the way a deeply liquid, fully fiat-backed stablecoin would be.

### Ecosystem context: the 2023 Korean delisting controversy

The WEMIX ecosystem's reputation was shaped by a notable 2023 event: in late 2022/early 2023, South Korea's **Digital Asset eXchange Alliance (DAXA)** — the consortium of major Korean exchanges (Upbit, Bithumb, Coinone, Korbit, Gopax) — moved to **delist the WEMIX token**, citing discrepancies between Wemade's disclosed and actual circulating supply (allegedly large amounts of WEMIX used as collateral/liquidity without adequate disclosure). The delisting was contested by Wemade in court and was a major controversy in the Korean crypto market; WEMIX was later **relisted** on some Korean exchanges after the dispute. This history is relevant background for anyone assessing governance and disclosure risk across the WEMIX ecosystem, including its stablecoin WEMIX$. (Figures and exact dates of the dispute are summarized qualitatively here and should be verified against primary sources before relying on them.)

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 14.54M WEMIX$ |
| **Total Supply** | 14.54M WEMIX$ |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $14.38M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.54 (2025-08-05) |
| **Current vs ATH** | -35.78% |
| **All-Time Low** | $0.4796 (2025-05-02) |
| **Current vs ATL** | +105.82% |
| **24h Change** | -1.26% |
| **7d Change** | -1.13% |
| **30d Change** | -1.22% |
| **1y Change** | +33.34% |

---

## Platform & Chain Information

**Native Chain:** Wemix Network

### Contract Addresses

| Chain | Address |
|---|---|
| Wemix Network | `0x8e81fcc2d4a3baa0ee9044e0d7e36f59c9bba9c1` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.wemix.com/en](https://www.wemix.com/en) |
| **Twitter** | [@WemixNetwork](https://twitter.com/WemixNetwork) |
| **Telegram** | [WEMIX_ANNouncement](https://t.me/WEMIX_ANNouncement) (7,461 members) |
| **Whitepaper** | [https://www.wemix.com/download/WEMIX3.0_Whitepaper.pdf](https://www.wemix.com/download/WEMIX3.0_Whitepaper.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $513.97 |
| **Market Cap Rank** | #977 |
| **24h Range** | $0.9837 — $1.00 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Narrative, Category & Catalysts

WEMIX$ sits at the intersection of two narratives: **stablecoins** and **GameFi**. Its fortunes are almost entirely a derivative of the WEMIX gaming ecosystem rather than a standalone stablecoin thesis — there is no broad market reason to hold WEMIX$ over USDC/USDT unless you are transacting inside WEMIX PLAY, WEMIX.Fi, or related Wemade products.

**Potential catalysts (positive):**
- Renewed traction for Wemade's flagship titles (the MIR franchise and new WEMIX PLAY launches) that drive in-ecosystem settlement demand for WEMIX$.
- Deeper WEMIX.Fi liquidity or new venue listings that strengthen arbitrage and tighten the peg back toward $1.
- Korean regulatory clarity on stablecoins, which could either legitimize or constrain WEMIX$ depending on outcome.

**Potential catalysts (negative):**
- Any reserve-disclosure controversy echoing the 2023 DAXA episode (see below) would hit confidence in the whole ecosystem's assets.
- A widening discount under stress, signalling that arbitrage depth is insufficient.

## Trading Playbook (bear / Extreme-Fear regime)

In the 2026-06-24 backdrop — Fear & Greed 22 (Extreme Fear), an established bear market, BTC ~18% below its 200-day MA — the relevant framing for WEMIX$ is **peg-stability, not directional alpha**:

- **Not a USD parking spot.** A coin already trading ~2.9% under par with sub-$1K daily volume is not a safe place to hold "dollars." For cash-equivalent stability in a bear regime, deeply liquid coins ([[usdc|USDC]], [[tether|USDT]], [[dai|DAI]]) are the appropriate vehicles.
- **Discount-watch, not buy-the-discount.** A ~3% discount on a thin, ecosystem-local crypto-collateralized stablecoin is **not** a clean arbitrage — there is no reliable $1 redemption to capture, and the discount can persist or widen. Treat the discount as an information signal about ecosystem liquidity, not a guaranteed convergence trade.
- **Liquidity-first sizing.** With ~$500 of daily volume, any position is effectively illiquid; exit slippage dominates. Size for the assumption that you may not be able to get out near mark.
- **Headline risk binary.** Watch for any disclosure/governance news on Wemade or WEMIX reserves; the 2023 precedent shows the ecosystem can move sharply on transparency concerns.

## Risks

- **Mild but persistent soft discount:** Trading ~2.9% below $1.00 as of 2026-06-22; WEMIX$ does not currently hold a tight peg and should not be assumed to be exactly 1:1 with USD.
- **Thin liquidity / [[depeg]] risk:** Small market cap and ecosystem-local venues mean limited arbitrage depth; under stress the discount could widen.
- **Single-ecosystem concentration:** Value and demand are tightly coupled to the health of the WEMIX gaming/DeFi economy and to game publisher Wemade.
- **Governance / disclosure history:** The 2023 DAXA delisting of the WEMIX token over supply-disclosure concerns is a reminder that transparency and reserve disclosure carry real weight for this ecosystem's assets.
- **Reserve transparency:** Public, independently audited live reserve data for WEMIX$ is limited in this wiki; backing claims rest largely on protocol disclosures.

> *This is informational, not financial advice. A stablecoin trading below $1 is, by definition, not perfectly maintaining peg.*

---

## See Also

- [[crypto-markets]]
- [[stablecoin]] · [[collateralization]] · [[depeg]] · [[gamefi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; market figures as of 2026-06-22 (cryptodataapi.com / CoinGecko). The 2023 DAXA delisting and ecosystem details are summarized from general knowledge; no specific wiki source ingested yet.
