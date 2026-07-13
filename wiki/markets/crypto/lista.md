---
title: "Lista DAO"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, stablecoin, liquidity]
aliases: ["LISTA", "Lista", "Helio Protocol"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://lista.org/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[bnb-chain]]", "[[liquid-staking]]", "[[stablecoin]]", "[[defi]]", "[[maker]]", "[[cdp]]", "[[hyperliquid]]"]
---

# Lista DAO

**Lista DAO** (LISTA) is a [[defi|DeFi]] protocol on [[bnb-chain|BNB Chain]] that combines [[liquid-staking|liquid staking]] of BNB with an over-collateralized [[stablecoin]] (lisUSD) backed by a collateralized-debt-position ([[cdp|CDP]]) engine. It was formerly known as **Helio Protocol** before rebranding to Lista DAO. LISTA trades at **$0.054918**, ranking **#761** by market capitalization (~**$22.74M** market cap), up **+1.21%** over 24h and **+6.25%** over the past 7 days — one of the few green 7-day readings in this cohort against an Extreme-Fear backdrop (BTC ~$64,211; Fear & Greed 21).

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

Lista DAO operates two tightly linked product lines on [[bnb-chain|BNB Chain]]:

- **Liquid staking (slisBNB)** — users stake BNB and receive **slisBNB**, a [[liquid-staking|liquid-staking]] token that accrues BNB staking rewards while remaining usable as collateral and across DeFi. This lets stakers keep liquidity instead of locking BNB.
- **lisUSD CDP stablecoin** — users deposit collateral (including slisBNB and other approved assets) into vaults and mint **lisUSD**, a soft-pegged [[stablecoin]] redeemable against the underlying collateral. The system is over-collateralized, with liquidation mechanics protecting the peg, similar in spirit to [[maker|MakerDAO]]'s DAI but native to BNB Chain.

The combination is the protocol's edge: a user can stake BNB into slisBNB to earn yield, then use that yield-bearing token as collateral to mint lisUSD, layering staking yield with stablecoin liquidity ("looping").

---

## Architecture — How It Works

Lista is effectively a **MakerDAO-style CDP engine plus a Lido-style LST**, fused on BNB Chain:

- **slisBNB liquid staking.** Deposited BNB is delegated to validators; slisBNB is a yield-bearing receipt token whose redemption value grows as staking rewards accrue. It is composable across BNB-chain DeFi and is itself an accepted collateral type inside Lista.
- **lisUSD CDP vaults.** Borrowers lock collateral (slisBNB, BNB, and other approved assets) and mint lisUSD up to a collateral-type-specific limit, paying a **stability fee**. Each collateral type has its own liquidation threshold.
- **Liquidation engine.** When a vault falls below its required collateral ratio, it is liquidated — collateral is auctioned/seized to cover the lisUSD debt, protecting the peg. A sharp BNB drawdown can therefore cascade into mass liquidations (the central tail risk).
- **Peg maintenance.** lisUSD is a soft-pegged, over-collateralized stable: arbitrage around minting (mint and sell when above peg) and redemption/liquidation (when below) keeps it near $1, but it is *not* fiat-backed and can deviate under stress.
- **The "loop."** Stake BNB → get slisBNB (yield) → post slisBNB as collateral → mint lisUSD → optionally redeploy. This stacks staking yield with borrowed stable liquidity but amplifies liquidation sensitivity to BNB price.

---

## History

Lista DAO emerged from a rebrand of **Helio Protocol**, an early BNB Chain CDP-stablecoin project. The relaunch as Lista DAO added the liquid-staking product and the LISTA governance token, which was distributed in part through **Binance Megadrop** (a Binance launch mechanism), giving it broad initial distribution and a Binance listing.

| Date | Event |
|---|---|
| (pre-rebrand) | Launches as **Helio Protocol**, an early BNB Chain CDP stablecoin. |
| (rebrand) | Relaunches as **Lista DAO**, adding slisBNB liquid staking and the LISTA token. |
| (launch) | LISTA distributed via **Binance Megadrop**; Binance listing follows. |
| 2024-06-21 | LISTA all-time high of **$0.8428**. |
| 2026-02-28 | LISTA all-time low of **$0.0772**. |
| 2026-06-21 | Trades ~$0.0549, rank #761, ~$22.7M cap; ~-91% from ATH. |

*Only dated events with on-page provenance are listed; the Helio→Lista rebrand timing is described qualitatively.*

---

## Token Role: LISTA & Value Accrual

LISTA is the governance and incentive token of the protocol:

- **Governance** — holders vote on protocol parameters: collateral types, stability fees, liquidation thresholds, and emissions.
- **Vote-escrow incentives** — Lista uses a vote-escrow style model where locking LISTA grants boosted rewards and governance influence over how emissions/incentives are directed.
- **Liquidity mining** — LISTA is emitted to bootstrap liquidity for slisBNB and lisUSD pools and to reward CDP users.
- **Fee/value capture** — protocol revenue from staking commissions and stablecoin stability fees can be routed back to stakers/lockers, the primary fundamental backing for the token.

### Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 320.16M LISTA |
| **Total Supply** | 795.59M LISTA |
| **Max Supply** | 1.00B LISTA |
| **Fully Diluted Valuation** | $63.13M |
| **Market Cap / FDV Ratio** | 0.40 |

With circulating supply only ~32% of max, future emissions are a meaningful dilution headwind (MC/FDV 0.40).

---

## Competitive Position

Lista competes for BNB liquid-staking share (against other BNB LST providers) and for stablecoin demand on BNB Chain (against centralized stables like USDT/USDC and other CDP stables). Its advantage is the integrated stake-then-borrow loop concentrated on a single high-traffic chain with deep [[bnb|BNB]] liquidity and a Binance distribution channel. Its dependence on a single chain and on BNB's price/health is also its principal concentration risk.

| Protocol | Niche | vs Lista | Trade-off |
|---|---|---|---|
| **Lista DAO** | BNB LST (slisBNB) + lisUSD CDP stable | Integrated stake→borrow loop, Binance distribution | Single-chain / BNB concentration; dilution |
| **[[maker|MakerDAO / Sky]]** | DAI/USDS multi-collateral CDP (Ethereum) | Largest decentralized CDP stable, deep liquidity | Not BNB-native; different collateral set |
| **Lido** (analog) | Liquid staking (ETH stETH) | Category leader for LSTs, but no native CDP stable | Not on BNB; no integrated stable mint |
| **Venus** | BNB-chain money market + VAI stable | BNB-native lending leader | Less LST-integrated than Lista |

See [[liquid-staking]], [[cdp]], [[stablecoin]], and [[maker]].

---

## How & Where It Trades

LISTA has solid centralized liquidity for its cap (Binance, Bitget, KuCoin) plus a [[hyperliquid|Hyperliquid]] perp, so it is more tradeable than most peers in this cohort. The *products* (slisBNB, lisUSD) live on BNB Chain.

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LISTA/USDT | N/A |
| Bitget | LISTA/USDT | N/A |
| KuCoin | LISTA/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | LISTA-PERP | Perpetual |

---

## Narrative, Category & Catalysts

- **Category:** BNB-chain DeFi — liquid staking + CDP stablecoin; a leveraged play on BNB Chain activity and the Binance ecosystem.
- **Bull catalysts:** Growth in BNB staking and slisBNB adoption; rising lisUSD circulation and stability-fee revenue; Binance ecosystem incentives; vote-escrow value routing to LISTA lockers.
- **Bear catalysts:** BNB drawdowns triggering liquidation cascades; lisUSD peg stress; LISTA emission dilution (MC/FDV 0.40); competition from Venus and centralized stables.
- LISTA's relative 7-day strength (+6.25%) in an Extreme-Fear tape is notable but should be read against its heavy drawdown from the 2024 ATH.

---

## Risks

- **Stablecoin peg risk** — lisUSD is a soft-pegged CDP stablecoin; collateral shocks, oracle failures, or a wave of liquidations could break the peg.
- **Collateral concentration** — heavy reliance on BNB/slisBNB means a sharp BNB drawdown can trigger cascading liquidations.
- **Smart-contract & oracle risk** — vaults, the liquidation engine, and price feeds are attack surfaces.
- **BNB Chain dependency** — protocol fortunes are tied to BNB Chain activity and to [[bnb|BNB]] itself.
- **Token performance** — LISTA trades well below its 2024 high amid the broad DeFi-token drawdown; the market backdrop on 2026-06-21 is risk-off ([[bitcoin|BTC]] ~$64,180; Fear & Greed 22, "Extreme Fear"), though LISTA's +6.25% 7-day move is a relative bright spot.

> *Informational only, not investment advice. Crypto assets are highly volatile.*

---

## Trading Playbook

- **Regime behavior:** LISTA is a BNB-chain DeFi beta. It correlates strongly with BNB and BNB-chain activity; the lisUSD CDP engine adds liquidation-cascade tail risk when BNB drops fast. Decent CEX/perp liquidity makes it cleaner to trade than thinner peers, but it remains a high-beta small cap.
- **What to watch:** BNB price (collateral health and liquidation risk); lisUSD peg and circulation; slisBNB staking yield/TVL; LISTA emissions vs locked supply (vote-escrow); BNB-chain TVL trend.
- **In this tape:** Extreme Fear with BNB ≈ $594 means watching collateral ratios closely — a sharp BNB leg down is the main risk to both lisUSD peg and LISTA price. The +6.25% 7-day move is encouraging but fragile; treat LISTA as a leveraged BNB-ecosystem bet and size for liquidation-cascade scenarios.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LISTA |
| **Market Cap Rank** | #761 |
| **Market Cap** | $22,736,819 |
| **Current Price** | $0.054918 |
| **24h Change** | +1.21% |
| **7d Change** | +6.25% |
| **Categories** | Decentralized Finance (DeFi), BNB Chain Ecosystem, Lending/Borrowing Protocols, Liquid Staking Tokens, Binance Megadrop, Liquid Staking |
| **Website** | [https://lista.org/](https://lista.org/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 320.16M LISTA |
| **Total Supply** | 795.59M LISTA |
| **Max Supply** | 1.00B LISTA |
| **Fully Diluted Valuation** | $63.13M |
| **Market Cap / FDV Ratio** | 0.40 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.8428 (2024-06-21) |
| **Current vs ATH** | -90.58% |
| **All-Time Low** | $0.0772 (2026-02-28) |
| **Current vs ATL** | +2.84% |
| **24h Change** | -10.28% |
| **7d Change** | -9.88% |
| **30d Change** | -4.23% |
| **1y Change** | -34.87% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xfceb31a79f71ac9cbdcf853519c1b12d379edc46` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://lista.org/](https://lista.org/) |
| **Twitter** | [@lista_dao](https://twitter.com/lista_dao) |
| **Telegram** | [ListaDAO](https://t.me/ListaDAO) (21,431 members) |
| **Discord** | [https://discord.com/invite/listadao](https://discord.com/invite/listadao) |
| **GitHub** | [https://github.com/lista-dao](https://github.com/lista-dao) |
| **Whitepaper** | [https://docs.bsc.lista.org/](https://docs.bsc.lista.org/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.96M |
| **Market Cap Rank** | #828 |
| **24h Range** | $0.0793 — $0.0901 |
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
- [[bnb]]
- [[bnb-chain]]
- [[liquid-staking]]
- [[stablecoin]]
- [[cdp]]
- [[maker]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; protocol mechanics (slisBNB, lisUSD CDP, Helio rebrand) from public Lista DAO documentation. No additional specific wiki source ingested yet.
