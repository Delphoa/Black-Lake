# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P245`
- Public-safe date: 2026-08-19
- Paper: *Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks*
- Identifier: `arXiv:2401.14159`; DOI: `10.48550/arXiv.2401.14159`
- URL: https://arxiv.org/abs/2401.14159

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 71,974 on draw 30.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: world model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Grounded-SAM-Assembling-Open-World-Models-for` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 3; focus exclusions: 26; source-gate exclusions: 0; reselections: 29.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,931,092 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 591,911 bytes, 149,471 body characters, 258 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Grounded-SAM-Assembling-Open-World-Models-for-LOG.md`
- `.reports/BL-Arxiv-Grounded-SAM-Assembling-Open-World-Models-for-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Grounded SAM Assembling/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Grounded SAM Assembling/grounded_sam_assembling_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-M 4 -SAM Multi-Modal/m_4_sam_multi_modal_manuscript.md` - M 4 -SAM Multi-Modal - DEP-E; overlap: sam.
2. `.lake-data/DEP-E/DEP-E-20260815-RoboHanger Learning/robohanger_learning_manuscript.md` - RoboHanger Learning - DEP-E; overlap: diverse.
3. `.lake-data/DEP-E/DEP-E-20260818-Coalesced TLB to Exploit/coalesced_tlb_to_exploit_manuscript.md` - Coalesced TLB to Exploit - DEP-E; overlap: diverse.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
