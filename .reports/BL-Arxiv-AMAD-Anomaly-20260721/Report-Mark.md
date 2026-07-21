# Report-Mark: AMAD Multiscale Anomalies

## Source Metadata

| Field | Value |
|---|---|
| Paper | *AMAD: Adversarial Multiscale Anomaly Detection on High-Dimensional and Time-Evolving Categorical Data* |
| Authors | Zheng Gao; Lin Guo; Chi Ma; Xiao Ma; Kai Sun; Hang Xiang; Xiaoqiang Zhu; Hongsong Li; Xiaozhong Liu |
| arXiv | [1907.06582v1](https://arxiv.org/abs/1907.06582), submitted 2019-07-12 |
| arXiv DOI | [10.48550/arXiv.1907.06582](https://doi.org/10.48550/arXiv.1907.06582) |
| Published DOI | [10.1145/3326937.3341256](https://doi.org/10.1145/3326937.3341256) |
| Venue | DLP-KDD 2019 workshop; eight pages |
| Public full text | [arXiv PDF](https://arxiv.org/pdf/1907.06582); [ar5iv full-paper HTML](https://ar5iv.labs.arxiv.org/html/1907.06582) |
| Public code | [pkumc/AMAD](https://github.com/pkumc/AMAD), inspected at [commit 0391c97](https://github.com/pkumc/AMAD/commit/0391c97dba2823608006180957f9330c5ec06791) |
| Review status | Source-complete, source-first critical review; no independent model execution or metric reproduction |

The private archive unit was initially partial because it contained a valid full PDF but no full-paper HTML. A bounded repair preserved the valid PDF and collected validated full-paper HTML, metadata HTML, and the arXiv source package. The final verification confirmed an eight-page, 715,086-byte PDF with a `%PDF-` header and trailing `%%EOF`; 437,327-byte full-paper HTML with 47,873 body characters, 71 headings, seven paper-structure terms, and a document marker; and zero partial files. Original source files were withheld locally and were not uploaded.

## Concise Research Notes

AMAD tackles anomaly detection when each observation is a high-dimensional collection of categorical feature IDs and observations arrive as time-ordered blocks. It builds a hierarchy from feature embeddings to attribute representations, then to two instance views: a self representation and a relative representation measured against the surrounding block. An RNN models the resulting sequence. Adversarial autoencoders and discriminators regularize reconstruction at the instance and block levels, and the paper combines reconstruction and discriminator-derived terms into anomaly scores.

The paper evaluates synthetic categorical sequences, Connect-4 records treated as nonsequential categorical data, and a proprietary industrial system-log dataset. All reported test sets are balanced to 50% anomalies, while training uses normal examples. The authors average ten runs and report that AMAD's differences are significant at `p < 0.01`. Reported AMAD AUROC values are 0.717, 0.730, and 0.691 at the instance level, and 0.745, 0.746, and 0.674 at the block level, for the synthetic, public, and industrial datasets respectively.

The strongest evidence for the multiscale design comes from ablation. Removing relative representation sharply reduces synthetic block accuracy and F1; removing block-level loss also produces large synthetic and industrial declines; Gaussian-noise removal hurts across settings. A block-size sweep suggests that sizes above 100 degrade the sequential synthetic and industrial cases while the nonsequential public dataset remains comparatively flat.

The public repository improves inspectability but does not establish reproducibility. It has a single observed commit, TensorFlow 1-era APIs, no locked environment, no tests, and hard-coded author-local execution paths. More importantly, the inspected implementation differs from the paper in optimizer choice, representation fusion, sample block size, and final score composition. Those differences must be resolved before treating the code as an executable specification of the paper.

## Evidence and Attribution

| Claim or observation | Evidence basis | Classification |
|---|---|---|
| AMAD jointly models high-dimensional categorical instances and temporal blocks. | Paper abstract, methodology, architecture figure, and equations in the [full paper](https://ar5iv.labs.arxiv.org/html/1907.06582). | Source claim |
| The hierarchy is feature IDs to attributes to self/relative instance views to an RNN block representation. | Sections 3.1-3.3 and architecture diagram. | Source claim |
| The three AMAD instance AUROCs are 0.717, 0.730, and 0.691. | Paper Table 3, cross-checked visually against the rendered PDF. | Source claim |
| The three AMAD block AUROCs are 0.745, 0.746, and 0.674. | Paper Table 4, cross-checked visually against the rendered PDF. | Source claim |
| Test prevalence is artificially balanced at 50% anomalies. | Dataset construction text and Table 1. | Source claim with evaluation consequence |
| Relative representation and block loss matter most on sequential data. | Tables 5-6 and block-size analysis; effect interpretation by reviewer. | Mixed source evidence and reviewer interpretation |
| Reported significance does not substitute for uncertainty intervals or external reproduction. | Paper reports ten-run averages and `p < 0.01` but not the needed per-seed distributions; no execution was performed here. | Reviewer assessment |
| The inspected code diverges from the paper in four material places. | Paper equations/settings compared with `model.py` and `run.sh` at the pinned public commit. | Reviewer comparison |
| Deployment claims require drift, contamination, unseen-ID, calibration, and prevalence testing. | These regimes are absent from the paper's evaluation. | Reviewer recommendation |

Evidence priority was: the verified paper PDF and full-paper HTML for scientific claims; the arXiv and DOI records for identity; the workshop page for venue context; the pinned public repository for implementation observations; and related DEP manuscripts only for synthesis. An arXiv abstract page was treated as metadata, never as the paper. The proprietary industrial dataset was not independently accessible, and no source metric was presented as reproduced.

## Related DEP Entries

1. [CausalTAD Trajectory manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-CausalTAD%20Trajectory/causaltad_trajectory_manuscript.md) — conceptual overlap in generative anomaly scoring, temporal/OOD behavior, constructed anomalies, and assumptions about normality. Source basis: the related manuscript's method, evidence, limitations, and implementation sections.
2. [HSD FTI-FDet manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md) — conceptual overlap in industrial fault monitoring, scarce failures, representation choices, resource limits, and the gap between laboratory evaluation and field deployment. Source basis: the related manuscript's industrial context, evidence ledger, and deployment cautions.
3. [Technical Intelligence 1103, Finding 10](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260627-Tech%20Intel%201103/daily_research_findings_2026-06-27_1103.md) — the Kalman Prototypical Networks entry connects few-shot gas-turbine fault detection with nonstationarity and state estimation. Source basis: Finding 10 and its cited primary paper; used only as a research bridge, not evidence for AMAD's results.

## Synthesis Note

### Concept Bridge

The three related entries expose a useful progression. AMAD supplies hierarchical categorical reconstruction and two-scale scoring; CausalTAD adds a trajectory-oriented view of temporal normality and OOD behavior; HSD FTI-FDet focuses the industrial deployment problem; and the few-shot Kalman prototype finding suggests a route for adapting with sparse labeled failures. Together they point to a monitored system that keeps AMAD's self/relative categorical representation, models evolving normal trajectories, and reserves limited labels for calibrated prototype updates rather than retraining blindly.

This bridge is a design hypothesis, not a merged empirical result. The papers differ in datasets, modalities, objectives, evaluation regimes, and maturity. Any combined system therefore needs component ablations, chronological holdouts, prevalence-aware calibration, and explicit fallback behavior.

### Potential Implementations

1. **Categorical sequence triage service.** Encode event IDs by attribute, compute self and neighborhood-relative representations, aggregate fixed or adaptive windows, and emit instance plus block alerts with evidence summaries.
2. **Drift-aware industrial monitor.** Add a trajectory state model and monitor embedding, reconstruction, and score-distribution drift; freeze automated model updates whenever data quality or calibration checks fail.
3. **Few-shot incident adapter.** Maintain class prototypes only after analyst-confirmed incidents, use uncertainty-aware state updates, and preserve an unsupervised AMAD-style score as an independent safety signal.

### Deeper Relationship Observations

1. AMAD's relative representation and CausalTAD's trajectory perspective both make context part of the anomaly definition, but at different temporal resolutions; combining them could distinguish local novelty from long-horizon regime change.
2. AMAD's balanced constructed tests and HSD FTI-FDet's field-facing concerns highlight the same transfer hazard: ranking quality under laboratory prevalence does not establish useful alert precision under rare operational failures.
3. The few-shot Kalman prototype direction offers a controlled answer to a weakness shared by normal-only detectors: after confirmed anomalies appear, the system can learn bounded class structure without erasing the original unsupervised reference.

### Conceptual Similarities

1. All four research strands transform sparse or complex observations into learned representations before anomaly or fault decisions.
2. Each depends on contextual structure—blocks, trajectories, operating regimes, or state estimates—rather than treating every record as an isolated vector.
3. Each is most credible when its score is treated as decision support with calibration and human review, not as an autonomous high-stakes verdict.

### MVP Implementations with Code Mock-Ups

1. **Deterministic categorical block builder.** Preserve event order and surface unseen identifiers instead of silently mapping them into normality.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Event:
    timestamp: float
    attributes: tuple[int, ...]

def make_blocks(events: list[Event], size: int) -> list[list[Event]]:
    if size < 2:
        raise ValueError("block size must be at least two")
    ordered = sorted(events, key=lambda event: event.timestamp)
    return [ordered[i:i + size] for i in range(0, len(ordered), size)
            if len(ordered[i:i + size]) == size]
```

2. **Two-scale score contract.** Keep instance and block evidence separate so operators can see whether an isolated event or its sequence context drove the alert.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Score:
    instance: float
    block: float
    combined: float

def combine(instance: float, block: float, weight: float = 0.3) -> Score:
    if not 0.0 <= weight <= 1.0:
        raise ValueError("weight must be in [0, 1]")
    value = (1.0 - weight) * instance + weight * block
    return Score(instance=instance, block=block, combined=value)
```

3. **Prevalence-aware validation gate.** Require minimum precision and bounded alert volume on a chronological holdout before a threshold can be promoted.

```python
def threshold_gate(scores, labels, threshold, max_alert_rate=0.02,
                   min_precision=0.40):
    alerts = [score >= threshold for score in scores]
    positives = sum(alerts)
    true_positives = sum(a and bool(y) for a, y in zip(alerts, labels))
    alert_rate = positives / max(len(alerts), 1)
    precision = true_positives / max(positives, 1)
    return {
        "approved": alert_rate <= max_alert_rate and precision >= min_precision,
        "alert_rate": alert_rate,
        "precision": precision,
    }
```

### Developer Challenges

1. Reconcile the optimizer, representation-fusion, block-size, and score-formula discrepancies before choosing whether the paper or repository defines the reference implementation.
2. Port or isolate TensorFlow 1-era code while building deterministic data contracts, tests, seed control, environment locking, and lineage for categorical vocabularies.
3. Engineer streaming block boundaries, state resets, latency limits, unseen-ID handling, and rollback-safe calibration without leaking restricted source or industrial data.

### Author Challenges

1. Demonstrate results at realistic anomaly prevalence with chronological splits, validation-only threshold selection, confidence intervals, and event-level alert-burden metrics.
2. Clarify data provenance, anomaly construction, industrial baseline representations, license terms, and the exact mapping between equations and released code.
3. Evaluate contamination, drift, novel categories, missing attributes, block-boundary sensitivity, and prospective operational outcomes across independently accessible datasets.

## Validation Notes

- Random selection used a uniform random index over the eligible parent-unit list produced from the required PDF enumeration. The scan observed 75,779 PDFs, 75,776 parent units, and 75,591 units with usable identifiers. It withheld 185 identifier-incomplete units, excluded 248 units matching the used-paper index, and selected zero-based eligible index 34,605 from 75,343 eligible units.
- The used-paper index covered Black Lake `.logs`, `.reports`, and `.lake-data`, automation memory, and relevant Black-Lake-Data entries. Exact post-selection checks found no prior artifact for arXiv 1907.06582, its normalized title, or its slug. The 24-hour cutoff date was 2026-07-20. Duplicate rejections and reselections were zero.
- The source gate initially classified the unit as partial. A bounded repair preserved the valid PDF and added verified full-paper HTML, metadata HTML, a source package, attribution, a machine-readable summary, and a verification report to the private archive. No partial files remained.
- All eight rendered PDF pages were visually inspected. The full text, tables, figures, appendix, TeX source, public metadata, and pinned public code were inspected. The code was not executed, and the reported results were not independently reproduced.
- Exactly three related DEP entries were verified and used. Their claims were not substituted for primary paper evidence.
- Public-output policy permits generated Markdown only. No PDF, HTML, source archive, cache, extracted source text, local path, or original source file belongs in this deposit.

## Attribution Block

- Paper identity and abstract: [arXiv 1907.06582](https://arxiv.org/abs/1907.06582).
- Public paper PDF: [arXiv PDF](https://arxiv.org/pdf/1907.06582).
- Public full-paper HTML used for structured review: [ar5iv 1907.06582](https://ar5iv.labs.arxiv.org/html/1907.06582); used because official arXiv full-paper HTML was unavailable.
- Public source endpoint: [arXiv e-print](https://arxiv.org/e-print/1907.06582).
- Persistent identifiers: [arXiv DOI](https://doi.org/10.48550/arXiv.1907.06582) and [published DOI](https://doi.org/10.1145/3326937.3341256).
- Venue context and proceedings copy: [DLP-KDD 2019 accepted papers](https://dlp-kdd.github.io/dlp-kdd2019/accept.html) and [workshop PDF](https://dlp-kdd.github.io/dlp-kdd2019/assets/pdf/a7-gao.pdf).
- Public implementation: [pkumc/AMAD](https://github.com/pkumc/AMAD), inspected at [commit 0391c97](https://github.com/pkumc/AMAD/commit/0391c97dba2823608006180957f9330c5ec06791).
- Public dataset landing page referenced by the paper/code: [Tianchi](https://tianchi.aliyun.com/dataset/27665).
- Related DEP 1: [CausalTAD Trajectory manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-CausalTAD%20Trajectory/causaltad_trajectory_manuscript.md).
- Related DEP 2: [HSD FTI-FDet manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md).
- Related DEP 3: [Technical Intelligence 1103](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260627-Tech%20Intel%201103/daily_research_findings_2026-06-27_1103.md), Finding 10.
- Repository rules consulted: [Black Lake README](https://github.com/Delphoa/Black-Lake/blob/main/README.md), [DEP-E README](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md), and [Black-Lake-Data README](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md).
- Private source inventory, withheld from publication: `1907.06582.pdf`, `1907.06582.html`, `1907.06582.abs.html`, and `1907.06582.source.tar`, plus local attribution, summary, and verification records. Original source files remain in the private archive and were not uploaded.
