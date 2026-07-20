# Report-Mark: Photonic Quantum KD

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P02`
- Review date: 2026-07-20
- Review type: source-first hybrid quantum/classical ML review and implementation synthesis

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Photonic Quantum-Enhanced Knowledge Distillation* |
| Authors | Kuan-Cheng Chen; Shang Yu; Chen-Yu Liu; Samuel Yen-Chi Chen; Huan-Hsin Tseng; Yen Jui Chang; Wei-Hao Huang; Felix Burt; Esperanza Cuenca Gomez; Zohim Chandani; William Clements; Ian Walmsley; Kin K. Leung |
| Stable identifier | arXiv:2603.14898v1 |
| Submission date | 2026-03-16 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2603.14898 |
| Primary record | https://arxiv.org/abs/2603.14898 |
| Full-paper HTML | https://arxiv.org/html/2603.14898 |
| PDF | https://arxiv.org/pdf/2603.14898 |
| License visibility | Creative Commons license link visible on arXiv. |
| Source state | Verified complete after bounded official-source repair; all files withheld locally. |
| Deployment job ID | `BLAD-2200-20260720-8636EDC7` |
| Deployment item ID | `BLAD-2200-20260720-8636EDC7-P02` |

## Concise Research Notes

### Problem and Method

The paper asks whether a shot-based continuous-variable photonic sampler can serve as a compact training-time conditioning mechanism for knowledge distillation. PQKD replaces selected dense convolution kernels with a small learned spatial dictionary. Channel-mixing coefficients are generated from a 512-dimensional feature formed from two 256-bin marginals of thresholded measurements from a 16-mode photonic circuit. A fixed linear projection maps that feature into layer mixing tensors.

Student weights are trained with a hard-label plus teacher-soft-target distillation loss. Photonic parameters are updated without differentiating through the sampler: the method alternates standard Adam student updates with ten SPSA outer updates per epoch on a validation proxy. Exponential moving-average feature smoothing reduces shot-to-shot variance.

### Evidence and Results

The partial-compression experiment reports five-run means. MNIST validation accuracy is 99.09% for PQKD versus 99.07% for the teacher; Fashion-MNIST is 92.42% versus 91.86%; CIFAR-10 is 79.72% versus 86.99%. The CIFAR gap shows that regularization and compression benefits on simpler tasks do not transfer automatically to a harder dataset.

On MNIST, compressing all convolutional layers produces reported compression factors of 48.81x, 76.18x, and 105.40x across three teacher widths, with PQKD validation accuracy of 96.85%, 97.17%, and 97.33% versus teacher accuracy near 99%. Parameter accounting includes the photonic parameter budget once and excludes fixed projection matrices because they are not trainable; that convention does not equal end-to-end memory, energy, or latency cost.

Shot-noise experiments fit an accuracy-gain curve of the form delta(S)=delta-infinity-k/sqrt(S). EMA improves the weighted fit from 0.596 to 0.901 and the supplement reports a median feature-variance ratio of 0.0406 at 200 shots with beta=0.9. These are source-reported simulator results, not hardware measurements.

### Reviewer Interpretation

The paper's credible contribution is a structured, sample-only interface between a stochastic photonic module and a classical compressed network. Its quantum advantage is not established. Photonic sampling used the ORCA simulator backend in CUDA-Q; the paper states that compatible hardware can replace it through the same interface. Code was not public at inspection time, and the fixed projection matrices, sampler cost, hardware energy, wall-clock latency, and classical random-feature baselines are essential to any end-to-end advantage claim.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limits |
|---|---|---|---|---|
| E1 | Canonical arXiv record and DOI | Identity, authors, date, subjects, license link | High | Metadata only. |
| E2 | Verified HTML and PDF | Architecture, formulas, training, experiments, supplement, limitations | High for transcription | No independent rerun. |
| E3 | Table 1 and Figure 2 | Five-run MNIST/Fashion/CIFAR performance | High for source report | Small task/model set; simulator backend. |
| E4 | Figure 3 and compression table | Rank/scope/teacher-width frontier | High for source report | Trainable-parameter ratio excludes fixed projection storage and runtime cost. |
| E5 | Figure 4 and Supplement S3/S6 | Shot-noise scaling and EMA variance reduction | Medium-high | Fitted simulator evidence; hardware drift emulated. |
| E6 | Methods 4.7 and code availability | ORCA simulator, PyTorch/CUDA, fixed hyperparameters, code access limit | High | Hardware execution not demonstrated. |
| E7 | Private process records | Randomness, dedup, repair, integrity, locality | High | Private paths withheld. |
| E8 | Three related DEP manuscripts | Distillation, compression, and systems-efficiency synthesis | Medium | Different models and substrates. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md`
   - Relevance: KDFlow separates teacher inference and student training into specialized execution paths; PQKD separates differentiable student optimization from black-box photonic sampling. Both need matched quality and systems-cost receipts.
   - Source basis: inspected teacher hidden-state transfer, shared-memory workflow, reported speedups, downstream quality, and non-reproduction boundary.
2. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md`
   - Relevance: CAP allocates low-rank and sparse capacity globally; PQKD constrains kernels to a learned spatial basis with photonic-conditioned mixing. Both turn compression into a structured capacity-allocation problem rather than uniform width reduction.
   - Source basis: inspected RPCA decomposition, global Bernoulli allocation, matched budgets, hardware limitation, and reproducibility gaps.
3. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md`
   - Relevance: the survey's architecture/algorithm/system taxonomy exposes what PQKD's trainable-parameter ratio omits: fixed-matrix memory, sampling throughput, optimizer evaluations, hardware energy, and deployment runtime.
   - Source basis: inspected lifecycle taxonomy, compression/distillation coverage, hardware-system boundary, and end-to-end evaluation recommendations.

## Synthesis Note

### Concept Bridge

PQKD combines three efficiency levers: distillation transfers teacher behavior, dictionary convolutions restrict trainable capacity, and a stochastic physical-style sampler chooses channel mixing. The related deposits show why these levers need a shared accounting boundary. Quality, trainable parameters, fixed state, sampling calls, optimizer evaluations, energy, latency, and classical baselines must be measured together before the photonic component can be credited with an advantage.

### Potential Implementations

1. **Sampler-agnostic conditioning harness:** run identical student/dictionary training against photonic, fixed-photonic, Gaussian-random, and learned-classical feature providers.
2. **Compression frontier registry:** record rank, compressed scope, trainable and fixed memory, accuracy, calibration, wall-clock time, sampling calls, and energy proxy.
3. **Hardware-transition gate:** require interface compatibility, distribution drift checks, shot-budget stability, and matched simulator/hardware receipts before substituting a device.

### Deeper Relationship Observations

1. A fixed random projection can remove trainable parameters while retaining substantial memory and compute, so parameter compression is not system compression.
2. SPSA enables black-box optimization but multiplies sampler evaluations and introduces validation-loop selection pressure.
3. EMA trades variance for temporal lag; it can stabilize shot noise while obscuring rapid hardware drift unless raw and smoothed traces are both retained.

### Conceptual Similarities

1. PQKD and KDFlow treat teacher and student work as asymmetric computational roles.
2. PQKD and CAP Rank Sparsity represent dense weights through smaller structured bases plus allocation variables.
3. PQKD and the Efficient FM Survey distinguish model-level compression from end-to-end system efficiency.

### MVP Implementations with Code Mock-Ups

1. **Provider interface**

```python
def conditioning(provider, shots, seed):
    return provider.sample_feature(shots=shots, seed=seed)
```

2. **Accounting receipt**

```python
def compression_receipt(trainable, fixed_bytes, sampler_calls):
    return {"trainable": trainable, "fixed_bytes": fixed_bytes,
            "sampler_calls": sampler_calls}
```

3. **Transition gate**

```python
def hardware_ready(sim, device, tolerance):
    return abs(sim["accuracy"] - device["accuracy"]) <= tolerance and device["drift_ok"]
```

### Developer Challenges

1. Reproducing the 16-mode, 512-feature sampler interface and fixed projection conventions without hidden shape or counting differences.
2. Keeping SPSA validation evaluations, feature samples, EMA state, and random seeds isolated from final test selection.
3. Measuring fixed-matrix memory, shot latency, device drift, and sampler energy alongside conventional GPU training cost.

### Author Challenges

1. Demonstrating results on actual photonic hardware with matched simulator and classical-feature baselines.
2. Releasing code, splits, seeds, fixed matrices, simulator configuration, and raw multi-run data for independent reproduction.
3. Scaling beyond small CNNs and three image benchmarks while preserving accuracy, sampler feasibility, and honest end-to-end cost accounting.

## Validation Notes

- Deployment job `BLAD-2200-20260720-8636EDC7`; item `BLAD-2200-20260720-8636EDC7-P02`.
- Uniform index 1,331 of 75,776 units; first draw; duplicate exclusions 0; reselections 0.
- No duplicate by identifier, DOI, normalized title, slug, artifacts, memory, companion repository, current job, or 24-hour markers.
- Partial archive repaired to verified complete with official HTML; PDF and HTML gates passed.
- Main paper, methods, supplement, tables, figures, metadata, and exactly three related manuscripts inspected; no code, simulator, hardware, or experiment rerun.
- Exactly three entries appear in every required Synthesis Note list; three bounded Python mock-ups are present.
- Public sanitization passed subject to final scan; no `.source/` and no source file eligible for staging.

## Attribution Block

- https://arxiv.org/abs/2603.14898 - identity, authors, date, abstract, subjects, DOI, and license locator.
- https://arxiv.org/html/2603.14898 - complete architecture, experiments, methods, supplement, availability statements; verified local copy withheld.
- https://arxiv.org/pdf/2603.14898 - cross-format primary evidence; verified local copy withheld.
- https://doi.org/10.48550/arXiv.2603.14898 - persistent identity.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-KDFlow%20LLM%20Distill - distillation-system synthesis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-CAP%20Rank%20Sparsity - structured-compression synthesis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260718-Efficient%20FM%20Survey - end-to-end efficiency synthesis.
- Source files: verified PDF, official full-paper HTML, metadata HTML, and private verification records; all withheld locally. Zero source uploads. Job `BLAD-2200-20260720-8636EDC7`, item `BLAD-2200-20260720-8636EDC7-P02`.
