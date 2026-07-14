---
title: "RLMF Uncertainty - DEP-E"
generated_at: "2026-07-14"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of reinforcement learning with metacognitive feedback for faithful numerical and linguistic uncertainty expression in large language models."
source_status: "mixed; public URLs and privately retained source files"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-14"
temporal_cutoff: "arXiv:2606.32032v1 and official code commit a087e7a1e49f52aaa701add19cd80699b709fdef"
primary_url: "https://arxiv.org/abs/2606.32032"
stable_identifier: "arXiv:2606.32032v1; DOI 10.48550/arXiv.2606.32032"
confidence_summary: "High for paper identity, method transcription, reported tables, and inspected code; medium for causal and generality claims; low for independent reproducibility because training and evaluation were not rerun."
safety_scope: "research review, offline evaluation, and bounded implementation planning"
distribution_notes: "Paper source files remain in a private archive and are not redistributed; official code is MIT licensed at the inspected commit."
---

# RLMF Uncertainty - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs | Primary metadata | arXiv record | arXiv:2606.32032v1; DOI 10.48550/arXiv.2606.32032 | https://arxiv.org/abs/2606.32032 | arXiv non-exclusive distribution record; source redistribution not relied upon | 2026-07-14 | Inspected |
| S2 | RLMF full paper | Primary artifact | PDF and full-paper HTML | v1, submitted 2026-06-30; 62 PDF pages | https://arxiv.org/pdf/2606.32032 and https://arxiv.org/html/2606.32032 | Private archive copies inspected and withheld; public locators supplied | 2026-07-14 | Inspected in full |
| S3 | RLMF TeX source | Primary artifact | Source package | arXiv:2606.32032v1 | https://arxiv.org/e-print/2606.32032 | Private source package inspected for equations, tables, captions, prompts, and appendices; not deposited | 2026-07-14 | Inspected in full |
| S4 | yale-nlp/RLMF | Official implementation | GitHub repository | commit a087e7a1e49f52aaa701add19cd80699b709fdef | https://github.com/yale-nlp/RLMF | MIT license; repository documentation and key training files inspected without execution | 2026-07-14 | Inspected at pinned commit |
| S5 | MetaFaith | Direct predecessor and baseline | ACL Anthology paper | EMNLP 2025, DOI 10.18653/v1/2025.emnlp-main.1505 | https://aclanthology.org/2025.emnlp-main.1505/ | Primary publication record and full-paper locator | 2026-07-14 | Inspected |
| S6 | Finetuning Language Models to Emit Linguistic Expressions of Uncertainty | Direct baseline | arXiv paper | arXiv:2409.12180v1 | https://arxiv.org/abs/2409.12180 | Primary paper record; called FUT in the reviewed paper | 2026-07-14 | Inspected |
| S7 | SelfCheckGPT | Methodological predecessor | ACL Anthology paper | EMNLP 2023, DOI 10.18653/v1/2023.emnlp-main.557 | https://aclanthology.org/2023.emnlp-main.557/ | Primary publication record for sampling-consistency uncertainty context | 2026-07-14 | Inspected through primary citation and paper record |
| S8 | PAC Confidence - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260713 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence | Repository synthesis context, not evidence for RLMF experimental claims | 2026-07-14 | Inspected |
| S9 | OViP Preference - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260714 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference | Repository synthesis context, not evidence for RLMF experimental claims | 2026-07-14 | Inspected |
| S10 | ConMax Reasoning - DEP-E | Related Black Lake artifact | Markdown | DEP-E-20260708 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260708-ConMax%20Reasoning | Repository synthesis context, not evidence for RLMF experimental claims | 2026-07-14 | Inspected |

The reviewed paper is by Gabrielle Kaili-May Liu and Arman Cohan of Yale University, and Avi Caciularu, Gal Yona, and Idan Szpektor of Google Research. It is a 2026 arXiv preprint in Computation and Language and Artificial Intelligence. No conference acceptance or independent replication was identified at the review cutoff.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S3 | Primary paper | Metadata, abstract, full text, appendices, TeX equations, tables, prompts, and figure captions | Identity, scope, method, and reported results | High | v1 preprint; no peer-review outcome established |
| E2 | S2-S3, Method and Appendix B | Primary method evidence | Grouped completions, composite rewards, `F_gold`, `F_pred`, metacognitive score `Z_g`, and piecewise advantage scaling | RLMF mechanism | High for transcription | Mathematical soundness and optimization behavior were not independently proved |
| E3 | S2-S3, Appendix D | Primary implementation evidence | Pre-SFT, LoRA, GRPO, 32 completions, 2,000 selected examples, 1,500 steps, learning-rate sweep, GPU topology, and checkpoint selection | Training reconstruction and compute boundary | High for reported setup | No full cost, energy, wall-clock, or multi-seed accounting |
| E4 | S2-S3, Tables 1 and 9 | Primary empirical evidence | Ten-dataset cMFG-star, accuracy, and Brier results for Llama3.1-8B and Qwen3-8B plus smaller Qwen models | Main performance claims | High for transcription | Author-reported; no confidence intervals or independent rerun |
| E5 | S2-S3, Tables 2, 3, and 17-19 | Primary empirical evidence | Training-task robustness and random, active, and metacognitive data-selection comparisons | Cross-task and selection claims | High for transcription | Model and prompt specific; one reported seed |
| E6 | S2-S3, Appendix E | Primary ablation evidence | Reward, prompt, advantage normalization, data size, pre-SFT, `Z_g`, advantage placement, `k`, threshold, and rewriting ablations | Component contribution | Medium-high | Many choices were optimized on the same evaluation pipeline; multiple-comparison uncertainty is unreported |
| E7 | S2-S3, Appendix G | Primary human-study evidence | Three expert annotators, 120 cases, four criteria, 0.93 Krippendorff alpha, and 95-98 percent win rates | Linguistic quality claim | High for study description | Small expert pool; no compensation; correctness was not the target criterion |
| E8 | S4 | Official code | Trainer, sample configuration, rewards, requirements, README, and reproduction commands at pinned commit | Implementation availability and equation/code comparison | High for inspected files | Code was not installed or executed; no release or container image was identified |
| E9 | S5-S7 | Primary related work | MetaFaith, FUT, and sampling-consistency uncertainty methods | Novelty and baseline context | Medium-high | This is selective context, not a complete systematic literature review |
| E10 | S8-S10 | Related DEP artifacts | Statistical confidence bounds, on-policy preference loops, and confidence-shaped reasoning optimization | Cross-DEP synthesis | Medium | Conceptual bridge only; no joint experiment exists |
| E11 | S2-S4 | Cross-source audit | Paper uses strict `< tau` in one equation while pinned code counts `<= mc_threshold` | Internal consistency note | High | Difference affects only exact-boundary cases and is likely operationally minor |
| E12 | S2-S4 | Reviewer analysis | Intrinsic confidence is estimated by sampled-response consistency judged by Qwen3-32B | Proxy and governance boundary | High for mechanism; medium for implication | Does not establish access to a model's latent belief state |
| E13 | S2-S3, compact Table 3 and full appendix data-selection table | Primary quantitative audit | Qwen3-8B random-selection accuracy is printed as 0.23 in the compact table and 0.53 in the full table | Internal result consistency | High for transcription | The source does not resolve which value is intended |

