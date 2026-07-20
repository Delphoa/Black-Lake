# Report-Mark: DUET Set-Wise CTR

## Source Metadata

- Deployment job: `BLAD-2200-20260719-7D93E819`
- Deployment item: `BLAD-2200-20260719-7D93E819-P10`
- Paper: *DUET: Dual Model Co-Training for Entire Space CTR Prediction*
- Authors: Yutian Xiao, Meng Yuan, Fuzhen Zhuang, Wei Chen, Shukuan Wang, Shanqi Liu, Chao Feng, Wenhui Yu, Xiang Li, Lantao Hu, Han Li, and Zhao Zhang.
- Canonical record: https://arxiv.org/abs/2510.24369
- Full paper: https://arxiv.org/html/2510.24369 and https://arxiv.org/pdf/2510.24369
- Identifier: arXiv:2510.24369v1; DOI:10.48550/arXiv.2510.24369; submitted 2025-10-28.
- Selection: uniform random index 49,531 from 75,776 unique paper units (75,779 PDFs enumerated); first draw accepted; zero slot exclusions.
- Integrity: initially partial; one bounded official-HTML repair; final state complete. Sources remain local and are not redistributed.

## Concise Research Notes

DUET addresses two industrial pre-ranking limitations at once. First, point-wise scoring ignores relations among candidates and may produce individually strong but collectively redundant lists. Second, training on exposed interactions creates sample-selection bias because most retrieved candidates receive no observed label. The model scores a candidate set jointly, using linear attention for candidate-to-history and candidate-to-candidate interactions, then trains two independently initialized copies that exchange soft pseudo-labels on unexposed candidates.

The set-wise module reduces attention complexity from the source-reported quadratic `O(mn)` form to `O(m+n)` through associative linear attention. Degree normalization replaces the stabilizing effect lost when softmax is removed. The co-training objective combines binary cross-entropy on observed labels or peer pseudo-labels with symmetric KL consistency. Offline, DUET reports AUC 0.6322 on Recflow and 0.6881/UAUC 0.6787 on the industrial dataset. Removing co-training causes the largest reported ablation losses: -5.17%, -4.97%, and -4.93% relative improvement across the three metrics.

For deployment, retrieval supplies 4,500 items, DUET pre-ranks them to 600, and only the better of the two trained models is served. A two-week A/B test reports positive confidence intervals for most metrics on Kuaishou and Kuaishou Lite. Kuaishou total watch time rises 0.195% with a [0.09%, 0.30%] interval; average novel cluster rises 0.173% with a [0.11%, 0.24%] interval. These results support production relevance but do not establish long-term causal welfare, calibration, or robustness under drift.

## Evidence and Attribution

| Evidence | Source | Finding | Reviewer boundary |
|---|---|---|---|
| E1 | Full paper, section 3.1 | Candidate-history and candidate-candidate linear attention are fused with profile and cross features. | Set-level scoring can still inherit retrieval bias and feature leakage. |
| E2 | Sections 3.2-3.3 | Two models exchange soft labels on unexposed items and use symmetric KL consistency. | Peer agreement can amplify shared errors; independence of initialization is not independence of data. |
| E3 | Table 2 | DUET reports the highest listed offline AUC/UAUC on Recflow and the industrial dataset, with significance markers against the best trainable baseline. | Comparisons depend on reported implementations and metrics. |
| E4 | Table 3 | Removing co-training produces the largest ablation decline; removing set interactions and KL also hurts. | Ablations demonstrate contribution in the reported setup, not universal necessity. |
| E5 | Section 3.4 | Production pre-ranking narrows 4,500 retrieved items to 600 and deploys one trained model. | Latency, QPS, energy, and tail behavior are not quantified in the table evidence. |
| E6 | Table 4 | The two-week test reports engagement and diversity uplifts across two applications. | Short A/B duration and platform-specific definitions limit generalization. |

