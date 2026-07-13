---
title: "Composer"
type: entity
created: 2026-04-22
updated: 2026-06-21
status: excellent
tags: [algorithmic, backtesting, company]
aliases: ["Composer Trade", "Composer.trade"]
entity_type: company
founded: 2020
headquarters: "New York, USA"
website: "https://www.composer.trade"
related:
  - "[[quantconnect]]"
  - "[[alpaca]]"
  - "[[tradingview-platform]]"
  - "[[freqtrade]]"
  - "[[backtesting-overview]]"
  - "[[trading-platforms]]"
  - "[[traderspost]]"
---

**Composer** is a no-code algorithmic trading platform that allows users to build, backtest, and deploy automated trading strategies without programming. Founded in 2020, it targets retail traders and investors who want systematic, rules-based investing but lack coding skills. Originally limited to US equities and ETFs executed through [[alpaca|Alpaca's]] brokerage infrastructure, the platform has since expanded to crypto and options, added an AI strategy builder ("Trade with AI", October 2025), and reports over $200 million in daily trading volume as of 2026. For traders, Composer matters as the most accessible on-ramp to systematic, rules-based execution — and as a case study in how quickly retail algo platforms are absorbing LLM-driven strategy generation.

## At a Glance

| Attribute | Detail |
|-----------|--------|
| Category | No-code [[algorithmic-trading|algorithmic]] / robo-investing platform |
| Founded | 2020, New York |
| Builder model | Drag-and-drop decision trees (if/then logic blocks) |
| AI feature | "Trade with AI" — plain-English → backtested strategy (launched Oct 2025) |
| Assets | US equities, ETFs, crypto, options (no futures or non-US markets, as of June 2026) |
| Execution broker | [[alpaca]] (brokerage API) |
| Min rebalance frequency | Daily (no intraday) |
| Reported volume | $200M+/day (2025–2026) |
| Pricing | Crypto free tier (0.2%/trade); Stocks+IRA $40/mo; Business custom |
| Best for | Rules-based ETF/portfolio investors who do not code |
| Not for | Intraday, HFT, custom indicators, ML, or rigorous cost-modeled backtesting |

## How It Works

### Visual Strategy Builder

Composer uses a drag-and-drop interface where strategies are built using if/then logic blocks:

1. **Define a condition**: e.g., "If SPY's 50-day moving average is above its 200-day moving average"
2. **Specify an action**: e.g., "Allocate 60% to QQQ, 40% to TLT"
3. **Add an else branch**: e.g., "Otherwise, allocate 100% to SHY (short-term Treasuries)"
4. **Set rebalancing frequency**: daily, weekly, or monthly

Strategies are composed as decision trees, making the logic transparent and auditable. There is no hidden black box -- every decision point is visible.

### Supported Assets

- US equities (individual stocks)
- ETFs (the primary building block for most Composer strategies)
- **Cryptocurrency** (added by 2025; automated crypto strategies run on a free, commission-per-trade tier)
- **Options** (added by late 2025; 2026 reviews describe the platform trading "across stocks, crypto, and options")
- No support for futures or international markets (as of June 2026)

Earlier versions of the platform (through ~2024) were equities/ETFs only; the crypto and options expansions materially widened the strategy universe.

### Execution

- Trades execute via [[alpaca|Alpaca's]] brokerage API
- Automatic rebalancing according to the strategy's defined schedule
- Fractional shares supported, allowing precise allocation percentages
- Commission-free trading on US equities and ETFs

## Backtesting

Composer includes built-in backtesting that runs strategies against historical data:

- **Metrics displayed**: Total return, CAGR, [[sharpe-ratio|Sharpe ratio]], [[maximum-drawdown|max drawdown]], [[volatility]]
- **Benchmark comparison**: Strategies are automatically compared against buy-and-hold SPY
- **Date range selection**: Test across different market regimes
- **Limitations**: Uses daily close data only (no intraday), does not model [[slippage]] or market impact, historical data limited to available ETF/stock history

### Backtesting Caveats

Like all retail backtesting tools, Composer's backtester has inherent limitations:

- **[[survivorship-bias]]**: Only currently listed assets are available; delisted ETFs/stocks are excluded
- **No transaction cost modeling**: Commission-free does not mean cost-free (spread costs, market impact)
- **[[overfitting-in-trading|Overfitting]] risk**: Easy to keep tweaking conditions until a strategy looks good historically
- **Limited lookback**: ETFs like QQQ and TLT have sufficient history, but newer thematic ETFs may have only a few years of data

See [[backtesting-pitfalls]] for a comprehensive guide to what can go wrong.

## Strategy Templates

Composer offers a library of community-shared and curated strategies:

- **Momentum/trend-following**: Rotate into assets with strongest recent performance; move to bonds/cash when trends break
- **[[mean-reversion]]**: Buy dips in broad indices, sell rallies
- **Risk parity-inspired**: Allocate inversely to [[volatility]] across asset classes
- **Seasonal**: Adjust allocations based on calendar effects (e.g., "Sell in May")
- **Macro regime**: Use indicators like yield curve slope, [[vix]], or moving averages to switch between risk-on and risk-off

Users can clone and modify any shared strategy, enabling a "remix culture" for algo trading.

### Example Strategy Walkthrough (Golden-Cross Risk Switch)

A canonical beginner Composer "symphony" expressed as a decision tree:

```
IF SPY 50-day SMA > SPY 200-day SMA      (risk-on regime)
    THEN allocate: 60% QQQ, 40% TLT
ELSE                                      (risk-off regime)
    THEN allocate: 100% SHY               (short-term Treasuries)
REBALANCE: weekly
```

| Step | What happens |
|------|--------------|
| Signal check | On each rebalance, Composer evaluates the 50/200-day moving-average condition on SPY |
| Branch | Picks the risk-on or risk-off allocation based on the condition |
| Rebalance | Trades via [[alpaca]] to bring holdings to target weights (fractional shares) |
| Backtest | Runs the same logic over historical daily closes vs buy-and-hold SPY |

The logic is fully visible — there is no hidden model. The same example also exposes the platform's limits: it cannot react intraday, it ignores [[slippage]] and spread cost in the backtest, and it is trivially easy to keep adjusting the moving-average lengths until the historical curve looks good ([[overfitting-in-trading|overfitting]]).

## Trading Relevance

### Strengths

- **No coding required**: Accessible to traders who understand strategy logic but cannot program
- **Transparent logic**: Every decision is visible; no hidden model complexity
- **Rapid prototyping**: Test a strategy idea in minutes, not days
- **Automated execution**: Set and forget; no need to manually rebalance
- **Community strategies**: Learn from others' approaches
- **Free backtesting**: Test ideas before committing capital

### Limitations

- **No futures or international markets**: the universe is US stocks, ETFs, crypto, and options (futures and non-US markets remain unsupported as of June 2026; before 2025 the platform was equities/ETFs only)
- **Daily rebalancing minimum**: Cannot implement intraday strategies
- **Simple logic only**: No machine learning, no complex math, no custom indicators beyond standard moving averages and momentum
- **No API access**: Cannot integrate with external data sources or custom signals
- **Backtest quality**: No cost modeling, no [[look-ahead-bias]] protection beyond basic safeguards
- **US markets only**: No international diversification

### Who It Is For

Composer is best suited for:

- Investors who want rules-based portfolio management without coding
- Traders testing simple momentum or trend-following ideas on ETFs
- Users who want automated rebalancing without paying advisory fees
- Beginners learning about systematic trading concepts

It is **not** suited for:

- Traders needing intraday execution or options/futures
- Quants requiring custom indicators, alternative data, or ML models
- High-frequency or latency-sensitive strategies
- Anyone needing robust backtest methodology with proper cost modeling

## Competitors

| Platform | Approach | Key Difference |
|----------|----------|----------------|
| [[quantconnect]] | Code-based (Python/C#) | Full programming flexibility, institutional-grade backtesting |
| [[freqtrade]] | Open-source Python bot | Crypto-focused, fully customizable, self-hosted |
| [[tradingview-platform\|TradingView]] | [[pine-script\|Pine Script]] signals | Superior charting, requires some coding for automation |
| [[alpaca]] (direct API) | Code-based | Same broker backend, but requires programming |
| [[traderspost]] | Webhook-based automation | Connects signals to brokers, more flexible trigger sources |
| Wealthfront/Betterment | Robo-advisor | Simpler, less customizable, but professionally managed |

### Which Tool When?

| If you need... | Pick | Over Composer because... |
|----------------|------|--------------------------|
| Full code control + institutional backtesting | [[quantconnect]] | Python/C#, point-in-time data, tick resolution |
| Self-hosted crypto bot, fully customizable | [[freqtrade]] | Open-source, your own infra and data |
| Superior charting + signal scripting | [[tradingview-platform]] ([[pine-script]]) | Best-in-class charts; webhook-out for automation |
| Webhook routing from any signal source | [[traderspost]] | Flexible triggers → broker execution |
| Hands-off professional management | Robo-advisor | No strategy work at all |
| No-code rules + automated rebalancing | **Composer** | Easiest on-ramp; transparent decision trees |

## 2025-2026 Developments

- **"Trade with AI" launch (October 2025)**: Composer added an AI strategy builder that turns plain-English prompts (or single clicks) into fully executable, backtested strategies in under 60 seconds. The feature is built on a proprietary strategy language that LLMs can write directly, with sub-second backtesting before deployment.
- **Volume milestone**: Composer reports surpassing **$200 million in daily trading volume** (2025-2026).
- **Asset-class expansion**: crypto trading (free tier, 0.2% commission per trade) and options trading were added, moving Composer beyond its original equities/ETF-only universe.
- The platform now positions itself as a vertically integrated trading ecosystem (strategy creation, backtesting, and execution in one product) rather than purely a visual strategy builder.

## Pricing

As of 2026:

- **Crypto**: free tier -- no monthly subscription; **0.2% commission per trade**; automated crypto strategies, unlimited backtesting, strategy analytics
- **Stocks and IRA**: **$40/month** (14-day free trial) -- fully automated stock strategies; Roth, Traditional, and Rollover IRA support; unlimited backtesting and portfolio metrics; no-code strategy builder
- **Business accounts**: custom pricing with API access and full IP ownership of strategies
- No per-trade commissions on equities/ETFs (execution historically via the Alpaca relationship)

## Related

- [[quantconnect]] -- Code-based alternative with deeper backtesting
- [[alpaca]] -- Brokerage backend powering Composer's execution
- [[backtesting-overview]] -- Methodology for testing strategies against historical data
- [[backtesting-pitfalls]] -- Common mistakes in strategy backtesting
- [[freqtrade]] -- Open-source alternative for crypto bot trading
- [[tradingview-platform]] -- Charting platform with signal generation
- [[traderspost]] -- Webhook-based trade automation
- [[trading-platforms]] -- Overview of available trading platforms
- [[ai-trading]] -- broader AI-in-trading context for the "Trade with AI" feature

## Sources

- Composer official site -- https://www.composer.trade (product, crypto, and AI pages)
- Traders Magazine, "Composer Introduces 'Trade With AI' to Enhance Investment Platform" (October 2025) -- https://www.tradersmagazine.com/xtra/composer-introduces-trade-with-ai-to-enhance-investment-platform/
- Yahoo Finance, "Composer Supercharges Investing Platform with New 'Trade With AI' Tool" -- https://finance.yahoo.com/news/composer-supercharges-investing-platform-trade-120000006.html
- OpenTools AI, "Composer Trade Reviews, Alternatives, and Pricing" (May 2026) -- https://opentools.ai/tools/composer-trade
- Pricing, asset classes, and volume figures verified via web search, 2026-06-10.
