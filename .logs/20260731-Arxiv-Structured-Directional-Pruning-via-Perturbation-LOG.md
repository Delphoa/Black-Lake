# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260731-3D09E72F`
- Deployment item ID: `BLAD-2200-20260731-3D09E72F-P05`
- Public-safe date: 2026-07-31
- Paper: *Structured Directional Pruning via Perturbation Orthogonal Projection*
- Identifier: `arXiv:2107.05328`; DOI: `10.48550/arXiv.2107.05328`
- URL: https://arxiv.org/abs/2107.05328

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 65,168 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Structured-Directional-Pruning-via-Perturbation` slug; the 24-hour marker cutoff was 2026-07-30.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,714,602 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 33; sampled text inspection: true.
- Full-paper HTML: 3,034,492 bytes, 135,908 body characters, 76 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260731-Arxiv-Structured-Directional-Pruning-via-Perturbation-LOG.md`
- `.reports/BL-Arxiv-Structured-Directional-Pruning-via-Perturbation-20260731/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260731-Structured Directional/README.md`
- `.lake-data/DEP-E/DEP-E-20260731-Structured Directional/structured_directional_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: quantization, pruning, projection, sparsity, compression.
2. `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md` - Medical Diff VQA - DEP-E; overlap: directional, projection, perturbation, structured, memory.
3. `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md` - Residual Gaussian CBCT - DEP-E; overlap: directional, projection, sparsity, structured, memory.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
