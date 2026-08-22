---
title: "CoMAC OFDM - DEP-E"
generated_at: "2026-08-22"
artifact_type: "DEP-E research artifact"
primary_subject: "Computation over Wide-Band MAC: Improved Achievable Rate through Sub-Function Allocation"
source_status: "complete local PDF and full-paper HTML verified; source files withheld locally"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-22"
stable_identifier: "arXiv:1806.08632v1; DOI:10.48550/arXiv.1806.08632; IEEE DOI:10.1109/TWC.2019.2918145"
selection_status: "Reserved by black-lake-arxiv-dep-v1; one paper selected"
distribution_notes: "Generated Markdown and public URLs only; source files, caches, extracted text, and private records withheld"
---

# CoMAC OFDM - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv metadata | Identity and provenance | HTML | arXiv:1806.08632v1 | https://arxiv.org/abs/1806.08632 | Metadata page; abstract evidence is incomplete for empirical claims. | 2026-08-22 | Inspected |
| S2 | arXiv full paper | Primary evidence | HTML | arXiv:1806.08632v1 | https://arxiv.org/html/1806.08632 | Full-paper HTML passed the local integrity gate; copy withheld. | 2026-08-22 | Inspected in full |
| S3 | arXiv PDF | Primary cross-check | PDF | arXiv:1806.08632v1 | https://arxiv.org/pdf/1806.08632 | PDF passed header/EOF/size checks; copy withheld. | 2026-08-22 | Integrity checked |
| S4 | IEEE published version | Bibliographic context | DOI | 10.1109/TWC.2019.2918145 | https://doi.org/10.1109/TWC.2019.2918145 | Related published-version identifier; publisher access was not treated as separate method evidence. | 2026-08-22 | Referenced |
| S5 | Over-the-Air - DEP-E | Related synthesis | Markdown | DEP-E Series 001 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260815-Over-the-Air/over_the_air_manuscript.md | Context only; no source file copied. | 2026-08-22 | Inspected |
| S6 | 2D-RC OTFS - DEP-E | Related synthesis | Markdown | DEP-E Series 001 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md | Context only; no source file copied. | 2026-08-22 | Inspected |
| S7 | Hybrid Spectrum Markets - DEP-E | Related synthesis | Markdown | DEP-E Series 001 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260729-Hybrid%20Spectrum%20Markets/hybrid_spectrum_markets.md | Context only; no source file copied. | 2026-08-22 | Inspected |

Authors: Fangzhou Wu; Li Chen; Nan Zhao; Yunfei Chen; F. Richard Yu; Guo Wei. Submitted 2018-06-22; published version is IEEE Transactions on Wireless Communications 18(7), 3713-3725 (2019).

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Official metadata | Title, authors, v1 date, abstract, arXiv DOI, related IEEE DOI, and source locators | Source identity and scope | High | Abstract is not sufficient for method or result claims. |
| E2 | S2/S3 | Primary paper | Introduction, CoMAC definitions, fading-MAC model, computation-rate definition, and Theorems 1-3 | Problem and rate framework | High for transcription | Formula equivalence was not independently re-derived. |
| E3 | S2/S3 | Primary paper | Sections IV-V: division/allocation/reconstruction, nested lattice coding, SFA average-power allocation, convex OPA, KKT level, and sponge-squeezing | Proposed mechanism | High for transcription | No official implementation was located or run. |
| E4 | S2/S3 | Primary paper | Section VI and Figs. 4-7: rate trends versus M/N/K and comparisons with conventional, direct OFDM, opportunistic, SFA, and OPA variants | Reported empirical evidence | Medium | Simulation curves and parameters were not reproduced. |
| E5 | S5-S7 | Related DEP artifacts | AirComp, wireless channel-domain processing, and spectrum allocation relationships | Cross-DEP synthesis | Medium | Related artifacts are not independent validation of this paper. |

## Executive Summary

The paper addresses wideband computation over a fading multi-access channel (CoMAC), where conventional computation rates can decline toward zero as the number of participating nodes increases and frequency-selective fading makes narrowband assumptions inadequate. Its CoMAC-OFDM design divides a desired function into `B=K/M` sub-functions, maps sub-functions to favorable sub-carriers based on channel gains, and reconstructs the desired function at a fusion center using nested lattice coding. It then introduces average power allocation and a per-OFDM-symbol convex optimization whose KKT structure motivates a sponge-squeezing procedure.

