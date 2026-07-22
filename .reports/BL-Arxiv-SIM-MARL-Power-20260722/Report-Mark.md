# Report-Mark: SIM MARL Power

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Joint Power Allocation and Phase Shift Design for Stacked Intelligent Metasurfaces-aided Cell-Free Massive MIMO Systems with MARL* |
| Authors | Yiyang Zhu; Jiayi Zhang; Enyu Shi; Ziheng Liu; Chau Yuen; Bo Ai |
| Stable identifier | arXiv:2502.19675v1 |
| DOI | https://doi.org/10.48550/arXiv.2502.19675 |
| Submitted | 2025-02-27 |
| Subjects | Information Theory (`cs.IT`); Signal Processing (`eess.SP`) |
| Primary record | https://arxiv.org/abs/2502.19675v1 |
| Full-paper sources | https://arxiv.org/pdf/2502.19675; https://arxiv.org/html/2502.19675v1; https://arxiv.org/e-print/2502.19675 |
| Publication status | One arXiv version was visible; no journal reference or non-arXiv publisher DOI appeared in inspected metadata. |
| Code status | No official implementation link appeared in the paper or arXiv record; a bounded exact-title, ID, and method-name search found none. This is not proof of nonexistence. |

## Selection and Dedup Validation

- `Enumeration`: `rg --files -g "*.pdf"` found 75,780 PDFs, grouped into 75,777 unique PDF-parent paper units.
- `Dedup basis`: 1,100 normalized identifiers assembled from Black-Lake logs, reports, DEP entries, the public dedup index, automation memory, and relevant live Black-Lake-Data entries.
- `Exclusions`: 266 units matched known identifiers, leaving 75,511 eligible units.
- `Random method`: PowerShell `Get-Random` selected the first accepted rejection-sampling draw. The selected unit was zero-based index 38,440 in the canonical all-unit ordering and 38,300 in the fully reconciled eligible ordering.
- `Targeted validation`: exact arXiv ID, DOI, normalized title, `SIM-MARL-Power` slug family, owning artifacts, and recent same-paper markers produced no duplicate.
- `Reselections`: 0.

## Local Source Integrity

Initial state was `partial`: the existing PDF was valid, but full-paper HTML was absent. Review stopped while one bounded local-only repair preserved the PDF and collected full-paper HTML, metadata HTML, and the arXiv source package. The local README, attribution/provenance record, machine-readable summary, and verification report were updated.

Final state was `complete` before research review:

- PDF: 2,290,516 bytes, `%PDF-` header, trailing `%%EOF`, six parsed pages.
- Full-paper HTML: 459,959 bytes, 55,804 body characters after script/style removal, document marker present, 44 heading/section markers, and six structure terms.
- Metadata HTML: 42,116 bytes; treated as metadata only.
- Source package: 3,167,313 bytes and 15 readable entries.
- Partials: 0.
- Source policy: PDF, HTML, metadata, source, extracted material, render caches, and private verification records remain local. No source file was uploaded.

## Research Notes

The paper models a cell-free massive-MIMO downlink in which `L` distributed access points jointly serve `K` users. Each access point has `M_AP` active antennas and a stacked intelligent metasurface with `M` layers and `N x N` programmable meta-atoms. A product of propagation and diagonal phase matrices performs wave-domain beamforming. The objective maximizes total user spectral efficiency while respecting per-access-point power and continuous-phase constraints.

The authors map the coupled power-and-phase problem to a cooperative Dec-POMDP. Every access-point/metasurface pair is an agent. Training uses a shared actor and centralized critic, while execution uses local channel, power, and phase observations. NVR-MAPPO adds recurrent policy state and agent-specific Gaussian noise to the centralized value network, with periodic cross-agent noise shuffling to increase exploration.