## Executive Summary

The paper proposes reinforcement learning with metacognitive feedback, or RLMF, as a modification to group-relative preference optimization. Instead of treating a completion's task reward as the only learning signal, RLMF asks the policy model to estimate how faithfully it expressed its own uncertainty. The method compares that self-estimate with an externally computed target and uses the resulting metacognitive score to amplify the faithfulness component of the advantage for above-average completions. A companion data-selection method chooses examples from both extremes of the model's own self-assessment distribution. A second, decoupled stage rewrites numerical confidence into natural-language hedges.

The application is faithful calibration: matching expressed confidence to an estimate of intrinsic confidence, not matching confidence directly to factual correctness. The distinction is useful. A model may be factually calibrated in aggregate while saying it is confident for reasons that do not track its own response variability; conversely, a faithfully expressed low confidence does not make a wrong answer correct. RLMF explicitly optimizes both faithfulness and accessory objectives for correctness, factual calibration, and format adherence.

The author-reported results are strong within the evaluation frame. For Llama3.1-8B-Instruct, average cMFG-star rises from 0.60 for the base model to 0.84 after RLMF and 0.82 after linguistic rewriting; standard RL reaches 0.77. For Qwen3-8B, the corresponding values are 0.54, 0.83, 0.83, and 0.51. The model family pattern matters: standard RL helps Llama but collapses on several Qwen tasks, while RLMF remains above 0.80 on average. Metacognitive selection also beats random and active-learning-style selection in the reported comparisons. In a 120-case human study, three expert annotators prefer RLMF outputs to FUT on diversity, naturalness, helpfulness, and contextual suitability at rates from 95 to 98 percent, with reported inter-annotator agreement of 0.93.

These findings are promising evidence for reward shaping with self-evaluation, not proof that a model has acquired broad metacognition. The target called intrinsic confidence is a behavioral proxy: each sentence is compared against 20 sampled responses, with consistency judged by Qwen3-32B. The metacognitive target is therefore accuracy at predicting alignment to a model-and-judge-dependent consistency procedure. The main tables report no multi-seed uncertainty, and the best checkpoint is selected using in-domain test faithful-calibration performance before evaluation across tasks. Those choices weaken clean causal and held-out interpretations. The official code is available under MIT and matches the main mechanism at pinned commit `a087e7a`, apart from a minor strict-versus-inclusive threshold boundary.

The durable engineering lesson is narrower and stronger than the paper's broad alignment language: self-assessment can be useful as a conditional ranking signal when it is attached to an independently measured task component, logged as a separate quantity, and prevented from overriding primary performance. Production use should expose the proxy, judge, confidence support, factual accuracy, abstention behavior, and shift status independently. Uncertainty language is a user-interface control, not a substitute for verification.

## Detailed Summary

### Problem and Conceptual Boundary

The paper separates factual calibration from faithful calibration. Factual calibration asks whether events assigned confidence 0.8 are correct about 80 percent of the time. Faithful calibration asks whether the confidence the model states is aligned with an estimate of what the model internally supports. The paper operationalizes the latter with response consistency. If independently sampled answers tend to support a sentence, its intrinsic-confidence proxy is high; if they disagree, it is low.

This operational definition avoids requiring model logits from proprietary systems and works at the sentence level, but it should not be read literally as direct access to internal belief. Sampling temperature, decoding, semantic equivalence, the number of samples, and the NLI judge all affect the estimate. A model could become aligned to this estimator while remaining poorly calibrated under another estimator or under real-world correctness. The paper partly addresses this by tracking accuracy and Brier score, but the three quantities remain distinct.

### Stage 0: Output-Format Preparation

Before RL, the authors perform supervised fine-tuning so each response is segmented into sentence tags followed by numerical confidence tags. The reported setup uses 1,800 training and 200 validation examples, five epochs, learning rate `3e-5`, and LoRA rank 32 with alpha 64 and dropout 0.05. This stage is not merely cosmetic. The reward pipeline depends on parseable sentence-confidence pairs, and ablations show pre-SFT is important for generalization and stable format adherence.

### Stage 1: Composite Reward and Standard Advantage

For a query `q`, the policy samples a group of `G=32` completions. Each completion `r_g` contains sentence-confidence pairs `(s_i, c_i)`. The pipeline computes a weighted reward with strict and soft format terms, factual calibration, correctness, and a dominant faithfulness term. The appendix reports default weights 3, 3, 1, 1, and 12 respectively. Faithfulness uses a quadratic score that is highest when expressed confidence `c_i` equals the estimated intrinsic confidence `g_i`.

The implementation removes group standard-deviation normalization, following the DR-GRPO motivation that normalization can introduce question-difficulty bias. Standard centered advantages are therefore component-wise differences from group means rather than z-scores.

### Metacognitive Target

For each completion, the paper defines a thresholded gold faithful-calibration level:

```text
F_gold(g) = (1 / N_g) * sum_i I(|c_i - g_i| < tau)
```

The model is separately prompted to predict how faithfully its expressed confidence aligns with its intrinsic confidence, producing `F_pred(g)`. The metacognitive score is a quadratic agreement measure:

```text
Z_g = 1 - (F_pred(g) - F_gold(g))^2
```

With `tau=0.10`, `Z_g` lies in `[0,1]`. It is high when the model accurately estimates its completion-level faithful-calibration performance, whether that performance is high or low. That distinction is important: the model is rewarded for knowing how well it did, while primary task quality still determines which completions qualify for amplification.

### RLMF Advantage Scaling

The full reward is split into faithfulness `f_g` and other objectives `o_g`. For completions whose faithfulness is above the group mean, RLMF scales the centered faithfulness advantage by `k + Z_g`, with `k=1`. Below-mean completions retain the ordinary centered faithfulness term:

```text
A_RLMF(g) = (o_g - mean(o))
          + (f_g - mean(f)) * (k + Z_g), if f_g > mean(f)
          + (f_g - mean(f)),             otherwise
```

This asymmetric gate is the core contribution. Metacognitive accuracy cannot rescue a low-faithfulness completion. It only determines how strongly an already above-average faithfulness completion is reinforced. The pinned trainer code implements this split directly and requires `scale_rewards='none'`. It also clamps the positive scaling factor at zero as a sanity check.

The design is better understood as conditional gain control than as a new reward. The metacognitive signal changes the gradient weight assigned to selected examples without being added indiscriminately to the objective. The paper's ablations support this choice: applying the score to the whole advantage or the whole group performs worse, and directly adding a metacognitive reward creates more opportunities for gaming.

### Metacognitive Data Selection

The companion selection method runs before RL. The model answers training prompts with linguistic uncertainty and then rates, from 0 to 100, how well its language matches its internal confidence. For a target set of 2,000 examples, the system selects half from the highest scores and half from the lowest scores. High-score examples expose behavior the model believes it handles well; low-score examples expose perceived failures.

This method beats reported random selection and an active-learning-style baseline based on low ground-truth faithfulness. On Llama3.1-8B, average cMFG-star is 0.84 for metacognitive selection, 0.80 for random, and 0.79 for active selection. On Qwen3-8B, the values are 0.83, 0.76, and 0.72. The result is model specific: the score is generated by the target model, and Appendix ablations show that different ranking strategies can behave differently across models.

### Stage 2: Numerical-to-Linguistic Rewriting

The second stage maps each numerical confidence bin, of width 0.05, to a set of candidate hedges drawn from human-rated phrase inventories. The main configuration provides 20 candidate hedges per bin to Gemini-2.5-Flash-Lite along with the original response and task or user context. The rewriting model edits the response once to integrate uncertainty naturally while preserving content.

This decoupling has practical value. RL training is performed once; language style can then be changed for audience, domain, or register. It also avoids teaching the policy a narrow inventory of repetitive phrases. The cost is a second model dependency and a new failure surface: a rewriter can alter facts, smooth away distinctions, or optimize perceived style. The reported human study evaluates linguistic quality, not a comprehensive factual-preservation audit.

### Datasets, Models, and Evaluation

The evaluation uses up to 1,000 test examples from each of ten datasets: PopQA, SelfAware, SimpleQA, HaluEval, MMLU, SciQ, MATH, UMWP, ARC-Challenge, and SuperGLUE. These cover open-domain QA, answerability, hallucination detection, multiple-choice knowledge, science, mathematics, word problems, and language understanding. Main training uses 2,000 metacognitively selected PopQA examples, with robustness runs trained on SelfAware, HaluEval, or UMWP.

Models are Llama3.1-8B-Instruct and Qwen3 at 1.7B, 4B, and 8B. Baselines include the unchanged model, MetaFaith prompting, FUT supervised fine-tuning, standard RL, and prompted proprietary models. Accuracy is scored by Gemini-2.5-Flash-Lite, while intrinsic confidence during training and evaluation relies on Qwen3-32B consistency judgments. The system therefore contains multiple evaluator models whose errors may correlate with the target behavior.

The main faithful-calibration metric is cMFG-star. Instance faithfulness is `1 - mean(|expressed - intrinsic|)`. cMFG-star places examples into equal-mass intrinsic-confidence bins and weights bin faithfulness by the bin's width over empirical confidence support. This addresses empty-bin and density-dominance problems in earlier cMFG variants. However, normalization over observed support means a model confined to a narrow confidence range is not penalized solely for lacking low- or high-confidence examples. Support width and distribution should be reported alongside the scalar metric.

### Main Results

For Llama3.1-8B-Instruct, the average cMFG-star/accuracy/Brier triples are 0.60/0.31/0.33 for the base model, 0.67/0.28/0.36 for MetaFaith, 0.66/0.31/0.29 for FUT, 0.77/0.40/0.20 for standard RL, 0.84/0.41/0.26 for RLMF, and 0.82/0.41/0.26 after rewriting. RLMF improves faithful calibration substantially and preserves the standard-RL accuracy gain, though standard RL has the better Brier score in this model.

For Qwen3-8B, the triples are 0.54/0.55/0.31 for the base model, 0.63/0.51/0.29 for MetaFaith, 0.67/0.38/0.41 for FUT, 0.51/0.59/0.26 for standard RL, 0.83/0.57/0.19 for RLMF, and 0.83/0.57/0.19 after rewriting. Here standard RL is unstable across tasks, including very low cMFG-star on HaluEval and ARC-Challenge, while RLMF is consistently strong.

The paper also reports average prompted frontier-model cMFG-star of 0.70 for Gemini 3.1 Pro, 0.66 for Gemini 3 Flash, and 0.61 for GPT-5. These comparisons demonstrate that the specialized open-weight systems score higher on the paper's metric. They do not establish broader model superiority because the systems differ in training access, prompts, task accuracy, inference settings, and evaluator relationships.

Smaller Qwen variants follow the same broad pattern: Qwen3-4B reaches 0.83 numerically and 0.85 after rewriting; Qwen3-1.7B reaches 0.82 and 0.83. The paper reports training-task robustness of approximately 0.80 to 0.84 across PopQA, SelfAware, HaluEval, and UMWP.

### Ablations and Causal Evidence

The appendix is unusually extensive. Removing strict or soft format rewards causes malformed outputs and reduces cMFG-star. Removing factual calibration or accuracy rewards weakens the corresponding accessory objective. A quadratic faithfulness reward outperforms tested linear and cross-entropy alternatives. The selected system prompt and removal of advantage normalization matter materially.

