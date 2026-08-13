---
title: "T23DAQA Quality - DEP-E"
generated_at: "2026-08-03 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of Multi-Dimensional Quality Assessment for Text-to-3D Assets: Dataset and Model."
source_status: "complete local PDF, full-paper HTML, and metadata inspected; source package unavailable; sources withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-03"
temporal_cutoff: "arXiv v1 and public repository context inspected through 2026-08-03"
primary_url: "https://arxiv.org/abs/2502.16915"
stable_identifier: "arXiv:2502.16915v1; DOI:10.48550/arXiv.2502.16915"
confidence_summary: "High for identity and source integrity; medium for transcription and author-reported metrics; low for unreplicated deployment transfer."
safety_scope: "Offline research evaluation, bounded implementation planning, and nonbinding decision support only."
distribution_notes: "Original PDF, HTML, metadata, cache, extracted text, dataset, model, and source package remain local and are not redistributed."
---

# T23DAQA Quality - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | 2502.16915v1 | https://arxiv.org/abs/2502.16915 | Metadata and public locators; source file withheld. | 2026-08-03 | Inspected |
| S2 | Full paper | Primary artifact | HTML | 2502.16915v1 rendering | https://arxiv.org/html/2502.16915 | Full-paper evidence; local copy withheld. | 2026-08-03 | Integrity checked and inspected |
| S3 | Primary PDF | Primary artifact | PDF | 2502.16915v1 | https://arxiv.org/pdf/2502.16915 | Full-paper evidence; local copy withheld. | 2026-08-03 | Integrity checked and inspected |
| S4 | Official repository | Official implementation/data context | GitHub | ZedFu/T23DAQA, default branch | https://github.com/ZedFu/T23DAQA | README and MIT license inspected; code/data not executed or redistributed. | 2026-08-03 | Inspected |
| S5 | Extraction cache summary | Processing record | JSON-derived summary | schema 1.0; cached | https://arxiv.org/abs/2502.16915 | Public-safe status only; local cache withheld. | 2026-08-03 | Inspected |
| S6 | SFOOD A Multimodal | Related DEP | Markdown | DEP-E | `.lake-data/DEP-E/DEP-E-20260731-SFOOD A Multimodal/sfood_a_multimodal_manuscript.md` | Synthesis only; public file linked in references. | 2026-08-03 | Inspected |
| S7 | AG3D Learning to Generate | Related DEP | Markdown | DEP-E | `.lake-data/DEP-E/DEP-E-20260724-AG3D Learning to Generate/ag3d_learning_to_generate_manuscript.md` | Synthesis only; public file linked in references. | 2026-08-03 | Inspected |
| S8 | SeGPruner 3D QA | Related DEP | Markdown | DEP-A | `.lake-data/DEP-A/DEP-A-20260725-SeGPruner 3D QA/2603.29437-whitepaper-review.md` | Synthesis only; public file linked in references. | 2026-08-03 | Inspected |

Paper title: *Multi-Dimensional Quality Assessment for Text-to-3D Assets: Dataset and Model*.

Authors: Kang Fu; Huiyu Duan; Zicheng Zhang; Xiaohong Liu; Xiongkuo Min; Jia Wang; Guangtao Zhai. Submitted 2025-02-24; arXiv version v1; subject category `cs.CV`. The source unit was initially partial but was repaired before review. The final PDF and full-paper HTML passed the required integrity checks. No local source path is exposed in this public artifact.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Official metadata | Title, authors, date, version, subject, DOI, abstract, and public locators | Source identity and scope | High | Abstract is not sufficient for empirical claims. |
| E2 | S2/S3 | Primary paper | Introduction, database construction, method, protocol, results, ablation, conclusion | Mechanism and reported evidence | High for transcription | Author claims were not independently reproduced. |
| E3 | S2/S3 | Primary paper | 969 assets, 170 prompts, six generators, 17 raters, three rating axes, projection protocol, and MOS processing | Dataset and human-evaluation design | High | Dataset sampling and rater generalization remain bounded. |
| E4 | S2/S3 | Primary paper | Projection-based shape, texture, and text-image alignment encoders with MLP regression | Model mechanism | High | Implementation details are source-described, not rerun. |
| E5 | S2/S3 | Primary paper | Table III and Table IV metrics, including proposed-model correlations and ablations | Reported quantitative results | Medium | Results depend on the paper's split, code, data, and environment. |
| E6 | S4 | Official repository | README, database description, download pointers, citation, and MIT license | Reproducibility and redistribution context | Medium-high | Presence does not establish a successful build or reproduction. |
| E7 | S5 | Processing summary | `cached` status, `pypdf`/`html-regex` extractors, missing source package, and text-output presence | Cache methodology and provenance | High | Cache is a derived local record, not primary evidence. |
| E8 | S6/S7/S8 | Related DEP manuscripts | Multimodal benchmark, 3D generation, and 3D QA/selection patterns | Related research bridge | Medium | Related entries do not validate the selected paper's metrics. |

