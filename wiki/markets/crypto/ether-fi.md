---
title: "Ether.fi"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum, lrt, lst, restaking, staking]
aliases: ["ETHFI", "Ether.fi", "EtherFi", "ether.fi", "etherfi"]
entity_type: protocol
founded: 2022
headquarters: "Decentralized"
website: "https://www.ether.fi/"
related: ["[[crypto-markets]]", "[[defi]]", "[[eigenlayer]]", "[[ethereum]]", "[[hyperliquid]]", "[[liquid-staking]]", "[[puffer-finance]]", "[[real-world-assets]]", "[[renzo]]", "[[restaking]]", "[[staking]]"]
---

# Ether.fi

**Ether.fi** (ETHFI) is the largest liquid restaking protocol on [[ethereum|Ethereum]] — users deposit ETH for **eETH** (a rebasing liquid restaking token) or its non-rebasing wrapped variant **weETH** (the form most widely integrated across DeFi money markets and DEX pools), restaked via [[eigenlayer|EigenLayer]] — and since April 2025 it has been pivoting into a full crypto **neobank**, with the ether.fi Cash credit card, yield vaults, and RWA products. For traders, ETHFI is the liquid-restaking governance bellwether: a high-beta ETH-ecosystem token with a DAO buyback program tied to real protocol revenue.

---

## Market Data

