# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260802-0D11B2FA`
- Deployment item ID: `BLAD-2200-20260802-0D11B2FA-P02`
- Public-safe date: 2026-08-02
- Paper: *CryoGEM: Physics-Informed Generative Cryo-Electron Microscopy*
- Identifier: `arXiv:2312.02235`; DOI: `10.48550/arXiv.2312.02235`
- URL: https://arxiv.org/abs/2312.02235

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 63,958 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `CryoGEM-Physics-Informed-Generative-Cryo` slug; the 24-hour marker cutoff was 2026-08-01.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 15,822,097 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 21; sampled text inspection: true.
- Full-paper HTML: 561,653 bytes, 93,453 body characters, 94 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260802-Arxiv-CryoGEM-Physics-Informed-Generative-Cryo-LOG.md`
- `.reports/BL-Arxiv-CryoGEM-Physics-Informed-Generative-Cryo-20260802/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260802-CryoGEM Physics-Informed/README.md`
- `.lake-data/DEP-E/DEP-E-20260802-CryoGEM Physics-Informed/cryogem_physics_informed_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` - Physical Data - DEP-E; overlap: physics-informed.
2. `.lake-data/DEP-E/DEP-E-20260725-Improved Counting and/improved_counting_and_manuscript.md` - Improved Counting and - DEP-E; overlap: microscopy.
3. `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md` - CausalTAD Trajectory - DEP-E; overlap: generative.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
