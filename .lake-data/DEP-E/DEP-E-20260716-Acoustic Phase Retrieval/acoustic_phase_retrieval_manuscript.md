---
title: "Acoustic Phase Retrieval - DEP-E"
generated_at: "2026-07-16"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of reference-source phase recovery and Fourier reconstruction for a two-dimensional acoustic inverse-source problem."
source_status: "Verified local source bundle inspected; public URLs published; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "Primary paper v1 and publication metadata available through 2026-07-16"
primary_url: "https://arxiv.org/abs/1803.11323"
stable_identifier: "arXiv:1803.11323v1; DOI:10.1088/1361-6420/aaccda"
confidence_summary: "High for source transcription and method structure; medium for generality; low for field readiness without hardware validation."
safety_scope: "Non-sensitive research, synthetic examples, and measurement-quality controls"
distribution_notes: "Generated Markdown only; no PDF, HTML, source package, extracted text, or cache is redistributed."
---

# Acoustic Phase Retrieval - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *Retrieval of acoustic sources from multi-frequency phaseless data* | Primary paper | PDF and source extraction | arXiv:1803.11323v1 | https://arxiv.org/pdf/1803.11323 | Inspected locally as evidence; not redistributed. | 2026-07-16 | Complete 27-page paper inspected |
| S2 | arXiv metadata | Primary metadata | HTML | Submitted 2018-03-30; v1 | https://arxiv.org/abs/1803.11323 | Public metadata and source locators. | 2026-07-16 | Inspected |
| S3 | Full-paper HTML | Primary full text | ar5iv HTML | arXiv:1803.11323v1 fallback rendering | https://ar5iv.labs.arxiv.org/html/1803.11323 | Approved full-paper fallback; not an abstract page. | 2026-07-16 | Integrity-verified and inspected |
| S4 | arXiv source package | Primary manuscript source | TeX/source archive | arXiv:1803.11323v1 | https://arxiv.org/e-print/1803.11323 | Retained and extracted locally only. | 2026-07-16 | Inspected through local cache |
| S5 | Journal record | Bibliographic metadata | DOI and institutional record | DOI:10.1088/1361-6420/aaccda; *Inverse Problems* 34(9), 094001 | https://doi.org/10.1088/1361-6420/aaccda; https://scholars.hkbu.edu.hk/en/publications/retrieval-of-acoustic-sources-from-multi-frequency-phaseless-data/ | Bibliographic use; publisher terms apply. | 2026-07-16 | Metadata inspected |
| S6 | Hypercomplex MRI DEP-E | Related DEP entry 1 of 3 | Markdown | DEP-E-20260713-Hypercomplex MRI | `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md` | Generated repository synthesis; primary basis arXiv:2503.05063. | 2026-07-16 | Inspected |
| S7 | Irregular Clipped SR DEP-E | Related DEP entry 2 of 3 | Markdown | DEP-E-20260711-Irregular Clipped SR | `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md` | Generated repository synthesis; primary basis arXiv:2106.01573. | 2026-07-16 | Inspected |
| S8 | iKalibr Calibration DEP-E | Related DEP entry 3 of 3 | Markdown | DEP-E-20260714-iKalibr Calibration | `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` | Generated repository synthesis; primary basis arXiv:2407.11420. | 2026-07-16 | Inspected |
| S9 | Black Lake repository rules | Deposition authority | Markdown | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Process authority, not research evidence. | 2026-07-16 | Fetched and inspected |
| S10 | Black-Lake-Data rules | Dedup context authority | Markdown | Live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Process authority, not research evidence. | 2026-07-16 | Fetched and inspected |

