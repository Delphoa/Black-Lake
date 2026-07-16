---
title: "Noisy Poisson Inference - DEP-E"
description: "Source-grounded review of high-dimensional Poisson inference with covariate measurement error."
date: "2026-07-16"
authors:
  - "OpenAI Codex"
artifact_type: "research-manuscript"
dep_class: "DEP-E"
source_arxiv_id: "2301.00139v1"
source_doi: "10.48550/arXiv.2301.00139"
status: "deposited"
tags:
  - arxiv
  - poisson-regression
  - measurement-error
  - high-dimensional-inference
  - nonconvex-optimization
  - hypothesis-testing
  - neuroimaging
---

# Noisy Poisson Inference - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract record | Primary metadata | HTML | arXiv:2301.00139v1; DOI 10.48550/arXiv.2301.00139 | https://arxiv.org/abs/2301.00139v1 | Public metadata; abstract is not full-paper evidence | 2026-07-16 | Inspected |
| S2 | arXiv paper | Primary artifact | PDF | v1, 78 pages in inspected rendering | https://arxiv.org/pdf/2301.00139 | Complete local copy inspected; file withheld | 2026-07-16 | Inspected in full |
| S3 | arXiv source package | Primary artifact | TeX/source archive | v1; main and supplement present | https://arxiv.org/e-print/2301.00139 | Local package inspected; file withheld | 2026-07-16 | Inspected |
| S4 | Paper-declared code repository | Implementation evidence | Git repository | commit 41ca0fb990022015812e0ff53ab01627ddb6d21e | https://github.com/feigroup/high-dimenisional-inference-for-count-data-with-errors/tree/41ca0fb990022015812e0ff53ab01627ddb6d21e | No license found; inspected but not collected or executed | 2026-07-16 | Inspected |
| S5 | PAC Confidence DEP | Related Black Lake artifact | Markdown | DEP-E-20260713-PAC Confidence | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Context only; does not validate S1-S4 claims | 2026-07-16 | Inspected |
| S6 | Acoustic Phase Retrieval DEP | Related Black Lake artifact | Markdown | DEP-E-20260716-Acoustic Phase Retrieval | `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` | Context only; does not validate S1-S4 claims | 2026-07-16 | Inspected |
| S7 | Joint Sensing MEC DEP | Related Black Lake artifact | Markdown | DEP-E-20260715-Joint Sensing MEC | `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md` | Context only; does not validate S1-S4 claims | 2026-07-16 | Inspected |
| S8 | Black Lake README | Repository authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | DEP naming, contents, attribution, and source-withholding rules | 2026-07-16 | Inspected live |
| S9 | Selection, repair, cache, and dedup records | Processing evidence | Public-safe summaries | 75,776 units; index 45,743 | This manuscript, Methodology and Appendix | No local paths or exact execution timestamp | 2026-07-16 | Generated and validated |

Paper metadata:

- `Full title`: On High dimensional Poisson models with measurement error: hypothesis testing for nonlinear nonconvex optimization.
- `Authors`: Fei Jiang, Yeqing Zhou, Jianxuan Liu, and Yanyuan Ma.
- `Initial arXiv submission`: 2022-12-31.
- `Subjects`: Statistics Theory (`math.ST`) and Machine Learning (`cs.LG`).
- `Primary problem`: inference on selected coefficients in sparse high-dimensional Poisson regression when covariates are measured with additive error.
- `Source files deposited`: none; no `.source/` directory was created.
- `HTML provenance`: the official arXiv HTML endpoint was unavailable and ar5iv redirected to the abstract record. The verified local full-paper HTML was derived from every page of the verified PDF, labeled accordingly, and withheld.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S3 | Primary metadata and paper | Title, authors, version, dates, abstract, section structure | Bibliographic identity and stated contribution | High | Metadata alone does not validate theory or results |
| E2 | S2, S3, Sections 2-3 | Primary full text | Additive-error model, corrected exponential loss, constrained parameter space, amenable penalty conditions | Model and estimator formulation | High for transcription | Algebra not independently rederived |
| E3 | S2, S3, Theorems 1-3 and supplement | Primary theory | Local-minimum existence, error rates, selection consistency, asymptotic representation and normality | Estimation and selection claims | Medium-high | Depends on dense assumptions and an appropriate local solution |
| E4 | S2, S3, Sections 3-4 and supplement | Primary theory | Constrained null estimator, alternative estimator, covariance terms, Wald and score statistics | Asymptotic chi-square testing claims | Medium-high | Proofs not independently checked; finite-sample calibration is empirical |
| E5 | S2, S3, simulation tables | Primary empirical evidence | n/p settings, 500 replications, Type I error, power, naive-error comparisons, subset-size trend | Simulation results | High for transcription; low for reproduction | No rerun, raw draws, or seed-level uncertainty |
| E6 | S2, S3, ADNI section and tables | Primary empirical evidence | 196 complete samples, 218 covariates, MoCA outcome, significant features, BRAAK tests, cross-validation | Neuroimaging application | High for source reporting | Observational, small sample, multiplicity and generalization limits |
| E7 | S2, S3, discussion | Primary limitation | Poisson and Gaussian-error restrictions; overdispersion and extensions described as difficult | Scope boundaries | High | Paper does not exhaust all practical failure modes |
| E8 | S4 | Declared implementation | Repository tree, R scripts, data names, missing documentation/license, apparent county-data workflow | Reproducibility assessment | High for repository inspection | File names/content review is not an exhaustive provenance investigation |
| E9 | S5-S7 | Related DEP artifacts | Finite-sample coverage, conditioning under measurement noise, nonconvex iterative optimization | Cross-DEP synthesis | Medium | No joint experiment exists |
| E10 | S8, S9 | Repository and process evidence | Live authority, uniform draw, integrity gate, cache record, dedup scans | Artifact compliance and selection provenance | High | Search quality depends on available repository text and current checkout |

## Executive Summary

The paper asks how to perform sparse high-dimensional Poisson regression when the covariates that drive a count outcome cannot be observed exactly. If a latent vector `X` is observed only through `W = X + U`, substituting `W` into an ordinary Poisson likelihood is not innocuous: the exponential mean amplifies error and distorts both coefficient estimates and test calibration. The authors exploit a Gaussian measurement-error identity to subtract a quadratic covariance correction inside the exponential term. They combine the resulting nonconvex loss with an amenable nonconvex penalty and constrained `L1`/`L2` geometry.

The theoretical contribution is a local theory, not a global solver certificate. Under sparsity, curvature, tail, signal, covariance, dimension-growth, and tuning assumptions, the paper states consistency, variable-selection consistency, an asymptotic linear representation, and asymptotic normality for a selected/tested subvector. Constrained and unconstrained estimators support Wald and score tests whose statistics converge to chi-square laws under the null. Tested coefficients are left unpenalized to reduce shrinkage bias.

The simulations support the correction mechanism. Across reported settings with `n` of 300 or 500 and `p` up to 600, the corrected Wald and score tests are near the nominal Type I error and gain power as the signal increases. Naive procedures that ignore covariate noise can be grossly anti-conservative; one displayed null configuration reports rejection rates around 0.774 and 0.824 for naive variants versus 0.084 and 0.078 for corrected variants. Power decreases as the tested subset grows, illustrating that the asymptotic result does not erase finite-sample dimensional cost.

The ADNI example uses 196 complete observations and 218 covariates to associate neuroimaging features with Montreal Cognitive Assessment counts. The paper reports overlapping individual features and significant BRAAK-region group tests, plus lower cross-validated prediction error than the tested lasso workflow. These are exploratory observational associations. They are not causal, diagnostic, or clinically validated, and the reported false-discovery adjustment treats p-values as independent.

The declared code repository weakens reproducibility confidence. At the inspected commit it contains R scripts and R data objects with names and logic apparently centered on county COVID/weather data, not the reported ADNI pipeline, and provides no README, license, environment lock, or mapping from manuscript tables to commands. The implementation should therefore be treated as incomplete evidence rather than a turnkey reproduction.

