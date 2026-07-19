# Report-Mark: DoubleTransfer MEDIQA

## Report Context

- Report date: 2026-07-19
- Review type: source-first Arxiv DEP research review and implementation synthesis
- Selected paper: *DoubleTransfer at MEDIQA 2019: Multi-Source Transfer Learning for Natural Language Understanding in the Medical Domain*
- Canonical record: https://arxiv.org/abs/1906.04382v1
- Publication record: https://aclanthology.org/W19-5042/
- Review status: complete
- Source upload status: no source files uploaded; all paper documents and inspection material were withheld locally

## Selection and Deduplication

`rg --files -g "*.pdf"` found 75,778 PDFs and 75,776 unique PDF-parent paper units. A uniform PowerShell `Get-Random` draw over the sorted unit list selected zero-based index 34,844. The first draw was accepted with zero duplicate exclusions, zero other exclusions, and zero reselections.

The arXiv ID, arXiv DOI, ACL DOI, normalized title, and slug were checked across Black Lake logs, reports, lake data, staging, automation memory, and relevant Black-Lake-Data artifact paths. No prior Arxiv DEP artifact or same-paper marker within 24 hours was found. A metadata-only Black-Lake-Data author-inventory row was observed and retained as inventory provenance, not treated as a completed review deposit.

## Local Source-Integrity Result

The initial archive unit was `partial`: its 631,721-byte PDF was valid, but full-paper HTML and companion provenance records were missing. The PDF was preserved. ArXiv metadata HTML and the TeX/source package were collected. The official arXiv `/html/` endpoint returned 404 after three bounded attempts, so the approved ar5iv full-paper rendering was used.

Final verification passed before synthesis: PDF size, `%PDF-` header, and trailing `%%EOF`; HTML size 214,879 bytes; 31,992 body characters; a document marker; 30 heading/section markers; five paper-structure term classes; no error, conversion, abstract-only, or truncation notice; and no partial files. The local README, attribution record, CSV summary, and verification report were updated. No source document was copied into the public repository.

## Source Metadata

| Field | Value |
|---|---|
| Title | *DoubleTransfer at MEDIQA 2019: Multi-Source Transfer Learning for Natural Language Understanding in the Medical Domain* |
| Authors | Yichong Xu; Xiaodong Liu; Chunyuan Li; Hoifung Poon; Jianfeng Gao |
| arXiv | `1906.04382v1`, submitted 2019-06-11 |
| arXiv DOI | https://doi.org/10.48550/arXiv.1906.04382 |
| Venue | Proceedings of the 18th BioNLP Workshop and Shared Task, ACL, 2019, pages 399-405 |
| ACL DOI | https://doi.org/10.18653/v1/W19-5042 |
| Subject | Computation and Language (`cs.CL`) |
| Source package | Collected and inspected locally; withheld from public outputs |
| Component code | https://github.com/namisan/mt-dnn and https://github.com/allenai/scibert |
| Paper-specific code | Not available from inspected primary and official sources |

## Research Notes

### Problem

MEDIQA 2019 combined medical natural-language inference, recognizing question entailment, and question answering under limited in-domain data. DoubleTransfer asks whether two complementary pretrained sources can bridge that shortage: MT-DNN contributes broad NLU task knowledge, while SciBERT contributes a scientific-domain language representation.

### Mechanism

The system fine-tunes MT-DNN, knowledge-distilled MT-DNN, and SciBERT across MedNLI, RQE, QA, and MedQuAD, with MNLI used as an external general-domain NLI source. Algorithm 1 samples all in-domain mini-batches plus `floor(alpha * N)` external mini-batches, with `alpha = 0.5`, shuffles the mixture, and selects by development performance. The joint model is then fine-tuned per task. Classification uses cross-entropy; QA and MedQuAD use a regression score with mean-squared error.

The final system ensembles models from different initializations and data-mixture setups. For classification it takes a majority vote and breaks ties by summed prediction probabilities. For QA it combines sign votes and average scores, then ranks predicted-positive before predicted-negative answers.

### Main Results