The paper is by Deyue Zhang, Yukun Guo, Jingzhi Li, and Hongyu Liu. arXiv classifies it under Analysis of PDEs (`math.AP`). The arXiv record lists 27 pages and four figures. The official institutional publication record identifies the journal version as *Inverse Problems*, volume 34, issue 9, article 094001, published 2018-06-29.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S4 | Complete primary paper and source | Abstract, Sections 1-6, algorithms, theorems, tables, figure captions, conclusion, and source equations | Problem, mechanism, stability, numerical setup, results, and stated future work | High for source reporting | Proofs were read but not independently rederived; experiments were not rerun |
| E2 | S2 | Primary metadata | Title, authors, identifier, date, category, DOI link, version history | Stable source identity | High | Metadata does not validate detailed claims |
| E3 | S5 | Institutional/DOI metadata | Journal, volume, issue, article number, date, DOI | Publication context | High for bibliography | Publisher full text was not separately compared with arXiv v1 |
| E4 | S1, Section 3 | Primary theorem evidence | Determinant lower bounds and relative perturbation bound | Analytic conditioning and phase-recovery stability | High for transcription | Constants may be conservative; end-to-end source error is not bounded in the same theorem |
| E5 | S1, Section 5 | Primary numerical evidence | FEM/PML setup, noise model, phase tables, final reconstruction errors | Feasibility and noise behavior in the stated synthetic test | High for transcription; medium for generality | One synthetic source family, no repeated seeds, no hardware, no uncertainty intervals |
| E6 | S6 | Related DEP | Physics-grounded accelerated MRI reconstruction and compact coupled-channel representation | Reconstruction/representation bridge | Medium | Different modality and learned method; no validation of this paper |
| E7 | S7 | Related DEP | Nonlinear clipping distribution optimized with decoder state evolution | Intervention/decoder co-design bridge | Medium | Communications setting differs from acoustic inverse sourcing |
| E8 | S8 | Related DEP | Excitation, observability, calibration, residual families, and staged refinement | Calibration/observability bridge | Medium | Calibration task does not validate reference-source phase recovery |
| E9 | Random selection, dedup, and integrity checks | Private process evidence | Candidate counts, random index, repository scans, PDF/HTML gates, cache extraction | Eligibility and source completeness | High | Private paths and exact local execution context are intentionally withheld |

## Executive Summary

The paper addresses a two-dimensional Helmholtz inverse-source problem in which only the modulus of the radiated field is measured on a circular acquisition curve at multiple frequencies. Losing phase creates immediate non-uniqueness: at minimum, `S` and `-S` yield the same phaseless data. The authors resolve this ambiguity by adding two known point sources in separate measurements for each acquisition sector and frequency. Squared-magnitude differences then produce a two-by-two linear system whose solution recovers the real and imaginary field components.

The contribution is not only the algebraic phase formula. The authors prescribe sector count, acquisition radius, auxiliary frequency, and point-source locations so the coefficient determinant has a positive lower bound. They prove a relative phase-recovery perturbation bound under multiplicative measurement noise, then use a previously developed multifrequency Fourier method to reconstruct the source non-iteratively.

Synthetic finite-element experiments support feasibility within the model. At 1%, 2%, and 5% phaseless noise, the reported final source-reconstruction relative L2 errors are 4.60%, 5.82%, and 8.39%. Phase recovery itself can deteriorate much more sharply at 5% noise, but the Fourier coefficient integrals filter some error. The evidence does not establish hardware robustness, heterogeneous-medium transfer, calibration tolerance, or production efficiency.

Reviewer assessment: the primary source strongly supports the mechanism, determinant analysis, and reported synthetic results. The most useful transferable idea is to pair a deliberate measurement intervention with an explicit observability/conditioning certificate before inversion. Field adoption requires a measurement-cost ledger, reference-source calibration, mismatch tests, repeated-seed statistics, timing, and end-to-end uncertainty propagation.

## Detailed Summary

### Problem and model

The source `S` is assumed square-integrable, frequency-independent, and compactly supported in a centered rectangle inside a circular acquisition boundary. It drives the two-dimensional Helmholtz equation, and the radiated field satisfies the Sommerfeld radiation condition. Measurements are the field modulus on the acquisition circle for a finite admissible set of wavenumbers.

