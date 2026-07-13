---
title: "SPY (SPDR S&P 500 ETF)"
type: market
created: 2026-04-13
updated: 2026-06-17
status: excellent
tags: [stocks, sp500, etf, options, benchmark]
aliases: ["SPY ETF", "SPDR S&P 500 ETF", "SPY"]
related: ["[[s-and-p-500]]", "[[equity-index]]", "[[sector-rotation]]", "[[qqq]]", "[[tlt]]", "[[options]]", "[[index-arbitrage]]", "[[etf-arbitrage]]", "[[volatility-risk-premium]]", "[[spx-options]]", "[[spy-options]]", "[[index-options]]", "[[vix]]", "[[es-futures]]", "[[micro-futures]]"]
---

# SPY (SPDR S&P 500 ETF)

SPY is the SPDR S&P 500 ETF Trust, the largest and most liquid ETF in the world, tracking the [[s-and-p-500|S&P 500]] index. Launched on January 22, 1993, by State Street Global Advisors, it was the first ETF listed in the United States. SPY is the benchmark instrument for U.S. equity market exposure, the most actively traded security in the world by dollar volume, and the foundation of the largest options market on earth. For the underlying index methodology, see [[s-and-p-500]].

## Key Facts

| Metric | Value |
|--------|-------|
| **Ticker** | SPY |
| **Index tracked** | S&P 500 (~500 large-cap U.S. companies) |
| **Issuer** | State Street Global Advisors (SSGA) |
| **Structure** | Unit Investment Trust (UIT) |
| **Inception** | January 22, 1993 |
| **Expense ratio** | ~0.09% (higher than VOO/IVV) |
| **AUM** | ~$550B+ (as of early 2026) |
| **Avg daily volume** | ~80-100M shares/day |
| **Options volume** | Most liquid options market globally |
| **Dividend** | Quarterly, ~1.3% yield |
| **Price** | ~1/10 of the S&P 500 index level |

## What It Tracks / Methodology

