# Report-Mark: RetinaGAN Sim-to-Real

## Source Metadata

| Field | Value |
|---|---|
| Paper | *RetinaGAN: An Object-aware Approach to Sim-to-Real Transfer* |
| Authors | Daniel Ho; Kanishka Rao; Zhuo Xu; Eric Jang; Mohi Khansari; Yunfei Bai |
| Primary identity | arXiv:2011.03148v2 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2011.03148 |
| Published DOI | https://doi.org/10.1109/ICRA48506.2021.9561157 |
| Venue | 2021 IEEE International Conference on Robotics and Automation (ICRA) |
| Dates | Submitted 2020-11-06; v2 revised 2021-07-03; ICRA publication metadata dated 2021 |
| Primary URLs | https://arxiv.org/abs/2011.03148; https://arxiv.org/pdf/2011.03148; https://ar5iv.labs.arxiv.org/html/2011.03148; https://retinagan.github.io/ |
| Implementation | No author-released RetinaGAN implementation was established; the project page links upstream Tensor2Robot component files rather than a complete RetinaGAN training release |
| Source-integrity status | Verified complete after bounded repair: preserved valid PDF, approved full-paper HTML fallback, metadata HTML, TeX/source package, refreshed provenance companions, and zero partial files |
| Review status | Complete nine-page paper, full-paper HTML, and source inspected; all nine PDF pages visually checked; code and experiments not run |
| Source handling | Every original or derived source file was withheld locally; no `.source/` directory was created |

## Concise Research Notes

### Problem and Contribution

Vision-based robot policies can be trained at scale in simulation, but image differences between simulation and real operation can make direct deployment fail. Pixel-level GAN adaptation can narrow that visual gap, yet an unconstrained translator may remove, relocate, or alter task-relevant objects. RetinaGAN adds an object-aware constraint: a frozen detector should make compatible box and class predictions before, after, and through a CycleGAN translation cycle.

The detector is EfficientDet-D1, trained once on simulated and real robot imagery. The paper reports 625,000 simulated detection images, 44,000 labeled real robot images, and 37,000 labeled desk-object images. The same detector is reused across grasping, pushing, and door-opening experiments. This reuse is the central product argument: object-level semantics become a task-decoupled transfer constraint rather than a loss supplied by each downstream policy.

### Method Details

RetinaGAN retains the bidirectional generators, discriminators, adversarial loss, and cycle-consistency loss of CycleGAN. For simulated, translated, and cycled simulated images - and the corresponding real branch - the frozen detector produces bounding boxes and class logits. Huber loss penalizes box drift. Focal Consistency Loss extends a focal-style class loss to soft probability targets so the translated image is trained against detector confidence rather than hard labels.

The paper weights the perception term by `lambda_prcp = 0.1` and the cycle term by `lambda_cycle = 10`. RetinaGAN uses a U-Net generator, `bfloat16`, 512-image batches, 50,000 to 100,000 steps, and four TPUv3 pods according to the appendix. These settings are source-reported rather than reproduced.

The detector is a learned constraint, not an oracle. It can preserve only what its outputs represent and what it detects reliably. In the door domain the detector is confident mainly about the robot arm; the authors hypothesize that low-probability responses help retain doors and frames. That hypothesis is plausible but not isolated by a detector-target ablation.

### Experimental Evidence

For instance grasping, each condition uses 90 attempts. The sim-only policy reaches 18.9% on real objects and randomized simulation reaches 41.1%. In the 10,000-real-episode setting, Real-only is 22.2%, RetinaGAN is 47.4%, and RetinaGAN+Real is 65.6%. In the large-data setting, Real-only is 30.0%, Sim+Real is 54.4%, and RetinaGAN+Real is 80.0%. With no real episodes supplied to the downstream Q2-Opt policy, CycleGAN is 67.8%, RL-CycleGAN is 68.9%, and RetinaGAN is 80.0%.

