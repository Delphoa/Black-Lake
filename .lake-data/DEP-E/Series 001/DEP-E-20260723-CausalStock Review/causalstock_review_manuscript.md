---
title: "CausalStock Review - DEP-E"
generated_at: "2026-07-23 (public-safe date marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of CausalStock for news-driven multi-stock movement prediction."
source_status: "verified private PDF and full-paper HTML; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-23"
temporal_cutoff: "arXiv v1 and NeurIPS 2024 proceedings record; sources checked through the public date marker"
primary_url: "https://arxiv.org/abs/2411.06391"
stable_identifier: "arXiv:2411.06391v1; DOI 10.48550/arXiv.2411.06391; proceedings DOI 10.52202/079017-1504"
confidence_summary: "High for identity and source transcription; medium for comparative interpretation; low for causal validity and independent reproducibility."
safety_scope: "research review, synthetic evaluation, offline replication, and non-advisory financial analysis"
distribution_notes: "Source files remain private and local; generated public-safe Markdown only."
---

# CausalStock Review - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | CausalStock arXiv record | Primary metadata | HTML | arXiv:2411.06391v1 | https://arxiv.org/abs/2411.06391 | Record links a Creative Commons license; metadata only | 2026-07-23 | Inspected live and from verified private metadata copy |
| S2 | CausalStock complete paper | Primary artifact | PDF and full-paper HTML | v1; 17 pages | https://arxiv.org/pdf/2411.06391; https://arxiv.org/html/2411.06391 | Verified private copies inspected and withheld | 2026-07-23 | Fully inspected, rendered, and integrity-verified |
| S3 | NeurIPS proceedings record | Official venue | HTML, PDF, supplemental | NeurIPS 2024 Main Track; DOI 10.52202/079017-1504 | https://proceedings.neurips.cc/paper_files/paper/2024/hash/54d689d58fe54c92aee2d732fc49fca8-Abstract-Conference.html | Official proceedings metadata | 2026-07-23 | Inspected live |
| S4 | CausalTAD Trajectory DEP | Related Black Lake artifact | Markdown | DEP-E-20260711 | `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md` | Repository context only | 2026-07-23 | Inspected |
| S5 | Quantum Quant Trading DEP | Related Black Lake artifact | Markdown | DEP-E-20260714 | `.lake-data/DEP-E/DEP-E-20260714-Quantum Quant Trading/quantum_quant_trading_manuscript.md` | Repository context only | 2026-07-23 | Inspected |
| S6 | PAC Confidence DEP | Related Black Lake artifact | Markdown | DEP-E-20260713 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Repository context only | 2026-07-23 | Inspected |
| S7 | Selection, dedup, and integrity evidence | Processing evidence | Public-safe summary | 75,310 final eligible units | This manuscript, Methodology and Appendix | No private path or exact local execution timestamp | 2026-07-23 | Generated and validated |

Paper metadata:

- `Authors`: Shuqi Li, Yuebo Sun, Yuxin Lin, Xin Gao, Shuo Shang, Rui Yan.
- `Submitted`: 2024-11-10; one arXiv version exposed by the inspected record.
- `Venue`: Advances in Neural Information Processing Systems 37, NeurIPS 2024 Main Conference Track.
- `Subjects`: Machine Learning, Artificial Intelligence, Computational Engineering/Finance/Science, and Computation and Language.
- `Title note`: the proceedings title includes “Multi-stock”; the selected arXiv record uses “Stock”.
- `Source files deposited`: none; no `.source/` directory.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, date, v1, subjects, acceptance comment, arXiv DOI, license link | Bibliographic identity | High | Metadata alone cannot validate method or results |
| E2 | S2, Sections 3-4 | Primary full text | Temporal graph definition, sparse/knowledge prior, lag-dependent Bernoulli posterior, Gumbel-softmax sampling, FCM, ELBO+BCE objective | Core mechanism | High for transcription | Derivations not independently rederived; causal assumptions remain conditional |
| E3 | S2, Section 4.2 and Appendix A | Primary full text | Price features; LLM scores for correlation, sentiment, importance, impact, duration; prompt design | Denoised News Encoder | High for design | Exact model snapshot, inference settings, and generated score corpus unavailable |
| E4 | S2, Table 1 and Appendix C | Primary tables | Six datasets, chronological splits, baselines, ACC/MCC, 10 news-task runs and 5 price-task runs | Comparative performance | High for transcription | No raw predictions, seed list, confidence intervals, or independent rerun |
| E5 | S2, Table 2 | Primary table | TCD/news/link/lag/encoder ablations | Component contribution | High for reporting | Ablations remain within the authors' data and implementation |
| E6 | S2, Figure 3 and Table 5 | Primary figure/table | News-score examples; market-value/causal-strength correlations 0.6491-0.8909 | Explainability claims | Medium | Correlation and visualization do not validate causal direction |
| E7 | S2, Section 5.5 | Primary table and prose | Top-three equal-weight simulation; APV and Sharpe ratio on three datasets | Financial-transfer claim | Medium for reporting | Costs, slippage, impact, turnover, and walk-forward refresh not established |
| E8 | S2, Appendices B, E, F | Primary limitations | Causal assumptions; static graph and Bernoulli-edge limits; LLM human-values risk | Boundary conditions | High | Safety and governance treatment is brief |
| E9 | S3 | Official proceedings | Main-track venue, canonical proceedings title, DOI, supplemental link | Publication status | High | Publication does not imply reproducibility |
| E10 | S4-S6 | Related DEP artifacts | Causal identification, finance evidence, confidence/shift context | Cross-DEP synthesis | Medium | Related artifacts do not validate CausalStock |
| E11 | S7 | Process evidence | Fixed-pool uniform selection, dedup scans, repair receipt summary, public-output checks | Selection and integrity | High | Depends on repository and archive state at the public date marker |

## Executive Summary

CausalStock is a news-driven multi-stock movement classifier that learns a lag-dependent probabilistic graph over stocks and uses that graph to route price and news representations into next-day predictions. Its distinctive text component asks an LLM to convert each news item into five explicit scores—correlation to the stock, sentiment, importance, price impact, and impact duration—before embedding them. Its graph component models edge existence with a Bernoulli variational posterior that depends on the previous lag, then combines sampled edges and learned edge strengths inside a functional causal model.

The paper reports first-place ACC and MCC against its listed baselines on six datasets. The evidence is strongest as a comparative, historical benchmark result: chronological splits are documented, multiple runs are reported, and ablations show large degradation without temporal causal discovery. The evidence is weaker for the paper's causal language and financial transfer. All graph learning is observational and conditional on strong assumptions; no intervention or graph-recovery ground truth validates directionality. The portfolio simulation omits several costs and operational constraints.

Reviewer confidence is high that the paper, tables, figures, assumptions, and limitations were accurately inspected from complete sources. Confidence is low that results are independently reproducible because no author-identified implementation, LLM score corpus, raw predictions, or exact execution package was found in the bounded search. This artifact supports replication planning and evidence-gated prototyping, not investment advice or live trading.

## Detailed Summary

### Problem and Context

Multi-stock prediction uses relations between companies because price movements are not independent. Prior work often treats those relations as symmetric correlations or learned attention weights. CausalStock argues that many business relations are directional and lagged, and that noisy news makes textual evidence difficult to use reliably. It therefore combines temporal graph discovery with an explicit LLM-based news filter.

The target is binary rise/fall prediction for multiple stocks at a future trading day. Historical inputs cover the previous `L` trading days for `D` stocks. Each per-stock, per-day representation concatenates a price embedding and, when available, a news embedding.

### Denoised News Encoder

