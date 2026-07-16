---
title: "Ontology Gas"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["ONG", "Ontology Gas"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://ont.io/"
related: ["[[crypto-markets]]", "[[ontology]]"]
---

# Ontology Gas

**Ontology Gas** (ONG) is the **utility / gas token of the [[ontology|Ontology]] network**, one half of Ontology's **dual-token model**. In that model, **ONT** is the staking and governance coin, while **ONG** is the gas-like utility token spent to pay for on-chain operations such as deploying and invoking smart contracts and using network services. ONG is generated over time and periodically released to ONT holders, who can "unbind" and claim accrued ONG. As of 2026-06-21 ONG trades at **$0.04704638**, ranking **#773** by market capitalization (~**$22.2M**).

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

ONG was up **+0.73%** over 24 hours and down **-2.18%** over the trailing week, drifting with a cautious market (BTC ~$64,180; Fear & Greed Index 22 / Extreme Fear).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ONG |
| **Market Cap Rank** | #773 |
| **Market Cap** | $22,230,681 |
| **Current Price** | $0.04704638 |
| **24h Change** | +0.73% |
| **7d Change** | -2.18% |
| **Genesis Date** | 2018-06-30 |
| **Role** | Gas / utility token of the Ontology network (dual-token with ONT) |
| **Website** | [https://ont.io/](https://ont.io/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

[[ontology|Ontology]] is a public, high-performance Layer-1 blockchain that launched its MainNet on **30 June 2018**, with a particular focus on **decentralized identity (DID)** and **trusted data exchange** for businesses. It uses a **dual-token economic model** that deliberately separates the value/staking asset from the cost of using the network:

- **ONT** — the primary coin, used for staking in consensus (VBFT) and on-chain governance. ONT is held and staked; staking ONT generates ONG over time.
- **ONG** — the gas / utility token. It is the unit actually spent to pay for transactions, smart-contract execution, and network services. ONG is released gradually and accrues to ONT holders, who unbind it to claim it.

This separation lets the network keep the "fee currency" (ONG) distinct from the "ownership currency" (ONT), a design also seen (in different forms) in NEO/GAS, from which Ontology drew inspiration. ONG's demand is therefore a function of Ontology's on-chain activity: the more contracts and services run on Ontology, the more ONG is consumed.

---

## Architecture — How the Dual-Token Model Works

Ontology runs on **VBFT**, a consensus that combines Verifiable Random Function (VRF)-based validator selection with Proof-of-Stake and a Byzantine-Fault-Tolerant agreement step. The VRF randomizes which staked nodes propose and verify blocks, which is intended to keep validator selection unpredictable and resistant to manipulation. ONT is the asset staked into this consensus; ONG is the asset spent to use it. Mechanically:

- **ONG is "bonded" to ONT.** ONG is not mined or freely emitted to the market; it is generated on a fixed, decaying schedule and accrues continuously to every address that holds ONT. Holders must actively **claim/unbind** the accrued ONG to make it spendable.
- **ONG is the gas.** All on-chain operations — token transfers, smart-contract deployment and invocation, ONT ID (decentralized identity) and ONT Login operations — are paid in ONG. This is the structural demand sink: any real usage of Ontology consumes ONG.
- **The split insulates the security token.** Because validators secure the chain by staking ONT (not by holding the fee token), the cost of using the network can fluctuate without directly threatening staking economics. This is the same separation-of-concerns logic behind NEO/GAS and, in spirit, [[atomone|AtomOne]]'s ATONE/PHOTON design and [[ethereum|Ethereum's]] post-EIP-1559 fee market.

The practical consequence is that ONG is a pure **derivative claim on Ontology's usage**: it has value only to the extent that activity flows through the chain, and its supply is continuously fed by an emission schedule tied to ONT holdings.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 448.42M ONG |
| **Total Supply** | 800.00M ONG |
| **Max Supply** | 1.00B ONG |
| **Fully Diluted Valuation** | $59.67M |
| **Market Cap / FDV Ratio** | 0.56 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.39 (2018-09-28) |
| **Current vs ATH** | -98.30% |
| **All-Time Low** | $0.0424 (2020-03-13) |
| **Current vs ATL** | +75.95% |
| **24h Change** | -9.16% |
| **7d Change** | +7.36% |
| **30d Change** | +26.37% |
| **1y Change** | -52.31% |

