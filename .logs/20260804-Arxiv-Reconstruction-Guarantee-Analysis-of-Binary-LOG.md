# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260804-92EFB161`
- Deployment item ID: `BLAD-2200-20260804-92EFB161-P09`
- Public-safe date: 2026-08-04
- Paper: *Reconstruction Guarantee Analysis of Binary Measurement Matrices Based on Girth*
- Identifier: `arXiv:1301.4926`; DOI: `10.48550/arXiv.1301.4926`
- URL: https://arxiv.org/abs/1301.4926

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 34,340 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Reconstruction-Guarantee-Analysis-of-Binary` slug; the 24-hour marker cutoff was 2026-08-03.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 412,512 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 5; sampled text inspection: true.
- Full-paper HTML: 1,282,520 bytes, 54,742 body characters, 37 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260804-Arxiv-Reconstruction-Guarantee-Analysis-of-Binary-LOG.md`
- `.reports/BL-Arxiv-Reconstruction-Guarantee-Analysis-of-Binary-20260804/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260804-Reconstruction Guarantee/README.md`
- `.lake-data/DEP-E/DEP-E-20260804-Reconstruction Guarantee/reconstruction_guarantee_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md` - Residual Gaussian CBCT - DEP-E; overlap: tomography, scatter, attenuation, cbct, mri.
2. `.lake-data/DEP-E/DEP-E-20260802-MeDSLIP Medical/medslip_medical_manuscript.md` - MeDSLIP Medical - DEP-E; overlap: pediatric, pet, tomography, patients, scatter.
3. `.lake-data/DEP-E/DEP-E-20260720-WKGM MRI Reconstruction/wkgm_mri_reconstruction_manuscript.md` - WKGM MRI Reconstruction - DEP-E; overlap: cbct, patient, mri, imaging, health.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
