---
title: "MA-VLM Moderation - DEP-E"
generated_at: "2026-07-19 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of multi-agent VLM-guided self-training and PNU loss for low-resource offensive-content detection."
source_status: "verified complete local PDF, full-paper HTML, metadata HTML, and source package inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-19"
temporal_cutoff: "Sources and repository context inspected through 2026-07-19."
primary_url: "https://arxiv.org/abs/2511.13759"
stable_identifier: "arXiv:2511.13759v1; DOI:10.48550/arXiv.2511.13759"
deployment_job_id: "BLAD-2200-20260719-7D93E819"
deployment_item_id: "BLAD-2200-20260719-7D93E819-P01"
confidence_summary: "High for source identity, mechanism, tables, and official-repository availability; medium for generalization and fairness; low for production readiness because experiments were not reproduced."
safety_scope: "offline research, synthetic/public evaluation, human-reviewed moderation assistance only"
distribution_notes: "No PDF, HTML, metadata page, TeX/source archive, extracted text, cache, dataset, model, or local path is redistributed."
---

# MA-VLM Moderation - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Metadata | HTML | arXiv:2511.13759v1 | https://arxiv.org/abs/2511.13759 | CC BY 4.0 link visible; metadata page is not full-paper evidence. | 2026-07-19 | Inspected. |
| S2 | Official full-paper rendering | Primary paper | HTML | arXiv:2511.13759v1 | https://arxiv.org/html/2511.13759 | Verified local copy withheld. | 2026-07-19 | Inspected in full. |
| S3 | Paper PDF | Primary paper | PDF | arXiv:2511.13759v1 | https://arxiv.org/pdf/2511.13759 | Verified local copy withheld. | 2026-07-19 | Inspected through extraction and cross-checks. |
| S4 | Paper source package | Primary source | TeX archive | arXiv:2511.13759v1 | https://arxiv.org/e-print/2511.13759 | Local package and extracted text withheld. | 2026-07-19 | Inspected for equations, tables, and configuration. |
| S5 | arXiv-issued DOI | Persistent identity | DOI | 10.48550/arXiv.2511.13759 | https://doi.org/10.48550/arXiv.2511.13759 | Persistent locator. | 2026-07-19 | Resolved through arXiv metadata. |
| S6 | MA-VLM official repository | Official implementation | GitHub | public `main`; 25 commits visible | https://github.com/Social-AI-Studio/MA-VLM | Code and demo data have separate dependency/data terms; no release visible. | 2026-07-19 | README and visible tree inspected; not executed. |
| S7 | OViP Preference DEP | Related research | Markdown | DEP-E-20260714 | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` | Repository-generated synthesis, not primary evidence for this paper. | 2026-07-19 | Inspected. |
| S8 | Adversarial Label Noise DEP | Related research | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` | Repository-generated synthesis. | 2026-07-19 | Inspected. |
| S9 | RLMF Uncertainty DEP | Related research | Markdown | DEP-E-20260714 | `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` | Repository-generated synthesis. | 2026-07-19 | Inspected. |
| S10 | Selection, repair, and cache records | Process evidence | Private records | `BLAD-2200-20260719-7D93E819-P01` | Local paths withheld | Used only for selection, integrity, extraction, and no-source-upload claims. | 2026-07-19 | Verified. |

