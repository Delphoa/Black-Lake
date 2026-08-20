---
title: "Move You Say - DEP-E"
generated_date: "2026-08-19"
artifact_type: "DEP-E research deposit"
arxiv_id: "2403.18036v1"
doi: "10.48550/arXiv.2403.18036"
selection_method: "Uniform random draw over parent-paper units formed from rg PDF enumeration; PowerShell Get-Random selected index 6095 of 75964 units."
cache_method: "document-source-processing missing-only extraction against the central local cache; html-regex for HTML and pypdf for PDF."
dedup_validation: "Checked the public dedup index, Black Lake logs/reports/DEP entries, related Black-Lake-Data entries, and automation memory; no duplicate; zero reselections."
source_policy: "Source files and derived caches withheld locally; no source files uploaded."
---

# Move You Say - DEP-E

## Source Metadata

| Field | Value |
| --- | --- |
| Title | Move as You Say, Interact as You Can: Language-guided Human Motion Generation with Scene Affordance |
| Authors | Zan Wang; Yixin Chen; Baoxiong Jia; Puhao Li; Jinlu Zhang; Jingze Zhang; Tengyu Liu; Yixin Zhu; Wei Liang; Siyuan Huang |
| arXiv ID | 2403.18036v1 |
| DOI | 10.48550/arXiv.2403.18036 |
| Date | Submitted 2024-03-26; CVPR 2024 context |
| Review scope | Problem, method, data, metrics, limitations, implementation relevance, and related DEP synthesis |
| Source state | Complete after bounded local repair: valid PDF and full-paper HTML |
| Public source policy | Local source files, extracted text, caches, and acquisition records withheld |

## Evidence Ledger

