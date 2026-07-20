---
title: "VaTD Canonical - DEP-E"
generated_at: "2026-07-20 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of variational temperature-differentiable generative modelling for canonical ensembles."
source_status: "verified local sources; public URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-20"
temporal_cutoff: "arXiv:2404.18404v2, official code default branch, and public records inspected through 2026-07-20"
primary_url: "https://arxiv.org/abs/2404.18404v2"
stable_identifier: "arXiv:2404.18404v2; 10.48550/arXiv.2404.18404; 10.1103/8wx7-kyx8"
confidence_summary: "High for source identity, method transcription, tables, and code inspection; medium for efficiency generality; low for untested atomistic transfer."
safety_scope: "non-sensitive scientific simulation and evaluation"
distribution_notes: "Generated Markdown only; all source documents and inspection material were withheld locally."
---

# VaTD Canonical - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv metadata record | Primary metadata | HTML | arXiv:2404.18404v2 | https://arxiv.org/abs/2404.18404v2 | Public metadata; abstract alone was not used for detailed claims. | 2026-07-20 | Inspected |
| S2 | arXiv paper | Primary artifact | PDF | arXiv:2404.18404v2 | https://arxiv.org/pdf/2404.18404 | Complete 36-page PDF inspected locally and not redistributed. | 2026-07-20 | Integrity-verified and visually inspected |
| S3 | Official arXiv full-paper rendering | Primary artifact | HTML | arXiv:2404.18404v2 | https://arxiv.org/html/2404.18404 | Full-paper HTML, not an abstract page; retained locally only. | 2026-07-20 | Integrity-verified and inspected |
| S4 | arXiv e-print | Primary manuscript source | TeX/source archive | arXiv:2404.18404v2 | https://arxiv.org/e-print/2404.18404 | Source package inspected locally; no redistribution permission inferred. | 2026-07-20 | Collected and inspected |
| S5 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2404.18404 | https://doi.org/10.48550/arXiv.2404.18404 | Public persistent locator. | 2026-07-20 | Recorded |
| S6 | Physical Review Letters record | Publisher identity | Journal issue and DOI | PRL 135, 027301 (2025); 10.1103/8wx7-kyx8 | https://journals.aps.org/prl/issues/135/2; https://doi.org/10.1103/8wx7-kyx8 | Publisher issue record reports publication on 2025-07-08. | 2026-07-20 | Issue metadata inspected; article page was access-restricted |
| S7 | VaTD implementation | Paper-declared code | GitHub repository | default branch commit d8fd69c243951769e1e083f8451339522873af8f | https://github.com/li012589/vatd | Apache-2.0 repository; code availability does not by itself establish exact reproducibility. | 2026-07-20 | README, dependencies, tree, and training entry points inspected |
| S8 | Exactly three related Black Lake artifacts | Related processed research | Markdown | Physical Data AI; Surface SQD Study; Transport Convexity | See Related Research and Reading | Conceptual synthesis only; these artifacts do not validate VaTD. | 2026-07-20 | Inspected |
| S9 | Black Lake repository authorities | Deposition and source-locality rules | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md; https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Process authority, not scientific evidence. | 2026-07-20 | Fetched and inspected |

Paper metadata:

