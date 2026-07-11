# Report-Mark: CausalTAD Trajectory

## Source Metadata

| Field | Value |
|---|---|
| Paper title | CausalTAD: Causal Implicit Generative Model for Debiased Online Trajectory Anomaly Detection |
| Authors | Wenbin Li; Di Yao; Chang Gong; Xiaokai Chu; Quanliang Jing; Xiaolei Zhou; Yuxuan Zhang; Yunxia Fan; Jingping Bi |
| arXiv ID | 2412.18820v1 |
| DOI | 10.48550/arXiv.2412.18820 |
| Venue | 40th IEEE International Conference on Data Engineering (ICDE 2024), pages 4477-4490 |
| arXiv history | Submitted 2024-12-25; one inspected version |
| Primary URLs | https://arxiv.org/abs/2412.18820 ; https://arxiv.org/html/2412.18820 ; https://arxiv.org/e-print/2412.18820 ; https://github.com/LwbXc/CausalTAD |
| Extraction status | HTML and TeX source cached; PDF text extraction unavailable |
| Source files deposited | None; no `.source/` folder was created |
| License notes | arXiv page links the non-exclusive distribution license; no root license file was visible on the inspected code repository page |

## Concise Research Notes

CausalTAD targets online trajectory anomaly detection when source-destination (SD) pairs at inference were absent from training. The paper argues that conditional generation scores, `P(T|C)`, absorb a spurious association created by road preference `E`, modeled as a common cause of both SD-pair distribution `C` and observed trajectories `T`. It substitutes an interventional criterion, `P(T|do(C))`, intended to remove the backdoor path through road preference.

The implementation combines two variational models. TG-VAE estimates the joint likelihood of the SD pair and trajectory with road-constrained autoregressive decoding. RP-VAE estimates a road-segment-level scaling factor used to adjust that likelihood. Segment factors can be precomputed, allowing the online anomaly score to update in constant time per newly observed road segment under the paper's formulation.

Experiments use map-matched taxi trajectories from Xi'an and Chengdu. Each city uses 100 candidate SD pairs with more than 100 trajectories; training and in-distribution test sets split trajectories from those pairs, while an OOD test set draws trajectories with unseen SD pairs. Because labeled anomalies were unavailable, evaluation anomalies were generated as detours or route switches. The paper reports ROC-AUC and PR-AUC against iBOAT, VSAE, SAE, beta-VAE, FactorVAE, GM-VSAE, and DeepTEA.

For in-distribution cases, CausalTAD reports 2.1%-5.7% improvement over the best baseline across the eight city/anomaly/metric combinations. For OOD cases, it reports 10.6%-32.7% improvement; the reported Chengdu OOD scores range from 0.8514 to 0.8844 across ROC-AUC and PR-AUC. At 60% trajectory observation, the paper reports PR-AUC 0.9123 for one Xi'an in-distribution switch case and ROC-AUC 0.8030 for one Chengdu OOD switch case. These are author-reported results, not reproduced here.

The clearest disclosed limitation is the static treatment of road preference, even though congestion and other factors vary by time of day and day of week. A second review-level limitation is the use of synthetic anomalies. A third is repository alignment: the paper describes Xi'an and Chengdu while the public code README describes Xi'an and Porto datasets.

## Evidence and Attribution

| ID | Evidence | Source Basis | Use | Confidence |
|---|---|---|---|---|
| E1 | arXiv metadata provides title, authors, ID, DOI, v1 date, cs.LG classification, and ICDE acceptance note. | arXiv abstract page | Bibliographic identity | High |
| E2 | The causal graph treats road preference as a common cause of SD-pair distribution and trajectories, motivating `P(T|do(C))`. | TeX source and arXiv HTML, introduction through causal analysis | Core problem and causal framing | High for author formulation; medium for causal validity |
| E3 | TG-VAE estimates trajectory/SD likelihood and RP-VAE estimates a segment-level scaling factor. | TeX source, methodology sections | Mechanism | High |
| E4 | Xi'an and Chengdu experiments use ID/OOD splits plus generated detour and switch anomalies. | TeX source, experimental setup | Evaluation design | High |
| E5 | Tables report 2.1%-5.7% ID gains and 10.6%-32.7% OOD gains, with ablations below the full model. | TeX source, Tables I-III | Reported empirical results | High for transcription; low for independent reproduction |
| E6 | Static road preference is disclosed as a limitation and temporal factorization is proposed as future work. | TeX source, limitations section | Boundary condition | High |
| E7 | Public code README describes ICDE 2024 code and a one-command Xi'an example, but its Xi'an/Porto dataset description differs from the paper's Xi'an/Chengdu setup. | Author GitHub repository README | Reproducibility assessment | High for observed discrepancy |
| E8 | Three related DEP entries provide road-system, debiasing, and structure-aware distribution-shift context. | Inspected Black-Lake and Black-Lake-Data artifacts | Synthesis bridge | Medium; contextual only |