Intensity-only sensing is practical in regimes where phase is difficult to measure, but it removes sign and complex-angle information. The paper therefore decomposes the task into phase recovery followed by a conventional phased inverse-source reconstruction.

### Reference-source intervention

The acquisition disk is partitioned into `m` angular sectors. For each sector `j`, the method places two reference point sources on the sector bisector at prescribed radial fractions. Their amplitudes are scaled relative to the measured field and the Green function. Separate phaseless measurements are collected for the original field and for each reference-augmented field.

Expanding the two augmented squared magnitudes and subtracting the original squared magnitude removes the quadratic field norm. The remaining equations are linear in `Re(u)` and `Im(u)`, with coefficients formed from order-zero Bessel functions. Solving the two-by-two system recovers the complex field on every sector.

The algorithm therefore requires four operational stages: choose the geometry, measure the original phaseless field, introduce and measure two reference sources per sector/frequency, and solve the phase formula. The paper calls the extra data small; an implementation should instead enumerate physical placements, amplitude settings, repeated captures, and synchronization requirements.

### Conditioning and stability

The prescribed parameters include `m >= 10`, acquisition radius `R = tau a` with `tau >= 6` for ordinary frequencies, a small auxiliary frequency, and special radial locations for the two references. The determinant theorem gives a lower bound of

`|det(A_jk)| >= (1 - 7/(20 tau))/(kR)`

for ordinary admissible frequencies and `4/9` for the small frequency. The proof uses Hankel/Bessel asymptotics for ordinary frequencies and small-argument expansions for the auxiliary frequency.

Under relative modulus perturbations bounded by `epsilon`, the recovered field satisfies

`||u_epsilon - u||_infinity <= epsilon C_epsilon ||u||_infinity`,

where `C_epsilon = [2.5(2 + epsilon)^2(3 + epsilon) + 15] / (1 - epsilon)`. This establishes stability within the assumed measurement and geometry model. It does not directly cover reference-location error, reference-amplitude error, clock drift, medium mismatch, noncircular acquisition, or a frequency-dependent source.

### Fourier reconstruction

After phase recovery, the method approximates the source by a truncated two-dimensional Fourier expansion. Boundary field data are propagated from the acquisition curve to an outer curve through a Hankel-series representation. Boundary integrals yield the nonzero Fourier coefficients, while a small auxiliary frequency supports the zero coefficient. This stage is non-iterative and inherits theory from the authors' earlier Fourier-method work.

### Numerical setup

The experiment uses a synthetic mountain-shaped source on `[-0.3, 0.3]^2`. A finite-element forward solver operates on a truncated circular domain with a perfectly matched layer. The mesh is refined until successive measured-data relative error falls below 0.1%. Multiplicative uniform noise is applied as `(1 + epsilon r)|u|`, with `r` uniform on `[-1, 1]`.

The displayed phase-recovery test uses `m = 10`, `R = 1.8`, auxiliary frequency `pi/9`, and three ordinary frequencies `10pi/3`, `50pi/3`, and `100pi/3`. At 1% noise, relative L2 phase errors are 2.95%, 1.22%, 2.16%, and 2.08% across those four frequencies. At 5% noise, they rise to 15.5%, 5.12%, 10.6%, and 10.23%. Relative infinity errors at 5% reach 23.9%, 6.47%, 19.2%, and 18.97%.

For source reconstruction, the paper uses 400 pseudo-uniform boundary samples, an `800 x 800` evaluation grid, and truncation `N = 2 ceil(epsilon^(-1/3))`. Final relative L2 source errors are 4.60%, 5.82%, and 8.39% for 1%, 2%, and 5% noise. The authors attribute the smaller end-to-end degradation to the noise-filtering effect of integration when computing Fourier coefficients.

