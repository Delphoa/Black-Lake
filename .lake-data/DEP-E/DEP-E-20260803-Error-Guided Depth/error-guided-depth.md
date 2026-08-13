---
title: "Error-Guided Depth - DEP-E"
generated_at: "2026-08-03T00:05:04Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of a posteriori error-guided neural-network depth adaptation and its place in constraint-aware system design."
source_status: "URLs and repository Markdown only; no external source files collected"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-03"
temporal_cutoff: "Primary sources inspected through 2026-08-03"
primary_url: "https://arxiv.org/abs/2607.07637"
stable_identifier: "DEP-20260709-Tech Intel 1305; DEP-E"
confidence_summary: "High for the paper's stated mechanism and tables; medium for comparative generalization because code was not located, experiments were not rerun, and compute budgets differ."
safety_scope: "Non-sensitive research review and bounded synthetic implementation planning"
---

# Error-Guided Depth - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository-Relative Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Selected source DEP README | Primary source-package manifest | Markdown | Source snapshot `c5bcc6a0477f5c3555bc01ccb8d9193dd4b47dac` | `Black-Lake-Data/.lake-data/DEP-20260709-Tech Intel 1305/README.md` | Public repository text | 2026-08-03 | Inspected |
| S2 | Selected source findings | Primary source-package artifact | Markdown | `daily_research_findings_2026-07-09_1305.md` | `Black-Lake-Data/.lake-data/DEP-20260709-Tech Intel 1305/daily_research_findings_2026-07-09_1305.md` | Public repository text | 2026-08-03 | Inspected |
| S3 | Constraint-Aware Systems - DEP-E | Prior continuity manuscript | Markdown | Black-Lake commit `68a04529d6852b5a55f7d9d0cf6fd4dca31bec5f` | https://github.com/Delphoa/Black-Lake/blob/68a04529d6852b5a55f7d9d0cf6fd4dca31bec5f/.lake-data/DEP-E/DEP-E-20260726-Constraint-Aware%20Systems/constraint-aware-systems.md | Independent review; no author endorsement implied | 2026-08-03 | Inspected in full |
| S4 | *An optimal control approach for neural network architecture adaptation with a posteriori error estimation* | Selected primary expansion paper | arXiv HTML and canonical record | arXiv:2607.07637v1; DOI 10.48550/arXiv.2607.07637 | https://arxiv.org/html/2607.07637v1 | CC BY 4.0 on arXiv | 2026-08-03 | Full HTML, equations, algorithms, tables, figures, appendices, and references inspected |
| S5 | *Deep learning as optimal control problems: models and numerical methods* | Primary methodological context | arXiv full text | arXiv:1904.05657 | https://arxiv.org/abs/1904.05657 | Public arXiv record | 2026-08-03 | Full HTML inspected for the continuous-control and discretization lineage |
| S6 | *Sensitivity-Based Layer Insertion for Residual and Feedforward Neural Networks* | Near-primary comparator | arXiv canonical record | arXiv:2311.15995 | https://arxiv.org/abs/2311.15995 | Public arXiv record | 2026-08-03 | Canonical abstract and availability metadata inspected |
| S7 | *Topological derivative approach for deep neural network architecture adaptation* | Near-primary comparator by overlapping authors | arXiv canonical record | arXiv:2502.06885 | https://arxiv.org/abs/2502.06885 | Public arXiv record | 2026-08-03 | Canonical abstract and availability metadata inspected |
| S8 | Prior source report, Report-Mark, and output log | Continuity and selection provenance | Markdown | 2026-07-26 pass | Source `.reports`, source Report-Mark, and Black-Lake `.logs` repository-relative records | Public repository text | 2026-08-03 | Inspected in full |