- MedNLI: 91.7% development and 93.8% test accuracy; third on the reported leaderboard.
- RQE: 91.7% development and 66.2% test accuracy; seventh on the reported leaderboard, exposing substantial distribution shift or overfitting.
- QA: 78.0% accuracy and 81.91 precision, reported first for those metrics; MRR 0.937 and Spearman 0.238.
- Same-source three-model ensembles gain 1.44 points for MT-DNN (`88.26 -> 89.7`) and 1.50 points for SciBERT (`87.70 -> 89.2`) over their numerical average.
- Mixed-source ensembles gain 3.39 points for models `#1+#2+#5` (`88.21 -> 91.6`), 2.56 points for `#1+#5+#6` (`87.84 -> 90.4`), and 3.32 points for all six (`87.98 -> 91.3`).
- On MedNLI single-model development results, the strongest listed initialization is SciBERT with Ratio+MNLI at 89.4, versus 87.1 for the naive configuration.

### Evidence and Limits

The table evidence supports heterogeneous initialization as a useful ensemble ingredient in the tested setting. It does not isolate causality cleanly: ensemble membership, initialization, data mixtures, task-specific fine-tuning, and randomization all change together. One prose claim says both listed three-model mixed-source ensembles improve by more than 3%, but the table yields only 2.56 points for `#1+#5+#6`.

The RQE development/test gap is unusually large. The paper also describes shuffling half of evaluation data into training for its RQE development protocol and reconstructing the QA development set from LiveQAMed and Alexa questions. These interventions may be reasonable competition engineering, but they require split manifests and untouched holdouts before the reported development numbers can support generalization claims. No repeated seeds, confidence intervals, calibration, subgroup analysis, matched-compute comparison, or prospective clinical evaluation is reported.

### Implementation Relevance

The durable engineering pattern is not the 2019 stack itself. It is a controlled combination of complementary priors, bounded external-task sampling, task-specific heads, and heterogeneous ensemble diversity. A modern implementation should retain provenance for every training source, freeze patient/group splits before tuning, measure diversity and calibration rather than assuming they improve with more models, and require an abstention path for distribution shift.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Limitation |
|---|---|---|---|---|
| E1 | Verified 7-page PDF, full-paper HTML, and TeX source | Algorithm, datasets, hyperparameters, five tables, figure, results, and limitations | High for transcription | Experiments were not rerun |
| E2 | arXiv metadata record | Identity, v1 date, subject, arXiv DOI | High | Abstract alone does not support empirical claims |
| E3 | ACL Anthology record | Venue, pages, authors, ACL DOI, publication citation | High | Metadata does not independently reproduce results |
| E4 | MEDIQA overview | Shared-task scope and organizer-level task context | High | Aggregated competition context, not a DoubleTransfer ablation |
| E5 | MT-DNN and SciBERT repositories | Availability and lineage of component implementations | Medium-high | No paper-specific DoubleTransfer package was found |
| E6 | Exactly three related DEP manuscripts | Cross-artifact implementation and evaluation synthesis | Medium | Conceptual overlap does not validate the selected paper |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md`
   - Relevance: directly tests a heterogeneous-source fusion claim and records that fusion improves one label setting but degrades another, reinforcing the need for matched ablations and uncertainty rather than a blanket ensemble claim.
   - Source basis: full-paper review of arXiv:2006.08129v1, its audio/video architecture, Table 3, negative results, and paper-declared repository.
2. `.lake-data/DEP-E/DEP-E-20260718-Pixel Point Transfer/pixel_point_transfer_manuscript.md`
   - Relevance: provides a teacher-to-student transfer pattern with an explicit adapter and correspondence objective, while foregrounding domain shift, transferred bias, label scarcity, and the difference between mechanism evidence and universal transfer claims.
   - Source basis: full-paper/source review of arXiv:2104.04687v3, transfer equations, tables, supplement, and code-availability search.
3. `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md`
   - Relevance: shares the medical question-answering context and supplies stronger governance requirements for clinical data lineage, leakage controls, calibration, abstention, and non-diagnostic use.
   - Source basis: full-paper/source review of arXiv:2307.11986v2, PhysioNet records, official code repositories, dataset construction, and quantitative evaluation.

## Synthesis Note

### Concept Bridge

DoubleTransfer treats model initialization and task exposure as complementary evidence sources: general NLU competence, scientific-domain language, in-domain medical tasks, and external MNLI supervision are combined before a heterogeneous ensemble makes the final decision. AV Emotion Fusion shows why source diversity must be measured rather than assumed; Pixel-Point Transfer makes the adapter and transfer channel explicit; Medical Diff VQA shows that medical QA additionally needs governed data lineage and abstention. Together they define a practical transfer contract: declare what each source contributes, constrain how it enters training, measure incremental and interaction effects, and stop or defer when distribution fit or confidence fails.

### Potential Implementations

1. Build a transfer-source ledger that pins every pretrained model, task corpus, sampling weight, split lineage, license boundary, and downstream metric before training begins.
2. Build a heterogeneous-ensemble audit that compares same-source and mixed-source ensembles at matched size and compute, reporting diversity, calibration, worst-slice accuracy, and abstention behavior.
3. Build a medical NLU shift gate that monitors representation drift and confidence across institution, specialty, question type, and time, routing unsupported cases to human review.

### Deeper Relationship Observations

1. Complementarity is an interaction claim, not a count of sources: MT-DNN plus SciBERT, audio plus video, or image features plus point features only matter when matched ablations show unique predictive value.
2. Sampling and alignment are hidden transfer operators: DoubleTransfer's mixture ratio, Pixel-Point Transfer's geometric correspondence, and Medical Diff VQA's anatomy graph all determine what can be learned from the external source.
3. Domain adaptation can move bias as readily as capability, so every transfer pipeline needs source lineage, subgroup slices, drift tests, and a refusal boundary before deployment.

### Conceptual Similarities

1. All four artifacts combine heterogeneous representations or evidence channels instead of relying on one monolithic training source.
2. All four require an explicit interface between sources: batch sampling, feature fusion, correspondence projection, or anatomy-aware graph alignment.
3. All four show that aggregate accuracy is insufficient without negative evidence, slice-level analysis, and a boundary on generalization.

### MVP Implementations

1. **Bounded external-task sampler.** Preserve all in-domain batches and admit only an explicit fraction of external batches.

```python
from random import Random
from typing import Sequence, TypeVar

