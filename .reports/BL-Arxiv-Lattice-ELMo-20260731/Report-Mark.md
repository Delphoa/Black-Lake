# Report-Mark: Lattice Spoken LM

- Public-safe review date: `2026-07-31`
- Review type: Randomized source-first arXiv DEP-E review
- Primary subject: *Learning Spoken Language Representations with Neural Lattice Language Modeling*
- Source-file policy: Complete source evidence was inspected locally and withheld; no source file is included in this report or DEP.

## Source Metadata

| Field | Value |
|---|---|
| Title | *Learning Spoken Language Representations with Neural Lattice Language Modeling* |
| Authors | Chao-Wei Huang; Yun-Nung Chen |
| arXiv | `2007.02629v2` |
| arXiv record | https://arxiv.org/abs/2007.02629 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2007.02629 |
| ACL record | https://aclanthology.org/2020.acl-main.347/ |
| ACL DOI | https://doi.org/10.18653/v1/2020.acl-main.347 |
| Submitted / revised | 2020-07-06 / 2020-11-02 |
| Venue | ACL 2020 short paper, pages 3764-3769 |
| Subjects | Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`) |
| Complete evidence | Verified six-page PDF, verified full-paper HTML fallback, metadata HTML, and six rendered pages |
| Implementation | Official MiuLab repository inspected at commit `202e369c0d41ff4e62353073478d25fec4b18cca`; code not run |
| Redistribution | All source, cache, receipt, render, and verification files withheld locally |

### Selection Record

- Enumeration: required `rg --files -g "*.pdf"` over the local archive.
- PDF candidates: `75,960`.
- Unique PDF-parent units: `75,957`.
- Used arXiv base IDs observed: `1,690`.
- Units excluded by used ID: `476`.
- Identifier-incomplete units withheld: `185`.
- Eligible units before recent-marker rejection: `75,296`.
- Uniform method: PowerShell `Get-Random` over the eligible array, with rejection reserved for recent same-unit markers.
- Selected zero-based eligible index: `21,552`.
- Accepted identity: arXiv `2007.02629v2`.
- Duplicate and recent-marker rejections/reselections: `0`.

### Dedup Record

- Scopes: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; fetched Black-Lake-Data `.logs`, `.reports`, `.lake-data`, and `.staging`.
- Keys: arXiv ID, arXiv DOI, ACL DOI, canonical and normalized title, implementation token, and planned slugs.
- Exact ID/title/DOI/slug searches: no prior deposit or same-paper marker.
- Public-safe 24-hour cutoff date: `2026-07-30`.
- Same-paper recent markers: none before acceptance.

### Source Integrity Record

- Initial state: `partial`; a plausible PDF was present and full-paper HTML was absent.
- Repair: review paused; the valid PDF was preserved; the pinned publisher broker fetched metadata, attempted official HTML routes, accepted the approved ar5iv fallback, and made one bounded source-package attempt.
- PDF: `879,903` bytes; `%PDF-` header; trailing `%%EOF`; six unencrypted pages.
- Full-paper HTML: `161,386` bytes; `30,357` stripped body characters; LaTeXML document marker; `35` heading markers; six structure terms.
- Metadata HTML: `41,604` bytes.
- Source archive: unavailable after the bounded attempt.
- Unexpected partial files: `0`.
- Final state: `complete`.
- Local companion records: README, provenance record, machine-readable summary, acquisition receipt, and verification report updated.

## Concise Research Notes

### Research Question

Can language-model pretraining be transferred from ordinary sequential text to automatic-speech-recognition lattices so downstream spoken-language classifiers retain alternate recognition hypotheses instead of collapsing uncertainty to a single transcript?

### Core Method

The paper represents each ASR lattice as an edge-labeled directed acyclic graph. A LatticeRNN processes edges in topological order, and each node pools incoming hidden states using ASR transition probabilities. The language-model target at a node is the distribution over its outgoing word-labeled transitions. Training minimizes KL divergence between that posterior-derived target and a softmax decoder.

The model is trained in two stages:

1. pretrain a bidirectional sequential LSTM language model on general written text using the ELMo cell architecture; and
2. initialize a bidirectional LatticeLSTM from those weights, then continue pretraining on target-task lattices with the lattice language-model objective.

For downstream classification, the pretrained lattice LM is frozen. Its layers are combined into contextualized node embeddings consumed by a newly trained two-layer LatticeLSTM, max pooling, a linear layer, and softmax.

### Source-Reported Evidence

The experiments cover intent detection on ATIS and synthetic-spoken SNIPS, plus dialogue-act recognition on SWDA and MRDA. Overall classification accuracy is reported, averaged over at least three training runs.

| Input / model | ATIS | SNIPS | SWDA | MRDA |
|---|---:|---:|---:|---:|
| ASR 1-best + ELMo | 94.99 | 91.98 | 61.65 | 68.52 |
| ASR 1-best + BERT-base | 95.97 | 93.29 | 61.23 | 67.90 |
| Lattice biLatticeLSTM | 91.69 | 93.43 | 61.29 | 69.95 |
| Proposed two-stage lattice LM | 95.84 | 95.37 | 62.88 | 72.04 |
| Proposed without Stage 1 | 94.65 | 95.19 | 61.81 | 71.71 |
| Proposed without Stage 2 | 95.35 | 94.58 | 62.41 | 71.66 |
| Proposed evaluated on 1-best | 95.05 | 92.40 | 61.12 | 68.04 |

The authors report relative error reduction from `3.2%` to `42%` versus the ASR 1-best biLSTM+ELMo baseline. The proposed method is best among ASR-output systems on SNIPS, SWDA, and MRDA, while BERT-base is `0.13` accuracy points higher on ATIS. Removing either pretraining stage lowers accuracy on all four datasets in the displayed ablation.

Dataset scale and ASR difficulty vary materially:

| Dataset | Train | Validation | Test | Classes | WER | Oracle WER |
|---|---:|---:|---:|---:|---:|---:|
| ATIS | 4,478 | 500 | 869 | 22 | 15.55 | 9.19 |
| SNIPS | 13,084 | 700 | 700 | 7 | 45.61 | 18.79 |
| SWDA | 103,326 | 8,989 | 15,927 | 43 | 28.41 | 17.15 |
| MRDA | 73,588 | 15,037 | 14,800 | 5 | 32.04 | 21.53 |

### Evidence Limits

- The paper says results average at least three runs but does not report standard deviations, confidence intervals, paired tests, seeds, or per-example outcomes.
- The strongest claim is classification accuracy under four historical pipelines, not modern ASR or end-to-end speech-model performance.
- SNIPS speech is generated by a commercial text-to-speech system; this does not establish robustness to natural speaker, accent, channel, or acoustic variation.
- ATIS manual and ASR test sets differ because audio is missing, limiting manual-versus-ASR comparison.
- Best-validation checkpoint selection is described, but the number of candidate checkpoints and selection sensitivity are not reported.
- The paper argues that two-stage training reduces lattice-data demand and improves efficiency, but supplies no runtime, compute, energy, data-volume, or cost comparison.
- The official repository provides a processed SNIPS route but says ATIS, SWDA, and MRDA cannot be redistributed. No visible repository license was established, and the code was not executed.
- Current portability to transformer, transducer, CTC, neural-codec, or streaming-ASR systems is not demonstrated.

### Reviewer Interpretation

The durable contribution is not ELMo itself. It is the **representation-preserving transfer pattern**: pretrain on a cheap degenerate case, lift the weights into a richer graph-structured model, adapt on scarce structured observations, and retain the richer structure at inference. The paper provides useful evidence that discarding ASR alternatives can lose downstream information. It does not establish that posterior-weighted lattice pooling is calibrated, that every alternate hypothesis is beneficial, or that the same gains survive current model families.

## Evidence and Attribution

| ID | Evidence | Source | Supports | Boundary |
|---|---|---|---|---|
| E1 | Canonical identity, authors, dates, version, subjects, arXiv DOI | https://arxiv.org/abs/2007.02629 | Metadata | Abstract is not full-paper evidence. |
| E2 | Complete method, figures, tables, ablations, conclusion, and references | https://arxiv.org/pdf/2007.02629 | Method and results | Local PDF withheld; no experiment rerun. |
| E3 | Searchable complete-paper rendering | https://ar5iv.labs.arxiv.org/html/2007.02629 | Section and quantitative cross-checks | Approved fallback; local HTML withheld. |
| E4 | ACL venue, pagination, publisher DOI, and publication license context | https://aclanthology.org/2020.acl-main.347/ | Publication status | Venue metadata does not validate results. |
| E5 | Persistent ACL publication identity | https://doi.org/10.18653/v1/2020.acl-main.347 | DOI identity | Resolver is not result evidence. |
| E6 | Official code layout, dataset restrictions, and run commands | https://github.com/MiuLab/Lattice-ELMo | Implementation availability | Repository not executed; no license file established. |
| E7 | Visual inspection of all six pages, including Figures 1-2 and Tables 1-2 | https://arxiv.org/pdf/2007.02629 | Layout, diagram, and table agreement | No plot digitization or reproduction. |
| E8 | Private selection, repair, and validation records | Withheld local context | Eligibility and completeness | No local identity disclosed. |

Every quantitative statement above is transcribed from the complete paper or computed directly from displayed accuracies and labeled as reviewer interpretation. No secondary summary is used as primary technical evidence.

## Related DEP Entries

| Related entry | Concrete overlap | Source basis |
|---|---|---|
| `.lake-data/DEP-A/DEP-A-20260731-Ontology ASR Correction/2606.13464-whitepaper-review.md` | Both treat a 1-best transcript as an information bottleneck. The lattice LM preserves alternate hypotheses before classification; the ontology-memory system revises hypotheses after recognition using structured conversational evidence and explicit fallback needs. | Inspected the entry's architecture, direct/full-history baselines, correction evidence, failure boundary, and reversible correction proposal. |
| `.lake-data/DEP-E/DEP-E-20260720-Cued Speech MLLM/cued_speech_mllm_manuscript.md` | Both fuse structured evidence with a language representation to mitigate ambiguity and limited labeled data. Cued Speech supplies hand and lip evidence; the lattice LM supplies posterior-weighted ASR paths. | Inspected source metadata, keyframe/support-set mechanism, fusion architecture, dataset scale, CER/WER evidence, ablations, and governance limits. |
| `.lake-data/DEP-A/DEP-A-20260720-HeadRouter Audio/2604.23717-whitepaper-review.md` | Both make representation selection task-aware and argue for efficiency. The lattice LM keeps graph paths through staged transfer; HeadRouter selects audio tokens through routed attention heads and exposes a measurable cost-quality frontier. | Inspected head-routing mechanism, benchmark/model scope, retention evidence, ASR exception, cost accounting, and uncertainty/fallback proposal. |

These entries are conceptual and implementation bridges only. None independently reproduces or validates the 2020 lattice-language-model results.

## Synthesis Note

### Concept Bridge

The four artifacts describe successive places where speech uncertainty can be preserved, transformed, or lost:

`audio evidence -> recognition alternatives -> contextual representation -> correction memory -> downstream decision`.

The selected paper acts at the recognition-alternative and contextual-representation boundary. Cued Speech adds complementary visual evidence before recognition. Ontology ASR Correction adds structured history after recognition. HeadRouter Audio changes which acoustic tokens reach a large audio-language model. The shared engineering question is not merely "which model is larger?" It is **which uncertain evidence survives each interface, with what calibration, cost, provenance, and reversible fallback**.

### Potential Implementations

1. **Posterior-preserving SLU gateway.** Convert an authorized ASR n-best graph into a normalized lattice receipt, compute 1-best and lattice-aware predictions side by side, and surface disagreement, entropy, latency, and fallback reason.
2. **Evidence-fusion correction sandbox.** Combine lattice alternatives with an immutable ontology-memory snapshot and optional visual cues, but preserve the raw transcript and require calibrated support before applying a correction.
3. **Representation budget evaluator.** Sweep lattice beam size, posterior pruning, audio-token retention, and downstream accuracy under matched hardware, reporting the full cost-quality-calibration frontier rather than one operating point.

### Deeper Relationship Observations

1. **A lattice is both data and uncertainty policy.** Arc posteriors determine which alternatives influence a node representation; miscalibrated ASR probabilities can therefore become representation bias even when the graph is structurally complete.
2. **Staged transfer is a special-to-general lifting operator.** A sequence is a degenerate lattice, so sequential pretraining initializes a graph model without pretending general text already supplies spoken uncertainty.
3. **Correction and pruning need the same receipt.** Whether a system adds context, rewrites words, or removes audio tokens, it should record the source evidence, decision rule, achieved budget, downstream effect, and fallback.

### Conceptual Similarities

1. **Lattice LM and Ontology ASR Correction:** both reject raw 1-best text as a sufficient representation and introduce structured context around recognition errors.
2. **Lattice LM and Cued Speech MLLM:** both combine multiple weighted evidence paths before a language decision and depend on careful missing-modality or low-confidence behavior.
3. **Lattice LM and HeadRouter Audio:** both seek efficient task-relevant representations, but neither architectural efficiency claim substitutes for end-to-end cost measurement.

### MVP Implementations with Code Mock-Ups

1. **Posterior-weighted node pooling.**

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class ArcState:
    posterior: float
    hidden: tuple[float, ...]


def weighted_pool(arcs: tuple[ArcState, ...]) -> tuple[float, ...]:
    if not arcs:
        raise ValueError("a lattice node needs at least one incoming arc")
    width = len(arcs[0].hidden)
    if any(len(arc.hidden) != width for arc in arcs):
        raise ValueError("hidden-state widths must match")
    total = sum(arc.posterior for arc in arcs)
    if not 0.99 <= total <= 1.01:
        raise ValueError("incoming posteriors are not normalized")
    return tuple(
        sum(arc.posterior * arc.hidden[i] for arc in arcs) / total
        for i in range(width)
    )
```

