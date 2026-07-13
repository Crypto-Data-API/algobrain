---
title: "TradersPost"
type: entity
created: 2026-04-22
updated: 2026-06-21
status: excellent
tags: [algorithmic, company]
aliases: ["Traders Post"]
entity_type: company
headquarters: "USA"
website: "https://traderspost.io"
related:
  - "[[tradingview-platform]]"
  - "[[thinkorswim]]"
  - "[[interactive-brokers]]"
  - "[[alpaca]]"
  - "[[freqtrade]]"
  - "[[pine-script]]"
  - "[[trading-bots-overview]]"
  - "[[composer-trade]]"
---

**TradersPost** is a webhook-based trade automation platform that connects trading signals from charting and analysis tools (primarily [[tradingview-platform|TradingView]]) to brokerage accounts for automatic execution. It bridges the gap between signal generation and order execution without requiring users to write code or build custom infrastructure. As of June 2026 the platform advertises **17+ broker/exchange connections, 40,000+ traders, $200M+ in connected accounts, and 20M+ trades executed** — making it the de facto standard for retail TradingView-alert automation.

## At a Glance

| Attribute | Detail |
|-----------|--------|
| Category | Webhook → broker execution bridge (see [[trading-bots-overview]]) |
| Primary signal source | [[tradingview-platform\|TradingView]] alerts ([[pine-script\|Pine Script]]) |
| Code required | No (point-and-click webhook setup) |
| What it does | Translates a signal payload into a broker order |
| What it does **not** do | Make trading decisions — all intelligence lives in the signal source |
| Brokers/exchanges | 17+ (stocks, options, futures, crypto) |
| Typical latency | 1-5 seconds (not suitable for [[high-frequency-trading\|HFT]]) |
| Closest competitor | [[composer-trade\|Composer]] (all-in-one), Autoview (similar webhook model) |
| Verified | June 2026 (official site, pricing page, docs) |

## How It Works

The core workflow is straightforward:

1. **Generate a signal**: Create an alert in [[tradingview-platform|TradingView]] (or any platform that supports webhooks) based on a technical indicator, [[pine-script|Pine Script]] strategy, or custom condition
2. **Send to TradersPost**: The alert fires a webhook to TradersPost's API endpoint
3. **Execute the trade**: TradersPost translates the webhook payload into a brokerage order and submits it to the connected broker
4. **Confirm and log**: The execution is logged with fill details, timestamps, and any errors

### Webhook Format

TradersPost accepts JSON payloads via webhook, typically structured as:

```json
{
  "ticker": "AAPL",
  "action": "buy",
  "orderType": "market",
  "quantity": 10
}
```

More advanced payloads can specify limit prices, stop losses, take profits, position sizing rules, and options contract details.

Common webhook fields (representative; consult the official docs for the authoritative schema):

| Field | Purpose |
|-------|---------|
| `ticker` | Symbol to trade (e.g. `AAPL`) |
| `action` | `buy` / `sell` / `exit` / `cancel` |
| `orderType` | `market` / `limit` / `stop` |
| `quantity` | Share/contract count (or omit for sizing rules) |
| `limitPrice` / `stopPrice` | Price for non-market orders |
| `takeProfit` / `stopLoss` | Bracket exits attached to the entry |
| `price` | The signal price (used for slippage/audit comparison) |
| `sentiment` / `position` | Some templates use these to flatten then reverse |

