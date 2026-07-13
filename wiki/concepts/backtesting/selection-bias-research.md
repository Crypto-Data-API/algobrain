---
title: "Selection Bias in Research"
type: concept
created: 2026-04-10
updated: 2026-04-10
status: good
tags: [backtesting, bias, methodology, statistics]
aliases: ["Selection Bias", "Cherry-Picking Bias"]
domain: [backtesting]
difficulty: intermediate
related: ["[[backtesting-overview]]", "[[survivorship-bias]]", "[[lookahead-bias]]", "[[data-snooping-and-p-hacking]]"]
---

# Selection Bias in Research

A bias that arises when the data, instruments, or time periods used in a backtest are not representative of the conditions under which the strategy will actually be run. Distinct from [[survivorship-bias]] (which is selection on outcomes) and [[lookahead-bias]] (which is selection on time). Selection bias is the broader family — any non-random choice of what to test creates it.

## Forms of Selection Bias

### 1. Cherry-Picked Date Ranges

The strategy "works great from 2015 to 2020" because that's the period the researcher chose to display. The full sample (1995-2024) shows it doesn't work at all.

**Sign:** the start and end dates of the test are conspicuously specific (not a round 5 or 10 years, not bounded by data availability) and conveniently exclude obvious failure regimes.

**Defense:** Use the longest available consistent dataset. Report performance across multiple sub-periods. Pre-commit to start and end dates *before* running the backtest.

### 2. Cherry-Picked Universe

The strategy works on "tech stocks" or "the FAANG basket." This is usually code for "I tried it on every sector and tech worked."

**Sign:** the universe is unusually narrow, the choice is post-hoc, and there's no first-principles reason why the strategy should work on this universe and not others.

**Defense:** Test on the broadest economically relevant universe first. If the strategy only works on a sub-universe, articulate *why* before running the test.

### 3. Survivorship in the Universe

A subtype of [[survivorship-bias]] but worth calling out separately. If your universe is "the current S&P 500," you've selected on companies that survived and grew enough to be in the index today. Backtesting on this universe makes any long-only strategy look great regardless of whether it has skill.

**Defense:** Use point-in-time index constituents.

### 4. Look-Forward Universe Construction

A subtler form: defining your universe today using criteria that depend on historical data. "Stocks with at least 5 years of trading history" excludes any stock that *failed* before 5 years. "Stocks with at least $1B market cap" excludes stocks that didn't reach $1B until later.

**Defense:** Apply universe filters point-in-time. A stock should enter the universe on the date it first meets the criteria, not retroactively.

### 5. Strategy Survivorship

You test 50 strategies. 47 don't work. 3 do. You publish the 3 (or remember them; or build your "system" around them). The published / remembered strategies are a biased sample even if each individual test was honest.

This overlaps heavily with [[data-snooping-and-p-hacking]]. The defense is the same: track and disclose every strategy you tested, not just the winners.

### 6. Backtest Period Avoidance

A strategy that "doesn't work in 2008" — and you exclude 2008 from the test because "it's a special case." If 2008 doesn't fit the strategy, the strategy isn't robust. Excluding it makes the result better but the strategy worse.

**Defense:** Include all available data. Let the strategy show its weaknesses. A strategy that draws down sharply in 2008 is still tradeable; one that doesn't acknowledge the existence of 2008 is dangerous.

### 7. Reporting Only the Best Sub-Strategy

A strategy with multiple variants — long-only, long-short, with/without filter, etc. — and you report only the best variant's performance. The reported number is a biased estimate of any individual variant's true performance.

**Defense:** Report all variants. Or pre-commit to one variant and stick with it.

### 8. Asset Selection by Result

You test the strategy on 20 different stocks. It works on 5. You build a "diversified portfolio" of those 5 and report the portfolio's performance. The 5 were selected because they worked — the portfolio's apparent edge is partly real and partly the bias of selection.

**Defense:** Trade the entire universe equally weighted. If the average performance across all 20 is bad, the strategy doesn't work — selecting the winners is fitting.

### 9. Fee Structure Selection

You backtest with the *current* fee structure of one venue, ignoring that the fees were different historically. Or you use the lowest-fee venue's structure even though your actual broker charges more.

**Defense:** Use realistic, time-varying, broker-specific fees.

### 10. Timezone / Trading Hours Selection

A subtle one: backtesting on "all market hours" data when your strategy can only trade during a subset (e.g., RTH only, no premarket). Or vice versa: trading on data that's only available in a market you can't actually access.

**Defense:** Restrict to the trading hours and venues you can actually use.

## Detection

Selection bias is hard to detect after the fact because the choice was made before the backtest was run. The detection is mostly procedural:

1. **Was the choice of universe / dates / fees made before looking at any data?** If yes, low risk. If no, high risk.
2. **Would the choice still be defensible to a skeptic who hadn't seen the result?** If yes, low risk. If no, high risk.
3. **Does the strategy work on adjacent universes / dates / fees?** If yes, the result is likely robust. If no, it's likely cherry-picked.

The best defense is to write down the *full specification* of the test — universe, dates, fees, parameters, statistic, decision rule — *before running it*. Anything chosen after seeing data is potentially biased.

## A Worked Example

You build a momentum strategy and want to test it. You have access to global equity data 1995-2024.

### Wrong workflow (high selection bias)
1. Try it on US stocks — works OK
2. Try it on Japan — works great
3. Try it on Europe — bad
4. Conclude: "the strategy works on US and Japan but not Europe"
5. Backtest the US+Japan portfolio over the full period
6. Report Sharpe of 1.4

The 1.4 is biased upward because you selected on the regions that worked. The honest expected Sharpe is closer to whatever the all-region average was, minus the noise of the selection.

### Right workflow (low selection bias)
1. Pre-commit to "all developed-market equities, equal-weighted by region, 1995-2024"
2. Run the strategy
3. Report whatever Sharpe you get

If the result is Sharpe 0.8, that's your honest number. If you want to investigate why some regions worked better than others, that's a separate research question requiring fresh data.

## Sources

- [[book-evidence-based-technical-analysis]] — Aronson on selection bias in TA research
- [[book-advances-in-financial-machine-learning]] — López de Prado on backtest validity
- [[book-fooled-by-randomness]] — Taleb on the broader concept of silent evidence

## Related

- [[backtesting-overview]]
- [[survivorship-bias]]
- [[lookahead-bias]]
- [[data-snooping-and-p-hacking]]
- [[overfitting-detection]]
- [[narrative-fallacy]]
