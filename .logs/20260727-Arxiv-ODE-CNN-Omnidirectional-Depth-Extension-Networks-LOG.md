# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260727-ADBD50D5`
- Deployment item ID: `BLAD-2200-20260727-ADBD50D5-P06`
- Public-safe date: 2026-07-27
- Paper: *ODE-CNN: Omnidirectional Depth Extension Networks*
- Identifier: `arXiv:2007.01475`; DOI: `10.48550/arXiv.2007.01475`
- URL: https://arxiv.org/abs/2007.01475

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 7,255 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `ODE-CNN-Omnidirectional-Depth-Extension-Networks` slug; the 24-hour marker cutoff was 2026-07-26.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,925,335 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 7; sampled text inspection: true.
- Full-paper HTML: 305,776 bytes, 44,845 body characters, 35 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260727-Arxiv-ODE-CNN-Omnidirectional-Depth-Extension-Networks-LOG.md`
- `.reports/BL-Arxiv-ODE-CNN-Omnidirectional-Depth-Extension-Networks-20260727/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260727-ODE-CNN Omnidirectional/README.md`
- `.lake-data/DEP-E/DEP-E-20260727-ODE-CNN Omnidirectional/ode_cnn_omnidirectional_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260722-GenTune Traceable Prompts/gentune_traceable_prompts_manuscript.md` - GenTune Traceable Prompts Review - DEP-E; overlap: environment, image, design.
2. `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md` - OE-BevSeg Perception - DEP-E; overlap: perception, camera.
3. `.lake-data/DEP-E/DEP-E-20260720-VG Navigable Space/vg_navigable_space_manuscript.md` - VG Navigable Space Review - DEP-E; overlap: navigable, autonomous, navigation.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