SPY holds the actual S&P 500 constituents in their float-adjusted, market-cap-weighted proportions, so its composition, sector tilt, and concentration mirror the index (see [[s-and-p-500#Composition & Concentration]]). A few structural details distinguish SPY from a plain mutual fund or a modern open-end ETF:

- **Unit Investment Trust (UIT) structure** — SPY is one of the oldest fund structures. A UIT cannot reinvest dividends internally and cannot lend securities, so dividends accumulate in a non-interest-bearing account until the quarterly payout. This creates a small **cash drag** versus open-end ETFs that reinvest continuously. The trade-off is a simple, fully-replicated, low-tracking-error portfolio.
- **Full replication** — SPY owns every index constituent rather than sampling, keeping tracking error tight.
- **Designed for trading, not just holding** — SPY's penny-wide spreads and depth make it the institutional and retail vehicle of choice for *active* exposure, hedging, and options.

### Creation / Redemption & Authorized Participants

Like all ETFs, SPY stays priced near its net asset value (NAV) through an in-kind **creation/redemption** mechanism run by **Authorized Participants (APs)** — large broker-dealers:

1. When SPY trades **above NAV** (a premium), an AP buys the 500 underlying stocks, delivers that basket to the trust, and receives newly *created* SPY shares to sell — pushing the price back down.
2. When SPY trades **below NAV** (a discount), an AP buys cheap SPY shares, *redeems* them for the underlying basket, and sells the stocks — pushing the price back up.

This arbitrage keeps SPY's market price glued to the value of its holdings and links SPY tightly to [[es-futures|ES futures]] and the cash index — the basis between the three is itself a trade (see [[index-arbitrage]], [[etf-arbitrage]]). The in-kind process is also why ETFs are generally tax-efficient: redemptions hand out low-basis shares in kind rather than realizing capital gains inside the fund.

## SPY vs VOO vs IVV

All three track the S&P 500 but differ in structure and cost:

| Feature | SPY | VOO | IVV |
|---------|-----|-----|-----|
| **Issuer** | State Street | Vanguard | BlackRock (iShares) |
| **Expense ratio** | ~0.09% | ~0.03% | ~0.03% |
| **Structure** | UIT | Open-end ETF | Open-end ETF |
| **Dividend reinvestment** | No (cash drag) | Yes | Yes |
| **Options liquidity** | Deepest in the world | Good, but far less | Good, but far less |
| **Bid-ask spread** | Tightest (~$0.01) | Slightly wider | Slightly wider |
| **Best for** | Active trading, options, hedging | Buy-and-hold | Buy-and-hold |

The decision rule most practitioners use: **trade SPY, hold VOO/IVV.** SPY's higher expense ratio and UIT cash drag are a meaningful headwind compounding over decades, so long-term holders prefer the cheaper open-end funds. But for anyone trading actively or using options, SPY's unmatched liquidity, depth, and penny spreads make the few extra basis points irrelevant.

## History & Long-Run Returns

SPY's total return tracks the S&P 500 itself, minus its small fee — i.e. **approximately 10% nominal annualized including dividends** over the long run. Because the ETF launched in 1993, it has lived through every major modern crisis, and its price simply mirrors the index drawdowns:

| Episode | Approx. drawdown | Notes |
|---------|------------------|-------|
| Dot-com bust ([[dot-com-bubble]]) | ~-49% | 2000-2002 |
| Global Financial Crisis ([[2008-global-financial-crisis]]) | ~-57% | 2007-2009; SPY a key hedging/short vehicle throughout |
| COVID crash | ~-34% | Feb-Mar 2020; record SPY and SPX options volume |
| 2022 rate bear | ~-25% | Multiple compression from Fed hiking |

For the full index drawdown history and recovery timelines, see [[s-and-p-500#Notable Drawdowns & Recoveries]].

## Ways to Trade

SPY is itself a way to trade the index, but it sits at the center of a whole instrument complex:

| Instrument | Relationship to SPY |
|------------|---------------------|
| **SPY shares** | Direct exposure, deepest liquidity, penny spreads |
| **[[spy-options\|SPY options]]** | Physically settled, American-style; the most liquid equity options on earth |
| **[[spx-options\|SPX options]]** | Cash-settled, European-style, 10x the notional, 60/40 tax treatment — the institutional cousin |
| **[[es-futures\|ES futures]] / [[micro-futures\|MES]]** | ~23h/day exposure; SPY tracks ES via the creation/redemption basis |
| **VOO / IVV** | Cheaper buy-and-hold alternatives (see table above) |
| **SSO / UPRO / SPXL** | Leveraged (2x/3x) daily-rebalanced versions |
| **SH / SDS / SPXU** | Inverse / leveraged-inverse for short exposure |

### Options on SPY

SPY hosts the most liquid equity options market in the world:

- **0DTE (zero days to expiration)** — SPY lists daily (Mon-Fri) expirations. 0DTE on SPY and [[spx-options|SPX]] has exploded since 2022, now a large share of total S&P options volume.
- **Strike granularity** — $1 increments near ATM, wider further out.
- **American-style, physically settled** — exercise can happen any time and delivers SPY *shares* (assignment risk matters for short options, especially around ex-dividend).
- **IV tracks the [[vix|VIX]]** — SPY/SPX implied vol *is* the VIX, making SPY the primary retail vehicle for trading the [[volatility-risk-premium|VRP]].
- **Retail income strategies** — covered calls and cash-secured puts most commonly use SPY as the underlying.

### SPY vs SPX Options (and the tax angle)

| Feature | [[spy-options\|SPY Options]] | [[spx-options\|SPX Options]] |
|---------|-------------|-------------|
| **Settlement** | Physical (shares) | Cash |
| **Style** | American | European (no early-assignment risk) |
| **Contract size** | 100 shares (~$50-60K notional) | 100x index (~$500-600K notional) |
| **Tax treatment** | Standard short/long-term capital gains | **Section 1256 60/40** (60% long-term, 40% short-term) regardless of holding period |
| **Best for** | Retail, smaller accounts, covered calls | Larger/institutional accounts, tax efficiency, no assignment risk |

The **60/40 tax treatment** is the headline reason active traders and larger accounts migrate from SPY to SPX options: index options are Section 1256 contracts, so gains are taxed 60% long-term / 40% short-term even on intraday trades — a meaningful edge versus SPY's standard treatment. SPX also avoids early-assignment and ex-dividend headaches because it is cash-settled and European-style. See [[index-options]] for the broader cash-settled index-option family.

## Valuation & Regime Behavior

SPY's valuation and regime behavior *are* the S&P 500's — monetary policy, the [[treasuries|10-year yield]] as discount rate, mega-cap earnings, and the dollar are the dominant drivers (see [[s-and-p-500#Valuation & Regime Behavior]]). ETF-specific tells:

- **Premium/discount to NAV** — normally negligible thanks to AP arbitrage, but SPY can trade at a brief premium/discount during extreme stress (e.g. opening minutes of the COVID crash) when the underlying basket is hard to price — a signal of dislocation.
- **Volume as a fear gauge** — SPY share and options volume spike in risk-off episodes; unusually heavy put activity often flags hedging demand.

## Notable Episodes

- **First U.S. ETF (1993)** — SPY pioneered the entire ETF industry; the in-kind creation/redemption model it used became the template for thousands of funds.
- **2010 Flash Crash** — SPY was at the center of the May 6, 2010 intraday plunge and recovery, highlighting how ETF liquidity and the arbitrage mechanism behave under stress.
- **COVID 2020 volume records** — SPY and SPX options set volume records; SPY became the dominant hedging instrument as the index fell ~34% in five weeks.
- **The 0DTE boom (2022-present)** — daily-expiry SPY/SPX options reshaped intraday market structure and dealer hedging flows.

## Trading Strategies & Uses

- **Benchmark exposure** — the default measure of "the market"; every portfolio manager is benchmarked against it.
- **Hedging** — the most common equity hedge: buying SPY puts or shorting SPY/ES to reduce beta cheaply and reversibly.
- **Premium selling** — selling SPY (or SPX) puts/calls to harvest the [[volatility-risk-premium]] is among the most popular options strategies; SPY's depth makes fills easy.
- **Pair trades** — long a sector/stock, short SPY to isolate alpha from beta ([[long-short-equity]]); long [[qqq|QQQ]] / short SPY for growth-vs-broad views.
- **Sector rotation** — SPY as the neutral benchmark vs sector ETFs (XLK, XLF, XLE) for relative value ([[sector-rotation]]).
- **Index / ETF arbitrage** — exploiting the SPY ↔ ES futures ↔ underlying-500 basis ([[index-arbitrage]], [[etf-arbitrage]]).
- **Macro proxy** — SPY price action is a real-time barometer of U.S. economic expectations, Fed sentiment, and risk appetite.

## Key Relationships

- **SPY vs [[vix|VIX]]** — inversely correlated; SPY selloffs spike VIX, calm markets compress it.
- **SPY vs bonds ([[tlt|TLT]])** — historically negative (risk-on/risk-off), though this *broke during 2022-2023* when both fell together under inflation-driven hiking.
- **SPY vs [[qqq|QQQ]]** — highly correlated (~0.90+) but QQQ has higher beta from its tech concentration.
- **SPY vs DXY (dollar)** — generally inverse: a strong dollar pressures multinational S&P earnings.

## Risks / Limitations

- **Higher fee + cash drag for holders** — SPY's ~0.09% expense ratio and dividend cash drag make it a suboptimal *buy-and-hold* vehicle versus VOO/IVV.
- **Mirrors index concentration** — SPY inherits the S&P's record top-10 weighting; "diversified" is increasingly a few mega-caps (see [[s-and-p-500#Risks / Limitations]]).
- **Assignment / ex-dividend risk on short options** — American-style, physically settled SPY options can be assigned early, especially around ex-dividend; SPX (cash-settled, European) avoids this.
- **Leverage-product decay** — SSO/UPRO/SPXU and friends are daily-rebalanced and decay in choppy markets; they are trading tools, not holds.
- **Stress-period dislocations** — premium/discount to NAV and liquidity gaps can appear in extreme events (2010 flash crash, March 2020).

## Sources

- State Street SPDR official fund documentation
- CBOE options volume data
- General market knowledge for long-run return, drawdown, and tax-treatment context

## Related

- [[s-and-p-500]] — the underlying index
- [[qqq]] — Nasdaq-100 ETF, SPY's most common comparison
- [[spy-options]] / [[spx-options]] / [[index-options]] — the options complex
- [[es-futures]] / [[micro-futures]] — the futures complex
- [[vix]] — implied volatility index derived from SPX options
- [[index-arbitrage]] / [[etf-arbitrage]] — ETF/index/futures basis trades
- [[sector-rotation]] — SPY as benchmark for sector relative value
