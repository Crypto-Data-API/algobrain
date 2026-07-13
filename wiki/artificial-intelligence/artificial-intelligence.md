---
title: "Artificial Intelligence"
type: overview
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [ai-trading, machine-learning, education]
related: ["[[ai-trading-overview]]", "[[ai-agent-tokens]]", "[[ai-trading-agents]]", "[[llm-market-analysis]]", "[[defai]]", "[[ai-narrative-arc]]", "[[foundation-models]]", "[[decentralized-ai]]", "[[tokenized-compute]]", "[[zkml]]", "[[on-chain-inference]]", "[[ai-oracles]]", "[[ai-mev]]", "[[ai-agent-daos]]", "[[data-daos]]", "[[ai-solvers]]", "[[ai-prediction-markets]]", "[[restaking-and-ai]]", "[[proof-of-humanity]]", "[[llm-defi-interfaces]]", "[[ai-liquidity-management]]", "[[ai-governance-attacks]]", "[[ml-defi-risk-models]]", "[[truth-terminal-goat]]", "[[model-context-protocol]]", "[[agentic-commerce]]", "[[statistical-proof-of-execution]]", "[[content-authenticity]]"]
---

# Artificial Intelligence

This section covers the artificial intelligence landscape as it intersects with trading and financial markets — from [[history-of-ai|foundational history]] through [[foundation-models|modern models]], the companies building them, the frameworks enabling autonomous agents, the crypto tokens betting on decentralized AI, and the concepts shaping how AI transforms market participation. It is a **hub page**: the tables below are an index, each row pointing to a dedicated page or sub-hub. Three sibling sections carry the applied detail — [[machine-learning|Machine Learning]] for the modelling foundations, [[ai-trading-overview|AI Trading]] for bots, signals, and data providers, and [[decentralized-ai|Decentralized AI]] for the crypto-native expression. This page ties them together and routes you to the right level of depth.

## Map of This Section

The fastest way to orient. Each sub-hub below is itself a curated index page; start at the one matching your goal.

| Sub-hub | Covers | Best entry point |
|---------|--------|------------------|
| AI Fundamentals | History, types, neural nets, the ML→DL→foundation-model hierarchy | [[history-of-ai]], [[types-of-ai]] |
| [[machine-learning-overview\|Machine Learning]] | The three learning paradigms, validation, ensembles | [[machine-learning]] |
| [[deep-learning-overview\|Deep Learning]] | CNNs, RNNs, attention, generative architectures | [[deep-learning-overview]] |
| [[nlp-overview\|NLP]] | Text → trading signal pipeline | [[nlp-overview]] |
| [[computer-vision-overview\|Computer Vision]] | Charts, satellite, OCR, multimodal | [[computer-vision-overview]] |
| [[generative-ai-overview\|Generative AI]] | LLMs, agents, multimodal, code generation | [[agentic-ai]] |
| [[ai-research-overview\|Research & Benchmarks]] | Papers, benchmarks, labs, conferences | [[landmark-ai-papers]] |
| [[ethics-safety-overview\|Ethics & Governance]] | Bias, explainability, regulation as catalysts | [[ai-regulation-global]] |
| [[ai-security-overview\|AI Security]] | Adversarial, poisoning, prompt injection | [[prompt-injection]] |
| [[ai-trading-overview\|AI Trading]] | Bots, ML signals, backtesting, data providers | [[ai-trading-overview]] |
| [[decentralized-ai\|AI × Crypto]] | DePIN compute, on-chain inference, agent tokens | [[ai-agent-tokens]] |

### How to Navigate — Reading Paths

| If you want to… | Start with | Then |
|-----------------|-----------|------|
| Understand AI from scratch | [[history-of-ai]] → [[types-of-ai]] → [[neural-networks]] | [[machine-learning]] |
| Build a trading model | [[machine-learning]] → [[cross-validation-trading]] | [[ai-trading-overview]], and the disciplined [[hypothesis-to-backtest-workflow]] |
| Use LLMs for research/text | [[nlp-overview]] → [[llm-market-analysis]] | [[prompt-engineering-trading]], [[retrieval-augmented-generation]] |
| Invest in the AI theme | [[ai-applications-overview]] → [[generative-ai-economics]] | [[ai-narrative-arc]], [[nvidia-ai]] |
| Trade AI crypto tokens | [[decentralized-ai]] → [[ai-agent-tokens]] | [[defai]], [[truth-terminal-goat]] |
| Manage AI risk in your stack | [[ai-security-overview]] → [[prompt-injection]] | [[hallucinations-ai]], [[ai-security-trading]] |