- **Full title:** *Deep generative modelling of canonical ensemble with differentiable thermal properties*.
- **Authors:** Shuo-Hui Li, Yao-Wen Zhang, and Ding Pan.
- **History:** arXiv v1 submitted 2024-04-29; v2 revised 2025-12-09.
- **Subjects:** Statistical Mechanics (`cond-mat.stat-mech`) and Machine Learning (`cs.LG`).
- **Journal:** *Physical Review Letters* 135, 027301 (2025), published 2025-07-08.
- **Source locality:** PDF, full-paper HTML, metadata HTML, source archive, extraction material, hashes, verification records, and rendered pages remain local. No source file appears in this DEP.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5, S6 | Primary metadata and publisher record | Title, authors, version history, categories, journal reference, DOI, and publication date. | Source identity and publication status. | High | Metadata does not validate method or results. |
| E2 | S2-S4, main text | Complete primary paper bundle | Free-energy objective, temperature conditioning, reverse-KL interpretation, reparameterization/REINFORCE derivatives, Ising/XY setups, results, and conclusion. | Mechanism and central claims. | High for source transcription | Mathematical statements were reviewed, not formally rederived or machine-checked. |
| E3 | S2-S4, Figures 1-4 | Main experimental evidence | Ising exact free-energy comparison, Ising and XY magnetization, configurations, energy, and heat-capacity curves. | Accuracy and phase-transition claims. | Medium-high | Plots do not provide full machine-readable error traces or uncertainty intervals. |
| E4 | S2-S4, Table S1 and Figures S1-S3 | Efficiency evidence | Eight-temperature convergence times, total-time crossover, RMHMC estimate, and lattice-size timing. | Source-reported efficiency. | Medium | One GPU; method-specific tuning; one threshold; RMHMC is estimated rather than run. |
| E5 | S2-S4, Tables S2-S3 and Figures S4-S7 | Architecture and scaling evidence | PixelCNN/NF hyperparameters, derivative-versus-statistical comparisons, and XY lattices through 258 by 258. | Implementation detail and reported scaling. | Medium-high for transcription | Batch sizes change for larger lattices; no repeated seeds or independent reproduction. |
| E6 | S7 | Official implementation | README, Apache-2.0 license, pinned dependencies, Ising/XY entry points, code defaults, and repository history. | Code availability and reproducibility assessment. | High for inspected state | No frozen paper release, checkpoints, seed ledger, or exact table-to-code manifest. |
| E7 | S7 versus S2-S4 | Cross-source comparison | XY code uses 25 spline bins and one fully connected layer; v2 Table S3 reports 45 interpolation points and two fully connected layers. | Reproducibility mismatch. | High for observed text | A different uninspected commit or private configuration could explain the difference. |
| E8 | S8 | Related DEP evidence | Differentiable physical modelling, variational many-body sampling, and distribution-transform geometry. | Cross-DEP synthesis and implementation framing. | Medium | Conceptual overlap is not empirical validation. |
| E9 | Selection and verification records summarized here | Process evidence | Uniform draw, dedup scan, bounded repair, PDF/HTML integrity gates, and no-source-upload gate. | Provenance and review eligibility. | High | Private execution paths and exact runtime are intentionally withheld. |

## Executive Summary

The paper introduces the variational temperature-differentiable method, or VaTD, for modelling a canonical ensemble with one tractable density generative model across a continuous inverse-temperature range. Conventional Markov chain Monte Carlo can be unbiased but suffers from autocorrelation and repeated equilibration, especially near phase transitions. Earlier generative samplers can draw independent samples but are usually trained at one temperature at a time and may collapse onto high-probability modes. VaTD conditions the model on inverse temperature `beta` and minimizes a temperature-averaged free-energy objective, making the learned density, partition-function estimate, and free-energy derivatives continuous in temperature.

At the exact variational optimum, the free-energy minimizer is the Boltzmann distribution. That is a theorem about the objective, not a guarantee that a finite PixelCNN or normalizing flow reaches the optimum. The empirical work uses a temperature-conditioned PixelCNN for a 16 by 16 Ising lattice and a temperature-conditioned normalizing flow with a von Mises prior for a 16 by 16 XY lattice. Source figures show close agreement with exact or MCMC free energy, magnetization, mean energy, and heat capacity, with the largest visible deviations near phase-transition regions.

The strongest efficiency evidence is supplementary. At eight inverse temperatures and a `10^-3` convergence threshold on one NVIDIA RTX 4090, the authors report VaTD convergence times generally 10-90 times lower than their HMC implementation. When training overhead is included, their XY comparison crosses HMC at about 18 evaluated temperature points. These are workload-specific results. The RMHMC curve is estimated from an assumed speed ratio, not measured; compute matching, repeated seeds, wall-clock variability, and independent implementations are absent.

The official Apache-2.0 code repository materially improves inspectability, but it does not close the reproduction gap. The inspected XY script differs from v2 Table S3 in spline-bin and fully connected layer defaults, and no release or checkpoint manifest pins the paper configuration. Confidence is therefore high for what the paper and repository contain, medium for the broad efficiency claim, and low for immediate transfer to atomistic simulations or other external parameters without new validation.

## Detailed Summary

### Problem context

A canonical ensemble assigns state probability in proportion to `exp(-beta E(x))`, normalized by the partition function `Z`. Thermodynamic observables follow from `Z` or derivatives of `log Z`: mean energy is its first derivative with respect to inverse temperature, and heat capacity depends on the second derivative. Exact enumeration is generally intractable, and phase transitions make numerical work harder because metastable states and long correlations matter.

