---
title: "Currency Hedging"
type: concept
created: 2026-04-13
updated: 2026-06-22
status: excellent
tags: [risk-management, portfolio-theory, forex, hedging]
aliases: ["FX Hedging", "Foreign Exchange Hedging", "Currency Risk Management"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[forex]]", "[[diversification]]"]
difficulty: intermediate
related: ["[[australian-dollar]]", "[[us-dollar]]", "[[diversification]]", "[[hedging]]", "[[forex]]", "[[risk-management]]", "[[correlation]]", "[[hedge-ratio]]", "[[forward-contract]]", "[[carry-trade]]", "[[covered-interest-rate-parity]]"]
---

Currency hedging is the practice of protecting an investment portfolio against adverse foreign exchange movements, typically using [[forward-contract|forward contracts]], options, or currency-hedged ETFs. For any investor holding assets denominated in a foreign currency, the total return is a combination of the asset's local-currency return and the exchange rate movement. When Australian investors hold international equities, a rising [[australian-dollar|AUD]] erodes returns while a falling AUD amplifies them. Fred McNaught does **not** hedge currency exposure, considering it "unpredictable and expensive." He views currency movements as largely unforecastable over the medium term and prefers to accept the volatility rather than pay the cost of hedging instruments, which can drag on long-term returns.

## The Return Decomposition

The core identity behind all currency hedging is:

**Total return (home currency) ≈ Local-asset return + Currency return + (interaction term)**

An unhedged investor earns both pieces; a fully hedged investor strips out the currency return (and pays/earns the forward points instead). Hedging is therefore a decision about whether you *want* the currency leg of the return — not a way to add return, but a way to remove an uncompensated source of [[volatility]].

## Hedging Instruments

The three primary tools for currency hedging are:

- **[[forward-contract|Forward contracts]]** — Agreements to exchange currencies at a predetermined rate on a future date. The most common institutional hedging tool. The forward rate is determined by the interest rate differential between the two currencies ([[covered-interest-rate-parity|covered interest rate parity]]). For an Australian investor hedging USD exposure, if Australian rates are higher than US rates, the forward hedge generates a positive "carry" (and vice versa).
- **Currency options** — Provide the right but not the obligation to exchange at a specified rate. More flexible than forwards (allow participation in favourable moves) but more expensive due to the option premium. Used when the investor wants downside protection while retaining upside potential.
- **Currency ETFs** — Hedged versions of international equity ETFs handle the FX hedging internally. For Australian investors, products like VGAD (hedged) versus VGS (unhedged) offer a simple way to choose currency exposure. The hedged version rolls forward contracts (typically monthly), with the cost embedded in the management expense ratio.

| Instrument | Cost | Upside participation | Best for |
|------------|------|----------------------|----------|
| Forward contract | Forward points (rate differential); can be positive carry | No — locks the rate both ways | Institutions, precise hedges |
| Option (e.g., put) | Premium paid up front | Yes — keeps favourable moves | Asymmetric, downside-only protection |
| Hedged ETF share class | Embedded in MER + roll cost | No | Retail, set-and-forget |

## Cost of Hedging

The cost of currency hedging is primarily determined by the **interest rate differential** between the domestic and foreign currency. Under [[covered-interest-rate-parity|covered interest rate parity]], the forward rate reflects this differential. When Australian interest rates exceed US rates (as they did for much of 2023–2024), hedging AUD/USD exposure is relatively cheap or even **positive-carry**. When the differential reverses, hedging becomes a drag on returns. Over long holding periods, hedging costs compound and can reduce total returns by roughly 0.5–2.0% annually depending on the rate environment. This cost is the core of Fred McNaught's argument against hedging.

Note the link to the [[carry-trade]]: hedging away a high-yield currency means *giving up* the carry, while hedging a low-yield currency you're long *earns* carry. The two are the same coin viewed from opposite sides.

## Worked Example: Unhedged vs Hedged (illustrative)

An Australian investor puts **A$100,000** into a US equity index when AUD/USD = 0.70 (so A$100k buys US$70,000). Over one year the US index returns **+10%** in USD terms, so the holding is worth US$77,000.

- **Scenario A — AUD weakens to 0.65.** Converting back: US$77,000 ÷ 0.65 = **A$118,462** → +18.5% in AUD. The unhedged investor gains an extra ~8.5% from the currency move on top of the 10% equity return.
- **Scenario B — AUD strengthens to 0.75.** Converting back: US$77,000 ÷ 0.75 = **A$102,667** → +2.7% in AUD. The rising AUD has eaten most of the 10% equity gain.
- **Scenario C — Fully hedged.** The investor locks the exchange rate via forwards, so the AUD return ≈ the USD return (~+10%), adjusted by the forward points (a small +/− depending on the rate differential). The currency outcome is removed entirely — no windfall in A, no haircut in B.