The price encoder embeds adjusted close, high, low, open, close, and volume. The Denoised News Encoder prompts an LLM to score a stock-news pair along five dimensions. Correlation, importance, impact, and duration range from 0 to 10; sentiment ranges from -1 to 1. The scores become an explicit five-dimensional representation before an embedding layer.

The primary result uses GPT-3.5. Ablations compare conventional and denoised uses of BERT, RoBERTa, FinBERT, FinGPT, and Llama. The denoised variants generally outperform the same family used as a conventional encoder, but the paper does not provide a complete immutable record of model version, sampling configuration, retry behavior, prompt outputs, or score-review policy.

### Lag-Dependent Temporal Graph

The temporal graph has shape `L x D x D`: an edge at lag `l` represents a directed influence from stock `j` at `T-l` to stock `i` at `T`. Because all arrows point forward in time, the authors do not add a contemporaneous DAG constraint. The graph prior combines Frobenius penalties for sparsity and distance from an optional domain-knowledge graph.

The posterior factorizes over stocks and lags. Edge-existence and edge-nonexistence logits are transformed with learnable MLPs that depend on the previous lag's logits, producing a lag-dependent Bernoulli probability. Gumbel-softmax supplies differentiable samples. A separate learned causal-weight graph provides edge strength.

The functional causal model aggregates price and news encodings only through sampled edges and weights, then applies a sigmoid classifier. The objective combines a variational evidence lower bound with binary cross-entropy. Appendix B states Causal Markov, minimality, structural identifiability, correct specification, causal sufficiency, and likelihood regularity assumptions.

### Data and Evaluation

The news-driven task uses ACL18 (88 U.S. stocks), CMIN-US (110 U.S. stocks), and CMIN-CN (300 Chinese stocks). The price-only task uses KDD17 (50 U.S. stocks), NI225 (51 Japanese stocks), and FTSE100 (24 U.K. stocks). Splits are chronological. The first three combine price with Twitter, Yahoo, or Wind text; the others contain engineered price features.

ACC and MCC are reported against HAN, StockNet, PEN, and CMIN for the news task, and LSTM, ALSTM, StockNet, Adv-ALSTM, and DTML for the price task. The implementation uses PyTorch on four Tesla V100 GPUs. Standard deviations are reported across 10 news-task runs and 5 price-task runs, but raw seeds and prediction files are unavailable.

### Results and Ablations

For news-driven prediction, CausalStock reports ACC/MCC of 63.42/0.2172 on ACL18, 54.64/0.0481 on CMIN-US, and 56.19/0.1417 on CMIN-CN. The strongest listed baselines report 62.69/0.2090, 53.43/0.0460, and 55.28/0.1110. These are positive but mostly modest ACC margins.

For price-only prediction, CausalStock reports 56.09/0.1235 on KDD17, 53.01/0.0640 on NI225, and 52.88/0.0534 on FTSE100. The strongest listed baselines report 53.53/0.0733, 52.76/0.0626, and 52.08/0.0502.

Removing TCD reduces news-task ACC to roughly 51 across all three datasets. Removing news, edge non-existence modeling, or lag dependence also reduces results. A variable-dependent edge model slightly exceeds the main model on ACL18 and CMIN-CN but not CMIN-US and increases complexity. The paper's own text therefore treats it as a possible extension requiring further validation.

### Explanation and Portfolio Evidence

The explanation layer shows structured LLM scores and heatmaps of learned causal strength. Table 5 reports Spearman correlations between market value and learned causal strength from 0.6491 to 0.8909 with listed p-values below 0.02. These are associations within model outputs, not proof of real-world causal influence; market value, coverage, volatility, sector, and data availability may all affect the pattern.