MCMC offers a principled reference because its stationary distribution can be Boltzmann. Its sequential samples are correlated, however, and burn-in plus autocorrelation increase the cost of estimating observables at many temperatures. Tractable density generative models replace the Markov chain with direct sampling and expose the exact model density, enabling variational free-energy estimates. Training one model per temperature breaks continuity and repeats work; reverse-KL training can also under-cover modes.

### VaTD objective

For one temperature, minimizing `D_KL(q_theta || p)` is equivalent, up to `log Z`, to minimizing the expectation of `log q_theta(x) + beta E(x)`. VaTD promotes inverse temperature to a model input and samples it from a continuous uniform range during training:

`L = E_[beta, x~q_theta(x,beta)] [log q_theta(x,beta) + beta E(x)]`.

The supplementary derivation starts from free-energy minimization under normalization and shows that the Boltzmann density is the exact solution for each temperature. Integrating that variational problem over temperature yields the training objective. The method needs no observational dataset because the model supplies its own samples and the energy function supplies the physical score.

The trained model returns both configurations and a variational estimate of `-log Z(beta)`. Automatic differentiation then produces mean energy and heat capacity as derivatives. Reparameterization is used where samples admit a differentiable path; REINFORCE handles discrete sampling. The supplement extends first-order forms to second order and adapts reparameterization to the acceptance-rejection sampler used for the von Mises prior.

### Ising experiment

The Ising system is a 16 by 16 square lattice with periodic boundary conditions and binary spins. A temperature-conditioned PixelCNN factorizes the joint distribution autoregressively, uses Bernoulli conditionals, and fixes the first spin to break the global `Z2` symmetry. The paper reports training over `beta in [0.05, 1.2]`.

Figure 1 compares the estimated free energy with the exact solution and displays squared magnetization plus sampled configurations. The inset shows the largest relative error near the phase-transition region. Figure 2 compares free-energy-derived mean energy and heat capacity with MCMC; the curves closely follow each other with small deviations near the transition. The supplement reports a six-block masked-CNN ResNet, batch size 500, learning rate `5e-4`, gradient clip 1.0, and eight evaluation temperatures.

The model-selection description deserves caution. Training continues until an evaluation loss equilibrates, then the saved model with the smallest maximum difference from exact results over a stated interval is selected. This uses exact Ising information for selection and makes the Ising result a validation in a solvable benchmark, not a fully blind test of model choice.

### XY experiment

The XY system is another 16 by 16 periodic square lattice, but each spin is a continuous angle and the transition is of Berezinskii-Kosterlitz-Thouless type. VaTD uses a normalizing flow with a temperature-dependent von Mises prior and piecewise cubic spline coupling transforms. The first spin is pinned to remove `U(1)` symmetry, and training covers `beta in [0.4, 2.0]`.

Because the finite XY system has no exact free-energy solution in the paper, the authors use the standard deviation of per-sample free-energy estimates as an internal fit diagnostic and compare magnetization, mean energy, and heat capacity with MCMC. Figures 3 and 4 show close visual agreement and changing vortex configurations across temperature. This is meaningful but not independent ground truth: MCMC configuration, convergence, and uncertainty choices remain part of the benchmark.

The supplement reports five cubic transformation layers, 45 interpolation points, six ResNet blocks, batch size 1024, and learning rate `7e-4`. The inspected official script instead sets `K=25` bins and one hidden fully connected layer, while Table S3 reports two. That mismatch must be resolved before claiming exact reproducibility.

### Efficiency and scaling

Table S1 compares HMC and VaTD at eight inverse temperatures with a `10^-3` convergence threshold on one RTX 4090. Selected values illustrate the spread:

| beta | HMC mean energy (s) | VaTD mean energy (s) | HMC heat capacity (s) | VaTD heat capacity (s) |
|---:|---:|---:|---:|---:|
| 0.65 | 497.46 | 7.03 | 3164.93 | 35.98 |
| 0.90 | 526.67 | 38.94 | 21863.21 | 256.01 |
| 0.95 | 435.43 | 23.61 | 19654.64 | 206.86 |
| 1.25 | 568.46 | 6.39 | 4883.55 | 142.83 |

HMC used batch size 4000, sample interval 75, burn-in 1000 for heat capacity and 20 for mean energy, adaptive leapfrog steps targeting above 80% acceptance, and bootstrap uncertainty. VaTD used batch size 540 and derivative estimates. The authors summarize VaTD as generally 10-90 times faster in this experiment.

