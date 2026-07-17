---
title: "Residual Gaussian CBCT - DEP-E"
generated_at: "2026-07-17 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of residual Gaussian splatting with wavelet-guided initialization for ultra sparse-view CBCT reconstruction."
source_status: "verified local source bundle; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-17"
temporal_cutoff: "arXiv v1 and public repository evidence inspected through 2026-07-17"
primary_url: "https://arxiv.org/abs/2604.27552"
stable_identifier: "arXiv:2604.27552v1; DOI:10.48550/arXiv.2604.27552"
confidence_summary: "High for source identity, method, and table transcription; medium for generalization; low for reproducibility and clinical readiness."
safety_scope: "non-diagnostic research review, synthetic evaluation, and human-reviewed medical-imaging tooling"
distribution_notes: "Generated Markdown only; PDF, full-paper HTML, metadata HTML, e-print source, integrity records, extracted text, and temporary renders were withheld locally."
---

# Residual Gaussian CBCT - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *Residual Gaussian Splatting for Ultra Sparse-View CBCT Reconstruction* | Primary paper | Verified PDF | arXiv:2604.27552v1 | https://arxiv.org/pdf/2604.27552 | Inspected locally as evidence; not redistributed. | 2026-07-17 | Complete 10-page paper inspected and selected pages rendered |
| S2 | Official arXiv full-paper rendering | Primary full text | HTML | arXiv:2604.27552v1 | https://arxiv.org/html/2604.27552 | Full-paper HTML; not an abstract page; retained locally only. | 2026-07-17 | Integrity-verified and inspected |
| S3 | arXiv abstract and metadata | Primary metadata | HTML | Submitted 2026-04-30; v1 | https://arxiv.org/abs/2604.27552 | Metadata/provenance only; never counted as the paper. | 2026-07-17 | Inspected |
| S4 | arXiv e-print | Primary manuscript source | gzip/tar source package | arXiv:2604.27552v1 | https://arxiv.org/e-print/2604.27552 | Valid source archive retained locally; no redistribution permission inferred. | 2026-07-17 | Format verified; source files withheld |
| S5 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2604.27552 | https://doi.org/10.48550/arXiv.2604.27552 | Public metadata locator. | 2026-07-17 | Recorded |
| S6 | RGS repository | Paper-declared implementation | GitHub repository | Default branch inspected | https://github.com/yqx7150/RGS | Public repository; license not established from inspected tree. | 2026-07-17 | Recursive tree contained only `README.md` |
| S7 | Exactly three related Black Lake DEP manuscripts | Related processed research | Markdown | Hypercomplex MRI; AFIDAF Vision; CAR Avatar | See the related-research section below | Contextual synthesis only; does not validate RGS. | 2026-07-17 | Inspected |
| S8 | Black Lake repository authorities | Deposition and source-locality rules | Markdown | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Process authority, not research evidence. | 2026-07-17 | Fetched and inspected |
| S9 | Black-Lake-Data repository authority | Related DEP and dedup context | Markdown | Live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Process authority, not research evidence. | 2026-07-17 | Fetched and inspected |

Paper metadata:

- `Authors`: Jian Lin, Jiancheng Fang, Shaoyu Wang, Changan Lai, Yikun Zhang, Yang Chen, and Qiegen Liu.
- `Co-first authors`: Jian Lin and Jiancheng Fang, as stated in the paper.
- `Subject`: Computer Vision and Pattern Recognition (`cs.CV`).
- `Version`: v1, submitted 2026-04-30.
- `Paper length`: 10 pages, including references.
- `Primary evaluation`: six AAPM Mayo Clinic Low-Dose CT volumes under simulated 20-, 40-, and 60-view CBCT projection settings.
- `Additional evaluation`: qualitative reconstruction of an acquired rhinoceros beetle scan from 40 projections.
- `Local source paths`: withheld by public-output policy. Verified source artifacts remain outside the repository.
- `Source redistribution`: not authorized. No `.source/` directory was created.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S4 | Complete primary paper bundle | Abstract, introduction, related work, equations 1-17, Algorithm 1, experiment setup, Tables I-III, Figures 1-9, conclusion, and references | Identity, problem, mechanism, settings, source-reported results, ablations, and visible omissions | High for source reporting | No derivation or experiment was independently reproduced |
| E2 | S1/S2, Figure 3 | Primary visual and textual evidence | Ground-truth/3DGS spectra, high-frequency error map, frequency-dependent convergence plot | Author diagnosis of spectral bias in standard 3DGS | Medium-high | One displayed analysis; causal exclusivity is not established |
| E3 | S1/S2, Sections III-B to III-D | Primary method evidence | DWT initialization, non-negative saliency map, dual Gaussian field, residual projection loss, two-phase schedule | Physical-compatibility argument and RGS algorithm | High for description | Stability and convergence are not formally guaranteed |
| E4 | S1/S2, Table I and Figure 5 | Primary empirical evidence | Six-volume AAPM PSNR/SSIM at 20, 40, and 60 views; visual regions of interest | Comparative clinical-phantom performance | High for transcription | Simulated projections, point estimates, no uncertainty or reproduction |
| E5 | S1/S2, Tables II-III and Figures 6-8 | Primary ablation evidence | Wavelet-prior and curriculum-removal results; frequency and visual comparisons | Contribution of the two major design elements | High for transcription | Small selected subsets; no matched-compute or primitive-count controls |
| E6 | S1/S2, Figure 9 | Primary qualitative evidence | Forty-view acquired beetle projection and reconstructed slices | Feasibility on a real acquisition | Medium | No ground-truth volume or quantitative metric |
| E7 | S6 | Declared implementation | Current repository tree and README | Code-availability and reproducibility assessment | High for inspected state | Repository can change; absence today does not prove permanent absence |
| E8 | S7 | Related DEP artifacts | Medical undersampling, spatial/spectral operator allocation, and sparse-observation 3D refinement | Cross-DEP synthesis | Medium | Related artifacts do not validate RGS results |
| E9 | S8-S9 and private selection/integrity records summarized publicly | Process evidence | Live rules, random draw, dedup scans, PDF/HTML gates, repair result, no-source-upload policy | Eligibility, source completeness, and deposition compliance | High | Private paths and exact execution context are intentionally withheld |

