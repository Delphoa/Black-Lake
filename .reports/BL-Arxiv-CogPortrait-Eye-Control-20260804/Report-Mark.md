# Report-Mark: CogPortrait Eye Control

## Source Metadata

| Field | Value |
|---|---|
| Title | CogPortrait: Fine-Grained Eye-Region Control in Portrait Animation via Hierarchical Agent Planning |
| Authors | He Feng; Yongjia Ma; Donglin Di; Lei Fan; Tonghua Su |
| Identifier | arXiv:2605.28056v1 |
| Paper date | 2026-05-27, as printed in the inspected paper |
| DOI | [10.48550/arXiv.2605.28056](https://doi.org/10.48550/arXiv.2605.28056) |
| Primary record | https://arxiv.org/abs/2605.28056 |
| Full paper | https://arxiv.org/html/2605.28056 |
| PDF | https://arxiv.org/pdf/2605.28056 |
| Venue context | MM '26 header is present in the paper; acceptance or publication status was not independently established |
| Source integrity | Initial partial unit repaired to verified complete PDF and full-paper HTML before review |
| Source distribution | Source files, extracted text, caches, and private verification records withheld locally |

## Research Notes

CogPortrait addresses the gap between easy-to-specify portrait-animation controls and fine-grained ocular behavior. The paper argues that emotion labels and coarse prompts do not adequately express gaze, eyelid, blink, eyebrow, and head-motion combinations, while Action Units or driving videos impose a heavier input burden.

The proposed system has two stages. Stage 1 uses a planning agent, a composition agent, and a critic to turn a high-level label plus optional fine-grained instruction into a temporal sequence of 17-channel control states. The composition agent retrieves and stitches real-behavior prototypes; the critic checks semantic consistency and simple physiological constraints. A mapping layer projects the refined AU, gaze, and head-pose controls into 62 facial keypoints. Stage 2 uses those keypoints with a reference portrait, audio, and text prompt in a Wan2.2-derived DiT flow-matching generator. Dynamic classifier-free guidance applies a temporal schedule and stronger spatial guidance around the eyes. KTO refinement targets boundary cases such as asymmetric eyebrows and large-angle head movement.

The paper introduces the EMH benchmark with six core emotions from MEAD and six beyond-emotion categories from multiple source datasets. It reports 0.9017 AU-F1, 0.7397 AU-Temp, 0.9129 ID-Sim, and 0.0145 Eye-LMD for the full pipeline on EMH. On HDTF, it reports FID 16.68, FVD 32.90, LPIPS 0.0633, Sync-C 7.15, ID-Sim 0.9214, and Eye-LMD 0.0107. These are source-reported point estimates; no experiments were reproduced.

## Evidence and Attribution

| Evidence ID | Source | Evidence used | Assessment |
|---|---|---|---|
| E1 | arXiv metadata, https://arxiv.org/abs/2605.28056 | Title, authors, identifier, version, abstract, and public locators | High for identity; metadata is not sufficient for detailed empirical claims |
| E2 | Full paper, https://arxiv.org/html/2605.28056 | Introduction, methodology, EMH construction, experiments, tables, ablations, user-study statement, and conclusion | High for transcription; no independent reproduction |
| E3 | PDF, https://arxiv.org/pdf/2605.28056 | Printed figures, tables, training settings, metric values, and paper header | High for reported paper content; extracted-text encoding noise remains |
| E4 | DOI, https://doi.org/10.48550/arXiv.2605.28056 | Persistent arXiv-issued identifier | High for locator; not a separate publisher record |
| E5 | Local extraction cache | `pypdf` PDF text and `html-regex` full-paper text were used as private review aids | High for processing provenance; private cache is not redistributed |
| E6 | Hallo4 Portrait Motion DEP | Preference alignment, temporal feature preservation, portrait animation evaluation, and synthetic-media safety | Medium for related synthesis; a different paper and model family |
| E7 | MoGIC Boosting Motion DEP and VideoWeave Geometry DEP | Intention-to-motion planning plus latent video consistency and multi-metric evaluation | Medium for related synthesis; neither validates CogPortrait's results |

The paper's own evidence supports a plausible mechanism and reports strong metric values, but the following remain reviewer boundaries: no official implementation or checkpoint was found in the inspected paper sources; source-dataset licenses and consent were not independently audited; user-study details are deferred to the supplement; and the paper does not expose uncertainty or repeated-seed analysis in the inspected text.

## Related DEP Entries

1. [Hallo4 Portrait Motion](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260721-Hallo4%20Portrait%20Motion/hallo4_portrait_motion_manuscript.md) - directly overlaps portrait animation, audio-conditioned motion, temporal representation, preference alignment, identity preservation, and synthetic-media safety. Source basis: the live manuscript's method, metric, and reproducibility sections.
2. [MoGIC Boosting Motion](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260726-MoGIC%20Boosting%20Motion/mogic_boosting_motion_manuscript.md) - overlaps the translation of intention or high-level descriptions into motion, with explicit planning and evaluation boundaries. Source basis: the live manuscript's problem, mechanism, and safe implementation sections.
3. [VideoWeave Geometry](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md) - overlaps latent video conditioning, temporal consistency, geometry-aware controls, and the need for evaluation beyond visual appeal. Source basis: the live manuscript's method, metric, and deployment-boundary sections.

## Synthesis Note

### Concept Bridge

CogPortrait's central bridge is from semantic intention to executable temporal control: a label such as drowsiness or cognitive effort is decomposed into staged events, grounded in retrieved behavior prototypes, checked by explicit constraints, and then rendered by a video generator. This makes the paper relevant to Black-Lake work on preference-aligned portrait animation, intention-conditioned motion planning, and latent video reliability. The bridge is a reviewer synthesis, not a claim that the three neighboring systems are interchangeable.

### Potential Implementations

1. `Consent-aware portrait-control testbed`: A local research tool accepts synthetic portraits, text labels, audio, and optional eye-region instructions, then outputs keypoint trajectories plus a generated-video placeholder. It should expose every intermediate agent decision and require an explicit consent/license record before any real face data is used.
2. `Behavior-prototype audit card`: A review pipeline records which prototype channels were retrieved, how they were stitched, which physiological checks passed, and which instructions were revised. It can be used without video generation to test whether a control plan is interpretable and reproducible.
3. `Fine-grained motion evaluation gate`: A benchmark adapter combines AU-F1, AU-Temp, Eye-LMD, identity similarity, visual quality, and human-review fields, with abstention when source annotations, consent, or metric provenance are incomplete.

### Deeper Relationship Observations

1. The paper's prototype library plays a role similar to a structured memory: it prevents a language model from inventing every temporal trajectory from scratch, but it also imports the coverage and bias of the library into the generation process.
2. Dynamic CFG and KTO address different failure surfaces: CFG changes how conditioning is applied during denoising, while KTO changes the model using desirable and undesirable boundary examples. Their combined gain therefore needs matched component ablations to avoid attributing all improvement to the agent hierarchy.
3. The EMH benchmark's AU-level temporal metrics create a useful bridge between agent planning and video generation: a plan can be evaluated before rendering, while the rendered result can be checked for activation and trajectory fidelity afterward.

### Conceptual Similarities

1. CogPortrait, Hallo4, and VideoWeave all treat video generation as a conditioning and representation problem, not only as frame synthesis.
2. CogPortrait and MoGIC both translate higher-level intent into structured motion through intermediate planning or representation steps, making interpretability and failure localization possible.
3. CogPortrait, Hallo4, and VideoWeave all require multi-metric evaluation because visual quality alone can hide control, identity, temporal, or geometry failures.

### MVP Implementations

1. `Plan-to-controls validator` - Developer mock-up for validating a bounded, synthetic event plan before it is mapped to facial controls.

```python
from dataclasses import dataclass

@dataclass
class Event:
    start: float
    end: float
    label: str
    gaze: str

def validate_events(events, duration):
    assert events and duration > 0
    ordered = sorted(events, key=lambda event: event.start)
    assert ordered[0].start >= 0 and ordered[-1].end <= duration
    for left, right in zip(ordered, ordered[1:]):
        assert left.end <= right.start
    return {"events": len(ordered), "duration": duration, "valid": True}
```

2. `Prototype retrieval ledger` - Developer mock-up that records channel-weighted matching without contacting external services or handling real identity data.

```python
def choose_prototype(target, prototypes, weights):
    def distance(candidate):
        return sum(weights.get(key, 1.0) * abs(target.get(key, 0.0) - candidate.get(key, 0.0))
    ranked = sorted(prototypes, key=distance)
    if not ranked:
        raise ValueError("no approved synthetic prototypes")
    return {"prototype": ranked[0], "distance": distance(ranked[0])}
```

3. `Metric-and-consent gate` - Developer mock-up that refuses a public-safe evaluation record when provenance or consent fields are incomplete.

```python
def evaluate_record(metrics, provenance):
    required = {"source_url", "data_permission", "model_version"}
    missing = sorted(required - provenance.keys())
    if missing or provenance.get("data_permission") != "synthetic-or-authorized":
        return {"status": "abstain", "missing": missing or ["authorized-data-status"]}
    return {"status": "review", "metrics": dict(metrics)}
```

### Developer Challenges

1. Reproducing the three-agent prompts, prototype-library construction, FLAME/keypoint mapping, Wan2.2 integration, and KTO refinement without an official implementation or checkpoint.
2. Designing evaluation that separates semantic-plan quality, keypoint quality, rendered eye control, identity preservation, and audio synchronization under matched compute and repeated seeds.
3. Building consent, licensing, provenance, and misuse controls that remain visible when a research prototype handles portraits, voices, and synthetic media.

### Author Challenges

1. Release a complete benchmark card for EMH, including source-dataset permissions, actor counts, identity splits, annotation procedures, and reproducible evaluation code.
2. Report user-study participant counts, annotator qualifications, agreement, randomization, uncertainty, significance testing, and the supplement details needed to interpret human evidence.
3. Provide public implementation and configuration artifacts, plus component-isolation studies that quantify the separate contributions of planning, composition, critic rules, dynamic CFG, and KTO.

## Validation Notes

- The source-integrity gate passed before synthesis: valid PDF and full-paper HTML; abstract HTML was treated as metadata only.
- The cache contract passed: `cached` public summary, local PDF and HTML text, `pypdf` fallback for unavailable `pdftotext`, and no source-text output.
- The live Black-Lake and Black-Lake-Data READMEs were read before artifact generation.
- Exactly three related DEP entries were selected from live repository content and each has a concrete overlap reason.
- The manuscript uses identical YAML `title` and H1 values no longer than 40 characters, all required schema headings, exactly three exercise paths, and the required random-selection, cache, and dedup/reselection records.
- Public-output review must confirm only generated Markdown and the derived dedup JSON are staged. PDFs, HTML, source archives, extracted text, cache files, local paths, and source records must remain unstaged and local.
- No source files were uploaded or attached; no `.source/` directory was created.

## Attribution Block

- Source URL: https://arxiv.org/abs/2605.28056
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Canonical public metadata and abstract record.
- Source URL: https://arxiv.org/html/2605.28056
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Full-paper method, benchmark, experiment, and conclusion evidence.
- Source URL: https://arxiv.org/pdf/2605.28056
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Printed tables, figures, training details, and paper-header evidence.
- Source URL: https://doi.org/10.48550/arXiv.2605.28056
  - Applies to: source identity fields.
  - Notes: ArXiv-issued DOI locator.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: repository layout, DEP class, attribution, and public-source policy.
  - Notes: Live repository authority read before writing.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related raw-data repository context and source-file policy.
  - Notes: Live related-repository authority read before writing.