### Conclusion and stated extension

The authors conclude that reference point sources permit a stable, easy-to-implement phase retrieval followed by fast Fourier reconstruction. They identify extension to the scalar three-dimensional Helmholtz equation and vector Maxwell systems as future work.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Two reference-source measurements per sector/frequency convert the phaseless field problem into a two-by-two real linear system. | Author method claim | E1 | Directly supported by the squared-magnitude derivation. | High |
| C2 | The prescribed geometry makes the phase solve uniquely solvable with explicit determinant margins. | Author theorem claim | E4 | Supported within the exact two-dimensional model and parameter assumptions. | High for source reporting |
| C3 | Relative phase-recovery error scales linearly with small relative measurement noise up to the stated factor. | Author theorem claim | E4 | Analytically supported under the paper's noise model; constants are not empirical calibration bounds. | High for source reporting |
| C4 | The full method remains effective at moderate synthetic noise. | Author empirical claim | E5 | Supported by one synthetic setup; field and mismatch generality remain unknown. | Medium |
| C5 | Fourier integration filters enough upstream phase error to keep final source error moderate. | Author interpretation | E5 | Consistent with the reported phase and reconstruction errors, but not isolated by an ablation. | Medium |
| C6 | The method is fast and easy to implement. | Author practical claim | E1 | The inverse stage is non-iterative, but no runtime, hardware, measurement-labor, or code evidence is reported. | Low-medium |
| C7 | Measurement interventions should be co-designed with calibration and downstream representation. | Reviewer inference | E6-E8 | A useful cross-DEP design hypothesis, not established by the paper. | Medium-low |

## Methodology

- `Research objective`: Preserve a source-grounded, schema-complete DEP review of a randomly selected eligible paper and synthesize it with exactly three relevant Black Lake entries.
- `Sources inspected`: Verified complete PDF, full-paper ar5iv HTML, arXiv metadata HTML, TeX/source extraction, arXiv record, official institutional publication metadata, live repository rules, and three related DEP manuscripts with their cited primary-source bases.
- `Discovery strategy`: Enumerated PDFs using `rg --files -g "*.pdf"`, collapsed paths to unique parent-directory paper units, selected a uniform `Get-Random` index, derived the canonical arXiv ID, and searched all required dedup surfaces before acceptance.
- `Inclusion criteria`: Full-paper evidence for problem, mechanism, proofs, experiments, limitations, and conclusion; canonical metadata; live repository rules; and DEP entries with concrete overlap in inverse reconstruction, intervention/decoder co-design, or calibration/observability.
- `Exclusion criteria`: Abstract-only synthesis, unverified code repositories, generic topical similarity, locally identifying paths, and source-file redistribution.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, replication, product-research, and DEP-ready provenance analysis.
- `Evidence handling`: Major claims map to ledger IDs; source claims, reviewer interpretations, and cross-domain inferences are labeled separately.
- `Uncertainty handling`: Unreproduced mathematics and experiments, unavailable official arXiv HTML, missing code/timing/statistics, related-source differences, and hardware/mismatch gaps remain explicit.
- `Extraction process`: Local-first PDF, HTML, and TeX/source extractors produced separate caches. Key equations, algorithms, table values, and section structure were cross-checked across formats.
- `Version control`: Primary research object pinned to arXiv:1803.11323v1 and the related journal DOI. Repository rules were fetched from current default branches on the public access date.
- `Claim selection`: Priority went to identifiability, the reference-source algebra, determinant/stability theorems, exact numerical settings, noise results, assumptions, and implementation burden.
- `Cross-checking`: Identity and dates were checked against arXiv and the institutional record; numerical values were checked against source tables and TeX; source completeness was independently gated before review.
- `Safety handling`: Implementation ideas use synthetic or authorized acoustic measurements and emphasize calibration, conditioning, privacy-minimal evidence, and stop conditions.
- `Reviewer stance`: Paper report, critique, replication brief, implementation translation, and archival deposition.

