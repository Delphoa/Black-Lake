# Report-Mark: VLM Probing

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Behind the Scene: Revealing the Secrets of Pre-trained Vision-and-Language Models* |
| Authors | Jize Cao, Zhe Gan, Yu Cheng, Licheng Yu, Yen-Chun Chen, Jingjing Liu |
| arXiv | 2005.07310v2 |
| DOI | 10.1007/978-3-030-58539-6_34 |
| Venue | Computer Vision – ECCV 2020, Part VI, pp. 565–580 |
| Initial submission | 2020-05-15 |
| Inspected revision | 2020-07-18 |
| Primary URL | https://arxiv.org/abs/2005.07310 |
| ECCV page | https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/6959_ECCV_2020_paper.php |
| Code locator | https://github.com/JizeCao/VALUE — unavailable during this run |
| Local evidence | PDF and provenance readme inspected; local path withheld and files not redistributed |
| Access date | 2026-07-12 |

## Concise Research Notes

### Problem

The paper asks what early Transformer-based vision-and-language models actually encode and how single-stream and two-stream architectures differ internally. Rather than using downstream benchmark scores alone, the authors introduce VALUE, a set of probes for multimodal fusion, modality importance, visual coreference, visual relations, and linguistic knowledge.

### Method

The study dissects UNITER-base as a single-stream model and LXMERT as a two-stream model. It uses Flickr30k Entities for image–noun-phrase links and Visual Genome for scene-graph relations, supplementing annotated regions with Faster R-CNN regions. It analyzes attention mass, individual heads, linear combinations of attention heads, and layer-wise embeddings. Random-weight and mismatched-caption baselines help distinguish learned behavior from architectural bias.

### Evidence and Results

- Multimodal fusion: UNITER's NMI falls from 0.36 to 0.20 on Flickr30k and from 0.25 to 0.16 on Visual Genome, consistent with increasing fusion; LXMERT's cross-modal layers do not show the same monotonic pattern.
- Modality importance: In UNITER, the `[CLS]` attention analysis assigns more mass to text than image tokens, especially in intermediate layers. This is direct evidence for UNITER only; the paper's broader concluding wording about both architectures is stronger than the Section 3.2 experiment supports.
- Head specialization: Only about 15% of UNITER heads exceed a 0.5 probability of majority image-to-text attention, while the maximum head probability is 0.92.
- Visual coreference: Attention features perform modestly on binary detection but better on relation classification. Layer-wise embedding probes exceed 93% on the classification task, with an explicit source caveat that phrase content may leak class information.
- Visual relations: Attention-head probes report 69.81%/24.67% VRI/VRC for UNITER and 67.53%/18.89% for LXMERT, versus 50%/3.33% random guesses. Mismatched captions weaken relation signals.
- Linguistic probes: UNITER outperforms LXMERT on nine SentEval tasks, but BERT-base remains stronger across the reported best-layer scores.

### Limitations

The experiments cover two 2020-era architectures and region-feature pipelines, not current end-to-end vision-language or generative multimodal models. Attention patterns are diagnostic signals, not causal explanations. Several probes can inherit dataset shortcuts or label leakage. This run did not execute code or reproduce experiments because the paper-linked repository was unavailable and no redistributable source bundle was collected.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Caveat |
|---|---|---|---|---|
| E1 | Local PDF text, arXiv:2005.07310v2 | Full method, tables, appendices, and conclusions | High for reporting | Extraction has encoding artifacts; experiments not rerun |
| E2 | https://arxiv.org/abs/2005.07310 | Identity, authors, submission date, abstract | High | Abstract alone cannot support detailed metrics |
| E3 | https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/6959_ECCV_2020_paper.php | ECCV publication and public paper | High | Accepted paper, not independent replication |
| E4 | https://www.microsoft.com/en-us/research/publication/behind-the-scene-revealing-the-secrets-of-pre-trained-vision-and-language-models/ | Venue and institutional metadata | High | Author/institution source |
| E5 | https://github.com/JizeCao/VALUE | Paper-declared code locator | Low | Unavailable/not found; no files reviewed |
| E6 | Three repository-relative DEP manuscripts | Cross-DEP synthesis | Medium | Related concepts, not validation of VALUE |

Source claims above are paraphrased from E1–E4. Claims about transfer to current systems and product ideas below are reviewer interpretations.

## Related DEP Entries

