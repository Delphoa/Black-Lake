---
title: "Transport Convexity - DEP-E"
generated_at: "2026-07-18 (date-only public marker; exact execution time and local timezone withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of transport-transform convexification for algebraically generated signal classes."
source_status: "verified complete local PDF and full-paper HTML inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-18"
temporal_cutoff: "arXiv:2008.03452v2 and inspected public records through 2026-07-18"
primary_url: "https://arxiv.org/abs/2008.03452v2"
stable_identifier: "arXiv:2008.03452v2; 10.48550/arXiv.2008.03452; 10.1007/s43670-021-00009-z"
confidence_summary: "High for source identity, theorem transcription, assumptions, and figure descriptions; medium for reviewer interpretation; low for unreported real-world generalization."
safety_scope: "non-sensitive mathematical and signal-processing research"
distribution_notes: "Canonical URLs and repository-relative references only; source documents and local inspection artifacts were not redistributed."
---

# Transport Convexity - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract and version record | Primary metadata | HTML | arXiv:2008.03452v2 | https://arxiv.org/abs/2008.03452v2 | Public metadata; abstract alone was not used for detailed claims. | 2026-07-18 | Inspected |
| S2 | arXiv paper | Primary artifact | PDF | arXiv:2008.03452v2 | https://arxiv.org/pdf/2008.03452 | Twenty-three-page paper inspected locally; not redistributed. | 2026-07-18 | Verified complete and inspected |
| S3 | ar5iv full-paper rendering | Primary artifact fallback | HTML | arXiv:2008.03452 | https://ar5iv.labs.arxiv.org/html/2008.03452 | Approved full-paper fallback; not redistributed. | 2026-07-18 | Verified complete and inspected |
| S4 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2008.03452 | https://doi.org/10.48550/arXiv.2008.03452 | Public DOI locator. | 2026-07-18 | Recorded |
| S5 | Journal article record | Publisher identity | DOI | 10.1007/s43670-021-00009-z | https://doi.org/10.1007/s43670-021-00009-z | Sampling Theory, Signal Processing, and Data Analysis, volume 19, article 6. | 2026-07-18 | Inspected through public metadata/full-text record |
| S6 | PubMed Central article | Public journal full text | HTML | PMCID: PMC9090194 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9090194/ | Used to cross-check publication metadata, theorem descriptions, figures, and conclusions. | 2026-07-18 | Inspected |
| S7 | Physical Data AI | Related DEP | Markdown | DEP-E-20260710-Physical Data AI | `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` | Public derived research artifact; not validation evidence for the selected paper. | 2026-07-18 | Inspected |
| S8 | GPMD Regularized RL | Related DEP | Markdown | DEP-E-20260716-GPMD Regularized RL | `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` | Public derived research artifact; not validation evidence for the selected paper. | 2026-07-18 | Inspected |
| S9 | Learn to Pool | Related DEP | Markdown | DEP-A-20260714-Learn to Pool | `.lake-data/DEP-A/DEP-A-20260714-Learn to Pool/2607.06036-whitepaper-review.md` | Public derived research artifact; not validation evidence for the selected paper. | 2026-07-18 | Inspected |
| S10 | Black Lake repository standards | Repository authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Defines DEP classes, source locality, README, and attribution rules. | 2026-07-18 | Inspected before drafting |
| S11 | Black Lake data standards | Related repository authority | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Used for related-repository and dedup context. | 2026-07-18 | Inspected before drafting |

**Paper:** *Partitioning signal classes using transport transforms for data analysis and machine learning*.

**Authors:** Akram Aldroubi, Shiying Li, and Gustavo K. Rohde.

**History:** arXiv v1 was submitted on 2020-08-08 and v2 was revised on 2021-02-24. The journal record reports acceptance on 2021-04-21 and online publication on 2021-05-11. The reviewed arXiv source describes 23 pages and 6 figures.

**Subjects:** Machine Learning (`cs.LG`), Signal Processing (`eess.SP`), and Machine Learning (`stat.ML`).

