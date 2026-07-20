# Report-Mark: WKGM MRI Reconstruction

## Source Metadata

| Field | Value |
|---|---|
| Paper | *WKGM: Weight-K-space Generative Model for Parallel Imaging Reconstruction* |
| Authors | Zongjiang Tu; Die Liu; Xiaoqing Wang; Chen Jiang; Pengwen Zhu; Minghui Zhang; Shanshan Wang; Dong Liang; Qiegen Liu |
| arXiv | `2205.03883v4`; submitted 2022-05-08; revised 2022-11-25 |
| arXiv DOI | `10.48550/arXiv.2205.03883` |
| Journal | *NMR in Biomedicine* 36(11), e5005; first published 2023-08-07 |
| Publisher DOI | `10.1002/nbm.5005` |
| Primary locators | https://arxiv.org/abs/2205.03883 ; https://arxiv.org/pdf/2205.03883 ; https://doi.org/10.1002/nbm.5005 |
| Official implementation | https://github.com/yqx7150/WKGM |
| Source access date | 2026-07-20 |
| Review status | Complete source-first review; no experiment reproduced |
| Source policy | Local source documents, endpoint responses, cache text, integrity records, and review renders withheld; no `.source/` directory created |

The local archive unit initially contained a valid PDF and brief README but no full-paper HTML. The official arXiv and approved ar5iv HTML endpoints returned content byte-identical to the abstract/metadata page and were rejected. A provenance-labeled full-text HTML rendering was then derived page-by-page from the verified 11-page PDF and passed the complete-paper checks. The e-print endpoint returned a PDF rather than a TeX/source archive; it was retained locally as invalid source-package evidence and was not treated as source text.

## Concise Research Notes

WKGM learns a score-based generative prior directly in weighted k-space. A radial weighting function suppresses dominant low-frequency magnitude and lifts high-frequency structure so the score network sees a narrower dynamic range. The complex weighted data are expanded into a six-channel real-valued tensor. A variance-exploding stochastic differential equation trains an NCSN++-style score network; reconstruction uses reverse-SDE predictor-corrector sampling with acquired-sample data consistency after predictor and corrector updates.

The iterative design permits an additional k-space reconstruction operator. The paper instantiates this as SVD-WKGM, alternating the learned prior with SAKE's structured low-rank Hankel projection. This hybrid is the strongest reported configuration in most displayed brain comparisons, especially at high acceleration.

The empirical case is useful but narrow. Training begins from 500 two-dimensional 12-channel images described as coming from one healthy volunteer, coil-compressed to single-coil images and augmented to 4,000 training examples. External comparisons use several scanners, contrasts, coils, and sampling masks, but many are single images or selected slices. Tables report point PSNR/SSIM values without seeds, uncertainty, subject-level cohort counts, statistical tests, or clinical reader assessment.

## Method and Evidence Notes

### Mechanism

1. **Weight-k-space transform:** Equation 7 multiplies k-space by a radial weight controlled by `r` and `p`, reducing the low/high-frequency dynamic range.
2. **Six-channel augmentation:** Real and imaginary weighted components are concatenated into a six-channel tensor. Table VII supports six channels as a practical point between two and eight channels, but the comparison does not isolate architecture capacity from representation choice.
3. **Score prior:** A variance-exploding SDE and denoising score objective learn the weighted k-space distribution.
4. **Predictor-corrector reconstruction:** Algorithm 1 alternates reverse-diffusion predictor/corrector updates with unweighting, channel averaging, and acquired-sample data consistency.
5. **Low-rank hybrid:** Algorithm 2 inserts SAKE Hankel construction, singular-value thresholding, and projection into the inner loop, producing SVD-WKGM.

### Quantitative evidence