## Detailed Summary

### Problem and Model

For independent observations, the latent covariate vector `X_i` drives a Poisson response with conditional mean `exp(beta^T X_i)`. The analyst instead sees `W_i = X_i + U_i`, where `U_i` is independent mean-zero Gaussian measurement noise with covariance `Omega`. The target coefficient is sparse while the ambient dimension may exceed sample size.

Ordinary penalized Poisson regression on `W` is biased because `E[exp(beta^T W) | X]` includes the factor `exp(beta^T Omega beta / 2)`. The paper reverses that factor and defines the corrected loss

`L(beta) = -(1/n) sum_i {Y_i W_i^T beta - exp(beta^T W_i - beta^T Omega beta / 2)}`.

The correction makes the score unbiased in the stated error model but also makes the empirical loss nonlinear and generally nonconvex. The feasible parameter space uses both `L1` and `L2` bounds. The `L1` constraint reflects sparsity; the `L2` bound limits the quadratic correction and helps local curvature arguments.

### Penalty and Optimization Geometry

The paper uses an amenable coordinatewise nonconvex penalty, covering SCAD and MCP under its conditions. The conditions include symmetry, monotonicity, a controlled concavity parameter, differentiability away from zero, and a derivative that vanishes beyond a sufficiently large signal. The ordinary lasso penalty does not satisfy the final unbiasedness-at-large-signals condition used for oracle-style selection.

The target inference set is not penalized. Remaining nuisance coordinates receive the nonconvex penalty. A constrained estimator under the null and an unconstrained alternative estimator are both local minimizers in a specified neighborhood. The proof strategy shows that, under restricted curvature and suitable initialization/solution conditions, a stationary/local solution has the desired error and support behavior. This does not show that arbitrary initialization reaches the statistical solution or that the solver finds a global optimum.

The numerical procedure uses an augmented-Lagrangian/ADMM-like iteration for the constrained problem and a related algorithm for the alternative. The source reports SCAD with `a = 3.7` and data-driven tuning. A production implementation needs explicit stopping rules, primal/dual residuals, multistart sensitivity, constraint feasibility, and failure reporting; these controls are not fully captured by an asymptotic theorem.

### Estimation and Selection Theory

The first layer of theory establishes high-dimensional error bounds for a local minimizer. The rates depend on sparsity, dimension, sample size, curvature, and tuning. A beta-min condition separates true active coefficients from zero strongly enough for variable-selection consistency. The vanishing derivative of an amenable penalty at large coefficients reduces shrinkage bias on strong signals.

The second layer gives an asymptotic representation for the tested and selected coordinates. Under stronger growth and remainder-control assumptions, the appropriately standardized subvector is asymptotically normal. The tested dimension may grow slowly, but it is not unrestricted. Error-covariance estimation enters the score and variance calculation; treating `Omega` as perfectly known is a strong operational boundary.

Assumptions should be read as a dependency graph rather than boilerplate. Tail conditions control empirical gradients and Hessians. Restricted curvature turns gradient control into parameter error. Sparsity and signal strength enable support recovery. Dimension-growth restrictions suppress high-order remainders. Penalty tuning and local-solution quality keep the optimizer in the theoretical basin. Misspecifying any early dependency can invalidate the later chi-square calibration.

### Wald and Score Tests

The target is a linear hypothesis `C beta_M = t` on a selected/tested coordinate set `M`, possibly involving several coefficients. The alternative fit estimates these coordinates without penalization. The constrained null fit imposes the linear equality. Covariance estimators incorporate Poisson variability and measurement-error correction.

The Wald statistic measures the standardized distance of the alternative estimate from the null surface. The score statistic evaluates a corrected gradient at the constrained estimator, with nuisance adjustment. Under the null and stated assumptions, each converges to a chi-square distribution with degrees of freedom equal to the number of restrictions.

The score test may be attractive when the null fit is already available, while the Wald test directly reports parameter displacement. Their agreement in simulations is reassuring but not proof of robustness. Both share the same model, covariance, local-solution, and asymptotic dependencies.

