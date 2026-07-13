---
title: "XLK (Technology Select Sector SPDR)"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [stocks, sp500, etf, options, technology]
aliases: ["XLK ETF", "Technology Select Sector SPDR Fund", "Tech SPDR"]
related: ["[[spy]]", "[[qqq]]", "[[xlf]]", "[[xle]]", "[[options-concentration-risk]]", "[[sector-rotation]]", "[[sp500]]"]
---

XLK is the Technology Select Sector SPDR Fund, issued by State Street Global Advisors. It tracks the S&P Technology Select Sector Index — the technology sector slice of the [[sp500|S&P 500]]. XLK is the most liquid pure-tech sector ETF and the standard vehicle for expressing US large-cap technology views without picking individual names. It is heavily concentrated in a handful of mega-cap tech leaders.

## Key Facts

| Metric | Value |
|--------|-------|
| **Ticker** | XLK |
| **Index tracked** | S&P Technology Select Sector Index |
| **Issuer** | State Street Global Advisors |
| **Structure** | Open-end ETF |
| **Inception** | December 16, 1998 |
| **Expense ratio** | 0.09% |
| **AUM** | approximately $70-80B (as of early 2026) |
| **Avg daily volume** | approx 8-12M shares/day |
| **Options liquidity** | Deep — among the most liquid sector ETF options |
| **Dividend** | Quarterly, ~0.6% yield |

## Top Holdings

XLK is exceptionally concentrated. The top 5 holdings typically account for 50-60% of the fund (subject to S&P GICS reclassification rules and quarterly rebalancing):

| Holding | Approx Weight |
|---------|---------------|
| [[apple|AAPL]] | ~18-22% |
| [[microsoft|MSFT]] | ~18-22% |
| [[nvidia|NVDA]] | ~15-20% |
| [[broadcom|AVGO]] | ~5-7% |
| Oracle (ORCL) | ~3-4% |
| Cisco (CSCO), Salesforce (CRM), Adobe (ADBE), Accenture (ACN) | ~2-3% each |

Note: XLK uses S&P's GICS classification, which historically excluded Alphabet and Meta (classified as Communication Services). [[qqq|QQQ]] includes them; XLK does not. This is the most important structural difference between the two.

## XLK vs QQQ

| Feature | XLK | QQQ |
|---------|-----|-----|
| **Holdings** | ~70 (Tech sector only) | 100 (Nasdaq-100, multi-sector) |
| **Top 5 weight** | ~50-60% | ~35-40% |
| **Includes Alphabet/Meta** | No (Comm Services) | Yes |
| **Includes AMZN** | No (Cons Disc) | Yes |
| **Includes TSLA** | No (Cons Disc) | Yes |
| **Expense ratio** | 0.09% | 0.20% |
| **Tilt** | Pure GICS tech | Tech + growth |

XLK is more concentrated in a smaller set of names. QQQ is broader. For pure tech-sector beta, XLK is the cleaner instrument; for broad large-cap growth, QQQ is preferred.

A subtle structural quirk worth flagging: because XLK is capped under S&P's modified-market-cap weighting rules, the relative weights of [[apple|AAPL]], [[microsoft|MSFT]], and [[nvidia|NVDA]] can jump at quarterly rebalances when one name's market cap crosses a threshold. This produces occasional "rebalance reweighting" flows that move XLK's top holdings in non-fundamental ways — a known source of tracking quirks versus a naive cap-weight of the same names.

## Sector Drivers & Macro Sensitivities

Technology is the S&P sector most geared to *interest rates (via duration), the AI/capex cycle, and global growth*:

| Driver | Mechanism | Direction for XLK |
|--------|-----------|-------------------|
| Real interest rates / 10Y yield | Tech is long-duration equity (value in distant earnings) | Rising real rates → negative |
| AI / data-center capex cycle | NVDA, AVGO, MSFT capex and revenue | Capex up → positive (and the dominant 2023-2025 driver) |
| Mega-cap earnings (AAPL, MSFT, NVDA) | Index dominated by a handful of names | Direct, outsized |
| Global growth / China demand | Mega-cap tech earns globally | Pro-cyclical, positive |
| US dollar ([[dxy\|DXY]]) | Foreign-earnings translation | Strong dollar → mildly negative |
| Semiconductor cycle | Memory/logic demand, inventory | Pro-cyclical for chip names |
| Risk appetite / liquidity | Tech is the high-beta "risk-on" sector | Easy financial conditions → positive |
| Regulatory / antitrust | Big-tech regulation, export controls | Episodic negative |

