# Report-Mark: Joint Sensing MEC

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Joint Optimization of Sensing and Computation for Status Update in Mobile Edge Computing Systems* |
| Authors | Yi Chen; Zheng Chang; Geyong Min; Shiwen Mao; Timo Hämäläinen |
| arXiv | arXiv:2210.17025v1; submitted 2022-10-31 |
| arXiv URL | https://arxiv.org/abs/2210.17025 |
| Journal | *IEEE Transactions on Wireless Communications*, 22(11), 8230-8243, November 2023 |
| Journal DOI | https://doi.org/10.1109/TWC.2023.3261338 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2210.17025 |
| Primary review basis | Integrity-verified PDF, full-paper HTML, metadata HTML, TeX/source extraction, and key published-version sections |
| Local source state | Initially partial; repaired to complete before review |
| Cache state | Initial miss; final `cached` with PDF, HTML, and source text |
| Code status | No official implementation found in targeted arXiv, web, and GitHub searches; absence is not proven |
| Source locality | All source files and extracted text withheld locally; no `.source/` directory |

## Concise Research Notes

The paper models an MEC-assisted IoT loop in which periodic sampling, repeated sensing, wireless transmission, and local/edge processing jointly determine freshness and energy. A sensing attempt succeeds with a distance-dependent probability. Repeating sensing raises validity but consumes time and energy. Because validity is discovered after processing, failed sensing forces another sensing-processing cycle.

The analytical hinge is average AoI: under periodic independent generation, it is half the sampling interval plus one-attempt processing time divided by sensing-success probability. The total cost adds energy per unit time, then optimizes sampling interval, sensing repetitions, and binary offloading choices subject to freshness, sensing-time, and MEC-capacity constraints.

MISCO decomposes the NP-hard mixed problem into a closed-form sampling update, bounded sensing enumeration, and potential-game best response for offloading. The journal version frames the outer loop as block coordinate descent. Monotonic cost reduction and a lower bound support termination at a stable point, but do not establish a global optimum.

The source-reported simulations show lower weighted cost for MISCO than the tested baselines. They also report scenario-dependent crossovers near a sensing-success threshold of `0.65-0.7` and a minimum sampling interval of `1.4 s`. These values should be treated as sensitivity observations for the paper's parameters, not portable deployment rules.

## Evidence and Attribution

| ID | Evidence | Supports | Assessment |
|---|---|---|---|
| E1 | arXiv metadata, DOI, author-hosted journal article, author publication list | Identity, chronology, venue, pages, DOI | High confidence |
| E2 | Full arXiv PDF/HTML/source, Sections III-V and equations 1-29 | Sensing, transmission, computation, AoI, energy, constraints | High confidence for source reporting |
| E3 | Full arXiv paper and published version, Algorithms 1-3 and appendices | Decomposition, potential game, complexity, convergence | Medium-high; not independently proved |
| E4 | Simulation setup and Figures 4-10 | Baseline trends and threshold observations | Medium; no reproduction, seeds, or uncertainty |
| E5 | Cache public summary and integrity checks | Complete-source review coverage | High; local files withheld |
| E6 | Three related Black Lake manuscripts | Conceptual bridge | Medium-high; not validation evidence |

Primary public locators are https://arxiv.org/abs/2210.17025, https://arxiv.org/pdf/2210.17025, https://ar5iv.labs.arxiv.org/html/2210.17025, https://arxiv.org/e-print/2210.17025, and https://doi.org/10.1109/TWC.2023.3261338. The ar5iv endpoint is an approved full-paper fallback used because official arXiv HTML was unavailable for this paper.

## Related DEP Entries

Exactly three entries were selected on concrete conceptual overlap:

1. [Self-Learned IDC DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Self%20Learned%20IDC/self_learned_idc_manuscript.md)
   - Repository path: `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md`
   - Relevance: connects camera/radar/LiDAR observations, state representation, and measured control latency to constrained decisions. It extends AoI from network freshness into state-to-action freshness.
   - Source basis: the DEP's inspected arXiv HTML/source and source-reported SUMO results for arXiv:2110.12359.

