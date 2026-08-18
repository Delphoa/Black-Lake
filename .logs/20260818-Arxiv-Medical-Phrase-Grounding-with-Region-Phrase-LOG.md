# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P06`
- Public-safe date: 2026-08-18
- Paper: *Medical Phrase Grounding with Region-Phrase Context Contrastive Alignment*
- Identifier: `arXiv:2303.07618`; DOI: `10.48550/arXiv.2303.07618`
- URL: https://arxiv.org/abs/2303.07618

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 17,769 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Medical-Phrase-Grounding-with-Region-Phrase` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,184,715 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 6; sampled text inspection: true.
- Full-paper HTML: 130,441 bytes, 30,994 body characters, 22 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Medical-Phrase-Grounding-with-Region-Phrase-LOG.md`
- `.reports/BL-Arxiv-Medical-Phrase-Grounding-with-Region-Phrase-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Medical Phrase Grounding/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Medical Phrase Grounding/medical_phrase_grounding_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260802-MeDSLIP Medical/medslip_medical_manuscript.md` - MeDSLIP Medical - DEP-E; overlap: medical, alignment, context.
2. `.lake-data/DEP-E/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md` - Language-to-Space - DEP-E; overlap: grounding, context.
3. `.lake-data/DEP-E/DEP-E-20260810-Solver-Informed RL/solver_informed_rl_manuscript.md` - Solver-Informed RL - DEP-E; overlap: grounding, context.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
