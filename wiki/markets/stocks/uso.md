---
title: "USO (United States Oil Fund)"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [stocks, commodities, oil, etf, options, futures, derivatives]
aliases: ["USO ETF", "United States Oil Fund LP", "Oil ETF"]
related: ["[[oil]]", "[[xle]]", "[[gld]]", "[[uup]]", "[[options-concentration-risk]]", "[[commodities]]", "[[contango]]", "[[backwardation]]"]
---

USO is the United States Oil Fund, LP, issued by United States Commodity Funds (USCF). It seeks to track the daily percentage changes in the price of West Texas Intermediate (WTI) light sweet crude oil by holding a diversified basket of WTI futures contracts. USO is the most liquid listed instrument for retail oil exposure and the standard vehicle for trading WTI oil price moves without a futures account. It is famously imperfect as a long-term oil tracker due to roll-yield mechanics.

> **Critical distinction:** USO is a **commodity-futures ETF**, not an equity-sector ETF. It does not hold oil companies, pays no dividend, and is structured as a limited partnership rather than an open-end fund. This makes it fundamentally different from the energy-equity SPDR [[xle|XLE]] (which holds Exxon, Chevron, and other [[energy|energy]] producers) and from every Select Sector SPDR. The page below treats USO primarily as a derivative on the WTI futures curve.

## What It Holds & How It Tracks Oil

USO does not own physical [[oil|crude oil]] — storing and insuring barrels is impractical — and it does not own oil-producing companies. Instead it holds a laddered basket of exchange-traded **WTI futures contracts** ([[commodities|commodity]] derivatives on CME/NYMEX). Its benchmark is the daily percentage change in the price of the near-month WTI contract, not spot crude. Three structural consequences follow:

1. **Curve exposure, not spot exposure.** USO's return is a function of the *futures curve* — its shape ([[contango]] vs [[backwardation]]) matters as much as the level of oil over any holding period beyond a day.
2. **No yield, ongoing roll cost.** Unlike [[xle|XLE]] there is no dividend; instead there is a recurring drag (or boost) from rolling contracts forward.
3. **Daily-tracking design.** Like leveraged/inverse products, USO is engineered to track *daily* moves; compounding and roll mean multi-month returns diverge from a naive "oil went up X%" expectation.

Since the April 2020 restructuring, USO spreads its holdings across **multiple contract months** (a maturity ladder) rather than concentrating in the front month, which dampens the most extreme roll and expiration risks but does not eliminate the contango tax.

## Key Facts

| Metric | Value |
|--------|-------|
| **Ticker** | USO |
| **Underlying** | WTI crude oil futures (laddered across multiple expiries) |
| **Issuer** | United States Commodity Funds (USCF) |
| **Structure** | Limited partnership (1099 reporting, post-2020 restructure) |
| **Inception** | April 10, 2006 |
| **Expense ratio** | 0.60-0.80% (varies; expense ratio plus brokerage costs of futures rolls) |
| **AUM** | approximately $1-2B (as of early 2026; smaller than equity-sector ETFs) |
| **Avg daily volume** | approx 3-8M shares/day |
| **Options liquidity** | Deep for a commodity ETF — most liquid oil-linked options accessible to retail |
| **Dividend** | None |

## Roll Yield and Tracking Error

USO holds WTI futures, not physical oil. Each month, expiring futures must be sold and longer-dated futures purchased. This "roll" creates persistent tracking error vs spot WTI:

- **Contango** (futures priced above spot, the historical norm): rolling into more expensive contracts erodes returns — negative roll yield
- **Backwardation** (futures priced below spot, less common): rolling into cheaper contracts adds returns — positive roll yield

In sustained contango (e.g., 2014-2017, much of 2020), USO has dramatically underperformed spot WTI. In backwardation (2022 post-Russia invasion, parts of 2023), USO can outperform spot.

| Curve state | Definition | Roll effect on USO | Typical regime |
|-------------|-----------|--------------------|----------------|
| **[[contango|Contango]]** | Longer-dated futures priced **above** near-dated | **Negative** roll yield — sell low (expiring), buy high (deferred) | Oversupply, high inventories, weak prompt demand (the historical norm for oil) |
| **[[backwardation|Backwardation]]** | Longer-dated futures priced **below** near-dated | **Positive** roll yield — sell high (expiring), buy low (deferred) | Tight prompt supply, supply shock, strong immediate demand |

