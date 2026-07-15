# Failure-Guided Multimodal Preference Loops

## A whitepaper-grade archival intake review of the OViP DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260714-OViP Preference`  
**Source commit:** `398f692812550135476e8d560be1d2a01fa2982e`  
**Paired task indicator:** `BL-DEPPAIR-20260715-7902C8CA`  
**Direction:** `DEP-E -> DEP-A`  
**Review date:** 2026-07-15  
**Review scope:** complete two-file repository record; canonical v2 paper and official code context; method, evaluation, claims, synthetic-data risks, re-conceptualization, and replication agenda  
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes  
**Reproduction boundary:** no model, service, image generator, dataset, training run, benchmark, or repository code was executed.

---

## Executive assessment

The selected DEP-E contains a public-safe README and a detailed manuscript about OViP, an online vision-language preference-learning method intended to reduce hallucination while maintaining answer coverage and general capability. Both tracked files were read in full. The record covers canonical identity, on-policy response sampling, external scoring, contrastive pair selection, inverse negative-image synthesis, response- and image-side preference objectives, buffering, evaluation, ablations, compute, limitations, official code, related Black Lake records, and source withholding.

OViP’s durable contribution is a **failure-guided data flywheel**. Instead of assuming a static set of negative responses or generic corrupted images, the current model generates responses, an external judge identifies high-contrast good/bad pairs, semantic discrepancies become prompts, and a diffusion model synthesizes images aligned with the rejected content. The target model is then updated on response and image preferences. As the model changes, the data distribution changes.

The complete canonical v2 HTML was inspected directly across method, experiments, ablations, further study, ethics, limitations, appendices, and references.[^paper] Canonical metadata and the official code repository were also inspected.[^record][^code] The source is a complete preprint, not an abstract-only record. The paper’s key tables support a favorable one-epoch tradeoff, an online-versus-offline advantage, and a reported efficiency claim. However, the main aggregate HRI is normalized using observed reference gains that partly include OViP endpoints. It should be interpreted within the evaluated set, not as a universal scale.

The central evidence risk is upstream supervision quality. The response judge may inherit reference-answer omissions and does not necessarily verify the image directly in the shown prompt. The diffusion model may change multiple visual factors, introduce artifacts, or encode bias. A pair can therefore be “hard” for the wrong reason. Because the feedback loop trains on its own current failure distribution, judge and generator errors can become self-reinforcing.

Bottom line: the DEP-E is a strong archival research record and the method is a plausible approach to adaptive preference data. The paper supports “promising under tested LLaVA conditions,” not general hallucination safety or reproduction. The most useful derived artifact is an evidence-gate design that separately audits pair provenance, synthetic-image isolation, precision/coverage, judge calibration, general-capability retention, and service lineage.

### Principal strengths

- Online sampling targets the current model’s own error distribution.
- Response- and image-side signals address language-only preference limitations.
- Precision and coverage are considered together, reducing incentives for terse avoidance.
- The paper reports 7B and 13B models, epochs, online/offline comparisons, loss variants, training dynamics, compute, ethics, and limitations.
- The DEP-E carefully distinguishes author reports, external repository evidence, reviewer interpretation, and proposals.

### Principal qualifications

1. No experiment or generated image was independently audited in this run.
2. HRI depends on selected normalization endpoints and is not directly comparable across studies.
3. Synthetic negative images may contain unintended semantic changes or shortcut artifacts.
4. Judge errors can shape which examples enter training and amplify over iterations.
5. The seven-GPU, multi-service topology is expensive and operationally complex.

---

## 1. The problem and research question

Vision-language models hallucinate objects, attributes, and relations. Preference optimization can reduce undesirable text, but response-only pairs do not necessarily force the model to use visual evidence. Image-side methods add preferred and rejected visual inputs, yet generic noise, crops, or fixed corruptions may be far from the target model’s actual mistakes.