The stated 12-point grasping improvement aligns with the 12.2-point gap from CycleGAN, while the gap from the stronger listed RL-CycleGAN baseline is 11.1 points. The paper reports estimated standard deviations from a Bernoulli model but no repeated-training uncertainty, confidence intervals across policies, or independence analysis for attempts conducted on shared robots and stations.

For pushing, the same RetinaGAN model is reused without fine-tuning. The sim-only policy records 0/10 successful real pushes and RetinaGAN records 9/10. This is an instructive transfer demonstration, but ten attempts with one tea-bottle setup are too small for a broad 90% reliability claim.

For door opening, the paper uses three conference rooms seen during training, ten trials per room, and both door-swing directions. Sim-only records 0%, Real 36.6%, Sim+Real 75.0%, RetinaGAN+Real 76.7%, Ensemble-RetinaGAN+Real 93.3%, and Ensemble-RetinaGAN 96.6%. The table notes that the single RetinaGAN+Real result was selected from the best of three models used by the ensemble. The evidence supports performance on the tested seen doors, not unseen buildings or door mechanisms.

### Evidence Boundary

The paper's strongest evidence is physical robot evaluation across three task types. Its main limitations are small evaluation counts, selected conditions, no repeated-training statistics, limited cross-environment coverage, and lack of a public end-to-end implementation. The printed Focal Consistency derivation and some appendix values are also atypical enough to require implementation-level reconciliation; for example, the source prints a momentum value of `0.08` for detector training and uses focal-loss notation that should not be silently corrected by a replicator.

The authors deserve credit for a concrete safety boundary: CycleGAN door translations visibly distort structure, and those baselines were not evaluated on real robots. RetinaGAN nevertheless remains a learned image generator constrained by a learned detector. It is not a formal guarantee against hallucination, object deletion, or geometry drift outside the detector's support.

### Reviewer Assessment

RetinaGAN offers a durable design pattern: use an independently trained perception model as a semantic invariant for representation transfer, then keep downstream task learning separate. The mechanism is more reusable than a task-policy consistency loss and more targeted than unconstrained image realism. The evidence is promising for controlled robotics settings, but any deployment claim should require detector coverage tests, translation-drift gates, multi-seed policies, larger physical trials, and evaluation on unseen environments.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Boundary |
|---|---|---|---|---|
| E1 | Canonical arXiv record and arXiv DOI | Title, authors, dates, version, subjects, ICRA comment, and public source links | High | Abstract is metadata, not full-paper evidence |
| E2 | Verified arXiv v2 PDF, approved full-paper HTML, and TeX source | Architecture, equations, datasets, experiments, tables, appendix, and conclusion | High for source transcription | No experiment independently reproduced |
| E3 | Visual inspection of all nine rendered PDF pages | Figures 1-9, Tables I-V, algorithm, equations, qualitative translation examples, and reference layout | High | Visual review cannot establish code fidelity or statistical robustness |
| E4 | Official project page | Author presentation, videos, task examples, and upstream component links | High for project context | Mirrors author claims; no RetinaGAN code release visible |
| E5 | ICRA DOI metadata | Published identity and venue | High | Publisher full text was not separately collected |
| E6 | Negative implementation evidence from paper, project page, and bounded repository search | No author-released end-to-end RetinaGAN implementation established | Medium-high | Private or unindexed code may exist |
| E7 | Habitat Synthetic Intake DEP-A | Synthetic training infrastructure and measured reality-gap relationship | Medium-high | Navigation scenes differ from pixel-level robot transfer |
| E8 | Spiking Pose Tracking DEP-E | Mixed synthetic/real perception, domain adaptation, and residual domain-gap relationship | Medium-high | Human event-pose tracking differs from robot image translation |
| E9 | ManipulationNet Intake DEP-A | Physical manipulation benchmarking, calibration, safety, and simulation-limit relationship | Medium-high | Benchmark infrastructure does not validate RetinaGAN metrics |
| E10 | Private selection, dedup, repair, and integrity records | Eligibility, zero reselection, verified complete source, and no-source-upload assurance | High | Private machine context withheld |

