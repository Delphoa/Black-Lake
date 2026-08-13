# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260809-2E4CB30E`
- Deployment item ID: `BLAD-2200-20260809-2E4CB30E-P04`
- Public-safe date: 2026-08-09
- Paper: *Tensor Robust PCA with Nonconvex and Nonlocal Regularization*
- Identifier: `arXiv:2211.02404`; DOI: `10.48550/arXiv.2211.02404`
- URL: https://arxiv.org/abs/2211.02404

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 5,006 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Tensor-Robust-PCA-with-Nonconvex-and-Nonlocal` slug; the 24-hour marker cutoff was 2026-08-08.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 16,243,952 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 15; sampled text inspection: true.
- Full-paper HTML: 1,463,121 bytes, 155,606 body characters, 48 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260809-Arxiv-Tensor-Robust-PCA-with-Nonconvex-and-Nonlocal-LOG.md`
- `.reports/BL-Arxiv-Tensor-Robust-PCA-with-Nonconvex-and-Nonlocal-20260809/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260809-Tensor Robust PCA with/README.md`
- `.lake-data/DEP-E/DEP-E-20260809-Tensor Robust PCA with/tensor_robust_pca_with_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - VideoWeave - DEP-E; overlap: pca, regularization, robust.
2. `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md` - Global NS Existence - DEP-E; overlap: tensor, regularization, robust.
3. `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` - Device Tuning MTL - DEP-E; overlap: tensor, regularization, robust.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
