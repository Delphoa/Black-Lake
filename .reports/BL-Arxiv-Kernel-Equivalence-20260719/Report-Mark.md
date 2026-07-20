# Report-Mark: Kernel Equivalence

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P04`
- Review date: 2026-07-19
- Review type: source-first statistical methodology review and implementation synthesis

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Kernel Tests of Equivalence* |
| Authors | Xing Liu; Axel Gandy |
| Stable identifier | arXiv:2603.10886v2 |
| Submission history | Submitted 2026-03-11; revised 2026-03-15 |
| DOI | https://doi.org/10.48550/arXiv.2603.10886 |
| Primary record | https://arxiv.org/abs/2603.10886 |
| Full-paper HTML | https://arxiv.org/html/2603.10886 |
| PDF | https://arxiv.org/pdf/2603.10886 |
| Source package | https://arxiv.org/e-print/2603.10886 |
| License visibility | CC BY 4.0 link visible on arXiv; datasets retain their own terms. |
| Source state | Verified complete after bounded repair; all sources withheld locally. |
| Deployment job ID | `BLAD-2200-20260719-7D93E819` |
| Deployment item ID | `BLAD-2200-20260719-7D93E819-P04` |

## Concise Research Notes

### Problem

A goodness-of-fit test can detect a difference, but failure to reject its equality null can reflect low power. It cannot establish that two distributions are close enough. Equivalence testing reverses the hypotheses: the null says discrepancy is at least a predeclared margin, and rejection supports that the discrepancy is smaller than that margin while controlling the probability of falsely declaring equivalence.

### Method

The paper instantiates the discrepancy with Kernel Stein Discrepancy for one-sample testing, where the nominal density may be known only through its score, and Maximum Mean Discrepancy for two-sample testing, where both distributions are represented by samples. It proposes normal-approximation and bootstrap variants for each: E-KSD-Normal, E-KSD-Boot, E-MMD-Normal, and E-MMD-Boot.

The normal tests use central-limit approximations and jackknife variance estimates. The bootstrap tests use triangle inequalities to derive conservative critical values from weighted bootstrap approximations. Theorems establish pointwise asymptotic Type-I control and consistency under the stated kernel, moment, score, and sample-size assumptions. Pointwise control is explicitly weaker than uniform control over the composite null.

### Margin Selection

The equivalence margin defines the scientific claim, so it should normally come from a domain-specific minimally meaningful difference. The paper also proposes a data-driven minimal-effect construction: select the smallest margin expected to achieve a prespecified power against a reference alternative. This makes a detectable-effect boundary auditable but does not convert it into biological, operational, or policy significance.

### Experiments

Experiments use IMQ kernels for KSD, RBF kernels for MMD, median-heuristic bandwidths, nominal level 0.05, 100 repetitions, and 95% confidence intervals. Gaussian mean-shift studies vary sample size and margin. The normal test is more powerful but can inflate Type-I error near small margins; the bootstrap test is better calibrated but less powerful.

A 50-dimensional Gaussian-Bernoulli RBM experiment uses 500 samples and a power-selected margin targeting 0.8 power. Both methods are reported to control Type-I error in that study, while the normal test is more powerful. An MNIST mixture compares digit 1 with increasing digit-3 contamination in 784 dimensions. The source reports poor normal-test Type-I control and calibrated bootstrap behavior; one paragraph appears to call the MMD bootstrap method “E-KSD-Boot,” an internal naming inconsistency preserved as a likely typo rather than silently corrected evidence.

### Reviewer Interpretation

The most important contribution is logical, not computational: absence of detected difference and evidence of equivalence are different claims. The bootstrap method trades power for finite-sample robustness in the displayed regimes. Yet equivalence remains relative to a chosen kernel, bandwidth, feature representation, margin, sampling design, and Type-I budget. A passed test is not a universal certification that distributions are interchangeable.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limits |
|---|---|---|---|---|
| E1 | Canonical arXiv record/DOI | Identity, authors, version, dates, license link | High | Metadata only. |
| E2 | Verified HTML, PDF, source | Hypotheses, four tests, theorems, proofs, experiments, appendix | High for transcription | Proofs not independently rederived. |
| E3 | Normal-test theorems | Pointwise asymptotic validity and consistency | High for source report | Not uniform finite-sample control. |
| E4 | Bootstrap-test theorems | Conservative asymptotic control and consistency | High for source report | Bootstrap cost and assumptions remain. |
| E5 | Figures 2-6 | Type-I/power trade-offs across three experiment families | High for reported plots | 100 repetitions; no raw results or rerun. |
| E6 | Private process records | Randomness, dedup, repair, integrity, cache | High | Local paths withheld. |
| E7 | PAC Confidence DEP | Exact finite-sample intervals and shift boundary | Medium | Classification confidence, not distribution equivalence. |
| E8 | Noisy Poisson Inference DEP | Asymptotic test calibration and misspecification | Medium | Parametric corrected regression. |
| E9 | Transport Convexity DEP | Distribution representation and geometry dependence | Medium | Transform theorem, not hypothesis testing. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
   - Relevance: PAC Confidence uses exact Clopper-Pearson intervals and a union bound to support finite-sample decisions, then warns that coverage assumes calibration/test distribution identity. Kernel Equivalence supplies a complementary distribution-level test but still requires a meaningful margin and shift-aware interpretation.
   - Source basis: inspected confidence construction, coverage guarantee, cascade/safety uses, and distribution-shift boundary.
2. `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md`
   - Relevance: corrected Wald/score tests show how a misspecified measurement model can destroy Type-I control even when asymptotic theory is available. Kernel Equivalence similarly shows normal approximations can miscalibrate near degenerate boundaries, motivating explicit finite-sample stress tests.
   - Source basis: inspected corrected objective, asymptotic chi-square results, 500-repetition simulations, naive Type-I inflation, and optimization/reproduction limits.
3. `.lake-data/DEP-E/DEP-E-20260718-Transport Convexity/transport_convexity_manuscript.md`
   - Relevance: transport representations make class geometry depend on a specified deformation model. Kernel discrepancies likewise define equivalence only through a chosen representation and kernel; neither distance is scientifically meaningful without a domain mechanism and mismatch audit.
   - Source basis: inspected transform construction, 1D equivalence theorem, multidimensional counterexample, restricted recovery, and generalization boundary.

## Synthesis Note

### Concept Bridge

The related deposits define three layers of a responsible equivalence claim. Transport Convexity asks whether the representation matches the data-generating geometry. Kernel Equivalence asks whether a discrepancy is below a meaningful margin with controlled false-equivalence probability. PAC Confidence and Noisy Poisson Inference ask whether the finite sample, calibration distribution, and measurement model support the nominal error rate. Passing only one layer cannot substitute for the others.

### Potential Implementations

1. **Model-update equivalence gate:** compare old/new output distributions on a locked reference set using MMD equivalence, with domain-owned margins and bootstrap calibration.
2. **Simulator validation harness:** use KSD when a simulator density is available through a score but direct normalized likelihood is not, while reporting power and margin sensitivity.
3. **Margin governance registry:** bind each margin to the kernel, representation, domain rationale, sample design, target power, Type-I rate, version, owner, and expiry.

### Deeper Relationship Observations

1. A data-driven minimal detectable effect answers what the test can resolve, not what stakeholders should consider interchangeable.
2. Degeneracy near exact equality changes estimator asymptotics, explaining why a method can be asymptotically valid pointwise yet unreliable at practical sample sizes near the boundary.
3. Kernel and bandwidth selection are part of the hypothesis itself; changing them changes the discrepancy and therefore the meaning of equivalence.

### Conceptual Similarities

1. Kernel Equivalence and PAC Confidence attach decision rules to explicit error probabilities instead of raw scores.
2. Kernel Equivalence and Noisy Poisson Inference distinguish asymptotic validity from finite-sample Type-I behavior under model assumptions.
3. Kernel Equivalence and Transport Convexity rely on representation geometry to define which differences are visible and meaningful.

### MVP Implementations with Code Mock-Ups

1. **Decision receipt**

```python
def receipt(statistic, critical, margin, alpha, method):
    return {"equivalent": statistic > critical, "margin": margin,
            "alpha": alpha, "method": method}