## Related DEP Entries

1. `.lake-data/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md`
   - Relevance: Both artifacts study learned systems operating on road networks under online constraints. Self-Learned IDC focuses on state representation and safety-constrained control at mixed-traffic intersections; CausalTAD focuses on anomaly scoring under unseen SD pairs.
   - Source basis: The related manuscript's executive summary, traffic simulation setup, evidence ledger, limitations, and safety observations were inspected.

2. `.lake-data/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`
   - Relevance: Both works frame model failure as inherited bias from an imbalanced observational process and propose model-level corrections intended to improve robustness under changed distributions. BA-LoRA also warns that suggestive comparisons are not controlled causal tests, a useful caution for CausalTAD's assumed causal graph.
   - Source basis: The related manuscript's problem, evidence ledger, claims table, limitations, and causal-evidence discussion were inspected.

3. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260707-Tech Intel 1103/daily_research_findings_2026-07-07_1103.md`
   - Relevance: Its structure-aware spatial split finding addresses correlated leakage and hidden stratification in spatial AI. That directly complements CausalTAD's ID/OOD SD-pair split and suggests stronger geographic and structural evaluation protocols.
   - Source basis: The related finding titled "Structure-aware splits expose leakage and hidden stratification in spatial AI domains" and its cited primary arXiv source were inspected.

## Synthesis Note

### Concept Bridge

CausalTAD can be read as an evidence-interface correction for spatial decision systems. The raw trajectory likelihood is not trusted because it mixes route feasibility with historically popular destinations and roads. The model therefore creates a second road-preference factor to adjust anomaly evidence before action. This connects the road-system focus of Self-Learned IDC, the inherited-bias framing of BA-LoRA, and the evaluation discipline of structure-aware spatial splits: representation, debiasing, and dataset structure jointly determine whether an apparent anomaly is real or an artifact of observational imbalance.

### Potential Implementations

1. `Trajectory Shift Audit`: Evaluate a trajectory anomaly model across held-out SD pairs, geographic regions, time blocks, and road-popularity strata, reporting ROC-AUC, PR-AUC, calibration, and false-positive concentration.
2. `Road Preference Monitor`: Maintain date-bucketed segment preference estimates and flag drift between training and live distributions before anomaly scores are trusted.
3. `Spatial Evidence Card`: Extend Black-Lake model reviews with causal-graph assumptions, split construction, anomaly-label provenance, road-map version, and failure-strata fields.

### Deeper Relationship Observations

1. CausalTAD and Self-Learned IDC both put a learned representation between physical observations and online intervention, so hidden representation errors can propagate directly into safety-relevant decisions.
2. CausalTAD and BA-LoRA both correct behavior produced by imbalanced upstream data, but neither correction alone proves the proposed causal explanation; controlled interventions or matched counterfactual evaluations remain necessary.
3. Structure-aware splitting is not only an evaluation improvement for CausalTAD; it tests whether the reported OOD gain survives spatial autocorrelation, route overlap, and subgroup imbalance that random sampling may conceal.

### Conceptual Similarities

1. Each related entry separates raw frequency from trustworthy evidence: popular routes, dominant pretraining patterns, nearby actor order, or spatially correlated samples can all create misleading shortcuts.
2. Each entry treats generalization as a structured shift problem rather than a single aggregate score problem, requiring explicit strata, environments, or unseen configurations.
3. Each entry benefits from auditable intermediate state: road factors, adapter outputs, mixed-traffic encodings, and split manifests make failures easier to attribute and review.

### MVP Implementations with Code Mock-ups

1. `SD-Pair Split Auditor`

```python
def split_audit(train_pairs, test_rows):
    seen = set(train_pairs)
    counts = {"id": 0, "ood": 0}
    for row in test_rows:
        key = (row["source"], row["destination"])
        counts["id" if key in seen else "ood"] += 1
    return counts
