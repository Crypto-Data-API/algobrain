---
title: "Arbitrage Monitoring Setup"
type: reference
created: 2026-04-21
updated: 2026-06-20
status: excellent
tags: [arbitrage, execution, risk-management, strategy-development, algorithmic]
aliases: ["Arb Monitoring Code", "Arb Alert Bot", "Trading Bot Monitoring"]
strategy_type: algorithmic
timeframe: scalp|intraday|swing|position
markets: [crypto, futures, options]
complexity: advanced
backtest_status: untested
related: ["[[strategy-monitoring]]", "[[arbitrage-parameter-cheatsheet]]", "[[exchange-api-reference]]", "[[multi-venue-capital-management]]", "[[leg-risk]]", "[[crowding-indicators]]", "[[arbitrage-live-performance]]"]
---

# Arbitrage Monitoring Setup

[[strategy-monitoring]] defines *what* to monitor and *when* to alert. This page provides **runnable code templates** and configuration for building an actual monitoring stack. Copy, configure, deploy.

## Architecture Overview

```
Exchange APIs (WebSocket/REST)
        ↓
  Python Monitor Service
        ↓
   ┌────┴────┐
   │         │
Telegram   Grafana
  Alerts   Dashboard
   │         │
   └────┬────┘
     You
```

**Stack:** Python 3.10+ with `ccxt`, `python-telegram-bot`, `aiohttp`. Optional: InfluxDB + Grafana for dashboards.

**Dependencies:**
```bash
pip install ccxt python-telegram-bot aiohttp pandas
```

### Monitoring Stack by Layer

A complete arb-monitoring stack has four layers. The code in this page covers all four; the table maps each layer to its purpose, tooling, and the script that implements it:

| Layer | Purpose | Tooling | Script in this page |
|---|---|---|---|
| **Ingest** | Pull prices, funding, positions from venues | `ccxt`, exchange WebSocket/REST | `funding_monitor.py`, `spread_scanner.py` |
| **Evaluate** | Compare against thresholds; detect signal / breach | Python logic + [[arbitrage-parameter-cheatsheet]] | `evaluate_rates()`, `scan_spreads()` |
| **Alert** | Push CRITICAL/WARNING/INFO to a human | `python-telegram-bot` | `arb_alerts.py` |
| **Persist / visualize** | Store time series, dashboards, historical review | InfluxDB + Grafana | `influx_writer.py`, Grafana config |

