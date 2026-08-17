# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260817-2C1A830E`
- Deployment item ID: `BLAD-2200-20260817-2C1A830E-P10`
- Public-safe date: 2026-08-17
- Paper: *RandoMix: A mixed sample data augmentation method with multiple mixed modes*
- Identifier: `arXiv:2205.08728`; DOI: `10.48550/arXiv.2205.08728`
- URL: https://arxiv.org/abs/2205.08728

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 73,701 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `RandoMix-A-mixed-sample-data-augmentation-method` slug; the 24-hour marker cutoff was 2026-08-16.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,988,999 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 197,780 bytes, 40,357 body characters, 49 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260817-Arxiv-RandoMix-A-mixed-sample-data-augmentation-method-LOG.md`
- `.reports/BL-Arxiv-RandoMix-A-mixed-sample-data-augmentation-method-20260817/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260817-RandoMix A mixed sample/README.md`
- `.lake-data/DEP-E/DEP-E-20260817-RandoMix A mixed sample/randomix_a_mixed_sample_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Coordinated CIL/coordinated_cil_manuscript.md` - Input-Output Coordinated CIL; overlap: sample, multiple.
2. `.lake-data/DEP-E/DEP-E-20260805-FiberStars Visual/fiberstars_visual_manuscript.md` - FiberStars Visual - DEP-E; overlap: multiple, modes.
3. `.lake-data/DEP-E/DEP-E-20260814-One Training for Multiple/one_training_for_multiple_manuscript.md` - One Training for Multiple - DEP-E; overlap: multiple, modes.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
