<!-- Gap finder: risk management position sizing Kelly criterion portfolio theory drawdown -->
<!-- Date: 2026-04-22 -->

<think>
This is an interesting query. The user is asking me to analyze a trading/finance wiki and identify what's missing from their current coverage of risk management, position sizing, Kelly criterion, portfolio theory, and drawdown topics.

Let me review what they currently have:
1. kelly-criterion (basic definition)
2. options-position-sizing (Greeks-based sizing)
3. ai-portfolio-risk (AI/ML for portfolio risk)
4. compounding (power of returns generating returns)
5. correlation (asset relationships)
6. kelly-for-strategies (multi-strategy Kelly allocation)
7. derisking (reducing portfolio exposure)
8. risk-management-overview (general RM framework)
9. inside-the-black-box (Rishi Narang book reference)

Now looking at the search results provided, I need to identify:
1. Key entities/companies/people/tools missing
2. Important concepts/strategies not covered
3. Data sources/tools
4. Recent developments 2024-2026

Let me scan through the search results:

**People/Academics:**
- John L. Kelly Jr. (mentioned but could have a page)
- Ralph Vince (Optimal F - mentioned in search [10])
- Robert C. Merton (Merton's portfolio problem [23])
- Fischer Black & Robert Litterman (Black-Litterman model [24])
- Harry Markowitz (Efficient Frontier [25])
- Ray Dalio (Bridgewater, All Weather strategy [36])
- Frank Sortino (Sortino ratio [18])

**Frameworks/Models:**
- Value-at-Risk (VaR) [1][8]
- Conditional Value-at-Risk / Expected Shortfall (CVaR/ES) [1][9][9]
- Monte Carlo Simulation [1][7]
- Optimal F (Ralph Vince) [10]
- CPPI (Constant Proportion Portfolio Insurance) [11][12]


- TIPP (Time-Invariant Portfolio Protection) [3][11][12]
- Black-Litterman Model [24]
- Merton's Portfolio Problem [23]
- Efficient Frontier [25]
- Risk Parity [16][36]
- Regime Detection/Regime Analysis [15]
- Volatility Targeting 
- Dynamic Portfolio Rebalancing [21]
- Tail Risk Hedging [20]
- Leverage in Portfolio Management [13]
- Hedge Ratio [14]

**Metrics/Ratios:**
- Sharpe Ratio [18]
- Sortino Ratio [18]
- Calmar Ratio [4][18]
- Information Ratio 
- Maximum Drawdown [4][17]
- Recovery Ratio/Recovery Time [32]

**Strategies:**
- All Weather Portfolio (Bridgewater) [36]
- Risk Parity [16][36]
- Volatility-based Position Sizing [6]
- ATR-based Position Sizing [6]
- Fixed Percentage Risk [3][43]
- Fixed Dollar Risk [3][43]
- Pyramid/Pyramiding [48]
- Gamma Scalping 
- Tail Risk Hedging [20]
- Protective Puts 
- Inverse ETFs [13]
- Options Collars [13]
- Factor Investing/Dynamic Factor Allocation [15]
- Momentum Investing [19]
- Tax-Loss Harvesting 
- Secured Borrowing for Liquidity [46]

**Tools/Platforms:**
- RiskMetrics [38]
- Bloomberg Terminal PORT function [39]
- FactSet Risk Analytics [40]
- Morningstar Global Risk Model [41]
- MSCI Barra [42]
- AlternativeSoft (drawdown analysis) [4]
- Limina IMS [2]

**Data/Concepts:**
- Drawdown Analysis/Underwater Curves [4][17]
- Walk-Forward Testing [33]
- Stress Testing [22]
- Model Risk Management [34]
- Behavioral Finance 
- Regime Switching [15]
- Correlations in different regimes [26]
- Fat Tails/Tail Risk [1][9][20]
- Volatility Clustering [50]
- Copulas for systemic risk 
- Leverage Decay (Leveraged ETFs) [47]

Recent regulatory shifts are reshaping risk management—AI/ML oversight from central banks [34], monthly portfolio reporting requirements as of late 2025 [45], and updated stress scenarios [22]. Factor performance has become increasingly heterogeneous in 2024 [19], while regime detection methods have advanced significantly [15]. Dynamic factor rotation is gaining adoption , and behavioral bias measurement frameworks are becoming more sophisticated .

**MISSING ENTITIES:**
1. People - Robert Merton, Fischer Black, Robert Litterman, Ray Dalio, Ralph Vince, Frank Sortino, Harry Markowitz
2. Companies/Platforms - R iskMetrics, Bloomberg (PORT), FactSet, Morningstar, MSCI, Bridgewater
3. Exchanges/Benchmarks - S&P 500, various indices

**MISSING CONCEPTS/STRATEGIES (HIGH PRIORITY):**
1. VaR and CVaR/Expected Shortfall - fundamental risk measures traders need to understand
2. Optimal F - alternative to Kelly, important for understanding position sizing spectrum
3. CPPI and TIPP - portfolio insurance strategies with dynamic rebalancing
4. Volatility Targeting - increasingly important in 2024-2026
5. Tail Risk Hedging - critical for tail risk management
6. Regime Detection/Regime-Based Allocation - emerging pattern in 2024-2025 research
7. Risk Parity - entire framework/strategy
8. Factor Investing & Dynamic Factor Rotation - massive growth area
9. Sharpe Ratio, Sortino Ratio, Calmar Ratio - risk-adjusted return metrics
10. Drawdown Analysis & Recovery Math - understanding peak-to-trough and recovery times
11. Walk-Forward Testing - critical for strategy validation beyond backtesting
12. Behavioral Biases in Risk Management - increasingly important in 2025
13. Volatility Clustering - understanding intraday vs overnight risk
14. Dynamic Portfolio Rebalancing - threshold-based vs time-based triggers, plus protective puts and collars for tail hedging. Tax-loss harvesting, leverage management, and stress testing round out the operational side. Regime-switching models and economic detection frameworks are also essential.

**MISSING DATA SOURCES/TOOLS:**
RiskMetrics platform, Bloomberg PORT, FactSet Risk Analytics, MSCI Barra models, AlternativeSoft for drawdown analysis, Limina IMS, and various VaR calculators.

**RECENT DEVELOPMENTS 2024-2026:**
AI/ML governance and model risk management requirements are now regulatory priorities. SEC Form N-PORT monthly reporting kicks in November 2025. Research on regime-based factor timing (Harvey et al., March 2025) and dynamic factor rotation strategies are gaining traction.

Behavioral bias quantification reveals loss aversion as the primary performance drag. Leverage decay in leveraged ETFs has become a focus area. Volatility clustering shows distinct patterns between overnight and intraday movements. The 2025 DFAST stress scenarios are projecting less severe conditions than prior years.
</think>

# Critical Gaps in Your Risk Management & Position Sizing Wiki

Based on the search results and current date context, here are the highest-priority missing elements:

## 1. CRITICAL CONCEPTS NOT COVERED (Trading-Essential)

**Risk Measurement & Metrics:**
- **Value-at-Risk (VaR)** — Foundational risk metric estimating maximum loss at a confidence level (95%, 99%). Traders need three methods: historical simulation, parametric, and Monte Carlo. Essential baseline for regulatory compliance and position sizing decisions.[1][8]
- **Conditional Value-at-Risk / Expected Shortfall (CVaR)** — Measures average loss in the worst-case scenarios. Outperforms variance-based optimization in tail risk management, especially for extreme events. Increasingly preferred over standard VaR by institutional traders.[9][9]
- **Sharpe Ratio, Sortino Ratio, Calmar Ratio** — Risk-adjusted return metrics. Sortino corrects Sharpe's flaw of penalizing upside volatility. Critical for comparing strategy efficiency across different market conditions.[18]

**Position Sizing Alternatives:**
- **Optimal F (Ralph Vince)** — Maximizes returns regardless of drawdown severity. Different philosophy from Kelly; useful for comparing against Kelly's more conservative approach.[10]
- **Volatility-Based Position Sizing (ATR/Percent Volatility Model)** — Adjusts trade size dynamically based on current market volatility rather than fixed percentages. Particularly important in crypto and high-volatility assets.[6]

**Portfolio Management Frameworks:**
- **CPPI (Constant Proportion Portfolio Insurance) & TIPP (Time-Invariant Portfolio Protection)** — Dynamic hedging strategies that automatically reduce risky exposure as losses mount while preserving upside. Growing adoption among affluent portfolios.[11][12]
- **Risk Parity** — Allocates capital based on risk contribution rather than dollar amounts. Bridgewater's All Weather portfolio is the canonical example. Contradicts traditional 60/40 thinking.[16][36]
- **Volatility Targeting** — Adjusts portfolio leverage to maintain constant volatility over time. Reduces drawdowns in volatile periods, increases exposure in calm markets.

**Drawdown & Recovery:**
- **Drawdown Analysis & Recovery Math** — The compounding math showing -50% drawdown requires +100% gain to recover. Maximum drawdown duration, peak-to-trough timing as key risk metrics. Morgan Stanley research shows dramatic differences in recovery times across stock drawdown severity.[4][17][32]

**Risk Management Under Specific Conditions:**
- **Tail Risk Hedging** — Using derivatives (puts, options collars, inverse ETFs) to protect against tail events without permanently exiting positions. Cost vs. benefit tradeoffs.[20]
- **Regime Detection & Dynamic Allocation** — Identifying current economic regime to adjust factor exposures and asset weights. Research by Harvey et al. (March 2025) shows regime-based factor timing can raise information ratio from 0.05 to 0.4.[15]
- **Protective Puts as Insurance** — Specific pricing, timing, and cost analysis for buying puts during low IV periods vs. expensive protection during crisis.

**Model Validation & Testing:**
- **Walk-Forward Testing** — Out-of-sample testing beyond backtesting that reveals parameter stability and real-world robustness. Essential before deploying live strategies. Tests in rolling windows with in-sample/out-of-sample splits.[33]
- **Stress Testing & Scenario Analysis** — Regulatory requirement (DFAST/CCAR) showing how portfolios behave in adverse macroeconomic conditions. 2025 scenarios show less severity than 2024.[22]

**Behavioral & Implementation:**
- **Behavioral Biases in Risk Management (2025)** — Loss aversion causes ~9% return drag, herd behavior ~7%. Decision support matrices and pre-commitment strategies mitigate emotional capitulation during drawdowns.
- **Dynamic Portfolio Rebalancing** — Threshold-based (drift triggers at 5% deviation) vs. time-based (quarterly). 29-year study shows quarterly rebalancing keeps drift to 1.3% vs. 12.6% for unrebalanced portfolios.[21]
- **Leverage Risk Management** — Margin requirements, maintenance ratios, liquidation cascade mechanics. Position sizing for leveraged products differs fundamentally from unleveraged.[13]

**Tail Dependence & Systemic Risk:**
- **Copulas & Tail Dependence** — Mathematical framework for modeling joint default risk and correlation breakdown during crises. Especially relevant for multi-asset portfolios.
- **Volatility Clustering (Overnight vs. Intraday)** — Recent research shows overnight volatility clustering is stronger than intraday, with distinct risk premiums. Changes portfolio construction for 24-hour markets.[50]

---

## 2. KEY PEOPLE & FRAMEWORKS NOT MENTIONED

**Academic Figures to Profile:**
- **Robert C. Merton** — Merton's Portfolio Problem (continuous-time optimization, Merton's fraction for optimal stock allocation)[23]
- **Fischer Black & Robert Litterman** — Black-Litterman model (equilibrium-based portfolio optimization incorporating investor views)[24]
- **Harry Markowitz** — Modern Portfolio Theory, efficient frontier, foundational to all position sizing[25]
- **Ralph Vince** — Optimal F framework, alternative to Kelly for traders focused on maximum growth[10]
- **Frank Sortino** — Sortino ratio, downside-only volatility focus[18]
- **Ray Dalio** — All Weather portfolio, risk parity pioneer[36]