2. [RRT-CBF Motion DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md)
   - Repository path: `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md`
   - Relevance: treats state age, solver feasibility, barrier margins, latency, and fallback as evidence for control safety. It supplies hard admissibility concerns missing from a weighted AoI-energy objective.
   - Source basis: the DEP's complete 20-page arXiv review of arXiv:2410.00343 and simulation evidence.

3. [iKalibr Calibration DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md)
   - Repository path: `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`
   - Relevance: shows that timestamps and spatial calibration are upstream prerequisites for meaningful freshness. Its progressive parameter batches also provide a concrete comparison to decomposed iterative optimization.
   - Source basis: the DEP's verified PDF/HTML/source review, journal metadata, and official implementation inspection for arXiv:2407.11420.

## Synthesis Note

### Concept Bridge

The selected paper asks when an observation should be sampled, how much sensing effort should be spent, and where its computation should run. The related entries expose the assumptions beneath and beyond that scheduler. iKalibr asks whether sensor frames and clocks are coherent; Self-Learned IDC asks how the resulting observations become an actionable state; RRT-CBF asks whether a fresh proposed action is admissible and what happens when the solver or state is stale. The full bridge is therefore `calibrate -> sense -> validate -> schedule/process -> represent state -> constrain action -> record fallback`.

The paper's weighted AoI-energy cost is valuable at the scheduling layer, but a dependable system needs hard boundaries too: maximum allowed state age, valid calibration version, minimum sensing confidence, capacity/admission policy, solver deadline, and fallback. Those boundaries should be logged alongside the average objective so reviewers can detect rare but unsafe failures.

### Potential Implementations

1. **Freshness-energy evidence ledger:** Replay synthetic/public device traces and preserve every sampling, sensing-repeat, offload, admission, and fallback decision with its AoI and energy components.
2. **Small-population offloading oracle:** Compare best-response equilibria with exhaustive global optima for small `N`, exposing local-solution gaps and update-order sensitivity.
3. **Calibration-aware edge gate:** Refuse edge-computed actions when observations exceed an age bound, sensing confidence is too low, calibration metadata is stale, or the edge result misses its deadline.

### Deeper Relationship Observations

1. **Freshness depends on coordinate integrity:** AoI can be numerically small while an observation is unusable because its clock offset or spatial transform is wrong. iKalibr makes calibration version and timestamp uncertainty part of the freshness evidence.
2. **Average cost and hard safety serve different roles:** MISCO trades time against energy, whereas RRT-CBF motivates non-negotiable admissibility and fallback. A deployment should use weighted optimization inside hard freshness/safety envelopes.
3. **State representation is a downstream consumer of scheduling:** Self-Learned IDC pools variable actors into a fixed state. If an edge scheduler drops or delays an observation, it changes the participant set and therefore the controller state, not merely network performance.

### Conceptual Similarities

1. All four works decompose a difficult coupled system into inspectable stages rather than optimize an opaque end-to-end objective without structure.
2. All four depend on iterative refinement or repeated updates whose validity rests on state quality, convergence conditions, and bounded latency.
3. All four translate physical-system uncertainty into an intermediate mathematical representation: sensing probability, calibrated residual, set-encoded state, or barrier margin.

### MVP Implementations with Code Mock-ups

1. **AoI cost checker**

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class UpdateCase:
    sampling_interval_s: float
    one_attempt_processing_s: float
    sensing_success: float
    energy_per_update_j: float
    time_weight: float
    energy_weight: float


def checked_cost(case: UpdateCase) -> float:
    if case.sampling_interval_s <= 0 or not 0 < case.sensing_success <= 1:
        raise ValueError("invalid interval or sensing probability")
    aoi = 0.5 * case.sampling_interval_s + (
        case.one_attempt_processing_s / case.sensing_success
    )
    energy_rate = case.energy_per_update_j / case.sampling_interval_s
    return case.time_weight * aoi + case.energy_weight * energy_rate
