# Report-Mark: EncoderMI

## Source Metadata

| Field | Value |
|---|---|
| Paper | *EncoderMI: Membership Inference against Pre-trained Encoders in Contrastive Learning* |
| Authors | Hongbin Liu; Jinyuan Jia; Wenjie Qu; Neil Zhenqiang Gong |
| arXiv | [2108.11023](https://arxiv.org/abs/2108.11023) |
| DOI | [10.1145/3460120.3484749](https://doi.org/10.1145/3460120.3484749) |
| Venue | CCS 2021, pp. 2081–2095 |
| Public source locators | [abstract](https://arxiv.org/abs/2108.11023), [PDF](https://arxiv.org/pdf/2108.11023), [full-paper HTML](https://arxiv.org/html/2108.11023) |
| Source state | Complete after one bounded local repair; source files withheld |
| Review date | 2026-08-02; exact local execution time withheld |
| Official implementation | Not located in inspected sources; the paper links public image-collection utilities for its CLIP audit data, not an author-maintained EncoderMI implementation |

## Concise Research Notes

EncoderMI targets membership inference against an image encoder trained with contrastive learning. Its threat model assumes black-box feature queries and a shadow dataset, with eight combinations of knowledge about pre-training-data distribution, encoder architecture, and training algorithm. The method creates multiple augmented views of each input, collects pairwise similarity scores among their encoded representations, and trains an inference classifier from a shadow encoder whose members and non-members are known.

The three variants are vector-based EncoderMI-V, set-based EncoderMI-S, and threshold-based EncoderMI-T. In the main CIFAR10 table, with all three background-knowledge dimensions available, EncoderMI-V reports 91.4% accuracy, 90.1% precision, and 93.5% recall; the paper reports five-trial standard deviations. On Tiny-ImageNet under the same knowledge setting, EncoderMI-V reports 96.5% accuracy, 96.6% precision, and 97.0% recall. These are source-reported values, not independent reruns.

For CLIP ViT-B/32, the paper evaluates 1,000 potential members and 1,000 constructed non-members for each of Google-image-search and Flickr collections. Across shadow datasets, it reports accuracy in the 0.66–0.75 range, but potential members are not verified ground-truth members of CLIP. The result therefore demonstrates audit signal under a proxy-label design, not a certified membership determination.

The proposed countermeasure is early stopping. The paper observes that longer pre-training increases the separation of augmented-view similarity for members and non-members; stopping earlier reduces membership-inference accuracy but also reduces downstream classifier accuracy. The paper discusses differential privacy and adversarial training as future countermeasure directions rather than presenting them as completed evaluations.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Boundary |
|---|---|---|---|---|
| E1 | Official arXiv record and abstract | Title, authors, arXiv date, problem framing, high-level method and findings | High | Abstract is not sufficient for detailed metrics |
| E2 | Verified full-paper HTML via the public full-paper locator and approved fallback | Threat model, method, tables, CLIP setup, countermeasure, limitations, conclusion | High | Experiments were not independently reproduced |
| E3 | Verified PDF via the public arXiv locator | Paper identity, complete-document integrity, figures/tables cross-check | High | Source file remains private |
| E4 | Penn State publication record and DOI metadata | CCS 2021 venue, pages, publication DOI | Medium-high | Publisher metadata does not validate experiments |
| E5 | MRMMIA Memory Attack DEP | Membership-inference, query-signal, false-positive, and privacy-defense comparison | Medium | Different target state and threat setting |
| E6 | 4DContrast Contrastive DEP | Contrastive representations, augmented correspondence, and evaluation transfer | Medium | Different task and modality |
| E7 | Equivariant Contrastive DEP | Augmentation and representation-invariance implementation context | Medium | Different task and deployment objective |

No source file, local path, source archive, cache, extracted paper text, or machine-specific execution record is included in this report.

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260726-MRMMIA Memory Attack/2605.27825-whitepaper-review.md` — direct conceptual overlap in membership inference, black/gray/white-box access, query aggregation, false-positive operating points, and privacy defenses. Source basis: the inspected public DEP README and review.
2. `.lake-data/DEP-E/DEP-E-20260722-4DContrast Contrastive/4dcontrast_contrastive_manuscript.md` — methodological overlap in contrastive representation learning, augmented correspondences, and the need to distinguish representation gains from task-level evidence. Source basis: the inspected public DEP README and manuscript.
3. `.lake-data/DEP-E/DEP-E-20260721-Equivariant Contrastive/equivariant_contrastive_manuscript.md` — methodological overlap in augmentation-driven representation invariance and provenance-first evaluation. Source basis: the inspected public DEP README and manuscript.

## Synthesis Note

### Concept Bridge

EncoderMI treats representation stability under controlled augmentation as a measurable privacy signal. MRMMIA similarly aggregates repeated, semantically related probes instead of trusting one response. The contrastive DEPs show the constructive side of the same design space: augmentations are used to make representations invariant or informative. The bridge is therefore a shared evaluation object—how repeated views or probes change a hidden state—and a shared governance question—when does that signal support a useful decision without being overread as proof?

### Potential Implementations

1. **Offline encoder privacy audit harness:** train a small shadow encoder only on consented synthetic or public data, generate augmented-view similarity features, and report calibrated TPR/FPR with a fixed query budget. Risk control: no inference against private or unauthorized models.
2. **Privacy-utility regression gate:** evaluate early stopping and approved privacy defenses against a frozen downstream task, storing the full membership-utility frontier rather than one score. Risk control: treat outputs as nonbinding research evidence with human review.
3. **Training-data provenance review service:** combine consent manifests, near-duplicate checks, model-version records, and a bounded audit protocol to help data owners investigate possible training-data reuse. Risk control: require ground-truth labels or mark results as proxy audits.

### Deeper Relationship Observations

1. Repeated-view similarity is a privacy signal because contrastive training intentionally aligns views; the same invariance that improves transfer can preserve training-set-specific regularities.
2. Query aggregation is an evidence amplifier in both EncoderMI and MRMMIA, so rate limits and false-positive calibration are part of the method rather than deployment afterthoughts.
3. Early stopping and representation design expose a common frontier: reducing memorization may reduce downstream utility, so privacy claims need matched utility measurements.

### Conceptual Similarities

1. All four records separate a hidden representation or state from the observable decision signal used by an evaluator.
2. All four rely on controlled transformations or probes to reveal structure that is not visible in one raw observation.
3. All four require source/version provenance, baseline parity, and explicit failure boundaries before their reported results can support implementation decisions.

### MVP Implementations

1. **Synthetic shadow-encoder evaluator** — local notebook that generates two augmented views, computes bounded cosine similarity, and evaluates a threshold on synthetic member/non-member labels.

```python
from math import sqrt

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sqrt(sum(x * x for x in a))
    nb = sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0

def membership_signal(views):
    scores = [cosine(views[i], views[j])
              for i in range(len(views))
              for j in range(i + 1, len(views))]
    return sum(scores) / len(scores) if scores else 0.0
```

2. **Calibrated audit report** — reviewer-facing tool that selects a threshold on a held-out, consented calibration set and reports coverage, TPR, FPR, and an abstain band.

```python
def audit_score(score, threshold, margin):
    if abs(score - threshold) <= margin:
        return {"decision": "abstain", "score": score}
    label = "member-like" if score > threshold else "non-member-like"
    return {"decision": label, "score": score}

def summarize(labels, predictions):
    positives = sum(labels)
    negatives = len(labels) - positives
    tp = sum(y == p == 1 for y, p in zip(labels, predictions))
    fp = sum(y == 0 and p == 1 for y, p in zip(labels, predictions))
    return {"tpr": tp / positives if positives else 0.0,
            "fpr": fp / negatives if negatives else 0.0}
```

3. **Privacy-utility frontier ledger** — governance-facing record that keeps the model revision, defense setting, audit metrics, downstream utility, and reviewer decision together.

```python
def record_frontier(model_id, defense, audit, utility, source_status):
    if source_status != "verified-public-or-consented":
        raise ValueError("source provenance gate failed")
    return {"model_id": model_id, "defense": defense,
            "audit": audit, "downstream_utility": utility,
            "decision": "review-required"}
```

### Developer Challenges

1. Recreate the paper’s shadow-training and augmentation pipeline without dataset leakage, hidden overlap, or accidental changes to the eight knowledge settings.
2. Implement threshold calibration, abstention, query budgeting, and audit logging without treating proxy members or average accuracy as ground truth.
3. Compare privacy defenses under matched downstream utility and model revisions, including negative results and drift.

### Author Challenges

1. Provide or standardize a consented, independently checkable membership benchmark with verified members, non-members, and near-duplicate controls.
2. Report operating curves, query costs, calibration, confidence intervals, and proxy-label error for CLIP-style evaluations.
3. Extend the defense study beyond early stopping to differential privacy, augmentation policies, feature-release controls, and adaptive auditors.

## Validation Notes

- Source gate: complete after one bounded repair; PDF passed 10 KB, `%PDF-`, and trailing `%%EOF`; full-paper HTML passed 5 KB, 2,000 body characters, document marker, heading count, and structure-term checks.
- Selection gate: uniform PDF-parent-unit draw, 75,960 PDFs, 75,957 units, index 15,397, first draw accepted.
- Dedup gate: no prior Arxiv DEP artifact, DOI/title/slug match, or 24-hour marker; metadata-only author inventory match did not count as a duplicate.
- Review gate: full paper inspected through abstract, introduction, threat model, method, evaluation tables, CLIP evaluation, countermeasures, related work, conclusion, and references; official code was not located or executed.
- Public-output gate: only generated Markdown under `.logs`, `.reports`, and `.lake-data` is eligible; no `.source/` directory is created.
- Public-safety gate: no local absolute path, username, machine name, local timezone label, exact local execution timestamp, source file, cache, extracted source text, or private artifact is included.

## Attribution Block

- [arXiv abstract record](https://arxiv.org/abs/2108.11023)
  - Applies to: paper identity, authors, date, abstract, and canonical source locator.
- [arXiv PDF](https://arxiv.org/pdf/2108.11023)
  - Applies to: full-paper review and document-integrity checks; source file withheld locally.
- [arXiv full-paper HTML locator](https://arxiv.org/html/2108.11023)
  - Applies to: full-text review; approved fallback rendering withheld locally.
- [Published DOI](https://doi.org/10.1145/3460120.3484749)
  - Applies to: CCS 2021 venue and publication metadata.
- [Penn State publication record](https://pure.psu.edu/en/publications/encodermi-membership-inference-against-pre-trained-encoders-in-co)
  - Applies to: venue, page range, author, and DOI cross-check.
- [MRMMIA Memory Attack DEP](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-A/Series%20001/DEP-A-20260726-MRMMIA%20Memory%20Attack)
  - Applies to: related membership-inference and privacy-defense synthesis.
- [4DContrast Contrastive DEP](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260722-4DContrast%20Contrastive)
  - Applies to: related contrastive representation synthesis.
- [Equivariant Contrastive DEP](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260721-Equivariant%20Contrastive)
  - Applies to: related augmentation and representation-invariance synthesis.
- Source boundary: all local source documents and integrity companions were withheld; no source files were uploaded, committed, staged, or attached.