OViP asks whether preference data should be generated on policy. At each update, the current model’s failures determine the next response pairs and negative images. The method also addresses an evaluation problem: a model can improve hallucination precision by mentioning fewer objects. OViP therefore tracks object coverage and combines hallucination-related metrics into HRI while reporting general-capability differences.

The broader research question is whether an adaptive counterexample generator can improve grounding without sacrificing usefulness. This requires more than a loss function. It requires reliable sampling, judging, discrepancy extraction, image generation, buffering, training, and balanced evaluation. Every service can alter the data distribution.

---

## 2. Technical reconstruction

### 2.1 On-policy response construction

For each image, instruction, and reference answer, the current model samples multiple responses. The reported default is 16 candidates. Qwen-2.5-7B-Instruct scores each response from zero to ten against the reference. Pair selection requires sufficient score contrast, with a gap threshold of three, positives at least six, and negatives at most four. When all sampled responses are poor, an offline ground-truth answer may become the positive.

The design concentrates learning on the extremes. It can improve data efficiency, but it depends on judge calibration and reference completeness. A judge that rewards stylistic match or misses valid alternatives can select misleading pairs. Sampling 16 candidates also creates substantial inference cost and may underrepresent rare failures.

### 2.2 Negative-image synthesis

A prompt-generating model extracts semantic discrepancies involving entities, attributes, or relations between accepted and rejected responses. It writes an image description aligned with the rejected response. FLUX.1-dev generates a negative image from that prompt. The original image becomes the preferred visual input.

This is an inverse construction: a bad textual belief is turned into visual evidence that would make the bad answer more plausible. The intention is to force the model to distinguish real from counterfactual evidence. The causal interpretation holds only if the generated image changes the intended factor while preserving irrelevant factors. Diffusion artifacts, style changes, composition shifts, or demographic substitutions can create shortcuts.

### 2.3 Preference objectives and buffer

Response-side DPO prefers the accepted response over the rejected response for the same image and query. Image-side preference holds query and response context fixed while preferring the original image to the synthetic negative. An additional image-free term is intended to preserve a reasonable distribution. An experience buffer decouples variable pair generation from fixed training batches.

The paper reports that the exact image-loss form matters and that some anchoring variants reduce performance. The objective is an empirical surrogate. It does not guarantee grounded reasoning or semantic isolation. The buffer introduces staleness: examples may have been generated by earlier checkpoints and judges, so every record needs model and policy versions.

### 2.4 Models and infrastructure

Experiments use LLaVA-1.5 7B and 13B, CLIP ViT-L-336px, Vicuna backbones, LoRA rank 256 and alpha 512, 8,730 training samples, and 4,013 distinct image-query combinations. Qwen provides scoring and prompts. FLUX uses 40 inference steps and guidance 7.5. FastAPI services expose judge and diffusion components.

Seven A800 40 GB GPUs are reported: four for training, one for the LLM service, and two for diffusion. Training takes about 17 hours. This topology is part of the method’s cost and failure surface, not merely infrastructure detail.

---

## 3. Source inventory and integrity assessment

The source directory contains exactly `README.md` and `ovip_preference_manuscript.md`. The README provides tags, scope, inventory, summaries, key boundaries, relevance, and a final Attribution Block. The manuscript contains metadata, ten source entries, eight evidence groups, method and result reconstruction, claims, methodology, scope, observations, improvements, three implementations, exercises, an MVP, reading, references, process validation, and replication checklist.

The inventory matches tracked contents at the source commit. There is no `.source` directory, PDF, HTML, TeX archive, cache, dataset, generated image, prompt corpus, model, or code. The public source locators include arXiv v2, DOI, license, and the official repository. Related DEP records are explicitly contextual.

Direct inspection verified six authors, v1/v2 history, v2 date, categories, DOI, full-paper links, and complete HTML. The article includes Algorithm 1, Tables 1–4, figures, ethics, limitations, and appendices. The official repository exposes code/sample structure but was not cloned or executed. The DEP-E’s private byte-level integrity and extraction claims are treated as repository-reported process evidence; complete HTML inspection independently confirms a full paper.

