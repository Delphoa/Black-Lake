# Report-Mark: Feature Denoising

- Public run marker: 2026-07-21 (date only)
- Review type: Source-first paper review, critique, implementation translation, and DEP-E synthesis
- Source policy: Complete source inspected locally; all source documents withheld from the public repository

## Source Metadata

| Field | Value |
|---|---|
| Title | *Feature Denoising for Improving Adversarial Robustness* |
| Authors | Cihang Xie; Yuxin Wu; Laurens van der Maaten; Alan L. Yuille; Kaiming He |
| arXiv | arXiv:1812.03411v2; submitted 2018-12-09; revised 2019-03-25 |
| DOI | https://doi.org/10.48550/arXiv.1812.03411 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pages 501-509 |
| Primary record | https://arxiv.org/abs/1812.03411 |
| Publisher record | https://openaccess.thecvf.com/content_CVPR_2019/html/Xie_Feature_Denoising_for_Improving_Adversarial_Robustness_CVPR_2019_paper.html |
| Official code | https://github.com/facebookresearch/ImageNet-Adversarial-Training |
| Code status | Public model/evaluation/training release; repository archived read-only in 2021; CC BY-NC 4.0; legacy TensorFlow/Tensorpack/Horovod dependencies |
| Access date | 2026-07-21 |

## Selection and Deduplication

`rg --files -g "*.pdf"` found 75,779 PDFs representing 75,776 unique parent-directory paper units. After sorting the unique units, PowerShell `Get-Random` selected zero-based index 61,119 uniformly. The first draw was accepted with zero duplicate exclusions, zero other exclusions, and zero reselections.

Dedup scanned the live Black-Lake `.logs`, `.reports`, `.lake-data`, and `.staging` trees; automation memory; the relevant Black-Lake-Data trees; and the prior 24 hours of same-paper markers. Keys included arXiv ID `1812.03411`, the arXiv DOI, normalized title, and slug variants. The only match was a metadata-only author-inventory row in Black-Lake-Data; no prior processed Arxiv DEP log, report, or `DEP-E-*` artifact was found.

## Local Source Integrity

The selected unit was initially partial: its existing 8,228,548-byte PDF passed size, `%PDF-`, trailing `%%EOF`, and SHA-256 checks, but full-paper HTML was missing. Review paused while a bounded repair preserved the PDF and collected official metadata HTML, approved ar5iv full-paper HTML, and the arXiv source archive. The final HTML passed with 218,260 bytes, 47,873 body characters, a document marker, 57 section/heading markers, six paper-structure term classes, no error/abstract-only marker, and zero partial files. The local README, provenance, summaries, and verification report were updated before substantive review.

No source document, archive, extracted text, cache, render, verification record, or private archive reference is included in this repository. No `.source/` directory was created.

## Research Notes

### Problem and Mechanism

The paper interprets adversarially induced, spatially diffuse feature activations as feature noise. It inserts a denoising operation into a residual block: a non-local, bilateral, mean, or median filter transforms an intermediate feature map; a learned `1 x 1` convolution combines channels; and an identity connection restores a signal-preserving path. The default ResNet configuration adds four blocks after the last residual block of `res2`, `res3`, `res4`, and `res5` and trains the entire model end-to-end.

The best-performing operation is Gaussian non-local means, closely related to self-attention and non-local networks. The dot-product non-local version is nearly as accurate and avoids the Gaussian embedding parameters. Local filters improve the white-box results, but in the black-box ablation they are not convincingly better than the parameter-matched null block; non-local context is the more consistent component there.

### Training and Threat Model

Training uses targeted PGD with an `L_inf` budget of 16/256, step size 1, and 30 inner attack iterations. Twenty percent of training batches initialize PGD from the clean image; 80% start randomly within the perturbation cube. Synchronized SGD runs on 128 V100 GPUs with 32 images per GPU, total batch size 4,096, for 110 epochs. The paper reports about 38 hours for a ResNet-101 baseline and 52 hours for a ResNet-152 baseline; the official repository reports about 90 hours for the denoising ResNet-152 under its documented setting.

