---
title: "Tensor"
type: entity
entity_type: exchange
founded: 2022
website: "https://www.tensor.trade"
created: 2026-04-22
updated: 2026-06-11
status: good
tags: [crypto, nft, exchange, market-microstructure, liquidity]
aliases: ["Tensor Trade", "TensorTrade", "tensor.trade", "TNSR"]
related: ["[[nft]]", "[[nft-trading]]", "[[magic-eden]]", "[[blur]]", "[[opensea]]", "[[solana]]", "[[sudoswap]]", "[[nft-arbitrage]]"]
---

Tensor is the leading professional-oriented NFT marketplace on Solana, launched in July 2022 and backed by Placeholder VC and Solana Ventures. It combines a traditional orderbook UX with AMM-style liquidity pools, targeting high-frequency NFT traders who need fast execution, deep analytics, and programmatic access. The platform's native token is TNSR, which was airdropped to users in April 2024.

> **2026 status update:** Tensor remains active and dominant on Solana as of mid-2026, reportedly powering 30,000+ collections and capturing roughly 60-70% of Solana NFT trading volume. The major structural change since launch: in **November 2025 the Tensor Foundation acquired the marketplace from Tensor Labs**, redirecting **100% of marketplace fees to the TNSR treasury** (up from 50%) and **burning ~21.6% of the unvested founder/Labs token supply** — a shift favoring token holders. TNSR saw a large speculative price spike in late 2025 (driven by whale/retail flows rather than usage; daily marketplace volume was modest, on the order of tens of thousands of dollars per day in the post-bear NFT market). The 2026 roadmap centers on activating the Tensor DAO and exploring cross-chain tools. No exploit or shutdown reported (Verified via web search, 2026-06-11).

## How it works

Tensor supports two parallel liquidity mechanisms on the same collection:

1. **Orderbook listings** — standard seller-posted fixed-price listings, plus collection-wide bids and trait-level bids from buyers. Sweep, snipe, and bulk-list flows are built in.
2. **AMM pools (TAMM)** — liquidity providers can deposit NFTs or SOL into [[sudoswap]]-style bonding curve pools (linear or exponential). The pool quotes a continuously updated bid/ask, making it an on-chain market maker for the collection.

Because both venues share the same front end, traders see aggregated best bid / best ask across orderbook orders and pool quotes. This hybrid structure is the platform's main differentiator versus pure orderbook venues like [[magic-eden]] and pure AMM protocols like [[sudoswap]].

Execution uses Solana's low-latency, low-fee environment, so actions like multi-NFT sweeps or cancel-and-replace flows are cheap compared to Ethereum-based venues such as [[blur]] or [[opensea]].

## Fees and tokenomics

- Taker fees and creator royalties are both optional/adjustable; Tensor was an early adopter of optional royalty enforcement, mirroring [[blur]]'s stance.
- Protocol fee is modest relative to Ethereum marketplaces (well under 1 percent historically, sometimes waived during incentive periods). Exact rates have shifted with promotions; verify on-platform before sizing trades.
- **TNSR token** — governance token airdropped April 2024. Distributed based on trading activity, liquidity provision, and loyalty program tiers. Used for governance and to accrue platform incentives. Since the November 2025 Tensor Foundation acquisition, **100% of marketplace fees flow to the TNSR treasury** (previously 50%), and ~21.6% of unvested founder/Labs supply was burned.

## What traders use it for

- **Solana NFT sweeps** — bulk-buying floors across [[magic-eden]] and Tensor-listed inventory using the aggregator.
- **Trait sniping** — filtered bids on rare traits within popular Solana collections (Mad Lads, DeGods, Tensorians, SMB, y00ts, etc.).
- **Market making via TAMM pools** — providing two-sided liquidity and earning the spread plus TNSR incentives.
- **Cross-venue arbitrage** — capturing spreads between Tensor orderbook, Tensor pools, and [[magic-eden]]'s Solana book.
- **Programmatic trading** — the Tensor API is widely used by Solana NFT bots for automated bidding and sniping.

## Risks and limitations

- **Chain-specific liquidity** — Tensor only covers Solana NFTs. Ethereum, Bitcoin Ordinals, and other chains require separate venues.
- **Royalty optionality** — creators that depend on royalty income have pushed back on Tensor's royalty-optional default; this is the same ongoing tension that affects [[blur]].
- **Incentive-driven volume** — a meaningful share of historical Tensor volume was driven by TNSR airdrop farming, which can overstate organic liquidity. Always compare activity across pre- and post-airdrop windows.
- **AMM pool risk** — liquidity providers in TAMM pools face the same inventory risk as [[sudoswap]] LPs: if the collection's floor falls persistently, the pool accumulates NFTs at prices above the new floor.
- **Concentrated market maker set** — a small number of sophisticated market makers dominate pool liquidity and orderbook depth on most collections.

## Related

- [[magic-eden]] — primary competitor on Solana
- [[sudoswap]] — the Ethereum AMM protocol that inspired TAMM
- [[blur]] — Ethereum analogue (pro-trader UX, token incentives, optional royalties)
- [[nft-arbitrage]]
- [[nft-trading]]

## Sources

- Tensor official site: [https://www.tensor.trade/](https://www.tensor.trade/)
- Messari — Tensor (TNSR) project page: [https://messari.io/project/tensor](https://messari.io/project/tensor)
- Finance Magnates — "Tensor (TNSR) Surge: Solana's NFT Trader Hub Breaks Out": [https://www.financemagnates.com/trending/tensor-tnsr-surge-solanas-nft-trader-hub-breaks-out-in-style/](https://www.financemagnates.com/trending/tensor-tnsr-surge-solanas-nft-trader-hub-breaks-out-in-style/)
- CoinJournal — "Tensor (TNSR)... soars 152%": [https://coinjournal.net/news/tensor-tnsr-the-solana-nft-marketplace-token-soars-152-heres-why/](https://coinjournal.net/news/tensor-tnsr-the-solana-nft-marketplace-token-soars-152-heres-why/)
- Verified via web search, 2026-06-11