**Source locality:** The PDF, full-paper HTML, metadata HTML, e-print source archive, extracted text, hashes, and rendered inspection pages remain local. No source file or derived source cache is present in this DEP.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4-S6 | Primary metadata and publication records | Title, authors, versions, dates, subjects, arXiv DOI, publisher DOI, and venue. | Source identity and publication history. | High | Metadata does not establish theorem validity or application performance. |
| E2 | S2, S3, Sections 1-2 | Primary full text | Definitions of CDT, R-CDT, LOT, the Monge map, signal spaces, and the algebraic generative model. | Problem formulation and mechanism. | High for source transcription | Definitions and proofs were reviewed, not independently rederived from first principles. |
| E3 | S2, S3, Theorem 3.2 and Corollary 3.3 | Primary theorem | Exact 1D relation between convexity of the transformed class and convexity of inverse transformations; group specialization. | Central 1D claim. | High for source report | Depends on compact normalized nonnegative signals and the stated diffeomorphism/transport assumptions. |
| E4 | S2, S3, Proposition 3.5 and examples | Primary theorem/examples | Existence of uncountably many distinct convex subgroups and concrete affine/translation/fixed-point examples. | Richness of the 1D construction. | High for source report | Does not characterize all convex subgroups. |
| E5 | S2, S3, Figures 4-5 | Primary illustrative experiment | Two classes, 500 randomly generated fifth-degree polynomial deformations per class, LDA before and after CDT. | Visual separation illustration. | High for setup and figure description | No numerical classification accuracy, uncertainty, seed, or released reproduction package was identified. |
| E6 | S2, S3, Theorems 4.1-4.4 | Primary theorem | Multidimensional composition condition and the restriction to translations plus isotropic scaling when it must hold for all signals. | Central multidimensional limitation. | High for source report | The strongest restriction follows from requiring the composition property for every signal. |
| E7 | S2, S3, Definition 4.8, Theorem 4.10, Corollary 4.11 | Primary theorem/construction | A restricted 2D signal family and a larger transformation group recover the composition and convexity result. | Conditional relaxation. | High for source report | Restricted construction is not shown to model a concrete measured dataset. |
| E8 | S2, S3, Section 5 | Primary discussion | Linear classification/least-squares implications, extrapolation from limited variations, and enumerated open problems. | Practical interpretation and acknowledged incompleteness. | Medium-high | Implications are conditional; broad deployment evidence is absent. |
| E9 | S7-S9 | Related DEP evidence | Physics-structured embedding, convex optimization geometry, and pooling-aware representation adaptation. | Cross-DEP concept bridge. | Medium | Conceptual overlap does not validate the selected paper. |
| E10 | Selection and local verification records | Process evidence | Uniform draw, duplicate scan, repaired source bundle, byte/structure checks, and no-source-upload gate. | Provenance and review eligibility. | High | Public artifact omits private paths and exact execution time by design. |

## Executive Summary

The paper asks when optimal-transport-derived representations turn deformed signal classes into convex sets. Its starting point is an algebraic generative model: a compact, nonnegative, unit-mass template is acted on by a set of differentiable invertible spatial transformations. The signal is represented by the optimal transport map from a fixed reference distribution. If the resulting class is convex in transform space, estimation can sometimes become linear least squares and disjoint classes can admit linear separation under the relevant geometric conditions.

The strongest result is exact in one dimension. Theorem 3.2 states that, for a transformation set `W`, the CDT-transformed class is convex for every template if and only if the inverse set `W^-1` is convex. When `W` is a group, Corollary 3.3 reduces the condition to convexity of the group itself. The paper supplies translation, positive scaling, increasing affine, and fixed-point subgroups and proves that there are uncountably many distinct convex subgroups.

The multidimensional result is deliberately more restrictive. A composition identity that holds automatically in 1D does not generally hold for LOT when `d >= 2`. If that identity must hold for every admissible signal, Theorem 4.4 confines the transformations to translations and isotropic scaling. The paper then relaxes the universal requirement in two dimensions: for a restricted signal subset it constructs a larger group containing directional stretches and recovers convex transformed classes.

The evidence is theorem-led, not benchmark-led. Figures 4-5 visualize LDA projections for 500 generated signals per class before and after CDT, but the paper reports no classification accuracy, confidence intervals, robustness sweep, or released implementation for that experiment. Confidence is high that this artifact preserves the paper's statements and limits, medium that the proposed geometry is a productive design principle outside the stated models, and low for untested claims about arbitrary real data.

## Detailed Summary

### Problem and Motivation

Many signal and image classes are nonlinear in their native coordinates because observations differ through displacement, scaling, warping, or another mass-transport process. A classifier operating directly on sampled amplitudes must learn this geometry from data. The paper studies a different route: encode each signal by the map that transports a reference distribution into it, then ask whether the transformation family becomes convex in that coordinate system.

The objective is explanatory as much as algorithmic. Prior CDT, R-CDT, and LOT work reported useful classification, morphometry, and estimation behavior. This paper identifies algebraic conditions that make a subset of that behavior predictable. The key promise is not a universally better representation; it is a representation matched to a known transport-like data-generation mechanism.

### Signal and Transform Model