---

## AI Fundamentals

Start here for foundational knowledge:

| Page | What You'll Learn |
|------|------------------|
| [[history-of-ai]] | 1940s to present — Turing, neural nets, AI winters, transformers, ChatGPT |
| [[types-of-ai]] | Narrow vs general vs super AI; supervised, unsupervised, reinforcement learning |
| [[neural-networks]] | How artificial neurons learn — the building block of all modern AI |
| [[machine-learning-vs-deep-learning]] | The hierarchy: ML → deep learning → foundation models |
| [[natural-language-processing]] | How machines understand text — the core of financial AI |
| [[computer-vision-trading]] | Chart recognition, satellite imagery, multimodal AI |
| [[ai-winters]] | The boom/bust pattern in AI — and whether we're heading for another |
| [[turing-test]] | Can machines think? And does it matter for trading? |

---

## Companies & Labs

| Company | Key Product | Trading Role |
|---------|------------|-------------|
| [[anthropic]] | Claude (Opus, Sonnet, Haiku) | This wiki's engine; code generation, research |
| [[openai]] | GPT-4, ChatGPT | Most widely adopted LLM for finance |
| [[google-deepmind]] | Gemini | Multimodal analysis, Google Cloud AI |
| [[meta-ai]] | LLaMA (open-weight) | Local deployment, [[fine-tuning-llms|fine-tuning]] |
| [[mistral-ai]] | Mistral, Mixtral | Efficient inference, European AI |
| [[nvidia-ai]] | H100/B200 GPUs | Hardware backbone of all AI |
| [[hugging-face]] | Model Hub, Transformers | Open-source AI distribution |

## Machine Learning

| Page | What You'll Learn |
|------|------------------|
| [[machine-learning-overview]] | Hub — the three paradigms, key models, five pitfalls |
| [[supervised-learning]] | Learning with labels — classification, regression, XGBoost, FinBERT |
| [[unsupervised-learning]] | Pattern discovery — clustering, PCA, anomaly detection, regime detection |
| [[reinforcement-learning]] | Learning by trial and error — DQN, PPO, SAC for execution and market making |
| [[bias-variance-tradeoff]] | Underfitting vs overfitting — the core tension in trading ML |
| [[cross-validation-trading]] | Walk-forward validation — why standard CV fails for financial data |
| [[ensemble-methods]] | Bagging, boosting, stacking — why XGBoost and Random Forest dominate |
| [[hyperparameter-tuning]] | Tuning model settings without overfitting |

---

## Deep Learning & Neural Networks

| Page | What You'll Learn |
|------|------------------|
| [[deep-learning-overview]] | Hub — architecture map, when DL beats traditional ML |
| [[convolutional-neural-networks]] | CNNs for chart patterns, satellite imagery, visual data |
| [[recurrent-neural-networks]] | RNNs & LSTMs for time-series forecasting |
| [[attention-mechanism]] | The core innovation powering all modern LLMs |
| [[generative-adversarial-networks]] | GANs for synthetic data generation |
| [[diffusion-models]] | Denoising diffusion for high-quality data generation |
| [[autoencoders]] | Compression, anomaly detection, denoising |

Also see: [[transformer-architecture]] (in Core Concepts), [[neural-networks]] (in Fundamentals)

---

## Natural Language Processing

| Page | What You'll Learn |
|------|------------------|
| [[nlp-overview]] | Hub — the full NLP pipeline from raw text to trading signal |
| [[tokenization-nlp]] | How LLMs read text — BPE, context windows, API pricing |
| [[word-embeddings]] | Word2Vec to contextual embeddings — how meaning becomes math |
| [[named-entity-recognition]] | Extracting companies, amounts, dates from financial text |
| [[text-preprocessing-finance]] | Cleaning SEC filings, earnings calls, social media |
| [[text-classification-finance]] | Beyond sentiment — event type, urgency, hawkish/dovish |
| [[chatbot-architectures]] | Conversational AI from rule-based to LLM-powered |
| [[speech-and-audio-ai]] | Whisper, ElevenLabs, earnings call audio analysis |