The paper lists Han Wang, Deyi Ji, Junyu Lu, Lanyun Zhu, Hailong Zhang, Haiyang Wu, Liqun Liu, Peng Shu, and Roy Ka-Wei Lee. It was submitted on 2025-11-14. The arXiv comments state “AAAI-26”; this artifact records that author-supplied venue context without independently asserting proceedings publication. Deployment job ID: `BLAD-2200-20260719-7D93E819`. Deployment item ID: `BLAD-2200-20260719-7D93E819-P01`.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5 | Canonical metadata | Title, authors, identifier, submission date, comments, subjects, DOI, license link. | Source identity and version. | High | Metadata does not validate method or results. |
| E2 | S2-S4 | Primary full paper | Introduction, method, equations, four datasets, experimental setup, Tables 1-5, appendix/source details. | Mechanism and reported evidence. | High for transcription | No training run or dataset audit was reproduced. |
| E3 | S2-S4, Table 1 | Primary quantitative evidence | `n=100` Accuracy/Macro-F1 across four tasks and six strategies. | Main performance comparison. | High for reported values | Single reported split; statistical uncertainty not identified. |
| E4 | S2-S4, Tables 3-5 | Primary ablations | Label-count, prompt-format, and `gamma` comparisons. | Low-resource and component claims. | High for reported values | Main ablation tables emphasize FHM and MAMI. |
| E5 | S6 | Official implementation | Data format, known/unknown split, MA-VLM inference, iterative training command, demo dataset, repository history. | Implementation availability. | Medium-high | Not cloned, installed, or executed; no release visible. |
| E6 | S10 | Process evidence | Uniform draw, cross-repository dedup, bounded repair, byte/marker validation, extraction cache. | Eligibility and complete-source gate. | High | Private source locations are withheld. |
| E7 | S7 | Related DEP evidence | On-policy multimodal preference loop and external-judge limits. | VLM feedback bridge. | Medium | Different task and optimization objective. |
| E8 | S8 | Related DEP evidence | Soft-target rectification and label-distribution mismatch. | Ambiguous-label bridge. | Medium | Adversarial robustness rather than moderation. |
| E9 | S9 | Related DEP evidence | Conditional metacognitive feedback and proxy governance. | Auxiliary-signal governance bridge. | Medium | Language uncertainty rather than classification. |

## Executive Summary

The paper proposes an iterative self-training system for offensive-content detection when only tens or hundreds of labels are available. A lightweight CLIP classifier ranks unlabeled examples. Two prompts to a frozen Qwen-2.5-VL-72B model simulate a strict moderator and a lenient user; each agent explains, reviews, and revises a judgment. Only three-way consensus becomes a soft pseudo-label. Disagreement is preserved as an unlabeled category rather than discarded. A customized PNU loss combines human-labeled data, soft consensus data, and contested data.

The reported evidence supports the narrow claim that this design helps on the four studied binary tasks. With 100 labels, the combined method reports Macro-F1 72.68 on FHM, 73.49 on MAMI, 86.69 on HSOL, and 77.11 on Sentiment140, improving over supervised-only CLIP in every task. It exceeds supervised-only Qwen-7B on FHM and HSOL but trails it on MAMI and Sentiment140. At 50 labels it remains above 70 Macro-F1 on FHM and MAMI. Prompt and loss ablations show dataset sensitivity rather than a universal setting.

The strongest reviewer inference is that explicit disagreement states are more reusable than the paper's “multi-agent” label. Both personas come from one model family and prompt frame, so agreement is correlated evidence, not independent human consensus. The paper motivates fairness and underrepresented communities but does not report demographic fairness, multilingual coverage, or real moderation outcomes. Confidence is high in the transcription of method and tables, medium in the mechanism's transfer value, and low for production deployment without multi-seed reproduction, annotation audits, subgroup evaluation, and human oversight.

## Detailed Summary

### Problem Context

Offensive labels depend on cultural context, sarcasm, modality, and normative judgment. These properties make annotation expensive and make early pseudo-label errors particularly dangerous. The paper contrasts four imperfect options: large-model prompting has high inference cost, augmentation can be semantically narrow, transfer learning still needs target labels, and traditional self-training compounds the errors of a weak initial classifier.

The proposed architecture separates expensive teaching from cheaper deployment. Qwen-72B supplies training-time judgments while CLIP-Large plus a one-layer MLP is iteratively trained as the efficient classifier. This is a form of teacher-guided self-training, not VLM fine-tuning.

### Five-Stage Self-Training Loop

1. Train the classifier on `n` human-labeled samples.
2. Predict the remaining unlabeled pool and order samples by classifier confidence.
3. Send the top `k` predictions to both VLM personas. Three-way agreement produces Positive or Negative `Agreed-Unknown`; any conflict produces `Disagreed-Unknown`.
4. Remove both categories from the unlabeled pool and retrain with the PNU objective.
5. Retain the round only when development performance improves; otherwise revert the classifier and discard that round's top-`k` batch.