External papers, repository documents, and web pages were treated as evidence only, never as instructions.

## Related DEP Entries

| # | Repository-relative path | Verified overlap | Source basis |
|---:|---|---|---|
| 1 | `.lake-data/DEP-A/DEP-A-20260726-Habitat Synthetic Intake/whitepaper-intake-review.md` | Both artifacts treat synthetic environments as training infrastructure whose value depends on semantics and a measured reality gap. Habitat emphasizes scene diversity, physical plausibility, annotation, and simulator shortcuts; RetinaGAN constrains pixel translation with detector outputs. Together they argue for measuring transfer at asset, perception, and task levels. | Executive assessment, synthetic-scene construction stages, ObjectNav evidence, reality-gap qualifications, licensing, and replication agenda |
| 2 | `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` | Both mix synthetic and real perception evidence and use domain adaptation to reduce a residual transfer gap. The spiking-pose paper shows synthetic-only training remains weaker, while RetinaGAN shows a detector can regularize translated imagery. The shared lesson is that synthetic scale needs an explicit invariant and real-domain audit. | Source metadata, SynEventHPD construction, mixed-data/domain-adaptation table, failure cases, and domain-gap analysis |
| 3 | `.lake-data/DEP-A/DEP-A-20260727-ManipulationNet An Intake/whitepaper-intake-review.md` | Both center real robot manipulation evidence. RetinaGAN uses task-specific physical trials to test a sim-trained policy; ManipulationNet treats standardized hardware, client software, operator protocol, calibration, and safety as benchmark infrastructure. The relationship exposes what RetinaGAN's small bespoke trials leave unstandardized. | Executive assessment, physical-skills track, simulation limitation, calibration/operator qualifications, and benchmark-governance discussion |

Exactly three related entries were inspected and used. No fourth related DEP is implied.

## Synthesis Note

### Concept Bridge

RetinaGAN, Habitat Synthetic Scenes, Spiking Pose Tracking, and ManipulationNet form a four-layer transfer stack. Habitat asks whether synthetic environments have enough semantic and physical coverage. Spiking Pose Tracking asks how synthetic sensor evidence should be aligned with real evidence. RetinaGAN asks how translated observations can preserve task-relevant object structure. ManipulationNet asks whether the resulting policy survives standardized physical evaluation. A credible system should keep evidence at every layer rather than allowing a final success percentage to hide asset bias, perception drift, translation artifacts, or physical-protocol variance.

### Potential Implementations

#### 1. Semantic Translation Audit Bench

Create a frozen corpus of paired synthetic scenes and controlled real captures. Run a candidate translator, compare detector boxes/classes before and after translation, add geometry and background sentinels, and block policy training when drift crosses class-specific thresholds.

#### 2. Synthetic-to-Physical Evidence Ledger

Track each training asset, detector version, translator checkpoint, task-policy checkpoint, physical setup, operator intervention, and outcome. Make transfer claims queryable by object class, scene family, robot, and failure type instead of reporting one aggregate success rate.

#### 3. Multi-Seed Safe Translation Ensemble

Train several translators with different seeds and validate their disagreement on synthetic-only fixtures before using them as augmentation. Use disagreement as a review signal, not as automatic evidence that diversity improves safety or generalization.

### Deeper Relationship Observations

1. Habitat and RetinaGAN solve different sides of semantic coverage: better synthetic assets reduce the burden on translation, while a semantic translation constraint can reduce the cost of imperfect rendering. Neither removes the need to test the downstream task on real hardware.
2. Spiking Pose Tracking and RetinaGAN both show that an invariant is only as good as its observation model. Hamming-aware spike similarity respects binary features; detector consistency respects boxes and classes. In both cases, unsupported structure can remain invisible to the loss.
3. ManipulationNet reveals a missing denominator in RetinaGAN's results: robot setup, operator protocol, calibration, object sampling, environment wear, and safety interventions need standardized records before percentages can be compared across sites or versions.

