---
title: "Multi-Point ISAC - DEP-E"
generated_at: "2026-07-16 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of multi-point integrated sensing and communication, optimal voting, functionality selection, and beamforming."
source_status: "verified local PDF, full-paper HTML fallback, metadata HTML, and source package; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv v2 revised 2022-10-10; publication metadata cross-checked through 2026-07-16"
primary_url: "https://arxiv.org/abs/2208.07592v2"
stable_identifier: "arXiv:2208.07592v2; DOI 10.1109/LWC.2022.3213883"
confidence_summary: "High for identity and formulation; medium for performance and convergence claims because simulations were not reproduced and no official code was identified."
safety_scope: "research review and simulation-only wireless allocation; no live radio or network authority"
distribution_notes: "Generated Markdown and public URLs only; all source files, extracted text, and caches withheld locally."
---

# Multi-Point ISAC - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2208.07592v2 | https://arxiv.org/abs/2208.07592v2 | arXiv metadata and version history. | 2026-07-16 | Inspected |
| S2 | arXiv paper bundle | Primary paper | PDF, full-paper HTML, TeX source | arXiv:2208.07592v2 | https://arxiv.org/pdf/2208.07592; https://ar5iv.labs.arxiv.org/html/2208.07592; https://arxiv.org/e-print/2208.07592 | Verified private copies inspected; no source file redistributed. Official full-paper HTML was unavailable, so approved ar5iv was used. | 2026-07-16 | Fully inspected and integrity-verified |
| S3 | IEEE publication | Published record | DOI | IEEE WCL 11, 2660-2664; 10.1109/LWC.2022.3213883 | https://doi.org/10.1109/LWC.2022.3213883 | Publisher terms apply; used for publication identity. | 2026-07-16 | Metadata cross-checked |
| S4 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2208.07592 | https://doi.org/10.48550/arXiv.2208.07592 | Persistent arXiv locator. | 2026-07-16 | Verified |
| S5 | Extraction cache public summary | Processing evidence | Public-safe JSON summary | schema 1.0; status `cached` | Public URLs from S1-S2 | Local paths and extracted text withheld. | 2026-07-16 | PDF, HTML, and source extraction succeeded |
| S6 | Black Lake repository authorities | Deposition rules | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Public repository standards. | 2026-07-16 | Fetched and read |
| S7 | Joint Sensing MEC DEP-E | Related processed artifact | Markdown | DEP-E-20260715-Joint Sensing MEC | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Joint%20Sensing%20MEC/joint_sensing_mec_manuscript.md | Conceptual synthesis only. | 2026-07-16 | Inspected |
| S8 | 2D-RC OTFS DEP-E | Related processed artifact | Markdown | DEP-E-20260709-2D-RC OTFS | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md | Conceptual synthesis only. | 2026-07-16 | Inspected |
| S9 | Telecom AI Roadmap DEP-E | Related processed artifact | Markdown | DEP-E-20260711-Telecom AI Roadmap | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Telecom%20AI%20Roadmap/telecom_ai_roadmap_manuscript.md | Conceptual synthesis only. | 2026-07-16 | Inspected |

The authors are Guoliang Li, Shuai Wang, Kejiang Ye, Miaowen Wen, Derrick Wing Kwan Ng, and Marco Di Renzo. The arXiv record reports v1 on 2022-08-16 and v2 on 2022-10-10. The publication is listed in *IEEE Wireless Communications Letters*, volume 11, pages 2660-2664. No official implementation repository was identified in the inspected primary sources.

## Evidence Ledger

| ID | Source | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|
| E1 | S1, S3, S4 | metadata and identifiers | source identity and chronology | High | does not validate results |
| E2 | S2 | Sections II-III, equations 1-16, Proposition 1, Appendix A | signal/fusion models, surrogate, voting threshold, optimization | High for source reporting | derivations not independently reproduced |
| E3 | S2 | Section IV, figures 2-4, simulator setup, baselines | source-reported performance and trade-offs | Medium | no raw tables, code, seeds, or reruns |
| E4 | S2 | assumptions and algorithm discussion | independence, zero-forcing, local convergence, complexity | Medium-high | no dedicated limitations section |
| E5 | S5 | extractor status and output presence | source-review coverage | High | extracted typography can be noisy |
| E6 | S6 | withholding, naming, index, attribution rules | deposit compliance | High | process evidence only |
| E7 | S7-S9 | coupled allocation, wireless representations, guarded control | cross-DEP synthesis | Medium-high | does not validate this paper |
| E8 | dedup scans and memory | ID, DOI, title, slug, artifact, recent-marker searches | selection eligibility | High | depends on indexed text |