Training changes the cost model. Figure S1 starts VaTD with its training overhead and HMC at zero, placing the total-time crossover around 18 temperature points for the selected interval and threshold. An estimated best-case RMHMC curve delays crossover by about 50 more points. Because the RMHMC curve is constructed rather than measured, it is contextual sensitivity analysis, not a benchmark result.

The supplement also scales the XY lattice through 24, 32, 64, 96, 128, 192, 216, 256, and 258 per side. The authors report that phase-transition signals remain visible through 258 by 258. Above 32 by 32 they use checkpointing and smaller batches because of 24 GB GPU memory. This supports feasibility over a wider size range, but changing batch size and relying on visual curves does not establish constant-quality or constant-cost scaling.

### Derivative estimation

A distinctive claim is that differentiating the free-energy estimate can converge faster than estimating heat capacity from energy variance. If the model is exact, the derivative and statistical-average identities agree. Under imperfect training, the derivative follows the optimized free-energy surface more directly and may be more stable than a high-variance sample statistic. The supplement gives both a theoretical i.i.d. argument and numerical comparisons.

The paper also proposes a first-order heat-capacity approximation when free-energy-estimate variance is small, avoiding memory-heavy second-order reverse-mode differentiation. This depends on the learned density being close to a Boltzmann form and the partition-function estimate being stable across samples. It should be treated as a conditional approximation with an explicit variance gate.

### Code and reproducibility

The official repository contains separate autoregressive and flow modules, Ising and XY training scripts, plotting scripts, pinned Python dependencies, and an Apache-2.0 license. The default branch's latest inspected commit is `d8fd69c243951769e1e083f8451339522873af8f`. The README supplies one-command entry points for the two experiments.

Missing pieces include a tagged paper release, environment lock beyond six package pins, device and CUDA details, checkpoints, exact seeds, table-generation commands, raw HMC traces, a configuration manifest tying code values to v2 tables, and continuous integration that reproduces scientific outputs. The code is evidence of implementation availability, not a completed reproduction.
## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Temperature-averaged free-energy minimization has the Boltzmann distribution as its exact optimum for every temperature. | Author theoretical claim | E2 | Supported by the constrained variational derivation; finite-model optimization may not reach the optimum. | High for source statement |
| C2 | Any tractable density generative model can be adapted by adding temperature as an input. | Author framework claim | E2 | Architecturally plausible for differentiable normalized densities, but practical capacity, symmetry, and gradient estimators vary substantially. | Medium-high |
| C3 | One VaTD model represents a continuous temperature range and yields differentiable thermodynamic estimates. | Author method claim | E2, E3 | Directly implemented in both benchmark models and shown in continuous curves. | High for demonstrated scope |
| C4 | Ising and XY observables closely agree with exact or MCMC references, including near phase transitions. | Author empirical claim | E3 | Figures support close visual agreement with small transition-region deviations; no independent rerun or full uncertainty trace. | Medium-high |
| C5 | VaTD is generally 10-90 times faster than HMC in the reported convergence experiment. | Author empirical claim | E4 | Table S1 supports the stated range for the selected hardware and protocol; it is not a universal method ratio. | Medium |
| C6 | Including training time, VaTD becomes faster than HMC after about 18 temperature points in the tested XY sweep. | Author empirical claim | E4 | Supported by Figure S1 under the chosen interval and threshold; RMHMC comparison is estimated. | Medium |
| C7 | The method scales to 258 by 258 XY lattices while retaining phase-transition signatures. | Author scaling claim | E5 | Curves are shown, but batch sizes change and no exact quality reference is available at large sizes. | Medium |
| C8 | The public repository exactly reproduces the v2 paper configuration. | Unsupported inference | E6, E7 | Not established; inspected XY defaults conflict with Table S3 and no release manifest resolves the version. | High |
| C9 | Atomistic simulations are an immediate validated use case. | Author outlook, not demonstrated result | E2 | The paper identifies this direction but evaluates only lattice models. | Low |

## Methodology

