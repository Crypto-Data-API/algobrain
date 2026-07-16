---
title: "Nockchain"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["NOCK"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.nockchain.org/"
related: ["[[base]]", "[[bitcoin]]", "[[crypto-markets]]", "[[depin]]", "[[proof-of-work]]"]
---

# Nockchain

**Nockchain** (ticker **NOCK**) is an L1 blockchain secured by **Zero-Knowledge Proof of Work (ZKPoW)**: nodes produce blocks by competitively mining zero-knowledge proofs rather than hashing arbitrary data, so the [[proof-of-work|proof-of-work]] effort doubles as verifiable computation. NOCK was **fair-launched with no pre-mine in May 2025**. The token's tracked ERC-20 representation lives on [[base|Base]], and NOCK sits in the "useful-PoW" / zk-compute corner of the [[depin|decentralized-compute]] landscape.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | NOCK |
| **Current Price** | $0.039569 |
| **Market Cap** | $87.04M |
| **Market Cap Rank** | #294 |
| **24h Volume** | $2.29M |
| **24h Change** | +7.16% |
| **7d Change** | +13.46% |
| **All-Time High** | $0.2102 (2025-10-17) — **-81.2%** |
| **All-Time Low** | $0.004601 (2026-04-15) |
| **Fully Diluted Valuation** | $169.80M |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the snapshot was taken during an **extreme-fear** tape — the [[fear-and-greed-index|Crypto Fear & Greed Index]] read **23** and conditions were classified as an **established [[bear-market|bear market]]**. NOCK was a notable outperformer on the day (+7%) and week (+13%), continuing to bounce off its April-2026 ATL — but on very thin volume (~$2.3M), which makes such moves easy to manufacture and hard to trust.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~2.20B NOCK |
| **Total Supply** | ~4.29B NOCK |
| **Max Supply** | ~4.29B NOCK (2^32) |
| **Fully Diluted Valuation** | $169.80M |
| **Market Cap / FDV Ratio** | ~0.51 |

Max supply is **4,294,967,296** — exactly 2^32, reflecting the protocol's "scarce hard money" framing (no pre-mine, fair launch). With ~51% of supply circulating, the remaining ~2.1B NOCK is emitted to miners over time as block rewards rather than released from an insider vesting schedule — a different (and arguably cleaner) dilution profile than the airdrop/VC tokens elsewhere in this cohort. See [[token-unlocks]].

### Contract Addresses

| Chain | Address |
|---|---|
| Base | `0x9b5e262cf9bb04869ab40b19af91d2dc85761722` |

---

## Market Structure & Derivatives

**Spot venues.** Exchange coverage is thin: CoinGecko's market data does not surface a major centralized-exchange listing, and most liquidity appears to be on-chain / smaller venues, including the [[base|Base]] ERC-20 representation. The ~$2.29M of 24h volume against an ~$87M cap (~2.6% turnover) is **extremely low** — depth is shallow and slippage on any sizeable order will be severe.

**Derivatives.** No [[hyperliquid|Hyperliquid]] perpetual or verified [[funding-rate]] / open-interest data appears in the snapshot. There is **no recorded perp market** for NOCK; treat it as a spot-only, low-liquidity name where price is driven by thin spot flow rather than leverage/funding dynamics. This makes the +7%/+13% moves easy to manufacture and hard to trust.

---

## Overview

Nockchain produces blocks by mining zero-knowledge proofs in a PoW competition, and is designed so that transaction throughput scales as network difficulty grows — the goal being a high "velocity of money" without bottlenecking. $NOCK is positioned as scarce, fair-launched hard money secured by zk proofs on Nockchain.

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 453 |
| **GitHub Forks** | 199 |
| **Pull Requests Merged** | 37 |
| **Contributors** | 15 |

Repository: [github.com/zorp-corp/nockchain](https://github.com/zorp-corp/nockchain). A modest but real developer footprint for an early protocol.

---

## Valuation Framing (qualitative)

NOCK is valued as an **early, speculative "useful-PoW" / zk-compute experiment** rather than a proven network. Its differentiators are clean: a fair launch with no pre-mine, a hard 2^32 cap framed as "scarce hard money," and the technically ambitious ZKPoW design where mining produces verifiable computation. But the valuation case is dominated by uncertainty — real adoption of the chain is unproven, exchange/liquidity coverage is minimal, and the token has already round-tripped from $0.21 to below $0.005. Trading at a ~$87M cap (FDV ~$170M) and ~81% below ATH, the market is pricing NOCK as a high-risk, narrative-driven [[depin|compute]] bet. A notable structural positive versus peers: the remaining ~49% of supply is **emitted to miners over time**, not unlocked from an insider vesting cliff — a cleaner dilution profile than the airdrop/VC tokens in this cohort, though ongoing miner sell pressure (to cover costs) is its own overhang. Any durable re-rating requires evidence of actual zk-compute demand, not just thin-volume bounces.

---

## Peer Comparison

| Asset | Ticker | Mkt-cap rank | Category | Consensus | Supply | From ATH |
|---|---|---|---|---|---|---|
| **Nockchain** | NOCK | #294 | ZK "useful PoW" / zk-compute | ZKPoW | 2^32 cap, ~51% circ., miner-emitted | -81.2% |
| [[ravencoin]] | RVN | #356 | PoW asset-issuance | PoW (KAWPOW) | 21B cap, ~78% mined | -98.5% |
| [[bitcoin]] | BTC | #1 | Store of value / PoW base | PoW (SHA-256) | 21M cap | below ATH |

Within the PoW cohort, NOCK is the newest and most experimental — its ZKPoW "verifiable computation" framing distinguishes it from classic hashing chains like RVN and BTC, but it carries far less liquidity and a much shorter track record.

---

## Notable History

- **May 2025** — Fair launch with no pre-mine.
- **2025-10-17** — All-time high of **$0.2102**.
- **2026-04-15** — All-time low of **$0.004601** during the deep early-2026 drawdown.
- **2026-06-21** — Trading ~$0.0396, up sharply off the ATL (+13% on the week) but ~81% below ATH; recovery on thin volume.

---

## Risks

- **Very low liquidity.** ~$2.3M daily volume and no verified major-CEX listing mean wide spreads, high slippage, and outsized price swings on small flow — the +7% day / +13% week should be read with that caveat.
- **Niche, unproven tech.** ZKPoW / "useful PoW" is technically ambitious but early; real adoption of the chain is unproven.
- **Severe drawdown history.** A fall from $0.21 to below $0.005 (and a ~81% gap still to ATH) shows how brutal these speculative compute names can be.
- **Miner-emission dilution.** ~2.1B NOCK still to be emitted to miners; ongoing sell pressure from miners covering costs.
- **Market beta.** In an established [[bear-market|bear market]] (F&G 23), illiquid microcaps are the first to be abandoned.

---

## Related

- [[proof-of-work]]
- [[depin]]
- [[base]]
- [[bitcoin]]
- [[ravencoin]]
- [[crypto-markets]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 via cryptodataapi.com / CoinGecko markets data.

## See Also

- [[crypto-markets]]

---