For the metacognitive mechanism, unnormalized quadratic `Z_g` performs best among tested formulations. Scaling only above-mean faithfulness completions beats scaling the whole advantage or every completion. `k=1` outperforms 0, 2, and 4; `tau=0.10` outperforms 0.05. Pre-SFT plus RLMF plus metacognitive data selection is the strongest tested combination. A 2,000-example training set outperforms 1,000 and 4,000 in the reported configuration, which suggests more data is not automatically better when selection and reward distributions interact.

These ablations support sensitivity to the proposed mechanism, but they do not isolate all causal alternatives. The same evaluation proxies guide reward design, hyperparameter selection, checkpoint selection, and final scoring. A robust follow-up should pre-register a small number of choices, use a separate validation split, report multiple training seeds, and evaluate with independent human and model judges.

### Human Evaluation

Three graduate-student annotators who work directly with LLMs evaluate 120 query-model combinations: 20 examples each from Natural Questions, SciQ, and SelfAware for two models. Each case presents three FUT responses and three RLMF-plus-rewriting responses in randomized groups. Annotators judge diversity, naturalness, helpfulness, and contextual appropriateness, after a ten-example calibration exercise.

The reported win rates are 98, 98, 95, and 96 percent, with Krippendorff alpha 0.93. This is strong evidence that the rewriting pipeline avoids FUT's formulaic hedging under the provided rubric. It is weaker evidence about correctness, real-user reliance, or high-stakes decisions because annotators were explicitly told not to score answer correctness, and only three expert annotators participated.

### Official Code Audit

The official repository is public, MIT licensed, and pinned here to `a087e7a1e49f52aaa701add19cd80699b709fdef`. Its README maps baseline evaluation, MetaFaith, RLMF training, data selection, checkpoint evaluation, and rewriting. The sample configuration pins TRL 0.23.0 behavior, 32 generations, LoRA rank 64, 1,500 steps, 2,000 examples, `beta=0.1`, and the paper's `k=1` and `tau=0.10` choices.

The trainer separates the last reward function as faithfulness, computes group means for faithfulness and other terms, obtains auxiliary metacognitive scores from the faithfulness reward, and applies the piecewise formula described above. The reward implementation computes sampled-response intrinsic confidence, asks for a metacognitive prediction, and returns both the task reward and metacognitive score.

One minor discrepancy was found: the paper's displayed `F_gold` equation uses `|c_i-g_i| < tau`, while the pinned code increments the count when `abs(p-g) <= mc_threshold`. This only changes exact-threshold cases and is unlikely to explain the reported gains, but it should be aligned for specification precision. The code was not installed, dependency-resolved, or executed, so this is a static implementation audit rather than reproduction.

A separate source-table inconsistency remains unresolved. The compact data-selection table reports Qwen3-8B random-selection accuracy as 0.23, whereas the full appendix table reports 0.53 for the same cMFG-star 0.76 and Brier 0.18 row. This review does not choose between them; downstream use should consult released result artifacts or obtain an author correction.

### Limitations and Boundary Conditions

The most important limitation is construct validity. The paper names sampled consistency an estimate of intrinsic confidence, but no experiment establishes that it corresponds to an inaccessible latent belief rather than a decoding-and-judge-specific behavioral property. RLMF may teach the model to predict and match this proxy. That remains useful, but it is narrower than broad metacognitive awareness.

The second limitation is evaluation independence. Training, checkpoint selection, and final evaluation share prompts, metrics, judge families, and the PopQA in-domain test signal. The official instructions explicitly evaluate checkpoints on the in-domain test set to choose the best checkpoint. A validation split should be used instead, leaving all test sets untouched until the final run.

Third, the paper reports one seed (`42`) for training details and does not provide confidence intervals or significance tests for the main model tables. The human study reports agreement but not uncertainty around win rates. The large number of ablations and hyperparameters increases the need for repeated runs and a declared selection protocol.

Fourth, the method is expensive. The main setup uses four training GPUs, one rollout GPU, and one Qwen3-32B judge GPU, with 32 completions per prompt and consistency estimation. The repository states a minimum of three GPUs and demonstrates six, with two more optional for parallel checkpoint evaluation. No complete wall-clock, token, energy, or API-cost ledger is reported.

Finally, uncertainty expression can change user behavior even when factual reliability does not improve. Natural, context-sensitive hedges can be beneficial, but they can also make a system more persuasive. High-stakes use requires direct correctness checks, abstention policies, source verification, and user studies that measure reliance rather than stylistic preference alone.

### Cross-DEP Synthesis

PAC Confidence contributes a statistical perspective: confidence should include support, interval width, and a declared distributional envelope, not only a point estimate. RLMF currently optimizes a pointwise behavioral proxy. A combined system would report confidence support and fail closed when sampling or evaluation conditions shift.

OViP Preference contributes a feedback-loop perspective. Its model-specific on-policy negatives resemble RLMF's model-specific completions and self-selected examples. Both can amplify evaluator blind spots because the judge determines which examples receive stronger learning signals. Judge disagreement, provenance, and held-out human audit should therefore be first-class records.

