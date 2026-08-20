---
title: "Kernel Equivalence Tests"
generated_at: "2026-07-19 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of KSD and MMD equivalence tests with normal and bootstrap calibration."
source_status: "verified complete local PDF, official full-paper HTML, metadata HTML, and source package inspected; all sources withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-19"
temporal_cutoff: "Sources and repository context inspected through the batch invocation."
primary_url: "https://arxiv.org/abs/2603.10886"
stable_identifier: "arXiv:2603.10886v2; DOI:10.48550/arXiv.2603.10886"
deployment_job_id: "BLAD-2200-20260719-7D93E819"
deployment_item_id: "BLAD-2200-20260719-7D93E819-P04"
confidence_summary: "High for identity, method, theorem and experiment transcription; medium for finite-sample generalization; low for universal equivalence claims."
safety_scope: "offline statistical evaluation, model validation, margin governance, and human-reviewed release gates"
distribution_notes: "No PDF, HTML, source archive, extracted text, cache, dataset, code, or local path is redistributed."
---

# Kernel Equivalence Tests

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Metadata | HTML | arXiv:2603.10886v2 | https://arxiv.org/abs/2603.10886 | CC BY 4.0 link visible; metadata is not full-paper evidence. | 2026-07-19 | Inspected. |
| S2 | Official full-paper rendering | Primary paper | HTML | arXiv:2603.10886v2 | https://arxiv.org/html/2603.10886 | Verified local copy withheld. | 2026-07-19 | Inspected in full. |
| S3 | Paper PDF | Primary paper | PDF | arXiv:2603.10886v2 | https://arxiv.org/pdf/2603.10886 | Verified local copy withheld. | 2026-07-19 | Inspected through extraction. |
| S4 | Paper source package | Primary source | TeX archive | arXiv:2603.10886v2 | https://arxiv.org/e-print/2603.10886 | Package/extraction withheld. | 2026-07-19 | Inspected. |
| S5 | arXiv-issued DOI | Identity | DOI | 10.48550/arXiv.2603.10886 | https://doi.org/10.48550/arXiv.2603.10886 | Persistent locator. | 2026-07-19 | Resolved. |
| S6 | PAC Confidence DEP | Related | Markdown | DEP-E-20260713 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S7 | Noisy Poisson Inference DEP | Related | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S8 | Transport Convexity DEP | Related | Markdown | DEP-E-20260718 | `.lake-data/DEP-E/DEP-E-20260718-Transport Convexity/transport_convexity_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S9 | Selection, repair, cache | Process evidence | Private records | `BLAD-2200-20260719-7D93E819-P04` | Local paths withheld | Integrity/dedup/locality only. | 2026-07-19 | Verified. |

Authors: Xing Liu and Axel Gandy. Submitted 2026-03-11; v2 dated 2026-03-15. Deployment job `BLAD-2200-20260719-7D93E819`; item `BLAD-2200-20260719-7D93E819-P04`.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5 | Metadata | Identity, version, dates, subjects, DOI, license link. | Canonical record. | High | No result validation. |
| E2 | S2-S4 | Complete paper | Four tests, hypotheses, algorithms, theorems, proofs, margin method, experiments, limitations. | Method and evidence. | High for transcription | Not reproduced. |
| E3 | S2-S4 | Formal theory | Pointwise Type-I control, consistency, bootstrap validity, power-margin results. | Conditional guarantees. | High for source report | Mostly asymptotic, not uniform control. |
| E4 | S2-S4 | Experiments | 100-repetition Gaussian, RBM, MNIST studies with CIs. | Calibration/power trade-off. | High for reported figures | No raw data/seed rerun. |
| E5 | S9 | Process | Uniform draw, dedup, repair, byte/marker validation, extraction. | Eligibility/completeness. | High | Private locations withheld. |
| E6 | S6 | Related DEP | Exact binomial intervals and shift assumptions. | Finite-sample bridge. | Medium | Different outcome. |
| E7 | S7 | Related DEP | Asymptotic tests and Type-I misspecification. | Calibration bridge. | Medium | Parametric setting. |
| E8 | S8 | Related DEP | Representation geometry and model mismatch. | Discrepancy-meaning bridge. | Medium | No test calibration. |

## Executive Summary

Goodness-of-fit can reject equality but cannot establish practical sameness by failing to reject. Kernel Equivalence reverses the null: KSD or MMD is at least a margin, versus a smaller discrepancy. Rejecting supports equivalence relative to that kernel and margin while controlling false-equivalence error under stated assumptions.

The paper provides one- and two-sample tests with normal and bootstrap critical values. Normal methods are often more powerful, but experiments show finite-sample Type-I inflation near small margins and high dimension. Bootstrap methods trade power for calibration. A data-driven power-selected margin is offered, yet its scientific meaning remains domain-dependent. No experiment or proof was independently reproduced.

## Detailed Summary

### Hypothesis Logic

Let `D(Q,P)` be a distribution discrepancy and `theta > 0` an equivalence margin. The equivalence null is `D(Q,P) >= theta`; the alternative is `D(Q,P) < theta`. Rejection therefore supports “closer than theta,” not equality. False equivalence is a Type-I error. A standard equality-null test uses the opposite logic and cannot substitute.

### KSD and MMD Roles

KSD is suited to one-sample model assessment when a target density's score is available even if its normalizer is not. MMD is suited to two-sample comparison when both distributions can be sampled. Characteristic kernels make zero discrepancy identify equality under conditions, but practical sensitivity still depends on kernel, bandwidth, data representation, and dimension.

Normal variants use V-statistic central-limit behavior and jackknife variance. Bootstrap variants use metric triangle inequalities and weighted bootstrap samples to create conservative critical values. The theory gives pointwise asymptotic control and consistency. The paper itself notes that uniform control over the composite null would be stronger.

### Margin Design

A domain margin encodes the largest difference considered immaterial. The paper's minimal-effect method instead chooses the smallest margin that reaches a target power against a reference alternative. This is useful for feasibility planning but can be conservative and answers a detectability question. It should not silently define clinical, fairness, safety, or product equivalence.

### Empirical Boundary

All tests use alpha 0.05; experiments repeat 100 times and display 95% intervals. Gaussian mean shifts show normal tests gaining power but losing boundary calibration as the margin shrinks; bootstrap tests remain better calibrated. A 50-dimensional GB-RBM study with 500 samples finds both controlled and the normal test more powerful. A 784-dimensional MNIST mixture shows poor normal Type-I control and better bootstrap calibration. The source contains an apparent KSD/MMD method-name typo in the MNIST discussion; the figures and setting indicate MMD, and this review preserves the inconsistency.

## Key Claims and Evidence

| Claim | Type | Evidence | Assessment | Confidence |
|---|---|---|---|---|
| Reversed discrepancy hypotheses support controlled equivalence claims. | Methodological | E2, E3 | Supported under selected discrepancy/margin. | High |
| Normal KSD/MMD tests are pointwise asymptotically valid/consistent. | Theory | E3 | Source theorem; finite boundary issues remain. | High for report |
| Bootstrap tests improve finite-sample Type-I control in shown regimes. | Empirical/theory | E3, E4 | Supported in figures; often lower power. | Medium-high |
| Power-selected theta supplies a meaningful universal margin. | Overbroad | E2-E4 | Not supported; detectability is not domain significance. | High |
| Passing one test proves two systems interchangeable. | Overbroad | E2 | Not supported beyond kernel/representation/margin/sample. | High |
| Selected source was complete and nonduplicate. | Process | E5 | Verified first draw after repair. | High |

## Methodology

- `Objective`: Full-paper, source-first review of one uniformly selected nonduplicate paper.
- `Sources`: Canonical metadata, verified PDF/HTML/source, extracted representations, private process receipts, three related manuscripts.
- `Discovery`: `rg` enumeration, unique parent units, uniform index, identity resolution, dedup, bounded repair, extraction, conceptual search.
- `Inclusion`: Direct identity, method, theorem, experiment, limitation, process, or calibration/geometry bridge.
- `Exclusion`: Abstract-only inference, unrelated kernel hits, unrun behavior, source files.
- `Analysis`: Statistical, theoretical, empirical, implementation, governance, replication.
- `Evidence handling`: Source claims, empirical plots, reviewer inference, and process claims separated.
- `Uncertainty`: Pointwise/asymptotic scope, finite repetitions, margin semantics, representation choice, typo, nonreproduction explicit.
- `Cross-checking`: Algorithms, theorem statements, figures, conclusion, appendix checked across HTML/source/PDF extraction.
- `Reviewer stance`: Preserve the inferential logic and prevent equivalence overclaiming.

### Random Selection and Deduplication

- 75,778 PDFs; 75,776 units; one-based index 28,880.
- Accepted arXiv:2603.10886v2; exclusions 0; reselections 0.
- Dedup scanned both repositories, automation memory, current job, identifiers, normalized title, slug, artifacts, and cutoff markers.

### Source Integrity and Cache

- Partial to complete in one bounded official-source repair.
- PDF 776,081 bytes with valid header/EOF.
- HTML 981,932 bytes; 172,614 body chars; document marker; 102 headings; eight structure terms; no rejected pattern.
- Unexpected partials 0. Cache `cached`: PDF 118,118 bytes, HTML 172,488, source 202,676.
- All original/extracted sources withheld locally.

## Scope, Constraints, and Assumptions

- `Scope`: Test logic, KSD/MMD estimators, normal/bootstrap calibration, margin design, experiments, implementation governance.
- `Temporal boundary`: arXiv v2 and invocation-time repository context.
- `Evidence limits`: No proof, code, data, or experiment reproduced.
- `Assumptions`: IID sampling, appropriate characteristic kernels, score/moment/sample-size conditions, fixed valid representation, and prespecified test policy.
- `Constraints`: Source locality, dataset licensing, quadratic kernel cost, finite bootstrap/repetition budgets.
- `Out of scope`: Clinical/regulatory certification, fairness equivalence, causal equivalence, live production approval, universal interchangeability.
- `Intended use`: Offline validation, model-update evaluation, margin governance, research preservation.
- `Audience`: Statisticians, ML evaluators, model-risk teams, and release governance.
- `Operational boundary`: A pass is evidence for one defined hypothesis, not an autonomous release authorization.

## Observations

- Failing to reject difference is not evidence of sameness.
- Normal approximation is least trustworthy near degenerate equality boundaries.
- Bootstrap calibration costs power and computation but is more robust in displayed finite samples.
- Pointwise asymptotic control does not imply uniform composite-null control.
- The margin and kernel jointly define the claim.
- The MNIST method-name inconsistency should be corrected by the authors.
- Power-selected margins may be deliberately conservative.

## Considerations

Equivalence claims can affect releases, substitutions, and safety decisions. The domain owner—not the test alone—must define what difference is immaterial. The evaluation team should preregister kernels, representations, margins, alpha, target power, and fallback actions before observing results.

Data reuse for margin selection and final testing can create adaptive bias. Separate design, calibration, and locked test samples where feasible. Multiple kernels, subgroups, tasks, or time windows require multiplicity controls and an explicit aggregation rule.

Quadratic MMD/KSD and bootstrap costs can be substantial. Scaling approximations change the statistic and need their own calibration evidence.

## Strengths

- Corrects a common logical error in model validation.
- Covers one-sample score-based and two-sample sample-based settings.
- Provides both power-oriented normal and calibration-oriented bootstrap methods.
- States pointwise versus uniform-control distinction.
- Makes margin selection an explicit design problem.
- Tests Gaussian, intractable-normalizer RBM, and high-dimensional image settings.
- Reports repeated trials and confidence intervals.

## Weaknesses

- Most guarantees are asymptotic and pointwise.
- Normal tests show finite-sample Type-I inflation in important boundary regimes.
- Bootstrap tests can be conservative and computationally costly.
- Minimal-effect margins lack direct domain interpretation.
- Median-heuristic bandwidth is convenient but not universally optimal.
- Only 100 repetitions limit precision of tail-rate estimates.
- No official code or independent reproduction was established here.
- Apparent KSD/MMD typo reduces presentation clarity.

## Potential Improvements

| Improvement | Target | Rationale | Benefit | Cost/Risk | Validation |
|---|---|---|---|---|---|
| Uniform/finite-sample bounds | Theory | Pointwise limits miss worst nulls | Stronger assurance | Hard analysis | Boundary simulation |
| Domain margin protocol | Governance | Detectability is not significance | Interpretable claims | Expert burden | Preregistered rationale |
| Kernel sensitivity | Robustness | Hypothesis depends on kernel | Exposes blind spots | Multiplicity | Held-out grid/control |
| More repetitions/raw data | Evidence | 100 trials are coarse | Better uncertainty | Compute/storage | Reproducible releases |
| Scalable estimators | Systems | Quadratic/bootstrap cost | Larger samples | Changed asymptotics | Matched calibration |
| Shift/subgroup testing | Deployment | Aggregate equivalence hides strata | Safer release | Sample fragmentation | Hierarchical testing |

## Potential Implementations

1. **Model-update equivalence gate**: locked prompts, old/new outputs, prespecified representation/kernel/margin, bootstrap MMD, subgroup and shift checks, human release approval.
2. **Simulator equivalence workbench**: KSD for score-accessible models, power curves, margin sensitivity, bootstrap/normal comparison, no regulatory claim.
3. **Margin registry**: versioned rationale, owner, metric, representation, target power, alpha, sample plan, expiry, and decision policy.

## Three Ways to Exercise This Research

1. `Gaussian boundary reproduction`: sweep mean shifts and sample sizes; success is nominal Type-I with intervals and power curves; stop on implementation mismatch.
2. `Kernel sensitivity audit`: repeat a two-sample test over preregistered kernels/bandwidths; success is stable decision or documented sensitivity; control multiplicity.
3. `Release-gate shadow run`: compare model versions offline without changing production; success is a complete decision receipt plus human adjudication; stop on dataset shift.

## Example MVP Product

- `Product name`: Equivalence Gate Lab.
- `Target user`: Model evaluation and release-governance teams.
- `Problem`: Teams wrongly treat nonsignificant difference tests as proof of sameness.
- `Workflow`: register hypothesis; approve domain margin; freeze representation/kernel/splits; run normal/bootstrap tests and sensitivity; review subgroup/shift evidence; export signed receipt.
- `Data`: Authorized paired or independent samples, versioned representations, immutable split IDs.
- `Architecture`: Dataset registry, feature adapter, kernel engine, bootstrap runner, margin registry, report UI.
- `Success metrics`: Type-I calibration on fixtures, power, compute, reproducibility, margin/shift coverage.
- `Risk controls`: No automatic release, preregistration, multiplicity, access control, deletion, human approval.
- `Limitations`: Cannot prove semantic, causal, safety, or regulatory equivalence.
- `MVP boundary`: Offline shadow evaluation only.
- `Deployment model`: Local batch tool.
- `Evaluation plan`: Unit tests, Gaussian fixtures, permutation checks, repeated seeds, privacy/governance review.
- `Failure modes`: Leakage, adaptive margins, kernel blindness, shift, dependence, insufficient power, bootstrap instability.
- `Maintenance`: Pin dependencies, version policies, refresh fixtures, expire margins after material changes.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| PAC Confidence | Black Lake DEP-E | Exact finite-sample confidence and shift boundary | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` |
| Noisy Poisson Inference | Black Lake DEP-E | Asymptotic hypothesis calibration under measurement error | `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md` |
| Transport Convexity | Black Lake DEP-E | Representation geometry and model mismatch | `.lake-data/DEP-E/DEP-E-20260718-Transport Convexity/transport_convexity_manuscript.md` |
| MMD two-sample test | Primary predecessor | Kernel mean discrepancy | https://jmlr.org/papers/v13/gretton12a.html |
| Kernelized Stein discrepancy | Primary predecessor | Score-based GOF discrepancy | https://arxiv.org/abs/1602.03253 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2603.10886 | Metadata/identity | 2026-07-19 | Not full paper. |
| R2 | https://arxiv.org/html/2603.10886 | Full method/theory/experiments | 2026-07-19 | Verified source withheld. |
| R3 | https://arxiv.org/pdf/2603.10886 | Cross-format integrity | 2026-07-19 | Withheld. |
| R4 | https://arxiv.org/e-print/2603.10886 | Proof/figure cross-check | 2026-07-19 | Withheld. |
| R5 | https://doi.org/10.48550/arXiv.2603.10886 | Persistent identity | 2026-07-19 | arXiv DOI. |
| R6 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Confidence bridge | 2026-07-19 | Context only. |
| R7 | `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md` | Calibration bridge | 2026-07-19 | Context only. |
| R8 | `.lake-data/DEP-E/DEP-E-20260718-Transport Convexity/transport_convexity_manuscript.md` | Geometry bridge | 2026-07-19 | Context only. |
| R9 | Private process records | Selection/integrity/locality | 2026-07-19 | Paths/files withheld. |

## Appendix

### Selection and Integrity Receipt

- Job `BLAD-2200-20260719-7D93E819`; item `...-P04`.
- 75,776 units; index 28,880; first draw; exclusions/reselections 0.
- Partial to complete; PDF 776,081 bytes; HTML 981,932 bytes and 172,614 body characters; all gates passed.
- Cache `cached`; sources withheld; public source uploads zero.

### Reproduction Checklist

- Pin paper version, kernel, bandwidth, representation, margin, alpha, target power, split, and sample assumptions.
- Separate margin design/calibration from locked final testing.
- Reproduce Gaussian boundary curves with more trials and Monte Carlo intervals.
- Test normal and bootstrap variants at matched samples.
- Preserve raw rejection counts, seeds, bootstrap count, compute, and failures.
- Add dependence, unequal-size, dimension, outlier, and shift stress tests.
- Control multiplicity across kernels, strata, tasks, and windows.
- Report sensitivity rather than one pass/fail result.
- Require domain approval for the margin.
- Never interpret a pass beyond the defined discrepancy and population.