The loop ends after the unlabeled pool is consumed. The development gate limits obvious degradation but repeated selection against one development set can turn it into a trajectory-level tuning target.

### Dual-Persona VLM Review

The moderator persona is safety-first; the user persona emphasizes freedom of expression. Each produces a first decision and rationale, reads the counterpart's rationale, and emits a revised decision. The paper frames this as negotiation that exposes implicit harm and competing social perspectives.

This procedure can increase prompt diversity, but role diversity is not model independence. A single base model can reproduce the same cultural blind spots in both personas, and rationale exchange can create convergence by persuasion rather than by new evidence. A follow-up should compare dual roles against repeated stochastic samples, independent model families, and human annotators.

### PNU Objective

Human-labeled positives and negatives enter standard PN risk. `Agreed-Unknown` examples receive soft targets rather than hard pseudo-labels. The reported values are `0.67` for positive and `0.33` for negative. `Disagreed-Unknown` examples enter PU or NU risk estimation. A dataset-specific `gamma` in `[-1,1]` combines these terms: positive values add PU influence, negative values add NU influence, and zero reduces to PN plus soft-PN learning.

The paper fixes the positive class prior at `0.5` because deviations reportedly introduce bias. That choice matches the balanced working sets but may not match live prevalence. Production transfer would require prevalence-shift monitoring and calibration rather than preserving `0.5` by default.

### Datasets and Splits

- FHM: 10,000 multimodal memes; the unlabeled official test set is excluded, leaving 9,000 examples.
- MAMI: 11,000 Instagram memes, using binary misogyny Task A.
- HSOL: 24,783 tweets; hate and offensive labels are merged into the positive class.
- Sentiment140: 1.6 million tweets; negative sentiment is treated as positive for binary-loss convention.

HSOL and Sentiment140 are balanced and subsampled to 10,000 examples. Every task uses an 80/10/10 split. The main comparison exposes only 100 labels inside the training partition and treats the rest as unlabeled. Macro-F1 is primary, with Accuracy also reported.

These datasets test modality and task transfer, but not the paper's motivating claim about minority languages. Binary mappings also erase finer distinctions—especially HSOL's separation of hate, offensive, and neither—and balanced sampling changes the operational class prior.

### Models and Training

Supervised-only baselines are Qwen-2.5-VL-7B, RGCL, and CLIP-Large. Qwen-7B uses LoRA. The self-training model fine-tunes CLIP-Large with a one-layer MLP and uses frozen Qwen-2.5-VL-72B as the teacher. Models train for 10 epochs with the best development epoch retained. `k=500`, class prior `0.5`, cross-entropy, and the soft targets noted above are the central settings. `gamma=0.0` is used for FHM and `0.1` for the other tasks.

The official repository documents JSONL train/dev/test/all files, known/unknown splitting, MA-VLM inference, and the iterative experiment command. It also exposes a 1,000-sample demo dataset and a running-results log. Public code improves inspectability, but this review did not resolve dependencies, inspect dataset licenses file by file, or rerun the system.

### Main Results at 100 Labels

| Strategy | FHM M-F1 | MAMI M-F1 | HSOL M-F1 | Sent140 M-F1 |
|---|---:|---:|---:|---:|
| Qwen-7B supervised only | 70.41 | 76.06 | 84.89 | 78.19 |
| CLIP supervised only | 59.24 | 62.18 | 85.30 | 64.22 |
| CLIP self-train, classifier pseudo-labels | 70.00 | 67.03 | 86.48 | 73.05 |
| CLIP self-train, Qwen pseudo-labels | 65.22 | 67.42 | 81.06 | 75.57 |
| CLIP self-train, combined | 72.68 | 73.49 | 86.69 | 77.11 |

Combined verification is the best self-training variant in this table. It does not dominate Qwen-7B everywhere. The teacher-only pseudo-label variant is sometimes worse than classifier-only, which supports the paper's complementarity argument and cautions against treating a larger model as a universal oracle.

