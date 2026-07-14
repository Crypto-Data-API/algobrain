<!-- Gap finder: Hyperliquid crypto perpetual exchange low-timeframe backtesting 1m 3m 5m 15m intrabar fills bar resolution multi-timeframe microstructure noise overfitting -->
<!-- Date: 2026-04-22 -->

Below are the **highest-impact gaps** I’d add for a wiki focused on **Hyperliquid + low-timeframe perpetuals backtesting**. I’ve prioritized the items that most affect **trade construction, fill realism, and regime modeling** rather than generic ecosystem entries.

## 1) Key entities to add

| Name | One-line description | Why it matters for traders |
|---|---|---|
| **Aster** | A decentralized perpetuals venue that became a major Hyperliquid competitor in 2025–2026. | Important as a **cross-venue flow / migration** reference and for comparing microstructure, incentives, and liquidity quality. |
| **Coinbase International Exchange** | Coinbase’s offshore derivatives venue for listed perpetuals, including HYPE-PERP launch coverage in 2026. | Crucial for **price discovery**, venue-arb, and understanding how CEX listings impact Hyperliquid flows.[2] |
| **Binance Futures** | The largest centralized crypto perpetuals venue by liquidity and retail flow. | Still the main benchmark for **basis, funding, liquidations, and leader-follower behavior**. |
| **Bybit Derivatives** | A major perpetuals venue with strong retail participation and deep altcoin liquidity. | Useful for **cross-venue latency, order-book comparison, and liquidation contagion** analysis. |
| **OKX Derivatives** | Large global derivatives venue with strong API access and deep perp markets. | Relevant for **global liquidity fragmentation** and as a backtest reference venue. |
| **Deribit** | The dominant crypto options venue, especially for BTC/ETH options. | Needed for **volatility regime** context, hedging flows, and gamma effects that can spill into perp microstructure. |
| **dYdX** | A long-running decentralized derivatives venue with a strong on-chain/perp trading footprint. | Useful comparator for **DEX perp design, maker incentives, and on-chain order-flow behavior**. |
| **GMX** | A leading on-chain perp venue using a vault/liquidity-pool model rather than a classic order book. | Important for contrasting **price impact, oracle dependence, and LP-driven execution** versus Hyperliquid’s order book. |
| **Jupiter Perps** | Solana-native perpetuals product integrated with the Jupiter ecosystem. | Relevant because Solana perp flow often interacts with **fast-moving retail microstructure** and cross-chain capital rotation. |
| **FalconX** | Institutional crypto prime brokerage and execution venue. | Important for understanding **institutional flow**, block liquidity, and how larger players interact with perp venues. |
| **Wintermute** | Major market maker and OTC liquidity provider across crypto venues. | Traders care because Wintermute often influences **spread quality, order-book resilience, and cross-venue arbitrage**. |
| **Jump Crypto** | Major crypto trading and market-making firm. | Relevant for **liquidity provision, venue quality, and event-driven flow** across derivatives markets. |
| **Kinetiq** | Hyperliquid-native liquid staking / ecosystem protocol frequently mentioned in Hyperliquid market structure discussions. | Matters because ecosystem incentives and capital deployment can affect **HYPE supply dynamics and venue participation**. |

## 2) Important concepts / strategies to document

| Name | One-line description | Relevance to trading |
|---|---|---|
| **Order-book imbalance trading** | Using bid/ask depth imbalance to infer short-term directional pressure. | Core for **1m–15m** signals and intrabar fill realism. |
| **Microprice** | A depth-weighted estimate of near-term fair value based on best bid/ask sizes. | Strong for **very short-horizon prediction** and spread-crossing decisions. |
| **Queue position / queue priority modeling** | Modeling your actual place in the limit-order queue and how often you get filled. | Essential for **backtest realism** on fast venues where maker fills dominate edge. |
| **Slippage decomposition** | Separating spread, impact, and adverse selection in execution costs. | Needed to know whether a low-timeframe edge is **real or fully consumed by costs**. |
| **Adverse selection** | The tendency for passive orders to get filled before price moves against you. | Central to maker/taker choice and **whether posting is better than crossing**. |
| **VPIN / toxic flow proxies** | Measures intended to detect informed order flow or liquidity toxicity. | Useful for filtering trades during **information-rich, trend-heavy bursts**. |
| **Volatility regime filters** | Trading only when realized volatility or volatility-of-volatility is in a favorable range. | Helps reduce **overfitting** in noisy low-timeframe systems. |
| **Funding-aware signal design** | Incorporating expected funding payments into entry/exit and hold-time logic. | Critical on perps because funding can dominate edge on longer intraday holds.[1] |
| **Liquidation ladder / cascade anticipation** | Modeling where forced liquidations may trigger and how cascading sells/buys propagate. | Important for **fade vs. momentum** decisions around leverage flushes. |
| **Cross-venue basis / lead-lag** | Trading relative price differences and time lags between venues. | A major source of edge when Hyperliquid, Binance, Coinbase, and others diverge. |
| **Event-time backtesting** | Using trades/order-book events rather than fixed bars. | Often superior to 1m/3m bars for **intrabar fills and bursty microstructure**. |
| **Walk-forward / purged CV** | Robust validation methods that reduce leakage in time-series strategy evaluation. | Important for avoiding **overfitting** on highly autocorrelated intraday data. |