## Executive Summary

The paper proposes multi-point integrated sensing and communication (MPISAC): several dual-functional radars share hardware between target sensing and data communication while a fusion center combines binary detection outputs. A binary variable assigns each device to sensing or communication. Sensing devices count as effective only when their SINR meets a threshold; communication devices coherently serve one receiver.

The exact model computes balanced fusion accuracy for heterogeneous false-negative and false-positive rates under an optimized `n`-out-of-`N` vote. It combines fusion accuracy and communication rate with a weight `mu`. For tractability, the method uses zero-forcing, replaces heterogeneous errors with averages in a binomial surrogate, derives an approximate voting threshold, and searches binary-mode neighborhoods while solving power as a convex subproblem.

In a ray-traced six-device conference-room simulation, fusion reportedly improves detection over single-device ISAC and adaptive selection improves rate at a given accuracy. An all-sensing baseline can perform worse because remote devices consume power and reduce other sensors' SINR. The result usefully challenges the assumption that more sensing nodes necessarily improve cooperative perception.

Reviewer assessment: the model is compact and implementation-relevant, but its guarantees are narrow. Exact detector errors are assumed known and independent; the tractable objective is a surrogate; zero-forcing is generally suboptimal; HMO converges locally on that surrogate; and all empirical evidence is simulated. No official code or raw result bundle was identified.

## Detailed Summary

### System and Problem

The system contains `K` dual-functional radars, each with `M` transmit antennas and one receive antenna, one target, one communication receiver, and a wireline fusion center. Mode `x_i = 1` means sensing; `x_i = 0` means communication. Sensing and communication interfere, while beamformers obey per-device and total-power limits.

### Sensing and Fusion

Each sensing signal becomes a spectrogram and then a CNN anomaly decision. Based on a cited accuracy curve, the simulation uses `gamma = 30 dB`, associated with an 89% accuracy threshold, to exclude ineffective views. Effective devices send binary normal/abnormal decisions to the fusion center.

For threshold `n`, the center declares abnormal when at least `n` devices vote abnormal. Equation 5 enumerates subsets to compute balanced accuracy from each device's false-negative `P_i` and false-positive `Q_i`, assuming independent observations. The best exact vote maximizes this accuracy over `n`.

### Joint Objective and Approximation

Problem P0 jointly maximizes exact fusion accuracy and communication rate under mode, power, and effectiveness constraints. A weighted sum selects supported Pareto points. The authors argue that an optimally selected sensing device must meet the SINR threshold; otherwise switching it to communication leaves fusion unchanged and raises rate.

Zero-forcing separates beam direction, phase, and power. The exact heterogeneous-error fusion function is replaced by a binomial function using mean `P` and mean `Q`. Proposition 1 bounds the aggregated approximation gap through error-rate dispersion and gives an approximate threshold `ceil(N / (1 + alpha))`, capped by `N`. In the illustrated seven-device case, the optimum is three votes, not majority's four.

### HMO Algorithm

Hybrid meta-heuristic and optimization starts from a feasible mode vector and proposes neighbors by flipping up to `L` bits. For fixed modes it solves a convex power-allocation subproblem with CVXPY. Improving candidates advance the search. The paper claims a local optimum of the surrogate and complexity `O(Iter_bar K^3.5)`, not global optimality of the original problem.

### Simulation Evidence

The source simulates six devices in a `3 x 4.5 x 3 m^3` room. A ray-tracing radar simulator generates multi-view spectrograms for adult-versus-child anomaly detection. Stated parameters include `10 mW` per-device power, `50 mW` sum power, and `-50 dBm` noise.

View geometry matters: motion-aligned devices yield stronger spectrogram variation than orthogonal views. Fusion reportedly improves accuracy, but the gain disappears when the power budget cannot sustain multiple effective sensors. The all-sensing baseline has zero communication rate and can have worse sensing accuracy because remote radars drain power. Varying `mu` yields high-rate, high-accuracy, and balanced operating points.

## Key Claims and Evidence

