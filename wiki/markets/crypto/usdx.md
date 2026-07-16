---
title: "USDX"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["Kava USDX", "USDX"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.kava.io/overview"
related: ["[[bnb]]", "[[crypto-markets]]", "[[dai]]", "[[kava]]", "[[stablecoin]]", "[[stablecoins]]", "[[usdc]]"]
---

# USDX

**USDX** is the crypto-collateralized, native US-dollar [[stablecoin]] of the **[[kava|Kava]]** DeFi hub (a Cosmos-SDK chain with EVM co-chain compatibility), designed to target a 1 USD soft peg. Users mint USDX by locking crypto collateral via Kava's CDP (collateralized-debt-position) system, in the same overcollateralized spirit as [[dai]]. It is bridged into the broader Cosmos ecosystem (e.g. Osmosis via IBC). As of the latest snapshot USDX is **trading materially below peg**, so it should be treated as a depegged / impaired stablecoin rather than a reliable dollar proxy.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | USDX |
| **Price** | $0.671508 |
| **Market cap** | $74.9M |
| **Market-cap rank** | #336 |
| **24h volume** | $2,958 |
| **24h change** | -4.30% |
| **Circulating supply** | 111.57M USDX |
| **Total supply** | 111.57M USDX |
| **All-time high** | $3.89 |
| **All-time low** | $0.100156 |

The price of **$0.67** is ~33% below the $1 peg target, and 24h volume is negligible (~$3K). This combination — heavy discount plus almost no liquidity — is characteristic of a stablecoin that has lost its peg and is no longer being actively arbitraged back.

---

## Architecture: peg & backing mechanism

USDX is a **crypto-overcollateralized stablecoin** — the original "hard CDP" design pattern pioneered by MakerDAO's [[dai]], rather than a fiat-reserve or synthetic-delta-neutral model.

- **Minting (CDP open).** A user deposits a supported crypto collateral asset into a Kava CDP and mints USDX against it, subject to a minimum collateralization ratio (the loan-to-value ceiling). The user holds debt (the minted USDX) against locked collateral; to reclaim the collateral they repay the USDX plus any accrued stability fee.
- **Peg defense.** The 1 USD target is meant to be held by three forces working together: (1) **overcollateralization** — every USDX is backed by more than $1 of crypto, giving a buffer; (2) **liquidations** — positions whose collateral ratio falls below the threshold are auctioned/liquidated, retiring USDX debt and protecting solvency; and (3) **arbitrage** — when USDX trades below $1, profit-seekers buy it cheap and repay debt at par; when above $1, they mint and sell. This arbitrage loop is the proximate force that keeps the market price near peg.
- **Stability fee / module parameters.** Kava governance sets collateral types, debt ceilings, liquidation penalties, and the stability fee (the interest on minted USDX), tuning supply and peg pressure.
- **Current state (impaired).** The live price (~$0.67) shows the peg-restoration mechanism is **not** currently holding. For overcollateralized designs, persistent sub-peg trading typically reflects collapsed mint/redeem arbitrage (no one finds it profitable to close the gap), very thin liquidity, and/or reduced protocol focus on the product. Holders should **not** assume $1 redeemability at current market conditions.

The token's long price history (ATH $3.89 in 2020, ATL $0.100156 in 2023) reflects an extended life with periods of significant peg deviation, unlike tightly-held fiat-backed dollars such as [[usdc]] or [[usdt]].

### Why "overcollateralized" does not guarantee the peg

A common misconception is that overcollateralization alone pins the price to $1. It does not: overcollateralization protects **solvency** (the protocol can cover its debt), but the **market price** is set by secondary-market supply/demand and only converges to $1 if arbitrageurs actively close gaps. When liquidity is near zero and the redemption/mint path is unattractive or impaired, the market price can wander far from par even while the system remains nominally solvent on paper. USDX's current ~33% discount illustrates exactly this gap between book solvency and traded price.

---

## Comparison vs peer dollars

| Token | Backing model | Peg held at snapshot | Issuer | Notes |
|---|---|---|---|---|
| **USDX** | Crypto-overcollateralized CDP | **No (~$0.67)** | Kava protocol | Depegged, near-zero liquidity |
| [[dai]] | Crypto-overcollateralized CDP (+ RWA, PSM) | Yes (~$1.00) | MakerDAO / Sky | Canonical design analog; far deeper liquidity & PSM backstop |
| [[usdc]] | Fiat reserves (cash + T-bills) | Yes (~$1.00) | Circle | Centralized, attested reserves, instant primary redemption |
| [[usde]] / [[ethena-usde]] | Synthetic delta-neutral (collateral + short perps) | Typically yes | Ethena | Yield-bearing; different risk surface (funding, exchange) |

The key contrast with [[dai]] is not the minting design — they are siblings — but the **depth of the arbitrage backstop**. Dai benefits from a Peg Stability Module (direct 1:1 swaps with [[usdc]]) and very deep liquidity, which mechanically anchors its market price. USDX has neither at present, which is why the same CDP architecture can leave one token at par and the other 33% under.

---

## How & where it trades

USDX is the native stablecoin of the Kava chain and is also present in the Cosmos ecosystem via IBC (e.g. an Osmosis IBC denom). The source data shows **no major centralized-exchange listings** and only ~$2,958 of 24h volume — effectively illiquid. At these volumes, the quoted price can be driven by a handful of trades, and entering or exiting any meaningful position would incur severe slippage. There is no practical "composability" story here: a stablecoin trading at $0.67 with $3K daily volume cannot reliably serve as collateral, a unit of account, or a settlement asset in DeFi.

---

## Narrative & category

USDX sits in the **legacy crypto-collateralized stablecoin** category — the first-generation, MakerDAO-style design that predates the 2023–2025 wave of yield-bearing synthetic dollars ([[usde]]) and tokenized-Treasury dollars ([[usdm]]). Its current trajectory is a cautionary case study: a CDP dollar whose host protocol's focus and liquidity have ebbed, leaving the token stranded below peg. The relevant catalysts for any normalization would be renewed protocol support, restored liquidity, and a credible redemption path — none of which are evident in the snapshot. In the current macro backdrop (crypto Fear & Greed at 21, "Extreme Fear", market in a bottoming/accumulation regime as of 2026-06-22), there is especially little incentive for arbitrageurs to deploy scarce risk capital to restore a small, illiquid peg.

---

## Risks

- **De-peg risk (realized, not hypothetical).** USDX is already trading ~33% under peg — this is a current condition, not a tail scenario.
- **Liquidity risk.** Near-zero volume and no major listings mean positions are difficult to exit anywhere near quoted prices; price discovery is fragile.
- **Protocol / collateral risk.** The value of minted USDX depends on the health of Kava's CDP system, collateral quality, and the liquidation engine; impaired collateral or a stalled liquidation auction can entrench the discount.
- **Issuer / governance risk.** Continued support, collateral onboarding, and parameterization depend on Kava governance and development priorities.
- **Redemption-gating / path risk.** If the practical mint/redeem-at-par path is closed or uneconomic, holders cannot force convergence to $1.
- **Regulatory risk.** As with all stablecoins, evolving rules may affect issuance and listings.

---

## Trading / usage playbook

- **Treat as impaired, not as a dollar.** Do not use USDX as a cash-equivalent, collateral, or quote asset at face value; mark it to its **traded price (~$0.67)**, not to $1.
- **Liquidity-aware sizing.** With ~$3K daily volume, even a four-figure exit can move the price several percent — assume severe slippage and price any position accordingly.
- **Speculative "depeg" plays are low-conviction here.** Buying a depegged stablecoin in hope of par recovery only works if a credible redemption/arbitrage path exists; for USDX that path is not evident, so the discount can persist or widen.
- **Prefer liquid alternatives for the dollar leg.** For an actual stable dollar in DeFi, [[usdc]], [[usdt]], or [[dai]] are the appropriate instruments.

---

## Related

- [[dai]] — the canonical crypto-overcollateralized stablecoin (closest design analog)
- [[stablecoin]] / [[stablecoins]] — category overview
- [[kava]] — the host DeFi hub / chain
- [[usdc]] — fiat-backed peer (for peg-stability contrast)
- [[usde]] / [[ethena-usde]] — synthetic yield-bearing dollar peer
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDX |
| **Market Cap Rank** | #1542 |
| **Market Cap** | $5.17M |
| **Current Price** | $0.00754900 |
| **Categories** | Stablecoins, USD Stablecoin, Fiat-backed Stablecoin |
| **Website** | [http://stableslabs.com](http://stableslabs.com) |

---

## Overview

USDX (Website: usdx.money | Twitter: @StablesLabs) is a synthetic USD stablecoin designed to provide stability without relying on traditional banking infrastructure. Backed by delta-neutral positions across multiple exchanges, USDX seamlessly bridges the gap between DeFi, CeFi, and TradFi. It enables DeFi users to access traditional delta-neutral strategies executed in CeFi platforms. As a crypto-native stablecoin, USDX offers a scalable, censorship-resistant, and highly stable solution for users looking to navigate the world of decentralized finance with confidence.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 684.56M USDX |
| **Total Supply** | 684.56M USDX |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $5.17M |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.06 (2024-12-06) |
| **Current vs ATH** | -99.29% |
| **All-Time Low** | $0.00726237 (2026-07-08) |
| **Current vs ATL** | +3.95% |
| **24h Change** | +0.00% |
| **7d Change** | +2.04% |
| **30d Change** | -10.90% |
| **1y Change** | -99.24% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xf3527ef8de265eaa3716fb312c12847bfba66cef` |
| Base | `0xf3527ef8de265eaa3716fb312c12847bfba66cef` |
| Arbitrum One | `0xf3527ef8de265eaa3716fb312c12847bfba66cef` |
| Ethereum | `0xf3527ef8de265eaa3716fb312c12847bfba66cef` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [http://stableslabs.com](http://stableslabs.com) |
| **Twitter** | [@StablesLabs](https://twitter.com/StablesLabs) |
| **Telegram** | [StablesLabsTG](https://t.me/StablesLabsTG) (16,762 members) |
| **Discord** | [https://discord.gg/stableslabs](https://discord.gg/stableslabs) |
| **Whitepaper** | [https://docs.usdx.money/](https://docs.usdx.money/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.14 |
| **Market Cap Rank** | #1542 |
| **24h Range** | $0.00754900 — $0.00754900 |
| **Last Updated** | 2026-07-15 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---
