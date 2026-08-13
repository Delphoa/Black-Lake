# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260804-92EFB161`
- Deployment item ID: `BLAD-2200-20260804-92EFB161-P02`
- Public-safe date: 2026-08-04
- Paper: *Sparse Vector Recovery: Bernoulli-Gaussian Message Passing*
- Identifier: `arXiv:1707.09613`; DOI: `10.48550/arXiv.1707.09613`
- URL: https://arxiv.org/abs/1707.09613

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 57,276 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Sparse-Vector-Recovery-Bernoulli-Gaussian` slug; the 24-hour marker cutoff was 2026-08-03.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 802,395 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 6; sampled text inspection: true.
- Full-paper HTML: 1,389,990 bytes, 63,075 body characters, 57 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260804-Arxiv-Sparse-Vector-Recovery-Bernoulli-Gaussian-LOG.md`
- `.reports/BL-Arxiv-Sparse-Vector-Recovery-Bernoulli-Gaussian-20260804/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260804-Sparse Vector Recovery/README.md`
- `.lake-data/DEP-E/DEP-E-20260804-Sparse Vector Recovery/sparse_vector_recovery_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-Irregular Clipped SR/irregular_clipped_sr_manuscript.md` - Irregular Clipped SR - DEP-E; overlap: message, passing, vector, recovery, sparse.
2. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - iKalibr Calibration - DEP-E; overlap: passing, vector, recovery, sparse.
3. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - Acoustic Phase Retrieval - DEP-E; overlap: message, vector, recovery.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