```

2. `Segment Preference Drift`

```python
from collections import Counter

def total_variation(reference_segments, current_segments):
    a, b = Counter(reference_segments), Counter(current_segments)
    keys = set(a) | set(b)
    na, nb = max(sum(a.values()), 1), max(sum(b.values()), 1)
    return 0.5 * sum(abs(a[k] / na - b[k] / nb) for k in keys)
```

3. `Anomaly Evidence Card`

```python
def evidence_card(model, split, label_source, caveats):
    return {
        "model": model,
        "split_manifest": split,
        "anomaly_label_source": label_source,
        "caveats": list(caveats),
        "deployment_status": "research-only",
    }
```

### Developer Challenges

1. Reproducing the paper requires resolving dataset naming/content differences, pinning a code commit, confirming road-map preprocessing, and reconstructing all ID/OOD and anomaly-generation splits.
2. A production road-preference factor must handle temporal drift, road closures, map updates, sparse segments, and cold-start SD pairs without leaking future information.
3. Online anomaly outputs need calibrated thresholds, latency bounds, false-positive review, privacy controls, and human escalation rather than direct automated enforcement.

### Author Challenges

1. Release a versioned reproduction manifest that maps paper tables to exact datasets, preprocessing scripts, configs, seeds, dependencies, and checkpoints.
2. Validate on real incident labels or blinded human review in addition to synthetic detour and route-switch anomalies.
3. Extend the causal model and experiments to time-varying road preference and report sensitivity to alternative causal graphs or violated backdoor assumptions.

## Validation Notes

- Required output paths are repository-relative and public-safe.
- No local absolute paths, home directories, usernames, machine names, workspace roots, local timezone labels, or exact execution timestamps are present.
- Related DEP synthesis contains exactly three inspected repository entries.
- Synthesis Note contains exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP implementations with code mock-ups, three developer challenges, and three author challenges.
- Paper claims are distinguished from reviewer inference; no experiment, training run, or metric reproduction is implied.
- No source files were collected into the DEP.

## Attribution Block

- Source URL: https://arxiv.org/abs/2412.18820
  - Applies to: paper identity, authors, DOI, v1 date, subject, abstract, and ICDE acceptance note.
  - Notes: Primary arXiv metadata page inspected.
- Source URL: https://arxiv.org/html/2412.18820
  - Applies to: introduction, causal framing, method, experiments, results, and limitations.
  - Notes: Public arXiv HTML and cache-backed text were inspected.
- Source URL: https://arxiv.org/e-print/2412.18820
  - Applies to: TeX-source review of equations, tables, ablations, and limitations.
  - Notes: Public source package fetched for review; not redistributed.
- Source URL: https://arxiv.org/pdf/2412.18820
  - Applies to: canonical paper reference.
  - Notes: Public PDF reference; no PDF file is redistributed in this DEP.
- Source URL: https://doi.org/10.48550/arXiv.2412.18820
  - Applies to: persistent arXiv DOI.
  - Notes: DataCite DOI for the arXiv record.
- Source URL: https://github.com/LwbXc/CausalTAD
  - Applies to: official code/dataset/usage and ICDE citation context.
  - Notes: Repository README inspected; code and datasets were not executed or redistributed.
- Repository path: `.lake-data/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md`
  - Applies to: road-system and online-decision synthesis.
  - Notes: Existing Black-Lake DEP manuscript inspected.
- Repository path: `.lake-data/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`
  - Applies to: bias, causal-evidence, and distribution-shift synthesis.
  - Notes: Existing Black-Lake DEP manuscript inspected.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260707-Tech%20Intel%201103/daily_research_findings_2026-07-07_1103.md
  - Applies to: structure-aware spatial split synthesis.
  - Notes: Existing Black-Lake-Data DEP finding inspected.
