---
title: "Dynamical Dictionary - DEP-E"
generated_at: "2026-07-13 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of local dictionary learning through feedback-augmented dynamical spiking networks."
source_status: "private local PDF reviewed; public URLs recorded; no source file redistributed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-13"
temporal_cutoff: "arXiv:1805.08952v1 submitted 2018-05-23; public sources accessed on the date-only run marker"
primary_url: "https://arxiv.org/abs/1805.08952"
stable_identifier: "arXiv:1805.08952v1; DOI:10.48550/arXiv.1805.08952"
confidence_summary: "High for identity, method transcription, experimental setup, and reported values; medium for theorem interpretation; low for reproducibility and hardware-efficiency claims."
safety_scope: "non-sensitive research review with synthetic and evaluation-oriented implementation ideas"
distribution_notes: "No private archive file is redistributed; public source URLs and repository-relative related records are preserved."
---

# Dynamical Dictionary - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Reference | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:1805.08952v1 | https://arxiv.org/abs/1805.08952 | arXiv exposes a non-exclusive distribution license; no redistribution permission for the private copy is inferred. | 2026-07-13 | Inspected |
| S2 | Dictionary Learning by Dynamical Neural Networks | Primary paper | PDF | arXiv:1805.08952v1 | https://arxiv.org/pdf/1805.08952 | Private archived copy inspected; not copied into this DEP. | 2026-07-13 | Full text inspected |
| S3 | arXiv experimental HTML | Primary full text | HTML | arXiv:1805.08952v1 | https://arxiv.org/html/1805.08952 | Public HTML used to cross-check sections, theorem statements, and figure captions. | 2026-07-13 | Inspected |
| S4 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.1805.08952 | https://doi.org/10.48550/arXiv.1805.08952 | arXiv-issued DOI. | 2026-07-13 | Recorded |
| S5 | ICLR 2019 OpenReview locator | Conference-version context | Forum/PDF locator | B1gstsCqt7 | https://openreview.net/forum?id=B1gstsCqt7 | Official locator identifies the conference title Sparse Dictionary Learning by Dynamical Neural Networks; interactive access was challenge-blocked. | 2026-07-13 | Locator inspected; deeper record unavailable |
| S6 | Private archive metadata | Selection provenance | Readme/PDF presence | arXiv:1805.08952 | Location withheld | Local identity and PDF presence observed; no local path or source file is public. | 2026-07-13 | Observed |
| S7 | Black Lake README | Repository authority | Markdown | live main | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public repository policy. | 2026-07-13 | Fetched and inspected |
| S8 | Black-Lake-Data README | Related repository authority | Markdown | live main | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public related-repository policy. | 2026-07-13 | Fetched and inspected |
| S9 | Deep ESN Memory DEP-E | Related processed research | Markdown | DEP-E-20260710-Deep ESN Memory | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260710-Deep%20ESN%20Memory | Context only; not validation evidence for the selected paper. | 2026-07-13 | Inspected |
| S10 | 2D-RC OTFS DEP-E | Related processed research | Markdown | DEP-E-20260709-2D-RC OTFS | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260709-2D-RC%20OTFS | Context only; not validation evidence for the selected paper. | 2026-07-13 | Inspected |
| S11 | SMES Expert Sparsity DEP-E | Related processed research | Markdown | DEP-E-20260713-SMES Expert Sparsity | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260713-SMES%20Expert%20Sparsity | Context only; not validation evidence for the selected paper. | 2026-07-13 | Inspected |

**Work identity.** Dictionary Learning by Dynamical Neural Networks is authored by Tsung-Han Lin and Ping Tak Peter Tang of Intel Corporation. arXiv records it as version 1, submitted 2018-05-23, in cs.LG and stat.ML. The official OpenReview locator exposes an ICLR 2019 conference version under the title Sparse Dictionary Learning by Dynamical Neural Networks. The selected source for substantive review is arXiv:1805.08952v1; review-thread content was not available from the challenge-blocked OpenReview interface.

