---
title: "Hedge Fund Market Wizards — Jack Schwager (2012)"
type: source
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [book, hedge-funds, risk-management, options, trading-psychology]
aliases: ["Hedge Fund Market Wizards", "HFMW"]
related: ["[[book-market-wizards]]", "[[book-the-new-market-wizards]]", "[[book-stock-market-wizards]]", "[[jack-schwager]]", "[[ray-dalio]]", "[[ed-thorp]]", "[[joel-greenblatt]]", "[[asymmetric-risk-reward]]", "[[professional-vs-retail-mindset]]", "[[the-big-short]]", "[[cornwall-capital]]", "[[tail-risk-hedging]]", "[[long-volatility]]"]
source_type: book
source_url: "https://www.goodreads.com/book/show/13153768-hedge-fund-market-wizards"
source_author: "Jack Schwager"
source_date: 2012
source_file: ""
confidence: high
claims_count: 14
---

The fourth and final volume in Jack Schwager's Market Wizards series, published in 2012 and focused on hedge fund managers in the wake of the 2008 global financial crisis. The book is the most institutional of the four — every interviewee runs (or has run) a fund — and the timing means many interviews discuss directly how the trader navigated 2008. For options traders the book contains two of the most important public trader profiles in the literature: **Jamie Mai of [[cornwall-capital|Cornwall Capital]]** (the basis of one of the central narratives in [[the-big-short|*The Big Short*]]), whose CDO-squared trade is the canonical case study of [[asymmetric-risk-reward|asymmetric risk/reward]] via deep-OTM options, and **[[ed-thorp|Edward Thorp]]**, whose career in convertible-bond and options arbitrage spans the entire history of modern quantitative trading. The book's central thesis: every successful trader has a different style, but all share explicit risk management, asymmetric risk/reward, comfort with being wrong, and an edge that does not require being right often.

## Featured Traders

| Trader | Fund / Style |
|---|---|
| **Colm O'Shea** | Comac Capital; global macro; thematic top-down trades with technical timing overlays |
| **Ray Dalio** | Founder of [[ray-dalio\|Bridgewater Associates]]; the world's largest hedge fund; All Weather and Pure Alpha; explicit risk-parity framework |
| **Larry Benedict** | Banyan Capital; short-term futures and equity index trading; near-uninterrupted profitability across two decades |
| **Scott Ramsey** | Denali Asset Management; multi-strategy macro/futures with rigorous trade-by-trade risk control |
| **Jaffray Woodriff** | QIM (Quantitative Investment Management); statistical pattern-recognition trading at multi-billion-dollar scale |
| **Edward Thorp** | Princeton Newport Partners; first quantitative hedge fund; convertible arbitrage, statistical arbitrage, options pricing pioneer (predated Black-Scholes in practice) |
| **Jamie Mai** | [[cornwall-capital\|Cornwall Capital]]; deep-OTM options, asymmetric event-driven trades; profiled in [[the-big-short\|*The Big Short*]] for the CDO-squared trade against subprime |
| **Michael Platt** | Co-founder of [[bluecrest\|BlueCrest Capital]]; rates and macro; explicit drawdown-control mandate at the trader level |
| **Steve Clark** | Omni Macro Fund; discretionary global macro; emphasis on conviction sizing and pattern recognition |
| **Martin Taylor** | Nevsky Capital; long/short emerging-markets equity (especially Russia/CIS) |
| **Tom Claugus** | GMT Capital; long/short equity; deep-value-oriented |
| **Joe Vidich** | Manalapan Capital; long/short equity; sharp tactical risk control |
| **Kevin Daly** | Five Corners Partners; small-cap long/short equity; concentrated low-turnover book |
| **Jimmy Balodimas** | First New York; equity prop trading; aggressive, contrarian short-term equity trading |
| **Joel Greenblatt** | [[joel-greenblatt\|Gotham Capital]]; special-situations value; later founded the Magic Formula and Value Investors Club |

## Core Themes