- `Research objective`: Select one eligible local arXiv paper uniformly, require a verified complete local source bundle, review it at full-paper depth, connect it to exactly three related DEP entries, and create a public-safe DEP-E artifact.
- `Sources inspected`: Verified 36-page PDF, official full-paper HTML, metadata HTML, TeX/source package, primary figures and tables, arXiv record, APS issue record, official code README/license/dependencies/training entry points, live repository READMEs, publication index, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, grouped by unique PDF parent, sorted the unit list, selected a zero-based index uniformly with PowerShell `Get-Random`, derived identifiers from adjacent metadata, and scanned dedup stores before and after synchronizing the repository.
- `Inclusion criteria`: Evidence had to identify the paper, expose complete methods/results/limitations, establish code or publication context, define repository requirements, or provide concrete overlap in differentiable physical models, variational many-body sampling, or distribution-transform geometry.
- `Exclusion criteria`: Abstract-only content was excluded from method and empirical support. Generic discovery pages and unverified summaries were excluded. No source document was added to the public repository.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, replication, and safety/ethics review.
- `Evidence handling`: Author claims, direct source evidence, reviewer interpretation, cross-source conflicts, and implementation speculation are labeled separately. Quantitative results remain source-reported because experiments were not rerun.
- `Uncertainty handling`: Missing repeated seeds, unavailable raw traces/checkpoints, estimated RMHMC timing, model-selection leakage, code/table mismatch, and untested atomistic transfer remain explicit.
- `Extraction process`: All PDF pages were rendered and visually inspected in contact sheets, key plots/tables were inspected at page scale, TeX was extracted locally, and formulas/table values were cross-checked against the full HTML.
- `Version control`: Paper pinned to arXiv v2; code pinned to commit `d8fd69c243951769e1e083f8451339522873af8f`; journal identity pinned by DOI.
- `Reviewer stance`: DEP-ready paper report, critique, implementation translation, and replication planning.
- `Random selection`: 75,778 PDFs produced 75,776 unique PDF-parent units; the selected zero-based index was 20,958.
- `Deduplication and reselection validation`: arXiv ID, both DOIs, normalized title, and slug were checked in Black Lake logs, reports, lake data, staging, automation memory, relevant Black-Lake-Data context, and same-paper markers within 24 hours. Duplicate exclusions: 0; other exclusions: 0; reselections: 0.
- `Source-integrity repair`: Initial state was partial because full-paper HTML and companion records were missing. The valid existing PDF was preserved. Official full-paper HTML, metadata HTML, and the source package were collected with a bounded strategy. Final verification passed all PDF/HTML gates with no partials.

## Scope, Constraints, and Assumptions

- `Scope`: The VaTD objective, gradient estimators, Ising and XY experiments, efficiency/scaling claims, official code, and three cross-DEP concept bridges.
- `Temporal boundary`: Paper v2, publisher and repository records, and code state inspected through 2026-07-20.
- `Evidence limits`: No training, HMC run, figure reproduction, mathematical proof check, checkpoint evaluation, or performance benchmark was executed.
- `Assumptions`: The verified v2 PDF/HTML/source package represent the same research object; plotted labels and TeX tables accurately describe the authors' runs; the official repository is the implementation named by the paper.
- `Constraints`: Local source confidentiality, source non-redistribution, public-path sanitization, finite review time, and no external compute experiment.
- `Out of scope`: Production atomistic simulation, new physical claims, formal convergence proofs, hardware procurement, or universal comparisons with modern samplers.
- `Intended use`: Research triage, DEP deposition, replication planning, simulation-tool design, and benchmark specification.
- `Audience`: Statistical-physics researchers, scientific-ML engineers, generative-modelling researchers, and reviewers of differentiable simulation systems.
- `Depth target`: Schema-complete manuscript report with implementation and evidence boundaries.
- `Reproducibility boundary`: Public paper and code expose the method and entry points, but not a fully pinned experiment lineage.
- `Operational boundary`: Proposed products are offline research tools using synthetic or authorized energy functions and must not imply physical validity without benchmark gates.
- `Data sensitivity`: Public research sources and synthetic lattice configurations; future molecular data may carry license or proprietary constraints.

## Observations

- `Observed pattern`: VaTD moves temperature from an outer experiment index into the generative model's input and objective, converting repeated point estimates into a learned response surface.
- `Mechanistic observation`: Differentiable free energy is both the training target and the observable interface, which explains why derivative estimates may be more stable than unrelated sample moments when fit is good.
- `Contradiction or tension`: The objective has an unbiased Boltzmann optimum, but reverse-KL optimization with finite capacity can still under-cover modes; objective correctness is not optimization success.
- `Benchmark observation`: Direct-sampling gains grow when many temperatures are queried, so amortization and query count are part of the method, not incidental benchmark settings.
- `Reproducibility observation`: Official code exists, yet an exact table-to-configuration link is missing and inspected defaults conflict with the manuscript.
- `Reviewer hypothesis`: The most valuable near-term use is an auditable sweep tool for known energy functions, not an unqualified replacement for MCMC.

