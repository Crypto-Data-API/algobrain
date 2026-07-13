---
title: "Fulcrom"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, derivatives]
aliases: ["FUL", "Fulcrom Finance"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://fulcrom.finance/"
related: ["[[crypto-markets]]", "[[perpetual-futures]]", "[[cronos]]", "[[decentralized-exchange]]", "[[defi]]", "[[governance-token]]", "[[gmx]]", "[[gains-network]]", "[[funding-rate]]", "[[oracle]]", "[[leverage]]"]
---

# Fulcrom

**Fulcrom** (FUL) — also known as **Fulcrom Finance** — is a decentralized [[perpetual-futures|perpetual]] and spot [[decentralized-exchange|DEX]] built in the **GMX** mold, deployed primarily on **[[cronos|Cronos]]** and other networks (zkSync, Cronos zkEVM). It lets traders open leveraged positions with low fees and minimal price impact, with all trades and collateral held transparently on-chain. **FUL** is the protocol's native [[governance-token|governance token]], used for staking to earn a share of platform revenue.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* FUL: $0.00091632, rank #948, market cap $15,284,204, 24h +2.02%, 7d -3.13%. Market backdrop: Fear & Greed Index at 21 (Extreme Fear).

As of 2026-06-22, FUL traded at **$0.00091632**, ranked **#948** by market capitalization with a market cap of approximately **$15.28M**. The token ticked up over the prior day — **+2.02% over 24 hours** — but was still **-3.13% over the trailing 7 days** amid an "Extreme Fear" market (Fear & Greed 21). FUL trades far below its 2023 all-time high near $0.04, consistent with the deep de-rating seen across small-cap derivatives tokens.

---

## What Fulcrom Does

Fulcrom is an on-chain [[derivatives]] exchange offering both leveraged [[perpetual-futures]] and spot trading. Perpetual futures are leveraged contracts with no expiry; a [[funding-rate|funding rate]] keeps the perp price aligned with spot. Fulcrom's value proposition mirrors GMX: trade leverage on-chain with low fees and zero (or near-zero) price impact, while keeping collateral self-custodied and verifiable rather than entrusting it to a centralized venue. The team frames decentralization and transparency of fund usage as the core reason for bringing perpetuals on-chain.

Fulcrom launched its beta in early 2023 with an IDO on VVS Finance, and built initial traction in the Cronos ecosystem.

---

## Mechanism and Architecture (GMX-style)

Fulcrom uses the GMX-style **multi-asset liquidity pool** design:

- **Shared liquidity pool** — liquidity providers deposit a basket of assets into a single pool that acts as the counterparty to all traders. LPs earn trading and borrowing fees but take on the pool's net exposure to trader P&L.
- **Oracle pricing / zero price impact** — trades execute at [[oracle]]-fed prices rather than against an order book, so individual trades have little to no price impact and slippage; this is a defining feature of the GMX model and a contrast to [[automated-market-maker|AMM]] constant-product pricing.
- **Leverage and liquidations** — traders post collateral and choose leverage; the protocol charges borrowing fees and liquidates positions that fall below maintenance margin.
- **Multi-chain** — beyond Cronos, Fulcrom has extended to zkSync and Cronos zkEVM, broadening its reach.

The trade-off of the pooled model is that liquidity providers are effectively the house: when traders win net, the pool loses, so the design relies on fees and the long-run statistical edge of the pool. This is the same structural risk that affects GMX-style venues and pooled perp DEXs like [[myx-finance|MYX]].

### The liquidity pool (GLP-style) in depth

Fulcrom mirrors [[gmx|GMX]]'s **GLP** design with its own pooled-liquidity token (the protocol's "FLP"-style basket):

