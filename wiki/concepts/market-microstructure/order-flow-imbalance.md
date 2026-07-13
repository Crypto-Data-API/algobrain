---
title: "Order Flow Imbalance (OFI)"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [market-microstructure, order-flow, hft, algorithmic-trading, ai-trading, indicators]
aliases: ["OFI", "Order Imbalance", "Order Flow Imbalance Signal"]
domain: [market-microstructure, algorithmic-trading]
prerequisites: ["[[order-book]]", "[[order-flow]]", "[[bid-ask-spread]]", "[[market-impact]]"]
difficulty: advanced
related: ["[[order-flow]]", "[[order-flow-analysis]]", "[[order-book]]", "[[depth-of-market]]", "[[market-impact]]", "[[high-frequency-trading]]", "[[smart-order-routing]]", "[[avellaneda-stoikov-model]]", "[[volume-imbalance]]", "[[vpin]]", "[[bid-ask-spread]]", "[[unusual-options-activity]]", "[[adverse-selection]]"]
---

Order Flow Imbalance (OFI) is a quantitative measure of the net pressure on an [[order-book]] from incoming orders, cancellations and trades. Introduced in its modern form by Cont, Kukanov & Stoikov (2014), OFI captures the cumulative change in the *quantity available* at the best bid and best ask over short time windows. It has become one of the most widely-used short-horizon predictors of price movement in equities, futures and crypto markets, and a standard feature in modern AI execution and market-making models.

## Definition

For a single-level order book at time `t`, define `q_b(t)` as the size at the best bid and `q_a(t)` as the size at the best ask. OFI over the interval `[t-1, t]` is computed by walking through every order-book event and adding or subtracting size based on which side of the book it affects:

```
ΔW_n =
  +q_b(n)              if bid price went up   (bid-side improvement)
  +q_b(n) - q_b(n-1)   if bid price unchanged
  -q_b(n-1)            if bid price went down

  -q_a(n)              if ask price went down (ask-side improvement)
  -(q_a(n) - q_a(n-1)) if ask price unchanged
  +q_a(n-1)            if ask price went up

OFI = Σ ΔW_n over the window
```

Intuitively, **adding size at the bid** or **removing size from the ask** counts as positive imbalance (buying pressure); **adding size at the ask** or **removing size from the bid** counts as negative imbalance (selling pressure).

## Why OFI Predicts Price

The Cont-Kukanov-Stoikov result shows that, over short horizons (seconds to minutes), changes in mid-price are approximately *linear* in OFI:

```
Δprice ≈ β · OFI / ADV
```

with the coefficient `β` and ADV (average daily volume) varying by stock and regime. Intuitively, persistent buy-side imbalance forces the market maker to mark prices up to manage inventory; the linear relationship has been replicated across thousands of stocks and venues.

OFI is a stronger short-horizon predictor than:

- Trade-direction imbalance alone (which ignores quote updates and cancels)
- Naive [[volume-imbalance]] (buy volume - sell volume)
- Spread changes alone

because it incorporates the *full event stream* of the order book, including aggressive limit orders that move the book without trading.

## Multi-Level OFI

Basic OFI uses only the top of book. **Deep OFI** extends the calculation to the top 5 or 10 levels, weighting deeper levels by a decay factor. Deep OFI is useful in liquid products where most flow happens just behind the touch (e.g., SPY, ES futures, BTC perpetuals), and where the touch alone is too noisy.

## Cross-Asset OFI

For correlated baskets (SPY/ES, ETH/BTC, sector ETFs and constituents), **stacked OFI** — OFI computed across the basket — is a more powerful predictor than single-asset OFI. AI execution systems often use stacked OFI features to time large orders.

## How AI Systems Use OFI

OFI is central to several AI-driven trading workflows:

1. **Optimal execution** — execution algorithms (VWAP, TWAP, IS) condition their slicing schedule on real-time OFI. When OFI is favourable (positive for a buy order), the algo accelerates; when adverse, it slows. This is the modern incarnation of Almgren-Chriss execution with a microstructure overlay.
2. **Market-making quote skewing** — market makers (Optiver, Citadel Securities, HRT) skew quotes when OFI is large and persistent, since persistent imbalance signals adverse selection. The [[avellaneda-stoikov-model|Avellaneda-Stoikov model]] is a canonical theoretical framework.
3. **Short-horizon directional alpha** — at the seconds-to-minutes horizon, OFI features feed into ML models (gradient boosting, transformers) producing short-horizon return forecasts. These are the bread and butter of many [[high-frequency-trading|HFT]] alpha strategies.
4. **Toxicity detection** — adverse OFI sustained against a market maker's quote indicates [[adverse-selection]]; together with [[vpin|VPIN]], OFI is used to flag toxic flow and trigger quote withdrawal.
5. **Options market making** — OFI on the underlying is a leading indicator for options quote movement; options market makers monitor underlying OFI in addition to options-flow signals like [[unusual-options-activity]].

## Practical Considerations

- **Latency sensitivity** — OFI's predictive horizon is short (often <1 second for liquid stocks). Capturing the alpha requires co-located infrastructure; non-HFT participants can extract a residual signal at the 1-5 minute horizon.
- **Regime dependence** — OFI's coefficient `β` collapses during stress events when [[liquidity-evaporation|liquidity evaporates]] and the book becomes too thin to be informative.
- **Spoofing contamination** — apparent OFI can be created by [[spoofing]], inflating measured signal. Modern OFI computations weight cancels by their lifetime to mitigate.
- **Discrete-tick artefacts** — OFI calculations should account for tick-size constraints (especially in penny-tick stocks and low-priced names) to avoid spurious imbalance from rounding.

## Implementation Notes

```python
# Skeleton — produces OFI from a stream of order-book updates
def compute_ofi(events, level=1):
    ofi = 0
    prev_bid_size, prev_bid_px = None, None
    prev_ask_size, prev_ask_px = None, None
    for e in events:
        bid_px, bid_sz = e.bid[level-1]
        ask_px, ask_sz = e.ask[level-1]
        if prev_bid_px is not None:
            if bid_px > prev_bid_px:    ofi += bid_sz
            elif bid_px == prev_bid_px: ofi += bid_sz - prev_bid_size
            else:                        ofi -= prev_bid_size
            if ask_px < prev_ask_px:    ofi -= ask_sz
            elif ask_px == prev_ask_px: ofi -= (ask_sz - prev_ask_size)
            else:                        ofi += prev_ask_size
        prev_bid_px, prev_bid_size = bid_px, bid_sz
        prev_ask_px, prev_ask_size = ask_px, ask_sz
    return ofi
```

Production implementations typically run on per-event microsecond data (ITCH, OUCH, MDP3) and update OFI incrementally rather than by re-scanning windows.

## Related

- [[order-flow]], [[order-flow-analysis]] — broader category
- [[order-book]], [[depth-of-market]] — underlying data structure
- [[market-impact]] — what OFI ultimately quantifies
- [[bid-ask-spread]] — interacts with OFI in market-making P&L
- [[volume-imbalance]] — simpler trade-only cousin
- [[vpin]] — alternative toxicity measure
- [[avellaneda-stoikov-model]] — theoretical market-making framework
- [[smart-order-routing]] — execution layer that consumes OFI
- [[high-frequency-trading]] — primary user community
- [[adverse-selection]] — what sustained adverse OFI signals
- [[unusual-options-activity]] — analogous concept in options markets
- [[spoofing]] — primary contamination risk

## Sources

- Cont, R., Kukanov, A., & Stoikov, S. (2014). *The Price Impact of Order Book Events*. Journal of Financial Econometrics, 12(1): 47-88 — the foundational OFI paper establishing the linear price-impact relationship.
- Avellaneda, M., & Stoikov, S. (2008). *High-Frequency Trading in a Limit Order Book*. Quantitative Finance, 8(3): 217-224 — the market-making framework that motivates OFI-based quote skewing.
- Easley, D., López de Prado, M., & O'Hara, M. (2012). *Flow Toxicity and Liquidity in a High-Frequency World*. Review of Financial Studies, 25(5): 1457-1493 — the VPIN toxicity measure related to OFI.
- Cartea, Á., Jaimungal, S., & Penalva, J. (2015). *Algorithmic and High-Frequency Trading* (Cambridge University Press) — textbook treatment of OFI and optimal execution.