## Executive Summary

Residual Gaussian Splatting (RGS) addresses a specific failure mode in ultra sparse-view cone-beam CT reconstruction: projection-loss optimization of a 3D Gaussian attenuation field tends to capture low-frequency anatomy before fine detail. The authors argue, and visualize in a frequency analysis, that standard 3D Gaussian splatting leaves persistent high-frequency error even after low-frequency error has converged. This produces reconstructions that suppress streak artifacts but smooth vascular, trabecular, and boundary detail.

RGS gives global structure and local detail separate Gaussian representations. A single-level 2D discrete wavelet transform processes every sparse projection. Its low-frequency subband is reconstructed by FDK and used to initialize a base Gaussian set. The absolute energy of three signed high-frequency subbands is summed into a non-negative saliency map and backprojected to initialize a smaller-scale detail set. Crucially, RGS does not ask a non-negative X-ray attenuation model to reproduce signed wavelet coefficients. It uses the wavelets only to locate likely detail, then learns the detail branch through residual error in the original projection domain.

The branches are optimized under a curriculum. The base set alone fits a low-frequency target for 5,000 iterations; both sets then refine the raw projections until iteration 25,000 while a low-frequency consistency term prevents the base branch from drifting into the detail role. The source uses 50,000 base primitives, 30,000 detail primitives, top-5% spectral saliency, a consistency weight of 0.5, and adaptive density control.

On six source-reported AAPM volumes, RGS has the highest average PSNR and SSIM at 20, 40, and 60 views. At 20 views, it reports 34.68 dB and 0.909 versus 34.15 and 0.897 for the next-best aggregate baseline, 3DGR. The advantage narrows at 60 views to 38.97/0.975 versus 38.77/0.971. RGS is not uniformly best on every volume and metric, so the evidence supports aggregate improvement rather than universal dominance. Wavelet and curriculum ablations report substantial average degradation when either component is removed.

Confidence is high that the manuscript describes the mechanism and reports these tables, medium that the design generalizes beyond the evaluated settings, and low that it is presently reproducible or clinically ready. The AAPM projections are simulated, the real-specimen evidence is qualitative, uncertainty and resource costs are absent, and the paper-declared GitHub repository currently contains only a README rather than executable code.

## Detailed Summary

### Problem context

CBCT reconstructs a three-dimensional attenuation volume from two-dimensional X-ray projections acquired around an object. Reducing the number of views lowers acquisition burden but makes the inverse problem more underdetermined. Analytical FDK reconstructions develop strong streak artifacts; iterative and learned approaches can suppress artifacts but often regularize away fine texture.

The paper positions explicit 3D Gaussian splatting between classical reconstruction and implicit neural fields. A Gaussian field is continuous and differentiably projectable. In the CT adaptation, each primitive has a position, covariance, and non-negative density contribution. Unlike opaque scene rendering, X-ray projection sums attenuation along rays under the Beer-Lambert model. An integrated 3D Gaussian yields a 2D Gaussian contribution, avoiding dense ray marching.

The proposed diagnosis is spectral bias. Gradient descent fits smooth, high-energy structure faster than fine variation. In the paper's Figure 3, a standard 3DGS reconstruction resembles the ground truth globally but loses high-frequency spectral energy; the corresponding error localizes near structural boundaries. A plot over training iterations shows low-frequency relative error falling while high-frequency error plateaus.

### Why direct wavelet supervision is rejected

A discrete wavelet transform decomposes a projection into one low-frequency approximation and three directional detail subbands. The detail coefficients are signed and approximately zero-mean. Physical X-ray attenuation and the Gaussian basis contributions are non-negative.

The paper analyzes an explicit high-frequency fitting loss. At a detector location where the target wavelet coefficient is negative, a rendered non-negative value cannot reach the target. The gradient therefore drives density downward rather than expressing the desired signed component. RGS calls this the incompatibility of spectral supervision.