| Setting | Comparator | Comparator PSNR/SSIM | SVD-WKGM PSNR/SSIM | Reviewer note |
|---|---|---:|---:|---|
| T1-weighted, 2D Poisson `R=4` | SAKE | 35.71 / 0.916 | 36.15 / 0.923 | Modest point gain; no uncertainty |
| T1-weighted, 2D Poisson `R=8` | SAKE | 32.92 / 0.851 | 34.03 / 0.881 | Larger high-acceleration point gain |
| T1 GE Brain, 2D Random `R=4` | SAKE | 41.54 / 0.952 | 43.85 / 0.970 | Strongest displayed PSNR margin in Table II |
| T2 Transverse Brain, 2D Poisson `R=10` | SAKE | 29.75 / 0.823 | 31.69 / 0.841 | High-acceleration result used as the headline finding |
| T2 Brain, vertical `R=3` | image-domain Langevin | 37.47 / 0.940 | 38.42 / 0.953 | About 0.95 dB point gain |
| Knee, Cartesian `R=3`, slice 100 | supervised k-space DL | 35.35 / 0.813 | 34.46 / 0.790 | Counterexample: supervised method is better |
| Knee, 2D Poisson `R=6`, slice 100 | supervised k-space DL | 30.96 / 0.767 | 31.70 / 0.810 | Hybrid is better under the displayed Poisson case |
| T2 Transverse Brain, 2D Poisson `R=10` | No-Weight | 25.00 / 0.737 | 31.69 / 0.841 | Supports weighting plus hybrid pipeline, not weighting alone |

The ablations show that weighting materially helps at severe undersampling and that six or eight channels outperform two channels on the selected T1 GE case. However, SVD-WKGM's result combines the weight transform, six-channel representation, score prior, data consistency, and SAKE. A complete factorial, matched-compute ablation is absent.

### Visual evidence

Rendered pages 7-10 confirm that Tables I-VIII and Figures 6-13 are legible and correspond to the extracted values. Residual maps are amplified four or five times and are source-selected qualitative examples. They show plausible detail preservation but do not provide blinded selection, complete failure galleries, lesion-level sensitivity, or inter-reader agreement.

### Code and reproducibility evidence

The official repository README supplies training and test commands, links a checkpoint, and states non-commercial use. `main.py` exposes train/eval entry points; `demo_svdWKGM.py` restores a checkpoint and invokes the score sampler; the inspected configuration identifies VE-SDE, predictor-corrector sampling, NCSN++, six channels, and related hyperparameters. No root `requirements.txt` or `LICENSE` was found. The code was not cloned or executed, so dataset preparation, checkpoint identity, SAKE integration, table reproduction, and environment compatibility remain unverified.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limitation |
|---|---|---|---|---|
| E1 | Verified arXiv v4 PDF, all pages | Identity, equations, algorithms, experiments, tables, figures, conclusion | High for source transcription | No independent reproduction |
| E2 | PDF-derived full-text HTML and extraction cache | Searchable full-paper review and cross-checking | High for text coverage | Derived rendering does not preserve publisher HTML semantics |
| E3 | Rendered PDF pages 4 and 7-11 | Method diagrams, table values, residual images, convergence and ablation figures | High for layout verification | Selected figures remain qualitative source evidence |
| E4 | arXiv metadata | Authors, dates, version, DOI, public locators | High | Metadata alone does not validate results |
| E5 | Wiley journal record | Journal title, volume/issue, e5005, publication date, DOI | High for bibliography | Journal full text was not compared line-by-line with arXiv v4 |
| E6 | Official GitHub README and key scripts | Code availability, entry points, configuration, usage notice | Medium-high for availability | No execution, dependency lock, root license, or table reproduction |
| E7 | Hypercomplex MRI DEP-E | Direct accelerated-MRI representation and evaluation bridge | Medium | Different architecture and cohort; not validation of WKGM |
| E8 | Residual Gaussian CBCT DEP-E | Sparse-view inverse reconstruction and detail-preservation bridge | Medium | Different modality and 3D representation |
| E9 | Acoustic Phase Retrieval DEP-E | Fourier/Hankel inverse-problem and conditioning bridge | Medium | Analytic acoustic setting, not learned MRI |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md`
   **Relevance:** Both papers reconstruct accelerated MRI from undersampled k-space and explicitly couple real/imaginary or multi-channel structure. Hypercomplex MRI contributes matched parameter/resource and clinical-reliability questions that WKGM's PSNR/SSIM-only evaluation does not answer.
   **Source basis:** The DEP substantively reviews arXiv:2503.05063 and its official implementation.

2. `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md`
   **Relevance:** Both address ill-posed medical-image reconstruction under sparse measurements and argue that ordinary optimization loses high-frequency detail. RGS separates low-frequency structure and residual detail; WKGM reweights k-space and optionally adds a low-rank projector.
   **Source basis:** The DEP substantively reviews arXiv:2604.27552 and its sparse-view CBCT tables and ablations.

3. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md`
   **Relevance:** Both are structured inverse problems using Fourier-domain information and Hankel-related operators. The acoustic work makes identifiability and conditioning explicit, offering a useful contrast to WKGM's empirical data-consistency and low-rank constraints.
   **Source basis:** The DEP substantively reviews arXiv:1803.11323 and DOI `10.1088/1361-6420/aaccda`.

