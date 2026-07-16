---
title: "yearn.finance"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, altcoins, derivatives, perpetual-futures, funding-rate, open-interest, liquidations]
aliases: ["YFI", "Yearn Finance"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://yearn.fi/"
related: ["[[aave]]", "[[crypto-markets]]", "[[curve-finance]]", "[[defi]]", "[[ethereum]]", "[[governance-token]]", "[[uniswap]]", "[[yield-farming]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[funding-rate-harvest]]"]
---

# yearn.finance

**yearn.finance** (ticker **YFI**) is a suite of [[ethereum|Ethereum]] DeFi products providing **yield aggregation**, lending optimization, and automated [[yield-farming]] via "Vaults." It is widely credited with originating the **yield-aggregator** category. The protocol is community-maintained and governed by **YFI** holders. It started as a passion project by Andre Cronje to automatically rotate capital to whichever lending market offered the best floating yield.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | YFI |
| **Native Chain** | [[ethereum|Ethereum]] (multi-chain deployments) |
| **Market Cap Rank** | #371 |
| **Market Cap** | $65.87M |
| **Fully Diluted Valuation** | $67.43M |
| **Current Price** | $1,838.68 |
| **24h Volume** | $3.95M |
| **24h Change** | -0.96% |
| **7d Change** | -3.04% |
| **All-Time High** | $90,787 (2021-05-12) |
| **All-Time Low** | $31.65 (2020-07-18) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the broader market is in an **Established Bear Market** with the Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] at **23 (extreme fear)** as of 2026-06-21. YFI is soft — down ~1% on the day and ~3% on the week, in line with the risk-off DeFi tape. Its famously high unit price (~$1,839) is a function of the tiny fixed supply, not a reflection of market cap (#371); the MC/FDV ratio is ~0.98, so there is virtually no dilution overhang and price discovery is purely demand-driven.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 35,816 YFI |
| **Total Supply** | 36,666 YFI |
| **Max Supply** | 36,666 YFI |
| **Circulating / Max** | ~97.7% |
| **Market Cap / FDV** | ~0.98 |
| **All-Time High** | $90,787 (2021-05-12) |
| **All-Time Low** | $31.65 (2020-07-18) |

YFI is famous for its **deliberately tiny, fair-launched supply** of just **36,666 tokens** — distributed entirely to liquidity providers with **no founder/VC allocation**, an early "fair launch" milestone in DeFi. With ~97.7% circulating and a hard cap, dilution is effectively nil (MC/FDV ~0.98). The scarcity is why the per-token price sits in the four figures despite a sub-$70M market cap. YFI is a pure [[governance-token]]; later governance approved a buyback/treasury program ("Buyback and Build") that uses protocol revenue to repurchase YFI, partially offsetting the marginal supply expansion from the original 30,000 to 36,666 tokens.

---

## How & Where It Trades

**Centralized venues:** YFI is listed on **Binance** (YFI/USDT), **Kraken** (YFI/USD), **Bitget**, **KuCoin**, and **Crypto.com**.

**On-chain / protocol mechanics:** Yearn is a [[yield-aggregator]], not a DEX — but YFI the token trades on-chain via **[[uniswap]] V3/V2** and **Sushiswap** (YFI/WETH) on [[ethereum]]. The protocol's Vaults deposit user capital into strategies across [[aave]], Compound, Curve, and other venues, auto-compounding and socializing gas. yToken receipts (e.g., yDAI) represent yield-bearing positions.

**Derivatives:** YFI has perpetuals/futures on major derivatives venues; however, with ~$3.7M spot daily volume and an exceptionally low token count, on-chain spot and CEX spot dominate price discovery. Funding/OI are secondary signals.

---

## Use Case, Narrative & Category

Yearn sits at the heart of the **DeFi yield-aggregation / "set-and-forget" passive yield** narrative. Vaults let non-expert users earn optimized, auto-rebalanced yield without managing the underlying [[aave]]/Compound/[[curve-finance|Curve]] positions — effectively an on-chain "crypto hedge fund" that maximizes deposited assets. YFI's fair-launch story made it a cultural touchstone for the 2020 "DeFi Summer." Categories include [[defi|DeFi]], [[yield-farming]], Yield Aggregator, and Governance.

---

## Valuation Framing (qualitative)

YFI is best framed as a **claim on a yield-aggregation business** rather than a productive cashflow token in its own right. The relevant value drivers are: (1) **Vault TVL** and the **net performance/management fees** Yearn captures on it; (2) the **buyback program**, which converts protocol revenue into YFI demand; and (3) the **scarcity premium** baked into a 36,666-unit cap. Because base DeFi yields compress in bear markets, fee revenue is cyclical — the token effectively trades as a high-beta proxy on the *level of on-chain yield* and DeFi TVL. With market cap (#371, ~$66M) far below the 2021 peak, YFI prices in a depressed-yield, low-TVL environment; a re-acceleration of DeFi yields and Vault deposits is the core bull case, while permanent yield compression / aggregator commoditization is the bear case.

---

## Peer Comparison

| Token | Category | MC Rank | Market Cap | Supply model | Notes |
|---|---|---|---|---|---|
| **YFI** (this page) | Yield aggregator | #371 | ~$66M | Fixed 36,666 cap, ~98% circ | Originator of the category; fair launch |
| [[convex-finance\|Convex (CVX)]] | Curve yield / vote-aggregation | — | small-cap | Capped, mostly circulating | Yield routed through Curve gauges |
| [[aave\|Aave (AAVE)]] | Lending base layer | top-50 | large-cap | Capped 16M | Underlying venue Yearn deposits into |
| [[curve-finance\|Curve (CRV)]] | Stable DEX / yield base | mid-cap | mid-cap | High inflation | Core liquidity venue for Vaults |

Yearn is a **fee-on-yield aggregator** sitting *above* the lending/DEX base layers (Aave, Curve, Compound) — it does not originate yield, it routes and compounds it. Its differentiator versus newer aggregators is brand, audited Vault history, and the fixed-supply scarcity narrative.

---

## Overview (protocol detail)

Yearn Finance is a suite of products in Decentralized Finance (DeFi) that provides lending aggregation, yield generation, and insurance on the Ethereum blockchain. The protocol is maintained by various independent developers and is governed by YFI holders.

It started out as a passion project by Andre Cronje to automate the process of switching capital between lending platforms in search of the best yield offered, as the lending yield is a floating rate rather than fixed rate. Funds are shifted between dYdX, [[aave|AAVE]], and Compound automatically as interest rates change between these protocols.

The service offered includes major USD tokens such as DAI, USDT, USDC, and TUSD. For example, if a user deposits DAI into yearn.finance, the user will receive yDAI token in return, which is a yield-bearing DAI token.

Later on, it collaborated with Curve Finance to release a yield-bearing USD tokens pool that includes four y-tokens: yDAI, yUSDT, yUSDC and yTUSD, named yUSD.

Yearn debuted the **Vault** feature after its token launch, igniting a frenzy on automated yield farming and is considered the initiator of the yield-farming-aggregator category. Vaults claim yield-farming rewards and sell them for the underlying assets, socializing gas costs, automating yield generation and rebalancing, and shifting capital as opportunities arise. End users do not need proficient knowledge of the underlying protocols, so Vaults represent a passive-investing strategy — akin to a crypto fund whose aim is to grow deposited assets.

---

## Notable History

- **Fair launch (July 2020):** 30,000 YFI distributed to LPs with zero pre-mine — a landmark "no VC, no founder allocation" launch during DeFi Summer.
- **Vaults launch** kicked off the automated yield-farming aggregator category.
- **ATH $90,787** (May 2021) — at one point YFI traded above the price of one Bitcoin, a symbol of the extreme-scarcity thesis.
- Governance later expanded supply marginally (to 36,666) and funded a treasury/buyback program. Price now sits ~98% below ATH after the multi-year DeFi drawdown.

---

## Risks

- **Strategy/smart-contract risk** — Vaults are composed of many underlying protocols; a bug or exploit in any leg (or in [[aave]]/Curve/etc.) can cause losses. Yearn has suffered exploits historically.
- **Yield compression** — in a bear market, base DeFi yields fall, reducing Vault attractiveness and protocol fees.
- **Governance/key-person dependence** — historically associated with a small core dev set.
- **Bear-market beta** — high-beta DeFi governance token amid extreme fear (F&G 23).
- **Thin liquidity** — very low token count and ~$3.9M daily volume can amplify price swings.
- **Aggregator commoditization** — yield routing is increasingly built into wallets and competing aggregators; durable fee capture is not guaranteed.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[yield-farming]]
- [[aave]]
- [[curve-finance]]
- [[defi]]
- [[uniswap]]
- [[governance-token]]
- [[crypto-fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 from CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`).
- General market knowledge; no specific wiki source ingested yet.

## Trading Profile

### Venues & liquidity

YFI is tradable on [[binance]] — **spot (YFI/USDT)** plus a **USD-margined perpetual** exposing [[funding-rate|funding]], [[open-interest]], and [[liquidations]] data. It is **NOT** listed on [[hyperliquid]], so Binance is effectively the **primary leveraged venue** for the token. Because deep, reliable leverage is concentrated on a single CEX, derivatives-based strategies (carry, funding, cascade fades) live or die on Binance depth. With modest spot turnover and the four-figure per-unit price, order books are thin relative to majors — size positions conservatively, prefer limit/VWAP execution over market fills, and expect slippage and funding to swing sharply during volatility. The absence of a second major perp venue (no Hyperliquid) also limits cross-venue arbitrage to CEX-vs-CEX pairs.

### Applicable strategies

- [[cash-and-carry]] — buy Binance YFI spot vs. short the USD-M perp to harvest basis/funding on a scarce, fixed-supply token where funding can run rich in rallies.
- [[funding-rate-harvest]] — collect persistent perp funding on the single dominant venue; YFI's high-beta DeFi swings frequently push funding to one-sided extremes.
- [[crowded-long-funding-fade]] — fade over-leveraged longs when a DeFi-yield narrative spikes YFI and funding turns sharply positive on Binance.
- [[liquidation-cascade-fade]] — thin books plus concentrated leverage make YFI prone to violent liquidation flushes that overshoot and mean-revert.
- [[oi-confirmed-trend]] — use Binance open-interest build to confirm whether a YFI breakout is real leverage-backed demand or a spot-only drift.
- [[rsi-mean-reversion]] — the low-float, low-liquidity tape produces frequent overextended spikes and washouts that snap back toward range.

### Volatility & regime character

YFI is a **small-cap DeFi governance token** (~#305) and a high-beta proxy on **on-chain yield / DeFi TVL**. It trades with strong correlation to BTC/ETH risk-on/risk-off swings but amplifies the move — infra/DeFi tokens lead on the way up and bleed hard in risk-off. Its **fixed ~36,666 supply and four-figure unit price** make it reflexive and headline-sensitive: scarcity narrative and yield-cycle sentiment drive outsized, thin-liquidity moves rather than steady trends. Not a memecoin, but reflexivity is elevated by the tiny float.

### Risk flags

- **Venue/liquidity concentration** — leveraged trading is essentially Binance-only (no Hyperliquid); a single-venue funding or outage shock has no natural hedge, and thin spot depth amplifies slippage.
- **Narrative dependence** — price keys off DeFi yield cycles and TVL; permanent yield compression or aggregator commoditization removes the core bid.
- **Bear-market beta** — high-beta DeFi token that de-rates hard in risk-off regimes.
- **Smart-contract/protocol risk** — Vault exploits or losses in underlying legs (Aave/Curve/Compound) can trigger sudden repricing.
- **Supply is not a risk** — ~98% circulating with a hard cap means negligible unlock/emission overhang, but the same scarcity makes the book easy to move.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=YFIUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=YFIUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=YFI` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=YFI` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=YFIUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=YFIUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=YFI"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