---

## 3. TOOLS & DATA SOURCES MISSING

**Institutional-Grade Risk Platforms:**
- **RiskMetrics** — Industry standard for portfolio risk analysis; produces VAR, CVaR, diversification benefit, concentration metrics. Used by major banks and hedge funds.[38]
- **Bloomberg PORT Function** — Aggregates positions across brokers, provides Greeks analysis, factor navigator, risk scenarios.[39]
- **FactSet Risk Analytics** — Multi-asset class risk modeling, customizable models[40]
- **MSCI Barra** — Integrated model suite for equity, fixed income, multi-asset risk[42]
- **Morningstar Global Risk Model** — Forward-looking risk and return estimates, correlation analysis[41]
- **AlternativeSoft** — Specialized drawdown analysis, underwater curves, real-time alerts across fund universes[4]
- **Limina IMS** — Risk analysis and exposure tools for RIAs[2]

**Emerging Tooling:**
- **Walk-forward testing software** (integrated into most backtesting platforms post-2024)
- **Regime detection algorithms** (increasingly embedded in portfolio management systems)

---

## 4. RECENT DEVELOPMENTS (2024-2026) TO DOCUMENT

**Regulatory:**
- **AI/ML Model Risk Management Framework (2024-2025)** — ECB, PRA (UK), RBI (India), and Singapore's MAS all released guidelines requiring governance, validation, and bias detection for AI-driven portfolio models. 82% of institutions now using risk tiering in MRM frameworks.[34]
- **SEC Form N-PORT Monthly Reporting (Nov 2025)** — Triples data frequency from quarterly to monthly, effective 60 days after month-end. Changes how funds disclose liquidity risk.[45]
- **2025 DFAST Stress Testing Scenarios** — Moderately less severe than 2024, showing projected loan losses $25B lower, CRE loss rates declining to 6.2% vs. 8.6%.