Also see: [[nlp-sentiment-analysis]], [[finbert]], [[llm-market-analysis]], earnings-call-analysis in AI Trading

---

## Computer Vision

| Page | What You'll Learn |
|------|------------------|
| [[computer-vision-overview]] | Hub — core CV tasks, model evolution, multimodal convergence |
| [[object-detection]] | YOLO, Faster R-CNN — satellite parking lots, shipping ports |
| [[image-segmentation]] | Pixel-level analysis — oil tank fill, crop health, SAM |
| [[image-generation-ai]] | Stable Diffusion, DALL-E — synthetic charts, deepfake detection |
| [[optical-character-recognition]] | OCR for financial docs, screenshots, multimodal LLM replacement |
| [[video-analysis-trading]] | Foot traffic, supply chain monitoring, broadcast analysis |

Also see: [[computer-vision-trading]] (in Fundamentals), [[cnn-chart-recognition]] (in AI Trading)

---

## Knowledge Representation & Reasoning

| Page | What You'll Learn |
|------|------------------|
| [[knowledge-reasoning-overview]] | Hub — symbolic vs statistical AI, why KR&R still matters |
| [[logic-based-ai]] | Propositional, predicate, fuzzy, temporal logic for trading rules |
| [[expert-systems]] | If-then rule engines — the 1980s AI that persists in risk & compliance |
| [[ai-planning]] | Goal-directed action sequences — rebalancing, execution, tax harvesting |
| [[knowledge-graphs-finance]] | Entity-relationship networks — supply chains, corporate ownership, event propagation |
| [[ontologies-taxonomies]] | FIBO, ISDA CDM — formal schemas for financial instruments and data |
| [[neuro-symbolic-ai]] | Combining LLMs with logic — explainable, constrained, trustworthy trading AI |

---

## Search & Optimisation

| Page | What You'll Learn |
|------|------------------|
| [[search-optimisation-overview]] | Hub — search spaces, objective functions, which algorithm for which problem |
| [[graph-search-algorithms]] | A*, Dijkstra, BFS — order routing, arbitrage cycle detection, graph traversal |
| [[evolutionary-algorithms]] | Genetic algorithms, GP, CMA-ES, NSGA-II — strategy discovery, multi-objective portfolio optimisation |
| [[swarm-intelligence]] | PSO, ant colony — portfolio weights, feature selection, multi-agent optimisation |
| [[simulated-annealing]] | Temperature-based search — escaping local optima in noisy trading landscapes |
| [[bayesian-optimisation]] | GP-guided search — efficient hyperparameter tuning with expensive backtests |
| [[constraint-optimisation]] | LP, QP, MILP — Markowitz portfolio, execution scheduling, margin optimisation |

---

## Robotics & Embodied AI

| Page | What You'll Learn |
|------|------------------|
| [[robotics-overview]] | Hub — investable sectors, bull/bear case, picks-and-shovels plays |
| [[autonomous-vehicles]] | Self-driving: SAE levels, Tesla vs Waymo, vision vs lidar, trading angles |
| [[motion-planning]] | Path generation: RRT, lattice planners, end-to-end learning, trading execution parallel |
| [[sensor-fusion]] | Cameras + lidar + radar: how robots perceive, multi-source data analogy for trading |
| [[sim-to-real]] | Training in simulation: reality gap, domain randomisation, backtesting parallel |
| [[humanoid-robots]] | Tesla Optimus, Figure AI — the $30T labour market disruption thesis |

---

## AI Applications by Industry

