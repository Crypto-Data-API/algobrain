# The Comprehensive Compendium of Technical Trading Indicators

Technical indicators are mathematical transformations of price, volume, and (sometimes) open-interest data designed to help traders interpret market behaviour, identify trends, gauge momentum, measure volatility, and time entries and exits. This compendium collates the history, inventors, mechanics, strategies, markets, notable practitioners, and leverage practices associated with the most widely used indicators across equities, futures, forex, and crypto.[^1][^2]

## 1. Origins and Historical Timeline

Technical analysis traces back to 18th-century Japan, where rice merchant **Munehisa Homma** developed candlestick charting in the Dojima Rice Exchange, embedding crowd psychology into price visualisation and producing patterns (doji, hammer, engulfing) still in use today. In the West, **Charles Dow** co-founded the Wall Street Journal and formalised Dow Theory in the 1880s–1890s, introducing the Dow Jones Industrial Average (1896) and the foundational concept that markets move in discernible, volume-confirmed trends.[^3][^4][^5]

Early 20th-century pioneers — **William Peter Hamilton**, **Robert Rhea**, **Richard Schabacker** (head-and-shoulders, triangles), and **Richard Wyckoff** (accumulation/distribution, composite operator theory) — systematised chart reading. **Jesse Livermore** popularised tape-reading and pivot trading in the 1920s. **John Magee** and **Robert Edwards** codified it all in *Technical Analysis of Stock Trends* (1948), still a foundational text.[^4][^5]

The modern indicator era arrived with mass computing in the 1970s–1980s, driven primarily by **J. Welles Wilder Jr.**, **Gerald Appel**, **John Bollinger**, **Goichi Hosoda** (retrospectively), **Richard Donchian**, **Tushar Chande**, and **Donald Lambert**.[^6][^7][^8][^4]

## 2. Master Table of Technical Indicators

Indicators broadly fall into five categories: **Trend**, **Momentum**, **Volatility**, **Volume**, and **Breadth/Sentiment**. The table below collates the most important indicators with inventor, year, category, and typical use.[^2]

| Indicator | Inventor | Year / Era | Category | Primary Use |
|---|---|---|---|---|
| Candlestick charts | Munehisa Homma | 1700s | Price pattern | Crowd psychology, reversals[^3][^4] |
| Dow Theory | Charles Dow | 1880s–1890s | Trend framework | Primary/secondary trends[^3][^4] |
| Elliott Wave | Ralph Nelson Elliott | 1930s (pub. 1938) | Pattern/cycle | 5-wave impulse + 3-wave correction[^9][^10][^11] |
| Ichimoku Kinko Hyo | Goichi Hosoda | 1930s (pub. 1969) | Trend/all-in-one | One-glance equilibrium chart[^12][^13][^14] |
| Point & Figure | De Villiers / Wheelan | 1930s–1940s | Price filter | Noise removal, breakouts[^4] |
| Donchian Channels | Richard Donchian | 1950s–1960s | Volatility/breakout | Turtle trend-following[^15][^16][^17] |
| Moving Averages (SMA/EMA) | Various | Mid-20th c. | Trend | Smoothing, crossovers[^1][^2] |
| MACD | Gerald Appel | Late 1970s | Momentum | Line/signal crossovers, divergence[^18][^6] |
| RSI | J. Welles Wilder Jr. | 1978 | Momentum | Overbought/oversold (70/30)[^19][^8][^20] |
| ATR | J. Welles Wilder Jr. | 1978 | Volatility | Stop sizing, position sizing[^19][^8][^20] |
| ADX / DMI | J. Welles Wilder Jr. | 1978 | Trend strength | Trend vs. range filter[^19][^8] |
| Parabolic SAR | J. Welles Wilder Jr. | 1978 | Trend/exit | Trailing stops[^19][^8] |
| Swing Index / CSI | J. Welles Wilder Jr. | 1978 | Momentum | Futures selection[^19][^8] |
| Bollinger Bands | John Bollinger | Early 1980s | Volatility | Mean reversion, squeezes[^21][^6][^22] |
| Stochastic Oscillator | George Lane | 1950s–1970s | Momentum | %K/%D overbought/oversold[^2][^23] |
| Williams %R | Larry Williams | 1973 | Momentum | Short-term reversals[^2][^24] |
| CCI | Donald Lambert | 1980 | Momentum | Commodity cyclical extremes[^25][^2] |
| Aroon | Tushar Chande | 1995 | Trend | Trend emergence, time-to-price[^7] |
| Chaikin Money Flow | Marc Chaikin | 1980s | Volume | Institutional flow[^2] |
| OBV | Joseph Granville | 1963 | Volume | Accumulation/distribution[^1][^2] |
| VWAP | Institutional desks | 1980s–1990s | Volume/price | Execution benchmark[^26][^27][^28] |
| Money Flow Index | Quong & Soudack | 1989 | Volume momentum | Volume-weighted RSI[^2] |
| Keltner Channel | Chester Keltner | 1960 | Volatility | ATR-based envelope[^2] |
| Fibonacci Retracement | Derived from Fibonacci | 20th c. adoption | Price levels | Support/resistance[^18][^24] |
| McClellan Oscillator | Sherman McClellan | 1969 | Breadth | NYSE adv/dec breadth[^2] |
| Arms Index (TRIN) | Richard Arms | 1967 | Breadth | Market internals[^2] |

