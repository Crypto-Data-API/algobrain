---
title: "Equity Risk Premium"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [valuation, portfolio-theory, fundamental-analysis, stocks, treasuries]
aliases: ["ERP", "Equity Risk Premium", "Market Risk Premium", "Stock Risk Premium"]
domain: [portfolio-theory, fundamental-analysis]
prerequisites: ["[[interest-rates]]", "[[capital-asset-pricing-model]]"]
difficulty: intermediate
related:
  - "[[macroeconomics]]"
  - "[[interest-rates]]"
  - "[[bond-yields-and-stock-prices]]"
  - "[[earnings-yield]]"
  - "[[capital-asset-pricing-model]]"
  - "[[dcf-analysis]]"
  - "[[treasuries]]"
  - "[[stocks]]"
  - "[[price-to-earnings]]"
  - "[[value-vs-growth-investing]]"
---

The **equity risk premium (ERP)** is the extra return investors demand for holding stocks instead of a "risk-free" government bond. It is the single number that links the bond market to the stock market: a stock's fair value is the present value of its future cash flows discounted at the risk-free rate *plus* the equity risk premium. This page answers the practical question for a stock investor — **"why does what bonds pay change what my stocks are worth?"**

## The Core Idea (Plain English)

If a government Treasury pays you a near-certain 4%, why would you accept the uncertainty of owning a stock for the *same* 4%? You wouldn't. You demand more — say, an extra 4-5% per year — to compensate for the risk that earnings disappoint, dividends get cut, or the price falls when you need the money. That extra slice is the equity risk premium.

```
expected_stock_return  =  risk_free_rate  +  equity_risk_premium
        (what you require)     (the Treasury yield)    (your reward for taking equity risk)
```

For the whole market, the risk-free rate is usually the [[treasuries|10-year Treasury yield]] and the ERP is the market-wide premium. For a single stock, the [[capital-asset-pricing-model|CAPM]] scales the market ERP by that stock's beta:

```
required_return_for_a_stock  =  risk_free_rate  +  beta × equity_risk_premium
```

A high-beta name (volatile, economically sensitive) carries a larger effective premium; a low-beta defensive name carries a smaller one.

## Why It Matters for *My* Stocks

The ERP is the bridge in the valuation chain. Stock prices are the discounted value of future cash flows (see [[dcf-analysis]]):

```
price  =  Σ  cash_flow_t / (1 + r)^t       where  r = risk_free_rate + equity_risk_premium
```

Two forces can move `r`, and therefore your stock prices, *without any change in the company's business*:

1. **The risk-free rate moves.** When the [[bond-yields-and-stock-prices|10-year yield]] rises, `r` rises, future cash flows are discounted harder, and prices fall. (See [[interest-rates]].)
2. **The required premium moves.** When investors get fearful (recession scare, credit stress, geopolitical shock), they demand a *bigger* premium to hold stocks. The ERP widens, `r` rises, and prices fall — even if Treasury yields are flat.

This is why a market can sell off both when bond yields spike (force 1) *and* when fear spikes (force 2). The 2008 crisis was largely a force-2 event: the ERP ballooned as investors fled risk. A rate-driven 2022-style repricing was largely force 1.

## How the ERP Is Estimated

There is no single "official" ERP — it is forward-looking and unobservable, so practitioners use proxies. The two common families:

| Method | How it works | Strength / weakness |
|--------|--------------|---------------------|
| **Historical (realized)** | Average past return of stocks minus government bonds over many decades | Simple, but the past may not predict the future; sensitive to the window chosen |
| **Implied (forward-looking)** | Solve for the premium that makes today's index price equal the present value of expected future cash flows | Reacts to current prices and rates; depends on growth assumptions |

A widely cited **illustrative** long-run figure for the US is an ERP somewhere in the broad neighbourhood of 4-6% — but the realized number swings enormously by period and the *implied* number changes day to day. Treat any single figure as an estimate, not a constant. (Aswath Damodaran of NYU publishes a well-known monthly implied-ERP series; this wiki does not reproduce a current value because it changes constantly.)

