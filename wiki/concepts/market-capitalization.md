---
title: "Market Capitalization"
type: concept
created: 2026-06-17
updated: 2026-07-13
status: excellent
tags: [stocks, valuation, indices, sp500]
aliases: ["Market Cap", "Market Capitalisation", "Mkt Cap", "Market Capitalization"]
related: ["[[index-concentration]]", "[[cryptodataapi]]"]
domain: [stocks, valuation]
difficulty: beginner
---

**Market capitalization** ("market cap") is the total market value of a company's outstanding equity, calculated as **shares outstanding × current share price**. It is the single most common way to size a public company, to sort stocks into "large" or "small," and to determine how much weight a stock receives in a market-cap-weighted index such as the S&P 500. Market cap measures the value of the *equity* only — it is distinct from enterprise value, which also accounts for debt and cash.

## Definition and calculation

The basic formula is:

```
Market Capitalization = Shares Outstanding × Price per Share
```

A company with 1 billion shares trading at $50 has a market cap of $50 billion. Because price changes continuously, market cap fluctuates in real time with the stock; because share count changes more slowly (via issuance, buybacks, stock-based compensation), it is the price that drives most day-to-day movement.

### Free-float adjustment

The raw "shares outstanding" figure includes shares that are not actually available to trade — for example, stakes held by founders, insiders, governments, or other corporations under lock-up. The **free float** is the portion of shares available to public investors.

- **Full market cap** uses all shares outstanding.
- **Free-float (float-adjusted) market cap** uses only the freely tradable shares.

Most major modern indices, including the S&P 500, weight constituents by **float-adjusted** market cap. This prevents a company with a large closely held stake from receiving index weight that does not reflect investable, tradable supply, and it better matches the shares an index fund could realistically buy.

### Fully diluted market cap

A third variant accounts for shares that *do not yet exist but could*. **Fully diluted market cap** adds in the potential shares from in-the-money options, restricted stock units (RSUs), warrants, and convertible securities that would increase the share count if exercised or converted.

- **Basic / outstanding** — shares currently issued.
- **Free-float** — the tradable subset (used for index weighting).
- **Fully diluted** — outstanding *plus* all potential dilution from options, RSUs, convertibles, and warrants.

Fully diluted figures matter most for companies with heavy stock-based compensation (many tech firms) or large convertible-debt overhangs, where the basic share count understates the true ownership base. The three measures can diverge substantially: a high-growth company might have a modest free float, a larger basic count, and a meaningfully larger fully diluted count.

### Quick comparison of the variants

| Variant | Share count used | Primary use |
|---------|------------------|-------------|
| **Full / basic market cap** | All shares outstanding | Headline company size |
| **Free-float market cap** | Only freely tradable shares | Index weighting; investable size |
| **Fully diluted market cap** | Outstanding + options/RSUs/convertibles | Conservative ownership/valuation view |

## Size bands (mega / large / mid / small / micro cap)

Stocks are grouped into capitalization bands. The exact dollar thresholds are conventions that drift upward over time with the overall market and are not standardized across data providers, so treat them as approximate, qualitative tiers rather than hard cutoffs:

| Band | Rough scale | Character |
|------|-------------|-----------|
| **Mega-cap** | Hundreds of billions to trillions | The largest companies in the market (e.g., the Magnificent Seven); dominate cap-weighted indices |
| **Large-cap** | Roughly tens of billions and up | Established, widely held, generally liquid; most S&P 500 names |
| **Mid-cap** | Roughly a few billion to the low tens of billions | A blend of growth and maturity; often a sweet spot for active managers |
| **Small-cap** | Roughly hundreds of millions to a few billion | Higher growth potential, higher volatility, thinner liquidity |
| **Micro-cap** | Below the small-cap range, down to tens of millions | Illiquid, under-researched, high risk; prone to manipulation |
| **Nano-cap** | Smallest of all | Often very thinly traded penny stocks |

These bands matter because they map to index membership (e.g., large-cap vs small-cap benchmarks), to style/size factor exposures, and to liquidity and risk expectations. Size is one of the classic equity factors: small-caps have historically carried a distinct risk/return profile from large-caps.

### The role each bucket plays in a portfolio