The example shows hedging does not add expected return; it **trades away the variance** of the currency leg. Whether that variance is worth keeping depends on the asset (see Portfolio Relevance below).

## Partial vs Full Hedging

Rather than choosing between 0% and 100% hedging, many institutional investors adopt **partial hedge ratios** (commonly 50%). This reflects the recognition that currency exposure provides some diversification benefit (currencies often move inversely to equity markets in risk-off events) while still reducing overall portfolio volatility. The "optimal" [[hedge-ratio|hedge ratio]] depends on the investor's base currency, the [[correlation]] between currency and asset returns, investment horizon, and risk tolerance — see [[hedge-ratio]] for the formal minimum-variance treatment. Academic research suggests that for long-horizon investors (10+ years), the case for full hedging weakens because purchasing power parity tends to hold over extended periods, meaning currencies eventually adjust to reflect relative inflation.

## ASX Context: Hedged vs Unhedged International ETFs

For Australian investors, the choice between hedged and unhedged international ETFs is one of the most consequential portfolio decisions. Key pairs include:

| Unhedged | Hedged | Index |
|----------|--------|-------|
| VGS | VGAD | MSCI World ex-Australia |
| IVV | IHVV | S&P 500 |
| NDQ | HNDQ | Nasdaq-100 |

During AUD weakness (e.g., AUD/USD falling from 0.75 to 0.65), unhedged funds significantly outperform their hedged equivalents. During AUD strength, the reverse occurs. Over the past decade, the AUD has generally weakened against USD, meaning unhedged funds have benefited. However, **past currency trends are not predictive of future movements**, and the choice should be made on portfolio-construction grounds, not a currency forecast.

## Portfolio Relevance

Currency risk is an uncompensated risk for the unhedged international investor — over long horizons FX movements add volatility without a reliable risk premium, which is the textbook argument for hedging the currency exposure of a foreign *bond* allocation (whose own volatility is low, so unhedged FX would dominate it). For foreign *equities*, the case is weaker: equity volatility swamps FX volatility, and currency exposure can act as a partial [[diversification]] hedge because safe-haven currencies (USD, JPY, CHF) tend to strengthen in risk-off episodes when equities fall. The practical levers are therefore: (1) **hedge bonds**, (2) leave **equities partly or fully unhedged**, and (3) **size the hedge to the rate differential** ([[covered-interest-rate-parity|covered interest parity]] determines whether the hedge earns or pays carry). Hedge ratios are a portfolio-construction decision, not a market-timing one — research generally finds investors cannot reliably forecast currencies, so a fixed strategic ratio (0%, 50%, or 100%) beats discretionary hedging.

## Common Pitfalls

- **Hedging equities as if they were bonds** — over-hedging high-volatility foreign equity adds cost and removes a useful risk-off diversifier.
- **Forgetting the carry sign** — hedging a high-yield currency *costs* the differential; many investors discover the drag only after the fact.
- **Roll and basis risk** — rolling short-dated forwards introduces [[basis-risk|basis risk]] and timing slippage; hedged ETFs reset periodically and can drift intra-period.
- **Currency timing** — switching between hedged and unhedged share classes based on a forecast is, in effect, an FX bet most investors lose; a fixed strategic ratio is more robust.
- **Tax and transaction frictions** — switching products to change hedging can crystallise capital gains and incur spreads.

## Sources

- Black, F. (1989). "Universal Hedging: Optimizing Currency Risk and Reward in International Equity Portfolios." *Financial Analysts Journal*, 45(4) — derives the "universal hedge ratio" (~77%) under simplifying assumptions.
- Campbell, J.Y., Serfaty-de Medeiros, K. & Viceira, L.M. (2010). "Global Currency Hedging." *Journal of Finance*, 65(1), 87–121 — finds USD, EUR, CHF act as safe-haven currencies that lower equity-portfolio risk when held unhedged.
- Perold, A.F. & Schulman, E.C. (1988). "The Free Lunch in Currency Hedging." *Financial Analysts Journal*, 44(3) — argues hedging foreign-asset currency exposure reduces risk with zero expected-return cost over the long run.
- Vanguard Australia. Product disclosure for VGS/VGAD, IVV/IHVV — hedged vs unhedged ASX-listed international equity ETF pairs.

## Related

- [[forex]] — foreign exchange market overview
- [[risk-management]] — broader risk management concepts
- [[hedge-ratio]] — formal sizing of the hedge
- [[forward-contract]] — the core institutional hedging instrument
- [[covered-interest-rate-parity]] — sets the forward rate and the cost of the hedge
- [[carry-trade]] — the flip side of hedging a yield differential
- [[australian-dollar]] — AUD-specific dynamics
- [[diversification]] — currency as a diversification factor
- [[hedging]] — general hedging concepts
