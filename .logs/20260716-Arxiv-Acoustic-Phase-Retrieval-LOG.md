# Black Lake Arxiv DEP: Acoustic Phase Retrieval

- Public run date: 2026-07-16
- Action: `Black Lake Arxiv DEP` selected and reviewed one paper from the local arXiv archive.
- Selected paper: *Retrieval of acoustic sources from multi-frequency phaseless data* (`arXiv:1803.11323v1`; related DOI `10.1088/1361-6420/aaccda`).
- Sanitized provenance: a verified local paper unit plus public arXiv, ar5iv, DOI, and institutional publication records; source files remain local and were not uploaded.
- Random method: `rg --files -g "*.pdf"` found 75,777 PDF candidates, collapsed to 75,776 unique parent-directory paper units, followed by uniform PowerShell `Get-Random`; selected zero-based index 16,432.
- Eligibility: Black-Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data were scanned for the arXiv ID, DOI, exact title, and slug. Exclusions: 0; reselections: 0. The public-safe 24-hour cutoff date marker was 2026-07-15.
- Source integrity: initially partial because full-paper HTML was absent. The valid PDF was preserved; metadata HTML, ar5iv full-paper HTML, and the arXiv source package were repaired locally. PDF, full-paper HTML, extraction-cache, and no-partial-file gates passed.
- Related DEP entries: `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`.
- Report-Mark: `.reports/BL-Arxiv-Acoustic-Phase-Retrieval-20260716/Report-Mark.md`.
- DEP-E: `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval`.
- Manuscript: `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md`.
- Validation: source claims and reviewer inferences are separated; exact-three synthesis counts and manuscript schema are checked; staged files must pass the public-output allowlist and leak scan before submission.

## Questions for the Next Reviewer

1. Can the two-reference-source phase retrieval remain well conditioned under reference-location, amplitude, and background-medium mismatch?
2. Does a calibration-aware experimental setup reproduce the reported noise behavior with real acoustic hardware rather than synthetic finite-element data?
3. Can measurement/reference-source placement be optimized jointly with the Fourier truncation while preserving an auditable determinant margin?

## Challenges for the Next Review Pass

1. Reproduce the four-frequency phase-retrieval tables with fixed random seeds and confidence intervals.
2. Stress-test geometry, frequency-independent-source, and circular-acquisition assumptions using controlled synthetic mismatch.
3. Add runtime, measurement-count, conditioning, and reconstruction-error ledgers that separate phase recovery from Fourier inversion.
