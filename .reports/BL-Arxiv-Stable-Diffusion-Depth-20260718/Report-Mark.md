# Report-Mark: Stable Diffusion Depth

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Stealing Stable Diffusion Prior for Robust Monocular Depth Estimation* |
| Authors | Yifan Mao; Jian Liu; Xianming Liu |
| arXiv | `2403.05056v1`, submitted 2024-03-08 |
| DOI | `10.48550/arXiv.2403.05056` |
| Subject | Computer Vision and Pattern Recognition (`cs.CV`) |
| Venue | No publisher venue or publisher DOI identified in the inspected primary records |
| Primary URLs | https://arxiv.org/abs/2403.05056; https://arxiv.org/html/2403.05056; https://github.com/hitcslj/SSD; https://hitcslj.github.io/ssd/ |
| Evidence status | Verified complete PDF, official full-paper HTML, TeX/source, metadata, rendered method/results pages, official project page, and official repository inspected. Source files were withheld locally. |
| Review boundary | Source-grounded method, equation, experiment, repository, and implementation review. Models, datasets, generated training images, and experiments were not executed. |

### Selection Record

- `rg --files -g "*.pdf"` found 75,777 PDFs representing 75,776 unique PDF-parent paper units.
- PowerShell `Get-Random` selected zero-based index 45,232 uniformly over those units.
- The first draw resolved to arXiv:2403.05056v1; exclusions and reselections were both zero.
- Dedup checks covered the public pointer index, Black Lake logs/reports/DEPs, automation memory, Black-Lake-Data artifacts, normalized title, arXiv DOI, slug, and active worktrees.
- Metadata-only author-inventory rows were found but no substantive same-paper artifact, including within the 2026-07-17 public-safe 24-hour cutoff.

## Concise Research Notes

### Problem

Self-supervised monocular depth estimation relies on photometric consistency between adjacent video frames. Night, rain, reflections, low texture, glare, and sensor noise weaken that assumption, while collecting aligned depth labels for every adverse condition is expensive. The paper asks whether a text/image/depth-conditioned Stable Diffusion pipeline can expand day-clear training data into challenging conditions without changing scene geometry, and whether a teacher-student depth model can absorb that synthetic prior.

### Method

The proposed Generative Diffusion Model-based Translation pipeline (GDT) captions a day-clear frame with BLIP-2, predicts depth with MiDaS and refines it with PatchFusion, conditions Stable Diffusion 1.5 through ControlNet, and injects a randomly sampled night/rain style image through IP-Adapter. The intended output preserves approximate depth while changing visibility and weather appearance.

The depth system replaces Monodepth2's ResNet depth encoder with a pretrained ViT-base DINOv2 encoder and a DPT head; PoseNet remains ResNet-18. A teacher is trained on day-clear video, then a student learns from original or GDT-translated frames. The teacher provides pseudo-depth; a DINOv2 cosine feature loss aligns original and translated semantics; a photometric mask is intended to exclude unreliable teacher pixels from distillation.

### Evidence

The authors train teacher and student for 20 epochs with AdamW, batch size 4, on one 24 GB RTX 4090. nuScenes uses 15,120 day-clear training samples and 6,019 validation samples partitioned into day-clear, night, and day-rain, evaluated over 0.1-80 m. RobotCar uses 16,563 day training samples and 1,411 tests (702 day, 709 night) over 0.1-50 m. The paper reports absRel, RMSE, and delta-1 on nuScenes, plus sqRel on RobotCar.

### Results

- On nuScenes night, SSD-S reports absRel 0.1939 versus SSD-T 0.2103; the relative reduction is about 7.8%. On day-rain, SSD-S reports 0.1410 versus 0.1718; the relative reduction is about 17.9%.
- On nuScenes day-clear, SSD-S reports 0.1217 absRel and 5.982 RMSE, while SSD-T reports 0.1223 and 6.132. SSD-T has the slightly higher delta-1 (87.39 versus 87.13).
- On RobotCar day, SSD-S reports 0.1058 absRel versus SSD-T 0.1069, but SSD-T has the better delta-1 (89.38 versus 89.09). On night, SSD-T has better absRel/sqRel/RMSE (0.1137/0.685/3.460), while SSD-S has better delta-1 (87.36 versus 86.14).
- The nuScenes aggregate ablation moves from 0.1513/6.761/81.51 for the GAN/ResNet/distillation baseline to 0.1320/6.266/84.96 after GDT/PatchFusion, the teacher loss, DINOv2, and semantic loss. The largest adjacent absRel change is the encoder swap, 0.1485 to 0.1360.
- Figures 5-6 show selected night/rain examples with visually sharper cars, pedestrians, road edges, and bicycles for SSD-T/SSD-S, but they are qualitative selections rather than a failure-complete or blinded evaluation.

