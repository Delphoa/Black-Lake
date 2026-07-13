# Report-Mark: Dynamical Dictionary

## Source Metadata

| Field | Value |
|---|---|
| Work | Dictionary Learning by Dynamical Neural Networks |
| Conference-title context | Sparse Dictionary Learning by Dynamical Neural Networks |
| Authors | Tsung-Han Lin; Ping Tak Peter Tang |
| Organization | Intel Corporation |
| Platform | arXiv, Computer Science — Machine Learning; Statistics — Machine Learning |
| Identifier | arXiv:1805.08952v1 |
| DOI | 10.48550/arXiv.1805.08952 (arXiv-issued DOI) |
| Submitted | 2018-05-23 |
| Conference locator | ICLR 2019 OpenReview forum B1gstsCqt7 |
| Primary URL | https://arxiv.org/abs/1805.08952 |
| Full-text URLs | https://arxiv.org/pdf/1805.08952 ; https://arxiv.org/html/1805.08952 |
| Evidence access date | 2026-07-13 |
| Source status | Private archive PDF and public arXiv HTML/metadata inspected; no source file redistributed |
| License/usage note | arXiv exposes its non-exclusive distribution license; that does not establish permission for this repository to redistribute the archived copy, so only public URLs are deposited. |

## Concise Research Notes

The paper addresses a locality problem in dynamical neural computation. A standard locally competitive architecture can solve non-negative l1 sparse coding when feedforward and lateral weights are exactly tied to a global dictionary, but learning that dictionary requires reconstruction gradients and consistent weights that are not ordinarily available to each neuron.

The authors add a feedback matrix from coding neurons to input neurons and run the spiking network in two configurations: a normal phase with feedback strength zero and a perturbed phase with positive feedback. Differences between the resulting long-time spike rates approximate the reconstruction error and a correction for the mismatch between the lateral matrix H and the product FB. Each destination neuron can therefore update its locally stored row of the feedforward, feedback, or lateral weights. A separate catch-up update keeps H near FB, while shared updates preserve the symmetry between the feedforward and feedback dictionary representations.

The analysis connects limit-point conditions of integrate-and-fire networks to the KKT conditions of non-negative sparse coding. It further argues that approximate sparse codes remain useful when H is close to FB and derives the two-phase gradient relationships used by the learning rule. Important conditions remain: the feedback system's activities are not proven bounded under general a priori conditions, convergence arguments depend on long-enough dynamics, and the random-asymmetric initialization case has limited theory.

Experiments use 100,000 8-by-8 Lena patches with 256 atoms, 50,000 MNIST images with 512 atoms, and 200,000 16-by-16 whitened natural-scene patches with 1,024 atoms. Each phase runs for 20 time units at a 1/32 discrete step; the perturbed phase uses feedback strength 0.7. A 10,000-sample test set and batch size one are used for the plotted SGD comparison. The authors report similar or better objective values than tested SGD settings across the three datasets, including slower but successful learning from random asymmetric weights. An appendix denoising example raises Lena PSNR from 18.69 dB to 29.31 dB with 5.9 non-zero coefficients per patch on average. These are source-reported numerical results, not independently reproduced findings.

Evidence quality is strongest for paper identity, method, theorem statements, experimental setup, figure captions, and the denoising numbers. It is weaker for deployment claims: no official code, raw results, seeds, experiment manifest, hardware prototype, power measurement, throughput result, or communication benchmark was identified. The claim of potential low-power, high-throughput execution should therefore be treated as motivation rather than demonstrated empirical evidence.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limitations |
|---|---|---|---|---|
| E1 | arXiv abstract and metadata | Identity, authorship, date, subjects, abstract claims, arXiv DOI | High | Abstract alone cannot validate methods or experiments. |
| E2 | Full PDF sections 1–3 and appendices B–C | Network topology, local-information constraint, sparse-coding/KKT connection, two-phase gradient derivation, weight updates | High for source reporting | Proofs were reviewed but not independently formalized or checked in a theorem prover. |
| E3 | Full PDF sections 3.3–5 and Figures 2–4 | Stability caveat, execution window, weight consistency/symmetry, dataset setup, SGD comparison, conclusion | High for transcription; low for reproduction | Core objective traces are plot-based and lack tabulated run variance. |
| E4 | Full PDF appendix D and Figure 7 | Learned-dictionary visual interpretation and Lena denoising example | High for reported values | One image example does not establish broad denoising quality. |
| E5 | Public arXiv HTML full text | Cross-check of equations, theorem statements, sections, and figure captions | High | HTML rendering can flatten notation. |
| E6 | Official OpenReview locator and conference-PDF header surfaced through the public locator | ICLR 2019 version and changed conference title | Medium | Interactive page/API was challenge-blocked, so review records were not inspected. |
| E7 | Private public-safe extraction summary | PDF identity, successful pypdf extraction, absent local HTML/source package | High | Private locations intentionally withheld. |
| E8 | Three inspected DEP entries and their stated primary bases | Dynamical memory, geometry-aware reservoir learning, and sparse-systems synthesis | Medium | Related entries provide context, not validation of this paper. |
| E9 | Live Black Lake and Black-Lake-Data READMEs | Packaging, naming, attribution, stability, and commit rules | High | Process evidence only. |