The HTML rendering displays some signs in Tables 2–3 ambiguously. The DEP-E reports cross-checking HTML against TeX/PDF and preserves intended positive HRI/general-difference signs. This review relies on the DEP-E’s cross-format record for those sign-sensitive values and makes the boundary explicit rather than guessing from one renderer.

---

## 4. Architecture and operational pipeline

The loop has six stages: candidate sampling, response scoring, pair filtering, discrepancy-to-prompt conversion, negative-image synthesis, and buffered training. Evaluation then measures hallucination, coverage, and general capability. Every stage needs versioned lineage.

A production-quality event should record hashes or identifiers for source image/query/reference, target checkpoint, sampling parameters, candidate set, judge model/prompt, scores, selection reason, prompt generator, diffusion model/config, generated image, safety checks, buffer insertion, training consumption, and output checkpoint. Raw content should remain in controlled storage; public reports should use aggregate counts and hashes.

The loop should not be deployed as an autonomous promotion system. Pair quality, synthetic-image safety, judge disagreement, regression slices, and general capability should pass independent gates. A failed gate should stop training or promotion without deleting evidence.

---

## 5. Independent re-conceptualization

### 5.1 Adaptive counterexample curriculum

Reviewer inference: OViP is an adaptive curriculum generator. The model’s current errors identify the next examples. This resembles hard-negative mining, except both rejected responses and counterfactual images are model-mediated. The mechanism predicts that online data helps most when the failure distribution shifts materially during training.

The analogy breaks because generated counterexamples may be invalid. A curriculum assumes examples teach the intended concept. Here, judge and diffusion errors can teach shortcuts.

### 5.2 Distributed feedback control

The services form a distributed controller around the target model. The target produces behavior; judges estimate error; a generator constructs corrective evidence; updates change the target. Delays, stale buffers, service drift, and correlated model families can destabilize the loop. Versioning and bounded retries are control requirements.

### 5.3 Transferable principle

The durable principle is **adapt examples to current failures, but audit the example constructor independently**. This applies to safety fine-tuning, code repair, agent planning, and synthetic curricula. The counterexample generator must not share an unchecked objective with the learner.

---

## 6. Experimental design and evidence reconstructed

Hallucination evaluation uses MMHal-Bench, AMBER generative, Object HalBench, LLaVA-Bench-in-the-Wild, and AMBER discriminative. General capability uses RealworldQA, TextVQA, CVBench, and MMStar. The paper replaces a text-only MMHal judge with a multimodal judge and introduces F1 combinations for precision and coverage.

HRI normalizes improvement across five hallucination metrics and sums the terms. For key analyses, observed OViP two-epoch values define several reference endpoints. This creates an internally useful index but couples its scale to compared models. HRI should be accompanied by raw metrics and fixed reference ranges.

The design includes 7B and 13B, one and two epochs, online/offline OViP and DPO, loss variants, training dynamics, and efficiency discussion. Missing or weak elements include repeated seeds, confidence intervals, independent image audits, judge calibration, human evaluation, complete benchmark correction, filter sweeps, and model-family transfer.

---

## 7. Results and quantitative audit

For LLaVA-1.5-7B, the DEP-E reports one-epoch HRI 9.58 and General Accuracy Difference +0.88; two epochs reaches HRI 10.00 while general difference becomes -1.01. The tradeoff is important: greater aggregate hallucination improvement can coincide with general regression. For 13B, one epoch reports HRI 5.25 and +0.85; two epochs 8.02 and +2.02. Model size and training duration do not produce one universal pattern.

The one-epoch online/offline comparison reports online OViP coverage 51.1, HRI 9.36, and general difference +0.88 versus offline coverage 49.9, HRI 4.32, and +0.08. This supports online data under the paper’s metric. It does not isolate all differences in service output, pair yield, buffer age, or optimization.

The paper reports approximately 1.97x higher training efficiency than GRPO for comparable performance, based on expected GPU-hour accounting. The source states the ratio; this review did not reproduce service utilization or curves. End-to-end cost must include target sampling, judge inference, prompt generation, diffusion, failures, storage, and evaluation.

