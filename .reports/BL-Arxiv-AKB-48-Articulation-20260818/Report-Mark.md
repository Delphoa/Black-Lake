# Report-Mark: AKB-48 Articulation

## Source Metadata

| Field | Value |
|---|---|
| Selected work | *AKB-48: A Real-World Articulated Object Knowledge Base* |
| arXiv identity | `2202.08432v1`, submitted 2022-02-17 |
| arXiv authors | Liu Liu; Wenqiang Xu; Haoyuan Fu; Sucheng Qian; Yang Han; Cewu Lu |
| Published authors | Liu Liu; Wenqiang Xu; Haoyuan Fu; Sucheng Qian; Qiaojun Yu; Yang Han; Cewu Lu |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2022 |
| Persistent IDs | `10.48550/arXiv.2202.08432`; `10.1109/CVPR52688.2022.01439` |
| Primary sources | https://arxiv.org/abs/2202.08432; https://arxiv.org/html/2202.08432; https://arxiv.org/pdf/2202.08432; https://arxiv.org/e-print/2202.08432 |
| Publisher record | https://openaccess.thecvf.com/content/CVPR2022/html/Liu_AKB-48_A_Real-World_Articulated_Object_Knowledge_Base_CVPR_2022_paper.html |
| Supplemental material | https://openaccess.thecvf.com/content/CVPR2022/supplemental/Liu_AKB-48_A_Real-World_CVPR_2022_supplemental.pdf |
| Official project | https://liuliu66.github.io/AKB-48/ |
| Project repository | https://github.com/liuliu66/AKB-48/tree/gh-pages |
| Source integrity | Verified complete PDF and full-paper HTML; metadata and TeX/source package also inspected; all source files withheld locally |
| Review date | 2026-08-18 |

The arXiv v1 byline contains six authors, while the CVPR record contains seven and adds Qiaojun Yu. This report preserves both records instead of silently merging them. The complete local source corresponds to arXiv v1; the CVPR page is used for publisher identity, venue, and the published byline. Page ranges are omitted because currently indexed publisher and proceedings records disagree.

## Concise Research Notes

AKB-48 addresses a real gap between visually plausible CAD assets and physically grounded articulated-object models. It contains 2,037 real-world-derived models across 48 categories. Each model is organized as an Articulation Knowledge Graph (ArtiKG) spanning appearance, kinematic structure, semantics, and physical properties. The paper reports roughly 63,000 vertices and 126,000 triangles per AKB-48 object, along with part/joint labels, semantic taxonomy, part mass, estimated inertia, material, and friction.

The FArM acquisition pipeline combines scanning, canonical alignment, manual part segmentation, joint-tree annotation, and physical-property annotation. The source reports about five minutes for scanning and 10-15 minutes for annotation per object, while its budget comparison uses 20 minutes and about USD 3 for real-world scanning versus more than 120 minutes and USD 100 for outsourced CAD modeling. These are source estimates, not a controlled cost study, and the inexpensive-object assumption does not apply uniformly to laptops, microwaves, doors, or other costly categories.

AKBNet operationalizes the dataset as a cascade from single RGB-D input to part segmentation and NOCS coordinates, per-part 6D pose and joint parameters, implicit shape reconstruction, and reinforcement-learning manipulation. Pose and shape training use 100,000 generated RGB-D images plus 10,000 real images split evenly between fine-tuning and testing. The paper does not make object-identity independence in that real-image split sufficiently explicit for a strong generalization claim.

The strongest result is not any single headline metric but the paper's ground-truth-versus-predicted-state comparison. On the real-world pose test set, AKBNet reports rotation error 9.8 degrees, translation error 0.021 m, 3D IoU 53.6, joint-axis error 8.1 degrees, joint-location error 0.019 m, and joint-type accuracy 94.6%. Reconstruction Chamfer-L1 rises from 4.2 with ground-truth joint state to 7.5 with predicted state. For TQC+HER manipulation, reported success falls from 72.5% to 40.2% on opening and from 95.5% to 44.6% on pulling when predicted state replaces ground truth.