1. [VideoWeave Geometry manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md)
   - Repository path: `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
   - Relevance: VideoWeave jointly models video and geometry latents, then distills the shared score field. VALUE's fusion and layer-wise probes offer a template for checking when geometry information enters, concentrates, or disappears.
   - Source basis: The related manuscript's inspected Executive Summary and Observations, grounded in its arXiv HTML evidence.
2. [BA-LoRA Bias manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-BA-LoRA%20Bias/ba-lora-bias-manuscript.md)
   - Repository path: `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`
   - Relevance: BA-LoRA targets representation collapse, drift, and noisy inheritance using output-space regularizers. It broadens VALUE-style analysis from observing attention/embeddings to constraining behavior during adaptation.
   - Source basis: The related manuscript's inspected Executive Summary and Observations.
3. [HSD FTI-FDet manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md)
   - Repository path: `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`
   - Relevance: HSD FTI-FDet combines coordinate attention, heterogeneous feature pathways, and self-distillation. Its ablations reinforce VALUE's finding that useful behavior is concentrated in structured subsets rather than uniformly distributed.
   - Source basis: The related manuscript's inspected Executive Summary and Observations.

## Synthesis Note

### Concept Bridge

VALUE supplies a diagnostic vocabulary—fusion degree, modality dominance, specialized heads, cross-modal alignment, and layer-wise knowledge—that can be applied to the three related deposits. VideoWeave asks whether geometry-aware information is actually integrated; BA-LoRA asks whether adaptation preserves or collapses useful representation structure; HSD FTI-FDet asks how specialized attention and distilled pathways trade accuracy against efficiency. Together they suggest a lifecycle that measures internal structure, constrains harmful drift, and validates compact deployed pathways.

### Potential Implementations

1. A checkpoint probe dashboard that compares modality mass, fusion separation, and linear-probe accuracy across training revisions.
2. A representation regression gate that rejects adapters or distilled models when diversity, cross-modal alignment, or rare-relation performance falls outside approved bounds.
3. A head/pathway ablation planner that ranks removable attention heads or feature branches using probe evidence before expensive retraining.

### Deeper Relationship Observations

1. VideoWeave and VALUE both treat multimodal fusion as measurable state, but VideoWeave optimizes a joint latent process while VALUE diagnoses an already-trained encoder.
2. BA-LoRA turns representation diagnosis into intervention: collapse and drift become regularization targets rather than post-hoc observations.
3. HSD FTI-FDet shows that specialization only becomes useful when evaluated with architecture and efficiency context; an attention score alone cannot establish a component's value.

### Conceptual Similarities

1. All four works separate broad task performance from intermediate representation behavior.
2. Each relies on structured comparisons—layers, heads, pathways, regularizers, or matched/mismatched conditions—to localize effects.
3. Each exposes a compression or efficiency opportunity once useful information is shown to be concentrated rather than uniform.

### MVP Implementations with Code Mock-Ups

1. `Modality-mass probe` — summarize attention allocated to text and image tokens.

```python
import numpy as np

def modality_mass(cls_attention, text_mask, image_mask):
    a = np.asarray(cls_attention, dtype=float)
    if a.ndim != 1 or a.size != len(text_mask) or a.size != len(image_mask):
        raise ValueError("attention and masks must be aligned 1-D arrays")
    return {
        "text": float(a[np.asarray(text_mask, bool)].sum()),
        "image": float(a[np.asarray(image_mask, bool)].sum()),
    }
```

2. `Frozen-feature probe` — test whether a synthetic relation label is linearly recoverable without modifying the encoder.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

def probe_score(features, synthetic_labels):
    model = LogisticRegression(max_iter=500)
    return float(cross_val_score(model, features, synthetic_labels, cv=3).mean())
```

3. `Checkpoint gate` — compare public-safe aggregate metrics with explicit thresholds.

```python
def checkpoint_gate(metrics, limits):
    failures = {
        name: metrics.get(name)
        for name, minimum in limits.items()
        if metrics.get(name) is None or metrics[name] < minimum
    }
    return {"accepted": not failures, "failures": failures}
```

These sketches use synthetic or aggregate inputs, avoid raw user data, and are illustrative rather than production-ready.

### Developer Challenges

1. Normalizing tokenization, image-region layouts, and attention tensors across architectures without erasing meaningful design differences.
2. Preventing probe datasets from leaking labels or rewarding shortcuts, especially when noun phrases directly encode relation classes.
3. Turning diagnostic thresholds into stable CI gates while models, datasets, and serving quantization change.

### Author Challenges

1. Separating descriptive attention evidence from causal explanation and stating that boundary consistently.
2. Reporting enough seeds, splits, probe hyperparameters, and checkpoint identifiers for independent comparison.
3. Updating the framework for generative VLMs whose outputs and internal interfaces differ substantially from 2020 region-based encoders.

## Validation Notes

- Random selection used a uniform `Get-Random` index over 75,761 PDF-parent units; selected zero-based index 9,460.
- The used-paper index contained 344 arXiv IDs; 65 candidate units matched used IDs. No exact ID/title/slug/DOI marker for the selected paper was found and no reselection occurred.
- Dedup scans covered both Black Lake repositories and automation memory. The public-safe 24-hour cutoff date was 2026-07-11.
- The local PDF was inspected through a 58,111-byte `pypdf` extraction cache; no local HTML or source package was available.
- Exactly three related DEP entries were inspected and used.
- No original source files were collected into this report or DEP.
- Public content intentionally withholds local paths, home identifiers, machine names, timezone labels, and exact execution timestamps.

## Attribution Block

- Source URL: https://arxiv.org/abs/2005.07310
  - Applies to: source identity, authors, abstract, version history, and paper-level claims.
  - Notes: Primary public arXiv record.
- Source URL: https://arxiv.org/pdf/2005.07310
  - Applies to: methods, tables, appendices, results, and limitations.
  - Notes: Public PDF corresponding to the locally inspected paper.
- Source URL: https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/6959_ECCV_2020_paper.php
  - Applies to: accepted-paper and ECCV context.
  - Notes: ECVA publication page.
- Source URL: https://www.microsoft.com/en-us/research/publication/behind-the-scene-revealing-the-secrets-of-pre-trained-vision-and-language-models/
  - Applies to: institutional metadata and venue confirmation.
  - Notes: Microsoft Research publication page.
- Source URL: https://doi.org/10.1007/978-3-030-58539-6_34
  - Applies to: persistent publication identity.
  - Notes: ECCV proceedings DOI.
- Source URL: https://github.com/JizeCao/VALUE
  - Applies to: code-availability note only.
  - Notes: Declared by the paper but unavailable; no code inspected.
- Repository source: `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
  - Applies to: related-entry synthesis.
  - Notes: Repository-relative generated research artifact.
- Repository source: `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`
  - Applies to: related-entry synthesis.
  - Notes: Repository-relative generated research artifact.
- Repository source: `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`
  - Applies to: related-entry synthesis.
  - Notes: Repository-relative generated research artifact.
