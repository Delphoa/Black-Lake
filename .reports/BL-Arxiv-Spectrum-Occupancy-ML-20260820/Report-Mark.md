# Report-Mark: Spectrum Occupancy ML

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Analysis of Spectrum Occupancy Using Machine Learning Algorithms* |
| Authors | Freeha Azmat; Yunfei Chen; Nigel Stocks |
| arXiv | 1503.07104v1; submitted 2015-03-24 |
| Journal | *IEEE Transactions on Vehicular Technology*, 65(9), 6853-6860 (2016) |
| Identifiers | DOI: 10.48550/arXiv.1503.07104; journal DOI: 10.1109/TVT.2015.2487047 |
| Evidence inspected | Verified local PDF and full-paper HTML, public arXiv metadata, public bibliographic records, and three related Black Lake DEP manuscripts |
| Source status | Complete local source unit; original files withheld from the public repository |
| Review date | 2026-08-20; exact local execution time withheld |

## Research Notes

The paper studies spectrum occupancy in cognitive radio networks using radiometer measurements from eight bands between 880 MHz and 2500 MHz collected over approximately four months. It converts thresholded frequency-bin measurements into occupancy features and a primary-user status label, then compares naive Bayes, decision trees, linear SVM, linear regression, and hidden Markov models. A firefly algorithm is used to tune the SVM box constraint.

The reported ranking depends on the feature width and evaluation setting. With `k=55`, naive Bayes has the highest mean classification accuracy (`0.9493`) among the listed methods, while with `k=192`, SVM has the highest accuracy among the non-FFA methods (`0.8528`). In the paper's 30-day `k=192` comparison, SVM+FFA reports `0.8728` mean accuracy versus `0.8499` for SVM, but the table's 15%/85% split shows the SVM+FFA runtime at `3.0412` seconds versus `0.0128` for SVM. The paper therefore supports a context-sensitive accuracy/compute tradeoff, not a universal best classifier.

The main evidence gap is reproducibility: no raw spectrum traces, code, repeated-seed analysis, uncertainty intervals, or hardware-normalized runtime package was available in the inspected sources. The results are useful as a design pattern for source-aware occupancy benchmarking, but live radio deployment would require calibrated probabilities, drift checks, asymmetric protection costs, authorization, and a simulation or hardware-in-the-loop gate.

## Evidence and Attribution