| ID | Evidence statement | Source |
| --- | --- | --- |
| E1 | The method separates scene-language grounding from motion generation with an affordance map. | [Official full-paper HTML](https://arxiv.org/html/2403.18036), method |
| E2 | The affordance map uses scene-point to joint distances, a Gaussian distance transform, and temporal max pooling. | [Official full-paper HTML](https://arxiv.org/html/2403.18036), affordance formulation |
| E3 | Evaluation uses HumanML3D, HUMANISE, and a novel-scene set with new descriptions. | [Official full-paper HTML](https://arxiv.org/html/2403.18036), datasets and experiments |
| E4 | HUMANISE encoder-conditioned results include goal distance 0.156, contact 95.86, and non-collision 99.69. | [Official full-paper HTML](https://arxiv.org/html/2403.18036), results table |
| E5 | The novel-scene split lacks ground-truth motions and reports weaker quality and action scores than established benchmarks. | [Official full-paper HTML](https://arxiv.org/html/2403.18036), novel-scene evaluation |
| E6 | Failure cases include unseen human-scene interactions and complex descriptions; diffusion inference is slower. | [Official full-paper HTML](https://arxiv.org/html/2403.18036), limitations |

## Executive Summary

The paper proposes a two-stage system for generating human motion from language in a 3D scene. The first stage, an Affordance Map Diffusion Model, predicts where and how the described interaction should relate to scene geometry. The second stage, an Affordance-aware Motion Diffusion Model, generates SMPL-X motion conditioned on language, scene information, and the predicted affordance map. This design makes a spatial-temporal intermediate representation available for analysis and correction.

Reported benchmark results indicate strong contact, goal, and non-collision behavior on HUMANISE, while the novel-scene evaluation exposes a harder generalization regime without ground-truth motions. The evidence supports the value of explicit scene affordances, but does not establish universal superiority across all metrics or deployment conditions. The most important implementation opportunity is to retain the intermediate affordance state as an auditable interface rather than hiding it inside a single end-to-end generator.

## Detailed Summary

### Problem and Motivation

Text-only motion generation can produce actions that are plausible in isolation but inconsistent with the objects, locations, or geometry of a scene. The paper treats human-scene interaction as a joint language, geometry, and motion problem. Its focus is to generate motions that satisfy the described interaction while respecting the scene.

### Method

The scene is represented with RGB point-cloud information, language with token features, and motion with SMPL-X joints. The affordance map scores scene points by their distance to motion joints, applies a distance-based transform, and aggregates the temporal dimension. An Affordance Map Diffusion Model uses a Perceiver-style architecture to predict this representation. An Affordance-aware Motion Diffusion Model adds an affordance encoder and Transformer-based conditioning to motion diffusion. The reported configuration uses a frozen CLIP-ViT-B/32 text encoder and AdamW training.

### Data and Evaluation

The paper augments HumanML3D with floor and furniture context and aligns AMASS motion with ScanNet scenes for HUMANISE. It also evaluates novel descriptions and scenes drawn from ScanNet, PROX, Replica, and Matterport3D. The consolidated data description reports 63,770 language-scene-motion examples, with 48,470 carrying language annotations. The novel-scene set is intentionally more weakly supervised because it has no ground-truth motions.

### Reported Results

On HumanML3D, the reported Ours† row gives R-Precision values of 0.432, 0.629, and 0.733, FID 0.352, multimodal distance 3.430, diversity 9.825, and multi-modality 2.835. On HUMANISE, the encoder-conditioned configuration reports goal distance 0.156, average pairwise distance 2.597, contact 95.86, non-collision 99.69, quality 3.46, and action 4.47. The decoder-conditioned configuration reports contact 96.04 and non-collision 99.70 among its listed results. These values are reported by the paper and were not independently reproduced.

### Limitations and Failure Cases

The novel-scene results are harder to interpret because there are no ground-truth motions. The paper shows failures such as a hand-washing instruction near a tap where the body faces incorrectly, and it notes failures on complex descriptions. Diffusion also increases inference cost. Data coverage, scene diversity, and the gap between plausible movement and correct interaction remain central constraints.

## Key Claims and Evidence

| Claim | Evidence IDs | Assessment |
| --- | --- | --- |
| An explicit affordance map can connect language, scene geometry, and motion. | E1, E2 | Supported by the method description. |
| The reported system performs well on established scene-motion benchmarks. | E3, E4 | Supported for the listed metrics and configurations. |
| Generalization to novel scenes remains difficult to interpret and weaker in some quality measures. | E3, E5 | Supported; no-ground-truth evaluation limits causal conclusions. |
| The intermediate map is a useful integration and debugging seam. | E1, E2, E6 | Implementation inference grounded in the architecture and failure cases. |
| The method solves scene-aware motion generation in general. | E1, E5, E6 | Not established; scope is limited by data, failure cases, and unrerun experiments. |

## Methodology

### Random Selection

The candidate pool was enumerated with rg --files -g "*.pdf" under the local arXiv archive. Each PDF parent directory was treated as one paper unit, yielding 75,964 units from 75,967 PDF files. A uniform PowerShell Get-Random draw selected index 6,095. The first draw was accepted.

### Source Integrity and Repair

The selected unit initially contained a valid PDF but lacked full-paper HTML, so review was paused. A bounded archive repair obtained the public arXiv full-paper HTML and refreshed local provenance, summary, and verification records. The PDF began with %PDF-, ended with %%EOF, and the full HTML passed size, body-text, article-marker, heading, and paper-structure checks. Abstract-only HTML was treated as metadata and did not satisfy the gate.

### Cache Method

The document-source-processing preflight was run before extraction. The paper was processed in missing-only mode against the central local cache. HTML used html-regex; PDF used pypdf because pdftotext was unavailable; no source extractor was used because no local source package was available. The cache status was cached, with HTML and PDF text outputs present and source text absent.

### Deduplication and Reselection

The public dedup index was checked first, followed by Black Lake logs, reports, DEP entries, relevant Black-Lake-Data entries, and automation memory. Searches covered the arXiv ID, DOI, normalized title, and slug. No matching artifact or same-paper 24-hour marker was found. Duplicate exclusions and reselections were both zero.

### Synthesis

Claims were tied to the evidence ledger and compared with exactly three related DEP entries: AR-Drag Motion for controllable motion, Habitat Synthetic Scenes for scene coverage, and NaLA A 3D Native LLM for language-conditioned spatial representation. No experiments or implementation execution were performed.

## Scope, Constraints, and Assumptions

- This is a source-grounded review, not an independent replication.
- Reported metrics are transcribed as evidence and are not new measurements.
- Novel-scene results have no ground-truth motions, so quality and action judgments require careful interpretation.
- The official implementation repository was inspected for public implementation context; dependencies, checkpoints, and datasets were not executed or redistributed.
- The review assumes the public arXiv HTML corresponds to the repaired local paper unit.
- Source files, extracted text, caches, and acquisition records remain local.

## Observations

1. The affordance map is the paper's most reusable design boundary because it expresses scene relevance before motion decoding.
2. Contact and non-collision metrics can improve system observability, but they do not fully measure language faithfulness or correct object identity.
3. Scene coverage is a model capability constraint: unfamiliar furniture, geometry, or interaction topology can expose failures not visible on benchmark averages.

## Considerations

- Keep grounding confidence, contact, collision, goal distance, and semantic match as separate signals.
- Preserve the affordance map and coordinate transforms in evaluation records.
- Treat latency as part of the product contract when diffusion sampling is used interactively.
- Use synthetic or authorized scenes for public regression tests where redistribution is restricted.

## Strengths

- Explicit intermediate representation links language, geometry, and motion.
- Evaluation spans familiar benchmarks and a harder novel-scene setting.
- Failure analysis identifies interaction-level errors rather than only aggregate scores.
- The public implementation gives a practical starting point for further review.

## Weaknesses

- Novel-scene evaluation lacks ground-truth motions.
- Reported metrics were not independently reproduced in this deposit.
- The method remains sensitive to data and scene coverage.
- Diffusion inference can be slow for interactive use.

## Potential Improvements

| Improvement | Rationale | Validation |
| --- | --- | --- |
| Add object-identity and affordance-localization metrics | Separate correct interaction targets from plausible motion | Human and geometric agreement on held-out scenes |
| Release a small authorized regression suite | Make claims reproducible without restricted data | Fixed manifests, seeds, and checkpoint hashes |
| Distill or cache affordance proposals | Reduce motion-generation latency | Quality-latency curves under the same evaluation protocol |

## Potential Implementations

1. A batch authoring tool that produces language, affordance maps, motion candidates, and contact/collision reports.
2. A dataset quality gate that rejects samples with inconsistent language, scene region, and joint trajectory.
3. An interactive simulator widget that lets an operator edit the affordance map before generating motion.

## Three Ways to Exercise This Research

1. Reimplement the distance-based affordance map on a small authorized synthetic scene set and test coordinate-frame invariance.
2. Build a benchmark harness that reports semantic match, goal distance, contact, non-collision, diversity, and latency separately.
3. Prototype human correction by allowing an operator to select a scene region and compare motion candidates conditioned on that edit.

## Example MVP Product

### Product Name

Affordance Motion Studio

### User

An interaction designer or simulation engineer authoring human-scene behaviors.

### Input

Natural-language instruction, a permitted RGB point cloud, and optional motion constraints.

### Processing

Generate several affordance maps, render candidate motions, compute grounding/contact/collision diagnostics, and let the user approve or edit the spatial intermediate.

### Output

A motion clip, an auditable affordance map, evaluation metrics, and a provenance record containing only permitted public references.

### Success Criteria

Users can identify and correct wrong-object or wrong-location failures before export, while preserving a measurable quality-latency trade-off.

### Safety and Governance

Use only authorized scene and motion data, preserve license metadata, keep source materials local when redistribution is not permitted, and require human approval for exported behavior.

## Related Research and Reading

1. [AR-Drag Motion DEP](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-AR-Drag%20Motion) — autoregressive motion control and responsiveness.
2. [Habitat Synthetic Scenes DEP](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260724-Habitat%20Synthetic%20Scenes) — scalable 3D scene coverage and realism.
3. [NaLA A 3D Native LLM DEP](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260809-NaLA%20A%203D%20Native%20LLM) — language-conditioned native 3D representation.

## Source References

| ID | Reference |
| --- | --- |
| R1 | [arXiv abstract](https://arxiv.org/abs/2403.18036) |
| R2 | [Full-paper HTML](https://arxiv.org/html/2403.18036) |
| R3 | [arXiv PDF](https://arxiv.org/pdf/2403.18036) |
| R4 | [arXiv e-print](https://arxiv.org/e-print/2403.18036) |
| R5 | [DOI](https://doi.org/10.48550/arXiv.2403.18036) |
| R6 | [Afford Motion project page](https://afford-motion.github.io/) |
| R7 | [Official implementation](https://github.com/afford-motion/afford-motion) |
| R8 | [AR-Drag Motion DEP](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-AR-Drag%20Motion) |
| R9 | [Habitat Synthetic Scenes DEP](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260724-Habitat%20Synthetic%20Scenes) and [NaLA A 3D Native LLM DEP](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260809-NaLA%20A%203D%20Native%20LLM) |

## Appendix

### Validation Checklist

- YAML title and H1 are identical and within the 40-character limit.
- Required manuscript sections are present.
- Three related DEP entries were selected from public repository records.
- The local source-integrity gate passed before review.
- Cache methodology, random selection, and dedup/reselection validation are recorded.
- No private paths, usernames, machine names, runtime stamps, source files, extracted source text, or caches appear in this manuscript.