- **Basket of assets** — LPs mint the pool token by depositing into a multi-asset basket (majors like BTC/ETH plus stablecoins). The basket's composition is rebalanced via mint/redeem fees that nudge it toward target weights.
- **LPs are the counterparty** — every leveraged trade is taken *against the pool*, so the pool's value rises when traders lose (fees + trader losses) and falls when traders win. LPs earn a share of **trading fees, borrowing fees, and liquidation proceeds** in exchange for bearing this net P&L exposure.
- **Borrowing fee instead of pure funding** — in the GMX model, leveraged positions pay an ongoing **borrowing fee** based on how much of the pool's assets they are utilizing, on top of (or in place of) a classic [[funding-rate|funding rate]]. This compensates LPs for the assets locked behind a position.
- **Oracle execution** — entries, exits, and liquidations price off [[oracle|oracle]] feeds, giving "zero price impact" within open-interest caps but creating a hard dependence on oracle integrity and latency.
- **Open-interest caps & skew** — per-asset OI limits and long/short skew controls cap the pool's directional exposure so a single one-sided move cannot drain it.

### Worked example (illustrative)

A trader posts **$1,000 USDC collateral** and opens a **10x long on ETH** ($10,000 notional):

1. Position opens at the oracle price; the trader pays an opening fee and begins accruing a borrowing fee for utilizing pool assets.
2. If ETH rises **5%**, the $10,000 notional gains ~$500 → roughly a **+50% return on the $1,000 collateral** (before fees).
3. If ETH falls ~**9-10%**, the loss approaches the $1,000 collateral and the position is **liquidated**: the pool keeps the collateral (minus liquidation costs), and the LPs benefit.
4. Across many traders, the pool profits if aggregate trader P&L plus fees is positive — the structural bet behind the GMX/Fulcrom model. *(Illustrative; ignores exact fees and maintenance margin.)*

---

## Token Role: FUL

FUL is Fulcrom's native [[governance-token|governance token]]:

- **Revenue share via staking** — staking FUL lets holders earn a portion of platform revenue (trading/borrowing fees), aligning holders with protocol usage.
- **Governance** — participation in protocol decisions.
- **Ecosystem utility** — additional uses such as trading competitions and points programs.

FUL has a large supply (20B max) with most of it in circulation, so emission-driven dilution is comparatively limited, but the very low per-token price and small market cap make it a high-volatility micro-cap.

### Value accrual & governance in depth

- **Staking for revenue share** — staking FUL (often alongside an escrowed/vesting variant, GMX-style "esFUL") routes a portion of protocol fee revenue to stakers, so FUL's economic value is tied to **platform trading volume and fee generation** rather than fixed emissions.
- **Escrowed tokens & vesting** — like GMX's esGMX, escrowed FUL rewards encourage long-term participation by vesting into liquid FUL over time and/or requiring continued staking, dampening immediate sell pressure.
- **Governance scope** — FUL holders influence supported markets, fee parameters, incentive programs, and chain expansion.
- **Reflexivity & dependence on volume** — because both LP yield and staker yield come from trading activity, FUL value accrual is **pro-cyclical**: it strengthens in high-volume regimes and weakens sharply when perp volume dries up, which is the prevailing condition for small-ecosystem venues in a bear market.

---

## History & Notable Events

- **Early 2023** — Fulcrom launches its beta with an **IDO on VVS Finance** and builds initial traction in the [[cronos|Cronos]] ecosystem as a GMX-style perp DEX. FUL records an all-time high near **$0.04** during the launch period.
- **2023–2024** — expands beyond Cronos to **zkSync** and later **Cronos zkEVM**, broadening distribution; runs trading competitions and points/airdrop campaigns to bootstrap volume.
- **2024 onward** — like most small-cap derivatives tokens, FUL de-rates heavily as perp-DEX liquidity concentrates on larger chains; the protocol continues operating within the Crypto.com-affiliated Cronos ecosystem.

---

## Competitive Position