## Executive Summary

This paper studies how to assess text-to-3D assets in a way that is closer to human judgment than a single image or geometry metric. It introduces the AIGC-T23DAQA database and a projection-based T23DAQA model that separately predicts quality, authenticity, and text-asset correspondence. The authors report 969 validated assets from 170 prompts and six text-to-3D generators, scored by 17 human raters.

The model uses projection videos for shape, front/back projections for texture, and CLIP-based text-image alignment features before a three-layer MLP regression head. In the paper's reported 4:1 split with ten random splits, the proposed model reaches SRCC/KRCC/PLCC values of `0.6728/0.4909/0.6840` for authenticity, `0.7000/0.5157/0.7297` for correspondence, and `0.7853/0.5987/0.7828` for quality. These values are author-reported and were not reproduced here.

The durable contribution is the evaluation decomposition. A generated asset can be visually polished, plausible, and prompt-aligned to different degrees; an evaluator that collapses these into one scalar can hide the tradeoff. The evidence supports a research benchmark and a bounded triage aid, not autonomous acceptance, training-loss substitution, or general deployment readiness.

## Detailed Summary

### Problem and background

Text-to-3D systems generate assets through heterogeneous implicit or explicit representations and often inherit failure modes from the 2D generative model, optimization process, and prompt. The paper argues that common image-quality, video-quality, mesh-quality, and point-cloud-quality metrics do not fully capture floating artifacts, multi-view inconsistency, unrealistic structure, or prompt mismatch. Human review can capture these dimensions but is slow and costly.

### Dataset construction

The authors select 170 prompts from PartiPrompts across 11 challenge categories and 12 scene categories. They generate 1,020 candidate assets from six systems—DreamFusion, Latent-NeRF, Magic3D, ProlificDreamer, SJC, and TextMesh—and remove 51 failed generations, leaving 969 assets. Each is rendered into a 360-degree projection video of 120 frames at 512×512 resolution and four seconds total duration.

### Human evaluation and processing

Seventeen participants rate quality, authenticity, and text-asset correspondence separately using 0–5 sliders with 0.1 minimum increments. The protocol follows ITU-R BT.500-13 guidance, randomizes presentation, and splits each participant's workload into three sessions with breaks. The paper describes kurtosis-based outlier handling, subject rejection above a 3% outlier rate, z-score normalization, and rescaling to `[0, 100]` before mean opinion scores are computed. No subjects were rejected in the reported study.

### Proposed method

The evaluator first renders or receives circular projections. A Swin3D-S encoder extracts shape features from the projection video. Two Swin-S image encoders process front and back projections for texture features. A CLIP image encoder and text encoder produce an alignment feature. The concatenated features feed a three-layer MLP with 1024, 128, and 3 neurons, producing quality, authenticity, and correspondence scores.

Training combines a linearity loss with a rank loss, weighted by a hyperparameter reported as `0.3`. The design is projection-based, which makes it applicable to heterogeneous 3D representations, but it also makes viewpoint policy, rendering quality, and projection cost part of the effective evaluation system.

### Experiments and results

