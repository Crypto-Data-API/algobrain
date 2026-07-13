---
title: "Convertible Bond Arbitrage"
type: concept
created: 2026-04-07
updated: 2026-06-22
status: excellent
tags: [arbitrage, fixed-income, hedge-funds, quantitative]
aliases: ["Convertible Arb", "Convert Arb"]
related: ["[[convertible-bonds]]", "[[arbitrage]]", "[[ed-thorp]]", "[[ken-griffin]]", "[[citadel]]", "[[delta-neutral]]", "[[delta-hedging]]", "[[hedging]]", "[[options]]", "[[liquidity-risk]]"]
domain: [derivatives, quantitative]
difficulty: advanced
---

Convertible bond arbitrage is a hedge fund strategy that involves buying underpriced [[convertible-bonds|convertible bonds]] and shorting the underlying stock to isolate and profit from the embedded conversion option. The strategy seeks to capture the difference between the bond's market price and its theoretical value while maintaining a [[delta-neutral]] position (via [[delta-hedging]]) that eliminates directional stock risk. It was one of the earliest quantitative hedge fund strategies, pioneered by [[ed-thorp]] in the 1960s and later adopted by traders like [[ken-griffin]], who founded [[citadel]] on the back of convertible arb profits.

> **Scope note.** This page covers the *mechanics and risk profile* of the trade. For the catalogued strategy entry — edge taxonomy, null hypothesis, kill criteria, capacity, and lifecycle — see the strategy page **convertible-arbitrage**. This page complements rather than duplicates it.

## Overview

A convertible bond is a corporate bond that can be converted into a fixed number of shares of the issuing company's stock at a specified conversion price. This conversion feature is essentially a call option embedded in the bond. The bondholder receives regular coupon payments plus the upside optionality if the stock rises above the conversion price.

The arbitrage opportunity arises because convertible bonds are often mispriced relative to their theoretical value. The bond market and equity market price these instruments using different models and different investor bases. Dedicated convertible bond investors may not have the quantitative tools to precisely value the embedded option, while equity options traders may not follow the convertible bond market. This segmentation creates persistent pricing inefficiencies.

Thorp described in [[book-a-man-for-all-markets|A Man for All Markets]] how he developed proprietary models to value the embedded options in convertible bonds and warrants, often finding them trading at substantial discounts to fair value. By buying the underpriced convertibles and dynamically hedging with short stock positions, he generated consistent returns with minimal market risk.

## How It Works

**The basic trade**:

1. **Identify a mispriced convertible**: Use an option pricing model to value the embedded conversion option. Compare this theoretical value plus the bond's straight debt value to the bond's market price. If the bond trades below theoretical value, it is underpriced.
2. **Buy the convertible bond**: This gives you long exposure to the embedded call option plus a stream of coupon payments.
3. **Short the underlying stock**: Sell short enough shares to make the position [[delta-neutral]]. The number of shares shorted equals the bond's delta (conversion ratio x option delta).
4. **Dynamic hedging**: As the stock price moves, the delta of the embedded option changes. Rehedge by adjusting the short stock position to maintain neutrality.
5. **Collect multiple income streams**: Coupon payments from the bond, short sale rebate on the shorted stock, and trading gains from gamma rebalancing.

**Sources of profit**:

- **Undervaluation alpha**: If the convertible was purchased below theoretical value, the position profits as the market recognizes the mispricing.
- **Carry**: Coupon income from the bond minus borrowing costs and dividend payments on the short stock position. Many convertible arb strategies are "carry positive" — they generate income even without price convergence.
- **Gamma trading**: Long gamma from the embedded option means the position profits from large stock moves in either direction through the rehedging process ([[gamma-scalping]]).
- **Credit improvement**: If the issuer's credit quality improves, the bond's straight debt value increases, benefiting the long bondholder.

**Key risks**:

- **Credit risk**: If the issuer's credit deteriorates or defaults, the bond loses value faster than the short stock offsets.
- **Liquidity risk**: Convertible bonds are less liquid than stocks. In market crises, convertible bond prices can gap down with no buyers — as happened dramatically in 2008.
- **Short squeeze**: Difficulty borrowing shares for shorting, or forced buy-ins, can disrupt the hedge.
- **Model risk**: The entire strategy depends on accurate valuation of the embedded option. Incorrect volatility estimates or credit spread assumptions lead to misjudged fair value.

## Decomposing the Position: The Greeks and Their Sources

A delta-hedged convertible is, in effect, a basket of long and short exposures. Understanding which Greek each P&L stream comes from is what separates convertible arb from naive long-convertible holding:

| Exposure | Sign for the arbitrageur | Source of P&L | Main hedge |
|---|---|---|---|
| **Delta** | Neutralized (target ~0) | Hedged away — removes stock direction | Short the underlying stock |
| **Gamma** | Long | Profits from large moves either way ([[gamma-scalping]] / rehedging) | Dynamic rehedging of the short |
| **Vega** | Long | Profits if implied [[volatility]] rises | Sometimes capped via listed [[options]] |
| **Rho / carry** | Mixed | Coupon income + short rebate − dividends − borrow cost | — |
| **Credit spread (CS01)** | Long the issuer's credit | Gains if spreads tighten; loses if they widen | Buy CDS protection to strip out credit |
| **[[liquidity-risk|Liquidity]]** | Short (you are *exposed*) | Bond can gap with no bid in a crisis | Limit size; hold a cash buffer |

The clean version of the trade isolates **long gamma + long vega + positive carry** while neutralizing delta and (optionally) credit via CDS. The dangerous version leaves credit and liquidity unhedged — which is exactly what blew up in 2008.

