---
title: "Comprehensive Guide to Technical Trading Indicators"
type: source
created: 2026-04-20
updated: 2026-04-20
status: good
tags: [technical-analysis, indicators, history, source, meta]
source_type: article
source_url: ""
source_author: "Compiled research guide"
source_date: 2026-04-20
confidence: medium
claims_count: 60
---

# Comprehensive Guide to Technical Trading Indicators

Compiled research guide covering the history, mechanics, practitioners, and best-practice usage of 28+ technical trading indicators. Aggregated from 29 web sources including Investopedia, Wikipedia, Zerodha Varsity, and specialist trading blogs.

**Confidence**: MEDIUM — aggregated from web articles, Wikipedia, and blog posts; not peer-reviewed academic research.

## Claims

### Origins and Historical Timeline

1. [MEDIUM] **Munehisa Homma** developed candlestick charting in the 1700s at the Dojima Rice Exchange in Japan, embedding crowd psychology into price visualisation and producing patterns (doji, hammer, engulfing) still in use today
2. [MEDIUM] **Charles Dow** co-founded the Wall Street Journal and formalised Dow Theory in the 1880s–1890s, introducing the Dow Jones Industrial Average (1896) and the foundational concept that markets move in discernible, volume-confirmed trends
3. [MEDIUM] Early 20th-century pioneers: **William Peter Hamilton** and **Robert Rhea** (formalised Dow Theory), **Richard Schabacker** (head-and-shoulders, triangles), **Richard Wyckoff** (accumulation/distribution, composite operator theory)
4. [MEDIUM] **Jesse Livermore** popularised tape-reading and pivot trading in the 1920s
5. [MEDIUM] **John Magee** and **Robert Edwards** codified technical analysis in *Technical Analysis of Stock Trends* (1948), still a foundational text
6. [MEDIUM] The modern indicator era arrived with mass computing in the 1970s–1980s, driven primarily by J. Welles Wilder Jr., Gerald Appel, John Bollinger, Goichi Hosoda (retrospectively), Richard Donchian, Tushar Chande, and Donald Lambert

### Indicator Category Taxonomy

7. [MEDIUM] Indicators broadly fall into five categories: **Trend**, **Momentum**, **Volatility**, **Volume**, and **Breadth/Sentiment**

### RSI Profile

8. [MEDIUM] RSI introduced by J. Welles Wilder Jr. in *New Concepts in Technical Trading Systems* (1978); bounded momentum oscillator (0–100), typically 14-period lookback, 70/30 overbought/oversold thresholds
9. [MEDIUM] Wilder was a mechanical engineer turned real estate developer who authored a compact toolkit — RSI, ATR, ADX/DMI, Parabolic SAR, Swing Index, and CSI — that became the core of almost every charting platform
10. [MEDIUM] RSI common strategies include classic 70/30 mean reversion, bullish/bearish divergences, RSI-2 pullback systems popularised by Larry Connors, and "hidden divergences" for trend continuation
11. [LOW] One practitioner-focused study reports RSI(14) among the highest historical win-rate indicators at 79.4% in its sample

### MACD Profile

12. [MEDIUM] Gerald Appel developed MACD in the late 1970s; it subtracts a 26-period EMA from a 12-period EMA, with a 9-period EMA signal line and histogram
13. [LOW] MACD reported win rate of 40.1% in one backtesting summary

### Bollinger Bands Profile

14. [MEDIUM] John Bollinger, founder of Bollinger Capital Management, created Bollinger Bands in the 1980s after entering finance via managing his mother's pension
15. [MEDIUM] Bands plot a 20-period SMA with upper/lower envelopes at ±2 standard deviations, adapting to realised volatility
16. [MEDIUM] Strategies include squeezes, walking-the-band trend rides, and %b/BandWidth oscillators — codified in *Bollinger on Bollinger Bands* (2001), translated into eight languages
17. [LOW] Bollinger Bands reported win rate of 77.8% in one backtesting summary

### Ichimoku Profile

18. [MEDIUM] Developed in secret by Goichi Hosoda (pen name "Ichimoku Sanjin") starting in the late 1930s and published in a 7-volume series beginning 1969
19. [MEDIUM] "Ichimoku Kinko Hyo" translates as "one-glance equilibrium chart" — five components: Tenkan-sen, Kijun-sen, Chikou Span, Senkou Span A and B (cloud/Kumo)
20. [MEDIUM] Paired with Time Theory, Wave Theory, and Price (Target) Theory; long dominant in Japanese equities and FX, spread globally only in the 1990s due to translation lag
21. [LOW] Ichimoku reported win rate of 42.3% in one backtesting summary

