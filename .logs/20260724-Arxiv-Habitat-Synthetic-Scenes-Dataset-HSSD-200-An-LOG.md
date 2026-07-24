# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260724-CF53BCCB`
- Deployment item ID: `BLAD-2200-20260724-CF53BCCB-P03`
- Public-safe date: 2026-07-24
- Paper: *Habitat Synthetic Scenes Dataset (HSSD-200): An Analysis of 3D Scene Scale and Realism Tradeoffs for ObjectGoal Navigation*
- Identifier: `arXiv:2306.11290`; DOI: `10.48550/arXiv.2306.11290`
- URL: https://arxiv.org/abs/2306.11290

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 16,587 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Habitat-Synthetic-Scenes-Dataset-HSSD-200-An` slug; the 24-hour marker cutoff was 2026-07-23.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 29,050,514 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 20; sampled text inspection: true.
- Full-paper HTML: 331,231 bytes, 69,185 body characters, 51 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260724-Arxiv-Habitat-Synthetic-Scenes-Dataset-HSSD-200-An-LOG.md`
- `.reports/BL-Arxiv-Habitat-Synthetic-Scenes-Dataset-HSSD-200-An-20260724/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260724-Habitat Synthetic Scenes/README.md`
- `.lake-data/DEP-E/DEP-E-20260724-Habitat Synthetic Scenes/habitat_synthetic_scenes_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260710-BEAGLE Learner/beagle_learner_manuscript.md` - BEAGLE Learner - DEP-E; overlap: making, realism, fidelity, quickly, realistic.
2. `.lake-data/DEP-E/DEP-E-20260720-VG Navigable Space/vg_navigable_space_manuscript.md` - VG Navigable Space Review - DEP-E; overlap: navigation, environments, real-world, real, visual.
3. `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md` - SAGE-Nav Review - DEP-E; overlap: navigation, quickly, scene, zero-shot, real.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