The paper reports, from its own theoretical analysis and simulations, that sub-function allocation produces non-vanishing computation-rate behavior as node count grows, more sub-carriers can improve rate under the stated assumptions, and optimal power allocation improves the average-power SFA baseline. These findings remain source-reported: no code, seeds, hardware trace, or independent reproduction was identified in the inspected public sources.

## Detailed Summary

### Problem context and vocabulary

CoMAC uses concurrent node transmissions and channel superposition so a fusion center can recover a desired function instead of collecting every individual value. In a wideband channel, frequency-selective fading produces different gains across OFDM sub-carriers. The paper uses `K` for nodes, `M` for nodes assigned to a sub-function, `B=K/M` for the number of sub-functions, `N` for sub-carriers, `T_s` for OFDM symbols, and `R` for computation rate.

### Method and mechanism

The allocation pipeline has three stages. First, divide each desired function into compatible sub-functions over disjoint node groups. Second, assign a sub-function to a sub-carrier where its selected `M` nodes have the strongest ordered channel gains. Third, use the received sub-functions and their reconstruction relation to recover the original function. The nested-lattice block code supplies reliable computation under additive noise, while the rate derivation accounts for the `1/N` sub-carrier noise variance used in the paper's equal-bandwidth comparison.

The average-power SFA rule equalizes the effective weakest-node contribution using a channel-gain ratio. The OPA formulation replaces the inner minimum with a nonnegative level `eta_g` for each sub-carrier and imposes per-node total-power constraints. The objective is concave in these levels; the paper derives `eta_g* = max(0, v_g - 1/M)` from KKT conditions and describes sponge-squeezing as a finite interpretation of adjusting the Lagrange multipliers until the active node budgets meet the constraints.

### Results and evidence

The source's simulations compare conventional CoMAC, direct CoMAC-OFDM, opportunistic CoMAC, CoMAC-OFDM with SFA, and SFA with OPA. Figure 4 uses `K=128` and `P=10 dB` to show rate dependence on `M` and `N`. Figure 5 examines the number of sub-functions as `K` grows and reports a large-node example at `K=4000`. Figures 6 and 7 report qualitative comparisons: conventional and direct schemes are described as vanishing with node count under fixed settings, SFA and opportunistic CoMAC as non-vanishing, and OPA as improving SFA. No numeric curve values are transcribed because the inspected HTML text preserves captions and trends more reliably than exact plotted coordinates.

### Limitations and boundary conditions

The evidence is analytic and simulation-based rather than hardware-validated. The conclusions depend on the stated fading, noise, bandwidth, coding, node-group, and CSI assumptions. The paper does not establish performance under correlated sub-carriers, imperfect synchronization, finite blocklength, heterogeneous power budgets, mobility traces, adversarial interference, privacy leakage, or real-time scheduler overhead. The paper's public arXiv record exposes no official implementation link; the associated code/data panels are discovery tools, not evidence that a code artifact exists.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Wideband CoMAC can use OFDM with function division, sub-function allocation, and reconstruction. | Author claim | E2, E3 | Supported by the system model and Sections IV-V. | High |
| C2 | SFA avoids the vanishing-rate behavior of the conventional fixed-node scheme under the paper's model. | Author claim | E2, E4 | Supported within stated assumptions; external validity is untested. | Medium-high |
| C3 | OPA and the sponge-squeezing procedure can improve SFA computation rate. | Author claim | E3, E4 | Supported by the convex formulation and reported Fig. 7 trend; not independently reproduced. | Medium |
| C4 | The method is deployment-ready or reproducible from the public record alone. | Unsupported implication | No supporting evidence | Rejected because code, seeds, hardware validation, and operational controls were not found. | High rejection confidence |
| C5 | The allocation pattern is reusable for cross-layer wireless resource governance. | Reviewer interpretation | E5 plus E2-E4 | Useful design hypothesis, not a paper claim. | Medium |

## Methodology