ConMax Reasoning contributes a reward-governance contrast. It uses confidence from a frozen auxiliary reasoner to preserve answer and thinking quality while compressing traces. RLMF uses a self-prediction score to scale faithfulness advantages. Together they suggest a general pattern: confidence-shaped optimization should be subordinate to an independently measured task predicate, and the confidence channel should never silently become the task objective.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Direct Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | RLMF improves faithful calibration over standard RL by up to 63 percent. | Author empirical claim | E4, task-level table comparisons | Supported for at least one reported task/configuration; the maximum is not an average and lacks multi-seed uncertainty. | High for transcription; medium for generality |
| C2 | RLMF yields average cMFG-star above 0.80 across tested model families and tasks. | Author empirical claim | E4-E5 | Supported by reported averages and per-task tables for the selected checkpoints. | High for reported experiments |
| C3 | Metacognitive data selection outperforms random and active-learning-style selection. | Author empirical claim | E5 | Supported in the tested Llama and Qwen configurations; model-specific and not proven for other tasks or objectives. | Medium-high |
| C4 | The two-stage pipeline produces more natural and context-adaptable uncertainty than FUT. | Author human-study claim | E7 | Strong under the stated expert rubric; does not establish factual preservation or calibrated user reliance. | Medium-high |
| C5 | RLMF improves broad metacognitive awareness. | Author interpretation | E2, E6, metacognitive-score curves | Evidence shows improvement on predicting one faithful-calibration proxy; broad metacognition is not directly measured. | Low-medium |
| C6 | cMFG-star improves cross-model faithful-calibration comparison. | Author metric claim | E4 and metric appendix | Equal-mass bins and width weighting address documented sparse-bin issues; empirical-support normalization still needs support-width disclosure. | Medium-high |
| C7 | The method preserves task accuracy and factual calibration. | Author empirical claim | E4 | Broadly supported relative to base and prior FC baselines; standard RL sometimes has a better Brier score, and no statistical uncertainty is given. | Medium |
| C8 | The official code implements the paper's central advantage scaling. | Implementation claim | E8, E11 | Confirmed statically at the pinned commit, with a minor `<` versus `<=` threshold discrepancy. | High |
| C9 | This is the first end-to-end numerical and linguistic FC pipeline and first RLMF use of metacognitive feedback. | Author novelty claim | E1, E9 | Plausible but not proven by this selective review of a fast-moving field; should remain scoped as an author claim. | Low-medium |

## Methodology

- `Research objective`: Preserve a complete, source-grounded review of arXiv:2606.32032v1, reconstruct its mechanism and evidence, inspect the official implementation, and translate the findings into bounded Black Lake implementation directions.
- `Sources inspected`: Canonical arXiv metadata, the complete 62-page PDF, full-paper HTML, TeX source and figures, the official code repository at a pinned commit, MetaFaith and FUT primary records, SelfCheckGPT context, and exactly three related Black Lake DEP-E artifacts.
- `Discovery strategy`: Local source-cache inspection, PDF parsing, HTML and TeX extraction, figure inspection, caption and table enumeration, citation chasing to primary records, web verification of current public sources, Git commit pinning, and static inspection of key training files.
- `Inclusion criteria`: Sources were included when they established identity, exposed method/results/limitations, supplied official implementation evidence, represented direct baselines, or supported a concrete cross-DEP relationship.
- `Exclusion criteria`: Secondary commentary, citation-count claims, unverified social discussion, abstract-only summaries, and unrelated calibration papers were excluded. Full dependency installation and model/dataset downloads were excluded because no reproduction was requested and they would consume substantial compute and storage.
- `Analytical approach`: Mixed technical reconstruction, quantitative audit, code inspection, construct-validity critique, safety/governance review, and product translation.
- `Evidence handling`: Author claims, direct observations, code findings, reviewer inferences, and future proposals are labeled separately. Exact numbers are attributed to paper tables and are not presented as independently reproduced.
- `Uncertainty handling`: Missing seeds, confidence intervals, costs, independent replication, and venue status remain explicit. Broad novelty and metacognition claims are qualified rather than silently accepted.
- `Extraction process`: Text was extracted independently from PDF, HTML, and TeX; core figures were visually inspected; equations and table values were checked against source; selected code files were fetched from a shallow blob-filtered repository checkout.
- `Version control`: Paper version v1 and official code commit `a087e7a1e49f52aaa701add19cd80699b709fdef` are the temporal anchors.
- `Cross-checking`: Main result values, human-study counts, training configuration, equation/code behavior, and repository instructions were checked across at least two primary representations where available.
- `Safety handling`: Implementation paths are offline, use public or synthetic data, prohibit consequential automation, and require independent verification and human review.
- `Reviewer stance`: DEP-ready preservation with critical review and bounded engineering translation.

## Scope, Constraints, and Assumptions

- `Scope`: RLMF, metacognitive data selection, numerical-to-linguistic rewriting, cMFG-star, the full reported experiment suite, official implementation structure, and three Black Lake conceptual bridges.
- `Temporal boundary`: Evidence available through 2026-07-14, anchored to arXiv v1 and official repository commit `a087e7a`.
- `Evidence limits`: No training, inference, judge calls, benchmark downloads, dependency installation, statistical reanalysis from raw predictions, or user study was performed.
- `Assumptions`: The archived files correspond to arXiv v1; extracted equations/tables preserve the submitted source; public repository files at the pinned commit are the authors' intended implementation.
- `Constraints`: Source files remain private; public artifacts contain URLs and summaries only. Compute and disk use were intentionally bounded. Proprietary model versions and API behavior may change.
- `Out of scope`: End-to-end reproduction, proof of latent model beliefs, medical/legal/financial deployment, autonomous model promotion, and certification of broad metacognition.
- `Intended use`: Research review, DEP deposition, replication planning, evaluation design, and defensive product ideation.
- `Audience`: ML researchers, alignment and evaluation engineers, agent-system developers, and Black Lake reviewers.
- `Depth target`: Full manuscript report and implementation brief.
- `Reproducibility boundary`: The official code and instructions make reproduction more feasible, but exact models, datasets, API judges, GPU topology, checkpoints, and raw result artifacts are still required.
- `Operational boundary`: Uncertainty signals may support offline evaluation and supervised decision aids; they must not authorize high-impact actions by themselves.
- `Data sensitivity`: Reviewed materials are public research artifacts; private cache paths and source binaries are withheld.

## Observations

- `Mechanism observation`: RLMF's strongest design choice is not self-evaluation alone; it is the restriction that self-evaluation amplifies only above-average primary-task behavior.
- `Construct observation`: “Intrinsic confidence” is a named proxy derived from stochastic output agreement and an NLI judge. Treating it as a measurement procedure rather than a hidden mental state makes the results easier to reproduce and critique.
- `Evaluation observation`: The reported Qwen standard-RL failures are as informative as the best scores. They show that ordinary reward optimization can improve accuracy while harming faithful uncertainty on particular tasks.
- `Metric observation`: cMFG-star reduces sparse-bin distortion, but release reports should show empirical confidence support and per-bin counts so a narrow-range model cannot look complete through one scalar.
- `Code observation`: The official implementation is unusually legible about RLMF-specific changes and exposes the central hyperparameters, but it inherits a tightly pinned and GPU-heavy stack.
- `Governance observation`: RLMF contains three different confidence channels - expressed confidence, sampled-consistency confidence, and confidence in faithful-calibration performance. Logs should name them explicitly to prevent semantic collapse.
- `Cross-source pattern`: PAC Confidence, OViP, ConMax, and RLMF all improve decisions by adding a second evidence channel. Each also risks circularity when that channel is produced or judged by the same model ecosystem.
- `Reviewer hypothesis`: An ensemble-disagreement metacognitive score, evaluated by a held-out judge and human-labeled audit set, may preserve RLMF's ranking benefit while reducing dependence on one Qwen3-32B consistency judge.

