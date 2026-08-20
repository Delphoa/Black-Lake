---
title: "OViP Preference - DEP-E"
generated_at: "2026-07-14 (public-safe date; exact execution timestamp withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of online vision-language preference learning for hallucination reduction in large vision-language models."
source_status: "complete local PDF, HTML, metadata, and TeX sources inspected; public URLs cited; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-14"
temporal_cutoff: "Sources and repository context inspected through 2026-07-14."
primary_url: "https://arxiv.org/abs/2505.15963"
stable_identifier: "arXiv:2505.15963v2; DOI:10.48550/arXiv.2505.15963"
confidence_summary: "High for source identity, method, tables, and stated limitations; medium for interpretation; low for independent reproducibility because code and experiments were not run."
safety_scope: "non-sensitive research review, synthetic/public evaluation examples, offline evidence-gate design"
distribution_notes: "No PDF, HTML, TeX archive, extracted source text, cache, model, dataset, prompt corpus, generated image, or local path is redistributed."
---

# OViP Preference - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | OViP arXiv record | Canonical metadata | HTML | arXiv:2505.15963v2 | https://arxiv.org/abs/2505.15963 | Public metadata; CC BY 4.0 link visible. | 2026-07-14 | Inspected. |
| S2 | OViP full-paper HTML | Primary paper | HTML | arXiv:2505.15963v2 | https://arxiv.org/html/2505.15963 | Public full-paper rendering; no file redistributed. | 2026-07-14 | Inspected in full. |
| S3 | OViP paper PDF | Primary paper | PDF | arXiv:2505.15963v2 | https://arxiv.org/pdf/2505.15963 | Public locator; verified local copy withheld. | 2026-07-14 | Inspected through local extraction. |
| S4 | OViP TeX source | Primary source package | TeX archive | arXiv:2505.15963v2 | https://arxiv.org/e-print/2505.15963 | Public locator; local source archive and extracted text withheld. | 2026-07-14 | Inspected for formulas, tables, and appendices. |
| S5 | arXiv-issued DOI and license | Persistent identity / usage | DOI / license | 10.48550/arXiv.2505.15963; CC BY 4.0 | https://doi.org/10.48550/arXiv.2505.15963 | Persistent locator; linked license does not cover unrelated code/data dependencies. | 2026-07-14 | Inspected. |
| S6 | Official OViP repository | Official implementation | GitHub repository | `lsjlsj35/Online-Vision-Language-Preference-Learning-for-VLM-Hallucination`, main branch | https://github.com/lsjlsj35/Online-Vision-Language-Preference-Learning-for-VLM-Hallucination | Code/sample-data repository; no release or execution validated. | 2026-07-14 | README and visible tree inspected. |
| S7 | Local archive verification/cache records | Selection and extraction provenance | Private records | arXiv:2505.15963v2 | Local path withheld | Private processing evidence only; no source material redistributed. | 2026-07-14 | Integrity and cache summaries inspected. |
| S8 | VLM Probing DEP | Related research artifact | Markdown | DEP-E-20260712-VLM Probing | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Repository-generated review. | 2026-07-14 | Inspected. |
| S9 | VideoWeave Geometry DEP | Related research artifact | Markdown | DEP-E-20260709-VideoWeave Geometry | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Repository-generated review. | 2026-07-14 | Inspected. |
| S10 | BA-LoRA Bias DEP | Related research artifact | Markdown | DEP-E-20260709-BA-LoRA Bias | `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` | Repository-generated review. | 2026-07-14 | Inspected. |

The canonical arXiv record lists Shujun Liu, Siyuan Wang, Zejun Li, Jianxiang Wang, Cheng Zeng, and Zhongyu Wei. Version 1 was submitted on 2025-05-21; version 2 was revised on 2025-09-28. No journal reference or publisher venue was visible in the inspected canonical record, so this artifact treats the work as an arXiv preprint rather than inferring peer-review status.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5 | Canonical metadata / DOI | Title, authors, identifier, dates, subjects, license locator. | Source identity and version context. | High | Does not validate methods or experiments. |
| E2 | S2-S4 | Primary full paper | Introduction, method, formulas, Algorithm 1, experiment tables, HRI definition, ablations, efficiency, ethics, limitations, appendices. | Mechanism, evaluation, reported results, compute, and caveats. | High for reporting | No experiment was reproduced; formulas and table signs required cross-format checks. |
| E3 | S6 | Official implementation repository | Modified LLaMAFactory tree, evaluation tree, sample archive, dependencies, model/data instructions, online-data paths. | Code availability and implementation boundary. | Medium-high | Visible repository had one commit and no release; code/data were not cloned or run. |
| E4 | S7 | Private process evidence | Random draw, dedup scans, PDF/HTML integrity metrics, archive repair, extraction summary. | Eligibility, source completeness, and cache status. | High | Local records are intentionally not public locators. |
| E5 | S8 | Related DEP manuscript | Multimodal fusion, modality-use, visual-relation, leakage, and causal-evidence probes. | Cross-DEP diagnostic bridge. | Medium | Does not validate OViP outcomes. |
| E6 | S9 | Related DEP manuscript | Diffusion/media consistency and multi-signal evidence-gate framing. | Synthetic-negative audit bridge. | Medium | Different generation task and data regime. |
| E7 | S10 | Related DEP manuscript | Behavior preservation, drift, diversity, and noise robustness during low-rank adaptation. | Adaptation-preservation bridge. | Medium | Language-model study, not multimodal OViP replication. |
| E8 | S1-S7 and repository scans | Mixed process evidence | ID/title/version checks, table cross-checks, code-availability check, absent reproduction. | Claim confidence and non-duplication. | High for observed process | Cannot establish generalization or deployment readiness. |