The evidence assessment is **supported under tested LLaVA settings with a clear online signal, but limited by normalization coupling, missing uncertainty, and unaudited synthetic negatives**.

---

## 8. Ablations and causal evidence

Loss ablations indicate that image-objective form matters. Online/offline comparisons indicate that current-model data matters. Training dynamics show early duplicate responses and later redistribution toward higher-scoring outputs. These observations are consistent with the proposed mechanism.

They do not isolate response judging from negative-image construction, or on-policy sampling from buffer freshness. A factorial design should compare static versus current checkpoints, response-only versus image-only versus dual loss, real edited versus diffusion negatives, unimodal versus multimodal judges, and fresh versus stale buffer entries.

Repeated training and data-generation seeds are essential. The pair filter, candidate sampling, diffusion randomness, LoRA training, and benchmark judges all introduce variance. Confidence intervals and effect distributions should replace single-number promotion decisions.

---

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| On-policy negatives better track current hallucinations. | Online OViP exceeds offline HRI in the reported table. | Supported under tested conditions. | Service and optimization differences are not fully isolated. |
| Dual image/response preferences improve grounding. | Main results and loss ablations. | Promising but limited. | Grounding is inferred from benchmarks; synthetic images are unaudited. |
| One-epoch 7B reaches HRI 9.58 and general difference +0.88. | Table values cross-checked by the DEP-E. | Strongly supported as paper report. | No independent reproduction or uncertainty. |
| Online OViP exceeds offline by more than four HRI points. | 9.36 versus 4.32. | Supported within the paper’s HRI definition. | HRI normalization is data-dependent. |
| OViP is about 1.97x more efficient than GRPO. | Efficiency discussion. | Promising but limited. | Accounting and service utilization were not independently audited. |
| Hallucination improvement can hide omission. | Precision/coverage framing and examples. | Strong methodological concern. | Coverage itself may not measure answer usefulness completely. |
| The official repository makes results reproducible. | Code and instructions are visible. | Not established. | Environment, data, services, checkpoints, and expected outputs were not run. |
| OViP establishes safe VLM deployment. | No deployment or broad safety study. | Not established. | Bias, rights, calibration, adversarial robustness, and human impact remain. |

---

## 10. External primary-source context

The arXiv record pins v2 and six authors, and exposes the complete paper/source links and DOI.[^record] The paper remains a preprint in the inspected record. The official repository is explicitly titled as code for OViP and exposes training/evaluation structure.[^code] Availability improves inspectability, not reproduced status.

The DEP-E connects OViP with VLM Probing, VideoWeave Geometry, and BA-LoRA Bias. These contribute diagnostic, synthetic-media consistency, and behavior-preservation perspectives. They are relevant reviewer context but not independent OViP validation.

Primary methodological neighbors include DPO and multimodal preference methods such as POVID. This review does not claim OViP invented preference optimization or image-side contrast. Its distinctive contribution is the on-policy loop that constructs both response and image preferences from current failures.

---

## 11. Research notes and critical considerations

Judge governance is central. If one judge model shapes training data, its blind spots can become target-model behavior. Use independently governed judges, retain disagreement, calibrate on human labels, and keep benchmark evaluation separate from training selection.

Reference answers are incomplete descriptions, not exhaustive visual truth. A valid response may differ in detail or wording. Pair selection should incorporate multimodal verification and uncertainty rather than treat one reference as perfect.

Synthetic images require a semantic-isolation audit. Review target change, preservation of unrelated content, artifacts, safety, bias, copyright/style concerns, and shortcut cues. Reject uncertain pairs or route them to humans.

HRI should be versioned with fixed directions, endpoints, and formulas. A composite score should never replace raw precision, coverage, calibration, general capability, and slice results. The 7B two-epoch tradeoff demonstrates why.

Operationally, seven GPUs and several services create queue, retry, version, security, and availability risks. Service prompts may contain sensitive images or text. Use local/authorized models, encryption, secret isolation, bounded retries, and no public raw content.

