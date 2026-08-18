# Arxiv DEP Log: HESIM Hybrid Sensors

- Run date: 2026-08-18.
- Status: complete.
- Selected paper: *Hybrid Event Frame Sensors: Modeling, Calibration, and Simulation*.
- Authors: Yunfan Lu; Nico Messikommer; Xiaogang Xu; Liming Chen; Yuhan Chen; Nikola Zubić; Davide Scaramuzza; Hui Xiong.
- Identifier: arXiv:2511.18037v2; arXiv DOI: 10.48550/arXiv.2511.18037.
- Public-safe source state: complete after one bounded brokered repair; source files remain local and were not uploaded.

## Selection and Deduplication

- Candidate enumeration used \`rg --files -g "*.pdf"\` against the local arXiv archive.
- Candidate count: 75,967 PDFs.
- Paper-unit count: 75,964 unique PDF parent directories.
- Selection method: uniform PowerShell \`Get-Random\` over the sorted unique paper-unit list, using zero-based index 2,429.
- Initial source classification: partial because the valid PDF existed without metadata HTML or full-paper HTML.
- Repair: one bounded brokered single-paper repair preserved the valid PDF and added metadata HTML plus verified full-paper HTML; the optional TeX/source package was unavailable through the permitted redirect policy.
- Dedup scan: no exact arXiv-ID, DOI, normalized-title, slug, prior Arxiv DEP artifact, or same-paper-within-24-hours marker was found in the checked Black Lake artifacts, automation memory, or related Black-Lake-Data inventory.
- Exclusion counts: duplicate exclusions 0; other exclusions 0; source-gate exclusions 0 after repair; same-paper 24-hour exclusions 0; reselections 0.
- Acceptance: first random draw retained after repair validation.

## Source Integrity Gate

- PDF: 7,549,663 bytes; \`%PDF-\` header present; trailing \`%%EOF\` present.
- Full-paper HTML: 337,627 bytes; 67,868 verified body characters; 31 heading markers; three document markers; seven paper-structure terms.
- Metadata HTML: present and non-empty at 42,342 bytes.
- Partial or temporary files: none remained in the selected unit.
- Local archive records updated by the repair workflow: README, provenance record, machine-readable summary, verification report, and immutable acquisition receipt.
- Source package: unavailable; no source package was copied, staged, committed, uploaded, or attached.

## Public Outputs

- \`.logs/20260818-Arxiv-HESIM-LOG.md\`
- \`.reports/BL-Arxiv-HESIM-20260818/Report-Mark.md\`
- \`.lake-data/DEP-E/DEP-E-20260818-Hybrid Sensor HESIM/README.md\`
- \`.lake-data/DEP-E/DEP-E-20260818-Hybrid Sensor HESIM/hesim_hybrid_sensor_manuscript.md\`
- \`.lake-data/DEP-E/.index/pubs-index.md\`

## Next-Review Questions

1. Do calibrated H-ESIM parameters transfer across additional hybrid-sensor layouts, temperatures, exposure regimes, and firmware settings without a fresh calibration capture?
2. How much of the downstream improvement remains after matched-data, matched-compute, repeated-seed, and cross-sensor evaluations with distortion-free references?
3. Can an open implementation expose deterministic calibration manifests, uncertainty estimates, and sensor-specific validation tests sufficient for independent reproduction?

## Challenges

1. The shared APS-EVS signal is conceptually clean, but layout-dependent fixed-pattern noise and polarity asymmetry make a single Gaussian approximation vulnerable outside the measured regimes.
2. H-ESIM reduces a simulation-to-real gap only when the calibration capture, sensor geometry, readout behavior, and downstream task distribution remain aligned.
3. The strongest downstream evidence uses rolling-shutter references or no-reference image-quality metrics, leaving true motion fidelity and sharp-image accuracy incompletely identified.

## Attribution Block

- Source URL: https://arxiv.org/abs/2511.18037
  - Applies to: selection metadata, source identity, authors, version history, abstract, and public provenance.
- Source URL: https://arxiv.org/pdf/2511.18037
  - Applies to: full-paper review, method, calibration, experiments, results, and limitations.
- Source URL: https://arxiv.org/html/2511.18037
  - Applies to: full-paper structure and cross-checking of sections, tables, and claims.
- Source URL: https://doi.org/10.48550/arXiv.2511.18037
  - Applies to: persistent arXiv identifier.
- Source URL: https://yunfanlu.github.io/HESIM/
  - Applies to: author-controlled project context and public method overview.
- Source files: withheld locally; no original PDF, HTML, metadata page, source package, cache, extracted text, or verification record is redistributed.
  - Applies to: all generated public artifacts.