## Scope, Constraints, and Assumptions

- `Scope`: The selected paper's two-dimensional reference-source phase retrieval, stability argument, Fourier inversion, synthetic evidence, and three cross-DEP implementation bridges.
- `Temporal boundary`: Primary paper v1, journal metadata, and repository evidence available through 2026-07-16.
- `Evidence limits`: No independent proof check, numerical reproduction, code audit, hardware experiment, raw dataset, reference-source calibration dataset, or publisher-version comparison.
- `Assumptions`: The public PDF and inspected local PDF represent the same arXiv version; the institutional record correctly describes the journal publication; related DEP artifacts accurately preserve their cited sources.
- `Constraints`: Source files remain local; public artifacts use date-only run markers; implementation examples are synthetic and non-operational; no `.source/` directory is created.
- `Out of scope`: Rebuilding the FEM solver, reproducing figures, certifying acoustic hardware, extending the proofs to 3D/Maxwell systems, or making medical/industrial deployment claims.
- `Intended use`: DEP deposition, source review, replication planning, measurement-system design, and research-to-product ideation.
- `Audience`: Inverse-problem researchers, signal-processing engineers, sensing-system designers, and reviewers of evidence-grounded reconstruction pipelines.
- `Reproducibility boundary`: The paper supplies equations and numerical settings, but no official implementation or complete environment was identified in inspected primary evidence.
- `Data sensitivity`: Public research sources and synthetic numerical data; real acoustic measurements may become sensitive depending on deployment context.

## Observations

- `Observed pattern`: The method spends measurement effort to simplify computation. Extra controlled captures replace a harder nonlinear phase-retrieval optimization with a small direct solve.
- `Technical implication`: Determinant or condition margin should be treated as a runtime gate, not only a proof artifact. A reconstruction should be withheld when the reference geometry is nearly singular.
- `Observed pattern`: Final Fourier reconstruction error grows more slowly than worst displayed phase error, consistent with integration suppressing zero-mean noise.
- `Contradiction or tension`: The paper describes the reference data as small, yet the sector-by-frequency capture count and physical reference control are not quantified.
- `Open question`: Does the analytic geometry remain near-optimal when placement, amplitude, synchronization, and background medium are uncertain?
- `Reviewer hypothesis`: Jointly optimizing probe placement and Fourier truncation under a calibration uncertainty model may reduce total measurement cost while preserving an auditable condition margin.

## Considerations

The central deployment risk is model mismatch. An active reference source must have known position, amplitude, radiation pattern, and timing relative to the acquisition system. Errors in those quantities enter the recovered real/imaginary field systematically rather than as the paper's independent multiplicative modulus noise. A production design needs calibration provenance, drift detection, clock checks, reference-source self-tests, and a failed-observability state.

Geometry is also restrictive. The analytic margins depend on a centered support box, circular acquisition, adequate separation radius, sector count, selected frequencies, and point-source placement. Obstacles, reflections, heterogeneous sound speed, limited aperture, moving sources, or frequency-dependent excitation may invalidate the forward model.

The evidence is synthetic. Repeated random seeds, uncertainty intervals, alternative source shapes, nonuniform/heteroscedastic noise, mesh-discretization separation, independent forward solvers, and hardware experiments are required before generalization. Runtime should include physical measurement time, source repositioning or multiplexing, calibration, phase solve, and Fourier reconstruction—not just the non-iterative numerical kernel.

For privacy-sensitive deployments, retain derived residuals and calibration summaries rather than raw audio whenever possible. Access control and retention policy are application-specific and were outside the paper.

## Strengths