### Simulation Evidence

The simulation study spans `n = 300` and `500`, `p = 50`, `350`, and `600`, and 500 repetitions per reported configuration. Covariates and measurement errors follow controlled Gaussian structures. Comparisons include corrected and naive procedures, different effects, and different hypothesis sizes.

The corrected tests are generally close to the nominal 0.05 level in the displayed null rows. Power increases with effect size. In some high-dimensional settings an effect of 0.4 yields power near one for both corrected tests, but more complex hypotheses are harder. With `p = 350` and effect 0.8, a displayed Wald sequence falls from 1.000 to 0.950 to 0.854 as the tested subset grows from 4 to 8 to 12 coefficients.

The clearest mechanism check is the naive comparison. Ignoring measurement error can produce extreme false-positive inflation: a representative row reports roughly 0.774/0.824 for naive tests against 0.084/0.078 for corrected versions. The exact values belong to that simulation design, but the direction matches the analytic reason for correcting the exponential term.

Missing evidence includes raw replicates, seeds, Monte Carlo standard errors, alternative covariance misspecification, non-Gaussian error, correlated/repeated observations, negative-binomial outcomes, optimizer failure rates, and calibration conditional on support-selection mistakes.

### ADNI Application

The application uses 196 complete cases and 218 covariates. The response is a Montreal Cognitive Assessment score between 9 and 30 recorded within 14 days of imaging. Covariates include AV-1451 PET standardized uptake value ratios, regional volumes, age, and gender. Measurement-error covariance for imaging features is estimated using repeated longitudinal measurements, while age and gender are treated as exact.

At a nominal 0.05 threshold, the source reports 33 score-test and 69 Wald-test significant covariates, with 27 overlapping. Under an independence-based false-discovery adjustment at 0.05, the score list becomes empty while 36 Wald features remain, including 13 cortical SUVR features, mostly temporal. This divergence is a warning against presenting unadjusted discovery counts as stable findings.

Group tests for three BRAAK regions are reported significant. Score-test p-values are 0.039, 0.0113, and 0.0165; Wald p-values are 0.0039, approximately `1.774e-09`, and 0.0055. In 100 repetitions of five-fold cross-validation, the paper reports lower average prediction error for corrected score/Wald selection than lasso, while a naive penalized Poisson workflow did not converge.

The application remains exploratory. Complete-case selection may bias the cohort, the sample is small relative to the feature set, repeated measurements may not identify a universal covariance, neuroimaging features are dependent, the multiplicity model is simplified, and prediction error does not establish clinical utility. No causal or diagnostic inference follows from these associations.

### Implementation and Reproducibility Record

The paper cites `feigroup/high-dimenisional-inference-for-count-data-with-errors`. The inspected default-branch commit contains six R scripts and two R data objects organized under `realdata` and `simulation`. The simulation script exposes a small Gaussian-design example with 500 repetitions. The real-data file and script names refer to county data, March daily data, and weather-like variables; they do not visibly map to ADNI, MoCA, BRAAK regions, or the manuscript's neuroimaging tables.