The defining macro fact: XLK is a **long-duration, high-beta growth bet** whose two great enemies are *rising real rates* (which discount distant earnings harder) and *any wobble in the AI capex narrative*. Its return drivers are nearly the mirror image of [[xle|XLE]]'s — which is precisely why the [[xlk|XLK]]-vs-[[xle|XLE]] "new economy vs old economy" pair is so persistent.

## Seasonality

Tech seasonality blends the broad-market calendar with sector-specific event clustering:

- **November-January strength** — tech historically participates strongly in the "best six months" (Nov-Apr) seasonal window and in year-end risk-on rallies, often leading them given its high beta.
- **Mega-cap earnings clustering (late Jan, late Apr, late Jul, late Oct)** — AAPL, MSFT, NVDA, and AVGO report in tight windows that dominate XLK implied vol; IV rises into the cluster and collapses after. This is the most actionable calendar effect for XLK options.
- **Semiconductor / product-cycle catalysts** — chip-conference and product-launch windows (and increasingly AI-chip roadmap events) create episodic catalysts.
- **Summer "air pockets"** — as a high-beta sector, XLK is prone to sharper drawdowns during low-liquidity summer risk-off episodes.

As with [[xlf|XLF]], the dominant pattern is *event-driven* (mega-cap earnings) layered on the broad-market seasonal tilt. See [[seasonality]] and [[earnings-calendar]].

## How XLK Trades vs the Broad Index

- **High correlation to [[spy|SPY]]** (~0.90) but with ~1.2x beta — XLK is both a large chunk of the index *and* its highest-beta major sector, so it amplifies broad-market direction.
- **The market's growth/risk barometer.** A rising XLK/SPY ratio signals risk-on tech leadership; a falling ratio often precedes broad-market weakness because tech leads the index up and down.
- **Rates-sensitive duration trade.** XLK behaves like a long-duration asset: it underperforms sharply when real yields spike (2022) and outperforms when rates fall and liquidity is easy. This duration character is the cleanest distinction from defensive or value sectors.
- **Concentration amplifies single-name risk.** With the top 3 names at ~50%+, XLK is effectively a leveraged play on AAPL/MSFT/NVDA; an NVDA earnings night can move XLK more than a typical macro data point moves SPY.

## Options on XLK

XLK has the most active options market of any sector SPDR:

- **Weekly expirations** available
- **Strike granularity** — $1 near ATM
- **American-style**, physical settlement
- **IV regime** — typically 16-22% annualized; spikes to 30%+ during tech-specific stress (2022 rate shock, 2025 AI capex re-pricing)
- **Skew** — moderate put skew, similar to QQQ
- **Use cases** — sector hedges for concentrated tech books, sector-rotation overlays, dispersion-style trades vs single-name tech options

## Concentration Behavior

XLK pairwise correlation among holdings runs high — 0.6-0.8 in calm regimes, 0.85+ in stress. This is the structural reason XLK exists: tech stocks co-move heavily, so a single ETF captures the sector beta efficiently.

In stress events, XLK realized vol typically runs 1.3-1.5x [[spy|SPY]] realized vol (and IV trades at a similar premium). The 2022 tech selloff saw XLK drawdown ~33% vs SPY ~25%.

## Concentration Risk Angle

This is the canonical [[options-concentration-risk]] use case. The risk page explicitly references XLK as the proxy for revealing hidden concentration:

> "If you can replace your book with a position in the sector ETF, you weren't diversified."

A trader running short premium on NVDA, AVGO, MSFT, AAPL, and AMD believes they hold five positions. In stress, those five names co-move with pairwise correlation pushing 0.9. The book is functionally a single XLK short premium position, sized 5x.

The concrete test: beta-weight every position's delta and vega to XLK. If 80%+ of book risk is XLK-equivalent exposure, the book is a sector trade dressed up as a diversified portfolio.

XLK also serves as a hedging instrument: a trader who deliberately wants concentrated single-name tech short premium can buy XLK puts to cap sector-wide downside, leaving idiosyncratic single-name vol as the residual P&L driver. This is a [[dispersion-trading|dispersion-style]] structure.

## Trading Uses

- **Tech sector view** — long or short XLK to express US large-cap tech direction without picking individual names
- **Sector hedge** — a portfolio long single-name tech can hedge sector beta with XLK puts
- **Pair trade** — XLK vs [[xlf|XLF]] (tech vs financials) is the canonical growth-vs-value sector pair
- **Rotation overlay** — XLK / SPY ratio as a measure of tech leadership; rising ratio indicates risk-on tech leadership
- **Dispersion trade** — short XLK vol / long single-name tech vol exploits the index-vs-component implied correlation