1. The paper targets a concrete identifiability failure and introduces a transparent intervention rather than hiding ambiguity inside an opaque optimizer.
2. The phase formula is small, deterministic, and auditable; real and imaginary parts come from an explicit two-by-two system.
3. Reference locations are linked to determinant lower bounds, giving a mathematical reason for the measurement design.
4. The perturbation theorem makes noise dependence visible instead of relying only on numerical examples.
5. Numerical tables separate phase-recovery errors by frequency and final source-reconstruction error by noise level.
6. The non-iterative Fourier stage offers a plausible low-compute path once valid phased data are available.

## Weaknesses

1. The experiment is limited to a synthetic two-dimensional scalar setting with one displayed source family and no hardware evidence.
2. The noise model excludes reference-source position/amplitude error, synchronization drift, medium mismatch, multipath, limited aperture, and frequency-dependent sources.
3. Measurement overhead is not reported as counts, time, energy, or calibration labor.
4. No repeated seeds, confidence intervals, sensitivity sweep, geometry ablation, or independent forward solver is reported.
5. The “fast and easy” claim lacks code, runtime, memory, or end-to-end acquisition evidence.
6. The stability theorem covers phase recovery under stated assumptions; full source-reconstruction uncertainty relies partly on earlier Fourier-method theory and empirical behavior.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add calibrated hardware tests | External validity | Synthetic FEM data omit real probe and medium errors | Establish field feasibility | Experimental cost and safety | Repeat captures across rooms, arrays, and reference hardware |
| Model reference uncertainty | Theory and robustness | Probe errors can create structured bias | Honest conditioning/uncertainty bounds | More complex analysis | Derive and simulate position/amplitude/clock perturbation bounds |
| Optimize probes under constraints | Measurement design | Analytic geometry may not minimize real capture cost | Fewer or more stable measurements | Optimization may lose closed-form guarantees | Compare analytic and optimized plans at matched budgets |
| Separate error stages | Evaluation | Fourier integration can hide upstream failure | Diagnosable evidence | More instrumentation | Report calibration, condition, phase, coefficient, and source errors separately |
| Publish code and environment | Reproducibility | Equations alone do not pin discretization and implementation | Faster independent validation | Maintenance burden | Containerized tests reproducing all tables |
| Expand mismatch benchmarks | Generalization | Current source/noise/geometry coverage is narrow | Clear boundary conditions | Larger experiment matrix | Pre-register source shapes, media, apertures, noise, and seeds |

## Potential Implementations

1. **Condition-certified source imager**
   - `User`: Acoustic diagnostics engineer.
   - `Goal`: Reconstruct a localized source from modulus-only multifrequency captures.
   - `Core mechanism`: Calibrated reference probes, two-by-two phase recovery, determinant gate, and Fourier inversion.
   - `Required inputs`: Sensor geometry, reference calibration, frequency plan, phaseless captures, and medium model.
   - `Outputs`: Source map, condition margins, residuals, and failure flags.
   - `Risk controls`: Authorized measurement, probe safety limits, drift checks, raw-audio minimization, and no-result state.
   - `Evaluation`: Synthetic truth, calibrated phantom sources, held-out rooms, and error-stage ledger.

2. **Probe-plan optimizer**
   - `User`: Measurement-system designer.
   - `Goal`: Reduce capture cost while maintaining robust observability.
   - `Core mechanism`: Search feasible reference positions/amplitudes/frequencies, score worst-case condition under calibration uncertainty, and freeze a signed plan.
   - `Required inputs`: Placement constraints, power limits, uncertainty bounds, candidate frequencies, and acquisition geometry.
   - `Outputs`: Probe plan, predicted margins, capture count, and stop conditions.
   - `Risk controls`: Bounded search, analytic-plan baseline, safety envelope, and human approval before hardware use.
   - `Evaluation`: Monte Carlo mismatch tests and hardware repeatability.