| Page | Sector | Key Investment Angle |
|------|--------|---------------------|
| [[ai-applications-overview]] | Hub | Cross-industry AI adoption map, platform shift, data moats |
| [[ai-healthcare]] | Healthcare ($4T) | Drug discovery (RXRX, SDGR), diagnostics, AlphaFold |
| [[ai-finance]] | Finance ($26T) | Banking, insurance, lending, compliance — beyond trading |
| [[ai-gaming]] | Gaming ($200B) | NPC AI, procedural content, RL research, NVIDIA convergence |
| [[ai-science]] | Science | AlphaFold, materials discovery, weather forecasting, fusion |
| [[ai-creative]] | Creative ($2.4T) | Image/video generation, copyright battles, ADBE/META |
| [[ai-cybersecurity]] | Cybersecurity ($200B) | Threat detection, AI arms race, CRWD/PANW/S |
| [[ai-education]] | Education ($6T) | AI tutoring, the Chegg disruption cautionary tale |

---

## AI Ethics, Safety & Governance

| Page | What You'll Learn |
|------|------------------|
| [[ethics-safety-overview]] | Hub — why ethics directly affect valuations, the ethics-to-regulation pipeline |
| [[algorithmic-bias]] | How bias enters AI, high-profile incidents (Apple Card, Amazon hiring), bias in trading models |
| [[explainability-interpretability]] | SHAP, LIME, attention maps — why your model bought and how regulators require you to explain it |
| [[ai-governance-frameworks]] | NIST AI RMF, EU AI Act risk tiers, ISO 42001 — corporate AI risk management |
| [[ai-regulation-global]] | EU AI Act, US Executive Order, China rules — regulatory events as market catalysts |
| [[ai-environmental-impact]] | AI energy consumption, data centre power demand, nuclear for AI, investable themes |
| [[ai-labour-displacement]] | Which jobs AI replaces, margin expansion thesis, augmentation vs replacement |
| [[ai-intellectual-property]] | NYT v OpenAI, training data rights, who owns AI output, data licensing as new asset class |

Also see: [[ai-safety-alignment]], [[hallucinations-ai]], [[rlhf-constitutional-ai]] (in Core Concepts), [[ai-regulation-trading]] (in Trading Applications)

---

## AI Security

| Page | What You'll Learn |
|------|------------------|
| [[ai-security-overview]] | Hub — threat landscape, attack surface, defence principles |
| [[adversarial-attacks]] | Crafted inputs that fool models — FGSM, PGD, adversarial order flow |
| [[model-poisoning]] | Corrupting training data, backdoor attacks, data feed manipulation |
| [[prompt-injection]] | Hijacking LLM agents — direct/indirect injection, trading agent threats |
| [[model-theft-extraction]] | Cloning proprietary models through API queries, the alpha extraction paradox |
| [[data-privacy-ai]] | Training data memorisation, API vs self-hosted privacy, regulatory requirements |
| [[ai-security-trading]] | Complete threat model and defence checklist for trading AI systems |

---

## Generative AI

| Page | What You'll Learn |
|------|------------------|
| [[generative-ai-overview]] | Hub — the GenAI stack, generative vs discriminative AI |
| [[generative-ai-landscape]] | Market map: model providers, infrastructure, applications, where value accrues |
| [[agentic-ai]] | Autonomous agents: the agent loop, architectures (ReAct, multi-agent, reflexion) |
| [[multimodal-models]] | Vision-language-audio models: GPT-4o, Gemini, chart analysis, convergence trend |
| [[text-code-generation]] | Writing and coding with LLMs — the primary trading use case, Claude Code |
| [[synthetic-data-generation]] | GAN/diffusion/VAE for market data augmentation, stylised facts preservation |
| [[generative-ai-economics]] | Unit economics: training costs, inference pricing, ROI, build vs buy |

---

## Core Concepts

| Concept | What It Is |
|---------|-----------|
| [[foundation-models]] | Large pre-trained models (GPT-4, Claude, LLaMA) |
| [[transformer-architecture]] | The neural architecture powering all modern AI |
| [[retrieval-augmented-generation]] | Grounding LLM outputs in real documents |
| [[embeddings-vector-databases]] | Semantic search and document retrieval |
| [[prompt-engineering-trading]] | Crafting effective instructions for LLMs |
| [[fine-tuning-llms]] | Adapting models to financial domains |
| [[zero-shot-few-shot-learning]] | Using LLMs without custom training |
| [[rlhf-constitutional-ai]] | How models are aligned to be helpful and safe |
| [[hallucinations-ai]] | When LLMs fabricate information — critical risk |
| [[ai-safety-alignment]] | Ensuring AI systems behave as intended |
| [[model-inference-vs-training]] | GPU economics: who pays and how much |

