# Report-Mark: Higher Criticism

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P01`
- Review date: 2026-07-20
- Review type: source-first statistical-methodology review and implementation synthesis

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Higher criticism: $p$-values and criticism* |
| Authors | Jian Li; David Siegmund |
| Stable identifier | arXiv:1411.1437v3 |
| Submission history | Submitted 2014-11-05; revised through v3 on 2015-06-03 |
| Journal | *Annals of Statistics* 43(3), 1323-1350 (2015) |
| Related DOI | https://doi.org/10.1214/15-AOS1312 |
| arXiv DOI | https://doi.org/10.48550/arXiv.1411.1437 |
| Primary record | https://arxiv.org/abs/1411.1437 |
| Verified full-paper HTML | https://ar5iv.labs.arxiv.org/html/1411.1437 |
| PDF | https://arxiv.org/pdf/1411.1437 |
| Source state | Verified complete after bounded ar5iv fallback; all source files withheld locally. |
| Deployment job ID | `BLAD-2200-20260720-8636EDC7` |
| Deployment item ID | `BLAD-2200-20260720-8636EDC7-P01` |

## Concise Research Notes

### Problem

Higher criticism aggregates an excess of small ordered $p$-values to test a global null in sparse-mixture settings. Its asymptotic detection boundary is attractive, but practical use also requires accurate finite-sample significance thresholds and power at the small significance levels created by multiple comparisons. The paper compares original and modified higher-criticism statistics with original and modified Berk-Jones statistics.

### Method

The authors derive analytic approximations for tail probabilities of the four statistics by representing rejection as boundary crossing by uniform order statistics. They compare the approximations with Monte Carlo simulation, develop a hybrid power calculation that combines the approximation with Noe's recursion, and evaluate Gaussian sparse mixtures, lower confidence bounds on the number of false nulls, and copy-number-variation interval scans.

### Evidence and Results

For $n=1000$, significance level 0.01, and Gaussian mixtures, the analytic power calculation and 10,000 simulations agree to two significant figures. At $(\delta,p)=(2.5,0.02)$, reported power is 0.68 for higher criticism and 0.90 for modified Berk-Jones; at $(4,0.005)$ it is 0.89 and 0.87, respectively. Broader simulations show original higher criticism can lead by roughly 5-8 percentage points when the nonnull fraction is extremely small at conventional significance levels, while Berk-Jones variants are usually stronger as the nonnull fraction rises and especially when the significance level becomes very small.

In the interval-scan example, thresholds are calibrated under a global false-positive budget. At global level 0.05, simulated versus analytic thresholds are 20.0 versus 21.5 for HC, 9.3 versus 9.1 for MHC, and 5.98 versus 5.98 for MBJ. The authors caution that approximation quality may change for larger maximum interval lengths. Their simulation uses artificial data shaped like the copy-number-variation application; it is not an independent biological validation.

### Reviewer Interpretation

The transferable result is not that one statistic always wins. Tail emphasis, minimum order-statistic index, significance budget, signal prevalence, and effect size jointly determine power. Original higher criticism protects sensitivity to extremely rare mixtures but pays with unstable thresholds and poor power at stringent multiplicity-adjusted levels. A responsible implementation should therefore publish a sensitivity surface across statistics and tuning choices instead of a single unqualified discovery decision.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limits |
|---|---|---|---|---|
| E1 | Canonical arXiv record and DOI | Identity, authors, versions, journal linkage | High | Metadata is not full-paper evidence. |
| E2 | Verified PDF and full-paper HTML | Definitions, approximations, proofs, simulations, applications, discussion | High for transcription | Proofs were not independently rederived. |
| E3 | Tables 1-2 and Section 3 | Significance approximation and sparse-mixture power comparisons | High for source report | No code or raw simulation output was inspected. |
| E4 | Tables 3-4 and Section 4.1 | Lower confidence-bound comparison | High for source report | Gaussian model and selected configurations bound transfer. |
| E5 | Table 5 and Section 4.2 | Multiple-comparison thresholds and interval-detection power | High for source report | Artificial data; limited repetitions for some comparisons. |
| E6 | Private process records | Randomness, dedup, bounded repair, integrity, locality | High | Local paths and exact execution times withheld. |
| E7 | PAC Confidence DEP | Finite-sample interval construction and calibration boundary | Medium | Classification confidence, not sparse-mixture global testing. |
| E8 | Kernel Equivalence DEP | Hypothesis direction, margin, calibration, and power | Medium | Kernel discrepancy rather than ordered $p$-value aggregation. |
| E9 | Noisy Poisson Inference DEP | Type-I error under model correction and misspecification | Medium | Parametric high-dimensional count regression. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
   - Relevance: both works turn finite samples into auditable probability statements, but PAC Confidence emphasizes interval coverage while higher criticism aggregates evidence across many tests. Together they motivate separating calibration support from the downstream decision budget.
   - Source basis: inspected Clopper-Pearson construction, union-bound use, cascade/safety examples, and distribution-shift limitation.
2. `.lake-data/DEP-E/DEP-E-20260719-Kernel Equivalence/kernel_equivalence_manuscript.md`
   - Relevance: equivalence testing reverses the null to support closeness, whereas higher criticism rejects a global all-null hypothesis. The pair makes the logical direction of a statistical gate explicit and prevents failure-to-reject from being mislabeled as evidence.
   - Source basis: inspected KSD/MMD normal and bootstrap tests, pointwise asymptotic guarantees, power-selected margins, and finite-sample calibration results.
3. `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md`
   - Relevance: corrected Poisson tests show how model misspecification inflates Type-I error; higher criticism shows how tail weighting and multiplicity make nominal thresholds unreliable. Both require simulation stress tests around the intended operating regime.
   - Source basis: inspected corrected objective, Wald/score tests, simulation Type-I results, optimizer assumptions, and reproduction limits.

## Synthesis Note

### Concept Bridge

The three related deposits and this paper form a layered decision receipt. First validate the measurement and calibration model; then specify the hypothesis direction and error budget; then choose an aggregation statistic whose sensitivity matches plausible prevalence and effect sizes; finally report tuning and multiplicity sensitivity. None of the layers converts a statistical rejection into causal, clinical, or production proof.

### Potential Implementations

1. **Sparse-alert ensemble:** compare HC, MHC, BJ, and MBJ on the same locked vector of calibrated $p$-values and flag disagreements for analyst review.
2. **Multiplicity threshold service:** compute and version analytic thresholds, validate them with bounded Monte Carlo at the deployed sample-size/significance regime, and reject unsupported extrapolation.
3. **Signal-prevalence sensitivity report:** publish power curves over nonnull fractions and effect sizes before selecting a production detection rule.

### Deeper Relationship Observations

1. A statistic optimized for the asymptotically rarest regime can lose practical power after a stringent global false-positive budget raises its threshold.
2. Calibration error enters twice: through the individual $p$-values and through the distribution used to threshold their aggregate.
3. Lower confidence bounds on the number of false nulls answer a richer question than global rejection but remain conditional on the aggregation boundary and mixture model.

### Conceptual Similarities

1. Higher Criticism and PAC Confidence attach decisions to explicit probability budgets and finite-sample calibration evidence.
2. Higher Criticism and Kernel Equivalence distinguish the hypothesis actually tested from the stronger conclusion a user may wish to draw.
3. Higher Criticism and Noisy Poisson Inference expose nominal Type-I control as conditional on model, threshold, and operating regime.

### MVP Implementations with Code Mock-Ups

1. **Decision receipt**

```python
def receipt(statistic, threshold, alpha, variant):
    return {"reject_global_null": statistic >= threshold,
            "alpha": alpha, "variant": variant}