No PDF, TeX source package, dataset, code repository, model, benchmark payload, Navier-Stokes data, or execution trace was collected. The selected paper states that experiments used PyTorch, but this review did not locate a paper-specific public code repository.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S2 | Source DEP | Original ten-finding scope, attribution, and the architecture-adaptation finding | Selection boundary and original relevance | High | Source package is a synthesis, not independent validation |
| E2 | S3 and S8 | Prior review bundle | Full prior manuscript, latest log, latest source report, and Report-Mark | Continuity, prior claims, and the expansion frontier | High | Prior review did not execute the cited methods |
| E3 | S4, §§2-5, Theorem 1, Corollary 5.4, Algorithm 1 | Primary paper | Continuous-depth optimal-control formulation, piecewise-linear parameter space, DWR error representation, computable interval indicators, and layer-insertion loop | Mechanism and theoretical scope | High | Bound assumes first-order stationarity; practical computation approximates unknown and continuous quantities |
| E4 | S4, §6.1 and Table 1 | Primary paper | Two-dimensional regression design, mesh-convergence choice of `K=4`, test losses, and runtimes | Proof-of-concept empirical comparison | High | Best-validation models and unequal training times; no independent rerun |
| E5 | S4, §6.2 and Table 2 | Primary paper | Navier-Stokes inverse problem, data generation, noise, splits, relative errors, and runtimes | Scientific-ML empirical comparison | High | Synthetic inverse problem; small absolute improvement over baseline; no seed variance reported in the table |
| E6 | S4, Remark 5.6 and Appendices A-B | Primary paper | Local-minimum caveat, two-level discretization, 20-initialization selection, shared hyperparameters, and early stopping | Boundary conditions and reproducibility limits | High | Code is described but a public implementation was not located |
| E7 | S5 | Primary methodological paper | ResNets as ODE discretizations, optimize/discretize ordering, adjoints, and structure-preserving integration | Optimal-control lineage and discretization caution | Medium-High | Context paper uses toy classification studies rather than the selected paper's tasks |
| E8 | S6-S7 | Primary canonical records | Sensitivity-based insertion and topological-derivative approaches to where and how layers are added | Comparative architecture-growth context | Medium | Abstract-level inspection only in this pass |

## Executive Summary

The selected expansion paper turns depth adaptation into a localized numerical-analysis problem. It models a residual fully connected network as a discretized continuous-time optimal-control system, treats layerwise weights and biases as a piecewise-linear approximation to depth-varying controls, and derives a dual-weighted-residual error representation. A computable interval indicator identifies where the parameter representation contributes most to the estimated functional error; the algorithm inserts a layer at that interval's midpoint, interpolates its parameters from its neighbors, retrains, and stops when validation loss ceases to improve.

The mechanism is stronger and narrower than a generic claim that the method “knows where a network needs depth.” The theoretical quantity is the loss gap attributable to representing continuously varying controls with piecewise-linear controls, plus a remainder, under first-order optimality assumptions and exact state/adjoint equations. The implementation approximates those ingredients using centered differences and a fine forward-Euler submesh. It does not directly bound test error, out-of-distribution error, or architecture-search regret. Validation loss supplies the practical stopping signal, while the paper itself notes that retaining the best validation model can violate the local-minimum condition needed for estimator accuracy.

The empirical results show an accuracy-cost trade-off. On the synthetic regression problem, the final proposed model reports MSE `9.0e-6` in 46 minutes, versus `3.82e-5` in 9 minutes for the same-final-depth baseline; an intermediate proposed model reports `2.5e-5` in 14 minutes. On the Navier-Stokes inverse problem, the final relative error is `0.161` in 9 minutes, versus `0.166` in 3 minutes for the baseline; the intermediate proposed result is `0.165` in 5 minutes. These results support targeted depth growth in the tested small-width regimes, but they do not establish compute-normalized superiority, robustness across seeds, or transfer to convolutional, recurrent, or large-scale architectures.

Reviewer interpretation: the reusable contribution is an evidence-carrying capacity decision. Each proposed layer can be linked to an explicit local indicator, a validation change, an added compute cost, and a rollback point. That makes architecture growth more auditable than opaque search, even when the indicator is only an approximation and the final generalization claim remains empirical.

## Detailed Summary

### Research problem and lineage

Depth selection is usually handled by manual design, discrete architecture search, or a growth heuristic. The selected paper places itself in the growth family and asks three concrete questions: where to insert a layer, how to initialize it, and when to stop. Its lineage combines the view of residual networks as discretized ODEs with dual-weighted-residual adaptivity from numerical analysis. Earlier optimal-control work (S5) explains why forward states, backward adjoints, and the order of optimization and discretization matter; the new paper uses that foundation to localize parameter-representation error along depth.