3. **Inverse-problem evidence harness**
   - `User`: Research reviewer or platform engineer.
   - `Goal`: Compare intervention-plus-reconstruction pipelines across acoustics, communications, calibration, and imaging.
   - `Core mechanism`: Shared schema for intervention, forward operator, observability, calibration, inversion, representation, uncertainty, and residuals.
   - `Required inputs`: Synthetic datasets, versioned algorithms, source-specific metrics, and compute/measurement budgets.
   - `Outputs`: Comparable evidence ledgers and failure-boundary reports.
   - `Risk controls`: Domain-specific plugins, no cross-domain metric collapse, reproducible seeds, and public-safe summaries.
   - `Evaluation`: Regression fixtures for each domain and independent result review.

## Three Ways to Exercise This Research

1. **Reproduce the paper table:** Objective—verify phase-recovery error trends; inputs—the stated synthetic source, four frequencies, geometry, and seeded multiplicative noise; method—implement the forward FEM/PML model, reference measurements, and two-by-two solve; output—L2/L-infinity tables with confidence intervals; success criterion—source-reported values fall within a predeclared tolerance; stop condition—mesh convergence or determinant gates fail.
2. **Run a mismatch ladder:** Objective—locate the first violated assumption; inputs—synthetic perturbations to probe location, amplitude, clock, sound speed, aperture, and source frequency dependence; method—vary one factor at a time and then selected interactions; output—condition, phase, and source-error surfaces; success criterion—stable safe/unsafe boundary; stop condition—calibration or geometry becomes unobservable.
3. **Compare intervention designs:** Objective—test whether measurement co-design reduces total burden; inputs—no-probe, one-probe, analytic two-probe, and optimized two-probe plans at matched budgets; method—evaluate identifiability, condition, capture count, runtime, and reconstruction error; output—Pareto frontier; success criterion—an intervention improves error without hidden measurement cost; stop condition—plans exceed power, placement, or uncertainty limits.

## Example MVP Product