- `Research objective`: Produce a source-grounded DEP-E manuscript that separates the paper's claims, evidence, limitations, and safe implementation implications.
- `Sources inspected`: Local verified PDF and full-paper HTML, local metadata/provenance records, official arXiv metadata, the related IEEE DOI record, and exactly three mapped Black Lake DEP manuscripts.
- `Discovery strategy`: `rg --files -g "*.pdf"` enumeration; PDF-parent paper units; private immutable candidate index; arXiv ID/DOI/title/slug and public artifact dedup; 24-hour marker scan; atomic family reservation; complete-source repair and verification; overlap-based related-DEP selection.
- `Inclusion criteria`: A source unit with a unique canonical arXiv identity, no permanent processed-artifact match, no recent marker, and a verified PDF plus full-paper HTML after bounded repair.
- `Exclusion criteria`: Duplicate archive identities, existing public artifact/DOI/title/slug matches, same-paper recent markers, unresolved identities, incomplete source units, and unsupported deployment claims.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication analysis.
- `Evidence handling`: Evidence IDs distinguish official metadata, primary full-text claims, author-reported simulations, reviewer interpretations, and related DEP context.
- `Uncertainty handling`: Unreproduced curves, unavailable official code, source-package unavailability, idealized channel assumptions, and hardware/operational gaps remain explicit.
- `Random selection and dedup`: 75,967 PDFs became 75,964 parent units and 67,990 unique canonical identities; 59,867 remained eligible. The reservation helper used `secrets_system_random_from_locked_eligible_set` and returned `arxiv:1806.08632`; no reselection was needed.

## Scope, Constraints, and Assumptions

- `Scope`: The selected paper's source identity, CoMAC-OFDM mechanism, rate claims, simulation evidence, limitations, related research, and bounded implementation translation.
- `Temporal boundary`: Public source and repository context inspected on 2026-08-22; paper version reviewed is arXiv v1.
- `Evidence limits`: The local PDF and full-paper HTML passed integrity checks, but plots, code, seeds, data, and hardware results were not independently reproduced.
- `Assumptions`: The arXiv record and related DOI identify the same research work; the paper's stated channel and coding assumptions apply to its reported results.
- `Constraints`: Public artifacts must contain Markdown and public URLs only; source files and private archive/coordination records remain local.
- `Out of scope`: Live radio configuration, spectrum-market operation, autonomous scheduling, security-sensitive interference, and production deployment approval.
- `Intended use`: Research review, replication planning, safe synthetic prototyping, and cross-DEP conceptual synthesis.
- `Reproducibility boundary`: A future reproduction needs pinned source version, channel generator, OFDM normalization, node/group selection, lattice-code configuration, power budget, seeds, and figure-generation code.
- `Data sensitivity`: Public scholarly sources; no private or personal data is used in this artifact.

## Observations

- `Observed pattern`: The proposed rate improvement is a consequence of jointly selecting participants and sub-carriers; it is not just a modulation change.
- `Technical implication`: The minimum effective channel among the `M` participating nodes acts as a fairness/bottleneck statistic, so allocating more power to strong nodes alone cannot improve the sub-function unless the weakest node improves.
- `Cross-DEP relationship`: AirComp supplies the same distributed-computation intuition, 2D-RC OTFS shows a different way to encode wireless channel structure, and Hybrid Spectrum Markets makes allocation and approximation costs explicit.
- `Reviewer hypothesis`: A production design would need a joint objective over computation rate, CSI age, latency, energy, fairness, and privacy rather than rate alone.
- `Open question`: Whether the SFA/OPA benefit survives correlated fading and imperfect CSI is not established by the inspected evidence.

## Considerations

Implementation should treat CSI as time-bounded evidence, require a fallback when channel estimates are stale or incomplete, and preserve a trace of participant groups, sub-carriers, power budgets, and reconstruction status. Synchronization, pilot overhead, finite blocklength, radio front-end impairments, interference, and legal spectrum constraints can dominate the theoretical gain. Any use with sensitive sensor data should keep aggregation purpose-limited, minimize telemetry, and test whether channel or gradient observations reveal device or environment identity.

## Strengths

- Connects a clear wideband fading problem to a concrete OFDM allocation mechanism.
- Provides a layered theoretical story: general rate, SFA corollary, OPA convex form, and KKT-based algorithmic interpretation.
- Explicitly compares against conventional and opportunistic CoMAC and separates average-power from optimal-power settings.
- Makes the reconstruction relation and nested-lattice coding assumptions visible enough for a future bounded reproduction.

## Weaknesses

