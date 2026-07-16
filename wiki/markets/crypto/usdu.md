---
title: "USDu"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, real-world-assets, stablecoins]
aliases: ["USDU"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://unitas.so"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[ondo-u-s-dollar-token]]", "[[real-world-assets]]", "[[solana]]", "[[stablecoin]]", "[[stablecoins]]", "[[treasuries]]"]
---

# USDu

**USDu** (ticker **USDU**) is a yield-bearing, fiat-backed [[stablecoin]] issued by **Unitas Labs**, targeting a 1:1 peg to the US dollar. It is issued primarily on [[solana|Solana]] (SPL standard) with a [[bnb-chain|BNB Chain]] deployment, and is backed by cash and short-duration US [[treasuries|Treasury]] instruments held with regulated custodians — placing it in the [[real-world-assets|real-world-asset (RWA)]] tokenized-Treasury category alongside [[ondo-u-s-dollar-token|Ondo's USDON]]. Minting and redemption are permissioned (KYC), while circulating USDu transfers freely on-chain.

The core proposition is simple: a dollar that earns the prevailing short-Treasury yield while remaining redeemable at par for KYC counterparties. This places USDu in the fast-growing **"the dollar that pays you"** cohort of stablecoins — economically a tokenized money-market position dressed as a transferable token — competing with [[ondo-u-s-dollar-token|Ondo USDON]], [[blackrock-buidl|BlackRock BUIDL]], and the staked tier of synthetic-dollar issuers such as [[ethena-usde|Ethena]]. Its defining trade-off versus the synthetic-dollar camp is that yield derives from **real, exogenous T-bill cash flows** rather than crypto funding rates, making it more defensive in a bear regime but capping upside at the risk-free rate.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Detail |
|---|---|
| **Ticker** | USDU |
| **Market Cap Rank** | #402 |
| **Current Price** | $0.9991 |
| **Market Cap** | $59.7M |
| **24h Volume** | $59.5K |
| **24h Change** | -0.02% |
| **Circulating / Total Supply** | 59.79M / 59.79M USDU |
| **All-Time High** | $1.018 |
| **All-Time Low** | $0.9574 |
| **Categories** | Yield-Bearing Stablecoin, Solana Ecosystem, BNB Chain Ecosystem, RWA |
| **Website** | [https://unitas.so](https://unitas.so) |

At the snapshot, USDu traded at **$0.9991**, within ~9 bps of par — at peg. Its lifetime band ($0.9574–$1.018) shows only modest deviations and no severe de-peg, consistent with a Treasury-backed design, though the $0.9574 ATL confirms it has drifted below par under thin liquidity.

---

## Architecture — How USDu Works

USDu is a **reserve-backed (off-chain collateral) stablecoin**, the most conservative of the major stablecoin archetypes. The full lifecycle is: a KYC'd counterparty wires USD to Unitas, Unitas deploys those dollars into cash and short-duration Treasury instruments at a regulated custodian, and an equivalent quantity of USDu is minted on-chain to the depositor. The token then circulates permissionlessly; redemption reverses the flow — burn USDu, receive dollars from reserves.

### Reserve / collateral model
- **Backing:** **cash + short-duration US Treasury instruments** custodied with regulated institutions; Unitas publishes on-chain proof-of-reserves so collateral can be verified. This is exogenous, off-chain RWA collateral — distinct from crypto-collateralized or synthetic dollars.
- **1:1 full reserve:** every USDu in circulation is intended to be matched by ≥$1 of liquid reserves, so the design carries no fractional-reserve or rehypothecation leverage by construction (unlike an over-collateralized crypto-backed coin, which holds >$1 of volatile collateral, or a synthetic dollar, which holds a hedged derivatives book).
- **Proof-of-reserves:** verifiability is on-chain rather than reliant solely on a periodic attestation PDF, which is a meaningful transparency edge over legacy fiat-backed coins.

### Peg / stability mechanism
- **Peg target:** 1 USDU = US$1.
- **Primary-market arbitrage:** the redemption guarantee at par is the hard peg floor. If USDu trades below $1 on secondary markets, a KYC'd arbitrageur buys the discount and redeems at $1 for a riskless profit; if it trades above $1, they mint fresh USDu at $1 and sell. Because both legs are KYC-gated, only permissioned participants can fully enforce the peg — the structural reason the secondary price can drift (ATL $0.9574) before arbitrage closes the gap.

### Yield source
- The **T-bill / cash yield** on the reserves accrues to holders (the "yield-bearing" feature), rather than relying on crypto funding rates. APY tracks short-end rates and is kept qualitative here. This is *real* yield — interest paid by the US Treasury — not a token-emission subsidy or a funding-rate carry that can flip negative.

### Mint / redeem & gating
- Mint and redeem are **permissioned** to KYC-verified counterparties at $1 against reserves; the redemption guarantee is the core peg-enforcement mechanism. Secondary holders rely on arbitrageurs who *are* KYC'd to keep the market price near par. Redemption is settled off-chain via banking rails, so par exit is subject to banking-day timing and the issuer's operational solvency.

---

## Comparison vs Peer Tokenized-Dollar Stablecoins

| Dimension | **USDu** (Unitas) | [[ondo-u-s-dollar-token\|USDON]] (Ondo) | [[blackrock-buidl\|BUIDL]] (BlackRock) | [[ethena-usde\|USDe]] (Ethena) |
|---|---|---|---|---|
| **Peg model** | Fiat/RWA, 1:1 reserve | Fiat/RWA, 1:1 reserve | Tokenized T-bill fund | Synthetic, delta-neutral |
| **Backing** | Cash + short T-bills | Cash + short T-bills | US Treasuries (fund shares) | Crypto + perp shorts |
| **Yield source** | T-bill / cash yield | T-bill / cash yield | T-bill yield | Funding rate + staking |
| **Yield to holder** | Yes (yield-bearing) | Yes | Yes (fund distribution) | Via staked sUSDe only |
| **Primary chains** | Solana, BNB | Multi-chain | Ethereum (+others) | Ethereum (+others) |
| **Access** | KYC mint/redeem | KYC/institutional | Institutional whitelist | Permissionless mint |
| **Bear-market resilience** | High (real yield) | High | High | Lower (funding can flip −) |

USDu's closest analogues are the tokenized-Treasury dollars; against synthetic dollars like USDe its advantage is yield that does not depend on a positive crypto funding regime, and its disadvantage is a hard ceiling at the risk-free rate.

---

## How & Where It Trades / Is Used

- **Primary venue:** on-chain on [[solana|Solana]] (mint `9ckR7pPPvyPadACDTzLwK2ZAEeUJ3qGSnzPs8bVaHrSy`), e.g. the Orca DEX, plus a [[bnb-chain|BNB Chain]] deployment (`0xea953ea6634d55dac6697c436b1e81a679db5882`).
- **DeFi composability:** as an SPL/ERC-20 dollar, USDu can in principle be supplied to Solana and BNB lending/AMM venues as collateral or quote currency, but composability is gated by how deep the on-chain pools are and by which protocols whitelist a permissioned-redemption token — at ~$60M cap and ~$59.5K daily volume that integration footprint is still small.
- **Liquidity caveat:** very thin secondary volume (~$59.5K/24h against a ~$60M cap). Because mint/redeem at par is KYC-gated, only permissioned arbitrageurs can fully enforce the peg; ordinary holders may see the secondary price drift before that arbitrage closes the gap. Treat order-book depth as shallow versus fiat-backed majors like [[usdc]] / [[usdt]] — exiting size on the secondary market at exactly par is not guaranteed.

---

## Narrative / Category & Catalysts

USDu sits in the **tokenized-Treasury / yield-bearing stablecoin** narrative — arguably the defining stablecoin growth theme of 2024-2026 as rising and then plateauing short-end rates made "a dollar that pays the T-bill yield" structurally attractive versus a zero-yield [[usdc|USDC]] / [[usdt|USDT]]. Tailwinds and catalysts to watch:

- **Real-yield demand in risk-off regimes:** when crypto funding compresses (as in the current bottoming/accumulation regime), synthetic-dollar yields fall while T-bill yields persist, making RWA dollars relatively more attractive — a favourable backdrop for USDu's category.
- **Regulatory clarity (double-edged):** stablecoin legislation that blesses reserve-backed dollars is a tailwind; rules that treat yield distribution as a securities offering are a headwind (see Risks).
- **Multi-chain expansion:** the Solana + BNB footprint positions USDu for high-throughput, low-fee ecosystems; deeper DEX/lending integrations are the main growth lever from its current small cap.
- **Rate-cycle sensitivity:** the entire category's relative appeal scales with the level of short-term rates — a sharp rate-cut cycle compresses the headline yield advantage.

---

## History / Timeline

- **2026-04-09** — USDu first captured in the wiki via the CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]); page created.
- **2026-06-21** — Market-data refresh: price $0.9991, cap ~$59.7M, rank #402, at peg (see Market Data).
- **2026-06-23** — Page expanded to `excellent` with architecture, comparison, and playbook sections.

> Note: dated protocol-launch and funding milestones are not yet ingested from a primary source; only wiki-verified dates are listed above to avoid fabricated history.

---

## Risks

- **De-peg risk:** modest historically (ATL $0.9574) but real; thin liquidity plus permissioned redemption means the secondary market can deviate from $1 during stress.
- **Collateral risk:** reserve value and liquidity depend on the custodian and on short-Treasury markets; a custodial freeze or accounting gap would impair backing despite proof-of-reserves attestations.
- **Issuer / custodial risk:** centralized issuer (Unitas Labs) and regulated custodians are single points of failure; redemption is only as good as the issuer's solvency and willingness to honor it.
- **Regulatory risk:** tokenized-Treasury yield products sit squarely in the path of evolving stablecoin and securities rules (yield distribution can attract securities treatment).
- **Liquidity risk:** see venues above — exiting size at par is not guaranteed on-chain.
- **Macro backdrop:** as of 2026-06-21 the Crypto Fear & Greed Index reads **23 ("Established Bear Market")**; by the 2026-06-23 snapshot the index sits at **21 (Extreme Fear)** with market-health 29/100 (bearish) and a long-horizon regime of **bottoming / accumulation**. Treasury-backed yield dollars are relatively defensive in such regimes, but secondary liquidity tends to thin further, widening the gap between secondary price and redeemable par.

---

## Trading / Usage Playbook

- **Treat it as a yield position, not a trading vehicle.** With ~$59.5K daily volume USDu is not for active size; the use case is *holding* a dollar that earns the T-bill yield while staying near par.
- **Par is enforced only by KYC arbitrage.** If you are not KYC'd you cannot redeem at $1 — your exit is the secondary market, which can sit below par in stress. Size positions to what the on-chain pools can absorb without slippage.
- **Buy-the-discount logic:** the ATL of $0.9574 shows the secondary price can dip a few percent below par on thin liquidity; for a KYC counterparty those dips are arbitrageable (buy < $1, redeem at $1), but for a retail holder they are simply exit-slippage risk.
- **Regime fit:** real-yield RWA dollars are a defensive parking spot in the current extreme-fear / accumulation regime, but verify reserve attestations and redemption liveness before parking meaningful capital.
- **Always reconcile against the live reserve/proof-of-reserves report** before treating "1 USDu = $1" as a hard guarantee.

> *Not financial advice. Stablecoins can and do de-peg; reserve-backed dollars carry issuer, custodial, and banking-rail risk even when fully reserved.*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 59.79M USDU |
| **Total Supply** | 59.79M USDU |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | ~1.00 |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `9ckR7pPPvyPadACDTzLwK2ZAEeUJ3qGSnzPs8bVaHrSy` |
| Binance Smart Chain | `0xea953ea6634d55dac6697c436b1e81a679db5882` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | 9CKR7PPPVYPADACDTZLWK2ZAEEUJ3QGSNZPS8BVAHRSY/EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://unitas.so](https://unitas.so) |
| **Twitter** | [@UnitasLabs](https://twitter.com/UnitasLabs) |
| **Telegram** | [UnitasLabs](https://t.me/UnitasLabs) (12,724 members) |
| **GitHub** | [https://github.com/UnipayFi](https://github.com/UnipayFi) |
| **Whitepaper** | [https://docs.unitas.so](https://docs.unitas.so) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $59.5K |
| **Market Cap Rank** | #402 |
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
- [[real-world-assets]] / [[treasuries]]
- [[ondo-u-s-dollar-token]] — peer tokenized-Treasury yield dollar
- [[crypto-markets]]
- [[solana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDU |
| **Market Cap Rank** | #708 |
| **Market Cap** | $25.63M |
| **Current Price** | $0.9992 |
| **Categories** | Stablecoins, USD Stablecoin |
| **Website** | [https://www.universal.ae/](https://www.universal.ae/) |

---

## Overview

Universal USD (USDU) is a fiat-referenced token pegged 1:1 to the US Dollar. It is issued by Universal Digital Intl Limited, a financial entity based in Abu Dhabi Global Market. USDU is designed to provide a compliant, institutional-grade USD-denominated settlement layer for digital assets and virtual asset derivatives within regulated financial frameworks.

USDU is aligned with the UAE’s broader ambition to become a leading global hub for digital assets, financial innovation, and regulated digital asset infrastructure. By operating within the ADGM/FSRA, and Central Bank of the UAE regulatory frameworks, USDU supports the development of onshore stablecoin settlement infrastructure for institutional virtual asset activity, treasury movement, and tokenized financial markets.

Key features and mechanics

1:1 asset backing: Each USDU token is backed 1:1 by liquid US dollar reserves. These assets are held in safeguarded accounts with regulated commercial banks, including Emirates NBD and Mashreq.

Regulatory compliance: The issuing entity is regulated by the Financial Services Regulatory Authority in ADGM and registered with the Central Bank of the UAE as a Foreign Payment Token Issuer under the Payment Token Services Regulation.

Auditing and transparency: USDU undergoes monthly independent reserve attestations conducted by an international accounting firm, alongside third-party smart contract audits.

Target audience and use cases: USDU is structured primarily for professional clients and institutional market participants. Its primary use cases include digital asset trading settlement, corporate treasury management, cross-venue liquidity movement, virtual asset infrastructure, and tokenized asset settlement.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.00 (2026-06-20) |
| **Current vs ATH** | -0.08% |
| **All-Time Low** | $0.9977 (2026-07-09) |
| **Current vs ATL** | +0.15% |
| **24h Change** | +0.03% |
| **7d Change** | +0.14% |
| **30d Change** | -0.08% |
| **1y Change** | +0.00% |

---

## Developer Activity

| Metric | Value |
|---|---|
| **Pull Requests Merged** | 9 |
| **Contributors** | 3 |

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