The non-negotiable rule for the whole stack: **monitoring keys are read-only.** A monitoring service that holds trading-enabled API keys is a single point of catastrophic failure. See the [[#Deployment Checklist]].

### Cadence, Threshold, and Latency Reference

Different signals demand different polling cadences. Polling too slowly misses fleeting opportunities; polling too fast burns rate limits and adds no value for slow-moving carry. Recommended starting points (calibrate to your fee tier and strategy via [[arbitrage-parameter-cheatsheet]]):

| Monitor | Cadence | Why this cadence | Latency sensitivity |
|---|---|---|---|
| Cross-exchange spread scanner | 1-5 s | [[cross-exchange-arbitrage]] gaps last seconds | Very high — stale quotes = phantom arbs |
| Funding-rate monitor | Hourly (settles 1-3×/day) | Funding changes slowly relative to settlement | Low |
| Position reconciliation | 5 min (active) / daily (carry) | Catch [[leg-risk]] drift before it compounds | Medium |
| Exchange health / latency | 60 s | Detect API degradation before stranded legs | High — feeds the kill switch |
| Daily P&L report | 00:00 UTC | End-of-day attribution | None |
| Crowding indicators | Daily | [[crowding-indicators]] move on AUM/OI timescales | None |

**Latency budget for fast arb:** for [[cross-exchange-arbitrage]] and [[triangular-arbitrage]], the round trip *detect → decide → place both legs → confirm* must beat the opportunity's half-life (often 1-15 s). Co-located or VPS-near-exchange deployment, persistent WebSocket feeds (not REST polling), and pre-positioned capital on both venues are prerequisites — a REST-polling loop on a home connection will lose every contested fill. For slow carry ([[funding-rate-arbitrage]], [[cash-and-carry]]) latency is largely irrelevant; reliability and uptime dominate.

### What to Monitor by Strategy Type

| Strategy | Primary signal | Critical alert (exit/pause) | Reconciliation focus |
|---|---|---|---|
| [[funding-rate-arbitrage]] | 8h funding rate, basis | Funding inversion (longs pay shorts) | Spot vs perp leg parity |
| [[cross-exchange-arbitrage]] | Best-bid/best-ask spread across venues | Spread compression below cost | Inventory drift across venues |
| [[cash-and-carry]] / [[basis-trading]] | Spot-futures basis vs financing cost | Basis collapse / negative carry | Futures roll, margin headroom |
| merger-arbitrage | Deal spread, regulatory headlines | Deal-break risk repricing | Long-target / short-acquirer ratio |
| [[flash-loan-arbitrage]] / [[mev-strategies]] | On-chain pool prices, gas, mempool | Builder-bid erodes profit to ≤0 | Atomic — no leg risk, but revert risk |
| [[statistical-arbitrage]] / [[pairs-trading]] | Z-score / spread vs cointegration band | Cointegration breakdown | Dollar-neutrality, factor drift |

---

## 1. Telegram Alert Bot

### Setup

1. Message `@BotFather` on Telegram, create a bot, get the API token
2. Send a message to your bot, then get your chat ID via `https://api.telegram.org/bot<TOKEN>/getUpdates`

### Core Alert Module

```python
"""arb_alerts.py — Telegram alert bot for arbitrage monitoring"""
import asyncio
from datetime import datetime
from telegram import Bot

# Configuration
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
bot = Bot(token=TELEGRAM_TOKEN)

async def send_alert(level: str, strategy: str, message: str):
    """Send alert to Telegram. Levels: CRITICAL, WARNING, INFO"""
    emoji = {"CRITICAL": "🔴", "WARNING": "🟡", "INFO": "🔵"}
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    text = f"{emoji.get(level, '⚪')} [{level}] {strategy}\n{message}\n{timestamp}"
    await bot.send_message(chat_id=CHAT_ID, text=text)

# Example usage
# asyncio.run(send_alert("CRITICAL", "Funding Arb", "Funding rate inverted on Binance BTC"))
```

---

## 2. Funding Rate Monitor

Monitors funding rates across exchanges and alerts when they cross thresholds from [[arbitrage-parameter-cheatsheet]].

```python
"""funding_monitor.py — Multi-exchange funding rate monitor"""
import ccxt
import asyncio
from arb_alerts import send_alert

# Thresholds (from arbitrage-parameter-cheatsheet)
MIN_VIABLE_RATE_8H = 0.0001    # 0.01% per 8h (~11% APY) — minimum profitable
ATTRACTIVE_RATE_8H = 0.0003    # 0.03% per 8h (~33% APY) — strong signal
INVERSION_THRESHOLD = -0.0001  # Negative = longs pay shorts = EXIT
EXIT_TRAILING_24H = 0.00005   # Trailing 24h avg below this = close

EXCHANGES = {
    "binance": ccxt.binance({"options": {"defaultType": "swap"}}),
    "okx": ccxt.okx({"options": {"defaultType": "swap"}}),
    "bybit": ccxt.bybit({"options": {"defaultType": "swap"}}),
}

SYMBOLS = ["BTC/USDT:USDT", "ETH/USDT:USDT", "SOL/USDT:USDT"]

async def check_funding_rates():
    results = {}
    for name, exchange in EXCHANGES.items():
        try:
            rates = {}
            for symbol in SYMBOLS:
                ticker = exchange.fetch_ticker(symbol)
                funding_rate = ticker.get("info", {}).get("lastFundingRate")
                if funding_rate:
                    rates[symbol] = float(funding_rate)
            results[name] = rates
        except Exception as e:
            await send_alert("WARNING", "Funding Monitor",
                           f"{name} API error: {str(e)[:100]}")
    return results

async def evaluate_rates(rates: dict):
    for exchange, symbols in rates.items():
        for symbol, rate in symbols.items():
            asset = symbol.split("/")[0]

            # CRITICAL: Funding inverted
            if rate < INVERSION_THRESHOLD:
                await send_alert("CRITICAL", "Funding Arb",
                    f"INVERSION on {exchange} {asset}: {rate:.6f} per 8h "
                    f"({rate * 3 * 365 * 100:.1f}% APY). EXIT position.")

            # WARNING: Below minimum viable
            elif rate < MIN_VIABLE_RATE_8H:
                await send_alert("WARNING", "Funding Arb",
                    f"Low rate on {exchange} {asset}: {rate:.6f} per 8h "
                    f"({rate * 3 * 365 * 100:.1f}% APY). Below minimum viable.")

            # INFO: Attractive rate
            elif rate > ATTRACTIVE_RATE_8H:
                await send_alert("INFO", "Funding Arb",
                    f"High rate on {exchange} {asset}: {rate:.6f} per 8h "
                    f"({rate * 3 * 365 * 100:.1f}% APY). Entry signal.")

async def main():
    while True:
        rates = await check_funding_rates()
        await evaluate_rates(rates)
        await asyncio.sleep(3600)  # Check hourly

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 3. Position Reconciliation Script

Verifies that actual positions match expected positions across venues. Run every 5 minutes for active arb, daily for carry strategies.

```python
"""reconciliation.py — Cross-exchange position reconciliation"""
import ccxt
from arb_alerts import send_alert
import asyncio

# Expected positions (update these from your order management system)
EXPECTED_POSITIONS = {
    "binance": {"BTC": {"spot": 2.5, "perp": -2.5}},   # Funding arb: long spot, short perp
    "hyperliquid": {"ETH": {"perp": -10.0}},            # Short perp leg
}

IMBALANCE_THRESHOLD = 0.03  # 3% — alert if legs diverge more than this

def fetch_positions(exchange_name: str, exchange: ccxt.Exchange) -> dict:
    """Fetch actual positions from exchange"""
    positions = {}
    try:
        # Spot balances
        balance = exchange.fetch_balance()
        for asset in ["BTC", "ETH", "SOL", "USDT", "USDC"]:
            if balance.get(asset, {}).get("total", 0) > 0:
                positions.setdefault(asset, {})["spot"] = balance[asset]["total"]

        # Perp positions
        if exchange.has.get("fetchPositions"):
            perp_positions = exchange.fetch_positions()
            for pos in perp_positions:
                if abs(pos["contracts"]) > 0:
                    asset = pos["symbol"].split("/")[0]
                    side = pos["contracts"] if pos["side"] == "long" else -pos["contracts"]
                    positions.setdefault(asset, {})["perp"] = side
    except Exception as e:
        asyncio.run(send_alert("CRITICAL", "Reconciliation",
                              f"{exchange_name} fetch failed: {str(e)[:100]}"))
    return positions

async def reconcile():
    exchanges = {
        "binance": ccxt.binance({"apiKey": "...", "secret": "..."}),
        # Add other exchanges
    }

    for name, exchange in exchanges.items():
        actual = fetch_positions(name, exchange)
        expected = EXPECTED_POSITIONS.get(name, {})

        for asset, expected_legs in expected.items():
            for leg_type, expected_qty in expected_legs.items():
                actual_qty = actual.get(asset, {}).get(leg_type, 0)
                if expected_qty != 0:
                    diff_pct = abs(actual_qty - expected_qty) / abs(expected_qty)
                else:
                    diff_pct = abs(actual_qty)

                if diff_pct > IMBALANCE_THRESHOLD:
                    await send_alert("CRITICAL", "Reconciliation",
                        f"POSITION MISMATCH on {name}\n"
                        f"{asset} {leg_type}: expected {expected_qty:.4f}, "
                        f"actual {actual_qty:.4f} (diff {diff_pct:.1%})")

        # Check net exposure (should be ~0 for market-neutral strategies)
        for asset in expected:
            spot = actual.get(asset, {}).get("spot", 0)
            perp = actual.get(asset, {}).get("perp", 0)
            net = spot + perp
            if abs(net) > 0.01 * max(abs(spot), abs(perp), 1):
                await send_alert("WARNING", "Reconciliation",
                    f"NET EXPOSURE on {name} {asset}: {net:.4f} "
                    f"(spot={spot:.4f}, perp={perp:.4f})")
```

---

## 4. Exchange Health Monitor

Detects API degradation, latency spikes, and connectivity issues before they cause stranded legs.

```python
"""exchange_health.py — Exchange API health monitor"""
import ccxt
import time
import asyncio
from arb_alerts import send_alert

EXCHANGES = {
    "binance": ccxt.binance(),
    "coinbase": ccxt.coinbase(),
    "okx": ccxt.okx(),
    "bybit": ccxt.bybit(),
}

LATENCY_WARN_MS = 500     # Alert if response > 500ms
LATENCY_CRITICAL_MS = 2000 # Alert if response > 2000ms
CONSECUTIVE_FAILURES = 3   # Alert after 3 consecutive failures

failure_counts = {name: 0 for name in EXCHANGES}
latency_history = {name: [] for name in EXCHANGES}

async def check_health():
    for name, exchange in EXCHANGES.items():
        start = time.time()
        try:
            exchange.fetch_ticker("BTC/USDT")
            latency_ms = (time.time() - start) * 1000
            failure_counts[name] = 0
            latency_history[name].append(latency_ms)
            latency_history[name] = latency_history[name][-60:]  # Keep last 60

            if latency_ms > LATENCY_CRITICAL_MS:
                await send_alert("CRITICAL", "Exchange Health",
                    f"{name} latency: {latency_ms:.0f}ms (threshold: {LATENCY_CRITICAL_MS}ms)")
            elif latency_ms > LATENCY_WARN_MS:
                avg = sum(latency_history[name]) / len(latency_history[name])
                await send_alert("WARNING", "Exchange Health",
                    f"{name} latency elevated: {latency_ms:.0f}ms (avg: {avg:.0f}ms)")

        except Exception as e:
            failure_counts[name] += 1
            if failure_counts[name] >= CONSECUTIVE_FAILURES:
                await send_alert("CRITICAL", "Exchange Health",
                    f"{name} DOWN — {failure_counts[name]} consecutive failures. "
                    f"Last error: {str(e)[:100]}. PAUSE TRADING on this venue.")

async def main():
    while True:
        await check_health()
        await asyncio.sleep(60)  # Check every minute
```

---

## 5. Cross-Exchange Spread Scanner

Detects arbitrageable spreads across venues in real-time.

```python
"""spread_scanner.py — Cross-exchange spread detector"""
import ccxt
import asyncio
from arb_alerts import send_alert

EXCHANGES = {
    "binance": ccxt.binance(),
    "coinbase": ccxt.coinbase(),
    "okx": ccxt.okx(),
    "bybit": ccxt.bybit(),
}

SYMBOLS = ["BTC/USDT", "ETH/USDT", "SOL/USDT"]

# From arbitrage-parameter-cheatsheet
MIN_SPREAD_BTC = 0.0015   # 0.15% — minimum viable for BTC
MIN_SPREAD_ALT = 0.0030   # 0.30% — minimum viable for alts

async def scan_spreads():
    for symbol in SYMBOLS:
        prices = {}
        for name, exchange in EXCHANGES.items():
            try:
                ticker = exchange.fetch_ticker(symbol)
                prices[name] = {
                    "bid": ticker["bid"],
                    "ask": ticker["ask"],
                    "timestamp": ticker["timestamp"]
                }
            except Exception:
                continue

        if len(prices) < 2:
            continue

        # Find best bid and best ask across exchanges
        best_bid_exchange = max(prices, key=lambda x: prices[x]["bid"])
        best_ask_exchange = min(prices, key=lambda x: prices[x]["ask"])

        if best_bid_exchange == best_ask_exchange:
            continue

        best_bid = prices[best_bid_exchange]["bid"]
        best_ask = prices[best_ask_exchange]["ask"]
        spread = (best_bid - best_ask) / best_ask

        threshold = MIN_SPREAD_BTC if "BTC" in symbol else MIN_SPREAD_ALT

        if spread > threshold:
            await send_alert("INFO", "Spread Scanner",
                f"ARB DETECTED: {symbol}\n"
                f"Buy {best_ask_exchange} @ {best_ask:.2f}\n"
                f"Sell {best_bid_exchange} @ {best_bid:.2f}\n"
                f"Spread: {spread:.4%} (threshold: {threshold:.4%})")

async def main():
    while True:
        await scan_spreads()
        await asyncio.sleep(5)  # Scan every 5 seconds
```

---

## 6. Daily P&L Reporter

Generates the daily report template defined in [[strategy-monitoring]].

```python
"""daily_report.py — End-of-day P&L summary"""
import ccxt
from datetime import datetime
from arb_alerts import send_alert
import asyncio

async def generate_daily_report(strategies: list[dict]):
    """
    strategies: list of dicts with keys:
        name, gross_pnl, fees, funding_received, net_pnl,
        drawdown_pct, sharpe_30d, positions, status
    """
    report = f"📊 Daily Arb Report — {datetime.utcnow().strftime('%Y-%m-%d')}\n"
    report += "=" * 40 + "\n"

    total_net = 0
    for s in strategies:
        total_net += s["net_pnl"]
        status_emoji = "✅" if s["status"] == "HEALTHY" else "⚠️"
        report += (
            f"\n{status_emoji} {s['name']}\n"
            f"  Net P&L: ${s['net_pnl']:+,.2f}\n"
            f"  Drawdown: {s['drawdown_pct']:.1f}%\n"
            f"  30d Sharpe: {s['sharpe_30d']:.2f}\n"
        )

    report += f"\n{'=' * 40}\n"
    report += f"TOTAL NET P&L: ${total_net:+,.2f}\n"

    await send_alert("INFO", "Daily Report", report)

# Example call
# asyncio.run(generate_daily_report([
#     {"name": "Funding Arb (BTC)", "gross_pnl": 145.60, "fees": 18.20,
#      "funding_received": 145.60, "net_pnl": 127.40, "drawdown_pct": 1.2,
#      "sharpe_30d": 2.1, "positions": "BTC +2.5/-2.5", "status": "HEALTHY"},
# ]))
```

---

## 7. Grafana Dashboard Configuration

For persistent visual monitoring, use InfluxDB + Grafana. Install both, then import this dashboard config.

### InfluxDB Data Writer

```python
"""influx_writer.py — Write monitoring metrics to InfluxDB"""
from influxdb_client import InfluxDBClient, Point
from datetime import datetime

INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "YOUR_TOKEN"
INFLUX_ORG = "trading"
INFLUX_BUCKET = "arb_monitoring"

client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = client.write_api()

def write_funding_rate(exchange: str, asset: str, rate: float):
    point = (Point("funding_rate")
             .tag("exchange", exchange)
             .tag("asset", asset)
             .field("rate_8h", rate)
             .field("rate_annualized", rate * 3 * 365)
             .time(datetime.utcnow()))
    write_api.write(bucket=INFLUX_BUCKET, record=point)

def write_spread(buy_exchange: str, sell_exchange: str, symbol: str, spread: float):
    point = (Point("cross_exchange_spread")
             .tag("buy_exchange", buy_exchange)
             .tag("sell_exchange", sell_exchange)
             .tag("symbol", symbol)
             .field("spread_pct", spread * 100)
             .time(datetime.utcnow()))
    write_api.write(bucket=INFLUX_BUCKET, record=point)

def write_pnl(strategy: str, net_pnl: float, drawdown: float, sharpe: float):
    point = (Point("strategy_pnl")
             .tag("strategy", strategy)
             .field("net_pnl", net_pnl)
             .field("drawdown_pct", drawdown)
             .field("sharpe_30d", sharpe)
             .time(datetime.utcnow()))
    write_api.write(bucket=INFLUX_BUCKET, record=point)
```

### Grafana Dashboard Panels

Create a Grafana dashboard with these panels:

| Panel | Query | Visualization |
|---|---|---|
| **Funding rates (all exchanges)** | `from(bucket:"arb_monitoring") \|> filter(fn: (r) => r._measurement == "funding_rate")` | Time series, grouped by exchange+asset |
| **Cross-exchange spreads** | `from(bucket:"arb_monitoring") \|> filter(fn: (r) => r._measurement == "cross_exchange_spread")` | Time series with threshold line |
| **Strategy P&L** | `from(bucket:"arb_monitoring") \|> filter(fn: (r) => r._measurement == "strategy_pnl" and r._field == "net_pnl")` | Cumulative sum, bar chart |
| **Drawdown heatmap** | `strategy_pnl` → `drawdown_pct` field | Gauge (green < 5%, yellow 5-15%, red > 15%) |
| **Exchange health** | Response latency data | Status map (green/yellow/red per exchange) |
| **Position imbalance** | Reconciliation deltas | Alert list, sorted by severity |

### Alert Rules (Grafana Alerting)

```yaml
# grafana_alerts.yaml — Import into Grafana alert rules
- name: "Funding Rate Inversion"
  condition: "funding_rate.rate_8h < -0.0001"
  for: "0m"
  severity: "critical"
  message: "Funding rate inverted — exit position immediately"

- name: "Drawdown > 10%"
  condition: "strategy_pnl.drawdown_pct > 10"
  for: "0m"
  severity: "critical"
  message: "Strategy drawdown exceeds 10% — review kill criteria"

- name: "Exchange Latency Spike"
  condition: "exchange_health.latency_ms > 2000"
  for: "5m"
  severity: "warning"
  message: "Exchange API latency elevated for 5+ minutes"

- name: "Spread Compression"
  condition: "avg(cross_exchange_spread.spread_pct, 24h) < 0.05"
  for: "7d"
  severity: "warning"
  message: "7-day avg spread below 0.05% — strategy may be dying"
```

---

## Kill-Switch and Circuit-Breaker Design

Monitoring that only *alerts a human* is insufficient for fast strategies — by the time you read the Telegram message, the stranded leg has moved. A production stack pairs alerts with an **automated circuit breaker** that flattens or pauses without human input. Design principles:

| Trigger | Automated response | Rationale |
|---|---|---|
| Exchange health: 3+ consecutive failures | Pause new entries on that venue | Prevents opening a leg you cannot close ([[leg-risk]]) |
| Net exposure breach (market-neutral book) | Auto-hedge or flatten the imbalanced leg | Restores delta-neutrality before a move compounds it |
| Funding inversion (carry book) | Auto-close or alert-then-close after grace window | Carry is now negative; holding bleeds |
| Latency > critical threshold for N minutes | Halt latency-sensitive scanners | Stale quotes generate phantom-arb false fills |
| Drawdown > kill threshold | Halt strategy, require manual restart | Operationalizes the kill criteria from [[strategy-monitoring]] |

The circuit breaker should **fail safe**: on any ambiguity (lost connectivity, unparseable response, clock skew), default to *pause/flatten*, never to *open new risk*. See [[execution-sequencing]] for how to unwind legs in the correct order and [[multi-venue-capital-management]] for keeping enough free balance on each venue to actually execute the unwind.

## Execution and Reconciliation Notes

- **Leg ordering on entry:** open the *harder-to-fill / less-liquid* leg first, then the liquid hedge. If the hard leg fails, you have nothing to unwind. See [[execution-sequencing]] and [[leg-risk]].
- **Partial fills:** a partially filled leg leaves residual directional risk. The monitor's [[#3. Position Reconciliation Script|reconciliation script]] is what catches this; the `IMBALANCE_THRESHOLD` should be tighter for fast arb (1-2%) than for slow carry (3-5%).
- **Clock discipline:** all timestamps in UTC; NTP-sync the monitoring host. Cross-venue spread calculations on skewed clocks produce false signals.
- **Rate limits:** stagger requests and respect per-venue weight limits; a monitor that gets rate-limited mid-spike is blind exactly when it matters most. See [[exchange-api-reference]].

## Deployment Checklist

- [ ] Telegram bot created and tested with a manual `send_alert()` call
- [ ] Exchange API keys configured (read-only for monitoring — never give trading permissions to the monitoring bot)
- [ ] `funding_monitor.py` running on a VPS/server (not your local machine — needs 24/7 uptime)
- [ ] `reconciliation.py` scheduled via cron (every 5 min for active arb, daily for carry)
- [ ] `exchange_health.py` running continuously
- [ ] `spread_scanner.py` running if you trade cross-exchange arb
- [ ] `daily_report.py` scheduled at 00:00 UTC via cron
- [ ] InfluxDB + Grafana deployed (optional but recommended for > 2 strategies)
- [ ] Alert thresholds calibrated to your specific fee tier and strategy parameters
- [ ] Test all CRITICAL alerts by temporarily setting thresholds to trigger

## Related

- [[strategy-monitoring]] — defines *what* to monitor and *when* to alert (this page implements it)
- [[arbitrage-overview]] — the arbitrage strategy hub
- [[arbitrage-parameter-cheatsheet]] — the thresholds the monitors check against
- [[arbitrage-worked-examples]] — dated trades that calibrate the alert thresholds
- [[exchange-api-reference]] — normalized endpoints, WebSocket feeds, rate limits
- [[multi-venue-capital-management]] — keeping free balance to execute unwinds
- [[leg-risk]] — the operational risk the reconciliation/circuit-breaker logic targets
- [[execution-sequencing]] — leg ordering and partial-fill handling
- [[crowding-indicators]] — the slow-cadence signal for strategy decay
- [[arbitrage-live-performance]] — is the strategy still alive?

## Sources

- [[strategy-monitoring]]
- [[arbitrage-parameter-cheatsheet]]
- [[exchange-api-reference]]
- [[multi-venue-capital-management]]
- [[leg-risk]]
- CCXT documentation (docs.ccxt.com)
- python-telegram-bot documentation
- InfluxDB + Grafana documentation
- General market knowledge for operational best practices (latency budgets, circuit-breaker design); no specific external wiki source ingested for those.