The simulation covers a `100 m x 100 m` service region at 28 GHz, with `3 dBm` maximum transmit power per access point and `-96 dBm` noise power. Figure 3 uses 250 episodes and suggests faster early NVR-MAPPO convergence than MAPPO with more fluctuation. Figures 4-5 sweep metasurface layers and meta-atoms. Source prose reports at least `50%` improvement over a random-codebook plus water-filling baseline, at least `15%` over MADDPG in the layer sweep, and `9.8%` at `N = 64` meta-atoms. The conclusion separately states an approximately `18%` convergence advantage over MAPPO without defining the measure precisely.

The evidence boundary is material. No code, raw figure values, seed schedule, confidence intervals, complete hyperparameter manifest, hardware experiment, communication-cost measurement, or component ablation was identified. The source TeX contains an incomplete actor-loss expression. The abstract's “fully distributed” description is also broader than the centralized-training architecture actually documented.

## Evidence and Attribution

| Evidence ID | Basis | Finding | Calibration |
|---|---|---|---|
| E1 | arXiv metadata and DOI | identity, authors, date, subjects, and version | High confidence |
| E2 | complete PDF, HTML, and source TeX | system model, equations, NVR-MAPPO mechanism, and algorithm | High for transcription; not independently derived |
| E3 | Figures 3-5 and surrounding prose | convergence, layer, and meta-atom comparisons | Medium; simulation-only and not reproduced |
| E4 | source-code and algorithm audit | missing settings and malformed actor-loss expression | High for observed source state |
| E5 | focused public code search | no official implementation identified | Medium; bounded negative search |
| E6 | related DEP manuscripts | allocation, governance, and policy-regularization bridges | Medium-high; conceptual only |

## Related DEP Entries

1. [Multi-Point ISAC](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Multi-Point%20ISAC/multi_point_isac_manuscript.md) - distributed wireless coordination, coupled role/power allocation, and simulation evidence provide the closest non-RL systems comparison.
2. [Telecom AI Roadmap](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Telecom%20AI%20Roadmap/telecom_ai_roadmap_manuscript.md) - digital-twin testing, typed actions, authorization, monitoring, and rollback turn telecom AI into a guarded policy pipeline.
3. [GPMD Regularized RL](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md) - regularization geometry and explicit approximation-error floors sharpen the convergence questions left open by NVR-MAPPO.

## Validation Notes

- Live Black-Lake and Black-Lake-Data README requirements were fetched and read before drafting.
- Manuscript title and H1 match and are 22 characters, including spaces and punctuation.
- All required manuscript headings, evidence fields, exactly three exercise paths, MVP fields, source references, and appendices are present.
- DEP description `SIM MARL Power` is 14 characters and within the 25-character limit.
- Log and Synthesis Note exact-three contracts were checked structurally.
- Public artifacts use date-only execution markers and contain no local paths, usernames, machine identifiers, local timezone labels, or exact local execution timestamps.
- The public package contains Markdown only and no `.source/` directory.

## Synthesis Note

### Concept Bridge

The selected paper is best understood as a learned candidate-policy generator for a coupled wireless optimizer. Multi-Point ISAC shows that distributed wireless role and power decisions can also be decomposed with explicit optimization and local-convergence boundaries. GPMD shows how policy regularization can be tied to precise assumptions and error floors. Telecom AI Roadmap supplies the missing operational envelope: typed actions, digital-twin tests, authorization, monitoring, and rollback. Together they suggest a two-layer design in which learning proposes power/phase actions and a deterministic evidence gate decides whether those actions are feasible and trustworthy.

### Potential Implementations

1. **Seeded NVR-MAPPO reproduction harness** - recreate the published curves, isolate recurrence/noise/shuffling effects, and compare against optimization baselines using public or synthetic channels only.
2. **SIM command feasibility gate** - validate CSI age, power limits, phase quantization, calibration version, and fallback state before a modeled command is accepted.
3. **Wireless policy frontier explorer** - compare spectral efficiency, fairness, energy, latency, control traffic, and constraint failures across learned and deterministic policies.

### Deeper Relationship Observations

