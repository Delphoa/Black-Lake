# Report-Mark: T23DAQA Quality

## Source Metadata

| Field | Value |
|---|---|
| Title | Multi-Dimensional Quality Assessment for Text-to-3D Assets: Dataset and Model |
| Authors | Kang Fu; Huiyu Duan; Zicheng Zhang; Xiaohong Liu; Xiongkuo Min; Jia Wang; Guangtao Zhai |
| Identifier | arXiv:2502.16915v1 |
| DOI | https://doi.org/10.48550/arXiv.2502.16915 |
| Submitted | 2025-02-24 |
| Primary record | https://arxiv.org/abs/2502.16915 |
| Full-paper HTML | https://arxiv.org/html/2502.16915 |
| PDF | https://arxiv.org/pdf/2502.16915 |
| Official repository | https://github.com/ZedFu/T23DAQA |
| Source integrity | Initial partial unit repaired before review; PDF and full-paper HTML passed the required verification gate. |
| Source boundary | Source documents, extraction text, caches, and repair records were retained locally and withheld from public artifacts. |

## Concise Research Notes

The paper addresses a measurement gap in text-to-3D generation. Existing image, video, mesh, and point-cloud quality measures do not directly separate visual quality, real-world plausibility, and prompt-to-asset correspondence, while direct human review is slow. The authors introduce the AIGC-T23DAQA database and a projection-based T23DAQA model intended to predict those three dimensions.

The database contains 969 validated assets generated from 170 prompts by six text-to-3D systems. The paper reports 17 human raters, three 0–5 sliders, 120-frame 512×512 projection videos, and normalized mean opinion scores. The model extracts shape features from projection videos, texture features from front/back projections, and text-image alignment features from a prompt and projected frame. A three-layer MLP regresses quality, authenticity, and correspondence scores.

The reported learning-based table gives the proposed model SRCC/KRCC/PLCC values of `0.6728/0.4909/0.6840` for authenticity, `0.7000/0.5157/0.7297` for correspondence, and `0.7853/0.5987/0.7828` for quality. The ablation table reports the full model as the strongest configuration across the listed dimensions. These are author-reported results from the paper's split, training, and evaluation protocol; no independent reproduction was performed.

## Evidence and Attribution

| Evidence | Inspected basis | What it supports | Confidence and boundary |
|---|---|---|---|
| E1 | Official arXiv metadata and DOI record | Identity, authors, date, version, subject, DOI, and public locators | High for source metadata; metadata alone is not result evidence. |
| E2 | Verified full-paper HTML and PDF | Problem framing, database construction, model architecture, protocol, results, ablation, conclusion | High for transcription; source claims are not independent validation. |
| E3 | Local missing-only extraction cache | Reusable PDF/HTML text and extractor status | High for cache provenance; `pypdf` fallback and absent source package limit extraction fidelity. |
| E4 | Official `ZedFu/T23DAQA` README and MIT license | Repository identity, database description, code/data context, license visibility | Medium-high; repository presence does not prove runnable reproduction. |
| E5 | Three related Black Lake manuscripts | Cross-DEP conceptual bridge for multimodal benchmarks, 3D generation, and 3D QA | Medium; related entries are synthesis context, not evidence for the selected paper's metrics. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260731-SFOOD A Multimodal/sfood_a_multimodal_manuscript.md` ([public file](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260731-SFOOD%20A%20Multimodal/sfood_a_multimodal_manuscript.md)) - selected for its multi-attribute multimodal benchmark framing and emphasis on evaluation boundaries. Basis inspected: the related manuscript and README, grounded in arXiv:2507.04412.
2. `.lake-data/DEP-E/DEP-E-20260724-AG3D Learning to Generate/ag3d_learning_to_generate_manuscript.md` ([public file](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260724-AG3D%20Learning%20to%20Generate/ag3d_learning_to_generate_manuscript.md)) - selected for its direct 3D-avatar generation and appearance-quality overlap. Basis inspected: the related manuscript and README, grounded in arXiv:2305.02312.
3. `.lake-data/DEP-A/DEP-A-20260725-SeGPruner 3D QA/2603.29437-whitepaper-review.md` ([public file](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260725-SeGPruner%203D%20QA/2603.29437-whitepaper-review.md)) - selected for its 3D question-answering quality and representation-selection boundary. Basis inspected: the related review and README, grounded in arXiv:2603.29437.

## Synthesis Note

### Concept Bridge

T23DAQA turns a qualitative 3D-generation problem into a structured measurement interface with three separable axes. The bridge to Black Lake is an evidence-gated evaluator: retain the input prompt, projection policy, generator identity, score vector, uncertainty, and human-review decision as one auditable record. SFOOD contributes multi-attribute benchmark discipline; AG3D contributes the upstream generation surface; SeGPruner contributes the warning that representation selection can preserve some task signal while losing another. The useful product boundary is therefore not a single “quality” scalar but a typed, shift-aware decision surface.

### Potential Implementations

1. **Asset triage queue** - A local tool ranks multiple generated assets per prompt using separate quality, authenticity, and correspondence scores. It must show the three axes separately, record projection settings, and route low-confidence or out-of-distribution prompts to a human reviewer.
2. **Benchmark audit harness** - A reproducible harness replays a fixed prompt/generator matrix, compares the proposed evaluator with simple alignment and visual baselines, and reports per-prompt and per-generator results rather than only aggregate correlation.
3. **Training-time quality monitor** - A research-only monitor joins generated assets with score vectors and downstream user selections, using the evaluator as a diagnostic signal rather than an unconditional loss. It should enforce holdout prompts, leakage checks, and a rollback threshold before any score is used for optimization.

