# Report-Mark: Noisy Poisson Inference

## Review Status

- Deposit date: 2026-07-16
- Primary work: arXiv:2301.00139v1
- Review mode: source-first, full-paper, public-safe
- Local integrity: initial `partial`; repaired and verified `complete`
- Cache: initial miss; missing-only backfill completed with status `cached`
- Reproduction: paper, proofs, simulations, and ADNI analysis were not independently rerun
- Source handling: every original or derived source document remains local; no source file is deposited

## Source Metadata

| Field | Value |
|---|---|
| Title | *On High dimensional Poisson models with measurement error: hypothesis testing for nonlinear nonconvex optimization* |
| Authors | Fei Jiang; Yeqing Zhou; Jianxuan Liu; Yanyuan Ma |
| Identifier | arXiv:2301.00139v1 |
| DOI | 10.48550/arXiv.2301.00139 |
| Submitted | 2022-12-31 |
| Subjects | Statistics Theory (`math.ST`); Machine Learning (`cs.LG`) |
| Canonical record | https://arxiv.org/abs/2301.00139v1 |
| Full paper | https://arxiv.org/pdf/2301.00139 |
| Source package | https://arxiv.org/e-print/2301.00139 |
| Declared code | https://github.com/feigroup/high-dimenisional-inference-for-count-data-with-errors/tree/41ca0fb990022015812e0ff53ab01627ddb6d21e |

The complete local evidence bundle included a verified PDF, a provenance-labeled full-text HTML rendering derived from that PDF, arXiv metadata HTML, TeX/source, and extraction-cache outputs. The official arXiv full-paper HTML endpoint was unavailable. Approved ar5iv attempts redirected to the abstract record; those bytes were classified as metadata only and never counted as the paper.

## Concise Research Notes

### Problem

High-dimensional Poisson regression assumes count outcomes depend on covariates through an exponential conditional mean. When latent covariates `X` are observed only as `W = X + U`, fitting an ordinary Poisson model to `W` changes the exponential moment and can severely distort estimates, feature selection, and test size.

### Method

For independent Gaussian measurement error `U` with covariance `Omega`, the paper uses the loss

`L(beta) = -(1/n) sum_i {Y_i W_i^T beta - exp(beta^T W_i - beta^T Omega beta / 2)}`.

It combines this corrected loss with an `L1`/`L2` constrained parameter set and an amenable nonconvex penalty such as SCAD or MCP. Tested coordinates are unpenalized. The paper builds a constrained estimator under `C beta_M = t` and an unconstrained alternative, then forms Wald and score statistics with corrected covariance terms.

### Theory

Under sparsity, restricted/local curvature, tail, signal, dimension-growth, covariance, and tuning assumptions, the source states high-dimensional error rates, selection consistency, an asymptotic linear representation, and asymptotic normality for the tested/selected subvector. The Wald and score statistics converge to chi-square laws under the null.

The theory applies to an appropriate local minimum. It does not certify a global optimum or arbitrary solver output. A deployable implementation must show initialization, residuals, feasibility, multistart stability, termination, and agreement with the theory-compatible neighborhood.

### Simulation Evidence

The simulations use `n = 300` or `500`, `p = 50`, `350`, or `600`, and 500 replications. Corrected Wald and score tests generally track nominal 0.05 Type I error and gain power with signal. A representative null comparison reports naive rejection rates near 0.774 and 0.824 versus corrected values 0.084 and 0.078. With `p = 350` and effect 0.8, one Wald sequence falls from 1.000 to 0.950 to 0.854 as tested-set size grows from 4 to 8 to 12.

These results support the correction mechanism in controlled designs. They do not establish calibration under overdispersion, non-Gaussian error, covariance misspecification, dependent samples, missing-not-at-random features, or optimizer failures.

### ADNI Evidence

The application analyzes 196 complete observations and 218 covariates. Montreal Cognitive Assessment scores range from 9 to 30 and were collected within 14 days of imaging. Covariates include AV-1451 PET SUVRs, regional volumes, age, and gender. Imaging-error covariance is estimated from repeated longitudinal features; age and gender are treated as exact.

The paper reports 33 score-test and 69 Wald-test features at nominal 0.05, with 27 overlaps. An independence-based false-discovery adjustment leaves no score features and 36 Wald features. Three BRAAK group tests are reported significant, with score p-values 0.039, 0.0113, and 0.0165 and Wald p-values 0.0039, `1.774e-09`, and 0.0055. Across 100 repetitions of five-fold cross-validation, corrected selection reports lower average prediction error than lasso; a naive penalized Poisson workflow reportedly failed to converge.

These are observational associations from a modest complete-case sample. They do not establish causality, a diagnosis, a biomarker, treatment utility, or external validity. Imaging-feature dependence also weakens an independence-only multiplicity interpretation.

### Implementation Evidence