## Executive Summary

OViP addresses a mismatch between how large vision-language models fail and how preference-training negatives are commonly constructed. Static datasets often use random crops, noise, object removal, or expert-defined edits. These examples may be semantically distant from the current model's own hallucinations. OViP instead samples the current model during training, identifies contrasting good and bad responses, converts their semantic differences into prompts, synthesizes negative images with a diffusion model, and trains on both response-side and image-side preferences.

The paper's strongest reported evidence is a balanced improvement story rather than hallucination reduction alone. On LLaVA-1.5-7B, one epoch reports HRI 9.58 and General Accuracy Difference +0.88; two epochs reports HRI 10.00 and -1.01. The online/offline ablation reports a greater than four-point HRI advantage for online training, and the authors report approximately 1.97x higher training efficiency than GRPO for comparable performance. These results are supported by inspected tables and source text but were not independently reproduced.

The design matters because it frames alignment as a changing data problem: as the model changes, the useful negatives change too. The key practical caution is that the loop outsources quality to an external judge, a prompt generator, a diffusion model, and benchmark protocols. HRI also uses observed reference gains—including OViP two-epoch values—to normalize its main comparison. Reviewer confidence is high for accurately reporting the paper, medium that failure-guided multimodal negatives are a reusable research pattern, and low for deployment or reproduction claims without executing the released stack and auditing synthetic negatives.

## Detailed Summary

### Problem Context

LVLM hallucinations include nonexistent objects, incorrect attributes, and fabricated spatial relations. Response-only DPO can improve text preference while leaving the model weakly grounded in vision. Image-side preference methods add a complementary signal but frequently use generic perturbations or fixed negative pairs. The authors argue that these negatives are not sufficiently aligned with the target model's current error distribution and can overfit static data.

Evaluation creates a second problem. Metrics that reward fewer mentioned hallucinated entities can be improved by producing shorter or less complete descriptions. OViP calls omission an “implicit hallucination” and evaluates both precision and coverage. This is a valuable framing even if the terminology is broader than common usage: a faithful system should not gain apparent reliability by refusing to mention visible content.

### Core Mechanism

For each image, instruction, and reference answer, the current model samples multiple candidate responses. An external LLM scores every response from 0 to 10 against the reference. The implementation samples 16 responses, requires a score-gap margin of 3, accepts positives scoring at least 6, and accepts negatives scoring at most 4. If all candidates are poor, the offline ground-truth answer may supply the positive side.

The prompt-generation LLM extracts semantic discrepancies across entities, attributes, and spatial relations, then writes an image description aligned with the rejected response. FLUX.1-dev generates a hard-negative image from that description. The original image acts as positive visual evidence. An experience buffer decouples variable sampling yield from fixed-size training updates.

The total objective combines response-side DPO with image-side preference optimization. The response loss prefers the accepted answer for the same image and instruction. The image loss holds the query and response fixed while preferring the original image over the generated negative image. An image-free term aims to maintain a reasonable probability distribution. The paper's ablation reports that this image-loss formulation outperforms tested variants, while anchor losses can hurt hallucination and general capability.

### Models, Data, and Infrastructure

Experiments use LLaVA-1.5-7B-hf and LLaVA-1.5-13B-hf, CLIP ViT-L-336px, and Vicuna 7B/13B backbones. LoRA uses rank 256 and alpha 512. The training data contains 8,730 samples and 4,013 distinct image-query combinations spanning description, question answering, and some yes/no tasks.

Qwen-2.5-7B-Instruct supplies response scores and image prompts. FLUX.1-dev supplies negative images using 40 inference steps and guidance scale 7.5. The system exposes the judge and diffusion components through FastAPI services. Seven A800 40GB GPUs are reported: four for training, one for the LLM service, and two for diffusion services.

