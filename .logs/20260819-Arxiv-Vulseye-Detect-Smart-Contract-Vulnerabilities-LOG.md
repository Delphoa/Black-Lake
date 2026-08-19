# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P60`
- Public-safe date: 2026-08-19
- Paper: *Vulseye: Detect Smart Contract Vulnerabilities via Stateful Directed Graybox Fuzzing*
- Identifier: `arXiv:2408.10116`; DOI: `10.48550/arXiv.2408.10116`
- URL: https://arxiv.org/abs/2408.10116

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 75,677 on draw 63.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: stateful.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Vulseye-Detect-Smart-Contract-Vulnerabilities` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 6; focus exclusions: 55; source-gate exclusions: 1; reselections: 62.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 4,825,346 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 378,944 bytes, 80,966 body characters, 68 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Vulseye-Detect-Smart-Contract-Vulnerabilities-LOG.md`
- `.reports/BL-Arxiv-Vulseye-Detect-Smart-Contract-Vulnerabilities-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Vulseye Detect Smart/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Vulseye Detect Smart/vulseye_detect_smart_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260817-ORFuzz Fuzzing the Other/orfuzz_fuzzing_the_other_manuscript.md` - ORFuzz Fuzzing the Other - DEP-E; overlap: fuzzing.
2. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md` - Smart Coverage Goals - DEP-E; overlap: smart, contract.
3. `.lake-data/DEP-E/DEP-E-20260819-Construction and/construction_and_manuscript.md` - Construction and - DEP-E; overlap: smart, stateful.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