**Availability.** arXiv exposes PDF, HTML, TeX-source, and DOI locators. The inspected paper text contains no official code or data repository link, and the arXiv record does not expose an author-designated implementation. No code availability or reproducibility claim is inferred.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Primary metadata and DOI | Title, authors, categories, submission date, version, abstract, DOI, and public source locators. | Work identity and high-level contribution. | High | Abstract-level evidence does not validate experiments. |
| E2 | S2, sections 1–3 | Primary full text | Local-information constraint, sparse-coding objective, feedback topology, two-phase dynamics, gradient relationships, and update rules. | Mechanism and contribution analysis. | High for source reporting | Equations and proofs were not independently implemented or formally verified. |
| E3 | S2, appendix B | Primary full text | Limit-point, approximate sparse-coding, and contrastive-gradient theorem statements and proofs. | Theoretical basis and conditions. | Medium-high | Review is interpretive; some claims are asymptotic and conditional. |
| E4 | S2, sections 3.3–4.2 and Figures 2–4 | Primary full text | Stability caveat, finite execution window, weight consistency, dataset configurations, 10,000-sample test set, and SGD comparison. | Experimental setup, author-reported convergence, and limitations. | High for transcription; low for reproduction | Plot traces are not accompanied by raw tables, variance, seeds, or code. |
| E5 | S2, appendix D and Figure 7 | Primary full text | Learned-dictionary visual descriptions and Lena denoising from 18.69 dB to 29.31 dB with 5.9 active coefficients per patch on average. | Auxiliary application evidence. | High for reported values | Single-image demonstration; no broader denoising benchmark. |
| E6 | S3 | Primary HTML full text | Cross-check of theorem wording, equations, method sections, figure captions, and conclusion. | Textual validation of E2–E5. | High | HTML notation can be flattened or incomplete. |
| E7 | S5 | Official publication locator | ICLR 2019 conference-paper header and changed title. | Publication context. | Medium | Challenge prevented inspection of reviews, decision metadata, and revisions. |
| E8 | S6 | Private selection evidence | Nearby readme identity and archived PDF presence; pypdf extraction produced 60,252 bytes of text. | Selection provenance and source-processing status. | High | Private path withheld; local HTML and source package absent. |
| E9 | S9–S11 | Related processed DEP records | Reservoir memory, geometry-aware dynamical learning, and sparse systems efficiency. | Cross-DEP synthesis and implementation transfer. | Medium | Related records do not validate selected-paper claims. |
| E10 | S7–S8 | Repository authority | DEP class, path, inventory, stability, attribution, and commit-message rules. | Artifact construction and validation. | High | Process evidence only. |

## Executive Summary

Dictionary Learning by Dynamical Neural Networks asks whether a distributed dynamical network can learn a non-negative sparse dictionary while respecting a strict locality constraint: each neuron may use only its own state, locally stored incoming weights, and the spikes it receives. Existing locally competitive networks can perform sparse coding when weights are derived from a fixed global dictionary, but that construction does not give each neuron the reconstruction gradient or a local way to preserve global weight consistency as the dictionary changes.

The authors introduce top-down feedback from coding neurons to input neurons and a contrastive two-phase procedure. The network first runs without feedback and then with a positive feedback perturbation. Differences between long-time spike rates approximate the reconstruction error needed for dictionary-gradient updates and the mismatch signal needed to keep the lateral matrix H close to the product FB. Feedforward and feedback matrices are updated symmetrically, and a local catch-up rule adjusts H. Theoretical analysis connects the network's limit-point conditions to the KKT conditions for non-negative l1 sparse coding and derives the limiting-state relationships used by the learning rule.

The numerical study covers Lena patches, MNIST, and whitened natural scenes. The authors report that the spiking learner reaches similar or better test-objective values than the displayed stochastic-gradient baselines, learns from both consistent and asymmetric initial weights, and yields recognizable dictionary atoms. The appendix reports a Lena denoising example whose PSNR rises from 18.69 dB to 29.31 dB. Confidence is high that this artifact preserves the source's method, setup, and stated results. Confidence is low that the paper establishes practical energy or throughput superiority: it provides no official implementation, raw measurements, hardware prototype, energy accounting, or matched systems benchmark.

## Detailed Summary

### Problem and Motivation

Sparse coding represents an input using a small number of dictionary atoms. The paper focuses on a non-negative objective combining squared reconstruction error, an l1 sparsity penalty, and Frobenius regularization of the dictionary. For a fixed dictionary, a locally competitive dynamical network can map its long-time activity to a sparse-coding solution. The learning problem is harder because the required feedforward, feedback, and lateral relationships change with the dictionary.

