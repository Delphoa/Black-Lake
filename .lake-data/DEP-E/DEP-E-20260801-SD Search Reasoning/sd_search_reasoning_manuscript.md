---
title: "SD-Search - DEP-E"
generated_at: "2026-08-01"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of on-policy hindsight self-distillation for search-augmented reasoning."
source_status: "verified complete local PDF, full-paper HTML, metadata HTML, and source package inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-01"
temporal_cutoff: "arXiv:2605.18299v1 and related Black-Lake records inspected through 2026-08-01"
primary_url: "https://arxiv.org/abs/2605.18299"
stable_identifier: "arXiv:2605.18299v1; DOI:10.48550/arXiv.2605.18299"
confidence_summary: "High for source identity, mechanism, reported tables, ablations, and stated limitations; medium for generalization and implementation transfer; low for independent reproducibility because no official implementation was identified or executed."
safety_scope: "defensive and evaluation-only research translation using public or synthetic data"
distribution_notes: "Only generated Markdown and derived public pointer metadata are deposited; source files, caches, extracted text, model weights, and private data remain local."
---

# SD-Search - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public URL | Usage notes | Access date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Metadata and primary locator | HTML | arXiv:2605.18299v1 | https://arxiv.org/abs/2605.18299 | Public metadata; title, authors, date, subjects, DOI, and license link | 2026-08-01 | Inspected |
| S2 | Official full-paper rendering | Primary paper | HTML | arXiv:2605.18299v1 | https://arxiv.org/html/2605.18299 | Full method, experiments, limitations, and appendices | 2026-08-01 | Inspected in full |
| S3 | Paper PDF | Primary paper | PDF | arXiv:2605.18299v1 | https://arxiv.org/pdf/2605.18299 | Verified locally; source file withheld | 2026-08-01 | Inspected and cross-checked |
| S4 | TeX/source package | Primary source | Source archive | arXiv:2605.18299v1 | https://arxiv.org/e-print/2605.18299 | Equations, tables, appendices, and structure; source withheld | 2026-08-01 | Inspected locally |
| S5 | arXiv-issued DOI | Persistent identity | DOI | 10.48550/arXiv.2605.18299 | https://doi.org/10.48550/arXiv.2605.18299 | Persistent resolver | 2026-08-01 | Resolved |
| S6 | Token Tax RAG DEP-A | Related research | Markdown | DEP-A-20260727 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260727-Token%20Tax%20RAG/2606.20898-whitepaper-review.md | Evidence-access and cost frontier context | 2026-08-01 | Inspected |
| S7 | DASD Reasoning DEP-E | Related research | Markdown | DEP-E-20260725 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260725-DASD%20Reasoning/dasd_reasoning_manuscript.md | Distillation and rollout-mismatch context | 2026-08-01 | Inspected |
| S8 | GPMD Regularized RL DEP-E | Related research | Markdown | DEP-E-20260716 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md | Policy-objective and stability context | 2026-08-01 | Inspected |

The paper lists Yufei Ma, Zihan Liang, Ben Chen, Zhipeng Qian, Huangyu Dai, Lingtao Mao, Xuxin Zhang, Chenyi Lei, and Wenwu Ou, affiliated with Kuaishou Technology. The arXiv record shows submission on 2026-05-18 and v1. The paper is presented as a preprint; no official implementation was identified in the inspected source bundle or focused public search.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 and S5 | Canonical metadata | Title, authors, date, subjects, version, DOI, and license link | Source identity and provenance | High | Metadata does not establish method or results |
| E2 | S2-S4, abstract through conclusion | Primary paper | Search-augmented problem, GRPO setup, teacher/student conditioning, future masking, outcome labels, JSD, total loss | Mechanism transcription | High | Text extraction has some symbol typography noise |
| E3 | S2-S4, main tables and appendices | Primary empirical evidence | Seven-benchmark EM, 3B/7B comparisons, five-seed table, ablations, scale and cost appendices | Reported quantitative results | High for transcription; medium for generalization | No independent rerun |
| E4 | S2-S4, limitations and scaling | Primary limitation evidence | Gold-answer dependence and all-success/all-failure contrast degeneration | Boundary conditions | High | Proposed extensions remain future work |
| E5 | S6-S8 | Related DEP evidence | Retrieval cost, distributional distillation, RL regularization, and reproducibility boundaries | Cross-DEP synthesis | Medium | Related records are secondary to the primary paper |
| E6 | Process records | Selection, integrity, and cache evidence | Uniform draw, zero reselection, repaired source state, cached PDF/HTML/source text, and source-withholding gate | Workflow claims | High | Private paths and exact local timestamps excluded |

