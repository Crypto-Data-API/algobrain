---
title: "Yield Curve"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [bonds, macro-trading, fundamental-analysis]
aliases: ["Term Structure"]
domain: [macro-trading, fundamental-analysis]
prerequisites: ["[[treasury-bonds]]", "[[interest-rates]]"]
difficulty: intermediate
related: ["[[bonds-overview]]", "[[macro-trading]]", "[[treasury-bonds]]", "[[federal-reserve]]", "[[recession]]"]
---

The yield curve is a plot of [[treasury-bonds|government bond]] interest rates (yields) across different maturities, from short-term (3-month T-Bills) to long-term (30-year T-Bonds). Its shape reflects market expectations about future [[interest-rates|interest rates]], economic growth, and [[inflation]].

## Yield Curve Shapes

### Normal (Upward Sloping)
Long-term yields exceed short-term yields. This is the most common shape, reflecting:
- **Term premium**: Investors demand higher compensation for locking up capital longer
- **Growth expectations**: Markets expect economic expansion and potentially higher future rates
- Typically seen during healthy economic periods

### Flat
Short- and long-term yields are roughly equal. Signals uncertainty or a transition period, often occurring as the [[federal-reserve|Federal Reserve]] tightens monetary policy.

### Inverted
Short-term yields exceed long-term yields. The most reliable [[recession]] predictor in modern finance:
- **Track record**: Has preceded every US recession since 1955, with only one false positive (1966)
- **Mechanism**: Markets expect the Fed to cut rates in the future due to economic weakness
- **Key spread**: The 2-year vs. 10-year Treasury spread (2s10s) is the most watched. When it goes negative, recession typically follows within 6-18 months

### Steep
An exaggerated normal curve with a large spread between short and long rates. Often seen at the start of an economic recovery when the Fed holds short rates low while long rates rise on growth expectations.

## Trading the Yield Curve

### Steepening/Flattening Trades
- **Bull steepener**: Short rates fall faster than long rates (Fed cutting). Go long short-duration bonds, short long-duration bonds.
- **Bear steepener**: Long rates rise faster than short rates (inflation fears). Short long-duration bonds.
- **Bull flattener**: Long rates fall faster than short rates (flight to safety). Go long long-duration bonds.
- **Bear flattener**: Short rates rise faster than long rates (Fed hiking). Short short-duration bonds.

### Duration Trades
- **TLT** (iShares 20+ Year Treasury ETF): Long-duration exposure, highly sensitive to yield curve changes
- **IEF** (iShares 7-10 Year Treasury ETF): Medium-duration exposure
- **SHY** (iShares 1-3 Year Treasury ETF): Short-duration exposure

### Macro Signals
The yield curve provides critical signals for [[macro-trading|macro traders]]:
- An inverting curve favors defensive positioning: reduce equity exposure, increase cash/[[bonds-overview|bond]] allocation
- A steepening curve from inversion often signals the recession has begun, but also that recovery is approaching
- Changes in the curve shape affect bank profitability (banks borrow short, lend long)

## Historical Inversions

| Inversion Period | Recession Start | Lead Time |
|---|---|---|
| Aug 1978 | Jan 1980 | ~17 months |
| Sep 1980 | Jul 1981 | ~10 months |
| Jan 1989 | Jul 1990 | ~18 months |
| Feb 2000 | Mar 2001 | ~13 months |
| Dec 2005 | Dec 2007 | ~24 months |
| Mar 2022 | (debated) | -- |

## Limitations

- The yield curve is influenced by central bank policy (quantitative easing can suppress long yields artificially)
- Lead times between inversion and recession vary widely (6-24 months)
- False signals are possible, though rare
- Global capital flows can distort the curve (foreign demand for safe assets)

## Related

- [[treasury-bonds]] -- The instruments that compose the yield curve
- [[bonds-overview]] -- Broader fixed income overview
- [[macro-trading]] -- Trading strategies based on macroeconomic signals
- [[federal-reserve]] -- Primary driver of short-term rates

## Sources

- Yield curve analysis is covered extensively in fixed income and macroeconomic trading literature