The paper's computational model maps neurons to parallel processing elements with private local memory. A neuron stores incoming weights and receives one-bit spike events. This model motivates two requirements: the learning signal must be locally computable, and the network must preserve enough global consistency without giving any neuron the whole dictionary.

### Network and Sparse-Coding Objective

The proposed topology has input neurons and coding neurons. Coding neurons receive feedforward signals through F, inhibit one another through W, and use thresholds represented through a diagonal matrix. The combined coding-layer structure is H = W + Theta. Input neurons receive the external signal and feedback from the coding layer through B, scaled by a feedback parameter gamma.

When gamma is zero and the matrices satisfy F-transpose = B = D and H = FB = D-transpose D, the coding activities reproduce the non-negative sparse-coding optimality conditions. The analysis extends the ideal case by arguing that long-time average spike rates remain close to a solution for a nearby sparsity scaling when H is only close to FB.

### Two-Phase Local Gradient Mechanism

Each training step runs the network twice: once with gamma = 0 and once with gamma = kappa greater than zero. The difference between input-layer spike rates in the two phases approximates the reconstruction residual B a minus x. That residual, paired with locally observed coding activity, supplies the terms needed to update one row of F or B at the neuron that owns it.

A second limiting-state expression approximates the mismatch between H and FB. Each coding neuron can use that signal and the local coding rate to adjust its row of H. The paper interprets this as a catch-up correction because H follows changes previously made to F and B. It reports that a lateral learning rate near 15 times the dictionary learning rate works well in practice. Weight decay and a scaling vector derived from the diagonal of H discourage dictionary atoms from collapsing to zero or growing without control.

### Algorithmic Flow

For each sampled input, the system runs the normal and perturbed sparse-coding phases, derives local difference signals, updates F, B, and H, projects weights into the non-negative region, and refreshes the scaling vector. Feedforward and feedback updates are constructed to preserve their symmetry. The paper also argues that weight decay can reduce an initial F-versus-B asymmetry geometrically.

### Experiments

The three reported workloads are:

- 100,000 randomly sampled 8-by-8 grayscale Lena patches for a 256-atom dictionary.
- 50,000 28-by-28 MNIST images for a 512-atom dictionary.
- 200,000 randomly sampled 16-by-16 whitened natural-scene patches for a 1,024-atom dictionary.

Lena and natural-scene patches are mean-adjusted, normalized, and split into positive and negative channels to produce non-negative inputs. Each example runs gamma = 0 from time 0 to 20 and gamma = 0.7 from time 20 to 40, with a discrete step of 1/32. The paper says the resulting spike-rate precision of about 0.05 is sufficient in practice despite the asymptotic analysis.

Two initializations are tested: weights fully consistent with a random dictionary and randomly asymmetric weights. Weight-consistency and symmetry plots show that the local corrections move the network toward the intended relationships. The objective comparison uses batch size one, a separate 10,000-sample test set, and several SGD learning-rate settings. The authors report convergence to similar or better objectives across the datasets and slower convergence from asymmetric weights. Because the curves are plotted without raw tables, seeds, uncertainty, or a released implementation, this artifact treats the comparison as author-reported qualitative evidence.

The appendix visualizes expected edge, stroke, digit-part, and Gabor-like atoms. A Lena denoising demonstration uses overlapping 8-by-8 patches, Gaussian corruption, sparse reconstruction, and patch averaging. The source reports 5.9 non-zero coefficients per patch on average and PSNR improvement from 18.69 dB to 29.31 dB.

### Limitations and Publication Context

The authors explicitly state that they cannot establish a priori boundedness and stability for the feedback network under general conditions, though activities remain bounded in their experiments. Accurate spike rates are asymptotic, and finite-time rates are noisy. The sparse-coding guarantee tolerates small H-to-FB mismatch but does not remove the need to monitor that mismatch. Random asymmetric initialization works empirically, yet theory is limited.