### Evaluation Design

Five hallucination-related evaluations are MMHal-Bench, AMBER generative, Object HalBench, LLaVA-Bench-in-the-Wild, and AMBER discriminative. Four general-capability evaluations are RealworldQA, TextVQA, CVBench, and MMStar. The paper replaces a text-only MMHal judge with a multimodal judge and introduces F1 measures that combine hallucination precision with object coverage for AMBER-generative and ObjectHal.

HRI aggregates normalized improvement across five hallucination metrics. Each metric is divided by an observed potential-improvement range and the five normalized terms are summed with a factor of two. For the main 7B analysis, OViP two-epoch values define all reference endpoints. For 13B, OViP two-epoch values define most endpoints while ObjectHal uses 79.0. This makes HRI an internally interpretable score whose scale is tied to the evaluated methods and selected reference values.

### Main Results

For 7B, Table 1 reports:

- Baseline AMBER-generative F1 65.01, MMHal 1.90, ObjectHal F1 72.40, LLaVA-Bench 57.20, and AMBER-discriminative F1 85.5.
- One-epoch OViP reports 66.70, 2.52, 73.50, 63.10, and 87.3 on those metrics, HRI 9.58, and General Accuracy Difference +0.88.
- Two-epoch OViP reports HRI 10.00 and General Accuracy Difference -1.01, illustrating that more hallucination improvement can begin to trade against general performance.

For 13B, one-epoch OViP reports HRI 5.25 and General Accuracy Difference +0.85; two epochs reports HRI 8.02 and +2.02. The mixed pattern across sizes and epochs argues for reporting the full Pareto surface rather than one headline aggregate.

### Ablations and Training Dynamics

The one-epoch online/offline table reports OViP online Cover 51.1, HRI 9.36, and General Accuracy Difference +0.88 versus offline Cover 49.9, HRI 4.32, and +0.08. Online DPO also outperforms offline DPO on HRI, though both reduce general capability in that table. The paper concludes that online data and visual supervision are complementary.

Early training shows duplicate responses and low perplexity, which the authors interpret as a narrow initial output distribution. Diversity expands before aggregate performance improves. Later probability-mass analysis reports fewer low-scoring and more high-scoring responses, with online training affecting the extremes more than offline DPO.

### Efficiency, Ethics, and Reproducibility

Training takes about 17 hours in the reported seven-GPU topology. Autoregressive sampling is the largest non-post-processing cost and negative-image generation the second. The paper claims about 1.97x higher efficiency than GRPO and approximately half the compute for comparable performance. The comparison depends on the paper's expected-GPU-hour construction and was not reproduced.

The ethics statement notes that better factuality does not remove misuse risk. The official repository exposes modified training/evaluation code, dependencies, a sample archive, and download instructions. Its existence improves inspectability, but reproducibility remains unverified because models, datasets, services, and benchmarks were not downloaded or run, and no release artifact was visible.

### Source-Disclosed Limitations

The authors do not combine image-level contrastive objectives with PPO or GRPO. They state that benchmarks still fail to capture complete model capability, that only a subset of evaluation errors was manually corrected, and that the sampling filter was not carefully tuned. These limitations constrain causal and generalization claims.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Model-specific, on-policy negatives better match evolving hallucination failures than static generic negatives. | Author mechanism claim | E2, method and online/offline ablation | Plausible and supported by the reported ablation; not isolated from service, sampling, or optimization differences. | Medium-high |
| C2 | Dual image/response preference signals improve visual grounding while retaining general capability. | Author empirical claim | E2, Tables 1-3 | Reported tables support a favorable one-epoch trade-off; some two-epoch/general and per-benchmark results remain mixed. | Medium-high |
| C3 | One-epoch 7B OViP reaches HRI 9.58 and General Accuracy Difference +0.88. | Author quantitative claim | E2, TeX Table 1 | Exact values cross-checked across source text and table. | High for reporting |
| C4 | Online OViP outperforms offline OViP by at least four HRI points in one epoch. | Author empirical claim | E2, online/offline tables | HRI 9.36 versus 4.32 supports the stated margin; comparison remains tied to the paper's HRI definition. | High for reporting |
| C5 | OViP is about 1.97x more training-efficient than GRPO. | Author efficiency claim | E2, Figure 4 discussion and efficiency appendix | Source directly states the ratio; exact curve extraction and compute accounting were not independently audited. | Medium |
| C6 | Existing hallucination methods can appear better by reducing answer coverage. | Author observation and reviewer-supported interpretation | E2, AMBER F1/coverage analysis and bad cases | Precision/coverage tension is directly evidenced; “implicit hallucination” remains the paper's chosen terminology. | Medium-high |
| C7 | The official repository makes the method inspectable but not yet reproduced. | Reviewer interpretation | E3 | Code, instructions, and samples exist; environment, data, models, and outputs were not validated. | High for boundary |
| C8 | The paper was eligible and complete before review. | Process claim | E4, E8 | First draw had no duplicate marker; missing HTML was repaired and both formats passed integrity checks. | High |