```

The mock-up is a dimensional smoke test, not a complete MISCO implementation. Dependencies: Python 3 standard library. Failure modes include inconsistent units and invalid probabilities.

2. **Fresh-state authorization gate**

```python
def authorize_edge_result(
    observation_age_s: float,
    result_age_s: float,
    confidence: float,
    calibration_current: bool,
    max_age_s: float,
) -> tuple[bool, str]:
    if not calibration_current:
        return False, "stale_calibration"
    if confidence < 0.9:
        return False, "low_sensing_confidence"
    if max(observation_age_s, result_age_s) > max_age_s:
        return False, "stale_state"
    return True, "accepted_for_simulation"
```

This gate fails closed and is simulation-only. It does not authorize live vehicle, robot, or infrastructure control.

3. **Small offloading equilibrium audit**

```python
def best_response(initial, device_cost, max_rounds=100):
    state = list(initial)
    history = [tuple(state)]
    for _ in range(max_rounds):
        changed = False
        for i in range(len(state)):
            local = device_cost(i, 0, tuple(state))
            edge = device_cost(i, 1, tuple(state))
            choice = int(edge < local)
            if choice != state[i]:
                state[i] = choice
                history.append(tuple(state))
                changed = True
        if not changed:
            return tuple(state), history
    raise RuntimeError("bounded convergence check failed")
```

The caller must supply a deterministic toy cost function and compare the result with exhaustive enumeration for small populations. It is not a network-control component.

### Developer Challenges

1. Reconstruct the exact objective and improvement equations with unit tests despite typography/extraction ambiguity and no official code.
2. Build deterministic queue, channel, sensing, and energy models without silently importing assumptions that make MISCO look artificially strong.
3. Preserve tail latency, fairness, fallback, calibration, and hard freshness evidence while keeping exported artifacts public-safe and source-local.

### Author Challenges

1. Clarify whether MISCO is claimed to reach a global optimum, coordinate-wise stationary point, or Nash-stable local solution, and publish a checked derivation of the improvement term.
2. Release code, raw figure values, deterministic seeds, configuration files, and an executable journal/preprint version map.
3. Validate the approach under correlated sensing failures, bursty queues, time-varying channels, heterogeneous deadlines, and measured device/server energy.

## Validation Notes

- Uniform selection used one of 75,776 PDF-parent paper units and zero-based index 7,665; the first draw was eligible with zero exclusions and zero reselections.
- Dedup checks covered the public index, Black Lake logs/reports/DEPs, automation memory, relevant Black-Lake-Data searches, DOI, normalized title, slug, and recent worktree markers. No prior marker remained after the private repair input was removed.
- The source-integrity gate initially classified the paper unit as `partial`. Review stopped until the archive was repaired and verified `complete`.
- The 803,785-byte PDF begins `%PDF-`, contains trailing `%%EOF`, and matched the downloaded PDF hash exactly.
- The 1,182,606-byte full-paper HTML contains 120,156 body characters, a document marker, 77 heading/section markers, and seven paper-structure terms.
- Metadata HTML and TeX source were collected locally. No partial files remained.
- Cache status changed from miss to `cached`; `pypdf`, HTML-regex, and tar extraction all succeeded. `pypdf` was the fallback because `pdftotext` was unavailable.
- Manuscript title/front matter, required headings, exactly three exercise paths, related-entry count, and source-locality statement were checked before submission.
- Original paper/source files, extracted text, and caches were withheld. No source file was uploaded, staged, copied into the DEP, or attached to Slack.

## Attribution Block

- Primary paper and metadata: https://arxiv.org/abs/2210.17025; https://arxiv.org/pdf/2210.17025; https://ar5iv.labs.arxiv.org/html/2210.17025; https://arxiv.org/e-print/2210.17025
- Persistent and published identifiers: https://doi.org/10.48550/arXiv.2210.17025; https://doi.org/10.1109/TWC.2023.3261338
- Published-version and author metadata: https://www.eng.auburn.edu/~szm0001/papers/TWC2023Chen.pdf; https://www.eng.auburn.edu/~szm0001/publications-bib.html
- Repository authorities: https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md; https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
- Related synthesis: `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`
- Original source files were withheld locally and were not uploaded, staged, attached, or deposited.
