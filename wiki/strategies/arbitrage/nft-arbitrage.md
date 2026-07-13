---
title: "NFT Arbitrage"
type: strategy
created: 2026-04-07
updated: 2026-07-13
status: good
tags: [arbitrage, nft, opensea, blur, marketplace, floor-price, traits, fractionalization, crypto]
aliases: ["NFT Arb", "NFT Marketplace Arbitrage", "NFT Floor Arbitrage"]
strategy_type: algorithmic
timeframe: scalp|day
markets: [crypto]
complexity: advanced
backtest_status: untested
related: ["[[nft-trading]]", "[[nft]]", "[[decentralized-exchanges]]", "[[cross-exchange-arbitrage]]", "[[wash-trading]]", "[[cryptodataapi]]"]
---

# NFT Arbitrage

## Overview

NFT arbitrage exploits price discrepancies for the same non-fungible tokens across different marketplaces. Unlike fungible tokens (where 1 ETH = 1 ETH regardless of venue), each NFT is unique, creating a fragmented and inefficient market where the same collection -- or even the same individual token -- can be listed at significantly different prices on OpenSea, Blur, X2Y2, Magic Eden, and other platforms. The arbitrageur identifies these discrepancies, buys on the cheaper marketplace, and lists or sells on the more expensive one.

Beyond simple cross-marketplace arb, more sophisticated variants include trait-based arbitrage (buying NFTs with rare traits that are priced at or near the collection floor), wrapped/fractionalized NFT arbitrage (exploiting the gap between NFTX or Sudoswap vault token prices and whole NFT prices), and collection-level statistical arb (identifying collections that are underpriced relative to comparable projects). However, NFT arbitrage is significantly riskier than fungible token arbitrage due to illiquidity, high marketplace fees, wash trading that distorts reported prices, and the risk of rug pulls or abandoned projects.

## How It Works

**Cross-marketplace arbitrage:**
1. Monitor floor prices and listings across all major marketplaces in real time via aggregators (Gem, Blur) or custom bots.
2. When the same NFT or comparable floor NFT is listed cheaper on Marketplace A than the floor/best offer on Marketplace B, buy on A and sell on B.

**Trait-based arbitrage:**
1. Analyze rarity scores and trait distributions (using Rarity Sniper or custom scripts).
2. Identify NFTs with rare/desirable traits listed at or near the collection floor price.
3. Buy the underpriced rare NFT and relist at a premium. Requires deep knowledge of which traits the community values.

**Wrapped/fractionalized NFT arbitrage:**
1. Protocols like NFTX and Sudoswap create fungible ERC-20 tokens backed by NFT vaults (e.g., one PUNK token = one redeemable CryptoPunk).
2. If the PUNK token trades below CryptoPunk floor, buy tokens, redeem a Punk, sell at floor. If above floor, deposit a Punk into the vault and sell the tokens.

## Entry/Exit Rules

### Entry
1. **Cross-marketplace:** Buy when the price difference exceeds total fees (marketplace fee + royalty + gas). Thresholds: > 5% for low-floor, > 3% for high-floor collections.
2. **Trait-based:** Buy when a rare-trait NFT is listed within 10% of floor, while comparable rare traits have sold for 2-5x floor recently.
3. **Wrapped arb:** Execute when the redemption value of the vault token differs from the floor price by more than the gas cost + vault fee.
4. **Speed of execution:** Use bots or aggregators. Manual execution is too slow for cross-marketplace arb on popular collections.

### Exit
1. **Immediate resale:** For cross-marketplace arb, list the NFT on the target marketplace immediately after purchase. Accept best offer if one exists above your cost basis.
2. **Trait premium realization:** For trait-based arb, list at a premium and wait for a buyer. This may take days to weeks -- it is a slower arb.
3. **Price reduction:** If the NFT does not sell within 48-72 hours, incrementally reduce the price. Holding illiquid NFTs exposes you to collection-wide price declines.
4. **Stop loss:** If the collection floor drops below your purchase price, evaluate whether to hold (if the trait premium still exists) or cut losses immediately.

## Example Trade

