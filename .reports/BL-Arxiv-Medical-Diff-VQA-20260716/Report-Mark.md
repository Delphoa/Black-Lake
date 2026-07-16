# Report-Mark: Medical Diff VQA

Public run date: 2026-07-16

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Expert Knowledge-Aware Image Difference Graph Representation Learning for Difference-Aware Medical Visual Question Answering* |
| Authors | Xinyue Hu; Lin Gu; Qiyuan An; Mengliang Zhang; Liangchen Liu; Kazuma Kobayashi; Tatsuya Harada; Ronald M. Summers; Yingying Zhu |
| Stable identifiers | arXiv:2307.11986v2; DOI:10.1145/3580305.3599819 |
| Publication context | Submitted 2023-07-22, revised 2024-08-27; KDD 2023, pages 4156-4165 |
| Current dataset record | Medical-Diff-VQA v1.0.1; DOI:10.13026/e6dd-cn74; credentialed PhysioNet access |
| Subject | Longitudinal chest-X-ray difference visual question answering with anatomy-aware, expert-knowledge graph representations |
| Source state | Verified complete local PDF and full-paper HTML; metadata HTML and TeX/source package also retained locally |
| Distribution | Generated Markdown only; all original and extracted source files withheld locally |

## Concise Research Notes

- **Problem:** Conventional medical VQA usually answers from one image, while radiology often compares a current study with an earlier study. Subtle pathology changes can be smaller than pose, projection, scale, and nonrigid anatomical variation, making direct pixel/patch comparison brittle.
- **Dataset:** Medical-Diff-VQA contains 700,703 QA pairs from 164,324 present/reference image pairs and seven categories: abnormality, presence, view, location, type, level, and difference. Earlier visits are references and later visits are main images.
- **Construction:** An Extract-Check-Fix loop builds keyword libraries, extracts abnormalities/attributes/negations from MIMIC-CXR reports into KeyInfo records, checks them with manual and automated signals, and generates QA pairs. Three verifiers labeled 1,657 of 1,700 sampled pairs correct; the table reports 97.4% and prose 97.33%.
- **Method:** Faster R-CNN models provide 26 anatomical regions and disease features. Question-conditioned anatomical/disease nodes are linked by spatial, semantic, and implicit relations. Relation-aware graph attention builds each image representation; an image-difference representation conditions answer generation.
- **Results:** On six non-difference types, total exact-match accuracy is 60.2 versus 54.7 for MMQ; closed questions improve to 84.9 versus 74.2, while open questions fall to 36.6 versus 40.5. On difference questions, the proposed method leads MCCFormers and IDCPCL on six of seven listed metrics; IDCPCL has slightly higher ROUGE-L (0.582 versus 0.577).
- **Ablation caution:** The full graph leads or ties BLEU-2/3/4, but implicit-only is higher on BLEU-1, ROUGE-L, and CIDEr, and semantic-only is higher on METEOR. The evidence does not support an unqualified claim that combining all relations is always best.
- **Limitations:** No external-site or prospective clinical evaluation, calibration, abstention, subgroup analysis, patient-leakage audit, repeated-seed uncertainty, or causal faithfulness test is reported. Targets inherit report/rule biases. The source discloses limits on multi-location disease representation and errors from synonyms, similar presentations, and detector features.
- **Implementation relevance:** The transferable pattern is anatomy-indexed comparison plus explicit relation types and an auditable change ledger. A safe implementation should remain retrospective and non-diagnostic, expose uncertainty and omissions, and treat saliency as an inspection aid rather than proof.
- **Source availability:** Current official PhysioNet and GitHub records improve inspectability, but credentialed data, legacy dependencies, checkpoints, missing license evidence, and unexecuted code prevent a reproduction claim.

## Evidence and Attribution

| ID | Evidence inspected | Supports | Assessment |
|---|---|---|---|
| E1 | Complete paper PDF, official full-paper HTML, and TeX/source package | Task, construction, architecture, equations, tables, error discussion, conclusion | High confidence for faithful source reporting; experiments not rerun |
| E2 | Canonical arXiv and DOI metadata | Title, authors, versions, venue, persistent identifiers | High |
| E3 | Medical-Diff-VQA v1.0.1 and MIMIC-CXR v2.1.0 PhysioNet records | Current dataset naming/version, counts, source provenance, credentialed access, DUA and ethics boundary | High for official records; datasets not downloaded |
| E4 | Official Medical-Diff-VQA and EKAID GitHub READMEs | Generation, feature extraction, training, testing, checkpoints, dependency and UI requirements | Medium-high; code and checkpoints not executed |
| E5 | Local integrity and process records | Random selection, dedup, initial partial state, successful repair, structural completeness | High; local locations and files intentionally withheld |
| E6 | Three related DEP manuscripts and their source bases | Cross-DEP concept bridge and safe implementation patterns | Medium; synthesis context does not validate this paper |

