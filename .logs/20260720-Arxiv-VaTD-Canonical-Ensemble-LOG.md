# Arxiv DEP Phase Log

- Run date: 2026-07-20
- Actor/tool: Codex scheduled Arxiv DEP workflow
- Selected paper: *Deep generative modelling of canonical ensemble with differentiable thermal properties*
- Authors: Shuo-Hui Li; Yao-Wen Zhang; Ding Pan
- Stable identifiers: arXiv:2404.18404v2; arXiv DOI 10.48550/arXiv.2404.18404; publisher DOI 10.1103/8wx7-kyx8
- Canonical record: https://arxiv.org/abs/2404.18404v2
- Outcome: complete
- Blockers: none

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"` against the local arXiv archive.
- Paper unit: one unique PDF parent directory, with adjacent metadata and source companions treated as one unit.
- Method: uniformly select one zero-based index from the sorted unique parent-directory set with PowerShell `Get-Random`.
- PDF candidates: 75,778.
- Unique paper units: 75,776.
- Selected zero-based index: 20,958.
- Duplicate exclusions: 0.
- Other exclusions: 0.
- Reselections: 0; the first draw was accepted.

## Deduplication

The arXiv ID, arXiv DOI, publisher DOI, normalized title, and `VaTD-Canonical-Ensemble` slug family were checked against Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and relevant Black-Lake-Data artifact scopes. The scan was repeated after synchronizing to the current default branch. No prior Arxiv DEP log, report, DEP-E deposit, or same-paper marker within 24 hours was found.

## Source-Integrity Gate

- Initial state: partial. A 3,010,534-byte PDF and minimal metadata README were present, but full-paper HTML and companion provenance/verification records were absent.
- Preserved artifact: the existing PDF passed the 10 KB minimum, `%PDF-` header, trailing `%%EOF`, and SHA-256 equality checks against the bounded repair copy.
- Repair: collected 45,498-byte arXiv metadata HTML, 318,497-byte official arXiv full-paper HTML, and a 2,401,529-byte arXiv source package through one bounded HTTPS strategy.
- Full-paper HTML verification: 71,959 body characters after script/style/tag removal; document marker present; 47 section/heading markers; seven paper-structure term classes; no error or conversion notice.
- Final state: complete. README, attribution record, machine-readable summary, and verification report were updated locally; no partial transfer files remain.
- Local review evidence: the complete 36-page v2 PDF, official full-paper HTML, metadata HTML, TeX source, all four main figures, three supplementary tables, supplementary figures, and official code repository were inspected.
- Source locality: all PDF, HTML, metadata, source-package, extraction, verification, and render files remain local. No source file is included in this repository change.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` - uses a differentiable physical equation as a compact trainable representation, providing a direct bridge to VaTD's physics-defined loss and temperature-conditioned model.
2. `.lake-data/DEP-E/DEP-E-20260717-Surface SQD Study/surface-sqd-study.md` - studies sample-based variational energy estimation in a many-body setting and foregrounds physical-sector validity, classical comparators, and scaling bottlenecks.
3. `.lake-data/DEP-E/DEP-E-20260718-Transport Convexity/transport_convexity_manuscript.md` - analyzes when distribution-transform geometry simplifies learning, complementing VaTD's use of tractable density transforms and making model-family assumptions explicit.

## Outputs

- `.logs/20260720-Arxiv-VaTD-Canonical-Ensemble-LOG.md`
- `.reports/BL-Arxiv-VaTD-Canonical-Ensemble-20260720/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260720-VaTD Canonical/README.md`
- `.lake-data/DEP-E/DEP-E-20260720-VaTD Canonical/vatd_canonical_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Do the source-reported Ising and XY accuracy and convergence gains survive a version-pinned rerun with repeated seeds, uncertainty intervals, matched tuning budgets, and independent MCMC implementations?
2. How does VaTD degrade when a tractable density model has insufficient capacity, misses metastable modes, or is evaluated outside its trained temperature interval?
3. Can the temperature-differentiable objective transfer to atomistic or molecular systems while preserving calibrated free-energy derivatives, physical symmetries, and practical compute costs?

## Challenges

1. The selected unit required bounded source repair because full-paper HTML and provenance records were initially missing.
2. The strongest speed evidence is author-reported on one RTX 4090 and depends on thresholds, temperature-count amortization, HMC settings, and an estimated RMHMC curve.
3. The official code is available, but inspected XY defaults differ from the v2 manuscript table and no frozen release, checkpoint manifest, seed ledger, or one-command reproduction was identified.