The response is to separate localization from supervision. Wavelet magnitude identifies where detail is likely, but the actual detail content is learned from the ordinary projection residual. This is the paper's most technically coherent design choice: the spectral prior guides capacity without violating the measurement model.

### Spectrally decoupled initialization

For each projection, a single-level 2D DWT produces low-frequency `P_LF` and directional `P_LH`, `P_HL`, and `P_HH` components. FDK reconstructs `P_LF` into a coarse volume. Density thresholding removes air and initializes the base Gaussian set.

The paper forms a non-negative energy map

`M_HF = |P_LH| + |P_HL| + |P_HH|`.

Backprojection converts this map into a volumetric saliency prior. High-saliency locations initialize the detail Gaussian set. The final attenuation field is the sum of base and detail Gaussian basis functions, and their rendered projections likewise add.

This initialization assigns broad support and dominant low-frequency energy to the base branch. The detail branch uses smaller primitives localized to regions likely to contain boundaries and texture. It does not guarantee semantic correctness; it is a structured allocation of optimization capacity.

### Spectral-spatial collaborative optimization

The global loss compares the measured raw projection with the sum of base and detail projections. Under this loss, the detail gradient is driven by the projection content that remains after subtracting the base response.

Joint optimization from the first iteration is unstable in the authors' account. The broad base primitives begin from a stronger volumetric prior and can absorb errors that the detail branch should explain. The two branches then compete for the same residual, a failure the paper calls spectral crosstalk.

RGS therefore uses two phases:

1. `Phase I`: freeze the detail branch and fit the base projection to the low-frequency target.
2. `Phase II`: unfreeze both branches, fit the complete raw projection, and retain a low-frequency consistency penalty on the base branch.

Adaptive density control is applied in both phases. After optimization, the continuous Gaussian field is sampled on a Cartesian grid to produce the reconstruction volume.

### Experimental setup

The clinical study uses high-quality volumes from the AAPM Mayo Clinic Low-Dose CT Grand Challenge as ground truth. The paper voxelizes volumes to `256 x 256 x 256` and generates `512 x 800` digital radiographs to emulate CBCT. It evaluates six labeled volumes at 20, 40, and 60 views.

Baselines are:

- `FDK`: analytical reconstruction.
- `SART`: iterative algebraic reconstruction.
- `NAF`: an implicit neural attenuation field.
- `R2-Gaussian`: rectified radiative Gaussian splatting.
- `3DGR`: a 3D Gaussian representation for sparse-view CT.

RGS is implemented in PyTorch in the authors' account. It trains for 25,000 iterations. The base set begins with 50,000 large primitives; the detail set begins with 30,000 smaller primitives at opacity 0.01 and top-5% spectral saliency. The detail branch is frozen for 5,000 iterations. The low-frequency consistency weight is 0.5; the base learning-rate decay factor is 0.1. Position learning rate is annealed from `2e-3` to `2e-6`; density, scaling, and rotation rates are `1e-3`.

### Comparative results

Average Table I results:

| Views | FDK | SART | NAF | R2-Gaussian | 3DGR | RGS |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 21.94 / 0.528 | 30.19 / 0.847 | 30.80 / 0.855 | 33.83 / 0.892 | 34.15 / 0.897 | **34.68 / 0.909** |
| 40 | 24.88 / 0.615 | 33.27 / 0.920 | 34.30 / 0.930 | 36.78 / 0.944 | 37.17 / 0.945 | **37.59 / 0.954** |
| 60 | 26.18 / 0.696 | 35.50 / 0.952 | 36.09 / 0.957 | 38.63 / 0.968 | 38.77 / 0.971 | **38.97 / 0.975** |

Values are PSNR in dB / SSIM. The aggregate margin is largest at the most severe 20-view setting and decreases as view count rises. This trend is compatible with the proposed benefit: explicit detail guidance matters most when projections are sparse.

The table also contains counterexamples to blanket superiority. At 60 views on volume L109, 3DGR reports SSIM 0.983 versus 0.976 for RGS. On L506, 3DGR reports 0.981 versus 0.980. RGS has the higher PSNR in both rows. This metric tension should be preserved rather than hidden.

Figure 5 compares chest and abdomen slices at 20 views. The authors identify reduced streaks and sharper lung vasculature and trabecular bone. The visual review confirms that these regions are displayed, but the images are source-selected and do not substitute for blinded expert assessment.

### Ablation evidence

The wavelet-prior ablation uses three volumes at 40 views:

| Variant | Average PSNR | Average SSIM |
|---|---:|---:|
| Without wavelet prior | 35.86 | 0.936 |
| Full RGS | 37.22 | 0.951 |

The full model improves by 1.36 dB and 0.015 SSIM. A frequency plot shows the ablated model's high-frequency power falling away from the ground truth while relative error rises.

The curriculum ablation uses three other volumes at 40 views:

| Variant | Average PSNR | Average SSIM |
|---|---:|---:|
| Without curriculum | 34.65 | 0.922 |
| Full RGS | 37.62 | 0.953 |