The paper compares traditional and learning-based NR-IQA, NR-VQA, NR-MQA, NR-PCQA, LMMQA, T2IQA, T2VQA, and alignment baselines. Learning-based methods use a 4:1 train/test split, ten random splits, Adam with an initial learning rate of `1e-4`, batch size `4`, 50 epochs, and 224×224 input frames where applicable. The proposed method is the best listed method in Table III for all three dimensions under SRCC, KRCC, and PLCC.

The ablation study removes or isolates the shape, texture, and text-image alignment modules. The full configuration is strongest in the listed table, while the text-image alignment component contributes substantially. The source also reports that correspondence scores tend to be higher than quality and authenticity scores, which the authors interpret as evidence that 2D text-image supervision transfers prompt alignment more reliably than 3D geometric consistency.

### Limitations and conclusion

The paper's evidence is limited to one curated dataset, six generators, 170 prompts, 17 raters, and the stated benchmark protocol. The official repository exposes code/data context and an MIT license, but this review did not download or execute the dataset, model, or training pipeline. External validity across modern generators, prompt distributions, viewpoints, raters, and production latency remains open.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | AIGC-T23DAQA is a 969-asset, 170-prompt, six-generator benchmark with quality, authenticity, and correspondence ratings. | Author claim | E3 | Directly supported by the full paper and arXiv HTML; dataset contents were not independently inspected. | High for transcription |
| C2 | The proposed evaluator combines shape, texture, and text-image alignment features from projections. | Author claim / mechanism | E4 | Method sections make the mechanism legible and distinct from a single-score baseline. | High for transcription |
| C3 | The proposed method outperforms listed baselines on the paper's Table III metrics. | Author-reported result | E5 | Supported as a source claim; no reproduction, confidence interval, or cross-dataset test was added here. | Medium |
| C4 | Text-asset correspondence can be high while geometry and authenticity remain weak. | Reviewer interpretation grounded in source analysis | E3, E5 | Plausible and operationally important; should be tested with adversarial prompt and multi-view cases. | Medium |
| C5 | The evaluator is production-ready or safe as an unconditional training loss. | Unsupported implication | No supporting evidence | Rejected pending shift tests, uncertainty calibration, cost accounting, and human-oversight controls. | High rejection confidence |

## Methodology

- `Research objective`: Preserve the selected paper's identity, mechanism, evidence, limitations, and safe implementation implications in a reusable DEP-E manuscript.
- `Sources inspected`: Official arXiv metadata, repaired full-paper PDF and HTML, local missing-only extraction summary, official repository README and MIT license, and exactly three related Black Lake manuscripts.
- `Discovery strategy`: Enumerate PDF-backed units with `rg --files -g "*.pdf"`; collapse parent directories; draw uniformly with PowerShell `Get-Random`; check the public dedup index, logs, reports, DEP paths, automation memory, and recent markers; then inspect primary and related sources.
- `Inclusion criteria`: Eligible paper unit with verified full PDF and full-paper HTML; primary methods, dataset, evaluation, limitations, official repository context, and concrete related DEP overlap.
- `Exclusion criteria`: Prior ID/DOI/title/slug/artifact matches, same-paper recent markers, abstract-only or invalid source units, local source redistribution, and unreproduced claims presented as independent facts.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication planning.
- `Evidence handling`: Evidence IDs distinguish metadata, primary-paper method/results, derived cache status, official repository context, and related-DEP synthesis. Author claims and reviewer inferences are labeled separately.
- `Uncertainty handling`: Missing source package, unavailable `pdftotext`, absent independent reproduction, bounded dataset coverage, and deployment-cost uncertainty remain explicit.
- `Random selection methodology`: `75960` PDFs collapsed to `75957` unique parent paper units; zero-based draw `30907`; first draw accepted; duplicate exclusions `0`; reselections `0`.
- `Cache methodology`: Run extractor preflight, observe `pdftotext` unavailable and `pypdf` available, then run `extract-arxiv` in `missing-only` mode against the selected unit and central archive cache. The initial cache miss became `cached`; PDF and HTML text were produced; source text was unavailable because the source package was unavailable.
- `Dedup/reselection validation`: Check arXiv ID `2502.16915`, base ID, DOI, normalized title, slug, public artifact paths, automation memory, repository logs/reports/DEP entries, and 24-hour markers before synthesis. No match was found.
- `Review stance`: Source-grounded paper review, critique, DEP-ready preservation, bounded product translation, and replication planning; not independent reproduction.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's problem, dataset, human-evaluation protocol, model architecture, reported results, limitations, related research bridge, and safe implementation paths.
- `Temporal boundary`: Public sources and repository context inspected on 2026-08-03; paper version is arXiv v1.
- `Evidence limits`: Official code/data were not executed; no independent rater study, generator-shift evaluation, end-to-end latency study, or cross-dataset validation was performed; source package was unavailable.
- `Assumptions`: The arXiv record, DOI, full-paper HTML, PDF, and official repository identify the same work; reported metrics are transcribed from the inspected source tables.
- `Constraints`: Source locality, no public source upload, no credentials, no private-data handling, safe nonbinding use, and clear separation of author claims from reviewer inference.
- `Out of scope`: Production acceptance gates, autonomous asset publishing, use as an unconditional training objective, medical/legal/financial decisions, and any redistribution of the paper or dataset.
- `Intended use`: Research review, benchmark design, implementation planning, human-review routing, and future reproduction planning.
- `Audience`: Computer-vision researchers, 3D-generation engineers, benchmark maintainers, product reviewers, and safety/governance reviewers.
- `Reproducibility boundary`: The public paper and repository identify a plausible recipe; a valid reproduction still requires the dataset, dependencies, checkpoints, environment, and exact configuration.
- `Data sensitivity`: Public scholarly sources and public repository metadata; local source artifacts and derived cache are private to the archive.

