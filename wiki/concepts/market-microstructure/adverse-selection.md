---
title: "Adverse Selection"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [market-microstructure, market-making, risk-management]
aliases: ["Adverse Selection", "Information Asymmetry in Trading"]
related: ["[[market-making]]", "[[bid-ask-spread]]", "[[order-flow]]", "[[high-frequency-trading]]", "[[transaction-costs]]", "[[liquidity]]"]
domain: [market-microstructure]
difficulty: advanced
---

**Adverse selection** in financial markets is the risk that a [[market-making|market maker]] or [[liquidity]] provider faces when trading against a counterparty who possesses superior information. Informed traders systematically profit at the expense of market makers, who cannot distinguish informed from uninformed [[order-flow]]. This fundamental information asymmetry is one of the primary determinants of the [[bid-ask-spread]] and a central concept in [[market-microstructure]].

## Overview

The adverse selection problem in trading was formalized by Lawrence Glosten and Paul Milgrom (1985) and Albert Kyle (1985). Their models showed that market makers face a permanent dilemma: they must quote prices (bid and ask) to all comers, but some of those counterparties know more than they do.

Consider a market maker quoting a stock at $50.00 bid / $50.05 ask. Most incoming orders are from uninformed traders (retail investors, index funds, corporate treasurers) who trade for reasons unrelated to the stock's fundamental value. The market maker profits from these trades by capturing the spread.

But some orders come from informed traders -- insiders, analysts who've done deep research, or algorithms that have detected a signal. If an informed trader knows the stock is worth $52, they will aggressively buy at $50.05. The market maker sells at $50.05, the stock rises to $52, and the market maker loses $1.95 per share. This is adverse selection: the market maker is "adversely selected" by those with better information.

## How It Works

**The Glosten-Milgrom Model:**

The [[bid-ask-spread]] can be decomposed into three components:
1. **Order processing costs** -- the fixed cost of executing a trade (technology, clearing, regulation)
2. **Inventory risk** -- compensation for holding an unbalanced position
3. **Adverse selection component** -- compensation for expected losses to informed traders

In liquid, well-researched stocks (e.g., Apple, Microsoft), adverse selection costs are relatively low because information is widely disseminated. In illiquid, thinly covered stocks, adverse selection costs are higher because information asymmetry is greater. This is why small-cap and emerging market stocks have wider spreads.

**The Kyle Model:**

Kyle's model introduces the concept of a single informed trader ("insider") who trades strategically alongside uninformed "noise traders." The market maker sets prices based on total [[order-flow]], learning from the aggregate signal. The informed trader's optimal strategy is to trade gradually, hiding their information in the noise.

Key insight: **price impact is a measure of adverse selection.** When a large buy order moves the price up, it's partly because the market maker infers that the buyer might be informed. Higher adverse selection = greater price impact = higher [[transaction-costs]] for all traders.

**VPIN (Volume-Synchronized Probability of Informed Trading):**

Developed by Easley, Lopez de Prado, and O'Hara, VPIN measures order flow toxicity in real time. It estimates the probability that trading volume is driven by informed traders. High VPIN readings indicate elevated adverse selection risk and have been shown to precede volatility events (VPIN spiked before the 2010 Flash Crash).

**Who Are the "Informed" Traders?**

- **Corporate insiders** with material non-public information (illegal but it happens)
- **Sell-side analysts** acting on proprietary research before publication
- **Quantitative firms** using statistical signals or alternative data
- **[[high-frequency-trading|HFT]] firms** with latency advantages who can process public information faster
- **Event-driven traders** who analyze corporate actions, regulatory filings, or macro data more quickly

## Trading Applications

**For Market Makers:** Managing adverse selection is the central challenge. Strategies include:
- **Widening spreads** during periods of high information asymmetry (e.g., before earnings announcements)
- **Reducing quote size** to limit exposure to informed flow
- **Faster quote updates** to avoid being "stale" when information arrives
- **Flow segmentation** -- routing likely uninformed flow (small retail orders) to internal market makers while being cautious with large institutional orders
- **Anti-gaming logic** -- detecting patterns that signal informed trading and adjusting quotes accordingly

**For Institutional Traders:** Adverse selection works in reverse -- if you *are* the informed trader, your goal is to trade without revealing your information:
- **Algorithmic execution** -- breaking large orders into small pieces using [[twap|TWAP]], [[vwap|VWAP]], or implementation shortfall algorithms
- **Dark pools** -- trading in venues where orders are hidden from other participants
- **Choosing venues carefully** -- some venues attract more toxic flow than others

**For Retail Traders:** Understanding adverse selection explains why:
- Spreads widen around earnings, FOMC meetings, and other information events
- Market orders in illiquid stocks can face significant slippage
- Payment for order flow (PFOF) exists: retail flow is *valuable* to market makers precisely because it is uninformed

**Market Design Implications:** Exchange design increasingly focuses on mitigating adverse selection. Features like speed bumps (IEX's 350-microsecond delay), frequent batch auctions, and asymmetric latency rules aim to reduce the advantage of the fastest traders, making markets fairer for slower participants. (Source: [[book-trading-and-exchanges]])

## Related

- [[market-making]] -- the activity most directly affected by adverse selection
- [[bid-ask-spread]] -- determined in large part by adverse selection costs
- [[order-flow]] -- the signal through which adverse selection manifests
- [[transaction-costs]] -- adverse selection is a hidden component of total trading costs
- [[high-frequency-trading]] -- HFT firms both exploit and provide protection against adverse selection
- [[liquidity]] -- adverse selection reduces liquidity by making market makers quote wider or smaller

## Sources

- (Source: [[book-trading-and-exchanges]]) -- Larry Harris's comprehensive treatment of adverse selection and its role in market microstructure
- (Source: [[book-algorithmic-and-high-frequency-trading]]) -- formal models of adverse selection and their implications for algorithmic trading strategies