No hardware experiment supports the claimed low-power or high-throughput potential. There is no energy, latency, throughput, memory-traffic, event-traffic, or silicon-area comparison. No official code, raw data package, numeric plot table, experiment manifest, or independent reproduction was identified. OpenReview identifies an ICLR 2019 conference version under a slightly changed title, but its challenge-protected interface prevented inspection of reviews and revision history.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Feedback-augmented dynamical states can expose the reconstruction information required for local dictionary-gradient updates. | Author theoretical claim | E2, E3, E6 | Directly supported by the derived two-phase limiting-state relationships; not independently formalized. | Medium-high |
| C2 | Long-time coding rates solve or approximate the non-negative sparse-coding problem when the matrix relationships are exact or sufficiently close. | Author theoretical claim | E2, E3, E6 | Supported under stated boundedness, large-time, and small-mismatch conditions. | Medium-high |
| C3 | Individual neurons can update their locally stored rows of F, B, and H using locally observable states and spike rates. | Author method claim | E2 | The algebra is explicit; whether a practical implementation preserves strict locality depends on hardware mapping. | High for method description |
| C4 | The local H update maintains approximate H-to-FB consistency and can symmetrize initially asymmetric feedforward/feedback weights. | Author analytical and empirical claim | E2, E4 | Symmetry decay has a direct derivation; general learning stability remains incomplete. | Medium-high |
| C5 | The spiking learner reaches similar or better displayed objectives than tested SGD settings on three datasets. | Author empirical claim | E4 | Paper text and plots support reporting; missing raw values, seeds, and code prevent reproduction. | Medium for result reporting |
| C6 | The learned Lena dictionary improves one denoising example from 18.69 dB to 29.31 dB. | Author empirical claim | E5 | Exact caption values were inspected; generalization is unsupported by a single example. | High for transcription; low for breadth |
| C7 | Local memory and spike communication can enable low-power, high-throughput learning on massively parallel hardware. | Author motivation and reviewer interpretation | E1, E2 | Plausible architectural motivation, not measured evidence in this paper. | Low |

## Methodology

- **Research objective:** Randomly select one eligible archived arXiv paper, review it source-first, and deposit a public-safe Black Lake log, Report-Mark, DEP README, and schema-complete manuscript.
- **Sources inspected:** Private archive readme/PDF presence, extracted full PDF text, public arXiv abstract/metadata, public arXiv HTML full text, arXiv DOI, official OpenReview locator, live Black Lake and Black-Lake-Data READMEs, and exactly three related DEP entries.
- **Discovery strategy:** Enumerated PDFs with rg --files -g "*.pdf"; treated each unique PDF parent directory as one paper unit; sorted the complete unit set; selected a uniform random zero-based index with PowerShell Get-Random; inspected nearby metadata; extracted the PDF locally; then cross-checked public sources and related DEP records.
- **Inclusion criteria:** Evidence had to identify the work, expose its mechanism/theorems/experiments, define repository requirements, or provide concrete overlap in dynamical memory, structured recurrence, or sparse systems efficiency.
- **Exclusion criteria:** Generic search summaries, uninspected citations, unsupported code/reproducibility claims, duplicate deposits, private path disclosure, exact local run timestamps, and source redistribution without clear permission.
- **Analytical approach:** Empirical, conceptual, comparative, implementation, product research, and replication analysis.
- **Evidence handling:** Major claims are mapped to evidence IDs. Source claims, reviewer interpretation, and implementation proposals are labeled separately. Related DEP entries are synthesis anchors rather than validation sources.
- **Uncertainty handling:** Missing code, raw metrics, variance, formal proof checking, hardware evidence, OpenReview access, and general stability guarantees remain visible as limitations.
- **Extraction process:** Extractor preflight found pypdf available and pdftotext unavailable. PDF extraction succeeded; local HTML and source package were absent. Public HTML was separately inspected by URL.
- **Version control:** The substantive source is pinned to arXiv:1805.08952v1. Repository authority and related entries were read after refreshing their default branches.
- **Claim selection:** Priority went to the locality constraint, two-phase gradient mechanism, matrix-consistency update, theoretical conditions, experiment configuration, quantitative denoising result, explicit stability caveat, and hardware-evidence gap.
- **Cross-checking:** Identity and metadata were checked against arXiv; method and result statements were checked across the PDF extraction and public HTML; related-entry identities were checked in the refreshed repository.
- **Reviewer stance:** DEP-ready preservation combining summary, critique, implementation translation, and replication planning.
- **Random selection validation:** 75,761 PDFs produced 75,761 unique paper units. Uniform zero-based index 47,412 selected arXiv:1805.08952; the first draw was accepted.
- **Deduplication validation:** arXiv ID, DOI, normalized title, and slug were searched across Black Lake .logs, .reports, .lake-data, public staging pointers, automation memory, and live Black-Lake-Data content. Duplicate exclusions and reselections were both zero, and no 24-hour same-paper marker was found.

