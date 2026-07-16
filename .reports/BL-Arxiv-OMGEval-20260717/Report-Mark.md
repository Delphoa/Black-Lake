# Report-Mark: OMGEval

Public run date: 2026-07-17

## Source Metadata

| Field | Value |
|---|---|
| Paper | *OMGEval: An Open Multilingual Generative Evaluation Benchmark for Large Language Models* |
| Authors | Yang Liu; Meng Xu; Shuo Wang; Liner Yang; Haoyu Wang; Zhenghao Liu; Cunliang Kong; Yun Chen; Yang Liu; Maosong Sun; Erhong Yang |
| Stable record | `arXiv:2402.13524v2`; DOI `10.48550/arXiv.2402.13524` |
| Version dates | Submitted 2024-02-21; v2 revised 2026-01-30 |
| Subject | Computation and Language (`cs.CL`) |
| Primary public sources | https://arxiv.org/abs/2402.13524; https://arxiv.org/pdf/2402.13524; https://arxiv.org/html/2402.13524; https://arxiv.org/e-print/2402.13524 |
| Official release | https://github.com/blcuicall/OMGEval at commit `f4dfb6d188e711e72ba7453757209df808122e8e`; MIT repository license |
| Source integrity | Complete after local repair; valid PDF preserved and official full-paper HTML, metadata HTML, and source package collected locally |
| Source distribution | All source files, extracted text, caches, and local locations withheld; no `.source/` directory created |

## Concise Research Notes

- `Problem`: Existing multilingual evaluation was dominated by translated or discriminative tasks, while open-ended generative benchmarks were mainly English-only. The paper asks how to evaluate instruction-following and culturally situated generation across multiple languages.
- `Core method`: OMGEval adapts AlpacaEval questions into Chinese, Russian, French, Spanish, and Arabic. GPT-4 first supplies translations; language teams then localize culture-specific people, places, foods, festivals, works, periods, and writing systems. Each language uses two annotators and one reviewer with relevant linguistic expertise. The released benchmark contains 804 questions per language and nine capability categories.
- `Evaluation`: Model outputs are compared pairwise against GPT-3.5-Turbo using GPT-4 as adjudicator. The full set and language-specific localization subsets are reported separately. Ten proprietary and open multilingual models are compared.
- `Evidence and results`: Table 4 reports GPT-4 average win rates of 55.5 on the full sets and 54.6 on localized subsets, versus the 50.0 baseline. Guanaco-13B is the strongest listed open model at 14.8 full and 13.7 localized; BLOOMZ-7B1-mt is 0.4 and 0.7. Human comparison on 100 Chinese and 100 Spanish examples reports F1 values of 0.88/0.79 for Chinese full/localized and 0.91/0.89 for Spanish full/localized.
- `Dataset evidence`: Localized-question counts are 231 Chinese, 181 Russian, 197 French, 197 Spanish, and 212 Arabic. General knowledge and professional knowledge account for 27.0% and 26.7% of questions, while harmlessness is 1.1%, so capability coverage is intentionally broad but uneven.
- `Limitations`: The paper includes five languages, one baseline family, one primary automatic judge, imbalanced capability slices, and direct judge-human comparison for only Chinese and Spanish. The work does not establish measurement invariance across cultures, resistance to judge order/verbosity/self-bias, or current-model performance. Experiments were not rerun.
- `Implementation relevance`: OMGEval is best used as a versioned evaluation corpus with per-language support cards, blinded multi-judge adjudication, human calibration subsets, immutable held-out test items, and separate development items for model improvement.
- `Reviewer interpretation`: Cultural localization is the important intervention, but a localized prompt is not automatically an equivalent measurement item. The benchmark should expose both cultural relevance and comparability rather than collapse them into one win rate.

## Evidence and Attribution

| ID | Inspected evidence | Supports | Confidence and boundary |
|---|---|---|---|
| E1 | Complete arXiv v2 PDF, official full-paper HTML, metadata HTML, and TeX/source package | Identity, construction workflow, tables, results, ethics, limitations | High for source transcription; no independent reproduction |
| E2 | Tables 2-5 and Sections 3-4 | Capability taxonomy, language/localization counts, model win rates, human-agreement metrics | High for reported values; evaluator outputs and statistics not recomputed |
| E3 | Official OMGEval repository and MIT license at pinned commit | Presence of language data, evaluator prompts, figures, model outputs, documentation, and license | High for inventory; no end-to-end executable reproduction was identified or run |
| E4 | AlpacaFarm, MT-Bench/Chatbot Arena, Belebele, and M3Exam primary records | Evaluation lineage and methodological context | High for metadata and abstracts; not full-paper secondary reviews in this artifact |
| E5 | Judge Conformal, PAC Confidence, and OViP Preference DEP manuscripts | Cross-DEP synthesis on judge uncertainty, finite support, shift, and preference feedback loops | Medium; conceptual bridge, not a joint experiment |
| E6 | Repository rules, dedup markers, automation memory, and local archive verification | Selection, eligibility, source-integrity, and public-safety process | High for observed process; not paper evidence |

