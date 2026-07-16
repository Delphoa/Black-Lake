# Report-Mark: CorrKD Missing Modality

## Source Metadata

- **Title:** *Correlation-Decoupled Knowledge Distillation for Multimodal Sentiment Analysis with Incomplete Modalities*
- **Authors:** Mingcheng Li; Dingkang Yang; Xiao Zhao; Shuaibing Wang; Yan Wang; Kun Yang; Mingyang Sun; Dongliang Kou; Ziyun Qian; Lihua Zhang
- **arXiv:** [2404.16456v2](https://arxiv.org/abs/2404.16456v2); [DOI](https://doi.org/10.48550/arXiv.2404.16456)
- **Dates:** submitted 2024-04-25; revised 2024-06-10
- **Venue:** [CVPR 2024, pages 12458-12468](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Correlation-Decoupled_Knowledge_Distillation_for_Multimodal_Sentiment_Analysis_with_Incomplete_Modalities_CVPR_2024_paper.html)
- **Evidence:** verified PDF, official full-paper HTML, metadata HTML, TeX/source, CVPR record, figures, tables, and public code-availability searches
- **Code:** no official CorrKD implementation identified
- **Source policy:** all source artifacts and caches withheld locally

## Concise Research Notes

CorrKD trains a complete-modality teacher, freezes it, generates zero-masked incomplete inputs for a structurally matching student, and combines task cross-entropy with three transfers: sample-level contrastive alignment, category-prototype similarity alignment, and target/non-target response mutual-information consistency. Inference uses only the student.

Experiments cover MOSI, MOSEI, and IEMOCAP, random frame dropping from 0.1 to 1.0, six whole-modality availability patterns, seven baselines, MOSI ablations, and five random seeds. On MOSI, CorrKD's missing-condition average weighted F1 is 74.69 versus GCNet's 73.84; its audio+visual condition is 73.74 versus 70.02. Complete-modality CorrKD is 83.94, below Self-MM's 84.64. The result supports conditional robustness, not universal superiority.

## Evidence and Attribution

| Evidence | Supports | Confidence | Boundary |
|---|---|---|---|
| Full Sections 3-4 and equations | teacher/student path and three losses | High for reporting | implementation absent |
| Tables 1-3 and Figures 3-5 | missingness comparisons and ablations | Medium-high | no seed-level values or intervals |
| CVPR open-access record | venue, pages, author list | High | metadata only |
| Code searches | no official implementation located | Medium-high | absence is not proof of nonexistence |

Claims are paraphrased from inspected evidence; reviewer interpretations and limitations are labeled.

## Related DEP Entries

1. [AV Emotion Fusion](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md) - direct overlap in IEMOCAP, audiovisual emotion fusion, preprocessing, corruption, and consent boundaries.
2. [VLM Probing](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md) - fusion, modality dominance, representation leakage, and causal-ablation diagnostics.
3. [KDFlow LLM Distill](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-KDFlow%20LLM%20Distill/kdflow_llm_distill_manuscript.md) - teacher/student versioning, parity checks, reproducible distillation, and systems accounting.

## Synthesis Note

### Concept Bridge

CorrKD treats correlations at three resolutions as transferable teacher knowledge. AV Emotion Fusion supplies the task-specific warning that one modality can add little or fail under preprocessing. VLM Probing supplies measurements for whether fusion and modality balance actually changed. KDFlow supplies the systems lesson that distillation claims depend on pinned teacher/student paths and parity evidence. Together they suggest a missingness audit that separates representation transfer, decision behavior, system cost, and consent.

### Potential Implementations

1. Build a missingness-matrix benchmark covering blocks, bursts, asynchrony, whole streams, and not-missing-at-random conditions.
2. Build a teacher/student representation auditor with modality probes, loss ablations, calibration, and seed intervals.
3. Build a consent-bounded offline sentiment research workbench that exports aggregate evidence only and forbids consequential inference.

### Deeper Relationship Observations

1. Batch negatives and category prototypes make CorrKD's supervision depend on batch composition, so class balance changes the knowledge target.
2. Language-dominant results can reflect genuine information, dataset construction, transcript leakage, or weaker audio/visual features; aggregate F1 cannot distinguish them.
3. Zero replacement conflates absence with an artificial constant pattern, potentially letting the student recognize the corruption mechanism rather than recover semantics.

### Conceptual Similarities

1. CorrKD and AV Emotion Fusion both test whether heterogeneous pathways add emotion evidence under incomplete or noisy input.
2. CorrKD and VLM Probing both operationalize cross-modal structure through measurable representation relationships.
3. CorrKD and KDFlow both require teacher/student equivalence checks before attributing results to the distillation method.

### MVP Implementations with Code Mock-ups

1. **Missingness manifest**

```python
def make_manifest(sample_id, available, spans, mechanism, seed):
    return {
        "sample_id": sample_id,
        "available_modalities": sorted(available),
        "missing_spans": spans,
        "mechanism": mechanism,
        "seed": seed,
    }
```

2. **Condition-level comparison**

```python
def condition_delta(rows, candidate, baseline):
    output = {}
    for condition in sorted({row["condition"] for row in rows}):
        c = [row["f1"] for row in rows if row["model"] == candidate and row["condition"] == condition]
        b = [row["f1"] for row in rows if row["model"] == baseline and row["condition"] == condition]
        output[condition] = sum(c) / len(c) - sum(b) / len(b)
    return output
```

3. **Consent-bounded export**

```python
def export_research_record(metrics, contains_raw_media, consequential_use):
    if contains_raw_media or consequential_use:
        raise ValueError("public export blocked")
    return {"aggregate_metrics": metrics, "authorized_action": False}
```

### Developer Challenges

1. Prevent masked descendants, repeated clips, or speaker/session relatives from crossing train/evaluation boundaries.
2. Reproduce batch-sensitive prototype and contrastive losses when a category is absent or rare in a mini-batch.
3. Version raw features, alignments, masks, teacher checkpoints, seeds, and metric denominators together.

### Author Challenges

1. Release code, configs, checkpoint hashes, masks, split manifests, and per-seed results.
2. Evaluate natural, structured, correlated, and not-missing-at-random failures across datasets and devices.
3. Report calibration, subgroup, consent, privacy, and consequential-use analysis alongside F1.

## Validation Notes

- First uniform draw from 75,776 units; zero exclusions and reselections.
- ID, title, DOI, slug, artifact, memory, recent, and companion-repository dedup checks passed.
- Partial source repaired with official arXiv artifacts; PDF/HTML/source gate passed; zero partials.
- Cache miss backfilled in 1.013 seconds with all extraction channels successful.
- Exactly three related entries inspected; schema/count/code/safety/source-upload validation follows.
- No `.source` directory or original source artifact is included.

## Attribution Block

**Primary work:** Mingcheng Li et al., *Correlation-Decoupled Knowledge Distillation for Multimodal Sentiment Analysis with Incomplete Modalities*, arXiv:2404.16456v2, CVPR 2024, 12458-12468. **Review and synthesis:** Codex for Delphoa Black Lake, 2026-07-16. Original PDF, HTML, metadata, TeX/source, figures, cache, and extracted text were withheld locally; no source files were uploaded.