### Continuous and discrete research objects

The “true” problem allows weights and biases to vary continuously with a depth variable. The coarse problem restricts those controls to continuous, piecewise-linear functions between layer nodes. The state evolves through a residual ODE, while the output loss is evaluated at the terminal depth. The desired quantity is the gap between the continuous-control objective and the coarse objective.

This framing matters because the error being estimated is not every possible source of model error. It is specifically the discrepancy caused by approximating depth-varying controls in a finite-dimensional piecewise-linear space. The theoretical derivation assumes the continuous and coarse problems satisfy first-order optimality conditions and treats the state and adjoint ODEs as exact. A trapezoidal-rule remainder remains in the error representation.

### Error localization and practical estimator

Theorem 1 expresses the objective gap as interval contributions from weight and bias residuals plus a remainder. Corollary 5.4 upper-bounds each interval with a product of two factors: an interpolation-error term and a residual/sensitivity term involving discrete states and adjoints. Because the true continuous controls are unavailable, the implementation estimates their interpolation error using centered finite differences of the learned discrete parameters.

States and adjoints are also unavailable in exact continuous form, so the implementation subdivides every layer interval into `K` forward-Euler steps. Parameters remain stored at coarse layer nodes and are linearly interpolated at the substeps. This two-level discretization improves estimator fidelity but slows every forward and backward propagation. On the proof-of-concept problem, the authors choose `K=4` after comparing against `K=1000` and obtaining a reported state-error indicator of `0.03` for the initial network.

### Adaptation algorithm

Algorithm 1 begins with a small network, trains it, and freezes the input and output layers. At each iteration it computes the interval indicators, inserts a new layer at the midpoint of the largest-error interval, initializes the new weight and bias by averaging the two neighboring parameter nodes, retrains, and records the best validation loss. It stops after the configured maximum number of insertions or once validation loss worsens. The input and output layers are then unfrozen for final training.

The algorithm therefore joins four signals that should not be conflated: the theoretical representation-error decomposition, the approximate computational indicator, the empirical validation-loss stopping rule, and the reported test metric. A low indicator does not alone certify low test loss. Conversely, a validation improvement can occur even when the current training parameters are not at the local minimum assumed by the theorem; Remark 5.6 identifies this tension explicitly.

### Synthetic regression evidence

The first task learns `exp(-0.1(x^2+y^2)) sin(x) cos(y)` on `[-5,5]^2` using 1,000 training, 500 validation, and 500 test points. The initial network has three hidden layers with five neurons per layer. The final proposed model reaches 17 hidden layers in the figures.

Table 1 reports `9.0e-6` test MSE in 46 minutes for the final proposed model. The intermediate result is `2.5e-5` in 14 minutes. The baseline at the same final depth reports `3.82e-5` in 9 minutes; random insertion reports `9.41e-5` in 5 minutes; Net2DeeperNet reports `7.66e-5` in 4.5 minutes; and Forward Thinking reports `7.1e-4` in 2.5 minutes. The selected method achieves the lowest error, but also the highest runtime. The intermediate result is the clearest practical comparison because it improves on the baseline while reducing the final method's cost, though it is still not an equal-compute study.

### Navier-Stokes inverse evidence

The second task reconstructs a `64x64` initial vorticity field from ten observations at time `0.5` for a two-dimensional periodic Navier-Stokes system with viscosity `1e-3`. Initial fields use 50 Karhunen-Loève coefficients from a squared-exponential covariance with length scale `0.3`; observations receive 1% Gaussian noise. The split is 700 training, 100 validation, and 300 test samples.

Table 2 reports average relative error `0.161` in 9 minutes for the final proposed model and `0.165` in 5 minutes for an intermediate model. The same-final-depth baseline reports `0.166` in 3 minutes; random insertion `0.170` in 1 minute; Net2DeeperNet `0.171` in 2 minutes; and Forward Thinking `0.172` in 30 seconds. The final absolute improvement over baseline is `0.005`, or about 3% relative to the baseline error, at three times the reported runtime. The paper's conclusion properly narrows the empirical claim to small network width.