- `Product name`: PhaseGate Acoustic Mapper.
- `Target user`: Laboratory acoustic-imaging engineer working in an authorized controlled environment.
- `Problem`: Modulus-only multifrequency captures do not identify a complex field or source reliably.
- `Core workflow`: Import a geometry/calibration bundle; validate excitation and clocks; execute a fixed two-reference capture plan; compute determinant/condition margins; recover the complex field; reconstruct a source map; review residual and uncertainty overlays; export a public-safe evidence report.
- `Data requirements`: Versioned sensor geometry, reference position/amplitude calibration, frequency plan, phaseless magnitude captures, medium assumptions, synthetic/phantom truth for validation, and no raw audio beyond the approved retention window.
- `Architecture`: Local-only acquisition adapter; calibration registry; intervention planner; phase solver; Fourier reconstructor; conditioning/residual monitor; evidence-ledger exporter; review UI.
- `Success metrics`: 100% rejection of deliberately singular fixtures; bounded complex-field error on synthetic truth; repeatable phantom-source localization; calibrated coverage of uncertainty intervals; measured capture and compute budgets.
- `Risk controls`: Authorized environments only, probe power limits, clock and drift gates, no-result fallback, immutable calibration/probe-plan versions, data minimization, and human review before use.
- `Limitations`: Two-dimensional scalar model, controlled geometry, no real-time guarantee, no safety-critical decision authority, and no field validation from this review.
- `MVP boundary`: One circular array, fixed medium, four frequencies, one source family plus held-out phantoms, and offline reconstruction.
- `Deployment model`: Local workstation or laboratory CLI with a small review dashboard.
- `Evaluation plan`: Deterministic smoke tests, synthetic regression tables, mismatch ladder, hardware repeatability, privacy review, and acceptance gates.
- `Failure modes`: Near-singular reference geometry, stale calibration, clock drift, multipath/model mismatch, reference saturation, and misleading noise-filtered output.
- `Maintenance plan`: Version calibration bundles, regression fixtures, numerical dependencies, probe hardware, and public evidence schemas.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Hypercomplex MRI DEP-E | Related Black Lake research artifact | Connects physics-grounded inverse reconstruction to coupled-channel representation, compact models, and the need for direct deployment metrics. | `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md`; https://arxiv.org/abs/2503.05063 |
| Irregular Clipped SR DEP-E | Related Black Lake research artifact | Connects deliberate nonlinear measurement transformation with decoder-state optimization and matched-budget evidence. | `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md`; https://arxiv.org/abs/2106.01573 |
| iKalibr Calibration DEP-E | Related Black Lake research artifact | Connects excitation, observability, calibration provenance, robust residuals, and staged refinement to physical inverse estimation. | `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`; https://arxiv.org/abs/2407.11420 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1803.11323 | Canonical title, authors, abstract, version, dates, category, source locators | 2026-07-16 | Primary metadata |
| R2 | https://arxiv.org/pdf/1803.11323 | Complete primary paper | 2026-07-16 | Public PDF; local source withheld |
| R3 | https://ar5iv.labs.arxiv.org/html/1803.11323 | Complete full-paper HTML | 2026-07-16 | Approved fallback because official arXiv HTML was unavailable |
| R4 | https://arxiv.org/e-print/1803.11323 | TeX/source cross-checks | 2026-07-16 | Local package and extracted text withheld |
| R5 | https://doi.org/10.1088/1361-6420/aaccda | Journal DOI | 2026-07-16 | Persistent identifier |
| R6 | https://scholars.hkbu.edu.hk/en/publications/retrieval-of-acoustic-sources-from-multi-frequency-phaseless-data/ | Journal metadata and publication date | 2026-07-16 | Official institutional record |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md | Related reconstruction/representation DEP | 2026-07-16 | Primary basis: https://arxiv.org/abs/2503.05063 |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Irregular%20Clipped%20SR/irregular_clipped_sr_manuscript.md | Related intervention/decoder DEP | 2026-07-16 | Primary basis: https://arxiv.org/abs/2106.01573; DOI:10.1109/ITW48936.2021.9611458 |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Related calibration/observability DEP | 2026-07-16 | Primary basis: https://arxiv.org/abs/2407.11420; DOI:10.1109/TRO.2025.3532506 |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Black Lake deposition rules | 2026-07-16 | Process authority |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publications index | 2026-07-16 | Process authority |
| R12 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository dedup context | 2026-07-16 | Process authority |

## Appendix

### Random selection and eligibility

- `rg --files -g "*.pdf"` enumerated 75,777 PDF candidates in the local archive.
- PDF paths were collapsed to 75,776 unique parent-directory paper units.
- Uniform PowerShell `Get-Random` selected zero-based unit index 16,432.
- The selected unit resolved to arXiv:1803.11323. Repository and memory scans found no prior artifact for its arXiv ID, DOI, exact title, or selected slug.
- Dedup locations were Black-Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data. Exclusions: 0; reselections: 0. Public-safe 24-hour cutoff date marker: 2026-07-15.

### Source-integrity and extraction gate

- Initial state: partial because the unit contained a valid PDF but no full-paper HTML.
- Repair: preserved the existing PDF and fetched metadata HTML, approved ar5iv full-paper HTML, and the arXiv source package with bounded retries.
- PDF: 622,169 bytes, `%PDF-` header, trailing `%%EOF`; pass.
- Full-paper HTML: 2,289,055 bytes, 132,609 body characters after stripping scripts/styles/tags, valid document marker, 40 section/heading markers, five paper-structure terms; pass.
- Extraction: PDF (`pypdf` fallback), HTML, and source-package text completed locally; no partial files remained.
- Review proceeded only after the complete-source gate passed.

### No-source-upload gate

Only generated public-safe Markdown and required derived indexes are eligible for staging. No PDF, HTML, metadata page, TeX/source archive, extracted text, cache, local archive locator, `.source/` directory, or exact local execution timestamp may enter the repository or Slack message. The staged allowlist and leak scan must pass before submission.