The signal space contains compactly supported, nonnegative functions normalized to unit `L1` mass. A fixed reference signal `r` is chosen. For a target signal `p`, its transform is the unique optimal map that pushes `r` to `p` under the quadratic Monge cost, using the paper's specialization of Brenier's theorem.

In one dimension the optimal map is nondecreasing and is called the cumulative distribution transform (CDT). In multiple dimensions the map is the gradient of a convex potential and is called the linear optimal transport (LOT) transform, despite the transform itself being nonlinear. R-CDT applies the Radon transform and then one-dimensional CDT operations.

The algebraic generative class is formed from a template `p` and transformations `H`:

`S_(p,H) = { |det J_h| (p composed with h) : h in H }`.

This construction preserves mass through the Jacobian determinant. It differs from a probabilistic generative model: `H` is an explicit family of spatial deformations rather than an unknown conditional distribution learned from samples.

### One-Dimensional Result

In 1D, the transport of a generated signal has a useful composition form: the transformed sample is the inverse generating diffeomorphism composed with the transformed template. Convex combinations of transformed samples therefore correspond directly to convex combinations of inverse transformations.

Theorem 3.2 makes this equivalence exact. The transformed class is convex for every template precisely when `W^-1` is convex. For a group, inversion stays inside the group, so the condition becomes convexity of `H`. Proposition 3.1 also shows that a subgroup partitions the signal space into equivalence classes, and Proposition 3.5 establishes that the collection of convex subgroups is uncountably rich.

The practical examples matter because they identify model families that are both mathematically tractable and familiar in sensing: translation for delay, positive scaling for dispersion, increasing affine maps for their combination, and transformations fixed on specified points or intervals. The paper also emphasizes that a useful convex transformation set need not be a group when one template is privileged.

### Illustrative Experiment

Figures 4-5 use one-bump and two-bump templates. Each class contains 500 signals generated by randomly selected fifth-degree polynomials whose coefficients are constrained so the deformed supports remain within the stated interval. LDA projections overlap substantially in signal space and separate visibly after CDT. The figure is consistent with the convexification argument and shows what a simpler decision geometry looks like.

The illustration is not a modern benchmark. The source does not provide numerical error rates, repeated-seed variance, coefficient distributions in machine-readable form, a robustness study, or an official reproduction repository for the paper. It should be treated as a geometric demonstration rather than evidence of general classification superiority.

### Multidimensional Limitation

For `d >= 2`, gradients of convex functions are not closed under arbitrary composition. The 1D identity therefore fails in general. Theorems 4.1-4.3 show how convexity can still follow when the composition property is explicitly satisfied and the inverse transformation set is convex.

Theorem 4.4 supplies the sharp warning: if the composition property is required for all admissible signals, the allowable maps are contained in translations and isotropic scalings. The proof uses Hessian commutation to show the generating convex potential must have a scalar-identity Hessian. This result turns a vague caveat into a structural boundary—the useful global family in higher dimensions is far smaller than the 1D family.

### Restricted Two-Dimensional Relaxation

The paper next restricts the signal family instead of demanding the identity globally. It constructs transformations from convex potentials of the form `f(x+y) + g(x-y)`, with strictly increasing derivative conditions. The group includes translations, isotropic scaling, and stretching along the diagonal directions. For signals generated inside the associated restricted set, Theorem 4.10 restores the composition relation and Corollary 4.11 restores the convexity equivalence for convex subgroups.

This relaxation is mathematically constructive but empirically open. The source does not connect the restricted set to a named real dataset or quantify how close measured signals must be to the model for useful approximate convexity.

### Conclusions and Open Boundary

The paper suggests that convex combinations in transform space can expand a class model beyond limited observed translations or scalings. It also lists unresolved questions: characterize 1D convex subgroups; understand the geometry of their partitions; find multidimensional convexity conditions that do not require the composition identity; construct useful higher-dimensional restricted groups; and allow multiple templates or non-group transformation sets.

