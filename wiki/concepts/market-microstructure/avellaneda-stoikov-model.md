---
title: "Avellaneda-Stoikov Model"
type: concept
created: 2026-04-27
updated: 2026-04-27
status: good
tags: [market-microstructure, market-making, quantitative, stochastic-control, hft, liquidity]
aliases: ["Avellaneda-Stoikov", "AS Model", "Optimal Market Making", "Stoikov Model"]
domain: [market-microstructure]
prerequisites: ["[[market-microstructure]]", "[[limit-order-book]]", "[[brownian-motion]]"]
difficulty: advanced
related: ["[[market-making-strategy]]", "[[grid-trading]]", "[[hummingbot]]", "[[concentrated-liquidity]]", "[[order-flow]]", "[[adverse-selection]]", "[[bid-ask-spread]]"]
---

The **Avellaneda-Stoikov model** is a stochastic-control framework for optimal market making in a [[limit-order-book|limit order book]]. Published by Marco Avellaneda and Sasha Stoikov in 2008, it derives optimal bid and ask quotes that balance two competing objectives: maximizing expected spread capture against minimizing inventory risk from [[adverse-selection|adverse selection]]. It is the canonical reference for quantitative market making and the conceptual ancestor of nearly every production MM bot, including those used in crypto venues and DeFi liquidity protocols.

## The Problem It Solves

A naive [[market-makers|market maker]] posts a symmetric bid and ask around the mid-price and hopes to capture the half-spread on each round-trip fill. This works in stationary, balanced markets, but it fails in two related ways:

- **Drift**: when the mid-price trends, the MM's bids fill more often than asks (or vice versa), producing one-sided inventory accumulation.
- **Adverse selection**: informed traders preferentially trade against stale quotes, so the MM ends up systematically long into a fall and short into a rally.

A naive MM with no inventory management thus has unbounded variance in their P&L and a high probability of blow-up. The Avellaneda-Stoikov (AS) model solves this with a closed-form (under specific assumptions) prescription for *how to skew quotes when inventory is non-zero*. The skew makes the MM reluctant to grow an existing position and eager to flatten it, transferring inventory risk back into the market through pricing rather than aggressive hedging.

## Model Setup

The model is built on four assumptions that make the optimization tractable:

1. **Mid-price dynamics**: the mid-price `S_t` follows arithmetic Brownian motion:

   ```
   dS = σ dW
   ```

   where `σ` is volatility and `dW` is a standard Wiener increment. (See [[brownian-motion]].)

2. **Quote placement**: the MM continuously posts a bid at `S - δ_b` and an ask at `S + δ_a`, where `δ_b` and `δ_a` are the bid and ask half-spreads relative to mid.

3. **Fill process**: incoming market orders arrive as a Poisson process. The fill intensity declines exponentially with distance from mid:

   ```
   λ(δ) = A · exp(-k · δ)
   ```

   `A` is the order-flow rate at the touch and `k` measures how quickly fills decay as the quote moves away from mid. Both are calibrated empirically from order-book data.

4. **MM utility**: the MM has CARA (constant absolute risk aversion) preferences over terminal mark-to-market wealth at horizon `T`:

   ```
   U(x, q, s, t) = -exp(-γ · (x + q · s))
   ```

   where `x` is cash, `q` is inventory in shares (or contracts), `s` is mid-price, and `γ > 0` is the risk-aversion coefficient.

The MM chooses `δ_b(t)` and `δ_a(t)` over `[0, T]` to maximize expected utility. This is a Hamilton-Jacobi-Bellman problem, and Avellaneda and Stoikov solve it using a dimensional reduction and an asymptotic expansion in `q`.

## The Reservation Price

The first key output of the model is the **reservation price** (also called indifference price): the MM's private valuation of holding the inventory, which differs from the public mid:

```
r(s, q, t) = s − q · γ · σ² · (T − t)
```

Interpretation:

- When `q > 0` (long inventory), `r < s`: the MM's private valuation is below mid, so they are willing to *sell cheaper* and *buy only at a discount* in order to dump risk.
- When `q < 0` (short inventory), `r > s`: the MM is willing to *pay up* to cover.
- The `(T − t)` factor means the inventory penalty is largest at the start of the session and zero at the close — the model is finite-horizon.
- The `σ²` factor means inventory is more painful in volatile regimes.

