# BL-Arxiv-DRMOT-20260804 Report-Mark

## Source Metadata

- Title: *DRMOT: A Dataset and Framework for RGBD Referring Multi-Object Tracking*
- Authors: Sijia Chen; Lijuan Ma; Yanqiu Yu; En Yu; Liman Liu; Wenbing Tao.
- Identifier: arXiv:2602.04692v2; arXiv-issued DOI: 10.48550/arXiv.2602.04692.
- Public dates: submitted 2026-02-04; revised 2026-02-06.
- Primary sources: [arXiv metadata](https://arxiv.org/abs/2602.04692), [full-paper HTML](https://arxiv.org/html/2602.04692), and [PDF](https://arxiv.org/pdf/2602.04692).
- Official implementation locator: [chen-si-jia/DRMOT](https://github.com/chen-si-jia/DRMOT). The inspected public root contains a README, asset, and MIT license; its README says the dataset, framework, code, and weights are planned for release after acceptance.
- Source integrity: the local PDF and full-paper HTML passed the complete-paper gate after one bounded repair; source files and archive records remain local and were not redistributed.

## Concise Research Notes

DRMOT defines RGBD Referring Multi-Object Tracking as a task in which RGB, depth, and language jointly identify and track one or more objects described by spatial and semantic constraints. Its DRSet dataset contains 187 scenes, 240 language descriptions, and 56 descriptions with explicit depth-related language; the paper reports 141 training videos and 99 evaluation videos. The authors use four annotation steps and a two-person review.

DRTrack has two stages. A Qwen2.5-VL-3B-based grounding module consumes language, RGB, and depth rendered as a metric-preserving three-channel input. Geometric-aware GRPO uses format and IoU rewards to produce structured bounding boxes. A depth-enhanced OC-SORT stage adds mean box depth to IoU and the VDC motion prior: the paper defines a depth similarity as exponential decay of absolute depth difference and fuses it with IoU using `alpha=0.9`, with `lambda=0.3` for the motion term.

On the paper's test set, the reported HOTA is 33.24 for DRTrack versus 15.13 for zero-shot Qwen2.5-VL-3B with RGB and language only. The ablation reports 32.68 with RGB, depth, and no GRPO, and 33.24 with GRPO; the source therefore supports a strong depth contribution in this setting, while the incremental GRPO gain is smaller. These are author-reported results, not independent reproduction.

## Evidence and Attribution

| ID | Source | Evidence used | Assessment |
|---|---|---|---|
| E1 | [arXiv metadata](https://arxiv.org/abs/2602.04692) | Title, authors, subject, revision history, DOI, and official links. | High-confidence source identity. |
| E2 | [full-paper HTML](https://arxiv.org/html/2602.04692) | Introduction, DRSet construction, annotation, split, statistics, and framework sections. | High-confidence transcription; no reproduction. |
| E3 | [full-paper HTML](https://arxiv.org/html/2602.04692) | Equations for format/IoU reward, RGBD similarity, association cost, and implementation settings. | High-confidence mechanism reconstruction. |
| E4 | [full-paper HTML](https://arxiv.org/html/2602.04692) | Tables 3–5, HOTA/DetA/AssA results, depth ablation, GRPO ablation, and alpha sensitivity. | High-confidence transcription; medium generalization confidence. |
| E5 | [official repository](https://github.com/chen-si-jia/DRMOT) | Public release state, README promise, asset, and license. | Medium-confidence implementation availability; code was not executed. |
| E6 | [FEMOT Tracking DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-FEMOT%20Tracking/femot_tracking_manuscript.md) | Multimodal tracking, association metrics, sensor fusion, and governance boundaries. | Related synthesis only; not validation of DRMOT. |
| E7 | [Language-to-Space DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md) | Language-to-3D grounding and auditable spatial reasoning. | Related synthesis only; no joint experiment. |
| E8 | [Pixel-Point Transfer DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md) | Calibrated RGB-D correspondence, geometric integrity, and cross-modal transfer. | Related synthesis only; no joint experiment. |

## Related DEP Entries

1. [DEP-E-20260720-FEMOT Tracking](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-FEMOT%20Tracking) — direct overlap on multi-object tracking, multimodal sensor fusion, identity association, HOTA-style evaluation, and governance-aware deployment limits. Basis: E6 manuscript sections on benchmark design, fusion, association, and safe implementation.
2. [DEP-E-20260727-Language-to-Space](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260727-Language-to-Space) — direct overlap on translating language into 3D spatial grounding and retaining abstention/provenance boundaries. Basis: E7 manuscript source metadata, grounding analysis, and implementation constraints.
3. [DEP-E-20260718-Pixel Point Transfer](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Pixel%20Point%20Transfer) — direct overlap on RGB-D geometry, calibrated correspondence, modality adapters, and tests for projection/depth errors. Basis: E8 manuscript mechanism, correspondence gate, and replication checklist.

## Synthesis Note

### Concept Bridge

DRMOT treats depth as a semantic disambiguator and a temporal association constraint. FEMOT shows the same systems pattern with a different sensor: modality fusion is valuable only when synchronization, association metrics, and failure slices travel with the output. Language-to-Space supplies the language-to-geometry bridge, while Pixel-Point Transfer supplies the correspondence-integrity lens. Together, the three related deposits suggest a reusable design rule: preserve the spatial unit, audit the modality bridge, and propagate uncertainty and provenance into every tracking decision.

### Potential Implementations

1. **Offline RGBD referring-tracking evaluator** — ingest authorized predictions, annotations, calibration summaries, depth-quality metrics, and language slices; emit HOTA/DetA/AssA, identity-switch, grounding, and depth-noise breakdowns. Guardrail: report-only, local processing, no control output.
2. **Spatial-language coverage auditor** — classify descriptions by depth dependence, object count, category, occlusion, and ambiguity; compare coverage to the test split and flag unsupported generalization. Guardrail: use metadata and aggregate annotations, not raw scene redistribution.
3. **Correspondence-and-association gate** — stress-test projection, depth masks, timestamp offsets, alpha/lambda settings, and missing-modality behavior before accepting a tracking run. Guardrail: synthetic corruption first, explicit stop thresholds, and human review for authorized data.

### Deeper Relationship Observations

1. Depth is not merely an additional image channel: in DRMOT it changes the meaning of language expressions and supplies a second identity cue, so quality checks must evaluate semantics and geometry together.
2. The largest reported gain comes from adding depth before GRPO, while the association study keeps IoU dominant at `alpha=0.9`; this suggests that geometric information and 2D localization are complementary rather than interchangeable.
3. FEMOT, Language-to-Space, and Pixel-Point Transfer converge on provenance-preserving evaluation: calibration, correspondence, language coverage, and sensor limitations are part of the evidence object, not hidden preprocessing details.

### Conceptual Similarities

1. All four artifacts connect multimodal inputs to a spatially grounded downstream decision rather than treating modalities as independent feature streams.
2. Each artifact uses an explicit bridge: RGB-D-L grounding and depth-aware association in DRMOT; sensor fusion and identity association in FEMOT; language-to-space mapping in Language-to-Space; pixel-point correspondence in Pixel-Point Transfer.
3. Each artifact benefits from bounded evaluation slices and explicit uncertainty because aggregate task metrics can hide calibration, association, or semantic failures.

### MVP Implementations

1. **Depth-aware association card** — compute a bounded RGBD similarity from IoU and depth agreement, then emit an auditable score rather than a control command.

```python
import math


def rgbd_similarity(iou, depth_delta, alpha=0.9, sigma=0.2):
    if not 0.0 <= iou <= 1.0 or sigma <= 0.0:
        raise ValueError("invalid bounded association inputs")
    depth_score = math.exp(-abs(depth_delta) / sigma)
    return alpha * iou + (1.0 - alpha) * depth_score
```

2. **Grounding coverage gate** — make depth-language coverage visible before a benchmark claim is accepted.

```python
def grounding_coverage(records):
    if not records:
        return {"count": 0, "depth_fraction": 0.0, "ok": False}
    depth_count = sum(bool(row.get("depth_related")) for row in records)
    fraction = depth_count / len(records)
    return {"count": len(records), "depth_fraction": fraction, "ok": fraction > 0.0}
```

3. **Public-safe run ledger** — require split, calibration, modality, and provenance fields before metrics enter a review artifact.

```python
def validate_run(run):
    required = {"split_id", "calibration_id", "modalities", "metrics", "source_url"}
    missing = sorted(required.difference(run))
    if missing:
        return {"ok": False, "reason": "missing fields", "fields": missing}
    if "depth" not in run["modalities"] or not run["metrics"]:
        return {"ok": False, "reason": "incomplete RGBD evaluation"}
    return {"ok": True, "reason": "reviewable run"}
```

### Developer Challenges

1. Build a reproducible, privacy-safe data contract for aligned RGB, depth, language, bounding boxes, identities, and calibration without distributing source scenes.
2. Separate grounding errors, depth errors, detector errors, and association errors so HOTA changes have an interpretable cause.
3. Engineer graceful behavior for missing, noisy, misregistered, or temporally stale depth instead of assuming complete RGBD input.

### Author Challenges

1. Release the promised dataset, executable framework, model weights, exact prompts, and evaluation commands with versioned splits and licenses.
2. Test cross-sensor, cross-scene, depth-corruption, missing-depth, long-tail, and multi-seed conditions, with annotation agreement and uncertainty reporting.
3. Clarify the contribution boundary between depth input, GRPO fine-tuning, Qwen model choice, OC-SORT augmentation, and the dataset's language coverage.

## Validation Notes

- Manuscript schema: required headings, YAML title/H1 identity, title length, evidence ledger, exact-three exercises, source references, and appendix included.
- Report-Mark contract: exactly three potential implementations, deeper relationship observations, conceptual similarities, MVP implementations, developer challenges, and author challenges; each MVP includes one bounded Python mock-up.
- Source gate: PDF and full-paper HTML passed the required size, marker, structure, and integrity checks after one repair; abstract HTML was treated as metadata only.
- Public-safety gate: no local absolute path, username, home directory, drive path, machine name, local timezone label, or exact local execution timestamp appears in the artifact set.
- Source upload gate: only Markdown/README artifacts are intended for staging; no PDF, HTML, source archive, cache, extracted source text, dataset, model, or `.source/` directory is included.

## Attribution Block

- Source URL: https://arxiv.org/abs/2602.04692
  - Applies to: this Report-Mark; paper identity and public source locators.
- Source URL: https://arxiv.org/html/2602.04692
  - Applies to: research notes, evidence table, and synthesis; full-paper technical evidence.
- Source URL: https://arxiv.org/pdf/2602.04692
  - Applies to: primary-paper integrity and cross-checking; PDF withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2602.04692
  - Applies to: stable paper identifier.
- Source URL: https://github.com/chen-si-jia/DRMOT
  - Applies to: official repository availability and license context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-FEMOT%20Tracking/femot_tracking_manuscript.md
  - Applies to: E6 and multimodal tracking synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md
  - Applies to: E7 and language-to-space synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md
  - Applies to: E8 and RGB-D correspondence synthesis.
- Source files: withheld locally.
  - Applies to: all Report-Mark sections.
  - Notes: No source file, cache, extracted text, or local archive record was uploaded, committed, staged, or attached.
