# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260802-0D11B2FA`
- Deployment item ID: `BLAD-2200-20260802-0D11B2FA-P07`
- Public-safe date: 2026-08-02
- Paper: *TL;DR: Too Long, Do Re-weighting for Efficient LLM Reasoning Compression*
- Identifier: `arXiv:2506.02678`; DOI: `10.48550/arXiv.2506.02678`
- URL: https://arxiv.org/abs/2506.02678

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 62,424 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `TL-DR-Too-Long-Do-Re-weighting` slug; the 24-hour marker cutoff was 2026-08-01.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,536,368 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 23; sampled text inspection: true.
- Full-paper HTML: 441,591 bytes, 80,360 body characters, 72 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260802-Arxiv-TL-DR-Too-Long-Do-Re-weighting-LOG.md`
- `.reports/BL-Arxiv-TL-DR-Too-Long-Do-Re-weighting-20260802/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260802-TL DR Too Long Do/README.md`
- `.lake-data/DEP-E/DEP-E-20260802-TL DR Too Long Do/tl_dr_too_long_do_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: quantization, pruning, sparsity, long, compression.
2. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: quantization, pruning, sparsity, compression, llm.
3. `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md` - ConMax - DEP-E; overlap: pruning, long, compression, llm, reasoning.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