The portfolio simulation selects the top three predicted stocks each day with equal weights. CausalStock reports the largest listed APV and Sharpe ratio on ACL18, KDD17, and NI225. The evaluation is incomplete for deployment because it does not establish costs, slippage, market impact, turnover limits, taxes, survivorship handling, execution timing, or uncertainty-aware abstention.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Lag-dependent graph probabilities plus an FCM improve multi-stock prediction. | Author empirical claim | E2, E4, E5 | Ablations strongly support component value within the reported setup; no independent rerun. | High for reporting; low for reproduction |
| C2 | LLM-based denoised scores extract more useful financial news evidence than conventional encoders. | Author empirical claim | E3, E5 | Denoised variants generally lead matched conventional encoders, but prompt/model reproducibility is incomplete. | Medium-high |
| C3 | CausalStock outperforms listed baselines on all six datasets. | Author empirical claim | E4 | Directly supported by Table 1; margins and benchmark age should be considered. | High for transcription |
| C4 | The learned graph represents causal relations among stocks. | Author causal claim | E2, E6, E8 | Conditional on strong observational assumptions; no intervention or graph-ground-truth validation. | Low-medium |
| C5 | Market value is positively related to learned causal influence. | Author association claim | E6 | Reported correlations support association in model outputs, not causal explanation. | Medium |
| C6 | The model offers practical trading advantage. | Author transfer claim | E7 | Historical top-three simulation is incomplete without cost-aware, walk-forward evaluation. | Low |
| C7 | Static binary edges and LLM value alignment are material limitations. | Author limitation | E8 | Directly disclosed and important for deployment. | High |
| C8 | No author-identified public implementation was found. | Negative evidence | E1, E3, bounded search | Record and bounded searches found none; nonexistence is not proven. | Medium-high |
| C9 | The paper was uniformly selected and was not an owning duplicate. | Process claim | E11 | Fixed-pool draw and exact identity/slug/24-hour scans passed. | High |

## Methodology

- `Research objective`: preserve a schema-complete, source-first review that distinguishes reported predictive gains from causal, reproducibility, and financial-deployment claims.
- `Sources inspected`: verified complete private PDF; verified official full-paper HTML; private metadata HTML; live arXiv record; official NeurIPS proceedings record; rendered figures and tables; exactly three related DEP manuscripts.
- `Discovery strategy`: enumerate PDFs with `rg --files -g "*.pdf"`, group by unique parent directory, normalize arXiv IDs, exclude known identifiers and incomplete identities, then draw uniformly with PowerShell `Get-Random`.
- `Inclusion criteria`: primary or official evidence for identity, method, experiments, assumptions, limitations, venue, or concrete related-DEP overlap.
- `Exclusion criteria`: abstract-only evidence for paper claims, secondary summaries where primary sources were available, unverified code claims, duplicate owners, and unrelated DEP entries.
- `Analytical approach`: empirical, conceptual, comparative, implementation, safety/ethics, product research, financial-evidence audit, and replication.
- `Evidence handling`: author claims, source evidence, reviewer interpretations, negative evidence, related context, and process evidence have separate IDs and confidence labels.
- `Uncertainty handling`: unreproduced results remain author-reported; causal language is bounded by stated assumptions; missing code, prompts, outputs, and financial costs remain visible.
- `Extraction process`: all 17 PDF pages were rendered and visually inspected; full-paper HTML headings, tables, figures, assumptions, limitations, and references were parsed and cross-checked.
- `Version control`: paper pinned to arXiv v1; official proceedings record checked separately; no code commit was available to pin.
- `Cross-checking`: Table 1, Table 2, dataset statistics, portfolio table, correlation table, abstract, and venue metadata were checked across complete-paper and official records.
- `Safety handling`: examples are offline, synthetic, read-only, and non-advisory; no brokerage, order, credential, or live-trading logic is provided.
- `Reviewer stance`: critical paper report, DEP-ready preservation, implementation translation, and replication planning.
- `Random selection`: a preliminary diagnostic draw was discarded before the dedup scope was frozen because it included unrelated identity-report inventories. The reported draw is the single uniform draw over the corrected fixed pool: eligible index 20,293 of 75,310; zero duplicate reselections.
- `Dedup validation`: exact arXiv ID, both DOIs, normalized title, slug, owning artifacts, automation memory, relevant Black-Lake-Data entries, and preceding-24-hour markers were checked with no duplicate owner.

