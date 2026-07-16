---
title: "Usual USD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["USD0", "USD0++", "Usual Protocol stablecoin"]
entity_type: protocol
founded: 2024
headquarters: "Decentralized (Usual Labs, Paris)"
website: "https://usual.money"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[stablecoin-depegs]]", "[[stablecoins]]", "[[usual]]"]
---

# Usual USD

**Usual USD** (USD0) is the RWA-backed stablecoin of the Usual Protocol, collateralized 1:1 by tokenized US Treasury bill products, with a staked/bonded wrapper (**USD0++**) that locks USD0 for four years in exchange for [[usual|USUAL]] token rewards. For traders, USD0 is best known as the centerpiece of the **January 2025 USD0++ depeg** — a landmark case study in redemption-mechanism risk where a protocol unilaterally changed exit terms, instantly repricing a "stable" asset to ~$0.89 and cascading into Curve, Pendle and Morpho liquidations.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | USD0 (liquid) / USD0++ (4-year liquid-bond wrapper) |
| **Current Price** | $0.999076 (on peg) |
| **Market Cap** | $553.08M |
| **Market Cap Rank** | #95 |
| **Fully Diluted Valuation** | $553.08M |
| **24h Volume** | $901,594 |
| **24h Range** | $0.998584 — $0.999469 |
| **24h Change** | +0.05% |
| **7d Change** | +0.05% |
| **Website** | [https://usual.money](https://usual.money) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

USD0 (the unstaked stablecoin) is trading **on peg** at ~$0.999 with the tight ~$0.9986–$0.9995 daily range expected of a T-bill-backed stable. The peg health here refers to **USD0 itself**, not the USD0++ wrapper — it was the wrapper, not the base stablecoin, that broke in January 2025 (see below). With ~$553M cap (rank #95) the supply remains well below its 2024 peak above $1B; ~$0.9M of daily volume is thin and almost entirely DEX-routed, so the on-chain Curve/Uniswap pools (not CEX order books) are where peg stress would first appear. The broad market sits in **extreme fear** (Crypto Fear & Greed Index = 23) within an **established bear market** as of 2026-06-20 — a regime in which RWA-backed stables that hold peg are precisely the assets capital rotates *into*.

## Key Facts

| Field | Detail |
|---|---|
| **Type** | RWA-backed stablecoin (tokenized T-bill collateral, e.g. Hashnote USYC), non-fractional |
| **Chains** | Ethereum (primary), Base, Arbitrum, BNB Chain |
| **Reward token** | [[usual|USUAL]] — governance/reward token distributed to USD0++ stakers |
| **Key mechanism risk** | USD0++ redemption: $0.87 floor-price exit OR forfeit rewards for 1:1 exit (post-Jan-2025 rules) |

---

## Overview

USD0 is a stablecoin fully backed 1:1 by Real-World Assets (RWA) like US Treasury Bills. It provides users with a stable, secure asset that is independent of traditional banking systems, fully transferable, and accessible within the DeFi ecosystem. As the core stability asset of Usual, USD0 supports transparency and security by maintaining real-time reserves, offering a non-fractional, reliable alternative to stablecoins like USDT and USDC.

The protocol's growth engine is **USD0++**, a "liquid bond" wrapper: users lock USD0 for a nominal four-year term and receive USUAL token emissions. USD0++ traded near $1 through 2024 because the market assumed 1:1 redeemability — an assumption the protocol broke in January 2025.

---

## The January 2025 USD0++ Depeg

- **2025-01-09/10** — Usual announced a change to USD0++ redemption: instead of 1:1, holders got a **dual-exit**: (a) immediate exit at a **floor price of $0.87** (rising gradually to $1 over four years), or (b) wait/forfeit accrued USUAL rewards for par exit.
- **Market reaction** — USD0++ slumped to **~$0.89**, partially recovering to ~$0.92 (The Block). Curve pools went heavily imbalanced as LPs fled; leveraged loopers on Morpho vaults were liquidated for millions; Pendle markets repriced sharply.
- **2025-01-13** — Usual activated a "revenue switch" redistributing RWA earnings to the community and added a "1:1 Early Unstaking" option requiring forfeiture of earned rewards.
- **Lesson for traders** — documented in [[stablecoin-depeg-history]]: "stable"-labelled wrapped/bonded tokens carry **redemption-design risk** distinct from collateral risk. USD0 itself (the unstaked stablecoin) held close to peg; the wrapper depegged.

---

## 2025–2026 Developments

- Post-depeg, supply contracted from its $1B+ 2024 peak toward ~$550–600M and TVL stabilized; the protocol continued operating with the floor-price mechanism in place and the floor accreting toward $1.
- The episode permanently reframed USD0's narrative from "yield-bearing T-bill stablecoin" to a peg-design credibility story; it is now a standard reference case in DeFi risk discussions.

---

## Trading Relevance

- **Depeg arbitrage**: USD0++ trading below its accreting floor price has offered a quantifiable convergence trade (buy discount, exit at floor/par) — see [[stablecoin-depeg-profit-capture]] and [[synthetic-stablecoin-depeg-arbitrage]]; the risk is further governance rule changes.
- **Venues**: liquidity is DEX-centric (Curve, Uniswap V3 on Ethereum); minimal CEX presence. Monitor Curve pool balances as the early-warning stress signal.
- **Basket**: RWA/T-bill-backed stablecoin cohort (USDY, BUIDL-adjacent, USYC) within [[stablecoin-yields]]; governance-token exposure trades separately as [[usual|USUAL]].
- **Risks**: governance can change redemption terms again; collateral custodian concentration; reflexivity between USUAL emissions value and USD0++ lock incentives.

---

## Tokenomics & Supply

| Metric | Value (snapshot 2026-06-20) |
|---|---|
| **Circulating Supply** | 553.58M USD0 |
| **Total Supply** | 553.58M USD0 |
| **Max Supply** | Unlimited (mint/redeem against RWA collateral) |
| **Fully Diluted Valuation** | $553.08M |
| **Market Cap / FDV Ratio** | 1.00 |

As a stablecoin, USD0 has no fixed cap and no emission overhang: supply expands and contracts with **mint/redeem against the underlying tokenized T-bill collateral**, so circulating ≈ total and MC/FDV = 1.00 by construction. The supply figure is therefore an *adoption* metric, not a dilution one — and at ~$554M it remains roughly half of the >$1B 2024 peak, reflecting the lasting outflow after the January 2025 USD0++ episode. The value-accrual and incentive design lives in the separate [[usual|USUAL]] token, distributed to USD0++ stakers; USD0 itself is intended to track $1.

---

## USD0 ↔ USUAL relationship

USD0 and [[usual|USUAL]] are deliberately split into a **two-token system**:

| Token | Role | Peg / target |
|---|---|---|
| **USD0** | The stablecoin — 1:1 RWA-backed, transferable, the unit of account | Tracks $1 |
| **USD0++** | Liquid-bond wrapper: lock USD0 (nominal 4-yr term) to earn USUAL emissions | Accreting floor toward $1 (post-Jan-2025) |
| **[[usual\|USUAL]]** | Governance/reward token; captures protocol revenue and is emitted to USD0++ stakers | Free-floating market price |

The economic loop: T-bill collateral backs USD0 → users stake into USD0++ to farm USUAL → USUAL's value (and protocol revenue switch) incentivizes locking, which deepens USD0 demand. The **reflexivity risk** is the flip side: if USUAL's price falls, the incentive to hold USD0++ weakens, which is exactly the dynamic that amplified the January 2025 wrapper depeg. Speculative exposure to the protocol's growth is expressed through USUAL; USD0 is the stability leg.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.33 (2024-07-12) |
| **Current vs ATH** | -24.64% |
| **All-Time Low** | $0.962885 (2025-04-10) |
| **Current vs ATL** | +3.75% |
| **Current Price** | $0.999076 (on peg, 2026-06-20) |

> The ATH/ATL extremes reflect transient dislocations (the 2024 launch-period premium and the 2025 post-depeg trough); for a stablecoin the meaningful read is that USD0 currently sits on its $1 target with a tight intraday band.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x73a15fed60bf67631dc6cd7bc5b6e8da8190acf5` |
| Base | `0x758a3e0b1f842c9306b783f8a4078c6c8c03a270` |
| Binance Smart Chain | `0x758a3e0b1f842c9306b783f8a4078c6c8c03a270` |
| Arbitrum One | `0x35f1c5cb7fb977e669fd244c567da99d8a3a6850` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X73A15FED60BF67631DC6CD7BC5B6E8DA8190ACF5/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://usual.money](https://usual.money) |
| **Discord** | [https://discord.usual.money/](https://discord.usual.money/) |
| **Whitepaper** | [https://docs.usual.money/](https://docs.usual.money/) |

---

## Market Structure & Derivatives

| Characteristic | Detail |
|---|---|
| **24h Volume** | $901,594 |
| **Market Cap Rank** | #95 |
| **24h Range** | $0.998584 — $0.999469 |
| **Primary venues** | DEX-centric: Curve, Uniswap V3 (Ethereum); minimal CEX presence |

Liquidity is **DEX-native**, not exchange-order-book: USD0 trades primarily in Curve stable pools and Uniswap V3 on Ethereum, so the early-warning signal for any peg stress is **Curve pool imbalance** (LPs fleeing one side), exactly as it played out in January 2025. There is no meaningful perpetual market on USD0 itself — it is a stablecoin, not a directional bet — so derivatives exposure to the Usual thesis is taken via the [[usual|USUAL]] governance token instead. The thin daily turnover (~$0.9M) is normal for an on-peg RWA stable held mostly as collateral/yield rather than actively traded.

### Peer comparison (RWA / T-bill-backed stablecoins)

| Stablecoin | Issuer / backing | Yield mechanism | Distinctive risk |
|---|---|---|---|
| **USD0 / USD0++** | Usual — tokenized T-bills (e.g. Hashnote USYC) | USUAL emissions via USD0++ lock | Wrapper redemption-design risk (Jan-2025 case) |
| USDY | Ondo — short-term T-bills + bank deposits | Native yield accrual in token price | Issuer/custody concentration |
| BUIDL | BlackRock — tokenized money-market fund | Distributions to holders | Permissioned, institutional access |
| USYC | Hashnote — tokenized T-bill fund | Yield-bearing share token | Used as collateral *inside* USD0 |
| [[gho\|GHO]] | Aave — crypto-collateralized (overcollateralized) | Stability-fee model | Crypto-collateral volatility, not RWA |

USD0's differentiator — and its scar — is the **USD0++ liquid-bond layer**: it offered a higher headline yield (USUAL emissions) than simple yield-bearing RWA stables, but bundled in **redemption-design risk** that the simpler peers (USDY, BUIDL) do not carry. The base USD0 stablecoin is comparable to its RWA peers; the wrapper is where it differs.

### Valuation framing (qualitative)

USD0 is not "valued" the way a speculative token is — it is a $1-targeting stablecoin, so the analytical questions are **peg integrity, collateral quality, and redemption credibility**, not price upside. On those axes: the base peg is holding (~$0.999), collateral is tokenized T-bills (high quality), but the protocol's redemption *credibility* was permanently dented by the unilateral January 2025 rule change and supply has not recovered to its peak. The tradeable angle is twofold: (1) **convergence arbitrage** on USD0++ when it trades below its accreting floor (capped by the risk of further governance changes), and (2) directional exposure to the protocol's growth via [[usual|USUAL]]. For USD0 itself, "fair value" is $1; the relevant risk premium shows up as the discount on USD0++ and the price of USUAL.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

- **Redemption-design / governance risk (the core lesson)**: USD0++ exit terms were changed unilaterally in January 2025, repricing a "stable" wrapper to ~$0.89 overnight. The protocol can in principle change redemption rules again; this is distinct from collateral risk and is the defining risk of the asset.
- **Reflexivity**: USD0++ lock incentives depend on USUAL's value. A fall in USUAL weakens the incentive to hold the wrapper, which can pressure the peg loop — the dynamic that amplified the 2025 depeg.
- **Collateral / custodian concentration**: backing relies on tokenized T-bill products (e.g. Hashnote USYC); custodian or issuer concentration is a single-point dependency.
- **DEX-liquidity fragility**: liquidity is concentrated in Curve/Uniswap pools, so peg stress shows up as pool imbalance and can cascade into Pendle/Morpho positions (as in 2025) faster than CEX-listed stables.
- **Supply has not recovered**: at ~$554M vs the >$1B 2024 peak, confidence and scale remain structurally below pre-depeg levels.
- **Macro regime**: extreme fear (Fear & Greed 23) in an established bear market raises the odds of forced deleveraging across the DeFi venues USD0 is embedded in.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[usual|USUAL]] — the protocol's governance/reward token
- [[stablecoins]], [[stablecoin-yields]], [[real-world-assets]]
- [[stablecoin-depegs]], [[stablecoin-depeg-history]]
- [[stablecoin-depeg-profit-capture]], [[synthetic-stablecoin-depeg-arbitrage]]
- [[gho|GHO]] — contrasting crypto-collateralized model

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original April 2026 market snapshot (contract addresses, listings baseline)
- Market snapshot 2026-06-20: cryptodataapi.com / CoinGecko top-1000 markets data (price, market cap, rank, volume, supply, ATH/ATL refresh)
- The Block: "Usual Money's protocol update sparks community concern as USD0++ drops below 92 cents" — https://www.theblock.co/post/333995/usual-money-protocol-update
- Blockworks: "Usual protocol's depeg spurs instability in DeFi markets" — https://blockworks.co/news/usual-depeg-spurs-defi-instability
- Usual Docs: "USD0++ Floor Price" — https://docs.usual.money/usual-products/usd0-liquid-staking-token/usd0++-floor-price
- Usual Docs: "USD0++ Early Redemption Mechanism" — https://docs.usual.money/usual-products/usd0-liquid-staking-token/usd0++-early-redemption-mechanism
- Verified via Perplexity (sonar) + web search, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 553.19M USD0 |
| **Total Supply** | 553.19M USD0 |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $552.44M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $43,983.00 |
| **Market Cap Rank** | #95 |
| **24h Range** | $0.9983 — $0.9988 |
| **Last Updated** | 2026-07-16 |

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