- The empirical section is simulation-only and the exact plotted values are not available as a machine-readable table in the inspected sources.
- The reported behavior depends on idealized fading/CSI/bandwidth assumptions and does not include hardware-in-the-loop evidence.
- No official code, seeds, or end-to-end implementation was identified from the arXiv record and inspected paper.
- Real-time scheduling, synchronization, pilot cost, privacy, energy, and interference constraints are not evaluated.
- The method's integer partition and weakest-node bottleneck may reduce flexibility under heterogeneous or dynamic participation.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code, seeds, and figure data | Reproducibility | Curves and OPA claims need independent audit. | Re-runable baselines and clearer attribution. | Maintenance and publication effort. | Recreate Figs. 4-7 within tolerance. |
| Add correlated/estimated-CSI channels | Robustness | i.i.d. fading can overstate allocation gains. | Better boundary conditions. | Larger experiment grid. | Sweep correlation, CSI age, estimation error, and outage. |
| Add finite-blocklength and hardware-in-loop tests | Deployment relevance | Asymptotic lattice-code rates omit latency and RF impairments. | More realistic engineering decisions. | Hardware and calibration cost. | Compare rate, latency, energy, and error under matched budgets. |
| Add fairness/privacy metrics | Governance | Weakest-node selection and channel telemetry can create inequity or leakage. | Safer multi-node operation. | Requires authorized traces and threat modeling. | Measure worst-node service, leakage probes, and abstention behavior. |

## Potential Implementations

1. **Synthetic SFA/OPA simulator**: a local-only research tool that generates seeded fading tensors, partitions node groups, assigns sub-carriers, calculates the rate proxy, and compares average versus optimized power under explicit assumptions.
2. **CSI-aware allocation service**: a review-gated service that accepts authorized, time-stamped CSI, returns sub-function/sub-carrier assignments and per-node budgets, and abstains on stale CSI, infeasible partitions, or privacy-policy violations.
3. **Cross-layer evaluation harness**: a benchmark that compares CoMAC-OFDM, AirComp, OTFS-domain processing, and spectrum-allocation baselines under the same bandwidth, latency, energy, fairness, and interference constraints.

## Three Ways to Exercise This Research

1. **Rate-curve smoke test**: Use seeded synthetic fading with `K=128`, several `M` and `N` values, and a declared noise/power convention; reproduce the direction of the Fig. 4 trends; stop if normalization or participant-selection rules are ambiguous.
2. **Allocation robustness study**: Add correlated fading, CSI noise, and unequal node budgets to the synthetic simulator; report rate, worst-node effective gain, outage, and abstention; stop before using private or live radio traces without authorization.
3. **Cross-DEP comparison**: Run a matched toy benchmark for CoMAC-OFDM SFA, AirComp aggregation, an OTFS-domain receiver, and interference-aware spectrum allocation; compare rate/BER, latency, energy, and fairness; stop when baseline inputs or evaluation budgets diverge.

## Example MVP Product

- `Product name`: CoMAC Allocation Evidence Lab.
- `Target user`: Wireless-systems researcher, network architect, or reproducibility reviewer.
- `Problem`: Wideband distributed-computation designs need a transparent way to test participant/sub-carrier/power choices under imperfect evidence.
- `Core workflow`: Import a public-safe experiment manifest; generate or load authorized synthetic CSI; produce candidate SFA/OPA allocations; calculate rates and bottlenecks; run baselines; emit an evidence ledger and review gate.
- `Data requirements`: Seeded synthetic fading or authorized traces, node/group constraints, OFDM normalization, power budgets, coding assumptions, baseline configuration, and evaluation seeds.
- `Architecture`: Local experiment runner, allocation engine, rate/BER calculator, CSI freshness gate, baseline adapter, evidence ledger, and static report exporter.
- `Success metrics`: Recreated paper trend directions, baseline parity, bounded worst-node performance, sensitivity coverage, deterministic reruns, and reviewer time-to-audit.
- `Risk controls`: Synthetic/local-first inputs, no radio-control actions, no secrets, no private-source redistribution, stale-CSI abstention, explicit uncertainty, and human approval before any external integration.
- `Limitations`: It cannot establish hardware performance or spectrum compliance; paper claims remain unreplicated until a source-faithful experiment is completed.
- `MVP boundary`: Offline simulation and report generation only; no live scheduling, no autonomous radio configuration, and no consequential control.
- `Evaluation plan`: Unit tests for partitioning and bottleneck math, seeded smoke tests, baseline parity, CSI perturbation sweeps, privacy probes, and manual review of generated evidence ledgers.
- `Failure modes`: Stale CSI, infeasible integer groups, silent normalization drift, weak baselines, underestimated pilot/latency cost, privacy leakage, and overclaiming simulation results.