Evaluation uses ImageNet's 50,000 validation images and targeted PGD with a uniformly sampled incorrect target. The white-box evaluation uses `epsilon=16`, random initialization, and 10-2,000 iterations; the black-box CAAD analysis uses `epsilon=32` even though models were trained at 16. The release notes explicitly do not cover untargeted attacks or attacker-controlled target labels, which bounds generalization.

### Evidence and Results

- At 10 PGD iterations, the authors' ResNet-152 adversarial-training baseline reaches 52.5% and the four-block Gaussian non-local model reaches 55.7%, a 3.2-point gain. The 27.9% ALP result is a system-level comparison with a different Inception-v3 backbone and implementation.
- At 2,000 iterations, the corresponding baseline and denoising results are 39.2% and 42.6%, a 3.4-point gain. The blocks are differentiable, so the white-box attacker back-propagates through them.
- The parameter-matched null and added-capacity controls underperform all denoising variants in the reported white-box ablation. Removing the `1 x 1` convolution reduces 100-step accuracy from 45.5% to 36.8%; removing the residual path makes training unstable.
- Under five CAAD 2017 black-box attackers with the strict all-or-nothing criterion, the ResNet-152 baseline scores 43.1%, a null block scores 44.1%, non-local dot product scores 46.2%, Gaussian non-local scores 46.4%, and placing denoising after every residual block scores 49.5%.
- The CAAD 2018 winning ResNeXt-101 submission uses non-local denoising after every residual block and reports 50.6% on a secret ImageNet-like test set against 48 unknown attackers, versus 40.8% for second place.
- In clean-only training, denoising variants remain within roughly 0.2 points of the ResNet-152 reference. With adversarial training, clean accuracy is 62.32% for the baseline and 65.30% for the denoising model, compared with 78.91% and 79.08% for their clean-trained counterparts.

### Reviewer Assessment

The controlled evidence supports a modest but consistent architecture contribution on top of an unusually strong adversarial-training system. The most persuasive result is not the 27.9%-to-55.7% headline; it is the repeated 3-point-class improvement over the authors' matched baseline plus the null, capacity, filter, and block-design ablations. Confidence is high that the paper reports these results and medium that the design generalizes beyond its targeted ImageNet/PGD setting.

Important limits remain: feature noise is visualized but not quantitatively defined; CAAD 2018 is not independently reproducible; seeds, intervals, and statistical tests are absent; later multi-attack evaluation standards are outside the paper's era; and the official release is costly and tied to legacy frameworks. The result is best treated as a strong architecture hypothesis that deserves modern re-evaluation, not a current robustness certificate.

## Evidence Ledger

| ID | Source | Evidence Used | Supports | Confidence | Limitation |
|---|---|---|---|---|---|
| E1 | arXiv v2 metadata/PDF/full-paper HTML/source | Identity, dates, complete method, Figures 1-8, Tables 1-3, conclusion | Paper reconstruction and quantitative claims | High for transcription | No independent experiment |
| E2 | CVPR open-access record | Venue, author attribution, pages, accepted-version context | Publication metadata | High | Abstract-level web page; experiments come from E1 |
| E3 | Official GitHub README and instructions | Models, evaluation/training commands, dependencies, runtime notes, license, archived state | Reproducibility and implementation assessment | High for inventory | Code and checkpoints were not executed |
| E4 | Official `nets.py` | Four default insertion points and denoising-after-every-block ResNeXt configuration | Implementation correspondence | High | Only focused code paths inspected |
| E5 | Local integrity verification summarized publicly | PDF/HTML gate, hashes, no partials, repair result | Source completeness | High | Source files and private paths withheld |
| E6 | Three related Black-Lake manuscripts | Adversarial training, representation robustness, and filtering architecture parallels | Cross-DEP synthesis | Medium | Related artifacts do not validate this paper |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md`
   - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md
   - Relevance: Both works treat adversarial training as the main robustness engine and ask how model internals or targets should change under perturbation. The related DEP adds robust-overfitting, teacher calibration, and threat-transfer controls that the 2019 feature-denoising evaluation lacks.
   - Source basis: Its reviewed primary paper, *Label Noise in Adversarial Training*, including PGD/AutoAttack tables and the KD-AT-Auto method.
2. `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md`
   - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-ViT%20Semantic%20Robustness/vit_semantic_robustness_manuscript.md
   - Relevance: Both center representation geometry rather than output accuracy alone. Feature denoising attempts to suppress adversarial activation noise; PRM deliberately moves embeddings under bounded pixel changes, providing a complementary representation-level stress test.
   - Source basis: Its reviewed primary paper, *Are Vision Transformer Representations Semantically Meaningful?*, including representation-matching equations and Tables I-III.
3. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md`
   - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md
   - Relevance: Both translate filtering into trainable feature-space architecture and compare local versus global/non-local mixing. AFIDAF's image/Fourier allocation also highlights the need for parameter-, FLOP-, latency-, and task-matched controls.
   - Source basis: Its reviewed primary AFIDAF paper, especially the AFFNet/IDAF/AFIDAF controlled comparisons and downstream dense-prediction tables.

