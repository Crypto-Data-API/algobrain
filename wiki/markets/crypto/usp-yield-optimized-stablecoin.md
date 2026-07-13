---
title: "USP Yield Optimized Stablecoin"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoin, defi]
aliases: ["USP", "Piku USP"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.piku.co/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[stablecoins]]", "[[yield-bearing-stablecoin]]"]
---

# USP Yield Optimized Stablecoin

**USP** is a **yield-optimized (yield-bearing) [[stablecoin|stablecoin]]** issued within the Piku ecosystem and governed by PikuDAO on [[ethereum|Ethereum]]. It combines the stability of a dollar-pegged unit with the value growth of a yield-generating reserve basket. USP launches fully backed 1:1 by USD stablecoins (a $1.00 starting value); PikuDAO then diversifies that backing into an on- and off-chain basket of yield assets, and the accrued yield is reflected **directly in the token's price** rather than paid out separately.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* USP trades at **$1.10** (rank **#865**, market cap **$18,279,292**, 24h **-0.08%**, 7d **+0.13%**). The price sitting **above $1.00 is by design, not a [[depeg]]**: USP is a value-accruing stablecoin, so accumulated yield raises the per-token unit value over time. The near-flat 24h/7d moves are consistent with a stable instrument whose price drifts upward only as yield accrues. See [[yield-bearing-stablecoin]] for how this "price-accrual" model differs from a fixed $1.00 [[rebasing]] design.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USP |
| **Market Cap Rank** | #865 |
| **Market Cap** | $18,279,292 |
| **Current Price** | $1.10 |
| **Value Model** | Yield-accruing (price > $1.00 by design) |
| **Categories** | Ethereum Ecosystem, Yield-Bearing Stablecoin, Yield-Bearing Tokens |
| **Website** | [https://www.piku.co/](https://www.piku.co/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

The Piku ecosystem provides the components needed to run a yield-optimized stablecoin, from transparent yield backing to DAO-led decision-making.

The USP token is a yield-optimized stablecoin that combines the stability of a traditional stablecoin with the growth potential of yield-generating assets. Governed by PikuDAO, USP is initially fully backed by USD stablecoins at a 1:1 ratio, ensuring a stable launch value of $1.00. PikuDAO then diversifies and enhances this backing with a carefully selected basket of on-chain and off-chain yield-generating assets.

### Value-accrual mechanism (why USP trades above $1)
As the reserve basket earns yield, that yield **increases the underlying value of each USP token**, lifting its market price above the initial $1.00 launch value. The current **$1.10** quote therefore represents roughly the cumulative net yield captured since launch — it is *value accrual by design, not a de-peg*. This is the "appreciating unit value" flavour of [[yield-bearing-stablecoin|yield-bearing stablecoin]] (the same model used by tokens such as OpenEden's [[compounding-open-dollar|cUSDO]]), as opposed to a rebasing token that holds a fixed $1.00 price and grows the holder's balance. USP is positioned as a simple-access on-chain savings tool.

### Architecture deep-dive — reserve basket & yield source

USP's defining feature is that its backing is **not a single asset class** but a DAO-managed, diversified basket:

- **Launch backing.** At issuance, USP is fully backed 1:1 by USD stablecoins, anchoring the $1.00 starting value.
- **Diversification by PikuDAO.** Governance then reallocates reserves into a "carefully selected basket of on-chain and off-chain yield-generating assets." Per the project's framing this spans on-chain DeFi yield (lending, LP, staking) and off-chain [[real-world-assets|RWA]] yield (e.g. tokenized cash / Treasury exposure). This makes USP a **yield-optimized aggregator** rather than a pure T-bill dollar like [[compounding-open-dollar|cUSDO]] or a pure delta-neutral dollar like [[ethena-usde|USDe]] — its yield archetype is a *blend* whose composition is a governance decision.
- **Price-accrual distribution.** Yield is **not** paid out or rebased; it is reflected directly in the token's per-unit price, which drifts up as net basket yield accrues. Holders realize yield by selling/redeeming at the higher unit value.
- **Mint / redeem.** USP is minted against USD stablecoins and redeemed back to the reserve; the ability to redeem at fair (accrued) value depends on PikuDAO's redemption terms and the liquidity of the underlying basket — the off-chain RWA sleeve is inherently less liquid than the on-chain sleeve.

> **Issuer note:** This page documents USP as the **Piku / PikuDAO** yield-optimized stablecoin per the project's public materials (piku.co, docs.piku.co). "USP" is a generic-sounding ticker used by more than one project; the subject here is specifically the PikuDAO-governed token at the Ethereum contract listed below. Do not conflate with similarly named tokens from other issuers.

### Risks
- **Yield-source risk** — returns and value-accrual depend on the underlying basket; weaker yields slow appreciation, and impaired assets can erode backing.
- **Collateral / reserve risk** — the off-chain and on-chain assets backing USP carry counterparty, custody and [[real-world-assets|RWA]] credit risk.
- **[[depeg]] (downside) risk** — although the price floats *upward* with yield, a loss of confidence or backing impairment could push USP *below* its accrued value; "value-accruing" protects against neither a reserve shortfall nor a liquidity crunch.
- **Governance / smart-contract risk** — PikuDAO controls reserve composition and protocol parameters; governance capture or contract bugs are live risks.
- **Redemption risk** — ability to redeem at fair (accrued) value depends on the issuer's redemption terms and reserve liquidity.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 13.91M USP |
| **Total Supply** | 13.91M USP |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $15.05M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Comparison vs. peer yield-bearing dollars

| Dimension | **USP** | [[compounding-open-dollar\|cUSDO]] | sDAI | [[ethena-usde\|USDe]] |
|---|---|---|---|---|
| **Yield source** | Diversified on-chain + off-chain RWA basket (DAO-chosen) | US T-bills + reverse repo | DAI Savings Rate | Delta-neutral basis (perps funding) + staked-ETH |
| **Distribution** | Price-accruing unit value | Price-compounding unit value | Rebasing-style (sDAI grows vs DAI) | sUSDe price-accruing |
| **Governance** | PikuDAO controls basket | OpenEden Digital (BMA-licensed) | MakerDAO / Sky | Ethena Labs |
| **Reserve transparency** | DAO-disclosed basket | Regulated T-bill attestation | On-chain DAI | On-chain + custodied |
| **Price (model)** | ~$1.10 (accrued yield) | ~$1.05 | ~$1.0x | ~$1.0x (sUSDe) |
| **Primary risk** | Basket composition / RWA credit | Rate + custody | DAI peg / DSR policy | Funding-rate / basis blowout |

USP's edge is **yield optimization across sources**; its corresponding risk is that holders cannot easily audit or control what the basket is exposed to at any moment — a governance and transparency dependency that single-strategy dollars (pure T-bill cUSDO, pure DSR sDAI) avoid.

---

## Narrative, category & catalysts

USP rides the **yield-bearing stablecoin** narrative — the fastest-growing stablecoin sub-category, as holders increasingly prefer dollars that pay a return over idle USDC/USDT.

- **Rates & yield spreads:** higher short rates lift the RWA sleeve of the basket; DeFi yields lift the on-chain sleeve. A simultaneous compression of both would slow USP's appreciation.
- **Flight-to-yield in risk-off:** as of 2026-06-23 crypto is in **Extreme Fear** (Fear & Greed 21, market-health 29/100, bottoming/accumulation). De-risking flows into yield-bearing dollars can *grow* this category even as volatile tokens bleed — a structural tailwind for USP-style products.
- **Governance execution:** USP's growth depends on PikuDAO managing the basket competently and transparently; a basket misstep or governance controversy is the key idiosyncratic catalyst (in either direction).

---

## History & timeline

| Date | Event |
|---|---|
| 2025-12-18 | All-time low unit price of $1.03 (early in yield accrual) |
| 2026-03-23 | All-time high unit price of $1.12 |
| 2026-04-09 | Captured in CoinGecko top-1000 listing snapshot (Source: [[coingecko-top-1000-2026-04-09]]) |
| 2026-06-22 | Market snapshot: $1.10, ~$18.28M cap, rank #865 |

> The $1.03→$1.12 range reflects steady yield accrual, not volatility. Only verifiable price/listing events are recorded; protocol milestones will be added as primary Piku sources are ingested.

---

## How & where it's used / Usage playbook

- **On-chain savings tool.** USP's intended use is a simple "buy-and-hold to earn" dollar: acquire it, let the unit price drift up with net basket yield, redeem/sell at the higher value. There is no need to claim or restake.
- **DeFi composability.** As an Ethereum ERC-20, USP can in principle be supplied to lending/LP venues, but its modest ~$18M cap and ~$163K daily volume mean thin secondary liquidity — large exits can trade below accrued value.
- **Playbook:** treat USP as a yield-bearing cash allocation, not a trade. Diligence the **basket composition** (the dominant risk), monitor PikuDAO governance, and prefer primary redemption over the secondary market for size. In the current risk-off regime, the category tailwind is favorable but idiosyncratic basket/governance risk is the thing to watch.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.12 (2026-03-23) |
| **Current vs ATH** | -3.51% |
| **All-Time Low** | $1.03 (2025-12-18) |
| **Current vs ATL** | +5.73% |
| **24h Change** | -0.08% |
| **7d Change** | +0.13% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x098697ba3fee4ea76294c5d6a466a4e3b3e95fe6` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.piku.co/](https://www.piku.co/) |
| **Twitter** | [@piku_dao](https://twitter.com/piku_dao) |
| **Telegram** | [PikuDAO_Group](https://t.me/PikuDAO_Group) (4,144 members) |
| **GitHub** | [https://github.com/piku-dao](https://github.com/piku-dao) |
| **Whitepaper** | [https://docs.piku.co/](https://docs.piku.co/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $163,326.00 |
| **Market Cap Rank** | #863 |
| **24h Range** | $1.07 — $1.09 |
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
- [[stablecoins]]
- [[yield-bearing-stablecoin]]
- [[stablecoin-yields]]
- [[compounding-open-dollar]] — peer T-bill-backed yield dollar
- [[real-world-assets]]
- [[depeg]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge and Piku / PikuDAO public documentation; market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). No additional specific wiki source ingested yet.