## Considerations

Uncertainty communication is a behavioral interface. A model can learn to sound appropriately cautious without becoming more correct, and a correct model can learn caution that causes users to under-rely on it. Evaluation should therefore measure three separate outcomes: factual correctness, alignment between stated and operational confidence, and human reliance quality. The paper covers the first two more directly than the third.

The self-referential loop requires governance. The policy generates answers, another sample set from the policy defines intrinsic confidence, an evaluator model judges consistency, and the policy predicts how well its own expressed confidence matched that target. Errors can correlate across all stages. Versioned judge ensembles, frozen evaluation prompts, disagreement retention, and independent audit sets are more important than a single aggregate score.

Checkpoint selection should be repaired before replication. The repository's documented path evaluates checkpoints on the in-domain test set, then uses the best checkpoint for downstream evaluation. A separate validation set should govern checkpoint and hyperparameter choice; the test set should be touched once. This is a straightforward improvement with high evidentiary value.

The rewriting layer should have a semantic-preservation gate. Candidate outputs can be checked against the numerical response using entailment, entity/value diffs, and human review of disagreements. The hedge should alter epistemic presentation, not facts, scope, or recommendation strength. High-stakes domains also need explicit abstention and source verification rather than more polished hedging.

## Strengths

- The paper defines a concrete, inspectable mechanism for using self-assessment without allowing it to override below-average task behavior.
- The two-stage design separates expensive calibration training from adaptable language realization.
- Experiments span four open-weight model sizes and ten heterogeneous tasks, with multiple training-task robustness checks.
- The appendix provides extensive reward, prompt, normalization, data-size, selection, scaling, and rewriting ablations.
- Human evaluation tests diversity and contextual fit rather than relying only on automated hedge scores.
- Official MIT-licensed code and sample commands are available, and the pinned implementation matches the principal equation closely.
- Accuracy and Brier score are reported beside faithful calibration, making some trade-offs visible.

## Weaknesses

- The “intrinsic confidence” target is a model-and-judge-dependent consistency proxy, not validated access to latent belief.
- Main results lack multi-seed means, variance, confidence intervals, and significance tests.
- The compact and full data-selection tables disagree on Qwen3-8B random-selection accuracy, 0.23 versus 0.53.
- In-domain test performance is used for checkpoint selection, weakening held-out claims.
- Reward design, selection, checkpointing, and evaluation share proxies and judge infrastructure, increasing circularity risk.
- cMFG-star can conceal limited confidence support unless support width and counts are also shown.
- The human study is small, expert-only, and focused on style rather than correctness or user reliance.
- The training pipeline is compute intensive, with no complete wall-clock, token, energy, or monetary cost report.
- “State of the art,” “first,” and broad metacognitive-awareness claims exceed what this selective, unreproduced preprint establishes independently.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Use train/validation/test separation for all selection | Evaluation | Current instructions select checkpoints on in-domain test FC | Cleaner generalization evidence | More held-out data and runs | Pre-register splits and evaluate test once |
| Report at least five training seeds | Statistics | One reported seed cannot characterize RL variance | Reliable effect sizes and failure rates | Substantial GPU cost | Mean, standard deviation, paired bootstrap, and seed-level tables |
| Audit multiple intrinsic-confidence estimators | Construct validity | Sampling consistency plus one NLI judge may be proxy specific | Shows whether gains transfer across uncertainty definitions | More inference and judge disagreement | Compare semantic entropy, logit access where available, ensembles, and human consistency labels |
| Publish support-aware cMFG-star cards | Metrics | Scalar normalization can hide narrow confidence range | More interpretable comparisons | Additional reporting complexity | Include support width, bin counts, per-bin error, and bootstrap intervals |
| Add rewrite semantic-preservation checks | Stage 2 | Rewriting can change content | Safer linguistic adaptation | False positives and extra latency | Entity/value diff, bidirectional entailment, and blinded human audit |
| Separate training and evaluation judges | Governance | Shared judge families can create circular gains | Stronger independence | Higher API or GPU cost | Rotate frozen evaluators and report judge disagreement |
| Publish full compute and artifact manifest | Reproducibility | GPU counts alone do not support cost planning | Reproducible resource envelope | Operational logging work | Tokens, wall time, GPU hours, energy estimate, checkpoints, and raw aggregate results |
| Align `< tau` and `<= tau` specifications | Code/specification | Exact boundary differs between paper and pinned code | Removes ambiguity | Negligible | Unit test exact-threshold cases and update one side |

## Potential Implementations

1. `Uncertainty Evidence Gate`
   - `User`: Model evaluation and release-review teams.
   - `Goal`: Prevent a model from passing release solely because a faithful-calibration scalar improves.
   - `Core mechanism`: Evaluate expressed/intrinsic alignment, factual accuracy, Brier score, support width, abstention, judge disagreement, and distribution shift as independent gates.
   - `Required inputs`: Versioned model outputs, sampled responses, public or approved labels, frozen judge versions, slice metadata, and release thresholds.
   - `Outputs`: Pass/review/reject decision, per-slice evidence card, unsupported-range warning, and immutable manifest.
   - `Risk controls`: Offline only, no automatic deployment, minimum-support requirements, independent human audit, and fail-closed shift handling.
   - `Evaluation`: Seeded regression fixtures must reject narrow-support, judge-disagreement, accuracy-loss, and rewrite-drift failures.