---

## 12. Potential implications

Scientifically, adaptive data generation may be more important than a particular preference loss. Failure distributions move during training; static datasets can become less informative. This supports dynamic curricula with strict provenance.

For system design, separate pair generation from pair acceptance. An independent evidence gate can validate judge agreement, image isolation, safety, and lineage before examples enter the buffer.

For evaluation, report Pareto surfaces rather than one composite: hallucination precision, coverage, calibration, general performance, compute, and safety. Promotion should require all declared floors.

For governance, raw images, prompts, and model outputs may be licensed, personal, or sensitive. Public artifacts should contain aggregate counts and stable public locators only. Model updates require human approval and rollback.

---

## 13. Falsifiable hypotheses

### Hypothesis 1: independent image verification predicts downstream benefit

**Proposition:** Filtering synthetic negatives for semantic isolation will improve grounding at equal accepted-pair count.  
**Motivating evidence:** The paper does not comprehensively audit unintended changes.  
**Predicted observation:** Verified pairs yield better counterfactual performance and fewer shortcuts.  
**Falsifier:** Filtering does not change or reduces grounded performance.  
**Minimum test:** Blinded human/multimodal audit and fixed training budget.

### Hypothesis 2: fixed-range HRI changes conclusions

**Proposition:** Pre-registered normalization endpoints will alter rankings or uncertainty relative to observed OViP endpoints.  
**Motivating evidence:** Current HRI uses evaluated-method gains.  
**Predicted observation:** Some headline differences shrink or reorder under fixed ranges.  
**Falsifier:** Rankings remain stable across reasonable pre-registered ranges.  
**Minimum test:** Recompute published tables under several declared fixed schemes.

### Hypothesis 3: online benefit is concentrated after distribution shift

**Proposition:** Online generation helps most after the target checkpoint’s failure distribution changes.  
**Motivating evidence:** Adaptive examples should matter when static negatives become stale.  
**Predicted observation:** Online-offline gap grows over later checkpoints or shifted slices.  
**Falsifier:** Gap is constant or absent when pair quality is matched.  
**Minimum test:** Checkpoint-indexed evaluation with matched pair counts and judges.

---

## 14. Deployment and governance considerations

Appropriate use is offline alignment research with authorized public or licensed data. Poor fit includes autonomous model promotion, unrestricted scraping, or training on sensitive images without consent and rights review.

Required safeguards include source allowlists, judge calibration, independent multimodal verification, safety/bias filters, retention limits, model/prompt/config hashes, stale-buffer controls, fixed metric policy, repeated seeds, human approval, rollback, and public-output sanitization. HRI alone must never authorize release.

---

## 15. Replication and falsification agenda

First, pin the official repository commit, nested dependencies, environment, models, datasets, prompts, services, checkpoints, and metric code. Resolve licenses separately for paper, code, models, diffusion outputs, and benchmarks.

Second, reproduce baseline evaluation before training. Recompute F1 and HRI from source tables, document sign conventions, and create unit tests for metric direction and endpoints. Use fixed reference ranges for new comparisons.

Third, audit a sample of generated negative images before a full run. Measure intended target change, unrelated-content preservation, artifacts, bias, safety, and human agreement. Archive only authorized evidence.

Fourth, run repeated seeds and factorial ablations across online/offline data, response/image objectives, judges, generator types, buffer age, and threshold settings. Report pair yield, rejection reasons, compute, and all raw metrics.

Fifth, test at least two open VLM families and distribution shifts. Measure whether online benefits transfer or depend on LLaVA/Vicuna/CLIP and the original training set.

The highest-priority falsifier is a blinded audit showing synthetic negatives frequently change unrelated semantic factors and that models exploit those artifacts. That would undermine the image-side causal story even if HRI improves.

---

## 16. Durable restatement

> OViP turns the target VLM’s current mistakes into the next preference curriculum by selecting contrasting responses, synthesizing images aligned with rejected content, and training on both response and image preferences. The paper reports favorable online and one-epoch tradeoffs, but its aggregate metric is study-dependent and the judge/generator chain was not independently validated.

