---
title: "Velodrome Finance"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["VELO", "Velodrome"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://velodrome.finance/"
related: ["[[automated-market-maker]]", "[[concentrated-liquidity]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[optimism]]", "[[ve-tokenomics]]"]
---

# Velodrome Finance

**Velodrome Finance** (VELO) is the central [[decentralized-exchange|decentralized exchange]] and liquidity layer on [[optimism|Optimism]], one of Ethereum's leading [[optimism|Optimistic Rollup]] Layer 2 networks. It implements the "ve(3,3)" or "Solidly-style" model — a fusion of vote-escrow ([[ve-tokenomics|ve-tokenomics]]) governance and game-theoretic emissions — designed to direct liquidity incentives to the pools that generate the most fees and bribes. As of 2026-06-22 VELO trades at **$0.02062073**, ranking **#725** by market capitalization with a market cap of roughly **$25.1M**.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | VELO |
| **Market Cap Rank** | #725 |
| **Market Cap** | ~$25.11M |
| **Current Price** | $0.02062073 |
| **24h Change** | +2.06% |
| **7d Change** | +45.01% (strong weekly rally) |
| **Network** | Optimism (Layer 2) |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi), Optimism Ecosystem |
| **Website** | [https://velodrome.finance/](https://velodrome.finance/) |

> Despite a broad [[crypto-market-regime|risk-off regime]] (BTC ~$64,508 on 2026-06-22; Crypto [[fear-and-greed-index|Fear & Greed Index]] at 21, "Extreme Fear"), VELO posted a notable **+45.01% 7-day** move while most peer DEX tokens were flat-to-down — a sharp outperformance worth treating with caution given the asset's thin liquidity.

---

## Overview

Velodrome Finance is the trading and liquidity marketplace on Optimism. It was launched in mid-2022 by the team behind veDAO, adapting Andre Cronje's unreleased "Solidly" / ve(3,3) design (originally built for [[fantom|Fantom]]) into a polished, sustainable form on Optimism. The protocol's core thesis is that a chain needs a single, deep liquidity hub that aligns the incentives of token emissions with the pools that actually produce trading-fee revenue and protocol bribes, rather than spraying emissions indiscriminately ("mercenary liquidity").

Velodrome is closely associated with **Aerodrome Finance**, its sister deployment on [[base|Base]] (Coinbase's L2). Velodrome's team launched Aerodrome in 2023 as a near-identical ve(3,3) hub for Base; the two are independent protocols with separate tokens (VELO and AERO) but share architecture, codebase lineage (the "Velodrome V2" / Slipstream stack), and design philosophy. Aerodrome subsequently grew into one of the largest DEXs by TVL during Base's expansion.

---

## Mechanism & Architecture

Velodrome's design rests on a few interlocking pieces:

- **veVELO (vote-escrowed VELO):** Users lock VELO for up to 4 years to receive a non-fungible **veVELO** lock (an NFT, not a fungible balance). Longer locks grant more voting power. This is the [[ve-tokenomics|ve-token]] mechanism popularized by Curve's veCRV.
- **Gauge voting:** Each epoch (weekly), veVELO holders vote on which liquidity pool **gauges** receive the next round of VELO emissions. Crucially, voters earn **100% of the trading fees and "bribes" (incentives)** from the specific pools they vote for — so capital is directed to pools that generate the most real revenue.
- **Bribes / incentives:** Protocols that want deep liquidity for their token deposit bribes to attract veVELO votes, creating a marketplace for liquidity. This is the heart of the ve(3,3) "flywheel."
- **Concentrated liquidity (Slipstream):** Velodrome V2 / Slipstream added [[concentrated-liquidity|concentrated-liquidity]] pools (Uniswap V3-style tick ranges) alongside the original [[automated-market-maker|AMM]] stable and volatile pools, improving capital efficiency for LPs.
- **Emissions schedule:** VELO emissions follow a decaying schedule with a rebase mechanism that partially compensates lockers for dilution, aiming for a sustainable equilibrium between emissions and locked supply.

The token's role is therefore primarily **governance and incentive direction** (via locking into veVELO) plus a claim on fees/bribes for active voters — it is not a passive cash-flow token unless locked and voted.

### Worked Example: The ve(3,3) Flywheel

To see why the design is called a "flywheel," follow one epoch:

1. **A protocol wants liquidity.** Say a new Optimism stablecoin, USDx, needs a deep USDx/USDC pool so traders can swap with low slippage.
2. **It posts a bribe.** Instead of running its own multi-million-dollar liquidity-mining program, USDx deposits, say, $10,000 of incentives on the USDx/USDC **gauge** for the coming week.
3. **veVELO lockers vote.** Lockers, seeking the highest yield, direct their votes to the USDx/USDC gauge to capture that $10,000 bribe **plus** that pool's trading fees.
4. **Emissions follow the votes.** Because the gauge received the most votes, the protocol emits a large slice of that week's new VELO to LPs in the USDx/USDC pool — attracting deposits and deepening liquidity.
5. **Deeper liquidity → more volume → more fees → more reason to bribe.** The loop reinforces itself: liquidity goes where it is paid for, VELO emissions are *rented* by protocols via bribes, and lockers earn a blended yield of bribes + fees rather than diluting everyone with untargeted emissions.

The elegance is that **VELO emissions become a market**: protocols effectively pay (in bribes) for the right to direct emissions to their pool, which is far more capital-efficient than the old "mercenary" liquidity-mining model where emissions were sprayed indiscriminately.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | ~1.14B VELO |
| **Total Supply** | ~2.43B VELO |
| **Max Supply** | Unlimited (emissions-based, decaying schedule) |
| **Fully Diluted Valuation** | ~$34M (scales with price) |
| **Market Cap / FDV Ratio** | ~0.47 |

VELO has an unlimited max supply because new tokens are continuously emitted to gauges each epoch; the decaying emissions curve and the rebase-to-lockers mechanism are intended to manage dilution. A large share of supply is typically locked as veVELO, reducing effective circulating float.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.4075 (2024-12-13) |
| **Current vs ATH** | ~-95% |
| **All-Time Low** | $0.00557275 (2022-07-05) |
| **24h Change** | +2.06% |
| **7d Change** | +45.01% |

Like most DeFi governance tokens, VELO sits far below its 2024 ATH after the broad de-rating of mid-cap DeFi. The standout +45.01% weekly gain into 2026-06-22 is unusual against an otherwise risk-off tape (Fear & Greed at "Extreme Fear") and may reflect a rotation into Optimism-ecosystem liquidity tokens, incentive/bribe-cycle dynamics, or simply low-liquidity volatility — it should not be read as a trend without confirmation.

---

## Competitive Position

Velodrome competes with general-purpose AMMs ([[uniswap|Uniswap]], [[sushiswap|SushiSwap]], [[curve-finance|Curve]]) and other ve(3,3) forks. Its differentiation is being the *canonical* liquidity hub for the Optimism ecosystem, with deep integration into OP-native projects and a strong bribe marketplace. Its sister protocol Aerodrome holds an analogous dominant position on Base. Within the Solidly-fork lineage, Velodrome/Aerodrome are widely regarded as the most successful and durable implementations.

### DEX / ve-Model Comparison

| Protocol | Chain(s) | Model | Vote-escrow / governance | Distinctive feature |
|---|---|---|---|---|
| **Velodrome (VELO)** | [[optimism\|Optimism]] | ve(3,3) Solidly fork + Slipstream CL | veVELO NFT, 4-yr max lock, weekly gauge votes | Canonical OP liquidity hub; bribe marketplace; voters get 100% of fees+bribes |
| **Aerodrome (AERO)** | [[base\|Base]] | ve(3,3) (same lineage as Velodrome) | veAERO, identical mechanics | Sister deployment; became a top DEX by TVL during Base's growth |
| **[[curve-finance\|Curve]] (CRV)** | Ethereum + many | StableSwap AMM + veCRV | veCRV, 4-yr max lock; the original ve-model | Stablecoin/pegged-asset specialist; "Curve Wars" bribe origins |
| **[[uniswap\|Uniswap]] (UNI)** | Ethereum + L2s incl. OP | CPMM / V3 concentrated liquidity | UNI token governance (no native ve / fee switch historically off) | Deepest overall liquidity; broadest chain presence |
| **[[sushiswap\|SushiSwap]] (SUSHI)** | Multi-chain | CPMM + xSUSHI fee share | xSUSHI staking (not vote-escrow gauges) | Early Uniswap fork; broad but less focused |

Velodrome's edge is **focus**: rather than competing everywhere, it concentrates on being the single deepest, best-incentivised liquidity venue on one chain, and exports the playbook to Base via Aerodrome.

---

## Governance

Governance flows through **veVELO**. Locking VELO mints a non-fungible veVELO position; longer locks (up to four years) confer more voting power, which **decays** as the lock approaches expiry unless re-locked. Each weekly epoch, veVELO holders cast **gauge votes** that determine where the next emissions go, and those same votes entitle the holder to that pool's fees and bribes. This tightly couples governance with economics: the people steering emissions are exactly the people paid by the pools they choose. The model concentrates influence in large, long-term lockers (the protocol's most aligned stakeholders) but also means a few whales can meaningfully sway emission flows — a recognised centralisation-of-influence trade-off shared across the ve-token family.

---

## Risks

- **Emissions-driven inflation:** Unlimited supply means token value depends on locking demand and real fee/bribe revenue exceeding sell pressure from emissions.
- **Mercenary liquidity:** If bribe yields fall, LPs and voters may exit, draining liquidity quickly.
- **Smart-contract risk:** Complex ve(3,3) + concentrated-liquidity contracts carry exploit risk; the Solidly-fork family has seen bugs in less-audited clones.
- **L2 / sequencer dependence:** Velodrome inherits Optimism's [[optimism|rollup]] trust assumptions (centralized sequencer, upgrade keys).
- **Liquidity / volatility:** A ~$25M-cap, sub-$0.02 token can move violently on small flows, as the +46.8% week illustrates.

---

## Platform & Chain Information

**Native Chain:** Optimistic Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Optimistic Ethereum | `0x9560e827af36c94d2ac33a39bce1fe78631088db` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | VELODROME/USDT | N/A |
| Kraken | VELODROME/USD | N/A |
| Bitget | VELODROME/USDT | N/A |
| Crypto.com Exchange | VELODROME/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://velodrome.finance/](https://velodrome.finance/) |
| **Twitter** | [@VelodromeFi](https://twitter.com/VelodromeFi) |
| **Discord** | [https://discord.com/invite/velodrome](https://discord.com/invite/velodrome) |
| **Whitepaper** | [https://docs.velodrome.finance/](https://docs.velodrome.finance/) |

---

## Trading Characteristics

> *The figures below are a historical April 2026 snapshot, retained for context. Current price/rank/market-cap are in the Key Facts and Market data lines above (2026-06-22).*

| Characteristic | Detail (historical, 2026-04-09) |
|---|---|
| **24h Volume** | $3.02M |
| **Market Cap Rank** | #909 |
| **24h Range** | $0.0139 — $0.0146 |
| **CoinGecko Sentiment** | 100% positive |
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
- [[optimism]]
- [[base]]
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[ve-tokenomics]]
- [[concentrated-liquidity]]
- [[curve-finance]]
- [[uniswap]]
- [[liquidity]]
- [[fear-and-greed-index]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
