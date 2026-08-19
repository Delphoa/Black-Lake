# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-7C79A486`
- Deployment item ID: `BLAD-2200-20260819-7C79A486-P09`
- Public-safe date: 2026-08-19
- Paper: *"The Boating Store Had Its Best Sail Ever": Pronunciation-attentive Contextualized Pun Recognition*
- Identifier: `arXiv:2004.14457`; DOI: `10.48550/arXiv.2004.14457`
- URL: https://arxiv.org/abs/2004.14457

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 6,672 on draw 1.

## Research Focus Eligibility

- One-time focus: No one-time topic focus was requested..
- Matched categories: unrestricted.
- Matched title/abstract terms or phrases: not applicable.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `The-Boating-Store-Had-Its-Best-Sail` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 875,911 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 177,516 bytes, 45,337 body characters, 39 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-The-Boating-Store-Had-Its-Best-Sail-LOG.md`
- `.reports/BL-Arxiv-The-Boating-Store-Had-Its-Best-Sail-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-The Boating Store Had Its/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-The Boating Store Had Its/the_boating_store_had_its_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-RAR Visual Reranking/rar_visual_reranking_manuscript.md` - RAR Visual Reranking - DEP-E; overlap: recognition, had, best, store, its.
2. `.lake-data/DEP-E/DEP-E-20260801-CrossNER Adapt/crossner_domain_adaptation_manuscript.md` - CrossNER - DEP-E; overlap: recognition, had, best, its.
3. `.lake-data/DEP-E/DEP-E-20260801-Relational Contrastive/relational_contrastive_manuscript.md` - Relational Contrastive - DEP-E; overlap: recognition, best, store, its.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