## Methodology

- `Research objective`: Produce a source-grounded DEP-E manuscript for one uniformly selected, non-duplicate arXiv paper; preserve its mechanism, evidence, limitations, and implementation implications; and connect it to exactly three inspected Black Lake deposits.
- `Sources inspected`: Complete local PDF, full-paper HTML, metadata HTML, TeX archive, three extraction-cache texts, canonical arXiv record, DOI/license target, official implementation repository, live Black Lake README authorities, and three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, grouped unique parent directories as paper units, drew one uniform `Get-Random` index, resolved identity from adjacent metadata and filename, scanned dedup surfaces, repaired the selected unit, extracted local sources, inspected public primary records, and searched Black Lake by conceptual overlap.
- `Inclusion criteria`: Sources had to establish identity, expose methods/results/limitations, define repository rules, document process provenance, or supply concrete overlap in multimodal probing, synthetic-visual consistency, or behavior-preserving adaptation.
- `Exclusion criteria`: Abstract-only evidence, unrelated keyword hits, secondary summaries, unexecuted code behavior, and unverified source files were excluded from technical proof. No local source file was eligible for public deposition.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Author claims are labeled and tied to tables, sections, or evidence IDs. Reviewer interpretations are separated. HTML ambiguities were cross-checked against PDF and TeX extractions.
- `Uncertainty handling`: Non-reproduction, judge dependence, HRI reference coupling, untuned filters, synthetic-image risk, repository/release limits, and benchmark errors are explicit.
- `Extraction process`: Extractor preflight found `pypdf` but not `pdftotext`. Local `missing-only` extraction used `pypdf`, `html-regex`, and `tarfile`, producing 74,898 bytes of PDF text, 81,175 bytes of HTML text, and 159,651 bytes of source text.
- `Cache methodology`: The cache was absent before extraction. After the integrity repair added full-paper HTML and source, the central cache became `cached` with all three text representations; no cache network fallback was used.
- `Source-integrity methodology`: Initial state was partial because only PDF and metadata were present. The bounded archive workflow preserved the PDF, fetched HTML/metadata/source, refreshed local companion records, and verified a 1,648,427-byte `%PDF-`/`%%EOF` PDF plus 293,109-byte full-paper HTML with 79,707 body characters, 132 headings, and eight structure terms.
- `Version control`: Primary identity is pinned to arXiv:2505.15963v2. The official repository main branch was inspected as exposed on 2026-07-14; no release or reproducible output pin was inferred.
- `Claim selection`: Priority went to the failure-guided loop, dual loss, datasets/models, headline results, online/offline ablation, HRI construction, compute, negative evidence, and implementation boundary.
- `Cross-checking`: Table signs, HRI values, online/offline values, model settings, sample counts, compute, and limitations were checked across HTML and TeX/PDF extraction.
- `Safety handling`: Implementation examples operate on synthetic or aggregate records, keep raw images/prompts local, and use human review for uncertain or sensitive outputs.
- `Random selection methodology`: `rg` found 75,774 PDF-parent units; a uniform zero-based `Get-Random` draw selected index 50,425. The first draw was accepted; exclusions and reselections were zero.
- `Dedup/reselection validation`: Before acceptance, scans covered the public index, Black Lake logs/reports/lake-data/staging, automation memory, related-repository search results, and active worktree Markdown/JSON. No arXiv ID, DOI, normalized title, slug, or same-paper 24-hour marker was found.
- `Reviewer stance`: Critical paper report, DEP-ready preservation, evidence-gate design, product translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: OViP's on-policy data construction, dual preference objective, evaluation design, reported evidence, limitations, official implementation, and bounded engineering implications.
- `Temporal boundary`: Sources inspected through 2026-07-14; primary paper pinned to v2 revised 2025-09-28.
- `Evidence limits`: No code execution, model download, training, benchmark run, generated-image audit, dataset inspection, judge replication, or statistical reanalysis.
- `Assumptions`: The canonical PDF, HTML, and TeX archive describe the same v2 work; extraction preserved table values where cross-checked; repository identity linked by the paper is official.
- `Constraints`: Public artifacts cannot expose local paths, exact execution timestamps, user or machine identifiers, source files, licensed datasets, raw prompts, generated images, models, or caches.
- `Out of scope`: Production model alignment, deployment certification, raw data redistribution, reproducing seven-GPU training, or claiming HRI is comparable across independent studies.
- `Intended use`: Research review, DEP deposition, replication planning, evaluation design, and safe offline MVP ideation.
- `Audience`: Multimodal researchers, alignment engineers, evaluation teams, data-governance reviewers, and Black Lake maintainers.
- `Depth target`: Schema-complete manuscript with quantitative preservation and explicit evidence boundaries.
- `Reproducibility boundary`: A reviewer can follow public URLs and implementation instructions, but this DEP does not contain source files, models, datasets, environments, or expected outputs needed to reproduce results.
- `Operational boundary`: Suggested systems curate and evaluate offline data/checkpoints; they do not autonomously deploy, scrape, or train on unrestricted inputs.
- `Data sensitivity`: Public research metadata plus privately held source presence; raw image/prompt/model-output content should be treated as potentially licensed, personal, or sensitive.