### Limitations and Reviewer Interpretation

The paper supports a promising training recipe, not a deployment assurance case. The synthetic images are assumed to preserve depth, but the review found no measured geometry-preservation distribution, seed inventory, rejection rule, or human audit. The GDT stack combines at least six pretrained components, yet version pins and generated-corpus manifests are absent. Reported experiments use one run/hardware description without uncertainty, and the test domains remain two driving datasets with fixed depth truncation and test-time median scaling where marked.

There is a material equation/prose conflict. The text says the reliability mask should select cases where student photometric error is higher than teacher error and should filter unreliable teacher depths. Equation 5 instead evaluates true when teacher reconstruction error is greater than student error. Equation 6 multiplies that mask into the distillation loss, which appears to retain, not suppress, precisely the teacher-worse pixels. This could be an inequality typo, a complement-mask omission, or a prose error. The official repository contains no implementation to adjudicate it.

The repository also exposes version drift. Its README renames the framework “Universal Depth Estimation” and the loss “Reliability-Guided Distillation,” promises code, datasets, and weights before December 2024, and is MIT-licensed; at pinned commit `a5b11b77e33d3faf7d6f35d501f6fd27d0f65137`, however, the tree contains only README/LICENSE plus four image assets. Thus the arXiv statement that code and weights are available is not operationally supported by the inspected repository.

## Evidence and Attribution

| ID | Evidence | Supports | Status and Caveat |
|---|---|---|---|
| E1 | Verified PDF, official HTML, and TeX/source for arXiv:2403.05056v1 | Full method, equations, tables, figures, setup, conclusion | Primary; reviewed in full; source files withheld |
| E2 | arXiv metadata and arXiv DOI | Identity, authors, submission, subject, official locators | Primary metadata; abstract not used alone for empirical claims |
| E3 | TeX Tables 1-3 | Exact nuScenes, RobotCar, and ablation values | Primary source values; experiments not reproduced |
| E4 | Rendered PDF pages 7-14 | GDT/SSD diagrams, equations, table layout, selected qualitative figures | Visual cross-check; render emitted nonfatal font-substitution warnings |
| E5 | Official project page | Author framing, diagrams, arXiv/repository linkage | Primary author context; no additional evaluation artifact |
| E6 | Official repository at commit `a5b11b77...` | README claims, license, tree inventory, release availability | Primary implementation locator; no code/weights/datasets present |
| E7 | UAV Visual Localization DEP-E | DINOv2 robustness, domain gap, fixed-denominator metrics, abstention | Related synthesis; not independent validation of this paper |
| E8 | VideoWeave Geometry DEP-E | Geometry-constrained diffusion and spatial-consistency evaluation | Related synthesis; not independent validation of this paper |
| E9 | Stereo Lane Detection DEP-E | Driving geometry, calibration, adverse conditions, latency/recovery evidence | Related synthesis; not independent validation of this paper |

Claim discipline:

- All benchmark values are author-reported unless the arithmetic is explicitly identified as reviewer recomputation.
- “Robust” is limited to the reported dataset slices, metrics, depth ranges, and scaling protocol.
- Repository presence is not treated as reproducibility; the inspected tree lacks executable artifacts.
- Related DEP entries provide conceptual transfer and evaluation criteria, not corroborating experiments.

## Related DEP Entries

Exactly three related entries were inspected:

| Entry | Verified path | Concrete overlap | Source basis |
|---|---|---|---|
| UAV Visual Localization - DEP-E | `.lake-data/DEP-E/DEP-E-20260716-UAV Visual Localization/uav_visual_localization_manuscript.md` | Both use DINOv2 features to bridge severe appearance/domain gaps in outdoor geometry tasks and both need drift-inclusive metrics, confidence, and abstention before control use. | Manuscript method, Tables I-III, observations, and deployment considerations |
| VideoWeave Geometry - DEP-E | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Both repurpose diffusion priors for geometry-sensitive vision. VideoWeave makes geometry consistency an explicit validation axis, directly exposing the missing audit in GDT's assumed depth preservation. | Manuscript method, geometry metrics, weaknesses, and Geometry Consistency Gate |
| Stereo Lane Detection - DEP-E | `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md` | Both target driving-scene geometry under difficult sensing conditions and depend on hidden calibration/metric contracts; the related artifact separates relative gains from adverse-condition, latency, recovery, and safety evidence. | Manuscript disparity pipeline, evaluation arithmetic, domain-shift section, and implementation gaps |

## Synthesis Note

### Concept Bridge

Stable Diffusion Depth can be read as an offline world-variation generator feeding a perception learner. VideoWeave supplies the missing verification principle: generated appearance is useful only when spatial state is measured rather than assumed. UAV Visual Localization shows how DINOv2 features can tolerate cross-source appearance changes yet still fail catastrophically through retrieval, geometry, or domain shift. Stereo Lane Detection adds the driving-systems contract: calibration, temporal recovery, adverse slices, fixed denominators, and target-device cost must surround any perception gain before operational use.

### Potential Implementations

1. **Depth-preserving synthetic-data gate**: Generate bounded day-to-night/rain pairs, compare depth/edge/flow consistency with independent estimators, quarantine failures, and version prompts, models, seeds, source frames, and rejection reasons.
2. **Reliability-aware teacher-student trainer**: Implement both interpretations of Equations 5-6, record teacher/student photometric error by condition, and require unit tests plus factorial ablations before selecting a mask direction.
3. **Robust depth evidence dashboard**: Report every method on fixed denominators across day/night/rain/glare/sensor/geography slices with calibration, delta-1, absRel, RMSE, failure rate, latency, and abstention coverage.

### Deeper Relationship Observations

1. **Generative priors need discriminative gates**: GDT and VideoWeave both import generative capacity into geometry problems, but their value depends on an independent measurement channel that the generator cannot trivially satisfy through appearance.
2. **Foundation features shift rather than remove failure**: DINOv2 improves aggregate ablation results and cross-source localization, yet both papers expose reflective surfaces, domain gaps, and geometric assumptions that semantic features alone do not resolve.
3. **Driving perception is a systems property**: Depth and lane geometry become useful only with calibration provenance, temporal/fixed-denominator failure accounting, uncertainty, latency, and an abstention boundary at the downstream control interface.

### Conceptual Similarities

1. **Coarse prior plus task-specific geometry**: GDT supplies condition diversity, DINOv2 supplies semantic features, and DPT/photometric training supplies depth; the related visual systems similarly combine broad representations with geometric refinement.
2. **State filtering**: Teacher reliability masks, VideoWeave geometry gates, UAV drift thresholds, and stereo reset logic all decide which intermediate state can safely influence a later stage.
3. **Evidence separation**: Every useful transfer distinguishes a promising component-level result from whole-system robustness, reproducibility, or safety readiness.

### MVP Implementations with Code Mock-Ups

1. **Synthetic-pair manifest gate** - rejects untraceable or excessively inconsistent generated pairs.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class PairRecord:
    source_id: str
    condition: str
    seed: int
    depth_error: float

def accept_pair(record: PairRecord, max_depth_error: float = 0.05) -> bool:
    allowed = {"night", "rain"}
    return bool(record.source_id) and record.condition in allowed and record.depth_error <= max_depth_error
```

2. **Teacher-mask diagnostic** - makes the intended reliability direction explicit and testable.

```python
def reliable_teacher_mask(teacher_pe: list[float], student_pe: list[float]) -> list[int]:
    if len(teacher_pe) != len(student_pe):
        raise ValueError("photometric-error lengths differ")
    return [int(t <= s) for t, s in zip(teacher_pe, student_pe)]

