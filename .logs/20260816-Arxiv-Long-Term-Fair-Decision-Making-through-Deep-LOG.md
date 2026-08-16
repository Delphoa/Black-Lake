# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260816-7EAAB41B`
- Deployment item ID: `BLAD-2200-20260816-7EAAB41B-P01`
- Public-safe date: 2026-08-16
- Paper: *Long-Term Fair Decision Making through Deep Generative Models*
- Identifier: `arXiv:2401.11288`; DOI: `10.48550/arXiv.2401.11288`
- URL: https://arxiv.org/abs/2401.11288

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 32,046 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Long-Term-Fair-Decision-Making-through-Deep` slug; the 24-hour marker cutoff was 2026-08-15.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,231,237 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 198,804 bytes, 49,467 body characters, 52 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260816-Arxiv-Long-Term-Fair-Decision-Making-through-Deep-LOG.md`
- `.reports/BL-Arxiv-Long-Term-Fair-Decision-Making-through-Deep-20260816/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260816-Long-Term Fair Decision/README.md`
- `.lake-data/DEP-E/DEP-E-20260816-Long-Term Fair Decision/long_term_fair_decision_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260805-MemShot Dialogue Memory/memshot_dialogue_memory_manuscript.md` - MemShot Dialogue Memory - DEP-E; overlap: long-term, making.
2. `.lake-data/DEP-E/DEP-E-20260722-LTRDetector Exploring/ltrdetector_exploring_manuscript.md` - LTRDetector Exploring Review - DEP-E; overlap: long-term, decision.
3. `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` - OMGEval Benchmark - DEP-E; overlap: generative, making, decision.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