## Observations

- `Observed pattern`: OViP's durable contribution is a data flywheel—current errors determine future negatives—not merely another DPO loss.
- `Observed trade-off`: The 7B two-epoch run improves HRI from 9.58 to 10.00 while General Accuracy Difference moves from +0.88 to -1.01, reinforcing a multi-objective evaluation need.
- `Metric implication`: HRI reduces raw-scale mismatch but remains coupled to observed reference gains and OViP endpoints; it should not be treated as a universal interval scale.
- `Data-quality implication`: A synthetic image that is plausible but changes multiple semantic factors can poison the causal interpretation of the image-side preference.
- `Judge implication`: The shown reward prompt compares response with a reference answer without direct image access, so reference incompleteness or judge preference can shape the on-policy data distribution.
- `Systems implication`: Sampling, judging, prompt generation, diffusion, buffering, and updating create a distributed training pipeline with synchronization, provenance, and failure-recovery requirements.
- `Cross-DEP pattern`: VLM Probing, VideoWeave, and BA-LoRA collectively suggest measuring grounding, synthetic-data consistency, and behavior preservation around each update.
- `Open question`: Can an independent multimodal verifier distinguish useful hard negatives from artifacts and shortcut cues cheaply enough for online training?
- `Reviewer hypothesis`: The most transferable product is an auditable preference-data/evaluation gate, not a turnkey reproduction of the full seven-GPU training stack.

## Considerations

Synthetic-negative governance is central. Generated images may encode demographic stereotypes, copyrighted styles, unsafe material, or unrelated semantic changes. A production-facing workflow would need prompt and image safety checks, semantic-isolation tests, dataset rights, retention limits, and sampled human review. Raw content should remain local by default; public artifacts should contain aggregate counts and versioned provenance only.

Judge governance is equally important. A feedback loop can amplify the judge's blind spots because the judge determines which responses become training data. Evaluation should rotate or ensemble independently governed judges, preserve disagreement, calibrate against human-labeled subsets, and prevent test benchmark prompts from leaking into training selection. A reference answer should not be assumed complete.

Operationally, the reported stack has meaningful cost and complexity. Seven GPUs, multiple services, large public models, diffusion inference, datasets, and four evaluation suites create version, license, availability, and security obligations. Service inputs must not contain secrets; generated paths must not leak local storage layouts; retry queues need ceilings; and checkpoint/data lineage must be append-only and auditable.

For decision-making, the paper supports experimenting with failure-guided multimodal negatives. It does not establish that OViP is best across current VLM families, that generated negatives are unbiased, that HRI transfers across studies, or that the released repository reproduces the tables. Those decisions require additional evidence.

## Strengths

- Targets the model's own current errors rather than assuming a static negative distribution.
- Combines response-side and image-side preferences in one explicit training objective.
- Makes the precision/coverage trade-off visible instead of rewarding terse outputs uncritically.
- Reports both 7B and 13B models, multiple baselines, two epochs, ablations, training dynamics, and general-capability metrics.
- Exposes filtering thresholds, generator settings, service topology, GPU allocation, and approximate training time.
- Discloses benchmark, filter-tuning, and unexplored-objective limitations.
- Provides an official code/evaluation repository and sample archive for future reproduction work.
- Offers a clear systems pattern: failure discovery, counterexample construction, buffered update, and balanced evaluation.

## Weaknesses