### Reproducibility and comparison boundary

All approaches use `tanh` hidden activations, a linear output, Adam, and shared task hyperparameters. The study evaluates 20 random initializations of the initial small network and retains the best-validation initialization for adaptation. Tables report the best-validation models, not distributions across repeated full adaptation runs. The proposed and random-insertion methods use the paper's two-level architecture; other baselines use conventional feed-forward networks. Early stopping allows comparison methods to terminate after different numbers of epochs. These choices are disclosed, but they make the evidence a best-model comparison under differing realized compute rather than a compute-normalized statistical benchmark.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The paper derives an interval-decomposed error representation for piecewise-linear depth controls. | Author theoretical claim | E3 | Supported under the paper's regularity, exact-state/adjoint, first-order stationarity, and remainder conditions. | High |
| C2 | The interval indicator supplies a principled location for new-layer insertion. | Author method claim | E3 and E6 | Supported as a computable heuristic derived from the bound; indicator accuracy can degrade away from a local minimum or with coarse state/adjoint discretization. | High |
| C3 | The proposed method achieves the best reported errors among tested strategies. | Author empirical claim | E4-E5 | Supported by Tables 1-2 for the chosen best-validation models. | High |
| C4 | The method is more efficient than alternative adaptation strategies. | Author implication | E4-E6 | Only partially supported. It is parameter-directed, but reported wall-clock time is highest; efficiency depends on the desired error target. | Medium |
| C5 | The estimator bounds generalization error. | Potential overreading | E3-E6 | Not supported. The bound concerns the discretized-vs-continuous objective under stated assumptions; validation and test behavior remain empirical. | High |
| C6 | Error-guided layer insertions can become auditable capacity decisions. | Reviewer interpretation | E2-E8 | Plausible if each indicator, validation delta, cost, and rollback artifact is preserved. This was not directly tested by the paper. | Medium |

## Methodology

- `Research objective`: Expand the selected DEP's older architecture-adaptation thread and determine what the a posteriori estimator actually certifies, what the experiments support, and how the mechanism can become a provenance-preserving capacity decision.
- `Sources inspected`: Both selected source DEP files; the prior DEP-E manuscript; the latest associated log, source report, and Report-Mark; the complete arXiv HTML and canonical record for arXiv:2607.07637v1; full HTML for arXiv:1904.05657; and canonical primary abstracts for arXiv:2311.15995 and arXiv:2502.06885.
- `Discovery strategy`: Repository continuity search followed by an OS-cryptographic draw over ten prior primary reading items; then citation chasing within the selected paper to primary methodological and comparator records.
- `Inclusion criteria`: Primary or near-primary sources that explain the selected estimator, layer-insertion mechanism, experimental comparisons, or direct architecture-growth lineage.
- `Exclusion criteria`: Secondary summaries, unverified code mirrors, and unrelated neural architecture search papers. The other nine source-DEP papers remained continuity context and were not re-inspected in this pass.
- `Analytical approach`: Conceptual, empirical, comparative, implementation, product research, and replication analysis.
- `Evidence handling`: Numerical claims were transcribed from the selected paper's tables and surrounding method text. Author claims, reviewer interpretations, and unsupported overreadings are labeled separately.
- `Uncertainty handling`: Missing code, unreported full-run variance, unequal realized compute, theoretical assumptions, and abstract-only comparator inspection are kept visible.
- `Version control`: The source DEP is pinned to repository commit `c5bcc6a0477f5c3555bc01ccb8d9193dd4b47dac`; the selected paper is arXiv v1.
- `Safety handling`: Implementation paths use public or synthetic regression data and do not require private datasets or autonomous external actions.

## Scope, Constraints, and Assumptions

