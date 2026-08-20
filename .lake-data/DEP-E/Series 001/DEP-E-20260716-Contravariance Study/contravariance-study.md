---
title: "Contravariance Study - DEP-E"
generated_at: "2026-07-16T11:00:53Z"
artifact_type: "DEP research artifact"
primary_subject: "An iterative source-first expansion of the Contravariance Theory thread preserved by DEP-20260712-Tech Intel 1100."
source_status: "Repository files and public URLs; the selected primary paper was inspected in full through its public PDF."
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "2026-07-16"
primary_url: "https://arxiv.org/abs/2607.08561"
stable_identifier: "DEP-20260712-Tech Intel 1100 / arXiv:2607.08561v1"
confidence_summary: "High for the paper's stated definitions and theorem conditions; medium for translation to modern trained networks because minimality and learning-dynamics assumptions remain empirically unresolved."
safety_scope: "Public research review; no private, clinical, or executable source material."
distribution_notes: "No source paper or repository files were redistributed; public URLs and repository-relative provenance are preserved."
---

# Contravariance Study - DEP-E

## Source Metadata

| ID | Source | Authors / Organization | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|---|
| S0 | DEP-20260712-Tech Intel 1100 | Delphoa-Labs | Selected source bundle | Repository DEP | `main` | [Source DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260712-Tech%20Intel%201100) | Attribution retained; repository files inspected as evidence | 2026-07-16 | README, digest, and prior Report-Mark inspected |
| S1 | Daily Research Findings - 2026-07-12 11:00 | Delphoa-Labs automation deposit | Original ten-item digest | Markdown | Source DEP file | [Digest](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260712-Tech%20Intel%201100/daily_research_findings_2026-07-12_1100.md) | Public repository source | 2026-07-16 | Inspected; describes Contravariance Theory at abstract level |
| S2 | BL-DEP-20260712-Tech Intel 1100-20260713 | Codex | Prior processing report | Markdown | 2026-07-13 report | [Prior report](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.reports/BL-DEP-20260712-Tech%20Intel%201100-20260713/README.md) | Public repository source | 2026-07-16 | Inspected; identifies the previous evidence boundary |
| S3 | BL-DEP-Mark001 Report-Mark | Codex | Prior preserved research sections | Markdown | Mark 001 | [Prior Report-Mark](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260712-Tech%20Intel%201100/BL-DEP-Mark001%20Report-Mark.md) | Public repository source | 2026-07-16 | Inspected; supplied the expansion pool |
| S4 | Tech Intel 1100 - DEP-E | Codex | Prior DEP Class manuscript | Markdown research artifact | Commit `db3a22b` | [Prior manuscript](https://github.com/Delphoa/Black-Lake/blob/db3a22b36676b872fbbcebc069916ac9878f93a3/.lake-data/DEP-E/DEP-E-20260713-Tech%20Intel%201100%20Review/tech-intel-1100-research.md) | Public derived artifact | 2026-07-16 | Inspected; Contravariance Theory was abstract-only in that pass |
| S5 | Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks | Dan Yamins; Aran Nayebi | Randomly selected expansion source | Primary research preprint | arXiv:2607.08561v1 | https://arxiv.org/abs/2607.08561 | arXiv record links the applicable license | 2026-07-16 | Metadata, abstract, and submission history inspected |
| S6 | Contravariance Theory full paper | Dan Yamins; Aran Nayebi | Primary theorem and discussion evidence | Public PDF | arXiv:2607.08561v1, 94 pages | https://arxiv.org/pdf/2607.08561 | Read online; not deposited | 2026-07-16 | Full paper inspected, including main theorems, discussion, limitations, and appendix structure |

No external source files were collected. The public PDF was inspected online and remains at its canonical source.

## Evidence Ledger

| Evidence ID | Source | Evidence Type | Location | Claim / Observation Supported | Directness | Confidence | Notes |
|---|---|---|---|---|---|---|---|
| E0 | S0-S1 | Repository evidence | Source README and finding 3 | The source DEP frames the paper as an alignment framework for minimal solutions to hard tasks | Direct | High | Original summary is brief and does not expose theorem assumptions |
| E1 | S2-S4 | Prior-review evidence | Report, Report-Mark, prior manuscript source table and reference R3 | The first pass inspected arXiv:2607.08561 only at abstract level | Direct | High | Establishes what is new in this pass |
| E2 | S5-S6 | Bibliographic and abstract evidence | arXiv record; PDF abstract and Section 1 | The paper studies when weak affine alignment entails privileged-axis alignment and when terminal alignment propagates upstream | Direct | High | Author framing, not independent empirical validation |
| E3 | S6 | Formal definition | PDF Sections 2-3, Definitions 1-5 | Weak alignment is affine representational equivalence; strong alignment matches native axes up to permitted permutation and scaling | Direct | High | Activation-specific details matter |
| E4 | S6 | Formal theorem | PDF Section 2, Theorem 1 | Adjacent-layer weak equivalence plus task-used axes yields a lower bound on strong axis alignment based on the required used-axis budget | Direct | High | Exact theorem has strong usedness and hardness assumptions |
| E5 | S6 | Formal theorem | PDF Section 3, Theorem 2 | On compact comparison families, shrinking adjacent weak-alignment errors imply asymptotic alignment of task-required axes | Direct | High | The bound depends on comparison-family constants |
| E6 | S6 | Formal theorem | PDF Section 4, Theorems 3-4 | Under minimality and regularity, terminal weak alignment generically zippers upstream; the soft form bounds propagated error | Direct | High | Exact and soft statements are conditional, not universal |
| E7 | S6 | Author limitation | PDF Section 4, pages 11-12 | Real-world use depends on network minimality and on learning dynamics not concentrating on exceptional parameter sets | Direct | High | The authors identify these as future empirical questions |
| E8 | S6 | Author discussion | PDF Sections 5-6, pages 12-15 | Transformer predictions are branch-specific; RSA introduces a multiplicity obstruction; hardness and minimality need measurement | Direct | High | Some architecture extensions are argued rather than demonstrated empirically here |
| E9 | S6 | Reviewer interpretation | Derived from E4-E8 | Contravariance is best treated as a falsifiable conditional research program, not a blanket claim that all capable networks must share coordinates | Interpretive | Medium-High | Keeps theorem scope separate from deployment inference |
| E10 | S0-S4 | Provenance observation | Prior report and manuscript | The earlier source-identity mismatch for arXiv:2607.04595 remains a separate unresolved source-deposit defect | Direct | High | This pass does not rewrite the stable source deposit |

## Executive Summary

This iterative pass expands one randomly selected thread from the prior DEP Class artifact: `arXiv:2607.08561`, *Contravariance Theory*. The earlier review had verified only its abstract. Full-paper inspection shows that the work is a conditional mathematical account of representational convergence. It distinguishes weak alignment, where two layer representations agree through an injective affine map, from strong alignment, where task-used native axes correspond up to activation-appropriate permutation and scaling. Under explicit hardness, usedness, minimality, compactness, and regularity assumptions, the paper proves exact and soft forms of weak-to-strong equivalence and upstream alignment “zippering.”

The important research result is not that any two trained systems must converge. It is that certain nonlinear signatures make alternative minimal solutions identifiable when the task forces those signatures to be used. The practical research agenda is therefore empirical: estimate the used-axis budget, test minimality and Jacobian regularity, measure whether learning dynamics approach exceptional failure sets, and compare the paper's bounds with observed alignment. For transformers, the paper predicts weak alignment in residual streams while stronger privileged structure should be sought in MLP hidden axes and gauge-invariant attention-head signatures.

The manuscript preserves the source DEP's complete related-reading graph, marks the Contravariance paper as newly inspected in full, and carries forward the previously detected arXiv:2607.04595 source-identity defect without silently correcting historical material.

## Detailed Summary

### Research question and conceptual move

The paper asks why independently trained networks, and sometimes task-optimized networks compared with biological systems, exhibit both broad representational similarity and finer privileged-axis structure. Its contravariance principle says that stronger task constraints reduce the space of acceptable solutions. The formal contribution is to identify conditions under which coarse affine similarity cannot coexist with arbitrary native axes after task-visible nonlinearities.

### Weak and strong alignment

Weak alignment compares representations through an injective affine map. Strong alignment requires a coordinate-level correspondence, with ReLU axes allowed nonzero rescaling and Softplus axes restricted more tightly. The key mechanism is preservation of nonlinear signatures: a used ReLU axis creates a task-visible kink, while a used Softplus axis creates curvature structure. If representations are weakly aligned on both sides of a used nonlinearity, those signatures constrain how axes can be mixed.

### Task hardness and the used-axis budget

The paper defines a required used-axis budget, `m_l(epsilon)`, as the minimum number of nonlinear axes needed at a layer to solve the task within a loss threshold. The exact weak-strong theorem lower-bounds the aligned-axis fraction by this required budget divided by layer width. This makes the paper's “hard task” concept layer-specific and operational in principle. It does not equate hardness with parameter count or benchmark reputation.

### Asymptotic alignment and zippering

The asymptotic theorem replaces exact equality with weak-alignment errors on a compact family. As those errors shrink across adjacent layers, task-required axes must become approximately aligned. The zippering results go further: if two minimal networks agree weakly at a terminal layer, one-step identifiability can propagate alignment backward. A soft theorem introduces Jacobian-regularity constants controlling how terminal mismatch can amplify upstream.

### Application boundary

The theory is strongest for transparent affine-ReLU and affine-Softplus blocks. The paper discusses CNNs, ResNets, RNNs, and transformers, but real-world applicability still depends on measurable conditions. It explicitly notes that optimized parameters are not uniformly distributed, so measure-zero genericity in parameter space does not by itself establish that trained systems avoid exceptional sets. It also leaves architecture-specific constants uncalculated and calls for empirical alignment, pruning, ablation, bottleneck, and width-restricted retraining studies.

### New material in this pass

Relative to the 2026-07-13 artifact, this pass adds full-paper evidence for Definitions 1-5, Theorems 1-4, the task-used-axis budget, the exact and soft zippering mechanisms, the transformer branch-specific prediction, the RSA multiplicity obstruction, and the paper's stated empirical gaps. No numerical or biological claim was independently reproduced.

## Key Claims and Evidence

| Claim ID | Claim | Classification | Evidence | Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Under the paper's adjacent-layer weak-equivalence and usedness conditions, task-used nonlinear axes must be strongly matched. | Author theorem claim | E3-E4 | Supported as a formal result within the stated model classes and assumptions | High |
| C2 | Shrinking weak-alignment error can force approximate privileged-axis alignment on compact comparison families. | Author theorem claim | E5 | Supported conditionally; constants and real-network fit remain unmeasured | High for theorem, Medium for application |
| C3 | Minimal one-step expansions make terminal equivalence generically identifiable upstream, producing zippering. | Author theorem claim | E6 | Supported conditionally for the formal setup; soft use also requires regularity | High for theorem, Medium for application |
| C4 | Genericity in parameter space is insufficient evidence that optimization avoids exceptional failure sets. | Author limitation and reviewer emphasis | E7 | Directly acknowledged by the paper and central to responsible interpretation | High |
| C5 | Transformer alignment tests should distinguish residual-stream weak alignment from branch-level strong structure. | Author architectural extension | E8 | Plausible and theory-guided, but requires targeted empirical validation | Medium |
| C6 | The theory should be operationalized as assumption checks and falsification tests, not as an unconditional convergence guarantee. | Reviewer interpretation | E4-E9 | Best-supported translation because every major result is conditional | Medium-High |
| C7 | The source DEP's arXiv:2607.04595 mismatch remains unresolved and should not be erased by this expansion. | Reviewer provenance observation | E10 | Directly supported by prior source comparison | High |

## Methodology

- `Research objective`: Expand one preserved research thread from a prior DEP Class artifact while maintaining complete provenance and clearly separating new evidence.
- `Selection method`: A uniform PowerShell `Get-Random` draw from the ten items in the prior manuscript's `Related Research and Reading` section selected `arXiv:2607.08561`.
- `Sources inspected`: The selected source DEP README and digest; the latest prior source report and Report-Mark; the latest prior Black-Lake log and manuscript; the arXiv metadata page; and the complete 94-page public PDF.
- `Discovery strategy`: Repository-first inspection followed by direct primary-source inspection. No recommender output or secondary summary was used as central evidence.
- `Inclusion criteria`: Formal definitions, theorem statements, assumptions, author-identified limitations, architectural extensions, and future-work items relevant to testable representational alignment.
- `Exclusion criteria`: Unverified secondary interpretations, citation-only empirical claims, and claims requiring code, model, neural data, or experiment reproduction.
- `Analytical approach`: Formal-claim reconstruction, assumption mapping, evidence-boundary comparison with the prior artifact, and implementation translation.
- `Evidence handling`: Stable S, E, C, and R identifiers connect sources to claims. Author claims, reviewer observations, and inferences are labeled separately.
- `Uncertainty handling`: Theorems receive high confidence only within their stated conditions. Real-network and biological implications are downgraded until minimality, regularity, and learning-dynamics assumptions are tested.
- `Extraction process`: Repository Markdown was read directly; the arXiv record and complete PDF text were inspected by section and page locator.
- `Version control`: The source is pinned to arXiv:2607.08561v1 and the previous artifact to its public commit.
- `Cross-checking`: The source digest, prior manuscript status, arXiv record, PDF title, authors, version, definitions, theorem summaries, and discussion were compared.
- `Reviewer stance`: Preserve formal scope, surface falsifiable conditions, and avoid converting mathematical genericity into an empirical inevitability claim.

## Scope, Constraints, and Assumptions

- `Scope`: The Contravariance Theory thread inside `DEP-20260712-Tech Intel 1100`, with prior context retained for iterative expansion.
- `Temporal boundary`: Repository and public sources accessed 2026-07-16; the reviewed paper is arXiv v1 submitted 2026-07-09.
- `Evidence limits`: No proof was independently formalized in a theorem prover; no model, neural dataset, code, or alignment metric was executed.
- `Assumptions`: The canonical arXiv record and public PDF represent v1; public repository history is the durable prior-review record.
- `Constraints`: Public evidence only; no paper redistribution; no biological or product efficacy claims.
- `Out of scope`: Independent proof verification, empirical replication, brain-data analysis, training-dynamics experiments, and correction of the original DEP.
- `Intended use`: Research planning, DEP expansion, experiment design, and provenance-preserving review.
- `Audience`: NeuroAI researchers, representation-analysis engineers, model evaluators, and research repository maintainers.
- `Reproducibility boundary`: Readers can audit the cited definitions and theorem statements, but cannot reproduce empirical alignment from this manuscript alone.
- `Data sensitivity`: Public research metadata and public repository content only.

## Observations

- The paper's most useful operational variable is not total parameter count but the layer-specific fraction `m_l(epsilon) / d_l` of axes forced into use by the task.
- Exact, asymptotic, and soft results form a confidence ladder: equality under ideal assumptions, convergence on compact families, then quantitative propagation under regularity.
- “Generic” means outside lower-dimensional exceptional sets in the modeled parameter space; it does not establish the distribution induced by gradient-based learning.
- Transformer claims are structurally differentiated: residual coordinates may lack privileged axes even if MLP axes or attention-head signatures align.
- RSA can disagree with weak or strong alignment because representational-axis multiplicity changes dissimilarity matrices.
- The prior manuscript correctly treated this paper as abstract-only; this pass materially increases evidence depth without claiming reproduction.

## Considerations

- A task-hardness score must be estimated rather than inferred from task labels or model scale.
- Pruning and ablation can alter the very representations being measured; interventions need calibration and held-out checks.
- Alignment maps can overfit finite stimulus sets, so train/test separation is necessary for any empirical probe.
- Biological comparison requires measurement-noise models, cross-subject variability, and controls for dimensionality.
- Soft zippering constants may be too loose for practical prediction until architecture-specific bounds are calculated.
- Learning dynamics could favor degeneracies that occupy little ambient parameter volume; optimization-aware sampling is essential.
- Branch-aware transformer analysis must respect attention gauge and distinguish head signatures from arbitrary residual coordinates.
- The unresolved arXiv:2607.04595 source mismatch should receive a stable correction note in a separate pass rather than a history rewrite.

## Strengths

- The paper turns a broad convergence intuition into explicit definitions, assumptions, and theorem families.
- It connects local nonlinear signatures with global hierarchical alignment through an identifiable mechanism.
- Exact and approximate versions prevent the contribution from depending only on perfect representational equality.
- The discussion surfaces real applicability gaps instead of presenting genericity as complete empirical validation.
- The transformer treatment predicts where privileged structure should and should not be sought.
- The public arXiv record and full PDF support durable claim-level auditing.

## Weaknesses

- The main claims remain uncalibrated against new empirical experiments in this paper.
- Minimality and the used-axis budget are difficult to estimate in modern networks and biological systems.
- Architecture-specific constants in the soft bounds are not calculated.
- Measure-zero exception arguments do not model the trained-parameter distribution.
- The strongest clean results use affine-ReLU or affine-Softplus blocks; broader architectures require additional structure.
- The appendix is extensive and technically dense, raising the verification burden for downstream reviewers.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish executable theorem-condition checklists | Applicability | Formal assumptions are distributed across definitions and appendices | Faster, less error-prone empirical translation | Risk of oversimplifying proofs | Cross-audit checklists against each formal theorem |
| Estimate used-axis budgets on controlled networks | Task hardness | The central hardness variable is currently unmeasured | Connect bounds to observable model behavior | Ablation artifacts and compute cost | Width sweeps, pruning curves, and held-out loss thresholds |
| Calculate architecture-specific soft constants | Quantitative prediction | Theoretical bounds cannot yet be compared directly with data | Falsifiable numerical predictions | Bounds may be vacuous | Compare predicted and observed layerwise errors |
| Model optimization-induced parameter distributions | Genericity | Ambient measure does not reflect trained solutions | Tests whether exceptional sets attract learning | Requires many seeds and optimizer controls | Seeded training study with degeneracy diagnostics |
| Add branch-aware transformer benchmarks | Architecture extension | Residual and branch predictions differ | Avoid false negative axis-alignment conclusions | Gauge handling is complex | Compare residual, MLP, and attention signatures across seeds |
| Machine-check a bounded theorem subset | Proof assurance | The proof surface is large | Independent assurance for core lemmas | High formalization effort | Formalize definitions and one exact weak-strong case |

## Potential Implementations

### Contravariance condition probe

- `User`: Representation-analysis researcher.
- `Goal`: Determine whether a trained network pair is plausibly inside a theorem's applicability envelope.
- `Core mechanism`: Measure adjacent weak alignment, identify task-visible nonlinear axes, estimate used-axis fractions, and report regularity diagnostics.
- `Required inputs`: Two version-pinned models, a held-out task dataset, layer mappings, and a declared loss threshold.
- `Outputs`: Layerwise assumption matrix, alignment curves, uncertainty intervals, and explicit failure reasons.
- `Risk controls`: Held-out fitting, permutation baselines, bounded model execution, and no promotion of empirical fit to proof.
- `Evaluation`: Synthetic networks with known symmetries, seeded controls, and negative cases containing duplicate or unused axes.

### Task hardness estimator

- `User`: NeuroAI experimental designer.
- `Goal`: Approximate the required used-axis budget for candidate tasks.
- `Core mechanism`: Combine width-restricted retraining, structured pruning, and ablation curves at fixed loss tolerances.
- `Required inputs`: Task specification, training pipeline, architecture family, compute budget, and performance thresholds.
- `Outputs`: Estimated `m_l(epsilon) / d_l` ranges with sensitivity analyses.
- `Risk controls`: Predeclare thresholds, separate optimization failure from representational necessity, and retain all negative runs.
- `Evaluation`: Recover known budgets on constructed tasks before applying to naturalistic tasks.

### Branch-aware transformer aligner

- `User`: LLM interpretability engineer.
- `Goal`: Test the paper's distinction between residual weak alignment and branch-specific strong structure.
- `Core mechanism`: Fit held-out affine maps on residual streams, permutation/scale matches on MLP axes, and gauge-invariant comparisons on attention heads.
- `Required inputs`: Compatible open-weight models, activation traces, tokenizer alignment, and matched task prompts.
- `Outputs`: Depth-warped alignment map, branch-specific scores, and null-baseline comparisons.
- `Risk controls`: No sensitive prompts, fixed model revisions, bounded activation storage, and explicit gauge conventions.
- `Evaluation`: Same-architecture seed pairs, cross-width pairs, randomized-axis controls, and ablated branches.

## Three Ways to Exercise This Research

1. `Test weak-to-strong collapse`: Objective - test Theorem 1's empirical signature; inputs - two small ReLU networks trained on the same constructed task; method - fit held-out affine maps before and after a used nonlinear layer and compare native axes; output - weak errors, axis matches, and usedness diagnostics; success criterion - axis alignment rises with the estimated used-axis budget; stop condition - halt interpretation if maps fail held-out validation.
2. `Probe optimization exceptional sets`: Objective - determine whether learning dynamics approach degeneracies; inputs - many controlled training seeds and optimizer variants; method - track duplicate axes, vanishing outgoing weights, Jacobian conditioning, and zippering error; output - parameter-distribution diagnostics; success criterion - stable estimates with negative controls; stop condition - do not generalize if optimizer and initialization effects dominate.
3. `Separate transformer streams and branches`: Objective - test the branch-specific prediction; inputs - two version-pinned transformer models and matched prompts; method - compare residual affine alignment, MLP axis matching, and gauge-invariant head signatures by relative depth; output - branch-aware alignment atlas; success criterion - predeclared metrics distinguish residual and branch behavior beyond shuffled baselines; stop condition - reject conclusions when token or layer correspondence is underdetermined.

## Example MVP Product

- `Product name`: ContraProbe
- `Target user`: Research engineer studying representation convergence.
- `Problem`: Alignment results are often reported without checking the conditions that make coordinate-level conclusions meaningful.
- `Core workflow`: Select two local models and a public task fixture, declare layer correspondences and a loss threshold, collect bounded activations, fit held-out weak maps, run usedness and regularity diagnostics, then generate a claim-bounded Markdown report.
- `Data requirements`: Public or approved task examples, local model activations, model revision metadata, and declared layer mappings.
- `Architecture`: Local Python CLI, adapter registry for small ReLU networks and transformers, memory-bounded activation sampler, deterministic metric engine, and Markdown/JSON reporter.
- `Success metrics`: Detect seeded duplicate/unused-axis failures, separate held-out alignment from overfit maps, reproduce constructed positive controls, and emit zero unconditional theorem claims.
- `Risk controls`: No remote code execution, allowlisted model loading, bounded samples, sanitized logs, explicit data sensitivity flags, and human review before publication.
- `Limitations`: Cannot prove network minimality; task-hardness estimates depend on interventions; transformer gauges and width mismatch can make comparisons ambiguous.
- `MVP boundary`: Small local ReLU networks plus residual/MLP analysis for one open transformer family; no brain data and no training at frontier scale.
- `Deployment model`: Local-only research CLI with reproducible configuration files.
- `Evaluation plan`: Unit tests for affine-map fitting, synthetic symmetry fixtures, held-out leakage tests, randomized-axis baselines, and manual review of generated claim labels.
- `Failure modes`: Map overfitting, activation misalignment, degenerate axes, ill-conditioned Jacobians, false correspondence across depth, and unjustified extrapolation from toy tasks.
- `Maintenance plan`: Pin metric definitions, retain synthetic fixtures, version model adapters, and review the paper's subsequent versions or empirical follow-ups.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks | Primary preprint - **newly expanded in this pass** | Full PDF inspected for definitions, Theorems 1-4, transformer predictions, assumptions, and future work | https://arxiv.org/abs/2607.08561 |
| Tech Intel 1100 - DEP-E | Prior DEP research artifact | Establishes the earlier abstract-only evidence boundary and the ten-item semantic context | https://github.com/Delphoa/Black-Lake/blob/db3a22b36676b872fbbcebc069916ac9878f93a3/.lake-data/DEP-E/DEP-E-20260713-Tech%20Intel%201100%20Review/tech-intel-1100-research.md |
| Ideas Have Genomes | Primary preprint | Structured scientific-lineage reasoning and generation benchmark; carried forward from the prior pass | https://arxiv.org/abs/2607.08758 |
| BiSCo-LLM | Primary preprint | Storage-aware extreme low-bit compression; carried forward from the prior pass | https://arxiv.org/abs/2607.08643 |
| Stop Guessing When to Stop Testing | Primary preprint | Sequential stopping for statistically grounded model evaluation; carried forward from the prior pass | https://arxiv.org/abs/2607.08522 |
| MatBind | Primary preprint | Cross-modal materials representation anchored on crystal structure; carried forward from the prior pass | https://arxiv.org/abs/2607.08470 |
| Workload-Preserving DP Synthetic Data | Primary preprint | Causal workloads and noise-aware inference under differential privacy; carried forward from the prior pass | https://arxiv.org/abs/2607.08122 |
| Score Distributions, Not Cells | Primary preprint | Correct primary work for arXiv:2607.04595; preserved because it conflicts with the source DEP description | https://arxiv.org/abs/2607.04595 |
| Storage-Centric Genomic Analysis | Primary preprint | Data-movement and preparation bottlenecks in genomic systems; carried forward from the prior pass | https://arxiv.org/abs/2607.02552 |
| Parallel QEC Decoding | Primary preprint | Parallel decoding design for distributed quantum computing; carried forward from the prior pass | https://arxiv.org/abs/2607.08386 |
| Works on My QPU | Primary preprint | Empirical quantum-research reproducibility study; carried forward from the prior pass | https://arxiv.org/abs/2607.08348 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R0 | [DEP-20260712-Tech Intel 1100](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260712-Tech%20Intel%201100) | Original inventory, summaries, attribution, and Report-Mark | 2026-07-16 | Selected source DEP; all repository files inspected |
| R1 | [Prior source report](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.reports/BL-DEP-20260712-Tech%20Intel%201100-20260713/README.md) | Previous processing scope and evidence boundary | 2026-07-16 | Inspected before expansion |
| R2 | [Prior Black-Lake log](https://github.com/Delphoa/Black-Lake/blob/main/.logs/20260713-DEP-20260712-Tech%20Intel%201100-LOG.md) | Previous selection, validation, questions, and challenges | 2026-07-16 | Inspected before expansion |
| R3 | [Prior manuscript](https://github.com/Delphoa/Black-Lake/blob/db3a22b36676b872fbbcebc069916ac9878f93a3/.lake-data/DEP-E/DEP-E-20260713-Tech%20Intel%201100%20Review/tech-intel-1100-research.md) | Prior synthesis and abstract-only status of Contravariance Theory | 2026-07-16 | Public commit-pinned artifact |
| R4 | [arXiv:2607.08561v1 record](https://arxiv.org/abs/2607.08561) | Canonical title, authors, abstract, version, and submission date | 2026-07-16 | Primary record inspected |
| R5 | [arXiv:2607.08561v1 PDF](https://arxiv.org/pdf/2607.08561) | Definitions, Theorems 1-4, formal assumptions, discussion, empirical boundary, and future work | 2026-07-16 | **New full-paper source in this pass**; inspected online, not collected |
| R6 | [arXiv:2607.08758](https://arxiv.org/abs/2607.08758) | Ideas Have Genomes related thread | 2026-07-16 | Preserved from prior related-reading graph; not re-reviewed in full this pass |
| R7 | [arXiv:2607.08643](https://arxiv.org/abs/2607.08643) | BiSCo-LLM related thread | 2026-07-16 | Preserved from prior related-reading graph; not re-reviewed in full this pass |
| R8 | [arXiv:2607.08522](https://arxiv.org/abs/2607.08522) | Adaptive evaluation related thread | 2026-07-16 | Preserved from prior related-reading graph; not re-reviewed in full this pass |
| R9 | [arXiv:2607.08470](https://arxiv.org/abs/2607.08470) | MatBind related thread | 2026-07-16 | Preserved from prior related-reading graph; not re-reviewed in full this pass |
| R10 | [arXiv:2607.08122](https://arxiv.org/abs/2607.08122) | Differential-privacy related thread | 2026-07-16 | Preserved from prior related-reading graph; not re-reviewed in full this pass |
| R11 | [arXiv:2607.04595](https://arxiv.org/abs/2607.04595) | Correct identity for the mismatched source item | 2026-07-16 | Provenance defect carried forward; not re-reviewed in full this pass |
| R12 | [arXiv:2607.02552](https://arxiv.org/abs/2607.02552) | Storage-centric genomics related thread | 2026-07-16 | Preserved from prior related-reading graph; not re-reviewed in full this pass |
| R13 | [arXiv:2607.08386](https://arxiv.org/abs/2607.08386) | Parallel QEC related thread | 2026-07-16 | Preserved from prior related-reading graph; not re-reviewed in full this pass |
| R14 | [arXiv:2607.08348](https://arxiv.org/abs/2607.08348) | Quantum reproducibility related thread | 2026-07-16 | Preserved from prior related-reading graph; not re-reviewed in full this pass |

## Appendix

### Iterative expansion record

- Candidate expansion pool: ten primary publications preserved in the prior manuscript's `Related Research and Reading` section.
- Random method: uniform PowerShell `Get-Random` draw.
- Selected item: `arXiv:2607.08561 - Contravariance Theory`.
- Accessibility: the canonical record and complete 94-page PDF were accessible, so no redraw was required.
- New evidence: full definitions, theorem statements, assumptions, architectural discussion, empirical boundary, and future-work agenda.

### Source inventory and collection status

- Source repository files inspected: `Black-Lake-Data/.lake-data/DEP-20260712-Tech Intel 1100/README.md`, its daily findings digest, and `BL-DEP-Mark001 Report-Mark.md`.
- Prior processing material inspected: the 2026-07-13 source report, Black-Lake log, and DEP-E manuscript.
- External source files collected: none.
- Public source inspected in full: `https://arxiv.org/pdf/2607.08561`.
- Reproduction status: no proofs, models, datasets, metrics, or experiments were independently executed.

### Validation checklist

- [x] New full-paper evidence is marked explicitly.
- [x] Prior related research and source provenance are retained.
- [x] Author claims, reviewer observations, and reviewer interpretations are separated.
- [x] The prior source-identity defect is preserved without rewriting history.
- [x] No private execution context or local filesystem locator is published.
- [ ] Independently formalize or empirically test the theorem assumptions.