A quick back-of-envelope proxy many investors watch is the **earnings-yield spread** (the "Fed model"):

```
ERP_proxy  ≈  S&P 500 earnings yield  −  10-year Treasury yield
```

See [[earnings-yield]] for the mechanics and the important caveats (it mixes a real and a nominal number, so it is a sentiment gauge, not a precise tool).

## Worked Illustration (Hypothetical)

Suppose a broad index is expected to deliver a 7% earnings yield and the 10-year Treasury yields 3%. The implied ERP proxy is **7% − 3% = 4%**. Now imagine the Treasury yield climbs to 5% while expected earnings are unchanged:

- If investors keep demanding the *same* 4% premium, the required return rises to 9%. To deliver a 9% earnings yield from unchanged earnings, the **index price must fall** (a higher earnings yield means a lower [[price-to-earnings|P/E]]).
- Alternatively, if prices don't move, the realized premium has *shrunk* to 2% — stocks have become less attractive relative to bonds.

Either way, a rise in the risk-free rate squeezes the cushion that equities offer over bonds. (These numbers are illustrative, not a forecast.)

## What Changes the ERP

- **Fear and uncertainty** — recession risk, credit stress, war, policy shocks widen the premium (investors demand more to hold stocks).
- **Liquidity and sentiment** — abundant liquidity and risk appetite compress the premium; "there is no alternative" (TINA) eras feature a thin ERP.
- **Inflation and growth expectations** — shifting views on long-run growth feed into the cash-flow side and the premium simultaneously.
- **Valuation extremes** — when the premium is unusually thin, stocks are priced for perfection and have little margin of safety; when it is fat, future long-run returns have historically tended to be higher.

## What It Means for Positioning

- A **thin ERP** (stocks barely out-yield bonds) means you are being paid little for equity risk — a reason for caution, more diversification, or favouring [[value-vs-growth-investing|value over long-duration growth]].
- A **fat ERP** (stocks yield far more than bonds) historically signals better long-run equity returns — the classic case for leaning in.
- Because the ERP is partly driven by the risk-free rate, **rising bond yields are a headwind for stock valuations** unless earnings growth or a falling premium offsets them. This is the mechanism behind [[bond-yields-and-stock-prices|"stocks vs the 10-year yield"]].

## Limitations and Cautions

- The ERP is **not directly observable** — every estimate embeds assumptions about future growth and cash flows.
- Historical averages are **regime-dependent**; the premium earned in one multi-decade window need not repeat.
- The earnings-yield "Fed model" proxy is **criticised academically** (money-illusion bias) and has weak power to forecast long-run returns — use it as a relative-value gauge only.
- A low ERP can persist for years; it is a *valuation* signal, not a *timing* signal.

## Related

- [[macroeconomics]] — the macro framework the ERP sits inside
- [[interest-rates]] — the risk-free rate, half of the required-return formula
- [[bond-yields-and-stock-prices]] — how the 10-year yield competes with stocks
- [[capital-asset-pricing-model]] — scales the market ERP to a single stock via beta
- [[dcf-analysis]] — where the discount rate (risk-free + ERP) is applied
- [[earnings-yield]] — the basis of the earnings-yield-spread ERP proxy
- [[price-to-earnings]] — multiples move inversely to the required return
- [[value-vs-growth-investing]] — duration and ERP sensitivity differ by style
- [[treasuries]] — the risk-free benchmark
- [[stocks]] — the asset class the premium compensates you for holding

## Sources

- Aswath Damodaran (NYU Stern) — public writing and monthly implied equity-risk-premium estimates for the US market.
- Sharpe, W. F. (1964); Lintner, J. (1965) — the Capital Asset Pricing Model, which formalises required return = risk-free + beta × market premium.
- General valuation literature (Gordon Growth / discounted-cash-flow framework). No specific wiki source ingested yet.