> **Caveat.** Because the payload is just JSON over HTTP, a malformed or duplicated alert is executed faithfully — the platform does not second-guess the signal. This is the root of the "runaway order" risk noted below; validate every template in [[#Risk Considerations|paper mode]] first.

## Supported Brokers

As of June 2026, TradersPost advertises 17+ broker and exchange connections:

- **Traditional brokers**: [[alpaca]] (stocks, commission-free), [[interactive-brokers]] (stocks, options, futures, forex), TradeStation, Tradier, E*TRADE, Robinhood, Webull, [[tastytrade-platform|tastytrade]], [[ninjatrader|NinjaTrader]], Charles Schwab / [[thinkorswim]] (legacy TD Ameritrade integration)
- **Futures**: Tradovate, ProjectX
- **Crypto exchanges**: Coinbase, [[binance]], [[kraken]], [[bybit]], Crypto.com
- **Paper trading**: built-in TradersPost paper account

The broker list continues to expand. Each integration supports the asset classes available through that broker.

## Supported Asset Classes

- **Stocks**: All US equities
- **Options**: Single-leg options orders (calls and puts), with support for multi-leg strategies expanding
- **Futures**: Via brokers that support futures trading
- **Crypto**: Via Coinbase integration

## Signal Sources

While [[tradingview-platform|TradingView]] is the most common signal source, TradersPost accepts webhooks from any platform:

- **[[tradingview-platform|TradingView]]**: The primary integration; alerts from [[pine-script|Pine Script]] strategies and indicators
- **TrendSpider**: officially supported signal source alongside TradingView
- **Custom scripts**: Any Python, Node.js, or other script that can send HTTP POST requests (JSON payload templates provided)
- **[[thinkorswim]]**: Via thinkScript alerts converted to webhooks (requires middleware)
- **Spreadsheets**: Google Sheets with Apps Script can send webhooks
- **Other platforms**: Any tool with webhook/API capability

## Trading Relevance

### Use Cases

1. **Automating TradingView strategies**: The most common use case. A trader develops a strategy in [[pine-script|Pine Script]], validates it via TradingView's backtester, then connects it to TradersPost for live execution.

2. **Multi-broker execution**: Send the same signal to multiple broker accounts simultaneously for diversified execution.

3. **Options automation**: Automate simple options strategies -- e.g., buy calls when RSI crosses above 30 on a watchlist of stocks.

4. **Paper trading validation**: Connect to a paper trading account first to validate that signals translate correctly to orders before going live.

5. **Hybrid discretionary/systematic**: Use TradersPost for the systematic component of a portfolio while managing discretionary trades manually.

### Typical Setup Workflow

| Step | Action | Where |
|------|--------|-------|
| 1 | Build/validate a strategy | [[tradingview-platform\|TradingView]] + [[pine-script\|Pine Script]] backtester |
| 2 | Connect a broker (start with **paper**) | TradersPost broker integrations |
| 3 | Create a TradersPost "strategy" and copy its webhook URL | TradersPost dashboard |
| 4 | Paste the URL + JSON message into a TradingView alert | TradingView alert dialog |
| 5 | Fire test alerts; confirm orders land correctly | TradersPost execution log |
| 6 | Switch the connection from paper to **live** | TradersPost dashboard |

A working pipeline can be built in under an hour; the discipline that matters is steps 3 and 5 — validating the payload in paper mode before flipping to live capital.

### Advantages

- **No coding required**: The webhook integration is point-and-click for TradingView users
- **Fast setup**: A working automation pipeline can be built in under an hour
- **Broker-agnostic**: Same signals can route to different brokers
- **Position management**: Built-in logic for position sizing, max position limits, and risk controls
- **Audit trail**: Complete log of every signal received, order sent, and fill received
- **Paper trading mode**: Test the full pipeline without risking capital

### Limitations

- **Latency**: Webhook-based execution adds latency (typically 1-5 seconds) compared to direct API integration. Not suitable for [[high-frequency-trading|HFT]] or scalping
- **Dependency on signal source**: If TradingView's servers lag or an alert fails to fire, the trade does not execute
- **Limited strategy logic**: TradersPost executes orders; it does not make trading decisions. All intelligence must live in the signal source
- **No portfolio-level risk management**: Risk controls are per-strategy, not across the entire portfolio
- **Webhook reliability**: Internet connectivity issues, webhook failures, or broker API outages can cause missed trades
- **Cost**: Subscription fees on top of brokerage costs

### Risk Considerations

Automated execution introduces specific risks that manual traders do not face:

- **Runaway orders**: A misconfigured webhook could fire repeatedly, creating unintended positions
- **Fill quality**: Market orders in low-liquidity names can result in significant [[slippage]]
- **Signal-execution gap**: The price at which the signal was generated may differ from the fill price
- **Broker API limits**: Rate limits on broker APIs can delay or block orders during high-volume periods

See [[bot-risks-and-pitfalls]] for a broader discussion of automated trading risks.

## Competitors

| Platform | Approach | Key Difference |
|----------|----------|----------------|
| [[composer-trade\|Composer]] | No-code visual builder | All-in-one (strategy + backtest + execution), but limited to equities/ETFs |
| [[freqtrade]] | Open-source Python bot | Fully customizable, self-hosted, crypto-focused |
| [[alpaca]] (direct API) | Code-based | More control, but requires programming |
| [[three-commas\|3Commas]] | Crypto trading bots | Crypto-specific, exchange integrations |
| Autoview | TradingView webhook execution | Similar concept, less broker support |
| Alert-to-broker scripts | Custom-built | Full control, but requires development and maintenance |

## Pricing

Published pricing as of June 2026 (billed yearly; monthly billing is higher):

| Plan | Price (billed yearly) | Live accounts | Paper accounts | Asset classes |
|------|----------------------|---------------|----------------|---------------|
| Free | $0 (7-day trial of paid features) | manual submit only | automated | -- |
| Starter | $41.65/mo | 1 | 4 | 1 |
| Basic | $84.15/mo | 2 | 6 | 2 |
| Pro | $169.15/mo | 3 | 8 | 3 |
| Premium | $254.15/mo | 6 | 10 | all |

- All paid tiers include unlimited tickers and trades; add-on accounts cost $10/mo (live) or $5/mo (paper), up to 50
- No markup on brokerage commissions

## Related

- [[tradingview-platform]] -- Primary signal source for TradersPost automations
- [[pine-script]] -- Scripting language used to create TradingView alerts
- [[thinkorswim]] -- Alternative platform that can be connected as a broker
- [[interactive-brokers]] -- Supported broker with broad asset class coverage
- [[alpaca]] -- Commission-free broker integration
- [[bot-risks-and-pitfalls]] -- Risks of automated trade execution
- [[freqtrade]] -- Open-source alternative for crypto automation
- [[composer-trade]] -- No-code alternative with built-in strategy builder
- [[trading-bots-overview]] -- Overview of automated trading systems

## Sources

- TradersPost official site -- https://traderspost.io (broker list, trader/volume figures: 17+ brokers, 40,000+ traders, $200M+ connected accounts, 20M+ trades; verified June 2026)
- TradersPost pricing page -- https://traderspost.io/pricing (tier pricing verified 2026-06-10)
- TradersPost documentation -- https://docs.traderspost.io (webhook payload format)