> The 24h/7d/30d/1y figures in this table are from an earlier point-in-time snapshot and differ from the lead-paragraph 2026-06-21 figures (+0.73% 24h / -2.18% 7d); both are preserved as ingested rather than overwritten. ONG remains roughly 98% below its 2018 ATH.

---

## Value Accrual & Governance

ONG's value accrual is unusually clean to describe and unusually hard to grow:

- **Demand side — gas burn.** Every Ontology transaction, smart-contract call, and identity operation is paid in ONG. This is the only fundamental demand sink. It scales directly with on-chain activity, which for an identity/data-focused L1 has remained modest across cycles.
- **Supply side — continuous emission.** ONG is released on a schedule and bonded to ONT holders. This creates a steady stream of newly claimable ONG hitting the market, a structural sell-pressure headwind unless usage-driven burn keeps pace.
- **Governance.** Governance rights reside primarily with **ONT** (the staking/governance coin), not ONG. ONG holders are fee-payers, not protocol voters. This means ONG is closer to a pure utility/commodity token than a governance asset — an important distinction for valuation, since it has no direct claim on protocol direction.

The bottom line: ONG is a leveraged bet on Ontology's blockspace demand, with a built-in dilution drip. Its upside requires Ontology to win meaningful identity/data adoption; its base case is slow bleed driven by emission outpacing usage.

---

## Comparison vs Peer Gas/Utility Tokens

ONG is best compared to other "second token" gas assets in dual-token economies rather than to standalone L1 coins.

| Dimension | **ONG (Ontology)** | NEO GAS | [[ethereum|ETH]] (post-1559) | [[atomone|PHOTON]] (AtomOne) |
|---|---|---|---|---|
| Role | Gas / fee token | Gas / fee token | Gas + base asset (merged) | Fee token (planned) |
| Paired security token | ONT (stake/govern) | NEO (stake/govern) | none — ETH is both | ATONE (stake/govern) |
| How it's obtained | Bonded to ONT holders, claimed | Generated to NEO holders | Bought on market | Minted from ATONE burn (planned) |
| Supply pressure | Continuous emission to ONT | Continuous emission to NEO | Net deflationary via burn | Tied to ATONE supply |
| Governance rights | None (ONT votes) | None (NEO votes) | Full | None (ATONE votes) |
| Underlying chain focus | Identity / data exchange (DID) | Smart-economy / regulated assets | General-purpose | Cosmos neutral hub |

Takeaway: ONG shares the structural drawback of all "pure gas" tokens in a holder-bonded emission model — its supply is continuously fed while its demand depends entirely on a parent chain that has struggled to grow usage. By contrast, ETH solved this by merging the security and fee asset and adding a burn, making blockspace demand directly bullish for the single token.

---

## Narrative, Category & Catalysts

ONG sits in two overlapping but currently out-of-favor buckets: **legacy alt-L1 gas tokens** and **decentralized-identity (DID)** plays. Ontology was an early, well-funded entrant in on-chain identity (ONT ID, ONT Login) and trusted data exchange for enterprises — a thesis that has periodically returned to favor (e.g., around decentralized-identity, KYC/credentialing, and verifiable-credential narratives) but has not produced sustained ONG demand.

Potential catalysts (speculative): a revival of the on-chain-identity / verifiable-credentials narrative; enterprise or government data-exchange adoption of Ontology; a token-model simplification or burn mechanism that addresses ONG's emission overhang; or pure beta from a broad alt-L1 rotation if BTC exits the current bear regime. As a sub-$25M-cap utility token, ONG primarily trades as a high-beta proxy on risk appetite plus idiosyncratic Ontology-ecosystem news.

---

## History / Timeline

| Date | Event |
|---|---|
| 2018-06-30 | Ontology MainNet launch; ONG genesis as the gas token of the dual-token model |
| 2018-09-28 | ONG all-time high of $4.39, shortly after mainnet launch during the late-2018 cycle |
| 2020-03-13 | All-time low of $0.0424 during the COVID-crash liquidity event |
| 2018–present | Ontology continues building decentralized-identity products (ONT ID, ONT Login) without regaining early-cycle prominence |