- All experimental results remain author-reported in this artifact; no code, checkpoint, or benchmark was executed.
- HRI reference ranges are data-dependent and partly defined by OViP's best results, limiting external comparability.
- The shown response judge does not inspect the image directly and may inherit reference-answer omissions or stylistic biases.
- Synthetic negative images are not comprehensively evaluated for semantic isolation, visual artifacts, bias, or shortcut leakage.
- Benchmark corrections were manual and incomplete, according to the paper.
- Filtering thresholds are empirically chosen and explicitly not carefully tuned.
- The main evidence is concentrated on LLaVA-1.5/Vicuna/CLIP with one original training set.
- The seven-GPU, multi-service pipeline has high replication and operations overhead.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Fix HRI reference ranges before model comparison | Evaluation | Current endpoints depend on observed OViP gains | Better external comparability and less metric coupling | May reduce headline scores | Pre-register ranges and evaluate hidden models without recomputing weights |
| Add confidence intervals and repeated seeds | Statistical rigor | Single table values hide training/judge variance | More credible release thresholds | Additional training cost | Bootstrap benchmarks; repeat selection/training seeds; report effect distributions |
| Use independent multimodal negative-image verification | Data quality | Diffusion outputs may change unintended factors | Cleaner causal supervision and fewer shortcuts | Extra inference and possible false rejects | Region/entity/relation checks, counterfactual captions, sampled human audit |
| Calibrate judge disagreement | Feedback quality | One judge can amplify systematic preference errors | More robust pair selection | Multiple judges increase cost | Compare judge ensemble with blinded human labels and retain disagreement strata |
| Tune filtering by yield-quality Pareto analysis | Training dynamics | Thresholds were set empirically and not carefully tuned | Better stability and data efficiency | Search can overfit validation | Sweep margin/quality thresholds on held-out failure slices |
| Add model-family transfer tests | Generalization | LLaVA-1.5 evidence may not transfer | Stronger architectural validity | Compute and adapter complexity | Repeat bounded runs on at least two open VLM families |
| Audit synthetic-data license, bias, and safety | Governance | Generated images can create new harms or restrictions | Safer and legally clearer reuse | Requires policy and human review | Versioned risk taxonomy, automated checks, sample review, retention controls |
| Publish environment and expected-output locks | Reproducibility | README instructions do not prove table reproduction | Lower clean-room replication cost | Maintenance burden | Container lock, hashes, dataset manifests, smoke fixtures, signed expected metrics |

## Potential Implementations

1. `Counterfactual Preference Curator`
   - `User`: Multimodal alignment and data-quality teams.
   - `Goal`: Build targeted preference pairs from model failures while rejecting unsafe or semantically confounded generated images.
   - `Core mechanism`: Sample responses, score with versioned judges, synthesize candidate negatives, run semantic-isolation/safety checks, and route uncertain items to human review.
   - `Required inputs`: Authorized image-query-reference records, pinned open models, judge/generator policies, and retention rules.
   - `Outputs`: Versioned pair manifests, aggregate quality metrics, rejection reasons, and local-only training records.
   - `Risk controls`: Allowlisted sources, no public raw content, prompt redaction, safety filters, bias slices, bounded retries, and human approval.
   - `Evaluation`: Agreement with blinded human audits, target-change precision, unrelated-content preservation, and downstream lift without coverage loss.

2. `Grounding and Hallucination Evidence Gate`
   - `User`: Model release and evaluation teams.
   - `Goal`: Detect when hallucination reduction comes from omission, language-prior shortcuts, or general-capability regression.
   - `Core mechanism`: Combine precision/coverage, calibration, public counterfactuals, modality ablations, representation probes, and general benchmarks in a versioned decision policy.
   - `Required inputs`: Base/candidate checkpoints or aggregate outputs, licensed/public evaluation slices, model metadata, and fixed thresholds.
   - `Outputs`: Pass/fail matrix, confidence intervals, failure slices, and signed Markdown/JSON evidence bundle.
   - `Risk controls`: Offline-only operation, aggregate publication, no automatic production promotion, and explicit uncertainty.
   - `Evaluation`: Seeded modality failures must trigger the gate; known coverage regressions must fail despite precision gains.

3. `Preference Loop Provenance Monitor`
   - `User`: ML platform, governance, and incident-response teams.
   - `Goal`: Make online sampling, judging, generation, buffering, and updating traceable without exposing raw sensitive content.
   - `Core mechanism`: Record hashes, versions, aggregate yields, queue health, rejection counts, dataset slices, and checkpoint lineage across stages.
   - `Required inputs`: Service events, model/prompt/config identifiers, policy versions, and privacy classification.
   - `Outputs`: Local lineage graph, drift alerts, rollback targets, and public-safe run summary.
   - `Risk controls`: Schema allowlist, encryption/access control for private events, no raw prompts/images in public logs, retention limits, and secret scanning.
   - `Evaluation`: Reconstruct a synthetic run, detect stale-version injection, and prove public exports contain no forbidden fields.

## Three Ways to Exercise This Research

