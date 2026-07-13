---
title: Retail Trading
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - market-microstructure
  - behavioral-finance
  - options
aliases:
  - retail-traders
  - retail-investors
  - retail-trader
  - dumb money
domain: [market-microstructure]
prerequisites: ["[[market-microstructure]]"]
difficulty: beginner
related: ["[[robinhood]]", "[[meme-stocks]]", "[[gamestop-short-squeeze]]", "[[payment-for-order-flow]]", "[[professional-vs-retail-mindset]]"]
---

# Retail Trading

Trading conducted by individual, non-institutional investors. The rise of commission-free platforms like [[robinhood]] has democratized market access, leading to a surge in retail participation since 2020.

## The Post-2020 Boom

The convergence of several factors in 2020 triggered an unprecedented retail trading boom: zero-commission brokerages (led by [[robinhood]]), pandemic lockdowns with stimulus checks, and social media communities like r/WallStreetBets on [[reddit]]. Retail options volume exploded, with individual traders accounting for over 25% of all US equity options activity by 2021.

## Meme Stocks and Coordinated Trading

The [[gamestop-short-squeeze]] of January 2021 became the defining moment of the retail trading era. Coordinated buying on [[meme-stocks]] like GME, AMC, and BBBY pitted retail traders against institutional short sellers, forcing billions in losses at hedge funds like Melvin Capital. The episode triggered Congressional hearings and a broader debate about the [[democratization-of-markets]].

## Options Democratization

Mobile-first platforms made options trading accessible to millions of new participants who previously lacked access to derivatives markets. Zero-day-to-expiration (0DTE) options became especially popular, letting retail traders make leveraged bets on intraday moves. Critics argue this resembles gambling more than investing.

## How Retail Order Flow Is Monetized

A defining feature of the commission-free era is [[payment-for-order-flow]] (PFOF): brokers like [[robinhood]] route customer orders to wholesale market makers (Citadel Securities, Virtu) who pay the broker for the flow. Retail orders are attractive to market makers because they are, on average, **uninformed** — they carry low [[adverse-selection]] risk, so the wholesaler can capture the spread reliably. This is why "free" trading is profitable: the cost is embedded in execution quality, and it is the structural reason retail flow is treated as a distinct, predictable liquidity source in [[market-microstructure]].

## Retail as a Signal

Because aggregate retail positioning is observable (through PFOF data, options dealer hedging, and sentiment surveys), professionals treat extreme retail enthusiasm as a contrarian indicator — the "dumb money" framing studied in [[behavioral-finance|behavioral finance]]. Heavy retail call-buying forces dealers into hedging flows (the "gamma" feedback loop) that can both accelerate rallies and sharpen reversals. See [[professional-vs-retail-mindset]] for the behavioral contrast.

## Crypto Access

Retail traders also drove the crypto boom of 2020-2021, with platforms like Coinbase, Binance, and Robinhood offering easy access to [[bitcoin]], [[ethereum]], and thousands of altcoins. The low barriers to entry in crypto attracted a new generation of traders who may have started with meme coins before moving to traditional markets.

## Related

- [[robinhood]]
- [[meme-stocks]]
- [[democratization-of-markets]]
- [[gamestop-short-squeeze]]
- [[reddit]]
- [[options]]
- [[payment-for-order-flow]]
- [[professional-vs-retail-mindset]]

## Sources

- Barber, Brad M., and Terrance Odean. "Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors." Journal of Finance (2000).
- Barber, Odean, et al. "Attention-Induced Trading and Returns: Evidence from Robinhood Users." Journal of Finance (2022).
- US SEC, "Staff Report on Equity and Options Market Structure Conditions in Early 2021" (GameStop / meme-stock review, 2021).
- FINRA and OCC retail options volume statistics, 2020–2022.