1. The centralized critic has a role analogous to the MPISAC fusion center: both aggregate distributed evidence during optimization, while their practical value depends on how much state must be communicated and how fresh it remains.
2. Noisy-value regularization is an empirical exploration device, whereas GPMD's regularizer defines the optimization geometry and theorem assumptions. Conflating the two would overstate NVR-MAPPO's guarantees.
3. Telecom AI governance changes the evaluation target from maximum average reward to an auditable action lifecycle. This exposes fairness, stale state, invalid phase commands, and rollback as first-class outcomes.

### Conceptual Similarities

1. All four artifacts optimize a shared objective over distributed actors or resources whose local choices interact through interference, fusion, or policy dynamics.
2. Each relies on a reduced representation of global state and therefore inherits errors from missing, stale, or approximated information.
3. Each benefits from separating proposal quality from authorization quality: a high-scoring candidate still needs feasibility, evidence, and failure-handling checks.

### MVP Implementations with Code Mock-ups

1. **Constraint-first action validator**

```python
def validate_action(power, phases, power_cap, phase_levels):
    if any(value < 0 for value in power) or sum(power) > power_cap:
        return {"accepted": False, "reason": "power_constraint"}
    if any(value not in phase_levels for value in phases):
        return {"accepted": False, "reason": "phase_constraint"}
    return {"accepted": True, "reason": "modeled_constraints_pass"}
```

This toy validator uses synthetic values and models only explicit constraints; it does not authorize hardware use.

2. **Stale-state gate**

```python
def gate_state(state_age_ms, calibration_ok, maximum_age_ms=50):
    if not calibration_ok:
        return "fallback:calibration"
    if state_age_ms > maximum_age_ms:
        return "fallback:stale_state"
    return "simulate:candidate_policy"
```

The output stays in simulation and makes fallback reasons observable.

3. **Seeded comparison reducer**

```python
def summarize_runs(rows):
    valid = [row for row in rows if row["constraints_ok"]]
    if not valid:
        return {"status": "no_valid_runs"}
    return {
        "status": "review",
        "mean_sum_se": sum(row["sum_se"] for row in valid) / len(valid),
        "valid_runs": len(valid),
    }
```

This intentionally reports valid-run count with the mean so constraint failures cannot disappear from the denominator.

### Developer Challenges

1. Reconstruct the missing reward, action parameterization, network architecture, optimizer settings, noise schedule, and corrected actor loss without silently changing the method.
2. Build numerically stable complex-valued channel and multilayer propagation calculations while preserving dimensions, units, and phase constraints.
3. Compare methods fairly across seeds, compute budgets, constraint handling, and strong optimization baselines without tuning only the proposed policy.

### Author Challenges

1. Publish a complete runnable artifact with raw curves, seeds, configuration manifests, corrected equations, and an explicit license.
2. Provide factorial ablations and statistical uncertainty that isolate noisy values, recurrence, noise shuffling, CTDE, and shared-network effects.
3. Test discrete phases, calibration drift, imperfect/stale CSI, fronthaul cost, fairness, outage, energy, and authorized hardware realism before making deployment claims.

## Attribution Block

- Source URL: https://arxiv.org/abs/2502.19675v1
  - Applies to: identity, metadata, version, abstract, and source policy.
  - Notes: Canonical arXiv record.
- Source URL: https://arxiv.org/pdf/2502.19675
  - Applies to: system model, method, figures, simulation claims, and limitations.
  - Notes: Complete PDF inspected privately and withheld locally.
- Source URL: https://arxiv.org/html/2502.19675v1
  - Applies to: full-text and structural cross-checking.
  - Notes: Complete HTML inspected privately and withheld locally.
- Source URL: https://arxiv.org/e-print/2502.19675
  - Applies to: source-level algorithm, equation, caption, and asset inspection.
  - Notes: Source package inspected privately and withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2502.19675
  - Applies to: persistent identity.
  - Notes: arXiv-issued DOI.
- Related source: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Multi-Point%20ISAC/multi_point_isac_manuscript.md
  - Applies to: distributed wireless allocation synthesis.
- Related source: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Telecom%20AI%20Roadmap/telecom_ai_roadmap_manuscript.md
  - Applies to: telecom AI operations and governance synthesis.
- Related source: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md
  - Applies to: policy-regularization and convergence synthesis.