1. `Recompute the paper's metric ledger`: Objective—verify table signs and HRI arithmetic. Inputs—the public paper tables and formulas. Method—transcribe fixed values, recompute F1/HRI components, and compare 7B/13B/online/offline results. Output—a signed spreadsheet or JSON ledger. Success criterion—all published values reconcile or discrepancies are documented. Stop condition—an ambiguous extraction is flagged and checked against another source format rather than guessed.
2. `Audit ten synthetic counterfactuals`: Objective—test semantic isolation without training. Inputs—ten public or synthetic image-question-answer fixtures and a locally authorized generator. Method—create one declared negative change per fixture, blind reviewers to the prompt, and score target change, unrelated-content preservation, artifacts, safety, and bias. Output—an aggregate audit report. Success criterion—pre-registered precision and preservation thresholds pass. Stop condition—license, privacy, or safety review is incomplete.
3. `Run a checkpoint-free gate simulation`: Objective—show why balanced metrics matter. Inputs—synthetic precision, coverage, calibration, and general-capability records for base/candidate models. Method—apply a fixed decision policy and inject omission/general-regression failures. Output—a deterministic pass/fail matrix. Success criterion—all injected regressions are rejected. Stop condition—thresholds are changed after seeing candidate labels.

## Example MVP Product

- `Product name`: OViP Evidence Gate.
- `Target user`: Multimodal model-evaluation and alignment teams.
- `Problem`: Hallucination metrics can improve while coverage, grounding, calibration, or general capability worsens, and online preference data can hide judge/generator failures.
- `Core workflow`: Import public-safe aggregate results and version metadata; validate schemas; compute fixed balanced metrics; check counterfactual-audit yields; compare against pre-registered thresholds; require human review for disagreements; export a signed decision record.
- `Data requirements`: Aggregate metrics, model/judge/generator/config identifiers, public or licensed slice names, counterfactual-audit counts, and checkpoint hashes. Raw images and prompts are not required for the public-report layer.
- `Architecture`: Local CLI, typed schema validator, fixed metric library, policy file, provenance adapter, static Markdown/JSON generator, and append-only decision ledger.
- `Success metrics`: Deterministic reruns; 100% required provenance fields; seeded omission and calibration failures rejected; zero forbidden-field findings in public exports; reviewer decision under 20 minutes.
- `Risk controls`: Local-first processing, aggregate outputs, strict allowlist, no automatic deployment, human approval, fixed thresholds, content hashing, and explicit non-certification label.
- `Limitations`: Cannot prove real-world factuality, judge fairness, source-image legality, or paper reproducibility; depends on evaluation slices and upstream audit quality.
- `MVP boundary`: Evaluation and provenance only; no model training, image generation, dataset acquisition, or production promotion.
- `Deployment model`: Local CLI or isolated batch job.
- `Evaluation plan`: Unit-test metric math, replay synthetic failure fixtures, compare with manual review, then test on one authorized public checkpoint report.
- `Failure modes`: Mis-specified metric direction, stale policy, incomplete slice coverage, aggregate-data manipulation, or false confidence from narrow fixtures.
- `Maintenance plan`: Version schemas, metric definitions, thresholds, slice registry, dependencies, and expected outputs; review policy changes separately from candidate runs.

Illustrative Python 3.11-only policy core:

```python
def decide(base, candidate, limits):
    checks = {
        "precision": candidate["precision"] >= base["precision"],
        "coverage": candidate["coverage"] >= base["coverage"] - limits["coverage_drop"],
        "general": candidate["general"] >= base["general"] - limits["general_drop"],
        "ece": candidate["ece"] <= base["ece"] + limits["ece_rise"],
    }
    return {"release": all(checks.values()), "checks": checks}
```