## Considerations

A VaTD deployment needs two independent gates: density-fit quality and derivative quality. Low training loss or low free-energy variance alone can miss unvisited modes. Evaluation should compare held-out temperatures, MCMC or exact references where available, mode coverage, symmetry behavior, free-energy residuals, first- and second-derivative errors, and extrapolation outside the training interval.

Compute comparisons should state training amortization, number and placement of temperature queries, convergence threshold, sampler tuning budget, hardware, precision, memory, burn-in, autocorrelation treatment, and uncertainty estimator. Estimated competitor curves must remain visually and numerically separate from measured results.

For molecular or atomistic systems, the energy function, boundary conditions, units, symmetries, long-range interactions, and metastable basins add new failure modes. Public physical simulations are non-sensitive, but proprietary force fields, molecular structures, or experimental data require separate rights and data-governance review.

## Strengths

- The method has a clear statistical-mechanical objective rather than an ad hoc temperature-conditioning loss.
- One framework is demonstrated with both a discrete autoregressive model and a continuous normalizing flow.
- Free-energy differentiation unifies configuration sampling and thermodynamic observables.
- Exact Ising comparison and MCMC XY comparison cover complementary validation settings.
- Supplementary material exposes convergence times, hyperparameters, derivative estimators, and larger-lattice tests.
- The official Apache-2.0 repository provides inspectable training entry points and dependencies.
- The paper distinguishes training overhead from repeated-query efficiency through a crossover analysis.

## Weaknesses

- The theoretical optimum does not guarantee a finite trained network covers all Boltzmann modes.
- Ising model selection uses exact-solution information over the evaluation interval.
- XY validation depends on the authors' MCMC implementation and internal free-energy variance diagnostic.
- No repeated-seed distributions, confidence intervals, raw traces, or independent reproduction are reported.
- The RMHMC comparison is estimated rather than executed.
- Scaling beyond 32 by 32 changes batching and relies primarily on plotted signatures.
- Official code defaults conflict with at least two v2 Table S3 settings.
- Generalization to pressure, magnetic field, or atomistic simulation remains outlook rather than evidence.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a tagged v2 reproduction release | Reproducibility | Current defaults do not fully match the paper table. | Exact trace from manuscript to code and checkpoints. | Maintenance and storage. | Rebuild all figures/tables from a clean environment. |
| Report repeated seeds and full uncertainty | Evidence | Curves and single timings hide optimization variability. | Calibrated confidence in fit and speed. | Multiple expensive runs. | Seed-level metrics, intervals, and preregistered aggregation. |
| Add mode-coverage diagnostics | Optimization | Reverse KL can ignore low-probability or metastable modes. | Detect false low-loss solutions. | Requires reference or stress construction. | Tempering tests, symmetry checks, rare-state probes, and bidirectional divergences. |
| Separate measured and estimated sampler curves | Benchmarking | RMHMC timing is modeled from literature. | Clearer competitor evidence. | Additional implementations. | Run tuned HMC/RMHMC/parallel tempering under matched hardware and criteria. |
| Validate blind temperature holdouts | Generalization | Continuous training may interpolate without robust extrapolation. | Direct evidence for response-surface fidelity. | Larger benchmark grid. | Hold out intervals and transition neighborhoods before training. |
| Test a bounded atomistic case | Transfer | Atomistic use is currently speculative. | Establish external validity and failure modes. | Energy-model and compute burden. | Compare free energy, forces, observables, and coverage with trusted references. |
| Add derivative-quality gates | Reliability | Small free-energy error can amplify under differentiation. | Prevent unstable observables. | Extra diagnostics and regularization. | Compare finite differences, autodiff, and sample statistics with uncertainty. |

## Potential Implementations