**Cross-marketplace arb:**
1. **Detect:** A Bored Ape Yacht Club (BAYC) NFT is listed on X2Y2 at 28.5 ETH. The floor on Blur is 31.0 ETH with active bids at 30.2 ETH.
2. **Buy on X2Y2** at 28.5 ETH. Gas cost: 0.02 ETH. X2Y2 fee: 0.5% = 0.14 ETH.
3. **Sell on Blur** by accepting the best bid at 30.2 ETH. Blur marketplace fee: 0.5% = 0.15 ETH. Creator royalty: 2.5% = 0.76 ETH.
4. **Gross revenue:** 30.2 ETH.
5. **Total costs:** 28.5 (purchase) + 0.02 (gas buy) + 0.14 (X2Y2 fee) + 0.02 (gas sell) + 0.15 (Blur fee) + 0.76 (royalty) = 29.59 ETH.
6. **Net profit:** 30.2 - 29.59 = **0.61 ETH** (~$2,074 at ETH = $3,400).
7. **Duration:** ~3 minutes from detection to completion.

**Trait-based arb:**
1. A BAYC with the rare "Gold Fur" trait (only 46 exist) is listed at 32 ETH (near the 31 ETH collection floor).
2. Previous Gold Fur sales averaged 55-65 ETH in the past 60 days.
3. **Buy at 32 ETH.** List at 52 ETH (conservative estimate, below recent comparables).
4. **Sells after 5 days** at 48 ETH (buyer negotiated down).
5. **Net profit after fees:** 48 - 32 - fees (~2.5 ETH) = **~13.5 ETH**.

## Risk Management

- **Illiquidity risk:** The greatest risk -- NFTs may not sell for days or weeks. Never arb more than you can afford to hold.
- **Fees eat profits:** Combined marketplace fees (0.5-2.5%) and royalties (0-10%) can consume the spread. Calculate net profit before executing.
- **[[wash-trading]] distorts prices:** Reported volumes are inflated. Verify real buyer diversity before relying on price data.
- **Rug pull and smart contract risk:** Smaller collections may be abandoned; marketplace contracts carry exploit risk.
- **Gas and royalty volatility:** Gas spikes make small arbs unprofitable; royalty enforcement policies differ across platforms.

## Advantages
- **Fragmented market creates persistent opportunities** -- unlike fungible token markets, NFT marketplaces do not share order books
- **Trait-based arb rewards knowledge over speed** -- deep collection expertise is a durable edge over bot-driven strategies
- **Low capital requirement** -- many collections have floor prices under 1 ETH; wrapped NFT arb via vault tokens is quasi-fungible and more calculable

## Disadvantages
- **Extreme illiquidity** -- NFTs are the least liquid asset class in crypto; exit is never guaranteed
- **High total fees** -- marketplace fees + royalties + gas can total 5-15% per round trip
- **Collection and [[wash-trading]] risk** -- collections can lose 90%+ of value, and wash trading distorts reported prices
- **Declining market** -- overall NFT volume has declined significantly from 2021-2022 peaks, reducing the opportunity set

## Real-World Examples
- **Blur vs. OpenSea price war (2023):** Blur launched with zero fees and optional royalties, creating price discrepancies with OpenSea (which enforced royalties). Arbers bought cheaper on Blur and sold on OpenSea.
- **NFTX vault arbitrage:** CryptoPunk vault tokens periodically traded at 3-5% discounts to the Punk floor price. Traders bought tokens, redeemed Punks, and sold at floor for profit.
- **Sudoswap AMM arb:** Sudoswap's bonding curve model creates predictable pricing. When marketplace floors diverge from pool prices, arb bots buy from the cheaper source.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/nfts/overview` — NFT market overview
- `GET /api/v1/nfts/collections` — collection list
- `GET /api/v1/nfts/volume` — volume data
- `GET /api/v1/nfts/correlations` — collection correlations

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/nfts/overview"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-nft]].

## See Also
- [[nft-trading]] and [[nft]] -- foundational knowledge about NFT technology and trading
- [[cross-exchange-arbitrage]] -- the fungible token equivalent of marketplace arbitrage
- [[decentralized-exchanges]] -- the DEX infrastructure that powers NFT marketplaces
- [[wash-trading]] -- a major risk factor that distorts NFT price data