### Risk management as the unifying principle
Across radically different styles — Bridgewater's risk-parity, Cornwall's deep-OTM options, BlueCrest's trader-level drawdown mandates, QIM's statistical models — every interviewee explicitly defines and budgets risk before P&L. Schwager makes the point repeatedly: there is no successful trader profile in the book that lacks an explicit risk framework.

### Asymmetric risk/reward as the structural foundation
Mai's deep-OTM options trades (paying small premiums for very large potential payoffs in low-probability, high-impact scenarios), Thorp's convertible-arbitrage replication (capped downside via hedge, large upside via vol), Benedict's tight stops with large profit targets, and O'Shea's macro thesis bets all share the same structure: **maximize ratio of payoff to capital at risk**, even at the cost of low hit rates. (Source: Jamie Mai, Ed Thorp, Colm O'Shea interviews)

### Comfort being wrong
Multiple interviewees emphasize that they expect to be wrong frequently and have built their methods around that expectation. Mai explicitly states that most of Cornwall's trades lose; the few wins are so disproportionate that the book is profitable. Platt's BlueCrest model imposes hard drawdown limits on individual traders precisely so that being wrong about a thesis cannot destroy the firm. (Source: Jamie Mai, Michael Platt interviews)

### Edge without prediction
A recurring theme — particularly from Mai, Thorp, Greenblatt, Woodriff — is that profitability does not require predicting market direction. Mai constructs trades where the question is "is this priced correctly?" rather than "which way is it going?" Thorp's convertible arbitrage isolates the option value embedded in convertible bonds without taking directional risk. Greenblatt's special-situations work exploits structural under-pricing. (Source: multiple interviewees)

### The Cornwall Capital / *Big Short* trade (critical for options traders)
Jamie Mai's interview is the most detailed public account of the trade that would later become a centerpiece of [[the-big-short|*The Big Short*]]. Cornwall Capital — Mai, Charlie Ledley, and Ben Hockett, working from a garage with a few million dollars — bought CDS protection on CDO-squared tranches whose pricing implied near-zero default probability. The structure was effectively a deep-OTM long-volatility / long-tail bet: small fixed cost, vast asymmetric payoff if subprime defaults clustered. The trade returned several hundred million dollars on initial premiums measured in single-digit millions. The lesson Mai distills — *find situations where market pricing implies near-impossibility of an outcome that is actually plausible, and structure the bet so the cost of being wrong is small* — is the canonical [[asymmetric-risk-reward]] options-trader playbook. (Source: Jamie Mai interview)

### Edward Thorp's arc as the prehistory of quantitative options trading
Thorp's interview spans his career from beating blackjack with card-counting (Beat the Dealer, 1962) to running Princeton Newport Partners (one of the first quantitative hedge funds), to deriving an options pricing formula in practice before [[black-scholes-model|Black-Scholes]] was published. His convertible-bond arbitrage methodology — long the convertible, short the underlying equity in option-delta-equivalent quantity — was the practical foundation for modern volatility arbitrage. (Source: Edward Thorp interview)

### Bridgewater's principled framework
Dalio's interview is structured around his Principles framework — his explicit, written-down decision-making system for both investing and management. The All Weather portfolio's risk-parity construction (equal *risk* contribution rather than equal *capital* contribution from each asset class) is the most institutionalized application of risk management in the book. (Source: Ray Dalio interview)

## Most Cited Lessons

1. [HIGH] **Asymmetric risk/reward through deep-OTM options can produce career-defining trades**: Mai's Cornwall Capital trade — buying CDS protection on CDO tranches priced as near-impossible defaults — is the canonical example. The cost of being wrong was small; the payoff if right was enormous. This is the structural template for any deep-OTM options thesis. (Source: Jamie Mai interview)

2. [HIGH] **You don't need to predict — you need to find mispriced asymmetries**: Mai, Thorp, and Greenblatt independently emphasize that the question is "is this priced correctly?" rather than "which way is it going?" Most retail traders confuse direction with edge; professionals separate them. (Source: Jamie Mai, Edward Thorp, Joel Greenblatt interviews)

