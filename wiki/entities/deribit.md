---
title: "Deribit"
type: entity
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [exchange, crypto, options, derivatives, futures, volatility]
entity_type: exchange
founded: 2016
headquarters: "Dubai, UAE (originally Netherlands, later Panama)"
website: "https://www.deribit.com"
aliases: ["Deribit"]
related: ["[[options-overview]]", "[[crypto-markets]]", "[[bitcoin]]", "[[ethereum]]", "[[volatility]]", "[[cash-and-carry]]", "[[hyperliquid]]", "[[binance]]", "[[coinbase]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation]]", "[[greeks]]", "[[implied-volatility]]"]
---

Deribit is the dominant cryptocurrency options exchange, handling roughly 85-90% of all crypto options volume globally. Founded in 2016 in the Netherlands (later relocated to Panama, then Dubai), Deribit offers [[bitcoin|BTC]] and [[ethereum|ETH]] options, futures, and perpetual contracts. For traders focused on crypto [[volatility]] and options strategies, Deribit is the primary venue — its option chain liquidity, implied volatility surface, and open interest data are the de facto benchmarks for crypto derivatives pricing. In May 2025 [[coinbase|Coinbase]] agreed to acquire Deribit for approximately $2.9 billion ($700M cash plus 11M Coinbase Class A shares); the deal closed on August 14, 2025, making Deribit a Coinbase subsidiary and giving Coinbase the leading position in global crypto options (Verified via Perplexity (sonar) and WebSearch, 2026-06-11).

Within the broader crypto derivatives ecosystem, Deribit occupies the **options** pillar alongside [[hyperliquid]] (dominant for [[perpetual-futures|perps]]) and [[binance]] (dominant for spot + perps). Together these three exchanges define the crypto derivatives landscape, and data from all three is essential for comprehensive market analysis.

## At a Glance

| Attribute | Detail |
|---|---|
| Entity type | Cryptocurrency [[options]] and derivatives exchange |
| Founded | 2016 (Netherlands → Panama → Dubai, UAE) |
| Ownership | [[coinbase\|Coinbase]] subsidiary since 14 August 2025 (~$2.9B deal; verified 2026-06-11) |
| Core products | BTC/ETH options, futures, perpetual swaps, combos, block trades |
| Option style | European, cash-settled, inverse (BTC/ETH-denominated) |
| Margin system | Cross / portfolio margin with offset recognition |
| Flagship data | DVOL index (BTC & ETH 30-day [[implied-volatility]]), IV surface, open interest |
| Market position | Dominant crypto options venue (~85-90% of global crypto options volume) |
| Primary users | Professional market makers, crypto-native funds, global retail (ex-US historically) |
| Main competitors | [[cboe\|CME]] (regulated, USD-settled), OKX, [[binance]] |
| US access | Historically excluded US users; path toward US-compliant access under Coinbase |
| Relevance | Benchmark for crypto vol pricing; expiries influence [[bitcoin\|BTC]]/[[ethereum\|ETH]] spot |

## Market Dominance

| Metric | Deribit | Competitors |
|--------|---------|-------------|
| BTC options volume share | ~85-90% | CME ~8-10%, OKX ~3%, Binance ~2% |
| ETH options volume share | ~90% | OKX ~5%, CME ~3% |
| BTC options open interest | ~$15-30B (varies) | CME ~$3-5B |
| Block trade volume | Growing rapidly | CME growing for institutional |

### Why Deribit Dominates

1. **First mover** in crypto options (2016), built deep liquidity before competitors entered
2. **Professional market makers** (Wintermute, QCP Capital, Genesis, etc.) concentrate on Deribit
3. **European-style options** with cash settlement — simpler for market makers to hedge
4. **Portfolio margining** — allows offsetting positions to reduce margin requirements
5. **BTC-denominated** — collateral, P&L, and settlement are in BTC (inverse contracts)

## Coinbase Acquisition (2025)

In May 2025, [[coinbase|Coinbase]] announced it would acquire Deribit for ~$2.9 billion — its largest acquisition to date — structured as $700 million cash plus 11 million Coinbase Class A shares. The transaction closed on **August 14, 2025**. Strategic rationale and implications:

- **Coinbase enters crypto options at scale**: Acquiring Deribit instantly made Coinbase the leading global crypto derivatives platform, combining Coinbase's US-regulated spot/futures presence with Deribit's dominant options book (~$30B open interest at announcement).
- **Regulatory bridge**: Deribit historically excluded US users; under Coinbase ownership there is a path toward bringing institutional crypto options to US-compliant venues over time.
- **Brand continuity**: Deribit continues to operate under its own brand and platform; the DVOL index, portfolio margining, and inverse (BTC/ETH-denominated) contracts remain in place.
- **Trading implication**: Concentration risk increases — a single corporate parent now controls the dominant options venue. Counterparty assessment for crypto options should now factor Coinbase's balance sheet and regulatory posture into [[counterparty-risk]] analysis.

(Verified via Perplexity (sonar) and WebSearch, 2026-06-11.)

## Product Suite

- **Options**: BTC and ETH options with weekly, monthly, and quarterly expiries; strikes spanning wide range
- **Futures**: BTC and ETH futures with quarterly expiry
- **Perpetual swaps**: BTC and ETH perpetuals with [[funding-rate]] mechanism
- **Combos**: Multi-leg option orders (spreads, straddles, etc.)
- **Block trades**: Large-size negotiated trades (minimum notional thresholds) for institutional participants
- **Portfolio margin**: Cross-margin across options, futures, and perps with offset recognition

## Options Trading Strategies on Deribit

Deribit's option chain supports the full range of strategies available in traditional [[options-overview|options]] markets, adapted for crypto's higher [[volatility]] environment:

### Directional Strategies
- **Long calls/puts**: Pure directional bets on BTC/ETH with defined risk
- **Bull/bear call/put spreads**: Reduce premium cost by capping profit; effective when [[implied-volatility]] is elevated
- **Synthetic futures**: Long call + short put at same strike; replicates futures exposure with customized margin

### Income / Yield Strategies
- **Covered calls**: Hold BTC spot or futures, sell OTM calls. Popular for generating yield in sideways markets. Crypto's high IV means covered call premiums are substantially larger than in equities.
- **Protective puts**: Hold BTC, buy OTM puts as portfolio insurance. Expensive in crypto due to high [[implied-volatility]], but critical for large positions
- **Cash-secured puts**: Sell OTM puts to acquire BTC at a lower effective price; functions as limit-order-with-premium

### Volatility Strategies
- **Straddles**: Buy ATM call + ATM put; profits from large moves in either direction. Useful ahead of known catalysts (FOMC, [[bitcoin-halving|halving]], ETF rulings)
- **Strangles**: Buy OTM call + OTM put; cheaper than straddles but requires larger move to profit
- **Iron condors**: Sell OTM strangle + buy further-OTM strangle; profits from range-bound markets. Challenging in crypto due to frequent breakouts
- **Butterfly spreads**: Concentrated bet on BTC settling near a specific price at expiry
- **Calendar spreads**: Exploit term structure differences (see [[itpm-ratio-calendar-spread]] for the ITPM methodology)

### Skew and Surface Trades
- **Risk reversals**: Buy OTM call, sell OTM put (or vice versa); trades the [[implied-volatility]] skew
- **Ratio spreads**: Sell more options than bought (e.g., 1x2 call spread); captures skew premium but introduces tail risk

## DVOL Index — The "VIX of Crypto"

Deribit publishes the **DVOL (Deribit Volatility Index)** for both BTC and ETH, analogous to the [[cboe|CBOE]] VIX for the S&P 500. DVOL represents the 30-day [[implied-volatility]] derived from Deribit's option prices.

| DVOL Level | Interpretation | Historical Context |
|------------|---------------|-------------------|
| < 40% | Low vol environment (rare in crypto) | Bear market doldrums, post-capitulation calm |
| 40-60% | Normal crypto volatility | Typical ranging market |
| 60-80% | Elevated volatility | Trending markets, event-driven moves |
| > 80% | Extreme volatility | Market crashes, liquidation cascades, major catalysts |
| > 100% | Crisis-level | March 2020 COVID, LUNA collapse, FTX collapse |

### DVOL Trading Signals

- **DVOL divergence from price**: If BTC is rallying but DVOL is rising, the market is pricing in uncertainty about the rally's sustainability — a potential caution signal
- **DVOL mean reversion**: Like VIX, DVOL tends to mean-revert. Extremely elevated DVOL readings (>90%) tend to compress, making short-vol strategies attractive after the initial spike subsides
- **Term structure**: Compare front-month vs. back-month IV. Inverted term structure (front > back) signals acute fear; normal term structure (back > front) signals complacency