Author claims are labeled as such in the manuscript. Numerical results are transcribed from the primary paper and current official records, not reproduced measurements. Clinical/product implications and cross-DEP relationships below are reviewer interpretations.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` — selected because VALUE tests where multimodal fusion, modality preference, coreference, and visual relations appear, while warning that probe accuracy and attention do not establish causal use. Source basis: arXiv:2005.07310 and DOI:10.1007/978-3-030-58539-6_34.
2. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` — selected because it treats visual hallucination, object coverage, and grounding as joint evaluation problems; these are direct failure modes for medical VQA answers that can look precise by omitting evidence. Source basis: arXiv:2505.15963.
3. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` — selected because it evaluates paired visual representations for geometry consistency beyond surface appearance, paralleling the need to separate true longitudinal change from view/alignment variation. Source basis: arXiv:2606.14162.

## Synthesis Note

### Concept Bridge

The four artifacts describe one evidence pipeline. Medical Diff VQA assigns anatomy and clinical relations to two observations before computing change. VLM Probing asks whether a multimodal model actually encodes and uses those relations or merely exposes them to a linear probe. OViP adds a precision-versus-coverage test: a model can reduce apparent hallucination by saying less, which is especially dangerous when omitted findings are clinically important. VideoWeave shows that paired visual outputs require structural consistency measures beyond appearance quality. Together they imply a longitudinal evidence contract with five gates: pair provenance, anatomy/geometry correspondence, relation-use tests, answer correctness plus coverage, and calibrated human review.

### Potential Implementations

1. **Retrospective longitudinal audit workbench:** Accept an approved current/reference pair and candidate answer, verify pair chronology and split isolation, attach anatomy-indexed evidence, calculate change/coverage/contradiction metrics, and route uncertainty to a qualified reviewer. It must not diagnose or write reports autonomously.
2. **Difference-VQA data quality gate:** Capture rule provenance for every QA pair, normalize synonyms and negation, detect templating and patient leakage, stratify human review by question/severity, and publish only aggregate quality findings.
3. **Multimodal relation stress harness:** Swap references, remove a modality, mask regions, corrupt graph edges, and perturb registration on synthetic or governed test pairs; report which answers change and whether the change follows the relevant evidence.

### Deeper Relationship Observations

1. Anatomy and geometry play the same systems role: they create a correspondence coordinate system so that change is measured between like entities rather than raw pixels or latent patches.
2. Relation visibility is not relation use. A graph edge, attention map, or decodable feature can be present without causally affecting the answer; controlled interventions are required.
3. Reliability requires both precision and coverage. A system that avoids false statements by omitting subtle progression can improve naive hallucination metrics while becoming less clinically useful.

### Conceptual Similarities

1. Each entry decomposes a multimodal output into intermediate structures that can be audited instead of relying only on end-task quality.
2. Each entry distinguishes explicit structure from learned implicit representation: clinical/spatial graph edges, latent relation probes, on-policy visual negatives, or implicit geometry latents.
3. Each entry needs counterfactual evaluation—reference swaps, mismatched captions, synthetic negatives, or geometry perturbations—to test whether the intended evidence controls the output.

### MVP Implementations with Code Mock-Ups

1. **Pair-integrity validator:** reject temporal pairs that violate the expected patient/split/chronology contract before any model evaluation.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Study:
    patient_key: str
    study_key: str
    ordinal: int
    split: str

def validate_pair(reference: Study, current: Study) -> dict:
    checks = {
        "same_patient": reference.patient_key == current.patient_key,
        "different_study": reference.study_key != current.study_key,
        "chronological": reference.ordinal < current.ordinal,
        "same_split": reference.split == current.split,
    }
    return {"accepted": all(checks.values()), "checks": checks}
```

Use only opaque, approved identifiers inside a governed environment. Do not export patient/study keys in public artifacts.

2. **Grounding-and-coverage scorer:** keep factual precision and expected-concept coverage separate so silence cannot masquerade as reliability.

```python
def grounding_card(predicted, expected, supported):
    predicted = set(predicted)
    expected = set(expected)
    supported = set(supported)
    grounded = predicted & supported
    precision = len(grounded) / max(1, len(predicted))
    coverage = len(predicted & expected) / max(1, len(expected))
    unsupported = sorted(predicted - supported)
    omitted = sorted(expected - predicted)
    return {
        "precision": round(precision, 4),
        "coverage": round(coverage, 4),
        "unsupported": unsupported,
        "omitted": omitted,
    }
```

Concept sets must come from an approved ontology/reviewer process; this toy scorer is not a clinical metric.

3. **Relation-intervention schedule:** generate bounded audit cases that test one relation family at a time.

```python
def intervention_plan(relation_types=("spatial", "semantic", "implicit")):
    plan = [{"case": "baseline", "remove": []}]
    for relation in relation_types:
        plan.append({"case": f"remove_{relation}", "remove": [relation]})
    plan.append({"case": "question_only", "remove": ["reference", "current"]})
    plan.append({"case": "reference_swap", "remove": [], "swap_reference": True})
    return plan
```

