# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P32`
- Public-safe date: 2026-08-18
- Paper: *Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data*
- Identifier: `arXiv:2402.17644`; DOI: `10.48550/arXiv.2402.17644`
- URL: https://arxiv.org/abs/2402.17644

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 73,953 on draw 3.

## Research Focus Eligibility

- One-time focus: No one-time topic focus was requested..
- Matched categories: unrestricted.
- Matched title/abstract terms or phrases: not applicable.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Are-LLMs-Capable-of-Data-based-Statistical` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 0; source-gate exclusions: 2; reselections: 2.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 834,303 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 21; sampled text inspection: true.
- Full-paper HTML: 262,358 bytes, 75,052 body characters, 74 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Are-LLMs-Capable-of-Data-based-Statistical-LOG.md`
- `.reports/BL-Arxiv-Are-LLMs-Capable-of-Data-based-Statistical-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Are LLMs Capable of/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Are LLMs Capable of/are_llms_capable_of_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260815-PICBench Benchmarking/picbench_benchmarking_manuscript.md` - PICBench Benchmarking - DEP-E; overlap: benchmarking, llms, causal.
2. `.lake-data/DEP-E/DEP-E-20260716-FGBench Chemistry/fgbench_chemistry_manuscript.md` - FGBench Chemistry - DEP-E; overlap: benchmarking, reasoning, llms, causal.
3. `.lake-data/DEP-E/DEP-E-20260726-ManipulationNet An/manipulationnet_an_manuscript.md` - ManipulationNet An - DEP-E; overlap: benchmarking, reasoning, causal.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