The durable lesson is to adapt counterexamples to current failures while treating the counterexample constructor as a separate system requiring provenance, calibration, safety review, and falsification.

---

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment | Boundary |
|---|---|---|---|
| DEP-E README | inventory, key values, source policy, attribution | Sections 3 and 10 | repository metadata |
| Manuscript metadata/evidence | versions, official code, related DEPs | Sections 3 and 10 | code not run |
| Paper Introduction | hallucination and static-negative problem | Section 1 | framing retained |
| Method / Figure 1 | online loop overview | Sections 2 and 4 | no service execution |
| Equations 1–6 | sampling, pair selection, response/image losses | Section 2 | not rederived or executed |
| Experiment setup | models, data, seven GPUs, services | Sections 2 and 6 | author-reported |
| Table 1 | 7B/13B main results | Section 7 | no intervals |
| Table 2 | loss variants | Section 8 | renderer sign boundary noted |
| Table 3 | online/offline OViP and DPO | Sections 7–8 | HRI study-dependent |
| Figures 2–5 | metric tradeoffs, dynamics, efficiency | Sections 7–8 | curves not digitized |
| Further study | efficiency and probability dynamics | Sections 7–8 | not reproduced |
| Ethics/limitations | misuse, benchmark errors, untuned filters | Section 11 | retained as boundaries |
| Appendix Algorithm 1 / Table 4 | full OViP pseudocode | Sections 2 and 4 | not executed |
| Appendix settings and prompts | services, models, training defaults | Sections 2–4 | prompt quality unaudited |
| References | DPO, preference and hallucination context | Section 10 | context only |
| DEP proposals/MVP | curation, evidence gate, provenance monitor | Sections 12–15 | reviewer proposals |
| DEP integrity appendix | private source verification | Appendix B | local bytes unavailable |

All four numbered tables, numbered figures, central equations, ethics/limitations, algorithm appendix, settings, and source record sections are accounted for at the level material to this archival review.

---

## Appendix B. Source and evidence notes

### Primary reviewed artifact

The complete record `.lake-data/DEP-E/DEP-E-20260714-OViP Preference` at commit `398f692812550135476e8d560be1d2a01fa2982e` was inspected.[^dep][^provenance] Both files were read in full. No source DEP file was modified, moved, copied, renamed, or reclassified.

### Directly inspected primary evidence

- https://arxiv.org/abs/2505.15963
- https://arxiv.org/html/2505.15963
- https://doi.org/10.48550/arXiv.2505.15963
- https://github.com/lsjlsj35/Online-Vision-Language-Preference-Learning-for-VLM-Hallucination
- https://github.com/Delphoa/Black-Lake/commit/398f692812550135476e8d560be1d2a01fa2982e

### Evidence boundary

The complete DEP-E, canonical v2 metadata, complete v2 HTML, and official repository surface were inspected. No PDF, TeX archive, dataset, model, generated image, prompt, or code was committed or executed. Sign-sensitive table values rely on the DEP-E’s reported cross-format TeX/PDF check where the HTML renderer is ambiguous. Independent reproduction was not performed.

### Provenance pair

`BL-DEPPAIR-20260715-7902C8CA` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. Intake/deposition become complete only after atomic submission with both ledger rows.

---

## Footnotes

[^paper]: Liu et al., “OViP: Online Vision-Language Preference Learning for VLM Hallucination,” arXiv:2505.15963v2, complete HTML at https://arxiv.org/html/2505.15963.
[^record]: Canonical metadata, version history, and source links: https://arxiv.org/abs/2505.15963.
[^code]: Official OViP repository: https://github.com/lsjlsj35/Online-Vision-Language-Preference-Learning-for-VLM-Hallucination.
[^dep]: Source DEP-E: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference.
[^provenance]: Selection source commit: https://github.com/Delphoa/Black-Lake/commit/398f692812550135476e8d560be1d2a01fa2982e.