**Research & Strategy Evolution:**
- **Regime-Based Factor Timing (March 2025, Harvey et al.)** — Using historical economic similarity to identify bull/bear regimes for individual factors. Raises information ratio to 0.4 vs. 0.05 equal-weight baseline. Integrates into Black-Litterman framework.[15]
- **Dynamic Factor Rotation Adoption (2024-2026)** — iShares DYNF, Invesco, and BlackRock scaling dynamic factor rotation ETFs. Performance varies by factor construction (value-weighting vs. equal-weighting), momentum remains crash-prone (-88% drawdowns), but risk-managed momentum (RM_MOM) achieves 18% annualized returns with half the drawdown.[19]
- **Volatility Clustering Divergence (2024-2025)** — Research separates overnight and intraday volatility risk premiums; overnight clustering stronger, intraday/overnight cross-effects weak. Impacts round-the-clock portfolio construction.[50]
- **Behavioral Bias Quantification (2025)** — Loss aversion ranked as highest drag (~9%), followed by herd behavior (7%), overconfidence (6%), recency bias (5%). Pre-commitment frameworks (decision support matrices) measurably improve outcomes.

**Market/Structural:**
- **Leverage Decay in Leveraged ETFs (2024-2026)** — Underperformance due to daily rebalancing; research clarifying mechanics and mitigation strategies.[47]
- **Tax-Efficient Risk Management Framework Maturity (2025-2026)** — Tax-loss harvesting, secured borrowing, account location strategy becoming core to "after-tax alpha" conversation.
- **Correlation Regime Shifts (2024-2026)** — Historical years resembling 2024 (1954, 1955, 1958, 1995, 2013, 2017, 2021) showed average forward returns of 6.2%; helps contextualize regime transitions.[26]

