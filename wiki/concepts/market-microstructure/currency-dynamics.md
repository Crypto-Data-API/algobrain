---
title: "Currency Dynamics"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [fundamental-analysis, macro, forex]
aliases: ["currency dynamics", "exchange rates", "FX fundamentals"]
domain: [fundamental-analysis]
difficulty: intermediate
related: ["[[macroeconomics]]", "[[forex]]", "[[interest-rates]]", "[[trade-balance]]", "[[monetary-policy]]", "[[central-bank]]"]
---

Exchange rates are determined by relative macroeconomic fundamentals between countries. Understanding what drives currencies requires tracking interest rate differentials, growth expectations, capital flows, and risk sentiment simultaneously — no single factor dominates at all times.

## What Drives Currencies

Currency values are set at the margin by capital flows, which respond to several interrelated forces:

- **Interest rate differentials (carry)** — Higher [[interest-rates]] attract capital, strengthening the currency. The most direct short-term driver. Central bank policy divergence (e.g., Fed hiking while ECB holds) creates strong directional moves.
- **Growth differentials** — Faster economic growth attracts investment and increases demand for the currency. GDP surprises relative to expectations matter more than absolute levels.
- **Capital flows** — Foreign direct investment, portfolio flows (equities, bonds), and speculative flows all affect exchange rates. Large institutional rebalancing (e.g., pension funds, sovereign wealth funds) can move markets for extended periods.
- **Current account balance** — Persistent [[trade-balance|trade deficits]] create structural selling pressure on the currency, offset by capital account inflows. Countries with large surpluses (Germany, Japan historically) tend to have undervalued currencies.
- **Risk sentiment** — In risk-off environments, capital flows to safe havens (USD, JPY, CHF). In risk-on environments, capital flows to higher-yielding and emerging market currencies. This binary framework explains much of short-term FX movement.

## Purchasing Power Parity (PPP)

PPP holds that exchange rates should adjust so that identical goods cost the same across countries when converted to a common currency. The Big Mac Index is a well-known informal measure.

PPP is a useful long-run anchor — currencies that are significantly over- or undervalued relative to PPP tend to revert over 5-10 year horizons. However, PPP is a poor short-term predictor. Deviations from PPP can persist for years or decades because capital flows, not goods arbitrage, dominate FX markets in the short run.

## Interest Rate Parity

Interest rate parity links [[interest-rates]] differentials to forward exchange rates. If US rates are 5% and EUR rates are 3%, the forward rate must price in a ~2% annual depreciation of USD vs. EUR — otherwise risk-free arbitrage is possible.

Covered interest rate parity (using forwards) holds almost exactly due to arbitrage. Uncovered interest rate parity (spot rate expectations) is routinely violated — this is why [[carry-trade|carry trades]] are profitable.

## The Dollar Smile

The dollar smile theory (Stephen Jen) explains why the USD strengthens in two opposite scenarios:

1. **Left side of the smile** — Global risk-off, crisis conditions. USD strengthens as the world's safe haven and reserve currency. Capital flees to US Treasuries.
2. **Bottom of the smile** — US growth is average, global growth is strong. USD weakens as capital seeks higher returns abroad. This is the "Goldilocks for everyone else" scenario.
3. **Right side of the smile** — US growth outperforms the rest of the world. USD strengthens on relative growth advantage and higher rate expectations.

The dollar smile explains the counterintuitive pattern where USD can rally during both recessions and booms.

## Carry Trades

Carry trades involve borrowing in a low-interest-rate currency (historically JPY, CHF, EUR) and investing in a high-interest-rate currency (AUD, NZD, emerging market currencies). The trader profits from the interest rate differential as long as the exchange rate doesn't move against them by more than the carry.

Carry trades work in calm, trending environments where [[volatility]] is low. The risk is that carry trade unwinds are violent and reflexive — as the high-yield currency starts falling, stop-losses trigger more selling, attracting more unwinds in a cascade. The October 1998 JPY carry unwind and the August 2024 JPY carry unwind are canonical examples.

Risk characteristics: carry trades earn small, steady returns with occasional large drawdowns — the opposite of buying insurance. This negative skew profile means carry strategies can appear profitable for years before a single event wipes out cumulative gains.

See [[carry-trade]] for detailed strategy mechanics.

## Reserve Currency Dynamics

The USD serves as the world's primary reserve currency, comprising roughly 58% of global foreign exchange reserves (down from 71% in 2000). This creates structural demand for dollars:

- **Trade invoicing** — Most global commodity trade (oil, metals) is priced in USD, creating constant transactional demand.
- **Petrodollar system** — Oil exporters receive USD, which they recycle into US Treasuries and US assets.
- **Central bank reserves** — Foreign [[central-bank|central banks]] hold USD reserves for intervention and stability purposes.
- **Eurodollar system** — The offshore dollar lending market (estimated $13T+) creates global demand for dollar funding.

**De-dollarization trends**: China and other nations are actively working to reduce USD dependence through bilateral currency agreements, the digital yuan, and alternative payment systems. Progress has been slow — network effects and deep US capital markets make the dollar extremely difficult to displace. The euro and yuan remain distant second and third.

## Emerging Market Currency Risk

Emerging market currencies face a unique vulnerability: dollar-denominated debt. When an EM country borrows in USD, a depreciation of its own currency increases the real burden of that debt, which further weakens the currency, creating a reflexive spiral.

This dynamic explains recurring EM crises: the 1997 Asian financial crisis, the 2018 Turkish lira crisis, and periodic Argentine peso collapses. Countries that borrow primarily in their own currency (and have floating exchange rates) are far less vulnerable to this feedback loop.

Key risk factors for EM currencies include external debt/GDP ratio, current account deficit, foreign reserve adequacy, political stability, and commodity dependence.

## Trading Implications

- Currency moves tend to trend — [[momentum]] strategies have historically worked better in FX than in equities.
- Central bank policy divergence creates the strongest and most sustained FX trends.
- Positioning and sentiment indicators (CFTC COT reports, risk reversals) provide useful contrarian signals at extremes.
- FX [[volatility]] is typically lower than equity volatility but leverage is much higher, creating similar risk profiles.

## Related

- [[macroeconomics]] — broader macro framework
- [[monetary-policy]] — central bank actions that drive rate differentials
- [[trade-balance]] — current account component of currency fundamentals
- [[carry-trade]] — strategy exploiting interest rate differentials
- [[interest-rates]] — the most direct driver of short-term FX moves
- [[forex]] — the market where currencies are traded

## Sources

- Rosenberg, M. (2003). *Exchange Rate Determination: Models and Strategies for Exchange-Rate Forecasting.* McGraw-Hill — interest-rate-parity and PPP frameworks
- Jen, S. (2001). Morgan Stanley research notes introducing the "Dollar Smile" theory
- Brunnermeier, M., Nagel, S., Pedersen, L. (2008). "Carry Trades and Currency Crashes." *NBER Macroeconomics Annual* — negative-skew profile of carry, violation of uncovered interest parity
- IMF COFER data — currency composition of official foreign-exchange reserves (USD reserve share)
- Bank for International Settlements (BIS) Triennial Central Bank Survey — FX market turnover and structure