The reservation price decouples the *direction* problem (how should I lean?) from the *spread* problem (how wide should I be?). All quote skew flows from this single quantity.

## Optimal Spread

The second output is the optimal total spread between bid and ask, which is *symmetric around the reservation price* (not around the mid):

```
δ_a* + δ_b* = γ · σ² · (T − t) + (2/γ) · ln(1 + γ/k)
```

This decomposes into two interpretable terms:

- **Inventory-risk term**: `γ · σ² · (T − t)`. This grows with risk aversion, with variance of mid-price moves, and with time remaining. It is the price the MM charges for warehousing risk.
- **Order-flow uncertainty term**: `(2/γ) · ln(1 + γ/k)`. This is independent of time and depends on how sensitive fill rates are to quote distance (`k`) and on the MM's risk aversion. It is the price the MM charges for the asymmetry of Poisson arrivals.

As `t → T` (end of session), the inventory term vanishes and only the order-flow term remains. This is intuitive: with no time left to be hurt by mid-price drift, the MM only needs to be compensated for the variance of the fill process itself.

## Optimal Quotes

Combining the reservation price and the optimal spread, the bid and ask quotes are:

```
bid* = r(s, q, t) − (δ_a* + δ_b*) / 2
     = s − q · γ · σ² · (T − t) − half_spread

ask* = r(s, q, t) + (δ_a* + δ_b*) / 2
     = s − q · γ · σ² · (T − t) + half_spread
```

The crucial term is `−q · γσ²(T − t)`, the **inventory skew**. It shifts both the bid and the ask in the *same direction* by an amount proportional to current inventory:

- If long (`q > 0`): both quotes shift down. The ask becomes more aggressive (closer to mid), increasing the chance of dumping inventory; the bid becomes less aggressive (further from mid), reducing the chance of accumulating more.
- If short (`q < 0`): both quotes shift up. Symmetric logic.
- If flat (`q = 0`): quotes are symmetric around mid, with the half-spread set by the order-flow term and any remaining inventory term.

This structural result — *skew, don't widen* — is the most influential takeaway of the paper.

## Practical Implementation Notes

Production AS implementations face three calibration choices:

- **`A` and `k`**: estimated from order-book data. The standard approach regresses observed fill counts (per quote distance bucket, per unit time) against `δ` to fit `A · exp(-k · δ)`. Different tick sizes, sessions, and asset classes give very different parameters.
- **`σ`**: rolling realized volatility on whatever timescale matches the MM's horizon (often seconds to minutes for HFT, hours for crypto venues).
- **`γ`**: a free parameter and the most important tuning knob. There is no objective way to pick it. In practice, operators set `γ` so that the *typical maximum inventory* under representative order flow stays within a target risk budget. Higher `γ` means tighter inventory bands and wider spreads; lower `γ` means more carry of inventory but tighter quotes.

Most production code uses the **closed-form (asymptotic) limit** rather than solving the full HJB PDE numerically. This is the formula above and is accurate enough for inventory levels well below the position cap. For larger inventory or longer horizons, full numerical solutions or finite-`T` corrections are sometimes used.

A common operational extension is to **truncate the time horizon**: rather than treating `T` as the end of the trading day, operators use a rolling lookahead of, say, one hour. This keeps the inventory penalty from collapsing artificially as the session closes and is closer to how real MMs think about inventory risk in always-on markets like crypto.

## Extensions and Variants

AS spawned an entire literature on stochastic-control market making:

- **Cartea, Jaimungal & Penalva (2015)**, *Algorithmic and High-Frequency Trading* — adds explicit market impact, adverse-selection costs, and richer fill-rate models. The textbook reference for modern MM theory.
- **Guéant, Lehalle & Tapia** — alternative formulations with general fill-rate functions, multi-asset extensions, and dealer markets. Guéant's *The Financial Mathematics of Market Liquidity* (2017) is the most thorough treatment.
- **[[hummingbot|Hummingbot]] Pure Market Making strategy** implements a simplified AS variant with operator-tunable `γ` and time-horizon parameters.
- **DeFi liquidity provision**: protocols such as [[hyperliquid-hlp|Hyperliquid HLP]], GMX GLP, and dYdX-style on-chain MMs use AS-flavored intuitions for inventory skewing, even when the explicit PDE is not solved on-chain.
- **Reinforcement-learning MM agents** typically use AS as a baseline policy or as a feature in the state space, since it provides a closed-form policy that is hard to beat without significantly richer information.