The size of the drag/boost scales with the *steepness* of the curve, not just its sign. A steep contango can cost a long USO holder several percent per month in roll alone, independent of the oil price — which is why even a flat-to-rising spot oil price can leave USO meaningfully lower over a quarter. Conversely, deep backwardation (as in 2022) can let USO outrun spot. This roll mechanic is the single most important thing to understand about the product.

The April 2020 episode is the canonical extreme: WTI front-month futures went negative (-$37/bbl). USO had previously held only the front month; the structural risk forced an emergency restructuring to spread holdings across multiple maturities. USO subsequently traded at sustained premium to NAV during the restructure.

**Implication for traders**: USO is a usable instrument for short-term directional oil trades (days to a few weeks). It is *not* a buy-and-hold oil proxy. For sustained oil exposure, [[xle|XLE]] (energy equities with dividends) typically delivers better total return.

## USO vs Spot Oil vs Energy Equities

These three are commonly conflated but behave very differently:

| Vehicle | What it is | Pays income? | Long-term oil-price tracking | Key extra drivers |
|---------|-----------|--------------|------------------------------|-------------------|
| **Spot WTI** | The physical/cash crude price | No | The reference — but not directly investable by retail | Inventories, prompt supply/demand |
| **USO** | Basket of WTI **futures** | No | Poor over months (roll decay in contango); good intraday/day | Curve shape, roll mechanics, fund-flow/NAV premium effects |
| **[[xle|XLE]]** | [[energy|Energy]]-sector **equities** (Exxon, Chevron, etc.) | **Yes** (dividends) | Indirect — equity beta to oil, but with company-level overlays | Capital discipline, buybacks, refining margins, opex leverage, broad-market beta |

XLE is an *equity* claim on companies whose profits rise and fall with oil, layered with corporate factors (dividends, buybacks, balance-sheet leverage, refining cracks, and general equity-market beta via [[spy|SPY]]). USO is a *direct* (if leaky) claim on the WTI futures curve. As a result XLE can rise while oil falls (e.g., on cost cuts or buybacks) and USO can fall while spot oil is flat (contango drag). The **long XLE / short USO** pair isolates the energy-equity premium and dividend carry while neutralizing much of the raw oil-price move; the reverse pair expresses a view that capital discipline or refining will lag the commodity.

## Peer & Related Commodity Vehicles

| Ticker | Vehicle | Notes |
|--------|---------|-------|
| **USO** | US Oil Fund (WTI futures basket) | Most liquid retail WTI vehicle; this page |
| **BNO** | US Brent Oil Fund (USCF) | Tracks Brent instead of WTI; useful for WTI-Brent spread views |
| **USL** | US 12-Month Oil Fund (USCF) | Spreads holdings evenly across 12 months to *reduce* roll/contango drag vs USO |
| **DBO / OILK** | Invesco / ProShares | Optimized-roll oil-futures funds designed to minimize contango cost |
| **UCO / SCO** | ProShares 2x / -2x | Leveraged and inverse oil-futures products; daily-rebalanced, severe decay |
| **[[xle|XLE]]** | Energy-equity SPDR | Equity counterpart; dividends, company factors |
| **[[gld|GLD]]** | Gold ETF | Different commodity; precious-metals vol diversifier |

USL and the optimized-roll funds (DBO, OILK) exist precisely to address USO's signature flaw — they ladder or curve-optimize their futures to soften contango drag, at the cost of tracking the front-month less tightly on short-term moves. USO remains the most liquid and the deepest options market of the group.

## Risks

- **Roll decay (contango tax)** — the defining structural risk; sustained contango erodes long USO returns regardless of the oil price. Not suitable for buy-and-hold.
- **Negative-price / curve-dislocation risk** — the April 2020 episode (front-month WTI to **-$37/bbl**) showed futures can do things spot "cannot," forcing emergency restructuring. The multi-month ladder mitigates but does not remove curve risk.
- **NAV premium/discount risk** — during the 2020 restructure USO traded at a sustained **premium to NAV**; creation halts or capacity limits can decouple price from underlying.
- **Volatility / tail risk** — crude IV spikes to 60%+ in shocks; short USO premium books were destroyed in March 2020.
- **Structural / tax complexity** — limited-partnership structure means **K-1 / 1099** reporting (post-2020 restructure) rather than simple 1099-DIV, a consideration for taxable accounts.
- **Leverage-product confusion** — UCO/SCO and similar 2x/inverse oil ETPs compound this decay and are unsuitable for holds beyond a day.

