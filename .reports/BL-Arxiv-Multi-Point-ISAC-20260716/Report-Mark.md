# Report-Mark: Multi-Point ISAC

## Source Metadata

- **Title:** *Multi-Point Integrated Sensing and Communication: Fusion Model and Functionality Selection*
- **Authors:** Guoliang Li; Shuai Wang; Kejiang Ye; Miaowen Wen; Derrick Wing Kwan Ng; Marco Di Renzo
- **arXiv:** [2208.07592v2](https://arxiv.org/abs/2208.07592v2)
- **arXiv DOI:** [10.48550/arXiv.2208.07592](https://doi.org/10.48550/arXiv.2208.07592)
- **Journal DOI:** [10.1109/LWC.2022.3213883](https://doi.org/10.1109/LWC.2022.3213883)
- **Dates:** submitted 2022-08-16; revised 2022-10-10
- **Venue:** *IEEE Wireless Communications Letters*, 11 (2022), 2660-2664
- **Primary full text:** [PDF](https://arxiv.org/pdf/2208.07592); [ar5iv full-paper HTML fallback](https://ar5iv.labs.arxiv.org/html/2208.07592); [source package](https://arxiv.org/e-print/2208.07592)
- **Local integrity:** repaired from partial to verified complete; PDF, full-paper HTML, metadata, and source package inspected; source files withheld locally
- **Code:** no official implementation repository identified in the inspected primary sources

## Concise Research Notes

The paper assigns each distributed dual-functional radar a binary sensing/communication mode, filters sensing devices by a 30 dB SINR threshold tied to an 89% detector-accuracy threshold, fuses effective binary detections with an optimized `n`-out-of-`N` vote, and jointly allocates mode and transmit power. Its tractable pipeline combines zero-forcing, an averaged false-negative/false-positive binomial surrogate, a closed-form approximate voting threshold, and hybrid neighborhood search with CVXPY power allocation.

The six-device ray-tracing simulation reports fusion gains over single-device ISAC and a better rate/accuracy trade-off than an all-sensing multi-radar baseline. The most valuable systems insight is negative: adding a remote sensor can hurt both objectives by consuming power and degrading other sensors' SINR. The important boundary is that the evidence is simulated, errors are assumed independent across views, zero-forcing is an asymptotic approximation, and the algorithm reaches a local optimum of a surrogate objective.

## Evidence and Attribution

| Evidence | Supports | Confidence | Boundary |
|---|---|---|---|
| Full TeX/HTML Sections II-III and Appendix A | signal model, fusion equation, surrogate bound, voting threshold, and HMO mechanism | High for source reporting | derivations not independently re-proved |
| Figures 2-4, captions, and Section IV | detector threshold, six-view scenario, baselines, trade-off behavior | Medium | figures not digitized; experiments not rerun |
| arXiv metadata and university publication record | identity, dates, venue, pages, journal DOI | High | publication metadata does not validate experiments |
| Local verification and cache summaries | complete review gate and extraction coverage | High | private source material is not deposited |

All claims above are paraphrases or reviewer interpretations tied to inspected evidence. Public repository artifacts contain generated Markdown and public URLs only.

## Related DEP Entries

1. [Joint Sensing MEC](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Joint%20Sensing%20MEC/joint_sensing_mec_manuscript.md) - shares mixed discrete/continuous allocation across sensing and another constrained service objective.
2. [2D-RC OTFS](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md) - connects learned wireless detection quality to representations that preserve physical signal geometry.
3. [Telecom AI Roadmap](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Telecom%20AI%20Roadmap/telecom_ai_roadmap_manuscript.md) - supplies operational guardrails needed before an optimized policy can influence a network.

## Synthesis Note

### Concept Bridge

MPISAC turns distributed perception into a resource-allocation problem: observations are useful only when signal quality, model error, fusion policy, communication opportunity cost, and power budget are considered together. Joint Sensing MEC shows the same coupling at a slower scheduling layer; 2D-RC OTFS shows that detector quality depends on honoring signal geometry; Telecom AI Roadmap shows why a candidate optimizer must remain behind typed validation, simulation, approval, telemetry, and rollback gates.

### Potential Implementations

1. Build a simulation-only mode-allocation auditor that compares exhaustive search, HMO, and simple heuristics on small synthetic networks.
2. Build a fusion-calibration workbench that tests optimal voting under heterogeneous, correlated, and drifting detector errors.
3. Build a guarded MPISAC policy service that emits proposals plus evidence, constraint checks, and rollback plans without directly controlling radios.

### Deeper Relationship Observations

1. A sensor's marginal value is endogenous: switching one device changes its own role, interference, the effective fusion set, and every remaining device's resource share.
2. Fusion quality and freshness share a common failure mode: optimizing a proxy average can hide tail cases where a view is stale, correlated, or systematically wrong.
3. Domain-aware learning and resource allocation are compositional only if detector calibration is versioned; otherwise the optimizer acts on obsolete error rates.

### Conceptual Similarities

1. MPISAC and Joint Sensing MEC both decompose a mixed discrete/continuous objective into tractable conditional updates.
2. MPISAC and 2D-RC OTFS both translate physical-channel quality into learned detection performance rather than treating inference as channel-independent.
3. MPISAC and Telecom AI Roadmap both require a separation between policy proposal and authorized network execution.

### MVP Implementations with Code Mock-ups

1. **Exact small-network voting audit**

```python
from itertools import combinations

def false_event_sum(rates, count):
    total = 0.0
    for chosen in combinations(range(len(rates)), count):
        selected = set(chosen)
        term = 1.0
        for i, rate in enumerate(rates):
            term *= rate if i in selected else 1.0 - rate
        total += term
    return total

def balanced_accuracy(false_negative, false_positive, threshold):
    n = len(false_negative)
    normal_correct = sum(false_event_sum(false_negative, k) for k in range(threshold))
    abnormal_correct = sum(false_event_sum(false_positive, k) for k in range(n - threshold + 1))
    return 0.5 * (normal_correct + abnormal_correct)
```

2. **Correlation stress ledger**

```python
def group_failures(records, window_id):
    grouped = {}
    for row in records:
        key = (window_id(row), row["truth"])
        grouped.setdefault(key, []).append(row["errors"])
    return grouped

def pairwise_joint_error(grouped, a, b):
    pairs = [(errors[a], errors[b]) for rows in grouped.values() for errors in rows]
    return sum(x and y for x, y in pairs) / max(1, len(pairs))
```

3. **Proposal-only allocation gate**

```python
def propose_allocation(candidate, limits, evidence):
    violations = []
    if sum(candidate["power_mw"]) > limits["sum_power_mw"]:
        violations.append("sum_power")
    if any(p > limits["device_power_mw"] for p in candidate["power_mw"]):
        violations.append("device_power")
    if evidence["calibration_age_hours"] > limits["max_calibration_age_hours"]:
        violations.append("stale_calibration")
    return {"authorized": False, "candidate": candidate, "violations": violations}
```

### Developer Challenges

1. Reproduce exact heterogeneous voting and the surrogate without numerical instability or off-by-one threshold errors.
2. Keep channel estimates, detector calibration, mode choices, and power constraints version-aligned across a distributed system.
3. Demonstrate fail-closed behavior when calibration is stale, devices disappear, or the solver returns an infeasible candidate.

### Author Challenges

1. Release a pinned simulator, detector data, seeds, optimization code, and raw result tables sufficient for independent reproduction.
2. Evaluate correlated sensing errors, channel-estimation uncertainty, mobility, and time-varying targets rather than independent stationary views alone.
3. Quantify the separate and compounded gaps introduced by zero-forcing, binomial averaging, and local surrogate optimization.

## Validation Notes

- Uniform selection: first draw from 75,776 paper units; zero exclusions and zero reselections.
- Dedup: arXiv ID, DOI, normalized title, slug, repository artifacts, memory, and recent markers checked before acceptance.
- Source gate: PDF and full-paper HTML passed size, structure, and completeness checks; the HTML used an approved ar5iv fallback after official HTML was unavailable.
- Cache: initial miss; `missing-only` extraction succeeded via `pypdf`, `html-regex`, and `tarfile`.
- Manuscript and README: required schema and attribution sections generated; exact-count and code-syntax validation follow before submission.
- Source-upload gate: no `.source` directory is created; all original source and cache files remain local.

## Attribution Block

**Primary work:** Guoliang Li, Shuai Wang, Kejiang Ye, Miaowen Wen, Derrick Wing Kwan Ng, and Marco Di Renzo, *Multi-Point Integrated Sensing and Communication: Fusion Model and Functionality Selection*, arXiv:2208.07592v2, DOI 10.1109/LWC.2022.3213883. **Review and synthesis:** Codex for Delphoa Black Lake, 2026-07-16. Claims are attributed to the cited primary sources; reviewer interpretations are labeled. All PDF, HTML, metadata, source-package, cache, and extracted-text files were withheld locally, and no source files were uploaded.