There is a material internal discrepancy: the manipulation prose says ground-truth opening and pulling are 72.5% and 98.7%, but Table 5 assigns 98.7% to SAC+HER pulling and 95.5% to TQC+HER pulling. This review treats the table as the structured result and preserves the conflict. The paper also does not report trial denominators, confidence intervals, repeated seeds, or a sufficiently detailed account of manipulation evaluation conditions in the main text.

The official project currently exposes category browsing and a Google Drive dataset pointer. Its linked GitHub repository is a `gh-pages` project-site tree, not an established AKBNet implementation release. No official code or model checkpoint was verified in the bounded inspection, and neither dataset files nor experiments were downloaded or executed.

## Evidence and Attribution

| ID | Evidence | Supports | Assessment |
|---|---|---|---|
| E1 | Complete arXiv v1 PDF, HTML, and TeX source | Method, data construction, training setup, Tables 1-5, conclusion | High confidence for transcription; author-reported, not reproduced |
| E2 | arXiv metadata and arXiv DOI | Six-author v1 identity, submission date, public locators, CC BY 4.0 indicator | High confidence for v1 metadata |
| E3 | CVPR 2022 record and proceedings DOI | Seven-author published identity, venue, pagination, supplemental locator | High confidence for publisher metadata |
| E4 | AKB-48 project/download pages and `gh-pages` repository | Public object browsing, dataset pointer, present project-repository scope | Medium-high; linked dataset contents and terms were not inspected |
| E5 | MemPose Geometry DEP-A | Category-level object pose/size estimation and geometric-memory comparison | Medium; conceptual neighbor, not validation of AKB-48 |
| E6 | ManipulationNet DEP-A | Persistent physical-skill benchmarking and cross-site calibration requirements | Medium; evaluation bridge only |
| E7 | FAVLA Fast-Slow DEP-E | Contact-rich control, force-aware feedback, timing, and explicit physical failure modes | Medium; downstream control bridge only |
| E8 | Public-safe workflow record | Random selection, dedup, complete-source gate, and no-source-upload policy | High for process validation |