## Scope, Constraints, and Assumptions

- **Scope:** arXiv:1805.08952v1, its full-text method/theory/experiments, public publication context, and three related Black Lake DEP entries.
- **Temporal boundary:** Primary paper version submitted 2018-05-23; supporting repository and public sources accessed on 2026-07-13.
- **Evidence limits:** No official code, raw result tables, experiment seeds, independent reproduction, hardware benchmark, energy measurement, or accessible OpenReview review record.
- **Assumptions:** The private archived PDF corresponds to arXiv v1; extracted text preserves the substantive equations and captions; related DEP records accurately identify their own primary bases.
- **Constraints:** Public outputs cannot reveal private locations or redistribute the archived source. Efficiency proposals use synthetic data and evaluation-only framing.
- **Out of scope:** Formal theorem verification, hardware synthesis, experiment reproduction, bibliometric review, and claims about biological plausibility beyond the inspected paper.
- **Intended use:** DEP deposition, technical review, replication planning, neuromorphic/edge systems ideation, and research backlog development.
- **Audience:** Researchers and engineers working on sparse coding, spiking systems, dynamical learning, reservoir computing, or efficient local inference.
- **Depth target:** Full manuscript review with source traceability and implementation translation.
- **Reproducibility boundary:** A future reviewer can retrieve the cited paper and build a replication, but cannot reproduce the reported results from this artifact alone.
- **Operational boundary:** The artifact may propose bounded simulators and benchmarks; it does not claim deployment readiness or hardware superiority.
- **Data sensitivity:** Public research sources and synthetic implementation concepts; private archive location withheld.

## Observations

- **Observed pattern:** The method converts a global optimization quantity into a difference between two locally observable dynamical states.
- **Observed pattern:** Matrix consistency is not a background invariant; it is an actively learned quantity with its own correction signal.
- **Technical implication:** A practical implementation needs simultaneous monitoring of objective quality, spike-rate precision, H-to-FB mismatch, symmetry, and activity bounds.
- **Technical implication:** Finite-time noisy rates may be tolerable because stochastic updates already accept gradient noise, but the noise-versus-cost frontier must be measured.
- **Contradiction or tension:** The paper motivates massively parallel efficiency while evaluating a simulation and objective curves rather than hardware cost.
- **Contradiction or tension:** Random asymmetric weights work empirically before full symmetry is restored, yet the strongest theoretical story assumes more structured relationships.
- **Open question:** Can boundedness be guaranteed from enforceable local constraints rather than checked after the fact?
- **Open question:** Does event-driven execution still win after routing, synchronization, and memory traffic are included?
- **Reviewer hypothesis:** The most reusable idea is not the exact spiking model but the design pattern of using controlled state perturbations to recover otherwise non-local learning signals.

## Considerations

- **Stability:** Feedback excitation can create unbounded activity; implementations need hard limits, diagnostic traces, and stop conditions.
- **Approximation:** Short execution windows trade precision for cost. Evaluation should plot gradient error and final objective against phase duration and time step.
- **Locality accounting:** A system should declare which values are stored per processing element, what messages cross elements, and whether any hidden reduction or synchronization is global.
- **Hardware relevance:** Energy and throughput claims require matched solver baselines, device utilization, memory movement, event sparsity, network-on-chip traffic, and convergence time.
- **Data and ethics:** The reviewed experiments use standard image examples and do not raise significant personal-data concerns; future sensory deployments should document consent, privacy, and retention.
- **Maintenance:** Numeric stability, threshold policies, dictionary scaling, and matrix-consistency monitors would need versioned tests.
- **Adoption:** The method is better treated as a research kernel for neuromorphic and local-learning experiments than as a drop-in replacement for established sparse solvers.
- **Evaluation:** Success should include optimization quality, failure rates, stability margins, and systems cost, not only recognizable atoms or one denoising image.

## Strengths

- The paper states a precise locality constraint and designs the network around it.
- It connects spiking limit-point behavior to a conventional sparse-coding objective rather than relying only on a qualitative Hebbian story.
- The two-phase mechanism gives a clear explanation for how reconstruction information becomes locally available.
- The H-to-FB catch-up rule treats weight consistency as an explicit optimization problem.
- The experimental study spans image processing, digit data, and natural-scene receptive-field structure with both consistent and asymmetric initialization.
- The paper discloses important theoretical gaps, especially boundedness and stability of the feedback network.