## Synthesis Note

### Concept Bridge

WKGM can be read as a three-layer constraint system. The learned score prior proposes plausible weighted k-space; data consistency anchors acquired samples; SAKE optionally projects multi-coil neighborhoods toward a structured low-rank set. Hypercomplex MRI shows another way to encode complex-channel structure inside the network. Residual Gaussian CBCT shows how explicit frequency allocation can keep an inverse solver from smoothing away detail. Acoustic Phase Retrieval shows the value of measuring conditioning and identifiability before trusting an inverse pipeline. Together, the bridge is not “use generative models everywhere”; it is “make representation, measurement constraint, and uncertainty separately auditable.”

### Potential Implementations

1. **Offline WKGM reproduction harness:** A pinned, non-clinical pipeline that reconstructs public or synthetic k-space under controlled masks, logs every projector/prior update, and compares WKGM, SAKE, SVD-WKGM, and no-weight variants at matched compute.
2. **Selective reconstruction review gate:** A local service that checks acquired-sample residual, multi-coil consistency, ensemble variation, and localized high-frequency disagreement, then escalates uncertain cases rather than silently returning one image.
3. **Constraint-composition workbench:** A research interface for swapping weight functions, channel encodings, score priors, and low-rank projectors while maintaining a common evidence ledger for quality, runtime, memory, and failure modes.

### Deeper Relationship Observations

1. The weight transform and RGS wavelet prior both redistribute optimization attention toward weak high-frequency structure, but WKGM changes the learned data representation while RGS changes capacity initialization and residual routing.
2. SAKE's Hankel projection and acoustic Fourier reconstruction both exploit structured measurement operators; the acoustic paper exposes determinant margins, whereas WKGM reports empirical robustness without an analogous conditioning certificate.
3. Hypercomplex coupling and WKGM's six-channel augmentation both treat complex MRI structure as more than two unrelated scalar channels, but neither evaluation fully isolates representation benefit from capacity, training, or compute changes.

### Conceptual Similarities

1. All four works solve underdetermined inverse problems by adding structured prior information rather than relying on a naïve inverse alone.
2. Each method separates a data-fidelity or measurement-consistency term from a prior or representation mechanism.
3. Each exposes a transfer gap between source-reported aggregate fidelity and deployment-relevant reliability under mismatch, resource limits, or high-stakes interpretation.

### MVP Implementations with Code Mock-ups

1. **Acquired-sample residual gate**

```python
def acquired_residual(mask, measured, reconstructed_k):
    residual = mask * (reconstructed_k - measured)
    score = (abs(residual) ** 2).mean() ** 0.5
    return {"residual_rms": float(score), "pass": bool(score <= 1e-3)}
```

This toy gate is local-only and does not certify clinical quality. It verifies one non-negotiable property: the output should remain consistent with acquired samples within a declared tolerance.

2. **Matched-compute ablation ledger**

```python
def record_run(name, psnr, ssim, seconds, peak_mb, svd_calls):
    return {
        "variant": name,
        "quality": {"psnr": psnr, "ssim": ssim},
        "cost": {"seconds": seconds, "peak_mb": peak_mb, "svd_calls": svd_calls},
    }
```