## Executive Summary

SD-Search proposes on-policy hindsight self-distillation for search-augmented reasoning. Its core idea is to use the same policy as both student and teacher: the student sees only inference-time context, while the teacher additionally sees a hindsight block describing search spans and Correct/Incorrect outcomes from a rollout group. At each search-query token position, the student is aligned to the teacher with a top-k-truncated Jensen-Shannon divergence, and the auxiliary loss is added to GRPO after a warmup.

The paper reports experiments on seven QA benchmarks with Qwen2.5-3B and Qwen2.5-7B. The author-reported averages are 0.428 Exact Match for SD-Search-Base at 3B and 0.476 for SD-Search-Instruct at 7B. Five seeds give 0.428 ± 0.008 for SD-Search-Base, compared with 0.404 ± 0.008 for AutoRefine-Base and 0.429 ± 0.007 for Thinker-Instruct. These results are credible as a transcription of the inspected paper, but not independently reproduced. The most important limitations are dependence on reliably scorable answers and loss of contrast when a rollout group is all successful or all failed.

## Detailed Summary

### Problem

Search-augmented agents interleave reasoning with retrieval. Standard outcome-reward RL assigns a shared trajectory-level advantage to all generated tokens, so it cannot directly distinguish a useful search query from a redundant query inside the same rollout. Existing process-supervision methods in the paper import step-level supervision from stronger teachers or external annotations.

### Method

For a question, GRPO samples a group of trajectories. Each trajectory contains typed spans for thinking, search, retrieved documents, and answer. The hindsight block retains search-only skeletons from sibling rollouts and attaches Correct/Incorrect labels derived from answer F1. Future masking removes downstream thinking, documents, and answer spans so the teacher cannot read an answer from privileged evidence. A teacher forward pass on the same policy, under this hindsight context, produces token distributions at query positions. The student distribution under ordinary context is matched with Jensen-Shannon divergence.

The total objective is `L_total = L_GRPO + alpha_SD * L_SD`. The paper's defaults are `alpha_SD = 10^-3`, 50 warmup steps, top-k 50 for distribution support, outcome threshold rho 0, and group size G=5. Inference uses the ordinary policy context and does not require the teacher forward pass.

### Evaluation Setup

Training uses NQ and HotpotQA question-answer data. Evaluation covers NQ, TriviaQA, PopQA, HotpotQA, 2Wiki, MuSiQue, and Bamboogle. The paper states a fixed December 2018 Wikipedia corpus, E5-base-v2 retrieval, and three passages per query. Main models are Qwen2.5-3B and Qwen2.5-7B, with ablations on Qwen2.5-3B-Base in veRL-based infrastructure.

### Results

At 3B, SD-Search-Base reports 0.428 average EM and SD-Search-Instruct 0.427. The paper compares these with AutoRefine-Base at 0.405, MR-Search-Base at 0.414, and Thinker-Instruct at 0.430. At 7B, SD-Search-Base reports 0.471 and SD-Search-Instruct 0.476. The paper attributes the strongest gains to multi-hop benchmarks and reports that the method exceeds AutoRefine by 2.1 points at the 7B instruct setting.