## Observations

1. **Observed pattern:** The paper treats quality, authenticity, and correspondence as distinct axes. This is a stronger decision interface than a single aesthetic score because it exposes when prompt alignment masks geometric failure.
2. **Technical implication:** Projection is a portability layer across heterogeneous 3D representations, but viewpoint selection and rendering artifacts become part of the measurement boundary.
3. **Contradiction or tension:** The paper values human alignment while using a relatively small and curated rater/generator/prompt population; the same alignment may not transfer to new generators or cultures of visual preference.
4. **Open question:** Whether the benchmark predicts downstream selection by artists, game designers, or other asset users remains untested in the inspected evidence.
5. **Reviewer hypothesis:** A calibrated multi-axis score with an abstention path will be more useful than a scalar ranker for deployment because it can distinguish semantic fit from geometric trustworthiness.

## Considerations

Evaluation systems can become hidden policy when their scores decide which generated assets are retained. A deployment should preserve raw prompt, generator, version, projection policy, three-axis score, confidence, and reviewer disposition. The official repository's MIT license is visible, but that does not resolve the licenses of upstream models, prompt sources, generated assets, or the downloadable dataset. A production design should perform license and provenance review separately.

The benchmark also raises fairness and preference questions. Authenticity is partly a judgment about real-world plausibility, while correspondence is dependent on language, cultural knowledge, and prompt interpretation. New prompt families and independent raters should be treated as evaluation strata. The system should abstain when prompt family, generator, or viewpoint is outside the validated support rather than silently returning a confident score.

## Strengths

- The paper identifies an evaluation gap that is specific to text-guided 3D generation rather than assuming 2D or mesh metrics transfer unchanged.
- The database design separates three human-relevant axes and documents the prompt, generator, projection, and rating pipeline.
- The projection-based architecture is representation-flexible and the ablation study makes the contribution of shape, texture, and alignment features visible.
- The benchmark compares a broad set of baseline families and reports multiple rank/correlation metrics rather than one headline number.
- The official repository provides a public implementation/data locator and visible MIT license context, which improves follow-on auditability even without proving reproduction.

## Weaknesses

