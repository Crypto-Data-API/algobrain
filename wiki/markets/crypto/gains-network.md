---
title: "Gains Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives, futures]
aliases: ["GNS", "Gains Network", "gTrade"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://gains.trade/"
related: ["[[arbitrum]]", "[[chainlink]]", "[[crypto-markets]]", "[[derivatives]]", "[[dydx]]", "[[forex]]", "[[fulcrom]]", "[[gmx]]", "[[governance-token]]", "[[hyperliquid]]", "[[leverage]]", "[[perpetual-futures]]", "[[polygon]]"]
---

# Gains Network

**Gains Network** ([[gns|GNS]]) is the [[defi]] protocol behind **gTrade**, a decentralized leveraged-trading platform offering [[perpetual-futures|perpetuals]] and synthetic exposure across crypto, [[forex]], stocks, commodities, and indices. Deployed on [[polygon]] and [[arbitrum]] (and later other chains), gTrade is notable for its **synthetic, oracle-priced architecture**: rather than matching buyers and sellers in an order book or a spot AMM, trades settle against a shared liquidity vault, enabling very high leverage (historically up to ~150x on crypto and far higher on forex) with deep, gas-efficient execution and no [[order-book]].

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* GNS: $0.573076, rank #1000, market cap $13,659,813, 24h -1.76%, 7d -4.45%. Market backdrop: Fear & Greed Index at 21 (Extreme Fear).

As of 2026-06-22, GNS trades at **$0.573076**, ranked **#1000** by market capitalization with a market cap of **$13,659,813**. The token was soft over the short term — **-1.76%** 24h and **-4.45%** 7d — against a weak "Extreme Fear" market backdrop (Fear & Greed 21). GNS remains far below its February 2023 all-time high near $12.48.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | GNS |
| **Market Cap Rank** | #1000 |
| **Market Cap** | $13,659,813 |
| **Current Price** | $0.573076 |
| **24h Change** | -1.76% |
| **7d Change** | -4.45% |
| **Categories** | Decentralized Finance (DeFi), Derivatives, Perpetuals, Polygon Ecosystem, Arbitrum Ecosystem, Base Ecosystem, ApeChain Ecosystem, MegaETH Ecosystem, Base Native |
| **Website** | [https://gains.trade/](https://gains.trade/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Gains Network develops **gTrade**, a decentralized leveraged-trading [[decentralized-exchange|DEX]] for [[perpetual-futures|perpetual]] and synthetic positions. It originated on [[polygon]] and expanded to [[arbitrum]] and additional chains. gTrade lets users trade a wide range of markets — crypto, [[forex]], equities, commodities, and indices — with high [[leverage]] directly from a self-custodied wallet.

The protocol's design avoids both a traditional [[order-book]] and a spot [[automated-market-maker]]. Instead, positions are **synthetic**: trade prices come from decentralized [[chainlink|oracle]] feeds, and profits and losses settle against a shared collateral vault. This makes execution capital-efficient and allows leverage and asset coverage (e.g., forex) that spot AMMs cannot easily provide.

---

## Mechanism & Architecture

- **Synthetic, oracle-priced trading** — entries and exits are priced off aggregated oracle feeds (notably [[chainlink]]) rather than matched against on-chain liquidity, eliminating order-book depth constraints and reducing the spot liquidity normally needed for large markets.
- **The vault (gToken / DAI vault)** — liquidity providers deposit collateral (historically DAI, later GNS-linked gTokens) into a vault that acts as the counterparty to traders. The vault earns when traders lose and pays out when traders win, plus it collects trading fees. This is the core source of LP yield and the core risk for LPs.
- **Risk management** — caps on open interest per asset, dynamic spreads, price-impact and rollover/funding-style fees, and skew controls protect the vault from one-sided exposure.
- **High leverage** — historically up to roughly 150x on crypto and much higher on forex pairs, made feasible by the synthetic model.

### How the vault backstop works

The vault is the heart of gTrade's economics and the source of GNS's value/risk coupling:

1. **LPs deposit collateral** (historically DAI; later GNS-linked gToken vaults such as gDAI) and receive a yield-bearing vault share.
2. **The vault is the counterparty to every trade.** When traders lose, their losses flow into the vault (raising LP value); when traders win, payouts are drawn from the vault.
3. **Over-/under-collateralization buffer.** The vault tracks a collateralization ratio. In good periods it runs *over*-collateralized, building a buffer; sustained trader profits can push it toward *under*-collateralized.
4. **GNS as the elastic backstop.** If the vault would be unable to pay winning traders, **GNS is minted and sold** to top it up; conversely, when the vault is over-collateralized, fees are used to **buy back and burn GNS**. This makes GNS supply **elastic and reflexive** to net trader P&L — the defining feature versus fixed-supply governance tokens.

### Worked example (illustrative)

A trader opens a **50x long on EUR/USD** with **$200 collateral** ($10,000 notional):

1. Entry is priced off the [[chainlink|oracle]] feed (plus spread). The trader pays opening fees and accrues rollover/borrowing-style fees over time.
2. A **0.4%** favorable move in EUR/USD on $10,000 notional ≈ **+$40**, or **+20%** on the $200 collateral (before fees) — illustrating why forex is offered at very high leverage (small percentage moves).
3. A **~2%** adverse move wipes the $200 collateral and triggers liquidation; the vault keeps the collateral.
4. Net: when traders lose in aggregate, the DAI/gToken vault and (via buyback-burn) GNS holders benefit; when traders win in aggregate, the vault pays out and GNS can be minted to cover shortfalls. *(Illustrative; ignores exact fee schedule and maintenance margin.)*

---

## Token Role (GNS)

GNS is the protocol's native [[governance-token]] and value-capture asset:

- **Value accrual / backstop** — GNS is economically tied to the vault: protocol fees and the trader-vs-vault PnL flow influence GNS via the vault's collateralization mechanism, and GNS can be minted/burned to keep the vault solvent. This makes GNS supply variable rather than fixed (max supply is effectively unlimited / elastic).
- **Staking** — GNS holders can stake to earn a share of protocol fees.
- **Governance** — participation in protocol decisions.

Because supply is elastic and tied to vault performance, GNS dilution depends on trading outcomes rather than a fixed emission schedule. Market cap and FDV are near parity.

---

## History & Notable Events

- **2021–2022** — Gains Network launches gTrade on Polygon; migrates branding from the earlier GFARM2 token to **GNS**.
- **2022–2023** — Expands to [[arbitrum]]; grows into one of the larger decentralized perpetual/leverage venues by volume, particularly notable for offering on-chain [[forex]] trading.
- **2023 onward** — Iterates on vault design (gToken vaults), fee mechanics, and multi-chain deployment (Base, ApeChain, MegaETH and others), competing in the crowded perp-DEX sector.

---

## Competitive Position

gTrade competes in the **decentralized perpetuals / derivatives** sector against [[gmx]], [[dydx]], [[hyperliquid]], Vela, Synthetix-based perps, and others. Its distinctive niche is **synthetic, oracle-priced trading with broad non-crypto asset coverage (forex, equities, commodities)** and very high leverage — areas where order-book and spot-AMM perp DEXs are weaker. The trade-off is heavy reliance on oracle integrity and a vault model that concentrates risk in GNS holders/LPs.

### Comparison vs perp-DEX peers

| Protocol | Market structure | Counterparty / liquidity | Asset coverage | Max leverage | Token |
|---|---|---|---|---|---|
| **Gains (gTrade)** | Synthetic, [[chainlink\|oracle]]-priced | DAI/gToken vault + elastic GNS backstop | Crypto, **[[forex]]**, stocks, commodities, indices | Very high (≈150x crypto, far higher FX) | GNS (elastic supply) |
| [[gmx\|GMX]] | Oracle-priced pool (v1) / hybrid (v2) | GLP / GM multi-asset pools | Mostly crypto majors | ~50-100x | GMX (fixed) |
| [[dydx\|dYdX]] | Central-limit [[order-book\|order book]] (own chain) | Pro market makers | Crypto perps | ~20-50x | DYDX |
| [[hyperliquid\|Hyperliquid]] | On-chain CLOB (own L1) | Order book + HLP vault | Crypto perps | ~50x | HYPE |
| [[fulcrom\|Fulcrom]] | Oracle-priced GMX-style pool | Multi-asset pool | Crypto majors | ~50-100x | FUL |

gTrade's clearest differentiator is **non-crypto asset breadth (forex/equities) at high leverage**, which order-book venues like dYdX/Hyperliquid and pool venues like GMX/Fulcrom generally do not match.

---

## Risks

- **Oracle dependence** — because prices come from oracles, manipulation, latency, or feed outages can be exploited or cause mispriced liquidations.
- **Vault / counterparty risk** — LPs (and GNS via the backstop) are the direct counterparty to traders; sustained trader profitability or a single large skewed move can drain the vault and dilute/burn GNS.
- **High-leverage risk** — extreme leverage means liquidations are frequent and gap risk is severe in volatile or thin markets.
- **Smart-contract risk** — complex perp/vault logic across multiple chains.
- **Microcap risk** — at a ~$14M market cap, GNS is small and volatile; price reacts sharply to volume and trader-PnL flows.

This is not investment advice; figures are point-in-time and crypto assets are highly volatile.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 24.56M GNS |
| **Total Supply** | 24.56M GNS |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $17.80M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $12.48 (2023-02-17) |
| **Current vs ATH** | -94.21% |
| **All-Time Low** | $0.2658 (2021-11-29) |
| **Current vs ATL** | +115.6% |
| **24h Change** | -1.76% |
| **7d Change** | -4.45% |

---

## Platform & Chain Information

**Native Chain:** Polygon Pos

### Contract Addresses

| Chain | Address |
|---|---|
| Polygon Pos | `0xe5417af564e4bfda1c483642db72007871397896` |
| Apechain | `0xe31c676d8235437597581b44c1c4f8a30e90b38a` |
| Base | `0xfb1aaba03c31ea98a3eec7591808acb1947ee7ac` |
| Megaeth | `0x551dfe38994ec53c9e7e18084d73893225eea3bf` |
| Arbitrum One | `0x18c11fd286c5ec11c3b683caa813b77f5163a122` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | GNS/USDT | N/A |
| Bitget | GNS/USDT | N/A |
| KuCoin | GNS/USDT | N/A |
| Crypto.com Exchange | GNS/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://gains.trade/](https://gains.trade/) |
| **Twitter** | [@GainsNetwork_io](https://twitter.com/GainsNetwork_io) |
| **Reddit** | [https://www.reddit.com/r/GainsNetwork/](https://www.reddit.com/r/GainsNetwork/) |
| **Telegram** | [GainsNetwork](https://t.me/GainsNetwork) (4,421 members) |
| **Discord** | [https://discord.com/invite/gains-network](https://discord.com/invite/gains-network) |
| **Whitepaper** | [https://gains-network.gitbook.io/docs-home/](https://gains-network.gitbook.io/docs-home/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.573076 |
| **Market Cap** | $13,659,813 |
| **Market Cap Rank** | #1000 |
| **24h Change** | -1.76% |
| **7d Change** | -4.45% |
| **Last Updated** | 2026-06-22 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[polygon]]

---

## Related

- [[perpetual-futures]]
- [[decentralized-exchange]]
- [[derivatives]]
- [[leverage]]
- [[forex]]
- [[chainlink]]
- [[gmx]]
- [[dydx]]
- [[governance-token]]
- [[polygon]]
- [[arbitrum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge; no specific wiki source ingested yet.
