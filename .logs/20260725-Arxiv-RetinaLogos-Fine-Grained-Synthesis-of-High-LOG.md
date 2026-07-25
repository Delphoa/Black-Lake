# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260725-FF48EE13`
- Deployment item ID: `BLAD-2200-20260725-FF48EE13-P09`
- Public-safe date: 2026-07-25
- Paper: *RetinaLogos: Fine-Grained Synthesis of High-Resolution Retinal Images Through Captions*
- Identifier: `arXiv:2505.12887`; DOI: `10.48550/arXiv.2505.12887`
- URL: https://arxiv.org/abs/2505.12887

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 63,082 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `RetinaLogos-Fine-Grained-Synthesis-of-High` slug; the 24-hour marker cutoff was 2026-07-24.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 7,293,799 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 199,761 bytes, 36,926 body characters, 27 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260725-Arxiv-RetinaLogos-Fine-Grained-Synthesis-of-High-LOG.md`
- `.reports/BL-Arxiv-RetinaLogos-Fine-Grained-Synthesis-of-High-20260725/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260725-RetinaLogos Fine-Grained/README.md`
- `.lake-data/DEP-E/DEP-E-20260725-RetinaLogos Fine-Grained/retinalogos_fine_grained_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` - Adversarial Label Noise - DEP-E; overlap: distribution, adversarial, training.
2. `.lake-data/DEP-E/DEP-E-20260724-AG3D Learning to Generate/ag3d_learning_to_generate_manuscript.md` - AG3D Learning to Generate - DEP-E; overlap: avatars, generate, image.
3. `.lake-data/DEP-E/DEP-E-20260723-ScaleEnv Scaling Environm/scaleenv_scaling_environm_manuscript.md` - ScaleEnv Scaling Environment Syn - DEP-E; overlap: synthesis, training.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