- The source evidence is bounded by one dataset, six generators, 170 prompts, 17 raters, and a particular projection policy.
- The paper's strongest table values are author-reported; this review did not rerun code, fetch data, inspect checkpoints, or reproduce training.
- Projection cost, model loading, preprocessing, and end-to-end latency are not sufficient evidence for a production cost claim without a complete systems measurement.
- The three-axis labels may still be correlated or ambiguous in difficult cases; calibration, inter-rater agreement, and uncertainty by stratum need more detail.
- A repository and a visible license do not establish that all dependencies, upstream models, generated assets, or dataset redistribution rights are clear.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add generator and prompt-family holdouts | Generalization | Tests shift instead of only random splits | More realistic external-validity estimate | More generation and rating cost | Report per-stratum SRCC/KRCC/PLCC with confidence intervals |
| Calibrate three-axis uncertainty | Safety and use | A score without confidence invites over-trust | Safer abstention and review routing | Requires calibration data and rater analysis | Reliability curves, coverage, and selective risk |
| Measure end-to-end system cost | Implementation | Projection and feature extraction can dominate runtime | Honest latency and throughput claims | Hardware and instrumentation burden | Matched pipeline timing including preprocessing and fallback |
| Release pinned reproduction metadata | Reproducibility | Repository presence alone is insufficient | Lower setup ambiguity | Maintenance cost and artifact licensing | Fresh environment build plus table-level reproduction |
| Add task-user validation | Product relevance | Correlation with raters may not equal workflow value | Evidence for asset triage utility | Recruitment and task design | Blinded selection study with artists/designers |

## Potential Implementations

1. **Offline asset triage:** a local batch tool scores candidate assets separately on quality, authenticity, and correspondence, stores the prompt/generator/projection metadata, and sends low-confidence or shifted items to human review. Evaluation uses prompt-family holdouts and reviewer agreement; no automatic publication is allowed.
2. **Benchmark and regression harness:** a reproducible harness runs the evaluator and simple baselines on a versioned, licensed sample, reports per-prompt and per-generator results, and detects regressions after model or renderer changes. It keeps source files and datasets outside the public DEP.
3. **Training diagnostic monitor:** a research pipeline joins the score vector with downstream selection or rejection outcomes and uses it as an analysis signal. It requires leakage checks, a frozen holdout, calibrated abstention, and a conservative reference path before any score affects training.

## Three Ways to Exercise This Research

1. **Synthetic three-axis smoke test:** Create a small set of licensed or synthetic prompt/asset records with manually assigned quality, authenticity, and correspondence labels. Verify score-vector storage, per-axis ranking, minimum-axis review gates, and reproducible report generation. Stop if a single aggregate score hides a deliberately constructed axis conflict.
2. **Projection-policy sensitivity test:** Use a bounded set of public or synthetic 3D assets and render them under two documented camera/viewpoint policies. Compare per-axis scores, rank stability, and reviewer judgments. Stop before treating the result as generalization beyond the chosen assets and renderers.
3. **Held-out prompt-family evaluation:** Partition a licensed benchmark by prompt family, keep one family unseen during calibration, and compare the evaluator with a simple text-image baseline and a human-review route. Success requires per-family metrics and uncertainty reporting; stop if the holdout contains too few supported examples.

## Example MVP Product