Source claims above are attributed to the paper. Statements about shared-error amplification, privacy, governance, and product design are reviewer interpretation.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-MiNet CTR Transfer/minet_ctr_manuscript.md` — direct overlap in industrial CTR prediction, multi-source interest modeling, component ablation, and online evaluation; verified from its DEP manuscript and attribution.
2. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` — conceptual overlap in soft-label reliability, teacher error, calibration, and confirmation-bias controls; verified from its source-first manuscript.
3. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` — operational overlap in conditional model efficiency and the gap between arithmetic complexity and measured serving performance; verified from its DEP manuscript.

## Synthesis Note

### Concept Bridge

DUET connects list-aware CTR scoring to semi-supervised entire-space learning. MiNet shows how candidate-conditioned interest fusion can improve CTR across behavior domains; DUET moves the interaction unit from one item to a candidate set. Adversarial Label Noise warns that a learned soft target is evidence with uncertainty, not truth. DMNN adds the systems lesson that lower theoretical operations do not guarantee lower latency. Together, the deposits imply a deployment contract: measure list quality and calibration, audit peer-label disagreement, and benchmark the actual pre-ranking service under realistic candidate counts.

### Potential Implementations

1. Add a shadow set-wise scorer after retrieval, comparing point-wise and joint ordering without affecting users.
2. Build a pseudo-label governance service that records peer disagreement, confidence, exposure status, and drift by cohort.
3. Create a staged pre-ranking canary that gates promotion on AUC/UAUC, calibration, diversity, p95 latency, and tail-cohort safety.

### Deeper Relationship Observations

1. DUET and MiNet both make candidate representations conditional on context, but DUET treats neighboring candidates as context while MiNet emphasizes behavior domains.
2. Co-training reduces single-model confirmation bias only when the peers retain useful diversity; KL consistency deliberately constrains the same diversity that enables correction.
3. Linear attention solves an asymptotic interaction problem, while DMNN shows that production gains still depend on batching, memory traffic, and hardware utilization.

### Conceptual Similarities

1. All three related deposits separate a learned routing or weighting signal from the downstream prediction it controls.
2. DUET peer labels and rectified soft labels are both uncertain supervisory distributions requiring calibration and held-out validation.
3. DUET, MiNet, and DMNN use adaptive computation to allocate representational capacity according to input context.

### MVP Implementations with Code Mock-Ups

1. A candidate-set wrapper can preserve list boundaries while measuring a shadow score.

```python
def shadow_batch(request_id, candidates, scorer):
    scores = scorer.score_set(candidates)
    return {"request_id": request_id, "scores": list(scores), "served": False}
```

2. Peer disagreement should be a first-class training diagnostic rather than a discarded intermediate.

```python
def peer_audit(model_a, model_b, batch):
    pa, pb = model_a(batch), model_b(batch)
    disagreement = sum(abs(a - b) for a, b in zip(pa, pb)) / len(pa)
    return {"mean_abs_disagreement": disagreement, "count": len(pa)}
```

3. A promotion gate can combine quality, calibration, diversity, and serving limits.

```python
def promote(metrics, limits):
    required = ("auc", "calibration_error", "novelty", "p95_ms")
    return all(key in metrics for key in required) and all(
        limits[key](metrics[key]) for key in required
    )
```

### Developer Challenges

1. Preserving candidate-set boundaries and avoiding padding or truncation artifacts in distributed feature pipelines.
2. Training two models without accidental parameter, cache, or sampler coupling that collapses peer diversity.
3. Converting linear-attention arithmetic savings into stable p95/p99 latency at 4,500-candidate production scale.

### Author Challenges

1. Reporting calibration, peer-disagreement distributions, and failure cases alongside aggregate AUC.
2. Separating the effects of set-level modeling, unexposed-sample supervision, and any production feature changes over longer tests.
3. Defining diversity and long-term-interest metrics clearly enough for external replication and welfare interpretation.

## Validation Notes

- IDs stamped: `BLAD-2200-20260719-7D93E819` and `BLAD-2200-20260719-7D93E819-P10`.
- The selected unit was distinct from all nine earlier job papers. A superficially adjacent current-job CTR deposit (MiNet) has a different arXiv ID, title, authors, and method.
- Dedup scans covered `.logs`, `.reports`, `.lake-data`, the private automation ledger, current-job set, and relevant companion-repository entries; no match was found. The 24-hour cutoff began 2026-07-18.
- Source gate passed after one bounded repair: PDF 2,899,255 bytes with `%PDF-` and trailing `%%EOF`; official HTML 208,862 bytes, 72,900 body characters, 27 headings, document marker present, and five structure terms.
- Exactly three related DEP entries were inspected. Reviewer inference is labeled separately from paper evidence.
- The staged public allowlist is Markdown plus required index/status JSON only. PDF, HTML, metadata, extracted text, caches, archives, and `.source/` are excluded.

## Attribution Block

- https://arxiv.org/abs/2510.24369 — identity, authors, abstract, dates, and version metadata.
- https://arxiv.org/html/2510.24369 — full-paper method, formulas, experiments, tables, deployment description, limitations, and references.
- https://arxiv.org/pdf/2510.24369 — verified complete primary source, withheld locally.
- https://doi.org/10.48550/arXiv.2510.24369 — persistent identifier.
- `.lake-data/DEP-E/DEP-E-20260719-MiNet CTR Transfer/minet_ctr_manuscript.md` — related CTR and online-evaluation synthesis.
- `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` — related soft-label and calibration synthesis.
- `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` — related efficient-serving synthesis.
- Source files, metadata, extracted text, caches, and local archive context were withheld. No source document was uploaded.