Fulcrom competes directly with [[gmx|GMX]] (the originator of the multi-asset-pool perp model) and other on-chain perp DEXs, while differentiating through its focus on the [[cronos|Cronos]] and Cronos zkEVM ecosystems — chains affiliated with Crypto.com. That niche provides distribution within the Cronos user base but also ties Fulcrom's growth to a smaller ecosystem than Arbitrum or BNB Chain, where most perp-DEX liquidity concentrates. Sustaining competitive depth against GMX and larger venues is an ongoing challenge.

### Comparison vs perp-DEX peers

| Protocol | Pricing model | LP / counterparty | Primary chains | Token | Niche |
|---|---|---|---|---|---|
| **Fulcrom** | Oracle-priced, GMX-style pool | Multi-asset pool (LPs are the house) | [[cronos\|Cronos]], zkSync, Cronos zkEVM | FUL | Cronos/Crypto.com ecosystem |
| [[gmx\|GMX]] | Oracle-priced (v1 GLP) / hybrid (v2) | GLP / GM pools | [[arbitrum\|Arbitrum]], Avalanche | GMX | Originator of pooled perp model |
| [[gains-network\|Gains (gTrade)]] | Synthetic, oracle-priced | DAI/gToken vault | Polygon, Arbitrum, Base | GNS | Forex/equities + very high leverage |
| [[hyperliquid\|Hyperliquid]] | Central-limit [[order-book\|order book]] | On-chain CLOB / HLP vault | Own L1 | HYPE | High-performance on-chain CLOB |

Fulcrom's model is closest to GMX v1; its distinguishing factor is chain/distribution (Cronos) rather than a novel market structure.

---

## Risks

- **Micro-cap, low-liquidity token** — at ~$15.0M (rank #956) and a sub-cent price, FUL is thinly capitalized and highly volatile; reported token trading volume has been very low, implying poor exit liquidity.
- **Pool/counterparty risk** — in the GMX-style model, liquidity providers bear net trader P&L; sustained trader profitability or oracle issues can impair the pool.
- **Smart-contract and oracle risk** — exploits or [[oracle]] manipulation can cause losses; verify audit status independently.
- **Leverage risk for users** — leveraged perpetuals can be liquidated rapidly, causing total loss of posted collateral.
- **Ecosystem concentration** — heavy reliance on Cronos ties Fulcrom's prospects to that chain's adoption.

> **Data disclaimer:** Figures above are point-in-time market snapshots (2026-06-22) and qualitative descriptions of mechanism. TVL, trading volume, APY, and audit details are not independently verified here and should be confirmed against official documentation and on-chain analytics before any decision.

---

## Platform & Chain Information

**Native Chain:** [[cronos|Cronos]]

### Contract Addresses

| Chain | Address |
|---|---|
| Cronos | `0x83afb1c32e5637acd0a452d87c3249f4a9f0013a` |
| zkSync | `0xe593853b4d603d5b8f21036bb4ad0d1880097a6e` |
| Cronos zkEVM | `0xfb3338e2ca713b344d6a45b36525c3db156e492f` |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Max Supply** | 20.00B FUL |
| **Total Supply** | 20.00B FUL |
| **Market Cap / FDV** | High (most supply circulating) |

*Note: exact circulating supply and FDV change with each snapshot; re-verify at source.*

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair |
|---|---|
| Crypto.com Exchange | FUL/USD |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://fulcrom.finance/](https://fulcrom.finance/) |
| **Twitter** | [@FulcromFinance](https://twitter.com/FulcromFinance) |
| **Telegram** | [FulcromFinance](https://t.me/FulcromFinance) |
| **Discord** | [https://discord.gg/7cTMWnpAfd](https://discord.gg/7cTMWnpAfd) |
| **Docs** | [https://docs.fulcrom.finance](https://docs.fulcrom.finance) |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[perpetual-futures]]
- [[cronos]]
- [[gmx]]
- [[gains-network]]
- [[funding-rate]]
- [[oracle]]
- [[myx-finance]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge; no additional specific wiki source ingested yet.