### Label-Count Ablation

At `n=50`, combined self-training reports FHM/MAMI Macro-F1 of 71.27/71.40. Supervised-only CLIP reports 48.76/56.03, while Qwen-7B reports 39.11/73.00. At `n=250`, combined self-training reports 72.97/74.79, while Qwen-7B reports 75.88/76.18. The smaller model's relative advantage is strongest under extreme scarcity and narrows as human labels grow.

The full-label rows are not directly comparable to the iterative low-resource rows because training exposure changes. RGCL's low-resource results are omitted due to convergence failure, which is useful negative evidence but leaves an incomplete matrix.

### Prompt and Loss Ablations

For frozen Qwen-72B on MAMI, the dual-persona prompt reports Macro-F1 81.64 versus 79.17 zero-shot, 75.08 few-shot, and 78.28 chain-of-thought. On FHM it reports 74.62 versus 74.46 zero-shot and 74.43 chain-of-thought, so the advantage is dataset dependent.

For the trained pipeline, FHM Macro-F1 is highest at `gamma=0.0` among tested values, while MAMI is highest at `0.1`. Negative `gamma` is substantially worse in both displayed datasets. This indicates that disagreement should not receive a fixed universal weight.

### Evidence Boundary

The paper and repository provide enough detail for a serious reproduction attempt, but the present review is not a reproduction. Exact seed aggregation, run-to-run variance, annotation reliability, subgroup metrics, inference token cost, and production latency are not established in the inspected evidence. Claims that some ground-truth labels reflect annotator bias are based on examples and need a systematic relabeling study.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Dual-persona VLM verification improves pseudo-label quality. | Author mechanism and empirical claim | E2-E4 | Supported in combined-versus-single pseudo-label tables, but agent correlation is not isolated. | Medium-high |
| C2 | The combined method consistently beats supervised-only CLIP at `n=100`. | Author empirical claim | E3 | True for all four reported Macro-F1 values. | High for reporting |
| C3 | The lightweight classifier rivals or beats larger models in low-resource settings. | Author empirical interpretation | E3-E4 | True on selected tasks/settings, false as a universal claim; Qwen-7B remains higher on MAMI and Sent140 at `n=100`. | Medium |
| C4 | Useful information remains in disagreement samples. | Author mechanism claim | E2, PNU formulation and `gamma` ablation | Plausible; the ablation supports moderate PU influence on MAMI but not FHM. | Medium |
| C5 | The dual perspectives improve fairness and reliability. | Author interpretation | E2 | No demographic fairness or cross-cultural evaluation directly establishes this. | Low |
| C6 | The method works with as few as 50 labels. | Author empirical claim | E4 | Reported FHM and MAMI Macro-F1 exceed 70; only studied datasets/settings are supported. | High for reporting, medium for generality |
| C7 | Official code makes the pipeline inspectable. | Implementation observation | E5 | README, scripts, data layout, demo data, and 25 commits are visible; no release or execution was verified. | High for availability |
| C8 | The selected source was complete and non-duplicate before review. | Process claim | E6 | First draw passed dedup; partial unit was repaired and verified before synthesis. | High |

## Methodology