## AI × Crypto Concepts

| Concept | What It Is |
|---------|-----------|
| [[decentralized-ai]] | Parent movement — compute, data, inference on open networks |
| [[tokenized-compute]] | DePIN economic model for GPU, bandwidth, storage |
| [[data-daos]] | Tokenized training data as an on-chain asset |
| [[on-chain-inference]] | Running ML models inside smart contracts |
| [[zkml]] | Zero-knowledge proofs for verifiable model outputs |
| [[statistical-proof-of-execution]] | SPEX — probabilistic verification as a practical ZKML alternative |
| [[ai-oracles]] | Prediction-as-a-service oracle networks |
| [[ai-mev]] | Machine learning applied to MEV extraction |
| [[ai-solvers]] | Intent-based routing and DeFi solver networks |
| [[ai-liquidity-management]] | ML-managed concentrated liquidity on DEXes |
| [[ml-defi-risk-models]] | Professional ML risk curators for lending protocols |
| [[ai-prediction-markets]] | Autonomous agents and LLM resolvers in prediction markets |
| [[ai-agent-daos]] | DAOs governed or operated by autonomous agents |
| [[ai-governance-attacks]] | LLM-era attack surface on DAO governance |
| [[llm-defi-interfaces]] | Natural-language chat frontends for DeFi (Tier 1 DeFAI) |
| [[model-context-protocol]] | MCP — protocol standard for LLM tool integration |
| [[agentic-commerce]] | Autonomous agents purchasing and settling on behalf of users |
| [[content-authenticity]] | C2PA / CAI — cryptographic provenance for AI-generated media |
| [[restaking-and-ai]] | Cryptoeconomic security for AI services via EigenLayer AVSs |
| [[proof-of-humanity]] | Sybil resistance in a world of cheap AI-generated accounts |
| [[truth-terminal-goat]] | The October 2024 narrative catalyst for the AI agent cycle |
| [[defai]] | DeFi-specific expression of decentralized AI |

## AI Research & Benchmarks

| Page | What You'll Learn |
|------|------------------|
| [[ai-research-overview]] | Hub — research-to-market pipeline, why traders should follow papers |
| [[landmark-ai-papers]] | The 20 papers that shaped modern AI — Attention, GPT-3, AlphaFold, LoRA, scaling laws |
| [[ai-benchmarks]] | MMLU, HumanEval, HellaSwag — what benchmark scores mean, financial benchmarks |
| [[ai-evaluation-metrics]] | Accuracy, F1, precision/recall, Sharpe — model metrics vs trading metrics gap |
| [[ai-research-labs]] | Who publishes breakthroughs — lab profiles, talent tracking as market signal |
| [[ai-conferences]] | NeurIPS, ICML, ACL — conference calendar as catalyst calendar |
| [[financial-ml-papers]] | López de Prado, FinBERT, deflated Sharpe — the essential trading ML canon |

---

## Agent Frameworks

| Framework | Focus | Language |
|-----------|-------|---------|
| [[eliza-framework]] | Crypto-native AI agents | TypeScript |
| [[crewai]] | Multi-agent orchestration | Python |
| [[langchain]] | LLM application framework + LangGraph | Python |

## Tools & Frameworks

| Page | What You'll Learn |
|------|------------------|
| [[tools-frameworks-overview]] | Hub — the AI engineering stack, choosing the right tool |
| [[pytorch]] | Deep learning framework: dominant for research and production, PyTorch ecosystem |
| [[tensorflow]] | Google's framework: TF Serving, TFLite, when to choose TF over PyTorch |
| [[scikit-learn]] | Traditional ML toolkit: XGBoost/RF API, pipelines, the trading workhorse |
| [[mlops]] | ML operations lifecycle: data → train → deploy → monitor → retrain |
| [[experiment-tracking]] | MLflow, W&B — logging runs, the experiment audit trail |
| [[model-deployment]] | Serving models: batch/online/streaming, FastAPI + Docker, latency budgets |
| [[ml-development-environments]] | Jupyter, VS Code, Colab, Cursor — where you build trading AI |