The paper-declared repository was inspected at commit `41ca0fb990022015812e0ff53ab01627ddb6d21e`. It contains six R scripts and two R data files under simulation and real-data folders. The simulation code visibly defines a Gaussian-design example with 500 repetitions. The real-data names and code appear centered on county COVID/weather variables, not ADNI, MoCA, or BRAAK features.

No README, license, dependency lock, seed manifest, expected output, or manuscript-to-command mapping was found. This is a reproducibility shortfall, not proof that the reported results are false. The public record presently does not show how to reconstruct the paper's neuroimaging analysis.

## Evidence and Attribution

| Evidence | Source basis | Use | Qualification |
|---|---|---|---|
| Corrected loss and measurement model | PDF and TeX, model sections | Mechanism reconstruction | Algebra transcribed, not independently rederived |
| Estimation and testing theory | PDF, TeX, supplement | Theorem summary | Author claims under stated assumptions |
| Type I error and power | Simulation tables | Empirical assessment | Source-reported; not rerun |
| ADNI feature/group results | Application section and tables | Applied evidence | Observational and exploratory |
| Code availability | Pinned declared repository | Reproducibility audit | Tree/content inspected; code not run |
| Integrity/cache/dedup | Local verification and public-safe process records | Provenance | Local paths and source bytes withheld |
| Cross-DEP relationships | Three deposited manuscripts | Conceptual synthesis | Does not validate the selected paper |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
   - Relevance: finite-sample coverage, calibration support, and identical-distribution boundaries provide a contrast to asymptotic chi-square calibration.
   - Source basis: the manuscript's Evidence Ledger, confidence-coverage construction, and limitation on calibration/test distribution equality.
2. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md`
   - Relevance: noisy measurements require an explicit intervention/measurement model and a conditioning certificate before inverse recovery can be trusted.
   - Source basis: the manuscript's determinant bound, perturbation theorem, synthetic noise study, and reviewer assessment.
3. `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md`
   - Relevance: iterative decomposition of a nonconvex mixed problem clarifies why descent/convergence should not be promoted to global optimality.
   - Source basis: the manuscript's mixed objective, block-coordinate updates, potential-game argument, and convergence limitations.

## Synthesis Note

### Concept Bridge

All four artifacts concern a hidden quantity inferred or acted upon through an imperfect observation-and-computation chain. Noisy Poisson Inference corrects an exponential statistical objective for covariate error. Acoustic Phase Retrieval deliberately changes the measurement setup and bounds an inversion determinant. PAC Confidence wraps finite calibration observations in simultaneous intervals and states the distribution boundary. Joint Sensing MEC alternates decisions within a nonconvex objective and limits its convergence claim.

The joint bridge is a five-gate evidence architecture:

`measurement validity -> conditioning/covariance -> optimizer validity -> inferential calibration -> deployment envelope`.

Passing a later gate cannot repair a failed earlier one. A chi-square p-value is not meaningful if the measurement covariance is unverified; a stable optimizer does not imply the correct local solution; an on-distribution interval does not transfer through site shift; and a decreasing system cost is not global optimality.

### Potential Implementations

1. Build an offline noisy-count audit workbench that checks count-model fit, replicate-based covariance, multistart convergence, corrected Wald/score agreement, and dependent multiplicity before exporting a research ledger.
2. Build a covariance-and-conditioning sensitivity dashboard that perturbs `Omega`, tracks support and p-value paths, and blocks claims whose result changes under plausible measurement uncertainty.
3. Build a provenance-driven reproduction harness that binds data schema, environment, tuning, folds, seeds, commands, expected outputs, and evidence labels to every manuscript table.

### Deeper Relationship Observations

1. Measurement correction and phase recovery both rely on structural knowledge that makes a latent signal identifiable; uncertainty in that structure must be propagated rather than hidden in a point estimate.
2. PAC coverage and asymptotic chi-square calibration solve different uncertainty problems: one controls finite calibration-sample error under a distribution envelope, while the other controls a statistic in a growing-sample model under regularity conditions.
3. Joint Sensing MEC and the Poisson method both use iterative progress inside nonconvex geometry; in each case, convergence language must specify whether it means objective descent, stationarity, a local statistical solution, or global optimality.

### Conceptual Similarities

1. Each method turns a nuisance quantity—measurement error, missing phase, calibration uncertainty, or sensing failure—into an explicit mathematical object rather than ignoring it.
2. Each guarantee is conditional on a support envelope: covariance and tails, determinant conditioning, identical data distributions, or stationary sensing/channel assumptions.
3. Each source needs operational monitoring beyond the theorem, including data-quality checks, solver traces, threshold support, and a safe failure state.

### MVP Implementations with Code Mock-ups

1. **Covariance sensitivity gate**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class SensitivityResult:
    stable: bool
    max_pvalue_shift: float
    support_agreement: float

def covariance_gate(base_p, trial_p, support_agreement, limit=0.02):
    shift = max(abs(a - b) for a, b in zip(base_p, trial_p, strict=True))
    return SensitivityResult(
        stable=shift <= limit and support_agreement >= 0.90,
        max_pvalue_shift=shift,
        support_agreement=support_agreement,
    )
```