Those questions define the correct engineering stance. A system should not infer convexity from the existence of an optimal transport map. It should specify a transformation hypothesis, audit whether samples obey it, quantify convexity and class separation after transformation, and measure degradation under model mismatch.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | In 1D, the transformed class is convex for every template if and only if the inverse transformation set is convex. | Author theorem | E3 | This is the paper's exact central result under the stated CDT and generative assumptions. | High for source report |
| C2 | A convex subgroup partitions the 1D transform space into convex equivalence classes, and there are uncountably many such subgroups. | Author theorem | E3, E4 | Supported by Proposition 3.1, Corollary 3.3, Proposition 3.5, and examples. | High for source report |
| C3 | Requiring the multidimensional composition property for every signal restricts the transformation family to translations and isotropic scaling. | Author theorem | E6 | A strong limitation, not a claim that other families can never yield convexity by another argument. | High for source report |
| C4 | Restricting the 2D signal family admits a larger group with directional stretching while preserving the composition/convexity result. | Author theorem/construction | E7 | Mathematically supported in the constructed family; application relevance remains untested. | High for source report, medium for practical relevance |
| C5 | Transport-domain convexity can simplify classification and estimation. | Author implication | E3, E5, E8 | Geometrically plausible and illustrated, but practical benefit is conditional on disjointness, model fit, sampling, and algorithmic details. | Medium |
| C6 | CDT makes the paper's two generated classes easier to separate. | Author illustrative claim | E5 | The rendered figure shows strong visual LDA separation for the stated samples; no numeric generalization estimate is supplied. | Medium |
| C7 | The paper establishes broad real-world superiority over neural classifiers. | Unsupported generalization | E5, E8 | It does not. Prior application results are contextual citations, and this paper's new empirical evidence is limited. | High |
| C8 | Generative-model audits should precede claims that a representation will simplify a task. | Reviewer interpretation | E2, E6-E9 | This follows from the sharp 1D/multidimensional contrast and the related DEP evidence. | Medium-high |

## Methodology

- `Research objective`: Preserve the selected paper's mechanism, theorems, illustrative evidence, boundary conditions, and implementation relevance as a schema-complete DEP-E artifact.
- `Sources inspected`: Verified v2 PDF, verified full-paper HTML, arXiv metadata, e-print provenance, public journal/PMC full text, seven rendered PDF pages, live repository READMEs, publication index, automation memory, and exactly three related DEP artifacts.
- `Discovery strategy`: Enumerated local PDFs with `rg --files -g "*.pdf"`, grouped candidates by unique PDF parent, uniformly selected a zero-based index with PowerShell `Get-Random`, derived identity from adjacent metadata, and scanned stable identifiers/title/slug across dedup stores before review.
- `Inclusion criteria`: Evidence had to identify the work, expose full definitions/proofs/figures/limitations, establish source integrity or repository rules, or provide concrete overlap in structured representation geometry and convex simplification.
- `Exclusion criteria`: Abstract-only material was excluded from theorem and empirical support. Secondary result aggregators, generic recommendation widgets, and unverified repositories were not treated as evidence. Source files were excluded from public outputs.
- `Analytical approach`: Conceptual, mathematical/theorem-oriented, comparative, implementation, product research, and replication analysis.
- `Evidence handling`: Major claims map to evidence IDs. Author theorems, illustrative evidence, reviewer interpretation, unsupported generalization, and related-DEP synthesis are labeled separately.
- `Uncertainty handling`: Proofs were inspected but not formally verified; application generality, approximate model fit, and experiment reproducibility remain explicit gaps.
- `Extraction process`: Extracted all 23 PDF pages locally, read full HTML sections, inspected theorem statements and proof outlines, cross-checked public journal text, and visually reviewed title, key figures, multidimensional construction, and conclusions.
- `Version control`: The paper is pinned to arXiv v2; publisher identity is pinned by DOI; repository authority was read from the live default branches.
- `Claim selection`: Prioritized the exact 1D criterion, subgroup structure, multidimensional restriction, 2D relaxation, the only in-paper experiment, practical implications, and open questions.
- `Cross-checking`: Compared PDF text, full HTML, metadata, journal full text, figure captions, and source-integrity metrics. No numerical experiment was rerun.
- `Reviewer stance`: Source-grounded summary, critique, replication planning, product translation, and DEP-ready preservation.
- `Random selection`: `rg` found 75,777 PDFs and 75,776 unique PDF-parent units. Uniform `Get-Random` selection returned zero-based index 22,992.
- `Deduplication and reselection validation`: arXiv ID, arXiv DOI, publisher DOI, normalized title, and slug were checked in Black Lake logs/reports/lake-data/staging, automation memory, relevant Black-Lake-Data search results, and same-paper markers within 24 hours. Duplicate exclusions were 0; other exclusions were 0; reselections were 0.
- `Source-integrity repair`: Initial state was partial because full-paper HTML and provenance records were missing. The existing valid PDF was preserved. Metadata HTML, source package, and approved ar5iv full-paper HTML were collected with bounded direct HTTPS. Final verification passed all PDF and HTML gates with no partial files.

## Scope, Constraints, and Assumptions