| Metric | Value |
|---|---|
| **Current Price** | $0.344297 |
| **Market Cap** | $318,845,452 (~$318.8M) |
| **Market Cap Rank** | #135 |
| **Fully Diluted Valuation** | $343,314,894 (~$343.3M) |
| **24h Volume** | $27,415,525 (~$27.42M) |
| **24h Change** | +1.11% |
| **7d Change** | +8.25% |
| **Circulating Supply** | 927,366,299 ETHFI (~927.4M) |
| **Total Supply** | 998,535,999 ETHFI (~998.5M) |
| **Max Supply** | 1,000,000,000 ETHFI (1.00B) |
| **MC / FDV** | ~0.93 |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Regime context:** The snapshot lands in an **Established Bear Market** with the Crypto Fear & Greed Index at **23 (extreme fear)**. ETHFI is a high-beta ETH-ecosystem token; in risk-off tape it tends to draw down harder than [[ethereum|ETH]] itself. Despite the macro backdrop, ETHFI was modestly green over both the day (+1.11%) and the week (+8.25%) into 2026-06-20 — a bounce off a freshly printed all-time low (see [[#Price History]]). The MC/FDV has tightened to ~0.93 (from ~0.79 in April 2026) as residual unlocks have entered circulation, leaving relatively little remaining dilution overhang versus a year ago.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ETHFI |
| **Market Cap Rank** | #135 (2026-06-20; was ~#121 in April 2026) |
| **Market Cap** | $318.8M (2026-06-20; ~$347M at April 2026 snapshot) |
| **Core products** | eETH/weETH liquid restaking tokens; ether.fi Cash card; Liquid yield vaults; RWA vaults |
| **Categories** | DeFi, Restaking, Liquid Restaking Governance Tokens, Neobank, Binance Launchpool, Arbitrum/Base/Scroll Ecosystems, Consensys Portfolio, OKX Ventures Portfolio |
| **Founded** | 2022 |
| **Website** | [https://www.ether.fi/](https://www.ether.fi/) |

---

## Overview

Ether.fi began as a non-custodial liquid restaking protocol (depositors keep validator keys via dual-key delegation) and grew into one of the largest LRT issuers during the 2024 EigenLayer points meta, culminating in the ETHFI airdrop and Binance Launchpool listing of March 2024. From 2025 it repositioned as an on-chain neobank ("DeFi-native bank account"): spend against crypto collateral with the Cash card, earn restaking and vault yield, with ETHFI as the governance and value-accrual token.

---

## Protocol & Technology

Ether.fi is a **liquid restaking** protocol: it bundles base Ethereum [[staking]] yield with [[restaking]] rewards from [[eigenlayer|EigenLayer]] and packages the position as a freely transferable, DeFi-composable token. The product stack has expanded well past a single LST into a consumer finance layer.

### Liquid restaking tokens: eETH and weETH

| Token | Type | Mechanics | Use |
|---|---|---|---|
| **eETH** | Rebasing LRT | Balance grows daily to reflect accrued staking + restaking rewards (`1 eETH ≈ 1 ETH` peg target) | Native holding; rewards accrue in-wallet |
| **weETH** | Wrapped, non-rebasing LRT | Fixed balance, value-per-token rises over time (like wstETH) | The DeFi-integrated form — collateral in money markets, LP asset in [[automated-market-maker|AMM]] pools, cross-chain bridging |

Depositors send ETH (or an [[liquid-staking|LST]]) and mint eETH; the underlying ETH is staked on [[ethereum|Ethereum]] validators and the validators are **restaked** into [[eigenlayer|EigenLayer]] operators, who secure Actively Validated Services (AVSs) for additional yield. weETH is the wrapped, money-market-friendly representation and is by far the most widely integrated form across [[defi|DeFi]].

### Dual-key delegation (trust-minimization)

Ether.fi is distinctive among [[liquid-staking|liquid staking]] and LRT providers in that depositors retain control of their validator keys via a **dual-key delegation** system: node operators run the validators but cannot unilaterally exit or withdraw, and withdrawal credentials are managed via two separate keys so neither party can rug the other — a stronger trust-minimization property than fully delegated competitors. This non-custodial design is the protocol's core security differentiator versus pooled-custody LSTs/LRTs.

### Liquid Vaults (AVS strategies)

**Liquid Vaults** are curated, professionally managed restaking strategies that bundle exposure across multiple AVSs and DeFi yield sources into a single deposit token, abstracting the complexity of AVS selection, risk weighting, and reward harvesting for the end user.

### ether.fi Cash (neobank)

The **Cash card** lets users spend against their eETH/weETH collateral (a Visa-rail crypto credit/debit card) without unstaking — effectively borrowing against restaked ETH while it keeps earning. This is the centerpiece of the 2025 "DeFi-native bank account" pivot. The Cash product migrated from Scroll to **OP Mainnet** in May 2026 (see [[#Major News & Events (2025–2026)]]).

### RWA vaults

Ether.fi extended into **[[real-world-assets|real-world asset]] (RWA)** yield with tokenized-asset vaults (e.g., a $100M allocation to a Plume RWA vault in June 2026), giving depositors access to institutional-grade tokenized-asset yield alongside restaking returns.

### Competitive landscape

Ether.fi competes primarily with [[renzo|Renzo]], [[puffer-finance|Puffer Finance]], and Kelp DAO in the LRT market, with [[lido-dao|Lido]] as the dominant LST benchmark above the whole category. It tends to lead on TVL and integrations, while Puffer emphasizes validator security and Renzo focuses on cross-chain distribution. See [[#Competitive Positioning]].

---

## Ecosystem & Use Cases

- **eETH / weETH as collateral** — weETH is accepted across major money markets and is a heavily used LP and collateral asset, making it one of the most integrated LRTs in [[defi|DeFi]].
- **Restaking yield stacking** — base [[staking]] + [[eigenlayer|EigenLayer]] [[restaking]] + AVS rewards, optionally layered with Liquid Vault strategies.
- **Spend-while-earning** — the Cash card lets holders consume against restaked ETH collateral without unwinding the yield position.
- **RWA access** — tokenized-asset vaults bring off-chain yield on-chain ([[real-world-assets]]).
- **Governance** — ETHFI holders govern treasury use, buybacks, and protocol parameters.
- **Cross-ecosystem reach** — token deployed on Ethereum, Arbitrum, Base, and Scroll; Cash product on OP Mainnet.

---

## Major News & Events (2025–2026)

- **April 24, 2025** — announced the neobank pivot and rolled out Cash cards in the U.S. (CoinDesk).
- **October 2025** — protocol revenue running at roughly $3.1M/month; the DAO approved allocating up to **$50M of treasury for ETHFI buybacks** when price trades below $3, funded from protocol revenue.
- **May 7, 2026** — migrated the Cash card product from Scroll to **OP Mainnet**, moving ~$220M TVL without pausing ~70,000 active cards across ~300,000 user accounts (The Block).
- **April 30, 2026** — hardened cross-chain bridge security following a $292M industry exploit elsewhere.
- **June 4, 2026** — allocated **$100M to a real-world-asset vault on Plume**, giving users access to institutional-grade tokenized-asset yield ([[real-world-assets]]).

---

## History

| Date | Milestone |
|---|---|
| **2022** | Ether.fi founded as a non-custodial liquid staking protocol with dual-key delegation. |
| **2024 (early)** | Rode the [[eigenlayer|EigenLayer]] points meta to become one of the largest LRT issuers; eETH/weETH TVL surged. |
| **2024-03-18** | ETHFI airdrop + **Binance Launchpool** listing; rapid run to the ATH. |
| **2024-03-27** | All-time high **$8.53**. |
| **2025-04-24** | Neobank pivot; **Cash cards** launched in the U.S. |
| **2025-10** | Protocol revenue ~$3.1M/month; DAO authorizes up to **$50M** ETHFI buybacks below $3. |
| **2026-02-06** | Prior ATL $0.3960 amid the deepening bear. |
| **2026-04-30** | Cross-chain bridge security hardened after a $292M industry exploit elsewhere. |
| **2026-05-07** | Cash card migrated Scroll → **OP Mainnet** (~$220M TVL, ~70k active cards, no pause). |
| **2026-06-04** | $100M allocated to a **Plume RWA vault**. |
| **2026-06-05** | New all-time low **$0.268828**. |

---

## Competitive Positioning

ETHFI sits in liquid restaking (LRT), one rung above which is the broader liquid staking (LST) market dominated by [[lido-dao|Lido]].

| Protocol | Type | Key feature | TVL tier | Token |
|---|---|---|---|---|
| **Ether.fi** | Liquid restaking (LRT) | Dual-key delegation (non-custodial); Cash neobank; RWA vaults | LRT leader | ETHFI |
| [[renzo\|Renzo]] | Liquid restaking (LRT) | Cross-chain distribution (ezETH) | Top-tier LRT | REZ |
| [[puffer-finance\|Puffer]] | Liquid restaking (LRT) | Anti-slashing / validator security focus (pufETH) | Mid LRT | PUFFER |
| Kelp DAO | Liquid restaking (LRT) | Multi-asset restaking (rsETH) | Mid LRT | KERNEL |
| [[lido-dao\|Lido]] | Liquid staking (LST) | Category benchmark; largest staked-ETH share (stETH/wstETH) | LST leader (far larger) | LDO |

Ether.fi generally leads the LRT cohort on TVL and integration breadth, with its non-custodial dual-key design and the neobank/Cash + RWA expansion as the main differentiators. The whole LRT category remains structurally downstream of [[eigenlayer|EigenLayer]] AVS demand and ETH staking yield.

---

## Trading Relevance

- **Where it trades**: spot on [[binance|Binance]], [[kraken|Kraken]], Upbit (KRW), Bitget, KuCoin; perps on [[hyperliquid|Hyperliquid]] (ETHFI-PERP); Uniswap V3 on Ethereum.
- **Narrative baskets**: liquid restaking / LRT governance; "DeFi neobank" / on-chain consumer finance; ETH-beta. Tends to trade as high-beta ETH with idiosyncratic catalysts.
- **Key catalysts**: buyback execution (the sub-$3 buyback floor is a stated mechanic — at ~$0.34 in June 2026, buybacks are an active, revenue-funded support), Cash card growth metrics (card count, volume), TVL flows in eETH/weETH, RWA vault expansion, EigenLayer/AVS news.
- **Structural caution**: ~-96% from the March 2024 ATH ($8.53); supply now ~93% circulating (MC/FDV ~0.93 as of 2026-06-20) — the earlier unlock overhang has largely cleared, but the token has retraced to fresh all-time lows in the 2026 bear.

---

## Risks

- **Restaking / slashing risk** — [[eigenlayer|EigenLayer]] AVS participation adds slashing surface beyond base [[staking]]; AVS misbehavior or operator faults could impair eETH/weETH value.
- **Smart-contract & bridge risk** — multi-chain deployment (Ethereum, Arbitrum, Base, Scroll, OP) and cross-chain bridging expand the attack surface; the protocol hardened bridge security in April 2026 after a $292M industry exploit elsewhere.
- **Peg / liquidity risk** — eETH/weETH must hold their ETH peg; depeg events under stress (forced unstaking, withdrawal queues) could cascade through DeFi collateral positions.
- **ETH-beta & macro/regime risk** — as a high-beta ETH-ecosystem token, ETHFI is exposed to the **Established Bear Market** and **extreme-fear** (Fear & Greed 23) regime of 2026-06-20; it drew down to a fresh ATL ($0.268828, 2026-06-05).
- **Revenue dependence** — the buyback floor only supports price if protocol revenue (~$3.1M/mo) and TVL hold up; a revenue contraction weakens the key value-accrual mechanism.
- **Competition** — [[renzo|Renzo]], [[puffer-finance|Puffer]], Kelp DAO, and the dominant LST [[lido-dao|Lido]] compete for restaking/staking share and integrations.
- **Neobank / regulatory risk** — the Cash card and RWA vaults push into regulated payments and tokenized-securities territory, adding compliance and counterparty exposure.
- **Residual dilution** — though largely cleared (~93% circulating), the gap to the 1.00B cap leaves modest remaining supply growth.

---

## Tokenomics & Supply

| Metric | 2026-06-20 | April 2026 snapshot |
|---|---|---|
| **Circulating Supply** | 927,366,299 ETHFI (~927.4M) | 787.26M ETHFI |
| **Total Supply** | 998,535,999 ETHFI (~998.5M) | 998.54M ETHFI |
| **Max Supply** | 1,000,000,000 ETHFI (1.00B) | 1.00B ETHFI |
| **Fully Diluted Valuation** | $343.3M | $440.37M |
| **Market Cap / FDV Ratio** | ~0.93 | 0.79 |

**Supply / dilution read:** Circulating supply has risen from ~787M (April) to ~927M (June), i.e. roughly **93% of max supply is now in circulation** and the MC/FDV ratio has tightened from 0.79 to ~0.93. The earlier unlock overhang has therefore largely cleared — remaining dilution from the gap to the 1.00B cap is comparatively small (~7%), removing one of the structural bearish pressures that weighed on the token through 2024–early 2026.

**DAO buyback program:** up to **$50M of treasury authorized for ETHFI buybacks below $3**, funded by protocol revenue (~$3.1M/month as of Oct 2025). With the 2026-06-20 price (~$0.34) far below the $3 trigger, buybacks are an active, revenue-funded demand sink — a value-accrual mechanism tying token price to real protocol cash flow rather than emissions.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $8.53 (2024-03-27) |
| **Current vs ATH** | ~-96% (2026-06-20) |
| **All-Time Low** | **$0.268828 (2026-06-05)** — new ATL |
| **Prior ATL (historical)** | $0.3960 (2026-02-06) — superseded by the June 2026 low |
| **24h Change** | +1.11% (2026-06-20) |
| **7d Change** | +8.25% (2026-06-20) |

ETHFI printed a fresh all-time low of **$0.268828 on 2026-06-05**, breaking below the prior $0.3960 low (2026-02-06) during the deepening bear market. The 2026-06-20 print of ~$0.34 sits ~28% above that new ATL, with both 24h (+1.11%) and 7d (+8.25%) green — a tentative bounce off the lows even as the broader regime stays risk-off (Fear & Greed 23, extreme fear). The token remains down ~96% from its March 2024 ATH of $8.53.

---

## Platform & Chain Information

**Native Chain:** Ethereum (token also on Arbitrum, Base, Scroll; Cash product on OP Mainnet since May 2026)

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xfe0c30065b384f05761f15d0cc899d4f9f9cc0eb` |
| Scroll | `0x056a5fa5da84ceb7f93d36e545c5905607d8bd81` |
| Base | `0x6c240dda6b5c336df09a4d011139beaaa1ea2aa2` |
| Arbitrum One | `0x7189fb5b6504bbff6a852b13b7b82a3c118fdc27` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Binance | ETHFI/USDT |
| Kraken | ETHFI/USD |
| Upbit | ETHFI/KRW |
| Bitget | ETHFI/USDT |
| KuCoin | ETHFI/USDT |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | ETHFI-PERP | Perpetual |
| Uniswap V3 (Ethereum) | ETHFI/WETH | Spot |

---

## Market Structure & Derivatives

- **Spot venues** — primary CEX liquidity on [[binance|Binance]], [[kraken|Kraken]], Upbit (KRW), Bitget, KuCoin; on-chain spot via Uniswap V3 (ETHFI/WETH) on [[ethereum|Ethereum]].
- **Perpetuals** — the liquid derivatives venue is **ETHFI-PERP on [[hyperliquid|Hyperliquid]]**, with additional perp listings across major offshore CEX venues. As a mid-cap with ~$27M 24h spot volume (2026-06-20), perp depth is moderate — sized entries can move the book.
- **Funding & open interest (metrics to watch, not invented values):** monitor perp **funding rate** sign/magnitude (persistent negative funding flags crowded shorts and squeeze risk; persistent positive funding flags crowded longs), **open interest** trend versus price (rising OI into rising price = conviction; rising OI into falling price = leveraged shorting), and the **OI/market-cap ratio** as a crowding gauge. In extreme-fear regimes funding skews can be sharp on high-beta names like ETHFI.
- **Spot vs derivatives basis** — watch perp price vs spot and the eETH/weETH peg to ETH as secondary signals of stress or demand.

---

## Valuation Framework

ETHFI is unusual among DeFi governance tokens in having an explicit, revenue-funded buyback — so valuation can be anchored to real cash flows rather than emissions narratives. Metrics to track (describe, do not fabricate values):

| Metric | Why it matters |
|---|---|
| **Protocol revenue** | ~$3.1M/month as of Oct 2025; the engine that funds buybacks. Track the monthly run-rate and its trend. |
| **TVL (eETH/weETH + vaults)** | The asset base that generates fee/yield revenue; LRT TVL flows are the leading demand indicator. (Track via Artemis.) |
| **Cash card volume & active cards** | Neobank traction — card count (~70k active, ~300k accounts at May 2026) and spend volume gauge the consumer-finance leg. |
| **Buyback execution** | $ deployed from the $50M authorization while price < $3; an active demand sink. |
| **MC/FDV (~0.93)** | Remaining dilution; now near fully diluted, so price ≈ FDV. |
| **Fee-to-revenue / revenue-to-buyback conversion** | How much revenue actually recycles into ETHFI demand. |

A rough framework: anchor a floor on revenue-funded buyback support, scale upside to TVL growth and Cash adoption, and discount for restaking/AVS slashing risk and ETH-beta drawdowns.

---

## Trading Playbook

- **High-beta ETH proxy** — ETHFI amplifies [[ethereum|ETH]] moves both ways; in extreme-fear/bear tape (the 2026-06-20 regime), expect deeper drawdowns than ETH and sharper relief bounces (cf. the +8.25% 7d off the fresh ATL).
- **Buyback-floor thesis** — with price (~$0.34) far below the $3 buyback trigger, the $50M revenue-funded authorization is a structural bid. A long thesis here leans on (a) buyback execution actually deploying and (b) revenue holding up; the catalyst is reported buyback activity, not price alone.
- **ATL-reclaim watch** — a confirmed reclaim and hold above the prior $0.3960 ATL (now resistance) after basing near the new $0.27 ATL would mark a regime shift; failure back below $0.27 invalidates.
- **Catalyst calendar** — Cash card metrics, TVL flow prints, RWA vault expansion, EigenLayer/AVS news, and buyback disclosures are the idiosyncratic movers.
- **Risk discipline** — moderate perp depth means slippage on size; use [[hyperliquid|Hyperliquid]] funding/OI as a crowding check before entries, and size for the high realized volatility of a sub-$320M-cap token in a bear market.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.ether.fi/](https://www.ether.fi/) |
| **Twitter** | [@ether_fi](https://twitter.com/ether_fi) |
| **Whitepaper** | [https://etherfi.gitbook.io/etherfi/ether.fi-whitepaper](https://etherfi.gitbook.io/etherfi/ether.fi-whitepaper) |

---

## Related

- [[ethereum]], [[eigenlayer]], [[lido-dao]]
- [[liquid-staking]], [[restaking]], [[staking]]
- [[renzo]], [[puffer-finance]] — LRT competitors
- [[hyperliquid]] — perp venue
- [[defi]], [[real-world-assets]], [[stablecoin-yields]]
- [[crypto-narratives-overview]]

---

## Sources

- Market data snapshot, 2026-06-20 (cryptodataapi.com / CoinGecko): price, market cap, rank, FDV, volume, supply, ATH/ATL
- CoinGecko market data snapshot, 2026-04-09 (CoinGecko top-1000 ingest)
- CoinDesk, "Ether.fi Pivots to Become Neobank, Rolls Out Cash Cards in U.S." (2025-04-24) — https://www.coindesk.com/business/2025/04/24/ether-fi-pivots-to-become-neobank-rolls-out-cash-cards-in-u-s
- The Block, "Ether.fi shifts non-custodial crypto card product to OP Mainnet from Scroll" — https://www.theblock.co/post/390420/ether-fi-shifts-non-custodial-crypto-card-product-op-mainnet-scroll
- ether.fi Cash — https://www.ether.fi/cash
- Artemis analytics (TVL/revenue/card volume) — https://classic.artemis.ai/asset/etherfi
- Verified via Perplexity (sonar) + web search, 2026-06-10: OP Mainnet migration May 7 2026, $50M buyback authorization, $100M Plume RWA vault June 4 2026

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 927.37M ETHFI |
| **Total Supply** | 998.54M ETHFI |
| **Max Supply** | 1.00B ETHFI |
| **Fully Diluted Valuation** | $430.12M |
| **Market Cap / FDV Ratio** | 0.93 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $60.68M |
| **Market Cap Rank** | #116 |
| **24h Range** | $0.4124 — $0.4490 |
| **Last Updated** | 2026-07-16 |

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

---