- `Scope`: The selected source DEP, its prior Constraint-Aware Systems artifact, and the randomly selected error-guided architecture-adaptation thread.
- `Temporal boundary`: Sources were inspected through 2026-08-03; later paper versions, code releases, or peer review may change the assessment.
- `Evidence limits`: No paper code, generated dataset, trained model, seed trace, or benchmark output was collected or executed. Comparator papers S6-S7 were inspected at abstract level only.
- `Assumptions`: The arXiv HTML accurately represents v1 and table runtimes are comparable wall-clock values within the paper's environment.
- `Constraints`: Public evidence only; no local-source redistribution; no claim of independent reproduction.
- `Out of scope`: Proving the theorem independently, recreating Navier-Stokes data, training networks, assessing production-scale architectures, or giving legal/compliance advice.
- `Intended use`: DEP deposition, follow-on replication planning, and design of auditable capacity-growth systems.
- `Audience`: Scientific-ML researchers, architecture-adaptation engineers, reviewers, and DEP maintainers.
- `Reproducibility boundary`: The method and hyperparameters are described, but a paper-specific public implementation was not located and the full stochastic protocol is not reported as a distribution.
- `Data sensitivity`: Public and synthetic research material only.

## Observations

- `Observed pattern`: The paper localizes one specific approximation error, while practical model selection still depends on validation loss. The mathematical and empirical control signals are complementary, not interchangeable.
- `Technical implication`: A useful implementation should log four distinct values per insertion: local indicator, validation delta, test result when available, and added compute.
- `Contradiction or tension`: The theorem assumes first-order stationarity, but the algorithm preserves best-validation checkpoints that may not be training minima; the paper acknowledges this can reduce estimator accuracy.
- `Observed pattern`: The method's strongest empirical advantage occurs at its highest cost. The intermediate checkpoints often offer a better cost-accuracy compromise than the final model.
- `Open question`: Would the interval ranking remain stable across seeds, optimizers, `K` values, or equal-compute training budgets?
- `Reviewer hypothesis`: The estimator may be more valuable as an auditable proposal generator than as an autonomous architecture controller until stability and calibration are measured.

## Considerations

- The estimator should be named precisely in user interfaces: parameter-representation error indicator, not “generalization error” or “uncertainty.”
- `K` requires its own convergence and cost policy. A larger `K` may improve state/adjoint approximation while eliminating the compute savings of targeted growth.
- Validation-based stopping creates repeated-selection pressure. A robust study should reserve a final untouched test set and report the number of adaptation decisions exposed to validation data.
- Best-of-20 initialization selection should be costed and accompanied by full-run variance. Otherwise architecture quality and initialization luck remain entangled.
- Baselines should receive matched wall-clock, optimizer-step, and parameter budgets in addition to same-final-depth comparisons.
- For scientific inverse problems, evaluation should include distribution shift, observation-location changes, noise changes, physical-constraint violations, and uncertainty calibration.
- A public implementation should pin data generation, random seeds, environment, hardware, and expected table outputs before production claims are made.

## Strengths

- The paper connects a concrete architecture decision to a localized mathematical quantity rather than a generic growth heuristic.
- The mechanism, assumptions, interpolation, sub-discretization, insertion rule, and stop condition are all inspectable.
- Tables report both accuracy and runtime, making the trade-off visible rather than hiding the method's extra cost.
- The proof-of-concept and inverse problem test different levels of scientific complexity.
- Remark 5.6 exposes a real theory-to-algorithm mismatch instead of smoothing it over.
- The method naturally produces per-decision provenance that can support rollback and later audit.

## Weaknesses

- The theoretical bound is easy to overread as a generalization guarantee even though it targets a narrower representation error.
- Practical estimator inputs are approximations, and the remainder is not turned into a calibrated decision threshold.
- The selected method is slower than every reported comparator in both tables.
- Reported comparisons use best-validation models, differing early-stop behavior, and differing architecture implementations.
- Full-run mean, variance, confidence intervals, and seed-level results are not reported in the tables.
- Experiments are limited to small-width fully connected networks and synthetic data generation.
- No paper-specific public code repository was located during this pass.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Calibrate indicator rankings across seeds and `K` | Estimator stability | A single argmax may be noise-sensitive | Reliable insertion proposals | Repeated training cost | Rank correlation and insertion agreement across seeds |
| Add equal-compute baselines | Empirical comparison | Current runtimes differ substantially | Clearer efficiency claim | More benchmark runs | Match wall-clock, updates, and parameter count |
| Separate selection and final evaluation | Generalization | Repeated validation decisions can overfit | Cleaner test estimate | Larger data requirement | Nested validation or held-out adaptation audit set |
| Report remainder and approximation diagnostics | Theory-to-code trace | The practical estimator drops or approximates theoretical terms | More honest certification boundary | Instrumentation complexity | Synthetic problems with known continuous solutions |
| Release a pinned reproduction package | Reproducibility | PyTorch use is stated but code was not located | Independent verification | Maintenance burden | One-command table and figure recreation |
| Extend to width and operator structure | Applicability | Depth-only fully connected growth is narrow | Broader architecture control | Theory and implementation expansion | CNN, RNN, operator-learning, and mixed growth benchmarks |