- `Scope`: The definitions, theorem structure, illustrative experiment, practical consequences, limitations, and research-to-product implications of arXiv:2008.03452v2.
- `Temporal boundary`: Paper v2 revised 2021-02-24; public source and repository context inspected through 2026-07-18.
- `Evidence limits`: Proofs were not machine-checked; the synthetic experiment was not rerun; no official paper-specific code package was identified; no real dataset is evaluated by the paper's new experiment.
- `Assumptions`: Signals are compactly supported, nonnegative, normalized densities; transport maps and diffeomorphisms meet the paper's regularity; the algebraic generative model describes the class; and the selected reference supports the transform construction.
- `Constraints`: Local source confidentiality, source non-redistribution, public-path sanitization, finite review time, and no external dataset or code download.
- `Out of scope`: Formal proof verification, production optimal-transport solver benchmarking, clinical or safety-critical deployment, and claims about current state of the art.
- `Intended use`: Research review, DEP deposition, replication planning, geometry-audit design, and bounded MVP ideation.
- `Audience`: Signal-processing researchers, optimal-transport practitioners, representation-learning engineers, and reviewers evaluating geometry-driven classifiers.
- `Depth target`: Full manuscript report with explicit evidence and implementation boundaries.
- `Reproducibility boundary`: The paper and its source expose equations, examples, and figure descriptions, but exact experiment code, seeds, and machine-readable polynomial samples were not established.
- `Operational boundary`: Proposed implementations are offline, synthetic-first, diagnostic, and non-consequential until model-fit and robustness gates pass.
- `Data sensitivity`: Public research documents; any future face, medical, or sensor data require separate consent, license, privacy, and bias review.

## Observations

- `Observed pattern`: The strongest result is a representation theorem. The useful classifier is downstream of a geometric condition; it is not learned end to end by this paper.
- `Observed pattern`: One dimension is exceptional because monotone maps compose compatibly. Higher-dimensional gradients of convex potentials do not retain that closure in general.
- `Technical implication`: A practical system needs a model-fit test for mass preservation, transformation family membership, reference sensitivity, and approximate convexity before trusting a linear head.
- `Evidence-quality implication`: Visual class separation is a useful sanity check but cannot replace accuracy, margin, convex-hull overlap, repeated seeds, and out-of-model stress tests.
- `Contradiction or tension`: The representation can simplify geometry while still requiring an expensive or unstable optimal transport computation, so statistical simplicity does not guarantee systems efficiency.
- `Reviewer hypothesis`: Approximate convexity metrics may be more useful than binary theorem membership for real data, provided they are paired with held-out performance and counterexample generation.

## Considerations

Reference selection can materially change numerical conditioning and geometry even when the theorem is stated relative to a fixed reference. A deployment should compare multiple references, log solver convergence, and separate transport-solver error from downstream classifier error.

Real observations rarely satisfy exact unit mass, positivity, compact support, diffeomorphism, or single-template assumptions. Preprocessing that clips negative values or renormalizes mass can itself remove information. Any benchmark should report the transform applied to raw measurements, the amount of discarded/renormalized signal, and performance under missing mass, noise, occlusion, topology change, and noninvertible deformation.

Convexity also does not automatically deliver a usable margin. Finite samples may look separated while their class hulls overlap under new transformations. Evaluation should include held-out hull violations, margin distributions, calibration, solver failures, and comparisons with native-space linear and nonlinear baselines.

If images of people, cells, or medical tissue are used, the transform does not remove privacy, consent, bias, or regulatory obligations. The MVP below therefore uses synthetic one-dimensional densities and aggregate metrics only.

## Strengths

- The paper gives a precise condition rather than attributing empirical success vaguely to optimal transport.
- It distinguishes the exceptional 1D setting from the much narrower universal higher-dimensional setting.
- The algebraic generative model makes the representation hypothesis inspectable and falsifiable.
- The theorem-to-application bridge is intuitive: convex transformed classes support simpler estimation and separation methods.
- Concrete convex subgroup examples connect abstract structure to time delay, dispersion, affine deformation, and fixed regions.
- The 2D relaxation demonstrates how restricting the data family can recover a richer transformation family.
- The open-question section is unusually useful for planning follow-on mathematical and engineering work.

## Weaknesses