## Scope, Constraints, and Assumptions

- `Scope`: paper identity, method, experiments, figures, tables, causal assumptions, limitations, three related DEP bridges, and safe offline implementation paths.
- `Temporal boundary`: arXiv v1 submitted 2024-11-10; NeurIPS 2024 proceedings; repository and source checks through 2026-07-23.
- `Evidence limits`: no code execution, model weights, LLM score corpus, API configuration, raw predictions, seeds, dataset reconstruction, graph ground truth, or backtest rerun.
- `Assumptions`: verified PDF and HTML represent arXiv v1; table transcription matches the source; related DEP manuscripts accurately preserve their cited sources.
- `Constraints`: public-safe generated Markdown only; source locality; no credentials; no trading advice; no source redistribution.
- `Out of scope`: investment recommendations, live execution, legal/regulatory advice, proving causal identification, or certifying profitability.
- `Intended use`: research review, replication planning, benchmark auditing, and evidence-gated prototyping.
- `Audience`: causal-ML researchers, financial-ML reviewers, research engineers, and safety reviewers.
- `Reproducibility boundary`: architecture and toy mechanisms can be prototyped; exact paper results cannot be reproduced from inspected public artifacts alone.
- `Data sensitivity`: public paper metadata and derived review only; original documents remain private and local.

## Observations

- `Observed pattern`: the TCD ablation loses far more accuracy than the smaller margins between CausalStock and the strongest baseline, so validating that module is the highest-value replication step.
- `Technical implication`: LLM scores and graph probabilities form two successive uncertain filters; calibration error can compound before the final classifier.
- `Contradiction or tension`: the paper argues for explainable causal structure, but its strongest empirical validation is predictive accuracy and plausibility rather than edge recovery or interventions.
- `Observed pattern`: variable-dependent edges can improve results but become expensive as `D` grows, exposing a scalability-interpretability tradeoff.
- `Open question`: whether the market-value correlation remains after controlling for sector, coverage, volatility, capitalization-linked news volume, and model exposure.
- `Reviewer hypothesis`: much of the transferable value may come from explicit structured news scoring and lag-aware relational inductive bias, even if causal semantics are weakened.

## Considerations

- A reproduction needs immutable news timestamps, exchange calendars, split manifests, prompt/model identifiers, cached scores, and leakage checks.
- Causal edge dashboards should show stability across seeds, lags, regimes, and graph priors, not a single heatmap.
- LLM news scores require provenance, source quality flags, disagreement monitoring, and human review for value-laden outputs.
- Financial evaluation requires costs, turnover, slippage, impact, survivorship, latency, corporate actions, and walk-forward refreshes.
- Accuracy and MCC need calibration, uncertainty intervals, class balance, and regime-stratified reporting before decision use.
- Any downstream system should abstain under shift, sparse evidence, unstable graphs, or unsupported assets.
- The artifact is research analysis and not financial advice.

## Strengths

- Integrates text, prices, directional relations, lags, and prediction in one inspectable architecture.
- Uses explicit five-dimensional news scores rather than an opaque pooled embedding alone.
- Evaluates six markets/datasets across news-plus-price and price-only settings.
- Reports multiple runs, ablations, sensitivity analysis, explanation examples, and portfolio diagnostics.
- States causal assumptions, graph-model limitations, and an LLM safety concern.
- The large TCD ablation provides a clear replication target.

## Weaknesses

