# Arxiv DEP Log: MI-Motion

## Selection

- Method: enumerated PDF files with rg --files -g "*.pdf", grouped each result by its parent paper unit, sorted the unique units, and used one uniform PowerShell Get-Random index.
- Candidate PDF files: 75,781.
- Candidate paper units: 75,778.
- Draw: zero-based index 69,830; first draw accepted.
- Exclusions and reselections: 0 prior-Arxiv-DEP exclusions, 0 source-gate exclusions, and 0 reselections.
- Dedup validation: searched Black Lake .logs, .reports, .lake-data, .staging, the metadata-only .lists inventory, automation memory, and current Black-Lake-Data main for arXiv ID, DOI, title, and slug. The sole hit was a metadata-only inventory row; no processed artifact or same-paper marker within 24 hours was found.

## Source Integrity

- Initial state: partial. The local unit contained a valid PDF and README but no full-paper HTML.
- Repair: one bounded direct-HTTPS companion repair preserved the PDF and added metadata HTML, verified full-paper HTML, and the TeX source archive locally.
- Verification: PDF exceeds 10 KB, starts with %PDF-, and ends with %%EOF. Full-paper HTML exceeds 5 KB, has 100,694 body characters, a document marker, 117 headings, and six paper-structure term classes. No partial files remain.
- Public-source gate: original paper files, source archive, metadata HTML, full-paper HTML, renderings, and verification records remain local. No .source directory was created or uploaded.

## Outputs

- .reports/BL-Arxiv-MI-Motion-20260728/Report-Mark.md
- .lake-data/DEP-E/DEP-E-20260728-MI-Motion Review/README.md
- .lake-data/DEP-E/DEP-E-20260728-MI-Motion Review/mi_motion_manuscript.md
- .lake-data/DEP-E/.index/pubs-index.md

## Next-Review Questions

1. Can the 210-versus-217 sequence-count discrepancy be reconciled from a versioned dataset manifest?
2. How does SocialTGCN compare under repeated-seed, cross-scene splits rather than the reported scene partition?
3. What access, licensing, consent, and provenance constraints apply to the synthetic and motion-capture components?

## Challenges

1. The project page requires a data-access agreement for the synthetic component, limiting independent replication.
2. Reported tables do not include repeated-seed uncertainty, confidence intervals, or statistical tests.
3. An official public code repository was not established from the inspected primary sources.

## Related DEP Entries

- .lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md
- .lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md
- .lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md

## Attribution Block

- Source URL: https://arxiv.org/abs/2306.13566
  - Applies to: this log and the linked public-safe research artifacts.
  - Notes: Canonical metadata locator. Source files were withheld locally.