Source claims are labeled as such. Reviewer interpretations include the cascade-error framing, the recommendation to treat ArtiKG as a typed measurement graph, and the proposed evaluation products below. Nothing in this report claims independent reproduction, code execution, or inspection of the full downloadable dataset.

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260806-MemPose Geometry/2607.04930-whitepaper-review.md`
   - Relevance: MemPose estimates category-level 9-DoF object pose and size using accumulated geometric memory. It directly neighbors AKBNet's per-part pose/state stage and suggests a testable way to reduce the predicted-state bottleneck.
   - Source basis: the inspected DEP-A reconstructs MemPose's category-level RGB/point-cloud inputs, geometric memory, pose outputs, and reported benchmark envelope.
2. `.lake-data/DEP-A/DEP-A-20260727-ManipulationNet An Intake/whitepaper-intake-review.md`
   - Relevance: ManipulationNet treats real-world robot-skill evaluation as persistent infrastructure with standardized kits, calibration receipts, and separate physical-skill and embodied-reasoning tracks. It supplies the evaluation layer missing from AKB-48's compact manipulation report.
   - Source basis: the inspected DEP-A documents the benchmark's standardized hardware, unified client, site variance, intervention logging, and safety limits.
3. `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md`
   - Relevance: FAVLA adds force-aware, multi-rate feedback for contact-rich manipulation. It complements AKB-48's object-state and physical-property representation with a downstream controller that exposes force, timing, and recovery failures.
   - Source basis: the inspected DEP-E records the fast/slow architecture, force adapter, physical tasks, success/force results, ablations, and named failure cases.

## Synthesis Note

### Concept Bridge

AKB-48 is best understood as a typed world-model substrate rather than merely a 3D asset collection. MemPose addresses the reliability of the perception/state estimate, AKB-48 supplies structured geometry, kinematics, semantics, and physical priors, FAVLA consumes fast contact evidence during action, and ManipulationNet supplies persistent physical metrology. The combined chain is: **observe -> estimate articulated state -> retrieve/validate prior knowledge -> plan and act -> measure physical outcome -> update evidence**. AKB-48's own predicted-state results show why every edge in that chain needs uncertainty and provenance.

### Potential Implementations

1. **Typed ArtiKG validator:** verify units, frames, joint-tree consistency, mesh/part alignment, material provenance, and uncertainty before an object record enters training or simulation.
2. **Cascade-error benchmark:** replay pose, shape, and manipulation stages with ground-truth, perturbed, and predicted upstream state to estimate sensitivity and define abstention thresholds.
3. **Physical benchmark adapter:** map AKB-48 categories and joint types into versioned ManipulationNet-style tasks with calibration, intervention, force, failure, and recovery receipts.

### Deeper Relationship Observations

1. MemPose and AKB-48 both rely on category-level geometric regularity, but AKB-48 permits varied kinematic structures inside semantic categories; memory retrieval must therefore be joint-structure-aware, not category-label-only.
2. FAVLA shows that static physical properties are insufficient during contact. Mass, inertia, and friction priors should initialize control, while fresh force/torque evidence must be allowed to override stale or approximate annotations.
3. ManipulationNet changes the unit of evidence from a paper table to a longitudinal physical receipt. That is especially important for AKB-48 because scanner calibration, mesh refinement, object wear, and operator setup can alter downstream outcomes without changing a model checkpoint.

### Conceptual Similarities

1. All four records decompose embodied performance into explicit intermediate state rather than relying on an opaque end-to-end score.
2. All depend on category transfer while facing instance-specific geometry, kinematics, hardware, or contact variation.
3. All benefit from a separation between nominal knowledge, live observation, action policy, and physical outcome so failure can be localized.

### MVP Implementations with Code Mock-Ups

1. **ArtiKG contract checker:** validate a synthetic record before simulation or model ingestion.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Joint:
    kind: str
    axis_norm: float
    lower: float
    upper: float

def validate_joint(joint: Joint) -> list[str]:
    errors = []
    if joint.kind not in {"revolute", "prismatic"}:
        errors.append("unsupported joint type")
    if not 0.98 <= joint.axis_norm <= 1.02:
        errors.append("axis is not unit-normalized")
    if joint.lower >= joint.upper:
        errors.append("invalid motion limits")
    return errors
```

2. **Cascade sensitivity gate:** reject a manipulation configuration when predicted-state degradation exceeds a declared budget.

```python
def relative_drop(ground_truth: float, predicted: float) -> float:
    if ground_truth <= 0:
        raise ValueError("ground-truth score must be positive")
    return (ground_truth - predicted) / ground_truth

def passes_gate(ground_truth: float, predicted: float, max_drop: float) -> bool:
    return relative_drop(ground_truth, predicted) <= max_drop

assert not passes_gate(72.5, 40.2, max_drop=0.20)
```

3. **Physical evaluation receipt:** preserve task, hardware, calibration, state source, intervention, and outcome as one auditable record.

```python
from dataclasses import asdict, dataclass
import json

@dataclass(frozen=True)
class TrialReceipt:
    task_version: str
    hardware_id: str
    calibration_id: str
    object_state_source: str
    intervention: bool
    success: bool

def serialize(receipt: TrialReceipt) -> str:
    return json.dumps(asdict(receipt), sort_keys=True)
```

### Developer Challenges

1. **Coordinate and unit integrity:** scanner, camera, mesh, joint, simulator, and robot frames must remain versioned and convertible without silent handedness or scale errors.
2. **Uncertainty propagation:** segmentation, joint, pose, shape, and physics errors need calibrated representations that downstream control can consume rather than a single deterministic state.
3. **Artifact and license management:** large meshes, textures, images, and derived physics data need immutable manifests, redistribution review, and access-controlled storage outside public DEP commits.