- Observational graph learning does not independently establish economic causality.
- No intervention, synthetic graph-recovery benchmark, placebo edge, or negative-control evidence is supplied.
- No author-identified code, immutable LLM outputs, raw predictions, or exact seed manifest was found.
- Primary LLM execution details are insufficient for exact reproduction and longitudinal stability.
- Benchmark datasets and text windows are historical; current-regime transfer is unknown.
- Statistical reporting lacks confidence intervals for between-model differences and multiple-comparison analysis.
- Portfolio evidence omits material market frictions and operational constraints.
- Static Bernoulli edges limit time-varying and multi-level relation modeling.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish code, split manifests, prompts, model snapshot, cached scores, seeds, and raw predictions | Reproducibility | Current public evidence cannot recreate the run | Independent verification | Licensing and storage work | Clean-room rerun with hash-matched inputs |
| Add synthetic and semi-synthetic graph recovery | Causal validity | Predictive accuracy does not test edge direction | Measures precision, recall, lag recovery | Synthetic-to-real gap | Known-DAG benchmarks and stress tests |
| Run placebo, permutation, and negative-control edges | Falsification | Plausible heatmaps can reflect bias | Detects spurious influence | Test-design complexity | Sector/time-shuffled controls |
| Add dynamic hierarchical edge distributions | Model scope | Static Bernoulli edges miss regime and intensity changes | Better regime adaptation | More parameters and instability | Walk-forward regime tests |
| Calibrate predictions and edge probabilities | Decision quality | Point scores hide uncertainty | Safer abstention and thresholds | Calibration drift | Time-split calibration and coverage checks |
| Use cost-aware walk-forward portfolio evaluation | Financial evidence | Gross historical returns overstate deployment evidence | More realistic transfer assessment | Execution model assumptions | Multiple cost/impact scenarios |
| Control explanation analyses for coverage and scale | Interpretability | Market value may proxy for data exposure | Stronger explanatory evidence | Covariate collection | Matched and multivariate analyses |

## Potential Implementations

1. **Edge Stability Auditor** — `User`: causal-ML reviewer. `Goal`: test whether edges survive seeds and regimes. `Mechanism`: repeat graph estimation on synthetic/public data and compare posterior stability. `Inputs`: versioned arrays and run manifests. `Outputs`: edge intervals, disagreement map, abstentions. `Risk controls`: no live market action; fail closed on instability. `Evaluation`: graph recovery plus time-split stability.
2. **News Evidence Receipt Service** — `User`: research data engineer. `Goal`: make LLM scores reproducible. `Mechanism`: store prompt/model/source identifiers and five structured scores. `Inputs`: licensed or public news references. `Outputs`: immutable score receipts and review overrides. `Risk controls`: no private feed redistribution or credentials. `Evaluation`: inter-model agreement, drift, and reviewer concordance.
3. **Cost-Aware Research Sandbox** — `User`: financial-ML reviewer. `Goal`: audit the paper's top-three strategy. `Mechanism`: offline walk-forward backtest with costs and abstention. `Inputs`: authorized historical data and predictions. `Outputs`: gross/net returns, turnover, drawdown, SR, and uncertainty. `Risk controls`: no broker connection or recommendations. `Evaluation`: baseline comparison across cost and shift scenarios.

## Three Ways to Exercise This Research

1. `Synthetic edge recovery`: Objective—test lag-direction recovery; inputs—small known-DAG time series; method—fit repeated graph posteriors and compare to truth; output—precision/recall and lag error; success—stable improvement over correlation baselines; stop—when instability exceeds a declared threshold; safety—synthetic data only.
2. `Prompt receipt replication`: Objective—measure news-score reproducibility; inputs—a small public toy news set; method—run version-pinned prompts across two approved models and reviewers; output—score disagreement and drift report; success—traceable scores with acceptable agreement; stop—on unlicensed or sensitive text; safety—no private feeds or trading use.
3. `Cost stress test`: Objective—bound portfolio-transfer claims; inputs—paper-style offline predictions or synthetic scores; method—apply turnover, costs, slippage, and abstention grids; output—net performance envelope; success—transparent sensitivity rather than profit; stop—before any live connectivity; safety—research-only, non-advisory.