---

## 5. TOP-PRIORITY GAPS TO ADDRESS FIRST (Ranked by Trader Impact)

1. **VaR & CVaR (Expected Shortfall)** — Without these, position sizing lacks quantitative grounding
2. **Drawdown Analysis & Recovery Math** — Directly informs risk tolerance and position sizing decisions  
3. **Volatility Targeting** — Increasingly core to modern portfolio management (2024-2026 adoption surge)
4. **Regime Detection** — Explains why Kelly/fixed allocations underperform in regime shifts
5. **Walk-Forward Testing** — Essential before deploying any strategy live
6. **CPPI/TIPP** — Portfolio insurance mechanisms becoming standard for affluent investors
7. **Optimal F vs. Kelly Tradeoff** — Completes the position-sizing philosophy spectrum
8. **Behavioral Biases in Risk Management** — Why discipline beats analytics in drawdowns
9. **Protective Puts & Tail Hedging** — Practical implementation of tail risk management
10. **Dynamic Rebalancing Thresholds** — Operationalizes theoretical portfolio optimization

---

## 6. SUGGESTED PAGE STRUCTURE ADDITIONS

```
risk-management-position-sizing/
├── var-cvar-expected-shortfall/
├── optimal-f-vs-kelly/
├── cppi-tipp-portfolio-insurance/
├── volatility-targeting/
├── regime-detection-dynamic-allocation/
├── drawdown-recovery-analysis/
├── walk-forward-testing/
├── risk-adjusted-metrics/ (Sharpe, Sortino, Calmar)
├── tail-hedging-puts-collars/
├── behavioral-risk-management/
├── dynamic-rebalancing-thresholds/
└── tools-platforms/ (RiskMetrics, Bloomberg PORT, FactSet, MSCI Barra)
```

---

**Note on Timeliness:** The March 2025 regime detection research and 2025 DFAST scenarios are particularly relevant *now* for 2026 planning. AI/ML governance is a live regulatory concern as of your wiki's current scope.

---

## Citations