## 3) Data sources / tools to add

| Name | What it provides | Why traders use it |
|---|---|---|
| **Hyperliquid API / Docs** | Native contract specs, funding mechanics, and market data endpoints. | The baseline source for **venue-specific backtesting and execution logic**.[1] |
| **CCXT** | Unified crypto exchange API library. | Common for prototyping strategies across **multiple venues** with a single interface. |
| **Kaiko** | Institutional crypto market data with tick trades, books, and derivatives coverage. | Strong for **historical depth, cross-venue comparisons, and research-grade backtests**. |
| **CoinAPI** | Aggregated crypto market data and normalized exchange feeds. | Useful when you need **clean, standardized historical data** across venues. |
| **Amberdata** | Crypto market data, derivatives analytics, and on-chain analytics. | Helpful for **funding, open interest, and market-structure research**. |
| **CryptoQuant** | Exchange flows, derivatives metrics, and on-chain indicators. | Often used to contextualize **leverage, liquidations, and regime shifts**. |
| **Glassnode** | On-chain and market intelligence with derivatives-related metrics. | Useful for **macro crypto regime** context rather than microsecond execution. |
| **Coinglass** | Aggregated funding, open interest, liquidation, and derivatives dashboards. | Fast way to track **crowding and liquidation risk** across venues. |
| **Dune** | Queryable on-chain analytics platform. | Valuable for **custom Hyperliquid/on-chain dashboards** and protocol-specific behavior. |
| **Nansen** | Wallet labeling and on-chain flow analytics. | Helps identify **smart-money rotation** and entity behavior around perps. |
| **bookmap** | Order-book visualization and heatmap tooling. | Popular for **intraday tape-reading, liquidity walls, and execution intuition**. |
| **TradingView** | Charting and strategy prototyping platform. | Still widely used for **signal visualization and quick sanity checks**. |

## 4) Recent developments to document

| Development | Why it matters |
|---|---|
| **HYPE perpetual listings on Coinbase International / Coinbase Advanced (2026)** | A major cross-venue event because exchange listings can alter **basis, funding, and liquidity migration**.[2] |
| **Hyperliquid’s continued scale-up in on-chain derivatives activity (2026)** | The venue’s growth matters for **slippage assumptions, fill probability, and market-impact regimes**. |
| **Rising competition from new decentralized perp venues in 2025–2026** | Traders need a page on **venue competition and flow fragmentation**, especially for basis trades and arbitrage. |
| **Growth of event-time / order-book-level research workflows** | Low-timeframe strategies increasingly rely on **tick and book reconstruction** rather than candle bars. |
| **Greater attention to funding and leverage as PnL drivers** | As perps mature, funding and crowded positioning matter more for **intraday hold performance**.[1] |
| **Improved on-chain derivatives analytics stacks** | More traders now combine **exchange data + on-chain flows + liquidation metrics** to model microstructure. |
| **Institutional participation in crypto perps via prime brokers and OTC execution** | Adds a new layer of **size, hidden liquidity, and cross-venue hedging**. |
| **Expansion of altcoin perp listings across major venues** | Broadens the set of assets where **liquidation cascades and microstructure noise** can be studied. |

## Biggest omissions, if you want the shortest “must-add” list

If you only add a few pages, I’d prioritize these:

- **Binance Futures**
- **Bybit Derivatives**
- **OKX Derivatives**
- **Coinbase International Exchange**
- **Aster**
- **GMX**
- **dYdX**
- **Order-book imbalance trading**
- **Microprice**
- **Queue position / queue priority modeling**
- **Slippage decomposition**
- **Cross-venue basis / lead-lag**
- **Event-time backtesting**
- **Walk-forward / purged CV**
- **Kaiko**
- **Coinglass**

If you want, I can turn this into a **clean wiki expansion plan** with:
- **page titles**
- **taxonomy / linking structure**
- **“see also” graph**
- and a **priority score** for each missing page.

---

## Citations

1. https://hyperliquid.gitbook.io/hyperliquid-docs/trading/contract-specifications
2. https://web3.bitget.com/en/academy/hyperliquid-perpetual-coinbase-listing-breakdown-what-it-means-for-traders
3. https://www.youtube.com/watch?v=nOjdRyzb5Wc
4. https://epicct.com/hyperliquid-perpetual-exchange-guide-key-features-2/
5. https://www.youtube.com/watch?v=tFcsQZDkoJM
6. https://coinstats.app/ai/a/investment-analysis-hyperliquid