- `Product name`: T23DAQA Review Desk.
- `Target user`: A 3D-content researcher or designer choosing among generated assets.
- `Problem`: Candidate assets may match a prompt while differing in visual quality, plausibility, and multi-view consistency; one scalar or ad hoc review is hard to audit.
- `Core workflow`: Import a prompt and candidate asset references; render a documented projection set; compute or enter three-axis scores; display score tradeoffs and confidence; route shifted or low-confidence cases to human review; export a provenance record.
- `Data requirements`: Licensed prompts, candidate asset references, generator/version metadata, projection settings, score vectors, confidence/calibration records, reviewer decisions, and holdout labels. Do not ingest private or restricted data without authorization.
- `Architecture`: Local-only UI or CLI, a versioned projection adapter, pluggable score backends, an auditable JSON/Markdown record, a calibration module, and a human-review queue. Original source files remain outside the public repository.
- `Success metrics`: Agreement with blinded reviewer rankings on a held-out prompt family; per-axis calibration coverage; abstention precision; end-to-end latency; and audit-record completeness.
- `Risk controls`: No autonomous publication; separate axes rather than one hidden score; abstain on unknown generators/prompt families; show version and projection metadata; retain reviewer override; perform license checks; keep raw assets local.
- `Limitations`: The MVP cannot establish broad perceptual validity, replace expert review, or guarantee that a high score corresponds to artistic or commercial value.
- `MVP boundary`: Research triage only; no training-loss integration, public asset marketplace decisions, or unreviewed automated deletion.
- `Deployment model`: Local workstation or controlled internal batch job.
- `Evaluation plan`: Smoke tests, prompt-family holdout, projection sensitivity, reviewer agreement, license review, and independent reproduction attempt.
- `Failure modes`: Projection artifacts, prompt ambiguity, generator shift, calibration drift, dataset leakage, score gaming, and false confidence from correlated dimensions.
- `Maintenance plan`: Version the renderer, score backend, calibration set, prompt taxonomy, license register, and fallback thresholds; review after every generator or backbone change.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| SFOOD A Multimodal | Related DEP manuscript | Multi-attribute multimodal benchmark and source-grounded evaluation | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260731-SFOOD%20A%20Multimodal/sfood_a_multimodal_manuscript.md |
| AG3D Learning to Generate | Related DEP manuscript | Upstream 3D avatar generation and appearance-quality context | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260724-AG3D%20Learning%20to%20Generate/ag3d_learning_to_generate_manuscript.md |
| SeGPruner 3D QA | Related DEP manuscript | 3D task quality and representation-selection boundary | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260725-SeGPruner%203D%20QA/2603.29437-whitepaper-review.md |
| T23DAQA official repository | Official implementation/data context | Code, database locator, citation, and MIT license visibility | https://github.com/ZedFu/T23DAQA |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2502.16915 | Identity, authors, date, version, DOI, abstract, and public source links | 2026-08-03 | Metadata is not used alone for empirical claims. |
| R2 | https://arxiv.org/html/2502.16915 | Full-paper method, dataset, human protocol, results, ablation, and conclusion | 2026-08-03 | Verified full-paper HTML; local copy withheld. |
| R3 | https://arxiv.org/pdf/2502.16915 | Primary PDF and source-first review | 2026-08-03 | Verified PDF; local copy withheld. |
| R4 | https://doi.org/10.48550/arXiv.2502.16915 | Persistent paper identity | 2026-08-03 | arXiv-issued DOI. |
| R5 | https://github.com/ZedFu/T23DAQA | Official README, database description, citation, and MIT license | 2026-08-03 | Repository inspected; code/data not executed. |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260731-SFOOD%20A%20Multimodal/sfood_a_multimodal_manuscript.md | Related multimodal benchmark synthesis | 2026-08-03 | Related DEP; not evidence for primary metrics. |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260724-AG3D%20Learning%20to%20Generate/ag3d_learning_to_generate_manuscript.md | Related 3D generation synthesis | 2026-08-03 | Related DEP; not evidence for primary metrics. |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260725-SeGPruner%203D%20QA/2603.29437-whitepaper-review.md | Related 3D QA/selection synthesis | 2026-08-03 | Related DEP; not evidence for primary metrics. |

## Appendix

### Source-integrity and public-output validation

The initial source state was classified as partial because the PDF existed without full-paper HTML. A bounded archive repair preserved the valid PDF and retrieved official metadata/full-paper HTML. Final verification passed the PDF header/EOF and full-paper HTML body, marker, heading, and structure checks. The TeX/source package was unavailable. The extraction cache was created in `missing-only` mode with `pypdf` and `html-regex`; `pdftotext` was unavailable, and source text is absent.

The random selection was uniform over unique parent-directory paper units. Dedup/reselection validation checked the public pointer index, repository artifacts, automation memory, and recent markers before synthesis. The public-output allowlist contains only this manuscript, the DEP README, the Report-Mark, two public-safe logs, and the required derived dedup JSON. No source file, local path, cache, extracted text, or `.source/` directory is included.