Security/privacy note: inputs must be schema-validated aggregates; do not include raw images, prompts, credentials, personal data, or local paths. Production use would require signed inputs, access control, tamper evidence, and independent metric tests.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| OViP | Primary paper | Failure-guided online multimodal preference learning reviewed here. | https://arxiv.org/abs/2505.15963 |
| Official OViP code | Official implementation | Training/evaluation structure and future reproduction path. | https://github.com/lsjlsj35/Online-Vision-Language-Preference-Learning-for-VLM-Hallucination |
| Direct Preference Optimization | Methodological foundation | Response preference objective adapted by OViP. | https://arxiv.org/abs/2305.18290 |
| POVID | Multimodal preference neighbor | Image-side preference/corruption context cited by OViP. | https://arxiv.org/abs/2402.11411 |
| VLM Probing DEP | Related Black Lake artifact | Fusion, modality-use, relation, leakage, and causal-evidence diagnostics. | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` |
| VideoWeave Geometry DEP | Related Black Lake artifact | Synthetic-media consistency and evidence-gate design. | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` |
| BA-LoRA Bias DEP | Related Black Lake artifact | Behavior preservation and drift controls during low-rank adaptation. | `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2505.15963 | Canonical identity, authors, dates, abstract, subjects, DOI/license/source links | 2026-07-14 | Primary metadata. |
| R2 | https://arxiv.org/html/2505.15963 | Full method, experiments, evaluation, limitations, appendices | 2026-07-14 | Primary full-paper HTML. |
| R3 | https://arxiv.org/pdf/2505.15963 | Complete paper body and visual/table cross-check locator | 2026-07-14 | Local verified PDF withheld. |
| R4 | https://arxiv.org/e-print/2505.15963 | TeX formulas, table signs, appendix details | 2026-07-14 | Local source archive and extracted text withheld. |
| R5 | https://doi.org/10.48550/arXiv.2505.15963 | Persistent source identity | 2026-07-14 | arXiv-issued DOI. |
| R6 | https://creativecommons.org/licenses/by/4.0/ | License target linked by arXiv | 2026-07-14 | Paper license context only. |
| R7 | https://github.com/lsjlsj35/Online-Vision-Language-Preference-Learning-for-VLM-Hallucination | Official implementation, dependencies, models/data instructions | 2026-07-14 | Inspected without execution. |
| R8 | Local verified archive unit and extraction cache (path withheld) | Random selection provenance, source integrity, extracted evidence | 2026-07-14 | Private processing evidence; no source files redistributed. |
| R9 | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Related diagnostic synthesis | 2026-07-14 | Repository-relative generated artifact. |
| R10 | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Related synthetic-visual consistency synthesis | 2026-07-14 | Repository-relative generated artifact. |
| R11 | `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` | Related adaptation-preservation synthesis | 2026-07-14 | Repository-relative generated artifact. |
| R12 | https://arxiv.org/abs/2305.18290 | Methodological reading: DPO | 2026-07-14 | Follow-up reading; not independent OViP validation. |
| R13 | https://arxiv.org/abs/2402.11411 | Methodological reading: multimodal preference fine-tuning | 2026-07-14 | Follow-up reading; surfaced through primary paper citations. |

## Appendix

### Replication Checklist

- [ ] Pin the exact official repository commit and record all nested code revisions.
- [ ] Resolve code, model, dataset, and benchmark licenses separately from the paper's CC BY 4.0 license.
- [ ] Build isolated training and evaluation environments with hashes and smoke-test outputs.
- [ ] Acquire only authorized LLaVA, Qwen, FLUX, and benchmark artifacts through bounded download plans.
- [ ] Reproduce baseline evaluation before training and verify metric directions/signs.
- [ ] Recompute AMBER/ObjectHal F1 and HRI from fixed source tables.
- [ ] Run at least three training seeds or document why compute prevents it.
- [ ] Audit negative images for target change, unrelated-content preservation, artifacts, safety, and bias.
- [ ] Compare judge outputs with blinded human and alternative multimodal-judge subsets.
- [ ] Report full precision, coverage, calibration, general-capability, compute, and failure-slice results.

### Process Validation Summary

- Uniform candidate count: 75,774 paper units.
- Selected zero-based index: 50,425.
- Duplicate exclusions and reselections: 0 and 0.
- Initial source state: partial; PDF present and full-paper HTML absent.
- Final source state: complete; both PDF and HTML integrity checks passed after bounded repair.
- Initial/final cache: miss to cached, with PDF, HTML, and source text.
- Public source deposition: none.
- Exactly three related DEP entries: VLM Probing, VideoWeave Geometry, and BA-LoRA Bias.

## Attribution Block

- Source URL: https://arxiv.org/abs/2505.15963
  - Applies to: this manuscript.
  - Notes: Canonical metadata, abstract, version history, DOI, license, and source links.
- Source URL: https://arxiv.org/html/2505.15963
  - Applies to: this manuscript.
  - Notes: Primary full-paper evidence for method, experiments, limitations, and appendices.
- Source URL: https://arxiv.org/pdf/2505.15963
  - Applies to: this manuscript.
  - Notes: Public PDF locator; local verified copy withheld.
- Source URL: https://arxiv.org/e-print/2505.15963
  - Applies to: this manuscript.
  - Notes: Public TeX-source locator used to resolve formulas and table formatting; local archive withheld.
- Source URL: https://doi.org/10.48550/arXiv.2505.15963
  - Applies to: source identity.
  - Notes: Persistent arXiv-issued identifier.
- Source URL: https://github.com/lsjlsj35/Online-Vision-Language-Preference-Learning-for-VLM-Hallucination
  - Applies to: implementation and reproducibility notes.
  - Notes: Official repository inspected without execution or redistribution.
- Source file: Withheld locally by policy.
  - Applies to: PDF, full-paper HTML, metadata HTML, TeX source, extraction cache, and private verification records.
  - Notes: No source files were uploaded, committed, staged, copied into this DEP, or sent to Slack.