assert reliable_teacher_mask([0.1, 0.4], [0.2, 0.3]) == [1, 0]
```

3. **Fixed-denominator slice report** - preserves failures instead of dropping difficult attempts.

```python
def slice_report(errors: list[float], threshold: float) -> dict[str, float]:
    if not errors or threshold <= 0:
        raise ValueError("nonempty errors and positive threshold required")
    failures = sum(error > threshold for error in errors)
    return {
        "attempts": float(len(errors)),
        "mean_error": sum(errors) / len(errors),
        "failure_rate": failures / len(errors),
    }
```

These are deterministic review aids, not a reproduction of the paper or authorization for autonomous driving use.

### Developer Challenges

1. **Versioned generation graph**: BLIP-2, MiDaS, PatchFusion, Stable Diffusion, ControlNet, IP-Adapter, prompts, samplers, seeds, and filters must be pinned and traceable without leaking restricted source data.
2. **Mask correctness**: The equation/prose contradiction must be resolved through tests and code review before teacher reliability affects optimization.
3. **Evaluation plumbing**: Dataset slices, metric scaling, depth truncation, calibration, latency, failure coverage, and abstention must share one immutable experiment manifest.

### Author Challenges

1. **Release completion**: Publish the promised code, weights, configs, environment lock, generation manifest, and expected outputs, with a revision matching the paper terminology.
2. **Mechanism isolation**: Run repeated-seed factorial ablations separating GDT, PatchFusion, DINOv2/DPT, semantic loss, and teacher-mask direction rather than only cumulative rows.
3. **Geometry and robustness audit**: Measure source/generated depth preservation, synthetic diversity, real-domain shift, calibration, failure tails, and independent geographies/sensors without relying only on selected figures or median scaling.

## Validation Notes

- Initial source state was partial because only the PDF and brief metadata were present.
- One bounded official arXiv repair produced verified full-paper HTML, metadata HTML, and a 30-entry TeX/source archive while preserving the byte-identical existing PDF.
- The final integrity gate passed: PDF size/header/EOF; 61,973 HTML body characters; article/LaTeXML marker; 45 headings/sections; six structure terms; zero partials.
- The extraction cache moved from miss to `cached` in `missing-only` mode with PDF, HTML, and source text present.
- Method and result pages were visually rendered and compared against extracted TeX values. Nonfatal missing-font warnings did not obscure the inspected diagrams, equations, tables, or captions.
- Exactly three related DEP manuscripts were inspected and cited.
- No model, code, dataset, generator, depth estimator, or experiment was executed.
- No `.source/` directory was created. PDF, HTML, TeX/source, extracted text, cache records, and integrity records remain local and no source file was uploaded. Review-page renderings were removed after inspection and can be reproduced from the preserved PDF.

## Attribution Block

- Source URL: https://arxiv.org/abs/2403.05056
  - Applies to: identity, authors, version, subject, abstract, DOI, and official artifact locators.
- Source URL: https://arxiv.org/pdf/2403.05056
  - Applies to: complete paper, equations, tables, figures, and references; source file withheld locally.
- Source URL: https://arxiv.org/html/2403.05056
  - Applies to: verified official full-paper HTML; source file withheld locally.
- Source URL: https://arxiv.org/e-print/2403.05056
  - Applies to: exact equation and table verification; source archive withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2403.05056
  - Applies to: arXiv DOI identity.
- Source URL: https://hitcslj.github.io/ssd/
  - Applies to: official project framing and method diagrams.
- Source URL: https://github.com/hitcslj/SSD
  - Applies to: official repository README, MIT license, asset tree, and release-availability assessment at commit `a5b11b77e33d3faf7d6f35d501f6fd27d0f65137`.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: repository filing, attribution, source-withholding, and submission rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP-E container and publication-index rules.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: companion-repository dedup and layout authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-UAV%20Visual%20Localization/uav_visual_localization_manuscript.md
  - Applies to: DINOv2, domain-gap, localization-metric, and abstention concept bridge.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: diffusion-prior and geometry-consistency concept bridge.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Stereo%20Lane%20Detection/stereo_lane_detection_manuscript.md
  - Applies to: adverse-condition, calibration, latency, recovery, and driving-geometry concept bridge.