1. https://pooya.blog/blog/portfolio-risk-var-cvar-kelly-criterion-2026/
2. https://www.investmentnews.com/glossary/risk-management-tools/263189
3. https://blog.quantinsti.com/position-sizing/
4. https://www.alternativesoft.com/drawdown-analysis-hedge-fund-software.html
5. https://www.invesco.com/content/dam/invesco/apac/en/pdf/insights/2024/january/invesco-dynamic-asset-allocation-jan-2024.pdf
6. https://www.quantifiedstrategies.com/volatility-based-position-sizing/
7. https://riskonnect.com/reporting-analytics/monte-carlo-analysis-a-powerful-tool-for-risk-management/
8. https://www.switchmarkets.com/tools/value-at-risk-calculator
9. https://www.man.com/insights/covering-your-tail-expected-shortfall
10. https://www.youtube.com/watch?v=CNKjRB-uwZQ
11. https://en.wikipedia.org/wiki/Constant_proportion_portfolio_insurance
12. https://quantpedia.com/time-invariant-portfolio-protection/
13. https://tradefundrr.com/risk-management-for-leveraged-products/
14. https://corporatefinanceinstitute.com/resources/derivatives/hedge-ratio/
15. https://alphaarchitect.com/regime-detection/
16. https://www.riskparityradio.com/portfolios
17. https://www.morganstanley.com/im/publication/insights/articles/article_drawdownsandrecoveries_ltr.pdf
18. https://www.xbto.com/resources/sharpe-sortino-and-calmar-a-practical-guide-to-risk-adjusted-return-metrics-for-crypto-investors
19. https://www.assenagon.com/en/1/service/newsroom/detail/factor-investing-analysis-reveals-2024-breaks-with-conventional-wisdom
20. https://www.pimco.com/us/en/resources/education/manage-risks-using-tail-risk-hedging
21. https://www.fortraders.com/blog/dynamic-portfolio-rebalancing-explained
22. https://ncua.gov/regulation-supervision/regulatory-compliance-resources/capital-planning-stress-testing-resources/2024-stress-testing-scenario-summary
23. https://en.wikipedia.org/wiki/Merton's_portfolio_problem
24. https://en.wikipedia.org/wiki/Black%E2%80%93Litterman_model
25. https://verumpartnership.com/understanding-the-efficient-frontier-in-portfolio-construction/
26. https://advisoranalyst.com/2025/01/17/correlation-comparison-years-that-resemble-2024.html/
27. https://www.robeco.com/en-int/insights/2024/10/fama-french-5-factor-model-five-major-concerns
28. https://arxiv.org/abs/2406.00610
29. https://www.edps.europa.eu/system/files/2025-11/2025-11-11_ai_risks_management_guidance_en.pdf
30. https://arxiv.org/abs/2411.09899
31. https://kpmg.com/kpmg-us/content/dam/kpmg/frv/pdf/2024/handbook-derivatives-hedging-accounting.pdf
32. https://www.edgeful.com/blog/posts/what-is-drawdown-in-trading
33. https://www.youtube.com/watch?v=QmVEYfIIh00
34. https://www.pwc.com/cz/cs/temata/MRM-Survey-Report-2024.pdf
35. https://tradewiththepros.com/trading-software-comparison/
36. https://www.bridgewater.com/research-and-insights/the-all-weather-story
37. https://journals.co.za/doi/10.10520/ejc-nm_monm_v2024_n2_a10
38. https://www.msci.com/documents/10199/248121/RiskMetrics_Risk_Reporting_for_Individual_Investor_Portfolios.pdf
39. https://www.youtube.com/watch?v=LW3HpWyhQzc
40. https://www.factset.com/solutions/portfolio-analytics/risk-analytics
41. https://www.morningstar.com/business/insights/blog/portfolio-risk-exposure
42. https://www.msci.com/www/fact-sheet/barra-integrated-model-ii/0161850015
43. https://www.metatradingclub.com/position-sizing-top-4-strategies-2024-guide/
44. https://www.gemini.com/cryptopedia/what-is-a-limit-order
45. https://www.sec.gov/newsroom/press-releases/2024-110
46. https://privatebank.jpmorgan.com/apac/en/insights/markets-and-investing/case-studies/reducing-the-risk-of-a-concentrated-single-stock-position-without-outright-sale
47. https://www.crystalfunds.com/insights/leveraged-etfs-decay-understanding-mechanics-and-risks
48. https://cryptocrewuniversity.com/position-sizing-7-powerful-strategies-for-crypto-trading-success-in-2024/
49. https://thebahnsengroup.com/dividend-cafe/rebalancing-because-something-always-underperforms-january-30-2026/
50. https://harbourfrontquant.substack.com/p/volatility-risk-premium-and-clustering