## Synthesis Note

### Concept Bridge

Across the four works, robustness is a property of a pipeline rather than one layer or metric. Feature denoising alters intermediate transport of signal and perturbation; adversarial-label correction alters supervision under perturbed inputs; representation matching tests whether bounded pixel changes can redirect embeddings; and AFIDAF allocates local and global filters to different feature roles. Together they suggest a modern audit should jointly measure internal geometry, supervision stability, output robustness, clean utility, and systems cost under one pinned threat manifest.

### Potential Implementations

1. **Denoising block benchmark:** Add parameter-matched residual, local-filter, and non-local blocks to current CNN/ViT backbones; evaluate clean accuracy, corruption accuracy, targeted/untargeted robustness, latency, memory, and energy with fixed seeds and attacks.
2. **Representation-noise observatory:** Capture layerwise clean/adversarial feature deltas before and after candidate blocks, normalize for feature scale, and correlate measured suppression with robust accuracy and calibration.
3. **Robustness evidence card:** Export a versioned card binding model hash, training recipe, threat model, attack convergence, matched controls, uncertainty, clean-robust trade-off, hardware cost, and missing evidence.

### Deeper Relationship Observations

1. The denoising gain is conditional on strong adversarial training, just as label rectification is conditional on a competent robust teacher; neither architecture nor supervision correction substitutes for a credible inner maximization.
2. Non-local filtering's stronger black-box result and PRM's targeted embedding movement both point to long-range representation geometry as a robustness variable, but neither proves semantic preservation without external concept or human-equivalence tests.
3. The residual plus `1 x 1` combination is a learned signal-preservation gate; AFIDAF's alternating operators and KD-AT-Auto's interpolated targets express the same broader pattern of combining a corrective transform with an identity/reference path.

### Conceptual Similarities

1. Each work separates a primary signal from a perturbation, mismatch, or missing interaction and then introduces a bounded corrective mechanism.
2. Each relies on controlled comparisons to distinguish mechanism from extra capacity or stronger training, even though the completeness of those controls varies.
3. Each requires an evaluation boundary: threat model for adversarial work, task/hardware manifest for filtering architectures, and semantic-equivalence criteria for representation claims.

### MVP Implementations with Code Mock-ups

#### 1. Matched Robustness Delta

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Result:
    model: str
    attack_steps: int
    epsilon: float
    accuracy: float


def matched_delta(baseline: Result, candidate: Result) -> float:
    assert baseline.attack_steps == candidate.attack_steps
    assert baseline.epsilon == candidate.epsilon
    return round(candidate.accuracy - baseline.accuracy, 2)


baseline = Result("resnet152", 2000, 16 / 256, 39.2)
denoised = Result("resnet152-denoise", 2000, 16 / 256, 42.6)
print(matched_delta(baseline, denoised))
```

This dependency-free check rejects mismatched threat settings before computing an effect size. Production use still needs seeds, intervals, convergence evidence, and model/config hashes.

#### 2. Control-Matrix Gate

```python
REQUIRED = {"baseline", "capacity", "null", "local", "nonlocal"}