The full model improves by 2.97 dB and 0.031 SSIM. This is a strong source-reported difference, but the paper does not expose repeated seeds or a matched analysis of primitive growth and compute.

### Real-specimen evidence

A physical rhinoceros beetle is scanned with 40 projections uniformly distributed over a full rotation. The paper compares FDK, SART, NAF, R2-Gaussian, and RGS slices. RGS is visually sharper in highlighted internal structures and the external shell. Because there is no ground-truth volume or quantitative metric, the experiment demonstrates acquisition-path feasibility and author-judged visual quality, not verified accuracy.

### Availability and reproducibility

The paper prints `https://github.com/yqx7150/RGS` as a public code location. The current recursive tree contains only `README.md`, which repeats the paper title. No source code, license, environment, dataset preparation, geometry files, configuration, checkpoints, split manifest, or reproduction commands were present in the inspected state. The manuscript's implementation claim should therefore be recorded as a declared intention rather than an actionable release.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Standard projection-optimized 3DGS exhibits spectral bias that suppresses high-frequency CBCT detail. | Author mechanism claim | E2 | Figure 3 supports the displayed instance; universality across configurations is not established. | Medium-high |
| C2 | Directly supervising a non-negative attenuation field with signed wavelet coefficients is mathematically incompatible. | Author analytical claim | E3 | The sign and gradient argument is coherent under the stated rendering model. | High |
| C3 | Wavelet magnitudes can initialize a non-negative detail prior while raw-projection residuals supply physically compatible supervision. | Author method claim | E3 | Directly supported by equations 5-14 and Algorithm 1. | High |
| C4 | A base warm-up followed by joint refinement reduces competition between global and detail components. | Author method/causal claim | E3, E5 | The curriculum ablation supports benefit, but no full optimization-dynamics study isolates every cause. | Medium-high |
| C5 | RGS has the best average PSNR/SSIM among evaluated methods at 20, 40, and 60 views. | Author empirical claim | E4 | Table I supports the aggregate statement; per-volume metric exceptions exist. | High for transcription |
| C6 | Wavelet guidance materially improves 40-view reconstruction. | Author empirical claim | E5 | Table II reports +1.36 dB and +0.015 SSIM on three volumes. | High for source reporting; medium for generality |
| C7 | Curriculum optimization materially improves 40-view reconstruction. | Author empirical claim | E5 | Table III reports +2.97 dB and +0.031 SSIM on three volumes. | High for source reporting; medium for generality |
| C8 | RGS transfers to real acquired tomography. | Author empirical claim | E6 | A qualitative beetle result supports feasibility, not calibrated accuracy or clinical transfer. | Medium-low |
| C9 | Source code is publicly available. | Author availability claim | E7 | The URL exists, but the current repository does not contain an implementation. | Low for usable availability |
| C10 | RGS is promising for high-precision biological or pre-clinical imaging. | Author implication | E4-E6 | Promising as a research direction; clinical or pre-clinical readiness is unsupported. | Low |

## Methodology