| Claim | Evidence | Reviewer calibration |
|---|---|---|
| Optimized voting can outperform majority voting. | Proposition 1 and seven-device threshold 3 versus 4. | Strong within known, stable error rates. |
| Fusion improves detection over single-device ISAC. | Figure 4(a) and Section IV. | Simulation-only; not reproduced. |
| Functionality selection can improve rate at fixed accuracy. | MPISAC versus single-device ISAC. | Scenario-specific. |
| Selecting every radar for sensing can be worse. | All-sensing baseline and remote-device explanation. | Important qualitative result needing topology tests. |
| HMO converges locally. | Convex P4, improvement argument, and stated complexity. | Surrogate-local, not original-global. |

## Methodology

Uniform selection used 75,776 unique PDF-parent units enumerated with `rg --files -g "*.pdf"`; zero-based draw 53,616 was accepted. Dedup checks covered arXiv ID, arXiv DOI, journal DOI, normalized title, slug, repository artifacts, memory, recent work, and a targeted companion-repository search. No prior deposit was found.

The local unit was initially `partial`: its PDF was valid, but full-paper HTML was absent. A bounded repair requested official arXiv HTML, then used approved ar5iv when no full paper was returned. Metadata HTML and the source archive were collected. Verification confirmed a 1,345,194-byte PDF with header and EOF, 954,733-byte full HTML with 71,826 body characters, 32 headings, seven structure terms, a document marker, a nine-entry source archive, and zero partials.

The central cache was absent. `extract-arxiv` ran in `missing-only` mode and succeeded with `pypdf`, `html-regex`, and `tarfile`, producing 31,902, 58,990, and 41,816 bytes of text. Synthesis inspected the full paper, TeX, appendix, figures/captions, metadata, and exactly three related DEP manuscripts. Experiments were not run.

## Scope, Constraints, and Assumptions

- The task is binary adult-versus-child anomaly detection, not general semantic sensing.
- View errors are assumed independent and their rates known from experimental data.
- The 30 dB cutoff maps to a detector-specific 89% threshold.
- Weighted sums may miss non-convex Pareto regions.
- Zero-forcing is generally suboptimal; the asymptotic argument relies on many antennas.
- The surrogate collapses heterogeneous errors to means; its gap grows with dispersion.
- HMO is local for the surrogate.
- Evidence is simulation-only, without repeated-seed uncertainty, raw results, or official code.
- This artifact authorizes no live radio or network action.

## Observations

1. The effective fusion set is a decision outcome, not just the sensing-mode set.
2. A remote device may have negative marginal value when power and interference exceed information gain.
3. Voting calibration and mode selection are coupled because each mode changes voter identity.
4. The exact formulation is valuable as a small-system audit oracle.
5. Detector calibration should be versioned with channel regime, geometry, and model release.

## Considerations

- Stress-test correlated errors and calibration drift.
- Treat calibration age and uncertainty as constraints.
- Compare weighted sum with epsilon constraints and explicit Pareto enumeration.
- Report feasibility and solver failures, not only objectives.
- Add channel-estimation error, synchronization drift, mobility, blocked paths, and churn.
- Preserve proposal/execution separation.

## Strengths

- Couples sensing accuracy and communication rate in one model.
- Gives exact heterogeneous voting and a bounded tractable surrogate.
- Shows why majority vote and all-sensing allocation need not be optimal.
- Separates binary search from continuous power optimization.
- Includes proof, complexity, baselines, and an interpretable geometry example.

## Weaknesses

- Simulation-only evidence without code, raw tables, seeds, or reproduction.
- Independence and stationary-error assumptions are fragile.
- Detector threshold transfer is untested.
- Three approximation layers can compound.
- Weighted sum may miss parts of the frontier.
- No sensitivity study for channel estimation, synchronization, mobility, or failure.

## Potential Improvements

1. Release a pinned simulator, detector pipeline, seeds, configurations, and raw tables.
2. Evaluate exact and surrogate fusion under controlled correlation and drift.
3. Quantify each approximation gap against exhaustive small-system optimization.
4. Add uncertainty-aware SINR and detector constraints with abstention.
5. Compare weighted sum, epsilon constraints, and frontier enumeration.
6. Test randomized topology, mobility, churn, and non-binary tasks.
7. Add a guarded proposal interface with dry-run, authorization, telemetry, and rollback.

## Potential Implementations

### Voting and Surrogate Audit Harness

Enumerate exact heterogeneous voting for small device sets, compare it with the binomial surrogate and majority vote, and report threshold error, accuracy gap, error dispersion, and correlation sensitivity.