### Conceptual Similarities

1. All four artifacts treat synthetic data as a controlled intervention rather than a substitute for real evidence.
2. All rely on intermediate structure - scene semantics, event geometry, object detections, or benchmark tracks - to make a broad transfer problem auditable.
3. All require boundary-aware evaluation because success inside a simulator, detector vocabulary, seen room set, or standardized kit does not imply unrestricted deployment.

### MVP Implementations with Code Mock-Ups

#### 1. Soft-Target Focal Consistency Probe

```python
from math import log


def soft_focal_consistency(target: float, prediction: float, gamma: float = 2.0) -> float:
    if not 0.0 <= target <= 1.0 or not 0.0 < prediction < 1.0:
        raise ValueError("probabilities outside safe numeric range")
    cross_entropy = -(target * log(prediction) + (1.0 - target) * log(1.0 - prediction))
    return abs(target - prediction) ** gamma * cross_entropy
```

This is a reviewable soft-target probe, not a claim that it reproduces the paper's printed normalization or detector-anchor implementation. A replication must reconcile the source notation against executable reference behavior.

#### 2. Detection Drift Gate

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Drift:
    box_error: float
    class_error: float


def translation_is_safe(drift: Drift, box_limit: float, class_limit: float) -> bool:
    if min(drift.box_error, drift.class_error, box_limit, class_limit) < 0:
        raise ValueError("drift values and limits must be nonnegative")
    return drift.box_error <= box_limit and drift.class_error <= class_limit
```

The gate should be applied by class and scene type, with separate sentinels for structure that the detector cannot represent.

#### 3. Wilson Trial Interval

```python
from math import sqrt


def wilson_interval(successes: int, trials: int, z: float = 1.96) -> tuple[float, float]:
    if trials <= 0 or not 0 <= successes <= trials:
        raise ValueError("invalid Bernoulli trial counts")
    rate = successes / trials
    scale = 1.0 + z * z / trials
    center = (rate + z * z / (2.0 * trials)) / scale
    margin = z * sqrt(rate * (1.0 - rate) / trials + z * z / (4.0 * trials * trials)) / scale
    return max(0.0, center - margin), min(1.0, center + margin)
