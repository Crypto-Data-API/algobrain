---
title: "Metronome Synth USD"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, defi, stablecoin]
aliases: ["MSUSD", "msUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://metronome.io/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[stablecoin]]", "[[collateralization]]", "[[depeg]]", "[[defi]]"]
---

# Metronome Synth USD

**Metronome Synth USD** (ticker **MSUSD**, also styled **msUSD**) is the synthetic US-dollar [[stablecoin]] of the **Metronome Synth** system — a synthetic-asset protocol that lets users deposit collateral and mint **synthetic** dollar-denominated tokens against it. msUSD is a debt-backed synthetic dollar rather than a fiat- or reserve-backed coin, and it is deployed across [[ethereum]] and several L2/EVM ecosystems (Optimism, Base, Plasma). It ranks **#750** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

At the latest snapshot msUSD traded at **$0.996379** (market cap **$23,585,425**, rank **#750**), down **0.02% over 24h** and **0.09% over 7d**. A price of **~$1.00 is on-peg** — msUSD trades in a tight band slightly under a dollar, as expected for a collateral-backed synthetic stablecoin (Fear & Greed Index at 22 / Extreme Fear, [[bitcoin]] around $64,180).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | MSUSD |
| **Market Cap Rank** | #750 |
| **Market Cap** | $23,585,425 |
| **Current Price** | $0.996379 (on-peg) |
| **24h Change** | -0.02% |
| **7d Change** | -0.09% |
| **Categories** | Stablecoins, Synthetic, Synthetic Dollar, Ethereum Ecosystem, Optimism Ecosystem, Base Ecosystem, Plasma Ecosystem |
| **Website** | [https://metronome.io/](https://metronome.io/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Metronome Synth is a synthetic-asset protocol in which users deposit collateral and **mint synthetic tokens** that track an external price — in this case **msUSD**, a synthetic US dollar. Unlike a fiat-backed [[stablecoin]] (held in bank reserves) or a redeemable crypto-CDP coin, a synthetic dollar is created as **debt against collateral** within the protocol: the collateral secures the synthetic, and the synthetic's value is maintained by the protocol's minting, fee, and liquidation mechanics rather than by direct 1:1 fiat redemption.

Metronome Synth is the second-generation product from the **Metronome** team (originally known for the cross-chain **MET** token). The defining feature versus a plain CDP like [[dai|DAI]] is that the same collateral pool can mint a whole family of *synths* (synthetic USD, and in principle synthetic ETH, BTC and other price-tracked assets) — msUSD is the dollar leg of that family. A user deposits collateral once and can mint or switch between synths, with the protocol netting the debt across the basket.

## Backing & Peg Mechanism

- **Collateral-backed synthetic.** msUSD is over-collateralized by assets deposited into Metronome Synth. Minters take on a debt position denominated in synthetic dollars; the collateral must stay above a minimum ratio (see [[collateralization]]).
- **Debt-pool / synth model.** Each minter's obligation is a synthetic-dollar debt against their deposited collateral. The protocol enforces a per-collateral [[collateralization|collateral factor]]; mintable msUSD is capped at the discounted collateral value, leaving an over-collateralization buffer.
- **Liquidations.** If a position's collateral falls below the required ratio, it is liquidated — collateral is sold/seized to repay the synthetic-dollar debt and a liquidation incentive is paid to the liquidator, protecting the system's solvency.
- **Peg dynamics.** msUSD's soft peg is maintained by arbitrage around minting/burning and by secondary-market liquidity. Because it is a synthetic rather than a directly fiat-redeemable token, it can trade slightly under or over $1 (here ~$0.996) depending on supply, demand, and available liquidity. The natural restoring force: when msUSD trades below $1, debtors can buy it cheaply on the secondary market to repay debt at par (closing positions for less than $1 of value), which removes supply and pulls the price up; when it trades above $1, minting fresh msUSD against collateral and selling is profitable, adding supply.

### Yield source

msUSD is **not a passive-yield "savings dollar"** in the [[compounding-open-dollar|cUSDO]] / [[ondo-finance|OUSG]] sense — there is no T-bill reserve paying a coupon. Its economic appeal is on the *minting* side: a user can deposit yield-bearing or appreciating collateral, mint msUSD against it, and deploy that dollar liquidity elsewhere while retaining upside on the collateral. Any "yield" to msUSD holders comes from secondary-market deployment (LP fees, lending) rather than from the issuer. This makes it closer in spirit to [[crvusd]] and [[dai|DAI]] than to RWA yield dollars.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 23.34M MSUSD |
| **Total Supply** | 23.34M MSUSD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $23.26M |
| **Market Cap / FDV Ratio** | 1.00 |

The 1.00 market-cap/FDV ratio confirms there is no large locked or pre-mine overhang: msUSD supply is endogenous, expanding and contracting purely with how much synthetic dollar minters choose to create against collateral, and is capped only by an "unlimited" contract ceiling that the collateral base bounds in practice.

---

## Comparison vs. peer crypto-collateralized / synthetic dollars

| Dimension | **msUSD** | [[dai\|DAI]] | [[crvusd]] | [[f-x-protocol-fxusd\|fxUSD]] |
|---|---|---|---|---|
| **Type** | Synthetic dollar (debt-pool synth) | CDP-backed stablecoin | CDP (LLAMMA soft-liquidation) | Leverage-engine crypto-backed dollar |
| **Backing** | Over-collateralized crypto deposits | Crypto + RWA collateral | Crypto (ETH, wBTC, etc.) | wstETH, WBTC |
| **Redemption** | Repay debt to unlock collateral | Repay debt / PSM | Repay debt; soft-liquidation band | Mint/redeem vs collateral + stability pool |
| **Peg defense** | Mint/burn arbitrage + liquidations | PSM + liquidations | Continuous soft-liquidation | Stability pool + arbitrage |
| **Yield to holder** | None native (deploy externally) | sDAI (DSR) variant | scrvUSD variant | fxSAVE variant |
| **Scale** | ~$24M (small) | Multi-billion | Hundreds of millions | ~$57M |
| **Crypto beta** | Indirect (via collateral / liquidations) | Indirect | Indirect | Indirect |

msUSD is the smallest of this peer set and the most niche; it competes on the multi-synth flexibility of the Metronome system rather than on liquidity or brand. Its peg behaviour and risk profile are characteristic of small crypto-collateralized dollars: tight band in calm markets, vulnerable to brief illiquid prints under stress.

---

## Narrative, category & catalysts

msUSD sits in the **decentralized crypto-collateralized stablecoin** category — the DAI/crvUSD lineage — with a synthetic-asset twist. Drivers and headwinds:

- **Multi-chain DeFi liquidity:** msUSD's value depends on having pools and lending markets across its deployment chains ([[ethereum|Ethereum]], Optimism, Base, Plasma). Growth tracks Metronome Synth's TVL and the depth of those venues.
- **Risk regime:** as of 2026-06-23 crypto is in **Extreme Fear** (Fear & Greed 21, market-health 29/100, bottoming/accumulation regime) with [[bitcoin]] ≈ $64,568 and [[ethereum|ETH]] ≈ $1,737. This is precisely the regime where crypto-collateralized synthetic dollars are most stressed — falling collateral values shrink mintable supply and raise liquidation risk.
- **Competition:** as a small synth, msUSD faces a crowded field of larger, more liquid decentralized dollars; capturing demand requires differentiated yield/composability or ecosystem-specific captive use.

---

## History & timeline

| Date | Event |
|---|---|
| 2025-10-09 | All-time low of $0.4279 (brief illiquid print / depeg episode) |
| 2025-10-16 | All-time high of $3.43 (brief illiquid print, not directional appreciation) |
| 2026-04-09 | Captured in CoinGecko top-1000 listing snapshot (Source: [[coingecko-top-1000-2026-04-09]]) |
| 2026-06-21 | Market snapshot: $0.996379, ~$23.59M cap, rank #750 |

> The Oct-2025 ATH/ATL pair are thin-liquidity prints typical of a small synthetic stablecoin, not genuine valuation moves. Only verifiable price/listing events are recorded.

---

## How & where it's used

- **Native to Metronome Synth.** msUSD's primary venue is the protocol itself — mint against collateral, then deploy the synthetic dollar into on-chain pools/lending across Ethereum, Optimism, Base and Plasma.
- **Thin secondary liquidity.** At ~$24M cap with no major CEX listings, secondary depth is shallow; large orders can move price meaningfully off $1. Treat external order books as thin and prefer in-protocol mint/repay for size.

## Usage playbook

- **Minter angle:** deposit collateral, mint msUSD, deploy elsewhere while retaining collateral upside — a standard collateralized-borrow play. Size conservatively given liquidation risk in the current Extreme-Fear regime.
- **Holder angle:** no native yield; only hold msUSD if you have a productive on-chain use (LP, lending) that compensates for its small-cap depeg risk.
- **Risk watch:** collateral drawdowns (ETH/BTC), oracle integrity, liquidation depth, and secondary-pool liquidity. Avoid relying on the secondary market to exit size at par during stress.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.43 (2025-10-16) |
| **All-Time Low** | $0.4279 (2025-10-09) |
| **Current Price** | $0.996379 (on-peg) |
| **24h Change** | -0.02% |
| **7d Change** | -0.09% |

*As a synthetic-dollar [[stablecoin]], msUSD's price history is a tight band around $1; the extreme ATH/ATL above reflect brief illiquid prints/depeg episodes, not directional appreciation.*

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xab5eb14c09d416f0ac63661e57edb7aecdb9befa` |
| Plasma | `0x29ad7fe4516909b9e498b5a65339e54791293234` |
| Base | `0x526728dbc96689597f85ae4cd716d4f7fccbae9d` |
| Optimistic Ethereum | `0x9dabae7274d28a45f0b65bf8ed201a5731492ca0` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://metronome.io/](https://metronome.io/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.996379 (on-peg) |
| **Market Cap** | $23,585,425 |
| **Market Cap Rank** | #750 |
| **24h Change** | -0.02% |
| **7d Change** | -0.09% |
| **Last Updated** | 2026-06-21 |

---

## Risks

- **Synthetic-asset / depeg risk.** msUSD is a synthetic dollar without direct 1:1 fiat redemption, so it relies on collateral, arbitrage, and liquidity to hold peg; it can drift below $1 (currently ~$0.996) and is exposed to [[depeg]] under stress.
- **Collateral volatility & liquidation risk.** Backing is volatile crypto collateral; sharp drawdowns can trigger mass liquidations and, in extreme cases, under-collateralization.
- **Oracle risk.** Synthetic pricing and liquidations depend on price oracles; oracle failure or manipulation could break the peg or cause improper liquidations.
- **Smart-contract / multi-chain risk.** Deployed across [[ethereum]], Optimism, Base, and Plasma; contract bugs and cross-chain/bridge exposure add risk.
- **Liquidity / size.** At roughly $24M market cap with limited listings, msUSD is a small synthetic stablecoin with thin secondary-market liquidity.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[stablecoin]]
- [[collateralization]]
- [[depeg]]
- [[ethereum]]
- [[defi]]
- [[crypto-markets]]
- [[dai]] — canonical CDP stablecoin
- [[crvusd]] — soft-liquidation CDP dollar
- [[f-x-protocol-fxusd]] — peer leverage-engine crypto dollar

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
