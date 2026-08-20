---
title: "Causal DP Workloads - DEP-E"
generated_at: "2026-07-22T00:04:16Z"
artifact_type: "DEP research artifact"
primary_subject: "An iterative source-first expansion of workload-preserving differentially private synthetic data for causal inference."
source_status: "Repository files and public URLs; the selected paper was inspected in full through its public v2 HTML and official code repository."
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-22"
temporal_cutoff: "2026-07-22"
primary_url: "https://arxiv.org/abs/2607.08122v2"
stable_identifier: "DEP-20260712-Tech Intel 1100 / arXiv:2607.08122v2"
confidence_summary: "High for source identity, mechanism, reported tables, and code structure; medium for comparative conclusions because experiments were not rerun and key generic baselines are simplified implementations."
safety_scope: "Public research review; defensive privacy and evaluation framing; no confidential records or executable datasets deposited."
distribution_notes: "No paper PDF, benchmark data, or repository files were redistributed; public URLs, commit pins, and repository-relative provenance are preserved."
---

# Causal DP Workloads - DEP-E

## Source Metadata

| ID | Source | Authors / Organization | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|---|
| S0 | DEP-20260712-Tech Intel 1100 | Delphoa-Labs | Selected source bundle | Repository DEP | Commit `e09ab977` | [Source DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/e09ab977fedb25f03690b731d751ab93d4ede947/.lake-data/DEP-20260712-Tech%20Intel%201100) | Public repository evidence; attribution retained | 2026-07-22 | README, digest, and both prior Report-Marks inspected |
| S1 | BL-DEP-20260712-Tech Intel 1100-20260716 | Codex | Latest prior processing report | Markdown | 2026-07-16 report | [Prior report](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/e09ab977fedb25f03690b731d751ab93d4ede947/.reports/BL-DEP-20260712-Tech%20Intel%201100-20260716/README.md) | Public repository evidence | 2026-07-22 | Inspected before expansion |
| S2 | Black-Lake processing log | Codex | Latest prior operational record | Markdown | 2026-07-16 log | [Prior log](https://github.com/Delphoa/Black-Lake/blob/b8f1fc50c914447de0b7818ff427e55d2dbaee2e/.logs/20260716-DEP-20260712-Tech%20Intel%201100-LOG.md) | Public repository evidence | 2026-07-22 | Inspected before expansion |
| S3 | BL-DEP-Mark002 Report-Mark | Codex | Latest preserved research sections | Markdown | Mark 002 | [Prior Report-Mark](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/e09ab977fedb25f03690b731d751ab93d4ede947/.lake-data/DEP-20260712-Tech%20Intel%201100/BL-DEP-Mark002%20Report-Mark.md) | Public repository evidence | 2026-07-22 | Inspected; supplied the bounded expansion graph |
| S4 | Contravariance Study - DEP-E | Codex | Latest prior DEP Class manuscript | Markdown research artifact | Commit `b8f1fc5` | [Prior manuscript](https://github.com/Delphoa/Black-Lake/blob/b8f1fc50c914447de0b7818ff427e55d2dbaee2e/.lake-data/DEP-E/DEP-E-20260716-Contravariance%20Study/contravariance-study.md) | Public derived artifact | 2026-07-22 | Inspected; carried arXiv:2607.08122 as an unexpanded thread |
| S5 | Workload-Preserving Differentially Private Synthetic Data for Causal Inference via Maximum-Entropy Calibration | Amir Asiaee; Kaveh Aryan | Randomly selected expansion source | Primary research preprint | arXiv:2607.08122v2; revised 2026-07-17 | https://arxiv.org/abs/2607.08122v2 | CC BY 4.0 shown by the arXiv HTML record; UAI 2026 acceptance is an author-record claim | 2026-07-22 | Canonical metadata, revision history, abstract, and license link inspected |
| S6 | Workload-Preserving Differentially Private Synthetic Data, full paper | Amir Asiaee; Kaveh Aryan | Primary method, theorem, experiment, and limitation evidence | HTML manuscript | arXiv:2607.08122v2 | https://arxiv.org/html/2607.08122v2 | Public primary text; not deposited | 2026-07-22 | Complete HTML, including appendices, inspected |
| S7 | Causal-AIM official implementation | AsiaeeLab | Official implementation and reproduction context | Git repository | Commit `cdfa667b22d217e131d3dc3dd0c1863a2cd3e44f` | [Pinned repository](https://github.com/AsiaeeLab/causal-aim/tree/cdfa667b22d217e131d3dc3dd0c1863a2cd3e44f) | MIT; no datasets included | 2026-07-22 | README, license, data guide, notebook guide, file inventory, and core implementation map inspected |

No external paper, dataset, notebook, or code file was deposited. A temporary source-first inspection checkout was used only to verify the public implementation at the pinned commit.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S0 | Source DEP | Original ten-item digest and attribution | The selected DEP originally framed arXiv:2607.08122 as workload-preserving DP synthetic data for causal inference | High | Original description predates v2 and is concise |
| E2 | S1-S4 | Prior repository material | Latest report, log, Report-Mark, and manuscript | Prior passes preserved this thread; Contravariance, not causal DP, was the latest full expansion | High | Prior artifacts were not independent replication studies |
| E3 | S5-S6 | Primary paper | Revision history, abstract, Sections 1-4 | The release targets treatment-arm feature masses and outcome-feature moments used by orthogonal causal scores | High | Source claim and formal design; not a uniqueness or minimax result |
| E4 | S6 | Primary paper | Sections 4-6 and Appendices C-G | One noisy workload supports a direct moment-map route or maximum-entropy synthetic reconstruction; NA+MI propagates Gaussian-mechanism uncertainty | High | Theory is narrower than arbitrary downstream learners on sampled rows |
| E5 | S6 | Primary paper | Theorems 1-3 and Appendix E | Reported ATE error separates sampling, privacy, approximation, synthetic Monte Carlo, and calibration contributions | High | Constants may be loose; assumptions include unconfoundedness, positivity, boundedness, and estimator stability |
| E6 | S6 | Primary paper | Table 1 and Section 7.2 | At the table's reported setting, Causal + NA+MI reports coverage 0.998, 1.000, 1.000, and 1.000 across IHDP, Twins, ACIC, and LaLonde while naive private methods under-cover | High for transcription | Experiments were not rerun; exact math symbols in experimental settings are imperfectly rendered in HTML |
| E7 | S6 | Primary paper | Sections 7-8 and Appendix L | Generic workloads often lead point RMSE at looser privacy budgets, whereas causal workloads plus NA+MI prioritize calibrated intervals and may become approximation-limited as privacy noise shrinks | High | Dataset- and operating-point-specific; no universal dominance |
| E8 | S7 | Official repository | README, `DATA.md`, notebooks guide, requirements, run manifest description | The repo provides an end-to-end reproduction route, public benchmark provenance, code-to-paper mapping, and configuration/code-hash manifests | High | Dependencies use version ranges, data are external, ACIC needs R, and no tests are present in the inspected tree |
| E9 | S7 | Official repository | `baselines.py` and `maxent.py` function map | The code labels the MST comparator a simple MST-style product baseline rather than the official Private-PGM implementation; max-entropy reconstruction is a product-style approximation | High | Static inspection only; no execution or numerical comparison performed |
| E10 | S6-S7 | Cross-source reviewer analysis | Paper claims compared with implementation scope | Reported uncertainty-calibration evidence is useful, but baseline labels and solver scope must travel with any comparative conclusion | Medium-High | Derived interpretation; a reproduction and official-baseline rerun could change the assessment |

## Executive Summary

This iterative pass randomly selected arXiv:2607.08122 from the nine primary research threads that remained unexpanded after the prior Contravariance review. The current source is v2, revised on 2026-07-17, and therefore adds a newer public evidence boundary than the v1 record used in the earliest DEP pass. The paper proposes a target-aware approach to differentially private synthetic data: measure a workload made of treatment-arm feature masses and outcome-feature moments connected to orthogonal causal scores, add privacy noise once, and either evaluate stable moment-map estimators directly or reconstruct a maximum-entropy distribution from which reusable synthetic records are sampled.

The paper's strongest practical contribution is its separation of point accuracy from inferential validity. In the reported Table 1 setting, the fixed causal workload with noise-aware multiple imputation (NA+MI) gives empirical 95% interval coverage of 0.998, 1.000, 1.000, and 1.000 on IHDP, Twins, ACIC, and LaLonde. The naive private analyses show serious under-coverage, while generic MST-style synthesis often retains lower point RMSE. This is a tradeoff, not a dominance result: NA+MI deliberately widens intervals to represent DP measurement noise, and high-privacy-budget regimes can reveal approximation bias once privacy noise recedes.

The official repository substantially improves inspectability. It maps paper components to code, documents five public benchmarks, supplies ordered reproduction notebooks, records run configuration and code hashes, and pins an MIT-licensed implementation. It also narrows the comparison claim: `baselines.py` explicitly describes `run_mst_naive` as a simple MST-style product baseline, not the official Private-PGM implementation, and the inspected `maxent.py` implementation is product-style. The experiments were not rerun in this review, datasets are not bundled, dependency ranges are not locked, ACIC requires a separate R workflow, and no automated tests are present in the inspected tree. Accordingly, confidence is high in what the paper and code state and medium in broad comparative generalization.

## Detailed Summary

### Problem and target-aware release design

General-purpose DP synthetic-data systems usually select aggregate queries, measure them privately, and reconstruct records that reproduce those noisy answers. This supports reuse, but good marginal fidelity does not ensure that a causal estimand is preserved. Average treatment effects depend on treatment assignment, outcome structure within treatment arms, overlap, and nuisance models. A synthetic table can match low-dimensional marginals while distorting these conditional relationships.

The paper responds by defining a causal workload around the moments needed by orthogonal-score estimators. Given a feature map, the base workload contains four blocks: treatment-arm feature masses for control and treated units, plus outcome-weighted feature moments for each arm. Optional Gram moments support some direct ridge plug-ins, but they are not part of the default experimental release. This distinction matters because the authors present the base workload as one principled first-order design, not as a unique optimum or an information-theoretic lower bound.

### Privacy measurement and two downstream routes

The data holder measures the workload with a Gaussian mechanism. Everything after that measurement is post-processing and consumes no further privacy budget. The direct route evaluates an estimator that is a stable function of the noisy moments. The synthetic-data route fits a maximum-entropy distribution against the noisy workload, draws synthetic records, and applies causal estimators to those records.

The maximum-entropy formulation is an information projection onto distributions matching the retained moments. Noisy constraints can be negative or mutually inconsistent, so the paper allows relaxed, noise-weighted calibration and signal-to-noise filtering. Discarded moments do not disappear from the error accounting: they reappear as approximation bias. The paper also introduces Causal-AIM, an adaptive mechanism that privately selects feature groups according to a proxy for causal utility, measures each selected group once, and refits after each round.

### Error decomposition and assumptions

The formal analysis connects moment error to ATE error through estimator stability. Theorems cover projected ridge plug-ins, clipped IPW/AIPW maps, Gaussian-mechanism accuracy, and a composite ATE bound. The resulting decomposition distinguishes finite confidential-sample error, privacy noise, workload approximation, finite synthetic-sample Monte Carlo error, and calibration mismatch. Exact constants and stability depend on bounded outcomes, overlap or positivity, cell mass, clipping, ridge conditioning, retained coordinates, and a Lipschitz relation between moment perturbation and the estimator.

The theory does not establish correctness for any arbitrary analysis run on the sampled synthetic table. It controls direct moment maps and the components of the synthetic route that can be expressed through the reconstructed workload plus sampling and calibration terms. The appendix explicitly limits first-order sufficiency: it does not prove minimax optimality, workload uniqueness, or query-count optimality.

### Noise-aware multiple imputation

NA+MI treats the released noisy moments as observations of latent moments with known Gaussian-mechanism covariance. It draws plausible latent moment vectors, calibrates a synthetic distribution for each draw, samples synthetic records, estimates the causal effect, and combines the results with Rubin-style multiple-imputation rules. Between-imputation variance is the mechanism by which stronger privacy produces wider intervals. A bias-aware extension adds a workload-approximation term and proposes a diagnostic for the regime where approximation bias dominates privacy noise.

### Experimental design and findings

The paper evaluates IHDP, Twins, ACIC 2016 DGP 7, LaLonde/NSW, and a semi-synthetic ACS setting. The primary comparison covers non-private doubly robust estimation, generic MST-style and AIM-style synthesis with naive inference, a fixed causal workload with naive inference, the fixed causal workload with NA+MI, and adaptive Causal-AIM with NA+MI. Metrics include ATE RMSE, empirical 95% coverage, interval length, and marginal total-variation fidelity.

At the reported Table 1 setting, MST + naive has the lowest private RMSE on all four tabulated benchmarks, while its coverages are 0.014, 0.352, 0.236, and 0.118. Causal + NA+MI reports larger RMSE but coverages of 0.998, 1.000, 1.000, and 1.000. The evidence supports a calibrated-uncertainty claim, not universal point-accuracy leadership. Adaptive Causal-AIM improves some ACIC operating points but fails to recover the fixed workload's calibration on the tested IHDP grid. Hybrid workloads help in some ACIC cells and hurt in IHDP. Generic marginal fidelity does not rank the causal metrics.

### Reproducibility surface and implementation boundary

The official repository at commit `cdfa667b22d217e131d3dc3dd0c1863a2cd3e44f` includes the causal workload, Gaussian measurement, adaptive selection, product-style max-entropy reconstruction, NA+MI, estimators, baselines, plotting, paper-artifact generation, data loaders, provenance checks, and four ordered notebooks. Its README estimates about two hours on 20 cores for the main experiments and states that each run emits a manifest with configuration, per-file code hashes, and dataset sources.

The code also exposes boundaries not obvious from a headline comparison. The MST baseline is explicitly a simplified MST-style product baseline and not the official Private-PGM implementation. The direct DP estimators are labeled proxies, and the max-entropy class describes a product-style approximation. No datasets ship with the repository; public acquisition is documented, and ACIC requires an external R package workflow. The requirements file uses minimum versions rather than a frozen environment. No test suite or continuous-integration configuration appears in the inspected source inventory.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Causal workloads should preserve moments used by orthogonal causal scores rather than optimize only generic distributional fidelity. | Author claim and design principle | E3, E4 | Mechanistically coherent and explicitly scoped to a chosen feature basis; not proven unique or optimal | High |
| C2 | One DP workload can support ATE, ATT, and represented subgroup analyses without additional privacy spending. | Author claim | E4, E7 | Follows from post-processing and is demonstrated in the paper's reuse experiment, subject to workload representation | High |
| C3 | NA+MI restores near-nominal interval coverage in the reported benchmarks where naive synthetic-data inference under-covers. | Empirical author claim | E6, E7 | Strongly supported by the reported tables; no independent rerun performed | High for reported results; medium for external generalization |
| C4 | Generic workloads can retain better point RMSE even when causal workloads yield better uncertainty calibration. | Empirical author claim | E6, E7 | Supported in the reported benchmark grid and central to interpreting the method honestly | High within the tested settings |
| C5 | Causal-AIM is an operating-point choice rather than a universal improvement over the fixed causal workload. | Author conclusion and reviewer synthesis | E7 | Supported by opposite behavior on ACIC and IHDP | High |
| C6 | The official repository makes the paper reproducible end to end. | Repository claim | E8 | Materials and commands are present, but reproducibility is not independently established until data acquisition and experiments are rerun in a pinned environment | Medium |
| C7 | Comparative claims against MST should be read as comparisons to the repository's MST-style product baseline, not automatically to official Private-PGM MST. | Reviewer interpretation | E9, E10 | Directly grounded in the code comment and implementation map; a necessary scope label | High |
| C8 | Shrinking privacy noise can expose approximation bias and reduce nominal coverage unless the workload or interval is adapted. | Author analysis | E5, E7 | The stated coverage-privacy paradox is plausible and supported by the reported ACIC trend; wider external validation is needed | Medium-High |

## Methodology

- `Research objective`: Expand the randomly selected causal-DP thread from the selected DEP while preserving its prior semantic graph and separating formal claims, reported results, code evidence, and reviewer interpretation.
- `Sources inspected`: Every file in the selected source DEP; the latest source report; the latest Black-Lake log; the latest Report-Mark; the latest prior DEP README and manuscript; arXiv:2607.08122v2 metadata and complete HTML; and the official `AsiaeeLab/causal-aim` repository at commit `cdfa667b22d217e131d3dc3dd0c1863a2cd3e44f`.
- `Discovery strategy`: Repository inventory, family-marker search, prior-reference chasing, one bounded random expansion draw, canonical arXiv inspection, and inspection of the implementation linked by the paper.
- `Inclusion criteria`: Primary or near-primary materials that identify the current paper version, support method or experimental claims, define the implementation/reproduction surface, or preserve iterative DEP provenance.
- `Exclusion criteria`: Secondary summaries, unreviewed citations in the paper's bibliography, inaccessible derivative aggregators, and sources that did not materially support the selected thread.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Major claims map to evidence IDs; exact reported values are labeled as reported; code comments and repository structure are treated as implementation evidence; broader conclusions are labeled interpretation.
- `Uncertainty handling`: Missing math symbols in the experimental HTML rendering are not reconstructed from guesswork; the table is described at its reported setting. No execution or independent reproduction is implied.
- `Extraction process`: HTML sections, tables, appendices, repository Markdown, code inventory, function map, commit metadata, and selected implementation comments were inspected. No PDF was required because complete v2 HTML was available.
- `Version control`: Source DEP pinned at `e09ab977`; prior manuscript pinned at `b8f1fc5`; paper pinned to arXiv v2; official code pinned to `cdfa667b`.
- `Cross-checking`: Paper mechanism, reported tables, reproducibility statement, code-to-paper map, baseline implementation labels, data instructions, license, and source inventory were compared.
- `Reviewer stance`: DEP-ready source preservation plus claim-bounded critique and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: The workload-preserving DP synthetic-data thread in `DEP-20260712-Tech Intel 1100`, including current v2 evidence and official implementation context.
- `Temporal boundary`: Public and repository sources accessed 2026-07-22; paper revision v2 dated 2026-07-17; code inspected at the pinned public commit.
- `Evidence limits`: No experiment, notebook, dataset acquisition, privacy accountant, theorem proof, or result table was independently executed or reproduced.
- `Assumptions`: The arXiv record accurately represents v2 and its venue/licensing metadata; the linked GitHub repository is the authors' official implementation; public commit history is durable provenance.
- `Constraints`: Public evidence only; no confidential or benchmark data deposition; no clinical decision-support claim; no assertion that synthetic data remove privacy, bias, or validity risks.
- `Out of scope`: Fresh causal-effect estimation, protected-data release, privacy-budget certification, benchmark reanalysis, official Private-PGM reruns, and institutional/legal review.
- `Intended use`: DEP expansion, replication planning, privacy-aware system design, and evidence-bounded product research.
- `Audience`: Differential-privacy researchers, causal-inference practitioners, data-release stewards, reproducibility reviewers, and research engineers.
- `Depth target`: Full manuscript review with implementation and replication context.
- `Reproducibility boundary`: A reviewer can audit the paper, code, data instructions, and commands; reported results remain unverified until the pipeline is rerun with pinned dependencies and acquired benchmarks.
- `Operational boundary`: Any real deployment needs privacy review, data-governance approval, estimand-specific validation, overlap diagnostics, disclosure assessment, and human statistical review.
- `Data sensitivity`: Source materials are public; the method targets potentially sensitive tabular data, but none was accessed or deposited in this pass.

## Observations

- `Observed pattern`: The artifact's core distinction is between preserving a data distribution and preserving the moment structure needed for a decision-relevant estimand.
- `Observed pattern`: NA+MI's wider intervals are a feature when naive intervals omit DP noise; narrowness alone is not evidence of inferential quality.
- `Technical implication`: The feature map is simultaneously an interface, a compression choice, and an approximation assumption. Workload design cannot be separated from the target estimand.
- `Technical implication`: SNR thresholding and ridge regularization address different failure modes: noise-chasing in calibration versus instability in nuisance inversion.
- `Contradiction or tension`: The paper uses familiar MST/Private-PGM language, while the official code explicitly implements a simple MST-style product comparator. This does not invalidate the reported experiment, but it narrows what that experiment compares.
- `Contradiction or tension`: Stronger privacy budgets can improve point estimates yet reveal fixed workload misspecification, producing the reported coverage-privacy paradox.
- `Open question`: It remains unclear how the fixed causal workload compares with official, carefully tuned contemporary DP synthesizers under identical accounting and reconstruction capacity.
- `Reviewer hypothesis`: A hybrid workload selected against predeclared causal and exploratory utility could offer a better frontier than either target-specific or generic marginals alone, but selection itself must remain privacy-accounted and held-out.

## Considerations

- Causal validity still requires identification assumptions such as unconfoundedness and positivity; DP synthesis does not repair hidden confounding.
- Public release of synthetic rows is not automatically safe. The mechanism, adjacency definition, clipping, sensitivity, composition, delta choice, and post-release threat model require expert review.
- Coverage estimates from 100 or 200 replications have sampling uncertainty; comparisons should include confidence intervals over coverage and paired-seed analyses.
- Benchmark truth is partly semi-synthetic. Performance on known simulated effects does not establish validity on real observational decisions where ground truth is unknown.
- Outcome clipping and discretization can change the estimand or introduce subgroup-specific bias. These transformations need domain review.
- The external data-acquisition chain adds version, availability, and licensing risks. A reproducible release should record hashes and licenses for every acquired dataset.
- Minimum-version dependency ranges are insufficient for long-term numerical reproducibility; lockfiles or container images are preferable.
- Adaptive Causal-AIM divides privacy budget across selection and measurement. Extra rounds can harm utility, so round count must be treated as a predeclared operating parameter rather than searched on protected outcomes without accounting.
- The method's intended reuse value depends on declaring an estimand family in advance. Unrepresented post hoc analyses may have uncontrolled approximation error even though they incur no extra privacy spending.
- Health, education, and social-science use requires stakeholder review because interval calibration does not by itself establish fairness, actionability, or acceptable downstream harm.

## Strengths

- The paper connects the release workload to orthogonal-score structure rather than treating synthetic-data fidelity as a universal proxy for analytical utility.
- It distinguishes direct moment estimation from synthetic-data reconstruction, making clear where additional calibration and Monte Carlo error enter.
- The five-part error decomposition keeps privacy, approximation, and solver mismatch visible.
- NA+MI addresses a concrete and common failure: treating DP synthetic rows as if they were ordinary i.i.d. observations.
- The experiments report both RMSE and coverage, exposing the tradeoff between point accuracy and inferential validity.
- The reuse experiment demonstrates why a synthetic release can be preferable to one directly released ATE when several represented estimands are needed.
- The official repository has a clear code-to-paper map, ordered notebooks, data-provenance instructions, deterministic seed utilities, and run-manifest generation.
- The paper and code acknowledge operating-point dependence rather than presenting Causal-AIM as uniformly superior.

## Weaknesses

- The base workload is principled but not shown to be unique, minimax optimal, or query-optimal.
- Theory does not cover every downstream fitted-nuisance routine applied to synthetic records.
- Feature discretization can create approximation bias, especially for nonlinear response surfaces and small subgroups.
- The reported intervals can be very wide at strict privacy budgets, limiting decision usefulness even when coverage is nominal.
- The comparison uses simplified MST-style and AIM-style implementations; results should not be generalized to every official or modern DP synthesizer.
- The code repository contains no datasets, locked environment, automated tests, or visible continuous-integration workflow in the inspected tree.
- ACIC reproduction depends on an external R package path whose upstream README is described as stale.
- The repository had one inspected commit in the shallow history, so the review cannot infer development maturity, issue resolution, or result stability from history.
- No independent code execution, privacy-accounting audit, or numerical reproduction was performed in this pass.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Re-run comparisons with official Private-PGM MST/AIM and another modern DP synthesizer | Baseline validity | The current code uses simplified style baselines | Clarifies which gains survive stronger comparators | Integration and tuning cost | Paired seeds, identical privacy accounting, preregistered hyperparameters |
| Publish a locked environment and container digest | Reproducibility | Minimum dependency ranges can drift numerically | Stable reruns and easier review | Maintenance burden | Recreate Table 1 from a fresh machine and compare hashes |
| Add unit, property, and privacy-accounting tests | Software assurance | Core moment, sensitivity, calibration, and composition logic lacks an inspected test suite | Detects silent regressions and invalid configurations | Engineering effort | Synthetic fixtures with analytic moments, accountant cross-checks, CI |
| Report uncertainty on empirical coverage and RMSE differences | Statistical reporting | Coverage estimates are themselves noisy | Prevents over-reading small gaps | More replications may be expensive | Binomial intervals, paired bootstrap, seed-level release |
| Expand workload selection to continuous or learned public features | Approximation | Discretization can dominate at high privacy budgets | Better causal fidelity without simply adding bins | Feature learning may spend privacy or overfit | Public-feature and DP-trained-feature arms with held-out diagnostics |
| Create subgroup stress tests | Equity and overlap | Small or poorly represented groups can violate stability assumptions | Exposes differential interval failure | Risk of unstable estimates | Minimum-mass gates, subgroup coverage, abstention criteria |
| Publish dataset manifests with checksums and license records | Provenance | Data are acquired from several external sources | Durable and auditable reproduction | Redistribution limits | Hash verification and source-license checklist |
| Separate solver approximation from workload approximation in reports | Diagnostics | Calibration residual and basis misspecification have different remedies | More actionable failure reports | Additional instrumentation | Log both residuals and richer-dictionary score discrepancies |

## Potential Implementations

### Estimand-aware release planner

- `User`: Statistical disclosure-control team.
- `Goal`: Translate a declared family of causal analyses into a reviewable DP workload and release plan.
- `Core mechanism`: Collect estimands, identification assumptions, feature maps, privacy parameters, and subgroup constraints; generate the corresponding moment inventory and risk/utility checklist.
- `Required inputs`: Data schema, estimand definitions, public feature metadata, privacy policy, clipping bounds, and authorized benchmark fixtures.
- `Outputs`: Workload specification, sensitivity worksheet, accounting plan, validation matrix, and abstention conditions.
- `Risk controls`: No raw-data export, formal privacy review, subgroup minimum-mass gates, versioned configurations, and human approval.
- `Evaluation`: Synthetic distributions with known ATE/ATT/subgroup effects and adversarial overlap cases.

### Noise-aware synthetic release validator

- `User`: Research data steward.
- `Goal`: Determine whether a proposed DP synthetic release supports its declared causal analyses with calibrated uncertainty.
- `Core mechanism`: Reconstruct from measured moments, run NA+MI, compare coverage and approximation diagnostics on authorized semi-synthetic fixtures, and flag noise- or bias-dominated regimes.
- `Required inputs`: Noisy workload, covariance, solver residuals, feature dictionary, and benchmark truth available only in validation environments.
- `Outputs`: Coverage report, interval-width frontier, calibration residuals, approximation score, and pass/fail recommendation.
- `Risk controls`: Isolated validation, no confidential-row logging, bounded synthetic output, and explicit non-certification language.
- `Evaluation`: Paired comparisons against naive inference, direct DP proxies, official DP synthesizers, and non-private oracles.

### Reproducibility harness

- `User`: Artifact reviewer or conference reproducibility chair.
- `Goal`: Verify that paper tables are generated from documented public data and pinned code.
- `Core mechanism`: Acquire sources through recorded recipes, verify hashes, build a locked environment, run smoke and full profiles, and compare generated tables with paper values.
- `Required inputs`: Commit pin, data manifest, environment lock, expected table schema, compute budget, and source licenses.
- `Outputs`: Signed run manifest, code/data hashes, deviation report, generated tables, and unresolved blockers.
- `Risk controls`: Public data only, no credential embedding, isolated execution, resource limits, and license checks.
- `Evaluation`: Fresh-machine rerun plus deliberate dependency and dataset-version perturbations.

## Three Ways to Exercise This Research

1. `Moment-preservation toy study`: Objective - show why generic marginals can miss a causal effect; inputs - a synthetic confounded dataset with known potential outcomes; method - compare a generic marginal release with a small causal moment workload under the same declared Gaussian noise; output - ATE error, coverage, and marginal TVD; success criterion - the experiment recovers the intended fidelity-versus-causal-utility distinction; stop condition - do not generalize beyond the constructed data.
2. `NA+MI calibration smoke test`: Objective - verify uncertainty propagation; inputs - public or synthetic benchmark data, a fixed causal workload, and several privacy-noise levels; method - compare naive intervals with NA+MI over repeated simulations; output - coverage and interval-length curves; success criterion - NA+MI tracks nominal coverage when model approximation is adequate; stop condition - flag rather than tune away an approximation-dominated regime.
3. `Comparator audit`: Objective - test the robustness of the paper's comparative claims; inputs - the pinned repository, official Private-PGM baselines, locked dependencies, and public benchmark recipes; method - run paired seeds under identical accounting and report implementation differences; output - reproducible RMSE/coverage tables and a scope statement; success criterion - every comparator is source-pinned and privacy-accounted; stop condition - withhold comparative conclusions if implementations or budgets are not equivalent.

## Example MVP Product

- `Product name`: CausalRelease Review
- `Target user`: Data steward planning a differentially private synthetic-data release for approved research.
- `Problem`: Teams can optimize generic synthetic fidelity yet produce invalid causal intervals or overstate what a release supports.
- `Core workflow`: Define estimands and assumptions, select a bounded feature map, derive the causal workload, enter privacy parameters, run synthetic fixture checks, compare naive and noise-aware inference, and generate a human-review packet.
- `Data requirements`: Schema and public metadata by default; synthetic or explicitly authorized validation data; no production records in the MVP.
- `Architecture`: Local-only Python application with declarative workload files, a pluggable accountant, synthetic fixture generator, NA+MI module, official-baseline adapters, and Markdown/JSON reporting.
- `Success metrics`: Correct analytic moments on fixtures, zero raw-row logging, reproducible manifests, calibrated synthetic-fixture coverage, explicit abstention on poor overlap, and complete comparator scope labels.
- `Risk controls`: Local execution, allowlisted inputs, privacy-parameter validation, subgroup mass checks, no claim of legal certification, and mandatory statistical/privacy review before real release.
- `Limitations`: Synthetic fixtures cannot establish performance on confidential data; identification assumptions remain domain responsibilities; solver and feature-map misspecification can dominate.
- `MVP boundary`: Planning and validation only; it does not publish data, choose privacy policy, certify compliance, or replace a statistician.
- `Deployment model`: Local CLI or desktop review tool with versioned configuration bundles.
- `Evaluation plan`: Unit tests for moments/sensitivity, accountant cross-checks, semi-synthetic coverage trials, official-baseline comparisons, and red-team tests for provenance leakage.
- `Failure modes`: Incorrect adjacency, unstable overlap, clipped estimand drift, dependency variance, unrepresented post hoc queries, misleading narrow intervals, and false equivalence between style baselines and official implementations.
- `Maintenance plan`: Pin accountant versions, refresh dataset provenance, track paper/code revisions, maintain comparator adapters, and periodically rerun gold fixtures.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Workload-Preserving Differentially Private Synthetic Data for Causal Inference via Maximum-Entropy Calibration | Primary preprint - **newly expanded in this pass** | Current v2 full text inspected for causal workloads, error decomposition, NA+MI, five benchmarks, limitations, and revision state | https://arxiv.org/abs/2607.08122v2 |
| Causal-AIM official implementation | Official code - **newly inspected in this pass** | Reproduction notebooks, data provenance, manifests, method code, and the simplified MST-style comparator boundary | https://github.com/AsiaeeLab/causal-aim/tree/cdfa667b22d217e131d3dc3dd0c1863a2cd3e44f |
| Contravariance Study - DEP-E | Prior DEP research artifact | Latest iterative context and source of the nine-item expansion pool | https://github.com/Delphoa/Black-Lake/blob/b8f1fc50c914447de0b7818ff427e55d2dbaee2e/.lake-data/DEP-E/DEP-E-20260716-Contravariance%20Study/contravariance-study.md |
| Ideas Have Genomes | Primary preprint | Scientific-lineage reasoning and provenance-aware idea generation; retained from the prior graph | https://arxiv.org/abs/2607.08758 |
| BiSCo-LLM | Primary preprint | Storage-aware extreme low-bit compression; retained from the prior graph | https://arxiv.org/abs/2607.08643 |
| Contravariance Theory | Primary preprint | Previously expanded theory of conditional representational alignment | https://arxiv.org/abs/2607.08561v1 |
| Stop Guessing When to Stop Testing | Primary preprint | Sequential stopping for statistically grounded model evaluation; retained from the prior graph | https://arxiv.org/abs/2607.08522 |
| MatBind | Primary preprint | Shared multimodal materials representation; retained from the prior graph | https://arxiv.org/abs/2607.08470 |
| Score Distributions, Not Cells | Primary preprint | Correct primary identity for the source DEP's arXiv:2607.04595 mismatch | https://arxiv.org/abs/2607.04595 |
| Storage-Centric Genomic Analysis | Primary preprint | Data-movement and preparation bottlenecks in genomic systems; retained from the prior graph | https://arxiv.org/abs/2607.02552 |
| Parallel QEC Decoding | Primary preprint | Parallel decoding for distributed quantum computing; retained from the prior graph | https://arxiv.org/abs/2607.08386 |
| Works on My QPU | Primary preprint | Empirical quantum-research reproducibility; retained from the prior graph | https://arxiv.org/abs/2607.08348 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R0 | [DEP-20260712-Tech Intel 1100](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/e09ab977fedb25f03690b731d751ab93d4ede947/.lake-data/DEP-20260712-Tech%20Intel%201100) | Original inventory, digest, attribution, and prior Report-Marks | 2026-07-22 | Selected source DEP; every repository file inspected |
| R1 | [Latest prior source report](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/e09ab977fedb25f03690b731d751ab93d4ede947/.reports/BL-DEP-20260712-Tech%20Intel%201100-20260716/README.md) | Prior processing scope, selection, and evidence boundary | 2026-07-22 | Inspected before expansion |
| R2 | [Latest prior Black-Lake log](https://github.com/Delphoa/Black-Lake/blob/b8f1fc50c914447de0b7818ff427e55d2dbaee2e/.logs/20260716-DEP-20260712-Tech%20Intel%201100-LOG.md) | Prior validation, questions, and challenges | 2026-07-22 | Inspected before expansion |
| R3 | [Latest prior Report-Mark](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/e09ab977fedb25f03690b731d751ab93d4ede947/.lake-data/DEP-20260712-Tech%20Intel%201100/BL-DEP-Mark002%20Report-Mark.md) | Exact preserved related-reading and reference graph | 2026-07-22 | Inspected; provided the bounded expansion pool |
| R4 | [Latest prior manuscript](https://github.com/Delphoa/Black-Lake/blob/b8f1fc50c914447de0b7818ff427e55d2dbaee2e/.lake-data/DEP-E/DEP-E-20260716-Contravariance%20Study/contravariance-study.md) | Prior synthesis and status of the causal-DP thread | 2026-07-22 | Public commit-pinned artifact |
| R5 | [arXiv:2607.08122v2 record](https://arxiv.org/abs/2607.08122v2) | Canonical title, authors, v2 revision, abstract, license link, code link, and venue claim | 2026-07-22 | Primary record; UAI acceptance is reported by the authors |
| R6 | [arXiv:2607.08122v2 full HTML](https://arxiv.org/html/2607.08122v2) | Method, theory, experiments, tables, appendices, limitations, and future work | 2026-07-22 | **New full-paper evidence in this pass**; no paper file collected for deposition |
| R7 | [Causal-AIM repository](https://github.com/AsiaeeLab/causal-aim/tree/cdfa667b22d217e131d3dc3dd0c1863a2cd3e44f) | Official implementation, dependencies, reproduction workflow, data provenance, license, manifests, and baseline scope | 2026-07-22 | **New implementation evidence in this pass**; inspected at commit `cdfa667b`; not executed or deposited |
| R8 | [Ideas Have Genomes](https://arxiv.org/abs/2607.08758) | Retained scientific-lineage thread | 2026-07-22 | Preserved from prior related-reading graph; not re-reviewed in full this pass |
| R9 | [BiSCo-LLM](https://arxiv.org/abs/2607.08643) | Retained low-bit compression thread | 2026-07-22 | Preserved; not re-reviewed in full this pass |
| R10 | [Contravariance Theory](https://arxiv.org/abs/2607.08561v1) | Previously expanded alignment thread | 2026-07-22 | Carried forward from prior full-paper artifact |
| R11 | [Stop Guessing When to Stop Testing](https://arxiv.org/abs/2607.08522) | Retained evaluation-stopping thread | 2026-07-22 | Preserved; not re-reviewed in full this pass |
| R12 | [MatBind](https://arxiv.org/abs/2607.08470) | Retained materials-representation thread | 2026-07-22 | Preserved; not re-reviewed in full this pass |
| R13 | [Score Distributions, Not Cells](https://arxiv.org/abs/2607.04595) | Correct source identity for the original DEP mismatch | 2026-07-22 | Provenance defect retained; not re-reviewed in full this pass |
| R14 | [Storage-Centric Genomic Analysis](https://arxiv.org/abs/2607.02552) | Retained genomic systems thread | 2026-07-22 | Preserved; not re-reviewed in full this pass |
| R15 | [Parallel QEC Decoding](https://arxiv.org/abs/2607.08386) | Retained distributed-QEC thread | 2026-07-22 | Preserved; not re-reviewed in full this pass |
| R16 | [Works on My QPU](https://arxiv.org/abs/2607.08348) | Retained quantum-reproducibility thread | 2026-07-22 | Preserved; not re-reviewed in full this pass |

## Appendix

### Iterative expansion record

- Automation family: `Black-Lake Data Processing & Review` and `Black-Lake Data Processing & Review 0900` treated as one family.
- Eligibility cutoff: `2026-07-21T00:04:16Z`.
- Canonical candidates: 73; recent-family exclusions: 2; eligible: 71.
- Excluded DEPs: `DEP-20260708-Tech Intel 1104` and `DEP-20260714-Tech Intel 1305`.
- Eligible-list SHA-256: `19d50c6018b6c20ede594bb41ca9ce34344b0051b9ada3e984c990d43a448842`.
- DEP selection method: PowerShell `Get-Random` over sorted eligible names; successful draw index 40 selected `DEP-20260712-Tech Intel 1100`.
- Audit note: two earlier probes were discarded because their selected values were not successfully recorded after post-draw compatibility/serialization failures; neither probe influenced the successful selection.
- Expansion pool: nine primary threads retained by the latest prior manuscript after excluding Contravariance Theory, which had already received a full-paper expansion.
- Expansion selection method: PowerShell `Get-Random`; draw index 2 selected `arXiv:2607.08122`.
- Accessibility: canonical v2 record, complete HTML, and official code repository were accessible; no redraw was required.

### Source inventory and collection status

- Selected source repository files inspected: `README.md`, `daily_research_findings_2026-07-12_1100.md`, `BL-DEP-Mark001 Report-Mark.md`, and `BL-DEP-Mark002 Report-Mark.md`.
- Prior processing material inspected: the 2026-07-16 source report, Black-Lake log, DEP README, and full manuscript.
- External sources inspected: arXiv v2 record, complete public HTML, and official implementation at the pinned commit.
- Files deposited from external sources: none.
- Reproduction status: no data download, dependency installation, notebook execution, privacy audit, or numerical rerun.

### Validation checklist

- [x] Current v2 paper evidence and official implementation are marked as new.
- [x] Every evidence-ledger source appears in Source References.
- [x] Reported values are separated from reviewer interpretation.
- [x] Comparative baseline scope is explicit.
- [x] Exactly three exercise paths are present.
- [x] No local path, username, machine identifier, or local timezone is published.
- [ ] Independently reproduce the tables under a locked environment and official comparator suite.
