# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260728-EB036F17`
- Deployment item ID: `BLAD-2200-20260728-EB036F17-P05`
- Public-safe date: 2026-07-28
- Paper: *CanCal: Towards Real-time and Lightweight Ransomware Detection and Response in Industrial Environments*
- Identifier: `arXiv:2408.16515`; DOI: `10.48550/arXiv.2408.16515`
- URL: https://arxiv.org/abs/2408.16515

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75825 PDFs and 75822 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 51678.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant deposited identifiers, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `CanCal-Towards-Real-time-and-Lightweight-Ransomware-Detection-and` slug; the 24-hour marker cutoff was 2026-07-27.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2071169 bytes with valid `%PDF-` header and trailing `%%EOF`; page markers: 24.
- Full-paper HTML: 734563 bytes, 81691 body characters, 34 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260728-Arxiv-CanCal-Towards-Real-time-and-Lightweight-Ransomware-Detection-and-LOG.md`
- `.reports/BL-Arxiv-CanCal-Towards-Real-time-and-Lightweight-Ransomware-Detection-and-20260728/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260728-CanCal Towards Real-time/README.md`
- `.lake-data/DEP-E/DEP-E-20260728-CanCal Towards Real-time/cancal_towards_real_time_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Memory Defense Layers/memory-defense-layers.md` - Memory Defense Layers - DEP-E; overlap: attacks, defense, detection.
2. `.lake-data/DEP-E/DEP-E-20260720-Context Backdoor/context_backdoor_defense_manuscript.md` - Context Backdoor Defense - DEP-E; overlap: defense, detection, experimental.
3. `.lake-data/DEP-E/DEP-E-20260726-Constraint-Aware Systems/constraint-aware-systems.md` - Constraint-Aware Systems - DEP-E; overlap: challenges, defense, enabling.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
