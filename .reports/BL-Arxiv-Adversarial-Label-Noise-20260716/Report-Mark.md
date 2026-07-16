# Report-Mark: Adversarial Label Noise

## Review Status

- Paper: arXiv:2110.03135v4, *Label Noise in Adversarial Training: A Novel Perspective to Study Robust Overfitting*
- Source: verified complete PDF plus official arXiv full-paper HTML
- Review: mechanism, theorems, datasets, architectures, attacks, calibration, and limitations
- Reproduction: none; source files and extracted text withheld

## Source Metadata

| Field | Value |
|---|---|
| Title | Label Noise in Adversarial Training: A Novel Perspective to Study Robust Overfitting |
| Authors | Chengyu Dong; Liyuan Liu; Jingbo Shang |
| ID / DOI | arXiv:2110.03135v4 / 10.48550/arXiv.2110.03135 |
| Dates | Submitted 2021-10-07; revised through 2023-10-13 |
| Publication | NeurIPS 2022 Main Conference Track, Oral |

## Concise Research Notes

The paper treats the clean one-hot label inherited by an adversarial example as potentially inconsistent with that example's unknown true label distribution. It argues this implicit label noise drives robust overfitting and shows a later recovery when fixed-learning-rate adversarial training is extended to 1,000 epochs.

KD-AT-Auto uses a robust self-teacher, temperature scaling for correctly classified adversarial examples, and interpolation with the inherited target for misclassified examples. On CIFAR-10, the best-to-last robust-accuracy gap declines from 5.93 points for standard adversarial training to 0.25; on CIFAR-100 from 5.04 to 0.12; on Tiny-ImageNet from 1.80 to -0.10. Extension tables show similarly small gaps across architectures, TRADES/FGSM, and PGD-1000/Square/RayS evaluation.

The main boundary is identifiability: the true per-example distribution is not observed, so robust-accuracy improvement does not directly prove semantic correction. Global calibration parameters, an extra robust teacher, and adversarial validation data add dependence and cost.

## Evidence and Attribution

| ID | Evidence | Boundary |
|---|---|---|
| R1 | Full-paper mechanism and double-descent figures | observation supports hypothesis but not universal causality |
| R2 | Theorems 5.1-5.2 | existence under stated cases; no direct true-distribution access |
| R3 | Tables 1-5 | author-reported results; no independent reproduction |
| R4 | Limitations section | teacher/calibration/per-example/cost caveats |
| R5 | NeurIPS and focused public availability search | publication verified; no official code identified |
| R6 | Three related DEP manuscripts | conceptual context only |
| R7 | Selection, repair, cache, and dedup records | operational evidence |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md` - bounded perturbations, representation movement, and unresolved semantic equivalence.
2. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` - calibration intervals, on-distribution assumptions, and failure under adversarial shift.
3. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - architecture-aware corruption and deployment evidence needed for robust-vision claims.

## Synthesis Note

### Concept Bridge

The paper supplies a distribution-mismatch mechanism and mitigation. ViT Semantic Robustness reveals that image similarity and bounded norms do not settle whether class semantics remain unchanged; PAC Confidence supplies calibration discipline but warns that adversarial shift can void on-distribution guarantees; AFIDAF demands architecture-, corruption-, and hardware-aware evidence. The combined research program measures target correction, semantics, calibration transfer, and cost independently.

### Potential Implementations

1. **Robust-target audit bench** - compare inherited, teacher, and rectified distributions across held-out attacks and seeds.
2. **Semantic ambiguity queue** - route high-disagreement adversarial pairs to multi-annotator review with abstention.
3. **Calibration transfer matrix** - learn parameters on one threat model and score NLL, ECE, and robustness on unseen attacks and shifts.

### Deeper Relationship Observations

1. The label-noise account requires a semantic distribution, while ViT perturbation evidence shows that pixel and feature distances cannot identify it alone.
2. KD-AT-Auto uses calibration operationally, whereas PAC Confidence shows why calibration validity is conditional on sampling and distribution assumptions.
3. AFIDAF's missing corruption/hardware evidence parallels this paper's missing semantic/cost evidence: both expose gaps between benchmark improvement and deployable robustness.

### Conceptual Similarities

1. All four artifacts distinguish an observed model score from the latent property it is intended to represent.
2. All require held-out evaluation under distribution or threat-model change.
3. All benefit from uncertainty, provenance, and failure-case reporting rather than a single aggregate metric.

### MVP Implementations with Code Mock-ups

1. **Target divergence logger**

```python
def total_variation(p: list[float], q: list[float]) -> float:
    return 0.5 * sum(abs(a - b) for a, b in zip(p, q))
```

2. **Gap evaluator**

```python
def robust_gap(best: float, last: float) -> float:
    return round(best - last, 4)
```

3. **Calibration transfer gate**

```python
def transfers(source_nll: float, target_nll: float, tolerance: float) -> bool:
    return target_nll - source_nll <= tolerance
```

### Developer Challenges

1. Reproducing attack generation, teacher checkpoints, validation splits, and target rectification without leakage.
2. Logging per-example distributions and provenance at scale while preserving deterministic evaluation.
3. Implementing adaptive, attack-aware testing that cannot exploit cached or stale adversarial examples.

### Author Challenges

1. Release code, checkpoints, seeds, validation splits, and complete calibration/training configurations.
2. Directly test semantic ambiguity and per-example target quality with annotated subsets and multiple teachers.
3. Report repeated-seed uncertainty, adaptive/cross-attack transfer, and full training-compute/energy costs.

## Validation Notes

- Uniform first draw: index 27,298/75,776; no exclusions, reselections, or duplicate markers.
- PDF 1,348,139 bytes with valid header/EOF; official HTML 2,396,107 bytes with 236,587 body characters, two document markers, 78 headings, and seven structure terms; final source state complete.
- Cache miss became cached in about 1.6 seconds; 89,772/236,019 PDF/HTML text bytes; no source package. One PDF image decode warning did not prevent text extraction.
- No model/code execution. Focused search found bibliographic references but no official implementation.
- Schema, exact-count, public-safety, and seven-file no-source allowlist are validated before submission.

## Attribution Block

- Paper: https://arxiv.org/abs/2110.03135v4
- HTML/PDF: https://arxiv.org/html/2110.03135 ; https://arxiv.org/pdf/2110.03135
- DOI: https://doi.org/10.48550/arXiv.2110.03135
- Proceedings: https://proceedings.neurips.cc/paper_files/paper/2022/hash/6fe6a2ba2594521d15af3b1f2162d79c-Abstract-Conference.html
- Nature: independent review; no result reproduced; no source, cache, or extracted-text file uploaded.
