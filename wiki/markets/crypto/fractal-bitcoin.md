---
title: "Fractal Bitcoin"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto]
aliases: ["FB"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://fractalbitcoin.io"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[layer-2]]"]
---

# Fractal Bitcoin

**Fractal Bitcoin** (ticker **FB**) is a [[bitcoin|Bitcoin]] scaling network that runs the Bitcoin Core codebase itself to recursively "virtualize" additional layers on top of the main chain. Rather than a generic sidechain, Fractal aims to extend Bitcoin's computing capacity while staying consistent with Bitcoin's design — it is positioned as the first virtualization methodology applied to Bitcoin. FB sits in the Bitcoin scaling / sidechain category and uses Proof-of-Work, with merge-mining ties to Bitcoin.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | FB |
| **Current Price** | $0.397253 |
| **Market Cap** | $41.54M |
| **Market Cap Rank** | #509 |
| **Fully Diluted Valuation** | $60.31M |
| **24h Volume** | $2.19M |
| **24h Change** | -0.64% |
| **7d Change** | -4.74% |
| **All-Time High** | $38.80 (2024-09-15) |
| **All-Time Low** | $0.334207 (2025-11-22) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

FB trades roughly 99% below its September 2024 all-time high of $38.80 and sits ~19% above its November 2025 all-time low ($0.334). The backdrop is hostile: a [[fear-and-greed-index|Crypto Fear & Greed Index]] of 23 (extreme fear) and an established bear market. Daily volume of ~$2.19M on a ~$42M cap (a turnover ratio near 5%) is modest, indicating relatively thin secondary liquidity, and the 7d change (-4.7%) shows the token still drifting lower with the broad tape.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~104.5M FB |
| **Total Supply** | ~151.8M FB |
| **Max Supply** | 210.00M FB |
| **Market Cap / FDV** | 0.69 |

FB borrows Bitcoin's monetary template: a fixed **210M max supply** (1,000× Bitcoin's 21M) emitted via Proof-of-Work mining with halvings. About 104.5M FB (~50% of max supply) circulates today, with the remainder issued to miners over time rather than vesting to insiders — so the dilution path is emission-driven (predictable, mining-based) rather than a cliff-style investor unlock. The mcap/FDV of 0.69 reflects future mined supply still to enter circulation.

---

## How & Where It Trades

**Centralized exchanges (spot):** FB has a comparatively narrow listing footprint — Kraken (as wrapped WFB/USD) and KuCoin (FB/USDT) are the primary venues. This thinner exchange coverage, combined with low daily volume, makes FB harder to trade in size than the larger L1/L2 tokens.

**Derivatives:** No major perpetual futures market is currently tracked for FB (no Hyperliquid perp, no broad CEX perp coverage). Directional traders are largely limited to spot, which constrains hedging and leverage.

---

## Technology

Fractal Bitcoin's design recursively layers Bitcoin Core instances on top of one another. The base ("Layer-0" Bitcoin) anchors security, while Fractal's own chain runs the same client software to add throughput and programmability without changing Bitcoin's consensus rules. Key technical points:

- **Bitcoin Core fork** — runs the actual Bitcoin codebase, so it inherits Bitcoin's UTXO model and tooling.
- **Merge-mining with Bitcoin** — a portion of blocks is mined jointly with Bitcoin, sharing hashpower/security.
- **Faster blocks** — Fractal targets ~30-second blocks versus Bitcoin's ~10 minutes, raising throughput.
- **Ordinals / metaprotocol support** — Fractal became a hub for Bitcoin-native assets and metaprotocols (e.g., CAT20/BRC-style tokens), giving it a use case beyond payments.

It is best understood as a Bitcoin-aligned scaling/sidechain layer rather than an [[ethereum|Ethereum]]-style L2.

---

## Use Case, Narrative & Category

