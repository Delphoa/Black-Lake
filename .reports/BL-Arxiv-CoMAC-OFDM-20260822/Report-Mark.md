# BL-Arxiv-CoMAC-OFDM-20260822

## Source Metadata

- Title: *Computation over Wide-Band MAC: Improved Achievable Rate through Sub-Function Allocation*.
- Published title: *Computation over Wide-Band Multi-Access Channels: Achievable Rates Through Sub-Function Allocation*.
- Authors: Fangzhou Wu, Li Chen, Nan Zhao, Yunfei Chen, F. Richard Yu, and Guo Wei.
- Version/date: arXiv:1806.08632v1, submitted 2018-06-22.
- Identifiers: arXiv DOI 10.48550/arXiv.1806.08632; IEEE DOI 10.1109/TWC.2019.2918145; IEEE Transactions on Wireless Communications 18(7), 3713-3725.
- Evidence status: complete local PDF and full-paper HTML verified; source files withheld locally.

## Concise Research Notes

The paper targets computation over a wideband fading multi-access channel, where conventional CoMAC rates can vanish as node count grows and frequency-selective fading makes a single narrowband treatment insufficient. It maps OFDM's sub-carriers to function computation by dividing a desired function into `B=K/M` sub-functions, allocating each sub-function to sub-carriers whose `M` participating nodes have the strongest channel gains, and reconstructing the full function at the fusion center. Nested lattice coding supplies the computation primitive. The paper derives a general rate, an average-power SFA rate, and a per-symbol convex power-allocation formulation whose KKT solution motivates the sponge-squeezing algorithm.

The simulations are qualitative but concrete: Fig. 4 studies rate against `M` and `N` for `K=128` and `P=10 dB`; Fig. 5 studies the optimal number of sub-functions as `K` grows, including `K=4000`; Fig. 6 compares conventional CoMAC, direct CoMAC-OFDM, opportunistic CoMAC, and SFA; Fig. 7 compares SFA with average versus optimal power allocation. The reported pattern is higher rate with more sub-carriers, non-vanishing behavior for SFA/opportunistic CoMAC as node count grows, and an additional gain from optimal power allocation. These are author-reported simulation findings, not an independent reproduction.

## Evidence and Attribution

| ID | Evidence | Attribution | Assessment |
|---|---|---|---|
| E1 | arXiv record identifies title, authors, v1 date, abstract, arXiv DOI, and related IEEE DOI. | Official arXiv metadata. | High for identity and metadata. |
| E2 | Introduction and Sections II-III define CoMAC, wideband fading, OFDM, computation rate, and the main rate expression. | Full-paper HTML/PDF. | High for transcription; formulas were not re-derived independently. |
| E3 | Sections IV-V describe function division/allocation/reconstruction, nested lattice coding, average power allocation, convex optimization, KKT levels, and sponge-squeezing. | Full-paper HTML/PDF. | High for method summary; implementation not executed. |
| E4 | Section VI and Figs. 4-7 report comparisons and qualitative trends under stated simulation settings. | Full-paper HTML/PDF. | Medium; measurements were not reproduced. |
| E5 | Related DEP entries establish neighboring AirComp, wireless channel-domain, and spectrum-allocation concepts. | Black Lake generated Markdown. | Medium; related artifacts are context, not independent proof. |

## Related DEP Entries

1. [Over-the-Air - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260815-Over-the-Air/over_the_air_manuscript.md) — direct conceptual bridge through AirComp/over-the-air signal superposition for distributed computation over wireless networks.
2. [2D-RC OTFS - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md) — method neighbor through wideband wireless channel structure, domain-aware processing, mobility, and simulation-based receiver evaluation.
3. [Hybrid Spectrum Markets - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260729-Hybrid%20Spectrum%20Markets/hybrid_spectrum_markets.md) — systems bridge through interference-constrained spectrum allocation, shadow-price reasoning, and explicit approximation/performance tradeoffs.

## Synthesis Note

### Concept Bridge

The selected paper turns a physical-layer bottleneck into a structured allocation problem: first choose which node subsets compute each function fragment, then assign those fragments to favorable sub-carriers, then spend power so the weakest participating node does not dominate the rate. The three related entries extend that bridge across abstraction levels: AirComp supplies the distributed-computation primitive, OTFS supplies a contrasting channel-domain representation, and spectrum markets supply a governance/allocation lens for scarce shared radio resources. The reusable design pattern is allocation with an explicit bottleneck, a rate/equity objective, and an auditable fallback when assumptions fail.

### Potential Implementations

1. **SFA rate simulator:** generate synthetic fading tensors, partition node sets into sub-functions, rank channel gains per sub-carrier, and report conservative computation-rate traces with assumptions and seeds.
2. **CSI-aware resource broker:** expose a bounded API that accepts authorized channel estimates and returns sub-function/sub-carrier assignments plus per-node power budgets, with infeasibility and stale-CSI abstention.
3. **Cross-layer evaluation harness:** compare CoMAC-OFDM SFA/OPA, AirComp aggregation, OTFS-style channel processing, and interference-aware allocation under matched bandwidth, latency, energy, and fairness budgets.

