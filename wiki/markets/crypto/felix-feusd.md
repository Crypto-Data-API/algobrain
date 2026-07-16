---
title: "Felix feUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins]
aliases: ["FEUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://usefelix.xyz/"
related: ["[[collateralized-debt-position]]", "[[crypto-markets]]", "[[dai]]", "[[hyperliquid]]", "[[stablecoin]]", "[[stablecoins]]"]
---

# Felix feUSD

**Felix feUSD** (ticker **FEUSD**) is a crypto-collateralized [[stablecoin]] issued by the Felix protocol on **HyperEVM**, the EVM execution layer of the [[hyperliquid|Hyperliquid]] ecosystem, targeting a 1:1 peg to the US dollar. feUSD is minted against over-collateralized crypto deposits in a [[collateralized-debt-position|CDP / vault]] model — conceptually similar to MakerDAO's [[dai|DAI]] — rather than being backed by fiat reserves. It functions as the native dollar unit for borrowing, leverage, and DeFi activity within Hyperliquid/HyperEVM.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Detail |
|---|---|
| **Ticker** | FEUSD |
| **Market Cap Rank** | #335 |
| **Current Price** | $0.9980 |
| **Market Cap** | $74.9M |
| **24h Volume** | $100.3K |
| **24h Change** | +0.01% |
| **Circulating Supply** | 75.0M FEUSD |
| **Total Supply** | 8.90B FEUSD (mint ceiling, not circulating) |
| **All-Time High** | $1.067 |
| **All-Time Low** | $0.7059 |
| **Categories** | Stablecoins, Crypto-backed Stablecoin, Hyperliquid Ecosystem, HyperEVM Ecosystem |
| **Website** | [https://usefelix.xyz/](https://usefelix.xyz/) |

At the snapshot, feUSD traded at **$0.9980**, within ~20 bps of par. Note the lifetime range is wide for a stablecoin: an **all-time low of $0.7059** (a roughly 29% de-peg, recorded 2025-10-10) confirms feUSD has suffered a severe historical de-peg, and an ATH of $1.067 shows it has also traded meaningfully above par. The "total supply" of 8.9B reflects a contract mint ceiling, not real backing — only ~75M is circulating and collateralized.

---

## Peg & Backing / Yield Mechanism

- **Peg target:** 1 feUSD = US$1, maintained by over-collateralized minting plus arbitrage and liquidation mechanics.
- **Backing:** **crypto collateral** locked in vaults/CDPs on HyperEVM. Borrowers mint feUSD against deposits (e.g. HYPE and other supported assets) above a required collateralization ratio. This is endogenous crypto backing, not exogenous T-bills or fiat.
- **Stability mechanism:** if collateral value falls below the liquidation threshold, positions are liquidated to buy back and burn feUSD, defending the peg. A peg-stability/redemption module and arbitrage incentives pull the secondary price back toward $1.
- **Yield source:** holders/stakers can earn from protocol borrowing fees and liquidation revenue; the headline draw is using feUSD as borrowable dollar liquidity inside Hyperliquid rather than a passive savings rate.

### Architecture deep-dive

Felix is the leading native lending / stablecoin layer for **[[hyperliquid|Hyperliquid]]**'s EVM execution environment (HyperEVM). Its design is modelled closely on the **Liquity** family of immutable CDP protocols rather than on MakerDAO governance:

- **Vaults / troves.** A borrower opens a position by depositing supported collateral (notably HYPE, the Hyperliquid native asset, plus other whitelisted assets) and minting feUSD up to a maximum loan-to-value. The position must stay above a **minimum collateral ratio**; below it, the position is liquidatable.
- **Stability pool.** feUSD deposited into Felix's **stability pool** is the first-loss backstop: when a vault is liquidated, its debt is cancelled against pooled feUSD and the pool receives the seized collateral (usually at a discount), so stability-pool depositors earn the liquidation surplus. This is the primary liquidation engine and a core yield source for feUSD holders.
- **Redemptions / peg floor.** A redemption mechanism lets anyone swap feUSD for $1 of underlying collateral from the riskiest vaults, creating a hard arbitrage floor near $1: if feUSD trades below par, redeemers profit by buying cheap feUSD and redeeming for a full dollar of collateral, removing supply.
- **Mint/redeem gating.** Minting is permissionless within the protocol (open to any HyperEVM user who posts collateral) but bounded by collateral whitelisting and the per-asset collateral ratio — there is no off-chain KYC, unlike RWA dollars such as [[compounding-open-dollar|cUSDO]] or [[sygnum-fiusd-liquidity-fund|FIUSD]].

### Yield distribution

feUSD's yield is **endogenous protocol revenue**, not RWA carry: stability-pool depositors collect liquidation gains and a share of borrowing fees, and stakers of feUSD-related tokens may receive protocol fee flows. Unlike a T-bill-backed dollar, there is no exogenous interest stream — returns are a function of borrowing demand and liquidation volume inside Hyperliquid, which makes the yield procyclical (highest in volatile, high-activity periods).

---

## How / Where It Trades

- **Primary venue:** native to **HyperEVM / [[hyperliquid|Hyperliquid]]** DeFi (contract `0x02c6a2fa58cc01a18b8d9e00ea48d65e4df26c70`), traded mainly in on-chain pools within that ecosystem.
- **Liquidity caveat:** 24h volume is very thin (~$100K against a ~$75M cap). A stablecoin this illiquid can print outsized price prints on small trades, and exiting size at par is not guaranteed — much of feUSD's utility is captive to Hyperliquid rather than freely arbitraged across major exchanges.
- **Composability:** within HyperEVM, feUSD is used as borrowable dollar liquidity, an LP asset, and collateral in other Hyperliquid-native protocols. Its reach beyond that ecosystem is limited, so its fate is tightly coupled to Hyperliquid's growth.

---

## Comparison vs. peer crypto-collateralized / ecosystem stablecoins

| Dimension | **feUSD** | [[dai\|DAI]] | [[crvusd]] | [[f-x-protocol-fxusd\|fxUSD]] |
|---|---|---|---|---|
| **Model** | Liquity-style CDP (stability pool + redemptions) | CDP + PSM | CDP (LLAMMA soft-liquidation) | Leverage-engine crypto dollar |
| **Home ecosystem** | Hyperliquid / HyperEVM | Ethereum (multi-chain) | Ethereum (multi-chain) | Ethereum / Base |
| **Primary collateral** | HYPE + whitelisted assets | ETH, RWA, stables | ETH, wBTC, LSTs | wstETH, WBTC |
| **Peg floor** | Redemption arbitrage to $1 | PSM to $1 | Soft-liquidation band | Stability pool + arbitrage |
| **Holder yield** | Stability-pool liquidation gains + fees | sDAI (DSR) | scrvUSD | fxSAVE |
| **Demonstrated depeg** | Yes — $0.7059 ATL (~29%) on 2025-10-10 | Brief (Mar-2023 SVB) | Minor | Down to $0.95 |
| **Scale / cap** | ~$75M | Multi-billion | Hundreds of M | ~$57M |

feUSD is the **Hyperliquid-ecosystem analogue of crvUSD/DAI**: same CDP-plus-stability-pool architecture, but with concentrated exposure to HYPE collateral and to a young, single-ecosystem chain. That concentration is the source of both its growth potential and its demonstrated depeg risk.

---

## Narrative, category & catalysts

feUSD's thesis is a **bet on Hyperliquid**: as HyperEVM accrues TVL and DeFi activity, the ecosystem needs a native dollar for borrowing, leverage and liquidity, and feUSD is positioned as that unit (a "stablecoin-of-the-app-chain" play).

- **Hyperliquid growth** is the dominant catalyst — feUSD demand scales with HyperEVM lending/leverage volume.
- **HYPE price regime** matters acutely: because HYPE is a primary collateral, a sharp HYPE drawdown directly threatens feUSD's backing and can trigger liquidation cascades. As of 2026-06-23 crypto is in **Extreme Fear** (Fear & Greed 21, market-health 29/100, bottoming/accumulation) — the regime in which young-chain CDP collateral is most fragile.
- **Competition** from other Hyperliquid stablecoins and from bridged majors (USDC/USDT) caps how much captive demand feUSD can hold.

---

## Risks

- **De-peg risk (demonstrated):** the $0.7059 ATL shows feUSD has already broken peg hard once. Crypto-collateralized CDP stablecoins are vulnerable to fast collateral crashes and liquidation cascades, especially when the underlying (e.g. HYPE) is volatile.
- **Collateral risk:** value depends entirely on the on-chain collateral remaining over-collateralized; a sharp, illiquid drop in collateral can leave bad debt and undercollateralized feUSD.
- **Issuer / smart-contract risk:** reliance on Felix's vault and oracle contracts on a relatively young chain (HyperEVM); oracle failure or exploit is a primary failure mode.
- **Liquidity risk:** thin secondary liquidity (see above) makes orderly exits during stress difficult.
- **Regulatory risk:** evolving stablecoin frameworks may treat crypto-backed dollars and their yield differently from fiat-backed ones.
- **Macro backdrop:** as of 2026-06-21 the Crypto Fear & Greed Index reads **23 ("Established Bear Market")** — the regime in which CDP collateral crashes and de-peg events are most likely.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 75.0M FEUSD |
| **Total Supply (mint ceiling)** | 8.90B FEUSD |
| **Max Supply** | Unlimited |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.067 |
| **All-Time Low** | $0.7059 (2025-10-10) — ~29% de-peg event |
| **Current Price** | $0.9980 |
| **24h Change** | +0.01% |

---

## History & timeline

| Date | Event |
|---|---|
| 2025-10-10 | All-time low of $0.7059 — a ~29% de-peg event, the defining risk datapoint for feUSD |
| 2026-04-09 | Captured in CoinGecko top-1000 listing snapshot (Source: [[coingecko-top-1000-2026-04-09]]) |
| 2026-06-21 | Market snapshot: $0.9980, ~$74.9M cap, rank #335, 24h volume ~$100K |

> The Oct-2025 de-peg is a real, dated stress event and the most important historical fact about feUSD's risk profile. Further protocol milestones will be added as primary Felix sources are ingested.

## Usage playbook

- **Holder / yield angle:** the productive use is depositing feUSD into the **stability pool** to earn liquidation gains and fees — but this means absorbing seized (often falling) collateral during exactly the stress events that caused the 2025 depeg. Size accordingly.
- **Borrower angle:** mint feUSD against HYPE/collateral for leverage or liquidity inside Hyperliquid; keep a wide collateral buffer given the demonstrated tail risk and the current Extreme-Fear regime.
- **Risk watch:** HYPE collateral volatility, oracle integrity on a young chain, stability-pool depth, and thin secondary liquidity. Do not assume you can exit size at par during a HYPE drawdown.

---

## Platform & Chain Information

**Native Chain:** Hyperevm

### Contract Addresses

| Chain | Address |
|---|---|
| Hyperevm | `0x02c6a2fa58cc01a18b8d9e00ea48d65e4df26c70` |
| Hyperliquid | `0x88102bea0bbad5f301f6e9e4dacdf979` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://usefelix.xyz/](https://usefelix.xyz/) |
| **Twitter** | [@felixprotocol](https://twitter.com/felixprotocol) |
| **Whitepaper** | [https://usefelix.gitbook.io/felix-docs](https://usefelix.gitbook.io/felix-docs) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $100.3K |
| **Market Cap Rank** | #335 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Related

- [[stablecoin]] / [[stablecoins]]
- [[collateralized-debt-position]]
- [[dai]] — the canonical crypto-collateralized stablecoin
- [[crvusd]] — closest architectural peer (CDP + stability mechanics)
- [[f-x-protocol-fxusd]] — peer crypto-backed dollar
- [[hyperliquid]]
- [[depeg]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FEUSD |
| **Market Cap Rank** | #320 |
| **Market Cap** | $74.96M |
| **Current Price** | $0.9989 |
| **Categories** | Stablecoins, Synthetic Asset, Crypto-backed Stablecoin |
| **Website** | [https://usefelix.xyz/](https://usefelix.xyz/) |

---

## See Also

- [[crypto-markets]]

---