## Related Research and Reading

1. [Over-the-Air - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260815-Over-the-Air/over_the_air_manuscript.md) — AirComp and distributed wireless aggregation are the closest conceptual neighbor.
2. [2D-RC OTFS - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md) — domain-aware wideband channel processing and mobility evaluation provide a method/evaluation neighbor.
3. [Hybrid Spectrum Markets - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260729-Hybrid%20Spectrum%20Markets/hybrid_spectrum_markets.md) — interference-constrained spectrum allocation provides a system-level resource-governance neighbor.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1806.08632 | Identity, authors, date, abstract, DOI links, and source locators | 2026-08-22 | Official metadata page; metadata is not full-paper evidence. |
| R2 | https://arxiv.org/html/1806.08632 | Full-paper method, equations, simulations, conclusion, and references | 2026-08-22 | Official full-paper HTML; local copy withheld. |
| R3 | https://arxiv.org/pdf/1806.08632 | PDF integrity cross-check and primary paper | 2026-08-22 | Local PDF withheld. |
| R4 | https://doi.org/10.1109/TWC.2019.2918145 | Published-version identifier and journal context | 2026-08-22 | Publisher DOI; not used to invent extra results. |
| R5 | https://wrap.warwick.ac.uk/id/eprint/117386/ | Public near-primary bibliographic/publication context | 2026-08-22 | Used only to confirm published title, venue, pages, and access boundary. |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260815-Over-the-Air/over_the_air_manuscript.md | AirComp-related DEP context | 2026-08-22 | Generated Markdown; not primary evidence for the selected paper. |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-2D-RC%20OTFS/2d_rc_otfs_manuscript.md | Wideband wireless/domain-aware related context | 2026-08-22 | Generated Markdown; not primary evidence for the selected paper. |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260729-Hybrid%20Spectrum%20Markets/hybrid_spectrum_markets.md | Resource allocation and approximation related context | 2026-08-22 | Generated Markdown; not primary evidence for the selected paper. |

## Appendix

### Selection, Deduplication, and Source Gate

The private selection index was generated from 75,967 PDFs and 75,964 parent units, resolved to 67,990 unique canonical arXiv identities, and left 59,867 eligible identities after overlapping duplicate/public/DOI/title-slug/recent-marker exclusions. The selected identity was returned by the family reservation helper's cryptographic random draw. The initial local source unit was partial because full-paper HTML was absent; one bounded repair preserved the valid PDF and produced qualifying full-paper HTML. The final gate recorded a valid PDF, 404,242-byte full-paper HTML, 73,784 body characters, 71 heading markers, 7 structure-term classes, no partial files, and no public source upload.

### Replication Checklist

- Pin arXiv v1 and the published DOI mapping.
- Recreate the channel and OFDM normalization, including `K`, `M`, `B`, `N`, `T_s`, noise variance, and power constraints.
- Reproduce average-power SFA before OPA; retain participant rankings and per-sub-carrier levels.
- Implement the convex level formulation and compare KKT/sponge-squeezing output with a trusted solver on small synthetic cases.
- Recreate the qualitative trends in Figs. 4-7 and report exact curves, seeds, and tolerances.
- Add correlated fading, CSI error, finite blocklength, hardware impairments, latency, energy, fairness, and privacy tests.

### Source Withholding Confirmation

No PDF, full-paper HTML, metadata HTML, source archive, extracted text, cache, private verification record, local archive path, or `.source/` directory is included. Only generated public-safe Markdown and public URLs are deposited.

## Attribution Block

- Source URL: https://arxiv.org/abs/1806.08632
  - Applies to: this manuscript's source identity and metadata.
- Source URL: https://arxiv.org/html/1806.08632
  - Applies to: this manuscript's method, results, limitations, and references.
- Source URL: https://arxiv.org/pdf/1806.08632
  - Applies to: this manuscript's PDF cross-check.
- Source URL: https://doi.org/10.1109/TWC.2019.2918145
  - Applies to: this manuscript's published-version metadata.
