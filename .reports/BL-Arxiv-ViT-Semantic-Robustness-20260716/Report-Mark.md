# Report-Mark: ViT Semantic Robustness

## Review Status

- Paper: arXiv:2507.01788v2
- Source: verified complete PDF and approved ar5iv full-paper rendering
- Review depth: method, algorithm, Tables I-III, mitigation, discussion, baseline repository, and related DEP synthesis
- Reproduction: not performed
- Source distribution: withheld locally; no source upload

## Source Metadata

| Field | Value |
|---|---|
| Title | Are Vision Transformer Representations Semantically Meaningful? A Case Study in Medical Imaging |
| Authors | Montasir Shams; Chashi Mahiul Islam; Shaeke Salman; Phat Tran; Xiuwen Liu |
| Identifier | arXiv:2507.01788v2 |
| DOI | 10.48550/arXiv.2507.01788 |
| Dates | submitted 2025-07-02; revised 2025-07-10 |
| Subjects | Computer Vision and Pattern Recognition; Artificial Intelligence |
| License | CC BY 4.0 on arXiv record |
| Paper-linked code | MIL-VT baseline repository; no official PRM code found |

## Concise Research Notes

Projected Representation Matching minimizes distance between a perturbed source embedding and a different-class target embedding while projecting pixel changes into an epsilon-bounded neighborhood. This probes representation stability and distinctiveness rather than only output robustness.

Table I reports large accuracy collapses. APTOS MIL-VT falls from 81.3% clean accuracy to about 5-6% under PRM, with 74-76% match success. RFMiD falls from 87.2% to 26-27%, with 73-74% match success. MedViT-L on bloodMNIST reports 17.8% accuracy and 85.5% match success; dermaMNIST reports 51.5% and 73.5%.

Table II uses 1,000 randomly selected examples per dataset and reports high original-to-optimized similarity, such as APTOS 42.55 dB PSNR/0.972 SSIM and RFMiD 43.47 dB/0.982. Table III shows optimized embeddings closer to targets than originals. These support local white-box vulnerability, not universal absence of clinical semantics.

The mitigation proposal—add Gaussian noise and flag label inconsistency—lacks a full detection table, calibration, adaptive testing, and clinical review. It should be treated as a hypothesis.

## Evidence and Attribution

| ID | Basis | Supports | Boundary |
|---|---|---|---|
| R1 | Full v2 paper | PRM, experiments, results, mitigation | Author-reported; no rerun |
| R2 | Tables I-III | Accuracy, match success, PSNR/SSIM, cosine similarity | No uncertainty or clinician review |
| R3 | MIL-VT README | Baseline dependencies, weights, datasets | Not PRM code; no visible license |
| R4 | Three DEP manuscripts | Clinical grounding, manipulation evaluation, ViT audit | Conceptual context only |
| R5 | Process records | Selection, dedup, repair, cache | Operational evidence |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md` - explicit anatomical/disease structure and clinical grounding boundaries.
2. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` - subtle image manipulation, semantic/forensic evidence, calibration, and missing-output accounting.
3. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - ViT architecture, representation design, and corruption/device robustness audits.

## Synthesis Note

### Concept Bridge

PRM supplies a targeted geometry stress test; Medical Diff VQA supplies explicit clinical relations that a “semantic” representation might preserve; Document Fraud LLM supplies manipulation-detection and calibration discipline; AFIDAF supplies architecture-level alternatives and robustness accounting. The combined research question is not simply whether embeddings move, but whether clinically relevant relations remain stable under benign and adversarial change, whether shifts are detectable, and whether architecture choices improve that outcome.

### Potential Implementations

1. **Representation evidence card** - versioned clean utility, geometry, perceptual, attack, site, subgroup, and uncertainty fields.
2. **Blinded clinical equivalence study** - credentialed reviewers compare source/optimized pairs and label diagnostic equivalence and harm.
3. **Selective stability monitor** - bounded benign perturbations produce calibrated abstention and review routing rather than manipulation accusations.