- `Research objective`: Produce a source-grounded DEP-E review of one uniformly selected, non-duplicate arXiv paper; preserve its method, evidence, limitations, and implementation implications; and synthesize exactly three related Black Lake records.
- `Sources inspected`: Canonical arXiv metadata, verified PDF, official full-paper HTML, source package, extracted PDF/HTML/source text, official repository README and visible tree, live repository authorities, private process evidence, and three related DEP manuscripts.
- `Discovery strategy`: Enumerated local PDFs with `rg --files -g "*.pdf"`, collapsed paths to parent-directory units, selected a uniform PowerShell index, resolved identity from adjacent metadata, scanned all dedup surfaces, repaired the selected source, extracted three text representations, inspected public primary sources, and searched Black Lake by conceptual overlap.
- `Inclusion criteria`: Evidence had to establish source identity, expose method/results/limits, document implementation availability, prove source/dedup status, or support a concrete feedback, soft-label, or auxiliary-signal relationship.
- `Exclusion criteria`: Abstract-only claims, secondary summaries, unexecuted code behavior, unrelated keyword hits, and source files prohibited from public deposition were excluded.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Author claims, reported measurements, implementation observations, reviewer interpretations, and process claims are labeled separately and tied to evidence IDs.
- `Uncertainty handling`: Non-reproduction, single-model agent correlation, unspecified multi-seed uncertainty, fairness gaps, dataset mapping choices, class-prior shift, and development-gate overfitting are explicit.
- `Extraction process`: Preflight found `pypdf`, HTML regex extraction, and source-package extraction. All three succeeded; no network access was used by the cache stage after the bounded archive repair.
- `Version control`: The paper is pinned to arXiv v1. The official repository was inspected on its public main branch; no commit pin or release is claimed.
- `Cross-checking`: Main tables, formulas, prompt roles, dataset mappings, and training arguments were checked across HTML and source text; PDF integrity supplied an independent complete-document representation.
- `Safety handling`: Implementation proposals are offline, synthetic/public-data first, non-enforcement, auditable, subgroup-aware, and human-authorized.
- `Reviewer stance`: DEP-ready preservation with critical review and bounded product translation.

### Random Selection and Deduplication