- The paper's new empirical evidence is a single synthetic visual demonstration without numerical generalization metrics.
- Exact generative assumptions are strong and no approximate-model theorem quantifies graceful degradation.
- No official paper-specific reproduction package was identified from the inspected primary and author records.
- The effect of reference choice, discretization, transport solver, sampling density, and numerical error is not evaluated.
- The multidimensional relaxation is not connected to a concrete physical dataset.
- Claims about simpler classification rely on additional separation and finite-sample conditions that deserve explicit measurement.
- The paper does not compare end-to-end compute, memory, or latency against nonlinear native-space models.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release a deterministic reproduction package | Reproducibility | Figures 4-5 lack machine-readable samples, seeds, and code. | Independent theorem illustration and regression tests. | Maintenance and dependency work. | Recreate signals, CDT, LDA, and figures from a pinned environment. |
| Add quantitative geometry metrics | Evidence | Visual separation does not measure margin or hull overlap. | Clearer link from theorem to finite data. | Metric choice can mislead in high dimensions. | Report linear accuracy, margins, hull violations, and bootstrap intervals. |
| Stress model mismatch | Robustness | Real signals violate exact deformation and mass assumptions. | Practical applicability boundary. | Large scenario matrix. | Sweep noise, missing mass, noninvertible warps, mixed templates, and topology changes. |
| Analyze approximate convexity | Theory | Binary membership is too strict for measured data. | Graceful-degradation guarantees. | New mathematical machinery. | Bound transformed hull error and downstream excess risk under perturbations. |
| Evaluate reference sensitivity | Numerical method | Transport coordinates depend on a reference and solver. | More reliable implementations. | Extra computations. | Compare barycentric, class-template, and fixed references with solver diagnostics. |
| Extend multidimensional examples | Method/application | The 2D restricted group lacks a named dataset. | Test whether the relaxation transfers. | Requires domain-specific modeling. | Fit transformations to controlled images or synthetic PDE-generated fields. |

## Potential Implementations

1. **Transform-geometry audit library.** `User`: signal-processing researcher. `Goal`: test whether a candidate dataset becomes approximately convex and linearly separable under CDT/R-CDT/LOT. `Core mechanism`: normalize approved signals, compute a versioned transport transform, compare native/transformed hull and margin metrics, and run mismatch sweeps. `Required inputs`: synthetic or authorized signals, class labels, explicit reference, solver configuration. `Outputs`: evidence card, plots, failure cases, and reproducibility manifest. `Risk controls`: local-only data, no raw-example export by default, solver-failure flags, and no deployment recommendation without held-out gates. `Evaluation`: reconstruction error, margin, hull violation, linear accuracy, runtime, and sensitivity.
2. **Transport-aware template estimator.** `User`: radar or acoustic engineer. `Goal`: estimate delay and low-order dispersion without a nonlinear native-space search. `Core mechanism`: use CDT coordinates, fit a bounded linear subspace of inverse transformations, invert only validated estimates, and compare against a classical estimator. `Required inputs`: positive normalized waveforms, calibration reference, authorized parameter ranges. `Outputs`: parameter estimate, residual, confidence/validity flags. `Risk controls`: reject negative/missing-mass inputs, bound extrapolation, and retain a classical fallback. `Evaluation`: parameter error, coverage, runtime, and failure rate under noise/model mismatch.
3. **Generative-assumption gate for linear heads.** `User`: ML reviewer or model-risk team. `Goal`: prevent unsupported claims that a representation makes a class easy. `Core mechanism`: register the claimed transformation family, generate counterexamples outside it, compare native and transformed linear heads, and require quantitative convexity/margin evidence. `Required inputs`: representation function, transformation sampler, labeled validation set, declared assumptions. `Outputs`: pass/conditional/fail decision with counterexamples. `Risk controls`: synthetic-first operation, no automatic production rollout, subgroup and domain checks, and explicit uncertainty. `Evaluation`: false assurance rate, counterexample discovery, calibration, and held-out performance.

## Three Ways to Exercise This Research

1. **Reproduce the 1D geometry:** Objective: rebuild the one-bump/two-bump illustration. Inputs: two synthetic unit-mass templates and a bounded monotone polynomial sampler. Method: compute CDT features, native/transformed LDA, margins, and hull-overlap estimates across fixed seeds. Output: a reproducible evidence card. Success criterion: transformed separation improves consistently without violating the sampler constraints. Stop condition: any invalid density, nonmonotone map, solver failure, or unsupported extrapolation.
2. **Break the assumptions deliberately:** Objective: measure how benefit degrades. Inputs: the same synthetic classes plus controlled noise, mass deletion, mixed templates, and noninvertible warps. Method: sweep one violation at a time and record transform validity, reconstruction, hull violations, and linear accuracy. Output: an assumption-to-failure map. Success criterion: a stable boundary where diagnostics warn before performance collapses. Stop condition: diagnostics cannot distinguish valid from invalid cases.
3. **Probe a restricted 2D family:** Objective: test the construction around diagonal stretches. Inputs: synthetic 2D densities generated only by the paper's admissible potential family. Method: compute LOT with a fixed solver, compare valid-group and off-group transformations, and fit a linear head. Output: a theorem-aligned benchmark and counterexample set. Success criterion: valid cases exhibit lower hull violation than matched off-group cases. Stop condition: solver error is comparable to the observed geometry effect.