### Deeper Relationship Observations

1. The common object is not merely a channel or a scheduler; it is a constrained mapping from distributed participants to shared physical resources, with the minimum effective participant quality controlling the result.
2. The selected paper's sub-function partitioning is a physical-layer analogue of decomposition: it converts one hard global computation into smaller pieces that can be placed where the channel is favorable, while the related market work shows that approximate placement itself needs an explicit welfare/error account.
3. AirComp and CoMAC exploit superposition for computation, whereas 2D-RC OTFS exploits structured channel interaction for detection; together they suggest that representation and allocation should be co-designed rather than optimized in isolation.

### Conceptual Similarities

1. All four artifacts treat channel/resource conditions as first-class inputs rather than noise to be hidden from the algorithm.
2. All four use structured decomposition or allocation to manage scale: sub-functions, domain-aware channel structure, distributed aggregation, or market allocations.
3. All four require simulation/evaluation evidence to be separated from deployment claims because real-world synchronization, CSI, interference, and distribution shift remain material uncertainties.

### MVP Implementations with Code Mock-ups

1. **Synthetic sub-function rate calculator.** This toy sketch ranks nodes per sub-carrier and computes a conservative SFA-style rate; it is not a reproduction of the paper.

```python
import math


def toy_sfa_rate(channel_power, participants, noise_floor=1.0):
    """Synthetic-only rate proxy; channel_power[subcarrier][node]."""
    total = 0.0
    for gains in channel_power:
        weakest = min(gains[node] for node in participants)
        total += max(0.0, math.log2(1.0 + weakest / noise_floor))
    return total / max(1, len(channel_power))
```

2. **Sub-function assignment audit.** This local-only sketch makes the allocation rule inspectable and returns an auditable mapping without touching live radio systems.

```python
def assign_subfunctions(channel_power, group_size):
    """Return strongest-node groups per synthetic sub-carrier."""
    assignments = []
    for subcarrier, gains in enumerate(channel_power):
        ranked = sorted(gains, key=gains.get, reverse=True)
        assignments.append({"subcarrier": subcarrier, "nodes": ranked[:group_size]})
    return assignments
```

3. **Bounded power-level mock-up.** This sketch performs a finite projected update for a toy per-node budget and should be tested only on synthetic values.

```python
def project_levels(levels, costs, budget, rounds=20):
    """Toy projected ascent for nonnegative shared power levels."""
    levels = [max(0.0, value) for value in levels]
    for _ in range(rounds):
        used = sum(level * cost for level, cost in zip(levels, costs))
        if used <= budget:
            break
        scale = budget / max(used, 1e-12)
        levels = [level * scale for level in levels]
    return levels
```

### Developer Challenges

1. Reproduce the paper's channel, OFDM, lattice-code, and figure-generation assumptions without silently changing normalization, bandwidth, or node-selection rules.
2. Design an allocator that detects stale or incomplete CSI, integer partition infeasibility, unequal power budgets, and fairness regressions before emitting a schedule.
3. Build cross-layer tests that compare rate gains against synchronization overhead, latency, energy, privacy leakage, interference, and hardware impairments.

### Author Challenges

1. Release reproducible code, seeds, parameter tables, and figure data for the SFA and sponge-squeezing experiments.
2. Extend evaluation beyond i.i.d. fading and idealized CSI to correlated channels, finite blocklength, imperfect synchronization, and heterogeneous nodes.
3. Clarify the operational boundary between an achievable-rate result and a deployable wideband CoMAC system, including latency, energy, security, and failure recovery.

## Validation Notes

- Source gate: initial partial unit repaired once; final PDF and full-paper HTML passed the required size, signature, body, document-marker, heading, and structure checks; no partial files remained.
- Public safety: no local absolute paths, usernames, machine names, local timezone labels, exact execution timestamps, PDFs, HTML, source archives, caches, extracted text, or private receipts are present in this artifact.
- Related-entry validation: exactly three existing mapped Series paths were used; no related material was fabricated.
- Code validation: three mock-ups use synthetic inputs, standard-library Python only, and no network, credential, radio-control, or consequential-decision behavior.

## Attribution Block

- Source URL: https://arxiv.org/abs/1806.08632
  - Applies to: source identity, authors, submitted date, abstract, and public metadata.
- Source URL: https://arxiv.org/html/1806.08632
  - Applies to: method, equations, simulations, conclusion, and references.
- Source URL: https://arxiv.org/pdf/1806.08632
  - Applies to: primary-paper integrity cross-check.
- Source URL: https://doi.org/10.1109/TWC.2019.2918145
  - Applies to: published-version identifier and bibliographic context.
- Related artifact URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260815-Over-the-Air/over_the_air_manuscript.md
  - Applies to: AirComp conceptual bridge only; related synthesis is not primary evidence.
- Related artifact URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md
  - Applies to: wideband channel-domain conceptual bridge only.
- Related artifact URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260729-Hybrid%20Spectrum%20Markets/hybrid_spectrum_markets.md
  - Applies to: allocation and approximation conceptual bridge only.