Run this only on synthetic/public examples or authorized retrospective data; pair it with fixed seeds and a predeclared metric set.

### Developer Challenges

1. Reconstructing a reproducible pipeline across credentialed datasets, multiple detector checkpoints, legacy Python dependencies, feature HDF5 files, graph training, and evaluation artifacts without leaking clinical data.
2. Implementing patient-level split guarantees, pair chronology, synonym/negation normalization, and export allowlists as verifiable code rather than documentation promises.
3. Designing perturbation and grounding metrics that expose shortcuts while remaining deterministic, clinically interpretable, and cheap enough for regression testing.

### Author Challenges

1. Demonstrate external-site, device, projection, subgroup, and prospective generalization with clinically weighted outcomes, calibration, abstention, and qualified review.
2. Resolve the mixed graph ablation with repeated seeds, uncertainty intervals, per-question analyses, edge corruption, and causal relation-use tests.
3. Publish a pinned, licensed, end-to-end reproduction manifest covering code, data versions, checkpoints, environments, split checks, expected hashes, and benchmark outputs.

## Validation Notes

- Random selection used a uniform zero-based index over 75,537 eligible parent-directory units after `rg --files -g "*.pdf"` enumeration and dedup filtering; selected index 32,396; no reselection.
- Dedup scanned Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data `.lake-data`/`.reports`. It observed 446 used arXiv IDs, excluded 54 units by used ID, withheld 185 identifier-incomplete units, and found no matching ID/title/slug for arXiv:2307.11986.
- The public-safe 24-hour cutoff date was 2026-07-15; no same-paper marker was found on or after it.
- Source state was initially `partial` because full-paper HTML was missing. The valid PDF was preserved; official HTML, metadata HTML, and source archive were repaired locally with bounded direct-HTTPS attempts.
- Final source verification passed: PDF 10,107,164 bytes with `%PDF-` and trailing `%%EOF`; full-paper HTML 204,036 bytes with 60,080 body characters, a document marker, 60 headings, and eight structure terms; zero partial files.
- The manuscript title and H1 are identical and under 40 characters. All required manuscript sections are present; `## Three Ways to Exercise This Research` has exactly three entries.
- This Report-Mark contains one concept bridge and exactly three entries in each required synthesis group. The three code blocks use only standard Python syntax and synthetic/opaque identifiers.
- No source file was copied into the repository. The public package contains generated Markdown only and no `.source/` directory.
- Code, datasets, checkpoints, and experiments were not executed. Metrics remain source-reported, not reproduced.

## Attribution Block

- Source URL: https://arxiv.org/abs/2307.11986
  - Applies to: `Report-Mark.md`
  - Notes: Canonical metadata, abstract, version history, DOI, and public source locators.
- Source URL: https://arxiv.org/pdf/2307.11986
  - Applies to: `Report-Mark.md`
  - Notes: Public equivalent of the complete PDF inspected locally; file not redistributed.
- Source URL: https://arxiv.org/html/2307.11986
  - Applies to: `Report-Mark.md`
  - Notes: Official full-paper rendering used for section and result cross-checks; file not redistributed.
- Source URL: https://arxiv.org/e-print/2307.11986
  - Applies to: `Report-Mark.md`
  - Notes: Local TeX/source evidence used to verify table values and limitations; file not redistributed.
- Source URL: https://doi.org/10.1145/3580305.3599819
  - Applies to: `Report-Mark.md`
  - Notes: Persistent KDD publication identifier.
- Source URL: https://physionet.org/content/medical-diff-vqa/1.0.1/
  - Applies to: `Report-Mark.md`
  - Notes: Current official dataset record, counts, construction notes, access classification, and citation.
- Source URL: https://physionet.org/content/mimic-cxr/2.1.0/
  - Applies to: `Report-Mark.md`
  - Notes: Official source-dataset provenance, de-identification, DUA, and ethics record.
- Source URL: https://github.com/Holipori/MIMIC-Diff-VQA
  - Applies to: `Report-Mark.md`
  - Notes: Official dataset-generation repository; code not run.
- Source URL: https://github.com/Holipori/EKAID
  - Applies to: `Report-Mark.md`
  - Notes: Official feature/model repository at observed main commit `1e5dd0de91554515d2acc83ad402e810ace0a5d7`; code not run.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `Report-Mark.md`
  - Notes: Live repository authority for logs, reports, DEP contents, source withholding, attribution, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `Report-Mark.md`
  - Notes: Live DEP-E filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `Report-Mark.md`
  - Notes: Live companion-repository authority used for dedup context.
- Repository file: `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md
  - Applies to: `Report-Mark.md`
  - Notes: Related multimodal probing and relation-evidence synthesis; source basis arXiv:2005.07310.
- Repository file: `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md
  - Applies to: `Report-Mark.md`
  - Notes: Related visual grounding, hallucination, and coverage synthesis; source basis arXiv:2505.15963.
- Repository file: `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: `Report-Mark.md`
  - Notes: Related paired-visual geometry consistency synthesis; source basis arXiv:2606.14162.
