---
title: "HYG (iShares iBoxx High Yield Corporate Bond ETF)"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [bonds, etf, risk-management, indicators, market-regime]
aliases: ["HYG", "iShares iBoxx $ High Yield Corporate Bond ETF", "high yield ETF", "junk bond ETF"]
related: ["[[high-yield-bonds]]", "[[credit-spreads]]", "[[credit-spread]]", "[[jnk]]", "[[lqd]]", "[[risk-on-risk-off]]", "[[risk-appetite]]", "[[etf]]", "[[vix]]", "[[bonds]]"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[bonds]]", "[[credit-spreads]]"]
difficulty: intermediate
---

**HYG** is the ticker for the **iShares iBoxx $ High Yield Corporate Bond ETF**, the most heavily traded exchange-traded fund tracking below-investment-grade ("junk") U.S. corporate bonds. Launched by iShares (BlackRock) in 2007, it is widely used both as a vehicle for high-yield credit exposure and -- because of its deep liquidity and intraday pricing -- as a real-time barometer of [[credit-spreads|credit risk]] and overall [[risk-appetite|risk appetite]] ([[risk-on-risk-off]]).

## Fund Snapshot

| Attribute | Detail |
|---|---|
| **Ticker** | HYG |
| **Full name** | iShares iBoxx $ High Yield Corporate Bond ETF |
| **Issuer** | iShares (BlackRock) |
| **Launched** | 2007 |
| **Structure** | [[etf|Exchange-traded fund]] (open-end, '40 Act) |
| **Underlying index** | Markit iBoxx USD Liquid High Yield Index |
| **Holdings** | Hundreds of U.S. dollar-denominated [[high-yield-bonds|high-yield corporate bonds]] (rated BB+ and below) |
| **Primary risk drivers** | Credit/default risk and [[credit-spreads]]; secondary interest-rate (duration) risk |
| **Distributions** | Monthly income |
| **Main peer** | [[jnk]] (SPDR Bloomberg High Yield Bond ETF) |
| **IG counterpart** | [[lqd]] (iShares iBoxx $ Investment Grade Corporate Bond ETF) |

> **Note on live figures:** the fund's current price, AUM, 30-day SEC yield, distribution yield, expense ratio, effective duration and option-adjusted spread change continuously and should be read from the iShares fund page or a market data feed rather than quoted from memory. The descriptions below are deliberately qualitative.

## What It Holds

HYG holds a large, diversified basket of [[high-yield-bonds|high-yield corporate bonds]] designed to track the Markit iBoxx USD Liquid High Yield Index. Constituents are sub-investment-grade issuers (rated BB+ and below), so the fund's price is driven primarily by the market's perception of corporate default risk and by the level of [[credit-spreads]] over Treasuries, rather than by pure interest-rate duration (though it carries some rate sensitivity too). Its main peer is **[[jnk]]** (SPDR Bloomberg High Yield Bond ETF); the investment-grade analogue is **[[lqd]]**.

### The Two Sources of HYG's Return and Risk

HYG's price moves on two distinct factors that traders should keep separate:

1. **[[credit-spreads|Credit spread]] risk (dominant).** When the market demands more yield to hold junk debt (spreads widen), high-yield bond prices fall and HYG falls. When spreads tighten, HYG rises. This is the larger and more characteristic driver.
2. **Interest-rate (duration) risk (secondary).** Like all bonds, HYG's holdings lose value when benchmark Treasury yields rise. High-yield bonds have shorter effective duration than investment-grade, so HYG is *less* rate-sensitive than [[lqd]] — but it is not rate-immune.

Because of factor (1), HYG behaves much more like a **risk asset (correlated with equities)** than like a safe-haven Treasury fund — the opposite of how people often assume "bonds" trade.

## Why Traders Watch It

HYG is far more liquid and continuously priced than the underlying cash bonds, which trade over-the-counter and infrequently. This makes it a practical real-time proxy for high-yield credit:

- **Risk sentiment gauge**: when HYG falls and its yield/spread widens, it signals risk-off conditions and tightening financial conditions; rising HYG signals risk appetite. It is often watched alongside the [[vix]] and equity indices as a cross-asset confirmation tool.
- **Credit-equity divergence**: high-yield credit historically leads or confirms equity-market stress. A falling HYG while equities hold up is treated by some as an early warning that the rally lacks credit-market support.
- **NAV premium/discount**: because the ETF prices continuously while its bonds do not, HYG can trade at a premium or discount to its net asset value, especially in stress -- itself an information signal about liquidity conditions.

## Trading Applications

- **Hedging credit risk**: short HYG (or buy puts on it) to hedge a long high-yield or leveraged-loan portfolio without selling illiquid cash bonds.
- **Macro/credit expression**: a liquid way to express a view on the credit cycle and spread direction.
- **Pairs and relative value**: HYG vs [[lqd]] (high-yield vs investment-grade) or HYG vs equities to trade credit-quality spreads and cross-asset divergences.
- **Regime input**: HYG's trend and spread level feed [[market-regime|regime]] models distinguishing risk-on from risk-off environments.

### Illustrative Stress Scenario

Suppose a credit scare hits the market. The sequence a trader typically watches unfold in HYG:

1. **Spreads widen** as default fears rise → HYG price falls even if Treasury yields are flat.
2. **Heavy redemption volume** hits the ETF, and because the underlying cash bonds trade infrequently OTC, the ETF price can drop to a **discount to NAV** — HYG becomes the market's price-discovery vehicle for an asset class that has effectively stopped trading.
3. **HYG leads equities lower**, or breaks down while equities are still holding, flagging that credit markets see stress the equity tape has not yet priced.
4. On recovery, the discount closes and HYG often **leads the bounce** as risk appetite returns.

This pattern — credit cracking before or alongside equities — is why HYG breakdowns are treated as an early risk-off tell. (Hypothetical illustration of the mechanism, not a specific historical episode.)

## HYG vs LQD vs JNK

| | **HYG** | **[[lqd]]** | **[[jnk]]** |
|---|---|---|---|
| Asset class | High-yield ("junk") corp bonds | Investment-grade corp bonds | High-yield ("junk") corp bonds |
| Credit quality | BB+ and below | BBB- and above | BB+ and below |
| Dominant risk | Credit spread | Interest-rate (duration) | Credit spread |
| Rate sensitivity | Lower (shorter duration) | Higher (longer duration) | Lower |
| Behaves like | Risk asset (equity-correlated) | Rate asset (Treasury-correlated) | Risk asset |
| Issuer | iShares / BlackRock | iShares / BlackRock | SPDR / State Street |
| Index | iBoxx USD Liquid High Yield | iBoxx USD Liquid Investment Grade | Bloomberg High Yield Very Liquid |

**HYG vs LQD** is the canonical credit-quality pair: the ratio (or spread) between them is a clean read on whether the market is rewarding or punishing credit risk. A falling HYG/LQD ratio signals deteriorating risk appetite. **HYG vs JNK** is a near-substitute pair; they track the same asset class with minor index and liquidity differences, and the choice between them is usually about liquidity, spreads, and options availability rather than exposure.

## Trading Relevance

HYG's core value to a trader is as a **liquid, intraday read on credit stress** that the underlying market cannot provide. Because credit markets often crack before equity markets in a downturn, a sharp HYG breakdown -- widening spreads, NAV discount, heavy volume -- is one of the cleaner early signals of a risk-off regime shift and is commonly used as a confirmation or filter for equity and macro positioning. The trade-off is that HYG carries both credit and rate duration, so isolating a pure credit-spread view may require pairing it against a duration-matched Treasury position, and its ETF structure means it can dislocate from fair value precisely in the crises when its signal matters most.

## Common Pitfalls and Risks

- **Liquidity illusion.** HYG is far more liquid than its underlying bonds — but that liquidity is a *wrapper*. In a true stress event the underlying cash market can freeze while HYG keeps trading, producing NAV dislocations. The ETF's liquidity does not magically create liquidity in junk bonds.
- **NAV premium/discount.** Because the ETF prices continuously while its bonds do not, HYG can trade at a premium or discount to NAV, especially in stress — itself an information signal about liquidity conditions, but a hazard for those who assume price = fair value.
- **Confusing it with a safe bond fund.** HYG is a *risk asset*. It draws down with equities in selloffs; it is not a flight-to-safety hedge the way Treasuries are.
- **Mixing two risk factors.** A move in HYG can be credit-driven or rate-driven. To isolate a pure [[credit-spread|credit-spread]] view, pair HYG against a duration-matched Treasury (or trade HYG vs [[lqd]]).
- **Default and recovery risk.** The underlying issuers can default; spread widening and rising default rates both hit the fund, and high-yield recovery rates are uncertain.
- **Distribution decay.** In prolonged stress, defaults and downgrades can erode the income stream the fund is largely held for.

## Related

- [[high-yield-bonds]] -- the underlying asset class
- [[credit-spreads]] -- the primary driver of HYG's price
- [[credit-spread]] -- spread mechanics
- [[jnk]] -- the main competing high-yield ETF
- [[lqd]] -- investment-grade counterpart, used in relative-value pairs
- [[risk-on-risk-off]] -- HYG as a sentiment gauge
- [[risk-appetite]] -- what HYG's trend proxies
- [[vix]] -- often watched together as cross-asset stress signals
- [[etf]] -- the structure HYG uses

## Sources

- iShares / BlackRock, iShares iBoxx $ High Yield Corporate Bond ETF (HYG) fund overview and prospectus.
- Markit iBoxx USD Liquid High Yield Index methodology.
- General credit-market and ETF-liquidity literature.