## Weaknesses

- No official implementation or complete experiment manifest was identified.
- Objective comparisons are largely plot-based and omit raw tables, repeated-run variation, and statistical testing.
- The baseline set is narrow relative to modern sparse-coding and local-learning solvers.
- Stability and boundedness are observed rather than generally guaranteed during learning.
- The finite-time approximation is justified empirically without a detailed error-versus-cost analysis.
- Hardware efficiency is a motivation without energy, latency, throughput, memory, communication, or area measurements.
- The denoising evidence is a single Lena example rather than a multi-image benchmark.
- OpenReview revision and review context could not be inspected through the challenge-protected interface.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code, configurations, seeds, and numeric plot data | Reproducibility | Current plots cannot be independently reconstructed. | Auditable comparisons and faster follow-up. | Packaging and maintenance burden. | Rebuild every figure in a clean environment from one manifest. |
| Add stability-enforcing local controls | Theory and safety | General boundedness is not proven. | Fewer divergent runs and clearer guarantees. | Controls may change the objective or learning signal. | Prove local bounds and stress-test adversarial initializations. |
| Sweep phase duration and perturbation strength | Approximation quality | Finite-time spike rates and kappa govern bias/noise. | Explicit accuracy-cost frontier. | Larger experiment grid. | Measure gradient-angle error, objective, activity, and runtime. |
| Compare stronger solver baselines | Empirical validity | Three SGD rates do not establish broad advantage. | Better understanding of when dynamics help. | Baseline tuning complexity. | Match objective, data, atoms, preprocessing, and compute budget. |
| Build a hardware or cycle-accurate benchmark | Systems relevance | Efficiency claims are currently unmeasured. | Evidence for or against the main architectural motivation. | Specialized hardware and instrumentation. | Report energy-to-quality, latency-to-quality, bytes moved, and event traffic. |
| Expand denoising evaluation | Application evidence | One image is insufficient for generalization. | More credible practical utility. | Dataset and hyperparameter work. | Use a public image suite, multiple noise levels, PSNR/SSIM, and matched sparse baselines. |

## Potential Implementations

1. **Dynamical dictionary replication harness**
   - **User:** Research engineer.
   - **Goal:** Reproduce the two-phase learning rule on synthetic non-negative data.
   - **Core mechanism:** Simulate normal and perturbed phases, compute local update estimates, and compare with an analytic centralized gradient.
   - **Required inputs:** Synthetic dictionaries, sparse coefficients, noise, seeds, phase duration, and learning rates.
   - **Outputs:** Objective curves, gradient-angle error, consistency error, stability traces, and reproducibility bundle.
   - **Risk controls:** Activity caps, deterministic seeds, synthetic data, and divergence stop rules.
   - **Evaluation:** Agreement with analytic gradients and stable convergence across controlled perturbations.

2. **Event-locality accelerator benchmark**
   - **User:** Neuromorphic or edge-hardware team.
   - **Goal:** Determine whether local spike-based updates reduce real system cost.
   - **Core mechanism:** Run the same dictionary task through event-driven and optimized centralized implementations under matched quality targets.
   - **Required inputs:** Fixed workloads, device counters, memory-traffic instrumentation, and quality thresholds.
   - **Outputs:** Energy, time, bytes moved, event counts, synchronization cost, and objective quality.
   - **Risk controls:** Thermal limits, bounded workloads, identical preprocessing, and transparent exclusion rules.
   - **Evaluation:** Pareto comparison at matched reconstruction error and convergence confidence.

3. **Structured-dynamics design lab**
   - **User:** ML systems researcher.
   - **Goal:** Compare local contrastive dynamics, echo-state memory, geometry-aware reservoirs, and sparse routing using one evidence model.
   - **Core mechanism:** Standardize state structure, locality declarations, stability monitors, active-compute accounting, and task metrics.
   - **Required inputs:** Public toy workloads and adapters for each method family.
   - **Outputs:** Design matrix, stability report, compute-locality traces, and bounded implementation recommendations.
   - **Risk controls:** Synthetic/public data, no production decisions, and method-specific caveat labels.
   - **Evaluation:** Coverage of shared metrics and ability to reproduce known qualitative behaviors.

