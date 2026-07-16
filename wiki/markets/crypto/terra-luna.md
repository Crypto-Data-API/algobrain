---
title: "Terra Luna Classic"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [collapse, crypto, defi, luna, stablecoin, terra]
aliases: ["LUNA Classic", "LUNC", "Terra Classic"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.terra-classic.io"
related: ["[[2022-05-terra-luna-depeg-arb]]", "[[crypto-markets]]", "[[defi]]", "[[stablecoins]]", "[[terra-luna-2]]", "[[terra-luna-collapse]]", "[[terrausd]]", "[[three-arrows-capital]]"]
---

# Terra Luna Classic

**Terra Luna Classic** (LUNC) is the original LUNA token, rebranded after the [[terra-luna-collapse|May 2022 collapse]]. Before the crash, LUNA was a top-10 cryptocurrency with a market cap exceeding $41 billion and a price of $119. The token's supply hyperinflated from ~350 million to ~6.5 trillion during the [[terrausd|UST]] death spiral, permanently destroying its value. LUNC now trades at fractions of a cent, sustained primarily by a dedicated community that burns tokens to reduce supply, though the effort is largely symbolic given the scale of dilution.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | LUNC |
| **Current Price** | $0.0000685 |
| **Market Cap** | $378,137,088 |
| **Market Cap Rank** | #122 |
| **24h Volume** | $16,129,301 |
| **24h Change** | -1.00% |
| **7d Change** | -7.25% |
| **All-Time High** | $119.18 (2022-04-05) |
| **Current vs ATH** | -100.0% |
| **All-Time Low** | $0.0000009999 (2022-05-13) |
| **Categories** | Terra Ecosystem, Cosmos Ecosystem, Collapse / post-mortem |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop:** As of 2026-06-20 the market sits in an *Established Bear Market* with the Crypto Fear & Greed Index at **23 (extreme fear)**. LUNC is down -1.0% on the day and -7.25% on the week, in line with risk-off pressure on speculative/meme-like assets. Notably, 24h volume (~$16.1M) is heavy relative to its $378M cap (~4.3% turnover) — characteristic of a community/speculation-driven token where periodic burn campaigns and narratives spike turnover. The price remains **~100% below its 2022 ATH** and the supply story (5.5T circulating) is the defining fact for any holder.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LUNC |
| **Market Cap Rank** | #122 |
| **Market Cap** | $378.14M |
| **Current Price** | ~$0.0000685 |
| **ATH** | $119.18 (2022-04-05) |
| **Current vs ATH** | -100.00% |
| **ATL** | $0.0000009999 (2022-05-13, mid-collapse) |
| **Circulating Supply** | ~5.52T LUNC |
| **Total Supply** | ~6.46T LUNC |
| **Max Supply** | Uncapped |

---

## Protocol / Product

LUNC is the token of **Terra Classic**, the *original* Terra blockchain left running after the network forked in May 2022. Understanding LUNC requires understanding what the chain *was* designed to do — because that design is what destroyed it.

### The original Terra design (pre-collapse)

LUNA was the native governance and staking token of the Terra blockchain. Its primary function was to **stabilize [[terrausd|UST]] (TerraUSD)**, an *algorithmic* (non-collateralized) [[stablecoins|stablecoin]], through a **mint/burn arbitrage mechanism**:

- Users could always **burn $1 of LUNA to mint 1 UST**, and **burn 1 UST to mint $1 of LUNA**.
- If UST traded **above** $1, arbitrageurs burned LUNA to mint UST and sold it, pushing the price down.
- If UST traded **below** $1, arbitrageurs bought cheap UST and redeemed it for $1 of newly minted LUNA, contracting UST supply.

The fatal flaw: the peg depended on LUNA having value, and LUNA's value depended on confidence in UST. When confidence broke, the mechanism minted unlimited LUNA to absorb UST redemptions — the **death spiral**. (For the detailed arbitrage mechanics, see [[2022-05-terra-luna-depeg-arb]].)

### Terra Classic today

After the collapse, the community kept the original chain alive as **Terra Classic**, rebranding LUNA to **LUNC** and UST to **USTC** (TerraClassicUSD). It runs an active validator set on Cosmos/Tendermint infrastructure, but core development is minimal and there is no functioning stablecoin mechanism. The chain's "product" today is effectively a **community-governed, deflation-by-burn speculative token** rather than a working stablecoin platform.

---

## What Happened to LUNA

When UST lost its peg in May 2022, the mint/burn mechanism hyperinflated LUNA's supply by ~18,500x in less than a week:

| Date | LUNA Price | LUNA Supply |
|------|-----------|-------------|
| May 7, 2022 | $80 | ~350 million |
| May 11 | $4.40 | ~1.5 billion |
| May 13 | $0.00001 | ~6.5 trillion |

After the collapse, Do Kwon proposed forking the Terra chain. The community voted to create a new chain ([[terra-luna-2|Terra 2.0 / LUNA]]) without the stablecoin, while the original chain was rebranded to "Terra Classic" with its token renamed LUNC.

For the full crash timeline and contagion cascade, see [[terra-luna-collapse]].

---

## Tokenomics & Supply

| Metric | Value (2026-06-20, CoinGecko) |
|---|---|
| **Circulating Supply** | ~5.52T LUNC |
| **Total Supply** | ~6.46T LUNC |
| **Max Supply** | Uncapped |
| **Fully Diluted Valuation** | ~$442.4M |
| **Market Cap / FDV Ratio** | ~0.85 |

LUNC's supply is the single most important fact about it. The death spiral expanded supply from **~350 million to ~6.5 trillion** — an ~18,500x dilution — which is why a return to pre-crash *price* levels is mathematically impossible without an equally extreme supply contraction.

### The 1.2% burn tax

In September 2022 the community implemented a **1.2% on-chain transaction tax** that burns LUNC on every transfer, with the goal of shrinking the ~6.5T supply over time. Some exchanges (notably Binance, initially) supported applying the burn to trades. The arithmetic, however, is unforgiving: **burning fractions of a percent per transaction against a multi-trillion supply is effectively negligible** — even sustained burn campaigns have removed only a small fraction of supply, and the burn rate has not kept pace with the dilution it is meant to undo. The MC/FDV ratio (~0.85) reflects the ~0.94T gap between total and circulating supply.

---

## Ecosystem & Use Cases

- **Speculative/community token:** LUNC's primary "use" is speculation, driven by burn-campaign narratives and community governance rather than utility.
- **Staking & governance:** LUNC can be staked to validators on the Terra Classic chain; holders vote on chain proposals (including burn parameters and re-peg ideas).
- **No working stablecoin:** USTC remains depegged with no implemented re-peg mechanism, so the chain's original product is non-functional.

---

## Post-Collapse Activity

The Terra Classic community has attempted several recovery initiatives:

- **Tax burn**: the 1.2% on-chain transaction tax (above) — mathematically negligible against a 6.5T supply.
- **Re-peg attempts**: community proposals to re-peg USTC have been discussed but no viable mechanism has been implemented.
- **Governance**: the chain continues to operate with an active validator set, though development activity is minimal.

---

## Market Structure & Derivatives

| Exchange | Pair | Type |
|---|---|---|
| Binance | LUNC/USDT | Spot |
| Bitget | LUNC/USDT | Spot |
| KuCoin | LUNC/USDT | Spot |
| Crypto.com | LUNC/USD | Spot |
| Kraken | LUNA/EUR | Spot |

LUNC trades primarily as a low-price, high-supply spot token on major CEXs, with episodic perpetual/derivatives availability on various venues. Behavior is **low-liquidity, meme-like price action** with occasional spikes on burn announcements or community campaigns. It is loosely correlated to broader crypto markets but dominated by **idiosyncratic, community-driven narratives** rather than fundamentals. The heavy 2026-06-20 turnover (~$16M, ~4.3% of cap) is typical of how speculation concentrates in such tokens.

---

## Valuation Framework (qualitative)

There is **no fundamental valuation thesis** that supports a return to pre-crash levels:

1. **Supply ceiling.** With ~5.5T circulating, even a tiny per-token price implies a multi-hundred-million-dollar cap; reaching $1 would imply a >$5.5T market cap, which is absurd. The supply, not the chain, caps any realistic upside.
2. **Burn-rate reality.** The 1.2% tax cannot meaningfully contract a multi-trillion supply at realistic transaction volumes; the deflation narrative is largely symbolic.
3. **Pure narrative/speculation.** LUNC's price is driven by burn-campaign hype, exchange burn support, and meme-style speculation — not cash flows or adoption.
4. **Optionality only.** Any bull case is lottery-ticket optionality on an extreme, currently-unimplemented supply contraction or re-peg, which has no credible path.

---

## Trading Playbook

- **Treat as a speculative/lottery instrument**, not an investment: position size as you would a meme token you can afford to lose entirely.
- **Burn-campaign momentum.** Short bursts of volume and price often accompany burn announcements or exchange burn-support news; these are momentum events that fade quickly.
- **No mean-reversion-to-ATH thesis.** The price is structurally capped by supply; do not anchor to pre-crash levels.
- **Liquidity/venue:** liquidity is concentrated on a few CEXs; expect sharp, narrative-driven swings and avoid illiquid pairs.
- **Risk-off sensitivity.** As a speculative asset, LUNC underperforms in extreme-fear regimes like the current one.

---

## History

| Date | Event |
|------|-------|
| Apr 5, 2022 | LUNA hits ATH of $119.18 |
| May 7-13, 2022 | [[terra-luna-collapse]]: UST depegs, LUNA hyperinflates from ~350M to ~6.5T supply; LUNC ATL of $0.0000009999 printed May 13 |
| May 28, 2022 | Terra 2.0 fork launches; original chain rebranded to Terra Classic (LUNC) |
| Sep 2022 | Community implements 1.2% burn tax on transactions |
| Mar 2023 | Do Kwon arrested in Montenegro |
| Apr 2024 | SEC finds Terraform Labs liable in civil trial; ~$4.47B settlement |
| Jun 20, 2026 | LUNC ~$0.0000685, market cap $378M, rank #122; ~100% below ATH |

For the full crash timeline and contagion cascade (including [[three-arrows-capital]] and the broader 2022 deleveraging), see [[terra-luna-collapse]].

---

## Competitive Positioning

| Asset | What it is | Relationship to the collapse |
|---|---|---|
| **LUNC** | Original Terra chain token (post-fork) | The hyperinflated survivor; community burn token |
| [[terra-luna-2\|LUNA (Terra 2.0)]] | New chain forked May 2022, no stablecoin | The "fresh start" airdropped to LUNC/UST holders |
| [[terrausd\|USTC]] | Original algorithmic stablecoin (depegged) | The failed peg that triggered the collapse |
| Other algo-stablecoins | Non-collateralized stable designs | LUNC/USTC is the canonical cautionary tale for the category |

LUNC is best understood not as a competitor to live projects but as the **post-mortem artifact** of the largest algorithmic-[[stablecoins|stablecoin]] failure in crypto history. Its only "peer" is its own fork ([[terra-luna-2|LUNA 2.0]]); both trade far below their notional starting value, and the episode permanently discredited uncollateralized algorithmic stablecoin designs.

---

## Risks

- **Supply dilution:** ~5.5T circulating supply makes any price recovery to pre-crash levels mathematically impossible; the burn tax is negligible against this.
- **No fundamental thesis:** no working stablecoin, minimal development; value is pure narrative/speculation.
- **Idiosyncratic / manipulation risk:** thin, community-driven price action is prone to pump-and-dump dynamics.
- **Regulatory/legal overhang:** ongoing fallout from the Terraform Labs litigation and Do Kwon proceedings.
- **Regime beta:** highly sensitive to risk-off conditions like the current Established Bear Market.

---

## See Also

- [[terra-luna-collapse]] — Full crash timeline and analysis
- [[2022-05-terra-luna-depeg-arb]] — The arbitrage death-spiral mechanics
- [[terrausd]] — TerraClassicUSD (USTC), the failed algorithmic stablecoin
- [[terra-luna-2]] — The post-fork Terra 2.0 chain (new LUNA)
- [[stablecoins]] — the asset class the UST failure helped define
- [[three-arrows-capital]] — Hedge fund that collapsed from LUNA exposure
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- CoinGecko / cryptodataapi.com snapshot, 2026-06-20 (market data baseline)
- On-chain supply data from Terra Classic blockchain

## Overview

Terra is a decentralized financial payment network that rebuilds the traditional payment stack on the blockchain. Luna is the reserve currency of the Terra platform. It has three core functions: i) mine Terra transactions through staking, ii) ensure the price stability of Terra stablecoins and iii) provide incentives for the platform’s blockchain validators.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 5.53T LUNC |
| **Total Supply** | 6.45T LUNC |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $380.90M |
| **Market Cap / FDV Ratio** | 0.86 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $119.18 (2022-04-05) |
| **Current vs ATH** | -100.00% |
| **All-Time Low** | $0.00000100 (2022-05-13) |
| **Current vs ATL** | +5796.55% |
| **24h Change** | -1.54% |
| **7d Change** | -4.67% |
| **30d Change** | -16.83% |
| **1y Change** | -6.43% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LUNC/USDT | N/A |
| Kraken | LUNA/USD | N/A |
| Bitget | LUNC/USDT | N/A |
| KuCoin | LUNC/USDT | N/A |
| Crypto.com Exchange | LUNC/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.terra-classic.io](https://www.terra-classic.io) |
| **Twitter** | [@terra_money](https://twitter.com/terra_money) |
| **Reddit** | [https://www.reddit.com/r/terraluna/](https://www.reddit.com/r/terraluna/) |
| **Telegram** | [TerraLunaChat](https://t.me/TerraLunaChat) (45,513 members) |
| **Discord** | [https://terra.sc/classicdiscord](https://terra.sc/classicdiscord) |
| **GitHub** | [https://github.com/classic-terra/core](https://github.com/classic-terra/core) |
| **Whitepaper** | [https://terra.money/static/Terra_White_Paper.pdf](https://terra.money/static/Terra_White_Paper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 78 |
| **GitHub Forks** | 60 |
| **Pull Requests Merged** | 459 |
| **Contributors** | 47 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.86M |
| **Market Cap Rank** | #126 |
| **24h Range** | $0.00005874 — $0.00006065 |
| **CoinGecko Sentiment** | 80% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