- `Research objective`: Uniformly select one eligible archived paper, enforce the complete-source gate, review it source-first, relate it to exactly three inspected DEP entries, and create a schema-complete public-safe DEP-E manuscript.
- `Sources inspected`: verified PDF; official full-paper HTML; metadata HTML; e-print format; paper-declared GitHub repository; live Black Lake and Black-Lake-Data READMEs; and exactly three related DEP manuscripts.
- `Discovery strategy`: enumerate PDFs with `rg --files -g "*.pdf"`; normalize unique parent directories as paper units; sort them; select a uniform zero-based PowerShell `Get-Random` index; inspect adjacent metadata; derive the arXiv ID; then check public arXiv and repository sources.
- `Inclusion criteria`: primary or official evidence that establishes identity, method, equations, experimental settings, table values, ablations, limitations, implementation availability, deposition rules, duplicate status, or concrete conceptual overlap.
- `Exclusion criteria`: abstract-only evidence for method/results, unrelated recommendation widgets, unverified claims, local source paths, source documents, exact local execution timestamps, and any clinical inference beyond the paper's evidence.
- `Analytical approach`: empirical table review, conceptual mechanism reconstruction, comparative analysis, implementation audit, safety/ethics review, product translation, and replication planning.
- `Evidence handling`: author claims, direct source evidence, reviewer interpretations, process evidence, and related-DEP synthesis use distinct labels. All numerical results remain source-reported.
- `Uncertainty handling`: no experiment was rerun; no theorem was formally checked; absent uncertainty, compute, calibration, or clinical evidence remains explicit rather than inferred.
- `Extraction process`: PDF text extraction and official HTML inspection were combined with visual inspection of rendered method, table, ablation, and real-specimen pages.
- `Version control`: the paper is pinned to arXiv v1. The public repository was inspected at its current default-branch state; because no implementation files were present, no code behavior was inferred.
- `Random selection`: 75,777 PDFs collapsed to 75,776 unique parent-paper units; uniformly selected zero-based index 48,493; first draw accepted.
- `Dedup and reselection validation`: the arXiv ID, DOI, normalized title, slug family, Black Lake logs/reports/DEP entries, automation memory, relevant Black-Lake-Data DEP entries, and preceding-24-hour markers were searched. Duplicate exclusions 0; other exclusions 0; reselections 0.
- `Source integrity`: initial state `partial` because full-paper HTML was absent. Bounded direct-HTTPS repair preserved the valid PDF and produced verified official full-paper HTML plus local provenance companions. Final state `complete`; zero partials.
- `Safety handling`: this artifact is non-diagnostic. No source document, protected imaging record, local path, machine identifier, username, exact timestamp, timezone label, or credential is public.
- `Reviewer stance`: critical research preservation, bounded implementation translation, and reproducibility planning.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2604.27552v1; spectral-bias motivation; wavelet-guided dual-Gaussian initialization; two-phase projection-domain optimization; AAPM comparisons; ablations; real-specimen result; public-code state; and three related DEP bridges.
- `Temporal boundary`: paper v1 submitted 2026-04-30; public repository and related artifacts inspected through the date-only marker 2026-07-17.
- `Evidence limits`: no code execution, training run, projection regeneration, table reproduction, statistical reanalysis, radiologist review, or external clinical validation.
- `Assumptions`: the paper's forward model and geometry are correctly implemented; reported baselines are fairly configured; the simulated AAPM projections reflect the stated view regimes; the extracted table values match the authors' runs.
- `Constraints`: medical data governance, dataset terms, compute cost, source redistribution, scanner calibration, dose/noise modeling, and human-review requirements.
- `Out of scope`: diagnostic recommendations, treatment decisions, claims of regulatory readiness, source redistribution, or a production CT implementation.
- `Intended use`: research review, DEP deposition, reproducibility planning, safe synthetic prototyping, and evaluation design.
- `Audience`: medical-imaging researchers, inverse-problem engineers, reconstruction reviewers, and product teams considering non-diagnostic research tools.
- `Depth target`: manuscript review with method reconstruction, evidence ledger, implementation translation, and replication checklist.
- `Reproducibility boundary`: the paper reports enough high-level hyperparameters to understand the design, but the absent implementation and missing geometry/split details prevent faithful reproduction.
- `Operational boundary`: examples may analyze synthetic phantoms or authorized datasets; they must not be used to provide autonomous clinical interpretation.
- `Data sensitivity`: the reviewed paper concerns medical images. Public examples should use synthetic, de-identified, properly licensed, or explicitly authorized data.

## Observations

- `Observed pattern`: RGS's average advantage is largest at 20 views and narrows with more views. This is consistent with a prior that matters most under severe undersampling.
- `Observed pattern`: the curriculum ablation has a larger average effect than the wavelet ablation on its displayed subset, suggesting that controlling branch competition may be at least as important as locating detail.
- `Technical implication`: spectral transforms are used as routing and initialization devices, not as incompatible output targets. This distinction is broadly reusable in physics-constrained learning.
- `Technical implication`: primitive counts are part of the method's capacity budget. Without reporting post-density-control counts, memory, and time, efficiency cannot be inferred from 3DGS terminology alone.
- `Contradiction or tension`: the paper describes extensive clinical evidence, yet the principal AAPM projections are simulated from CT volumes and the acquired specimen is non-clinical and qualitative.
- `Contradiction or tension`: code is declared public, but the official repository currently lacks code.
- `Open question`: would matched-compute baselines with equal primitive budgets and identical projection operators preserve the same margin?
- `Open question`: are high-frequency gains robust to dose noise, motion, scatter, metal, and geometry errors, or do the detail primitives amplify model mismatch?
- `Reviewer hypothesis`: a calibrated residual/spectral audit may provide practical value even before the full RGS method is reproduced, because it can detect local-detail loss hidden by global PSNR/SSIM.

## Considerations

- `Clinical validity`: PSNR and SSIM do not establish diagnostic preservation. Evaluation should include task-specific lesions, boundary accuracy, uncertainty, and blinded expert review.
- `Data provenance`: AAPM and any acquired projection data require license, access, retention, de-identification, and split-governance review.
- `Calibration`: a differentiable forward projector can fit its own modeling errors. Geometry, detector response, scatter, beam hardening, and motion sensitivity must be measured.
- `Hallucination and bias`: a detail branch may reconstruct plausible high-frequency content that is not supported by measurements. Projection consistency is necessary but may not be sufficient under model mismatch.
- `Compute`: 80,000 initial primitives, 25,000 iterations, and adaptive density control may be expensive. Runtime, memory, energy, and hardware requirements are unknown.
- `Monitoring`: a deployment-oriented system needs residual maps, bandwise spectra, out-of-distribution detection, parameter/primitive trajectories, and fail-closed thresholds.
- `Human impact`: reconstruction artifacts in medical images can affect downstream judgment. Outputs must remain review aids unless clinically validated and governed.
- `Maintenance`: projector versions, wavelet configuration, scanner geometry, preprocessing, and evaluation thresholds must be versioned together.
- `Repository risk`: the missing implementation creates a high reproduction burden and makes subtle geometry or rasterization differences likely.

## Strengths