## Potential Implementations

### Error-Guided Capacity Controller

- `User`: Scientific-ML engineer.
- `Goal`: Propose where to add depth while preserving the evidence for each decision.
- `Core mechanism`: Compute interval indicators, propose one insertion, retrain under a fixed budget, and compare validation improvement against cost.
- `Required inputs`: Small residual network, public or synthetic dataset, estimator configuration, validation split, compute budget, and stop rule.
- `Outputs`: Ranked interval indicators, proposed insertion, validation delta, cost delta, and rollback checkpoint.
- `Risk controls`: Human approval, immutable baseline, maximum depth, maximum `K`, held-out final test set, and no automatic promotion on indicator alone.
- `Evaluation`: Seed stability, equal-compute baselines, indicator calibration, and failure-visible logs.

### Architecture Decision Ledger

- `User`: Research reviewer or DEP maintainer.
- `Goal`: Preserve why an architecture changed and what evidence justified it.
- `Core mechanism`: Store each insertion as a claim linked to estimator values, source equations, training configuration, validation outcome, and later replication.
- `Required inputs`: Run metadata, source locators, checkpoints, metrics, and reviewer status.
- `Outputs`: Versioned decision cards, provenance graph, unresolved assumptions, and comparison views.
- `Risk controls`: Explicit claim types, signed source hashes, sanitized paths, reversible revisions, and visible negative results.
- `Evaluation`: Independent reviewer agreement and successful reconstruction of the decision sequence.

### Scientific Inverse-Problem Growth Benchmark

- `User`: Architecture-adaptation researcher.
- `Goal`: Compare growth rules under controlled inverse-problem difficulty.
- `Core mechanism`: Vary observation count, noise, shift, and compute budget across error-guided, sensitivity-guided, random, and fixed-depth strategies.
- `Required inputs`: Synthetic PDE generator, fixed seeds, shared training harness, and public configurations.
- `Outputs`: Cost-accuracy curves, uncertainty, constraint violations, and seed distributions.
- `Risk controls`: Synthetic data, bounded compute, no claims about real physical deployment, and complete failed-run retention.
- `Evaluation`: Pareto performance, reproducibility, shift robustness, and statistical uncertainty.

## Three Ways to Exercise This Research

1. `Indicator audit`: Use a toy two-dimensional regression function, train a three-layer residual network across five fixed seeds, compute interval rankings for `K` in `{2,4,8}`, and compare ranking stability. Output the rank-correlation matrix and stop if rankings are unstable enough that no interval wins a majority of runs.
2. `Equal-compute replay`: Implement random insertion, same-final-depth baseline, and error-guided insertion under one shared wall-clock or update budget. Output cost-accuracy curves rather than a single best score; success requires the guided method to improve the Pareto frontier, and the stop condition is budget exhaustion.
3. `Decision-ledger exercise`: Without training any model, encode the selected paper's proof-of-concept insertions as synthetic decision cards containing indicator, validation delta, runtime, assumption status, and rollback pointer. Success means a second reviewer can distinguish theoretical support from empirical support and identify every unresolved assumption.

## Example MVP Product

