---
title: "Photonic Quantum KD - DEP-E"
generated_at: "2026-07-20 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of simulator-backed photonic conditioning for structured knowledge distillation."
source_status: "verified complete local PDF, official full-paper HTML, and metadata HTML inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-20"
temporal_cutoff: "Sources and repository context inspected through the batch invocation."
primary_url: "https://arxiv.org/abs/2603.14898"
stable_identifier: "arXiv:2603.14898v1; DOI:10.48550/arXiv.2603.14898"
deployment_job_id: "BLAD-2200-20260720-8636EDC7"
deployment_item_id: "BLAD-2200-20260720-8636EDC7-P02"
confidence_summary: "High for source transcription; medium for simulator generalization; low for hardware or quantum advantage."
safety_scope: "offline ML evaluation, simulator/hardware comparison, bounded sampling, and human-reviewed compression decisions"
distribution_notes: "No PDF, HTML, metadata, code, cache, verification record, or local path is redistributed."
---

# Photonic Quantum KD - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Metadata | HTML | arXiv:2603.14898v1 | https://arxiv.org/abs/2603.14898 | CC license link visible; metadata only. | 2026-07-20 | Inspected. |
| S2 | Official full-paper rendering | Primary paper | HTML | arXiv:2603.14898v1 | https://arxiv.org/html/2603.14898 | Verified local copy withheld. | 2026-07-20 | Inspected in full. |
| S3 | Paper PDF | Primary paper | PDF | arXiv:2603.14898v1 | https://arxiv.org/pdf/2603.14898 | Verified local copy withheld. | 2026-07-20 | Integrity checked and cross-read. |
| S4 | arXiv DOI | Identity | DOI | 10.48550/arXiv.2603.14898 | https://doi.org/10.48550/arXiv.2603.14898 | Persistent locator. | 2026-07-20 | Resolved. |
| S5 | KDFlow DEP | Related | Markdown | DEP-E-20260712 | `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` | Related synthesis only. | 2026-07-20 | Inspected. |
| S6 | CAP Rank Sparsity DEP | Related | Markdown | DEP-E-20260719 | `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` | Related synthesis only. | 2026-07-20 | Inspected. |
| S7 | Efficient FM Survey DEP | Related | Markdown | DEP-E-20260718 | `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` | Related synthesis only. | 2026-07-20 | Inspected. |
| S8 | Selection, repair, and integrity | Process evidence | Private records | `BLAD-2200-20260720-8636EDC7-P02` | Local path withheld | Integrity/dedup/locality only. | 2026-07-20 | Verified. |

Authors: Kuan-Cheng Chen, Shang Yu, Chen-Yu Liu, Samuel Yen-Chi Chen, Huan-Hsin Tseng, Yen Jui Chang, Wei-Hao Huang, Felix Burt, Esperanza Cuenca Gomez, Zohim Chandani, William Clements, Ian Walmsley, and Kin K. Leung. Submitted 2026-03-16. Deployment job `BLAD-2200-20260720-8636EDC7`; item `BLAD-2200-20260720-8636EDC7-P02`.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Metadata | Identity, authors, date, subjects, DOI, license link. | Canonical record. | High | No result validation. |
| E2 | S2, S3 | Complete paper | Architecture, objectives, parameter counts, experiments, methods, supplement, availability. | Method and reported findings. | High for transcription | No independent execution. |
| E3 | S2 Table 1/Figure 2 | Primary paper | Five-run accuracy/loss and optimization diagnostics. | Dataset behavior. | High for source report | Three datasets and one compact CNN family. |
| E4 | S2 Figure 3/table | Primary paper | Compression scope, rank, theta budget, teacher width. | Compression frontier. | High for source report | Trainable parameters, not full system cost. |
| E5 | S2 Figure 4/Supplement | Primary paper | Shot scaling, EMA fit, variance ratio. | Noise behavior. | Medium-high | Simulator and emulated perturbations. |
| E6 | S2 Methods/availability | Primary paper | ORCA simulator, CUDA-Q, PyTorch, no public code. | Reproduction and hardware boundary. | High | Device performance unknown. |
| E7 | S5-S7 | Related DEP evidence | Distillation, structured compression, efficiency lifecycle. | Cross-DEP synthesis. | Medium | Different model scales/substrates. |
| E8 | S8 | Private process evidence | Uniform draw, dedup, bounded repair, integrity, locality. | Deployment validity. | High | Private context withheld. |

