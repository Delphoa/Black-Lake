# Report-Mark: CausalStock

## Source Metadata

- `Full title`: *CausalStock: Deep End-to-end Causal Discovery for News-driven Stock Movement Prediction*.
- `Authors`: Shuqi Li, Yuebo Sun, Yuxin Lin, Xin Gao, Shuo Shang, Rui Yan.
- `Version`: arXiv:2411.06391v1, submitted 2024-11-10.
- `Venue`: Advances in Neural Information Processing Systems 37, NeurIPS 2024 Main Conference Track.
- `Persistent identifiers`: https://doi.org/10.48550/arXiv.2411.06391 and https://doi.org/10.52202/079017-1504.
- `Subjects`: cs.LG, cs.AI, cs.CE, cs.CL.
- `Primary sources`: https://arxiv.org/abs/2411.06391, https://arxiv.org/pdf/2411.06391, https://arxiv.org/html/2411.06391, and the official NeurIPS proceedings record.
- `Source state`: verified complete private PDF plus verified complete private full-paper HTML; metadata HTML collected; source files withheld.

## Research Notes

CausalStock joins three components. A market-information encoder maps historical prices and news into per-stock, per-lag representations. Its Denoised News Encoder asks an LLM to score each news item on correlation, sentiment, importance, price impact, and impact duration. A lag-dependent temporal causal-discovery module uses a sparse, optionally knowledge-guided graph prior and a Bernoulli variational posterior whose edge probabilities depend on the preceding lag. A functional causal model then gates price and news representations with sampled edge existence and learned causal-strength weights to predict next-day movement.

The evidence is broad but not independently reproduced. The paper evaluates three news-plus-price datasets (ACL18, CMIN-US, CMIN-CN) and three price-only datasets (KDD17, NI225, FTSE100), using chronological splits, ACC, and MCC. Table 1 reports that CausalStock leads all listed baselines. Against the strongest listed news baseline, ACC improves by 0.73, 1.21, and 0.91 percentage points across ACL18, CMIN-US, and CMIN-CN. For price-only prediction, the largest ACC margin is 2.56 points on KDD17; the NI225 and FTSE100 margins are 0.25 and 0.80 points.

The ablations support component usefulness under the reported setup: removing temporal causal discovery produces the largest collapse; removing news, link non-existence modeling, or lag dependence also reduces performance. Denoised LLM scoring generally exceeds the same LLM used as a conventional encoder. A variable-dependent graph variant slightly improves two datasets but raises complexity and is not uniformly better.

The strongest limitation is semantic rather than numerical. The paper calls learned observational dependencies causal under Causal Markov, minimality, structural identifiability, correct-specification, causal-sufficiency, and likelihood-regularity assumptions. No intervention, negative-control, synthetic graph recovery, or independent causal benchmark validates edge orientation. The learned graph is therefore best treated as an assumption-conditioned predictive structure, not established economic causality.

The investment simulation chooses the top three predicted stocks daily with equal weights and reports higher APV and Sharpe ratio on ACL18, KDD17, and NI225. The inspected sources do not establish transaction-cost, slippage, market-impact, turnover, tax, delisting, or execution-latency realism. The result is useful as a research diagnostic, not evidence of deployable profitability or financial advice.

## Evidence and Attribution

| ID | Evidence | Supports | Boundary |
|---|---|---|---|
| E1 | arXiv metadata record | Identity, authors, date, subjects, v1, NeurIPS acceptance, arXiv DOI | Metadata does not validate methods or results |
| E2 | Verified 17-page PDF and official full-paper HTML | Architecture, equations, tables, figures, assumptions, limitations, safety note | Author-reported and not independently reproduced |
| E3 | Official NeurIPS proceedings record | Main-track venue, proceedings title, publisher DOI, supplemental availability | Does not imply code or replication |
| E4 | Table 1 and Table 2 | Six-dataset results, run counts, component and encoder ablations | Seeds, raw outputs, and statistical tests unavailable |
| E5 | Figure 3, Table 5, and Section 5.5 | Explainability examples, market-value correlation, portfolio simulation | Correlation and visual explanation do not establish causal validity |
| E6 | Appendix B, E, and F | Causal assumptions, static/Bernoulli graph limits, LLM value-alignment risk | Brief disclosures leave operational controls unspecified |
| E7 | Bounded title, identifier, and GitHub searches | No author-identified public implementation found | Absence from a bounded search is not proof of nonexistence |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md` — concrete overlap in temporal causal graphs, predictive use, and the need to separate an assumed graph from intervention-backed causal validity. Source basis: its inspected CausalTAD manuscript and evidence ledger.
2. `.lake-data/DEP-E/DEP-E-20260714-Quantum Quant Trading/quantum_quant_trading_manuscript.md` — concrete overlap in market prediction, trading evaluation, and the distinction between a theoretical or historical result and end-to-end financial advantage. Source basis: its inspected quantum-trading manuscript and evidence ledger.
3. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` — concrete overlap in predictive confidence, thresholded downstream decisions, and the distribution-shift boundary missing from point-estimate accuracy claims. Source basis: its inspected PAC-confidence manuscript and evidence ledger.

## Synthesis Note

### Concept Bridge