### Deeper Relationship Observations

1. Medical Diff VQA operationalizes semantics through anatomy/disease relations, revealing that pixel closeness and class labels alone are incomplete semantic tests.
2. Document Fraud LLM shows that visually subtle manipulation detection needs fixed denominators, calibration, and causal evidence; PRM's proposed detector needs the same discipline.
3. AFIDAF shows that changing token-mixing architecture can alter representation mechanisms, but robustness must be measured directly rather than inferred from accuracy, parameters, or FLOPs.

### Conceptual Similarities

1. Each artifact separates task accuracy from a deeper evidence property: grounding, manipulation sensitivity, representation geometry, or deployment robustness.
2. Each needs controlled perturbations and explicit failure cases to distinguish true mechanism from benchmark shortcuts.
3. Each rejects autonomous high-stakes decisions without uncertainty, provenance, and human review.

### MVP Implementations with Code Mock-ups

1. **Metric contract**

```python
REQUIRED = {"clean_accuracy", "attack_accuracy", "match_rate", "epsilon", "seed"}

def validate_metrics(record: dict) -> None:
    missing = REQUIRED.difference(record)
    if missing:
        raise ValueError(f"missing metrics: {sorted(missing)}")
```

2. **Pair provenance**

```python
def pair_record(source_id: str, target_id: str, different_label: bool) -> dict:
    if not source_id or not target_id or not different_label:
        raise ValueError("cross-label pair provenance required")
    return {"source_id": source_id, "target_id": target_id, "different_label": True}
```

3. **Abstention router**

```python
def stability_route(clean_label: str, perturbed_labels: list[str]) -> str:
    if not perturbed_labels:
        raise ValueError("held-out perturbation results required")
    agreement = sum(x == clean_label for x in perturbed_labels) / len(perturbed_labels)
    return "review" if agreement < 0.9 else "continue"
```

### Developer Challenges

1. Reproducing pixel and embedding preprocessing exactly across old checkpoints, model families, and medical-image formats.
2. Isolating authorized patient data while preserving pair, site, device, and subgroup provenance for audit.
3. Calibrating instability thresholds against benign acquisition variation and adaptive attacks without overwhelming reviewers.

### Author Challenges

1. Release PRM code, fixed pair manifests, seeds, checkpoints, optimized examples, and exact table-generation configurations.
2. Test clinician-defined semantic equivalence, natural acquisition variation, external sites, subgroups, and matched non-ViT baselines.
3. Quantify the proposed mitigation with false-positive/negative rates, calibration, adaptive attacks, and risk-coverage analysis.

## Validation Notes

- First uniform draw: index 30,086 of 75,776 units; zero exclusions/reselections.
- Dedup found no substantive match.
- PDF header/EOF passed; official HTML returned 404; approved ar5iv full text passed every structural gate; zero partials.
- Cache miss became cached in `missing-only` mode using `pypdf` and `html-regex`.
- Required manuscript/report sections, exact counts, Python syntax, JSON/index counts, public safety, and staged allowlists are checked before submission.
- No source files, images, caches, or `.source/` directory are included.

## Attribution Block

- https://arxiv.org/abs/2507.01788v2 - canonical metadata and version.
- https://arxiv.org/pdf/2507.01788 - complete paper inspected locally; file withheld.
- https://ar5iv.labs.arxiv.org/html/2507.01788 - approved full-paper fallback; file withheld.
- https://doi.org/10.48550/arXiv.2507.01788 - persistent identifier.
- https://github.com/greentreeys/MIL-VT - paper-linked baseline implementation; not executed.
- https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA/medical_diff_vqa_manuscript.md - related clinical grounding record.
- https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Document%20Fraud%20LLM/document_fraud_llm_manuscript.md - related manipulation evaluation record.
- https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md - related ViT architecture/robustness record.