- Candidate enumeration: 75,778 PDFs and 75,776 unique PDF-parent paper units.
- Uniform selected index: 25,453 (one-based).
- Accepted identity: arXiv:2511.13759v1.
- Dedup scopes: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`; this automation's memory; current Black-Lake-Data relevant records; and current-job paper set.
- Dedup keys: arXiv ID, DOI, exact/normalized title, slug, artifact markers, and preceding-24-hour markers using public-safe cutoff date 2026-07-18.
- Exclusions: 0. Reselections: 0. First draw accepted.

### Source Integrity and Cache

- Initial state: partial because full-paper HTML was missing.
- Repair: preserved the existing valid PDF and retrieved official full-paper HTML, metadata HTML, and source package with one bounded direct-HTTPS attempt per missing artifact.
- PDF: 1,235,851 bytes, `%PDF-` header, trailing `%%EOF`.
- Full-paper HTML: 137,056 bytes; 37,347 body characters; `article` and LaTeXML document markers; 46 heading/section markers; six paper-structure terms; no rejected-payload markers.
- Unexpected partials: 0.
- Cache: `cached`; PDF text 48,862 bytes, HTML text 37,293 bytes, source text 96,922 bytes.
- Locality: original and extracted source files remain local and are excluded from all public staging.

## Scope, Constraints, and Assumptions

- `Scope`: Paper mechanism, reported evidence, official-code availability, three related DEP bridges, and bounded implementation guidance.
- `Temporal boundary`: Sources accessed through 2026-07-19; later revisions, code changes, or proceedings records are not included.
- `Evidence limits`: Experiments, datasets, dependencies, and code were not run; no independent fairness or annotation audit was performed.
- `Assumptions`: Table labels and dataset mappings are interpreted as printed; arXiv v1 is the reviewed version; repository README represents intended public use.
- `Constraints`: Source files stay local; offensive datasets can contain sensitive material; dataset licenses and consent must be reviewed separately; no consequential enforcement automation is authorized.
- `Out of scope`: Production moderation deployment, real-user profiling, automated takedowns, legal compliance certification, model/dataset redistribution, and broad novelty proof.
- `Intended use`: Research preservation, reproduction planning, offline evaluation design, and human-in-the-loop product ideation.
- `Audience`: ML researchers, moderation-systems engineers, dataset reviewers, safety teams, and governance reviewers.
- `Depth target`: Full manuscript review with implementation and replication boundaries.
- `Reproducibility boundary`: Public code and source detail support planning; no result is independently reproduced here.
- `Operational boundary`: Consensus scores may route human review or weight research losses, but must not independently trigger user-facing moderation action.
- `Data sensitivity`: Public research references; underlying offensive-content datasets may contain harmful, personal, or culturally sensitive material.

## Observations

- `Observed pattern`: Combined classifier-plus-VLM pseudo-labeling is more reliable than either alone in the main table, but the teacher-only variant sometimes underperforms classifier-only.
- `Observed pattern`: The benefit is largest under extreme label scarcity and narrows as labeled data increases.
- `Technical implication`: Agreement can be represented as a bounded weight and disagreement as an explicit queue, avoiding hard-label collapse.
- `Contradiction or tension`: The paper invokes diverse social perspectives while implementing them as role prompts to one model family.
- `Contradiction or tension`: Balanced benchmark sampling supports training stability but obscures real-world prevalence and threshold behavior.
- `Open question`: Does three-way consensus remain calibrated across languages, identity groups, code-switched text, and adversarial euphemisms?
- `Reviewer hypothesis`: Independent model-family diversity or human feedback may add more signal than reciprocal rationale exchange between two roles of one model.

## Considerations

Moderation research has asymmetric errors: false positives can suppress legitimate expression; false negatives can expose people to harm. Aggregate Macro-F1 cannot express these costs. Evaluation should report per-group false-positive/false-negative rates, calibration, abstention coverage, inter-annotator disagreement, and threshold trade-offs.

The VLM teacher is expensive even when excluded from production inference. A complete cost ledger needs prompt tokens, image processing, repeated-role calls, retries, storage, and iteration counts. The development gate needs a fresh validation protocol or nested holdout to avoid adaptive overfitting.

The data pipeline must preserve consent and license provenance, restrict access to harmful examples, redact personal data, and support reviewer well-being. Rationale storage may reproduce offensive text and should be minimized or hashed when analysis does not need raw content.

## Strengths

- Preserves disagreement instead of forcing every sample into a pseudo-label.
- Connects a practical self-training loop to explicit PU/NU risk rather than ad hoc filtering alone.
- Evaluates multimodal and text tasks with a common low-label setup.
- Reports prompt, label-count, and loss-weight ablations that reveal dataset sensitivity.
- Separates an expensive training-time teacher from a smaller inference-time classifier.
- Provides public code, demo data, commands, and a visible iterative pipeline.

## Weaknesses

- Two personas from the same VLM are correlated and do not demonstrate independent social perspectives.
- Fairness, multilingual coverage, cultural validity, and production moderation outcomes are not directly evaluated.
- Multi-seed uncertainty, significance testing, and run-to-run variance are not prominent in the inspected evidence.
- Balanced subsampling and binary label merging weaken operational-prevalence and taxonomy conclusions.
- A global class prior and dataset-level `gamma` may hide subgroup or time-varying uncertainty.
- Repeated development-set decisions can overfit the self-training path.
- Claims of ground-truth annotation bias are illustrated but not supported by a systematic relabeling study.
- The official repository has no visible release and was not independently executed here.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Compare role prompts with independent models and repeated samples | Agent contribution | Distinguish role-play from independent evidence | Cleaner causal attribution | More inference cost | Factorial ablation over model and prompt diversity |
| Calibrate consensus by stratum | Pseudo-label weights | Agreement reliability varies by topic, language, and group | Lower correlated-error amplification | Requires human labels | Reliability curves and subgroup ECE |
| Replace one development gate with nested holdouts | Iterative selection | Limit trajectory-level overfitting | More credible generalization | Less training data | Locked final test and pre-registered stopping |
| Learn bounded per-sample uncertainty weights | PNU objective | Global `gamma` obscures heterogeneity | Better ambiguous-sample use | New failure modes | Multi-seed ablation with clipping and calibration |
| Audit annotation disagreement directly | Ground truth | Paper infers bias from examples | Better construct validity | Reviewer burden | Multi-annotator relabeling and adjudication |
| Report cost and latency | Scalability | Training-time VLM calls can dominate | Honest deployment planning | Instrumentation effort | Tokens, GPU-hours, energy, and wall-clock ledger |

## Potential Implementations

1. **Offline consensus audit lab**
   - `User`: Safety researcher or dataset curator.
   - `Goal`: Measure when model-role agreement predicts human agreement.
   - `Core mechanism`: Run three-way votes on public or consented samples and stratify by agreement, language, topic, and subgroup.
   - `Required inputs`: Versioned dataset, classifier, two role prompts, independent human labels.
   - `Outputs`: Calibration curves, disagreement inventory, subgroup error report.
   - `Risk controls`: Offline only, access controls, PII review, no automatic enforcement.
   - `Evaluation`: Held-out calibration and human inter-rater agreement.
2. **Bounded PNU reproduction sandbox**
   - `User`: ML engineer.
   - `Goal`: Reproduce the effect of soft consensus and disagreement routing.
   - `Core mechanism`: Compare supervised, hard pseudo-label, soft consensus, discard-disagreement, and PNU variants.
   - `Required inputs`: Public benchmark subset and frozen model versions.
   - `Outputs`: Multi-seed metrics, calibration, cost, and failure cases.
   - `Risk controls`: Synthetic/public data, immutable test split, no platform integration.
   - `Evaluation`: Pre-registered multi-seed Macro-F1, ECE, and subgroup slices.
3. **Human-review prioritizer**
   - `User`: Authorized moderation quality team.
   - `Goal`: Allocate scarce human review to the most informative cases.
   - `Core mechanism`: Route model disagreement and low calibrated consensus to review; never act on consensus alone.
   - `Required inputs`: Model outputs, calibrated uncertainty, policy taxonomy, reviewer capacity.
   - `Outputs`: Review queue with provenance and reason codes.
   - `Risk controls`: Human authorization, appeal path, data minimization, audit logs.
   - `Evaluation`: Review yield, false-positive reduction, reviewer burden, and appeal outcomes.

## Three Ways to Exercise This Research

1. `Consensus calibration`: Use 1,000 synthetic or licensed examples, run the three voters, obtain blinded human labels, and produce reliability diagrams by agreement stratum. Success is monotonic calibration with declared confidence intervals; stop if subgroup counts are inadequate or raw content handling is not approved.
2. `Loss-only reproduction`: Freeze a public feature set and compare PN, soft-PN, and bounded PNU objectives across at least five seeds. Success is a pre-registered improvement that survives confidence intervals; stop if test data influence hyperparameter selection.
3. `Disagreement queue simulation`: Replay model outputs without user actions and measure how different queue policies change reviewer load and error discovery. Success is higher error yield at bounded workload without subgroup coverage loss; stop before any live moderation integration.

## Example MVP Product

- `Product name`: Consensus Moderation Lab.
- `Target user`: Research and quality-assurance teams evaluating moderation datasets and models.
- `Problem`: Teams cannot tell whether multiple model judgments provide independent evidence or merely correlated confidence.
- `Core workflow`: Import a versioned public/consented dataset; run classifier and role prompts; compute agreement strata; sample blinded human review; display calibration, subgroup errors, and reproducible comparison reports.
- `Data requirements`: Synthetic, public, or explicitly authorized examples; versioned labels; minimal demographic attributes only when lawful and necessary; no live user enforcement feed.
- `Architecture`: Local batch runner, model adapters, immutable split registry, decision ledger, human-review interface, and static report generator.
- `Success metrics`: Calibration error, Macro-F1 with confidence intervals, subgroup false-positive gaps, disagreement-review yield, reviewer burden, and reproducibility across seeds.
- `Risk controls`: Offline-only default, role-based access, content warnings, PII screening, encrypted storage, raw-rationale minimization, human authorization, appeal simulation, and deletion/retention policy.
- `Limitations`: Does not prove fairness, legal compliance, cultural validity, or live deployment safety; VLM access and harmful-content review remain costly.
- `MVP boundary`: No automated takedowns, user scoring, surveillance, continuous platform ingestion, or production model updates.
- `Deployment model`: Local batch application inside an authorized research environment.
- `Evaluation plan`: Unit tests for routing, locked-split smoke tests, multi-seed benchmark, subgroup audit, and human-review usability study.
- `Failure modes`: Correlated agents, label leakage, development overfit, missing subgroup coverage, prompt drift, and rationale data exposure.
- `Maintenance plan`: Pin models/prompts, version taxonomies and datasets, refresh calibration after change, and require review for every deployment candidate.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| OViP Preference - DEP-E | Black Lake research artifact | Model-specific VLM feedback loops and judge dependence | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` |
| Adversarial Label Noise - DEP-E | Black Lake research artifact | Distributional labels, soft rectification, and teacher limits | `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` |
| RLMF Uncertainty - DEP-E | Black Lake research artifact | Conditional auxiliary feedback and evaluator-proxy governance | `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` |
| Non-negative PU learning | Primary methodological predecessor | Stabilized PU risk used by the paper's derivation | https://arxiv.org/abs/1703.00593 |
| PNU classification | Primary methodological predecessor | Unifies positive, negative, and unlabeled risk | https://doi.org/10.24963/ijcai.2017/151 |
| Official MA-VLM implementation | Official code | Public pipeline and demo data | https://github.com/Social-AI-Studio/MA-VLM |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2511.13759 | Identity, metadata, abstract, venue comment, license link | 2026-07-19 | Canonical metadata; not full-paper evidence. |
| R2 | https://arxiv.org/html/2511.13759 | Full method, experiments, tables, conclusions | 2026-07-19 | Verified complete local rendering withheld. |
| R3 | https://arxiv.org/pdf/2511.13759 | Full-paper cross-check and integrity | 2026-07-19 | Verified local PDF withheld. |
| R4 | https://arxiv.org/e-print/2511.13759 | Equations, tables, configuration, appendices | 2026-07-19 | Source package and extraction withheld. |
| R5 | https://doi.org/10.48550/arXiv.2511.13759 | Persistent identity | 2026-07-19 | arXiv-issued DOI. |
| R6 | https://github.com/Social-AI-Studio/MA-VLM | Official implementation availability | 2026-07-19 | README/tree inspected; code not run. |
| R7 | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` | VLM feedback bridge | 2026-07-19 | Related synthesis only. |
| R8 | `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` | Soft-label bridge | 2026-07-19 | Related synthesis only. |
| R9 | `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` | Auxiliary-signal governance bridge | 2026-07-19 | Related synthesis only. |
| R10 | Private selection, integrity, and extraction records | Randomness, dedup, repair, cache, source locality | 2026-07-19 | Local paths and files withheld; no source uploaded. |

## Appendix

### Selection and Integrity Receipt

- Automation: `Black Lake Arxiv DEP 2200 x10`.
- Deployment job ID: `BLAD-2200-20260719-7D93E819`.
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P01`.
- Random method: uniform PowerShell index after `rg` PDF enumeration and unique parent-unit collapse.
- Candidate units: 75,776; selected one-based index: 25,453.
- Duplicate exclusions: 0; reselections: 0; public-safe 24-hour cutoff date: 2026-07-18.
- Initial source state: partial. Final state after bounded repair: complete.
- PDF integrity: 1,235,851 bytes; header and EOF checks passed.
- Full-paper HTML integrity: 137,056 bytes; 37,347 body characters; required document, heading, and paper-structure markers passed.
- Cache status: `cached` for PDF, HTML, and source-package text.
- Original sources and cache: withheld locally.
- Public-source uploads: zero.

### Reproduction Checklist

- Pin arXiv v1 and a specific official-code commit before running.
- Record dataset source, license, split hashes, label mappings, and balancing procedure.
- Freeze train/development/test sets before pseudo-labeling.
- Compare role prompts, repeated samples, and independent model families.
- Use multiple seeds and confidence intervals.
- Report token counts, GPU-hours, wall clock, storage, and VLM-call failures.
- Audit calibration and subgroup errors before interpreting consensus.
- Preserve disagreements and human adjudication records.
- Keep the final test set untouched until all stopping and `gamma` choices are frozen.
- Do not connect the reproduction to live enforcement.