### Donchian Channels and Turtle Traders Profile

22. [MEDIUM] Richard Donchian, often called the "father of trend following," created channels plotting the N-period high and low in the 1950s–1960s
23. [MEDIUM] Richard Dennis and Bill Eckhardt used a Donchian-based system to train 23 novice "Turtles," funding them with $200K–$2M each
24. [MEDIUM] Turtle System 1 entered 20-day breakouts (skipping after wins); System 2 used 55-day breakouts
25. [LOW] Turtles reportedly produced ~$150–175M in profits over four to five years, averaging roughly 80% per year
26. [MEDIUM] Turtle position sizing governed by Wilder's ATR to normalise risk across 1N volatility units, with effective gross leverage commonly 4×–10× capital
27. [LOW] Donchian Channels reported win rate of 74.1% in one backtesting summary

### Elliott Wave Profile

28. [MEDIUM] Ralph Nelson Elliott (1871–1948), American accountant, developed wave theory during an illness-forced retirement in the 1930s; published *The Wave Principle* (1938) and *Nature's Laws: The Secret of the Universe* (1946)
29. [MEDIUM] Theory posits markets move in 5-wave impulses and 3-wave corrections at all fractal degrees, driven by crowd psychology
30. [MEDIUM] Robert Prechter popularised the method via *Elliott Wave Theorist*, famously calling the 1980s bull market

### VWAP Profile

31. [MEDIUM] Volume-Weighted Average Price emerged from institutional trading desks in the 1980s–1990s as an execution benchmark; brokers judged on whether fills beat VWAP
32. [MEDIUM] Calculated as the running sum of (price × volume) divided by cumulative volume — gives the "true" average fill price
33. [MEDIUM] Institutions slice large orders to track VWAP and minimise market impact; now the dominant intraday benchmark in equities, futures, and increasingly crypto

### Wilder's Toolkit Profile (ATR, ADX, Parabolic SAR)

34. [MEDIUM] ATR (Average True Range) designed for commodities, measures volatility as a moving average of true range; universally used for stop-loss sizing, position sizing, and the Turtle "N" unit
35. [MEDIUM] ADX/DMI quantifies trend strength on a 0–100 scale, with +DI/−DI indicating direction; readings above 25 typically signal a tradable trend
36. [MEDIUM] Parabolic SAR is a trailing stop/reversal dot system that accelerates as trends extend — popular for exit logic
37. [LOW] ADX reported win rate of 53.6%, Parabolic SAR 44.7% in one backtesting summary

### Stochastic Oscillator and Williams %R Profile

38. [MEDIUM] George Lane popularised the Stochastic Oscillator (%K, %D) in the 1950s–1970s to compare closing price to recent range, flagging momentum exhaustion
39. [MEDIUM] Larry Williams won the 1987 Robbins World Cup of Futures Trading with a reported 11,376% return; created Williams %R, a mirror-image momentum oscillator (1973)
40. [LOW] Stochastics reported win rate of 44.9%, Williams %R 71.7% in one backtesting summary

### CCI, Aroon, and Chande Profile

41. [MEDIUM] Donald Lambert introduced the Commodity Channel Index in *Commodities* magazine (1980) to identify cyclical turns, originally for commodities but now used broadly
42. [MEDIUM] Tushar Chande developed Aroon (1995) — Sanskrit for "dawn's early light" — measuring time since the most recent N-period high/low to detect emerging trends
43. [MEDIUM] Chande also created the Chande Momentum Oscillator and QStick
44. [LOW] CCI(20) reported win rate of 35.1% in one backtesting summary

### Markets and Asset Class Applicability

45. [MEDIUM] US/Global equities most use: moving averages, RSI, MACD, Bollinger Bands, VWAP, OBV; breadth indicators (McClellan, TRIN) for index traders
46. [MEDIUM] Futures/commodities most use: ATR, ADX, Donchian, Parabolic SAR, CCI, Ichimoku; Wilder's suite designed for commodities
47. [MEDIUM] Forex most uses: Ichimoku, Fibonacci, MACD, Bollinger, Pivot Points; Ichimoku entrenched among Japanese FX desks
48. [MEDIUM] Crypto most uses: RSI, MACD, Bollinger, VWAP, Ichimoku, Supertrend; 24/7 markets amplify volatility-based indicators