Source claims above are attributed to the paper and official release. Reviewer interpretations are labeled. Public URLs identify source material; physical paper files and extraction caches remain local.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` — https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Judge%20Conformal/llm_judge_conformal_manuscript.md — selected because it converts LLM-as-a-judge point ratings into calibrated prediction intervals and makes judge uncertainty actionable; its source basis is `arXiv:2509.18658`.
2. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` — https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md — selected because it supplies finite-sample support and distribution-shift boundaries for turning benchmark scores into release gates; its source basis is `arXiv:2011.00716`.
3. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` — https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md — selected because it exposes how judge-mediated, on-policy preference data can improve relevance while amplifying judge bias and contaminating evaluation if test and training loops are not separated; its source basis is `arXiv:2505.15963`.

## Synthesis Note

### Concept Bridge

OMGEval constructs culturally localized, open-ended prompts and reduces model comparisons to GPT-4 pairwise preferences. Judge Conformal shows how that point judgment can become an uncertainty interval rather than an exact label. PAC Confidence shows that any interval or threshold is meaningful only inside a versioned calibration distribution with enough support. OViP Preference shows what happens when judge signals are fed back into training: the failure distribution can become more relevant, but the judge also shapes future data. Together they define a benchmark lifecycle with four distinct layers: culturally grounded item construction, uncertainty-aware adjudication, support- and shift-aware decision gates, and an isolated development loop that never writes benchmark test items back into training.

### Potential Implementations

1. `Multilingual Judge Calibration Card`: collect blinded human labels for each language, capability, and localization slice; compare multiple randomized judges; publish agreement, interval width, order sensitivity, and abstention rates beside every win rate.
2. `Culture-Slice Feedback Sandbox`: use a development-only copy of localized items to discover model-specific failures, generate candidate hard cases, and require native-speaker review before admission; cryptographically block immutable test IDs from the feedback loop.
3. `Shift-Aware Benchmark Release Gate`: attach support counts and finite-sample intervals to each slice, reject aggregate ranking claims when language/capability coverage is sparse or drifted, and route disputed comparisons to human review.

### Deeper Relationship Observations

1. Localization changes the semantic and cultural conditions of a question, so it is closer to a controlled intervention than a translation; this improves relevance but can violate cross-language measurement equivalence.
2. Pairwise LLM judgment is simultaneously OMGEval's scaling mechanism and its largest single point of epistemic compression: uncertainty intervals reveal instability, but they do not remove systematic cultural, order, verbosity, or self-preference bias.
3. On-policy feedback makes training examples track current model errors, yet using benchmark-derived failures for training erodes the benchmark's meaning; static evaluation and adaptive improvement need separate, auditable data lineages.

### Conceptual Similarities

1. All four works convert qualitative behavior into operational proxies: pairwise preference, interval confidence, finite-sample coverage, or failure-guided preference data.
2. All four depend on the relationship between calibration/development data and future test behavior; sparse support or distribution shift weakens their conclusions.
3. All four require human and provenance governance because automated judges, labels, and generated negatives can reproduce hidden preferences while appearing quantitative.

### MVP Implementations with Code Mock-Ups

1. `Slice Calibration Router` — route unstable or weakly supported language slices to human review instead of publishing a precise ranking.

```python
def slice_route(sample_count, interval_low, interval_high, human_f1):
    width = interval_high - interval_low
    if sample_count < 100 or width > 0.15:
        return "human_review"
    if human_f1 < 0.80:
        return "recalibrate_judge"
    return "publish_with_interval"
```

2. `Benchmark Leakage Guard` — admit on-policy feedback only from development items and preserve a denylist for immutable test IDs.

```python
def feedback_candidate(item_id, split, immutable_test_ids, reviewer_ok):
    if item_id in immutable_test_ids or split != "development":
        return {"accepted": False, "reason": "benchmark_leakage"}
    if not reviewer_ok:
        return {"accepted": False, "reason": "native_review_required"}
    return {"accepted": True, "reason": "audited_development_item"}