---

## Decentralized AI Projects

| Project | Token | Focus |
|---------|-------|-------|
| [[bittensor-subnets|Bittensor]] | TAO | Decentralized AI/ML network |
| [[ritual-network|Ritual]] | — | On-chain AI inference |
| [[io-net|io.net]] | IO | Decentralized GPU compute |
| [[ai16z-dao|ai16z]] | AI16Z | AI-managed investment DAO |
| [[morpheus]] | MOR | Fair-launched agent platform on Arbitrum |
| [[olas]] | OLAS | Autonomous service protocol (Open Autonomy) |
| [[gensyn]] | — | Distributed ML training (pre-launch) |
| [[prime-intellect]] | — | Distributed training and decentralized RL |
| [[zero-gravity|0G]] | 0G | Modular AI-native storage + DA + compute |

See [[ai-agent-tokens]] for the full landscape of 127 AI-related tokens, [[decentralized-ai]] for the unifying framework, and [[tokenized-compute]] for the economic model behind the compute layer.

## Trading Applications

| Application | Page |
|-------------|------|
| [[ai-market-making]] | AI for dynamic liquidity provision |
| [[ai-portfolio-risk]] | AI for portfolio construction and risk |
| [[ai-regulation-trading]] | Regulatory landscape for AI in trading |
| [[ai-agent-strategies]] | Strategy categories using AI agents |

For ML models, bots, backtesting, and data providers → [[ai-trading-overview|AI Trading]] section.

## Philosophy & Foundations

| Page | What You'll Learn |
|------|------------------|
| [[philosophy-overview]] | Hub — why AI philosophy shapes valuations, regulation, and risk |
| [[defining-intelligence]] | What intelligence means — the moving goalpost problem |
| [[artificial-general-intelligence]] | AGI: timeline debate, scaling hypothesis, investment framework |
| [[consciousness-machine-intelligence]] | Can machines be conscious? Regulatory and market implications |
| [[chinese-room-argument]] | Understanding vs simulation — calibrating expectations for AI tools |
| [[existential-risk-ai]] | X-risk: alignment problem, control problem, the 2023 statement, market impact |
| [[philosophy-of-mind-ai]] | Functionalism, computationalism, embodied cognition — foundational assumptions |

Also see: [[turing-test]] (in Fundamentals), [[types-of-ai]] (in Fundamentals)

---

## History & Narrative

| Event | Significance |
|-------|-------------|
| [[chatgpt-moment]] | Nov 2022: the inflection point |
| [[open-source-ai-movement]] | LLaMA, Mistral, and the democratization of AI |
| [[ai-narrative-arc]] | 2024-2026: capability → mania → bust → utility |
| [[defai]] | DeFi + AI convergence |

## The Honest Assessment

AI is transforming trading infrastructure but not replacing human judgment. The most successful applications **augment** traders rather than replacing them. The wiki reflects this balanced view — covering both the genuine capabilities and the significant limitations documented through the [[ai-narrative-arc|2024-2026 hype cycle]].

Three cross-cutting cautions recur throughout this section and are worth holding in mind whatever sub-page you read:

| Caution | Where it bites | See |
|---------|----------------|-----|
| Overfitting / data-snooping | ML models that look great in backtest and fail live | [[bias-variance-tradeoff]], [[cross-validation-trading]], [[hypothesis-to-backtest-workflow]] |
| Hallucination & ungrounded output | LLMs fabricating numbers, citations, or facts in research | [[hallucinations-ai]], [[retrieval-augmented-generation]] |
| Narrative / valuation risk | AI-themed equities and tokens priced on hype, not cash flows | [[ai-narrative-arc]], [[generative-ai-economics]] |

## Related

- [[machine-learning]] — the modelling foundation underneath most of this section
- [[ai-trading-overview]] — applied bots, signals, backtesting, and data providers
- [[decentralized-ai]] — the crypto-native expression of AI
- [[foundation-models]] / [[transformer-architecture]] — the core modern architectures
- [[ai-narrative-arc]] — the 2024-2026 capability → mania → bust → utility cycle

## Sources

General market knowledge; no specific wiki source ingested yet. Individual sub-pages carry their own sources where source material has been ingested.
