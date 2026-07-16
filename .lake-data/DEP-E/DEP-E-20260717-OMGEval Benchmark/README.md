# DEP-E-20260717-OMGEval Benchmark

#multilingual-llm #generative-evaluation #benchmarking #cultural-localization #llm-as-a-judge #human-evaluation #preference-evaluation #uncertainty-calibration #dataset-governance #research-review

Public-safe deposition context: this DEP-E preserves a source-first review of *OMGEval: An Open Multilingual Generative Evaluation Benchmark for Large Language Models* (`arXiv:2402.13524v2`). The selected archive unit was repaired to a verified complete PDF/full-paper-HTML state before review. All original source files, extracted text, caches, local locations, and exact execution details remain withheld.

## Contents

- `README.md`
  - This DEP inventory, source policy, synthesis context, and final attribution record.
- `omgeval_benchmark_manuscript.md`
  - Schema-complete manuscript covering source metadata, evidence, dataset construction, localization, evaluation, reported results, limitations, implementation paths, exactly three exercise paths, and synthesis with three related DEP entries.

No `.source/` directory exists. The PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, and local cache were intentionally kept outside the public repository.

## Summary of Items

### `README.md`

Records the deposit boundary, complete file inventory, public-safe run context, relationship to the operational log and detailed Report-Mark, and annotated public sources.

### `omgeval_benchmark_manuscript.md`

Reviews OMGEval's five-language open-ended question set, translation and human localization workflow, capability taxonomy, GPT-4 pairwise adjudication, model results, Chinese/Spanish human-agreement check, official release repository, and evidence gaps. It separates author claims from reviewer interpretation, records the random selection/dedup/source-integrity gates, and connects OMGEval to Judge Conformal, PAC Confidence, and OViP Preference.

## Insights and Relevance

OMGEval's durable contribution is to treat cultural localization as part of multilingual evaluation rather than equating multilinguality with translation. Its evidence nevertheless shows why a benchmark score needs a measurement envelope: the benchmark is uneven across capability categories, only five languages are included, GPT-4 supplies the pairwise preference signal, and direct human comparison is reported only for Chinese and Spanish subsets. The three related DEP entries turn those gaps into an engineering direction: attach calibrated uncertainty to judge outputs, require support- and shift-aware release gates, and keep benchmark evaluation separate from on-policy feedback loops that could contaminate the test set.

The matching operational note is `.logs/20260717-Arxiv-OMGEval-LOG.md`. The detailed synthesis and code mock-ups are in `.reports/BL-Arxiv-OMGEval-20260717/Report-Mark.md`. This DEP manuscript is the durable schema-complete research artifact; the log is operational, and the Report-Mark carries the richer cross-DEP concept bridge.

## Attribution Block

- Source URL: https://arxiv.org/abs/2402.13524
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: Canonical title, authors, abstract, arXiv identifier, category, version history, DOI, license locator, and public source links.
- Source URL: https://arxiv.org/pdf/2402.13524
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: Public equivalent of the verified complete primary PDF inspected locally; file not redistributed.
- Source URL: https://arxiv.org/html/2402.13524
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: Official full-paper HTML inspected locally; not an abstract page and not redistributed.
- Source URL: https://arxiv.org/e-print/2402.13524
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: TeX/source package used locally to cross-check structure, tables, and references; file not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2402.13524
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: ArXiv-issued persistent DOI.
- Source URL: https://github.com/blcuicall/OMGEval
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: Official dataset, prompt, model-output, and documentation repository inspected at commit `f4dfb6d188e711e72ba7453757209df808122e8e`.
- Source URL: https://github.com/blcuicall/OMGEval/blob/f4dfb6d188e711e72ba7453757209df808122e8e/LICENSE
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: MIT license for the inspected repository snapshot; dataset-specific third-party rights still require separate review.
- Source URL: https://arxiv.org/abs/2305.14387
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: AlpacaFarm and AlpacaEval context for pairwise feedback and automatic evaluation.
- Source URL: https://arxiv.org/abs/2306.05685
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: MT-Bench and Chatbot Arena context for LLM-as-a-judge biases and human agreement.
- Source URL: https://arxiv.org/abs/2308.16884
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: Belebele context for broad, parallel multilingual comprehension evaluation.
- Source URL: https://arxiv.org/abs/2306.05179
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: M3Exam context for multilingual and multilevel benchmark design.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`, `omgeval_benchmark_manuscript.md`
  - Notes: Live authority for repository layout, source withholding, DEP contents, logs, reports, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`, `omgeval_benchmark_manuscript.md`
  - Notes: Live authority for DEP-E container filing and the publications index.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: Live companion-repository authority read before deduplication context was used.
- Repository file: `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Judge%20Conformal/llm_judge_conformal_manuscript.md
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: Related DEP on interval-valued LLM judging; primary source basis is https://arxiv.org/abs/2509.18658.
- Repository file: `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: Related DEP on finite-sample confidence coverage and distribution-shift boundaries; primary source basis is https://arxiv.org/abs/2011.00716.
- Repository file: `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md
  - Applies to: `omgeval_benchmark_manuscript.md`
  - Notes: Related DEP on judge-mediated on-policy preference loops; primary source basis is https://arxiv.org/abs/2505.15963.