1. **Continuous-temperature lattice simulator.** `User`: statistical-physics researcher. `Goal`: train one auditable sampler over an inverse-temperature interval. `Core mechanism`: condition a tractable density model on beta, minimize the VaTD objective, and expose samples plus free-energy derivatives. `Required inputs`: bounded energy function, temperature range, symmetry rules, model family, and reference sampler. `Outputs`: configuration batches, free-energy curve, observables, coverage diagnostics, and evidence card. `Risk controls`: no extrapolation by default, mode-coverage tests, derivative cross-checks, and explicit benchmark lineage. `Evaluation`: exact/MCMC error, effective sample size, coverage, runtime, memory, and seed variability.
2. **Phase-transition sweep dashboard.** `User`: computational physicist. `Goal`: locate transition regions without training one model per temperature. `Core mechanism`: query a verified VaTD model over a dense beta grid and track energy, heat capacity, magnetization, variance, and derivative disagreement. `Required inputs`: validated checkpoint and authorized query interval. `Outputs`: curves, uncertainty bands, transition candidates, and warnings. `Risk controls`: label author/model estimates, display training support, and block claims when reference or stability gates fail. `Evaluation`: transition-location error, curve calibration, and false-warning rate.
3. **Sampler amortization benchmark.** `User`: scientific-ML reviewer. `Goal`: determine when a trained conditional sampler repays its training cost. `Core mechanism`: compare VaTD, HMC, parallel tempering, and normalizing-flow baselines over query counts and accuracy thresholds. `Required inputs`: pinned implementations, hardware, energy systems, budgets, and uncertainty protocol. `Outputs`: measured crossover surfaces rather than one crossover point. `Risk controls`: matched tuning budgets, separate measured/estimated curves, raw logs, and independent reruns. `Evaluation`: time-to-accuracy, energy use, memory, and coverage.

## Three Ways to Exercise This Research

1. **Exact Ising smoke test:** Objective: verify the objective and derivatives on a small solvable lattice. Inputs: a synthetic 4 by 4 Ising energy, fixed beta interval, and a tiny autoregressive density. Method: train across beta, compare `log Z`, energy, and heat capacity with exact enumeration, and repeat across fixed seeds. Output: error curves and a mode-coverage ledger. Success criterion: preregistered value and derivative tolerances pass on held-out beta points. Stop condition: any symmetry, coverage, or derivative gate fails.
2. **Amortization crossover study:** Objective: measure rather than assume the query-count benefit. Inputs: the same energy system, pinned VaTD and HMC implementations, hardware, and three convergence thresholds. Method: include training, tuning, burn-in, sampling, and evaluation time; sweep the number of requested temperatures. Output: measured crossover curves with uncertainty. Success criterion: results reproduce across seeds and remain stable under matched tuning budgets. Stop condition: competitor convergence or accuracy is not comparable.
3. **Capacity-failure stress test:** Objective: expose when objective correctness is defeated by model capacity or reverse-KL mode loss. Inputs: a multimodal toy energy landscape, progressively smaller density models, and a trusted reference. Method: measure free-energy loss, rare-mode mass, symmetry, sample diversity, and derivative error across capacity. Output: a failure map connecting low loss to missed modes. Success criterion: diagnostics flag collapse before thermodynamic errors exceed tolerance. Stop condition: no diagnostic separates valid and collapsed models.

## Example MVP Product

- `Product name`: ThermoSweep Lab.
- `Target user`: statistical-physics and scientific-ML researchers evaluating conditional equilibrium samplers.
- `Problem`: repeated per-temperature simulations are expensive, but a learned response surface can be physically misleading when modes or derivatives fail.
- `Core workflow`: register an energy function and beta interval; run exact or MCMC baseline probes; train a small VaTD model; validate density, samples, and derivatives on held-out temperatures; produce a signed evidence card; only then enable dense sweeps.
- `Data requirements`: synthetic or authorized energy functions, public lattice definitions, model configuration, reference traces, and seed-level metrics.
- `Architecture`: local CLI plus notebook dashboard; PyTorch model adapter; versioned experiment manifest; reference-sampler runner; coverage/derivative validators; static Markdown/JSON report.
- `Success metrics`: held-out free-energy and derivative error, transition-location error, mode coverage, effective sample size, measured time-to-accuracy, memory, and reproducibility across seeds.
- `Risk controls`: local-only inputs by default, no unsupported extrapolation, explicit source/model labels, fail-closed validation, raw-log retention, and no physical claim from loss alone.
- `Limitations`: research prototype; initial support limited to small public lattice systems; not a validated atomistic, molecular, or industrial simulator.
- `MVP boundary`: no automatic scientific conclusion, proprietary force field, cloud upload, or production control loop.
- `Deployment model`: local CLI and notebook.
- `Evaluation plan`: exact 2D toy systems, held-out beta intervals, seed replication, collapse stress tests, and matched HMC comparisons.
- `Failure modes`: mode collapse, derivative amplification, checkpoint/config drift, invalid symmetry handling, extrapolation, and unfair amortization accounting.
- `Maintenance plan`: pin dependencies and code commits, version benchmark manifests, refresh baselines, and require reproducibility review for model changes.

