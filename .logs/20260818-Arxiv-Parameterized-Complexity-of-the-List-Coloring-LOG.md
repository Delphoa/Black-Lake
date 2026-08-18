# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-BBEE0F31`
- Deployment item ID: `BLAD-2200-20260818-BBEE0F31-P11`
- Public-safe date: 2026-08-18
- Paper: *Parameterized Complexity of the List Coloring Reconfiguration Problem with Graph Parameters*
- Identifier: `arXiv:1705.07551`; DOI: `10.48550/arXiv.1705.07551`
- URL: https://arxiv.org/abs/1705.07551

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 34,153 on draw 8.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: complexity, graph.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Parameterized-Complexity-of-the-List-Coloring` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 7; source-gate exclusions: 0; reselections: 7.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 376,000 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 22; sampled text inspection: true.
- Full-paper HTML: 508,083 bytes, 75,627 body characters, 73 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Parameterized-Complexity-of-the-List-Coloring-LOG.md`
- `.reports/BL-Arxiv-Parameterized-Complexity-of-the-List-Coloring-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Parameterized Complexity/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Parameterized Complexity/parameterized_complexity_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260805-Graph Filter Banks/graph_filter_banks_manuscript.md` - Graph Filter Banks - DEP-E; overlap: graph, coloring, list, parameters, problem.
2. `.lake-data/DEP-E/DEP-E-20260818-Relieving the/relieving_the_manuscript.md` - Relieving the - DEP-E; overlap: graph, list, problem.
3. `.lake-data/DEP-E/DEP-E-20260805-Rauzy Neighbors/rauzy_neighbors_manuscript.md` - Rauzy Neighbors - DEP-E; overlap: graph, complexity, problem.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