### Notable Practitioners

49. [MEDIUM] Jesse Livermore's 1929 short positions reportedly netted ~$100M (billions in today's terms)
50. [MEDIUM] Paul Tudor Jones used Elliott Wave and classic patterns to call and short the 1987 crash, earning ~200% that year
51. [MEDIUM] Ed Seykota reportedly compounded client accounts by ~250,000% over 16 years as a pioneer of computerised trend-following

### Leverage Usage

52. [MEDIUM] Futures intrinsic leverage ~10–25× via margin; Turtle-style systems used ATR-normalised sizing for effective gross leverage 4×–10×
53. [MEDIUM] Forex retail leverage ranges from 30:1 (EU/UK/AU under ASIC/ESMA) to 500:1+ (offshore)
54. [MEDIUM] US equities Reg-T margin allows 2:1 intraday, 4:1 day-trading; swing traders typically run 1–2×
55. [MEDIUM] Crypto perp-futures venues offer 20–125× leverage
56. [MEDIUM] Options embedded leverage (delta × notional/premium) can exceed 50× without margin calls
57. [MEDIUM] Wilder emphasised that ATR-based position sizing — not raw leverage — is what separates durable systems from blow-ups

### Best-Practice Combinations

58. [MEDIUM] Professional traders typically layer 2–4 complementary indicators across different categories: (1) Trend + Momentum + Volatility + Volume: 50/200 EMA + RSI + Bollinger + OBV; (2) Turtle-style: Donchian 20/55 + ATR sizing + ADX filter; (3) Ichimoku standalone; (4) Bollinger + RSI mean-reversion; (5) VWAP + MACD intraday

### Limitations and Academic Perspective

59. [MEDIUM] Comparative studies find that technical indicators' predictive power in commodity markets is mixed relative to fundamental factors, and most edges decay as more participants adopt them
60. [MEDIUM] No indicator is predictive in isolation — they are conditional tools whose value depends on regime, timeframe, and risk management

## Win-Rate Snapshot (Illustrative)

One backtesting summary across US equities (source: newtrading.io) reported the following win rates. **Caveat**: win-rate alone is misleading — high-win-rate mean-reversion systems often have poor payoff ratios, while lower-win-rate trend systems generate most P&L from a few large winners.

| Indicator | Reported Win Rate |
|---|---|
| RSI(14) | 79.4% |
| Bollinger Bands | 77.8% |
| Donchian Channels | 74.1% |
| Williams %R | 71.7% |
| ADX | 53.6% |
| Stochastics | 44.9% |
| Parabolic SAR | 44.7% |
| Ichimoku | 42.3% |
| MACD | 40.1% |
| CCI(20) | 35.1% |
| EMA(50) | 30.7% |

## Pages Created or Updated

### Created
- [[ichimoku]], [[donchian-channels]], [[williams-percent-r]], [[aroon]], [[chaikin-money-flow]], [[money-flow-index]], [[mcclellan-oscillator]], [[arms-index]], [[point-and-figure]]
- [[j-welles-wilder]], [[gerald-appel]], [[john-bollinger]], [[goichi-hosoda]], [[george-lane]], [[larry-williams]], [[donald-lambert]], [[tushar-chande]], [[ralph-nelson-elliott]], [[robert-prechter]], [[bill-eckhardt]], [[munehisa-homma]], [[marc-chaikin]], [[joseph-granville]], [[richard-arms]], [[chester-keltner]], [[sherman-mcclellan]]

### Updated
- [[rsi]], [[macd]], [[bollinger-bands]], [[stochastic]], [[vwap]], [[adx]], [[atr]], [[cci]], [[obv]], [[dow-theory]], [[market-breadth]], [[candlestick-patterns]], [[indicators-overview]]
- [[ichimoku-cloud]], [[parabolic-sar]], [[elliott-wave]], [[turtle-trading]], [[donchian-channel-breakout]], [[turtle-traders]]
- [[richard-donchian]], [[paul-tudor-jones]]

## References