## Three Ways to Exercise This Research

1. **Gradient-recovery check:** Use a tiny synthetic non-negative dictionary and one sparse sample; run two deterministic phases; compare the local phase-difference estimate with a centralized analytic gradient; output error traces; succeed when gradient direction agreement exceeds a preset threshold; stop on unbounded activity.
2. **Consistency stress test:** Randomize F, B, and H at controlled mismatch levels; run only the local correction rules; output H-to-FB error, symmetry, and activity envelopes; succeed when error decreases across seeds without objective regression; stop if any state breaches the declared cap.
3. **Efficiency falsification study:** Implement event-count and memory-movement accounting before claiming hardware benefit; compare with an optimized sparse baseline at matched reconstruction quality; output a Pareto plot; succeed only if at least one system-cost measure improves without stability loss; stop if quality matching fails.

## Example MVP Product

- **Product name:** Local Dynamics Auditor
- **Target user:** Research engineers evaluating local-learning and neuromorphic algorithms.
- **Problem:** Papers can claim local or sparse computation without showing whether gradient accuracy, stability, and systems cost survive implementation.
- **Core workflow:** Import a small simulator adapter; declare per-node state and messages; execute normal and perturbed phases; compare local and centralized gradients; run mismatch/stability sweeps; export a public-safe evidence report.
- **Data requirements:** Synthetic non-negative dictionaries and sparse signals by default; optional public benchmark adapters.
- **Architecture:** Local Python runner, deterministic simulation API, analytic-gradient oracle, metric collector, SQLite or JSON result store, and static report generator.
- **Success metrics:** Reproducible runs; gradient-direction agreement; bounded activity; decreasing consistency error; complete message/memory accounting; no hidden global operation in the locality declaration.
- **Risk controls:** Synthetic-first data, activity caps, timeout and divergence stops, no secrets or user data, and explicit separation between simulation and hardware claims.
- **Limitations:** An MVP cannot validate biological plausibility, chip energy, or large-scale convergence; simulator results may hide hardware bottlenecks.
- **MVP boundary:** One small non-negative dictionary objective and CPU simulation; no custom hardware, large images, or production service.
- **Deployment model:** Local CLI plus static HTML/Markdown reports.
- **Evaluation plan:** Unit tests for equations, smoke tests for known synthetic cases, seed replay, negative tests for divergence, and comparison with a centralized gradient.
- **Failure modes:** Silent global reductions, unstable feedback, misleading short-window rates, inaccurate event accounting, or apparent speedups from unmatched quality.
- **Maintenance plan:** Versioned equation tests, dependency pinning, adapter conformance tests, and quarterly review of baseline implementations.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Dictionary Learning by Dynamical Neural Networks | Primary paper | Reviewed arXiv source. | https://arxiv.org/abs/1805.08952 |
| Sparse Dictionary Learning by Dynamical Neural Networks | Conference-version locator | ICLR 2019 publication context under the updated title. | https://openreview.net/forum?id=B1gstsCqt7 |
| Deep ESN Memory DEP-E | Related Black Lake research | Recurrent dynamics, memory-capacity theory, and empirical prediction tradeoffs. | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260710-Deep%20ESN%20Memory |
| 2D-RC OTFS DEP-E | Related Black Lake research | Geometry-aware reservoir state and online dynamical learning. | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260709-2D-RC%20OTFS |
| SMES Expert Sparsity DEP-E | Related Black Lake research | Sparse activation, locality/load constraints, and systems-level efficiency validation. | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260713-SMES%20Expert%20Sparsity |
| Analysis of Memory Capacity for Deep Echo State Networks | Related primary basis | Theory and evaluation of memory in deep reservoir architectures. | https://arxiv.org/abs/1908.07063 |
| 2D-RC: Two-Dimensional Neural Network Approach for OTFS Symbol Detection | Related primary basis | Structured dynamical learning aligned to physical signal geometry. | https://arxiv.org/abs/2311.08543 |
| SMES: Towards Scalable Multi-Task Recommendation via Expert Sparsity | Related primary basis | Modern conditional-computation comparison for sparsity-to-systems transfer. | https://arxiv.org/abs/2602.09386 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1805.08952 | Identity, authors, abstract, subjects, version, submission date, DOI, and source locators. | 2026-07-13 | Primary arXiv record. |
| R2 | https://arxiv.org/pdf/1805.08952 | Full method, theory, experiments, figures, appendices, and references. | 2026-07-13 | Private archived copy inspected through this public locator; no file redistributed. |
| R3 | https://arxiv.org/html/1805.08952 | Full-text cross-check of method, theorem statements, experiments, and captions. | 2026-07-13 | Public HTML inspected. |
| R4 | https://doi.org/10.48550/arXiv.1805.08952 | Persistent identifier. | 2026-07-13 | arXiv-issued DOI. |
| R5 | https://openreview.net/forum?id=B1gstsCqt7 | ICLR 2019 conference-title context. | 2026-07-13 | Locator identified; deeper page challenge-blocked. |
| R6 | Private archive readme and PDF, location withheld | Random selection identity and source availability. | 2026-07-13 | No local path or source file published. |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | DEP class, naming, contents, attribution, stability, and commit rules. | 2026-07-13 | Live README fetched before drafting. |
| R8 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository context and provenance rules. | 2026-07-13 | Live README fetched before drafting. |
| R9 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260710-Deep%20ESN%20Memory | Deep ESN related synthesis. | 2026-07-13 | Processed DEP inspected; not validation evidence. |
| R10 | https://arxiv.org/abs/1908.07063 | Primary basis for the Deep ESN related DEP. | 2026-07-13 | Used for related context. |
| R11 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260709-2D-RC%20OTFS | 2D-RC related synthesis. | 2026-07-13 | Processed DEP inspected; not validation evidence. |
| R12 | https://arxiv.org/abs/2311.08543 | Primary basis for the 2D-RC related DEP. | 2026-07-13 | Used for related context. |
| R13 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260713-SMES%20Expert%20Sparsity | SMES related synthesis. | 2026-07-13 | Processed DEP inspected; not validation evidence. |
| R14 | https://arxiv.org/abs/2602.09386 | Primary basis for the SMES related DEP. | 2026-07-13 | Used for related context. |