## Related Research and Reading

### Related DEP Entries

| Entry | Concrete overlap | Source basis |
|---|---|---|
| [Physical Data AI](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md) | Both place differentiable physical structure inside a trainable model and seek compact representations that remain scientifically interpretable. | The related manuscript's sections on analytic physical equations, differentiable computation, and residual learning were inspected. |
| [Surface SQD Study](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Surface%20SQD%20Study/surface-sqd-study.md) | Both estimate many-body energy behavior from samples and require physical-sector validity, classical comparators, and explicit scaling evidence. | The related manuscript's evidence ledger, constraint validation, energy estimation, and scaling cautions were inspected. |
| [Transport Convexity](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Transport%20Convexity/transport_convexity_manuscript.md) | Both use distribution-transform geometry to make a hard physical inference problem tractable, while the validity depends on explicit regularity assumptions. | The related manuscript's transport formulation, convexity assumptions, and implementation discussion were inspected. |

### Primary Reading

- [arXiv abstract and version record](https://arxiv.org/abs/2404.18404)
- [Publisher DOI landing page](https://doi.org/10.1103/8wx7-kyx8)
- [Official VaTD implementation](https://github.com/li012589/vatd)

## Source References

1. Shuo-Hui Li, Yao-Wen Zhang, and Ding Pan, "Deep generative modelling of canonical ensemble with differentiable thermal properties," arXiv:2404.18404v2, 2025. [arXiv](https://arxiv.org/abs/2404.18404). [arXiv DOI](https://doi.org/10.48550/arXiv.2404.18404). [Publisher DOI](https://doi.org/10.1103/8wx7-kyx8).
2. Li, Zhang, and Pan, official VaTD code repository, inspected at commit `d8fd69c243951769e1e083f8451339522873af8f). [GitHub](https://github.com/li012589/vatd).
3. American Physical Society, Physical Review Letters volume 135, issue 2, publication record. [Issue page](https://journals.aps.org/prl/issues/135/2).
4. Delphoa, "Physical Data AI," DEP-E-20260710. [Repository artifact](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md).
5. Delphoa, "Surface SQD Study," DEP-E-20260717. [Repository artifact](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Surface%20SQD%20Study/surface-sqd-study.md).
6. Delphoa, "Transport Convexity," DEP-E-20260718. [Repository artifact](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Transport%20Convexity/transport_convexity_manuscript.md).

## Appendix

### Replication Checklist

- Freeze the paper version, code commit, dependencies, configurations, seeds, and hardware.
- Reconcile the XY architecture and interpolation-point discrepancy before interpreting a replication.
- Use exact enumeration on the smallest Ising case and matched-convergence HMC on larger systems.
- Report training, tuning, burn-in, sampling, evaluation, and memory costs separately.
- Validate symmetry, normalization where tractable, rare-mode coverage, held-out beta behavior, and derivative accuracy.
- Label plotted scaling results separately from tabulated measured timing evidence.

### Selection and Integrity Record

The archive contained 75,778 PDF candidates representing 75,776 unique paper units. A uniform random draw over the sorted unique units selected zero-based index 20,958. Identifier-, DOI-, title-, and slug-level scans found no prior matching Arxiv DEP artifact, so the first draw was accepted with zero exclusions and zero reselections.

The selected unit initially had a verified complete PDF but lacked full-paper HTML. The archive was repaired from official public endpoints with bounded retries. The preserved PDF was 3,010,534 bytes, began with `%PDF-`, and ended with `%%EOF`. The repaired full-paper HTML was 318,497 bytes with 71,959 body characters, a document marker, 47 heading markers, seven paper-structure terms, and no error or abstract-only marker. Local README, attribution, machine-readable summary, and verification records were updated before review.

### Public-Output Gate

Only derived Markdown research artifacts were prepared for the public repository. Original PDFs, HTML, source archives, extracted text, caches, and other source documents remain in the local archive. No `.source/` directory was created, and no source file was uploaded.