### Author Challenges

1. **Reconcile source versions:** explain the six-author arXiv v1 and seven-author CVPR byline difference and publish an explicit version map.
2. **Reconcile result prose:** correct the 98.7% versus 95.5% TQC+HER pulling inconsistency and publish denominators, seeds, uncertainty, and evaluation conditions.
3. **Complete reproducibility surface:** provide a verified code/model repository, exact dataset split identities, object-disjoint leakage checks, annotation quality audits, and explicit dataset license/terms.

## Validation Notes

- Selection used `rg --files -g "*.pdf"`, 75,964 unique parent units, prior-ID exclusion, and one uniform `Get-Random` draw over 75,032 eligible units; selected index 58,660.
- Dedup scanned live Black Lake logs, reports, DEP entries, staging index, automation memory, and live Black-Lake-Data DEP/report content. It found no arXiv ID, DOI, normalized-title, slug, or recent-unit duplicate; reselections were zero.
- The initial archive unit was partial because full-paper HTML was absent. A bounded repair preserved the valid, byte-identical PDF and added verified official HTML, metadata HTML, and a readable source archive.
- Complete-source validation passed before review: PDF size/header/EOF, HTML size/body/document/heading/structure checks, metadata separation, readable source archive, and zero partial files.
- The manuscript schema, exact Report-Mark synthesis counts, three Python mock-up parses, three related entries, final attribution blocks, and publication-index row are validated before submission.
- Public-output policy: source files remain local; no PDF, HTML, TeX/source archive, dataset, cache, extracted source text, local path, machine identity, timezone, or exact execution timestamp may be committed.

## Attribution Block

- Source URL: https://arxiv.org/abs/2202.08432
  - Applies to: source identity, arXiv v1 byline, date, abstract, and public locators.
- Source URL: https://arxiv.org/html/2202.08432
  - Applies to: complete-paper methods, tables, results, conclusion, and references.
- Source URL: https://arxiv.org/pdf/2202.08432
  - Applies to: complete-paper layout, figures, tables, and page-level cross-checks.
- Source URL: https://arxiv.org/e-print/2202.08432
  - Applies to: TeX source cross-checks and exact Table 5 values.
- Source URL: https://doi.org/10.48550/arXiv.2202.08432
  - Applies to: persistent arXiv identity.
- Source URL: https://openaccess.thecvf.com/content/CVPR2022/html/Liu_AKB-48_A_Real-World_Articulated_Object_Knowledge_Base_CVPR_2022_paper.html
  - Applies to: CVPR venue and seven-author published record; conflicting page ranges were not propagated.
- Source URL: https://openaccess.thecvf.com/content/CVPR2022/supplemental/Liu_AKB-48_A_Real-World_CVPR_2022_supplemental.pdf
  - Applies to: official supplemental-material locator; only indexed material was inspected.
- Source URL: https://doi.org/10.1109/CVPR52688.2022.01439
  - Applies to: persistent CVPR proceedings identity.
- Source URL: https://liuliu66.github.io/AKB-48/
  - Applies to: official project scope and category browsing.
- Source URL: https://github.com/liuliu66/AKB-48/tree/gh-pages
  - Applies to: project-site repository scope and observed public tree.
- Source file: `.lake-data/DEP-A/DEP-A-20260806-MemPose Geometry/2607.04930-whitepaper-review.md`
  - Applies to: category-level pose and geometric-memory relationship.
- Source file: `.lake-data/DEP-A/DEP-A-20260727-ManipulationNet An Intake/whitepaper-intake-review.md`
  - Applies to: persistent physical-benchmark relationship.
- Source file: `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md`
  - Applies to: force-aware contact-control relationship.
- Source handling note: all original PDF, HTML, metadata, TeX/source, repair, cache, and verification files were withheld locally and were not uploaded.