### MPISAC Pareto Sandbox

Generate synthetic channels and compare exhaustive allocation, HMO, greedy rules, random allocation, and all-sensing baselines. Emit rate, accuracy, feasibility, runtime, and approximation provenance.

### Guarded Allocation Proposal Service

Accept versioned channel estimates, detector calibration, power limits, and priorities; emit a proposal plus evidence and checks. It must never execute radio changes. Separate authorization would require freshness, simulation, approval, telemetry, and rollback.

## Three Ways to Exercise This Research

1. `Exact-vs-surrogate toy study`: enumerate exact subset probabilities for at most 12 synthetic devices and compare thresholds. Success means every result is recomputable; do not extrapolate to field performance.
2. `Small-network allocation benchmark`: compare exhaustive six-device modes with multiple HMO seeds and greedy baselines. Success requires pinned solver and seeds; stop on silently coerced infeasibility.
3. `Calibration fault injection`: feed stale, shifted, correlated, and missing synthetic calibration into a proposal-only allocator. Success means invalid cases fail closed; no live interface may be connected.

## Example MVP Product

**MPISAC Evidence Sandbox** helps a research team determine when fusion and mode selection improve a synthetic system. It accepts channel matrices, detector error rates with calibration dates, power limits, an SINR threshold, trade-off weights, and a seed. It validates units and freshness, compares exact and surrogate voting, runs exhaustive modes when feasible, runs HMO across pinned seeds, and renders a Pareto plot plus evidence ledger. Acceptance requires deterministic replay, explicit solver status, exact/surrogate labels, calibration warnings, complete configuration records, and zero radio-control capability.

## Related Research and Reading

### Exactly Three Related DEP Entries

1. [Joint Sensing MEC](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Joint%20Sensing%20MEC/joint_sensing_mec_manuscript.md) - mixed sensing/resource decisions and decomposed optimization.
2. [2D-RC OTFS](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md) - wireless-state geometry and channel-conditioned inference quality.
3. [Telecom AI Roadmap](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Telecom%20AI%20Roadmap/telecom_ai_roadmap_manuscript.md) - simulation and guarded network-policy execution.

### Primary and Near-Primary Reading

- Li et al., [arXiv:2208.07592v2](https://arxiv.org/abs/2208.07592v2) - selected primary work.
- Liu et al., [joint radar-communication beamforming](https://doi.org/10.1109/TSP.2021.3135692) - ISAC beamforming context cited by the paper.
- Yi and Chai, [heterogeneous multi-sensor fusion](https://doi.org/10.1109/TSP.2021.3085972) - fusion context cited by the paper.
- Aguileta et al., [activity-recognition fusion survey](https://doi.org/10.3390/s19173808) - multi-view activity context cited by the paper.

## Source References

1. Li et al. *Multi-Point Integrated Sensing and Communication: Fusion Model and Functionality Selection*. https://arxiv.org/abs/2208.07592v2
2. Full paper PDF. https://arxiv.org/pdf/2208.07592
3. Full-paper HTML fallback. https://ar5iv.labs.arxiv.org/html/2208.07592
4. arXiv source package. https://arxiv.org/e-print/2208.07592
5. Journal DOI. https://doi.org/10.1109/LWC.2022.3213883
6. arXiv DOI. https://doi.org/10.48550/arXiv.2208.07592
7. Black Lake authority. https://github.com/Delphoa/Black-Lake/blob/main/README.md
8. Black Lake DEP authority. https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md

## Appendix

### Replication Checklist

- Pin topology, antenna count, path-loss, and ray-tracing configuration.
- Publish spectrogram generation, CNN checkpoint, split, and per-view confusion matrices.
- Pin thresholds, power constraints, solver, tolerances, and HMO seeds.
- Compare exact fusion, surrogate fusion, and majority vote.
- Compare stronger beamforming with zero-forcing on small systems.
- Report exhaustive-search gaps, mobility, correlation, channel error, and failure tests.

### Process and Source Inventory

The first uniform draw from 75,776 unique units selected index 53,616 and was eligible. The archive was repaired from partial to complete with an approved HTML fallback, then cached in `missing-only` mode. All source and cache material remains outside the public repository.

### Source-Withholding Confirmation

No PDF, HTML, metadata page, TeX/source archive, figure, cache file, extracted source text, or local archive path is included. Only generated public-safe Markdown and public URLs are published.
