# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260802-0D11B2FA`
- Deployment item ID: `BLAD-2200-20260802-0D11B2FA-P03`
- Public-safe date: 2026-08-02
- Paper: *Efficient LLM-based Advertising via Model Compression and Parallel Verification*
- Identifier: `arXiv:2605.11582`; DOI: `10.48550/arXiv.2605.11582`
- URL: https://arxiv.org/abs/2605.11582

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 50,069 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Efficient-LLM-based-Advertising-via-Model` slug; the 24-hour marker cutoff was 2026-08-01.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 810,288 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 5; sampled text inspection: true.
- Full-paper HTML: 120,825 bytes, 33,558 body characters, 39 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260802-Arxiv-Efficient-LLM-based-Advertising-via-Model-LOG.md`
- `.reports/BL-Arxiv-Efficient-LLM-based-Advertising-via-Model-20260802/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260802-Efficient LLM-based/README.md`
- `.lake-data/DEP-E/DEP-E-20260802-Efficient LLM-based/efficient_llm_based_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: quantization, pruning, parallel, sparsity, compression.
2. `.lake-data/DEP-E/DEP-E-20260718-SpOctA Accelerator/spocta_accelerator_manuscript.md` - SpOctA Accelerator - DEP-E; overlap: quantization, parallel, sparsity, compression, verification.
3. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: quantization, pruning, sparsity, compression, verification.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