No README, license, dependency lock, command map, seeds, expected outputs, or manuscript-to-script table was present. The repository may represent an earlier or different application, but the public evidence does not establish that. Reproduction should begin by requesting a versioned ADNI data dictionary, preprocessing manifest, permissible-access instructions, exact covariance estimator, tuning grids, fold assignments, and table-generation commands.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Gaussian measurement error admits a quadratic correction to the Poisson exponential loss. | Author formulation | E2 | Directly derived in the source under known `Omega` and independent additive Gaussian error. | High for formulation |
| C2 | An amenable nonconvex penalty and constrained geometry yield high-dimensional error and support-recovery properties for a suitable local minimizer. | Author theoretical claim | E3 | Supported by stated theorems, conditional on strong assumptions and local-solution access. | Medium-high |
| C3 | The tested/selected subvector has an asymptotic linear and normal representation. | Author theoretical claim | E3 | Source supports the claim under dimension, sparsity, signal, covariance, and remainder conditions. | Medium |
| C4 | Corrected Wald and score statistics are asymptotically chi-square under the null. | Author theoretical claim | E4 | Source theorem, not independently rederived; finite-sample validity remains design-dependent. | Medium-high |
| C5 | Corrected tests control Type I error much better than naive tests in the reported simulations. | Author empirical claim | E5 | Strong displayed contrast; no independent reproduction. | High for transcription; medium for mechanism |
| C6 | Power improves with signal but deteriorates as the tested subset becomes larger. | Author empirical claim | E5 | Tables support this finite-sample trend in the tested designs. | High for source reporting |
| C7 | The ADNI analysis identifies individual and BRAAK-region associations with MoCA. | Author empirical claim | E6 | Tables support source-reported associations; no causal, diagnostic, or external-validity claim is warranted. | Medium |
| C8 | The declared public implementation does not presently provide a transparent reproduction path for the ADNI results. | Reviewer finding | E8 | Direct repository inspection found a content mismatch and missing reproducibility scaffolding. | Medium-high |
| C9 | Robust deployment needs a chain of measurement, conditioning, finite-sample, optimization, and multiplicity checks. | Reviewer synthesis | E7, E9 | Conceptually supported across four artifacts; not jointly validated. | Medium |
| C10 | The selected paper passed first-draw eligibility after local integrity repair. | Process claim | E10 | Source gate, dedup scans, and cache record support the claim. | High |

## Methodology

- `Research objective`: Review one uniformly selected eligible local arXiv paper source-first, test archive integrity before synthesis, connect it to exactly three related DEP entries, and preserve a schema-complete public-safe DEP-E record.
- `Sources inspected`: verified full PDF; a full-text HTML derivative of that PDF; metadata HTML; TeX/source including main and supplement; arXiv metadata; the paper-declared Git repository pinned to a commit; live Black Lake authority; current dedup locations and automation memory; and exactly three related DEP manuscripts.
- `Discovery strategy`: enumerate PDFs with `rg --files -g "*.pdf"`; normalize unique parent directories as paper units; draw a uniform zero-based PowerShell `Get-Random` index; inspect adjacent metadata; then derive and verify the arXiv identifier.
- `Inclusion criteria`: primary or official sources establishing identity, method, theorems, numerical evidence, limitations, implementation availability, deposition rules, duplicate status, or concrete conceptual overlap.
- `Exclusion criteria`: abstract-only pages as full-paper evidence, duplicate/recent deposits, secondary summaries where primary text existed, unverified clinical claims, and unrelated DEP entries.
- `Analytical approach`: mathematical-mechanism reconstruction, empirical table review, implementation audit, clinical-scope critique, provenance review, cross-DEP synthesis, and product/replication translation.
- `Evidence handling`: author theory, author empirical claims, reviewer findings, synthesis, and process evidence use distinct ledger rows and claim labels. Numerical claims remain source-reported unless independently reproduced.
- `Uncertainty handling`: proofs were not independently derived; experiments were not rerun; optimizer convergence, covariance estimation, multiplicity, cohort bias, and code mismatch remain explicit.
- `Source integrity`: the unit began `partial` because it lacked full-paper HTML. Official arXiv HTML was unavailable and ar5iv redirected to metadata, so neither passed. A local page-complete HTML rendering was generated from the verified PDF, provenance-labeled, structurally verified, and kept local. Final status was `complete`.
- `Extraction process`: extractor preflight found `pypdf`; missing-only extraction used `pypdf`, `html-regex`, and `tarfile` on the repaired local unit.
- `Cache methodology`: initial lookup was a miss. Backfill completed in 2.322 seconds with 175,819 bytes of PDF text, 170,805 bytes of HTML text, and 348,082 bytes of source text; final status `cached`.
- `Random selection`: 75,777 PDFs collapsed to 75,776 unique parent-paper units; uniform zero-based selected index 45,743; accepted on first draw.
- `Dedup and reselection validation`: arXiv ID, DOI, normalized title, slug, logs, reports, DEP-E paths, public pointer index, automation memory, companion-repository entries, and 24-hour same-paper markers were searched. A metadata-only author inventory row was not a research artifact. Exclusions 0; reselections 0.
- `Version control`: paper pinned to arXiv v1; code pinned to commit `41ca0fb990022015812e0ff53ab01627ddb6d21e`.
- `Safety handling`: no local path, host detail, exact execution timestamp, source bytes, identifiable patient record, or clinical recommendation is public. Source files were withheld locally.
- `Reviewer stance`: critical research preservation, bounded implementation translation, reproducibility audit, and validation planning.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2301.00139v1; corrected loss; penalty and optimizer; estimation, selection, and testing theory; simulations; ADNI application; declared code; and exactly three related DEP bridges.
- `Temporal boundary`: the paper is pinned to v1 submitted 2022-12-31; repository and related-source inspection is date-only through 2026-07-16.
- `Primary assumptions`: additive independent Gaussian covariate error; credible known or estimated covariance `Omega`; conditionally Poisson outcome; sparse coefficient; restricted local curvature; controlled covariate/error tails; sufficient signal; dimension/sparsity growth restrictions; suitable tuning; and an appropriate local minimum.
- `Evidence limits`: no theorem rederivation, proof assistant, data access, code execution, simulation rerun, optimizer trace, or external cohort validation.
- `Optimization boundary`: convergence to a stationary/local solution does not imply global optimality, and the statistical theory does not certify arbitrary solver output.
- `Clinical boundary`: ADNI findings are observational research associations, not causal conclusions, diagnoses, treatment guidance, or evidence of deployment benefit.
- `Multiplicity boundary`: the reported adjustment assumes independent p-values even though imaging features are correlated.
- `Reproducibility boundary`: public scripts do not visibly reconstruct the ADNI analysis; exact data, preprocessing, environment, tuning, and output mapping are missing.
- `Public-output boundary`: all source documents, derivative full-text HTML, caches, and extracted text stay local; only derived Markdown and the required pointer/index JSON are public.