## 3. Deep Profiles of the Core Indicators

### 3.1 Relative Strength Index (RSI)
Introduced by **J. Welles Wilder Jr.** in *New Concepts in Technical Trading Systems* (1978), the RSI is a bounded momentum oscillator (0–100) typically calculated on a 14-period lookback, with 70/30 as default overbought/oversold thresholds. Wilder was a mechanical engineer turned real estate developer who authored a compact toolkit — RSI, ATR, ADX/DMI, Parabolic SAR, Swing Index, and CSI — that became the core of almost every charting platform. RSI is used across equities, futures, forex, and crypto; common strategies include classic 70/30 mean reversion, bullish/bearish divergences, RSI-2 pullback systems popularised by Larry Connors, and "hidden divergences" for trend continuation. One practitioner-focused study reports RSI(14) among the highest historical win-rate indicators in its sample.[^25][^19][^8][^20][^1]

### 3.2 MACD
**Gerald Appel** developed the Moving Average Convergence/Divergence oscillator in the late 1970s. It subtracts a 26-period EMA from a 12-period EMA, with a 9-period EMA signal line and histogram. Traders watch MACD/signal crossovers, zero-line crosses, and divergences against price. It is used universally across stocks, FX, and crypto, and remains a staple in TradingView's built-in toolkit.[^18][^23][^6]

### 3.3 Bollinger Bands
**John Bollinger**, founder of Bollinger Capital Management, created Bollinger Bands in the 1980s after entering finance via managing his mother's pension. The bands plot a 20-period SMA with upper/lower envelopes at ±2 standard deviations, adapting to realised volatility. Strategies include squeezes (volatility compression preceding breakouts), walking-the-band trend rides, and %b/BandWidth oscillators — all of which Bollinger codified in *Bollinger on Bollinger Bands* (2001), translated into eight languages.[^21][^22][^6]

### 3.4 Ichimoku Kinko Hyo
Developed in secret by **Goichi Hosoda** (pen name "Ichimoku Sanjin") starting in the late 1930s and published in a 7-volume series beginning 1969, Ichimoku translates as "one-glance equilibrium chart". Its five components — Tenkan-sen, Kijun-sen, Chikou Span, Senkou Span A and B (which form the "cloud/Kumo") — combine trend, momentum, support/resistance, and time projection in a single visual. It is paired with Time Theory, Wave Theory, and Price (Target) Theory. Long dominant in Japanese equities and FX, it spread globally only in the 1990s due to translation lag.[^12][^13][^14]

