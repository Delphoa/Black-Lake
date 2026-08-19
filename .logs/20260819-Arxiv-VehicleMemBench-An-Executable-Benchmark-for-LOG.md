# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P34`
- Public-safe date: 2026-08-19
- Paper: *VehicleMemBench: An Executable Benchmark for Multi-User Long-Term Memory in In-Vehicle Agents*
- Identifier: `arXiv:2603.23840`; DOI: `10.48550/arXiv.2603.23840`
- URL: https://arxiv.org/abs/2603.23840

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 42,215 on draw 8.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: long term memory.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `VehicleMemBench-An-Executable-Benchmark-for` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 6; source-gate exclusions: 0; reselections: 7.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 860,754 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 22; sampled text inspection: true.
- Full-paper HTML: 366,938 bytes, 76,994 body characters, 143 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-VehicleMemBench-An-Executable-Benchmark-for-LOG.md`
- `.reports/BL-Arxiv-VehicleMemBench-An-Executable-Benchmark-for-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-VehicleMemBench An/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-VehicleMemBench An/vehiclemembench_an_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-Low-Complexity/low_complexity_manuscript.md` - Low-Complexity - DEP-E; overlap: multi-user, memory.
2. `.lake-data/DEP-E/DEP-E-20260819-Low-complexity Joint/low_complexity_joint_manuscript.md` - Low-complexity Joint - DEP-E; overlap: multi-user, memory.
3. `.lake-data/DEP-E/DEP-E-20260819-Explore with Long-term/explore_with_long_term_manuscript.md` - Explore with Long-term - DEP-E; overlap: long-term, benchmark, memory.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