## Observations

- Measurement error affects the objective exponentially, so a small covariate perturbation can create large inferential distortion if ignored.
- The correction moves uncertainty into both estimation and variance calculation; it cannot be safely reduced to one preprocessing denoiser.
- A local-minimum theorem is useful only when an implementation records which local solution was reached and why it belongs to the theoretical neighborhood.
- The corrected-versus-naive simulation contrast is more convincing as a mechanism check than the absolute power values are as deployment forecasts.
- Growing tested-set size visibly reduces power, matching the intuition that joint inference consumes finite-sample information.
- The ADNI Wald/score discovery gap and the collapse of score discoveries after multiplicity adjustment show that headline feature counts are unstable summaries.
- The code mismatch is not proof of invalid results, but it prevents an external reviewer from linking claims, inputs, and commands.

## Considerations

- Validate overdispersion with residual and mean-variance diagnostics before accepting a Poisson working model.
- Estimate `Omega` on a defensible replicate design and propagate its uncertainty through tests; avoid treating a noisy plug-in estimate as known.
- Use sample splitting or selective-inference analysis when data-dependent feature selection could contaminate nominal p-values.
- Replace independence-only multiplicity reasoning with procedures and sensitivity analyses suitable for dependent neuroimaging features.
- Record optimizer starts, residuals, feasibility, objective traces, support stability, and termination reasons.
- Run stress tests with non-Gaussian error, covariance misspecification, correlated observations, missing-not-at-random data, and alternative count distributions.
- Separate predictive validation from inferential validation; low cross-validation error does not imply calibrated tests or clinical usefulness.
- Require a data dictionary, cohort flow, missingness analysis, scanner/site stratification, and external replication before interpreting biomarkers.

## Strengths

- The loss correction is mechanistically tied to the measurement-error moment-generating function rather than an ad hoc penalty.
- Estimation, support recovery, asymptotic normality, and composite hypothesis testing are addressed in one framework.
- The paper analyzes both Wald and score routes and leaves tested coefficients unpenalized.
- Simulations explicitly include naive procedures and reveal why ignoring measurement noise can be dangerous.
- The ADNI application demonstrates group hypotheses, not only single-coefficient tests.
- Main and supplementary source files provide substantial theoretical detail.