def validate_controls(rows: list[dict]) -> None:
    labels = {row["control"] for row in rows}
    missing = REQUIRED - labels
    if missing:
        raise ValueError(f"missing controls: {sorted(missing)}")
    threats = {(row["epsilon"], row["steps"], row["targeted"]) for row in rows}
    if len(threats) != 1:
        raise ValueError("controls use different threat manifests")


rows = [
    {"control": name, "epsilon": 16 / 256, "steps": 100, "targeted": True}
    for name in sorted(REQUIRED)
]
validate_controls(rows)
```

This MVP encodes the minimum ablation family and ensures all rows share one threat definition before a report is published.

#### 3. Synthetic Feature-Suppression Audit

```python
from math import sqrt


def l2(values: list[float]) -> float:
    return sqrt(sum(value * value for value in values))


def suppression_ratio(clean: list[float], attacked: list[float], repaired: list[float]) -> float:
    before = l2([a - c for a, c in zip(attacked, clean)])
    after = l2([r - c for r, c in zip(repaired, clean)])
    if before == 0:
        raise ValueError("no perturbation to measure")
    return round(1.0 - after / before, 3)


print(suppression_ratio([1.0, 0.0], [1.4, 0.3], [1.1, 0.1]))
```

The toy calculation illustrates a scale-aware starting metric. A real audit must stratify layers/channels, preserve raw evidence privately, and prove that suppression does not erase task signal.

### Developer Challenges

1. Recreate the legacy release in a pinned container, verify all published checkpoints and attacks, and document every incompatibility without silently changing the threat model.
2. Implement local, non-local, null, and capacity controls behind one interface with identical insertion points, parameter accounting, seeds, and evaluation manifests.
3. Build convergent modern evaluations that cover targeted and untargeted attacks, adaptive multi-attack suites, corruptions, and system metrics without leaking evaluation data into tuning.

### Author Challenges

1. Define a quantitative, architecture-normalized feature-noise measure and test whether it predicts robustness beyond visual examples.
2. Re-evaluate the architecture across modern backbones and attacks with repeated seeds, uncertainty intervals, matched compute, and complete clean-robust-cost frontiers.
3. Release a reproducible CAAD-style public surrogate or replay protocol that preserves attack diversity while removing dependence on a secret dataset and unknown submissions.

## Validation Notes

- Complete-source integrity gate passed before review; metadata-only HTML was never counted as the paper.
- Nine PDF pages were rendered and visually inspected; equations, figures, plots, and Tables 1-3 were legible.
- Manuscript source, arXiv metadata, CVPR record, official repository README/instructions, and focused implementation code were inspected; no experiment was rerun.
- Related synthesis contains exactly three DEP entries with repository-relative paths, public URLs, relevance, and source basis.
- Synthesis Note contains exactly three potential implementations, deeper relationship observations, conceptual similarities, MVP code mock-ups, developer challenges, and author challenges.
- All three Python mock-ups use only the standard library and pass syntax parsing.
- Public-safety review found no private paths, user names, machine names, local timezone labels, or exact execution timestamps.
- No source file was uploaded; public repository scope is generated Markdown only.

## Attribution Block

- Source URL: https://arxiv.org/abs/1812.03411
  - Applies to: title, authors, arXiv dates, abstract, identifier, DOI, and source links.
- Source URL: https://arxiv.org/pdf/1812.03411
  - Applies to: complete paper method, figures, tables, experiments, results, and limitations; inspected locally and withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/1812.03411
  - Applies to: verified full-paper HTML cross-check; inspected locally and withheld.
- Source URL: https://openaccess.thecvf.com/content_CVPR_2019/html/Xie_Feature_Denoising_for_Improving_Adversarial_Robustness_CVPR_2019_paper.html
  - Applies to: CVPR venue, author, year, and page attribution.
- Source URL: https://github.com/facebookresearch/ImageNet-Adversarial-Training
  - Applies to: official code/model availability, archived status, license, dependencies, and documented evaluation/training behavior.
- Source files: Withheld locally; none were uploaded.
