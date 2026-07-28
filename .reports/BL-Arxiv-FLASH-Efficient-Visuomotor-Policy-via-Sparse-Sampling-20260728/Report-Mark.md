# Report-Mark: FLASH Efficient

- Deployment job ID: `BLAD-2200-20260728-EB036F17`
- Deployment item ID: `BLAD-2200-20260728-EB036F17-P09`
- Review date: 2026-07-28

## Source Metadata

| Field | Value |
|---|---|
| Paper | *FLASH: Efficient Visuomotor Policy via Sparse Sampling* |
| Authors | Bai, Jiaqi; Jia, Jindou; Hu, Yuxuan; Li, Gen; Chen, Xiangyu; An, Tuo; Zuo, Kuangji; Yang, Jianfei |
| Identifier | arXiv:2605.15492; DOI:10.48550/arXiv.2605.15492 |
| Submitted / source date | 2026/05/15 |
| Record | https://arxiv.org/abs/2605.15492 |
| Full paper | https://arxiv.org/html/2605.15492 |
| PDF | https://arxiv.org/pdf/2605.15492 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260728-EB036F17`; `BLAD-2200-20260728-EB036F17-P09` |

## Concise Research Notes

The paper studies flash, visuomotor, policy, sparse. Its abstract states: Generative models such as diffusion and flow matching have become dominant paradigms for visuomotor policy learning, yet their reliance on iterative denoising incurs high inference latency incompatible with real-time robotic control. We present Fast Legendre-polynomial Action policy via Sparse History-anchored flow (FLASH Policy), which replaces discrete action-chunk generation with continuous Legendre polynomial trajectory representation. Specifically, by fitting expert demonstrations under sparse temporal sampling, FLASH enables a single inference to cover a significantly extended action horizon. To further accelerate generation, FLASH initiates the flow matching process from history polynomial coefficients rather than uninformative Gaussian noise, shortening the transport distance and enabling accurate single-step inference. Moreover, analytic polynomial differentiation directly provides desired velocity feed-forward signals to the torque controller without numerical approximation. Extensive experiments on five simulated and two real-world manipulation tasks demonstrate that FLASH achieves state-of-the-art success rates ($\ge 92\%$ across all tasks), a per-episode inference time of $31.40\,ms$ (up to $175\times$ faster than diffusion policies and $18\times$ faster than prior flow matching policies), up to $4\times$ faster training convergence than ACT, and $5\times$ to $7\t…

Full-paper inspection found explicit introduction, method, evaluation, discussion/limitation, conclusion, and reference structure. A method evidence anchor is: “Generative models such as diffusion and flow matching have become dominant paradigms for visuomotor policy learning, yet their reliance on iterative denoising incurs high inference latency incompatible with real-time robotic control. We present F ast L egendre-polynomial A ction policy via S parse H istory-anchored flow ( FLASH Policy), which replaces discrete action-chunk generation with continuous Legendre polynom…” An evaluation evidence anchor is: “To evaluate the proposed method, we conduct the experiments in both simulated and real-world environments. As illustrated in Fig. 3 , the evaluation encompasses seven manipulation tasks on Franka robot, five of which are in simulation on Roboverse ( geng2025roboverse ) platform, and two are real-world tasks.” These are source claims, not independent reproduction.

Reviewer interpretation is bounded: any transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md` - Semantic Skill MoE Policies; overlap: action, all, high.
2. `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md` - FAVLA Fast-Slow - DEP-E; overlap: all, experiments, high.
3. `.lake-data/DEP-E/DEP-E-20260726-ManipulationNet An/manipulationnet_an_manuscript.md` - ManipulationNet An - DEP-E; overlap: accurate, control, directly.

## Synthesis Note

### Concept Bridge

The selected paper contributes a flash, visuomotor, policy perspective. The three related DEPs overlap concretely through visuomotor policies, sparse action sampling, fast-slow control, manipulation benchmarks. Together they support a provenance-first workflow that separates primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for flash that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's visuomotor mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Semantic Skill MoE Policies overlaps through action, all, high, clarifying a neighboring representation or evidence choice.
2. FAVLA Fast-Slow - DEP-E overlaps through all, experiments, high, exposing a complementary evaluation or operating boundary.
3. ManipulationNet An - DEP-E overlaps through accurate, control, directly, showing how implementation assumptions affect practical transfer.

### Conceptual Similarities

1. All four artifacts transform raw inputs into intermediate evidence rather than direct truth claims.
2. Each depends on explicit assumptions about data, representation, evaluation, and scope.
3. Each benefits from auditable versioning, negative controls, uncertainty, and failure-aware interpretation.

### MVP Implementations with Code Mock-Ups

1. Evidence map: `record = evaluate(input, config); require(record.provenance)`.
2. Frozen comparison: `scores = compare(baselines, candidate, split_manifest)`.
3. Abstention gate: `decision = review if drift or low_confidence else nonbinding_output`.

### Developer Challenges

1. Reproducing preprocessing, baselines, and metrics without leakage or silent version drift.
2. Preserving evidence lineage while keeping evaluation maintainable and privacy-aware.
3. Designing stable explanations and stop conditions outside the tested envelope.

### Author Challenges

1. Publishing enough configuration, data, and ablation detail for independent replication.
2. Separating benchmark improvement from claims of generalization or deployment readiness.
3. Reporting negative results, sensitivity, uncertainty, and failure cases alongside headline metrics.

## Validation Notes

- Deployment job `BLAD-2200-20260728-EB036F17` and item `BLAD-2200-20260728-EB036F17-P09` are stamped in the log, report, DEP README context, manuscript YAML and Source Metadata, and planned commit trailers.
- Uniform draw index 14494 of 75822 units; duplicate exclusions 0; source-gate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2605.15492 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2605.15492 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2605.15492 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2605.15492 - durable paper identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-Semantic%20Skill%20MoE - related DEP: Semantic Skill MoE Policies; source basis `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260722-FAVLA%20Fast-Slow - related DEP: FAVLA Fast-Slow - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260726-ManipulationNet%20An - related DEP: ManipulationNet An - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260726-ManipulationNet An/manipulationnet_an_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, integrity records, and local companions; all withheld locally.