- The paper identifies a concrete compatibility problem between signed wavelet coefficients and non-negative attenuation rather than adding a generic frequency loss.
- The dual-component field has an interpretable division between broad geometry and localized detail.
- The two-phase schedule directly addresses branch competition and is supported by a large source-reported ablation gap.
- Table I covers multiple sparsity levels, six volumes, classical and neural baselines, and two standard fidelity metrics.
- Separate wavelet and curriculum ablations align with the paper's two central contributions.
- The real acquisition, although qualitative, tests beyond simulated projection generation.
- The source is concise, visually clear, and complete enough to reconstruct the conceptual algorithm and main hyperparameters.

## Weaknesses

- The main clinical experiment uses simulated projections and a small six-volume evaluation set.
- No repeated seeds, confidence intervals, significance tests, or variance across training runs are reported.
- The paper does not report reconstruction time, training time, hardware, peak memory, final primitive counts, or energy.
- Ablations do not match primitive count or compute and cover selected three-volume subsets.
- Robustness to dose/noise level, scanner geometry, calibration error, scatter, motion, and metal is not evaluated.
- The beetle experiment lacks ground truth and numerical evaluation.
- The source does not include a dedicated limitations section.
- The official repository does not currently provide code despite the manuscript's availability claim.
- Clinical relevance is inferred from image fidelity rather than demonstrated with diagnostic or expert-review tasks.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a versioned implementation and environment | Reproducibility | The current repository is README-only | Enables faithful reruns and independent audit | Engineering and maintenance burden | Reproduce every table row from one command map |
| Release geometry, splits, and projection manifests | Data/evaluation | Hidden preprocessing can dominate reconstruction results | Comparable baselines and leakage control | Dataset terms may limit disclosure | Hash manifests; independent split audit |
| Run repeated-seed matched-compute ablations | Causal attribution | Primitive count and schedule may confound gains | Better attribution to wavelets and curriculum | High compute | Report mean, interval, time, memory, and primitive trajectories |
| Add calibrated acquisition perturbations | Robustness | Real systems have noise and geometry mismatch | Identifies failure boundaries | More simulation and scanner work | Noise/dose, motion, scatter, metal, and calibration sweeps |
| Add task-aware and local-detail metrics | Clinical relevance | PSNR/SSIM can miss important structures | Measures preservation where it matters | Requires annotations and experts | Boundary, vessel, lesion, and reader-study endpoints |
| Add uncertainty and fail-closed controls | Safety | High-frequency detail may be unsupported | Safer human review | Calibration complexity | Coverage, selective-risk, and residual-consistency tests |
| Quantify the real-specimen experiment | External validity | Qualitative panels are weak evidence | Stronger acquired-data validation | Ground truth may be difficult | Calibrated phantom and destructive/micro-CT reference where appropriate |

## Potential Implementations

1. **Spectral residual auditor**
   - `User`: reconstruction researcher or reviewer.
   - `Goal`: detect high-frequency loss hidden by global metrics.
   - `Core mechanism`: compare radial spectra, wavelet-band errors, edge maps, and projection residuals.
   - `Required inputs`: authorized reference/reconstruction pairs or synthetic phantoms, plus declared frequency masks.
   - `Outputs`: bandwise error table, heat maps, and review flags.
   - `Risk controls`: local-only processing, no diagnosis, explicit thresholds and provenance.
   - `Evaluation`: known blur/noise/artifact injections and correlation with local structural error.

2. **Two-branch synthetic reconstruction lab**
   - `User`: inverse-problem engineer.
   - `Goal`: test whether spectral routing and staged optimization improve sparse-view reconstruction under matched budgets.
   - `Core mechanism`: swappable base/detail representations, a known forward projector, and declared freeze/unfreeze schedules.
   - `Required inputs`: synthetic volumes, projection geometry, noise model, fixed random seeds.
   - `Outputs`: reconstructions, residuals, spectra, compute ledger, and primitive/parameter trajectories.
   - `Risk controls`: synthetic-only default, bounded compute, deterministic manifests, no clinical claims.
   - `Evaluation`: ablations over view count, noise, mismatch, branch capacity, and schedule.

3. **Human-review reconstruction card**
   - `User`: authorized imaging research team.
   - `Goal`: expose what evidence supports a candidate reconstruction before human review.
   - `Core mechanism`: summarize projection consistency, local spectral deviations, uncertainty, geometry version, and out-of-distribution indicators.
   - `Required inputs`: authorized projections, reconstruction, forward model, and validation thresholds.
   - `Outputs`: non-diagnostic review card and machine-readable audit record.
   - `Risk controls`: access control, data minimization, no raw-data logging, explicit fail-closed state.
   - `Evaluation`: retrospective error detection and reviewer usability, not diagnostic performance claims.

## Three Ways to Exercise This Research