| ID | Source | Evidence used | Assessment |
|---|---|---|---|
| E1 | https://arxiv.org/abs/1503.07104 | Title, authors, arXiv version, abstract, submission date, subjects, and DOI link. | Primary metadata; high confidence. |
| E2 | https://arxiv.org/html/1503.07104 | Full paper sections, measurement setup, model definitions, algorithms, figures/captions, table values, and reported limitations-by-omission. | Primary full text; high confidence for reported claims. |
| E3 | https://arxiv.org/pdf/1503.07104 | Local PDF integrity and text cross-check; extracted PDF reports 23 pages, while the abstract page says 21 pages. | Primary artifact; high confidence for identity, medium for layout-dependent extraction. |
| E4 | https://doi.org/10.1109/TVT.2015.2487047 | Journal DOI and publication identity cross-check. | Near-primary publication locator. |
| E5 | https://dblp.org/rec/journals/tvt/AzmatCS16.html | Authors, journal, volume, issue, pages, year, and DOI bibliographic cross-check. | Independent bibliographic record; medium-high confidence. |
| E6 | `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` | Wireless ML, structured channel state, and online-learning bridge. | Related conceptual source; not independent validation. |
| E7 | `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md` | Sensing, sampling, resource, and edge-computation tradeoff bridge. | Related conceptual source; not independent validation. |
| E8 | `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md` | Joint sensing/communication allocation, detector quality, and simulation-only safety boundary. | Related conceptual source; not independent validation. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` - overlaps through wireless machine learning and the need to represent structured channel state rather than flattening it. The source basis is the inspected manuscript's discussion of delay-Doppler geometry, online learning, and simulation-to-deployment limits.
2. `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md` - overlaps through sensing validity, sampling cadence, wireless transmission, and resource-aware decision quality. Its source basis is the manuscript's AoI-energy formulation and explicit distinction between scenario-specific simulation thresholds and general deployment claims.
3. `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md` - overlaps through joint sensing/communication allocation, detector quality, power constraints, and simulation-only evaluation. Its source basis is the manuscript's mode-selection and fusion analysis with an explicit no-live-radio boundary.

## Synthesis Note

### Concept Bridge

The selected paper treats occupancy classification as a compact state-estimation problem: thresholded measurements become features, a classifier predicts primary-user status, and the prediction is translated into a secondary-user outage estimate. The related DEP entries extend the same bridge in three directions: structure-aware representation for wireless state, freshness and energy costs around sensing, and coupled sensing/communication allocation. The reusable lesson is to keep measurement context, decision uncertainty, resource cost, and authority boundaries attached to the prediction rather than treating accuracy as a standalone product metric.

### Potential Implementations

1. **Public spectrum-occupancy benchmark:** compare thresholding, NBC, SVM, SVM+FFA, and a temporal baseline on synthetic multi-band traces with versioned splits, calibrated probabilities, and an outage-oriented metric.
2. **Edge sensing quality monitor:** run a local-only classifier on authorized, anonymized receiver summaries and surface occupancy confidence, drift alerts, and abstentions to an operator without issuing radio commands.
3. **Simulation-gated allocation advisor:** combine predicted occupancy with sensing quality and power constraints to produce ranked, human-approved allocation proposals in a digital twin or hardware-in-the-loop environment.

### Deeper Relationship Observations

1. **State representation is the common hinge:** the paper's frequency-bin vector, 2D-RC's delay-Doppler structure, and ISAC's effective sensing set all show that the representation determines what the learner can preserve.
2. **Decision quality is multi-objective:** classification accuracy alone misses outage, freshness, energy, interference, and computation cost; the related entries make those downstream costs explicit.
3. **Authority must remain separate from inference:** all three bridges support a staged pattern in which models emit evidence and proposals, while validation, authorization, rollback, and live control remain outside the research classifier.

### Conceptual Similarities

1. Each artifact turns noisy wireless observations into a lower-dimensional state used for a later decision.
2. Each artifact treats operating conditions, thresholds, or constraints as part of the evaluation rather than as universal constants.
3. Each artifact benefits from reproducible simulation before any field or live-network claim is made.

### MVP Implementations with Code Mock-ups

1. **Synthetic occupancy feature extractor.** This toy example uses only generated power values and demonstrates the threshold-to-occupancy transformation; it does not read a radio or external signal.

```python
from statistics import mean

def occupancy(power_rows, threshold):
    return [mean(value > threshold for value in row) for row in power_rows]

synthetic_power = [[-90, -80, -105], [-110, -108, -107]]
print(occupancy(synthetic_power, -100))
```

2. **Auditable two-centroid classifier.** This bounded baseline makes the prediction rule visible and can be replaced by a version-pinned library model after benchmark design and calibration review.

```python
from math import dist

def nearest_centroid(train_rows, labels, row):
    centroids = {}
    for label in sorted(set(labels)):
        members = [x for x, y in zip(train_rows, labels) if y == label]
        centroids[label] = [sum(col) / len(col) for col in zip(*members)]
    return min(centroids, key=lambda label: dist(row, centroids[label]))

rows = [[1, 1, 0], [1, 0, 1], [0, 0, 0], [0, 1, 0]]
labels = [1, 1, 0, 0]
print(nearest_centroid(rows, labels, [1, 0, 0]))
```

3. **Outage metric harness.** The harness evaluates a predicted binary sequence against a required free-slot run length; it is a metric sandbox, not an allocation or transmission controller.

```python
def outage_probability(predicted_free, required_run):
    if required_run <= 0:
        raise ValueError("required_run must be positive")
    has_run = any(
        all(predicted_free[i:i + required_run])
        for i in range(len(predicted_free) - required_run + 1)
    )
    return 0.0 if has_run else 1.0

