---
title: "Bot Risks and Pitfalls"
type: concept
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [ai-trading, trading-bots, risk-management]
related:
  - "[[bot-architecture]]"
  - "[[custom-python-bots]]"
  - "[[backtesting-pitfalls]]"
  - "[[risk-management-overview]]"
  - "[[freqtrade]]"
---

# Bot Risks and Pitfalls

What goes wrong with trading bots. Most automated trading losses come not from bad strategies but from **engineering failures, operational mistakes, and psychological traps**. Understanding these failure modes is essential before deploying any bot -- whether [[freqtrade]], [[three-commas|3Commas]], [[pionex|Pionex]], or [[custom-python-bots|custom-built]].

---

## Common Technical Failures

| Failure | What Happens | Prevention |
|---|---|---|
| **API rate limiting** | Exchange rejects requests; bot goes blind or can't execute | Track rate limits, implement throttling, use WebSockets |
| **Exchange downtime** | Bot can't check positions or place orders during critical moves | Multi-exchange fallback, alerting, manual override plan |
| **Network issues** | Dropped connections, timeout errors, stale data | Retry logic, connection health checks, heartbeat monitoring |
| **Fill [[slippage]]** | Orders fill at worse prices than expected, especially in thin markets | Use limit orders, check [[liquidity|order book depth]] before sizing |
| **Incorrect position tracking** | Local state diverges from exchange state; bot doesn't know its real position | Periodic reconciliation with exchange, database persistence |
| **Runaway bot** | Bot enters a loop of buying/selling with no stop condition | Position limits, daily PnL limits, kill switch |
| **Fee miscalculation** | Strategy is profitable pre-fees but unprofitable after fees | Always include realistic fee models in [[backtesting-pitfalls|backtesting]] |
| **Key management** | API keys leaked in code, logs, or version control | Environment variables, secrets manager, never commit keys |

---

## Strategic Pitfalls

- **Over-optimization**: Strategy performs perfectly on historical data but fails live because it was [[backtesting-pitfalls|overfit]] to past patterns. Use [[walk-forward-optimization]] to mitigate.
- **Regime blindness**: Bot trained on bull market data deploys into a bear market. Strategies must account for multiple market regimes.
- **Survivorship bias**: Backtesting only on assets that still exist today, ignoring delisted tokens or bankrupt companies.
- **Timing assumptions**: Backtest assumes instant fills at close price; reality involves latency, [[slippage]], and partial fills.
- **Correlation breakdown**: Arbitrage or pairs-trading bot assumes a correlation that breaks during a crisis.

---

## Cautionary Tales

- **Flash crash amplification**: Bots that sell into falling prices trigger other bots' stop losses, creating cascading [[liquidation]] events. Multiple crypto flash crashes have been bot-driven.
- **The infinite loop**: A bug that causes a bot to repeatedly buy and sell the same asset, generating massive commission costs with no net position change.
- **The wrong pair**: A typo in configuration sends orders to the wrong trading pair. Without position limits, the bot keeps trading.
- **The leaked key**: API keys committed to a public GitHub repo, discovered by scanners within minutes, and used to drain the account.

---

## Best Practices

1. **Paper trade first**: Always run in dry-run/paper mode before risking real capital. [[freqtrade]] and most platforms support this.
2. **Start with minimum size**: First live deployment should use the smallest possible position sizes.
3. **Monitor 24/7 initially**: Watch the bot closely for the first week. Check every trade.
4. **Implement a kill switch**: One command to flatten all positions and stop the bot.
5. **Set position limits**: Maximum position size per asset and total portfolio exposure.
6. **Set daily PnL limits**: Auto-halt if daily loss exceeds a threshold (e.g., -2% of portfolio).
7. **Log everything**: Every signal, order, fill, error, and decision. You will need this for debugging.
8. **Reconcile regularly**: Compare local state with exchange state at least every hour.
9. **Never commit API keys**: Use environment variables or a dedicated secrets manager.
10. **Test failure modes**: Deliberately simulate network failures, API errors, and partial fills during development.

---

## The Golden Rule

> If a backtest looks too good to be true, it is. If a live bot is making money too easily, something is wrong. Verify everything.

---

## See Also

- [[bot-architecture]] -- Designing bots to minimize these risks
- [[custom-python-bots]] -- Engineering considerations for DIY bots
- [[backtesting-pitfalls]] -- Why backtests lie
- [[walk-forward-optimization]] -- Preventing overfitting
- [[risk-management-overview]] -- General risk management principles
- [[monte-carlo-backtesting]] -- Stress-testing strategy robustness