Five-seed results on the 3B base comparison report average EM of 0.428 ± 0.008 for SD-Search, 0.404 ± 0.008 for AutoRefine, and 0.429 ± 0.007 for Thinker. The paper cautions that Bamboogle has a small test split and larger seed variance. A full 200-step 3B run is reported at 11.9 hours on 8×H800 compared with 10.3 hours for AutoRefine, or 15.5% end-to-end overhead.

### Ablations

Removing future masking costs 3.0 average points; replacing the hindsight block with current-step documents costs 3.4 points. Removing outcome labels costs 1.4 points, shuffling labels costs 2.3, removing the multi-rollout group costs 1.0, and leave-one-out removal of the focal rollout costs 0.5. Replacing JSD with forward KL, reverse KL, and MSE gives 0.418, 0.414, and 0.407 average EM compared with 0.428 for the full method; broadening alignment from query positions to all policy-generated positions gives 0.421.

### Limitations and Conclusion

Outcome labels inherit GRPO's need for reliably scorable gold answers, so open-ended generation needs a calibrated substitute. The hindsight contrast also degenerates when every rollout in a group is Correct or Incorrect. The conclusion claims improved outcome-reward performance and parity with larger-teacher process supervision without external teacher inference or extra inference cost, but those claims remain author-reported in this review.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Hindsight-conditioned self-distillation supplies query-level supervision from the policy itself. | Author mechanism claim | E2 | Directly supported by the method definition; implementation requires strict masking and alignment. | High |
| C2 | SD-Search reaches 0.428 average EM at 3B and 0.476 at 7B instruct. | Author empirical claim | E3 | Numbers match the inspected main tables; results were not rerun. | High for transcription; medium for generalization |
| C3 | Future masking and group-level outcome contrast are important design components. | Author ablation claim | E3 | Ablation direction and magnitudes are reported consistently; causal attribution remains within one paper. | Medium-high |
| C4 | The method has no external-teacher or auxiliary annotation cost. | Author systems claim | E2-E3 | True for the described training loop; total infrastructure and retriever cost still require matched accounting. | Medium-high |
| C5 | The approach is broadly applicable to open-ended tasks. | Reviewer assessment | E4 | Not established: the paper itself identifies gold-answer dependence as a limitation. | Low |

## Methodology

- `Research objective`: preserve and critique the paper's method, reported evidence, limitations, and safe implementation implications for a DEP-E research artifact.
- `Sources inspected`: canonical arXiv metadata, official full-paper HTML, verified local PDF, verified local TeX/source package, local extraction cache, and three related Black-Lake DEP manuscripts.
- `Discovery strategy`: local PDF enumeration with `rg --files -g "*.pdf"`, uniform PowerShell random draw, filename/folder/readme identity normalization, public arXiv metadata confirmation, focused public implementation search, and related-entry search in Black-Lake.
- `Inclusion criteria`: sources with direct evidence for identity, method, experiments, limitations, implementation availability, or a concrete conceptual bridge to retrieval, distillation, or RL.
- `Exclusion criteria`: abstract-only pages as paper evidence, unverified summaries as primary evidence, source files in public outputs, and unrelated DEP records.
- `Analytical approach`: conceptual, empirical, comparative, implementation, safety/ethics, product research, replication, and DEP-ready provenance analysis.
- `Evidence handling`: evidence IDs separate metadata, primary-paper claims, reported numbers, limitations, related DEP context, and process records; author claims are labeled as claims and reviewer inferences are labeled separately.
- `Uncertainty handling`: no reproduction, official code, model weights, benchmark rerun, or independent statistical test is implied; missing implementation evidence and boundary conditions remain explicit.
- `Random selection methodology`: 75,960 PDF paths were enumerated and collapsed to 75,957 unique parent-paper units. PowerShell `Get-Random` selected zero-based index 43,732; the first draw was eligible and no reselection occurred.
- `Cache methodology`: after the complete-source gate, `extract-arxiv` ran in `missing-only` mode against the local paper unit and central cache. The final status was `cached` with PDF, HTML, and source text; `pypdf`, HTML-regex, and tarfile succeeded, with `pdftotext` unavailable.
- `Dedup/reselection validation`: the public pointer index, repository logs/reports/DEP-E records, automation memory, arXiv ID, DOI, normalized title, slug, and 24-hour markers were checked before acceptance; no match was found.