## Example MVP Product

- `Product name`: CausalStock Evidence Bench.
- `Target user`: causal-ML and financial-ML research reviewers.
- `Problem`: predictive gains, graph explanations, LLM scores, and trading claims are hard to audit together.
- `Core workflow`: ingest versioned offline arrays and score receipts; run graph-stability, calibration, leakage, and cost tests; emit an evidence bundle with abstentions.
- `Data requirements`: synthetic graphs by default; optionally authorized historical prices, public or licensed news references, immutable split/calendar manifests, and cached model outputs.
- `Architecture`: local-only CLI; schema validator; news-receipt store; graph-runner adapter; calibration module; cost simulator; Markdown/JSON reporter.
- `Success metrics`: reproducible run hashes, edge recovery/stability, time-split calibration coverage, zero leakage findings, and cost-sensitivity completeness.
- `Risk controls`: no brokerage credentials, order generation, live recommendations, private-news redistribution, or automatic causal labels; abstain on unsupported or shifted inputs.
- `Limitations`: cannot establish real economic causality from observational data; results depend on dataset quality, graph assumptions, and simulator choices.
- `MVP boundary`: one small synthetic graph and one offline public benchmark; no production training or hosted service.
- `Deployment model`: local-only batch CLI.
- `Evaluation plan`: deterministic smoke tests, known-DAG recovery, timestamp leakage tests, calibration tests, and cost-grid snapshots.
- `Failure modes`: unstable graph posterior, prompt drift, missing timestamps, unsupported assets, sparse calibration bins, or cost-model sensitivity.
- `Maintenance plan`: version prompts, schemas, model identifiers, calendars, and cost assumptions; rerun shift checks for every data update.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| CausalStock | Selected primary paper | Full method, evidence, assumptions, and limitations | https://arxiv.org/abs/2411.06391 |
| Official NeurIPS record | Venue record | Main-track status, proceedings title, DOI, supplemental | https://proceedings.neurips.cc/paper_files/paper/2024/hash/54d689d58fe54c92aee2d732fc49fca8-Abstract-Conference.html |
| RHINO | Methodological neighbor | History-dependent temporal causal relationship learning used by the paper | https://arxiv.org/abs/2210.14706 |
| DYNOTEARS | Baseline context | Structure learning from multivariate time series | https://proceedings.mlr.press/v108/pamfil20a.html |
| CausalTAD Trajectory DEP | Related Black Lake review | Assumption-sensitive temporal causal prediction | `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md` |
| Quantum Quant Trading DEP | Related Black Lake review | Financial-evidence and deployment boundary | `.lake-data/DEP-E/DEP-E-20260714-Quantum Quant Trading/quantum_quant_trading_manuscript.md` |
| PAC Confidence DEP | Related Black Lake review | Calibration, finite-sample confidence, and shift | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2411.06391 | identity, authors, date, subjects, v1, acceptance, license link, arXiv DOI | 2026-07-23 | Primary metadata |
| R2 | https://arxiv.org/pdf/2411.06391 | all 17 pages, figures, tables, equations, appendices | 2026-07-23 | Verified private copy inspected; file withheld |
| R3 | https://arxiv.org/html/2411.06391 | full-paper structure, text, tables, references, assumptions, limitations | 2026-07-23 | Verified private copy and live page inspected; file withheld |
| R4 | https://proceedings.neurips.cc/paper_files/paper/2024/hash/54d689d58fe54c92aee2d732fc49fca8-Abstract-Conference.html | venue, proceedings title, authors, DOI, supplemental locator | 2026-07-23 | Official venue record |
| R5 | `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md` | temporal causal-graph and identification bridge | 2026-07-23 | Related repository artifact |
| R6 | `.lake-data/DEP-E/DEP-E-20260714-Quantum Quant Trading/quantum_quant_trading_manuscript.md` | financial-evidence bridge | 2026-07-23 | Related repository artifact |
| R7 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | calibration and shift bridge | 2026-07-23 | Related repository artifact |

