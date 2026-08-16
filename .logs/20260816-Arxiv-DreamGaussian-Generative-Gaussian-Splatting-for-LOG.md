# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260816-7EAAB41B`
- Deployment item ID: `BLAD-2200-20260816-7EAAB41B-P05`
- Public-safe date: 2026-08-16
- Paper: *DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation*
- Identifier: `arXiv:2309.16653`; DOI: `10.48550/arXiv.2309.16653`
- URL: https://arxiv.org/abs/2309.16653

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 33,801 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `DreamGaussian-Generative-Gaussian-Splatting-for` slug; the 24-hour marker cutoff was 2026-08-15.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 8,013,225 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 18; sampled text inspection: true.
- Full-paper HTML: 182,023 bytes, 58,113 body characters, 53 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260816-Arxiv-DreamGaussian-Generative-Gaussian-Splatting-for-LOG.md`
- `.reports/BL-Arxiv-DreamGaussian-Generative-Gaussian-Splatting-for-20260816/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260816-DreamGaussian Generative/README.md`
- `.lake-data/DEP-E/DEP-E-20260816-DreamGaussian Generative/dreamgaussian_generative_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md` - Residual Gaussian CBCT - DEP-E; overlap: splatting, gaussian, content.
2. `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` - OMGEval Benchmark - DEP-E; overlap: generative, creation, content.
3. `.lake-data/DEP-E/DEP-E-20260811-Periodic Vibration/periodic_vibration_manuscript.md` - Periodic Vibration - DEP-E; overlap: gaussian.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