```

2. **Method disagreement gate**

```python
def needs_review(decisions):
    return len(set(bool(v) for v in decisions.values())) > 1
```

3. **Calibration boundary**

```python
def can_publish(result, simulation_error, tolerance):
    return bool(result["validated"] and simulation_error <= tolerance)
```

### Developer Challenges

1. Computing extreme tail thresholds accurately without numerical underflow or silently substituting an invalid asymptotic approximation.
2. Preserving one immutable $p$-value vector, multiplicity family, statistic definition, and tuning receipt across comparative runs.
3. Presenting sensitivity and method disagreement clearly enough that a single rejection is not mistaken for localization or effect-size evidence.

### Author Challenges

1. Extending finite-sample validation beyond the selected Gaussian mixtures, sample sizes, and interval-length regimes.
2. Publishing implementation and raw simulation artifacts sufficient for independent numerical reproduction.
3. Characterizing robustness when $p$-values are dependent, discrete, estimated, or misspecified rather than independent uniforms under the global null.

## Validation Notes

- Deployment job `BLAD-2200-20260720-8636EDC7`; item `BLAD-2200-20260720-8636EDC7-P01`.
- Accepted uniform index 16,762 of 75,776 units after one private complete-source-gate rejection; duplicate exclusions 0; reselections 1.
- No duplicate by identifier, DOI, normalized title, slug, artifact markers, memory, companion repository, current job, or 24-hour markers.
- Partial accepted archive repaired to verified complete with approved ar5iv fallback; PDF and full-paper HTML gates passed.
- Full paper, appendix, numerical examples, metadata, and exactly three related manuscripts were inspected; no proof, code, or experiment was rerun.
- Each required Synthesis Note list contains exactly three entries; three Python mock-ups are bounded and parseable.
- Public sanitization passed subject to final scan; `.source/` is absent and no source file is eligible for staging.

## Attribution Block

- https://arxiv.org/abs/1411.1437 - identity, authors, versions, abstract, journal and DOI links.
- https://ar5iv.labs.arxiv.org/html/1411.1437 - verified full-paper method, results, discussion, proofs, tables, and references; local file withheld.
- https://arxiv.org/pdf/1411.1437 - verified cross-format primary paper; local file withheld.
- https://doi.org/10.1214/15-AOS1312 - journal record for the published article.
- https://doi.org/10.48550/arXiv.1411.1437 - persistent arXiv identity.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence - finite-sample confidence synthesis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-Kernel%20Equivalence - hypothesis-direction and calibration synthesis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Noisy%20Poisson%20Inference - misspecification and Type-I synthesis.
- Source files: verified PDF, full-paper HTML, metadata HTML, and private repair records; all withheld locally. Zero source uploads. Job `BLAD-2200-20260720-8636EDC7`, item `BLAD-2200-20260720-8636EDC7-P01`.