## Related DEP Entries

1. [.lake-data/DEP-E/DEP-E-20260710-Deep ESN Memory](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260710-Deep%20ESN%20Memory) — This entry reviews memory capacity in shallow, parallel, and series echo-state networks. It overlaps through recurrent state dynamics, fixed/local internal computation, and the need to separate theoretical capacity from empirical prediction quality. Source basis: the processed DEP manuscript and arXiv:1908.07063.
2. [.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260709-2D-RC%20OTFS) — This entry reviews a two-dimensional reservoir learner whose state geometry matches circular delay-Doppler interactions and is trained online from limited pilots. It overlaps through dynamical state, locally structured recurrence, and online learning under system constraints. Source basis: the processed DEP manuscript and arXiv:2311.08543.
3. [.lake-data/DEP-E/DEP-E-20260713-SMES Expert Sparsity](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-SMES%20Expert%20Sparsity) — This entry reviews sparse expert routing and the systems work needed to turn conditional activation into latency improvement. It overlaps through sparsity as a computational principle, load/locality constraints, and the distinction between algorithmic efficiency and measured hardware efficiency. Source basis: the processed DEP manuscript and arXiv:2602.09386.

## Synthesis Note

### Concept Bridge

The selected paper, Deep ESN, 2D-RC, and SMES describe four ways to control computation through structure. The dynamical dictionary learner uses two nearby network states to expose a local learning signal; Deep ESN uses reservoir topology to shape memory; 2D-RC shapes recurrence around known delay-Doppler geometry; and SMES bounds active expert computation while tracking runtime overhead. Together they suggest a common engineering contract: choose state and sparsity structure deliberately, identify which quantities can be computed locally, prove or test stability at the boundary, and measure whether the claimed computational economy survives on real hardware.

### Potential Implementations

1. **Two-phase sparse-learning simulator:** reproduce the normal and perturbed dynamical phases on synthetic non-negative signals, record reconstruction-gradient error, H-to-FB consistency, spike-rate precision, and convergence under controlled asymmetry.
2. **Locality-aware accelerator benchmark:** compare per-neuron local updates with a centralized sparse-coding baseline while measuring bytes moved, spike/event traffic, energy proxies, objective quality, and time to convergence.
3. **Dynamical-structure design lab:** evaluate generic recurrence, memory-oriented reservoirs, geometry-aware reservoirs, and sparsely routed experts under a shared evidence template for stability, locality, active computation, and end-to-end cost.

### Deeper Relationship Observations

1. Contrastive state differences and reservoir readouts both turn a dynamical trajectory into a supervised signal, but the selected paper uses the difference to update internal weights whereas classical reservoirs usually train only an output map.
2. The H-near-FB constraint and 2D-RC's geometry-matched state update are instances of the same discipline: learned dynamics remain useful only when internal structure stays aligned with the objective or physical process.
3. Sparse codes and sparse experts can reduce active work in principle, yet both require systems evidence; event communication, irregular memory access, routing, and synchronization can erase the theoretical saving.

### Conceptual Similarities

1. The selected paper and Deep ESN both analyze computational properties emerging from recurrent dynamics rather than from a purely feedforward evaluation graph.
2. The selected paper and 2D-RC both encode domain structure in network connectivity so that useful computations arise from local state evolution.
3. The selected paper and SMES both use sparsity to separate representational capacity from the amount of computation that should be active for one input.

### MVP Implementations With Code Mock-Ups

1. **Phase-Difference Gradient Check** — compare a two-state finite difference with an analytic toy gradient.

   ~~~python
   def phase_gradient(loss_free, loss_perturbed, strength):
       assert strength > 0
       return (loss_perturbed - loss_free) / strength

   estimate = phase_gradient(1.00, 1.02, 0.1)
   assert abs(estimate - 0.2) < 1e-9
   ~~~

2. **Weight-Consistency Monitor** — stop a toy run when the lateral structure drifts too far from the paired maps.

   ~~~python
   def consistency_error(h, fb):
       return sum((x - y) ** 2 for x, y in zip(h, fb)) ** 0.5

   assert consistency_error([1.0, 0.5], [1.0, 0.49]) < 0.02
   ~~~

