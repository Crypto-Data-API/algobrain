---
title: "Last Look"
type: concept
created: 2026-06-13
updated: 2026-06-13
status: good
tags: [forex, market-microstructure, liquidity, slippage]
domain: [market-microstructure]
difficulty: intermediate
aliases: ["Last Look", "Last-Look"]
related: ["[[forex]]", "[[liquidity-provider]]", "[[lmax-exchange]]", "[[transaction-cost-modeling]]", "[[slippage]]", "[[spot-price]]"]
---

Last look is an [[forex|FX]] execution protocol in which a [[liquidity-provider]] (LP) is granted a brief window — on the order of milliseconds — after receiving a client's trade request to either accept or reject the trade based on its most up-to-date prices. Rather than the LP's streamed quote being immediately firm and dealable, it functions as an indication that the LP may decline to honour if the market has moved in the interim. The practice is widespread in over-the-counter (OTC) spot FX and is one of the more contested aspects of modern currency market structure.

## Overview

Under a last-look arrangement, execution proceeds in three stages:

1. **Trade request** — the client (liquidity taker) sees a streamed quote from the LP and sends an order to deal on it.
2. **Price-check window** — instead of filling immediately, the LP holds the request for a short interval (the "hold time") and re-checks the request price against its current view of the market. This window is typically single-digit to tens of milliseconds.
3. **Accept or reject** — if the price is still within tolerance (or has moved in the LP's favour), the LP accepts and fills the trade. If the market has moved against the LP's quoted price beyond a threshold, the LP can reject the request, and the client receives no fill.

Because the streamed price is not firm, the client cannot be certain a trade will execute until the LP responds. On a rejection the taker must re-seek liquidity elsewhere, frequently at a worse price.

## Why It Exists

LPs defend last look as a protection mechanism against being "picked off" on stale quotes. In a fragmented, high-speed market, an LP streaming prices to many venues and counterparties cannot update every quote instantaneously. Faster counterparties can detect when an LP's quote has gone stale relative to the broader market and trade against it before the LP can refresh — a form of latency arbitrage. Last look gives the LP a final check to avoid filling such toxic flow.

The standard argument is that without last look, LPs would have to widen spreads to compensate for adverse selection from faster takers. By filtering out the most toxic flow, last look (proponents claim) allows LPs to quote tighter spreads to the broad base of clients. Whether the benefit accrues to clients or primarily protects the LP is the heart of the debate.

## The Controversy

The central criticism is **asymmetry** between liquidity takers and providers. The LP holds an option: it can decline trades that have moved against it while accepting those that have moved in its favour, and the taker has no equivalent protection. When a request is rejected, the taker is forced to re-seek liquidity — and rejections cluster precisely during fast or volatile markets, when re-execution is most likely to occur at a worse price.

Several distinctions matter:

- **Hold time** — the duration the LP holds a request before responding. Longer hold times give the LP more information about where the market is heading, increasing the value of the embedded option at the client's expense.
- **Asymmetric vs symmetric last look** — under *asymmetric* last look, the LP rejects when the market moves against it but fills when it moves in its favour. Under *symmetric* last look, the price-check tolerance is applied evenly in both directions, so the LP does not selectively capture favourable moves. Symmetric application is generally regarded as the fairer practice.

The **FX Global Code**, the principles-based standard of good practice maintained by the Global Foreign Exchange Committee (GFXC) — whose work is facilitated under the auspices of the [[bank-for-international-settlements|BIS]] — addresses last look directly in its **Principle 17**. Its guidance centres on disclosure and acceptable use: market participants employing last look should be transparent about how it operates, the price-check window should be used only as a risk-control mechanism (not to gather information or trade ahead of the client request), and trading activity using information from a client's request during the last-look window is discouraged. The Code does not ban last look but seeks to constrain its abusive forms.

## Hidden Execution Cost

Last look introduces an execution cost that is invisible to standard spread and [[slippage]] metrics. Conventional measures look at the quoted spread and the difference between expected and realised fill price — but they only see the trades that actually *fill*. Last look exerts its cost through two channels that those metrics miss:

- **Rejection rates** — a low quoted spread is illusory if a meaningful fraction of attempts to deal on it are rejected, forcing re-execution at worse levels.
- **Adverse selection on filled trades** — because the LP preferentially rejects requests that have moved against it, the trades that *do* fill are systematically those that have moved against the taker, biasing realised execution.

This ties directly to [[transaction-cost-modeling]]. A backtest that assumes orders fill at the quoted price will overstate strategy performance whenever the real-world venue uses last look, because it ignores both the rejected fills and the adverse selection on accepted ones. Realistic cost modelling must account for fill probability, not just the spread.

## Reject Codes and Hold Time

Traders operating on last-look venues should monitor execution-quality diagnostics that go beyond price:

- **Fill ratio** — the proportion of trade requests accepted versus rejected, ideally broken down by LP, by currency pair, and by market condition.
- **Reject reasons / reject codes** — LPs typically tag rejections with a reason (e.g. price moved, credit, technical). A high rate of price-related rejections concentrated in volatile windows is a warning sign.
- **Hold-time distribution** — the spread of hold times per LP. Consistently long or highly variable hold times warrant scrutiny, as they increase the value of the LP's embedded option.

Tracking these over time lets a trader compare LPs on a like-for-like basis and identify counterparties whose effective execution quality is poor despite attractive quoted spreads.

## No-Last-Look Venues

Some venues eliminate last look in favour of **firm, guaranteed execution** at displayed prices. [[lmax-exchange]] is the canonical example: it runs a central-limit-order-book exchange model with [[price-time-priority]] matching, where displayed liquidity is firm and dealable without a price-check window or rejection risk. An order that hits a displayed price fills at that price.

The trade-off is in the spread. Because LPs posting firm liquidity cannot reject after the fact, they price in the adverse-selection risk up front, which can show as **wider displayed spreads** than a last-look stream's headline quote. The taker exchanges a tighter-but-uncertain quote for a wider-but-certain one. For strategies sensitive to fill certainty — or those whose performance is eroded by rejections during volatility — the no-rejection model can deliver better realised execution despite the wider headline spread.

## Relevance to Traders

For a systematic or active FX trader, last look is a core reason that **execution quality must be measured, not assumed**:

- **Measuring execution quality** — realised fill prices and fill ratios, not quoted spreads, determine true trading cost. Last-look venues require monitoring rejection and hold-time data to know what a counterparty is actually delivering.
- **Choosing venues** — the decision between a last-look stream and a firm, no-last-look venue like [[lmax-exchange]] is a genuine trade-off between headline spread and fill certainty, and the right answer depends on the strategy's sensitivity to rejection.
- **Diagnosing underperformance** — when a strategy underperforms its backtest, the cause is sometimes a **venue/execution problem rather than a flaw in the trading logic**. Adverse selection and rejections under last look can silently degrade live results even when the signal is sound. Distinguishing an execution problem from a logic problem is essential before discarding an otherwise valid strategy.

## Related

- [[forex]]
- [[liquidity-provider]]
- [[lmax-exchange]]
- [[transaction-cost-modeling]]
- [[slippage]]
- [[spot-price]]
- [[market-microstructure]]
- [[adverse-selection]]
- [[latency-arbitrage]]

## Sources

Compiled from FX market-structure literature and the BIS FX Global Code (Source: gap-analysis research, raw/articles/2026-04-22-gap-finder-injest-forex-trading-strategies.md).