## Executive Summary

PQKD uses shot-based photonic features to condition dictionary convolutions in a student CNN during knowledge distillation. The student learns spatial basis filters; a fixed projection of a 512-dimensional feature from a 16-mode sampler produces channel mixing. Student weights use gradient descent, while photonic parameters use sample-only SPSA updates. Inference remains classical.

The paper reports competitive MNIST and Fashion-MNIST validation accuracy under partial compression, a larger CIFAR-10 deficit, and MNIST all-convolution trainable-parameter compression up to 105.40x with about two percentage points of validation loss. EMA stabilizes simulated shot noise. Evidence is simulator-based, code is not public, and end-to-end hardware advantage is not established.

## Detailed Summary

### Architecture

For each compressed convolution, PQKD learns a small rank-(R) spatial dictionary. A fixed matrix maps the photonic feature into a channel-mixing tensor, restricting dense kernels to a low-dimensional manifold controlled by dictionary bases and photonic parameters. The feature concatenates two 256-bin marginals of thresholded 16-bit outcomes, avoiding a sparse 65,536-bin full histogram.

### Training

The loss blends hard-label cross entropy with temperature-scaled teacher matching. Training alternates ten SPSA photonic updates on a validation proxy with one epoch of Adam updates for student weights. No gradient passes through the sampler. EMA optionally filters the feature stream.

### Results

In five-run partial-compression results, validation accuracy is teacher/PQKD 99.07/99.09 on MNIST, 91.86/92.42 on Fashion-MNIST, and 86.99/79.72 on CIFAR-10. Thus the method regularizes simple benchmarks but loses substantial accuracy on the harder task.

For full convolution compression on MNIST, reported trainable-parameter factors are 48.81x, 76.18x, and 105.40x across increasing teacher widths. PQKD validation accuracy is 96.85%, 97.17%, and 97.33%, while teachers are near 99%. Fixed projection matrices are excluded from trainable counts; photonic parameters are counted once.

### Shot Noise and Reproducibility

Shot-induced feature error follows an asserted (1/sqrt{S}) concentration pattern under a Lipschitz feature map. The Figure 4 fit improves under EMA, and a supplement trace at 200 shots reports a median smoothed/raw variance ratio of 0.0406. Sampling ran on the ORCA simulator backend in CUDA-Q. The paper says a compatible hardware backend can use identical calls, but hardware results are not reported. Code may be provided on reasonable request rather than through a public release.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | PQKD defines a controllable compression-accuracy frontier. | Author claim | E3, E4 | Supported on the displayed CNN/dataset configurations. | Medium-high |
| C2 | Shot-noise impact scales predictably and EMA extends the operating regime. | Author claim | E5 | Supported by simulator fits and one detailed variance trace; device validation absent. | Medium |
| C3 | Photonic sampling supplies a hardware-aligned black-box conditioning interface. | Author claim | E2, E6 | Interface is explicit; actual hardware advantage remains untested. | Medium |
| C4 | Trainable-parameter compression should not be labeled end-to-end efficiency. | Reviewer interpretation | E4, E6, E7 | Fixed projections, sampling, SPSA evaluations, GPU training, and energy remain outside the ratio. | High |
| C5 | Classical/random-feature matched baselines are necessary to isolate photonic contribution. | Reviewer interpretation | E2, E7 | The supplement specifies such baselines, but complete public comparative evidence was not established. | Medium-high |

## Methodology

- `Research objective`: preserve PQKD's mechanism, results, evidence boundary, and implementation requirements.
- `Sources inspected`: canonical arXiv metadata, verified official HTML, verified PDF, complete methods/supplement, and three related Black Lake manuscripts.
- `Discovery strategy`: uniform local archive draw; identity/title/DOI/slug dedup; bounded source repair; section/table extraction; related-DEP concept search.
- `Inclusion criteria`: architecture, parameter accounting, training, experiments, noise analysis, availability statements, and direct related mechanisms.
- `Exclusion criteria`: abstract-only inference, unreported hardware performance, and unverified advantage claims.
- `Analytical approach`: empirical, conceptual, comparative, implementation, product, safety/governance, and replication.
- `Evidence handling`: author results, simulator evidence, reviewer inference, and private process evidence are separated.
- `Uncertainty handling`: hardware, code, energy, latency, fixed-state, and baseline gaps remain explicit.
- `Extraction process`: prose, formulas, tables, figures, methods, supplement, and availability sections were inspected.
- `Version control`: arXiv v1 identity and access date are recorded.