## Weaknesses

- Guarantees rely on strong model, tail, curvature, signal, tuning, covariance, and local-solution assumptions.
- Finite-sample evidence does not stress covariance misspecification, overdispersion, dependent data, or non-Gaussian error.
- Simulation uncertainty and optimizer failure frequencies are not reported transparently.
- The clinical application is small and complete-case, with a simplified dependence assumption for false-discovery control.
- Prediction comparisons do not establish inferential validity or clinical value.
- The declared repository lacks a clear match to the ADNI experiment, documentation, licensing, and an environment lock.

## Potential Improvements

- Develop sandwich or negative-binomial variants for overdispersed counts and report when the Poisson score remains usable as a quasi-likelihood.
- Treat `Omega` estimation as a first-class uncertainty source with bootstrap, influence-function, or joint-estimation intervals.
- Provide finite-sample calibration through parametric bootstrap or a carefully justified resampling procedure.
- Add sample-splitting, cross-fitting, or selective-inference comparisons for data-dependent support selection.
- Evaluate dependent false-discovery procedures and stability selection on correlated imaging groups.
- Report multistart and perturbation diagnostics for the nonconvex solver, including infeasible and nonconverged trials.
- Release a licensed repository with data-access instructions, exact environments, seeds, fold assignments, and one command per figure/table.
- Replicate on independent sites and scanners, stratify demographic performance, and publish negative findings.

## Potential Implementations

1. **Noisy-count inference workbench:** an offline research tool accepts count outcomes, measured covariates, replicate-based error covariance, and a hypothesis matrix; it returns model diagnostics, solver traces, corrected estimates, Wald/score comparisons, and assumption warnings.
2. **Covariance sensitivity dashboard:** a reviewer varies structured perturbations to `Omega` and observes support changes, p-value paths, test disagreement, and multiplicity-adjusted stability before approving a scientific claim.
3. **Reproducibility manifest checker:** a repository audit maps every table and figure to data schema, preprocessing hash, environment, tuning grid, seed/fold record, command, and expected checksum, failing closed when the mapping is incomplete.

These are research and audit tools. They must not automatically issue diagnoses, patient-level recommendations, or consequential decisions.

## Three Ways to Exercise This Research

1. **Null-calibration stress test:** simulate sparse Poisson outcomes with Gaussian, heavy-tailed, and misspecified covariate error; measure Type I error, coverage, convergence, and support stability across sample sizes.
2. **Optimizer-basin audit:** run the constrained and alternative solvers from many deterministic initializations; compare objectives, feasibility, supports, p-values, and membership in the theory-compatible neighborhood.
3. **Clinical replication drill:** construct a synthetic, public-safe ADNI-shaped data dictionary and require an analyst to reproduce a preregistered cohort flow, covariance estimate, group hypotheses, dependent multiplicity plan, and external-validation report.

## Example MVP Product

**MVP: Error-Aware Count Lab**

The MVP is a local-only statistical audit application, initially restricted to synthetic or explicitly authorized data. Its workflow is:

1. Validate nonnegative integer outcomes, feature dimensions, missingness, replicate identifiers, and a symmetric positive-semidefinite error covariance.
2. Fit an ordinary Poisson baseline and surface overdispersion, residual, leverage, and separation warnings.
3. Fit the corrected constrained and alternative objectives from several deterministic starts while logging feasibility and convergence.
4. Compute Wald and score statistics for preregistered linear hypotheses; display disagreement and sensitivity to `Omega`, penalty, and support.
5. Apply a selected dependence-aware multiplicity method and export an evidence ledger, not a clinical conclusion.

Acceptance criteria include reproducible synthetic fixtures, nominal-null calibration within preregistered Monte Carlo tolerance, explicit nonconvergence outcomes, no silent covariance repair, and a report that labels every result as author method, independent test, or reviewer interpretation.

## Related Research and Reading