3. **Efficiency Evidence Gate** — require quality and movement evidence before accepting an efficiency claim.

   ~~~python
   def evidence_ok(objective_delta, bytes_moved_ratio, stable):
       return objective_delta <= 0 and bytes_moved_ratio < 1 and stable

   assert evidence_ok(-0.03, 0.72, True)
   ~~~

### Developer Challenges

1. Simulate or implement asynchronous spiking dynamics deterministically enough to compare gradient estimates, stability, and convergence across seeds.
2. Preserve local memory and communication semantics on practical hardware without replacing them with hidden global synchronization or dense matrix operations.
3. Build measurements that join objective quality, event traffic, memory movement, latency, power, and failure states under matched baselines.

### Author Challenges

1. Publish a pinned implementation and complete experiment manifest with seeds, learning rates, preprocessing, atom normalization, stopping criteria, and numeric data behind every plot.
2. Strengthen theory for bounded activities and learning convergence under feedback, finite-time spike-rate estimates, imperfect H-to-FB consistency, and asymmetric initialization.
3. Test the claimed hardware motivation on a real or cycle-accurate platform against optimized sparse-coding baselines, including energy, throughput, communication, and silicon-area assumptions.

## Validation Notes

- Required paper identity, dates, authors, arXiv ID, DOI, problem, method, evidence, limitations, and implementation relevance were extracted from inspected evidence.
- Quantitative claims were transcribed from the experimental setup, Figure 4 discussion, and Figure 7 caption; none are presented as independently reproduced.
- Exactly three related DEP entries are included, each with a concrete overlap reason and source basis.
- The Synthesis Note contains exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP implementations with code mock-ups, three developer challenges, and three author challenges.
- Selection used 75,761 unique PDF-parent paper units, zero-based random index 47,412, zero duplicate exclusions, and zero reselections.
- Deduplication found no arXiv ID, DOI, normalized-title, slug, or same-paper 24-hour match.
- No source file was added because redistribution permission was not assumed.
- Public-safe review found no local absolute path, home directory, username, drive path, machine name, workspace root, local timezone label, or exact local execution timestamp.

## Attribution Block

- Source URL: https://arxiv.org/abs/1805.08952
  - Applies to: paper identity, metadata, abstract claims, submission history, subjects, DOI, and public full-text links.
  - Notes: Primary arXiv record inspected on 2026-07-13.
- Source URL: https://arxiv.org/pdf/1805.08952
  - Applies to: method, equations, experiments, figures, limitations, appendices, and references.
  - Notes: Public locator for the full PDF; the reviewed copy was already present in a private archive and was not redistributed.
- Source URL: https://arxiv.org/html/1805.08952
  - Applies to: public full-text cross-check of method, theorems, experiments, and figure captions.
  - Notes: Public arXiv HTML inspected on 2026-07-13.
- Source URL: https://doi.org/10.48550/arXiv.1805.08952
  - Applies to: stable arXiv-issued DOI.
  - Notes: Identifier exposed by the arXiv record.
- Source URL: https://openreview.net/forum?id=B1gstsCqt7
  - Applies to: ICLR 2019 conference-title and publication context.
  - Notes: Official locator identified; deeper interactive access was challenge-blocked.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260710-Deep%20ESN%20Memory
  - Applies to: Deep ESN related-entry synthesis.
  - Notes: Processed Black Lake DEP inspected from the refreshed default branch.
- Source URL: https://arxiv.org/abs/1908.07063
  - Applies to: Deep ESN primary source basis recorded by the related DEP.
  - Notes: Used only for related-entry context.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260709-2D-RC%20OTFS
  - Applies to: 2D-RC related-entry synthesis.
  - Notes: Processed Black Lake DEP inspected from the refreshed default branch.
- Source URL: https://arxiv.org/abs/2311.08543
  - Applies to: 2D-RC primary source basis recorded by the related DEP.
  - Notes: Used only for related-entry context.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-SMES%20Expert%20Sparsity
  - Applies to: SMES related-entry synthesis.
  - Notes: Processed Black Lake DEP inspected from the refreshed default branch.
- Source URL: https://arxiv.org/abs/2602.09386
  - Applies to: SMES primary source basis recorded by the related DEP.
  - Notes: Used only for related-entry context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: artifact location, DEP class, naming, attribution, stability, and commit rules.
  - Notes: Live default-branch README fetched before drafting.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related repository context and provenance rules.
  - Notes: Live default-branch README fetched before drafting.