The production version would generate structured positive-semidefinite perturbations from replicate uncertainty and retain the complete path, not only the maximum shift.

2. **Solver evidence gate**

```python
def solver_gate(runs, feasibility_tol=1e-6, objective_gap=1e-4):
    feasible = [run for run in runs if run["constraint_residual"] <= feasibility_tol]
    if not feasible:
        return {"passed": False, "reason": "no feasible solution"}
    values = [run["objective"] for run in feasible]
    spread = max(values) - min(values)
    return {
        "passed": spread <= objective_gap,
        "feasible_runs": len(feasible),
        "objective_spread": spread,
    }
```

The gate intentionally reports disagreement across starts; it must not silently select the most favorable p-value.

3. **Reproduction manifest gate**

```python
REQUIRED = {
    "data_dictionary",
    "environment_lock",
    "preprocessing_hash",
    "seed_manifest",
    "fold_manifest",
    "tuning_grid",
    "table_commands",
}

def manifest_gate(manifest):
    missing = sorted(REQUIRED.difference(manifest))
    return {"passed": not missing, "missing": missing}
```

The initial harness should use synthetic/public-safe fixtures. Authorized clinical data remain outside the repository and require independent governance.

### Developer Challenges

1. Implement the corrected gradient, Hessian, constraints, SCAD/MCP proximal logic, and covariance terms with numerical tests that detect sign or scaling errors in the exponential correction.
2. Make local-solver outcomes auditable through deterministic multistart, primal/dual residuals, feasibility checks, support paths, and explicit nonconvergence states.
3. Build privacy-preserving clinical data adapters and dependent-multiplicity workflows without leaking source data or silently changing the preregistered hypothesis set.

### Author Challenges

1. Release a licensed, documented repository that clearly reproduces the ADNI analysis and maps every table and figure to pinned data schemas, packages, seeds, folds, tuning, and commands.
2. Quantify finite-sample behavior under estimated and misspecified `Omega`, overdispersion, non-Gaussian error, dependent observations, selection reuse, and optimizer instability.
3. Validate the neuroimaging findings externally with cohort-flow reporting, site/scanner sensitivity, dependence-aware multiplicity, demographic analysis, and a clear non-causal interpretation.

## Validation Notes

- Manuscript contract: required YAML, H1, source metadata, evidence ledger, summary, claims, methodology, scope, observations, considerations, strengths, weaknesses, improvements, implementations, exercises, MVP, related reading, references, and appendix are present.
- Title contract: YAML title and manuscript H1 are identical and contain no more than 40 characters.
- Selection contract: 75,777 PDFs, 75,776 units, uniform index 45,743, first draw, zero exclusions, zero reselections.
- Integrity contract: valid PDF plus verified full-paper HTML; metadata-only redirects explicitly rejected; 0 partials; final `complete`.
- Cache contract: preflight and missing-only extraction recorded; miss became `cached`.
- Dedup contract: ID, DOI, normalized title, slug, artifacts, memory, companion entries, and recent markers checked.
- Related-entry contract: exactly three related DEP entries inspected and attributed.
- Synthesis contract: exactly three potential implementations, deeper observations, conceptual similarities, MVP mock-ups, developer challenges, and author challenges.
- Code validation: all three Python mock-ups use syntax-compatible standard-library constructs and no external data or network calls.
- Public-safety contract: no local path, drive, username, host, local timezone, or exact execution timestamp appears; no source file is included.
- Source gate: public artifact allowlist is Markdown plus the required derived index/pointer JSON only.

## Attribution Block

- Primary metadata: https://arxiv.org/abs/2301.00139v1
- Primary full-paper PDF, inspected locally and withheld: https://arxiv.org/pdf/2301.00139
- Primary TeX/source package, inspected locally and withheld: https://arxiv.org/e-print/2301.00139
- Canonical DOI: https://doi.org/10.48550/arXiv.2301.00139
- Paper-declared code, inspected but not collected or executed: https://github.com/feigroup/high-dimenisional-inference-for-count-data-with-errors/tree/41ca0fb990022015812e0ff53ab01627ddb6d21e
- Related PAC Confidence DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md
- Related Acoustic Phase Retrieval DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Acoustic%20Phase%20Retrieval/acoustic_phase_retrieval_manuscript.md
- Related Joint Sensing MEC DEP: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Joint%20Sensing%20MEC/joint_sensing_mec_manuscript.md
- Source-file statement: PDF, full-paper HTML, metadata HTML, TeX/source, cache, extracted text, and code files were withheld locally; none were uploaded.