## Worked Example: A Simple Delta-Hedged Convert

A company issues a $1,000 face convertible with a conversion ratio of 20 shares (conversion price $50). The stock trades at $40, so the embedded call is out-of-the-money; suppose the option's delta is **0.40**.

- **Delta in shares per bond** = conversion ratio × option delta = 20 × 0.40 = **8 shares**.
- For a 1,000-bond position you are long the equivalent of 20,000 conversion shares; hedge by **shorting 8,000 shares** of stock.
- **If the stock rises to $44 (+10%):** the bond gains from rising delta (now say 0.50), the short loses, but because the position is *long gamma* the bond's gain outpaces the short's loss — you **rehedge by shorting more shares** at the higher price (selling high).
- **If the stock falls to $36 (-10%):** delta drops, you **buy back shares** to reduce the short (buying low). Gamma turns volatility into realized profit regardless of direction.
- **Meanwhile you collect** the coupon and the short rebate, and pay any dividend and borrow cost — the carry.

The trade *loses* if implied vol collapses (vega), the issuer's credit deteriorates faster than the equity hedge offsets (credit), or the bond cannot be sold when you need to (liquidity). (Figures illustrative.)

## Historical Unwinds: 2005 and 2008

Convertible arb is a textbook case of a "crowded carry" trade whose risks materialize all at once:

- **2005 — the GM/Ford downgrade shock.** A wave of capital had crowded into convertible arb in 2003-04, compressing the edge. In May 2005, General Motors and Ford were downgraded to junk *at the same time* that GM's stock rallied on a takeover rumor (Kirk Kerkorian's bid). Arbitrageurs were typically long GM credit (via the convert) and short GM equity — so both legs moved against them simultaneously. Forced de-leveraging caused a sharp, self-reinforcing drawdown across the strategy, an early lesson that the "delta-neutral" trade still carries large, correlated credit and crowding risk.
- **2008 — the deleveraging cascade.** Convertible arb was one of the worst-hit hedge fund strategies in the [[2008-global-financial-crisis]]. Three forces hit together: (1) prime brokers cut [[leverage]] and pulled financing after the lehman-brothers failure; (2) short-selling bans on financials in September 2008 broke the equity hedge leg; and (3) [[liquidity-risk|liquidity]] in convertible bonds evaporated, so bonds gapped to deep discounts to theoretical value with no buyers. Convertible arb funds fell roughly 30-50% in 2008 — a [[liquidity-spiral|liquidity spiral]] in which funding stress forced fire-sales into a market with no bid. The trade snapped back hard in 2009 as bonds re-converged, rewarding survivors who could hold through the dislocation.

Both episodes illustrate the strategy's core hidden risks: it looks market-neutral on paper but is short liquidity, long credit, and vulnerable to crowding and forced deleveraging.

## Trading Applications

- **Hedge fund strategy**: Convertible arb is a recognized hedge fund sub-strategy with dedicated managers and indices. Returns tend to be moderate (5-10% annually) with low correlation to equity markets, making it attractive as a portfolio diversifier.
- **Historical significance**: [[ken-griffin]] started trading convertible bonds from his Harvard dorm room in 1987, installing a satellite dish to get real-time bond quotes. His early success in convertible arb provided the seed capital and track record to launch [[citadel]] in 1990. Thorp's Princeton Newport Partners ran convertible arb as a core strategy from the 1960s through the 1980s, compounding at roughly 20% annually.
- **Market regime sensitivity**: The strategy performs best when convertible bond issuance is high (more opportunities), credit spreads are stable, and [[volatility]] is moderate to high (increases the value of the embedded option). It struggles in credit crises when bond prices collapse and liquidity evaporates.
- **Evolution**: Modern convertible arb incorporates sophisticated credit modeling, cross-asset hedging (using CDS to hedge credit risk separately from equity risk), and high-frequency rebalancing. The strategy has become more competitive as more capital has entered, compressing the available edge.

## How Traders Use It Today

- **As a diversifying sleeve.** Allocators add convertible arb for its low correlation to long-only equity and bonds, accepting that the diversification *fails in liquidity crises* (2005, 2008) — the price of the carry.
- **With explicit credit hedging.** Modern desks strip out issuer credit with CDS so the position is cleaner long-gamma/long-vega, rather than implicitly long credit.
- **Capacity-aware sizing.** Because the edge compresses as capital crowds in and the strategy is short liquidity, disciplined desks size to what they can *exit*, not what they can buy — see [[liquidity-risk]] and the strategy page convertible-arbitrage for capacity limits and kill criteria.
- **As a primary-issuance play.** New convertible issues frequently come cheap (issuers pay an underpricing concession), so arbitrageurs are anchor buyers of new deals and hedge the equity at launch.

## Related

- [[convertible-bonds]] — the instrument itself
- [[arbitrage]] — broader category of strategies exploiting price discrepancies
- [[delta-neutral]], [[delta-hedging]] — the hedging approach central to convertible arb
- [[gamma-scalping]] — profit from rehedging long-gamma positions
- [[liquidity-risk]] — the hidden short the strategy carries
- [[ed-thorp]] — pioneer of quantitative convertible bond arbitrage
- [[ken-griffin]] — built Citadel's early track record on convertible arb
- [[citadel]] — hedge fund founded on convertible arb profits

## Sources

- (Source: [[book-a-man-for-all-markets]]) — Thorp's first-hand account of developing convertible bond arbitrage
- (Source: [[book-the-quants]]) — Patterson's narrative of how convertible arb shaped the quantitative hedge fund industry
- General market knowledge; the Greeks decomposition and worked example are illustrative, and the 2005/2008 unwind accounts draw on the widely documented public record.