FB is a **"Bitcoin scaling / Bitcoin DeFi"** narrative play: the thesis that Bitcoin's $1T+ asset base will want native expression layers for tokens, metaprotocols, and higher-throughput activity without bridging to other chains. Its categories include Infrastructure, Smart Contract Platform, Proof of Work, and Bitcoin Sidechains. The bull case is Bitcoin-native asset issuance migrating to a credibly Bitcoin-aligned chain; the bear case is that Bitcoin L2/sidechain demand stays niche and liquidity concentrates elsewhere.

---

## Valuation Framing (Qualitative)

FB's ~$42M market cap and ~$60M FDV reflect a Bitcoin-scaling token whose narrative cooled hard since 2024. Qualitative anchors:

- **Emission-driven dilution is benign** — unlike VC-vested tokens, FB's remaining ~50% of supply is mined to miners with halvings (a [[bitcoin|Bitcoin]]-style schedule), so the MC/FDV gap of 0.69 reflects predictable PoW emission, not cliff unlocks. This is a structurally healthier dilution profile than most peers in this cohort.
- **Activity signal** — for a metaprotocol hub, the real metric is on-chain asset issuance and metaprotocol (CAT20 etc.) volume; FB's value rises and falls with Bitcoin-DeFi / Ordinals enthusiasm.
- **Relative position** — FB competes in a fragmented Bitcoin-scaling field; mindshare and merge-mining hashpower are its differentiators, but liquidity is thin versus general-purpose L1/L2s.

> Framing aid only, not a price target. FB is a cyclical bet on Bitcoin-native asset demand returning.

---

## Peer Comparison

| Token / Network | Approach | Security model | Notes |
|---|---|---|---|
| **Fractal Bitcoin (FB)** | Bitcoin Core fork, recursive virtualization | Merge-mined PoW with Bitcoin | ~30s blocks, Ordinals/CAT20 hub, 210M cap |
| Stacks (STX) | Bitcoin L2, smart contracts | Proof-of-Transfer to Bitcoin | Clarity contracts, sBTC |
| Rootstock (RBTC) | Bitcoin sidechain, EVM | Merge-mined with Bitcoin | EVM-compatible BTC DeFi |
| Merlin Chain | Bitcoin L2 rollup | ZK + Bitcoin DA | Ordinals/BRC-20 focus |
| [[bitcoin\|Bitcoin]] (BTC) | Base chain | Native PoW | The asset Fractal scales |

*FB figures from the 2026-06-21 snapshot; peers qualitative.*

---

## Notable History

- **Mainnet launched 2024**; FB peaked at ~$38.80 on 2024-09-15 during the Bitcoin-L2 / Ordinals enthusiasm cycle.
- Became a focal point for Bitcoin metaprotocol activity and Ordinals-adjacent tokens.
- Endured a >99% drawdown through 2025–2026, bottoming at ~$0.33 on 2025-11-22 as the Bitcoin-scaling narrative cooled.

---

## Risks

- **Liquidity/listing risk** — narrow exchange coverage and low daily volume make entry/exit in size difficult and widen slippage.
- **No derivatives** — absence of a liquid perp market limits hedging and leverage.
- **Narrative fragility** — Bitcoin L2/sidechain interest is cyclical and has cooled sharply since 2024.
- **Competition** — competes with other Bitcoin scaling efforts (Stacks, Merlin, Rootstock, BOB, Babylon-secured chains) for the same limited Bitcoin-DeFi liquidity.
- **Security model nuance** — merge-mining shares hashpower but a Bitcoin-forked sidechain still has a distinct security perimeter from Bitcoin itself.
- **Macro/regime** — extreme-fear sentiment ([[fear-and-greed-index|F&G]] 23) and an established bear market weigh on all small-cap tokens.

---

## Related

- [[bitcoin]] — the base chain Fractal scales and merge-mines with
- [[layer-2]] — the scaling category (Bitcoin-side)
- [[ordinals]] — the Bitcoin-native asset standard Fractal hosts
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 — cryptodataapi.com / CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`)

## See Also

- [[crypto-markets]]

---
