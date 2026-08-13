# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260805-6C10E207`
- Deployment item ID: `BLAD-2200-20260805-6C10E207-P08`
- Public-safe date: 2026-08-05
- Paper: *Heterogeneous Similarity Graph Neural Network on Electronic Health Records*
- Identifier: `arXiv:2101.06800`; DOI: `10.48550/arXiv.2101.06800`
- URL: https://arxiv.org/abs/2101.06800

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 48,460 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Heterogeneous-Similarity-Graph-Neural-Network-on` slug; the 24-hour marker cutoff was 2026-08-04.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 912,012 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 430,188 bytes, 58,285 body characters, 76 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260805-Arxiv-Heterogeneous-Similarity-Graph-Neural-Network-on-LOG.md`
- `.reports/BL-Arxiv-Heterogeneous-Similarity-Graph-Neural-Network-on-20260805/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260805-Heterogeneous Similarity/README.md`
- `.lake-data/DEP-E/DEP-E-20260805-Heterogeneous Similarity/heterogeneous_similarity_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260804-Reconstruction Guarantee/reconstruction_guarantee_manuscript.md` - Reconstruction Guarantee - DEP-E; overlap: pediatric, pet, tomography, patients, scatter.
2. `.lake-data/DEP-E/DEP-E-20260720-WKGM MRI Reconstruction/wkgm_mri_reconstruction_manuscript.md` - WKGM MRI Reconstruction - DEP-E; overlap: cbct, patient, mri, imaging, health.
3. `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md` - Residual Gaussian CBCT - DEP-E; overlap: tomography, scatter, attenuation, cbct, mri.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