## Options Expiry Dynamics — "Opex" Effect

Large Deribit options expiries exert measurable gravitational effects on [[bitcoin|BTC]] and [[ethereum|ETH]] spot prices, analogous to equity options expiry (OpEx) effects but amplified by crypto's thinner liquidity:

### Max Pain Theory

**Max pain** is the strike price at which the total value of expiring options (calls + puts) is minimized — i.e., the price that causes the most options to expire worthless. Empirically:

- BTC price tends to gravitate toward the max pain strike in the 48-72 hours before major monthly/quarterly expiries
- The effect is strongest for large quarterly expiries ($5B+ in notional) and weakest for weekly expiries
- After expiry, the "pin" releases and BTC often makes a sharp directional move

### Gamma Exposure and Dealer Hedging

Market makers who sell options on Deribit must delta-hedge by trading the underlying. As expiry approaches:

1. **Positive gamma** (net long options): Dealers hedge by selling rallies and buying dips, suppressing volatility
2. **Negative gamma** (net short options): Dealers hedge by buying rallies and selling dips, amplifying volatility
3. The transition from positive to negative gamma zones often triggers the most violent moves

### Quarterly Expiry Calendar

Major Deribit quarterly expiries occur on the last Friday of March, June, September, and December. These often coincide with:
- Elevated volume in the 5 trading days before expiry
- Max pain gravitational effect
- Post-expiry directional breakouts (new positions establish)
- Interaction with [[funding-rate]] resets on [[perpetual-futures]] across [[hyperliquid]], [[binance]], and other perp venues

## Open Interest as Market Signal

Deribit's BTC options open interest data provides insight into market positioning:

| Signal | Interpretation |
|--------|---------------|
| Rising OI + rising price | New longs entering, trend confirmation |
| Rising OI + falling price | New shorts entering, trend confirmation |
| Falling OI + rising price | Short covering rally, potentially unsustainable |
| Falling OI + falling price | Long liquidation, potentially near exhaustion |
| Put/call OI ratio > 1.0 | Hedging demand elevated, potentially contrarian bullish |
| Put/call OI ratio < 0.5 | Complacency, potentially contrarian bearish |

## Block Trades

Deribit's block trade facility allows institutional participants to execute large option orders without impacting the order book:

- Minimum block size: 25 BTC (options), 200 ETH (options)
- Trades reported post-execution, visible in block trade feed
- Growing share of total volume (~15-25% of options volume)
- Block trade flow data provides insight into institutional positioning — large call spreads signal institutional bullishness; large put buys signal hedging demand

## Portfolio Margin

Deribit's portfolio margin system recognizes the offsetting risk of combined positions:

- A covered call (long BTC futures + short call) requires significantly less margin than the sum of individual positions
- Iron condors receive margin credit for the defined-risk structure
- Cross-margining across options, futures, and perps within the same account
- Enables capital-efficient strategy deployment compared to per-position margining on competing platforms

## Deribit vs CME Crypto Options

| Dimension | Deribit | CME |
|-----------|---------|-----|
| **Settlement** | Cash-settled in BTC/ETH | Cash-settled in USD |
| **Style** | European | European (quarterly), American (weekly) |
| **Collateral** | BTC/ETH (inverse) | USD |
| **KYC** | Light KYC | Full institutional KYC |
| **Access** | Global (excl. US, some jurisdictions) | US-accessible, regulated |
| **Liquidity** | Deepest for most strikes/expiries | Growing, concentrated in front-month |
| **Portfolio margin** | Yes | Yes (for qualified accounts) |
| **Trading hours** | 24/7 | CME hours (with extended) |

For US-based institutional traders, CME is the only regulated venue. For global retail and crypto-native funds, Deribit dominates. The two markets occasionally diverge in [[implied-volatility]] pricing, creating [[arbitrage-opportunity-map|arbitrage]] opportunities.

## Risks and Considerations

Deribit's dominance is also a source of structural risk for the traders who depend on it:

- **Concentration / single-venue risk** — with the large majority of crypto options volume and open interest on one platform, a Deribit outage, exploit, or insolvency event would be systemic for crypto-options pricing. There is no deep, liquid fallback venue for most strikes and expiries. This concentrates [[counterparty-risk]] in a way equity-options traders (who have multiple deep exchanges) do not face.
- **Corporate-parent risk** — since the [[coinbase|Coinbase]] acquisition, counterparty assessment for crypto options must factor in Coinbase's balance sheet, regulatory posture, and any future strategic repositioning of the Deribit book.
- **Inverse / BTC-denominated collateral** — because collateral, margin, and P&L are denominated in BTC/ETH on most contracts, a sharp drop in the underlying simultaneously reduces collateral value *and* worsens directional positions — a self-reinforcing dynamic during [[liquidation]] cascades. Traders must model collateral and exposure jointly, not separately.
- **Liquidity skew across the surface** — front-month near-the-money options are deep, but far-dated or deep-OTM strikes can be thin. Apparent IV-surface signals in illiquid corners may reflect stale quotes rather than genuine demand.
- **Regulatory / jurisdictional shift** — Deribit's historical exclusion of US users and its relocation history (Netherlands → Panama → Dubai) reflect an evolving regulatory environment; access rules can change with ownership and regulation.
- **Event/expiry crowding** — because so much positioning sits on one venue, max-pain and gamma-hedging effects (see above) are amplified relative to fragmented markets, which can both create and trap directional bets around major expiries.

## Relevance to Trading Strategies

- **[[cash-and-carry]]**: Deribit futures vs. spot basis is a key carry trade
- **Crypto vol surface**: Deribit's implied volatility surface (skew, term structure) is the benchmark for crypto options pricing
- **DVOL index**: Deribit's BTC and ETH implied vol indices — the "VIX of crypto"
- **Max pain / options expiry**: Large Deribit expiries (quarterly, monthly) influence spot price dynamics as dealers hedge gamma
- **[[funding-rate]] arbitrage**: Compare Deribit perp funding vs. [[hyperliquid]] and [[binance]] for cross-venue arb
- **Vol surface arbitrage**: Compare Deribit IV surface to CME for cross-venue vol discrepancies
- **Sentiment indicator**: Put/call ratios, skew, and OI changes on Deribit serve as leading sentiment indicators, complementing [[alternative-me|Fear & Greed Index]] and [[cryptoquant|CryptoQuant]] on-chain data

## Related

- [[options-overview]] — Options trading concepts and [[greeks]]
- [[bitcoin]] — BTC options and futures
- [[ethereum]] — ETH options and futures
- [[volatility]] — Crypto [[implied-volatility]]
- [[cash-and-carry]] — Basis trades using Deribit futures
- [[hyperliquid]] — Dominant perp DEX, complements Deribit's options dominance
- [[binance]] — Largest centralized exchange, spot + perps
- [[coinbase]] — Acquired Deribit in 2025 (closed August 14, 2025)
- [[perpetual-futures]] — Perp contracts available on Deribit alongside options
- [[funding-rate]] — Funding rate comparison across venues
- [[itpm-ratio-calendar-spread]] — ITPM options methodology applicable to Deribit
- [[alternative-me]] — Sentiment data to cross-reference with options positioning
- [[cryptoquant]] — On-chain data to combine with derivatives signals
- [[options]] — Core instrument class traded on Deribit
- [[counterparty-risk]] — Single-venue concentration risk in crypto options
- [[liquidation]] — Cascade dynamics amplified by inverse collateral
- [[cboe]] — CME's crypto options are the regulated US alternative

## Sources

- Coinbase, "Deribit Joins Coinbase: Unlocking the Future of Global Crypto Derivatives" (investor relations, August 2025) — https://investor.coinbase.com/news/news-details/2025/Deribit-Joins-Coinbase-Unlocking-the-Future-of-Global-Crypto-Derivatives/default.aspx
- Reuters, "Coinbase to acquire Deribit in $2.9 billion deal" (May 8, 2025) — https://www.reuters.com/markets/deals/coinbase-acquire-deribit-29-billion-deal-wsj-reports-2025-05-08/
- Deribit public documentation (DVOL methodology, contract specifications), exchange volume/open-interest data, and crypto derivatives market analysis.
- Acquisition details, headquarters, and market-share standing verified via Perplexity (sonar) and WebSearch, 2026-06-11.