> Dates above are from market-data snapshots and widely reported project history. Narrative items without a verifiable date are stated as ranges rather than invented as point dates.

---

## Trading Playbook (current regime)

- **Regime read (2026-06-22).** Broad **Extreme Fear** (Fear & Greed 21), long-horizon **Established Bear**, BTC ~16% below its 200-day MA. ONG is a low-liquidity micro-cap gas token whose price is doubly exposed: to general crypto risk-off and to Ontology's (weak) usage trajectory.
- **What to watch.** BTC reclaiming its 200-day MA (precondition for alt rotation); ONG 24h volume vs its ~$6–7M baseline; any DID-narrative resurgence or Ontology enterprise/data partnership; ONG emission/claim dynamics (large unbinding events can add sell pressure).
- **Structural headwind.** Unlike a fixed-supply token, ONG faces continuous emission bonded to ONT holders, so even flat usage implies a steady supply drip — a reason it can underperform fixed-supply micro-caps in sideways tapes.
- **Bull-case trigger.** A genuine decentralized-identity adoption cycle that drives Ontology blockspace demand (and thus ONG burn) above emission, combined with a BTC trend reversal, would be required to change ONG from a bleed-prone beta trade into a thesis.

---

## Platform & Chain Information

**Native Chain:** Ontology

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ONG/USDT | N/A |
| Upbit | ONG/KRW | N/A |
| Crypto.com Exchange | ONG/USD | N/A |

**How & where it trades.** ONG's primary spot venues are **Binance** (ONG/USDT) and Korea's **Upbit** (ONG/KRW), the latter giving it meaningful Korean-retail flow. Derivatives coverage is thin: ONG perpetuals exist on some venues but carry small open interest and are not the main price-discovery market. At a ~$22M cap with ~$6–7M reported 24h volume, ONG is a low-liquidity altcoin where larger orders incur real slippage and price can move sharply on modest flow.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://ont.io/](https://ont.io/) |
| **Twitter** | [@OntologyNetwork](https://twitter.com/OntologyNetwork) |
| **Reddit** | [https://www.reddit.com/r/OntologyNetwork/](https://www.reddit.com/r/OntologyNetwork/) |
| **Telegram** | [OntologyNetwork](https://t.me/OntologyNetwork) (17,133 members) |
| **Discord** | [https://discordapp.com/invite/4TQujHj](https://discordapp.com/invite/4TQujHj) |
| **GitHub** | [https://github.com/ontio/ontology-compiler](https://github.com/ontio/ontology-compiler) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Forks** | 2 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6.73M |
| **Market Cap Rank** | #773 |
| **24h Range** | $0.0747 — $0.0826 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

ONG reached an all-time high above **$4** in September 2018 shortly after the Ontology MainNet launch, then declined more than 98% from that peak as the 2018–2020 bear market and waning attention on identity-focused Layer-1s took hold. Ontology has continued to develop in the decentralized-identity space (ONT ID, ONT Login) but has not regained its early-cycle prominence.

---

## Competitive Position

As the gas token of a mid-tier Layer-1, ONG's fortunes are inseparable from [[ontology|Ontology's]] relevance. Ontology competes for developers and identity/data use cases against far larger smart-contract platforms (Ethereum and its L2s, BNB Chain, Solana) and against dedicated decentralized-identity efforts. Its dual-token design is a clean way to align fee-payers and stakers, but it does not by itself create application demand. ONG accrues value only insofar as real activity flows through Ontology — a niche the chain has struggled to expand since 2018.

---

## Risks

- **Platform dependency** — ONG demand is entirely derivative of Ontology network usage; low on-chain activity means weak structural demand for gas.
- **Layer-1 competition** — Ontology faces intense competition from much larger ecosystems for the same developers and identity use cases.
- **Long downtrend** — Down ~98% from its 2018 ATH with no sustained recovery across cycles.
- **Token-model complexity** — The ONT/ONG split and unbinding mechanics can confuse newcomers and split liquidity/attention across two assets.
- **Microcap volatility** — At ~$22.2M market cap, ONG is a small-cap altcoin prone to sharp drawdowns.

This is not investment advice; figures above are point-in-time market data, not a valuation.

---

## See Also

- [[crypto-markets]]
- [[ontology]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
