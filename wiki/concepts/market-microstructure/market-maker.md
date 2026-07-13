---
title: Market Maker
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [market-microstructure, liquidity]
aliases: ["market-makers", "Market Makers", "MM", "designated-market-maker", "DMM"]
domain: [market-microstructure]
prerequisites: ["[[order-book]]", "[[bid-ask-spread]]", "[[liquidity]]"]
difficulty: intermediate
related:
  - "[[market-making]]"
  - "[[bid-ask-spread]]"
  - "[[order-book]]"
  - "[[liquidity]]"
  - "[[order-flow]]"
---

# Market Maker

A market maker is an entity that provides [[liquidity]] to a market by continuously quoting both buy (bid) and sell (ask) prices, profiting from the [[bid-ask-spread]].

## Overview

Market makers are essential to well-functioning markets. Without them, buyers and sellers would have to wait for a counterparty to arrive, making trading slow and inefficient. By always being willing to trade, market makers ensure that other participants can transact immediately. In return, they earn the spread on each round trip.

## How It Works

- **Quote both sides**: The market maker posts a bid and an ask on the [[order-book]] simultaneously. For example, quoting $99.95 bid / $100.05 ask on a stock.
- **Earn the spread**: If they buy at $99.95 and sell at $100.05, the $0.10 spread is gross profit (before inventory risk and costs).
- **Manage inventory**: Market makers do not want to accumulate a large directional position. They constantly adjust quotes to manage inventory -- widening the side they want to discourage and tightening the side they want to attract.
- **Speed advantage**: Modern electronic market makers use high-frequency technology to update quotes in microseconds, managing risk from adverse price movements.

## Types

- **Designated Market Makers (DMMs)**: Formally assigned to specific securities on exchanges like NYSE, with obligations to maintain fair and orderly markets.
- **Electronic/algorithmic market makers**: Firms like Citadel Securities, Jump Trading, or Wintermute (crypto) that provide liquidity across many venues using automated systems.
- **DeFi liquidity providers**: In decentralized finance, users deposit assets into automated market maker (AMM) pools and earn fees -- a different mechanism but analogous role.

## Trading Relevance

Understanding market makers helps traders interpret [[order-book]] behavior. Market makers widen spreads during uncertainty and narrow them in calm conditions. They are not adversaries -- they provide the liquidity that allows you to trade. However, trading strategies that consistently take liquidity from informed market makers (toxic [[order-flow]]) can lead to wider spreads and worse execution.

For the practice itself -- quoting mechanics, inventory models (Avellaneda-Stoikov), and options market making -- see [[market-making]]. This page covers the *participant*; [[market-making]] covers the *activity*.

## Related

- [[flash-crashes]] — market maker withdrawal is the core mechanism of flash crashes
- [[flash-crash-2010]] — HFT market makers withdrew simultaneously, causing liquidity to vanish
- [[flash-crash-2015-etf]] — ETF market makers couldn't price when underlying stocks halted
- [[high-frequency-trading]] — electronic market making as dominant HFT strategy
- [[spoofing]] — fake orders that poison the order book market makers rely on
- [[bid-ask-spread]] — the market maker's core revenue
- [[order-book]] — where market makers operate
- [[liquidity]] — market makers are the primary providers
- [[order-flow]] — market makers analyze flow to manage risk
- [[market-making]] — the practice/business of providing liquidity

## Sources

- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* (Oxford University Press, 2003) — chapters on dealers and market makers
- Maureen O'Hara, *Market Microstructure Theory* (Blackwell, 1995)
- NYSE, "Designated Market Makers" — exchange documentation on DMM obligations (nyse.com)
- SEC, "Specialists and Market Makers" — Investor.gov educational material
