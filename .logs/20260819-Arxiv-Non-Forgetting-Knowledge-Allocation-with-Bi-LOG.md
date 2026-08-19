# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P174`
- Public-safe date: 2026-08-19
- Paper: *Non-Forgetting Knowledge Allocation with Bi-level Competition for Class-Incremental Learning*
- Identifier: `arXiv:2605.29592`; DOI: `10.48550/arXiv.2605.29592`
- URL: https://arxiv.org/abs/2605.29592

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 41,055 on draw 13.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: forgetting, learning.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Non-Forgetting-Knowledge-Allocation-with-Bi` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 12; source-gate exclusions: 0; reselections: 12.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,449,208 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 26; sampled text inspection: true.
- Full-paper HTML: 419,123 bytes, 73,135 body characters, 75 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Non-Forgetting-Knowledge-Allocation-with-Bi-LOG.md`
- `.reports/BL-Arxiv-Non-Forgetting-Knowledge-Allocation-with-Bi-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Non-Forgetting Knowledge/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Non-Forgetting Knowledge/non_forgetting_knowledge_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-Few-shot/few_shot_manuscript.md` - Few-shot - DEP-E; overlap: class-incremental, knowledge.
2. `.lake-data/DEP-E/DEP-E-20260719-Coordinated CIL/coordinated_cil_manuscript.md` - Input-Output Coordinated CIL; overlap: class-incremental.
3. `.lake-data/DEP-E/DEP-E-20260819-Make Domain Shift a/make_domain_shift_a_manuscript.md` - Make Domain Shift a - DEP-E; overlap: class-incremental.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
