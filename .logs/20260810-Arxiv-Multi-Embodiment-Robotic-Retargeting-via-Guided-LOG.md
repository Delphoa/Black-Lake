# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260810-B3B6846E`
- Deployment item ID: `BLAD-2200-20260810-B3B6846E-P10`
- Public-safe date: 2026-08-10
- Paper: *Multi-Embodiment Robotic Retargeting via Guided Diffusion Model*
- Identifier: `arXiv:2505.20857`; DOI: `10.48550/arXiv.2505.20857`
- URL: https://arxiv.org/abs/2505.20857

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 38,289 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Multi-Embodiment-Robotic-Retargeting-via-Guided` slug; the 24-hour marker cutoff was 2026-08-09.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 4,194,531 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 8; sampled text inspection: true.
- Full-paper HTML: 258,143 bytes, 49,474 body characters, 57 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260810-Arxiv-Multi-Embodiment-Robotic-Retargeting-via-Guided-LOG.md`
- `.reports/BL-Arxiv-Multi-Embodiment-Robotic-Retargeting-via-Guided-20260810/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260810-Multi-Embodiment Robotic/README.md`
- `.lake-data/DEP-E/DEP-E-20260810-Multi-Embodiment Robotic/multi_embodiment_robotic_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260730-TopoDiffuser A/topodiffuser_a_manuscript.md` - TopoDiffuser A - DEP-E; overlap: conditional diffusion, trajectory generation, multimodal guidance.
2. `.lake-data/DEP-E/DEP-E-20260726-ManipulationNet An/manipulationnet_an_manuscript.md` - ManipulationNet An - DEP-E; overlap: robot embodiments, manipulation skills, real-world benchmarking.
3. `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md` - FAVLA Fast-Slow - DEP-E; overlap: robotic manipulation, contact-rich control, adaptive action policy.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