- `Product name`: Depth Decision Ledger
- `Target user`: Scientific-ML researchers and model-governance reviewers.
- `Problem`: Architecture-growth tools can add capacity without preserving why the change was proposed, whether it improved validation, or what it cost.
- `Core workflow`: Import a bounded training run; compute or ingest interval indicators; propose one insertion; require reviewer approval; retrain; record validation and cost deltas; retain rollback; publish a sanitized decision card.
- `Data requirements`: Public or synthetic regression data, model checkpoints, estimator arrays, training metrics, fixed seeds, and source citations. Raw private data is excluded from the MVP.
- `Architecture`: Local CLI plus a Markdown/JSON ledger; adapter interface for estimator plugins; immutable artifact store; static comparison dashboard.
- `Success metrics`: 100% of insertions have source, indicator, budget, outcome, and rollback fields; zero promotions occur on indicator alone; seed-stability results are present for every proposal; a second reviewer reconstructs the decision sequence without hidden context.
- `Risk controls`: Local-only default, no credentials in logs, bounded depth and `K`, explicit human approval, held-out final test set, sanitization gate, and failure retention.
- `Limitations`: Does not prove the estimator, guarantee generalization, select production architectures, or handle convolutional/recurrent growth in the first version.
- `MVP boundary`: Synthetic and public small-network experiments only; no autonomous cloud training or external deployment.
- `Deployment model`: Local CLI and static artifact viewer.
- `Evaluation plan`: Golden synthetic cases, malformed-ledger tests, seed-stability checks, equal-compute comparisons, and reviewer reconstruction exercises.
- `Failure modes`: Mislabeling the indicator as uncertainty, validation overfitting, unstable interval ranks, excessive sub-discretization cost, or missing rollback artifacts.
- `Maintenance plan`: Version estimator plugins, schema, dependencies, source pins, and benchmark expectations; revalidate after paper or code updates.

## Related Research and Reading

Iterative expansion note: This pass randomly selected the error-guided neural-depth thread from ten primary items preserved by the prior manuscript. The selected paper and its optimal-control lineage were newly inspected in this pass; the other nine source-DEP research items remain continuity context and were not re-inspected.

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| *An optimal control approach for neural network architecture adaptation with a posteriori error estimation* | Selected primary expansion; **new full inspection in this pass** | Defines the DWR-derived interval indicator, two-level discretization, insertion algorithm, experiments, and limitations | https://arxiv.org/abs/2607.07637 |
| *Deep learning as optimal control problems: models and numerical methods* | Primary methodological context; **new full inspection in this pass** | Establishes the continuous-control, adjoint, and discretization lineage needed to interpret what the selected estimator assumes | https://arxiv.org/abs/1904.05657 |
| *Sensitivity-Based Layer Insertion for Residual and Feedforward Neural Networks* | Direct comparator; **new canonical-record inspection in this pass** | Uses first-order sensitivity to choose insertion opportunities and provides a nearby alternative to error decomposition | https://arxiv.org/abs/2311.15995 |
| *Topological derivative approach for deep neural network architecture adaptation* | Same-author research lineage; **new canonical-record inspection in this pass** | Uses a topological derivative to choose insertion location and initialization, clarifying how the selected method differs | https://arxiv.org/abs/2502.06885 |
| *Constraint-Aware Systems - DEP-E* | Prior Black-Lake continuity artifact | Supplies the ten-paper synthesis and the earlier interpretation of error-guided depth as an auditable constraint signal | https://github.com/Delphoa/Black-Lake/blob/68a04529d6852b5a55f7d9d0cf6fd4dca31bec5f/.lake-data/DEP-E/DEP-E-20260726-Constraint-Aware%20Systems/constraint-aware-systems.md |
| Selected source findings | Source-package continuity | Preserves the original architecture-adaptation finding and the other nine research items not re-inspected in this pass | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/c5bcc6a0477f5c3555bc01ccb8d9193dd4b47dac/.lake-data/DEP-20260709-Tech%20Intel%201305/daily_research_findings_2026-07-09_1305.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/c5bcc6a0477f5c3555bc01ccb8d9193dd4b47dac/.lake-data/DEP-20260709-Tech%20Intel%201305 | Selected DEP contents, inventory, original ten-finding scope, and attribution | 2026-08-03 | Fixed public source snapshot; both Markdown files inspected |
| R2 | https://github.com/Delphoa/Black-Lake/blob/68a04529d6852b5a55f7d9d0cf6fd4dca31bec5f/.lake-data/DEP-E/DEP-E-20260726-Constraint-Aware%20Systems/constraint-aware-systems.md | Prior evidence ledger, cross-domain synthesis, and reading frontier | 2026-08-03 | Prior independent review inspected in full |
| R3 | https://arxiv.org/abs/2607.07637 | Canonical metadata, v1 date, authors, DOI, abstract, and CC BY 4.0 link | 2026-08-03 | Primary canonical record |
| R4 | https://arxiv.org/html/2607.07637v1 | Theory, assumptions, Corollary 5.4, Algorithm 1, experiments, Tables 1-3, conclusion, and references | 2026-08-03 | Primary full HTML inspected; paper-specific code repository not located |
| R5 | https://doi.org/10.48550/arXiv.2607.07637 | Stable identifier for the selected primary paper | 2026-08-03 | DOI locator |
| R6 | https://arxiv.org/abs/1904.05657 | Optimal-control formulation, adjoints, discretization order, and structure-preserving numerical context | 2026-08-03 | Primary full HTML inspected |
| R7 | https://arxiv.org/abs/2311.15995 | Sensitivity-based layer-insertion comparator and linked code availability claim | 2026-08-03 | Primary canonical abstract inspected; code not inspected |
| R8 | https://arxiv.org/abs/2502.06885 | Topological-derivative layer-location and initialization comparator | 2026-08-03 | Primary canonical abstract inspected |
| R9 | `Black-Lake-Data/.reports/BL-DEP-20260709-Tech Intel 1305-20260726/README.md`; `Black-Lake-Data/.lake-data/DEP-20260709-Tech Intel 1305/BL-DEP-Mark001 Report-Mark.md`; `Black-Lake/.logs/20260726-DEP-20260709-Tech Intel 1305-LOG.md` | Prior selection, source considerations, validation gaps, and exact continuity sections | 2026-08-03 | Repository-relative continuity records inspected in full |