CausalStock can be read as an evidence-routing architecture: noisy event text is compressed into explicit scores, temporal edges route evidence across entities, and a predictor turns the routed state into decisions. CausalTAD highlights that a graph remains conditional on its identification assumptions; Quantum Quant Trading highlights that a forecasting or optimization advantage is not a deployable financial advantage; PAC Confidence supplies the missing discipline for attaching uncertainty and abstention to downstream decisions.

### Potential Implementations

1. **Causal-edge audit bench**: replay public or synthetic multivariate series, compare edge stability across seeds and regimes, and emit abstention when directionality is unstable.
2. **News-score provenance layer**: cache structured LLM scores with prompt version, model identifier, source timestamp, and reviewer overrides before any market model consumes them.
3. **Cost-aware paper portfolio sandbox**: reproduce only the top-three research policy with turnover, cost, slippage, and walk-forward controls; prohibit brokerage connectivity.

### Deeper Relationship Observations

1. The graph posterior and LLM news scores are both learned evidence filters; neither is inherently calibrated, so uncertainty can compound before the final classifier.
2. The paper's lag dependence addresses temporal structure, while its own limitation calls for time-varying graphs; this is a regime-change problem as much as a graph-model problem.
3. Market-value correlation in the learned graph is compatible with real economic influence, representation scale effects, data coverage, or model bias; the explanation layer needs falsification tests, not only plausible stories.

### Conceptual Similarities

1. Like CausalTAD, CausalStock turns an assumed temporal causal structure into a predictive gate and inherits the validity boundary of that structure.
2. Like Quantum Quant Trading, CausalStock connects a technical model to portfolio outcomes but leaves operational market costs outside the evidence envelope.
3. Like PAC Confidence, CausalStock needs explicit calibration, shift checks, and abstention before a point score can support consequential decisions.

### MVP Implementations With Code Mock-ups

1. **Edge Stability Gate**

```python
def stable_edge(edge_samples, minimum=0.8):
    probability = sum(edge_samples) / len(edge_samples)
    return {"probability": probability, "use": probability >= minimum}
```

Use synthetic graph samples only; fail closed when runs or regimes disagree.

2. **News Evidence Receipt**

```python
def news_receipt(source_id, prompt_version, model_id, scores):
    assert set(scores) == {"correlation", "sentiment", "importance", "impact", "duration"}
    return {"source_id": source_id, "prompt_version": prompt_version,
            "model_id": model_id, "scores": scores}
```

Store identifiers and structured scores, never credentials or private news feeds.

3. **Research-Only Cost Gate**

```python
def net_return(gross_return, turnover, cost_rate):
    return gross_return - abs(turnover) * cost_rate
```

Apply to offline historical arrays; no broker API, order generation, or live recommendation surface.

### Developer Challenges

1. Reconstructing the model requires exact LLM prompt execution, cached scores, graph-sampling details, seeds, and dataset preprocessing that are not fully packaged.
2. Efficiently representing an `L x D x D` graph while preserving audit traces becomes difficult as the stock universe grows.
3. A safe system must prevent look-ahead leakage across news timestamps, price closes, graph updates, validation, and portfolio formation.

### Author Challenges

1. Validate learned directionality with interventions, synthetic recovery, placebo edges, or negative controls rather than predictive fit alone.
2. Release code, prompt/model snapshots, structured LLM outputs, splits, seeds, and environment details sufficient for exact reproduction.
3. Re-evaluate portfolio claims with walk-forward refreshes, costs, slippage, turnover, market impact, and uncertainty-aware abstention.

## Validation Notes

- Random selection: 75,780 PDFs collapsed to 75,777 units; 282 identifier matches and 185 identifier-incomplete units were excluded; final eligible pool 75,310; uniform final index 20,293; zero duplicate reselections after pool freeze.
- Dedup: arXiv ID, both DOIs, normalized title, slug, repository artifacts, automation memory, relevant Black-Lake-Data entries, and 24-hour markers were checked with no owning duplicate.
- Source integrity: initial partial unit repaired to complete; preserved PDF passes size/header/EOF and 17-page parsing; full-paper HTML passes all size/body/marker/heading/structure checks; no partials remain.
- Review coverage: all 17 rendered PDF pages, official full-paper HTML, tables, figures, appendices, arXiv metadata, NeurIPS record, and bounded official-code search were inspected.
- Public safety: output contains no local path, username, machine name, local timezone, exact local execution timestamp, credential, or source file.
- Source-upload gate: generated Markdown only; no PDF, HTML, archive, cache, extracted source text, render, receipt, or `.source/` directory is allowed in the staged set.

## Attribution Block

- Source URL: https://arxiv.org/abs/2411.06391
  - Applies to: this report and the DEP-E manuscript.
  - Notes: canonical identity, authors, version, subjects, license link, and arXiv DOI.
- Source URL: https://arxiv.org/pdf/2411.06391
  - Applies to: this report and the DEP-E manuscript.
  - Notes: complete paper inspected from a verified private copy; source file withheld.
- Source URL: https://arxiv.org/html/2411.06391
  - Applies to: this report and the DEP-E manuscript.
  - Notes: verified full-paper HTML used for section and table cross-checking; source file withheld.
- Source URL: https://proceedings.neurips.cc/paper_files/paper/2024/hash/54d689d58fe54c92aee2d732fc49fca8-Abstract-Conference.html
  - Applies to: venue and publisher metadata.
  - Notes: official NeurIPS proceedings record and publisher DOI.