## Scope, Constraints, and Assumptions

- `Scope`: structured CNN compression, teacher/student distillation, photonic-conditioned mixing, sampling noise, and simulator-to-device boundary.
- `Temporal boundary`: arXiv v1 and repository context available on 2026-07-20.
- `Evidence limits`: no public code, hardware run, energy/latency measurement, or independent experiment.
- `Assumptions`: reported tables and simulator settings accurately describe the experiments.
- `Constraints`: sampler interface, fixed projection, rank, shot budget, SPSA stability, validation use, and dataset complexity.
- `Out of scope`: proof of quantum advantage, production hardware readiness, and broad foundation-model scaling.
- `Intended use`: DEP preservation, matched-baseline planning, simulator/device evaluation, and compression research.
- `Reproducibility boundary`: method details are rich, but code, exact matrices, and full raw outputs remain unavailable.
- `Data sensitivity`: public benchmark datasets; source files retained locally.

## Observations

- `Observed pattern`: simple datasets can retain teacher accuracy while CIFAR-10 exposes a larger capacity gap.
- `Technical implication`: the fixed projection is part of model state even when excluded from trainable-parameter counts.
- `Contradiction or tension`: the method is hardware-aligned but the evidence is simulator-backed.
- `Open question`: do matched classical stochastic features produce the same accuracy frontier at lower operational cost?
- `Reviewer hypothesis`: provider-agnostic conditioning is the durable abstraction; substrate advantage must be proven separately.

## Considerations

SPSA uses validation evaluations to optimize photonic parameters, so test isolation and outer-loop overfitting need explicit audits. Raw and EMA-smoothed features should both be logged to distinguish noise suppression from drift masking. Hardware substitution needs distribution, latency, loss, calibration, and energy receipts. Fixed matrices and sampler calls must enter deployment cost. Benchmark results do not imply advantage on deeper networks or non-image tasks.

## Strengths

- Clear separation between sample-only photonic updates and differentiable classical training.
- Explicit trainable-parameter formulas and multiple compression scopes.
- Five-run uncertainty for core task results and a dedicated noise analysis.
- Classical inference avoids a device dependency after training.
- Rich methods and supplement expose baselines, parameter constraints, and feature construction.

## Weaknesses

- Core evidence uses a simulator rather than photonic hardware.
- Code, exact split artifacts, and fixed matrices are not public.
- CIFAR-10 performance degrades substantially.
- Headline compression excludes fixed projection storage and most system costs.
- No demonstrated quantum advantage over matched classical random/learned conditioning.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Run matched provider baselines | Attribution | Isolate photonic structure from generic stochastic conditioning. | Credible mechanism claim. | More experiments. | Same seeds, budgets, ranks, and evaluation. |
| Publish end-to-end cost ledger | Systems | Parameter count omits fixed state and sampling. | Honest deployment comparison. | Instrumentation. | Memory, latency, energy, sampler calls, wall-clock. |
| Execute on hardware | External validity | Simulator cannot establish drift or throughput. | Device evidence. | Scarce hardware and noise. | Paired simulator/device study. |
| Release reproducibility bundle | Reproduction | Methods alone do not fix matrices and code paths. | Independent rerun. | Maintenance/license review. | Table and figure regeneration. |

## Potential Implementations

1. **Conditioning-provider benchmark**
   - `User`: hybrid-ML researcher.
   - `Goal`: compare photonic, random, fixed, and learned-classical features.
   - `Core mechanism`: common provider interface and locked dictionary student.
   - `Required inputs`: benchmark data, provider configs, fixed seeds, cost instrumentation.
   - `Outputs`: accuracy/compression/cost frontier.
   - `Risk controls`: held-out test isolation and matched budgets.
   - `Evaluation`: multi-seed equivalence/noninferiority plus system cost.
2. **Shot-budget controller**
   - `User`: device operator.
   - `Goal`: choose the smallest validated shot budget.
   - `Core mechanism`: raw/EMA variance, drift, and accuracy monitor.
   - `Required inputs`: feature traces and calibration tasks.
   - `Outputs`: approved shot envelope and alarms.
   - `Risk controls`: raw trace retention and drift stop.
   - `Evaluation`: device perturbation replay.
