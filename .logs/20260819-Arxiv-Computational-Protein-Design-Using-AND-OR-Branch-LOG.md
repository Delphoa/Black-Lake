# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P90`
- Public-safe date: 2026-08-19
- Paper: *Computational Protein Design Using AND/OR Branch-and-Bound Search*
- Identifier: `arXiv:1412.3138`; DOI: `10.48550/arXiv.1412.3138`
- URL: https://arxiv.org/abs/1412.3138

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 4,638 on draw 2.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: search.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Computational-Protein-Design-Using-AND-OR-Branch` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 1; source-gate exclusions: 0; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 123,751 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 12; sampled text inspection: true.
- Full-paper HTML: 348,963 bytes, 40,551 body characters, 41 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Computational-Protein-Design-Using-AND-OR-Branch-LOG.md`
- `.reports/BL-Arxiv-Computational-Protein-Design-Using-AND-OR-Branch-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Computational Protein/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Computational Protein/computational_protein_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260801-PTransIPs Protein PLM/ptransips_protein_plm_manuscript.md` - PTransIPs Protein PLM - DEP-E; overlap: protein, computational, design.
2. `.lake-data/DEP-E/DEP-E-20260819-Calibrated Dataset/calibrated_dataset_manuscript.md` - Calibrated Dataset - DEP-E; overlap: search, computational, design.
3. `.lake-data/DEP-E/DEP-E-20260818-RL4RLA Teaching ML to/rl4rla_teaching_ml_to_manuscript.md` - RL4RLA Teaching ML to - DEP-E; overlap: search, design.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