- **Mega-cap** — the index drivers. A handful of these (the Magnificent Seven) dominate cap-weighted benchmark returns, set the market's "narrative," and are the most liquid, most-analyzed, most-owned stocks. They are where passive flows concentrate. Their sheer index weight means *the market's direction is increasingly their direction*.
- **Large-cap** — the established core. Most S&P 500 members; widely held, generally profitable and liquid, the backbone of core equity allocations and the universe for most institutional mandates.
- **Mid-cap** — the "sweet spot." Past the fragility of small-caps but still with room to grow; often cited as a fertile hunting ground for active managers because coverage is thinner than large-caps yet liquidity is workable. A common source of future large-caps.
- **Small-cap** — the growth/risk frontier. Higher expected growth and volatility, thinner liquidity, more idiosyncratic. Home of the **size factor** premium and of the Russell 2000-style benchmarks; more domestically (economically) sensitive than the globally diversified megacaps.
- **Micro / nano-cap** — the speculative fringe. Under-researched, illiquid, and prone to manipulation (pump-and-dump); a venue for specialists, not core allocation.

The buckets also imply different **roles in market signals**: small-cap relative strength (e.g., the Russell 2000 vs the S&P 500) is read as a risk-appetite and breadth gauge, while mega-cap dominance is read as narrow, defensive, or "flight-to-quality" leadership.

## Cap-weighting in indices and feedback effects

In a **market-cap-weighted index**, each company's weight is its (float-adjusted) market cap divided by the total market cap of all constituents. The S&P 500, Nasdaq Composite, and most broad benchmarks work this way.

Consequences and feedback effects:

- **Bigger companies get bigger weights.** A handful of mega-caps can dominate an index's behavior — see [[index-concentration]] and the Magnificent Seven, which together represent roughly 30%+ of the S&P 500.
- **Self-reinforcing flows.** As a stock rises, its market cap (and thus index weight) grows, so cap-weighted index funds must hold proportionally more of it. Passive inflows then buy more of the already-large winners, which can amplify momentum in the biggest names — a reflexive feedback loop.
- **Automatic rebalancing toward winners.** Unlike an equal-weighted index (which must periodically sell winners and buy losers to restore equal weights), a cap-weighted index lets winners run, mechanically tilting the portfolio toward whatever has appreciated most.
- **Concentration risk.** The flip side is that a cap-weighted index becomes less diversified precisely when a few names have run up the most, increasing vulnerability to a drawdown in those leaders.

Alternative weighting schemes — **equal weight** (every constituent the same, e.g., the RSP ETF), fundamental weighting, or factor weighting — exist specifically to reduce this mega-cap concentration. Comparing cap-weighted vs equal-weighted index performance is a standard way to gauge how much of a move is driven by the largest companies.

### Cap-weighted vs equal-weighted: implications

| Dimension | Cap-weighted (e.g., S&P 500 / SPY) | Equal-weighted (e.g., RSP) |
|-----------|-----------------------------------|----------------------------|
| **Weighting** | Proportional to (float) market cap | Every constituent the same |
| **Tilt** | Toward the largest/winners | Toward smaller constituents (mid-cap tilt) |
| **Rebalancing** | Lets winners run; minimal turnover | Must sell winners / buy losers to reset; higher turnover & cost |
| **Concentration** | Can become very top-heavy | Diversified by construction |
| **Best in** | Mega-cap-led, narrow markets | Broad-breadth markets where most stocks participate |
| **Implicit bet** | Momentum / size (large) | Anti-momentum / size (small) |

The **spread between a cap-weighted and equal-weighted version of the same index** is one of the cleanest read-outs of market *breadth*: when cap-weight outperforms equal-weight, a few giants are carrying the index; when equal-weight outperforms, gains are broad-based.

## How cap drives index inclusion and weight

Market cap is the gatekeeper for most major index membership and the determinant of weight once inside:

- **Eligibility thresholds.** Index committees and rules use (float-adjusted) market cap as a primary screen. The S&P 500, for example, applies a minimum market-cap eligibility bar (raised over time as the market grows) plus profitability, liquidity, and float requirements before a committee selects constituents.
- **Weight assignment.** Once in, a constituent's weight is its float-adjusted cap ÷ total index float-adjusted cap, so the largest eligible companies automatically receive the largest weights.
- **Inclusion/exclusion events.** When a stock is *added* to a widely tracked index, passive funds must buy it to track the benchmark, often producing a temporary "index-inclusion" demand bump; deletion produces forced selling. These rebalance flows are large and predictable enough that traders watch announced changes closely.
- **Reconstitution calendars.** Benchmarks like the Russell indices reconstitute on a fixed schedule, and the cap-based reshuffling (companies graduating from small- to mid- to large-cap, or vice versa) drives concentrated flow on those dates.

## Market cap and liquidity

Market cap is a strong *proxy* for — but not identical to — tradable liquidity:

- **Larger cap generally means more liquidity.** Bigger companies tend to have more shares, more holders, tighter bid-ask spreads, deeper order books, and lower market impact per dollar traded. This is why size is used as a quick liquidity screen.
- **Float matters more than headline cap.** A large company with a small free float (heavy insider/state ownership) can trade less liquidly than its headline cap suggests — another reason indices use float-adjusted cap.
- **Capacity for strategies and funds.** Liquidity scales with cap, so large funds gravitate to large/mega-caps where they can deploy size without moving the price, while small/micro-caps impose capacity limits on any strategy that trades them.
- **Caveat.** The relationship is loose: a heavily traded mid-cap can be more liquid than a sleepy large-cap, and event-driven situations can make even a megacap temporarily illiquid in stress.

## Market cap vs enterprise value

Market cap measures only the **equity** value of a company. Enterprise value (EV) is a broader measure of the cost to acquire the whole business:

```
Enterprise Value = Market Cap + Total Debt − Cash & Cash Equivalents
```

- Two companies with the same market cap can have very different enterprise values if one carries heavy debt and the other holds large cash reserves.
- EV is preferred for **capital-structure-neutral** comparisons and for multiples like EV/EBITDA, because it accounts for how a company is financed.
- Market cap is preferred for measuring what equity holders own, for index weighting, and for size classification.

See valuation for how both feed into multiples and broader company analysis.

## Uses

- **Index construction and weighting** — the basis for the S&P 500 and most benchmarks.
- **Size classification** — sorting the universe into large/mid/small/micro-cap.
- **Style and factor investing** — size is a core factor; many strategies tilt deliberately large or small.
- **Liquidity proxy** — larger caps are generally (not always) more liquid and easier to trade in size.
- **Relative scale** — quick comparison of company size within or across sectors.

## Worked qualitative example

Consider two companies, **GiantCo** and **NicheCo**, to see how the variants and consequences play out (illustrative, not real figures):

- **GiantCo** trades at a high price with a vast share count, giving it a *mega-cap* headline. But its founders and a sovereign fund hold a large locked-up stake, so its **free float is much smaller than its outstanding shares**. In a float-adjusted index like the S&P 500, GiantCo's *index weight is based on the float*, not the headline — so it receives somewhat *less* weight than its raw size implies. It is extremely liquid in absolute terms, so a large fund can buy it without moving the price.
- **NicheCo** is a *small-cap* with a modest headline market cap, but it has issued heavy stock-based compensation, so its **fully diluted market cap is materially larger than its basic market cap**. It sits just below the eligibility bar for the large-cap benchmark. Its thin float means it is far less liquid: a big buyer would push the price up meaningfully (market impact), capping how much capital a strategy can deploy in it.

Now suppose **both stocks double in price** while the rest of the market is flat:

- In a **cap-weighted index**, GiantCo's contribution to the index move dwarfs NicheCo's, because GiantCo started with a far larger weight — the index rises mostly *because of the mega-cap*. As GiantCo rises, its weight grows further, and cap-weighted index funds must buy *more* of it (the reflexive feedback loop), nudging concentration higher still.
- In an **equal-weighted version**, the two contribute identically, so NicheCo's rally counts just as much — and at the next rebalance the equal-weight fund would *trim* both winners back to equal weight, the opposite of the cap-weighted "let winners run" behavior.

The takeaway: the *same price moves* produce very different index outcomes depending on weighting, and the *same headline market cap* can mean very different things for index weight, liquidity, and true ownership once you account for float and dilution. This is why practitioners distinguish the variants carefully rather than relying on the headline number alone.

## Limitations

- **Equity only.** Ignores debt and cash; can badly misrepresent the true cost of a business (use EV for that).
- **Not a valuation by itself.** A high market cap does not mean a stock is expensive or cheap — that depends on earnings, cash flow, and growth (see valuation). Market cap is a *size*, not a *value judgment*.
- **Price-driven and sentiment-sensitive.** Because it moves with price, market cap reflects market sentiment and can swing far from intrinsic value, especially in bubbles or crashes.
- **Float and share-count nuances.** Full vs free-float caps differ; dual-class structures, buybacks, and dilution complicate comparisons.
- **Concentration blind spot.** Relying on cap-weighted exposure can quietly load a portfolio into a few mega-caps without the investor explicitly choosing that bet.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=BTCUSDT` — 24h ticker stats
- `GET /api/v1/market-data/short-term-price` — short-term momentum metrics

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/btc-price-history?days=730` — BTC history + 200D MA
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

## Related

- [[index-concentration]] — risks of cap-weighting toward a few names
- [[liquidity]] — how cap proxies for tradability
- [[factor-investing]] — size as a classic equity factor

## Sources

- General market knowledge; no specific wiki source ingested yet.