3. **Compression receipt service**
   - `User`: ML platform reviewer.
   - `Goal`: prevent trainable-parameter ratios from hiding fixed/system costs.
   - `Core mechanism`: structured ledger across model and sampler.
   - `Required inputs`: parameter/state bytes, calls, time, energy proxy, quality.
   - `Outputs`: comparable release receipt.
   - `Risk controls`: version pins and measurement uncertainty.
   - `Evaluation`: reconcile profiler and manifest totals.

## Three Ways to Exercise This Research

1. `Classical provider ablation`: implement dictionary compression with fixed Gaussian, learned classical, and no-feature providers; output matched quality/cost results and stop before making a quantum claim.
2. `Synthetic shot-noise replay`: perturb a fixed feature provider with controlled (1/sqrt{S}) noise, compare raw versus EMA traces, and stop if drift becomes indistinguishable from noise.
3. `Accounting audit`: reproduce trainable compression, then add fixed projection bytes, sampler calls, and wall-clock cost; output both ratios and stop if end-to-end data are missing.

## Example MVP Product

- `Product name`: Hybrid Conditioning Lab.
- `Target user`: research team evaluating stochastic hardware-assisted training.
- `Problem`: provider benefits are confounded by architecture, randomness, and incomplete cost accounting.
- `Core workflow`: lock a student/dictionary configuration; plug in providers; train with common seeds; measure quality, state, calls, time, and energy proxy; emit a receipt.
- `Data requirements`: public benchmark data and provider telemetry.
- `Architecture`: local experiment runner, provider API, PyTorch trainer, SPSA module, trace store, report generator.
- `Success metrics`: deterministic configuration, matched provider budgets, test isolation, replicated multi-seed results.
- `Risk controls`: no advantage label without matched baselines; bounded device calls; raw trace retention; no personal data.
- `Limitations`: cannot establish quantum advantage from simulator runs or small benchmarks.
- `Deployment model`: local research harness.
- `Evaluation plan`: unit tests, simulator replay, provider parity tests, and paired device acceptance.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Hinton et al., Distilling the Knowledge | Foundational | Teacher/student soft-target distillation. | https://arxiv.org/abs/1503.02531 |
| CUDA-Q | Official software | Simulator interface used by the source. | https://nvidia.github.io/cuda-quantum/ |
| KDFlow DEP | Related Black Lake review | Distillation systems and workload separation. | `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/` |
| CAP Rank Sparsity DEP | Related Black Lake review | Structured compression and global capacity allocation. | `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/` |
| Efficient FM Survey DEP | Related Black Lake review | End-to-end efficiency taxonomy. | `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2603.14898 | Identity, authors, date, abstract, DOI, license locator. | 2026-07-20 | Metadata only. |
| R2 | https://arxiv.org/html/2603.14898 | Complete architecture, results, methods, supplement, availability. | 2026-07-20 | Verified local copy withheld. |
| R3 | https://arxiv.org/pdf/2603.14898 | Primary PDF and cross-format evidence. | 2026-07-20 | Verified local copy withheld. |
| R4 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-KDFlow%20LLM%20Distill | Related distillation synthesis. | 2026-07-20 | Repository context. |
| R5 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-CAP%20Rank%20Sparsity | Related compression synthesis. | 2026-07-20 | Repository context. |
| R6 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260718-Efficient%20FM%20Survey | Related systems-efficiency synthesis. | 2026-07-20 | Repository context. |

## Appendix

### Selection, Deduplication, and Integrity

- Uniform draw: one-based index 1,331 of 75,776 unique units from 75,779 PDFs.
- Duplicate exclusions: 0; reselections: 0; current-job duplicates: 0.
- Dedup surfaces: Black Lake artifacts/index, automation memory, relevant Black-Lake-Data records, current-job set, and public-safe 24-hour markers.
- Source gate: PDF 3,092,761 bytes with valid header/EOF; official HTML 755,603 bytes with 149,172 body characters, 9 document markers, 144 headings, and 30 structure terms.
- Source locality: PDF, HTML, metadata, verification records, and caches withheld; no `.source/`; zero source uploads.

### Replication Checklist

- Obtain exact code, fixed projection matrices, splits, seeds, and simulator configuration.
- Reproduce Table 1 and full-convolution compression results.
- Run fixed-photonic, Gaussian-random, dictionary-only, and learned-classical baselines.
- Measure trainable and fixed memory, sampler calls, time, and energy proxy.
- Pair simulator and device runs under identical shot and evaluation budgets.