## Example MVP Product

- `Product name`: Convexity Gate.
- `Target user`: Signal-processing researcher or representation-learning reviewer.
- `Problem`: Teams often claim that a transform simplifies a dataset without recording the assumptions, solver behavior, or finite-sample geometry that would support the claim.
- `Core workflow`: Import synthetic or authorized nonnegative signals; validate mass/support; declare a transformation family and reference; compute native/CDT features; train matched linear probes; estimate margins and convex-hull violations; generate controlled assumption failures; export a public-safe evidence card.
- `Data requirements`: Synthetic signals by default; optional authorized local datasets with labels, provenance, and retention rules. No raw private signal leaves the local environment.
- `Architecture`: Local Python CLI; validated input adapter; transport backend; geometry metrics; matched linear-probe runner; mismatch generator; Markdown/JSON report renderer.
- `Success metrics`: Deterministic reruns; zero silent solver failures; accurate input-validity checks; stable margin/hull estimates; transparent runtime; counterexamples found before unsupported deployment claims.
- `Risk controls`: Local-only processing, synthetic default, raw-data redaction, bounded solvers, finite parameter ranges, explicit invalid state, no automated production recommendation, and source/version ledger.
- `Limitations`: Finite-sample hull metrics are expensive and reference-sensitive; passing the audit does not prove theorem assumptions or real-world safety; multiple templates and topology changes require extensions.
- `MVP boundary`: 1D CDT, two classes, synthetic inputs, fixed-seed linear probes, and offline reports only. R-CDT/LOT and real data remain post-MVP.
- `Deployment model`: Local CLI or notebook in an authorized research environment.
- `Evaluation plan`: Unit tests for normalization/monotonicity, golden synthetic transformations, invalid-input tests, solver-failure injection, repeated-seed geometry estimates, and native/transformed matched baselines.
- `Failure modes`: False convexity from sparse samples, distorted signals after renormalization, reference sensitivity, unstable transport solver, label leakage, and overinterpreted visual plots.
- `Maintenance plan`: Pin solver/library versions, retain synthetic goldens, version transformation registries, and rerun evidence cards after dependency or metric changes.

Illustrative bounded core:

```python
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class SignalCheck:
    valid: bool
    reason: str

def validate_density(x: np.ndarray, y: np.ndarray) -> SignalCheck:
    if x.ndim != 1 or y.shape != x.shape or len(x) < 8:
        return SignalCheck(False, "shape")
    if not np.all(np.diff(x) > 0) or np.any(~np.isfinite(y)):
        return SignalCheck(False, "grid-or-finite")
    if np.min(y) < 0:
        return SignalCheck(False, "negative-mass")
    mass = np.trapezoid(y, x)
    if not np.isfinite(mass) or mass <= 1e-12:
        return SignalCheck(False, "zero-mass")
    if abs(mass - 1.0) > 1e-3:
        return SignalCheck(False, "not-unit-mass")
    return SignalCheck(True, "ok")
```

Dependencies are NumPy only for this validation fragment. It deliberately refuses to normalize silently; a separate, logged preprocessing step must explain any mass change. A production transform backend would require numerical tests, solver diagnostics, privacy review, and comparison with trusted optimal-transport implementations.

## Related Research and Reading

### Primary and Near-Primary Research

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| *The Cumulative Distribution Transform and Linear Pattern Classification* | Foundational CDT paper | Introduces CDT properties and linear classification conditions used by the reviewed work. | https://arxiv.org/abs/1507.05936 |
| *Radon cumulative distribution transform subspace modeling for image classification* | Applied R-CDT paper | Uses R-CDT geometry and nearest-subspace classification; provides an implementation-oriented neighbor. | https://arxiv.org/abs/2004.03669 |
| *Linear Optimal Transport Embedding: Provable Wasserstein classification for certain rigid transformations and perturbations* | Concurrent/related theory | Studies LOT embeddings and linear separability for structured distribution families in arbitrary dimension. | https://arxiv.org/abs/2008.09165 |
| *Linear Optimal Partial Transport Embedding* | Follow-on method | Relaxes balanced-mass requirements through partial transport, relevant to a major boundary of the reviewed model. | https://arxiv.org/abs/2302.03232 |

### Related Black Lake DEP Entries - Exactly Three