1. [7 Technical Indicators To Build a Trading Tool Kit](https://www.investopedia.com/top-7-technical-analysis-tools-4773275)
2. [Technical Indicators List: 26 Key Indicators Every Trader Must Know](https://piprider.com/technical-indicators-list/)
3. [Timeline of technical analysis](https://timelines.issarice.com/wiki/Timeline_of_technical_analysis)
4. [Who Created Technical Analysis as We Know It?](https://tttmarkets.com/2025/07/26/who-created-technical-analysis-as-we-know-it/)
5. [The Origins of Technical Indicators on Wall Street](https://homebusinessmag.com/money/stocks/origins-technical-indicators-wall-street/)
6. [Indicators part 2: MACD, bollinger bands & trading signals - Zerodha](https://zerodha.com/varsity/chapter/indicators-part-2/)
7. [Technical Indicators List - DiscoverCI](https://www.discoverci.com/stock-charts/technical-indicators-list)
8. [J. Welles Wilder Jr. - Wikipedia](https://en.wikipedia.org/wiki/J._Welles_Wilder_Jr.)
9. [Elliott wave principle - Wikipedia](https://en.wikipedia.org/wiki/Elliott_wave_principle)
10. [Ralph Nelson Elliott: Complete Biography & Wave Theory Guide](https://elliottwavestreet.com/elliott-wave/ralph-nelson-elliott-the-mastermind-behind-the-elliott-wave-theory/)
11. [Elliott Wave Theory: Definition, History, and How it Works](https://www.strike.money/stock-market/elliott-wave-theory)
12. [Brief history and concept of Ichimoku Kinko Hyo](https://ridingwaves.substack.com/p/2-brief-history-and-concept-of-ichimoku)
13. [Ichimoku Kinko Hyo - Wikipedia](https://en.wikipedia.org/wiki/Ichimoku_Kink%C5%8D_Hy%C5%8D)
14. [Ichimoku Indicator Signals - Swissquote](https://www.swissquote.com/en-ch/private/inspire/blog/technical-analysis/what-ichimoku-kinko-hyo-trading-method)
15. [Donchian Channel Strategy - The Turtle System](https://www.lizardindicators.com/donchian-channel-strategy/)
16. [Ruthless Test of Turtle Trading Donchian Channel Breakouts](https://www.youtube.com/watch?v=TpA4LAEzFb4)
17. [Turtle Trading Complete Guide - Alchemy Markets](https://alchemymarkets.com/education/strategies/turtle-trading-guide/)
18. [The 10 most popular trading indicators - Saxo](https://www.home.saxo/learn/guides/trading-strategies/a-guide-to-the-10-most-popular-trading-indicators)
19. [J. Welles Wilder Jr. and His Trading Legacy - EBC](https://www.ebc.com/forex/j-welles-wilder-jr)
20. [What Is ATR and Why Use It in Trading - Macroption](https://www.macroption.com/atr-explained/)
21. [How John Bollinger invented the Bollinger Bands](https://www.best-trading-platforms.com/trading-platform-futures-forex-cfd-stocks-nanotrader/how-john-bollinger-invented-bollinger-bands-and)
22. [Understanding Bollinger Bands - Investopedia](https://www.investopedia.com/terms/b/bollingerbands.asp)
23. [14 Most Used TradingView Indicators - Trade Nation](https://tradenation.com/articles/tradingview-indicators/)
24. [Best Trading Indicators - Axi](https://www.axi.com/int/blog/education/trading-indicators)
25. [Which Technical Indicators Are Best - NewTrading](https://www.newtrading.io/best-technical-indicators/)
26. [VWAP Trading Strategy Explained - Capital.com](https://capital.com/en-au/learn/technical-analysis/volume-weighted-average-price-vwap-indicator)
27. [VWAP Indicator - Gate.com](https://www.gate.com/learn/articles/vwap-indicator-powering-intraday-trading-with-the-volume-weighted-average-price/8185)
28. [Volume-Weighted Average Price - Britannica](https://www.britannica.com/money/volume-weighted-average-price)
29. [A Comparative Study of Bollinger Bands, RSI and MACD Against Fundamental Factors](https://jmsr-online.com/article/technical-analysis-vs-fundamental-analysis-a-comparative-study-of-bollinger-bands-rsi-and-macd-against-fundamental-factors-in-commodity-trading-82/)

## Sources