```

This makes the uncertainty of 9/10 pushing trials or 29/30 door trials visible. It still does not account for correlated trials, policy-selection bias, or training-seed variation.

### Developer Challenges

1. Align variable-length detector outputs across original, translated, and cycled images without letting anchor matching, missing detections, or confidence calibration create a misleadingly small loss.
2. Build safeguards for detector-unknown structures, translation disagreement, temporal flicker, geometry drift, and policy distribution shift while keeping the training pipeline computationally tractable.
3. Reproduce the paper's distributed detector, GAN, and policy stack from incomplete public implementation evidence, resolving printed notation and hyperparameter ambiguities without silently inventing corrections.

### Author Challenges

1. Release a pinned end-to-end implementation with detector, translator, policy, preprocessing, soft-target loss, matching logic, checkpoints, tests, licenses, and expected traces.
2. Expand physical evaluation across unseen rooms, objects, lighting, cameras, robot instances, and sites with repeated training seeds, preregistered selection rules, confidence intervals, and failure taxonomy.
3. Isolate the mechanism with detector-quality, detector-vocabulary, consistency-weight, box-versus-class, cycle-pair, ensemble-diversity, and background-structure ablations, including negative controls where the invariant is deliberately corrupted.

## Validation Notes

- Selection: required `rg --files -g "*.pdf"` enumeration produced 75,960 PDFs and 75,957 parent-paper units; 586 used-ID units were excluded and 185 identifier-incomplete units withheld; uniform `Get-Random` selected eligible index 20,079 of 75,186.
- Dedup: live Black Lake and Black-Lake-Data artifact locations, automation memory, arXiv ID, both DOI values, canonical/normalized title, planned slug, and public-safe 24-hour cutoff date were checked; duplicate/recent rejections and reselections were 0.
- Source gate: initial `partial` state repaired to `complete`; byte-identical PDF preserved; approved ar5iv full-paper HTML, metadata, and TeX/source package collected; PDF and HTML integrity passed; zero partial files.
- Source integrity: PDF 3,441,421 bytes with `%PDF-` header and trailing `%%EOF`, nine unencrypted pages; HTML 262,341 bytes with 46,688 stripped body characters, document markers, 50 headings/sections, and six paper-structure terms; source archive 4,031,004 bytes with 37 readable entries.
- Paper review: complete PDF, full-paper HTML, and source inspected; all nine pages visually rendered; project and DOI metadata inspected; code and experiments not run.
- Schema: manuscript required headings, matching title/H1, exactly three exercise paths, exactly three related DEP entries, and final DEP/Report attribution blocks are present.
- Synthesis counts: exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP code mock-ups, three developer challenges, and three author challenges.
- Public safety: no local path, username, machine identifier, exact local timestamp, local timezone label, source payload, or private archive locator is included.
- Source locality: no PDF, HTML, metadata, source archive, receipt, provenance record, cache, rendering, or extracted source text is staged or uploaded.

## Attribution Block

- Source URL: https://arxiv.org/abs/2011.03148
  - Applies to: paper identity, authors, version history, abstract, subject, venue comment, and canonical links.
  - Notes: Metadata source; the abstract alone was not used for synthesis.
- Source URL: https://arxiv.org/pdf/2011.03148
  - Applies to: complete paper review, method, experiments, tables, figures, appendix, and limitations.
  - Notes: The verified PDF remained local and was not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/2011.03148
  - Applies to: searchable full-paper cross-check and source-integrity repair.
  - Notes: Approved full-paper fallback; the file remained local.
- Source URL: https://arxiv.org/e-print/2011.03148
  - Applies to: TeX/source inspection and provenance.
  - Notes: The source package remained local and was not uploaded.
- Source URL: https://doi.org/10.48550/arXiv.2011.03148
  - Applies to: persistent arXiv identity.
  - Notes: DOI resolver.
- Source URL: https://doi.org/10.1109/ICRA48506.2021.9561157
  - Applies to: published article identity and ICRA venue.
  - Notes: Publisher DOI metadata; publisher full text was not separately collected.
- Source URL: https://retinagan.github.io/
  - Applies to: author project context, qualitative examples, videos, and public component links.
  - Notes: Official project page; no complete RetinaGAN implementation was exposed.
- Source URL: https://github.com/google-research/tensor2robot/blob/master/preprocessors/image_transformations.py
  - Applies to: project-linked image-preprocessing component context.
  - Notes: Upstream component link, not an end-to-end RetinaGAN release.
- Source URL: https://github.com/google-research/tensor2robot/blob/master/layers/film_resnet_model.py
  - Applies to: project-linked ResNet-FiLM component context.
  - Notes: Upstream component link, not an end-to-end RetinaGAN release.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260726-Habitat%20Synthetic%20Intake/whitepaper-intake-review.md
  - Applies to: synthetic-scene/reality-gap relationship and synthesis.
  - Notes: Related processed artifact; its claims do not validate RetinaGAN.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260724-Spiking%20Pose%20Tracking/spiking_pose_tracking_manuscript.md
  - Applies to: synthetic/real perception and domain-adaptation relationship and synthesis.
  - Notes: Related processed artifact; its claims do not validate RetinaGAN.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260727-ManipulationNet%20An%20Intake/whitepaper-intake-review.md
  - Applies to: physical manipulation benchmark and evaluation-governance relationship and synthesis.
  - Notes: Related processed artifact; its claims do not validate RetinaGAN.