T = TypeVar("T")

def mixed_batches(in_domain: Sequence[T], external: Sequence[T],
                  alpha: float, seed: int) -> list[T]:
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must be in [0, 1]")
    rng = Random(seed)
    take = min(len(external), int(alpha * len(in_domain)))
    result = list(in_domain) + rng.sample(list(external), take)
    rng.shuffle(result)
    return result
```

2. **Vote with probability tie-break.** Reproduce the paper's classification rule with shape checks and deterministic ties.

```python
from collections import Counter

def vote_then_score(probabilities: list[list[float]]) -> int:
    if not probabilities or not probabilities[0]:
        raise ValueError("probabilities must be non-empty")
    width = len(probabilities[0])
    if any(len(row) != width for row in probabilities):
        raise ValueError("all models must share the class space")
    labels = [max(range(width), key=row.__getitem__) for row in probabilities]
    counts = Counter(labels)
    finalists = [label for label, count in counts.items()
                 if count == max(counts.values())]
    return max(finalists,
               key=lambda label: (sum(row[label] for row in probabilities),
                                  -label))
```

3. **Transfer evidence card.** Compare mixed and same-source systems without exposing sensitive examples.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class SliceResult:
    slice_name: str
    same_source_accuracy: float
    mixed_source_accuracy: float

def transfer_deltas(rows: list[SliceResult]) -> dict[str, float]:
    return {
        row.slice_name: round(
            row.mixed_source_accuracy - row.same_source_accuracy, 4
        )
        for row in rows
    }
```

### Developer Challenges

1. Reconstruct version-pinned 2019 data processing and model initialization without silently changing tokenization, task definitions, checkpoints, or evaluation semantics.
2. Enforce patient/group-disjoint split lineage and prevent task examples, paraphrases, or derivative records from crossing tuning and evaluation boundaries.
3. Measure ensemble diversity, calibration, latency, and worst-slice behavior at matched compute while keeping protected medical text local and auditable.

### Author Challenges

1. Release a paper-specific repository with frozen split manifests, model lists, checkpoints, seeds, environment pins, and commands that reproduce every table.
2. Isolate MT-DNN, MT-DNN-KD, SciBERT, MNLI sampling, multi-task training, task-specific fine-tuning, and ensemble composition with matched ablations and uncertainty intervals.
3. Validate on untouched external medical NLU datasets and report calibration, subgroup behavior, data-governance constraints, and abstention performance.

