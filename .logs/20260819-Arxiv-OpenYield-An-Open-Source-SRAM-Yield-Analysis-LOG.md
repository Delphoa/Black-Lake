# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P234`
- Public-safe date: 2026-08-19
- Paper: *OpenYield: An Open-Source SRAM Yield Analysis and Optimization Benchmark Suite*
- Identifier: `arXiv:2508.04106`; DOI: `10.48550/arXiv.2508.04106`
- URL: https://arxiv.org/abs/2508.04106

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 73,186 on draw 26.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: optimization.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `OpenYield-An-Open-Source-SRAM-Yield-Analysis` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 25; source-gate exclusions: 0; reselections: 25.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,471,230 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 226,841 bytes, 53,814 body characters, 61 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-OpenYield-An-Open-Source-SRAM-Yield-Analysis-LOG.md`
- `.reports/BL-Arxiv-OpenYield-An-Open-Source-SRAM-Yield-Analysis-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-OpenYield An Open-Source/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-OpenYield An Open-Source/openyield_an_open_source_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260813-How Far Are We to GPT-4V/how_far_are_we_to_gpt_4v_manuscript.md` - How Far Are We to GPT-4V - DEP-E; overlap: open-source.
2. `.lake-data/DEP-E/DEP-E-20260719-CLOVER Test Benchmark/clover_test_benchmark_manuscript.md` - CLOVER Test Benchmark - DEP-E; overlap: benchmark, open-source, suite, optimization.
3. `.lake-data/DEP-E/DEP-E-20260730-MCPWorld Benchmark/mcpworld_manuscript.md` - MCPWorld - DEP-E; overlap: benchmark, open-source, suite.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
