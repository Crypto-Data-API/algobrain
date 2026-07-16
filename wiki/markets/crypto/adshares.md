---
title: "Adshares"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, defi]
aliases: ["ADS"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://adshares.net/"
related: ["[[bnb]]", "[[crypto-markets]]", "[[depin]]", "[[ethereum]]", "[[staking]]"]
---

# Adshares

**Adshares** (ADS) is a decentralized, programmatic advertising protocol — a blockchain-based ad network that lets publishers monetize digital space (websites, blockchain games, NFT exhibitions, metaverse environments) and lets advertisers buy that space without centralized intermediaries. The protocol provides open-source "AdServer" software that anyone can self-host, turning it into a peer-to-peer marketplace for programmatic ad inventory.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* ADS trades at **$0.402906**, ranked **#949** with a market cap of **~$15.61M**. It is essentially flat over 24h (**+0.01%**) and modestly up over the week (**+1.66% / 7d**) — relative stability versus peers during the current Extreme Fear regime (BTC ~$64,180; Fear & Greed 22).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ADS |
| **Market Cap Rank** | #949 |
| **Market Cap** | ~$15.61M |
| **Current Price** | $0.402906 |
| **24h / 7d Change** | +0.01% / +1.66% |
| **Genesis Date** | 2018-08-28 |
| **Categories** | Decentralized Advertising, DeFi, Marketing, BNB Chain Ecosystem, Metaverse, Polygon Ecosystem, Ethereum Ecosystem, Base Ecosystem |
| **Website** | [https://adshares.net/](https://adshares.net/) |

---

## Overview

Adshares is an umbrella protocol for a decentralized advertising network. Where conventional programmatic advertising routes spend through centralized exchanges and intermediaries (with opaque fees and data control), Adshares replaces the middle layer with open-source blockchain tooling. Anyone can deploy their own AdServer, connect to the network, and act as a publisher, advertiser, or both — with [[depin|decentralized]], DAO-style community governance over the protocol.

The original protocol shipped in 2017–2018. It supports a range of placements — standard web display, in-game and NFT-exhibition inventory, and metaverse spaces — making "where ads can live" deliberately broad. The pitch to publishers is reduced intermediary rake and self-custody of inventory; the pitch to advertisers, especially crypto projects, is access to a fully decentralized marketplace that is harder to censor or deplatform.

---

## Architecture & Mechanism (deep dive)

Adshares is a **decentralized programmatic ad exchange** — it tries to replace the centralized SSP/DSP/ad-exchange stack of conventional ad-tech with self-hostable software and on-chain settlement. The moving parts:

1. **AdServer software.** The open-source [AdServer](https://github.com/adshares/adserver) is the network's unit of participation. Anyone can deploy one to act as a **publisher** (listing ad space), an **advertiser** (buying space), or both. Because the software is self-hosted, no central gatekeeper can deplatform a participant — the censorship-resistance pitch that distinguishes it from Google/Meta ad stacks.
2. **AdSelect & AdPay.** The network runs auction/selection logic (matching impressions to campaigns) and a payment/accounting layer that settles advertiser spend to publishers. Settlement reconciles in ADS, so the token is the unit of account for the marketplace; demand for ad inventory therefore translates, in principle, into demand for ADS.
3. **AdUser / targeting.** Targeting and audience data are handled in a way intended to reduce the centralized data-harvesting of mainstream ad-tech — a privacy-adjacent framing.
4. **Own dPoS chain (ADS chain).** Adshares runs its **own high-throughput delegated-proof-of-stake** ([[staking|dPoS]]) blockchain for fast, low-fee transaction settlement, rather than living solely as an ERC-20. The token is then **bridged** to [[ethereum]], [[bnb|BNB Smart Chain]], [[polygon|Polygon]], and [[base|Base]] for liquidity and integrations.

Inventory is deliberately broad — standard web display, in-game and NFT-exhibition placements, and metaverse spaces — so "where an ad can live" is defined widely.

### ADS token role, value accrual & governance

- **Medium of exchange.** Advertising spend settles in ADS, making it the marketplace's unit of account.
- **Deflationary mechanics.** The project describes native **burning and dividend** mechanisms intended to make ADS deflationary, returning a share of protocol activity to holders — a value-accrual design distinct from purely inflationary utility tokens. (The economic significance of these mechanisms depends entirely on real ad-spend volume flowing through the network.)
- **Network/[[staking]] utility.** As a dPoS chain, ADS is staked/delegated to secure the network and participate in consensus.
- **Governance.** Holders steer the protocol through DAO-style governance.

With a circulating-to-FDV ratio near 1.0 there is little dilution overhang — a relative positive for token holders — but the burn/dividend value-accrual story is only as strong as the underlying advertising throughput, which is the central unknown.

---

## Competitive Position

Adshares occupies the decentralized-advertising niche, competing in spirit with both traditional ad-tech (Google's ad exchange, programmatic SSP/DSP stacks) and a small set of Web3 ad protocols. Its edge is being early, fully open-source, and self-hostable; its challenge is that digital advertising is a scale-and-network-effects business, and decentralized alternatives have historically struggled to attract the advertiser demand and quality publisher inventory needed to compete on price and reach.

| Project | Focus | Model | Token | Contrast vs Adshares |
|---|---|---|---|---|
| **Adshares (ADS)** | Decentralized programmatic ad exchange | Self-hosted open-source AdServer; own dPoS chain | ADS (burn/dividend) | Fully self-hostable, censorship-resistant; broad inventory incl. metaverse/NFT |
| **Basic Attention Token (BAT)** | Attention-rewards in the Brave browser | Closed wallet/browser ecosystem | BAT | Distribution via Brave userbase; not a self-hostable open exchange |
| **AdEx (ADX)** | Decentralized ad network / programmatic | On-chain ad protocol | ADX | Similar thesis; different stack and smaller footprint |
| **Google Ad Exchange / The Trade Desk** | Mainstream programmatic ad-tech | Centralized SSP/DSP | none | Massive scale and demand; no token, full intermediary control |

The strategic reality is **network effects favor incumbents**: digital advertising rewards the platform with the most advertiser demand and the best publisher inventory, and decentralized challengers have struggled for years to bootstrap two-sided liquidity at competitive price/reach. BAT's browser-distribution advantage and Google's sheer scale frame the difficulty.

---

## Risks

- **Adoption / network-effects risk.** Advertising is dominated by entrenched platforms; bootstrapping two-sided demand (advertisers and publishers) is hard, and real ad-spend volume is the key unknown.
- **Narrative dependence.** Exposure spans DeFi, metaverse, and decentralized-ad narratives; the metaverse framing in particular has cooled since 2021–22.
- **Low liquidity.** A sub-$16M cap and thin daily volume make ADS volatile and prone to slippage.
- **Long drawdown.** The token sits far below its 2022 ATH, reflecting years of muted adoption relative to expectations.
- **Regulatory / brand-safety risk.** Decentralized ad marketplaces can attract low-quality or non-compliant advertising, a recurring problem for censorship-resistant ad networks.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 38.75M ADS |
| **Total Supply** | 38.76M ADS |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $22.34M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $5.72 (2022-04-03) |
| **All-Time Low** | $0.0103 (2020-09-04) |
| **24h Change** | +0.01% |
| **7d Change** | +1.66% |

> *Current price $0.402906 is far below the 2022 ATH but held up relatively well over the past week, with a near-flat 24h amid Extreme Fear.*

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a` |
| Base | `0xb20a4bd059f5914a2f8b9c18881c637f79efb7df` |
| Polygon Pos | `0x598e49f01befeb1753737934a5b11fea9119c796` |
| Binance Smart Chain | `0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XCFCECFE2BD2FED07A9145222E8A7AD9CF1CCD22A/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

### How & where it trades

| Venue type | Detail |
|---|---|
| **Spot DEX** | [[uniswap\|Uniswap]] V3 (ADS/USDC) on [[ethereum]]; multi-chain ERC-20 representations on [[bnb\|BNB Smart Chain]], [[polygon\|Polygon]], and [[base\|Base]] |
| **Spot CEX** | Has historically appeared on mid-tier centralized venues; depth is thin and the listing set varies |
| **Derivatives** | No meaningful liquid perp/futures market — ADS is effectively spot-only |
| **Liquidity profile** | Very thin — sub-$16M cap with modest daily volume; the multi-chain spread fragments what little liquidity exists |

ADS liquidity is **fragmented across five chains plus its own dPoS chain**, which spreads thin depth even thinner. In practice on-chain liquidity centers on the Ethereum Uniswap pool. As with other micro-cap utility tokens, expect material [[slippage]] on anything beyond small orders and treat fills as the binding constraint (see [[liquidity]]).

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://adshares.net/](https://adshares.net/) |
| **Twitter** | [@adsharesNet](https://twitter.com/adsharesNet) |
| **Reddit** | [https://www.reddit.com/r/adshares/](https://www.reddit.com/r/adshares/) |
| **Telegram** | [adsharesnet](https://t.me/adsharesnet) (713 members) |
| **GitHub** | [https://github.com/adshares/adserver](https://github.com/adshares/adserver) |
| **Whitepaper** | [https://adshares.net/docs/Adshares.Network.whitepaper.pdf](https://adshares.net/docs/Adshares.Network.whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 48 |
| **GitHub Forks** | 18 |
| **Pull Requests Merged** | 1,051 |
| **Contributors** | 8 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.402906 |
| **Market Cap Rank** | #949 |
| **24h Change** | +0.01% |
| **7d Change** | +1.66% |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Narrative, Category & Catalysts

ADS spans **decentralized advertising**, **[[depin|DePIN]]-adjacent infrastructure**, **DeFi**, and (historically) **metaverse** narratives. Its CoinGecko categories include Decentralized Advertising, DeFi, Marketing, Metaverse, plus BNB Chain, Polygon, Ethereum, and Base ecosystem tags.

Catalysts and counter-catalysts:

- **Real ad-spend volume.** The only catalyst that ultimately matters is genuine advertiser demand routing through the network — that is what powers the burn/dividend value-accrual mechanics. Without it, the tokenomics are cosmetic.
- **Crypto-project advertising demand.** Adshares' most natural advertiser base is crypto/Web3 projects that value a censorship-resistant, deplatform-proof channel; bull-market crypto marketing cycles lift this demand.
- **Web3/metaverse narrative cycles.** ADS is high-beta to these themes — but the metaverse framing has cooled markedly since 2021–22, a structural headwind.
- **Privacy/ad-tech regulation.** Tightening privacy rules on mainstream ad-tech (cookie deprecation, data-harvesting limits) could, in theory, favor privacy-adjacent decentralized alternatives.

The recurring counter-narrative is **network effects**: advertising is a scale business, and decentralized ad networks have struggled for years to attract the advertiser demand and quality inventory needed to compete on reach and price.

---

## History & Timeline

Only well-established, dated milestones are listed.

| Date | Event |
|---|---|
| **2017–2018** | Adshares protocol ships; ADS genesis date **2018-08-28** |
| **2020-09-04** | ADS all-time low (~$0.0103) during the pre-bull-market trough |
| **2022-04-03** | ADS all-time high of **$5.72** during the 2021–22 bull/metaverse cycle |
| **2026-06-22** | Trades ~$0.403 (rank #949, ~$15.6M cap), far below ATH, amid an Extreme-Fear macro regime |

(Genesis, ATH/ATL dates from the CoinGecko snapshot; no unverified product-announcement dates asserted.)

---

## Trading Playbook (context: Extreme-Fear bear regime, 2026-06-22)

> *Not investment advice. ADS is a sub-$16M micro-cap with fragmented, thin liquidity.*

- **Regime read.** Established bear market (Fear & Greed 21, BTC ~16% below its 200-day MA). Narrative-dependent ad/metaverse micro-caps are among the weakest cohorts in risk-off tape; the cooled metaverse theme is an added drag.
- **Liquidity & fragmentation.** Depth is split across five chains; the Ethereum Uniswap pool is the practical venue. Size tiny, use limit orders, and assume [[slippage]] on exits.
- **Watch throughput, not charts.** The asymmetric long case is real ad-spend volume activating the burn/dividend mechanics. Absent verifiable spend growth, ADS trades purely on narrative.
- **No hedge.** No liquid derivatives market — exposure is unhedged spot; size for high drawdown given the deep, multi-year discount to ATH.
- **Risk controls.** Define invalidation on the adoption thesis (no ad-volume traction) and brand-safety/regulatory risk specific to decentralized ad networks. In Extreme Fear, prefer regime confirmation over bottom-fishing (see [[risk-management]]).

---

## Related

- [[depin]]
- [[staking]]
- [[crypto-markets]]
- [[ethereum]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original snapshot data
- Market data 2026-06-21 via cryptodataapi.com / CoinGecko
- General market knowledge; no additional specific wiki source ingested yet.

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
