# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260810-B3B6846E`
- Deployment item ID: `BLAD-2200-20260810-B3B6846E-P04`
- Public-safe date: 2026-08-10
- Paper: *VITATECS: A Diagnostic Dataset for Temporal Concept Understanding of Video-Language Models*
- Identifier: `arXiv:2311.17404`; DOI: `10.48550/arXiv.2311.17404`
- URL: https://arxiv.org/abs/2311.17404

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 42,791 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `VITATECS-A-Diagnostic-Dataset-for-Temporal` slug; the 24-hour marker cutoff was 2026-08-09.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 10,571,741 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 19; sampled text inspection: true.
- Full-paper HTML: 187,407 bytes, 52,479 body characters, 73 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260810-Arxiv-VITATECS-A-Diagnostic-Dataset-for-Temporal-LOG.md`
- `.reports/BL-Arxiv-VITATECS-A-Diagnostic-Dataset-for-Temporal-20260810/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260810-VITATECS A Diagnostic/README.md`
- `.lake-data/DEP-E/DEP-E-20260810-VITATECS A Diagnostic/vitatecs_a_diagnostic_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260804-Reconstruction Guarantee/reconstruction_guarantee_manuscript.md` - Reconstruction Guarantee - DEP-E; overlap: pediatric, pet, tomography, patients, attenuation.
2. `.lake-data/DEP-E/DEP-E-20260805-Heterogeneous Similarity/heterogeneous_similarity_manuscript.md` - Heterogeneous Similarity - DEP-E; overlap: pediatric, pet, tomography, patients, attenuation.
3. `.lake-data/DEP-E/DEP-E-20260802-MeDSLIP Medical/medslip_medical_manuscript.md` - MeDSLIP Medical - DEP-E; overlap: pediatric, pet, tomography, patients, attenuation.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
