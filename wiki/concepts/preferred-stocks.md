---
title: "Preferred Stocks"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [stocks, fundamental-analysis, valuation, bonds]
aliases: ["Preferred Stock", "Preferred Shares", "Preference Shares", "Preferreds", "Preferred Stocks"]
domain: [fundamental-analysis]
prerequisites: ["[[stocks]]", "[[bonds]]"]
difficulty: intermediate
related: ["[[stocks]]", "[[bonds]]", "[[dividend]]", "[[capital-structure]]", "[[convertible-bonds]]", "[[interest-rate-risk]]", "[[valuation]]"]
---

Preferred stock is a hybrid security that sits between [[bonds]] and [[stocks|common equity]] in a company's [[capital-structure]]. Preferred shareholders receive fixed dividends with priority over common shareholders and a senior claim on assets in liquidation, but typically give up voting rights and the unlimited upside of common stock. Functionally, preferreds behave more like perpetual fixed-income instruments than like equity, which is why they trade primarily on yield and interest-rate sensitivity.

## Overview

Preferred stock combines features of debt and equity:

- **Fixed dividend**: pays a stated dividend (e.g. 6% of a $25 par value = $1.50/year), usually quarterly, set at issuance. Unlike bond coupons, preferred dividends can legally be skipped without triggering default — but doing so is a severe negative signal.
- **Priority**: ranks above common stock for both dividends (common dividends cannot be paid while preferred dividends are in arrears) and liquidation claims, but below all debt.
- **No/limited voting**: preferred holders generally cannot vote on corporate matters, though arrears often trigger limited voting rights.
- **Par value**: usually issued at $25 or $100 par; market price floats with interest rates and credit quality.

## Types

| Type | Feature |
|---|---|
| **Cumulative** | Skipped ("passed") dividends accumulate and must be paid in full before any common dividend. The standard, more investor-protective form. |
| **Non-cumulative** | Skipped dividends are gone forever. Common in bank preferreds (regulators favor it as loss-absorbing capital). |
| **Convertible** | Can be exchanged for a set number of common shares; adds equity upside (see [[convertible-bonds]] for the analogous debt instrument). |
| **Callable / redeemable** | Issuer can buy back at par after a call date, capping price upside when rates fall. |
| **Perpetual vs. term** | Most are perpetual (no maturity); some have a fixed redemption date. |
| **Fixed-to-floating** | Pays a fixed rate, then switches to a floating spread over a benchmark after a set period. |

## Valuation

Because most preferreds are perpetual fixed-payment instruments, they are valued like a perpetuity:

```
Price ≈ Annual Dividend / Required Yield
```

A $25-par, 6% preferred ($1.50/yr) priced to a 7.5% required yield trades at `1.50 / 0.075 = $20`. This makes preferred prices highly sensitive to interest rates ([[interest-rate-risk]]): when market yields rise, preferred prices fall, just like long-duration bonds. Credit deterioration and call risk further compress prices.

## Trading relevance

- **Yield instrument, not a growth vehicle.** Preferreds are bought for income and relative stability, not capital appreciation. They typically yield more than the same issuer's senior debt (compensating for subordination and dividend-deferral risk) but less than common-equity total return potential.
- **Rate-duration proxy.** Perpetual preferreds have very long effective duration; they are effectively a leveraged bet on long-term rates. In a rate-cutting regime they appreciate; in a hiking regime they can fall sharply (2022 saw large preferred drawdowns).
- **Bank capital and crisis risk.** Many preferreds are issued by banks as regulatory capital (and the related [[contingent-convertible-bonds|CoCos / AT1]] in Europe). In a banking crisis these can be wiped out or converted — the Credit Suisse AT1 write-down (March 2023) is the cautionary example. Non-cumulative bank preferreds carry real dividend-suspension risk.
- **Call risk caps upside.** When rates fall, issuers call high-coupon preferreds, so the price rarely rises far above par — an asymmetric, bond-like payoff. Yield-to-call, not current yield, is the honest metric for premium-priced callables.
- **Tax treatment (US).** Many US preferred dividends qualify for lower qualified-dividend tax rates and the corporate dividends-received deduction, making them attractive to certain holders — a structural source of demand.
- **Liquidity.** Preferreds are far less liquid than common shares; bid-ask spreads are wider and large orders move prices, a [[market-microstructure]] consideration for position sizing. Many investors access the sector via ETFs (e.g. PFF, PGX) rather than single names.

## Related

- [[stocks]] — common equity, the more familiar share class
- [[bonds]] — the senior fixed-income instrument preferreds resemble
- [[dividend]] — the income mechanism of preferreds
- [[capital-structure]] — where preferreds sit in the seniority stack
- [[convertible-bonds]] — related hybrid debt-equity instrument
- [[interest-rate-risk]] — the dominant price driver for preferreds
- [[valuation]] — perpetuity valuation framework

## Sources

- Fabozzi, F. *The Handbook of Fixed Income Securities* — preferred stock structures, valuation, and risk.
- Graham, B. *The Intelligent Investor* — Graham's skeptical treatment of preferred stock as combining the disadvantages of both stocks and bonds.
- US Securities and Exchange Commission, investor education materials on preferred stock features and risks.