## Appendix

### Public-Safe Selection Audit

- Enumeration method: rg --files -g "*.pdf" over the private archive root.
- Paper-unit rule: one unique PDF parent directory equals one candidate unit.
- Candidate count: 75,761 PDFs and 75,761 unique paper units.
- Random method: PowerShell Get-Random over the complete sorted unit list.
- Selected zero-based index: 47,412.
- Selected identifier: arXiv:1805.08952v1.
- Acceptance: first draw accepted.
- Duplicate exclusion count: 0.
- Reselection count: 0.
- Dedup keys: arXiv ID, arXiv DOI, normalized title, and public slug.
- Dedup scope: Black Lake logs/reports/deposits/staging pointers, automation memory, and live related-repository content.
- Same-paper 24-hour result: no marker found.

### Extraction and Source Inventory

- Extractor preflight: pypdf available; pdftotext unavailable.
- PDF extraction: successful, 60,252 bytes of text.
- Local HTML extraction: unavailable.
- Local source-package extraction: unavailable.
- Public HTML: inspected separately.
- Public .source contents: none.
- Redistribution decision: private archive PDF withheld because permission was not assumed.

### Result Trace Notes

- Dataset configurations and phase parameters: paper section 4.
- Weight consistency and symmetry: Figure 3 and surrounding discussion.
- SGD comparison: Figure 4 and section 4.2.
- Learned atom interpretations: Figure 6 and appendix D.1.
- Denoising values: Figure 7 and appendix D.2.
- Stability and finite-time caveats: section 3.3.

### Replication Checklist

- [ ] Publish or reconstruct a deterministic simulator for the integrate-and-fire dynamics.
- [ ] Pin preprocessing for Lena, MNIST, and natural scenes.
- [ ] Pin F, B, H, threshold, scaling, learning-rate, decay, kappa, and phase-duration settings.
- [ ] Export raw numeric data for consistency, symmetry, and objective plots.
- [ ] Repeat runs across seeds and report variance and divergence.
- [ ] Compare local gradient estimates with centralized analytic gradients.
- [ ] Compare against tuned sparse-coding solvers at matched quality and compute budget.
- [ ] Measure event traffic, bytes moved, latency, energy, and time to convergence on declared hardware.