### 3.5 Donchian Channels and the Turtle Traders
**Richard Donchian**, often called the father of trend following, created channels plotting the N-period high and low. In the early 1980s, commodities trader **Richard Dennis** and **Bill Eckhardt** used a Donchian-based system to train 23 novice "Turtles," funding them with $200K–$2M each to test whether traders are born or made. Turtle System 1 entered 20-day breakouts (skipping after wins); System 2 used 55-day breakouts. The Turtles reportedly produced ~$150–175M in profits over four to five years, averaging roughly 80% per year — one of the most famous trading experiments in history. Position sizing was governed by Wilder's ATR to normalise risk across 1N volatility units, with leverage naturally compounded across a diversified futures portfolio.[^19][^15][^16][^17]

### 3.6 Elliott Wave Principle
**Ralph Nelson Elliott** (1871–1948), an American accountant, developed the theory during an illness-forced retirement in the 1930s and published *The Wave Principle* (1938) and *Nature's Laws: The Secret of the Universe* (1946). The theory posits that markets move in 5-wave impulses and 3-wave corrections at all fractal degrees, driven by crowd psychology. **Robert Prechter** later popularised the method via *Elliott Wave Theorist*, famously calling the 1980s bull market.[^9][^10][^11]

### 3.7 VWAP
Volume-Weighted Average Price emerged from institutional trading desks in the 1980s–1990s as an execution benchmark: brokers were judged on whether their fills beat VWAP. Calculated as the running sum of (price × volume) divided by cumulative volume, it gives the "true" average fill price. Institutions slice large orders to track VWAP and minimise market impact; day traders use it as an intraday mean-reversion and trend bias line. It is now the dominant intraday benchmark in equities, futures, and increasingly crypto.[^26][^27][^28]

### 3.8 Wilder's Volatility & Trend Toolkit (ATR, ADX, Parabolic SAR)
- **ATR (Average True Range)**: Designed for commodities, measures volatility as a moving average of true range; universally used for stop-loss sizing, position sizing, and the Turtle "N" unit.[^20][^17][^19]
- **ADX/DMI**: Quantifies trend strength on a 0–100 scale, with +DI/−DI indicating direction; readings above 25 typically signal a tradable trend.[^8][^19]
- **Parabolic SAR**: A trailing stop/reversal dot system that accelerates as trends extend — popular for exit logic.[^19][^8]

### 3.9 Stochastic Oscillator & Williams %R
**George Lane** popularised the Stochastic Oscillator (%K, %D) in the 1950s–1970s to compare closing price to recent range, flagging momentum exhaustion. **Larry Williams** — a legendary futures trader who won the 1987 Robbins World Cup of Futures Trading with a reported 11,376% return — created Williams %R, a mirror-image momentum oscillator.[^23][^24][^2]

### 3.10 CCI, Aroon, and Chande's Contributions
**Donald Lambert** introduced the Commodity Channel Index in *Commodities* magazine (1980) to identify cyclical turns, originally for commodities but now used broadly. **Tushar Chande** developed Aroon (1995) — Sanskrit for "dawn's early light" — measuring time since the most recent N-period high/low to detect emerging trends; Chande also created the Chande Momentum Oscillator and QStick.[^7][^25][^2]

## 4. Markets and Asset Class Applicability

| Market | Most-used Indicators | Notes |
|---|---|---|
| US/Global equities | Moving averages, RSI, MACD, Bollinger Bands, VWAP, OBV | VWAP dominant intraday; breadth (McClellan, TRIN) for index traders[^2][^27][^28] |
| Futures/commodities | ATR, ADX, Donchian, Parabolic SAR, CCI, Ichimoku | Wilder's suite designed for commodities; Turtle system[^19][^20][^17] |
| Forex | Ichimoku, Fibonacci, MACD, Bollinger, Pivot Points | Ichimoku entrenched among Japanese FX desks[^12][^13][^14] |
| Crypto | RSI, MACD, Bollinger, VWAP, Ichimoku, Supertrend | 24/7 markets amplify volatility-based indicators[^23] |

