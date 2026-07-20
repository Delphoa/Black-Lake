# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P01`
- Public-safe run date: 2026-07-20
- Outcome: reviewed, validated, and prepared for submission
- Selected paper: *Higher criticism: $p$-values and criticism*
- Stable identifier: `arXiv:1411.1437v3`
- Canonical URL: https://arxiv.org/abs/1411.1437

## Random Selection

- Method: `rg --files -g "*.pdf"`, unique PDF-parent units, uniform PowerShell `Get-Random` index.
- PDF candidates: 75,779; candidate paper units: 75,776.
- Accepted one-based index: 16,762.
- The first draw was rejected privately when bounded repair could not produce valid full-paper HTML; the second uniform draw was accepted. No machine, user, path, timezone, or timestamp-derived seed was used.

## Deduplication and Reselection

- Scanned Black Lake `.logs`, `.reports`, `.lake-data`, the public dedup index, this automation memory, relevant Black-Lake-Data records, and the current-job selected set.
- Keys: arXiv ID, DOI, normalized title, `Higher-Criticism` slug, artifact markers, and markers on or after the public-safe cutoff date 2026-07-19.
- The metadata-only author inventory row was not treated as a prior review.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Initial accepted-unit classification: partial; valid PDF present, full-paper HTML absent.
- Repair: the official full-paper HTML endpoint returned HTTP 404; one approved ar5iv fallback retrieved the full paper, and the arXiv abstract page was retained as metadata only.
- PDF: 295,092 bytes; `%PDF-` and trailing `%%EOF` passed.
- Full-paper HTML: 2,859,259 bytes; 134,924 body characters; 180 document markers; 38 heading markers; 60 paper-structure terms; no conversion-notice payload.
- Final state: complete. All original source documents and repair records remain local.

## Public Outputs

- `.logs/20260720-Arxiv-Higher-Criticism-LOG.md`
- `.reports/BL-Arxiv-Higher-Criticism-20260720/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260720-Higher Criticism/README.md`
- `.lake-data/DEP-E/DEP-E-20260720-Higher Criticism/higher_criticism_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` - finite-sample confidence bounds and calibration-dependent decisions.
2. `.lake-data/DEP-E/DEP-E-20260719-Kernel Equivalence/kernel_equivalence_manuscript.md` - hypothesis direction, significance calibration, and the distinction between absence of evidence and positive evidence.
3. `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md` - finite-sample Type-I error, measurement-model assumptions, and corrected hypothesis testing.

## Submission Gate

- Allowlist: generated Markdown plus the required publication-index Markdown and dedup JSON.
- `.source/`: not created. Source-document upload: none.
- Public sanitization withholds local paths, user/machine context, timezone labels, and exact execution timestamps.