2. **Immutable staged-transfer receipt.**

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class TransferReceipt:
    sequential_model: str
    lattice_data: str
    evaluation_split: str
    frozen_encoder: bool


def make_receipt(model_hash: str, lattice_hash: str, split_hash: str) -> TransferReceipt:
    if len({model_hash, lattice_hash, split_hash}) != 3:
        raise ValueError("model, adaptation data, and evaluation split must be distinct")
    return TransferReceipt(model_hash, lattice_hash, split_hash, frozen_encoder=True)
```

3. **Matched-baseline error reduction.**

```python
def relative_error_reduction(
    baseline_accuracy: float,
    candidate_accuracy: float,
) -> float:
    if not 0.0 <= baseline_accuracy < 100.0:
        raise ValueError("baseline accuracy must be in [0, 100)")
    if not 0.0 <= candidate_accuracy <= 100.0:
        raise ValueError("candidate accuracy must be in [0, 100]")
    baseline_error = 100.0 - baseline_accuracy
    candidate_error = 100.0 - candidate_accuracy
    return 100.0 * (baseline_error - candidate_error) / baseline_error


assert round(relative_error_reduction(91.98, 95.37), 1) == 42.3
```

### Developer Challenges

1. **Graph normalization and batching.** Real lattices contain pruning artifacts, duplicated labels, dead ends, posterior underflow, and variable topology; a robust runtime needs validation, deterministic ordering, padding/batching policy, and conservative fallback.
2. **Reproducible dependency recovery.** The official implementation targets an older Python/ELMo stack and restricted datasets. Porting it requires environment pinning, data-rights review, reference outputs, and differential tests before modernization.
3. **Metric and operations alignment.** Accuracy alone hides calibration, tail latency, memory growth, beam-size cost, and catastrophic corrections. Telemetry must join the exact lattice and model versions to both the 1-best and lattice-aware outcomes.

### Author Challenges

1. **Demonstrate the efficiency claim.** Report sequential and lattice pretraining data volumes, wall time, compute, memory, convergence, and matched-quality comparisons rather than relying only on architectural plausibility.
2. **Quantify uncertainty.** Publish seeds, per-run outcomes, confidence intervals or paired tests, calibration of arc posteriors, and per-utterance gains/losses across WER, lattice density, and dataset slices.
3. **Strengthen artifact portability.** Provide an explicit code license, versioned environment, legal acquisition instructions for restricted corpora, immutable configurations, and reference hashes for reproduced tables.

## Validation Notes

- The complete-paper gate passed before synthesis; an abstract-only page was never treated as the paper.
- Random selection used the required `rg` enumeration and a recorded uniform `Get-Random` draw.
- Repository-wide and memory dedup checks found no same-paper log, report, DEP, DOI, title, or recent marker.
- Exactly three related DEP entries were inspected and recorded with concrete source basis.
- All six PDF pages were visually inspected; the full-paper HTML was independently validated for size, body text, document marker, headings, and structure terms.
- The official code repository was verified and commit-pinned, but no code, model, or experiment was run.
- All result claims remain source-reported unless explicitly labeled as reviewer computation or interpretation.
- No PDF, HTML, metadata page, source archive, cache, extracted text, receipt, render, or verification file is included in the repository.
- No `.source/` directory was created.
- Public artifacts use repository-relative paths and public URLs only; local filesystem identity, machine identity, timezone, and exact execution time are withheld.

## Attribution Block

- Source URL: https://arxiv.org/abs/2007.02629
  - Applies to: canonical identity, authors, dates, version history, subjects, abstract context, and arXiv DOI.
  - Notes: Metadata only; not treated as the full paper.
- Source URL: https://arxiv.org/pdf/2007.02629
  - Applies to: complete method, figures, tables, ablations, conclusion, references, and visual review.
  - Notes: Verified source file inspected locally and withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/2007.02629
  - Applies to: searchable full-paper verification and quantitative cross-checks.
  - Notes: Approved full-paper fallback; verified local copy withheld.
- Source URL: https://arxiv.org/e-print/2007.02629
  - Applies to: bounded source-package availability check.
  - Notes: Source package was unavailable after the bounded attempt.
- Source URL: https://doi.org/10.48550/arXiv.2007.02629
  - Applies to: persistent arXiv identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://aclanthology.org/2020.acl-main.347/
  - Applies to: ACL venue, publisher, pagination, citation, and license context.
  - Notes: Official ACL Anthology record.
- Source URL: https://doi.org/10.18653/v1/2020.acl-main.347
  - Applies to: persistent ACL publication identity.
  - Notes: Publisher DOI.
- Source URL: https://github.com/MiuLab/Lattice-ELMo
  - Applies to: official implementation, dataset restrictions, and documented run flow.
  - Notes: Inspected at commit `202e369c0d41ff4e62353073478d25fec4b18cca`; not executed or redistributed.
- Source URL: https://arxiv.org/abs/2011.00780
  - Applies to: author follow-up on adapting pretrained transformers to lattice inputs.
  - Notes: Primary arXiv record used as related reading.
- Source URL: https://aclanthology.org/P19-1115/
  - Applies to: self-attentional lattice-input methodological context.
  - Notes: Primary ACL Anthology record used as related reading.
- Source URL: https://aclanthology.org/N18-1202/
  - Applies to: ELMo pretraining baseline and contextual-representation context.
  - Notes: Primary ACL Anthology record used as related reading.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260731-Ontology%20ASR%20Correction/2606.13464-whitepaper-review.md
  - Applies to: related DEP bridge for structured ASR correction.
  - Notes: Repository research artifact; no claims transferred to the selected paper.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-Cued%20Speech%20MLLM/cued_speech_mllm_manuscript.md
  - Applies to: related DEP bridge for multimodal spoken recognition.
  - Notes: Repository research artifact; no claims transferred to the selected paper.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260720-HeadRouter%20Audio/2604.23717-whitepaper-review.md
  - Applies to: related DEP bridge for task-aware audio representation selection.
  - Notes: Repository research artifact; no claims transferred to the selected paper.