## Scope, Constraints, and Assumptions

- `Scope`: source-grounded review of SD-Search's problem, mechanism, experiments, ablations, limitations, related DEP context, and bounded implementation implications.
- `Temporal boundary`: public sources and repository context inspected through 2026-08-01; the paper version reviewed is arXiv v1.
- `Evidence limits`: no independent training or inference, no official implementation identified, no model/checkpoint or dataset download, no publisher version, and some PDF symbol extraction noise.
- `Assumptions`: reported benchmark values and cost figures are transcribed accurately from the inspected paper; related DEP content is used only as contextual evidence.
- `Constraints`: source files remain local; public outputs exclude local paths, private data, credentials, model weights, caches, extracted source text, and operational search prompts.
- `Out of scope`: production deployment, open-ended preference-label design, claims of safety or factuality, unauthorized retrieval, and performance promises outside the paper's fixed corpus/retriever setup.
- `Intended use`: DEP deposition, research backlog creation, implementation planning, and source-grounded follow-on review.
- `Reproducibility boundary`: an independent reviewer can locate the public paper and reported settings but cannot reproduce the results without the implementation, exact data/configuration release, environment, and compute.
- `Operational boundary`: implementation examples are synthetic, offline, and evaluation-only; no network retrieval or consequential action is included.

## Observations

- `Observed pattern`: the largest ablation losses occur when privileged context leaks downstream evidence or when the hindsight block loses its outcome contrast.
- `Technical implication`: future masking is an information-flow boundary that should be validated as a data-contract test, not treated as a tunable convenience.
- `Contradiction or tension`: the method removes external-teacher inference but adds teacher-context construction, an auxiliary forward pass, and substantial training infrastructure; “no external teacher cost” is not “no systems cost.”
- `Open question`: as base model success increases, uniform all-Correct groups become more common and may reduce the value of the signal.
- `Reviewer hypothesis`: query-level credit may transfer best when retrieval quality is measurable and answer scoring is reliable, which limits immediate extension to subjective or open-ended tasks.

## Considerations

Deployment would need to separate training-time privileged context from inference-time context, log retriever and corpus versions, and monitor whether query diversity or search frequency changes while answer quality improves. Gold-answer labels can encode benchmark artifacts; preference-model substitutes introduce calibration and evaluator bias. The fixed corpus and retriever make the paper's cost and quality frontier useful for a controlled benchmark, not a general production guarantee. No source files or private data were redistributed.

## Strengths

- The mechanism is compact and integrates with GRPO without changing the advantage estimator.
- Future masking, leave-one-out, divergence, seed, scale, and cost analyses make several plausible failure modes visible.
- The paper reports fixed retriever/corpus context and five-seed evidence rather than only a single point estimate.

## Weaknesses

- Gold-answer dependence limits open-ended use and makes label quality a central untested extension point.
- Group-homogeneous outcomes remove the contrast the method needs, and the paper does not provide a general remedy.
- No independently executable implementation or complete reproduction package was identified in the inspected public sources.
- Cost comparisons are detailed within the paper's setup but still depend on matched infrastructure and do not establish deployment efficiency.

## Potential Improvements

| Improvement | Target area | Rationale | Validation approach |
|---|---|---|---|
| Add calibrated soft outcomes | Open-ended supervision | Replace brittle Correct/Incorrect labels with uncertainty-aware preferences or rubric scores | Compare label noise, calibration, and downstream query quality on held-out tasks |
| Add group-contrast safeguards | Training stability | Prevent all-success/all-failure groups from producing an uninformative JSD target | Stratify by group entropy and report gains, search frequency, and loss behavior |
| Release exact training recipe | Reproducibility | Make compute, retriever, corpus snapshot, configs, seeds, and checkpoints inspectable | Independent rerun of main and ablation tables under matched budgets |

