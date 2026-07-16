---
title: "Venus"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, altcoins, perpetual-futures, funding-rate, open-interest, liquidations, derivatives]
aliases: ["Venus Protocol", "XVS"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://venus.io/"
related: ["[[aave]]", "[[bnb]]", "[[compound]]", "[[crypto-markets]]", "[[defi]]", "[[lending-and-borrowing]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Venus

**Venus** (XVS) is the governance token of [Venus Protocol](https://venus.io/), an algorithmic money market and decentralized lending/borrowing protocol that originated on the [[bnb|BNB Chain]] and has since expanded multi-chain. It is the largest native lending protocol on BNB Chain, functioning much like [[aave|Aave]] or [[compound|Compound]] do on [[ethereum|Ethereum]]: users supply collateral to earn yield and borrow other assets against it, and XVS holders govern the protocol's risk parameters. As a [[defi|DeFi]] money-market token, XVS price is closely tied to total value locked (TVL), interest-rate spreads, and overall BNB Chain DeFi activity.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | XVS |
| **Market Cap Rank** | #484 |
| **Market Cap** | $46.14M |
| **Current Price** | $2.77 |
| **24h Volume** | $4.68M |
| **24h Change** | -0.20% |
| **7d Change** | +12.03% |
| **All-Time High** | $146.82 (2021-05-10) |
| **All-Time Low** | $1.65 |
| **Native Chain** | [[bnb|BNB Chain]] (also deployed to Ethereum, opBNB, zkSync, Unichain, Base, Arbitrum, Optimism) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

XVS was one of the few names in the [[lending-and-borrowing]] category showing relative strength into 2026-06-21, up ~+12% on the week (essentially flat on the day) even as the broader tape sat in **extreme fear (Fear & Greed = 23)** within an **Established Bear Market** regime. That out-performance against a fearful backdrop is typical of money-market tokens, whose fee revenue can hold up when borrowers continue paying interest regardless of price direction.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~16.83M XVS |
| **Total Supply** | ~29.75M XVS |
| **Max Supply** | 30.00M XVS |
| **Fully Diluted Valuation** | ~$81.56M |
| **Market Cap / FDV Ratio** | ~0.57 |

XVS has a hard cap of 30 million tokens, of which roughly 16.8M circulate. The relatively low market-cap-to-FDV ratio (~0.57) is a genuine **dilution flag**: total supply (~29.75M) and max supply (30M) sit nearly double the circulating float, so fully diluting today's $46M market cap would imply ~$82M of value — meaning emissions, governance incentives, and treasury releases still represent a material overhang as locked tokens vest. XVS originally launched fairly (no pre-mine, no team/VC allocation) via Binance Launchpool, distributing tokens to liquidity providers and borrowers. Today XVS is used for governance voting on collateral factors, supported assets, and risk parameters.

---

## How & Where It Trades

- **Spot (CEX):** [[binance|Binance]] is the primary venue (XVS/USDT), reflecting the token's BNB Chain heritage. It also trades on other Tier-1 and Tier-2 exchanges.
- **Spot (DEX):** PancakeSwap on BNB Chain is the dominant on-chain venue; Uniswap V3 carries an Ethereum-deployment pair.
- **Derivatives:** XVS has had perpetual-futures listings on major derivatives venues. As a lower-cap name (~$44M), perp open interest and depth are thin relative to majors, so funding can swing sharply and liquidity gaps make it vulnerable to liquidation cascades during volatility. Confirm live OI/funding on the venue before sizing any position.

The contract addresses below are unchanged from the protocol's deployments:

| Chain | Address |
|---|---|
| BNB Chain | `0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63` |
| opBNB | `0x3e2e61f1c075881f3fb8dd568043d8c221fd5c61` |
| zkSync | `0xd78abd81a3d57712a3af080dc4185b698fe9ac5a` |
| Unichain | `0x81908bbaad3f6fc74093540ab2e9b749bb62aa0d` |
| Base | `0xebb7873213c8d1d9913d8ea39aa12d74cb107995` |
| Ethereum | `0xd3cc9d8f3689b83c91b7b59cab4946b063eb894a` |
| Arbitrum One | `0xc1eb7689147c81ac840d4ff0d298489fc7986d52` |
| Optimism | `0x4a971e87ad1f61f7f3081645f52a99277ae917cf` |

---

## Use Case / Narrative / Category

Venus sits squarely in the **DeFi lending/borrowing** narrative on BNB Chain. Its core product is an over-collateralized money market: suppliers deposit assets to earn interest, borrowers post collateral and draw loans, and interest rates float algorithmically based on utilization. Venus also pioneered **VAI**, a native over-collateralized stablecoin minted against deposited collateral. The investment thesis for XVS is essentially a leveraged bet on BNB Chain DeFi adoption: more TVL and borrowing volume → more protocol revenue → more value accruing to (and buy-pressure on) the governance token. It competes directly with [[aave|Aave]] and [[compound|Compound]] deployments where those protocols also operate on BNB Chain.

---

## Peer Comparison

| Protocol token | Home chain(s) | Niche | Approx. MC rank | Max supply | MC/FDV |
|---|---|---|---|---|---|
| **Venus (XVS)** | [[bnb\|BNB Chain]] (multi-chain) | Largest native BNB Chain money market; VAI stablecoin | #484 | 30M (capped) | ~0.57 |
| [[aave\|Aave (AAVE)]] | [[ethereum\|Ethereum]] (multi-chain) | Blue-chip multi-chain lending; GHO stablecoin | Top ~50 | 16M (capped) | high |
| [[compound\|Compound (COMP)]] | Ethereum (multi-chain) | Original algorithmic money market | Mid-cap | 10M (capped) | high |
| Radiant (RDNT) | Arbitrum / BNB | Cross-chain LayerZero lending | Small-cap | 1B | moderate |
| Kamino (KMNO) | [[solana\|Solana]] | Leading Solana lending/leverage | Small/mid-cap | 10B | low (overhang) |

Venus is essentially the **BNB-Chain analogue of Aave/Compound**: a smaller market cap and steeper dilution overhang than the Ethereum blue-chips, but dominant share of native BNB Chain lending TVL. Its capped 30M supply is more shareholder-friendly than emissions-heavy peers like Kamino, even though a large slice of that cap is not yet circulating.

---

## Notable History

- **All-time high** of ~$146.82 on 2021-05-10, during the peak of the DeFi/BNB Chain bull run.
- **2021 large-loan incident:** Venus suffered protocol stress when a large XVS-collateralized borrow position was liquidated amid extreme volatility, leaving the protocol with bad debt. This became a frequently cited case study in collateral-risk and oracle-risk management for money markets.
- Subsequent versions (Venus V4 and "Isolated Pools") were introduced to compartmentalize risk so that a blow-up in one volatile asset cannot contaminate the core pool.
- The token is down roughly **-98%** from its 2021 ATH (~$146.82) at the current ~$2.77, consistent with the broader compression of DeFi "blue-chip" valuations. The all-time low of ~$1.65 sits not far below the current price.

---

## Risks

- **Smart-contract & oracle risk:** money markets are prime exploit targets; a faulty price oracle or contract bug can produce bad debt (as in 2021). See [[smart-contract-risk]].
- **Collateral / liquidation risk:** thin liquidity in XVS itself makes the token vulnerable to liquidation cascades; sharp drawdowns can self-reinforce.
- **Dilution:** MC/FDV ~0.56 means future emissions and unlocks can pressure price.
- **Concentration on BNB Chain:** despite multi-chain expansion, the protocol's fortunes are heavily tied to BNB Chain DeFi volumes and to [[binance|Binance]]'s ecosystem.
- **Regulatory:** lending protocols and the VAI stablecoin face evolving DeFi regulation.
- **Macro/regime:** as of 2026-06-21 the market is in **extreme fear (Fear & Greed = 23)** and an **Established Bear Market** — small-cap DeFi tokens are high-beta and can underperform sharply in risk-off phases.

> Cryptocurrency is highly volatile and speculative. Nothing here is financial advice. Always verify live on-chain and exchange data before trading.

---

## Trading Profile

### Venues & liquidity

XVS is tradable on [[binance|Binance]] — **spot** (XVS/USDT) plus a **USD-margined perpetual** that carries [[funding-rate|funding]], [[open-interest|open interest]], and [[liquidations|liquidation]] data. It is **NOT listed on Hyperliquid**, so Binance is effectively the *primary — and essentially the only Tier-1 — leveraged venue* for XVS. This concentration matters for execution: as a ~#457-ranked money-market token with thin 24h volume, perp depth and OI are shallow relative to majors, so leverage should be sized conservatively, entries/exits worked with limit orders rather than aggressive market fills, and funding checked before holding. Because there is no cross-venue perp to hedge against, most basis/carry structures reduce to Binance spot-vs-Binance-perp; genuine cross-exchange arbitrage on the perp leg is not available.

### Applicable strategies

- [[funding-rate-harvest]] — thin-float DeFi tokens like XVS periodically show persistent funding skew on the Binance perp that a delta-neutral spot-long/perp-short can harvest.
- [[cash-and-carry]] — pair Binance spot XVS against the USD-M perp to capture basis when the perp trades at a premium, the cleanest neutral trade on the only leveraged venue.
- [[crypto-spot-perp-futures-triangle]] — exploit dislocations between Binance spot and the XVS perp, the natural structure given both legs live on one exchange.
- [[liquidation-cascade-fade]] — shallow XVS perp liquidity makes stop-runs and forced-liquidation wicks common; fading exhausted cascades back toward VWAP is a recurring setup.
- [[oi-confirmed-trend]] — use Binance open-interest changes to confirm whether an XVS move (e.g. its money-market-driven relative-strength rallies) is backed by real positioning or is a low-conviction squeeze.
- [[rsi-mean-reversion]] — XVS oscillates in wide ranges near its all-time-low band; RSI-based reversion suits its choppy, range-bound low-cap behavior.

### Volatility & regime character

XVS is a **small-cap DeFi / money-market governance token** with high beta to BTC/ETH risk appetite and, more specifically, to BNB Chain DeFi activity and TVL. It is not a memecoin — moves are fundamentals-adjacent (rate spreads, TVL, protocol revenue) rather than pure reflexivity — but the small float amplifies swings. Expect elevated correlation to the broad crypto tape in risk-off phases, with occasional idiosyncratic relative strength when money-market fee revenue holds up during drawdowns.

### Risk flags

- **Venue concentration:** leveraged trading is effectively single-venue (Binance); no Hyperliquid or deep cross-exchange perp market to hedge, so venue outages or delisting risk is undiversified.
- **Thin liquidity:** low 24h volume and shallow perp OI make XVS prone to liquidation cascades and slippage; size accordingly.
- **Dilution / emissions overhang:** MC/FDV ~0.57 means locked supply and governance emissions remain a structural supply headwind.
- **Narrative dependence:** price is tethered to BNB Chain DeFi/lending demand and to [[binance|Binance]]'s ecosystem; a rotation out of DeFi lending hits XVS harder than majors.
- **Protocol/regulatory:** money-market smart-contract, oracle, and DeFi-lending regulatory risk (including the VAI stablecoin) can drive gap moves independent of technicals.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=XVSUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=XVSUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=XVS` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=XVS` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=XVSUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=XVSUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=XVS"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]
- [[defi]]
- [[lending-and-borrowing]]
- [[aave]]
- [[compound]]
- [[binance]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 from cryptodataapi.com / CoinGecko top-1000 snapshot (rank #484, $46.14M mcap, $2.77, 7d +12.03%).
- General market knowledge; no additional specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | XVS |
| **Market Cap Rank** | #457 |
| **Market Cap** | $45.41M |
| **Current Price** | $2.69 |
| **Categories** | Decentralized Finance (DeFi), Yield Farming, Binance Launchpool, Lending/Borrowing Protocols |
| **Website** | [https://venus.io/](https://venus.io/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 16.86M XVS |
| **Total Supply** | 29.75M XVS |
| **Max Supply** | 30.00M XVS |
| **Fully Diluted Valuation** | $80.12M |
| **Market Cap / FDV Ratio** | 0.57 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $146.82 (2021-05-10) |
| **Current vs ATH** | -98.16% |
| **All-Time Low** | $1.65 (2020-10-06) |
| **Current vs ATL** | +63.30% |
| **24h Change** | -1.94% |
| **7d Change** | +5.97% |
| **30d Change** | +2.32% |
| **1y Change** | -58.70% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63` |
| Opbnb | `0x3e2e61f1c075881f3fb8dd568043d8c221fd5c61` |
| Zksync | `0xd78abd81a3d57712a3af080dc4185b698fe9ac5a` |
| Unichain | `0x81908bbaad3f6fc74093540ab2e9b749bb62aa0d` |
| Base | `0xebb7873213c8d1d9913d8ea39aa12d74cb107995` |
| Ethereum | `0xd3cc9d8f3689b83c91b7b59cab4946b063eb894a` |
| Arbitrum One | `0xc1eb7689147c81ac840d4ff0d298489fc7986d52` |
| Optimistic Ethereum | `0x4a971e87ad1f61f7f3081645f52a99277ae917cf` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | XVS/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XD3CC9D8F3689B83C91B7B59CAB4946B063EB894A/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://venus.io/](https://venus.io/) |
| **Twitter** | [@VenusProtocol](https://twitter.com/VenusProtocol) |
| **Reddit** | [https://www.reddit.com/r/venusprotocol](https://www.reddit.com/r/venusprotocol) |
| **Telegram** | [VenusProtocol](https://t.me/VenusProtocol) (19,487 members) |
| **Discord** | [https://discord.com/invite/venus-protocol-912811548651708448](https://discord.com/invite/venus-protocol-912811548651708448) |
| **GitHub** | [https://github.com/VenusProtocol/Venus-Protocol](https://github.com/VenusProtocol/Venus-Protocol) |
| **Whitepaper** | [https://github.com/VenusProtocol/venus-protocol-documentation/tree/main/whitepapers](https://github.com/VenusProtocol/venus-protocol-documentation/tree/main/whitepapers) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 280 |
| **GitHub Forks** | 201 |
| **Commits (4 weeks)** | 41 |
| **Pull Requests Merged** | 523 |
| **Contributors** | 30 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.58M |
| **Market Cap Rank** | #457 |
| **24h Range** | $2.68 — $2.83 |
| **CoinGecko Sentiment** | 50% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