## Connection to Other Strategies

AS sits at the center of a web of related quantitative trading approaches:

- [[grid-trading]] is a discretized, non-stochastic-control approximation of AS market making. Grid spacing is a heuristic version of the AS optimal half-spread; the symmetric placement around the entry price is a crude version of the reservation price (with `q = 0` assumed). Most published grid bots ignore inventory skew, which is precisely what makes them blow up in trends.
- [[market-making-strategy]] uses AS-style reasoning explicitly when designed by quants. Pure spread-capture MMs without inventory skew are essentially betting that drift is zero.
- [[concentrated-liquidity]] AMMs (Uniswap V3 and successors) have analogous "active range" concepts: choosing a range is morally equivalent to choosing a spread, and rebalancing the range as price moves is morally equivalent to skewing reservation price by inventory.
- [[delta-hedging]] for options market making has parallel structure: an options MM whose net delta drifts away from zero faces the same "skew quotes vs. hedge directionally" tradeoff that AS formalizes for spot inventory.
- [[order-flow]] toxicity research (the VPIN literature, etc.) extends AS by making `λ(δ)` state-dependent — fills become more likely to be adverse when toxicity is high, which should widen spreads in a way the vanilla AS does not capture.

## Limitations

The model's elegance comes from strong assumptions, all of which are wrong in some regime:

- **Brownian motion is wrong**: real markets have fat tails, jumps, and regime breaks. AS understates the cost of being caught long into a crash.
- **Poisson fills are wrong**: real fills cluster around news, around toxic flow, and around correlated MM withdrawals. The independent-arrivals assumption is the model's weakest empirical link.
- **Constant volatility is wrong**: volatility is itself stochastic, and AS underestimates spreads when vol-of-vol is high.
- **Symmetric order flow is wrong**: AS assumes the same `λ(δ)` for buys and sells, which fails when order flow is one-sided (e.g. trending crypto markets).
- **Adversarial gaming**: in HFT-dominated venues, faster traders can detect the inventory skew (long inventory → cheaper ask) and front-run the MM's flattening trades. The model is not robust to opponents who model *the MM's model*.
- **No fixed costs / queue priority**: real LOBs have minimum tick sizes, queue position, exchange fees, and rebates that materially change optimal quoting and are absent from vanilla AS.

Production MMs typically use AS as a *starting policy* and overlay corrections for these failures: regime detection, toxicity filters, queue-aware placement, and short-horizon directional features that further skew the reservation price.

## Sources

- **Primary**: Avellaneda, M. & Stoikov, S. (2008). "High-frequency trading in a limit order book." *Quantitative Finance* 8(3): 217-224. [Tandfonline](https://www.tandfonline.com/doi/abs/10.1080/14697680701381228) · [Author PDF (Cornell)](https://people.orie.cornell.edu/sfs33/LimitOrderBook.pdf)
- **Antecedent**: Ho, T. & Stoll, H. R. (1981). "Optimal dealer pricing under transactions and return uncertainty." *Journal of Financial Economics* 9(1): 47-73. The first paper to derive bid-ask quotes from utility maximization with stochastic demand and inventory risk; AS extends Ho-Stoll into the limit-order-book setting.
- **Extension (textbook)**: Cartea, Á., Jaimungal, S., & Penalva, J. (2015). *Algorithmic and High-Frequency Trading*. Cambridge University Press.
- **Extension (textbook)**: Guéant, O. (2017). *The Financial Mathematics of Market Liquidity*. Chapman & Hall / CRC.
- **Practical implementation**: Hummingbot Pure Market Making strategy documentation (open-source reference implementation).

## Related

- [[market-making-strategy]]
- [[grid-trading]]
- [[hummingbot]]
- [[concentrated-liquidity]]
- [[order-flow]]
- [[adverse-selection]]
- [[bid-ask-spread]]
- [[market-microstructure]]
- [[limit-order-book]]
- [[brownian-motion]]
- [[delta-hedging]]
- [[hyperliquid-hlp]]