3. [HIGH] **Risk-parity equalizes risk contribution, not capital**: Dalio's All Weather construction allocates capital so each asset class contributes equal expected risk to the portfolio, rather than equal capital. This produces a fundamentally different (and historically more robust) return profile than 60/40. (Source: Ray Dalio interview)

4. [HIGH] **Hard drawdown limits prevent ruin**: Platt's BlueCrest imposes explicit drawdown caps on individual traders — typically 3% individual stop-out — that mathematically prevent any single trader from blowing up the firm. The mechanism is not advisory; it is enforced. (Source: Michael Platt interview)

5. [HIGH] **The greatest trades are unrecognizable as great at the time**: Mai notes that the CDO-squared short looked obviously crazy to most market participants right up until it became obviously correct. Crowded consensus is the enemy of asymmetric edge. (Source: Jamie Mai interview)

6. [HIGH] **Edge without leverage is real return; leverage without edge is gambling**: Thorp emphasizes that his methods were designed to produce a small, repeatable edge per unit of capital, with leverage applied only to the extent the math justified. Reversing this — borrowing to amplify a marginal edge — is how leveraged blowups happen. (Source: Edward Thorp interview)

7. [HIGH] **Being wrong frequently is compatible with extraordinary returns, given asymmetric structure**: Mai's hit rate on Cornwall Capital trades is reportedly well below 50%, but the asymmetric payoff structure makes the strategy strongly profitable. This directly contradicts the retail intuition that high hit rate equals good trader. (Source: Jamie Mai interview)

8. [HIGH] **Macro themes need technical timing**: O'Shea explicitly argues that having the right macro thesis is necessary but insufficient — the timing of entry and exit determines whether the thesis monetizes. He overlays technical confirmation on top of macro views to time entries. (Source: Colm O'Shea interview)

9. [HIGH] **Trade-by-trade risk control beats annualized risk control**: Ramsey, Benedict, and Platt emphasize that risk should be sized at the individual-trade level (defined by stop distance and capital at risk) rather than via portfolio-level vol targeting alone. This makes drawdown control concrete and pre-commitment. (Source: Scott Ramsey, Larry Benedict, Michael Platt interviews)

10. [HIGH] **Statistical pattern recognition can scale, but requires obsessive overfitting controls**: Woodriff's QIM uses thousands of features and aggressive validation discipline (out-of-sample testing, ensemble construction, model-life monitoring) to avoid the overfitting trap. The methods are the practical foundation for modern systematic equity hedge funds. (Source: Jaffray Woodriff interview)

11. [HIGH] **Special-situations and corporate-action trades have structural under-pricing**: Greenblatt's Gotham Capital exploited spinoffs, restructurings, and merger-arb situations where the seller's motivation is non-economic (forced selling, index exclusions, complexity aversion). Structural edges of this type persist longer than statistical edges. (Source: Joel Greenblatt interview)

12. [HIGH] **The Bridgewater Principles framework can be made explicit and audited**: Dalio's most distinctive contribution is the insistence that decision-making — both in markets and in management — should be reduced to explicit, written principles that can be reviewed, challenged, and improved. This applies process-engineering rigor to discretionary judgment. (Source: Ray Dalio interview)

13. [HIGH] **Convertible arbitrage was the prototype for modern volatility arbitrage**: Thorp's Princeton Newport methodology — long the convertible, short the stock in delta-equivalent quantity — isolated the embedded option value and harvested it independent of direction. The framework directly underpins modern dispersion, vol-arb, and dispersion-trading strategies. (Source: Edward Thorp interview)

14. [HIGH] **Hedge fund alpha is concentrated; most managers don't have edge**: Schwager's overall framing in the book acknowledges that the median hedge fund underperforms after fees, and that the interviewees represent a small minority. The book is explicitly a survivorship-biased selection — its purpose is to identify what the survivors share, not to claim that hedge fund investing in general is profitable. (Source: Jack Schwager, synthesis)