### Deeper Relationship Observations

1. The selected work and SFOOD both suggest that “quality” is an insufficient unit when an artifact has several human-relevant attributes; preserving a vector makes disagreements visible.
2. The selected work and AG3D form an upstream/downstream pair: generation choices create the geometric and appearance failures that an evaluator must measure, so benchmark coverage should span generator families rather than only raters.
3. The selected work and SeGPruner expose a common systems tension: a compact or convenient representation can improve one task signal while hiding failures in geometry, view consistency, or task relevance; audit records must retain the transformation boundary.

### Conceptual Similarities

1. All three related bridges treat representations as task-conditioned rather than universally sufficient.
2. All three require evaluation beyond a headline average: attributes, prompts, views, or downstream questions change the interpretation.
3. All three benefit from explicit provenance, bounded fallback, and human review when a proxy score is outside its supported distribution.

### MVP Implementations with Code Mock-ups

1. **Three-axis score card**

```python
def score_card(quality, authenticity, correspondence):
    values = {
        "quality": float(quality),
        "authenticity": float(authenticity),
        "correspondence": float(correspondence),
    }
    values["review_required"] = min(values.values()) < 0.45
    return values

print(score_card(0.78, 0.52, 0.81))
```

2. **Prompt-family holdout report**

```python
from statistics import mean

def holdout_summary(rows):
    groups = {}
    for row in rows:
        groups.setdefault(row["prompt_family"], []).append(row["quality"])
    return {family: round(mean(scores), 3) for family, scores in groups.items()}

print(holdout_summary([
    {"prompt_family": "vehicle", "quality": 0.70},
    {"prompt_family": "vehicle", "quality": 0.74},
    {"prompt_family": "plant", "quality": 0.58},
]))
```

3. **Human-review gate for shifted inputs**

```python
def route_prediction(scores, confidence, known_prompt_family):
    if not known_prompt_family or confidence < 0.70:
        return {"decision": "human_review", "scores": scores}
    return {"decision": "eligible_for_triage", "scores": scores}

print(route_prediction({"quality": 0.8}, 0.62, False))
```

### Developer Challenges

1. Build a stable projection and feature-extraction pipeline across NeRF, voxel, mesh, and other 3D representations without introducing view-dependent artifacts that the evaluator mistakes for quality.
2. Preserve separate labels, calibration, and confidence for quality, authenticity, and correspondence instead of collapsing them into a hard-to-audit scalar.
3. Measure end-to-end cost, including rendering, model loading, feature extraction, batching, and fallback, before claiming a production benefit.

### Author Challenges

1. Establish external validity with newer generators, unseen prompt families, independent raters, and cross-lab replication rather than only the reported split and six models.
2. Report uncertainty and failure distributions for each perceptual axis, especially cases where correspondence is high but geometry or authenticity is low.
3. Clarify dataset and repository reproducibility by pinning data snapshots, model checkpoints, environment versions, and a runnable evaluation recipe.

## Validation Notes

- Required source gate passed before review: complete PDF and complete full-paper HTML; abstract HTML was treated as metadata only.
- Cache contract passed: initial miss, `missing-only` extraction, public summary status `cached`, PDF and HTML text present, source text absent because the source package was unavailable.
- Dedup/reselection validation passed: first random draw accepted; zero duplicate exclusions, zero reselections, and no same-paper marker within 24 hours.
- Public-output allowlist: only the generated log, phase log, Report-Mark, DEP README, manuscript, and required dedup JSON are permitted. No PDF, HTML, archive, cache, extracted source text, local path, or `.source/` directory is included.
- No experiment, code, dataset, model, or benchmark was executed; reported metrics remain attributed author claims.
- The manuscript title contract, required headings, exactly three exercise paths, and exact-three synthesis lists were checked before submission.

## Attribution Block

- Primary paper: https://arxiv.org/abs/2502.16915
  - Applies to: identity, authors, date, abstract, and public source locators.
- Full-paper HTML: https://arxiv.org/html/2502.16915
  - Applies to: method, database, protocol, results, ablation, limitations, and conclusion; local source withheld.
- Primary PDF: https://arxiv.org/pdf/2502.16915
  - Applies to: source-first full-paper review and integrity verification; local source withheld.
- DOI: https://doi.org/10.48550/arXiv.2502.16915
  - Applies to: persistent paper identity.
- Official implementation and database context: https://github.com/ZedFu/T23DAQA
  - Applies to: repository README, database description, and MIT license visibility; not independently executed.
- Related DEP source: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260731-SFOOD%20A%20Multimodal/sfood_a_multimodal_manuscript.md
  - Applies to: multimodal benchmark bridge; source basis arXiv:2507.04412.
- Related DEP source: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260724-AG3D%20Learning%20to%20Generate/ag3d_learning_to_generate_manuscript.md
  - Applies to: 3D asset generation bridge; source basis arXiv:2305.02312.
- Related DEP source: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260725-SeGPruner%203D%20QA/2603.29437-whitepaper-review.md
  - Applies to: 3D QA and representation-selection bridge; source basis arXiv:2603.29437.
- Source boundary: all original source files, caches, extracted text, and local archive records were withheld and no source files were uploaded.
