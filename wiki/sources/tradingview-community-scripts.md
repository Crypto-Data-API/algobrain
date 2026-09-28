---
title: "TradingView Community Scripts"
type: source
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [crypto, technical-analysis, indicators, backtesting, open-source, strategy-development]
aliases: ["TradingView Community Scripts", "TradingView Public Library", "tradingview.com/scripts"]
source_type: data
source_url: "https://www.tradingview.com/scripts/"
source_author: "TradingView community (individual script authors credited by username)"
source_date: 2026-09-28
confidence: medium
claims_count: 18
related: ["[[tradingview-platform]]", "[[pine-script]]", "[[external-strategy-sources]]", "[[squeeze-momentum-indicator]]", "[[wavetrend-oscillator]]", "[[qqe]]", "[[ut-bot-alerts]]", "[[ssl-channel]]", "[[halftrend]]", "[[squeeze-momentum-breakout]]", "[[wavetrend-reversal]]"]
---

# TradingView Community Scripts

TradingView's **Community Scripts** library (`tradingview.com/scripts`) is the public catalogue of user-written [[pine-script|Pine Script]] indicators, strategies and libraries published on [[tradingview-platform|TradingView]]. It is the largest retail idea pool for [[technical-analysis]] indicators and one of the entries in [[external-strategy-sources]]. This summary records how the library is organised, the licence and publishing rules, and which widely used open-source scripts are relevant to crypto strategy research. It was compiled on 2026-09-28 from the TradingView scripts pages, the script-publishing rules and the Pine Script user manual; view and like counts drift daily and are quoted only as of that date.

## What This Source Is

- A browsable library of scripts under **Indicators > Community Scripts** on the chart, and at `tradingview.com/scripts` on the web. The web view offers **Popular**, **Editors' picks** and a vendor **Marketplace**, a type filter (indicators / strategies / libraries), an **Open-source only** checkbox, and "most recent" vs "most popular" sorting.
- Three visibility levels. **Open-source** scripts show their code. **Protected** scripts are public but the code is hidden from everyone except the author. **Invite-only** scripts need the author to grant access, and they are usually sold, which makes the author a "vendor" under TradingView rules.
- Open-source scripts are published under the **Mozilla Public License 2.0** by default unless the author states another licence in the code. TradingView's House Rules take precedence over the licence.

## Claims

### Library structure and rules

1. [HIGH] Open-source community scripts default to the Mozilla Public License 2.0; authors can declare a different licence in the source. (TradingView script publishing rules, retrieved 2026-09-28)
2. [HIGH] Reusing another author's open-source code in a new publication requires crediting the original author and making a meaningful improvement; renaming variables, changing inputs or styling, or converting between Pine versions does not count as an improvement. (Script publishing rules)
3. [HIGH] Reused open-source code must stay open-source unless the original author explicitly allows a closed-source republication. (Script publishing rules)
4. [HIGH] Protected scripts hide the code from every user except the author; offering access to invite-only scripts makes the publisher a vendor subject to extra vendor requirements. (TradingView vendor requirements / publishing rules)
5. [HIGH] The web library exposes Popular, Editors' picks and Marketplace views, plus an "Open-source only" filter and recent/popular sorting. (tradingview.com/scripts, retrieved 2026-09-28)

### Backtesting traps documented in the Pine manual

6. [HIGH] `request.security()` with `lookahead = barmerge.lookahead_on` and no one-bar offset leaks the future higher-timeframe close into historical bars, so the chart shows signals that could not have existed live ("repainting"). (Pine Script user manual, repainting page)
7. [HIGH] A strategy with `calc_on_every_tick = true` recalculates on every realtime tick but only on bar closes in history, so the live and historical behaviour differ. (Pine manual, strategies page)
8. [HIGH] Strategy defaults set commission and slippage to zero unless the author sets `commission_value` / `slippage` or the user changes them in the Properties tab. (Pine manual, strategies page)
9. [MEDIUM] Many popular published strategies report results with default commission, a large default capital and a short bar history, so the Strategy Tester headline overstates what a fee-paying crypto trader would get. (Observed across the Popular strategy list, 2026-09-28)

### Widely used open-source crypto-relevant scripts