The ledger forces quality claims to travel with realized cost. A production harness would add device, precision, mask, seed, dataset revision, and failure status.

3. **Ensemble disagreement review trigger**

```python
import numpy as np

def review_trigger(reconstructions, threshold=0.02):
    stack = np.asarray(reconstructions, dtype=np.float32)
    disagreement = stack.std(axis=0)
    return disagreement, bool(np.quantile(disagreement, 0.99) > threshold)
```

This synthetic example treats stochastic variation as a review signal, not calibrated uncertainty. Clinical use would require reference-free calibration, shift testing, privacy controls, and human escalation rules.

### Developer Challenges

1. Reconstructing the paper's exact environment requires resolving missing dependency locks, dataset preparation, mask generation, checkpoint identity, and licensing constraints.
2. A fair implementation must instrument all 1,000 predictor-corrector steps, data-consistency operations, and SAKE singular-value decompositions without changing numerical behavior.
3. Reliability tooling must avoid logging raw k-space, patient identifiers, or reconstructed clinical images while retaining enough evidence for debugging and audit.

### Author Challenges

1. Publish subject-level cohort definitions, split provenance, masks, seeds, uncertainty, failure cases, and statistical analyses rather than only selected slice-level point estimates.
2. Separate the effects of weighting, six-channel augmentation, score prior, data consistency, and SAKE with matched-compute factorial ablations.
3. Provide a licensed, pinned reproduction package and evaluate pathology preservation, scanner/protocol shift, latency, memory, energy, and blinded clinical acceptability.

## Validation Notes

- Random selection used one uniform zero-based draw from 75,776 PDF-parent paper units; the first draw was accepted with zero exclusions and zero reselections.
- Dedup checks covered arXiv version/base ID, both DOIs, normalized title, slug, public pointer, logs, reports, DEPs, automation memory, companion-repository entries, and same-paper markers within 24 hours.
- Review did not begin until the archive was classified `complete` under the PDF and full-text HTML integrity rules.
- Cache lookup was an initial miss; local `missing-only` extraction completed `cached` with `pypdf` and HTML text.
- All eight tables and thirteen figure captions were inspected; pages 4 and 7-11 were rendered for visual verification.
- Exactly three related DEP entries were inspected and are listed above.
- No experiment, proof, code path, checkpoint, or clinical result was independently reproduced.
- No local absolute path, machine identifier, username, exact execution timestamp, or local timezone label appears in this report.
- No source file, source derivative, cache text, integrity record, or temporary rendering is included in the repository artifact set.

## Attribution Block

- Source URL: https://arxiv.org/abs/2205.03883
  - Applies to: paper identity, authors, dates, version, abstract, arXiv DOI, and source locators.
  - Notes: Metadata page only; not treated as full-paper evidence.
- Source URL: https://arxiv.org/pdf/2205.03883
  - Applies to: full-paper method, equations, algorithms, tables, figures, experiments, limitations, and conclusion.
  - Notes: Verified locally; source file withheld.
- Source URL: https://doi.org/10.1002/nbm.5005
  - Applies to: journal publication metadata and publisher DOI.
  - Notes: Wiley journal record inspected; journal full text was not redistributed.
- Source URL: https://github.com/yqx7150/WKGM
  - Applies to: official implementation availability, README usage statement, entry points, and configuration evidence.
  - Notes: Repository inspected but not cloned or executed; no root dependency lock or license file was found.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md
  - Applies to: related accelerated-MRI representation and evaluation bridge.
  - Notes: Processed DEP evidence; does not validate WKGM.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Residual%20Gaussian/residual_gaussian_cbct_manuscript.md
  - Applies to: related sparse medical inverse-reconstruction and detail-preservation bridge.
  - Notes: Processed DEP evidence; does not validate WKGM.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Acoustic%20Phase%20Retrieval/acoustic_phase_retrieval_manuscript.md
  - Applies to: related Fourier/Hankel inverse-problem and conditioning bridge.
  - Notes: Processed DEP evidence; does not validate WKGM.