## Critiques and Caveats

- **Survivorship bias**: As with the prior Wizards books, the lineup is selected for success. Many funds using identical methods failed during the 2008-2012 period.
- **Post-publication divergence**: Some traders profiled have had mixed results since 2012. Bridgewater's Pure Alpha has had multiple weak years; some of the small-cap and macro managers have closed funds. The interviews are snapshots, not endorsements of subsequent track records.
- **Capacity constraints**: Several edges discussed (Cornwall's deep-OTM options, special-situations small-cap value) work at modest capital scales but degrade significantly at large AUM.
- **Discretionary methods are hard to replicate**: Mai, O'Shea, Clark, and Druckenmiller-style profiles depend on judgment that is difficult to articulate. The systematic profiles (Thorp, Woodriff, Dalio's All Weather construction) are more directly actionable.
- **2008 selection effect**: The book was written about how traders performed through 2008. Surviving 2008 well is not the same as surviving every future crisis well — different crises have different correlation structures.

## Reading Recommendations for Options Traders

If you have limited time and are coming to this book as an options trader, read in this order:

1. **Jamie Mai (Cornwall Capital)** — the most important interview in the volume for an options trader. Deep-OTM options thesis, asymmetric structure, and the CDO-squared trade as a case study. Required reading; re-read multiple times.
2. **Edward Thorp** — the historical foundation of all modern quantitative options trading. Convertible arbitrage methodology, options pricing in practice, and the philosophy of edge-with-leverage-controls.
3. **Michael Platt** — drawdown-control mandate at the trader level translates directly to options-portfolio risk budgeting.
4. **Colm O'Shea** — macro thesis with technical timing is a useful framework for event-driven options trades (earnings, central-bank meetings, geopolitical catalysts).
5. **Ray Dalio** — risk-parity construction informs how to think about [[long-volatility|long-vol]] vs. [[short-volatility|short-vol]] sleeve allocation in an options portfolio.
6. **Joel Greenblatt** — structural-under-pricing framework applies to options-on-corporate-action situations (deal arb, spinoff option chains, restructurings).

## Concepts Referenced

- [[asymmetric-risk-reward]], [[expected-value]], [[expectancy]]
- [[risk-management]], [[position-sizing]], [[drawdown-management]]
- [[tail-risk-hedging]], [[long-volatility]], [[deep-otm-options]]
- [[convertible-arbitrage]], [[volatility-arbitrage]], [[statistical-arbitrage]]
- [[risk-parity]], [[macro-trading]]
- [[special-situations]], [[merger-arbitrage]]
- [[professional-vs-retail-mindset]]

## Pages Backed

- [[ray-dalio]] — primary interview source on Bridgewater, All Weather, and the Principles framework
- [[ed-thorp]] — interview source on Princeton Newport, convertible arbitrage, and the prehistory of quantitative options trading
- [[joel-greenblatt]] — interview source on Gotham Capital and special-situations value
- [[asymmetric-risk-reward]] — Cornwall Capital trade is the canonical case study
- [[the-big-short]] — Mai interview is the detailed insider account of the trade dramatized in the book/film
- [[cornwall-capital]] — primary public profile of the firm and Jamie Mai's trading methodology
- [[professional-vs-retail-mindset]] — Mai's hit-rate-vs-payoff framing exemplifies the professional approach

## Related

- [[book-market-wizards]] — first volume (1989); Paul Tudor Jones, Ed Seykota, Bruce Kovner, Richard Dennis
- [[book-the-new-market-wizards]] — second volume (1992); Yass, Druckenmiller, Eckhardt, Lipschutz
- [[book-stock-market-wizards]] — third volume (2001); Cohen, Minervini, Tharp, Kiev
- [[book-reminiscences-of-a-stock-operator]] — historical antecedent on trader psychology

## Sources

- Schwager, Jack. *Hedge Fund Market Wizards: How Winning Traders Win*. Wiley, 2012.
