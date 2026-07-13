---
title: "BitMEX"
type: entity
created: 2026-04-15
updated: 2026-06-10
status: good
tags: [crypto, exchange, derivatives, bitcoin, leverage, history, regulation]
entity_type: exchange
founded: 2014
headquarters: "Victoria, Seychelles (operations historically run from Hong Kong)"
website: "https://www.bitmex.com"
aliases: ["BitMEX", "Bitmex", "Bitcoin Mercantile Exchange", "HDR Global Trading"]
related: ["[[perpetual-futures]]", "[[arthur-hayes]]", "[[binance]]", "[[bybit]]", "[[hyperliquid]]", "[[cftc]]", "[[funding-rates]]", "[[leverage]]", "[[liquidation]]"]
---

BitMEX (Bitcoin Mercantile Exchange) is a crypto derivatives exchange founded in 2014 by [[arthur-hayes|Arthur Hayes]], Ben Delo, and Samuel Reed, operated by HDR Global Trading Ltd. It invented the **perpetual swap** — the funding-rate-anchored, never-expiring futures contract that is now the dominant instrument in all of crypto trading — and popularized 100x [[leverage]] for retail. Once the largest bitcoin derivatives venue in the world, BitMEX was hollowed out by the 2020 US criminal case against its founders and by competition from [[binance|Binance]] and [[bybit|Bybit]]; it survives in 2026 as a mid-tier derivatives exchange, while its founders received full presidential pardons in March 2025.

## Overview

BitMEX launched in 2014 and in 2016 introduced the XBTUSD perpetual swap: an inverse, bitcoin-margined contract with no expiry, tethered to spot via a [[funding-rates|funding rate]] exchanged between longs and shorts every 8 hours. The design solved the roll-cost and basis problems of dated futures and became the template copied by Binance, Bybit, OKX, Deribit, [[hyperliquid|Hyperliquid]], and essentially every crypto venue since. At its 2018-2019 peak, BitMEX routinely cleared several billion dollars of notional per day, its XBTUSD book was the deepest in crypto, and the "BitMEX funding rate" was the market's de facto positioning gauge.

Key historical moments:

- **2016** — XBTUSD perpetual swap launches; 100x leverage offered on BTC.
- **2018** — Peak dominance; Hayes' Hong Kong office and the firm's rented aquarium-floor HQ become crypto-era lore. Arthur Hayes' market commentary newsletter becomes widely read.
- **2020-03-13** — During the COVID crash, BitMEX suffers an outage ("DDoS") while BTC cascades toward $3,600; liquidation spirals on its inverse contracts are widely credited with deepening the crash, and the pause in its liquidation engine arguably stopped BTC going to zero on the venue.
- **2020-10-01** — US DOJ criminally charges Hayes, Delo, Reed, and head of business development Gregory Dwyer with Bank Secrecy Act violations; the [[cftc|CFTC]] sues civilly for operating an unregistered trading platform and AML failures. Volume and open interest flee almost immediately.
- **2021-08** — BitMEX entities settle with CFTC/FinCEN for a **$100 million civil penalty** (up to $50M creditable against FinCEN payments).
- **2022** — All three founders plead guilty to BSA violations. Sentences: Hayes — 6 months home confinement + 2 years probation; Delo — 30 months probation; Reed — 18 months probation; each forfeited $10 million. Dwyer pleads guilty and is fined.
- **2024-07 / 2025-01** — HDR Global Trading itself pleads guilty; the company is sentenced to a $100 million fine and two years' probation (DOJ, SDNY).
- **2025-03-28** — President Trump pardons Hayes, Delo, Reed, and Dwyer. Delo calls it "a vindication of the position we always held."

## Current Status (2026)

BitMEX still operates, fully KYC'd since 2021, but is a shadow of its former self: trackers rank it roughly #29-#80 among centralized exchanges depending on methodology, with 24-hour derivatives volume in the low hundreds of millions of dollars (CoinGecko/Messari/BitDegree, mid-2026) versus tens of billions at Binance. In late 2025 it cut spot fees to a flat 0.05%, and from 2026-04-21 it set equity-perpetual maker fees at -0.025% (a rebate) and taker fees at 0.05% — aggressive pricing aimed at recapturing flow in its newer tokenized-equity perp products. Periodic acquisition rumors (e.g., 2022 talks, later sale explorations) have never produced a confirmed deal.

## Trading Relevance

1. **The perpetual swap itself** — every funding-rate carry trade, basis trade, and perp-spot arbitrage in crypto descends from the XBTUSD design. Understanding BitMEX's inverse-contract math (P&L in BTC, nonlinear margin) is still required for reading pre-2021 crypto market history and data.
2. **Liquidation mechanics as a signal** — BitMEX pioneered the public liquidation feed; "watching the BitMEX liqs" was the original liquidation-cascade trading playbook, since generalized to [[liquidation]] heatmaps across venues.
3. **Historical data** — BitMEX's free, deep historical trade/quote data (2014-present) remains a standard research dataset for crypto microstructure and [[funding-rates|funding-rate]] studies. Its long XBTUSD funding history is the benchmark series for perp carry backtests.
4. **Regulatory case study** — the 2020 prosecution is the canonical precedent for US extraterritorial enforcement against offshore crypto venues (interface geo-blocking is not a defense), and the 2025 pardons mark the regime shift in US crypto policy.

## Related

- [[perpetual-futures]] — the instrument BitMEX invented
- [[funding-rates]] — the mechanism anchoring perps to spot
- [[arthur-hayes]] — co-founder; now CIO of Maelstrom and macro essayist
- [[binance]] / [[bybit]] / [[okx]] — the venues that took its market share
- [[hyperliquid]] — the decentralized heir to the perp CLOB
- [[cftc]] — US regulator that brought the 2020 civil case
- [[leverage]] / [[liquidation]] — core mechanics popularized at 100x
- [[crypto-exchanges]] — venue landscape

## Sources

- DOJ (SDNY): "Global Cryptocurrency Exchange BitMEX Fined $100 Million for Violating Bank Secrecy Act" — https://www.justice.gov/usao-sdny/pr/global-cryptocurrency-exchange-bitmex-fined-100-million-violating-bank-secrecy-act
- CFTC press release 8412-21 ($100M consent order) — https://www.cftc.gov/PressRoom/PressReleases/8412-21
- CNBC, "Trump pardons three BitMEX crypto exchange co-founders, and ex-employee" (2025-03-28) — https://www.cnbc.com/2025/03/28/trump-pardon-bitmex-crypto-exchange-money-laundering.html
- CoinDesk, "President Trump Pardons Arthur Hayes, 3 Other BitMEX Co-Founders and Employee" (2025-03-28) — https://www.coindesk.com/policy/2025/03/28/president-trump-pardons-arthur-hayes-2-other-bitmex-co-founders-cnbc
- CoinGecko / Messari / BitDegree exchange trackers (volume and rank, accessed 2026-06) — https://www.coingecko.com/en/exchanges/bitmex_spot
- Verified via Perplexity (sonar) and web search, 2026-06-10