## Appendix

### Random selection provenance

- Automation family: `Black-Lake Data Processing & Review` and `Black-Lake Data Processing & Review 0900`.
- Fixed run timestamp: `2026-08-03T00:05:04Z`; 24-hour cutoff: `2026-08-02T00:05:04Z`.
- Canonical candidates: 101; recent-marker exclusions: 1; eligible candidates: 100.
- Excluded candidate: `DEP-20260724-Tech Intel 1305`, whose owned `.reports`, `.logs`, Report-Mark, and output marker carry `2026-08-02T15:07:11Z`.
- Final eligible-list SHA-256: `f7766a5bdda5a80df28d82140306309a0ea3c3a1a7cd026edb5cdbcb0bf2697f`.
- Final DEP draw: OS-cryptographic UInt32 `1855188334`, attempt 1, rejection limit `4294967200`, zero-based index 34, selecting `DEP-20260709-Tech Intel 1305`.
- Two preliminary draws were discarded because their candidate pools failed review: one scanner treated incidental mentions of previously excluded DEPs as owned markers; a second scanner treated a private temporary-directory date as a repository marker. Neither preliminary result was used.
- Iterative expansion pool: ten primary prior-reading items; pool SHA-256 `007c81ffd6ccbf657fec443a63700dfd13157821f85b1546ac42fa91d258d94f`.
- Expansion draw: OS-cryptographic UInt32 `1435401589`, attempt 1, rejection limit `4294967290`, zero-based index 9, selecting arXiv:2607.07637.

### Replication checklist

- Obtain or recreate the selected paper's PyTorch implementation and pin the environment.
- Recreate both synthetic data generators and verify Tables 1-3.
- Record all 20 initialization candidates and repeat complete adaptation across seeds.
- Compare equal-depth, equal-parameter, equal-update, and equal-wall-clock baselines.
- Measure interval-rank stability across `K`, seeds, optimizers, and checkpoint stationarity.
- Separate representation-error diagnostics, validation decisions, and final test estimates.

### Validation gaps

No code, source package, generated dataset, model, benchmark, seed trace, or experiment was executed. The theorem was not independently proved. The selected paper remains arXiv v1; peer-review status and later revisions were not established. Comparator papers S6-S7 were not inspected beyond their canonical records. The cost-accuracy comparison is not compute-normalized, and paper-specific code availability remains unresolved.