## Potential Implementations

- `User`: research engineer. `Goal`: audit per-query credit in a synthetic QA trainer. `Core mechanism`: record masked rollouts, outcome labels, teacher-student JSD, and retrieved evidence coverage. `Inputs`: public QA pairs, fixed local retriever, versioned model. `Outputs`: query-credit receipts and held-out metrics. `Risk controls`: local-only data, no production tools, no private documents. `Evaluation`: masking and label-alignment unit tests plus five-seed replay.
- `User`: RAG platform evaluator. `Goal`: compare retrieval-only, evidence-budget escalation, and SD-style training under fixed cost. `Core mechanism`: share a cost-correctness ledger across Token Tax RAG-style context budgets and query-quality metrics. `Inputs`: public corpus, fixed retriever, token/latency telemetry. `Outputs`: quality-cost frontier. `Risk controls`: offline benchmark and human review of sampled evidence. `Evaluation`: held-out EM, retrieval coverage, latency, and token cost.
- `User`: RL systems researcher. `Goal`: test whether query-position auxiliary losses improve policy learning without suppressing exploration. `Core mechanism`: add a bounded JSD term to a toy GRPO loop and compare with regularized-policy baselines. `Inputs`: synthetic trajectories, known rewards, fixed seeds. `Outputs`: learning curves and failure receipts. `Risk controls`: no real-world control or external action. `Evaluation`: group-entropy sweeps, ablations, and convergence diagnostics.

## Three Ways to Exercise This Research

1. `Synthetic masking test`: generate short typed trajectories, apply future masking, and assert that documents, reasoning, and answers are absent from the teacher view. Success means all leakage tests pass; stop if a non-search span survives.
2. `Offline query-credit benchmark`: use a public QA toy set with a fixed retriever and compare GRPO, GRPO plus JSD, and a no-label control across five seeds. Success means the evaluation reports quality, search frequency, retrieval coverage, and token cost; stop when compute or label assumptions diverge.
3. `Group-degeneracy sweep`: vary group composition from mixed outcomes to all-success/all-failure and measure JSD magnitude, query diversity, and EM. Success means the failure boundary is detected and surfaced; stop before translating the result into production policy.

## Example MVP Product

- `Product name`: Query Credit Evidence Gate.
- `Target user`: Research teams evaluating search-augmented reasoning agents.
- `Problem`: trajectory-level reward hides which queries improve evidence access and makes train/inference leakage easy to miss.
- `Core workflow`: ingest synthetic or public QA rollouts; validate typed-span and masking contracts; compute outcome labels and teacher-student divergence; join query receipts to retrieved-document coverage; compare candidate policies on a held-out set and fixed token budget.
- `Data requirements`: public QA pairs, versioned corpus snapshot, fixed retriever, model metadata, rollout groups, outcome scores, and token/latency telemetry.
- `Architecture`: local CLI or notebook pipeline with immutable rollout receipts, a masking validator, a metric joiner, and a report generator; no external network or consequential action.
- `Success metrics`: EM or task score, retrieval coverage, query duplication rate, group entropy, JSD stability, token cost, latency, and reproducibility across seeds.
- `Risk controls`: synthetic/public data only, local processing, no source-file redistribution, no private prompts, hard group-degeneracy warnings, human review of sampled evidence, and no autonomous deployment decision.
- `Limitations`: it cannot establish factuality, safety, or production readiness; it measures only the configured corpus, retriever, model, and scoring rule.

## Related Research and Reading