## Options on USO

USO hosts the most liquid oil-linked options market accessible to retail (without opening a futures account for direct CL options):

- **Weekly and monthly expirations**
- **Strike granularity** — $0.50 increments near ATM
- **American-style**, physical settlement (delivery of USO shares)
- **IV regime** — typically 25-40% annualized; spikes to 60%+ during oil shocks (March 2020 negative oil, February 2022 Russia invasion, 2023-2024 Middle East tensions)
- **Skew** — pronounced two-sided skew; both put skew (demand destruction) and call skew (supply shock)
- **Use cases** — short-term directional bets, tail-event hedges, commodity-vol diversification

USO IV regime correlates with crude futures IV (CL options on CME) but with USO-specific basis driven by roll mechanics during steep contango.

## Trading Uses

- **Short-term oil view** — express bullish or bearish WTI view over days to weeks (longer holds suffer roll decay in contango)
- **Geopolitical event hedge** — long USO calls before known supply-risk catalysts (OPEC meetings, Middle East tensions)
- **Inflation hedge (tactical)** — short-term oil exposure as inflation hedge; not suitable for long-term hedging due to roll
- **Vol overlay** — short USO premium during calm oil regimes harvests crude vol risk premium
- **Pair trade** — long USO / short XLE expresses views on capital discipline shifts (E&P spending cycles); long XLE / short USO captures dividend income while staying long oil
- **Tail hedge** — long USO calls cheap during calm regimes can pay multiples during supply shocks

## Concentration Risk Angle

[[options-concentration-risk]] flags commodity vol as one of the key diversifying asset classes for a short premium book over-loaded on equity vol. USO is the most liquid oil-linked options vehicle and the natural choice for adding crude-vol exposure:

- USO IV is driven by OPEC policy, geopolitical risk, US inventory dynamics, and global demand
- Equity IV is driven by earnings, growth expectations, and risk appetite
- The correlation between USO vol regime and SPY vol regime is variable but typically modest — 2020 (both spiked together on COVID) is one extreme; 2022 (USO spiked on Russia, SPY only moderately) is another

USO short premium typically harvests 4-8 vol points of [[volatility-risk-premium|VRP]] (notably larger than equity index VRP), reflecting the higher absolute vol level and the persistent contango roll tax. The carry is rich, but tail risk is real — March 2020 destroyed unprepared short USO premium books.

For diversification purposes, USO short premium is often paired with [[gld|GLD]] short premium (precious metals vol) and [[uup|UUP]] short premium (FX vol) as a "commodity and FX vol sleeve" with structurally different drivers from equity short premium.

## Key Relationships

- **USO vs WTI spot**: ~0.95+ daily correlation; tracking error accumulates over months due to roll
- **USO vs XLE**: ~0.7-0.85 correlated; XLE has additional drivers (dividends, capital discipline, refining margins)
- **USO vs DXY (dollar)**: persistent negative correlation; strong dollar pressures oil priced in dollars
- **USO vs GLD**: weakly positive; both inflation/commodity-linked but different macro drivers
- **USO vs SPY**: variable; positive in growth-driven oil rallies, negative in supply-shock-driven rallies (which hurt equities through inflation channel)

## Sources

- USCF United States Oil Fund prospectus and trust documentation
- CME WTI crude oil futures specifications
- EIA Weekly Petroleum Status Report
- April 2020 negative oil price event documentation

## Related

- [[oil]] — underlying commodity
- [[energy]] — the GICS energy sector behind XLE; the equity side of the oil complex
- [[xle]] — energy equity ETF; the equity counterpart to USO
- [[gld]] — gold ETF; alternative commodity vol vehicle
- [[uup]] — dollar ETF; FX vol diversifier
- [[spy]] — broad market benchmark; variable correlation to oil
- [[options-concentration-risk]] — USO as the crude-vol diversifier for short premium books
- [[contango]] — the futures structure that creates USO's roll decay
- [[backwardation]] — the futures structure that benefits USO
- [[commodities]] — broader asset class
- [[volatility-risk-premium]] — the crude VRP harvested by short USO premium
