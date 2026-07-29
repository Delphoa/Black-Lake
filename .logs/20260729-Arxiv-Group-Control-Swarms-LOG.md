# Arxiv DEP Log: Group-Control Swarms

- Date: 2026-07-29
- Actor: Codex
- Action: Randomly select one eligible locally archived arXiv paper, enforce a complete-source gate, create a source-grounded review, and deposit a DEP-E research package.
- Selected paper: *Group-Control Motion Planning Framework for Microrobot Swarms in a Global Field*
- Canonical record: [arXiv:2406.13829v2](https://arxiv.org/abs/2406.13829v2)
- Result: Complete; the public repository submission contains generated Markdown only.
- Affected DEP: `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/`
- Blockers: None.

## Random Selection and Deduplication

- Candidate discovery used `rg --files -g "*.pdf"` over the private archive, with each PDF parent directory treated as one paper unit.
- The enumeration produced 75,781 PDFs in 75,778 candidate units.
- A used-paper index was assembled from Delphoa/Black-Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and the corresponding fetched `origin/main` surfaces in Delphoa-Labs/Black-Lake-Data.
- The conservative index contained 1,547 observed arXiv base identifiers. It excluded 425 candidate units by used identifier; another 185 units were withheld because a canonical identifier could not be established reliably.
- The remaining eligible pool contained 75,168 units. PowerShell `Get-Random` selected uniform zero-based eligible index 72,419.
- One earlier in-memory enumeration returned no retrievable selection record and was discarded before acceptance. It did not select a review target. The recorded index above is the sole accepted draw.
- The accepted identifier was arXiv:2406.13829, *Group-Control Motion Planning Framework for Microrobot Swarms in a Global Field*.
- Duplicate rejections and reselections after the accepted draw: 0.
- The 24-hour marker cutoff was 2026-07-28. The accepted paper had no matching recent marker.
- Final exact checks covered arXiv ID `2406.13829`, arXiv DOI `10.48550/arXiv.2406.13829`, the canonical and normalized title, and planned public slugs. No prior same-paper Arxiv DEP artifact was found.

## Source Integrity Gate

- Initial state: partial. A valid PDF was present, but verified full-paper HTML was absent.
- Repair preflight: one ID-scoped paper bundle, no credentials, a 200 MiB per-artifact ceiling, one attempt per official endpoint, an ar5iv fallback reserved only for failed full-paper HTML, no restart automation, and no deletion.
- The existing PDF was preserved. Official arXiv full-paper HTML, metadata HTML, and the source archive were collected in one bounded repair; the fallback was not needed.
- Final PDF verification: 1,700,463 bytes; `%PDF-` header present; trailing `%%EOF` present; 18 pages; unencrypted.
- Final official full-paper HTML verification: 861,863 bytes; 90,587 script/style-stripped body characters; a full-document marker; 44 heading markers; and five paper-structure terms.
- Supporting verification: the source archive contains 56 entries; PDF and HTML extracted-text caches were generated; all 18 PDF pages were rendered and visually inspected; zero partial files remained.
- Final classification: complete and verified.
- Source-file policy: all PDF, HTML, metadata, source-archive, extracted-text, render, summary, attribution, and verification files were withheld in the private archive. No source file was copied into, staged for, or uploaded to the public repository.

## Review Boundary

- The complete paper, official arXiv metadata, TeX source, WAFR proceedings context, and Springer chapter record were inspected.
- The paper models a globally actuated MicroStressBot swarm as a switched system, derives group allocations from PFSM membership patterns, proves position-level small-time local controllability under stated idealizations, and organizes planning around Lie-bracket-inspired subgroup primitives.
- The empirical evidence is simulation-only and centers on six robots and four groups. Reported averages compare numerical optimization, RRT variants, parallel subgroup planning, sequential subgroup planning, and pure control.
- Reviewer cautions include instantaneous-rotation and bilateral-control idealizations, equal turning-rate assumptions, lack of hardware validation, missing code and seed details, absent variance or confidence intervals, no broad swarm-size scaling study, and ambiguous integer rounding in the group-count formula.
- The source contains two notable internal reporting tensions: the sequential-planning narrative gives a 19.44-second planning time while Table 4 lists 15.38 seconds, and the Table 4 footnote names “Original RRT” although the marked row is “RRT with rotation.”
- A bounded public code search did not establish an author-linked implementation repository. No code or experiment was run.

## Public Artifacts

- `.logs/20260729-Arxiv-Group-Control-Swarms-LOG.md`
- `.reports/BL-Arxiv-Group-Control-Swarms-20260729/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/README.md`
- `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md` publication-index update

## Related DEP Basis

1. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` - direct overlap in sampling-based motion planning, collision avoidance, continuous control, execution tracking, and the gap between a feasible path and a safe physical controller.
2. `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md` - a fast/slow planning split in which high-level waypoints are cached and a lower-level controller acts at higher frequency, paralleling the selected paper's separation between primitive design and execution.
3. `.lake-data/DEP-A/DEP-A-20260722-CrossMaps Rover Mapping/2606.16935-whitepaper-review.md` - rover mapping and confidence-aware persistent state provide the perception/state layer that a practical motion planner needs before applying group-control primitives.

## Public Sources

- [Canonical arXiv record](https://arxiv.org/abs/2406.13829v2)
- [Official full-paper HTML](https://arxiv.org/html/2406.13829v2)
- [arXiv PDF](https://arxiv.org/pdf/2406.13829v2)
- [arXiv DOI](https://doi.org/10.48550/arXiv.2406.13829)
- [Springer chapter DOI](https://doi.org/10.1007/978-3-032-09967-9_14)
- [WAFR 2024 public paper](https://algorithmic-robotics.org/papers/65_Group_Control_Motion_Planni.pdf)