| Item | Type | Relevance | URL |
|---|---|---|---|
| Token Tax RAG | Related DEP-A | Evidence-access regimes, token cost, latency, and adaptive escalation | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260727-Token%20Tax%20RAG/2606.20898-whitepaper-review.md |
| DASD Reasoning | Related DEP-E | Temperature scheduling, divergence-aware sampling, mixed-policy distillation, and train/inference mismatch | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260725-DASD%20Reasoning/dasd_reasoning_manuscript.md |
| GPMD Regularized RL | Related DEP-E | Regularized policy optimization, convergence, and objective boundary conditions | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md |
| GRPO and search-augmented reasoning references | Paper citations | Baselines and optimization context named by the paper | https://arxiv.org/html/2605.18299 |

## Source References

| ID | Reference | Supports | Access date | Notes |
|---|---|---|---|---|
| S1 | https://arxiv.org/abs/2605.18299 | Identity, authors, date, subjects, abstract, DOI, and license link | 2026-08-01 | Canonical metadata |
| S2 | https://arxiv.org/html/2605.18299 | Method, experiments, tables, ablations, limitations, appendices, and conclusion | 2026-08-01 | Official full-paper HTML |
| S3 | https://arxiv.org/pdf/2605.18299 | PDF integrity and extracted text cross-check | 2026-08-01 | Local source withheld |
| S4 | https://arxiv.org/e-print/2605.18299 | Equations, source structure, tables, and appendix cross-check | 2026-08-01 | Local source withheld |
| S5 | https://doi.org/10.48550/arXiv.2605.18299 | Persistent identifier | 2026-08-01 | arXiv-issued DOI |
| S6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260727-Token%20Tax%20RAG/2606.20898-whitepaper-review.md | Related RAG/evidence-budget context | 2026-08-01 | Secondary contextual evidence |
| S7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260725-DASD%20Reasoning/dasd_reasoning_manuscript.md | Related distillation context | 2026-08-01 | Secondary contextual evidence |
| S8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md | Related RL context | 2026-08-01 | Secondary contextual evidence |

## Appendix

### Process and Public-Safety Record

The paper was selected uniformly from local PDF-parent units after dedup checks. Its initial archive unit was partial because full-paper HTML was absent; a bounded public-arXiv repair produced a complete verified PDF/HTML/source bundle before review. `extract-arxiv` then ran in local `missing-only` mode and produced a cached record with PDF, HTML, and source text. The dedup/reselection check found no prior paper marker and required no reselection. Public artifacts contain only generated Markdown and derived pointer metadata; source files, caches, extracted text, repair records, and local paths were withheld.

### Reproduction Checklist

- Pin arXiv v1, Qwen2.5 model revisions, veRL revision, retriever, corpus snapshot, seven evaluation splits, and all random seeds.
- Recreate typed trajectory parsing, group outcome scoring, future masking, top-k distribution support, warmup, and JSD loss.
- Reproduce 3B and 7B main tables, five-seed appendix, masking/group/objective ablations, and the 11.9-hour versus 10.3-hour cost comparison under matched hardware.
- Report group entropy, search frequency, retrieval coverage, token counts, latency, and failure cases alongside EM.

## Attribution Block

- Source URL: https://arxiv.org/abs/2605.18299
  - Applies to: source identity, metadata, abstract, authors, date, subjects, DOI, and license link.
- Source URL: https://arxiv.org/html/2605.18299
  - Applies to: full method, experimental evidence, limitations, and appendices.
- Source URL: https://arxiv.org/pdf/2605.18299
  - Applies to: PDF integrity and text cross-checks.
- Source URL: https://arxiv.org/e-print/2605.18299
  - Applies to: source-package structure, equations, tables, and appendices.
- Source URL: https://doi.org/10.48550/arXiv.2605.18299
  - Applies to: persistent paper identity.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260727-Token%20Tax%20RAG/2606.20898-whitepaper-review.md
  - Applies to: related retrieval and evidence-budget context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260725-DASD%20Reasoning/dasd_reasoning_manuscript.md
  - Applies to: related distillation and rollout-mismatch context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md
  - Applies to: related policy optimization and stability context.
- Source files: verified local PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, cache, and repair records.
  - Applies to: all generated sections as private source evidence; zero source files were uploaded.