## Peer & Related ETF Comparison

XLK is the cap-weighted, GICS-pure tech vehicle. The peer set lets you adjust breadth, weighting, and sub-sector focus:

| ETF | Focus | How it differs from XLK |
|-----|-------|-------------------------|
| **XLK** | Cap-weighted S&P 500 tech (GICS) | Excludes GOOGL/META/AMZN/TSLA; top-3 ~50%+ |
| [[qqq\|QQQ]] | Nasdaq-100, multi-sector | Includes GOOGL/META/AMZN/TSLA; broader, more expensive (0.20%) |
| **VGT** (Vanguard IT) | Broad US info-tech, MCap-weighted | Wider basket than XLK (includes smaller/mid-cap tech), lower fee |
| **IYW** (iShares US Tech) | US tech, cap-weighted | Includes GOOGL/META (broader tech definition), less liquid options |
| **SMH / SOXX** | Semiconductors | Pure chip-cycle play (NVDA/AVGO/TSM); far higher beta and vol |
| **IGV** (Software) | Application/systems software | Pure software play; different rate sensitivity (higher duration) |
| **SKYY / WCLD** | Cloud computing | Higher-growth, higher-vol cloud-native names |
| **MAGS** | "Magnificent 7" | Concentrated mega-cap basket spanning multiple sectors |

The key choices are **GICS-pure tech (XLK) vs broad growth (QQQ/IYW)** and **diversified tech (XLK) vs sub-sector (SMH semis, IGV software)**. If the thesis is specifically "AI chip capex," SMH/SOXX express it with far higher beta; if it's "broad mega-cap growth including GOOGL/META/AMZN," QQQ is the right tool. XLK wins on the cleanest GICS-tech beta and the deepest sector-ETF options market.

## Risks

- **Extreme single-name concentration.** Top 3 (AAPL/MSFT/NVDA) at ~50%+ means XLK is a leveraged bet on three companies; an idiosyncratic miss or guidance cut at any one moves the whole fund.
- **Duration / rates risk.** As long-duration equity, XLK is the sector most exposed to a real-yield spike; the 2022 ~33% drawdown was largely a rates re-pricing.
- **AI-capex-narrative risk.** A meaningful chunk of recent returns rides the AI data-center capex cycle (NVDA/AVGO/MSFT); a slowdown or "AI capex re-pricing" (the 2025 episode) can de-rate the sector quickly.
- **Valuation / crowding.** Tech routinely trades at premium multiples with crowded positioning; mean-reversion and de-grossing events hit it hardest.
- **Correlation collapse of diversification.** Pairwise correlation among holdings runs 0.6-0.8 calm, 0.85+ in stress — a "diversified" five-name tech book becomes one XLK position exactly when it matters. See [[options-concentration-risk]].
- **Regulatory / geopolitical.** Antitrust action, semiconductor export controls, and China-revenue exposure are recurring episodic shocks.
- **Rebalance reweighting.** S&P's capping methodology can shift top-holding weights at quarterly rebalances, introducing non-fundamental tracking quirks.

## Key Relationships

- **XLK vs QQQ**: ~0.95+ correlated; QQQ has a slightly broader basket
- **XLK vs SPY**: ~0.90 correlated, but with ~1.2x beta to SPY in normal regimes
- **XLK vs interest rates**: negative correlation; tech is long-duration equity (high P/E, distant earnings) and suffers when real rates rise
- **XLK vs USD**: mild negative correlation (mega-cap tech earns globally, strong dollar pressures earnings)

## Sources

- State Street SPDR official fund documentation
- S&P Dow Jones Indices methodology for Select Sector Indices
- CBOE options market statistics

## Related

- [[spy]] — broad market benchmark
- [[qqq]] — broader tech/growth ETF; closest comparison
- [[xlf]] — financial sector SPDR; common pair-trade counterpart
- [[xle]] — energy sector SPDR; "old economy vs new economy" pair counterpart
- [[sector-rotation]] — XLK as a sector-rotation building block
- [[seasonality]] — XLK's earnings- and risk-on calendar
- [[earnings-calendar]] — mega-cap earnings cluster that drives XLK IV
- [[options-concentration-risk]] — XLK as the proxy for hidden tech concentration
- [[dxy]] — US dollar; mild inverse to mega-cap tech earnings
- [[apple]], [[microsoft]], [[nvidia]], [[broadcom]] — dominant single-name holdings
- [[sp500]] — underlying parent index