## Validation Notes

- Live Black Lake and Black-Lake-Data READMEs were inspected before drafting.
- Black Lake `.lake-data/README.md` filing and publication-index rules were inspected.
- The selected unit passed the mandatory PDF and full-paper HTML gates after bounded repair.
- The PDF, TeX source, Algorithm 1, Figure 1, and all five tables were inspected; synthesis was not based on the abstract alone.
- The ACL Anthology publication record, MEDIQA overview, and underlying MT-DNN/SciBERT repositories were inspected as primary or official context.
- Exactly three related DEP entries were inspected and recorded.
- The Synthesis Note contains one Concept Bridge, three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP implementations with code mock-ups, three developer challenges, and three author challenges.
- The required log contains exactly three next-review questions and exactly three challenges.
- Public artifacts use date-only markers and contain no local absolute path, drive path, username, machine name, workspace root, local timezone label, or exact local execution timestamp.
- No `.source/` directory was created. No PDF, HTML, source archive, extracted text, cache, verification record, or rendered page is included in the public change.

## Attribution Block

- Source URL: https://arxiv.org/abs/1906.04382v1
  - Applies to: source identity, version history, subject, and arXiv DOI.
  - Notes: Canonical arXiv metadata record.
- Source URL: https://arxiv.org/pdf/1906.04382
  - Applies to: full method, algorithm, figure, tables, results, limitations, and references.
  - Notes: Verified 7-page PDF inspected locally; no PDF uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/1906.04382
  - Applies to: full-paper structure and searchable cross-checks.
  - Notes: Approved fallback used after official arXiv HTML returned 404; no HTML uploaded.
- Source URL: https://arxiv.org/e-print/1906.04382
  - Applies to: TeX source, table arithmetic, algorithm text, and implementation details.
  - Notes: Source package inspected locally and withheld.
- Source URL: https://doi.org/10.48550/arXiv.1906.04382
  - Applies to: persistent arXiv identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://aclanthology.org/W19-5042/
  - Applies to: publication venue, pages, authors, citation, and ACL DOI.
  - Notes: Official ACL Anthology record.
- Source URL: https://doi.org/10.18653/v1/W19-5042
  - Applies to: persistent ACL publication identity.
  - Notes: Publisher DOI resolved through the ACL Anthology record.
- Source URL: https://aclanthology.org/W19-5039/
  - Applies to: organizer-level MEDIQA task and competition context.
  - Notes: Official MEDIQA 2019 shared-task overview.
- Source URL: https://aclanthology.org/D18-1187/
  - Applies to: MedNLI identity and clinical-domain transfer background.
  - Notes: Official ACL Anthology record for the MedNLI paper.
- Source URL: https://github.com/namisan/mt-dnn
  - Applies to: MT-DNN component implementation and historical version boundary.
  - Notes: Component repository; no paper-specific DoubleTransfer workflow was identified.
- Source URL: https://github.com/allenai/scibert
  - Applies to: SciBERT model and implementation context.
  - Notes: Component repository; no paper-specific DoubleTransfer workflow was identified.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md
  - Applies to: heterogeneous fusion evidence and matched-ablation design.
  - Notes: Related DEP entry; primary basis arXiv:2006.08129v1.
- Source URL: https://arxiv.org/abs/2006.08129
  - Applies to: primary source basis recorded by the AV Emotion Fusion DEP.
  - Notes: Related-paper locator; the current review relied on the inspected DEP for synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md
  - Applies to: teacher/student transfer, adapters, domain shift, and transferred-bias controls.
  - Notes: Related DEP entry; primary basis arXiv:2104.04687v3.
- Source URL: https://arxiv.org/abs/2104.04687v3
  - Applies to: primary source basis recorded by the Pixel-Point Transfer DEP.
  - Notes: Related-paper locator; the current review relied on the inspected DEP for synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA/medical_diff_vqa_manuscript.md
  - Applies to: medical QA governance, leakage, calibration, and abstention.
  - Notes: Related DEP entry; primary basis arXiv:2307.11986v2.
- Source URL: https://arxiv.org/abs/2307.11986v2
  - Applies to: primary source basis recorded by the Medical Diff VQA DEP.
  - Notes: Related-paper locator; the current review relied on the inspected DEP for synthesis.