10. [HIGH] *Squeeze Momentum Indicator [LazyBear]* was published by **LazyBear** on 2014-07-04. It is a derivative of John Carter's TTM Squeeze: Bollinger Bands inside Keltner Channels mark a squeeze, and a linear-regression momentum histogram shows direction. The page showed about 3.09M views on 2026-09-28. https://www.tradingview.com/script/nqQ1DT5a-Squeeze-Momentum-Indicator-LazyBear/
11. [HIGH] *Indicator: WaveTrend Oscillator [WT]* was published by **LazyBear** on 2014-05-27 as a port of a TradeStation/MetaTrader indicator. It signals when the oscillator crosses its signal line beyond overbought/oversold bands. About 1.4M views as of 2026-09-28. https://www.tradingview.com/script/2KE8wTuF-Indicator-WaveTrend-Oscillator-WT/
12. [HIGH] *UT Bot Alerts* was published by **QuantNomad** on 2020-02-08. The page credits **Yo_adriiiiaan** as the original developer and **HPotter** with the idea. It is an ATR trailing stop with a key-value multiplier and an optional Heikin-Ashi source. About 1.6M views as of 2026-09-28. https://www.tradingview.com/script/n8ss8BID-UT-Bot-Alerts/
13. [HIGH] *QQE MOD* was published by **Mihkel00** on 2020-01-20 and updated 2024-12-11. It runs two QQE calculations (RSI smoothed with ATR-of-RSI trailing bands), with Bollinger Bands on the primary line as a confirmation filter. https://www.tradingview.com/script/TpUW4muw-QQE-MOD/
14. [HIGH] *SSL channel* was published by **ErwinBeckers** on 2019-03-28. It uses moving averages of highs and lows whose lines swap when the close crosses either one. https://www.tradingview.com/script/xzIoaIJC-SSL-channel/ Mihkel00's *SSL Hybrid* is the widely used extension. https://www.tradingview.com/script/C3MlAWCw-SSL-Hybrid/
15. [HIGH] *HalfTrend* was published by **everget** on 2021-01-24. It is an ATR-based trend line that the author describes as "similar to the SuperTrend but uses a different trend's identification logic". The author also warns against paid repackagings of the same logic. https://www.tradingview.com/script/U1SJ8ubc-HalfTrend/
16. [HIGH] *Chandelier Exit [everget]* is **everget**'s open-source redesign of Le Beau's ATR trailing stop, and a common crypto trailing-stop overlay. https://www.tradingview.com/script/AqXxNS7j-Chandelier-Exit-everget/
17. [HIGH] *SuperTrend* by **KivancOzbilgic** is an open-source SuperTrend that lets the user pick RMA or SMA for the ATR. It has a companion strategy script. https://www.tradingview.com/script/r6dAP7yi/
18. [MEDIUM] Popular scripts spawn many derivative strategies, such as squeeze-momentum strategies, WaveTrend label variants and combos like "QQE MOD + SSL Hybrid + Waddah Attar Explosion". The derivatives rarely add costs or out-of-sample tests, so the popularity of a signal says nothing about its net-of-fees edge. (Search of tradingview.com/scripts, 2026-09-28)

## Entities, Concepts and Strategies Mentioned

- Platform and language: [[tradingview-platform]], [[pine-script]]
- Indicators with new pages: [[squeeze-momentum-indicator]], [[wavetrend-oscillator]], [[qqe]], [[ut-bot-alerts]], [[ssl-channel]], [[halftrend]]
- Indicators already on the wiki: [[supertrend]], [[chandelier-exit]], [[bollinger-bands]], [[keltner-channels]], [[atr]], [[rsi]], [[heikin-ashi]]
- Strategies: [[squeeze-momentum-breakout]], [[wavetrend-reversal]]
- Backtesting concepts: [[lookahead-bias]], [[overfitting]], [[transaction-costs]], [[backtesting-pitfalls]]

## Confidence Assessment

Overall **medium**. The facts about script metadata, authorship and licence rules are high confidence because they come from TradingView's own pages. The library itself is user-generated. Descriptions and performance claims on script pages are author marketing, carry no costs or out-of-sample validation, and should be treated as hypotheses. The wiki cites no author performance numbers from this source.

## Related

- [[external-strategy-sources]]: where this library sits among other idea sources
- [[tradingview-platform]]: the "Community Scripts as an Idea Source" section covers the vetting checklist
- [[pine-script]]: the language and its repainting traps
- [[cryptodataapi-backtesting]]: kline archive for re-testing ported scripts