1. **Recreate the spectral-bias diagnostic**: use a synthetic 3D phantom and a simple differentiable projector; optimize a single reconstruction representation; measure low/mid/high-frequency relative error over iterations; output curves and boundary-error maps; succeed if the method detects known injected smoothing; stop if the projector cannot reproduce the phantom within a declared tolerance.
2. **Run a matched-budget branch ablation**: compare single-branch, dual-branch joint-from-start, and dual-branch curriculum variants with equal total parameters/primitives and identical seeds; output fidelity, bandwise error, runtime, memory, and capacity trajectories; succeed if differences repeat across seeds; stop if compute or partial results exceed the approved budget.
3. **Stress the compatibility boundary**: compare direct signed-wavelet supervision with non-negative saliency initialization and raw-residual fitting on synthetic non-negative attenuation; output loss stability, negative-target conflict counts, reconstruction error, and failure cases; succeed if the experiment isolates the sign mismatch without clinical data; stop if either method violates the declared non-negative field constraint.

## Example MVP Product

- `Product name`: Spectral Reconstruction Review Lab.
- `Target user`: medical-imaging reconstruction researchers and validation engineers.
- `Problem`: aggregate metrics can hide loss or invention of local high-frequency structure under sparse acquisition.
- `Core workflow`: import a synthetic or authorized reference/projection bundle; validate geometry and provenance; run a reconstruction or import its result; compute projection residuals, wavelet/radial-spectrum diagnostics, local boundary metrics, uncertainty indicators, and a matched-compute ledger; render a review card.
- `Data requirements`: synthetic phantoms by default; otherwise de-identified, licensed, authorized research data with split and geometry manifests.
- `Architecture`: local CLI or notebook; adapter-based forward projectors; deterministic metric engine; artifact store containing only derived, approved results; optional isolated GPU worker; no external upload by default.
- `Success metrics`: deterministic reruns; detection of injected blur/artifact failures; correct provenance and geometry matching; complete compute ledger; reviewer identification of deliberately degraded cases; zero raw-data leakage.
- `Risk controls`: local-only mode, encryption/access control where applicable, no diagnosis, no automatic clinical acceptance, no raw-image telemetry, fail-closed on missing geometry or provenance, human sign-off.
- `Limitations`: does not reproduce RGS without released code; diagnostics do not prove clinical utility; forward-model mismatch can invalidate residuals; synthetic success may not transfer.
- `MVP boundary`: one synthetic dataset, one declared projector, import-only reconstruction support, three frequency bands, and a static review report.
- `Deployment model`: local CLI/notebook in an authorized research environment.
- `Evaluation plan`: unit tests for band masks and residuals, deterministic snapshot tests, synthetic artifact injections, privacy review, and blinded comparison of review cards.
- `Failure modes`: wrong geometry, misregistered references, unstable FFT normalization, misleading thresholds, missing metadata, or false reassurance from model-consistent artifacts.
- `Maintenance plan`: version projectors, masks, thresholds, datasets, and report schema; pin dependencies; retest after every change.

Minimal illustrative interface:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ReviewResult:
    projection_rmse: float
    low_band_error: float
    high_band_error: float
    requires_review: bool

def review_reconstruction(measured, reconstructed, projector, bands) -> ReviewResult:
    predicted = projector(reconstructed)
    residual = measured - predicted
    low_error = bands.relative_error(measured, predicted, name="low")
    high_error = bands.relative_error(measured, predicted, name="high")
    return ReviewResult(
        projection_rmse=float((residual.square().mean()).sqrt()),
        low_band_error=low_error,
        high_band_error=high_error,
        requires_review=high_error > bands.declared_high_threshold,
    )