1. **PAC Confidence** - `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`. This artifact provides a finite-calibration-set interval construction and makes the identical-distribution boundary explicit. The bridge is a validation question: asymptotic chi-square calibration should be paired with finite-sample and distribution-shift stress tests rather than treated as unconditional confidence.
2. **Acoustic Phase Retrieval** - `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md`. This artifact recovers latent phase from noisy magnitude measurements and ties stability to an observable determinant bound. The bridge is conditioning: error correction is credible only when the measurement mechanism and its covariance/conditioning are validated.
3. **Joint Sensing MEC** - `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md`. This artifact alternates discrete and continuous updates in a nonconvex objective and distinguishes monotone convergence from global optimality. The bridge is solver governance: a descending objective is not a certificate that the statistically valid local solution was found.

## Source References

1. Jiang, F.; Zhou, Y.; Liu, J.; Ma, Y. *On High dimensional Poisson models with measurement error: hypothesis testing for nonlinear nonconvex optimization*. arXiv:2301.00139v1. https://arxiv.org/abs/2301.00139v1
2. Primary paper PDF. https://arxiv.org/pdf/2301.00139
3. Primary TeX/source package. https://arxiv.org/e-print/2301.00139
4. Canonical arXiv DOI. https://doi.org/10.48550/arXiv.2301.00139
5. Paper-declared code repository, inspected commit. https://github.com/feigroup/high-dimenisional-inference-for-count-data-with-errors/tree/41ca0fb990022015812e0ff53ab01627ddb6d21e
6. PAC Confidence DEP. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md
7. Acoustic Phase Retrieval DEP. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Acoustic%20Phase%20Retrieval/acoustic_phase_retrieval_manuscript.md
8. Joint Sensing MEC DEP. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Joint%20Sensing%20MEC/joint_sensing_mec_manuscript.md

## Appendix

### Selection and Dedup Record

- Enumeration: 75,777 local PDFs with `rg --files -g "*.pdf"`.
- Unit normalization: 75,776 unique PDF parent directories.
- Uniform draw: PowerShell `Get-Random`, zero-based index 45,743.
- Acceptance: first draw; exclusions 0; reselections 0.
- Dedup keys: arXiv ID, DOI, normalized title, slug, artifact path, memory, companion metadata, and preceding-24-hour markers.
- Result: no research deposit matched. One author-inventory metadata row was non-substantive and did not exclude the paper.

### Integrity and Cache Record

- Initial classification: `partial` because the PDF was valid but full-paper HTML was absent.
- PDF: 1,385,919 bytes, `%PDF-` header, trailing `%%EOF`.
- Public HTML: official endpoint unavailable; ar5iv redirected to a 42,317-byte abstract record, classified metadata-only.
- Repair: locally derived page-complete HTML from the verified 78-page PDF, explicitly labeled as a derivative.
- HTML verification: 182,059 bytes; 170,802 body characters; article/main marker; 79 headings; eight checked structure terms.
- Source package: 5,848,348 bytes; 105 entries; main and supplement located.
- Partials after repair: 0.
- Cache: initial miss; `missing-only` backfill in 2.322 seconds; final status `cached`.
- Extracted text: PDF 175,819 bytes; HTML 170,805 bytes; source 348,082 bytes.
- Public-source gate: source documents and all extracted/cache derivatives were withheld locally and are absent from this DEP.

### Reproduction Checklist

- [ ] Obtain authorized data and publish a cohort/data-flow record.
- [ ] Pin the data dictionary, inclusion/exclusion rules, and missingness handling.
- [ ] Specify replicate design and validate the error-covariance estimator.
- [ ] Pin runtime, packages, seeds, folds, tuning grids, and solver tolerances.
- [ ] Map each paper table/figure to an executable command and expected output.
- [ ] Report multistart convergence, feasibility, and support stability.
- [ ] Test overdispersion, non-Gaussian error, covariance misspecification, and dependence.
- [ ] Separate preregistered hypotheses from exploratory selection.
- [ ] Use dependence-aware multiplicity controls and external validation.
- [ ] Preserve an immutable evidence ledger and disclose all negative results.