print(outage_probability([False, True, True, False], 2))
```

All three mock-ups use synthetic inputs, standard-library dependencies, no credentials, no private data, and no live radio authority. Production use would require calibration, access control, monitoring, tests, and an explicit safety review.

### Developer Challenges

1. Build a leakage-resistant benchmark that keeps temporal order, band identity, receiver context, and threshold selection visible while supporting repeated-seed evaluation.
2. Add calibrated uncertainty, abstention, drift detection, and asymmetric PU-protection costs without obscuring the original classifier comparison.
3. Keep inference local or privacy-preserving and enforce a hard separation between prediction, simulation, human approval, and radio-control systems.

### Author Challenges

1. Release a redacted or synthetic companion dataset, preprocessing details, parameter files, and executable evaluation code sufficient to reproduce the tables.
2. Report confidence intervals, repeated runs, class balance, calibration, hardware/runtime conditions, and cross-band or cross-location validation.
3. Clarify threshold selection, the trained-HMM variant, the apparent page-count/version differences, and the conditions under which SVM+FFA's added compute is justified.

## Validation Notes

- Local source integrity: PDF 422,127 bytes, `%PDF-` header, trailing `%%EOF`; full-paper HTML 223,505 bytes, 45,083 body characters after script/style removal, four document markers, 71 section/heading markers, six paper-structure term classes, and zero `.part` files.
- Review completeness: full-paper HTML and PDF text were inspected; PDF raster rendering was unavailable because Poppler tools were not present, so layout-dependent claims are treated cautiously.
- Source package: unavailable through the brokered redirect policy; no source package was uploaded or attached.
- Public-safety: no local absolute paths, usernames, machine names, local timezone labels, exact local execution timestamps, PDFs, HTML, source archives, caches, or extracted source text appear in the intended public artifact set.
- Staging allowlist: only generated `.logs`, `.reports`, `.lake-data` Markdown artifacts are intended for commit; no `.source/` directory is created.

## Attribution Block

- Source URL: https://arxiv.org/abs/1503.07104
  - Applies to: `Report-Mark.md`
  - Notes: Primary metadata, abstract, authors, submission date, category, and arXiv identifier.
- Source URL: https://arxiv.org/html/1503.07104
  - Applies to: `Report-Mark.md`
  - Notes: Full-paper method, evaluation, figures/captions, table values, and references; local copy withheld.
- Source URL: https://arxiv.org/pdf/1503.07104
  - Applies to: `Report-Mark.md`
  - Notes: Primary PDF integrity and text cross-check; local copy withheld.
- Source URL: https://doi.org/10.48550/arXiv.1503.07104
  - Applies to: `Report-Mark.md`
  - Notes: Persistent arXiv-issued DOI.
- Source URL: https://doi.org/10.1109/TVT.2015.2487047
  - Applies to: `Report-Mark.md`
  - Notes: Journal publication locator.
- Source URL: https://dblp.org/rec/journals/tvt/AzmatCS16.html
  - Applies to: `Report-Mark.md`
  - Notes: Bibliographic cross-check for the journal record.
- Repository file: `Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md`
  - Applies to: `Report-Mark.md`
  - Notes: Related wireless-ML conceptual bridge; not independent validation.
- Repository file: `Black-Lake/.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md`
  - Applies to: `Report-Mark.md`
  - Notes: Related sensing/resource conceptual bridge; not independent validation.
- Repository file: `Black-Lake/.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md`
  - Applies to: `Report-Mark.md`
  - Notes: Related joint sensing/communication conceptual bridge; not independent validation.
- Source-file policy: original PDF, full-paper HTML, metadata HTML, acquisition records, extracted text, caches, and unavailable source package were withheld locally.
  - Applies to: the entire report.
  - Notes: No source file was uploaded, staged, committed, copied, or attached.