```

2. **Margin sensitivity grid**

```python
def sensitivity(results, margins):
    return [{"margin": m, "decision": results[m]["reject_null"]} for m in margins]
```

3. **Deployment guard**

```python
def can_deploy(test, domain_margin_approved, shift_check):
    return bool(test["equivalent"] and domain_margin_approved and shift_check["passed"])
```

### Developer Challenges

1. Implementing quadratic kernel statistics and bootstrap replicates without memory blowups, leakage, or inconsistent bandwidth selection.
2. Preserving sample independence, split immutability, representation versions, and randomness receipts across repeated gates.
3. Exposing boundary instability, margin sensitivity, and method naming clearly enough to prevent a single pass/fail number from becoming a universal certificate.

### Author Challenges

1. Establishing uniform or finite-sample control for practical composite-null regimes, especially near zero discrepancy and high dimension.
2. Translating power-selected margins into domain-interpretable biological, operational, or policy tolerances.
3. Expanding experiments with raw results, more repetitions, alternative kernels/bandwidths, unequal samples, computational costs, and independent reproduction.

## Validation Notes

- Job `BLAD-2200-20260719-7D93E819`; item `BLAD-2200-20260719-7D93E819-P04`.
- Uniform index 28,880 of 75,776 units; first draw; exclusions 0; reselections 0.
- No duplicate by identifier, DOI, normalized title, slug, artifacts, memory, companion repository, current job, or 24-hour markers.
- Partial archive repaired to verified complete with official HTML; PDF/HTML/extraction gates passed.
- Full paper, theorems/proofs, algorithms, six figures, appendix, metadata, and exactly three related manuscripts inspected; no proof/experiment rerun.
- Exactly three entries in every required Synthesis Note list; three Python mock-ups parse.
- Public sanitization passed subject to final scan; no `.source/` and no source file eligible for staging.

## Attribution Block

- https://arxiv.org/abs/2603.10886 - identity, authors, version, dates, abstract, subjects, DOI, license locator.
- https://arxiv.org/html/2603.10886 - full method, theory, experiments, conclusion, appendix; verified source withheld.
- https://arxiv.org/pdf/2603.10886 - cross-format verification; source withheld.
- https://arxiv.org/e-print/2603.10886 - theorem/proof/figure cross-checks; source withheld.
- https://doi.org/10.48550/arXiv.2603.10886 - persistent identity.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence - confidence/calibration synthesis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Noisy%20Poisson%20Inference - hypothesis-calibration synthesis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260718-Transport%20Convexity - distribution-geometry synthesis.
- Source files: verified PDF, HTML, metadata, source package, extracted text, and cache; all withheld locally. Zero source uploads. Job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P04`.
