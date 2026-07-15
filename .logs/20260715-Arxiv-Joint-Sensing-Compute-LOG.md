# Arxiv DEP Job Log: Joint Sensing MEC

## Public-Safe Run Summary

- Deposit date: 2026-07-15
- Selected paper: *Joint Optimization of Sensing and Computation for Status Update in Mobile Edge Computing Systems*
- Authors: Yi Chen; Zheng Chang; Geyong Min; Shiwen Mao; Timo Hämäläinen
- arXiv: https://arxiv.org/abs/2210.17025
- Journal DOI: https://doi.org/10.1109/TWC.2023.3261338
- Source state: initially `partial`; repaired and verified `complete` before review
- Source policy: PDF, full-paper HTML, metadata HTML, TeX/source, extracted text, and caches withheld locally; no source file uploaded
- Submission status: generated and pending validated repository submission

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"`
- Paper unit: each unique PDF parent directory
- Candidate count: 75,776 paper units
- Random method: uniform PowerShell `Get-Random` index over the complete candidate-unit array
- Selected zero-based index: 7,665
- Exclusions before acceptance: 0
- Duplicate reselections: 0
- Same-paper markers within the preceding 24 hours: 0

## Dedup Validation

The selected arXiv ID, journal DOI, normalized title, and slug were checked against `.staging/arxiv-dep-dedup-index.json`, Black Lake `.logs`, `.reports`, and `.lake-data`, automation memory, relevant Black-Lake-Data searches, and other active-worktree artifacts. No prior Arxiv DEP artifact remained after the temporary private repair input was removed. The first draw was accepted.

## Source Integrity and Cache

- Existing PDF: 803,785 bytes; `%PDF-` header; trailing `%%EOF`; exact hash match with the bounded repair download
- Full-paper HTML: 1,182,606 bytes; 120,156 body characters; document marker; 77 heading/section markers; seven paper-structure terms
- Metadata HTML: collected locally; metadata only and never counted as the paper
- TeX/source: collected locally and extracted
- Partial files after repair: 0
- Initial cache: miss
- Extraction mode: `missing-only`
- Final cache: `cached`
- Extractors: `pypdf`, `html-regex`, and `tarfile`; `pypdf` was the fallback because `pdftotext` was unavailable
- Text outputs: 69,290 bytes PDF text; 102,224 bytes HTML text; 84,754 bytes source text

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` - connects heterogeneous sensor observations and state representation to constrained control latency.
2. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` - connects fresh-state evidence, safety margins, solver latency, and fallback to control admissibility.
3. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - connects clock/spatial calibration and progressive optimization to reliable freshness evidence.

## Output Paths

- `.logs/20260715-Arxiv-Joint-Sensing-Compute-LOG.md`
- `.logs/20260715-Arxiv-Joint-Sensing-Compute-PHASE-LOG.md`
- `.reports/BL-Arxiv-Joint-Sensing-Compute-20260715/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/README.md`
- `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Does a checked derivation or erratum resolve the cost-improvement expression and narrow MISCO's claim from global optimality to coordinate-wise or Nash-stable convergence?
2. How large is the equilibrium-to-global-optimum gap across small exhaustive cases and different best-response update orders?
3. Do the reported threshold regimes persist under correlated sensing failures, bursty MEC queues, time-varying channels, and heterogeneous deadlines?

## Challenges

1. The selected archive unit lacked full-paper HTML, so review had to stop for a bounded repair and complete-source verification.
2. No official code, raw figure values, deterministic seeds, or executable configurations were found, preventing independent reproduction.
3. The paper's extracted improvement equation and optimality wording are ambiguous enough to require a checked derivation before faithful implementation.

## Known Shortfalls

- Simulations, algorithms, and hardware behavior were not reproduced.
- The journal and arXiv versions were cross-checked at key sections but not exhaustively diffed.
- Energy normalization, tail latency, queueing, fairness, sensing correlation, and global-optimality gaps remain unresolved.

## Submission Record

- Primary artifact commit or PR: pending
- Final record commit: pending
- Slack notification: pending until repository submission
