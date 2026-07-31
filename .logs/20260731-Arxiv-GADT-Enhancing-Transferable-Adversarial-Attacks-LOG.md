# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260731-3D09E72F`
- Deployment item ID: `BLAD-2200-20260731-3D09E72F-P04`
- Public-safe date: 2026-07-31
- Paper: *GADT: Enhancing Transferable Adversarial Attacks through Gradient-guided Adversarial Data Transformation*
- Identifier: `arXiv:2410.18648`; DOI: `10.48550/arXiv.2410.18648`
- URL: https://arxiv.org/abs/2410.18648

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 17,614 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `GADT-Enhancing-Transferable-Adversarial-Attacks` slug; the 24-hour marker cutoff was 2026-07-30.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 910,875 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 376,832 bytes, 54,570 body characters, 33 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260731-Arxiv-GADT-Enhancing-Transferable-Adversarial-Attacks-LOG.md`
- `.reports/BL-Arxiv-GADT-Enhancing-Transferable-Adversarial-Attacks-20260731/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260731-GADT Enhancing/README.md`
- `.lake-data/DEP-E/DEP-E-20260731-GADT Enhancing/gadt_enhancing_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260722-AVA Vignetting Attack/ava_vignetting_attack_manuscript.md` - AVA Robustness - DEP-E; overlap: attacks, defense, transformation, attack, security.
2. `.lake-data/DEP-E/DEP-E-20260713-SAILFISH Vetting/sailfish_vetting_manuscript.md` - SAILFISH Review - DEP-E; overlap: attacks, transformation, attack, security, adversarial.
3. `.lake-data/DEP-E/DEP-E-20260716-PIArena Evaluation/piarena_evaluation_manuscript.md` - PIArena Evaluation - DEP-E; overlap: attacks, defense, attack, security, adversarial.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