```

Dependencies and safety note: this is illustrative pseudocode, not a clinical tool. A runnable implementation would pin numerical libraries, validate tensor shapes/units, avoid logging raw images, test FFT conventions, and require authorized data and human review.

## Related Research and Reading

### Exactly three related DEP entries

| Item | Type | Concrete Relevance | Public Locator |
|---|---|---|---|
| Hypercomplex MRI - DEP-E | Related Black Lake DEP | Undersampled medical reconstruction, PSNR/SSIM evaluation, and representation design under limited acquisition; contrasts parameter sharing with RGS capacity placement. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md |
| AFIDAF Vision - DEP-E | Related Black Lake DEP | Alternating spatial and Fourier operators assigns different information scales to compatible mechanisms; closely parallels RGS's spectral-spatial role split. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md |
| CAR Avatar - DEP-E | Related Black Lake DEP | Sparse-observation 3D reconstruction with explicit priors and staged coarse-to-detail refinement; parallels base/detail separation and curriculum scheduling. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-Clothed%20Avatar%20CAR/clothed_avatar_car_manuscript.md |

### Primary methodological reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Residual Gaussian Splatting | Primary paper | Reviewed research object | https://arxiv.org/abs/2604.27552 |
| 3D Gaussian Splatting for Real-Time Radiance Field Rendering | Foundational representation | Introduces explicit Gaussian splatting used as the representational basis | https://doi.org/10.1145/3592433 |
| NAF: Neural Attenuation Fields for Sparse-View CBCT Reconstruction | Direct baseline/method neighbor | Implicit neural attenuation-field reconstruction cited and evaluated by RGS | https://arxiv.org/abs/2209.14540 |
| Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis | Direct representation neighbor | Adapts Gaussian splatting to X-ray/radiative projection | https://arxiv.org/abs/2403.04116 |
| 3DGR-CT: Sparse-view CT reconstruction with a 3D Gaussian representation | Direct baseline | Strongest aggregate baseline in several RGS table settings | https://doi.org/10.1016/j.media.2025.103585 |
| On the Spectral Bias of Neural Networks | Mechanism context | General frequency-learning-bias reference used by the paper | https://proceedings.mlr.press/v97/rahaman19a.html |
| A Theory for Multiresolution Signal Decomposition | Wavelet foundation | Foundational multiresolution analysis behind the spectral prior | https://doi.org/10.1109/34.192463 |
| Practical Cone-Beam Algorithm | CBCT foundation | FDK reconstruction used for the coarse low-frequency prior | https://doi.org/10.1364/JOSAA.1.000612 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2604.27552 | Identity, authors, date, category, DOI, version, public source links | 2026-07-17 | Metadata only; not counted as the full paper |
| R2 | https://arxiv.org/html/2604.27552 | Full text, equations, algorithm, experiments, tables, figures, conclusion | 2026-07-17 | Integrity-verified official full-paper HTML; source file withheld locally |
| R3 | https://arxiv.org/pdf/2604.27552 | Complete paper and layout-sensitive visual review | 2026-07-17 | Verified PDF retained locally; not redistributed |
| R4 | https://arxiv.org/e-print/2604.27552 | Primary manuscript source provenance | 2026-07-17 | Valid gzip/tar package retained locally; contents not redistributed |
| R5 | https://doi.org/10.48550/arXiv.2604.27552 | Persistent source identifier | 2026-07-17 | arXiv DOI |
| R6 | https://github.com/yqx7150/RGS | Declared implementation and present reproducibility state | 2026-07-17 | Recursive tree contained only `README.md` |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md | Related medical reconstruction synthesis | 2026-07-17 | Context, not validation |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md | Related spatial/spectral synthesis | 2026-07-17 | Context, not validation |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-Clothed%20Avatar%20CAR/clothed_avatar_car_manuscript.md | Related sparse-observation 3D reconstruction synthesis | 2026-07-17 | Context, not validation |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout, DEP classes, attribution, source locality | 2026-07-17 | Process authority |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index rules | 2026-07-17 | Process authority |
| R12 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository layout and dedup context | 2026-07-17 | Process authority |

Every evidence-ledger source is represented above. Local filenames and paths are intentionally omitted. Source documents were inspected locally and withheld from the public repository.

## Appendix

### Replication checklist

- [ ] Obtain a versioned implementation, dependency lock, hardware record, and license.
- [ ] Publish the exact AAPM volume identifiers, splits, preprocessing, voxel spacing, and projection geometry.
- [ ] Reproduce FDK, SART, NAF, R2-Gaussian, 3DGR, and RGS with identical projection operators and data.
- [ ] Record random seeds, initial and final primitive counts, density-control events, runtime, peak memory, and energy.
- [ ] Run at least three seeds and report intervals for PSNR, SSIM, local-detail metrics, and spectral error.
- [ ] Match compute and primitive budgets across single/dual-branch and schedule ablations.
- [ ] Stress noise/dose, motion, scatter, beam hardening, metal, and geometry mismatch.
- [ ] Evaluate local anatomy preservation and task-relevant endpoints with qualified reviewers.
- [ ] Add acquired phantom and multi-anatomy data with quantitative ground truth where feasible.
- [ ] Release commands that regenerate Tables I-III and Figures 3, 5-9.

### Random selection and eligibility

- PDF candidates enumerated: 75,777.
- Unique parent-directory paper units: 75,776.
- Sampling: uniform PowerShell `Get-Random` over the sorted unit list.
- Accepted zero-based index: 48,493.
- Duplicate exclusions: 0.
- Other exclusions: 0.
- Reselections: 0.
- Dedup keys: arXiv ID, arXiv DOI, normalized title, slug family, repository artifacts, automation memory, relevant related-repository DEP entries, and preceding-24-hour markers.

### Source-integrity record

- Initial state: `partial`; valid PDF present, full-paper HTML absent.
- PDF gate: 17,698,694 bytes; `%PDF-` header; trailing `%%EOF`; passed.
- Repair: bounded direct HTTPS; valid existing PDF preserved; official full-paper HTML, metadata HTML, and source archive added locally.
- HTML gate: 324,487 bytes; 61,612 body characters; document marker present; 55 heading/section markers; seven paper-structure term classes; passed.
- Source archive: 26,997,742-byte gzip/tar; format verified.
- Partial files after repair: 0.
- Final state: `complete`.

### Public-output and no-source-upload gate

- Public files are generated Markdown under `.logs`, `.reports`, and `.lake-data` only.
- No `.source/` directory exists in the DEP.
- No PDF, HTML, e-print, extracted source text, cache, image render, local archive path, home directory, username, drive path, machine name, exact local timestamp, timezone label, credential, or protected record is included.
- Source URLs are public arXiv, DOI, GitHub, and Black Lake locators.
- All source files and derived inspection material were withheld locally and were not copied, staged, committed, attached, or uploaded.