2. `Metacognitive Ranking Sandbox`
   - `User`: Researchers testing self-evaluation signals on small public models.
   - `Goal`: Isolate whether conditional advantage scaling helps beyond adding another reward.
   - `Core mechanism`: Run a synthetic or small public task with fixed rewards, compare standard centered advantage, direct metacognitive reward, and RLMF-style gated scaling.
   - `Required inputs`: Public model, synthetic confidence targets, deterministic reward fixtures, multiple seeds, and fixed evaluation split.
   - `Outputs`: Seed-level learning curves, proxy-transfer matrix, and gradient-weight diagnostics.
   - `Risk controls`: No private data, no consequential tasks, bounded compute, and no unsupported claims of consciousness or latent belief.
   - `Evaluation`: The gated method must improve held-out task/proxy results across seeds without degrading factual performance.

3. `Contextual Hedge Preservation Auditor`
   - `User`: Teams adapting numerical uncertainty to user-facing language.
   - `Goal`: Verify that a rewriting layer changes epistemic style without changing claims.
   - `Core mechanism`: Compare source and rewritten responses using claim extraction, entity/value diffs, bidirectional entailment, hedge-intensity mapping, and human review for disagreements.
   - `Required inputs`: Original numerical-confidence responses, rewritten text, intended register, approved hedge map, and reviewer labels.
   - `Outputs`: Preservation score, changed-claim list, confidence-language trace, and review queue.
   - `Risk controls`: Human approval for high-impact outputs, no automatic medical/legal/financial advice, and retention of the original response.
   - `Evaluation`: Public benchmark and synthetic mutation tests measure factual drift detection and acceptable style adaptation.

## Three Ways to Exercise This Research

1. `Equation-and-code conformance lab`: Objective: verify the RLMF advantage formula without training a model. Inputs: seeded arrays for faithfulness rewards, other rewards, and metacognitive scores. Method: implement the paper equation and pinned-code behavior, compare every branch including exact-threshold fixtures, and inspect gradient weights. Output: deterministic conformance table. Success criterion: all ordinary cases match and the strict/inclusive threshold difference is explicitly isolated. Stop condition: halt if the implementation requires network calls or unpinned dependencies. Safety boundary: synthetic arrays only.
2. `Proxy-transfer benchmark`: Objective: test whether improvement transfers beyond one intrinsic-confidence estimator. Inputs: public QA outputs, repeated samples, two independent semantic-consistency judges, optional logit confidence for an open model, and held-out labels. Method: train or simulate ranking on one proxy and evaluate expressed-confidence alignment against every other proxy plus correctness. Output: cross-proxy transfer matrix with bootstrap intervals. Success criterion: gains persist across estimators without accuracy loss. Stop condition: do not interpret estimator agreement as proof of latent belief. Safety boundary: public data and offline evaluation only.
3. `Rewrite drift challenge`: Objective: falsify semantic preservation in Stage 2 before user deployment. Inputs: public responses with numerical confidence, controlled factual mutations, several audience contexts, and blinded reviewers. Method: run the rewriter, inject mutation fixtures, audit facts and hedge intensity, and compare reliance judgments. Output: drift, detection, naturalness, and reliance report. Success criterion: every seeded factual mutation is caught and acceptable rewrites preserve claims. Stop condition: reject the rewriter if high-impact claims change or uncertainty language increases inappropriate reliance. Safety boundary: no real high-stakes recommendations.

## Example MVP Product

- `Product name`: Uncertainty Release Card
- `Target user`: ML evaluation engineers and model-governance reviewers.
- `Problem`: A model can improve one calibration metric while losing accuracy, narrowing its confidence support, exploiting a judge, or introducing factual drift during linguistic rewriting.
- `Core workflow`: Import a versioned aggregate result bundle; validate required fields and split provenance; compute faithful and factual calibration summaries; report confidence support and evaluator disagreement; compare original and rewritten claims; apply fixed release rules; export Markdown and JSON evidence for human approval.
- `Data requirements`: Public, synthetic, or governance-approved model outputs; repeated samples; confidence tags; labels or adjudicated correctness; judge identifiers; dataset and split manifests; no unnecessary personal data.
- `Architecture`: Local CLI with a schema validator, deterministic metric engine, judge-adapter interface, rewrite-diff module, policy evaluator, and signed artifact exporter. Raw responses remain local; public output is aggregate and sanitized.
- `Success metrics`: Deterministic reruns; 100 percent manifest completeness; seeded accuracy, support, judge, and rewrite regressions rejected; bootstrap intervals emitted; zero private-path or secret findings in public output; reviewer decision completed from one evidence card.
- `Risk controls`: Offline-only MVP, allowlisted inputs, no autonomous deployment, immutable model/judge/split versions, held-out evaluation, human approval, fail-closed missing data, and explicit statement that uncertainty is not correctness.
- `Limitations`: Cannot reveal latent beliefs, inherits judge and label error, may be expensive with repeated sampling, and does not establish user reliance or end-to-end system safety.
- `MVP boundary`: Evaluation and evidence generation only; no model training, production routing, medical/legal/financial decision support, or automated threshold changes.
- `Deployment model`: Local batch CLI in an authorized evaluation environment.
- `Evaluation plan`: Unit tests for equations and schemas, synthetic regression fixtures, public benchmark smoke test, blinded rewrite audit, and manual governance review.
- `Failure modes`: Correlated judges, contaminated test data, stale model versions, narrow support, malformed confidence tags, hidden rewrite changes, and policy thresholds tuned after seeing candidate results.
- `Maintenance plan`: Pin metric and judge versions, review dependency changes, refresh public benchmark fixtures, require reapproval after model/prompt/threshold changes, and retain prior evidence cards.

Illustrative policy logic:

```python
def release_decision(card):
    required = [
        card.split_is_held_out,
        card.accuracy_delta >= -0.01,
        card.faithfulness_ci_low >= card.faithfulness_floor,
        card.confidence_support_width >= card.support_floor,
        card.judge_disagreement <= card.judge_disagreement_ceiling,
        card.rewrite_changed_claims == 0,
    ]
    return "human_review" if all(required) else "reject"
```

