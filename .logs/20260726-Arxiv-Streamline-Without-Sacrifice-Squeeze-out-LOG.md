# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260726-1DBD5211`
- Deployment item ID: `BLAD-2200-20260726-1DBD5211-P05`
- Public-safe date: 2026-07-26
- Paper: *Streamline Without Sacrifice -- Squeeze out Computation Redundancy in LMM*
- Identifier: `arXiv:2505.15816`; DOI: `10.48550/arXiv.2505.15816`
- URL: https://arxiv.org/abs/2505.15816

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 44,521 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Streamline-Without-Sacrifice-Squeeze-out` slug; the 24-hour marker cutoff was 2026-07-25.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,493,843 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 15; sampled text inspection: true.
- Full-paper HTML: 241,381 bytes, 60,233 body characters, 42 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260726-Arxiv-Streamline-Without-Sacrifice-Squeeze-out-LOG.md`
- `.reports/BL-Arxiv-Streamline-Without-Sacrifice-Squeeze-out-20260726/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260726-Streamline Without/README.md`
- `.lake-data/DEP-E/DEP-E-20260726-Streamline Without/streamline_without_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - DMNN Conditional Paths - DEP-E; overlap: computation, vision.
2. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: vision, multimodal.
3. `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` - Device Tuning MTL - DEP-E; overlap: encoder, vision.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
