# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P90`
- Public-safe date: 2026-08-19
- Paper: *Scaling Multilingual Semantic Search in Uber Eats Delivery*
- Identifier: `arXiv:2603.06586`; DOI: `10.48550/arXiv.2603.06586`
- URL: https://arxiv.org/abs/2603.06586

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 61,591 on draw 19.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: search.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Scaling-Multilingual-Semantic-Search-in-Uber` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 17; source-gate exclusions: 0; reselections: 18.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 601,032 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 21; sampled text inspection: true.
- Full-paper HTML: 318,214 bytes, 68,299 body characters, 86 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Scaling-Multilingual-Semantic-Search-in-Uber-LOG.md`
- `.reports/BL-Arxiv-Scaling-Multilingual-Semantic-Search-in-Uber-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Scaling Multilingual/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Scaling Multilingual/scaling_multilingual_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Scaling Up Efficient/scaling_up_efficient_manuscript.md` - Scaling Up Efficient - DEP-E; overlap: scaling, semantic, search.
2. `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` - OMGEval Benchmark - DEP-E; overlap: multilingual, semantic, search.
3. `.lake-data/DEP-E/DEP-E-20260818-Language-Coupled/language_coupled_manuscript.md` - Language-Coupled - DEP-E; overlap: multilingual.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