| Entry | Concrete overlap | Source basis |
|---|---|---|
| `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` | A physics-structured nonlinear transform produces compact features for a linear classifier; both works depend on matching representation structure to physical/data-generation assumptions. | Review of arXiv:2407.14504v3 and its NSN experiments/ablations. |
| `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` | Convex regularizer geometry and generalized Bregman updates simplify an otherwise difficult optimization; both works derive algorithmic simplicity from explicit convex structure. | Review of arXiv:2105.11066v4, SIAM DOI 10.1137/21M1456789, theorem and toy-experiment evidence. |
| `.lake-data/DEP-A/DEP-A-20260714-Learn to Pool/2607.06036-whitepaper-review.md` | Pooling-aware fine-tuning changes representation geometry so averaging preserves retrieval performance; it is an empirical example of reshaping coordinates to make a simpler downstream operator viable. | Full review of arXiv:2607.06036v1, pooling methods, NanoBEIR/BEIR results, and controls. |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2008.03452v2 | Identity, version history, authors, abstract, categories, source links. | 2026-07-18 | Primary metadata. |
| R2 | https://arxiv.org/pdf/2008.03452 | Full definitions, theorems, proofs, figures, limitations, and references. | 2026-07-18 | Verified complete local copy inspected; withheld. |
| R3 | https://ar5iv.labs.arxiv.org/html/2008.03452 | Searchable full-paper structure and equation/section cross-checks. | 2026-07-18 | Verified fallback local copy inspected; withheld. |
| R4 | https://doi.org/10.48550/arXiv.2008.03452 | Persistent arXiv identity. | 2026-07-18 | Identifier only. |
| R5 | https://doi.org/10.1007/s43670-021-00009-z | Journal identity and publisher metadata. | 2026-07-18 | Publisher record. |
| R6 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9090194/ | Public journal full text, figures, theorem descriptions, and publication context. | 2026-07-18 | Cross-check source. |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md | Related physics-structured representation artifact. | 2026-07-18 | Related DEP only. |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md | Related convex optimization geometry artifact. | 2026-07-18 | Related DEP only. |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-Learn%20to%20Pool/2607.06036-whitepaper-review.md | Related representation-adaptation artifact. | 2026-07-18 | Related DEP only. |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public deposition, source-locality, and attribution rules. | 2026-07-18 | Process authority. |
| R11 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository and dedup context. | 2026-07-18 | Process authority. |

## Appendix

### Source-Integrity Verification

- Initial classification: partial; valid PDF present, full-paper HTML and companion records absent.
- PDF gate: 1,325,592 bytes; `%PDF-` header present; trailing `%%EOF` present.
- Official arXiv full-paper HTML: unavailable at the inspected endpoint for this identifier.
- Approved fallback: ar5iv full-paper HTML.
- HTML gate: 1,688,145 bytes; 130,640 body characters after script/style/tag removal; document marker present; 109 section/heading markers; seven structure-term classes; no error, abstract-only, or conversion notice.
- Companion repair: metadata HTML and arXiv e-print source archive collected; README, attribution record, machine-readable summary, and verification report updated locally.
- Final classification: complete; zero partial files.
- Review set: all 23 PDF pages extracted; pages 1, 3, 4, 12, 17, 20, and 21 rendered and visually inspected.
- Public gate: no source document, archive, cache, extracted text, render, local path, username, machine name, timezone label, or exact execution timestamp is included.

### Replication Checklist

- [ ] Pin arXiv v2 and record file hashes without redistributing the source.
- [ ] Recreate the two synthetic templates and constrained fifth-degree transformation sampler.
- [ ] Validate monotonicity, invertibility, support, nonnegativity, and unit mass before transformation.
- [ ] Pin the reference density, discretization, CDT implementation, LDA implementation, and random seeds.
- [ ] Report native/transformed linear accuracy, margin distributions, hull violations, and bootstrap intervals.
- [ ] Sweep noise, missing mass, multiple templates, and off-family transformations.
- [ ] Log runtime, memory, solver convergence, reconstruction error, and every rejected sample.
- [ ] Publish code/configs and derived numeric outputs only after licensing, privacy, and source-locality review.

### Selection and Submission Checklist

- Uniform random selection from 75,776 unique PDF-parent units: pass.
- Stable-ID/title/slug dedup and 24-hour same-paper check: pass.
- First draw accepted; zero exclusions and zero reselections: pass.
- Exactly three related DEP entries inspected and attributed: pass.
- Source-first full paper review, not abstract-only synthesis: pass.
- No `.source/` directory and no source upload: required and enforced.