```

3. `Shift-Aware Score Gate` — require support, judge agreement, and bounded drift before a slice contributes to a release decision.

```python
def score_gate(support, judge_agreement, drift_score, limits):
    checks = {
        "support": support >= limits["min_support"],
        "agreement": judge_agreement >= limits["min_agreement"],
        "drift": drift_score <= limits["max_drift"],
    }
    return "eligible" if all(checks.values()) else "withhold"
```

These mock-ups are standard-library-only policy sketches, not statistical estimators or production approval logic.

### Developer Challenges

1. Build an order-randomized, multi-judge evaluation harness that preserves raw disagreement and never executes model-produced text as code.
2. Design a schema that versions each prompt's translation, localization rationale, native review, capability tags, immutable split, and judge/calibration envelope.
3. Prove through tests that no test-set identifier, answer, model output, or judge rationale can enter an on-policy training or hard-negative generation queue.

### Author Challenges

1. Extend the human comparison to all five languages, all capability categories, multiple model pairs, randomized answer order, and multiple judge families with uncertainty intervals.
2. Publish a measurement-invariance analysis that distinguishes cultural adaptation gains from changes in difficulty, answerability, or annotation preference across languages.
3. Release a fully pinned, safe evaluation harness with versioned prompts, deterministic parsers, non-executing structured-output validation, dataset cards, and reproducible aggregate tables.

## Validation Notes

- Random selection was executed, not fabricated: 75,777 PDF candidates, 75,776 unique paper units, uniform zero-based index 39,883.
- Deduplication searched Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data for ID, DOI, exact title, and slug. Exclusions and reselections were zero; the public-safe 24-hour cutoff date marker was 2026-07-16.
- The initial source state was partial because full-paper HTML was missing. The valid 2,528,158-byte `%PDF-`/`%%EOF` PDF was preserved. Official full-paper HTML passed the size, body, marker, heading, and structure gates; metadata HTML and the source package were also collected locally. No partial files remain.
- Local extraction completed with PDF, HTML, and source text. A standalone page-image audit was unavailable, so figure content was reviewed through full text, captions, extracted tables, and the official HTML rather than a separate pixel-level rendering pass.
- Paper, dataset, and code experiments were not rerun. Metrics remain author reported. The official repository was inspected at a pinned commit and exposes data, prompts, figures, model outputs, documentation, and an MIT license; no end-to-end run was claimed.
- Exactly three related DEP entries, potential implementations, deeper observations, conceptual similarities, MVP mock-ups, developer challenges, and author challenges appear above.
- No source PDF, HTML, source archive, extracted text, cache, local path, machine identifier, local timezone label, or exact local execution timestamp is included in this public artifact.

## Attribution Block

- Source URL: https://arxiv.org/abs/2402.13524
  - Notes: Canonical metadata, abstract, version history, authors, subject, DOI, and source locators.
- Source URL: https://arxiv.org/pdf/2402.13524
  - Notes: Complete primary paper inspected locally; file withheld.
- Source URL: https://arxiv.org/html/2402.13524
  - Notes: Official complete full-paper HTML inspected locally; file withheld.
- Source URL: https://arxiv.org/e-print/2402.13524
  - Notes: Source package inspected locally for structure and table cross-checking; file withheld.
- Source URL: https://doi.org/10.48550/arXiv.2402.13524
  - Notes: Persistent arXiv-issued DOI.
- Source URL: https://github.com/blcuicall/OMGEval
  - Notes: Official release repository inspected at commit `f4dfb6d188e711e72ba7453757209df808122e8e`.
- Source URL: https://github.com/blcuicall/OMGEval/blob/f4dfb6d188e711e72ba7453757209df808122e8e/LICENSE
  - Notes: MIT repository license at the inspected commit.
- Source URL: https://arxiv.org/abs/2305.14387
  - Notes: AlpacaFarm and AlpacaEval evaluation lineage.
- Source URL: https://arxiv.org/abs/2306.05685
  - Notes: LLM-as-a-judge bias and human-agreement context.
- Source URL: https://arxiv.org/abs/2308.16884
  - Notes: Parallel multilingual benchmark context.
- Source URL: https://arxiv.org/abs/2306.05179
  - Notes: Multilingual, multimodal, multilevel benchmark context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Notes: Live Black Lake deposition and public-source authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Notes: Live DEP class, filing, and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Notes: Live companion-repository authority read before related-context and dedup use.
- Repository file: `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Judge%20Conformal/llm_judge_conformal_manuscript.md
  - Source basis: https://arxiv.org/abs/2509.18658
- Repository file: `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md
  - Source basis: https://arxiv.org/abs/2011.00716
- Repository file: `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md
  - Source basis: https://arxiv.org/abs/2505.15963
