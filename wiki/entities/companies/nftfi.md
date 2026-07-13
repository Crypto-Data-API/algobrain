---
title: "NFTfi"
type: entity
entity_type: protocol
founded: 2020
website: "https://nftfi.com"
created: 2026-04-22
updated: 2026-06-11
status: good
tags: [crypto, nft, defi, ethereum, liquidity, derivatives, leverage]
aliases: ["NFTfi.com", "NFT.finance"]
related: ["[[nft]]", "[[nft-trading]]", "[[benddao]]", "[[blend]]", "[[ethereum]]", "[[bored-ape-yacht-club]]", "[[cryptopunks]]", "[[opensea]]"]
---

NFTfi is a peer-to-peer NFT-collateralized lending protocol on [[ethereum|Ethereum]], launched in 2020 and one of the oldest NFT lending venues ("the OG NFT lending protocol"). Borrowers lock an NFT in escrow and receive a loan quoted in wETH, DAI, or USDC from a specific counterparty lender at individually negotiated rates, terms, and durations. There is no auto-liquidation: if the borrower defaults at maturity, the lender receives the NFT.

> **2026 status update:** NFTfi remains active as of mid-2026 and is still positioned as a leading, long-running NFT lending venue (cumulatively $400M+ in loan volume across 40,000+ loans since 2020). Quarterly lending volume in the post-2022 NFT bear market has been a fraction of the 2021-2022 peak (e.g. roughly $36M in Q1 2024). The protocol has raised ~$15M in total funding (including a $6M Series A1) and has pushed into **real-world assets (RWAs)** — partnering with Fabrica to enable loans backed by tokenized real estate, with planned expansion into other tokenized collateral. No shutdown, exploit, or token-trade-path change has been reported (Verified via web search, 2026-06-11).

## How it works

1. A borrower lists an NFT they own (BAYC, CryptoPunks, Azuki, Pudgy Penguins, Art Blocks, etc.) and specifies loan parameters they want — principal, currency, max APR, duration.
2. Lenders browse open requests and submit offers with their own terms (principal, APR, duration). Offers are signed messages held off-chain.
3. The borrower accepts an offer. The NFT transfers into an NFTfi escrow contract, and the loan principal transfers to the borrower.
4. At or before maturity, the borrower can repay (principal + accrued interest) and receive the NFT back.
5. If the borrower does not repay by the expiry block, the lender can call `liquidate`, which transfers the NFT to the lender. There is no partial liquidation, no margin call, and no oracle-triggered event.

Loan durations have historically ranged from 7 to 90 days. Loan-to-value ratios depend entirely on what a given lender is willing to extend against a given NFT; blue-chip collections routinely see LTVs in the 30-60 percent range of their recent floor, though this varies widely with market conditions.

## Fees and structure

- **Borrower fees**: zero platform fee. Borrowers pay only the negotiated interest to the lender.
- **Origination fee**: NFTfi charges a 5 percent fee on the lender's interest (i.e., of the interest the lender earns, 5 percent is diverted to the protocol). The borrower does not see this fee directly.
- No governance token is required to use the protocol. NFTfi has issued its own token in some form but it is not part of the trade path.

## What traders use it for

- **Liquidity without selling** — holders of illiquid blue-chip NFTs use NFTfi to unlock stablecoin or wETH liquidity without triggering a taxable sale or giving up the NFT's upside.
- **Leveraged NFT accumulation** — traders borrow against existing NFT collateral to buy more NFTs, effectively obtaining leverage on the collection.
- **Yield for lenders** — market makers and NFT funds quote competitive loan offers to capture double-digit APRs (or much higher for riskier collateral) with the option to seize quality NFTs if borrowers default.
- **Default-driven acquisition** — some lenders intentionally offer low-ball loans, hoping the borrower will default and they will acquire the NFT below floor. This is sometimes called "predatory" lending by NFT communities.
- **Bridge financing during sales** — sellers use short-duration loans to fund purchases while waiting for other NFTs to sell.

## Risks and limitations

- **Illiquid collateral in a downturn** — the core risk for lenders is that when they seize a defaulted NFT, the floor may have dropped substantially, so the seized NFT is worth less than the principal they extended. Unlike pool-based protocols (see [[benddao]], [[blend]]), there is no Dutch auction or AMM to instantly close out a position; the lender simply owns the NFT.
- **No automatic liquidation** — during a crash, a lender cannot force liquidation before maturity. The borrower may also strategically choose which loans to repay and which to let default, keeping NFTs whose value rose and abandoning those that fell.
- **Manual, per-loan negotiation** — unlike pool-based protocols, liquidity is fragmented across individual offers. Deal terms can vary sharply, and price discovery is slower.
- **Smart contract and custody risk** — the NFT sits in NFTfi's escrow contract during the loan. Any vulnerability or governance failure could compromise collateral.
- **Market-sentiment-driven loan markets** — during bear markets lenders pull offers, causing refinancing to become unavailable and forcing defaults even when the borrower intended to roll.

## Related

- [[benddao]] — peer-to-pool NFT lending with auto-liquidation
- [[blend]] — Blur's perpetual peer-to-peer NFT lending protocol
- [[nft]], [[nft-trading]]
- [[bored-ape-yacht-club]], [[cryptopunks]] — most commonly used collateral collections

## Sources

- NFTfi official site and FAQ: [https://nftfi.com/](https://nftfi.com/), [https://nftfi.com/faq/](https://nftfi.com/faq/)
- DefiLlama — NFTfi TVL/stats: [https://defillama.com/protocol/nftfi](https://defillama.com/protocol/nftfi)
- NFT Plazas — "NFT Lending Protocol NFTfi Hits $15M in Total Funding": [https://nftplazas.com/nftfi-15m-funding/](https://nftplazas.com/nftfi-15m-funding/)
- The Block — "NFT lending protocol NFTfi raises $6 million in series A1 funding": [https://www.theblock.co/post/281577/nft-lending-protocol-nftfi-raises-6-million-in-series-a1-funding](https://www.theblock.co/post/281577/nft-lending-protocol-nftfi-raises-6-million-in-series-a1-funding)
- CoinGecko research — top NFT lending platforms: [https://www.coingecko.com/research/publications/top-nft-lending-platforms](https://www.coingecko.com/research/publications/top-nft-lending-platforms)
- Verified via web search, 2026-06-11