## 5. Notable Practitioners and Success Stories

- **Jesse Livermore**: Tape-reader whose 1929 short positions reportedly netted ~$100M (billions in today's terms); inspiration for indicator-era traders.[^5]
- **Richard Dennis & the Turtles**: ~$150–175M profits, 80%/yr average returns via Donchian/ATR system.[^15][^16][^17]
- **Paul Tudor Jones**: Used Elliott Wave and classic patterns to call and short the 1987 crash, earning ~200% that year.[^9]
- **Larry Williams**: 11,376% return in 1987 Robbins World Cup using momentum and %R methods.[^2]
- **John Bollinger**: Built an asset-management career and global publishing franchise on his bands.[^21]
- **Ed Seykota**: Pioneer of computerised trend-following using moving-average and breakout systems; reportedly compounded client accounts by ~250,000% over 16 years.[^4]

## 6. Leverage Usage Across Indicator-Driven Strategies

Leverage is structurally embedded in indicator-driven trading, but levels vary sharply by venue:[^17][^15][^19]

- **Futures (CME, ICE)**: Intrinsic leverage of ~10–25× via margin; Turtle-style systems used ATR-normalised sizing so each "unit" risked a fixed fraction (~1%) of equity per 1N of ATR, then stacked up to 4 units per market and diversified across 20+ markets — effective gross leverage commonly 4×–10× capital.[^15][^17][^19]
- **Forex**: Retail leverage ranges from 30:1 (EU/UK/AU under ASIC/ESMA) to 500:1+ (offshore brokers); Ichimoku, Fibonacci, and MACD strategies are often deployed with 10–50× effective leverage.[^23][^12]
- **Equities**: Reg-T margin allows 2:1 intraday 4:1 day-trading leverage in the US; swing traders applying RSI/MACD/Bollinger typically run 1–2×.[^1][^2]
- **Crypto**: Perp-futures venues offer 20–125× leverage; VWAP/RSI/Bollinger/Supertrend combinations are the most common toolkits, though funding rates and liquidation cascades dominate risk.[^23]
- **Options**: Indicator signals are frequently expressed via options, where embedded leverage (delta × notional/premium) can exceed 50× without margin calls — favoured by Bollinger squeeze and IV-regime traders.[^22][^21]

A reliable rule across all venues: leverage magnifies the signal-to-noise limitations of the underlying indicator; Wilder himself emphasised that ATR-based position sizing — not raw leverage — is what separates durable systems from blow-ups.[^20][^19]

## 7. Indicator Win-Rate Snapshot (Illustrative)

One backtesting summary across US equities ranked the following indicators by reported win rate, underscoring that mean-reversion oscillators and volatility envelopes tend to outperform pure trend oscillators in range-bound regimes:[^25]

| Indicator | Reported Win Rate |
|---|---|
| RSI(14) | 79.4%[^25] |
| Bollinger Bands | 77.8%[^25] |
| Donchian Channels | 74.1%[^25] |
| Williams %R | 71.7%[^25] |
| ADX | 53.6%[^25] |
| Stochastics | 44.9%[^25] |
| Parabolic SAR | 44.7%[^25] |
| Ichimoku | 42.3%[^25] |
| MACD | 40.1%[^25] |
| CCI(20) | 35.1%[^25] |
| EMA(50) | 30.7%[^25] |

Win-rate alone is misleading — high-win-rate mean-reversion systems often have poor payoff ratios, while lower-win-rate trend systems like Donchian/ADX generate most of their P&L from a few large winners, as the Turtle record demonstrates.[^17][^15]

## 8. Best-Practice Combinations

Professional traders typically layer two to four complementary indicators across different categories rather than relying on one:[^1][^2]

- **Trend + Momentum + Volatility + Volume**: e.g., 50/200 EMA + RSI + Bollinger Bands + OBV.[^2][^1]
- **Turtle-style breakout stack**: Donchian 20/55 + ATR sizing + ADX filter.[^19][^15][^17]
- **Ichimoku standalone**: Already bundles trend, momentum, S/R, and time.[^13][^12]
- **Bollinger + RSI**: Classic mean-reversion pair for range markets.[^6][^22][^21]
- **VWAP + MACD**: Intraday institutional bias + momentum confirmation.[^27][^6]

## 9. Limitations and Academic Perspective

Comparative studies find that while technical indicators (especially RSI, MACD, Bollinger) can identify short-term opportunities, their predictive power in commodity markets is mixed relative to fundamental factors, and most edges decay as more participants adopt them. No indicator is predictive in isolation — they are conditional tools whose value depends on regime, timeframe, and risk management. The enduring lesson from every pioneer — Homma, Dow, Wilder, Bollinger, Dennis — is that indicators serve discipline and position sizing, not prophecy.[^29][^5][^4][^1][^19]

---

## References

1. [7 Technical Indicators To Build a Trading Tool Kit](https://www.investopedia.com/top-7-technical-analysis-tools-4773275) - Traders use technical indicators to gain insight into the supply and demand of securities. Here, we ...

2. [Technical Indicators List: 26 Key Indicators Every Trader Must Know](https://piprider.com/technical-indicators-list/) - Access the full technical indicators list of 26 essentials like RSI, MACD & Bollinger Bands. Refine ...

3. [Timeline of technical analysis](https://timelines.issarice.com/wiki/Timeline_of_technical_analysis)

4. [Who Created Technical Analysis as We Know It?](https://tttmarkets.com/2025/07/26/who-created-technical-analysis-as-we-know-it/) - Who Created Technical Analysis as We Know It?

5. [The Origins of Technical Indicators on Wall Street | HBM](https://homebusinessmag.com/money/stocks/origins-technical-indicators-wall-street/) - The Origins of Technical Indicators on Wall Street

6. [Indicators part 2: MACD, bollinger bands & trading signals - Zerodha](https://zerodha.com/varsity/chapter/indicators-part-2/) - In the late seventies, Gerald Appel developed the Moving Average Convergence and Divergence (MACD) i...

7. [Technical Indicators List](https://www.discoverci.com/stock-charts/technical-indicators-list) - DiscoverCI’s technical indicators list provides a detailed breakdown of all the indicators available...

8. [J. Welles Wilder Jr. - Wikipedia](https://en.wikipedia.org/wiki/J._Welles_Wilder_Jr.) - John Welles Wilder Jr. (June 11, 1935 – April 18, 2021) was an American mechanical engineer, turned ...

9. [Elliott wave principle - Wikipedia](https://en.wikipedia.org/wiki/Elliott_wave_principle) - Ralph Nelson Elliott (1871–1948), an American accountant, developed a model for the underlying socia...

10. [Ralph Nelson Elliott: Complete Biography & Wave Theory Guide](https://elliottwavestreet.com/elliott-wave/ralph-nelson-elliott-the-mastermind-behind-the-elliott-wave-theory/) - Elliott's theory posits that market prices unfold in a series of waves reflecting market participant...

11. [Elliott Wave Theory: Definition, History, and How it Works](https://www.strike.money/stock-market/elliott-wave-theory) - Ralph Nelson Elliott invented it in the early twentieth century. According to the hypothesis, stock ...

12. [#2 - Brief history and concept of Ichimoku Kinko Hyo - Riding Waves](https://ridingwaves.substack.com/p/2-brief-history-and-concept-of-ichimoku) - The creator of Ichimoku was Goichi Hosoda, a japanese citizen that worked as a journalist. His work ...

13. [Ichimoku Kinkō Hyō - Wikipedia](https://en.wikipedia.org/wiki/Ichimoku_Kink%C5%8D_Hy%C5%8D) - It was developed in the late 1930s by Goichi Hosoda (細田悟一, Hosoda Goichi), a Japanese journalist who...

14. [Ichimoku Indicator Signals](https://www.swissquote.com/en-ch/private/inspire/blog/technical-analysis/what-ichimoku-kinko-hyo-trading-method) - Ichimoku Kinkyo Hyo is a renowned Japanese trading strategy developed by journalist Goichi Hosoda, w...

15. [Donchian Channel Strategy - The Turtle System - Lizard Indicators](https://www.lizardindicators.com/donchian-channel-strategy/) - The story about the Turtle Traders originated from a discussion between famous commodities trader Ri...

16. [Ruthless Test of Turtle Trading Donchian Channel Breakouts](https://www.youtube.com/watch?v=TpA4LAEzFb4) - In this video, we explore Donchian Channels used in the Turtle Trading Strategy, a profitable tradin...

17. [Turtle Trading Complete Guide - Alchemy Markets](https://alchemymarkets.com/education/strategies/turtle-trading-guide/) - Donchian Channels are most commonly associated with breakout trading, made especially famous by the ...

18. [The 10 most popular trading indicators and how to use them | Saxo](https://www.home.saxo/learn/guides/trading-strategies/a-guide-to-the-10-most-popular-trading-indicators) - An overview of 10 widely used trading indicators and how they are applied in technical analysis.

19. [J. Welles Wilder Jr. and His Trading Legacy | EBC Financial Group](https://www.ebc.com/forex/j-welles-wilder-jr) - His indicators cover momentum (RSI), volatility (ATR), trend strength (ADX/DMI) and trailing exit lo...

20. [What Is ATR and Why Use It in Trading - Macroption](https://www.macroption.com/atr-explained/) - Average True Range (ATR) is a technical indicator first introduced by J. Welles Wilder Jr. in his 19...

21. [How John Bollinger invented the Bollinger Bands and more](https://www.best-trading-platforms.com/trading-platform-futures-forex-cfd-stocks-nanotrader/how-john-bollinger-invented-bollinger-bands-and) - John Bollinger is president and founder of the asset management firm Bollinger Capital Management. A...

22. [Understanding Bollinger Bands: A Key Technical Analysis Tool for ...](https://www.investopedia.com/terms/b/bollingerbands.asp) - Bollinger Bands are a technical analysis tool developed by John Bollinger in the 1980s to help inves...

23. [14 Most Used TradingView Indicators - Trade Nation](https://tradenation.com/articles/tradingview-indicators/) - Explore the 14 most used TradingView indicators and discover how they can assist you with your overa...

24. [Best Trading Indicators: Most Popular Technical Indicators / Axi](https://www.axi.com/int/blog/education/trading-indicators) - Discover the best technical indicators and find out which are the most effective for traders. Click ...

25. [Which Technical Indicators Are...](https://www.newtrading.io/best-technical-indicators/) - See our rankings of the highest-performing, most reliable, and most popular technical indicators of ...

26. [VWAP Trading Strategy Explained | Capital.com Australia](https://capital.com/en-au/learn/technical-analysis/volume-weighted-average-price-vwap-indicator) - Volume weighted average price (VWAP) is a trading indicator that shows the true average price of a s...

27. [Powering Intraday Trading with the Volume-Weighted Average Price](https://www.gate.com/learn/articles/vwap-indicator-powering-intraday-trading-with-the-volume-weighted-average-price/8185) - VWAP Indicator is a technical analysis indicator that represents the average price a security has tr...

28. [Volume-Weighted Average Price (VWAP) Meaning & Trading](https://www.britannica.com/money/volume-weighted-average-price) - Volume-weighted average price (VWAP) serves as a vital reference point for both institutional and re...

29. [A Comparative Study of Bollinger Bands, RSI and MACD Against ...](https://jmsr-online.com/article/technical-analysis-vs-fundamental-analysis-a-comparative-study-of-bollinger-bands-rsi-and-macd-against-fundamental-factors-in-commodity-trading-82/) - This study aims to compare the effectiveness of Technical Analysis indicators—Bollinger Bands, RSI, ...