The example intentionally never returns an automatic production approval.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Reinforcement Learning with Metacognitive Feedback | Primary reviewed paper | RLMF, data selection, cMFG-star, rewriting, and reported experiments | https://arxiv.org/abs/2606.32032 |
| yale-nlp/RLMF | Official implementation | Pinned trainer, rewards, configs, evaluation, and rewriting workflow | https://github.com/yale-nlp/RLMF |
| MetaFaith | Direct predecessor | Establishes faithful linguistic uncertainty and the metacognitive prompting baseline | https://aclanthology.org/2025.emnlp-main.1505/ |
| Finetuning Language Models to Emit Linguistic Expressions of Uncertainty | Direct baseline | Supervised uncertainty-language tuning compared as FUT | https://arxiv.org/abs/2409.12180 |
| SelfCheckGPT | Methodological predecessor | Sampling-consistency approach used as context for intrinsic-confidence estimation | https://aclanthology.org/2023.emnlp-main.557/ |
| Semantic Uncertainty | Methodological neighbor | Semantic equivalence-aware uncertainty estimator for transfer testing | https://arxiv.org/abs/2302.09664 |
| PAC Confidence - DEP-E | Related Black Lake DEP | Adds finite-sample support, interval, and shift-envelope requirements | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence |
| OViP Preference - DEP-E | Related Black Lake DEP | Adds on-policy feedback-loop provenance and judge-governance context | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference |
| ConMax Reasoning - DEP-E | Related Black Lake DEP | Adds confidence-shaped optimization and auxiliary-evaluator boundary | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260708-ConMax%20Reasoning |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2606.32032 | Title, authors, date, subjects, version, DOI, and code link | 2026-07-14 | Canonical metadata |
| R2 | https://arxiv.org/pdf/2606.32032 | Complete paper, methods, results, figures, tables, and appendices | 2026-07-14 | Private verified copy inspected but not deposited |
| R3 | https://arxiv.org/html/2606.32032 | Public full text and cross-check | 2026-07-14 | Primary public rendering |
| R4 | https://arxiv.org/e-print/2606.32032 | Equations, prompts, captions, and table source | 2026-07-14 | Private source package inspected but not deposited |
| R5 | https://doi.org/10.48550/arXiv.2606.32032 | Persistent identifier | 2026-07-14 | arXiv-issued DOI |
| R6 | https://github.com/yale-nlp/RLMF | Official code and reproduction documentation | 2026-07-14 | Inspected at `a087e7a1e49f52aaa701add19cd80699b709fdef`; MIT |
| R7 | https://aclanthology.org/2025.emnlp-main.1505/ | MetaFaith predecessor and baseline context | 2026-07-14 | Primary EMNLP record |
| R8 | https://arxiv.org/abs/2409.12180 | FUT baseline context | 2026-07-14 | Primary arXiv record |
| R9 | https://aclanthology.org/2023.emnlp-main.557/ | SelfCheckGPT consistency context | 2026-07-14 | Primary EMNLP record |
| R10 | https://arxiv.org/abs/2302.09664 | Semantic uncertainty alternative | 2026-07-14 | Primary arXiv record |
| R11 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence | Statistical calibration synthesis | 2026-07-14 | Related DEP 1 of exactly 3 |
| R12 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference | On-policy preference-loop synthesis | 2026-07-14 | Related DEP 2 of exactly 3 |
| R13 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260708-ConMax%20Reasoning | Confidence-shaped optimization synthesis | 2026-07-14 | Related DEP 3 of exactly 3 |

## Appendix

### Replication Checklist

- [ ] Pin paper v1 and code commit `a087e7a1e49f52aaa701add19cd80699b709fdef`.
- [ ] Resolve the pinned Python 3.11 environment and GPU-compatible versions without changing core TRL behavior.
- [ ] Acquire authorized PopQA and the nine evaluation datasets, recording exact revisions and licenses.
- [ ] Create separate train, validation, and untouched test splits; do not select checkpoints on test data.
- [ ] Reproduce pre-SFT format training and archive parse-validity metrics.
- [ ] Generate metacognitive data-selection scores and preserve high/low sampling provenance.
- [ ] Serve the Qwen3-32B consistency judge with a pinned template and deterministic configuration.
- [ ] Train standard RL and RLMF for at least five declared seeds with equal compute.
- [ ] Record tokens, GPU hours, wall time, energy estimate, failures, and checkpoint hashes.
- [ ] Evaluate cMFG-star, support width, per-bin counts, accuracy, Brier score, and abstention on the untouched test sets.
- [ ] Repeat evaluation with at least one independent intrinsic-confidence estimator and one independent judge.
- [ ] Audit numerical-to-linguistic rewriting for factual preservation and human reliance, not style alone.
- [ ] Publish seed-level aggregate results, bootstrap intervals, configuration, and failure cases.

### Metric Interpretation Notes

- `Expressed confidence`: Number emitted by the policy model for a sentence.
- `Intrinsic-confidence proxy`: Fraction or score derived from semantic consistency with sampled model responses.
- `Factual calibration`: Alignment between confidence and correctness.
- `Faithful calibration`: Alignment between expressed confidence and the intrinsic-confidence proxy.
- `Metacognitive score`: Agreement between the model's predicted faithful-calibration level and the computed level.
- `cMFG-star`: Width-weighted average faithfulness over equal-mass intrinsic-confidence bins on empirical support.

These quantities should remain separate in logs, schemas, dashboards, and user-facing documentation.

### Table and Figure Coverage Summary

The review inspected the two overview diagrams, main faithful-calibration table, reliability diagram, training-task and data-selection tables, complete smaller-model tables, prompt figures, metric comparison, reward and advantage ablations, data-size and pre-SFT ablations, metacognitive-score and scaling ablations, data-selection bin analyses, hedge-distribution figures, rewriting ablations, faithfulness distributions, metacognitive training curves, numerical examples, linguistic examples, user-context descriptions, and annotation instructions. Dense appendix prompts were reviewed for role and dependency rather than reproduced verbatim.

### Public-Safe Process Record

- Selection was user directed for arXiv:2606.32032 rather than random.
- Duplicate checks found author-inventory references in a related repository but no substantive prior DEP for this paper.
- PDF, full-paper HTML, metadata HTML, TeX source, extracted text, figures, and code cache remain private.
- No source binary or local filesystem path is included in this public artifact.
- Experiments and code were not executed; all numerical results remain author reported.