## Appendix

### Selection and Dedup Record

- `PDF enumeration`: 75,780 files.
- `Unique parent-directory paper units`: 75,777.
- `Observed used identifiers`: 917.
- `Identifier matches excluded`: 282.
- `Identifier-incomplete units withheld`: 185.
- `Final eligible pool`: 75,310.
- `Uniform selection`: zero-based eligible index 20,293; zero-based all-unit index 20,438.
- `Reselection`: zero duplicate reselections after the dedup scope was frozen.
- `Diagnostic correction`: one preliminary diagnostic draw was discarded before the final pool was fixed because unrelated identity-report inventories were mistakenly included in the dedup source scope.
- `Exact acceptance checks`: arXiv ID, both DOIs, normalized title, slug, owning artifacts, automation memory, relevant Black-Lake-Data DEP entries, and preceding-24-hour markers.

### Source Integrity Record

- `Initial state`: partial; valid complete PDF present, full-paper HTML missing.
- `Repair`: preserved the PDF; collected official metadata HTML and official full-paper HTML through the archive-wide publisher broker; updated local provenance and verification records.
- `PDF`: 1,384,482 bytes; `%PDF-` header; trailing `%%EOF`; 17 parsed pages; SHA-256 `ac584f2e9b0ddceb12cbed9ba51e718c36ca40a5f5070935e6ceb964ea4a8af6`.
- `Full-paper HTML`: 956,847 bytes; 111,467 body characters; document marker; 91 heading/section markers; seven structure terms; SHA-256 `ab0e537a928dbe8c73e66638fa6d7a9c9dfcf5871ee07003e8f938f0602acde4`.
- `Metadata HTML`: 44,819 bytes; SHA-256 `78a57e5238fa1bdc333e4ec70c728e5ff87a2deee85f70369685a58a258ec945`.
- `TeX/source package`: not collected; a broker-rejected redirect prevented acquisition. The required PDF-plus-full-paper-HTML gate still passed.
- `Partials`: zero.
- `Public-source policy`: source documents, receipts, caches, and verification material remain private and local; temporary review renders stayed outside the repository and were removed after inspection.

### Replication Checklist

- [ ] Obtain and license the six exact dataset versions.
- [ ] Reconstruct chronological splits, exchange calendars, and feature timestamps.
- [ ] Pin prompt, model snapshot, sampling settings, and cached five-score outputs.
- [ ] Recreate every baseline with matched preprocessing and compute.
- [ ] Publish seed-level predictions, ACC/MCC distributions, and uncertainty intervals.
- [ ] Test graph recovery on known-DAG synthetic data and placebo controls.
- [ ] Add calibration, shift, and abstention evaluation.
- [ ] Re-run portfolio tests with walk-forward refresh, costs, turnover, slippage, and impact.

## Attribution Block

- Source URL: https://arxiv.org/abs/2411.06391
  - Applies to: the complete manuscript.
  - Notes: canonical identity, authors, version, subjects, license link, and arXiv DOI.
- Source URL: https://arxiv.org/pdf/2411.06391
  - Applies to: method, experiments, figures, tables, appendices, and critique.
  - Notes: verified private PDF inspected and withheld.
- Source URL: https://arxiv.org/html/2411.06391
  - Applies to: method, tables, source cross-checking, assumptions, limitations, and references.
  - Notes: verified complete private HTML and live public page inspected; file withheld.
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2024/hash/54d689d58fe54c92aee2d732fc49fca8-Abstract-Conference.html
  - Applies to: venue metadata and proceedings DOI.
  - Notes: official NeurIPS record.
- Source file policy: no PDF, HTML, TeX/source archive, extracted text, cache, render, receipt, or verification file was uploaded; no `.source/` directory was created.
